## Statement

With the certified closed form (route `coordinate-bash-resultant-boundary-
pointwise-tangent`)

```
D₂(A,B) := ∂RHS/∂B = -sinB·cosβ₀ - sinβ₀·∂G(β₀)/∂B,   β₀ := (π-A)/3,
```

(all constituent quantities `K_c, P, Q` and their `B`-derivatives as defined
in that file), the value at the equilateral corner `A=B=π/3` satisfies

```
D₂(π/3,π/3) ≤ -0.8 < 0.
```

(In fact `D₂(π/3,π/3) = -0.83643057088879836…`, an exact algebraic number in
`ℚ(√3, cos(5π/18), sin(5π/18))`.)

## Proof

At `A=B=π/3`, `β₀=2π/9`, and direct substitution/simplification gives the
closed form (writing `c:=cos(5π/18)=sin(2π/9)`, `s:=sin(5π/18)=cos(2π/9)`,
via the complementary-angle identity `π/2-2π/9=5π/18`):

```
D₂(π/3,π/3) = (√3/2)(c-s) - (√3/4)sc - (5/4)c².
```

**Rational bound.** Using only the classical Archimedes bound
`223/71 < π < 22/7` and the Taylor series for `sin, cos` with Lagrange
remainder (standard facts), one gets `x:=5π/18 ∈ (0.87, 0.88)`, hence (by
monotonicity of `sin,cos` on `(0,π/2)`) rational interval enclosures for
`c=cos x ∈ [0.637151143299987, 0.6448265472416286]` and
`s=sin x ∈ [0.7643289369730583, 0.7707388788990813]`. Bounding each of the
four terms of `D₂(π/3,π/3)` above individually at the box-extremizing corner
(exploiting that all of `c,s>0`) and summing the four upper bounds (own
exact `fractions.Fraction` arithmetic) gives
`D₂(π/3,π/3) ≤ -0.8218022873656784 < -0.8`.

**Independent verification (proof-reviewer, round 14).** Re-derived `D₂`
directly from the raw definitions (`X₀, K_c, P, Q, G(β₀)`, own fresh `mpmath`
session, 50-digit precision, no reuse of the file's displayed simplified
form) and confirmed `D₂(π/3,π/3) = -0.83643057088879836412724821684306…`
exactly matches (to 50 digits) both the file's closed form `(√3/2)(c-s) -
(√3/4)sc - (5/4)c²` and its stated tighter `mpmath.iv` enclosure. This
independently confirms the rational bound `≤ -0.8` is valid (indeed loose;
the true value is comfortably further from `0`). ∎

## Status

Fully proved via a self-contained, hand-checkable rational computation (no
floating point; Archimedes' `π` bound plus Taylor-with-remainder). This is
the round's highest-rigor-tier result. Independently reproduced from the raw
definitions by the proof-reviewer.

## Consequence (already drawn in the source file)

Since the route's global target `Tgt(A,B) := 4(1+cosB)²X₀D₂² - T₁'²`
satisfies `Tgt(π/3,π/3) = (9/4)D₂(π/3,π/3)²` (as `T₁'(π/3,π/3)=0` is
separately proved), this gives `Tgt(π/3,π/3) ≥ (9/4)(0.8)² = 1.44 > 0`
unconditionally.

## Origin

`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-
pointwise-tangent.md`, round 14, "New result 7".
