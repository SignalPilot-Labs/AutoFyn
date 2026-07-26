# Lemma: et2-on-D-zero-relation

**Statement.** Let `e3_line(lx,ly,t)` be the field-reduction (mod `D₀`, over `Q(b,u,v,lx,t)[ly]`) of the third-angle polynomial `e3` (encoding `∠LCK=∠BMK`) after substituting `K=B+t·d(L)`. Let `et2` be its `t²`-leading coefficient. Then the **genuine polynomial identity**
```
et2 = (b³/2)·|C|²·(v−ly)·|L−C|²  −  b²·D(L)              (in Z[b,u,v,lx,ly])
```
holds, where `|L−C|²=(lx−u)²+(ly−v)²` and `D(L)=−(b/4)·|C|²·D₀(L)`. In particular, **on `D₀=0`** (where `D=0`):
```
et2|_{D₀=0} = (b³/2)·|C|²·(v−ly)·|L−C|².
```
Hence `et2>0` whenever `L` is strictly inside `△BNC` (so `ly<v` and `L≠C`).

**Proof.** Verified by direct subtraction: `et2 − [(b³/2)|C|²(v−ly)|L−C|² − b²·D] ≡ 0` over `Q(b,u,v,lx,t)` (the parameters `b,u,v,lx,t` are free). The on-`D₀=0` factorisation follows since `D|_{D₀=0}=0`. Positivity on the inside arc: write `L=λ_B·B+λ_N·N+λ_C·C` in barycentrics of `△BNC` (`λ_B,λ_N,λ_C>0`, `Σ=1`); then `ly=λ_N·v/2+λ_C·v=(1−λ_B−λ_N/2)·v<v` (since `λ_B>0`), and `|L−C|²>0` since `L≠C` (strict interiority). ∎

**Source.** `analytic-branch-cert` Section 6 (Lemma 3) + Section 7 (Lemma 5); re-verified in `analytic-resultant-cert` §5–6. Reviewer-certified round 2 (re-derived independently with parameters free; the on-`D₀=0` form is the one used for positivity).
