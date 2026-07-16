# Lemma S: a triangle product-to-sum identity

**Statement.** Let a triangle have angles `A = π − B − C`, circumradius `R`, and sides
`c = 2R sin C`, `b = 2R sin B`. Then for any angle `θ`:
```
c·sin(A − θ) + b·sin θ = 2R·sin A·sin(C + θ),
c·sin θ      + b·sin(A − θ) = 2R·sin A·sin(B + θ).
```

**Proof.** `c sin(A−θ) + b sinθ = 2R[sinC sin(A−θ) + sinB sinθ]`. By product-to-sum,
`sinC sin(A−θ) = ½[cos(C−A+θ) − cos(C+A−θ)]` and `sinB sinθ = ½[cos(B−θ) − cos(B+θ)]`.
Since `C + A − θ = π − B − θ`, `cos(C+A−θ) = −cos(B+θ)`, so the `−cos(C+A−θ)` and
`−cos(B+θ)` terms cancel, leaving `½[cos(C−A+θ) + cos(B−θ)] = cos((B+C−A)/2)·cos((C−A−B)/2+θ)
= cos(π/2 − A)·cos(C − π/2 + θ) = sin A·sin(C + θ)`. The second identity is the first
with `B ↔ C`, `θ → θ`. ∎

**Certification (proof-reviewer, round 1).** Both forms verified as exact symbolic identities
in sympy (`simplify(lhs − rhs) == 0`). Certified for reuse. Certified from approach
`power-of-point-balance` (Lemma S).
