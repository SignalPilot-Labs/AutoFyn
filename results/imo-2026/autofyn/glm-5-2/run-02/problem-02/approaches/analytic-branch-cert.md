## Status
solved

## Framing (1 sentence)
Place `A` at the origin, `B=(b,0)`, `C=(u,v)`; the directed-angle encodings `e1,e2` of `∠KBA=∠ACL` and `∠LBK=∠LNC` are homogeneous-linear in `K−B`, so for `K≠B` the determinant vanishes, giving the cubic `D₀(L)=0` and the line `K=B+t·d(L)`; substituting into `e3` (the third angle) and the cleared target `Q` (`OM=ON ⟺ Q=0`) and field-reducing modulo `D₀` (over `Q(b,u,v,lx,t)[ly]`) yields quadratics `e3_line, Q_line` in `t` whose `t²`-leading coefficients `et2, Qt2` satisfy the **verified polynomial identity** `Qt2·e3_line − et2·Q_line = D₀·G` (with `G` linear in `t`, explicit quotient, remainder `0` by true field division); on `D₀=0` this gives `et2·Q_line = Qt2·e3_line = 0`, and since `et2 = (b³/2)·|C|²·(v−ly)·|L−C|² > 0` on the inside arc `L∈△BNC`, we get `Q_line=0`, hence `Q=0`, hence `OM=ON`.

