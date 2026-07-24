# Lemma CRAMER (square-case Cramer integrality) — CERTIFIED round 7

Source: `dual-integer-certificate` §3 (also `concentration-exclusion-rigidity` §Setup). Reviewer
re-derived; standard Cramer's rule + integrality of integer-matrix cofactors.

## Statement
Let `U∈ℤ^{(n+1)×(n+1)}` be invertible, `Uw=b` with `b∈ℤ^{n+1}`, and `f=sᵀw` with `s∈ℤ^{n+1}`. Let `U_j`
be `U` with its `j`-th column replaced by `b`. Then
```
    f·det(U) = Σ_{j} s_j·det(U_j) ∈ ℤ,
```
so `f = M/det(U)` with `M:=Σ_j s_j det(U_j)∈ℤ`. Hence `f∈ℤ ⟺ det(U)∣M`, and `|det U|=1 ⟹ f∈ℤ`.

## Proof
`U` invertible ⟹ `w=U^{-1}b` unique; Cramer's rule (knowledge base: *Cramer's rule / determinant
solution of a linear system*) gives `w_j=det(U_j)/det(U)`. Then `f=Σ_j s_j w_j`, so
`f·det(U)=Σ_j s_j det(U_j)`. Each `U_j` is an integer matrix (`U,b` integer) ⟹ `det(U_j)∈ℤ`; `s_j∈ℤ`
⟹ `M∈ℤ`. ∎

## Verification (reviewer, independent)
- On the certified non-minimizer `{2,4/3,4/3,4/3,1}` (S-core, `p=3`): `det(U)=3`, `M=5`, `f=5/3`,
  `f·det(U)=5∈ℤ` — and `(D′)` fails there (`3∤5`), matching `gap-d-not-universal`.

## Use
Ties the square-case integrality target `f∈ℤ` to the concrete divisibility `det(U)∣M`, implied by (but
weaker than) `|det U|=1`. Makes the dual and primal square-case targets coincide up to a divisibility
slack. Note (certified `gap-d-not-universal`): the divisibility genuinely FAILS off the minimizer set,
so any proof of `det(U)∣M` MUST invoke minimality/Φ-maximality — this is not a pure incidence fact.
