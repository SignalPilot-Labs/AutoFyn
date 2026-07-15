## Goal
Solve hard olympiad problem `imo-2026-03` with a complete rigorous prose proof.
Metric: `results/imo-2026-03/current.md` status and approach population ranking.
Eval command: inspect `results/imo-2026-03/current.md` (`## Status`) and `results/imo-2026-03/approaches/.ranking.json` after proof review.
Baseline: no pre-existing workspace or ranked approaches; status effectively unsolved.
Target: `Status: solved` with proof-reviewer APPROVE, a complete `## Full proof`, every case justified, named tools cited from `knowledge_base.md`, and any final answer explicitly verified.
Constraints: one whole-problem attempt per slug; consult both `knowledge_base.md` and the crux corpus; write only under `results/imo-2026-03/`; do not hand-edit `.ranking.json`.

## Goal Updates

## Eval History
- Round 1 — BREAKTHROUGH — **Status: solved.** The problem is solved by the approved `threshold-parity-toggles` approach, and reviewer-owned `results/imo-2026-03/current.md` now contains the complete verified proof. Raw ranking signal after outcome recording: `threshold-parity-toggles`: Elo 1516.0, expanded 1, last outcome `verified-milestone`, stale `true` pending the next outline-reviewer Elo fold; `dyadic-reserve-induction`: Elo 1484.0, expanded 1, last outcome `advanced`, stale `true` pending the next outline-reviewer Elo fold.

## Rules
- ALWAYS: Keep each approach slug as a complete end-to-end attempt at the actual problem (because splitting a shared proof line across slugs creates correlated failure, round 1).
- ALWAYS: Consult both `knowledge_base.md` and domain/subtopic-filtered crux corpus hints, proving every borrowed move from scratch (because repository instructions require both retrieval resources, round 1).
- NEVER: Hand-edit `approaches/.ranking.json` (because it is tool-owned, round 1).
- ALWAYS: Treat refinement toggles as acting on current pieces and retain original-parent provenance through repeated cuts (because abstract toggles may otherwise be unrealizable, round 1).
- ALWAYS: For continuous refinements, verify positivity, interior/distinct marks, exact cut counts, and every minimax quantifier (because legality is load-bearing, round 1).
- NEVER: Promote reserve or scale-charging language to a lemma without an explicit invariant covering arbitrary real splits (because sorted fragments can cross many ranks, round 1).

## State
### Done
- Installed `numpy`, `scipy`, and `sympy`.
- Established the exact answer `c_n = 2^n/(2^{n+1}-1)`.
- Explored structural, computational, and crux-analogy lenses.
- Registered and ranked two whole-problem approaches.
- Built `threshold-parity-toggles` and `dyadic-reserve-induction`.
- Proof reviewer APPROVED `threshold-parity-toggles` as a complete rigorous solution and published reviewer-owned `current.md` plus six certified lemmas.
- Recorded ranking outcomes: threshold route verified milestone; reserve route advanced but partial.
- Validated the solved status, full-proof marker, boxed answer, and ranking JSON syntax.
- Ignored Claude Code isolated worktree artifacts in `.gitignore`.

### Broken
- `dyadic-reserve-induction` remains partial because its two all-n refinement inequalities are absent; this does not affect the solved status because the threshold route is approved.

### Next
- Goal achieved. End the session when the time lock permits.
