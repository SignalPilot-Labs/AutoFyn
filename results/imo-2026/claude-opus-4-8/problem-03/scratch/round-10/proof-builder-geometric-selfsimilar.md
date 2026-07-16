# Build report — geometric-selfsimilar (imo-2026-03, Round 10)

Status: **partial** (advanced: n = 3 upper bound now RIGOROUS in-framework).

## What was built
- **(T) at m = 4 PROVED analytically** — the four-strategy direct actual-A case split, written in full in
  the approach file (new section "R10: (T) for m = 4"). This closes the m = 4 residual gap case, and with
  the certified Cor R4.1 (m ≤ 3) + Cor AB.1 (b ≥ 4 ⇒ μ = 0) closes the **entire n = 3 upper bound**:
  val ≤ 8/15 = c(3).
- Re-derived every A-bound from scratch. The explorer's exact piece formulas were mislabeled (P/C
  effective instances are {δ, d₁−δ−d₃} and {δ, δ+d₃−d₁}; the "sum = δ" holds for the two final-cut BOUND
  terms, not the pieces). Only the bounds A_R≤d₂, A_S≤{d₃,|d₁−d₃|}, A_P≤δ/2, A_C≤δ+d₃−d₁ are load-bearing
  and were re-derived cleanly and independently.
- Wrote the gap-condition arithmetic explicitly: (1) d₁≤2δ+d₃ from p₁≤Σ/2; (2) δ+d₂+d₃<4t from p₂<τ/2;
  derived (2′) 7d₂+3d₃<δ+4d₁ line-by-line.
- Sub-case B (d₃>d₁) impossibility via the exact collision (X) 10t<δ+d₁ vs (Y) δ+d₁<2t ⇒ 8t<0.
- Sub-case A via δ<2t and P/C complementary averaging.
- Budget feasibility stated: each of R/S/P/C uses ≤3 = b cuts (2 pairing + ≤1 final); "min over
  merge-family ≤ t" justified as the existence-of-witness UB direction.
- Proposed new promotable **Lemma T4** ((T) at m=4) for certification.

## Verification (bounded, exact Fraction, budget-enforced #cuts ≤ 3)
- 0 violations / 1528 residual gap configs; worst A/t = 0.9375 at {25,17,13,9}.
- Designated per-case strategy passes every assertion; Sub-case B occurs 0 times; δ<2t holds in every
  Sub-case-A config. Runtime < 5 s.

## Honestly OPEN (recorded, not papered over)
- **m ≥ 5 (general-n upper bound):** set up as the generalized DIRECT actual-A case-split (matching
  strategies for small-difference regions + P/C-chain giving A ≤ p_m/2 with p_m < 2Σ/(2^m−1);
  generalized Sub-case-B impossibility). 0-violation at m=5 numerically, NOT proven. Explicitly forbidden
  routes listed: SB-monotone (dead, sb-obstruction), R3-cascade A≤Σ−2p₁ (refuted m≥4), complement-cut
  m=4→3→R4 (refuted).
- **Lower bound:** unchanged this round; open gap remains LL sub-case t≥2, A(Q)>0.

## Net status of the whole problem from this slug
- Answer c(n) = 2^n/(2^{n+1}−1) fully rigorous for n ≤ 2; **n = 3 upper bound now rigorous** (lower-bound
  n=3 still gated on the shared LL gap owned by the LL slugs).

## Spec concerns:
None. The reviewer-flagged typos in the explorer's A-value formulas were corrected (only bounds used);
the m≥5 gap is marked open, not overclaimed; budget and UB-direction confirmed in writing.
