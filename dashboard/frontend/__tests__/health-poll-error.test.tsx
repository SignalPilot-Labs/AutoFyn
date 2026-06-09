/**
 * Behavioral regression test: the health poll's check() must catch errors from
 * fetchAgentHealth() and set agentHealth to null (disconnected state) rather
 * than leaving stale data or throwing an unhandled rejection.
 *
 * Bug guarded: before the fix, check() had no try/catch — any error escaping
 * fetchAgentHealth() (e.g. a parse failure after a non-ok response) became an
 * unhandled promise rejection, silently stopping health updates and leaving the
 * UI with stale data.
 *
 * This replaces the prior source-grep test (which asserted on "try {",
 * "catch", "setAgentHealth(null)" substrings); it mounts the real hook, makes
 * fetchAgentHealth reject, and asserts agentHealth ends up null without the
 * hook throwing.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import {
  resetDashboardMocks,
  apiMocks,
} from "./helpers/dashboardHarness";
import { AGENT_HEALTH_POLL_MS } from "@/lib/constants";

import { useDashboard } from "@/hooks/useDashboard";

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
  // Silence the expected console.error("Health poll check() failed:", ...).
  vi.spyOn(console, "error").mockImplementation(() => undefined);
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("health poll: error handling", () => {
  // Note: there is deliberately no "rejects on mount → null" test. agentHealth
  // STARTS null, so such a test passes whether or not the catch exists (it is
  // vacuous). The test below is the real one: it drives a SUCCESSFUL poll first
  // so agentHealth is non-null, THEN forces a rejection and asserts it flips
  // back to null — which fails if the catch's setAgentHealth(null) is removed.
  it("does not leave health stale after a later poll error", async () => {
    vi.useFakeTimers({ shouldAdvanceTime: true });
    try {
      // First poll succeeds with a healthy snapshot.
      apiMocks.fetchAgentHealth.mockResolvedValueOnce({
        status: "running",
        active_runs: 1,
        max_concurrent: 4,
        runs: [{ run_id: "run-1", status: "running", started_at: 0 }],
      });

      const { result } = renderHook(() => useDashboard());

      await waitFor(() => expect(result.current.agentHealth).not.toBeNull());
      expect(result.current.agentHealth?.runs).toHaveLength(1);

      // Next poll rejects — health must reset to null, not stay stale.
      apiMocks.fetchAgentHealth.mockRejectedValue(new Error("blip"));
      await act(async () => {
        vi.advanceTimersByTime(AGENT_HEALTH_POLL_MS + 10);
        await Promise.resolve();
      });

      await waitFor(() => expect(result.current.agentHealth).toBeNull());
    } finally {
      vi.useRealTimers();
    }
  });
});
