## Goal
Solve `imo-2026-04` with a complete rigorous prose proof and explicit characterization, recorded in `results/imo-2026-04/current.md`.

Metric: proof-reviewer verdict and workspace status. Eval: inspect `results/imo-2026-04/current.md` `## Status` plus `results/imo-2026-04/approaches/.ranking.json`; terminal target is proof-reviewer `APPROVE` with status `solved` and a verified full proof. Baseline (round 1): workspace absent, no approaches/ranking, status unstarted. Target: solved. Constraints: follow CLAUDE.md rigor and file contracts; use both knowledge resources; characterize all admissible theta and verify both necessity and sufficiency; one whole-problem attempt per slug; no hand-editing ranking sidecar. The problem is labeled medium in the benchmark, but the user's explicit choice overrides the repository's usual hard-only selection policy.

## Goal Updates

## Eval History
- Round 1 baseline: `results/imo-2026-04/` absent; approach sampler returned zero entries; no `current.md`; status unstarted.
- Round 1 BREAKTHROUGH — **Exact requested characterization:** established as $\boxed{\theta=180^\circ/n\text{ for integers }n\ge2}$. **Necessity:** complete via branch-stable nonintegrality invariant. **Sufficiency:** complete via strict integer-crossing cut and balanced positive-integer-label descent. **Answer verification:** complete. Proof-reviewer verdict `APPROVE`; status `solved`; correctness/completeness/progress each 10/10. Ranking: `semigroup-crossing-binary-descent` Elo 1500, expanded 1, outcome `verified-milestone`.

## Rules
- ALWAYS: Treat the user's explicit `imo-2026-04` selection as fixed for this run despite its benchmark `medium` label (explicit user choice overrides default filtering, round 1).
- ALWAYS: Keep rival slugs as complete end-to-end solution attempts with genuinely distinct framings (avoid the shared-gap trap, round 1).
- NEVER: Treat rational-grid experiments as proof for arbitrary real angles (explorer warning, round 1).
- ALWAYS: For a counterstrategy, maintain a branch-stable invariant excluding every positive integral multiple of theta, not merely theta itself (explorer warning, round 1).

## State
### Done
- Round 1 setup: installed numpy, scipy, sympy; confirmed no test/CI setup applies.
- Established unstarted baseline and completed three distinct exploration passes (structural, algebraic, constructive).

### Broken
- None. The target problem is solved and independently approved.

### Next
- End the run; no further mathematical work is needed for `imo-2026-04`.

### Done (continued)
- Outlined and independently ranked four proposed framings; rejected three as duplicate variants and built the surviving whole-problem approach.
- Completed and independently verified a rigorous proof. `results/imo-2026-04/current.md` is solved; three reusable lemmas are certified; proof-reviewer verdict is APPROVE.
- Added `.claude/worktrees/` to `.gitignore` so only intended problem artifacts are committed.
