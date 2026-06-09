/**
 * Behavioral regression test: handleSessionResumed must guard against stale
 * async callbacks (the resumeGenRef generation-counter pattern).
 *
 * Bug: if a session-resumed event fires and loadRunHistory is in flight, then
 * the user selects a DIFFERENT run, the stale resume .then() must NOT call
 * sseRef.connect() with the old runId — that would tear down the new run's SSE
 * connection. The generation counter discards the stale callback.
 *
 * This replaces the prior source-grep test (asserted on resumeGenRef text);
 * it mounts the real hook and drives the race.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import {
  resetDashboardMocks,
  sseControl,
  apiMocks,
  runsControl,
  makeRun,
} from "./helpers/dashboardHarness";

import { useDashboard } from "@/hooks/useDashboard";

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("handleSessionResumed: stale callback discarded by generation counter", () => {
  it("a stale resume load does not connect after the user switches runs", async () => {
    runsControl.current.runs = [makeRun({ id: "run-A", run_id: "run-A" })];

    const { result } = renderHook(() => useDashboard());

    // Select run-A so selectedRunIdRef points at it.
    await act(async () => { await result.current.handleSelectRun("run-A"); });
    sseControl.connect.mockClear();

    // Make the NEXT loadRunHistory (the resume's) hang so we can interleave.
    let resolveResume!: (v: unknown) => void;
    apiMocks.loadRunHistory.mockImplementationOnce(
      () => new Promise((res) => { resolveResume = res; }),
    );

    // Fire session-resumed for run-A — its loadRunHistory is now pending.
    act(() => { sseControl.fireSessionResumed(); });

    // User switches to run-B before the resume load resolves. This bumps the
    // generation, so the pending resume callback is now stale.
    await act(async () => { await result.current.handleSelectRun("run-B"); });
    const connectsAfterSwitch = sseControl.connect.mock.calls.length;

    // Now the stale resume load resolves.
    await act(async () => {
      resolveResume({ events: [], lastToolId: 5, lastAuditId: 5, truncated: false });
      await Promise.resolve();
    });

    // The stale resume must NOT have issued another connect (especially not
    // for run-A). The only connects are from the two handleSelectRun calls.
    expect(sseControl.connect.mock.calls.length).toBe(connectsAfterSwitch);
    const connectedRunIds = sseControl.connect.mock.calls.map((c) => c[0]);
    // The last connect was for run-B (the live selection), never re-run-A.
    expect(connectedRunIds[connectedRunIds.length - 1]).toBe("run-B");
  });

  it("a session-resumed event for the current run reconnects with fresh cursors", async () => {
    runsControl.current.runs = [makeRun({ id: "run-A", run_id: "run-A" })];
    const { result } = renderHook(() => useDashboard());
    await act(async () => { await result.current.handleSelectRun("run-A"); });
    sseControl.connect.mockClear();
    sseControl.disconnect.mockClear();

    apiMocks.loadRunHistory.mockResolvedValueOnce({
      events: [], lastToolId: 42, lastAuditId: 7, truncated: false,
    });

    await act(async () => {
      sseControl.fireSessionResumed();
      await Promise.resolve();
    });

    await waitFor(() => expect(sseControl.connect).toHaveBeenCalled());
    // Reconnects for run-A with the cursors from the resume load.
    const lastConnect = sseControl.connect.mock.calls[sseControl.connect.mock.calls.length - 1];
    expect(lastConnect[0]).toBe("run-A");
    expect(lastConnect[1]).toEqual({ afterTool: 42, afterAudit: 7 });
    // Disconnect happened before the reconnect.
    expect(sseControl.disconnect).toHaveBeenCalled();
  });
});
