/**
 * Behavioral run-selection regression tests.
 *
 * The auto-selection effect in useDashboard picks a run ONLY when none is
 * selected and the runs list is non-empty. Its priority order is:
 *   1. an ACTIVE run (isActiveStatus) — selected immediately, short-circuits;
 *   2. otherwise, the run whose id is stored in localStorage under
 *      "autofyn_last_run_id" (if it still exists in the list);
 *   3. otherwise, runs[0].
 * It must never yank the user off a run they deliberately selected (it bails
 * when selectedRunId is already set), and selection always goes through
 * handleSelectRun (which connects SSE), never a bare setSelectedRunId.
 *
 * This replaces the prior source-grep test; it mounts the real hook and drives
 * the effect by seeding runsControl before renderHook.
 */

import { describe, it, expect, beforeEach, afterEach, vi } from "vitest";
import { renderHook, waitFor, act } from "@testing-library/react";
import {
  resetDashboardMocks,
  runsControl,
  sseControl,
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

describe("run auto-selection: active runs take priority", () => {
  it("auto-selects the active run when none is selected", async () => {
    runsControl.current.runs = [
      makeRun({ id: "done-1", run_id: "done-1", status: "completed" }),
      makeRun({ id: "live-1", run_id: "live-1", status: "running" }),
    ];

    const { result } = renderHook(() => useDashboard());

    await waitFor(() => expect(result.current.selectedRunId).toBe("live-1"));
    // Selection went through handleSelectRun → SSE connect for the active run.
    await waitFor(() => expect(sseControl.connect).toHaveBeenCalled());
    const connectedIds = sseControl.connect.mock.calls.map((c) => c[0]);
    expect(connectedIds).toContain("live-1");
  });

  it("active run wins even when a different last_run_id is stored", async () => {
    localStorage.setItem("autofyn_last_run_id", "done-1");
    runsControl.current.runs = [
      makeRun({ id: "done-1", run_id: "done-1", status: "completed" }),
      makeRun({ id: "live-1", run_id: "live-1", status: "running" }),
    ];

    const { result } = renderHook(() => useDashboard());

    await waitFor(() => expect(result.current.selectedRunId).toBe("live-1"));
  });
});

describe("run auto-selection: localStorage restore when no active run", () => {
  it("restores the stored last_run_id when no run is active", async () => {
    localStorage.setItem("autofyn_last_run_id", "done-2");
    runsControl.current.runs = [
      makeRun({ id: "done-1", run_id: "done-1", status: "completed" }),
      makeRun({ id: "done-2", run_id: "done-2", status: "completed" }),
    ];

    const { result } = renderHook(() => useDashboard());

    await waitFor(() => expect(result.current.selectedRunId).toBe("done-2"));
  });

  it("ignores a stored id that is no longer in the runs list", async () => {
    localStorage.setItem("autofyn_last_run_id", "gone-99");
    runsControl.current.runs = [
      makeRun({ id: "done-1", run_id: "done-1", status: "completed" }),
      makeRun({ id: "done-2", run_id: "done-2", status: "completed" }),
    ];

    const { result } = renderHook(() => useDashboard());

    // Stale stored id is dropped → falls back to runs[0].
    await waitFor(() => expect(result.current.selectedRunId).toBe("done-1"));
  });
});

describe("run auto-selection: runs[0] fallback", () => {
  it("falls back to the first run when no active run and no stored id", async () => {
    runsControl.current.runs = [
      makeRun({ id: "done-1", run_id: "done-1", status: "completed" }),
      makeRun({ id: "done-2", run_id: "done-2", status: "completed" }),
    ];

    const { result } = renderHook(() => useDashboard());

    await waitFor(() => expect(result.current.selectedRunId).toBe("done-1"));
  });
});

describe("run auto-selection: never yanks a deliberate selection", () => {
  it("does not re-select once a run is already selected", async () => {
    runsControl.current.runs = [
      makeRun({ id: "done-1", run_id: "done-1", status: "completed" }),
      makeRun({ id: "done-2", run_id: "done-2", status: "completed" }),
    ];

    const { result } = renderHook(() => useDashboard());

    // Auto-selection picks runs[0] first.
    await waitFor(() => expect(result.current.selectedRunId).toBe("done-1"));

    // User deliberately switches to done-2.
    await act(async () => { await result.current.handleSelectRun("done-2"); });
    expect(result.current.selectedRunId).toBe("done-2");

    // Let the auto-selection effect run again — it must NOT yank back to runs[0].
    await act(async () => { await new Promise((r) => setTimeout(r, 0)); });
    expect(result.current.selectedRunId).toBe("done-2");
  });
});
