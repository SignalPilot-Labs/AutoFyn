# Lemma (certified, round 1) — reduction of OM=ON to a scalar power identity

Source approach: `power-of-point-BC`. Certified by proof-reviewer (algebra re-derived
symbolically, sympy: all three identities reduce to 0).

Let `ω = ⊙(AKL)`, centre `O`, radius `R=OA`. For a point `X`, `pow(X):=|XO|²−R²`.

**L2a.** For any point `X`, `OX²−R²=pow(X)`; since `OM,ON≥0`,
`OM=ON ⟺ pow(M)=pow(N)`.
*Proof.* `OM²−ON²=(OM²−R²)−(ON²−R²)=pow(M)−pow(N)`. ∎

**L1 (power along a line / second-intersection).** For a line through `A∈ω` with unit
direction `u`, parametrised `P(s)=A+s·u`, one has `pow(P(s))=s²+2⟨u,A−O⟩s=s(s−a')`, a
MONIC quadratic with roots `s=0` (point `A`) and `s=a'=−2⟨u,A−O⟩` (the second
intersection `A'`). Leading coeff is 1 since `|u|=1`; constant term is 0 since `A∈ω`.
Consequence, taking `ℓ=AB` (`M` at `s=AB/2`, `B` at `s=AB`):
`pow(M)=pow(B)/2−AB²/4`, and by the mirror computation on `AC`,
`pow(N)=pow(C)/2−AC²/4`.

**Reduction.** Combining, `pow(M)−pow(N)=½[(pow(B)−pow(C))−(AB²−AC²)/2]`, hence
> **OM=ON ⟺ pow(B,ω)−pow(C,ω) = (AB²−AC²)/2.**   ("core identity")

Verification (reviewer): symbolic check `pow(B)−pow(C)−(AB²−AC²)/2 − 2(pow(M)−pow(N)) = 0`
identically; and a from-scratch physical configuration (θ∈{0.15,0.25,0.35}) confirms
`core=0` exactly when `OM=ON` (both ≤5e-13).

Status: gap-free, correct, no stronger than proved. CERTIFIED.
