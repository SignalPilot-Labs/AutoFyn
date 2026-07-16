# Lemma T4 — the tight-case inequality (T) at m = 4 (n = 3 upper-bound crux)

**Status:** certified (proof-reviewer, round 10). Analytic case split re-derived from scratch by the
reviewer; independent true-game search (structured half-integer 3-cut optimum) gives 0 violations of
`μ(X,3) ≤ Σ/15` over the integer gap region (worst ratio 0.88).

## Statement
Let `X = {p₁ > p₂ > p₃ > p₄ > 0}` be four **distinct** pieces, `Σ = p₁+p₂+p₃+p₄`, XY budget `b = 3`,
`D₃ = 2⁴−1 = 15`, `t := Σ/D₃ = Σ/15`. Assume the residual gap hypotheses
- **(1)** `p₁ ≤ Σ/2`  (complement `p₁ > Σ/2` handled by certified Case A.A, `gap-caseAA-subtract-chain.md`);
- **(2)** `p₂ < τ/2 = 4Σ/15`.

Then Xiang Yu has a legal `≤ 3`-cut strategy forcing the final alternating sum
`A ≤ t = Σ/15`, i.e. `μ(X,3) ≤ Σ/15`.

## Notation
`d₁ = p₁−p₂`, `d₂ = p₂−p₃`, `d₃ = p₃−p₄`, `δ = p₄`; `Σ = 4δ + d₁ + 2d₂ + 3d₃`.
Reversible translations: (1) ⟺ `d₁ ≤ 2δ+d₃`; (2) ⟺ `δ+d₂+d₃ < 4Σ/15`, and (multiplying by 15)
`7d₂ + 3d₃ < δ + 4d₁` (2′).

## Strategies (each: two pairing cuts by Lemma R1 `sum-bound-reductions.md`, reaching two effective
pieces `{u,v}`; the third cut halves the larger, so `A ≤ min(u−v, v)`, all `≤ 3` legal interior cuts)
- **R** (`{p₁,p₄},{p₂,p₃}`): effective `{d₁+d₂+d₃, d₂}` ⟹ `A_R ≤ d₂`.
- **S** (`{p₁,p₂},{p₃,p₄}`): effective `{d₁, d₃}` ⟹ `A_S ≤ |d₁−d₃|` and `A_S ≤ d₃`.
- **P** (`d₁ ≥ δ+d₃`): effective `{δ, d₁−δ−d₃}`, the two summing to `δ` ⟹ `A_P ≤ δ/2`.
- **C** (`d₁ ≤ δ+d₃`, `d₁ > d₃`): effective `{δ, δ+d₃−d₁}` ⟹ `A_C ≤ δ+d₃−d₁`.

## Case split (target `A ≤ t`)
- **Case 1** `d₂ ≤ t`: R gives `A_R ≤ d₂ ≤ t`. ✓
- **Case 2** `d₃ ≤ t`: S gives `A_S ≤ d₃ ≤ t`. ✓
- **Case 3** `|d₁−d₃| ≤ t`: S gives `A_S ≤ |d₁−d₃| ≤ t`. ✓
- **Case 4** (complement: `d₂>t`, `d₃>t`, `|d₁−d₃|>t`) — exhaustive with 1–3.
  - **Sub-case B (`d₃>d₁`) is vacuous.** From (2′): `10t+3d₁ < δ+4d₁ ⟹ 10t < δ+d₁` (X); from (2):
    `δ+d₁+2t < 4t ⟹ δ+d₁ < 2t` (Y). Chaining `10t < δ+d₁ < 2t` gives `8t < 0`, contradiction.
  - **Sub-case A (`d₁>d₃`, `d₁−d₃>t`).** From (2), `δ < 4t−d₂−d₃ < 2t` (Z). Exactly one of P, C applies:
    P ⟹ `A_P ≤ δ/2 < t` (by Z); C ⟹ `A_C ≤ δ+d₃−d₁ = δ−(d₁−d₃) < 2t−t = t` (by Z and `d₁−d₃>t`). ✓

Hence `μ(X,3) ≤ Σ/15` for every residual gap-case `X` with `m = 4`. ∎

## Consequence
With Corollary R4.1 (`m ≤ 3`, `gap-case-m3-closure.md`), Corollary AB.1 (`m=4, b≥4 ⟹ μ=0`,
`abundant-budget.md`), Case A.A (`p₁ > Σ/2`), and the certified R1/R2/R3 reduction, **the entire n = 3
upper bound is rigorous**: `A(final) ≤ 1/15`, so `val ≤ (1+1/15)/2 = 8/15 = c(3)`.

## Scope
`m = 4` (n = 3) only. The `m ≥ 5` generalization is NOT proven (open). This lemma does NOT close the
n = 3 lower bound, which remains gated on the shared LL gap.
