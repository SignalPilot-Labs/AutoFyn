# Lemma T1: Angle-matching on a ray reduces to a degree-≤2 polynomial

**Certified round 3** (proof-reviewer independently re-implemented the
construction from scratch and confirmed the resulting quadratic's roots
match the true geometric root of F2=0 in 4 independently-chosen
configurations, including a near-degenerate one).

**Source:** `approaches/trig-ceva-chase.md`, round 3.

## Statement

Let `V0` be a point, `u` a fixed unit vector, `P(r):=V0+r·u` a point tracing
a fixed ray. Let `V1≠V0, V2≠V0` be fixed points and `w1, w2` fixed nonzero
vectors. Define `Cross_i(r):=cross(w_i, P(r)−V_i)`, `Dot_i(r):=dot(w_i,
P(r)−V_i)` (`cross((x1,y1),(x2,y2)):=x1y2−x2y1`). Then `Cross_i, Dot_i` are
affine (degree ≤1) in `r`, and
```
Q(r) := Cross_1(r)·Dot_2(r) − Cross_2(r)·Dot_1(r)
```
is a polynomial of degree ≤2 in `r`. Writing `φ_i(r)` for the signed angle
from `w_i` to `P(r)−V_i`,
```
Q(r) = |w1||w2|·|P(r)−V1|·|P(r)−V2|·sin(φ_1(r)−φ_2(r)),
```
so `Q(r)=0` (all vectors nonzero) `⟺ φ_1(r) ≡ φ_2(r) (mod π)`.

## Proof

`P(r)−V_i = r·u + (V0−V_i)`; cross/dot are bilinear, giving the stated
affine forms with coefficients built from `w_i, u, V0, V_i`. `Q(r)` is then
a difference of two products of affine functions of `r`, hence degree ≤2.
The trigonometric identity follows from `dot(w,v)=|w||v|cosφ`,
`cross(w,v)=|w||v|sinφ` and the sine subtraction formula.

## Reviewer verification

Independently reimplemented the construction (§2 of trig-ceva-chase) for
the `F2(θ,r1)` application (`V0=B, u=u_1(θ)`, hinge 1 = `(M, B−M)`, hinge 2
= `(C, u_2(θ))`), fitting the quadratic from three sampled values of `Q(r)`
(confirming the degree-≤2 claim empirically, not just algebraically) and
solving for its roots, in 5 configurations (including
`(p,q)=(0.0025,5.0)`, θ=60°, the same shape that broke round 2's
`coordinate-trig-bash` monotonicity claim). In every case the smaller root
of the reconstructed quadratic matched (to 8+ significant figures) the true
root of `F2(θ,r1)=0` found by direct bisection on the unsigned `arccos`
angle definitions.

## Caveat (NOT part of the certified content — do not promote further)

`Q(r)=0` only pins the angle equality modulo `π` (i.e. up to a `±` branch
and modulo a possible supplement). Which root of the resulting quadratic
corresponds to the actual **geometric** (unsigned) angle-matching condition
required by the problem's hypotheses is verified only numerically (8 test
instances across both applications in `trig-ceva-chase.md`), not derived
synthetically from the containment/orientation hypotheses. This is the
same class of "sign convention" gap already flagged for the Sweep Lemma in
`decoupling-and-sweep-lemma.md`. Any future use of this lemma to establish
existence/uniqueness rigorously must still close this branch-selection gap.
