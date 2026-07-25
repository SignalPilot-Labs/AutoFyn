## Statement

Work in `R := ℝ[c,s,d,t]/⟨c²+s²-1, d²+t²-1⟩` (`c=cos A, s=sin A, d=cos B,
t=sin B`), graded by the `ℤ₂×ℤ₂` grading `deg₂(monomial) := (deg_c mod 2,
deg_d mod 2)` (this grading descends to `R` since both ideal generators are
even in `c` and in `d`). Let `σ:=s², τ:=t²`, and recall the already-certified
generators

- `G₀ := ct(1-2d²) - 2sd³`
- `E_num := ct·f₁(σ,τ) + ds·f₂(σ,τ)`, with `f₁ = -32σ²τ+24σ²+22στ-12σ-τ`,
  `f₂ = -32σ²τ+8σ²+38στ-8σ-6τ`
- `Num := c⁵t³ - 3c³d²s²t - c³s²t³ + 2c²d³s³ - 6c²ds³t² - 9cd²s⁴t`
  (round-13's authoritative, "as displayed" formula)

Then the `(0,0)`-graded components of the six degree-matched products
`{ct·G₀, sd·G₀, ct·(-E_num), sd·(-E_num), ct·(-Num), sd·(-Num)}` are exactly

```
B₁ := (ct·G₀)_{00}          = τ(1-σ)(2τ-1)
B₂ := (sd·G₀)_{00}          = -2σ(τ-1)²
B₃ := (ct·(-E_num))_{00}    = -τ(σ-1)(32σ²τ-24σ²-22στ+12σ+τ)
B₄ := (sd·(-E_num))_{00}    = -2σ(σ-1)(τ-1)(16στ-4σ-3τ)
B₅ := (ct·(-Num))_{00}      = τ(σ-1)(8σ²τ-6σ²-3σ+τ)
B₆ := (sd·(-Num))_{00}      = 2σ²(σ-1)(τ-1)(4τ-1)
```

In particular `B₆ = 2σ²(σ-1)(τ-1)(4τ-1)` — this **corrects** an earlier
(round-14 explorer) claim of `B₆ = 2σ²(σ-1)(τ-1)(2τ-1)(2τ+1)`, which differs
from the true value by the nonzero residual `-8σ²τ(σ-1)(τ-1)² ≠ 0`.

## Proof

Direct symbolic computation: reduce each raw product modulo the ideal
`⟨c²+s²-1, d²+t²-1⟩` (via `sympy.reduced`), then project onto the `(0,0)`
graded piece via the averaging projector
`f_{00} = 1/4·(f(c,s,d,t) + f(-c,s,d,t) + f(c,s,-d,t) + f(-c,s,-d,t))`,
then rewrite the resulting polynomial (now even in both `s` and `t`) in
terms of `σ=s², τ=t²`. Each of the six computations was independently
re-derived from scratch (proof-reviewer, round 14, own `sympy` session) and
matches the displayed closed forms with zero symbolic residual (`sympy.expand`
of the difference is identically `0` in all six cases). ∎

## Status

Fully proved, zero-residual, independently re-verified by the proof-reviewer
from the raw definitions (own `sympy` session, round 14). Reusable by any
future Positivstellensatz search for `-q₁, -r₀`, or for other `Num`-based
targets elsewhere in the population.

## Caveat / non-result

This lemma only records the *basis identities*, not a certificate. Round 14
also attempted, and found infeasible, the smallest natural exact linear
ansatz `-q₁ = Σ λ σ^aτ^b B_i` for `i∈{1,4,6}` (the three individually
sign-definite basis elements on the loose domain) with degree-matched
monomial multipliers — `sympy.linsolve` on the resulting 12-monomial exact
linear system returns the empty set (independently reconfirmed by the
proof-reviewer). This is an honest negative result for that specific small
ansatz, not a proof that no larger certificate exists.

## Origin

`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`,
round 14 section.
