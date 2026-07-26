# Lemma: Local-kink for level-1 perturbations (n=3, reals, asymmetric slopes)

**Status:** CERTIFIED (round 5, proof-reviewer). Proved in `approaches/dyadic-halving-induction.md` §3. Reviewer re-derived both explicit 2-mark strategies and the cap formulas `A·15 = 1 − e` (mass-up) and `A·15 = 1 + 2e` (mass-down) with exact-rational python.

## Statement

Consider the config `P_e = (8 + e, 4 − e, 2, 1)/15` (pieces in `1/15` units, sorted desc; `e ∈ (−1/2, 1/2) \ {0}` so all pieces positive and the sort is valid). This perturbs **only level 1** of the halving-defect (`p_1 = 8 + e ≠ 2(4 − e) = 8 − 2e`; levels 2, 3 remain exact: `p_3 = 2 = 2·1 = 2 p_4`; `Φ(P_e) = 3|e| > 0`). Then Xiang with **2 marks** has a strategy forcing `A < α(3) = 1/15` strictly, with:

- **(mass-up, `e > 0`)** `A · 15 ≤ 1 − e` (slope 1);
- **(mass-down, `e < 0`)** `A · 15 ≤ 1 + 2e = 1 − 2|e|` (slope 2).

In both cases `A < 1/15 = α(3)` strictly for `e ≠ 0`.

## Proof (explicit 2-mark strategies, all lengths in `1/15` units)

**(mass-up, `e > 0`):**
- Mark 1 at the midpoint of piece 1: splits `(8 + e)` into the equal pair `(4 + e/2, 4 + e/2)`.
- Mark 2 at distance `3/2` from the start of piece 2: splits `(4 − e)` into `(3/2, 5/2 − e)`.

Final multiset: `{4 + e/2, 4 + e/2, 5/2 − e, 3/2, 2, 1}`. For `e ∈ (0, 1/2)`: `4 + e/2 > 5/2 − e` and `5/2 − e > 2 > 3/2 > 1`, so sorted desc `4 + e/2, 4 + e/2, 5/2 − e, 2, 3/2, 1`. The equal pair cancels (ranks 1, 2). Then
```
A · 15 = (5/2 − e) − 2 + 3/2 − 1 = (1/2 − e) + 1/2 = 1 − e.
```
For `e > 0`: `1 − e < 1 = α(3)·15`. Strict. ✓

**(mass-down, `e < 0`):**
- Marks 1, 2 at the dyadic positions `1` and `3` (both interior to the enlarged piece 1, which spans `[0, 8 + e]` with `8 + e > 8 > 3` for `e > −1/2`). These split piece 1 `(8 + e)` into `(1, 2, 5 + e)`. Pieces 2, 3, 4 untouched: `(4 − e, 2, 1)`.

Final multiset: `{5 + e, 4 − e, 2, 2, 1, 1}`. For `e ∈ (−1/2, 0)`: `5 + e > 4 − e` (since `1 + 2e > 0 ⟺ e > −1/2`) and `4 − e > 2 > 1`, so sorted desc `5 + e, 4 − e, 2, 2, 1, 1`. Equal pairs `(2, 2)` (ranks 3, 4) and `(1, 1)` (ranks 5, 6) each cancel. Then
```
A · 15 = (5 + e) − (4 − e) = 1 + 2e.
```
For `e < 0`: `1 + 2e = 1 − 2|e| < 1`. Strict. ✓

In both cases `A < α(3)` strictly for `e ≠ 0`, with asymmetric slopes (1 for mass-up, 2 for mass-down). ∎

## Reusability

The asymmetric slope (1 vs 2) is the 2-adic signature of the dyadic kink: moving mass UP to the largest piece increases the level-1 defect by `3e` but the sliver absorbs only `e` of it (slope 1); moving mass DOWN lets the dyadic-position marks absorb `2|e|` (slope 2). The factor-of-2 asymmetry is the same `+1` vs `+2` multiplicity signature as the certified dyadic-ratio overshoot lemma. A genuine real-valued (not grid-only) strict-decrease result for the near-dyadic, level-1-perturbation structural class.

## Scope

- **`n = 3` only**, and **level-1 perturbations only** (the shallowest halving level broken; deeper levels exact).
- Does NOT cover deeper perturbations (level-2 break, multi-level breaks), far-from-dyadic configs, or general `n`.
- Does NOT prove the strict-decrease conjecture `Φ > 0 ⟹ cap < α(n)` (that conjecture is FALSE — see `lemma-ridge-falsification.md`). The local-kink is the LOCAL half of the (U-E) statement: the dyadic is a strict local max in the level-1 direction only, NOT an isolated strict global max.
- A harvestable PARTIAL lemma; NOT a regime-N proof.
