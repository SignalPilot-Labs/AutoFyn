# Build report — geometric-selfsimilar (imo-2026-03), round 2

Status: **partial** (strong). Both bounds reduced to one explicit, numerically-verified lemma each.

## What is now fully proven
- **Lemma G** (greedy = odd-index sum) — complete, tie-robust. The shared lemma file
  `results/imo-2026-03/lemmas/greedy-odd-index.md` already exists with an equivalent complete proof;
  I did NOT overwrite it. My write-up gives the same proof independently. Ready to certify.
- **Lemma M0** (measure form: A(P) = measure{x : N(x) odd}) — complete. New, clean, reusable.
- **Lemma M** (merge: val(X∪Y) ≥ val(X) + Σ_even(Y)) — complete, via M0.
- **Answer** c(n) = 2^n/(2^{n+1}−1); verified n=1 (2/3), n=2 (4/7).
- **Lower bound**: base n=1 complete; **Case 1** (largest piece uncut ⇒ val ≥ 2^n) complete; n=2
  fully closed. Case 2 reduced by IH to a single crux **Lemma LL**.
- **Upper bound**: exact tight value (replica vs geometric = c(n)) computed in full for general n;
  **n=1 upper bound complete** (careful median-maximization casework, corrected sign).

## Precise remaining gaps
1. **Lemma LL** (lower bound Case 2, sub-case A(Q) > 0): val(Q∪R) ≥ 2^n where Q partitions a length-2^n
   piece into ≥2 parts (A(Q) > 0) and R is a ≤(n−t)-cut refinement of G_{n−1} with val(R) ≥ 2^{n−1}.
   Merge alone is provably insufficient (n=3: 104/398 grid configs have merge-max < 8 while true val
   ≥ 8). True numerically. Needs a sharper Q–R interaction / deeper self-similar recursion.
2. **Claim U** (general upper bound): XY concentrating all n cuts on the largest piece caps LB at
   c(n) for arbitrary configs. True numerically (n=2). Needs the inductive cap: reduce A_1<1/2 "flat"
   case + (n−1)-reduction of subpieces-of-A_1 vs A_2,…,A_m.

## Spec concerns
- The reviewer's GAP U1 reword was correct and applied: the literal "push each A_i to an even position"
  interleaving is FALSE for near-equal pieces (a subpiece of A_1 cannot exceed A_1). Upper bound is
  stated as the inductive cap (Claim U), not literal interleaving.
- **Sign correction (load-bearing):** in the n=1 upper bound, LB gets odd positions = max + min =
  sum − median, so XY MINIMIZES LB by MAXIMIZING the median. An earlier mental error (LB gets the 2nd
  piece) spuriously suggested LB@1/2 guarantees 3/4; the correct analysis gives XY holding LB@1/2 to
  1/2. Any future builder must use "LB = sum − median" for 3-piece positions.
- Distinct-points/attainment: c(n) is attained by the admissible geometric marks; XY's optimal splits
  are interior points (infima approached by admissible cuts, exactly attained at the replica). Stated.

## Recommendation to orchestrator
- LL and U are now the two shared hard sub-targets. LL is the more tractable (fully self-contained,
  scaled-copy structure). Suggest next round push a builder specifically on LL via the self-similar
  recursion (R contains a scaled G_{n−2}), and keep extremal-smoothing warm as the U-bypass.
