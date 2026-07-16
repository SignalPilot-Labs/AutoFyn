## Goal

Solve **imo-2026-01** (IMO 2026 P1) with a complete, rigorous prose proof.

Statement: 2026 integers >1 on a blackboard. A move picks two entries m>1, n>1 from different places and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n). Moves continue while possible.
(a) Prove that after finitely many moves, exactly one integer M on the board is >1.
(b) Prove M does not depend on the choices.

Metric: proof-reviewer verdict on results/imo-2026-01/current.md.
Eval: proof-reviewer judges the built approach(es); Status in results/imo-2026-01/current.md must reach `solved` (both parts (a) and (b), rigorous, no gaps).
Baseline (round 1): no proof exists, Status unsolved, empty approach population.
Target: Status `solved`, proof-reviewer APPROVE, both parts complete.
Constraints: prose Markdown proof; no skipped cases; name every theorem; termination argument for (a) must be rigorous.

## Goal Updates
- [2026-07-15] User: solve imo-2026-01 (overrides CLAUDE.md "hard only" default; this problem is tagged medium, difficulty_rating 5).

## Eval History
- Round 1 baseline: empty population, Status unsolved.
- Round 1 result: BREAKTHROUGH — Status SOLVED. Three approaches all proof-reviewer APPROVE (gap-free proofs of both (a) and (b)). Elo: valuation-gcd 1516.8, omega-count-monovariant 1514.5 (adopted as Full proof in current.md), product-count-monovariant 1468.7. Certified lemma euclid-step-invariant. GOAL ACHIEVED round 1.

## Rules
- ALWAYS: attack ONLY imo-2026-01 this whole run (fixed in round 1, per CLAUDE.md).
- ALWAYS: dispatch math-explorer x(1-3) parallel with distinct lenses -> proof-outliner -> outline-reviewer -> proof-builder xN -> proof-reviewer, every round (because CLAUDE.md forbids fast-path, round 1).

## State
### Done
- Round 1: workspace created, packages installed. Full pipeline run: 3 explorers (algebraic/termination/computation) -> outliner (3 approaches) -> outline-reviewer (all APPROVE, registered, ranked) -> 3 builders (all solved) -> proof-reviewer (all 3 APPROVE). current.md Status=solved with Full proof (both parts). Certified lemma euclid-step-invariant.
### Broken
- (nothing broken; goal achieved)
### Next
- GOAL ACHIEVED. If more rounds run: optionally polish exposition of the adopted proof in current.md, or diversify a 4th route. No mathematical work remains.
