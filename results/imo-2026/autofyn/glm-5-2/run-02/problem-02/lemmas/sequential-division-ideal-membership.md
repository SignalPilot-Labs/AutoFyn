# Lemma (sequential-division ideal-membership certificate — round 3)

*Let `(T')_num, (C1)_num, (C2)_num` be the half-angle-tangent numerators (`t_γ=tan(γ/2)`, `t_β=tan(β/2)`, with `t_A=tan(A/2)`, `t_B=tan(B/2)`, `t_α=tan(α/2)` kept as `QQ.frac_field` atoms — NEVER `expand_trig`) of the trig-Ceva target `(T')` and the two incidence constraints `(C1),(C2)`. Then `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩` over `QQ(t_A,t_B,t_α,t_γ,t_β)`: `sp.div((T')_num, (C1)_num, t_γ, domain=QQ.frac_field(t_A,t_B,t_α,t_β))` gives remainder `r1` (degree 3 in `t_γ`, nonzero), then `sp.div(r1, (C2)_num, t_β, domain=QQ.frac_field(t_A,t_B,t_α,t_γ))` gives remainder `0` (`is_zero=True`). Both divisor leading-coefficients are generically nonzero rational functions (verified at one generic rational point: `0.4611`, `0.0439`), so the `sp.div` calls are genuine field division. Denominator-clearing (`D=d_{q1}·d_{q2}`) gives the polynomial-ring certificate `D·(T')_num = Q1·(C1)_num + Q2·(C2)_num` in `ℚ[t_A,t_B,t_α,t_γ,t_β]`.*

## Where proved
`approaches/antipode-rightangle.md`, §8 (round 3, reviewer-certified APPROVE). Independently reproduced by the scout, the outline-reviewer, and the proof-reviewer (3 independent reproductions, all remainder `is_zero=True`).

## Mechanism
Univariate polynomial division over a field is genuine field division (not pseudo-remainder) when the divisor's leading coefficient is a unit in the coefficient field. The sequential-division ideal-membership lemma: if `f ∈ F[t_γ,t_β]`, `g1 ∈ F[t_γ]` has unit leading coeff in `t_γ` over `F = QQ(t_A,t_B,t_α,t_β)`, and `g2` has unit leading coeff in `t_β` over `QQ(t_A,t_B,t_α,t_γ)`, then `rem_{g2}(rem_{g1}(f)) = 0` implies `f` vanishes on `{g1=g2=0}` wherever both leading coeffs are nonzero (the generic case).

## Transferable technique
The **half-angle-only-on-constrained-variables + frac_field-atoms trick**: apply `t_x = tan(x/2)` ONLY to the variables being eliminated (here `γ, β`), keeping the remaining angle variables (`A, B, α`) as `QQ.frac_field` atoms (their `sin/cos` carried as field elements `2t/(1+t²)`, `(1-t²)/(1+t²)`, NEVER expanded). This avoids the `expand_trig` monomial blowup (10⁴–10⁵ monomials) while preserving exact field-division correctness. Transferable to any trig-identity-over-incidence-constraints CAS certificate.
