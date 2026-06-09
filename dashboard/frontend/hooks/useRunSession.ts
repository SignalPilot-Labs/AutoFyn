"use client";

import { useCallback, useRef } from "react";
import type { RefObject } from "react";
import type { FeedEvent, ConnectionState } from "@/lib/types";
import { loadRunHistory } from "@/lib/loadRunHistory";
import { useSSE } from "@/hooks/useSSE";
import { useEventState } from "@/hooks/useEventState";

/**
 * Owns the live-run session: the SSE stream, the merged event state, and the
 * select / resume / teardown handlers that coordinate them.
 *
 * This exists to break the circular dependency that previously forced a
 * mutable-ref bridge in useDashboard: handleSessionResumed must be passed to
 * useSSE, but it also needs useSSE's connect/disconnect and useEventState's
 * setters — which are declared after useSSE. The old code forward-declared
 * no-op refs and back-patched them mid-render.
 *
 * Here the order is honest: useEventState → useSSE → handlers. useSSE reads its
 * callbacks from a ref at fire time (always post-render), so we pass a single
 * stable callbacksRef whose .current is assigned after the handlers are
 * defined. No no-op placeholders, no scattered back-patching.
 */

export interface RunSessionConfig {
  /** Ref to the currently-selected run id (kept in sync by useDashboard). */
  selectedRunIdRef: RefObject<string | null>;
  setSelectedRunId: (id: string | null) => void;
  /** Refresh the runs list (e.g. after select / run-ended). */
  refreshRunsRef: RefObject<() => void>;
  /** Clear the busy lock when a run ends. */
  setBusy: (v: boolean) => void;
}

export interface RunSession {
  liveEvents: FeedEvent[];
  allEvents: FeedEvent[];
  connected: boolean;
  connectionState: ConnectionState;
  historyLoading: boolean;
  historyTruncated: boolean;
  addEvent: (event: FeedEvent) => void;
  /** Select a run: tear down the current stream, load history, reconnect. */
  handleSelectRun: (id: string) => Promise<FeedEvent[]>;
  /** Reset the session for a context change (e.g. repo switch). */
  resetSession: () => void;
  /** Bump the select/resume generations to invalidate in-flight loads. */
  invalidatePendingLoads: () => void;
  sseRef: RefObject<{
    disconnect: () => void;
    clearEvents: () => void;
    connect: (id: string, cursors: { afterTool: number; afterAudit: number }) => void;
  }>;
  cursorsRef: RefObject<{ afterTool: number; afterAudit: number }>;
}

export function useRunSession(config: RunSessionConfig): RunSession {
  const { selectedRunIdRef, setSelectedRunId, refreshRunsRef, setBusy } = config;

  const selectGenRef = useRef(0);
  const resumeGenRef = useRef(0);
  const cursorsRef = useRef({ afterTool: 0, afterAudit: 0 });

  // Single stable indirection: useSSE reads these at fire time (post-render),
  // so we can define the real handlers below and assign them here once.
  const callbacksRef = useRef<{ onRunEnded: () => void; onSessionResumed: () => void }>({
    onRunEnded: () => undefined,
    onSessionResumed: () => undefined,
  });

  const { events: liveEvents, connected, connectionState, clearEvents, connect, disconnect } = useSSE(
    () => callbacksRef.current.onRunEnded(),
    () => callbacksRef.current.onSessionResumed(),
  );

  // Stable handle to the SSE controls so async callbacks (and useRunActions)
  // always reach the live functions.
  const sseRef = useRef({ connect, disconnect, clearEvents });
  sseRef.current = { connect, disconnect, clearEvents };

  const evState = useEventState(liveEvents);
  const { allEvents, historyLoading, historyTruncated, addEvent } = evState;
  const { setHistoryEvents, setHistoryLoading, setHistoryTruncated } = evState;

  const handleRunEnded = useCallback(() => {
    refreshRunsRef.current();
    setBusy(false);
  }, [refreshRunsRef, setBusy]);

  const handleSessionResumed = useCallback(() => {
    const runId = selectedRunIdRef.current;
    if (!runId) return;
    const gen = ++resumeGenRef.current;
    sseRef.current.disconnect();
    setHistoryLoading(true);
    loadRunHistory(runId).then(({ events, lastToolId, lastAuditId, truncated }) => {
      if (gen !== resumeGenRef.current) return;
      setHistoryEvents(events);
      setHistoryTruncated(truncated);
      cursorsRef.current = { afterTool: lastToolId, afterAudit: lastAuditId };
      sseRef.current.clearEvents();
      sseRef.current.connect(runId, { afterTool: lastToolId, afterAudit: lastAuditId });
      setHistoryLoading(false);
    }).catch((err) => {
      if (gen !== resumeGenRef.current) return;
      setHistoryLoading(false);
      addEvent({ _kind: "control", text: `Session resume failed: ${err}`, ts: new Date().toISOString() });
    });
  }, [selectedRunIdRef, setHistoryLoading, setHistoryEvents, setHistoryTruncated, addEvent]);

  // Wire the real handlers into the ref useSSE reads.
  callbacksRef.current = { onRunEnded: handleRunEnded, onSessionResumed: handleSessionResumed };

  const handleSelectRun = useCallback(
    async (id: string): Promise<FeedEvent[]> => {
      const gen = ++selectGenRef.current;
      // Also invalidate any in-flight session resume: selecting a run means we
      // no longer want a pending resume's loadRunHistory to connect() to the
      // run it was resuming (it would clobber this selection's connection).
      resumeGenRef.current++;
      sseRef.current.disconnect();
      setSelectedRunId(id);
      setHistoryLoading(true);
      sseRef.current.clearEvents();
      let lastToolId = 0;
      let lastAuditId = 0;
      let loadedEvents: FeedEvent[] = [];
      try {
        const result = await loadRunHistory(id);
        if (gen !== selectGenRef.current) return loadedEvents;
        setHistoryEvents(result.events);
        setHistoryTruncated(result.truncated);
        localStorage.setItem("autofyn_last_run_id", id);
        loadedEvents = result.events;
        lastToolId = result.lastToolId;
        lastAuditId = result.lastAuditId;
      } catch (err) {
        console.warn("Failed to load history:", err);
        if (gen === selectGenRef.current) setHistoryEvents([]);
      } finally {
        if (gen === selectGenRef.current) setHistoryLoading(false);
      }
      if (gen !== selectGenRef.current) return loadedEvents;
      cursorsRef.current = { afterTool: lastToolId, afterAudit: lastAuditId };
      sseRef.current.connect(id, { afterTool: lastToolId, afterAudit: lastAuditId });
      refreshRunsRef.current();
      return loadedEvents;
    },
    [setSelectedRunId, setHistoryLoading, setHistoryEvents, setHistoryTruncated, refreshRunsRef],
  );

  const invalidatePendingLoads = useCallback(() => {
    selectGenRef.current += 1;
    resumeGenRef.current += 1; // cancel any in-flight session resume too
  }, []);

  const resetSession = useCallback(() => {
    sseRef.current.disconnect();
    invalidatePendingLoads();
    setHistoryEvents([]);
    sseRef.current.clearEvents();
  }, [invalidatePendingLoads, setHistoryEvents]);

  return {
    liveEvents,
    allEvents,
    connected,
    connectionState,
    historyLoading,
    historyTruncated,
    addEvent,
    handleSelectRun,
    resetSession,
    invalidatePendingLoads,
    sseRef,
    cursorsRef,
  };
}
