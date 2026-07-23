# Lemma (certified, round 2) — (T)-reduction and Weierstrass ideal-membership certificate

Source approach: `trig-lawofsines` (§4–§6). Certified by proof-reviewer, who
independently rebuilt every object below in sympy and reproduced the certificate exactly.

## Part 1 — the (T)-reduction
Frame `B=(0,0)`, `C=(1,0)`; `A_x` = abscissa of `A`; `u=K−A`, `v=L−A`,
`D=u_1v_2−u_2v_1 ≠ 0` (A,K,L non-collinear). Then, from the certified power reduction
(`reduction-power-to-core.md`) plus the circumcentre formula,
> `OM²−ON² = [ 2(|u|²v_2−|v|²u_2) − D(1−2A_x) ] / (4D)`,
so **`OM=ON ⟺ (T): 2(|u|²v_2−|v|²u_2)=D(1−2A_x)`**.
Reviewer check: `OM²−ON²` computed from an independent circumcentre routine equals
`(T-difference)/(4D)` identically over random points (ratio = 1/(4D) exactly).

## Part 2 — the ideal-membership certificate
Write `sinγ,cosγ` via `t=tan(γ/2)` and `sinβ,cosβ` via `s=tan(β/2)`. The closing relations
E3′,E2′ (`closing-relations.md`) become degree-4 polynomials `P(t)`, `Q(s)` with
`lc(P,t)=−2 sinA sinθ sin(C−θ)`, `lc(Q,s)=−2 sinA sinθ sin(B−θ)`. Clearing the positive
factors turns (T)'s difference into a polynomial `TN(t,s)` (`deg_t=deg_s=4`), and
`TN=0 ⟺ (T) ⟺ OM=ON` on the physical config (clearing denominator
`Tden = sinA³·[sin(A+2θ+γ)(1+t²)]²·[sin(A+2θ+β)(1+s²)]² ≠ 0`). Then, modulo the Pythagorean
relations `ρ_1=sin²A+cos²A−1`, `ρ_2=sin²C+cos²C−1`, `ρ_3=sin²θ+cos²θ−1`,
> **`lc(P)·lc(Q)·TN = f·P + g·Q`**  (exact polynomial identity),
via one-step pseudo-divisions `lc(P)·TN=q_1P+R_1`, `lc(Q)·R_1=q_2Q+R_2` with `R_2≡0`
(mod ρ). Since `lc(P),lc(Q)≠0` on the physical range (⋆) and `P=0,Q=0` hold there, `TN=0`,
hence `OM=ON`.

Reviewer verification (independent): rebuilt `A,K,L,u,v,D,A_x`, `TN`, `P`, `Q` from the
angle definitions; sympy `pdiv` gave `deg_t R_1=3`, `deg_s R_2=3`, and Groebner reduction
of `R_2` modulo `⟨ρ_1,ρ_2,ρ_3⟩` returned exactly `0`; both leading coefficients matched the
claimed closed forms mod ρ; `Tden` factored as stated (strictly positive on (⋆)).

Status: gap-free; a from-scratch exact-arithmetic symbolic reduction to 0 (same standard as
`reduction-power-to-core.md`). This is the branch-free finish — no branch selection needed.
CERTIFIED.
