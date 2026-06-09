/**
 * Behavioral regression test: the health poll must NOT re-select runs.
 *
 * Run selection belongs to the auto-selection effect (which only fires when no
 * run is selected). Having selection logic in the health poll too caused races
 * where a poll re-selected a run that handleStartRun had just selected, clearing
 * the pending prompt message.
 *
 * This replaces the prior source-grep test (which asserted the health-poll
 * block does not contain the substring "handleSelectRun"). Here we assert the
 * absence of behavior: with run-A deliberately selected, a health poll that
 * reports a DIFFERENT active run (run-B) must leave the selection on run-A. The
 * poll may refresh the runs list, but it must never yank the selection.
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

describe("health poll: no selection side effects", () => {
  it("does not re-select when a poll reports a different active run", async () => {
    runsControl.current.runs = [makeRun({ id: "run-A", run_id: "run-A" })];
    // Initial poll: run-A is the only active run.
    apiMocks.fetchAgentHealth.mockResolvedValue({
      status: "running",
      active_runs: 1,
      max_concurrent: 4,
      runs: [{ run_id: "run-A", status: "running", started_at: 0 }],
    });

    vi.useFakeTimers({ shouldAdvanceTime: true });
    try {
      const { result } = renderHook(() => useDashboard());

      // Deliberately select run-A.
      await act(async () => { await result.current.handleSelectRun("run-A"); });
      expect(result.current.selectedRunId).toBe("run-A");

      // A later poll reports a DIFFERENT active run (run-B) appearing.
      apiMocks.fetchAgentHealth.mockResolvedValue({
        status: "running",
        active_runs: 2,
        max_concurrent: 4,
        runs: [
          { run_id: "run-A", status: "running", started_at: 0 },
          { run_id: "run-B", status: "running", started_at: 0 },
        ],
      });

      await act(async () => {
        vi.advanceTimersByTime(AGENT_HEALTH_POLL_MS + 10);
        await Promise.resolve();
        await Promise.resolve();
      });

      // agentHealth reflects the new run, but the selection is untouched.
      await waitFor(() =>
        expect(result.current.agentHealth?.runs).toHaveLength(2),
      );
      expect(result.current.selectedRunId).toBe("run-A");
    } finally {
      vi.useRealTimers();
    }
  });
});
