# Outline Review — imo-2026-03 (IMO 2026 P3)

Answer under review: **c(n) = 2^n / (2^{n+1} − 1)**. Confirmed independently here: exact-Fraction
maximin over an M=14 grid at n=2 gives 4/7 = c(2); c(1)=2/3, c(3)=8/15 match. Answer is correct.

## Shared foundation — Lemma G (greedy optimality): SOUND, lock it first
- Verified computationally: greedy (take-largest) == brute-force minimax on 200 random multisets.
- The crux "sorted-pairing identity" Σ_odd(L_j) ≥ Σ_odd(L_1) holds on 500 random sorted lists.
  I re-derived it by hand: Σ_odd(L_j) − Σ_odd(L_1) = Σ_{i<j}(−1)^{i+1}p_i − [p_j if j even],
  which is a sum of consecutive nonneg differences (p_{2t−1}−p_{2t} ≥ 0, plus p_{j−1}−p_j ≥ 0 when
  j even) — hence ≥ 0. The file's derivation is loose in wording but the mechanism is correct and
  the induction (zero-sum ⇒ minimax; mover's total = T − Σ_odd(L_j); minimize over j) is valid, not
  circular. **This is the one step every approach depends on; certify it to `lemmas/` first.**

## geometric-selfsimilar — CHANGES REQUESTED (strongest; BUILD)
Technique right. Lower bound (Lemma G + induction on the ratio-2 geometric structure; base n=1 done,
Case 1 = dominance, Case 2 = self-similar recursion **GAP L2**) is the accessible, well-supported
direction.

Upper-bound check (the reason to build this over the others): I tested XY's "concentrate all cuts on
the largest piece" strategy directly.
- First pass on a coarse grid (M=12) it *appeared to fail* (LB got 7/12 > 4/7 on configs like
  pieces {3/4, 1/6, 1/12}). **This was a grid artifact** — the coarse grid had no admissible cut
  point where XY needs it.
- With a fine XY grid (Mxy=60–140), XY cutting **only inside the largest piece** holds *every* n=2
  LB config to ≤ c(2) — worst observed LB share 0.501 ≪ 4/7. So concentrate-on-largest is a
  genuinely valid XY strategy, not a dead end.

Fixes for the builder:
1. **Re-word GAP U1.** The outline says XY "splits A_1 to push each A_i to an even position." That
   literal interleaving mechanism only works for the geometric config and breaks when pieces are
   near-equal (a subpiece of A_1 cannot exceed A_1). The true mechanism is: XY cuts optimally *inside
   A_1*, and the bound is proved by the self-similar induction — do NOT sell U1 as a universal
   "make each A_i even by an oversized partner" claim; state it as the inductive cap (GAP U2).
2. Prove GAP U2 (the general (n−1)-cap after splitting A_1) as the load-bearing upper-bound step; the
   numeric evidence says the target is true, so effort here is well-spent.
3. Distinct-points / attainment: state the value c(n) is attained by an admissible placement and that
   XY's optimal cut is an interior point (infimum attained in the closed config); flagged already.
4. Sequence: certify Lemma G → close the lower bound (L2) → then the upper bound (U2).

## alternating-sum-value — CHANGES REQUESTED (BUILD)
The reformulation LB = (1+A)/2 with A = p_1−p_2+p_3−… is exact (Σ_odd−Σ_even = A, Σ_odd+Σ_even = 1)
and gives a clean lens; the A-bounds (0 ≤ A ≤ p_1, even-run collapse) are correct. This is a
genuinely distinct route from geometric-selfsimilar (same lower-bound construction, different
upper-bound machinery + different target framing), not a split of one proof.

Fixes:
1. **GAP AU is under-specified.** "XY equalization drives A ≤ 1/D" needs the actual monovariant: the
   outline itself flags that per-cut A-drop is NOT uniform (one cut can drop A a lot), so a simple
   "Φ=A decreases by a bounded amount per cut" argument will not close. The builder must state the
   concrete equalization move (which piece is partnered with which) and the exact potential decrease,
   not "a controlled amount." Until that mechanism is written, AU is a bare label.
2. A ≤ p_1 is weak (flagged) — the real engine is cancellation via equal runs; keep that front-and-center.
3. Same Lemma G + lower-bound (GAP AL) foundation — import the certified Lemma G rather than re-prove.

## extremal-smoothing — CHANGES REQUESTED (KEEP LIVE, do NOT build this round)
Legitimate as bypass insurance: derives the geometric config as an extremal *conclusion*, needing
only ONE explicit XY response (against the geometric config) rather than a universal strategy. Not
circular. But the load-bearing **GAP S1 (smoothing monotonicity)** is the riskiest claim in the field:
- The maximizer is provably **not unique** (grid found {1/14, 3/14} also = 4/7), so any "strict
  improvement unless geometric" phrasing is false — the outline half-acknowledges this; it must be
  fully dropped, leaving only "weakly increasing V toward geometric," which is unproven and could
  fail if V is not monotone toward the geometric ridge.
- Before committing effort, the builder must first **numerically verify the perturbation sign** on a
  handful of explicit non-geometric spectra (bounded computation). Only build if the two shared
  upper-bound gaps (U2, AU) stall across rounds.

## Ranking (updated head-to-head this round)
- geometric-selfsimilar 1532.0 — most concrete; its upper-bound XY strategy (concentrate-on-largest)
  is directly verified valid at n=2 here. Beats both siblings.
- alternating-sum-value 1499.3 — clean distinct reframe; upper-bound mechanism (AU) less pinned down.
  Beats extremal-smoothing.
- extremal-smoothing 1468.7 — viable bypass but S1 is a bet with a known non-uniqueness hazard.

No new slugs to register (all three already in the population); no copies needed.

build set: geometric-selfsimilar, alternating-sum-value
