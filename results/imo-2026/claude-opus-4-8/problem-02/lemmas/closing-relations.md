# Lemma (certified, round 2) — closing relations E2′, E3′

Source approaches: `power-of-point-BC` (§E) and `trig-lawofsines` (§3). Certified by
proof-reviewer (derivation re-checked; both relations reproduced symbolically and
numerically to <1e-12 on from-scratch physical configs).

Notation: triangle angles `A,B,C` (`A+B+C=π`); `θ=∠KBA=∠ACL` (E1), `β=∠LBK=∠LNC` (E2),
`γ=∠LCK=∠BMK` (E3). Physical range (⋆): `0<θ<min(B,C)`, `0<γ<C−θ`, `0<β<B−θ`.

> **(E3′)** `sinγ·sinC·sin(A+2θ+γ) = 2 sinA·sin(θ+γ)·sin(C−θ−γ)`.
> **(E2′)** `sinβ·sinB·sin(A+2θ+β) = 2 sinA·sin(θ+β)·sin(B−θ−β)`.

*Proof.* Place `B=(0,0)`, `C=(1,0)` (BC=1). By the containments, ray `BK` lies inside
`∠ABC` with `∠KBC=B−θ`, and ray `CK` lies inside `∠ACB` with `∠KCB=C−(θ+γ)` (since
`∠ACK=∠ACL+∠LCK=θ+γ`, `L` inside `∠ACK`). Hence `∠BKC=A+2θ+γ` and, by the Law of Sines in
`△BKC`, `BK = BC·sin(C−θ−γ)/sin(A+2θ+γ) = sin(C−θ−γ)/sin(A+2θ+γ)`. The certified cevian
lemma (`cevian-lengths.md`) gives a second value `BK=(AB/2)sinγ/sin(θ+γ)`; with
`AB=sinC/sinA` (Law of Sines) and clearing the (nonzero on (⋆)) factors
`sinC,sin(θ+γ),sin(A+2θ+γ)` yields (E3′). The `B↔C, M↔N, γ↔β` mirror (using `∠CNL=β`,
`∠NCL=θ`, `CN=AC/2`, `AC=sinB/sinA`) yields (E2′). ∎

Reviewer verification: rebuilt both sides symbolically in sympy; solving (E3′) for γ in
(0,C−θ) and (E2′) for β in (0,B−θ) reconstructs the physical configuration with OM=ON to
machine precision across 6 random scalene triangles.

Status: gap-free given the certified cevian lengths; elementary Law of Sines. CERTIFIED.