## Approaches tried
- (round 1) Original outline proposed "P ∈ ⟨D(L), e3_sub⟩ as ideal membership" — FALSE (Gröbner remainder nonzero, Rabinowitsch fails). Reduction (2-var cubic+line) and real-variety vanishing retained.
- (round 2 draft) Replaced the false ideal-membership by a saturation identity `Qt2·e3_line − et2·Q_line = D·G`. Initially certified by ring pseudo-remainder.
- (round 1 fix-pass) Reviewer overruled `solved → partial`: Lemma 3 was mis-stated as an exact polynomial factorisation (it holds only ON `D=0`); re-verified the genuine identity is `et2 = (b³/2)|C|²(v−ly)|L−C|² − b²·D(L)`. **Also reported the saturation identity (Prop 4) FALSE** with an explicit counterexample `b=4,u=1,v=3,lx=1/2,ly=7/2,t=1/3` claiming `Q=256` gave nonzero LHS.
- (round 2, this round) **The round-1 "FALSE" verdict on Prop 4 was itself an arithmetic slip.** Two independent from-scratch re-verifications (complex explorer + outline-reviewer, and now the builder's own — see Reproducibility note below) confirm: at the alleged counterexample point, recomputing the cleared target `Q` from its defining formula gives `Q = 320/3`, NOT `256` (the slip was in the round-1 evaluation of `Q`). With the corrected `Q`, `Qt2·e3_line − et2·Q_line` evaluates to `0` at that point (verified: the full polynomial-in-`t` `Qt2·e3 − et2·Q` is identically `0` there because `D₀=0` there and the saturation identity holds). True field division `sp.div(Poly(LHS, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=...))` returns remainder `0` with an explicit quotient `G` that IS linear in `t` (degree `1` in `t`) — I re-derived the clean factored form `G = (b⁴·v·|C|²/4)·[t·(…) + (…)]` and confirmed `LHS − D₀·G_prop ≡ 0` over the field. Lemma 3 restated in its corrected on-`D=0` form. Status: **solved**.

## Current best
The complete rigorous proof below. The reduction machinery (Sections 1–5), the saturation identity (Proposition 4, Section 6 — verified TRUE by true field division with explicit `G` linear in `t`), the positivity `et2>0` on the inside arc (Lemma 5, Section 7), and the degenerate-component exclusion (Lemma 6, Section 7) together close the proof: on the inside arc, `D₀=0` and `e3_line=0` and `et2>0` force `Q_line=0`, hence `Q=0`, hence `OM=ON`.

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
Write `K = (kx, ky)`, `L = (lx, ly)`. The hypotheses we use are:
- the three (ordinary) angle equalities `∠KBA = ∠ACL`, `∠LBK = ∠LNC`, `∠LCK = ∠BMK`;
- `K` strictly inside `△BMC` (so in particular `K ≠ B`, since `B` is a vertex of `△BMC`);
- `L` strictly inside `△BNC` (so `L ≠ C` and `ly < v` — Lemma 5 below);
- `O` is the circumcentre of `△AKL`, so `A, K, L` are non-collinear: `det(K,L) := kx·ly − ky·lx ≠ 0`.

(The hypotheses `K ∈ ∠LBA` and `L ∈ ∠ACK` are ordinary-angle branch-selection conditions; they are not separately needed for the algebraic certificate below, since ordinary-angle equality implies directed-angle equality mod `π`, which is what we encode.)

### 2. The target as a linear equation in `O` (the `analytic-target-line` lemma)

For `A = 0`, the circumcentre `O = (ox, oy)` of `△AKL` is determined by the two perpendicular-bisector equations `2·O·K = |K|²`, `2·O·L = |L|²`. Solving the `2×2` system (Cramer's rule, denominator `det(K,L) ≠ 0`):
```
2·det(K,L)·ox = |K|²·ly − |L|²·ky,
2·det(K,L)·oy = kx·|L|² − lx·|K|².        (1)
```
A direct expansion (using `M = B/2`, `N = C/2`, so `N − M = (C−B)/2`, `|M|² = |B|²/4`, `|N|² = |C|²/4`) gives
```
OM² − ON² = |O − M|² − |O − N|² = 2·O·(N − M) + |M|² − |N|²
          = O·(C − B) + (|B|² − |C|²)/4.
```
Hence
```
OM = ON  ⟺  O·(C − B) = (|C|² − |B|²)/4.        (T)
```
Multiply (T) by `2·det(K,L)` (nonzero) and use (1); writing `|C|² = u² + v²`, `|B|² = b²`, `C − B = (u − b, v)`, the cleared target is the polynomial
```
Q(kx,ky,lx,ly) := 2·(|K|²·ly − |L|²·ky)·(u − b)
                + 2·(kx·|L|² − lx·|K|²)·v
                − (kx·ly − ky·lx)·(|C|² − |B|²).        (Q)
```
Then
> **`OM = ON  ⟺  Q = 0`  (given `det(K,L) ≠ 0`).**

This is the `analytic-target-line` promotable lemma.

### 3. Encoding the angle equalities as polynomials

For two directed angles `∠(p,q)` and `∠(r,s)` (rays `p→q`, `r→s`), the equality `∠(p,q) = ∠(r,s) mod π` is equivalent (KB: *tangent of directed angle*; the cross/dot form encodes `tan(∠) = cross/dot`) to
```
cross(p,q)·dot(r,s) − cross(r,s)·dot(p,q) = 0,        (†)
```
where `cross((x₁,y₁),(x₂,y₂)) = x₁y₂ − y₁x₂`, `dot = x₁x₂ + y₁y₂`. (When both dot products vanish, the equality is interpreted by continuity; the polynomial (†) is the Zariski-closed encoding of directed-angle equality `mod π`, and ordinary-angle equality implies it.) Applying (†) to the three given equalities gives polynomials `e1, e2, e3` in `kx, ky, lx, ly` with coefficients in `Z[b,u,v]`:
- `e1` from `∠KBA = ∠ACL`: rays `BK, BA` and `CA, CL`, i.e.
  `e1 = cross(K−B, A−B)·dot(A−C, L−C) − cross(A−C, L−C)·dot(K−B, A−B)`;
- `e2` from `∠LBK = ∠LNC`: rays `BL, BK` and `NL, NC`;
- `e3` from `∠LCK = ∠BMK`: rays `CL, CK` and `MB, MK`.

The configuration satisfies `e1 = e2 = e3 = 0`.

### 4. Reduction to a cubic in `L` and a line in `K` (the `angle-linearity-cubic-reduction` lemma)

Write `K = B + (sx, sy)`, i.e. `kx = b + sx`, `ky = sy`. A direct collection of terms (verified in `sympy` by `sp.Poly(e1, [sx,sy])`) gives:

> **Lemma 1 (homogeneous linearity in `K − B`).** `e1` and `e2`, regarded as polynomials in `(sx, sy)` over `Q(b,u,v)[lx,ly]`, are **homogeneous linear**: `e1 = a1·sx + b1·sy`, `e2 = a2·sx + b2·sy`, with **zero constant terms**. Here `a1, b1, a2, b2 ∈ Q(b,u,v)[lx,ly]` are explicit.

(The zero constants reflect that `K = B` always makes both `∠KBA` and `∠LBK` degenerate — the trivial branch.)

By Lemma 1, `e1 = e2 = 0` is a `2×2` **homogeneous** linear system in `(sx, sy) = K − B`:
```
[ a1  b1 ] [sx]   [0]
[ a2  b2 ] [sy] = [0].        (2)
```
Since `K ≠ B` (hypothesis), the system has a non-trivial solution, so its determinant vanishes:
```
D(L) := a1·b2 − b1·a2 = 0.        (D)
```
A `sympy` factorisation gives
```
D(L) = −(b/4)·|C|² · D₀(L),
D₀(L) := b·lx·v − b·ly·u + 2·lx²·ly − lx²·v − 2·lx·ly·u + 2·ly³ − 3·ly²·v + ly·u² + ly·v².        (D₀)
```
The scalar `−(b/4)·|C|²` is non-zero (`b > 0`, `|C|² > 0`), so `D(L) = 0  ⇔  D₀(L) = 0`; `D₀` is a (generically irreducible) cubic in `(lx, ly)`.

> **Geometric meaning of `D₀` (remark, not used in the proof).** In complex coordinates with `A = 0`, `B = b` real, `C = u + iv`, `N = (u+iv)/2`, a direct computation gives
> `Im[(L − N)/((L − B)(L − C))] = −D₀(L) / (2·|L − B|²·|L − C|²)`,
> so `D₀(L) = 0  ⇔  (L − N)/((L − B)(L − C)) ∈ ℝ`. Equivalently, `D₀` is (up to the real factor `−b|C|²/4`) the determinant that expresses elimination of `K` from the two angle equalities `∠KBA = ∠ACL`, `∠LBK = ∠LNC` — the product of the corresponding "ratio is real" conditions eliminates `K` and leaves this condition on `L` alone.

With `D₀(L) = 0`, the matrix in (2) has rank `1`, so its solution space is the `1`-dimensional kernel of the first row `(a1, b1)`, namely multiples of `d(L) := (b1, −a1)` (one checks `a1·b1 + b1·(−a1) = 0`). Hence
```
K = B + t·d(L) = (b + t·b1, −t·a1)        (3)
```
for a real parameter `t`. Because `K ≠ B`, the parameter `t` is non-zero modulo the direction `d(L)` (and `d(L) ≠ 0` away from the degenerate component `L = C` — Lemma 6).

> **Lemma 2.** Substituting (3) into `e1, e2`: `e1|_{(3)} ≡ 0` identically in `t` (since `d` is the kernel of row 1), and `e2|_{(3)} = −t·D(L)` (verified in `sympy`: `a2·b1 + b2·(−a1) = −D`). Hence on `D₀ = 0`, both `e1, e2` vanish for every `t`. ∎

### 5. The third condition and the cleared target on the line

Substitute (3) into `e3` and into `Q`; call the results `e3_sub(lx,ly,t)` and `Q_sub(lx,ly,t)`. Both are **quadratic in `t`** (the cubic `e3` is at most quadratic in `K` via the single radial term `|K|²`, and `Q` is quadratic in `K`). On the curve `D₀ = 0` we work modulo `D₀` (as a polynomial in `ly`). Define `e3_line, Q_line` to be the **field-reduction remainders** of `e3_sub, Q_sub` modulo `D₀` over the field `Q(b,u,v,lx,t)[ly]` — i.e. computed by `Poly(..., ly, domain=QQ.frac_field(b,u,v,lx,t)).rem(Poly(D₀, ly, domain=...))`. Because `D₀` is monic in `ly` (leading coefficient `2`, a unit in `Q`), this field reduction agrees with reduction in the polynomial ring `Q[b,u,v,lx,t][ly]`, and the remainders are genuine polynomials in `Q[b,u,v,lx,ly,t]` of `ly`-degree `< 3`. By construction,
```
e3_sub ≡ e3_line  (mod D₀),        Q_sub ≡ Q_line  (mod D₀),
```
so at any point with `D₀ = 0`, `e3_sub = e3_line` and `Q_sub = Q_line`. Both `e3_line, Q_line` are quadratic in `t`; write
```
e3_line(lx,ly,t) = et2·t² + et1·t + et0,        (e3_line)
Q_line(lx,ly,t)  = Qt2·t² + Qt1·t + Qt0,        (Q_line)
```
where `et2, et1, et0, Qt2, Qt1, Qt0 ∈ Q[b,u,v,lx,ly]`. The third angle condition `e3 = 0` at the configuration (where `D₀ = 0`) becomes `e3_line(lx, ly, t_config) = 0`. Likewise `Q = 0` at the configuration is equivalent to `Q_line(lx, ly, t_config) = 0`.

### 6. The leading coefficients and the saturation identity (the closing certificate)

> **Lemma 3 (`et2`-on-`D=0` relation — genuine polynomial identity).** The `t²`-coefficient `et2` of the field-reduced third-angle polynomial satisfies, in `Z[b,u,v,lx,ly]`,
> ```
> et2 = (b³/2)·|C|²·(v − ly)·|L − C|²  −  b²·D(L),        (et2)
> ```
> where `|L − C|² = (lx − u)² + (ly − v)²` and `D(L) = −(b/4)·|C|²·D₀(L)`. This is verified by direct subtraction: `et2 − ((b³/2)·|C|²·(v−ly)·|L−C|² − b²·D) ≡ 0` over `Q(b,u,v,lx,t)`. **In particular, ON `D(L) = 0`** (equivalently `D₀ = 0`) the `−b²·D` term vanishes, leaving
> ```
> et2|_{D=0} = (b³/2)·|C|²·(v − ly)·|L − C|².   (on D₀=0)
> ```
> ∎

(The factorisation `et2 = (b³/2)·|C|²·(v−ly)·|L−C|²` is valid **on the curve `D = 0`**; the genuine polynomial identity in the free variables is the one with the `−b²·D` correction, as stated.)

> **Proposition 4 (the saturation identity — TRUE, verified by true field division).** The polynomial identity
> ```
> Qt2·e3_line  −  et2·Q_line  =  D₀(L)·G(lx,ly,t)        (ID)
> ```
> holds in `Q[b,u,v,lx,ly,t]`, where
> ```
> G(lx,ly,t) = (b⁴·v·|C|² / 4) · {  t · [ |C|²·(3b² + b·lx − b·u)  −  3·b²·(lx·u + ly·v) ]
>                                  + [ b² + b·lx − b·u  −  3·lx·u − 3·ly·v  +  2·|C|² ] }.
> ```
> In particular `G` is **linear in `t`** (degree `1` in `t`), and polynomial in `b,u,v,lx,ly`.

*Proof of Proposition 4.* The identity is a parameter-free polynomial identity in the indeterminates `b,u,v,lx,ly,t`. I verified it by **true field division** (not ring pseudo-remainder): forming `LHS := Qt2·e3_line − et2·Q_line` and dividing by `D₀` as polynomials in `ly` over the fraction field `Q(b,u,v,lx,t)` — `sp.div(Poly(LHS, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=QQ.frac_field(b,u,v,lx,t)))` — returns **remainder `0`** with the displayed quotient `G`. The same identity `LHS − D₀·G ≡ 0` was independently confirmed by direct symbolic simplification (`sp.simplify(LHS − D₀*G_prop) == 0`) using the factored `G` displayed above. Because `D₀` is monic in `ly` (leading coefficient `2`, a unit in `Q`), divisibility over the fraction field `Q(b,u,v,lx,t)(ly)` implies divisibility in the polynomial ring `Q[b,u,v,lx,t][ly]`, so `G` is a genuine polynomial (no denominators); the displayed expression confirms this directly.

*Why the round-1 "FALSE" verdict was an arithmetic slip (safeguard note).* Round 1 evaluated the LHS at `b=4, u=1, v=3, lx=1/2, ly=7/2` (a point with `D₀ = 0`) and `t = 1/3`, using the value `Q = 256` for the cleared target; this gave `Qt2·e3 − et2·Q ≠ 0`. Recomputing `Q` at this point **from its defining formula (Q)** with `K = (8/3, 8/3)`, `L = (1/2, 7/2)` gives `Q = 320/3`, not `256` (the slip was in the round-1 evaluation of `Q`). With the corrected `Q = 320/3`, the full polynomial-in-`t` identity `Qt2·e3 − et2·Q` is **identically `0`** at this `(b,u,v,lx,ly)` (verified: `sp.expand(Qt2·e3 − et2·Q) = 0` as a polynomial in `t`), exactly as the saturation identity predicts at a `D₀ = 0` point. (Note: `ly = 7/2 > v = 3` there, so this point is NOT inside `△BNC` and `et2 = −80 < 0`; it is irrelevant to the theorem but confirms the polynomial identity.) ∎

> **Corollary (the forcing step).** At any point with `D₀ = 0` and `e3_line = 0` and `et2 ≠ 0`:
> ```
> et2·Q_line  =  Qt2·e3_line  −  D₀·G  =  0  −  0  =  0,
> ```
> so `Q_line = 0` (dividing by the non-zero `et2`).

### 7. The branch selection: `et2 > 0` on the inside arc, and the degenerate exclusion

> **Lemma 5 (`et2` is strictly positive on the inside arc).** The configuration has `D(L) = 0` (Section 4), so by Lemma 3 the factorisation `et2 = (b³/2)·|C|²·(v − ly)·|L − C|²` is valid AT the configuration (the `−b²·D` correction in Lemma 3 vanishes on `D = 0`). Under the hypothesis `L ∈ △BNC` (strictly inside), with `b > 0`, `v > 0`, `|C|² > 0`:
> (i) `ly < v`;
> (ii) `|L − C|² > 0` (i.e. `L ≠ C`).
> Hence, evaluated at the configuration (where `D = 0`),
> ```
> et2 = (b³/2)·|C|²·(v − ly)·|L − C|²  >  0.
> ```

*Proof.* The triangle `△BNC` has vertices `B = (b,0)`, `N = (u/2, v/2)`, `C = (u,v)`. Write `L` in barycentric coordinates of `△BNC`: `L = λ_B·B + λ_N·N + λ_C·C` with `λ_B, λ_N, λ_C > 0` (strictly inside) and `λ_B + λ_N + λ_C = 1`. Then
```
ly = λ_N·(v/2) + λ_C·v = (1 − λ_B − λ_N/2)·v.
```
Since `λ_B > 0`, we have `1 − λ_B − λ_N/2 < 1`, so `ly < v` (using `v > 0`). This proves (i). For (ii), `|L − C|² = 0 ⇔ L = C`; but `L = C` would force `λ_B = λ_N = 0`, contradicting strict interiority. So `|L − C|² > 0`. ∎

> **Lemma 6 (the degenerate spurious component is `L = C`, excluded).** The only `L` at which the direction `d(L) = (b1, −a1)` vanishes is `L = C`. At `L = C`, `e3_line ≡ 0` for all `t` (so the third angle condition is vacuous) and `K = B + t·d(C) = B` for all `t`. This entire degenerate component `{(K,L) = (B,C)}` is **excluded** by the strict hypotheses `K ∈ △BMC` (`K ≠ B`) and `L ∈ △BNC` (`L ≠ C`).

*Proof.* `e1` is identically zero as a polynomial in `K` iff both `dot(A−C, L−C) = 0` and `cross(A−C, L−C) = 0`, i.e. iff `(A−C)` and `(L−C)` are simultaneously orthogonal and parallel — possible only when `L − C = 0` (since `A − C = (−u,−v) ≠ 0` by non-degeneracy). Hence `d(L) = 0 ⇔ L = C`. The claims about `e3_line` and `Q_line` at `L = C` are direct `sympy` evaluations: `d(C) = (0,0)`, `D(C) = 0`, `e3_line|_{L=C} ≡ 0`, `et2|_{L=C} = 0` (consistent with `|L − C|² = 0` in Lemma 3). The degenerate component is excluded by the strict inside-hypotheses. ∎

### 8. Conclusion

Let `(K, L)` be a configuration satisfying all the hypotheses, and let `t_config` be the real parameter for which `K = B + t_config·d(L)` (this exists by Section 4, since `D₀(L) = 0` and `d(L) ≠ 0` by Lemma 6, and is the parameter of the actual configuration point `K` on the line). Then:
- `e1 = e2 = e3 = 0` (the three angle equalities, ordinary implying directed);
- `D₀(L) = 0` (forced by `e1 = e2 = 0` and `K ≠ B`, Section 4);
- `K ≠ B` (strict `K ∈ △BMC`);
- `L ∈ △BNC` strictly, so by Lemma 5, `et2(L) > 0` on `D = 0`, in particular `et2(L) ≠ 0`;
- `det(K, L) ≠ 0` (`O` is the circumcentre of non-degenerate `△AKL`).

Because `D₀(L) = 0`, the field-reduced polynomials `e3_line, Q_line` agree with `e3_sub, Q_sub` at `(L, t_config)`. The third angle condition `e3 = 0` gives
```
e3_line(lx, ly, t_config) = 0.
```
By Proposition 4 (the saturation identity), on `D₀ = 0`:
```
et2·Q_line  =  Qt2·e3_line  −  D₀·G  =  Qt2·e3_line.
```
At `t = t_config`, `e3_line = 0`, so the right-hand side is `0`, giving `et2·Q_line(lx, ly, t_config) = 0`. Since `et2 > 0 ≠ 0` (Lemma 5), we conclude
```
Q_line(lx, ly, t_config) = 0.
```
Since `Q_line = Q_sub` on `D₀ = 0` and `Q_sub(L, t_config) = Q(K, L)`, we have `Q(K, L) = 0`. By the `analytic-target-line` lemma (Section 2), `Q = 0` (with `det(K,L) ≠ 0`) is equivalent to `OM = ON`.

Therefore `OM = ON`. ∎

### Reproducibility note (the verification, from scratch)

All algebraic claims were re-verified from scratch in `sympy` this round, working over the **field** `Q(b,u,v,lx,t)[ly]` — NOT over the ring `Z[b,u,v,lx,t][ly]`, whose non-unit leading coefficient `−(b/2)·|C|²` of `D` makes `sp.rem` return a *pseudo-remainder* that can mislead (the round-1 trap). The script `/tmp/verify_sat4.py` (reproduced from the outline-reviewer) and the builder's own `/tmp/verify_G.py`, `/tmp/verify_ce.py`, `/tmp/verify_inside.py` confirm:

1. **Build** `e1, e2, e3, Q` from the cross/dot formula (†);
2. **Confirm** homogeneous linearity `c1 = c2 ≡ 0` (Lemma 1) and `e2|_{(3)} = −t·D` (Lemma 2);
3. **Factor** `D = −(b/4)·|C|²·D₀` with the displayed `D₀`;
4. **Lemma-3 relation** by DIRECT SUBTRACTION (not `factor`): `et2 − ((b³/2)·|C|²·(v−ly)·|L−C|² − b²·D) ≡ 0` over `Q(b,u,v,lx,t)` — the genuine polynomial identity;
5. **Proposition-4 saturation identity** — VERIFIED TRUE: `sp.div(Poly(Qt2·e3_line − et2·Q_line, ly, domain=QQ.frac_field(b,u,v,lx,t)), Poly(D₀, ly, domain=QQ.frac_field(b,u,v,lx,t)))` returns **remainder `0`** with an **explicit quotient `G` of degree `1` in `t`** (the displayed factored form). Independently confirmed by `sp.simplify(LHS − D₀·G_prop) == 0`. This contradicts the round-1 "FALSE" verdict, which was based on the wrong value `Q = 256` (correct value: `Q = 320/3`) at the alleged counterexample;
6. **Counterexample numerics corrected:** at `b=4,u=1,v=3,lx=1/2,ly=7/2` (a `D₀=0` point, note NOT inside `△BNC`), `K=(8/3,8/3)`, `Q = 320/3` (recomputed from formula (Q)), and the full polynomial-in-`t` `Qt2·e3 − et2·Q ≡ 0` at this `(b,u,v,lx,ly)` — exactly as the saturation identity predicts on `D₀ = 0`;
7. **Inside-arc sampling:** 117 valid configurations (satisfying all inside hypotheses, with `K ∈ △BMC`, `L ∈ △BNC`, `D₀ = 0`, `e3 = 0`): `max|Q| ≤ 1.4e-10`, `max|OM−ON| ≤ 2.1e-6` (numerical root error), `min et2 = 0.09 > 0` — confirming the theorem and `et2 > 0` on the inside arc.

The symbolic identities (Lemma 1, the `D`-factorisation, Lemma 2, the Lemma-3 relation, Proposition 4, Lemma 6) are parameter-free, so they hold for every non-degenerate triangle (`b > 0, v > 0`) simultaneously.

## Promotable lemmas
- **`analytic-target-line`** (Section 2): *With `A` at the origin, `OM = ON ⇔ O·(C−B) = (|C|²−|B|²)/4 ⇔ the cleared polynomial `Q` of equation (Q) vanishes (for `det(K,L) ≠ 0`).* — proved in full; reusable by any coordinate approach to this problem.
- **`angle-linearity-cubic-reduction`** (Section 4, Lemmas 1–2 + equation (D₀)): *The directed-angle encoding `e1,e2` of `∠KBA=∠ACL`, `∠LBK=∠LNC` is homogeneous-linear in `K−B`; for `K≠B` the determinant `D(L)` (a cubic in `L`, factored as `−(b/4)|C|²·D₀`) vanishes, and `K=B+t·d(L)` with `d=(b1,−a1)`; on `D₀=0`, `e1|≡0` and `e2|=−t·D`.* — proved in full; the structural spine of the analytic route.
- **`et2-on-D-zero-relation`** (Section 6, Lemma 3): *The `t²`-coefficient `et2` of the field-reduced (mod `D₀`) third-angle polynomial `e3_line` satisfies the genuine polynomial identity `et2 = (b³/2)·|C|²·(v−ly)·|L−C|² − b²·D(L)`; hence ON `D=0` it factorises as `(b³/2)·|C|²·(v−ly)·|L−C|²`, strictly positive whenever `L` is strictly inside `△BNC`.* — proved in full.
- **`saturation-identity-et2-positive`** (Section 6, Proposition 4 — RESCUED from round-1's false "FALSE" verdict; now verified TRUE): *With `e3_line, Q_line` the field-reduced (mod `D₀`) quadratics in `t` (after the `K=B+t·d(L)` line reduction), the polynomial identity `Qt2·e3_line − et2·Q_line = D₀·G` holds in `Q[b,u,v,lx,ly,t]` with `G` the explicit polynomial linear in `t` displayed in Section 6 (remainder `0` by true field division over `Q(b,u,v,lx,t)[ly]`). On `D₀=0` this gives `et2·Q_line = Qt2·e3_line`; combined with `et2>0` on the inside arc `L∈△BNC` (Lemma 5) and `e3_line=0` (third angle condition), it forces `Q_line=0`, hence `Q=0`, hence `OM=ON`.* — proved in full (verified by true field division AND direct simplification; the round-1 "FALSE" verdict was an arithmetic slip in evaluating `Q`).
- **`complex-cubic-D0-reformulation`** (Section 4 remark): *With `A=0`, `B=b` real, `C=u+iv` complex, `N=C/2`, the cubic `D₀(L)=0` is equivalent to `(L−N)/((L−B)(L−C)) ∈ ℝ` (specifically `Im[(L−N)/((L−B)(L−C))] = −D₀(L)/(2·|L−B|²·|L−C|²)`).* — proved in full; the geometric meaning of the elimination cubic.
