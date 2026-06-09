/**
 * Behavioral regression test: handleRepoSwitch must invalidate an in-flight
 * loadRunHistory started by handleSelectRun (BUG 11).
 *
 * Bug: handleSelectRun bumps selectGenRef to invalidate stale loads, but
 * handleRepoSwitch did not. So a loadRunHistory still in flight from a select
 * before the repo switch could resolve afterwards and apply stale state —
 * calling sseRef.connect() for the old run and clobbering the switched repo's
 * (empty) selection.
 *
 * Fix: handleRepoSwitch does selectGenRef.current += 1 (after disconnect,
 * before setSelectedRunId(null)). The stale select's resume `.then`/await sees
 * gen !== selectGenRef.current and returns early before reaching connect().
 *
 * This replaces the prior source-grep test (asserted on source text/position);
 * it mounts the real hook and drives the race, mirroring the interleaving in
 * session-resume-race.test.tsx.
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

beforeEach(() => {
  localStorage.clear();
  resetDashboardMocks();
});

afterEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
});

describe("handleRepoSwitch: invalidates in-flight loadRunHistory from a select (BUG 11)", () => {
  it("a stale run-A load resolving after a repo switch does not connect for run-A", async () => {
    runsControl.current.runs = [makeRun({ id: "run-A", run_id: "run-A" })];

    const { result } = renderHook(() => useDashboard());

    // Make the NEXT loadRunHistory (run-A's select) HANG so we can interleave a
    // repo switch before it resolves.
    let resolveSelect!: (v: unknown) => void;
    apiMocks.loadRunHistory.mockImplementationOnce(
      () => new Promise((res) => { resolveSelect = res; }),
    );

    // Start selecting run-A. Its loadRunHistory is now pending; don't await the
    // full handleSelectRun (it would never settle until we resolve).
    let selectPromise!: Promise<unknown>;
    act(() => {
      selectPromise = result.current.handleSelectRun("run-A");
    });

    // Switch repos before the run-A load resolves. This bumps selectGenRef, so
    // the pending select is now stale.
    await act(async () => {
      await result.current.handleRepoSwitch("other/repo");
    });

    const connectsAfterSwitch = sseControl.connect.mock.calls.length;

    // Now the stale run-A load resolves.
    await act(async () => {
      resolveSelect({ events: [], lastToolId: 9, lastAuditId: 9, truncated: false });
      await selectPromise;
      await Promise.resolve();
    });

    // The stale select returned early at the gen guard; it must NOT have issued
    // a connect after the switch, and certainly not for run-A.
    expect(sseControl.connect.mock.calls.length).toBe(connectsAfterSwitch);
    const connectedRunIds = sseControl.connect.mock.calls.map((c) => c[0]);
    expect(connectedRunIds).not.toContain("run-A");
  });

  it("the select still connects for run-A when NO repo switch interleaves", async () => {
    // Control case: without the invalidation race, the same select connects
    // normally. Proves the assertion above isn't trivially true.
    runsControl.current.runs = [makeRun({ id: "run-A", run_id: "run-A" })];

    const { result } = renderHook(() => useDashboard());

    apiMocks.loadRunHistory.mockResolvedValueOnce({
      events: [], lastToolId: 9, lastAuditId: 9, truncated: false,
    });

    await act(async () => {
      await result.current.handleSelectRun("run-A");
    });

    const connectedRunIds = sseControl.connect.mock.calls.map((c) => c[0]);
    expect(connectedRunIds).toContain("run-A");
  });
});
