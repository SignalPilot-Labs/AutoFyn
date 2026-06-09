/**
 * Regression test: WorkTree must not apply stale diff fetch results from a prior run.
 *
 * Before the fix, `fetchDiffBodies` and `fetchRunDiff` in the polling effect had no
 * generation guard. When the user rapidly switched runs, an older async fetch could
 * resolve after a newer one and overwrite `repoDiff`/`tmpDiff`/`diffData` with stale
 * data from the previous run, causing the wrong diff to be shown.
 *
 * The fix adds `diffGenRef` (a useRef counter), increments it on each new runId in
 * the initial fetch effect, and checks `gen !== diffGenRef.current` before every
 * `set*` call in `fetchDiffBodies` and in the shared `refetchDiff` callback that
 * both the polling effect and the event-driven refetch delegate to.
 */

import { describe, it, expect } from "vitest";
import * as fs from "fs";
import * as path from "path";

const SRC = fs.readFileSync(
  path.resolve(__dirname, "../components/worktree/WorkTree.tsx"),
  "utf-8",
);

describe("WorkTree: stale diff fetch guard via generation counter", () => {
  it("declares diffGenRef as a useRef", () => {
    expect(SRC).toContain("diffGenRef = useRef(0)");
  });

  it("initial fetch effect increments diffGenRef", () => {
    expect(SRC).toContain("const gen = ++diffGenRef.current");
  });

  it("fetchDiffBodies accepts a gen parameter", () => {
    // Function signature: (id: string, gen: number)
    expect(SRC).toMatch(/fetchDiffBodies\s*=\s*useCallback\(\s*\(id:\s*string,\s*gen:\s*number\)/);
  });

  it("fetchDiffBodies guards setRepoDiff with generation check", () => {
    const fnStart = SRC.indexOf("const fetchDiffBodies = useCallback");
    const fnEnd = SRC.indexOf("}, []);", fnStart);
    const fnBody = SRC.slice(fnStart, fnEnd + 7);
    expect(fnBody).toContain("if (gen !== diffGenRef.current) return");
    expect(fnBody).toContain("setRepoDiff(");
    expect(fnBody).toContain("setTmpDiff(");
  });

  it("refetchDiff guards setDiffData in .then with a generation check", () => {
    const fnStart = SRC.indexOf("const refetchDiff = useCallback");
    const fnEnd = SRC.indexOf("}, [fetchDiffBodies]);", fnStart);
    const fnBody = SRC.slice(fnStart, fnEnd);
    // setDiffData only runs when the captured gen still matches.
    expect(fnBody).toContain("if (gen === diffGenRef.current) setDiffData(d)");
  });

  it("initial fetch effect bumps the generation and delegates to refetchDiff", () => {
    const effectStart = SRC.indexOf("const gen = ++diffGenRef.current");
    expect(effectStart).toBeGreaterThan(-1);
    const callStart = SRC.indexOf("refetchDiff(runId, gen)", effectStart);
    expect(callStart).toBeGreaterThan(effectStart);
  });

  // The poll and the event-driven refetch both delegate to the shared
  // `refetchDiff` callback, which is where the generation guard now lives.
  // These assertions follow the guard into that callback rather than
  // expecting it inlined in each effect.
  it("refetchDiff is the shared stats+bodies fetcher taking (id, gen)", () => {
    expect(SRC).toMatch(/refetchDiff\s*=\s*useCallback\(\s*\(id:\s*string,\s*gen:\s*number\)/);
  });

  it("refetchDiff guards setDiffData with a generation check", () => {
    const fnStart = SRC.indexOf("const refetchDiff = useCallback");
    const fnEnd = SRC.indexOf("}, [fetchDiffBodies]);", fnStart);
    const fnBody = SRC.slice(fnStart, fnEnd);
    expect(fnBody).toContain("if (gen !== diffGenRef.current) return");
    expect(fnBody).toContain("setDiffData(");
    // Bodies are fetched through the gen-guarded fetchDiffBodies helper.
    expect(fnBody).toContain("fetchDiffBodies(id, gen)");
  });

  it("polling effect calls refetchDiff with the current generation", () => {
    const pollingEffect = SRC.indexOf("const id = setInterval");
    const pollingEnd = SRC.indexOf("return () => clearInterval(id)", pollingEffect);
    const pollingBody = SRC.slice(pollingEffect, pollingEnd);
    expect(pollingBody).toContain("refetchDiff(runId, diffGenRef.current)");
  });

  it("event-driven refetch calls refetchDiff with the current generation", () => {
    const debounceEffect = SRC.indexOf("const t = setTimeout");
    const debounceEnd = SRC.indexOf("return () => clearTimeout(t)", debounceEffect);
    const debounceBody = SRC.slice(debounceEffect, debounceEnd);
    expect(debounceBody).toContain("refetchDiff(runId, diffGenRef.current)");
  });
});
