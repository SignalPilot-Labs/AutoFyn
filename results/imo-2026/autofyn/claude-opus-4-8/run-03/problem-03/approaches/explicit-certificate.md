## Status
unsolved

## Approaches tried
(fresh approach, round 1)

## Current best
Nothing proven yet. This file lays out a complete attempt via explicit constructions and
order-statistics inequalities (no induction on n, no abstract potential).

---

# Approach: explicit two-sided certificate (order-statistics / interleaving)

**Top-level target.** c(n) = 2^n/(2^{n+1} − 1), both bounds.

**Distinct route.** Give an EXPLICIT optimal object on each side and a direct inequality,
avoiding both the induction-on-n recursion and the abstract S-potential. Lower bound:
LB's dyadic marking + a fixed interleaving lemma forcing each small original piece to an
even rank. Upper bound: XY's explicit "split the largest LB piece into n+1 interleaving
sub-pieces" response + a counting/majorization inequality. Both bounds are certificates
checkable without recursion.

## Shared foundations (import as certified lemmas)

- **L0 (Claiming lemma)** and **L1 (Order irrelevance)** — reduce to the multiset game
  (LB picks multiset of ≤ n+1 parts summing to 1; XY refines with ≤ n cuts; value =
  odd-rank sum). GAP: L0 exchange argument.

## Notation

D_n = 2^{n+1}−1. Dyadic parts g_j = 2^j/D_n, j = 0..n. g_n = 2^n/D_n = c(n) is the
unique largest; the n smaller parts are g_0 < g_1 < … < g_{n−1}.

## Skeleton

1. Reduce to the multiset game (L0, L1).
2. **Lower bound (LB dyadic, direct).** LB plays {g_0,…,g_n}. Show every XY refinement
   has odd-rank sum ≥ g_n = 2^n/D_n. Direct mechanism (Lemma E): whatever XY does, the n
   small parts g_0,…,g_{n−1} can be injected into DISTINCT even ranks of the final sorted
   list, so LB (odd ranks) is left with at least the complement, whose total ≥ g_n. — by
   an explicit rank-injection / Hall-type argument (KEY GAP).
3. **Upper bound (XY explicit response, direct).** For ANY LB partition a_1 ≥ … ≥ a_k,
   XY responds by splitting the largest part(s) into interleaving sub-pieces so that the
   n smaller-side pieces occupy the n even ranks and LB's odd-rank sum ≤ 2^n/D_n. Give
   the explicit split positions and a majorization inequality bounding the odd-rank sum
   by the dyadic value. — by explicit construction + order-statistics inequality
   (KEY GAP, Lemma F).
4. Conclude c(n) = 2^n/(2^{n+1}−1); verify n=1,2,3 explicitly (2/3, 4/7, 8/15).

## Key lemmas (claim + mechanism)

- **Lemma E (lower-bound interleaving / injection).** With LB = dyadic, for every XY
  refinement there is an injection from the n small parts {g_0,…,g_{n−1}} into the even
  ranks {2,4,…} of the final sorted multiset with each g_j landing at or above a distinct
  even-rank slot. Consequence: XY's total (even-rank sum) ≤ g_0+…+g_{n−1} = (2^n−1)/D_n,
  so LB ≥ g_n = 2^n/D_n. Mechanism: superincreasing spacing 2^j means that between
  consecutive dyadic thresholds there is room for exactly one XY-created sub-piece, and a
  Hall/marriage condition on "how many final pieces exceed g_j" is satisfied because XY's
  ≤ n cuts create ≤ n extra pieces; verify the Hall inequality |{pieces ≥ g_j}| ≤
  (number of odd ranks available above rank of g_j) for each j. WITNESS n=2: parts
  {4,2,1}/7; any XY split of the 4/7 into 3 sub-pieces has 2/7 at rank 2 and 1/7 at rank
  4, LB banks the 3 sub-pieces = 4/7 exactly (invariance observed numerically).
- **Lemma F (upper-bound explicit XY response + majorization).** For any LB partition,
  XY concentrates cuts on the largest part(s) (never spread across small parts — proven
  suboptimal for XY, "concentrate don't spread"), splitting a_1 (and ties) into sub-pieces
  chosen so that a_2,…,a_{k} land at even ranks and the odd-rank sum is a Schur-convex
  functional maximized (over LB choices) at the geometric profile, value 2^n/D_n.
  Mechanism: given the even ranks are "filled" by the smaller original pieces, the
  odd-rank sum = a_1 − Σ(threshold gaps); optimize the gaps via the majorization/
  rearrangement inequality; the constraint "≤ n cuts, ≤ n+1 parts" caps the number of
  even slots at n, forcing residue ≥ … ≤ 2^n/D_n with equality at dyadic. Reuse the
  "bisect when the top part exceeds the rest" branch to cover partitions with one huge
  part (cheap-kill {a_1 ≈ 1}: bisect repeatedly ⇒ LB ≈ 1/2 < 2^n/D_n).

## Open gaps (builder fills)

- L0 exchange argument.
- Lemma E: state and verify the Hall/marriage inequality that guarantees the injection
  of small parts into even ranks for EVERY XY refinement (not just the concentrated one).
  Prove XY cutting small parts, or slivering, cannot break it.
- Lemma F: (a) prove "concentrate cuts on the largest, don't spread" is optimal for XY
  (interchange/majorization); (b) give the explicit split of a_1 realizing the even-rank
  filling for an ARBITRARY partition; (c) the majorization inequality capping odd-rank
  sum at 2^n/D_n. Hardest gap.

## Cases to cover

- Lower: XY cuts concentrated on g_n / spread / cutting small parts / slivers / fewer
  than n cuts. Upper: LB partitions with a dominant part (bisect branch), with ties
  (cancel branch), with < n+1 parts, and the balanced/geometric near-optimal ones
  (match branch).

## Watch out for

- The "invariance" (any split of the top piece gives the same LB total) holds ONLY while
  the sub-pieces interleave correctly with the small parts; the interleaving CONDITIONS
  must be shown forced, not assumed. This is Lemma E's real content.
- "Concentrate don't spread" for XY is numerically observed, NOT yet proven — Lemma F(a)
  is a genuine obligation, not a given.
- Slivers sort to the GLOBAL bottom; they cannot locally flip parity of a suffix. Any
  rank-injection argument must be robust to XY inserting near-zero pieces.
- Majorization/Schur-convexity claims need the functional written explicitly and its
  monotonicity proven — no hand-waving "by symmetry".
