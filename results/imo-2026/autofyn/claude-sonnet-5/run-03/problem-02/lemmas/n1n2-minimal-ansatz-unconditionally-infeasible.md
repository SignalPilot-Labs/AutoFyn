## Statement (Theorem 3, route `coordinate-bash-resultant-boundary-pointwise-sos`)

With `u := tan(A/6)`, the certified degree-34 polynomial `Num(u,cosB,sinB)`
and the domain-defining polynomials `n₁(u,cosB,sinB)` (degree 10, coefficients
in `ℚ(√3)`), `n₂(u,cosB,sinB)` (degree 6, coefficients in `ℚ`) from Theorem 1
(`lemmas/star-weierstrass-denominators-positive.md`), at the exact rational
point

```
cosB = 808976/2721665,  sinB = 2598657/2721665   (cos²B+sin²B=1 exactly,
                                                    B = 2·arctan(1383/1879)
                                                    ≈ 1.269000132)
u = 1/4   (∈ (0, 2-√3), a legitimate value of tan(A/6) for A∈(0,π/2))
```

one has, exactly:

```
n₁(1/4, cosB, sinB) ≈ 1.2686 > 0
n₂(1/4, cosB, sinB) ≈ 0.0323 > 0   (a pure rational value, no √3)
Num(1/4, cosB, sinB) ≈ -0.00086 < 0.
```

Consequently, **no** Positivstellensatz representation
`Num = σ₀ + λ₁n₁ + λ₂n₂` with `σ₀, λ₁, λ₂` sums of squares (of any degree)
can exist: the minimal 2-generator (`n₁,n₂`-only) ansatz for a certificate
of `Num ≥ 0` is unconditionally impossible at this witness point, hence in
general.

## Proof

If such a representation existed, evaluating at `u=1/4` (with `cosB,sinB`
fixed at the stated rationals) would give `σ₀(1/4) ≥ 0` (SOS polynomials are
pointwise nonnegative on all of `ℝ`), `λ₁(1/4)·n₁(1/4) ≥ 0` (since
`n₁(1/4)>0` and `λ₁(1/4)≥0`), and likewise `λ₂(1/4)·n₂(1/4) ≥ 0`, forcing
`Num(1/4) ≥ 0` — contradicting the computed exact negative value. The three
displayed numeric values are exact algebraic numbers in `ℚ(√3)` (`Num, n₁`)
or `ℚ` (`n₂`), with signs confirmed by `sympy`'s exact algebraic-number sign
test and 50-digit numeric corroboration.

**Independent re-derivation (proof-reviewer, round 14).** Rebuilt `Num, n₁,
n₂` completely from scratch (own `sympy` session) from the *raw* trigonometric
definitions — `X₀ := sinB·cosA/(2sin(A+B))`, `RHS := (1+cosB)cosβ₀ -
sinβ₀·G(β₀)` with `β₀ = π/3 - A/3`, `K_c, P, Q` as in the source file, and the
Weierstrass substitution `u=tan(A/6)`, `cosA = 4x³-3x`, `sinA = 3y-4y³` with
`x=(1-u²)/(1+u²), y=2u/(1+u²)` — clearing denominators via `sympy.together`/
`sympy.fraction` independently reproduces the same denominator structure
(`Den = -16(u²+1)^{14}h` for the explicit `h`, matching Theorem 1) and, on
substituting the exact witness rationals above, gives

```
Num(1/4,·) ≈ -0.0008596575524743493
n₁-numerator(1/4,·) ≈ 1.2685616043314354  (n₁'s denominator also >0 there)
n₂-numerator(1/4,·) ≈ 0.03232250009949713  (n₂'s denominator also >0 there)
```

matching the file's claimed values to the precision reported. Also
independently confirmed `n₄(1/4,·) = w³cosB - u(3-u²) ≈ -0.4088 < 0` (with
`w=√(1+u²)`), i.e. this witness point genuinely lies outside the `n₄≥0`
sub-domain (Theorem 2), confirming `n₄` is a necessary fourth generator. ∎

## Status

Fully proved by exact algebraic-number computation (no floating point, no
SDP). Independently re-derived from the raw geometric/trigonometric
definitions (not from the file's displayed intermediate polynomials) by the
proof-reviewer, round 14, with an exact match. This resolves a genuine
cross-round contradiction (round 13's SDP-based infeasibility finding vs. a
round-14 explorer's SDP-based "feasible" finding at the same witness point)
decisively in round 13's favor, and upgrades round 13's numeric finding to an
unconditional theorem.

## Scope / non-result

This does **not** close the route's central open gap (`Num ≥ 0` on Case (b)'s
true domain, equivalently `(⋆)`) — it only rules out one specific (minimal,
2-generator) certificate shape. A valid certificate, if one exists, must use
at least a 4-generator ansatz including `n₄` (Theorem 2's `∠B≤∠C` encoding)
— not yet attempted.

## Origin

`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-
pointwise-sos.md`, round 14, "Theorem 3".
