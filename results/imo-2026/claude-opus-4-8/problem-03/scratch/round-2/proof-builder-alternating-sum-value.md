# Build report — alternating-sum-value (imo-2026-03)

**Status: partial.** Two hard directions remain open (GAP AL, GAP AU); everything else is now rigorous.

## Closed this round (full proofs in the approach file)
1. **Lemma G** (greedy/odd-index) — proved in full via zero-sum minimax + backward induction and the
   sorted-pairing identity Σ_odd(L_j) ≥ Σ_odd(L_1). Proposed to `lemmas/greedy-odd-index.md` for
   certification (shared by all approaches).
2. **Reformulation** LB = (1 + A)/2, reducing the problem to A\* = max_LB min_XY A = 1/D. Verified n=1,2.
3. **NEW tool — integral representation:** A = |{x ≥ 0 : N(x) odd}|, N(x) = #(pieces > x). This is the
   distinctive lever of this approach; also gives the exact per-cut parity-flip description (a cut with
   smaller subpiece s flips parity on two intervals of total measure 2s). Propose to
   `lemmas/alt-sum-integral.md`.
4. **A-bounds** 0 ≤ A ≤ p_1, even-run collapse, removal identity A = q_1 − A(rest). Full.
5. **Lower bound Case 1** (XY spares 2^n): A ≥ 2^{n−1} ≥ 1. Full, clean.
6. **Upper bound tight case:** XY's half-each replica forces A = 1 on the geometric config. Full.

## Still open (precise)
- **GAP AL** — lower bound Case 2 (XY cuts 2^n): prove A ≥ 1. TRUE (numerics: min A = 1 exactly, n=2,3,4).
- **GAP AU** — universal upper bound: XY forces A ≤ 1/D for any LB config. Shared with geometric-
  selfsimilar GAP U2.

## Recorded DEAD-END (save future rounds the detour)
The top/bottom decomposition A(M) = A_top + A_bot − 2B (B = measure{N_top odd ∧ N_bot odd}) does NOT
close Case 2 term-by-term: although A_bot ≥ 1 by induction, the natural sufficient inequality
**A_top ≥ 2B is FALSE** — a bounded random search gives min (A_top − 2B) ≈ −10.5 over valid Case-2
configs. The surplus of A_bot must absorb 2B *jointly*; no clean monovariant found yet. Any future
attempt using the additive split of A over the top/bottom groups should not assume A_top ≥ 2B.

## Spec concerns
- None on the answer: c(n) = 2^n/(2^{n+1}−1) reconfirmed (n=1,2 by hand; min A = 1 numerically n≤4).
- Distinctness/attainment: XY's optimal cuts are interior points distinct from LB's; the value 1/D is
  attained by an admissible placement (the geometric marks are interior and distinct). Still to be
  written formally once the bounds close, but no obstruction.
- KB has no dedicated "minimax game value" entry; Lemma G is proved from first principles (Zermelo /
  backward induction on a finite zero-sum tree). Suggest adding a KB line for future reuse.

## Recommendation
Both shared upper-bound gaps (AU here, U2 in geometric-selfsimilar) and the lower-bound Case 2 (AL/L2)
are the same across the two built approaches — this is a shared-gap plateau forming. If it persists next
round, dispatch an explorer specifically at Case 2 of the lower bound (the cleanest well-defined open
sub-target, known true and tight) and reconsider extremal-smoothing as the AU bypass.
