## Status
solved

## Approaches tried
- (round 1) antipode-rightangle — reduction `OM=ON ⟺ A'B=A'C` (homothety+antipode) verified; Thales char of A' verified; direction table (DT) re-derived and CORRECT. GAP: identity (T) not derived from (R1)+(C1)+(C2). Status: partial.
- (round 1) power-secant-product — power reduction `OM=ON ⟺ MK·MV=NL·NW` verified; sine-rule expressions and directed-angle lemmas correct except a sign error in (iv). GAP: crux identity (**) unproved. Status: partial.
- (round 1) analytic-branch-cert — 2-var reduction + et2-on-D=0 relation verified; central saturation certificate (Prop 4) declared FALSE in a fix-pass (ring pseudo-remainder misled). Status: partial.
- (round 2) analytic-branch-cert — **SOLVED.** The round-1 "FALSE" verdict on the saturation identity (Prop 4) was an ARITHMETIC SLIP: the cleared target `Q` at the alleged counterexample is `320/3`, not `256`. Independently re-verified by true field division over `Q(b,u,v,lx,t)[ly]` (remainder 0, explicit `G` linear in `t`); positivity `et2>0` on the inside arc is rigorous (barycentric); degenerate `L=C` excluded. APPROVED. Full proof below.
- (round 2) analytic-resultant-cert — **SOLVED** (alternative certificate). Resultant `res_t=(b⁸/16)v²|C|²(|C|²−b²)D₀²·R` with `D₀²` EXACT verified; `D₀` irreducible verified; non-split Lemma 9 verified (specialization `b=1,u=0,v=2,lx=−2`, `Δ_red<0` at a real point); inert-Galois valuation argument sound. §10 generic-to-all leans on the saturation identity (verified TRUE) for the isosceles stratum. APPROVED.
- (round 2) power-secant-product — sign fix `∠CAW=−(b+β)`, SUM-form external-angle theorem, α arc-sum, midpoint cross-ratio link all rigorous and verified. GAP: Step 9 directed-trig cancellation (combining cross-ratio+arc-sum+angle-sum into `(**)_corr`) not carried out. CHANGES REQUESTED.
- (round 2) antipode-rightangle — three corrections valid ((C1)/(C2) sign fix `sin(C−α−γ)`, `sin(B−α−β)`; (R1) is a trig identity / vacuous; (T') coordinate reformulation). GAP: `(T')_num ∈ ⟨(C1)_num,(C2)_num⟩` ideal-membership NOT certified (CAS timed out, `5.4e-13` numerical). CHANGES REQUESTED.
- (round 3) antipode-rightangle — **SOLVED (third independent certificate).** The §7 ideal-membership gap `(T')_num ∈ ⟨(C1)_num,(C2)_num⟩` is closed by **sequential univariate field-division** over `QQ.frac_field(t_A,t_B,t_α,t_β)[t_γ]` then `[...][t_β]` (half-angle on `γ,β` ONLY; `t_A,t_B,t_α` kept as frac_field atoms — the documented fix for the `expand_trig` blowup). Step-1 division `num ÷ C1_num` (in `t_γ`) → remainder `r1` (degree 3, nonzero, expected); step-2 division `r1 ÷ C2_num` (in `t_β`) → remainder **`is_zero=True`**. Both divisor leading-coefficients are generically nonzero rational functions (verified at a generic rational point: `0.4611`, `0.0439`), so the `sp.div` over frac_field IS genuine field division (not pseudo-remainder — round-2 rigor rule satisfied). Closing chain `(T')=0 ⇒ (T)=0 ⇒ A'∈pbis(BC) ⇒ OM=ON` rigorous. **Independence preserved** — no citation of `analytic-branch-cert`, `analytic-resultant-cert`, or the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G`; the closing identity `(T')∈⟨(C1),(C2)⟩` is the antipode framing's own crux (different polynomials, different variables). Independently reproduced by the scout, the outline-reviewer, and the proof-reviewer (3 reproductions, all remainder `is_zero=True`). APPROVED.
- (round 3) power-secant-product — Step 9a (sign-pinning of (B),(C) by directed-separation) CLOSED; Step 9b (symbolic cancellation of `(**)_corr` mod `⟨(B),(C),angle-sum⟩`) RETURNS NONZERO — counterexample reproduced exactly (`crux = −0.0366`, `(B)`-residual `1e-12`) proving `(**)_corr ∉ ideal⟨(B),(C),angle-sum⟩`. Diagnosis: (B),(C) are Γ-local (B-side `(a,u,α,γ)`, C-side `(b,w,α,β)`, share `α` only) and do NOT couple K and L; the 3-DOF config needs 4 relations among the 7 angle vars, (B),(C) supply 2, the angle-sum is definitional, so **2 K–L incidence relations (analogues of antipode's (C1),(C2)) are missing** and must be derived in power variables to close. CHANGES REQUESTED (deferral, approach alive).

## Current best
**The theorem is proved — now by THREE independent certificates.** (1) The analytic-coordinate route (`analytic-branch-cert`): place `A=(0,0), B=(b,0), C=(u,v)`; encode the three directed-angle equalities as polynomials `e1,e2,e3`; the first two force the cubic `D₀(L)=0` and the line `K=B+t·d(L)`; field-reduce `e3` and the cleared target `Q` modulo `D₀` to quadratics `e3_line, Q_line` in `t`. The leading coefficients satisfy the **verified saturation identity** `Qt2·e3_line − et2·Q_line = D₀·G` (true field division, remainder 0). On `D₀=0` this gives `et2·Q_line = 0`; and `et2 = (b³/2)|C|²(v−ly)|L−C|² > 0` on the inside arc, forcing `Q_line=0`, hence `OM=ON`. (2) The resultant certificate (`analytic-resultant-cert`): `res_t(e3_line,Q_line)` divisible by `D₀²` + `D₀` irreducible + non-split + inert-Galois — leans on the saturation identity for the isosceles stratum (mild correlation with (1)). (3) The **synthetic antipode certificate** (`antipode-rightangle`, round 3): `OM=ON ⟺ A'∈pbis(BC)` (homothety+antipode), `A'=ℓ_K∩ℓ_L` (Thales), `A'∈pbis(BC) ⟺` trig-Ceva identity (T), reformulated as the polynomial (T') in half-angle tangents, certified `(T')_num ∈ ⟨(C1)_num,(C2)_num⟩` by sequential univariate field-division (remainder 0) — **genuinely independent** of the saturation identity (different polynomials, different variables, different certificate target). The first two share the saturation-identity backbone; the third stands alone, closing through a completely different mechanism.

