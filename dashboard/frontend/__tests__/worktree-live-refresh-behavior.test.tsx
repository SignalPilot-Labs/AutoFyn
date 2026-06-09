/**
 * Behavioral regression tests for WorkTree's reactive diff refresh.
 *
 * These mount the real component, drive it through the mocked diff API, and
 * assert on actual calls — so they catch LOGIC regressions the source-grep
 * tests cannot (a grep test passes as long as the strings match, even if the
 * effect is wired to the wrong dependency or gated incorrectly).
 *
 * Covered:
 *  1. A new Write/Edit event triggers a debounced diff refetch mid-round.
 *  2. An active run whose diff source is "unavailable" (early-run 409) keeps
 *     refreshing instead of stalling until reload.
 *  3. A terminal run with a stored diff does NOT keep refetching.
 */

import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { render, act } from "@testing-library/react";
import type { FeedEvent, ToolCall, RunStatus } from "@/lib/types";
import type { DiffStats } from "@/lib/api";
import { DIFF_REFETCH_DEBOUNCE_MS } from "@/lib/constants";

// Mock the diff API at the module boundary so we can assert on calls and
// control responses without touching the network.
vi.mock("@/lib/api", () => ({
  fetchRunDiff: vi.fn(),
  fetchDiffRepo: vi.fn(),
  fetchDiffTmp: vi.fn(),
}));

import { fetchRunDiff, fetchDiffRepo, fetchDiffTmp } from "@/lib/api";
import { WorkTree } from "@/components/worktree/WorkTree";

const mockFetchRunDiff = vi.mocked(fetchRunDiff);
const mockFetchDiffRepo = vi.mocked(fetchDiffRepo);
const mockFetchDiffTmp = vi.mocked(fetchDiffTmp);

function diffStats(source: DiffStats["source"]): DiffStats {
  return { files: [], total_files: 0, total_added: 0, total_removed: 0, source };
}

function writeEvent(id: number, filePath: string): FeedEvent {
  const tc: ToolCall = {
    id,
    run_id: "run-1",
    ts: "2026-01-01T00:00:00.000Z",
    phase: "post",
    tool_name: "Write",
    input_data: { file_path: filePath },
    output_data: { filePath },
    duration_ms: 5,
    permitted: true,
    deny_reason: null,
    agent_role: "worker",
    tool_use_id: `tu-${id}`,
    session_id: null,
    agent_id: null,
  };
  return { _kind: "tool", data: tc };
}

beforeEach(() => {
  vi.useFakeTimers({ shouldAdvanceTime: true });
  mockFetchDiffRepo.mockResolvedValue({ diff: "" });
  mockFetchDiffTmp.mockResolvedValue({ diff: "" });
});

afterEach(() => {
  vi.useRealTimers();
  vi.clearAllMocks();
});

describe("WorkTree: reactive diff refresh (behavioral)", () => {
  it("refetches the diff when a new Write event lands mid-round", async () => {
    mockFetchRunDiff.mockResolvedValue(diffStats("live"));

    const { rerender } = render(
      <WorkTree events={[]} runId="run-1" runStatus={"running" as RunStatus} />,
    );

    // Initial mount fetch.
    await act(async () => { await Promise.resolve(); });
    const afterMount = mockFetchRunDiff.mock.calls.length;
    expect(afterMount).toBeGreaterThanOrEqual(1);

    // A Write event arrives over the stream.
    rerender(
      <WorkTree events={[writeEvent(1, "/home/agentuser/repo/a.ts")]} runId="run-1" runStatus={"running" as RunStatus} />,
    );

    // Before the debounce elapses, no extra refetch.
    expect(mockFetchRunDiff.mock.calls.length).toBe(afterMount);

    // After the debounce window, the diff is refetched reactively.
    await act(async () => {
      vi.advanceTimersByTime(DIFF_REFETCH_DEBOUNCE_MS + 10);
      await Promise.resolve();
    });
    expect(mockFetchRunDiff.mock.calls.length).toBeGreaterThan(afterMount);
  });

  it("keeps refreshing an active run whose diff source is 'unavailable'", async () => {
    // Early-run 409: the run is active but the sandbox/branch isn't ready yet.
    mockFetchRunDiff.mockResolvedValue(diffStats("unavailable"));

    const { rerender } = render(
      <WorkTree events={[]} runId="run-1" runStatus={"starting" as RunStatus} />,
    );
    await act(async () => { await Promise.resolve(); });
    const baseline = mockFetchRunDiff.mock.calls.length;
    expect(baseline).toBeGreaterThanOrEqual(1);

    // A write lands while the source is still "unavailable" — the gate must
    // still refetch (this is the startup-409 fix).
    rerender(
      <WorkTree events={[writeEvent(1, "/home/agentuser/repo/a.ts")]} runId="run-1" runStatus={"starting" as RunStatus} />,
    );
    await act(async () => {
      vi.advanceTimersByTime(DIFF_REFETCH_DEBOUNCE_MS + 10);
      await Promise.resolve();
    });
    expect(mockFetchRunDiff.mock.calls.length).toBeGreaterThan(baseline);
  });

  it("does not keep refetching a terminal run with a stored diff", async () => {
    mockFetchRunDiff.mockResolvedValue(diffStats("stored"));

    const { rerender } = render(
      <WorkTree events={[]} runId="run-1" runStatus={"completed" as RunStatus} />,
    );
    await act(async () => { await Promise.resolve(); });
    const afterMount = mockFetchRunDiff.mock.calls.length;

    // A late event + debounce window must NOT trigger a refetch for a
    // terminal, stored diff (it's final).
    rerender(
      <WorkTree events={[writeEvent(1, "/home/agentuser/repo/a.ts")]} runId="run-1" runStatus={"completed" as RunStatus} />,
    );
    await act(async () => {
      vi.advanceTimersByTime(DIFF_REFETCH_DEBOUNCE_MS + 10);
      await Promise.resolve();
    });
    expect(mockFetchRunDiff.mock.calls.length).toBe(afterMount);
  });
});

