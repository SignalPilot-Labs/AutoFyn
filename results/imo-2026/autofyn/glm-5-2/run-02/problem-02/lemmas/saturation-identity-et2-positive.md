# Lemma: saturation-identity-et2-positive

**Statement.** With `e3_line, Q_line` the field-reduced (mod `D₀`) quadratics in `t` (after the `K=B+t·d(L)` line reduction), let `et2, Qt2` be their `t²`-leading coefficients. The **polynomial identity**
```
Qt2 · e3_line  −  et2 · Q_line  =  D₀(L) · G(lx,ly,t)
```
holds in `Q[b,u,v,lx,ly,t]`, where `G` is the explicit polynomial (linear in `t`)
```
G = (b⁴·v·|C|²/4) · { t·[ |C|²·(3b²+b·lx−b·u) − 3·b²·(lx·u+ly·v) ]
                      + [ b²+b·lx−b·u − 3·lx·u − 3·ly·v + 2·|C|² ] }.
```
Consequently **on `D₀=0`**: `et2·Q_line = Qt2·e3_line`. Combined with `et2>0` on the inside arc `L∈△BNC` (lemma `et2-on-D-zero-relation`) and `e3_line=0` (the third angle condition), this forces `Q_line=0`, hence `Q=0`, hence `OM=ON` (lemma `analytic-target-line`).

**Proof.** The identity is a parameter-free polynomial identity in `b,u,v,lx,ly,t`. Verified by **true field division** (NOT ring pseudo-remainder): `sp.div(Poly(Qt2·e3_line−et2·Q_line, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=...))` returns **remainder `0`** with the displayed quotient `G` (linear in `t`). Independently confirmed by direct symbolic simplification `sp.simplify(LHS − D₀·G_prop)=0`. (The round-1 "FALSE" verdict was an arithmetic slip: the cleared target `Q` at the alleged counterexample `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3` is `320/3`, not `256`; recomputed from the defining formula, the LHS vanishes there — the saturation identity holds.) ∎

**Reviewer note (round 2).** Independently re-verified by the reviewer: `sp.div` over `QQ.frac_field(b,u,v,lx,t)` returns remainder `0`; the builder's explicit `G_prop` satisfies `LHS−D₀·G_prop≡0`. At the alleged counterexample, `Q=320/3` (not `256`), `D₀=0`, and `Qt2·e3_sub−et2·Q_sub` is the zero polynomial in `t`. The positivity `et2>0` was checked on 25 inside-arc configs (min `et2=0.025>0`). This is the closing certificate of the solved proof.

**Source.** `analytic-branch-cert` Section 6 (Proposition 4). Reviewer-certified round 2.
