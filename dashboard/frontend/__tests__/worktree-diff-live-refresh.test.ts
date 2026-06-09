/**
 * Regression test: WorkTree must refresh the diff mid-round, not only on the
 * 15s poll or a page reload.
 *
 * Before the fix, the authoritative git diff (stats + bodies) was refreshed
 * only by a fixed-interval poll, so a Write/Edit landed in the file tree (built
 * from SSE events) up to a full poll cycle before its diff body and line counts
 * caught up. To the user this read as "the diff doesn't update until I reload or
 * the round completes."
 *
 * Two changes fix it:
 *  1. An event-driven debounced refetch keyed on the live write count, so the
 *     diff refetches shortly after edits land instead of waiting for the poll.
 *  2. The refresh gate (`isRefreshSource`) now also covers an active run whose
 *     diff source is still "unavailable" (early-run 409 before the sandbox /
 *     working branch is ready) — otherwise a run selected at startup would
 *     never start refreshing and stay empty until reload.
 */

import { describe, it, expect } from "vitest";
import * as fs from "fs";
import * as path from "path";

const SRC = fs.readFileSync(
  path.resolve(__dirname, "../components/worktree/WorkTree.tsx"),
  "utf-8",
);

describe("WorkTree: event-driven live diff refresh", () => {
  it("derives a live write count from the event-stream changes", () => {
    expect(SRC).toContain("const liveWriteCount = writeChanges.length");
  });

  it("has a debounced refetch effect keyed on the live write count", () => {
    const effectStart = SRC.indexOf("const t = setTimeout");
    expect(effectStart).toBeGreaterThan(-1);
    const effectEnd = SRC.indexOf("return () => clearTimeout(t)", effectStart);
    const body = SRC.slice(effectStart, effectEnd);
    expect(body).toContain("refetchDiff(runId, diffGenRef.current)");
    expect(body).toContain("DIFF_REFETCH_DEBOUNCE_MS");
  });

  it("debounce effect lists liveWriteCount as a dependency", () => {
    // The effect re-arms whenever a new write lands.
    expect(SRC).toMatch(/\[runId,\s*isRefreshSource,\s*liveWriteCount,\s*refetchDiff\]/);
  });

  it("debounce effect is skipped when there are no live writes", () => {
    const effectStart = SRC.indexOf("const t = setTimeout");
    // Guard appears just above the setTimeout.
    const guardRegion = SRC.slice(effectStart - 200, effectStart);
    expect(guardRegion).toContain("liveWriteCount === 0");
  });

  it("refresh gate covers an active run whose source is still 'unavailable'", () => {
    expect(SRC).toContain("const runIsActive = runStatus !== null && !TERMINAL_STATUSES.has(runStatus)");
    expect(SRC).toMatch(/runIsActive\s*&&\s*diffData\?\.source === "unavailable"/);
  });

  it("refresh gate still covers the live/agent sandbox sources", () => {
    const gateStart = SRC.indexOf("const isRefreshSource");
    const gateEnd = SRC.indexOf(";", gateStart);
    const gate = SRC.slice(gateStart, gateEnd);
    expect(gate).toContain('diffData?.source === "live"');
    expect(gate).toContain('diffData?.source === "agent"');
  });
});