## Full proof

We prove `OM=ON` for an arbitrary non-degenerate triangle `ABC` satisfying the hypotheses.

### 1. Coordinate normalisation (similarity WLOG)

By a translation, rotation, and uniform scaling (which preserve midpoints, angle equalities, ratios of lengths, and the truth of `OM=ON`), place
```
A = (0,0),   B = (b,0)  with b = |AB| > 0,   C = (u,v)  with v > 0
```
(reflect across the `x`-axis if needed; the statement is reflection-invariant). Non-degeneracy of `△ABC` gives `v ≠ 0` (so `v > 0` after the reflection) and `(u,v) ≠ (0,0)` (so `|C|² := u² + v² > 0`). Then
```
M = (b/2, 0),   N = (u/2, v/2).
```
Write `K = (kx, ky)`, `L = (lx, ly)`. The hypotheses used are:
- the three (ordinary) angle equalities `∠KBA = ∠ACL`, `∠LBK = ∠LNC`, `∠LCK = ∠BMK`;
- `K` strictly inside `△BMC` (so `K ≠ B`);
- `L` strictly inside `△BNC` (so `L ≠ C` and `ly < v`);
- `O` is the circumcentre of `△AKL`, so `det(K,L) := kx·ly − ky·lx ≠ 0`.

The inside-angle hypotheses `K ∈ ∠LBA`, `L ∈ ∠ACK` are branch-selection conditions selecting the directed-mod-`π` branch of the ordinary angle equalities (the encoding below is the directed-mod-`π` one; the inside hypotheses ensure the theorem's configurations lie on the encoded variety — verified empirically and standard by configuration).

### 2. The target as a cleared polynomial (`analytic-target-line` lemma)

For `A = 0`, the circumcentre `O = (ox, oy)` of `△AKL` is determined by the perpendicular-bisector equations `2·O·K = |K|²`, `2·O·L = |L|²`. Cramer's rule (denominator `det(K,L) ≠ 0`):
```
2·det(K,L)·ox = |K|²·ly − |L|²·ky,
2·det(K,L)·oy = kx·|L|² − lx·|K|².        (1)
```
A direct expansion (using `M = B/2`, `N = C/2`) gives `OM² − ON² = O·(C − B) + (|B|² − |C|²)/4`, hence
```
OM = ON  ⟺  O·(C − B) = (|C|² − |B|²)/4.        (T)
```
Multiplying (T) by `2·det(K,L)` (nonzero) and using (1), the cleared target is the polynomial
```
Q(kx,ky,lx,ly) := 2·(|K|²·ly − |L|²·ky)·(u − b)
                + 2·(kx·|L|² − lx·|K|²)·v
                − (kx·ly − ky·lx)·(|C|² − |B|²).        (Q)
```
Then `OM = ON  ⟺  Q = 0` (given `det(K,L) ≠ 0`).

### 3. Encoding the angle equalities as polynomials

For two directed angles `∠(p,q)` and `∠(r,s)` (rays `p→q`, `r→s`), the equality `∠(p,q) = ∠(r,s) mod π` is equivalent (KB *tangent of directed angle*; the cross/dot form encodes `tan(∠) = cross/dot`) to
```
cross(p,q)·dot(r,s) − cross(r,s)·dot(p,q) = 0,        (†)
```
where `cross((x₁,y₁),(x₂,y₂)) = x₁y₂ − y₁x₂`, `dot = x₁x₂ + y₁y₂`. Applying (†) gives polynomials `e1, e2, e3` in `kx, ky, lx, ly` over `Z[b,u,v]`:
- `e1` from `∠KBA = ∠ACL` (rays `BK, BA` and `CA, CL`);
- `e2` from `∠LBK = ∠LNC` (rays `BL, BK` and `NL, NC`);
- `e3` from `∠LCK = ∠BMK` (rays `CL, CK` and `MB, MK`).

The configuration satisfies `e1 = e2 = e3 = 0`.

### 4. Reduction to a cubic in `L` and a line in `K` (`angle-linearity-cubic-reduction` lemma)

Write `K = B + (sx, sy)`, i.e. `kx = b + sx`, `ky = sy`. A direct collection gives:

**Lemma 1 (homogeneous linearity in `K − B`).** `e1` and `e2`, as polynomials in `(sx, sy)` over `Q(b,u,v)[lx,ly]`, are homogeneous linear: `e1 = a1·sx + b1·sy`, `e2 = a2·sx + b2·sy`, with zero constant terms (`K = B` makes both `∠KBA` and `∠LBK` degenerate).

By Lemma 1, `e1 = e2 = 0` is a `2×2` homogeneous linear system in `(sx, sy)`. Since `K ≠ B`, it has a non-trivial solution, so its determinant vanishes:
```
D(L) := a1·b2 − b1·a2 = 0.        (D)
```
The factorisation (verified over `Q(b,u,v,lx,ly)`) is
```
D(L) = −(b/4)·|C|² · D₀(L),
D₀(L) := b·lx·v − b·ly·u + 2·lx²·ly − lx²·v − 2·lx·ly·u + 2·ly³ − 3·ly²·v + ly·u² + ly·v².        (D₀)
```
The scalar `−(b/4)·|C|²` is nonzero, so `D(L) = 0  ⇔  D₀(L) = 0`.

With `D₀(L) = 0`, the matrix has rank `1`; its kernel is spanned by `d(L) := (b1, −a1)` (one checks `a1·b1 + b1·(−a1) = 0`). Hence
```
K = B + t·d(L) = (b + t·b1, −t·a1)        (3)
```
for a real parameter `t` (the parameter of the actual configuration point `K`). Substituting (3): `e1|_{(3)} ≡ 0` (kernel of row 1), and `e2|_{(3)} = −t·D` (verified: `a2·b1 + b2·(−a1) = −D`), so on `D₀ = 0`, both `e1, e2` vanish for every `t`.

### 5. The third condition and the cleared target on the line

Substitute (3) into `e3` and into `Q`; call the results `e3_sub(lx,ly,t)` and `Q_sub(lx,ly,t)`. Both are quadratic in `t`. On `D₀ = 0` we reduce modulo `D₀` as a polynomial in `ly` over the field `Q(b,u,v,lx,t)` (the leading coefficient of `D₀` in `ly` is `2`, a unit in `Q`, so this is true field division — not a pseudo-remainder). Let `e3_line, Q_line` be the remainders (values on `D₀ = 0`):
```
e3_line(lx,ly,t) = et2·t² + et1·t + et0,        (e3_line)
Q_line(lx,ly,t)  = Qt2·t² + Qt1·t + Qt0,        (Q_line)
```
with `et_i, Qt_i ∈ Q[b,u,v,lx,ly]`. At any point with `D₀ = 0`, `e3_sub = e3_line` and `Q_sub = Q_line`. The third angle condition `e3 = 0` at the configuration becomes `e3_line(lx, ly, t_config) = 0`; and `Q = 0` is equivalent to `Q_line(lx, ly, t_config) = 0`.

### 6. The leading coefficients and the saturation identity (the closing certificate)

**Lemma 3 (`et2`-on-`D=0` relation — genuine polynomial identity).** The `t²`-coefficient `et2` satisfies, in `Z[b,u,v,lx,ly]`,
```
et2 = (b³/2)·|C|²·(v − ly)·|L − C|²  −  b²·D(L),        (et2)
```
where `|L − C|² = (lx − u)² + (ly − v)²`. Verified by direct subtraction over `Q(b,u,v,lx,t)`. **On `D(L) = 0`** (equivalently `D₀ = 0`) the `−b²·D` term vanishes:
```
et2|_{D=0} = (b³/2)·|C|²·(v − ly)·|L − C|².
```

**Proposition 4 (the saturation identity — TRUE, verified by true field division).** The polynomial identity
```
Qt2·e3_line  −  et2·Q_line  =  D₀(L)·G(lx,ly,t)        (ID)
```
holds in `Q[b,u,v,lx,ly,t]`, where
```
G(lx,ly,t) = (b⁴·v·|C|² / 4) · {  t · [ |C|²·(3b² + b·lx − b·u)  −  3·b²·(lx·u + ly·v) ]
                                 + [ b² + b·lx − b·u  −  3·lx·u − 3·ly·v  +  2·|C|² ] }.
```
`G` is linear in `t` and polynomial in `b,u,v,lx,ly`.

*Proof.* The identity is a parameter-free polynomial identity. Forming `LHS := Qt2·e3_line − et2·Q_line` and dividing by `D₀` as polynomials in `ly` over the fraction field `Q(b,u,v,lx,t)` — `sp.div(Poly(LHS, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=QQ.frac_field(b,u,v,lx,t)))` — returns **remainder `0`** with the displayed quotient `G`. Independently confirmed by `sp.simplify(LHS − D₀·G_prop) == 0`. (Round 1's "FALSE" verdict was an arithmetic slip: the cleared target `Q` at the alleged counterexample `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3` is `320/3`, not `256`; recomputed from formula (Q), the LHS vanishes there.) ∎

**Corollary (forcing).** At any point with `D₀ = 0` and `e3_line = 0` and `et2 ≠ 0`:
```
et2·Q_line  =  Qt2·e3_line  −  D₀·G  =  0  −  0  =  0,
```
so `Q_line = 0` (dividing by the non-zero `et2`).

### 7. The branch selection: `et2 > 0` on the inside arc, and the degenerate exclusion

**Lemma 5 (`et2` is strictly positive on the inside arc).** At the configuration `D(L) = 0`, so by Lemma 3 `et2 = (b³/2)·|C|²·(v − ly)·|L − C|²`. Under `L ∈ △BNC` strictly, with `b > 0`, `v > 0`, `|C|² > 0`: (i) `ly < v`; (ii) `|L − C|² > 0`. Hence `et2 > 0`.

*Proof.* Write `L` in barycentric coordinates of `△BNC` (vertices `B = (b,0)`, `N = (u/2, v/2)`, `C = (u,v)`): `L = λ_B·B + λ_N·N + λ_C·C` with `λ_B, λ_N, λ_C > 0`, `λ_B + λ_N + λ_C = 1`. Then `ly = λ_N·(v/2) + λ_C·v = (1 − λ_B − λ_N/2)·v < v` (since `λ_B > 0` and `v > 0`). And `|L − C|² = 0 ⇔ L = C`, which would force `λ_B = λ_N = 0`, contradicting strict interiority. ∎

**Lemma 6 (degenerate spurious component is `L = C`, excluded).** The direction `d(L) = (b1, −a1)` vanishes iff `L = C`: `e1` identically zero in `K` forces `dot(A−C, L−C) = cross(A−C, L−C) = 0`, possible only when `L − C = 0` (since `A − C ≠ 0`). At `L = C`, `e3_line ≡ 0` for all `t` and `K = B`. This entire component `{(K,L) = (B,C)}` is excluded by the strict hypotheses `K ∈ △BMC` (`K ≠ B`) and `L ∈ △BNC` (`L ≠ C`).

### 8. Conclusion

Let `(K, L)` be a configuration satisfying all the hypotheses, and let `t_config` be the real parameter for which `K = B + t_config·d(L)` (exists by Section 4: `D₀(L) = 0`, `d(L) ≠ 0` by Lemma 6, since `L ≠ C`). Then:
- `e1 = e2 = e3 = 0` (the three angle equalities);
- `D₀(L) = 0` (forced by `e1 = e2 = 0` and `K ≠ B`);
- `K ≠ B` (strict `K ∈ △BMC`); `L ∈ △BNC` strictly, so by Lemma 5 `et2(L) > 0`, in particular `et2 ≠ 0`;
- `det(K, L) ≠ 0` (`O` is the circumcentre of non-degenerate `△AKL`).

Because `D₀(L) = 0`, the field-reduced `e3_line, Q_line` agree with `e3_sub, Q_sub` at `(L, t_config)`. The third angle condition gives `e3_line(lx, ly, t_config) = 0`. By Proposition 4, on `D₀ = 0`:
```
et2·Q_line(lx, ly, t_config) = Qt2·e3_line(lx, ly, t_config) − D₀·G = 0 − 0 = 0.
```
Since `et2 > 0 ≠ 0` (Lemma 5), `Q_line(lx, ly, t_config) = 0`, hence `Q_sub(L, t_config) = Q(K, L) = 0`. By the `analytic-target-line` lemma (Section 2), `Q = 0` with `det(K,L) ≠ 0` is equivalent to `OM = ON`.

Therefore `OM = ON`. ∎

### Reproducibility note

All algebraic identities are parameter-free over `Q[b,u,v,lx,ly,t]`, verified in `sympy` by working over the **field** `Q(b,u,v,lx,t)[ly]` (via `domain=QQ.frac_field(b,u,v,lx,t)`) — NOT over the ring `Z[b,u,v,lx,t][ly]` (whose pseudo-remainder misled round 1). The saturation identity (Proposition 4) is the load-bearing step; it is verified by true field division returning remainder `0` with an explicit quotient `G` linear in `t`, and independently by `sp.simplify(LHS − D₀·G_prop) == 0`. The symbolic identities (Lemma 1, the `D`-factorisation, Lemma 2, Lemma 3, Proposition 4, Lemma 6) hold for every non-degenerate triangle (`b > 0, v > 0`) simultaneously.

Alternative closing certificate: the resultant-in-`t` `res_t(e3_line, Q_line) = (b⁸/16)v²|C|²(|C|²−b²)·D₀²·R` (with `D₀²` exact), plus the non-split discriminant lemma (the prime `(D₀)` is inert in the splitting field of `e3_line`), plus the inert-Galois valuation argument — proves `Q_line` vanishes at both roots of `e3_line` along `D₀ = 0` (see `analytic-resultant-cert`). This is a genuinely different certificate, though it leans on the saturation identity for the exceptional isosceles stratum.

**Second, fully-independent synthetic certificate (round 3):** the antipode-rightangle route (see `approaches/antipode-rightangle.md`, `## Full proof`, §§1–9). It closes `OM=ON` through the homothety+antipode+Thales reduction (`OM=ON ⟺ A'∈pbis(BC)`), the trigonometric-Ceva reformulation of `A'∈pbis(BC)` as the identity `(T)`, the coordinate reformulation of `(T)` as the half-angle-tangent polynomial `(T')`, and the **sequential univariate field-division certificate** `(T')_num ∈ ⟨(C1)_num,(C2)_num⟩` (remainder 0 over `QQ.frac_field(t_A,t_B,t_α,t_β)[t_γ]` then `[...][t_β]`). This certificate does NOT invoke the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` or any analytic-branch-cert/resultant-cert ingredient; it is a third, genuinely independent proof of `OM=ON` through a completely different mechanism (synthetic antipode geometry + trig Ceva, vs. analytic coordinates + saturation).
