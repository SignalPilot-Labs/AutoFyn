## Goal
Solve exactly `imo-2026-05`: characterize all functions \(f:\mathbb R_{>0}\to\mathbb R_{>0}\) satisfying
\[
\sqrt{\frac{x^2+f(y)^2}{2}}\ge \frac{f(x)+y}{2}\ge \sqrt{x f(y)}
\]
for all positive real \(x,y\), and produce a proof-reviewer-certified complete rigorous proof in `results/imo-2026-05/current.md`.

Metric: proof-reviewer status and approach ranking. Eval: inspect `results/imo-2026-05/current.md` `## Status` and `results/imo-2026-05/approaches/.ranking.json`; terminal target is `solved` with an APPROVE verdict, explicit complete characterization, proof of necessity, and verification of sufficiency. Baseline (2026-07-16, round 1): workspace absent, status `unsolved`, zero registered approaches, no current best. Constraints: one whole-problem attempt per slug; consult both `knowledge_base.md` and the crux corpus; prose Markdown; all cases and final candidates verified.

## Goal Updates

## Eval History
- Round 1 baseline: `results/imo-2026-05/` absent; status `unsolved`; 0 approaches; no ranking; no current best.
- Round 1 Goal Progress — BREAKTHROUGH: both `lattice-envelope-amplification` and `orbit-collision-clopen` received proof-reviewer APPROVE with correctness/completeness/progress 10/10. `current.md` status is `solved` and certifies the complete characterization \(f(t)=t+c\) for arbitrary \(c\ge0\). Ranking: lattice-envelope-amplification Elo 1516, orbit-collision-clopen Elo 1484; both outcomes `verified-milestone`.

## Rules
- ALWAYS: Consult both `knowledge_base.md` and the crux corpus, proving any adapted crux move from scratch (project requirement, round 1).
- ALWAYS: Treat each approach slug as an end-to-end attempt at the full characterization, not as a sublemma (project requirement, round 1).
- ALWAYS: Explicitly state and verify every candidate function in both inequalities (compute-and-prove rigor requirement, round 1).
- ALWAYS: Derive the two signed squared-slack identities before using the absolute displacement bound, and justify the coefficient's sign (prevents circular sign reasoning, round 1).
- NEVER: Infer continuity of the displacement function; prove zero-fiber closure and openness directly from the numerical inequality (reviewer rigor check, round 1).
- ALWAYS: For isolated agents, synchronize completed artifacts into the main workspace before final evaluation (isolated worktrees are not automatically visible there, round 1).

## State
### Done
- Round 1 setup installed and verified numpy 2.5.1, scipy 1.18.0, and sympy 1.14.0.
- Consulted both retrieval resources through three independent scouting lenses.
- Registered, ranked, built, and reviewed two rival whole-problem approaches.
- Both approaches were independently certified complete and correct.
- `results/imo-2026-05/current.md` now contains the certified full lattice-envelope proof.
- Four reusable lemmas were reviewer-certified in `results/imo-2026-05/lemmas/`.
- Added `.claude/worktrees/` to `.gitignore` so agent worktrees are not committed.

### Broken
- None.

### Next
- Goal achieved; end the session.
