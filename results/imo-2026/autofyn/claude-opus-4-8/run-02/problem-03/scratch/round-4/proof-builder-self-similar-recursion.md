# Build report — self-similar-recursion (round 4)

## Verdict: SOLVED (Status flipped partial → solved)

The sole remaining GAP-L residual (tied non-degenerate minimizer) is closed. With the certified
upper bound, the whole problem is proved: `c(n) = 2^n/(2^{n+1}-1)`.

## What closed the gap (and how it differs from the outline)

The reviewer flagged three hard steps (Lemma I′ non-adjacent slides, cross-tie termination
monovariant, even-block sign check). The final argument **dissolves** the two hardest of these:

1. **No Lemma I′ needed.** `f` depends only on the *multiset* of sub-piece lengths, not their
   spatial arrangement. So the domain of a cut pattern is a plain product of simplices `∏Δ_k`, and
   any mass transfer between two sub-pieces of one piece is a legal direction. There is no
   "adjacency" constraint at all; the certified Lemma I applies to every within-piece transfer.

2. **No termination monovariant / no cross-tie walk needed.** Instead of walking a
   weakly-decreasing path (which the reviewer correctly warned can re-form ties and cycle), I use
   two static selections + a structural finish:
   - **Within-piece ties killed by P1 (Lemma W).** An equal same-piece pair is a matched pair,
     invisible to `f`. Moving it *jointly* (both up by `t`) while compensating with a third
     same-piece sub-piece (`−2t`) changes `f` only through the third sub-piece → strict descent →
     contradicts minimality, whenever `r_k≥3`. `r_k=2` equal cut = bisection, value `2^{k-1}∈ℤ`.
     This replaces the entire odd/even σ_a parity casework — no sign dichotomy is required.
   - **Cross-ties give an integer vertex (Lemmas S, T).** Choose the `Φ=Σx_i^2`-maximal global
     minimizer. Any nonzero sum-preserving component-value shift is a feasible line contradicting
     either minimality (non-flat) or Φ-maximality (flat, via strict convexity of Φ). Hence the
     piece–value-class incidence graph is a **forest** with a unique solution ⇒ all values integer
     (forest biadjacency is unimodular: a forest has ≤1 perfect matching ⇒ det ±1) ⇒ Theorem F
     (`f≡Σ=D_n≡1 mod 2`, `f≥0`) ⇒ `f≥1`.
   - **Degenerate** minimizers: cut-count strong induction (base `W_n`).

3. The even/odd block dichotomy `σ_a−σ_b∈{0,±2}` was verified symbolically for `k=2,3,4,5` (all
   ranks) as requested, but in the end is **not load-bearing** for the final proof (the P1 joint
   move sidesteps it).

## Computational checks (sympy/exact rationals)
- Tie-block sign `σ_a−σ_b`: `0` for odd `r`, `±2` for even `r`, uniform over ranks, `r=2,3,4,5`.
- Exact vertex enumeration `n=2,3`: every non-degenerate cross-tie-only vertex has a **forest**
  incidence and **integer** values; `min f = 1`. `non-forest = 0`, `non-integer = 0`.
- Allowing within-piece ties: non-integer vertices exist (values `5/3, 5/2, 7/3, …`) but **all have
  `f>1`**; every global-min vertex is integer, `min f = 1` (`n=2,3`). Matches the theory: odd
  within-piece ties (non-integer) are non-minimal (Lemma W descent); `r_k=2` bisection ties are
  integer.

## New lemmas proposed for certification (written to `results/imo-2026-03/lemmas/`)
- `within-piece-tie-p1.md` (Lemma W).
- `forest-vertex-integrality.md` (Lemmas S + T).

## Spec concerns
- None on the problem statement. One presentational note for the reviewer: the proof takes
  `\min_{\mathcal D_N} f` over the **closure** (lengths `≥0`) for Weierstrass; achievable game
  refinements (positive lengths, distinct cut points) are a subset, so a closure lower bound `≥1`
  implies the game bound. Degenerate closure points are exactly the reduced-cut-count configs the
  induction consumes. This is standard but worth a glance.
- The certified upper bound is imported, not re-derived here.

## Residual
None for this approach. The proof is complete end-to-end (both bounds).
