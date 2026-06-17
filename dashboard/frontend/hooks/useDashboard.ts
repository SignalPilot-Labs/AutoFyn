"use client";

import { useState, useCallback, useEffect, useRef } from "react";
import type { Run, RunStatus, SettingsStatus, RepoInfo } from "@/lib/types";
import {
  fetchAgentHealth,
  fetchRepos,
  setActiveRepo,
} from "@/lib/api";
import { useKeyboardShortcuts } from "@/hooks/useKeyboardShortcuts";
import type { AgentHealth } from "@/lib/api";
import type { DashboardState } from "@/hooks/dashboardTypes";
import { AGENT_HEALTH_POLL_MS, TERMINAL_STATUSES, isActiveStatus, DEFAULT_BASE_BRANCH } from "@/lib/constants";
import { fetchSettingsStatus } from "@/lib/settings-api";
import { isAtCapacity } from "@/lib/capacity";
import { useRuns } from "@/hooks/useRuns";
import { useMobile } from "@/hooks/useMobile";
import { useRunActions } from "@/hooks/useRunActions";
import { useDashboardUI } from "@/hooks/useDashboardUI";
import { useRunSession } from "@/hooks/useRunSession";

export function useDashboard(): DashboardState {
  const ui = useDashboardUI();
  const { setStartModalOpen, setOnboardingOpen, showShortcuts, setShowShortcuts, handleToggleSidebar } = ui;

  const [activeRepoFilter, setActiveRepoFilter] = useState<string | null>(() => {
    try { return localStorage.getItem("sp_improve_active_repo") || null; } catch { return null; }
  });
  const [repos, setRepos] = useState<RepoInfo[]>([]);
  const { runs, loading: runsLoading, refresh: refreshRuns } = useRuns(activeRepoFilter);
  const [selectedRunId, setSelectedRunId] = useState<string | null>(null);
  const [selectedRun, setSelectedRun] = useState<Run | null>(null);
  const [agentHealth, setAgentHealth] = useState<AgentHealth | null>(null);
  const [branches, setBranches] = useState<string[]>([DEFAULT_BASE_BRANCH]);
  const [defaultBranch, setDefaultBranch] = useState<string>(DEFAULT_BASE_BRANCH);
  const [settingsStatus, setSettingsStatus] = useState<SettingsStatus | null>(null);
  const initGenRef = useRef(0);
  const skipLastRunRestoreRef = useRef(false);
  const isMobile = useMobile();
  const [busy, setBusy] = useState(false);

  const selectedRunIdRef = useRef<string | null>(null);
  useEffect(() => { selectedRunIdRef.current = selectedRunId; }, [selectedRunId]);

  const refreshRunsRef = useRef(refreshRuns);
  refreshRunsRef.current = refreshRuns;

  const session = useRunSession({ selectedRunIdRef, setSelectedRunId, refreshRunsRef, setBusy });
  const {
    allEvents, connected, connectionState, historyLoading, historyTruncated,
    addEvent, handleSelectRun, resetSession, sseRef, cursorsRef,
  } = session;

  const runStatus: RunStatus | null = (selectedRun?.status as RunStatus) || null;

  const runActions = useRunActions({
    selectedRunId,
    selectedRunIdRef,
    addEvent,
    sseRef,
    cursorsRef,
    refreshRunsRef,
    handleSelectRun,
    activeRepoFilter,
    setStartModalOpen,
    setBusy,
  });

  const { controlAction } = runActions;

  useKeyboardShortcuts({
    handleToggleSidebar,
    setStartModalOpen,
    showShortcuts,
    setShowShortcuts,
    controlAction,
    runStatus,
    busy,
    activeRepoFilter,
  });

  // Health poll: only updates agentHealth state and triggers runs refresh
  // when a new run appears. Run selection is handled by the auto-selection
  // effect below — keeping selection logic in one place prevents races
  // (e.g. health poll re-selecting a run that handleStartRun just selected).
  useEffect(() => {
    const check = async () => {
      try {
        const h = await fetchAgentHealth();
        setAgentHealth((prev) => {
          const prevIds = new Set(prev?.runs.map((r) => r.run_id) ?? []);
          const hasNewRun = h.runs.some((r) => !prevIds.has(r.run_id));
          const selectedId = selectedRunIdRef.current;
          const selectedWasActive = selectedId !== null && prev?.runs.some((r) => r.run_id === selectedId);
          const selectedGone = selectedWasActive === true && !h.runs.some((r) => r.run_id === selectedId);
          if (hasNewRun || selectedGone) {
            refreshRunsRef.current();
          }
          return h;
        });
      } catch (err) {
        console.error("Health poll check() failed:", err);
        setAgentHealth(null);
      }
    };
    check();
    const id = setInterval(check, AGENT_HEALTH_POLL_MS);
    return () => clearInterval(id);
  }, []);

  useEffect(() => {
    const gen = ++initGenRef.current;
    fetchSettingsStatus().then((s) => {
      if (gen !== initGenRef.current) return;
      setSettingsStatus(s);
      if (!s.configured) setOnboardingOpen(true);
    });
    fetchRepos().then((r) => {
      if (gen !== initGenRef.current) return;
      setRepos(r);
      if (r.length > 0) {
        const stored = activeRepoFilter;
        if (!stored) return; // User never picked a repo — don't force one
        const valid = r.some((repo) => repo.repo === stored);
        if (!valid) {
          // Stored repo no longer exists — fall back to one with runs
          const withRuns = r.find((repo) => repo.run_count > 0);
          const picked = withRuns?.repo || r[0].repo;
          setActiveRepoFilter(picked);
          try { localStorage.setItem("sp_improve_active_repo", picked); } catch {}
        }
      }
    });
    return () => { initGenRef.current++; };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleRepoSwitch = useCallback(async (repo: string) => {
    skipLastRunRestoreRef.current = true;
    setActiveRepoFilter(repo || null);
    try {
      if (repo) localStorage.setItem("sp_improve_active_repo", repo);
      else localStorage.removeItem("sp_improve_active_repo");
    } catch {}
    // Tear down the session (disconnect, invalidate in-flight loads, clear
    // events) before clearing the selection for the new repo context.
    resetSession();
    setSelectedRunId(null);
    setSelectedRun(null);
    setBranches([DEFAULT_BASE_BRANCH]);
    setDefaultBranch(DEFAULT_BASE_BRANCH);
    if (repo) {
      try { await setActiveRepo(repo); } catch (e) { console.error("Failed to set active repo:", e); }
    }
    const repoGen = ++initGenRef.current;
    fetchRepos().then((r) => {
      if (repoGen !== initGenRef.current) return;
      setRepos(r);
    });
  }, [resetSession]);

  useEffect(() => {
    if (selectedRunId) {
      const found = runs.find((r) => r.id === selectedRunId);
      if (found) {
        setSelectedRun(found);
        if (TERMINAL_STATUSES.has(found.status as RunStatus)) setBusy(false);
      }
    }
  }, [runs, selectedRunId]);

  // Auto-selection: pick a run ONLY when none is selected. Never yank the
  // user away from a run they deliberately clicked — even if it's terminal
  // and an active run exists. The user can click the active run themselves.
  useEffect(() => {
    if (selectedRunId || runs.length === 0) return;
    if (activeRepoFilter && !runs.some((r) => r.github_repo === activeRepoFilter)) return;

    const active = runs.find((r) => isActiveStatus(r.status));
    if (active) {
      handleSelectRun(active.id);
      return;
    }
    const skipRestore = skipLastRunRestoreRef.current;
    skipLastRunRestoreRef.current = false;
    if (!skipRestore) {
      const lastRunId = localStorage.getItem("autofyn_last_run_id");
      if (lastRunId && runs.some((r) => r.id === lastRunId)) {
        handleSelectRun(lastRunId);
        return;
      }
    }
    handleSelectRun(runs[0].id);
  }, [runs, selectedRunId, handleSelectRun, activeRepoFilter]);

  const isConfigured = settingsStatus?.configured ?? false;
  const atCapacity = isAtCapacity(agentHealth);
  const activeRunHealth = selectedRunId
    ? agentHealth?.runs.find((r) => r.run_id === selectedRunId)
    : undefined;

  return {
    repos,
    runs,
    runsLoading,
    selectedRunId,
    selectedRun,
    allEvents,
    runStatus,
    agentHealth,
    activeRunHealth,
    connected,
    connectionState,
    historyTruncated,
    branches,
    defaultBranch,
    isMobile,
    isConfigured,
    atCapacity,
    busy,
    historyLoading,
    activeRepoFilter,
    settingsStatus,
    handleRepoSwitch,
    handleSelectRun,
    setBranches,
    setDefaultBranch,
    setSettingsStatus,
    setRepos,
    ...ui,
    ...runActions,
  };
}
