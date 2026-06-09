/**
 * Behavioral regression test: the health poll must detect when the selected run
 * disappears from the active runs list (run ended) and trigger a runs refresh.
 *
 * Bug guarded: a run that ends during an SSE gap (missed run_ended event) would
 * leave runActive stuck true. The health poll now notices the selected run
 * vanishing from h.runs (selectedGone) and calls refreshRunsRef.current() to
 * reconcile, while still NOT touching the selection itself.
 *
 * This replaces the prior source-grep test (which asserted the block contains
 * "selectedGone" and "refreshRunsRef.current()"). Here we select run-A while it
 * is active, then deliver a poll where run-A is gone, and assert the runs
 * refresh fires.
 *
 * Note on the selectedGone semantics: it only triggers when the run was present
 * in the PREVIOUS health snapshot and absent from the new one. So the test
 * first lets a poll observe run-A active (prev), then drops it.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import {
  resetDashboardMocks,
  apiMocks,
  runsControl,
  makeRun,
} from "./helpers/dashboardHarness";
import { AGENT_HEALTH_POLL_MS } from "@/lib/constants";

import { useDashboard } from "@/hooks/useDashboard";

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("health poll: run ended detection", () => {
  it("refreshes runs when the selected run disappears from the poll", async () => {
    runsControl.current.runs = [makeRun({ id: "run-A", run_id: "run-A" })];
    // First poll observes run-A active — this becomes `prev` for the next poll.
    apiMocks.fetchAgentHealth.mockResolvedValue({
      status: "running",
      active_runs: 1,
      max_concurrent: 4,
      runs: [{ run_id: "run-A", status: "running", started_at: 0 }],
    });

    vi.useFakeTimers({ shouldAdvanceTime: true });
    try {
      const { result } = renderHook(() => useDashboard());

      // Wait for the mount poll to record run-A in agentHealth (prev snapshot).
      await waitFor(() =>
        expect(result.current.agentHealth?.runs).toHaveLength(1),
      );

      // Select run-A while it's active.
      await act(async () => { await result.current.handleSelectRun("run-A"); });
      expect(result.current.selectedRunId).toBe("run-A");

      // handleSelectRun itself calls refreshRunsRef.current() — clear so the
      // next assertion isolates the run-ended-triggered refresh.
      runsControl.refresh.mockClear();

      // Next poll: run-A has vanished (ended during an SSE gap).
      apiMocks.fetchAgentHealth.mockResolvedValue({
        status: "idle",
        active_runs: 0,
        max_concurrent: 4,
        runs: [],
      });

      await act(async () => {
        vi.advanceTimersByTime(AGENT_HEALTH_POLL_MS + 10);
        await Promise.resolve();
        await Promise.resolve();
      });

      // The disappearance triggers a runs refresh...
      await waitFor(() => expect(runsControl.refresh).toHaveBeenCalled());
      // ...but the selection is left untouched (no-reselect invariant).
      expect(result.current.selectedRunId).toBe("run-A");
    } finally {
      vi.useRealTimers();
    }
  });
});
