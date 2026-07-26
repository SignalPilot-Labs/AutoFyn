# Lemma: angle-linearity-cubic-reduction

**Statement.** With `A=(0,0)`, `B=(b,0)`, `C=(u,v)`, encode the directed-angle equalities `∠KBA=∠ACL` (`e1`) and `∠LBK=∠LNC` (`e2`) via the cross/dot form `cross(p,q)·dot(r,s)−cross(r,s)·dot(p,q)=0`. Write `K=B+(sx,sy)`. Then `e1,e2` are **homogeneous linear** in `(sx,sy)`: `e1=a1·sx+b1·sy`, `e2=a2·sx+b2·sy` (zero constant terms), with `a1,b1,a2,b2∈Q(b,u,v)[lx,ly]`. For `K≠B`, the determinant
```
D(L) := a1·b2 − b1·a2 = −(b/4)·|C|²·D₀(L) = 0,
D₀(L) := b·lx·v − b·ly·u + 2·lx²·ly − lx²·v − 2·lx·ly·u + 2·ly³ − 3·ly²·v + ly·u² + ly·v²
```
vanishes (a cubic in `L`). The kernel of the system is spanned by `d(L):=(b1,−a1)`, so `K = B + t·d(L)` for a real `t`. On `D₀=0`: `e1|_{(3)}≡0` (identically in `t`) and `e2|_{(3)}=−t·D` (so `e2=0` on `D₀=0`).

**Proof.** Homogeneous linearity is by collection of `e1,e2` in `(sx,sy)` (the constant term vanishes because `K=B` makes both `∠KBA`, `∠LBK` degenerate). The determinant is a direct `2×2` computation; its factorisation `D=−(b/4)|C|²·D₀` is a direct `sympy` expansion (verified over `Q(b,u,v,lx,ly)`). The kernel claim is linear algebra. `e2|_{(3)}=a2·b1+b2·(−a1)=−D` is a direct expansion. ∎

**Source.** `analytic-branch-cert` Section 4 (Lemmas 1–2); re-verified in `analytic-resultant-cert` §3–4. Reviewer-certified round 2 (factorisation re-derived independently with parameters free).
