/**
 * Regression test: WorkTree must not get stuck when fetchRunDiff fails.
 *
 * Before the fix, if fetchRunDiff(runId) failed, diffData remained null. The
 * refresh condition requires diffData?.source === "live" | "agent" (or an
 * active "unavailable" run), which is false for null — so refreshing never
 * started and the component showed an empty state forever.
 *
 * The fix sets diffData to a live-source sentinel in refetchDiff's catch block
 * so the refresh gate (isRefreshSource) becomes true and the interval/event
 * refetch paths retry the fetch automatically. refetchDiff is the single shared
 * fetch path used by the mount effect, the poll, and the event-driven refetch,
 * so this guard protects all three.
 */

import { describe, it, expect } from "vitest";
import * as fs from "fs";
import * as path from "path";

const SRC = fs.readFileSync(
  path.resolve(__dirname, "../components/worktree/WorkTree.tsx"),
  "utf-8",
);

function refetchDiffBody(): string {
  const fnStart = SRC.indexOf("const refetchDiff = useCallback");
  const fnEnd = SRC.indexOf("}, [fetchDiffBodies]);", fnStart);
  return SRC.slice(fnStart, fnEnd);
}

describe("WorkTree: diff fetch retry via live sentinel on fetch failure", () => {
  it("refetchDiff catch block calls setDiffData", () => {
    const body = refetchDiffBody();
    const catchStart = body.indexOf(".catch(");
    expect(catchStart).toBeGreaterThan(-1);
    expect(body.slice(catchStart)).toContain("setDiffData(");
  });

  it("catch block sets source to 'live' to enable refresh retry", () => {
    const body = refetchDiffBody();
    expect(body.slice(body.indexOf(".catch("))).toContain('"live"');
  });

  it("catch block sets empty files array in sentinel", () => {
    const body = refetchDiffBody();
    expect(body.slice(body.indexOf(".catch("))).toContain("files: []");
  });

  it("refresh gate checks for 'live' source which the sentinel satisfies", () => {
    expect(SRC).toContain('diffData?.source === "live"');
  });
});
