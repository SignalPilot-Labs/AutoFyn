# Lemma: Goal reduction (equivalent restatements of OM=ON)

**Certified** (proof-reviewer, round 1). Independently verified.

Let `ABC` be a triangle, `M,N` the midpoints of `AB,AC`, and `O` the circumcentre of
`⊙AKL` (any circle through `A`), with circumradius `R`. Then the following are equivalent:

1. `OM = ON`.
2. `pow_M(⊙AKL) = pow_N(⊙AKL)`  (equal powers of the two midpoints).
3. `AO · BC = ¼(AC² − AB²)`  (vectors from `A`; `·` is the dot product).
4. In coordinates `B=(0,0), C=(a,0), A=(p,q)`:  `O_x = (2p+a)/4`.

**Proof.**
(1⇔2) Since `A∈⊙AKL`, `|OA|=R`, so `pow_X = |OX|²−R²` gives
`pow_M−pow_N = |OM|²−|ON|²`. As `|OM|,|ON|≥0`, `OM=ON ⇔ |OM|²=|ON|² ⇔ pow_M=pow_N`.
No case split on the sign of the power is needed (the `|OX|²−R²` form absorbs it).

(2⇔3) With `A` as origin, `AM=½AB`, `AN=½AC`, and `|OA|=R`:
`pow_M = |AO−AM|²−|AO|² = −2AO·AM+|AM|² = −AO·AB+¼AB²`, similarly
`pow_N = −AO·AC+¼AC²`. Subtracting, `pow_M−pow_N = AO·(AC−AB)+¼(AB²−AC²)
= AO·BC+¼(AB²−AC²)`. Setting this to zero gives `AO·BC = ¼(AC²−AB²)`.

(1⇔4) `M=(p/2,q/2)`, `N=((p+a)/2,q/2)` share the height `q/2`, so
`OM²−ON² = (O_x−p/2)²−(O_x−(p+a)/2)² = (a/2)(2O_x−(2p+a)/2)`. Since `a>0`,
`OM=ON ⇔ O_x=(2p+a)/4`. (Equivalently `O` lies on the vertical perp-bisector of the
horizontal segment `MN`.)

All identities are pure vector/coordinate algebra; they use no property of `K,L`.
</content>
