## Goal
Solve IMO 2026 Problem 5 (problem_id: imo-2026-05, algebra, hard, rating 8).
Statement: Determine all f: R_{>0} -> R_{>0} such that
  sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x * f(y))  for all x, y > 0.
Task type: compute_and_prove, answer_type: characterization — must state the full answer set AND prove both that these work and no others do.
Eval: results/imo-2026-05/current.md `## Status` reaches `solved` (proof-reviewer APPROVE); progress signal = approach ranking in results/imo-2026-05/approaches/.ranking.json.
Baseline (round 1): Status unsolved, zero approaches, empty workspace.
Constraint: prose Markdown rigor per CLAUDE.md rigor rules.

## Goal Updates
- [2026-07-17 01:10] Initial task: solve imo-2026-05.

## Eval History
- Round 0 baseline: unsolved, 0 approaches.
- Round 1: SOLVED — BREAKTHROUGH. Answer: f(x) = x + c, c >= 0 constant — both directions of the characterization proven; all load-bearing algebra re-checked with sympy by the reviewer. Ranking: two-point-pinch Elo 1531.3 (verified-milestone, APPROVE), marching-orbits Elo 1500.0 (verified-milestone, APPROVE — independent second proof), tangent-envelope Elo 1468.7 (unbuilt reserve, moot). current.md Status: solved, Full proof recorded.

## Rules
- ALWAYS: verify candidate answer families algebraically before assuming f=id — the true answer here was a one-parameter family x+c, not just identity (round 1).

## State
Done: Round 1 — 3 explorers (means-squeeze/analytic/retrieval), outliner opened 3 rivals, reviewer approved field, 2 builders produced complete proofs, proof-reviewer APPROVED both. Problem imo-2026-05 SOLVED: f(x)=x+c, c>=0. Lemmas certified: core-identity-ap-orbits, two-point-pinch-bound. current.md holds full proof.
Broken: nothing
Next: nothing — goal achieved; end session.
