## Goal

Solve problem `imo-2026-05` (IMO 2026 P5, algebra, difficulty 8, hard) with a complete rigorous prose proof.

- Statement: Determine all f: R_{>0} -> R_{>0} such that sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x,y > 0. Task: compute_and_prove, answer_type: characterization.
- Metric: `results/imo-2026-05/current.md` `## Status` reaching `solved` (proof-reviewer APPROVE); per-round signal is the approach ranking in `results/imo-2026-05/approaches/.ranking.json`.
- Eval: read `results/imo-2026-05/current.md` Status + `.ranking.json` each round.
- Baseline (round 1): no workspace existed — Status effectively `unsolved`, zero approaches.
- Constraint: prose Markdown proof, rigor rules in CLAUDE.md; characterization needs both directions.

## Goal Updates

- [2026-07-16 07:34] Initial user message: solve imo-2026-05 per CLAUDE.md. (recorded round 1)

## Eval History

- Round 1 — BREAKTHROUGH — Status: solved (from unsolved baseline). Three independent complete proofs all APPROVED in round 1: chain-lipschitz-squeeze (Elo 1531, verified-milestone, canonical proof in current.md), right-spreading-fixed-points (1486, verified-milestone), orbit-forbidden-zone (1483, verified-milestone). All live, zero open gaps. Answer of record: f(x) = x + c for all x > 0, c >= 0 constant — family verified by substitution (margin (x−y−c)²/4 both sides), uniqueness proven three independent ways, c < 0 excluded by codomain. Certified lemmas: fe-double-iterate, orbit-invariance, h-nonnegative, chain-inequality, increment-bounds, onepos-right.

## Rules

- ALWAYS: for functional-inequality problems, have one explorer verify the conjectured answer family numerically before outlining — the family here was x+c (not just id), and catching that early prevented a wrong-answer round (round 1).
- ALWAYS: have the outline-reviewer re-derive load-bearing identities in sympy before approving skeletons — it validated all five and caught nothing broken, cheap insurance (round 1).

## State

### Done

- Round 1: full pipeline (3 explorers → outliner → outline-reviewer → 3 builders → 1 reviewer). Problem imo-2026-05 SOLVED — three independently verified complete proofs; canonical proof (chain-lipschitz-squeeze) in results/imo-2026-05/current.md ## Full proof; 6 certified lemmas in lemmas/.

### Broken

- Nothing.

### Next

- Goal achieved; nothing remains. If the run continues, only polish (e.g. prose tightening of current.md) is available.
