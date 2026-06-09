/**
 * Behavioral regression test: handleSelectRun must NOT persist a run id to
 * localStorage("autofyn_last_run_id") unless loadRunHistory succeeds (BUG 10).
 *
 * Bug: localStorage.setItem("autofyn_last_run_id", id) used to run immediately
 * after setSelectedRunId(id), before loadRunHistory even started. If the load
 * failed (network error, 404, etc.) the invalid run id was already persisted,
 * and the next auto-selection effect would keep trying to restore it.
 *
 * Fix: setItem lives inside the try block, only on the success path (after the
 * load resolves). On a rejected load the catch path runs and never persists.
 *
 * This replaces the prior source-grep test (asserted on source text/position);
 * it mounts the real hook and drives both the success and failure paths.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, act } from "@testing-library/react";
import {
  resetDashboardMocks,
  sseControl,
  apiMocks,
  runsControl,
  makeRun,
} from "./helpers/dashboardHarness";

import { useDashboard } from "@/hooks/useDashboard";

const LAST_RUN_KEY = "autofyn_last_run_id";

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("handleSelectRun: persists last run id only on a successful load (BUG 10)", () => {
  it("persists the run id when loadRunHistory resolves", async () => {
    runsControl.current.runs = [makeRun({ id: "good-run", run_id: "good-run" })];
    apiMocks.loadRunHistory.mockResolvedValueOnce({
      events: [],
      lastToolId: 0,
      lastAuditId: 0,
      truncated: false,
    });

    const { result } = renderHook(() => useDashboard());

    await act(async () => {
      await result.current.handleSelectRun("good-run");
    });

    expect(localStorage.getItem(LAST_RUN_KEY)).toBe("good-run");
  });

  it("does NOT persist the run id when loadRunHistory rejects", async () => {
    runsControl.current.runs = [makeRun({ id: "bad-run", run_id: "bad-run" })];

    const { result } = renderHook(() => useDashboard());

    // handleSelectRun catches the load error internally and resolves normally,
    // so no try/catch is needed around the await here.
    apiMocks.loadRunHistory.mockRejectedValueOnce(new Error("network down"));

    await act(async () => {
      await result.current.handleSelectRun("bad-run");
    });

    // The failed run id must never have reached localStorage.
    expect(localStorage.getItem(LAST_RUN_KEY)).toBeNull();
    expect(localStorage.getItem(LAST_RUN_KEY)).not.toBe("bad-run");
  });

  it("a failed select after a successful one leaves the good id in place", async () => {
    runsControl.current.runs = [
      makeRun({ id: "good-run", run_id: "good-run" }),
      makeRun({ id: "bad-run", run_id: "bad-run" }),
    ];

    const { result } = renderHook(() => useDashboard());

    apiMocks.loadRunHistory.mockResolvedValueOnce({
      events: [],
      lastToolId: 0,
      lastAuditId: 0,
      truncated: false,
    });
    await act(async () => {
      await result.current.handleSelectRun("good-run");
    });
    expect(localStorage.getItem(LAST_RUN_KEY)).toBe("good-run");

    apiMocks.loadRunHistory.mockRejectedValueOnce(new Error("404"));
    await act(async () => {
      await result.current.handleSelectRun("bad-run");
    });

    // The bad id never overwrote the good one.
    expect(localStorage.getItem(LAST_RUN_KEY)).toBe("good-run");
  });
});