describe("WorkTree: diff fetch retry on failure (behavioral)", () => {
  it("a failed stats fetch falls back to a live sentinel and keeps retrying", async () => {
    // First call (mount) rejects; the catch sets a "live" sentinel so the
    // refresh gate stays open and subsequent writes drive a retry.
    mockFetchRunDiff
      .mockRejectedValueOnce(new Error("sandbox not ready"))
      .mockResolvedValue(diffStats("live"));

    const { rerender } = render(
      <WorkTree events={[]} runId="run-1" runStatus={"running" as RunStatus} />,
    );
    await act(async () => { await Promise.resolve(); await Promise.resolve(); });
    const afterFailedMount = mockFetchRunDiff.mock.calls.length;
    expect(afterFailedMount).toBeGreaterThanOrEqual(1);

    // Despite the failed mount, a write still triggers a retry — proving the
    // sentinel kept the run refreshable rather than stalling on empty.
    rerender(
      <WorkTree events={[writeEvent(1, "/home/agentuser/repo/a.ts")]} runId="run-1" runStatus={"running" as RunStatus} />,
    );
    await act(async () => {
      vi.advanceTimersByTime(DIFF_REFETCH_DEBOUNCE_MS + 10);
      await Promise.resolve();
    });
    expect(mockFetchRunDiff.mock.calls.length).toBeGreaterThan(afterFailedMount);
  });
});

function fileDiff(path: string, added: number): DiffStats {
  return {
    files: [{ path, status: "modified", added, removed: 0 }],
    total_files: 1,
    total_added: added,
    total_removed: 0,
    source: "live",
  };
}

describe("WorkTree: stale result discarding (behavioral)", () => {
  it("a slow fetch from a prior run does not overwrite the current run's diff", async () => {
    // run-1's stats fetch hangs; the user switches to run-2 which resolves
    // with distinguishable data.
    let resolveRun1!: (d: DiffStats) => void;
    mockFetchRunDiff.mockImplementation((id: string) => {
      if (id === "run-1") return new Promise<DiffStats>((res) => { resolveRun1 = res; });
      return Promise.resolve(fileDiff("run2-file.ts", 22));
    });

    const { rerender, queryByText } = render(
      <WorkTree events={[]} runId="run-1" runStatus={"running" as RunStatus} />,
    );
    await act(async () => { await Promise.resolve(); });

    // Switch to run-2 before run-1 resolves; run-2's diff renders.
    rerender(<WorkTree events={[]} runId="run-2" runStatus={"running" as RunStatus} />);
    await act(async () => { await Promise.resolve(); });
    expect(queryByText("run2-file.ts")).toBeInTheDocument();

    // Now run-1's stale fetch resolves with different data — it must be
    // discarded by the generation guard, not overwrite run-2's tree.
    await act(async () => {
      resolveRun1(fileDiff("run1-stale.ts", 99));
      await Promise.resolve();
    });

    expect(queryByText("run2-file.ts")).toBeInTheDocument();
    expect(queryByText("run1-stale.ts")).not.toBeInTheDocument();
  });
});
