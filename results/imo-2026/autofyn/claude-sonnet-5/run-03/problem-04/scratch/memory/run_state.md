## Goal

Solve IMO-2026-04 (Mulan's Triangle Game), explicitly requested by the user by problem id.

**Note:** This problem's `difficulty_level` in problems.jsonl is `"medium"` (difficulty_rating 7), not `"hard"` — it falls outside CLAUDE.md's default "hard problems only" filter. The user explicitly named this problem_id, overriding the default selection rule.

**Statement:** Shan-Yu and Mulan play a game. Let θ be an angle, 0°<θ<180°, known to both. Shan-Yu makes a paper triangle T of his choice. Repeat: if T has an angle exactly θ, Mulan wins. Otherwise Mulan picks a point P on the perimeter of T (not a vertex), cuts straight from P to the opposite vertex, splitting T into two triangles; Shan-Yu discards one, the other becomes the new T. For which θ can Mulan guarantee victory in finitely many steps, regardless of Shan-Yu's play?

Metric: `results/imo-2026-04/current.md` `## Status`, proof-reviewer APPROVE verdict.

Target: Status = solved, proof-reviewer APPROVE, answer characterized explicitly and verified.

**ANSWER (proved, solved):** Mulan has a winning strategy iff θ = 180°/n for some integer n ≥ 2.

## Goal Updates

## Eval History
- Round 1: Baseline unsolved → SOLVED same round. 3 math-explorers (angle-tracking, adversary, shapespace) converged numerically on θ=180°/n. proof-outliner produced 4 diverse approaches (shave-and-halve-forcing, mod-theta-invariant, ngon-arc-reduction, maximal-safe-set-fixedpoint). outline-reviewer registered+ranked all 4, built all 4. proof-reviewer verdicts: ngon-arc-reduction = APPROVE (Status: solved, complete gap-free proof both directions — "if" via Cut Formula/Shave Lemma/Residue-Alignment Lemma; "only if" via disjoint-bad-residue-sets invariant argument); shave-and-halve-forcing, mod-theta-invariant, maximal-safe-set-fixedpoint = CHANGES REQUESTED (Status: partial, each correctly proved partial pieces, no overclaiming). current.md updated to Status: solved with full combined proof. 4 lemmas certified to results/imo-2026-04/lemmas/. BREAKTHROUGH — full solve in round 1.

## Rules
- ALWAYS use exact-Fraction arithmetic (not floats) when numerically sanity-checking angle-game claims for this problem — float grid simulation gave spurious negatives in round 1 exploration (math-explorer-angle-tracking, round 1).
- User-named problem_id explicitly overrides CLAUDE.md's "hard difficulty_level only" default filter (round 1).

## State

### Done
- Round 1: Set up results/imo-2026-04/ workspace, installed numpy/scipy/sympy. Ran full pipeline (3 explorers → outliner → outline-reviewer → 4 parallel builders → 1 reviewer) and reached a fully verified, gap-free solve in a single round. results/imo-2026-04/current.md Status = solved with complete proof. 4 lemma files certified in results/imo-2026-04/lemmas/.

### Broken
(none)

### Next
Goal achieved: Status solved, proof-reviewer APPROVE on ngon-arc-reduction, current.md carries the full verified proof. No further rounds needed — end_session.
