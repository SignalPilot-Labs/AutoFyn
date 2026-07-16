# Build report — geometric-selfsimilar (Round 9)

**Status: partial.** Target was the whole remaining upper bound (m ≥ 4 gap case). I could not close it,
but I substantially narrowed it and proved one clean new lemma. Honest partial, no overclaim.

## SPEC CONCERNS (outline was overstated on two counts)

1. **The "complement cut" is illusory for a single cut.** The outline's central premise — cut `p₁` at
   `p₁ − pⱼ` (NOT `pⱼ`) to avoid a "triple `pⱼ`, odd parity" — is **false**. Cutting `p₁` at offset `pⱼ`
   and at offset `p₁ − pⱼ` produce the *identical* fragment pair `{pⱼ, p₁ − pⱼ}`, hence the identical
   sub-instance and identical A. Cutting at `pⱼ` makes **two** copies of `pⱼ` (a pair), not three. This is
   just Lemma R3. There is no single-cut parity distinction; the R8 refutation was of a *multi-cut
   cascade*.
2. **The outline's one-cut mechanism is insufficient (numerically REFUTED).** "One cut reduces m=4→m=3,
   closed by R4 (one cut on sub)" gives value `|2 max(sub) − Σ'|`, which **violates the target on 141/367**
   budget-enforced m=4 gap configs at b=3 (worst ratio 2.5, near-equal configs). The sub must be solved
   with its FULL budget `b−1`, not a single R4 cut. So the outline's step-4 sub-case algebra
   (`p₄ < Σ/(2D_b)` etc.) is attacking the wrong (too-weak) strategy.

## What I proved / established (in the approach file, section "R9")

- **Lemma AB (abundant budget), FULLY PROVED + promoted:** `μ(X, b) = 0` whenever `b ≥ |X|`. Pairing
  reduction to a single piece (|X|−1 cuts) then one halving cut. Verified 0/3000.
- **Corollary AB.1:** under the budget invariant `|X| ≤ b+1`, the m ≥ 4 residual gap case is nontrivial
  ONLY at the **tight budget `b = m − 1`**. All looser budgets give `μ = 0`. (Verified: m=4 at b≥4 → μ=0.)
  This is a real narrowing of the R8 frontier ("m≥4, all b≥3") to a single pinned budget.
- **Tight-case collapse:** with `b = m−1`, XY reduces X to ≤ 2 effective pieces by m−2 pairing cuts, then
  one final cut, achieving `A ≤ min(u−v, v)`. The reachable outcomes are an explicit finite merge-family.
  The whole m≥4 upper bound reduces to one **finite algebraic inequality (T)**: min over the merge-family
  ≤ Σ/(2^m − 1). Verified (T) on **0/9646** budget-enforced exact-Fraction m=4 gap configs (worst ratio
  0.9494). A clean 5-strategy closed-form sub-family covers 99.6% (312/81866 miss).

## The remaining gap (honest)

The closed-form analytic proof of the finite inequality (T) for the tight case `b = m−1`. It is now a
bounded, explicit algebraic min-inequality (no lookahead search, no unknown potential, budget pinned).
The essential subtlety: the pure balanced-partition bound `δ*` alone fails (42822/61517); the smaller-
effective-piece ("v") branch is indispensable and interleaves with the difference branch
configuration-dependently, which is why the 5-strategy family misses a few percent. A complete proof needs
either the right closed-form min over the full merge-family, or a slicker balanced-reduction argument.

## Files
- Approach: `/home/agentuser/repo/results/imo-2026-03/approaches/geometric-selfsimilar.md` (section R9).
- Promotable: Lemma AB (proposed `results/imo-2026-03/lemmas/abundant-budget.md`).
- Numerics (bounded, exact, budget-enforced): `/tmp/explore1..7.py`, `/tmp/verify_zero.py`.

## Recommendation to orchestrator
Route: **CHANGES REQUESTED** (real progress, gap remains). Next round: put an explorer on the tight-case
finite inequality (T) for m=4 specifically — it is a concrete 4-variable algebraic problem now, the most
tractable it has ever been. The abundant-budget lemma should be certified and imported by any approach.
