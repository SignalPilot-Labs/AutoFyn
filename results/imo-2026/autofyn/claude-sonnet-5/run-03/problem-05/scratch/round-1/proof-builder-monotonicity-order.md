# Build report — monotonicity-order, imo-2026-05, round 1 (final)

## Outcome: SOLVED

Started from the outline-reviewer's CHANGES REQUESTED (the LEFT-inequality-only 2-point
monotonicity mechanism was refuted by a concrete numerical counterexample). Replaced it with:

1. Four exact algebraic tools A, B, C, D derived from RIGHT/LEFT at (f(y),x) and (f(x),y) via the
   functional equation f(f(y))=2f(y)-y. All verified by full symbolic expansion (sympy).
2. **Lemma 1**: any two positive values of g(y):=f(y)-y coincide — full rigorous proof via an
   explicit escaping double-orbit construction (two APs with different positive common
   differences, paired via a smallest-crossing-index argument, giving a bounded-LHS-vs-diverging-
   RHS contradiction in Tool A).
3. **The final closing step** (this is what flipped the approach from `partial` to `solved`):
   ruled out the "mixed case" (a fixed point of f coexisting with a point of positive g) via an
   infimum/supremum limiting argument applied to Tool C. Key insight: since g only takes two
   values globally (0 or c, by Lemma 1), the open interval between a fixed point x0 and the
   infimum m of the positive-g points above it is forced entirely into the zero-set of g; then a
   sequence of zero-points approaching m, paired against a sequence of positive-g points also
   approaching m, drives the LHS of Tool C to 0 while the RHS tends to a fixed positive constant
   2c(2m+c) — a clean, rigorous contradiction (explicit epsilon-K argument given). Handled the
   symmetric "positive-g points below x0" case via the analogous supremum construction.

This closes exactly the gap that all four round-1 approaches for this problem were converging on
(promoting "g constant per orbit" to "g globally constant"), so Part 4 of the proof is directly
reusable by the other approaches if they've independently established the shared base layer +
Tool A/C + Lemma 1.

## Final answer
f(x) = x + c for arbitrary constant c >= 0. Verified: both original inequalities reduce exactly
to the identity (x-y-c)^2 >= 0 for this family (sufficiency, Part 1), and necessity is proved in
full in Parts 2-4.

## File
/home/agentuser/repo/results/imo-2026-05/approaches/monotonicity-order.md (Status: solved)

Promotable lemmas proposed: base layer (FE/injectivity/orbit structure), Tools A & C, Lemma 1
(positive g-values coincide), and the mixed-case-exclusion theorem (Part 4) — the last of these is
the key result that completes the whole problem and should be certified for reuse by the other
approaches.
