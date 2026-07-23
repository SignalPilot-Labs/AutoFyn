## Lemma: Radical-axis (frame-free) restatement of the power-of-a-point target (TI)

**Source approach:** labeling-duality (round 2). Certified by proof-reviewer,
round 2 (re-derived algebraically from scratch and cross-checked against the
`coordinate-om-on-reduction.md` frame; confirmed a genuine, correct,
frame-free equivalent of the existing target — NOT a new reduction that
bypasses the open gap).

### Statement
Let `Ω` = circumcircle(`ABC`) (center `O_Ω`, fixed, independent of `K,L`),
`Γ` = circumcircle(`AKL`) (center `O`). Then
$$\mathrm{pow}_\Gamma(X)-\mathrm{pow}_\Omega(X) = 2X\cdot(O_\Omega-O) + \text{(a constant independent of }X\text{)}$$
is affine-linear in `X` (i.e. its difference at two points depends only on
`X_1-X_2`), and since `B,C ∈ Ω` give `pow_Ω(B)=pow_Ω(C)=0`,
$$\mathrm{pow}_\Gamma(B)-\mathrm{pow}_\Gamma(C) = 2(B-C)\cdot(O_\Omega-O). \tag{R2}$$
Combined with the certified target (TI) (`median-length-power-reduction.md`):
`pow_Γ(B)-pow_Γ(C) = (AB²-AC²)/2`, this is equivalent to
$$(B-C)\cdot O = (B-C)\cdot O_\Omega - \frac{AB^2-AC^2}{4}, \tag{TI″}$$
i.e. the target is exactly "the scalar projection of `O` (circumcenter of
`AKL`) onto the fixed direction `B-C` is pinned to one specific fixed value."

### Proof
Expand `pow_Γ(X)=|X|^2-2X·O+|O|^2-R^2`, `pow_Ω(X)=|X|^2-2X·O_Ω+|O_Ω|^2-R_Ω^2`
(both from the definition `pow_c(X)=|X-\text{center}|^2-\text{radius}^2`,
where `A ∈ Γ,Ω` fixes `R=OA`, `R_Ω=O_ΩA`, but neither `R` nor `R_Ω` is needed
below). Subtracting, `|X|^2` cancels:
`pow_Γ(X)-pow_Ω(X) = 2X·(O_Ω-O) + (|O|^2-R^2)-(|O_Ω|^2-R_Ω^2)`, affine-linear
in `X`. Evaluate at `X=B,C` and subtract (constant term cancels):
`(pow_Γ(B)-pow_Ω(B)) - (pow_Γ(C)-pow_Ω(C)) = 2(B-C)·(O_Ω-O)`. Since
`B,C ∈ Ω`, `pow_Ω(B)=pow_Ω(C)=0` by definition, giving (R2). Substituting
`pow_Γ(B)-pow_Γ(C)=(AB^2-AC^2)/2` (TI) and rearranging
`2(B-C)·(O_Ω-O)=(AB^2-AC^2)/2` gives `(B-C)·O_Ω-(B-C)·O=(AB^2-AC^2)/4`, i.e.
(TI″). ∎

**Cross-check (equivalence, not a new reduction):** in the frame
`B=(-1,0),C=(1,0),A=(p,q)` (`coordinate-om-on-reduction.md`), direct
substitution gives `AB^2-AC^2=4p`, `O_Ω=(0,(p^2+q^2-1)/(2q))`, so
`(B-C)·O_Ω = (-2,0)·(0,\cdot)=0`; then (TI″) reads `-2O_x = 0-4p/4=-p`, i.e.
`O_x=p/2` — the exact same target certified in `coordinate-om-on-reduction.md`.

### Status and scope
Fully proved, general (works for any triangle and any circle `Γ` through
`A`). Reusable as an alternative, frame-free formulation of the same open
target. **Explicitly does not close the open gap**: it is informationally
equivalent to `O_x=p/2`/(TI), not a strictly weaker or easier target — proving
it still requires locating where `O` (circumcenter of `AKL`) projects onto
line `BC`, using the three angle hypotheses, which remains open.
