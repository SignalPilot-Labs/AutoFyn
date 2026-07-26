## Status
solved

## Framing (1 sentence)
Same verified analytic prefix as `analytic-branch-cert` (coordinates `A=0,B=b,C=(u,v)`; `OM=ON⇔Q=0`; directed-angle polynomials `e1,e2,e3`; 2-var reduction to the cubic `D₀(L)=0` and the line `K=B+t·d(L)`; field-reduced quadratics `e3_line,Q_line` in `t`), but closed by a **different certificate**: the resultant-in-`t` `res_t(e3_line,Q_line)` factors as `(b⁸/16)v²|C|²(|C|²−b²)·D₀²·R` (exact multiplicity 2, verified over the field); the discriminant `Δ_red` of `e3_line` is **not a square** in `Q(b,u,v,lx,ly)/(D₀)` (proven by a concrete real point where `Δ_red<0`), so the prime `(D₀)` is **inert** in the splitting field `L=F(√Δ)`; the inert-Galois valuation symmetry then forces `Q_line` to vanish at **both** roots of `e3_line` along `D₀=0` (the norm `res/et2²=Q_line(t₁)Q_line(t₂)` has `D₀`-valuation 2, conjugation makes the two factors equal-valued, so each has valuation 1 ⟹ both vanish); polynomiality extends this to every triangle; at the configuration (a real point of `D₀=0` with `e3_line(t₀)=0`, `et2>0`) this gives `Q_line(t₀)=0 ⟹ Q=0 ⟹ OM=ON`.

## Approaches tried
- (round 2) **NEW approach `analytic-resultant-cert` — built this round.** Reused the verified analytic prefix (the three promotable lemmas `analytic-target-line`, `angle-linearity-cubic-reduction`, `et2-on-D-zero-relation` are documented in `analytic-branch-cert.md` and were re-verified from scratch here). Independently recomputed, over the field `Q(b,u,v,lx,ly)`, the resultant `res_t(e3_line, Q_line)` and its factorisation `(b⁸/16)v²|C|²(|C|²−b²)·D₀²·R` (remainder 0 on field division by `D₀²`; `R mod D₀ ≠ 0`, so the multiplicity is **exactly 2**). Verified `D₀` irreducible over `Q(b,u,v,lx)[ly]` (sympy `factor` returns it unfactored; cross-check: at `b=1,u=0,v=2,lx=-2` the cubic `2ly³−6ly²+12ly−12 = 2(ly³−3ly²+6ly−6)` is irreducible over `Q` by the rational-root test). Verified `et2`, `R`, and the prefactor are each not divisible by `D₀`, so `v_{D₀}(res)=2` (exact) and `v_{D₀}(res/et2²)=2`. **Proved the non-split condition** (the genuinely new hard step): the discriminant `Δ=et1²−4·et2·et0` of `e3_line`, reduced mod `D₀`, is **not a square** in `K=Q(b,u,v,lx,ly)/(D₀)`. Proof by specialization: at `b=1,u=0,v=2,lx=−2`, `D₀` becomes `2ly³−6ly²+12ly−12`, which has a real root `ly₀∈(1,2)` by the intermediate-value theorem (value `−4` at `ly=1`, `+4` at `ly=2`); at that specialization `Δ_red = −(101/4)ly²+89ly−175/2`, a quadratic with discriminant `−1833/2<0` and leading coefficient `−101/4<0`, hence `<0` for every real `ly`, in particular at `ly₀`; a real square rational function is `≥0` wherever defined, so `Δ_red` is not a square in `K`. (Also `D₀∤Δ`, since `Δ_red≢0`: unramified.) Hence the prime `(D₀)` is **inert** in the quadratic splitting field `L=F(√Δ)` of `e3_line` over `F=Q(b,u,v,lx,ly)`. Closed the proof by the inert-Galois valuation argument (KB *Algebra & Polynomials — resultants / "transform the roots"* + the standard norm–valuation identity `v(Norm)=2·w` for an inert prime, KB *Linear Algebra — ideal saturation / Rabinowitsch* is NOT used here). Concluded `Q_line` vanishes at both roots of `e3_line` along `D₀=0` (generic triangle), extended to every triangle by polynomiality, hence at the configuration `Q_line(t₀)=0 ⟹ Q=0 ⟹ OM=ON`. Status: **solved**.
- (round 2, cross-check) Independently re-verified the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` (`G` linear in `t`, remainder 0 on field division over `Q(b,u,v,lx,t)[ly]`): it is TRUE. This is recorded as a cross-check / fallback for the exceptional measure-zero stratum where the generic Galois argument's open-set denominator could vanish; the present proof's **primary** certificate is the resultant+Galois argument, NOT the saturation identity (which is `analytic-branch-cert`'s route).

## Current best
The whole theorem is proved. The verified analytic prefix (coordinate normalisation, `OM=ON⇔Q=0`, the cubic `D₀(L)` + line `K=B+t·d(L)`, the field-reduced quadratics `e3_line,Q_line`, `et2>0` on the inside arc, degenerate `L=C` excluded) is imported from `analytic-branch-cert`'s certified lemmas and re-verified here. The **new** contribution is the resultant factorisation (exact `D₀²`-multiplicity), the rigorous non-split proof (`Δ_red` not a square, via a concrete real point with `Δ_red<0`), and the inert-Galois valuation closing — a genuinely different certificate from the saturation quotient `G`.

## Full proof

We prove `OM=ON` for an arbitrary non-degenerate triangle `ABC` satisfying the hypotheses.

### 1. Coordinate normalisation (similarity WLOG)

Translate, rotate, scale so that `A=(0,0)`, `B=(b,0)` with `b=|AB|>0`, `C=(u,v)` with `v>0` (reflect if needed; the statement is reflection-invariant). Non-degeneracy gives `v≠0` (take `v>0`) and `|C|²:=u²+v²>0`. Then `M=(b/2,0)`, `N=(u/2,v/2)`. The hypotheses are: `K∈△BMC` strictly (so `K≠B`); `L∈△BNC` strictly (so `L≠C`, `ly<v`); `K∈∠LBA`, `L∈∠ACK`; the three angle equalities `∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK`; and `O` circumcentre of the non-degenerate `△AKL`, so `det(K,L):=kx·ly−ky·lx≠0`. — KB *Geometry — coordinates/complex/barycentric*.

### 2. The target as a cleared polynomial (lemma `analytic-target-line`)

For `A=0`, the circumcentre `O` of `△AKL` is given by `2O·K=|K|²`, `2O·L=|L|²` (perpendicular bisectors). Cramer's rule (denominator `det(K,L)≠0`):
```
2·det(K,L)·ox = |K|²·ly − |L|²·ky,   2·det(K,L)·oy = kx·|L|² − lx·|K|².    (1)
```
Using `M=B/2`, `N=C/2`, `|M|²=|B|²/4`, `|N|²=|C|²/4`:
```
OM² − ON² = 2O·(N−M) + |M|²−|N|² = O·(C−B) + (|B|²−|C|²)/4,
```
hence `OM=ON ⇔ O·(C−B) = (|C|²−|B|²)/4`. Multiplying by `2·det(K,L)` (nonzero) and using (1), the cleared target is the polynomial
```
Q(kx,ky,lx,ly) := 2(|K|²·ly − |L|²·ky)(u−b) + 2(kx·|L|² − lx·|K|²)·v − det(K,L)(|C|²−|B|²).   (Q)
```
Then `OM=ON ⇔ Q=0` (given `det(K,L)≠0`). ∎ (lemma `analytic-target-line`, verified by direct expansion).

### 3. Directed-angle encoding (lemma `angle-linearity-cubic-reduction`, prefix)

For directed angles, `∠(p,q)=∠(r,s) mod π` is encoded (KB *Algebra & Polynomials — minimal-polynomial reduction*; tangent form) by `cross(p,q)·dot(r,s) − cross(r,s)·dot(p,q)=0`. Applying this to the three equalities gives polynomials `e1,e2,e3∈Z[b,u,v][kx,ky,lx,ly]`:
- `e1` from `∠KBA=∠ACL` (rays `BK,BA` and `CA,CL`);
- `e2` from `∠LBK=∠LNC` (rays `BL,BK` and `NL,NC`);
- `e3` from `∠LCK=∠BMK` (rays `CL,CK` and `MB,MK`).

The configuration satisfies `e1=e2=e3=0`.

**Lemma 1 (homogeneous linearity in `K−B`).** Write `K=B+(sx,sy)`. Then `e1=a1·sx+b1·sy`, `e2=a2·sx+b2·sy` with **zero constant terms** `c1=c2≡0`, where `a1,b1,a2,b2∈Q(b,u,v)[lx,ly]`. *(The zero constants reflect that `K=B` makes `∠KBA` and `∠LBK` degenerate; verified in `sympy` by collecting `e1,e2` in `(sx,sy)`.)* ∎

### 4. Reduction to the cubic `D₀(L)=0` and the line `K=B+t·d(L)` (lemma `angle-linearity-cubic-reduction`)

By Lemma 1, `e1=e2=0` is a homogeneous `2×2` linear system in `(sx,sy)`. Since `K≠B`, it has a nontrivial solution, so its determinant vanishes:
```
D(L) := a1·b2 − b1·a2 = 0.
```
`sympy` factorisation (verified by direct division over `Q(b,u,v,lx,ly)`):
```
D(L) = −(b/4)·|C|²·D₀(L),
D₀(L) := b·lx·v − b·ly·u + 2·lx²·ly − lx²·v − 2·lx·ly·u + 2·ly³ − 3·ly²·v + ly·u² + ly·v².   (D₀)
```
The scalar `−(b/4)·|C|²` is nonzero (`b>0`, `|C|²>0`), so `D(L)=0 ⇔ D₀(L)=0`.

**Lemma 2 (irreducibility of `D₀`).** `D₀` is irreducible over `Q[b,u,v,lx,ly]` (hence `(D₀)` is a height-one prime in the UFD `Q[b,u,v,lx,ly]`, and the discrete valuation `v_{D₀}` is well-defined).

*Proof.* As a polynomial in `ly` over `Q(b,u,v,lx)` (leading coefficient `2`, a unit), `D₀` is a cubic; it is reducible iff it has a root in `Q(b,u,v,lx)`. `sympy.factor(D₀, domain=QQ.frac_field(b,u,v,lx))` returns `D₀` unfactored, so it has no linear-in-`ly` factor. The content (gcd of the `ly`-coefficients `2, −3v, −bu+2lx²−2lxu+u²+v², blxv−lx²v`) is `1`, so `D₀` is primitive; by Gauss's lemma no factor of `ly`-degree `0` exists either. Hence `D₀` is irreducible over `Q(b,u,v,lx)[ly]`, equivalently over `Q[b,u,v,lx,ly]`. (Independent cross-check: at the specialization `b=1,u=0,v=2,lx=−2`, `D₀` becomes `2(ly³−3ly²+6ly−6)`, and `ly³−3ly²+6ly−6` is irreducible over `Q` — its only rational-root candidates `±1,±2,±3,±6` are all non-roots. A reducible polynomial over a function field would specialize to a reducible polynomial at a generic point; this specialization is irreducible, consistent with — and supporting — the generic irreducibility.) ∎

With `D₀(L)=0`, the matrix in the linear system has rank `1`, so its kernel is the `1`-dimensional span of `d(L):=(b1,−a1)` (one checks `a1·b1+b1·(−a1)=0`). Hence
```
K = B + t·d(L) = (b + t·b1, t·(−a1))    (3)
```
for a real `t` (fixed by the third angle condition `e3=0` below). Substituting (3) into `e1,e2`: `e1|_{(3)}≡0` (since `d` spans the kernel of row `1`), and `e2|_{(3)} = −t·D` (verified: `a2·b1 + b2·(−a1)=−D`). Hence on `D₀=0`, `e1≡0` and `e2≡0` for every `t`. ∎

### 5. The third condition and the cleared target on the line

Substitute (3) into `e3` and `Q`; field-reduce modulo `D₀` (over `Q(b,u,v,lx,t)[ly]`, using `sp.Poly(...,ly,domain=QQ.frac_field(b,u,v,lx,t))` — KB *Algebra & Polynomials — minimal-polynomial reduction*; the leading coefficient `2` of `D₀` (in `ly`) is a unit in `Q`, so this is true field division, not a pseudo-remainder). Write the remainders (values on `D₀=0`) as quadratics in `t`:
```
e3_line(lx,ly,t) = et2·t² + et1·t + et0,   Q_line(lx,ly,t) = Qt2·t² + Qt1·t + Qt0.   (line)
```
Both are quadratic in `t` (the cubic `e3` is at most quadratic in `K` via the single `|K|²` term; `Q` is quadratic in `K`). The angle condition `e3=0` becomes `e3_line=0` on `D₀=0`.

**Lemma 3 (the `t²`-coefficient `et2`; lemma `et2-on-D-zero-relation`).** The genuine polynomial identity (verified by direct subtraction over `Q(b,u,v,lx,t)`):
```
et2 = (b³/2)·|C|²·(v−ly)·|L−C|²  −  b²·D(L).   (et2)
```
Hence **on `D₀=0`** (where `D=−(b/4)|C|²·D₀=0`):
```
et2|_{D₀=0} = (b³/2)·|C|²·(v−ly)·|L−C|².
```

*Proof.* `et2 − [(b³/2)|C|²(v−ly)|L−C|² − b²·D] ≡ 0` over `Q(b,u,v,lx,t)`, verified by direct subtraction (not `factor` — the displayed factorisation holds *on `D₀=0`*, not as a standalone identity; the exact identity is (et2)). ∎

### 6. `et2>0` on the inside arc; degenerate exclusion (Lemmas 5, 6)

**Lemma 5 (`et2>0` on the inside arc, on `D₀=0`).** At the configuration `D₀(L)=0`, so by Lemma 3 `et2 = (b³/2)·|C|²·(v−ly)·|L−C|²`. The hypotheses `L∈△BNC` strictly, `b>0`, `v>0`, `|C|²>0` give: (i) `ly<v` (write `L` in barycentrics `L=λ_B B+λ_N N+λ_C C` with `λ_B,λ_N,λ_C>0`, `Σλ=1`; then `ly=λ_N v/2+λ_C v=(1−λ_B−λ_N/2)v<v` since `λ_B>0`); (ii) `|L−C|²>0` (else `L=C`, contradicting strict interiority). Hence `et2>0`. ∎

**Lemma 6 (degenerate component `L=C`).** `d(L)=0 ⇔ L=C` (since `e1` identically zero in `K` forces `dot(A−C,L−C)=cross(A−C,L−C)=0`, possible only if `L−C=0`). At `L=C`, `e3_line≡0` for all `t`, `Q_line=b·v·(|C|²−|B|²)`, and `K=B+t·d(C)=B`. This entire component `{(K,L)=(B,C)}` is excluded by `K∈△BMC` strictly (`K≠B`) and `L∈△BNC` strictly (`L≠C`). ∎

### 7. THE RESULTANT CERTIFICATE (the different closing step)

We now close by the **resultant-in-`t`** of `e3_line` and `Q_line`, NOT by the saturation quotient `G` (which is `analytic-branch-cert`'s route).

**Proposition 7 (resultant factorisation).** Over the field `Q(b,u,v,lx,ly)`,
```
res_t(e3_line, Q_line) = (b⁸/16)·v²·(u²+v²)·(u²+v²−b²)·D₀(L)²·R(lx,ly,u,v,b),   (RES)
```
where `R` is the explicit polynomial
```
R = −b²(u²+v²) − 3b·lx²·u − 3b·lx·ly·v + 4b·lx·u² + b·lx·v² + 3b·ly·u·v − b·u³ − b·u·v²
   + 9·lx²·u² + 18·lx·ly·u·v − 12·lx·u³ − 12·lx·u·v² + 9·ly²·v² − 12·ly·u²·v − 12·ly·v³
   + 4·u⁴ + 8·u²·v² + 4·v⁴.
```
The factor `D₀²` is **exact** (multiplicity 2): `R mod D₀ ≠ 0`, and the prefactor `(b⁸/16)v²|C|²(|C|²−b²)` is not divisible by `D₀` (it is constant in `(lx,ly)`).

*Proof.* Computed with `sp.resultant(Poly(e3_line,t,domain=QQ.frac_field(b,u,v,lx,ly)), Poly(Q_line,t,...))`; the displayed factorisation is `sp.factor(res)`. Exact multiplicity: field-division of `res` by `D₀²` (as `Poly(...,ly,domain=QQ.frac_field(b,u,v,lx))`) leaves remainder `0`, and field-division of `R` by `D₀` leaves a **nonzero** remainder (so `R` is not divisible by `D₀`, i.e. the `D₀`-multiplicity in `res` is exactly `2`). The prefactor is constant in `(lx,ly)` and nonzero generically, so not divisible by `D₀`. ∎

**Corollary 8 (`D₀² | res` ⟹ a common root on `D₀=0`).** By the fundamental property of the resultant (KB *Algebra & Polynomials — resultants / "transform the roots"*), `res_t(f,g)=0` iff `f,g` share a common root in `t` over the algebraic closure. Since `D₀² | res`, at every point of `D₀=0` (over the algebraic closure) `e3_line` and `Q_line` share at least one common root in `t`. (This is the *existential* content; the *selection* — that the configuration's root is shared — is closed in §8–9 below.) ∎

### 8. The non-split condition (the key structural fact)

Let `F=Q(b,u,v,lx,ly)` and let `Δ = et1²−4·et2·et0` be the discriminant of `e3_line` (as a quadratic in `t`). Let `Δ_red` be the reduction of `Δ` modulo `D₀` (an element of the residue function field `κ = F/(D₀) = Q(b,u,v,lx,ly)/(D₀)`).

**Lemma 9 (non-split + unramified).** (a) `D₀ ∤ Δ` (i.e. `Δ_red ≢ 0`): `e3_line` has **distinct** roots at the generic point of `D₀=0`. (b) `Δ_red` is **not a square** in `κ`. Consequently the prime `(D₀)` is **inert** (unramified, residue degree `2`, a single prime above it) in the splitting field `L=F(√Δ)` of `e3_line`.

*Proof.* (a) Field-reduce `Δ` modulo `D₀` (as `Poly(Δ,ly,domain=QQ.frac_field(b,u,v,lx,t))` divided by `D₀`): the remainder `Δ_red` is nonzero (verified: `Δ_red` is a nonzero polynomial of degree `4` in `lx`), so `D₀∤Δ`.

(b) We prove `Δ_red` is not a square in `κ` by specialization. Suppose `Δ_red = f²` in `κ` for some `f∈κ`. Specialize `b=1,u=0,v=2` (a ring homomorphism `κ→κ_s := Q(lx,ly)/(D₀_s)`, where `D₀_s = D₀|_{b=1,u=0,v=2}` is nonzero, so the specialization is well-defined). Then `Δ_red|_s = (f|_s)²` in `κ_s = Q(lx,ly)/(D₀_s)`. A square in `κ_s`, viewed as a rational function on the real curve `D₀_s=0`, is `≥0` wherever defined (it is the square of a real-valued function). Now specialize further to `lx=−2` (rational). Then `D₀_s|_{lx=−2} = 2·ly³−6·ly²+12·ly−12`; this cubic takes value `−4` at `ly=1` and `+4` at `ly=2`, so by the intermediate-value theorem it has a real root `ly₀∈(1,2)`. At this specialization, `Δ_red` becomes
```
Δ_red|_{b=1,u=0,v=2,lx=−2} = −(101/4)·ly² + 89·ly − 175/2   (verified by direct substitution + reduction mod the cubic)
```
— a quadratic in `ly` with discriminant `89² − 4·(−101/4)·(−175/2) = 7921 − 17705/2 = (15842−17705)/2 = −1833/2 < 0` and leading coefficient `−101/4 < 0`. Hence this quadratic is **strictly negative for every real `ly`**; in particular `Δ_red(lx=−2, ly₀) < 0`. (Cross-check: `Delta(lx=−2,ly) mod D₀(lx=−2,ly)` over `Q` equals the displayed quadratic — the reduction commutes with specialization.) This negative value contradicts `Δ_red|_s` being a square (squares are `≥0` at real points). Hence `Δ_red` is not a square in `κ`. 

(c) `Δ` is not a square in `F` either: if `Δ=g²` in `F`, then reducing mod `D₀` gives `Δ_red = (g mod D₀)²` in `κ`, a square — contradicting (b). Hence `L=F(√Δ)` is a genuine quadratic field extension of `F` (the splitting field of `e3_line`, since its roots are `(−et1±√Δ)/(2·et2)`). 

A quadratic prime `(D₀)` in `F` is unramified in `L=F(√Δ)` iff `v_{D₀}(Δ)=0`, i.e. `D₀∤Δ` — established in (a). It is inert (non-split, a single prime above, residue degree `2`) iff `Δ_red` is not a square in the residue field `κ` — established in (b). (The ramification index `e=1`; the residue degree `f=2`; `g=1` prime above; `L/F` is Galois since `char F=0`.) ∎

### 9. The inert-Galois closing: `Q_line` vanishes at both roots of `e3_line` on `D₀=0`

Work at the generic point, over `F=Q(b,u,v,lx,ly)`. Let `t₁,t₂` be the roots of `e3_line` (in the splitting field `L=F(√Δ)`; by Lemma 9, `L/F` is a quadratic Galois extension with `Gal(L/F)={1,σ}`, `σ(t₁)=t₂`, `σ(t₂)=t₁`). Let `w` be the extension of `v_{D₀}` to `L`; since `(D₀)` is inert, `w|_F = v_{D₀}` (ramification index `e=1`) and `σ` fixes the unique prime above `(D₀)`, so `w∘σ = w`.

The standard resultant identity (KB *resultants / "transform the roots"*; `f=e3_line` degree `2`, `g=Q_line` degree `2`, `deg f·deg g=4` even so the sign is `+`):
```
res_t(e3_line, Q_line) = et2² · Q_line(t₁) · Q_line(t₂) = et2² · Norm_{L/F}(Q_line(t₁)).   (NORM)
```
(Indeed `res_t(f,g) = lc(f)^{deg g} · ∏_i g(t_i)`, and `∏_i g(t_i) = g(t₁)g(t₂) = g(t₁)·σ(g(t₁)) = Norm(g(t₁))`.)

Now evaluate `v_{D₀}`-valuations. By Proposition 7, `v_{D₀}(res) = 2·v_{D₀}(D₀) + v_{D₀}(R) + v_{D₀}(\text{prefactor}) = 2+0+0 = 2` (exact, since `R`, the prefactor are not divisible by `D₀` — at the generic triangle where the prefactor `(b⁸/16)v²|C|²(|C|²−b²)≠0`). By Lemma 3, `et2 = (b³/2)|C|²(v−ly)|L−C|² − b²·D`, so `et2 mod D₀ = (b³/2)|C|²(v−ly)|L−C|² ≢ 0` in `κ` (it is a nonzero polynomial, not divisible by `D₀`), hence `v_{D₀}(et2)=0`, `v_{D₀}(et2²)=0`. Therefore
```
v_{D₀}( res/et2² ) = v_{D₀}(res) − v_{D₀}(et2²) = 2 − 0 = 2.   (V)
```
By (NORM), `res/et2² = Norm_{L/F}(Q_line(t₁))`. The norm–valuation identity for the **inert** prime (single prime above `(D₀)`, `e=1`, `σ` fixes `w`):
```
v_{D₀}(Norm_{L/F}(α)) = w(α) + w(σ(α)) = 2·w(α)   (for all α∈L),
```
since `w∘σ=w`. Applying to `α=Q_line(t₁)`:
```
2  =  v_{D₀}(Norm(Q_line(t₁)))  =  2·w(Q_line(t₁)),   hence   w(Q_line(t₁)) = 1 > 0.   (W)
```
So `Q_line(t₁)` lies in the maximal ideal of the valuation ring of `w` — i.e. `Q_line(t₁)` is divisible by `D₀` (the uniformizer) in the local ring of `L` at the prime above `(D₀)`. By `σ`-conjugation,
```
w(Q_line(t₂)) = w(σ(Q_line(t₁))) = w(Q_line(t₁)) = 1 > 0.   (W')
```
Hence **both** `Q_line(t₁)` and `Q_line(t₂)` vanish (to order `1`) along `D₀=0`, at the generic point.

**Consequence (generic vanishing).** At the generic point of `D₀=0`, `Q_line(t₁)=Q_line(t₂)=0` as algebraic functions. Equivalently: for the generic triangle (over `Q(b,u,v)`), at every point `(lx,ly)` of `D₀=0` at which `e3_line` has distinct roots, `Q_line` vanishes at **both** roots of `e3_line`. (At the finitely-many points where `Δ=0` on `D₀=0` — a double root — the vanishing extends by continuity, since `Q_line(t₁),Q_line(t₂)→Q_line(t₀)` there.) By the Nullstellensatz over `Q(b,u,v)`, this is the ideal-membership statement
```
Q_line  ∈  rad( D₀,  e3_line )   over  Q(b,u,v)[lx,ly,t].   (∗)
```

### 10. From generic to every triangle (polynomiality)

The statement (∗), "for the generic triangle, `Q_line` vanishes on the variety `{D₀=0, e3_line=0}` over the algebraic closure," is — after clearing the (finitely many) denominators that arise in the inert-Galois valuation argument — a **polynomial identity** in `Q[b,u,v,lx,ly,t]` (a member of `rad(D₀,e3_line)`). A polynomial identity that holds at the generic point of `Spec Q[b,u,v]` (i.e. over `Q(b,u,v)`) holds on a Zariski-dense open subset of `Spec Q[b,u,v]`; the locus where it holds is Zariski-closed, hence it is all of `Spec Q[b,u,v]`. Equivalently: (∗) specializes to every triangle `(b,u,v)` (including the measure-zero exceptional strata — e.g. the isosceles triangle `|C|²=b²` where the prefactor `(b⁸/16)v²|C|²(|C|²−b²)` vanishes and the generic-valuation count `v_{D₀}(res)=2` is no longer exact). At such exceptional triangles the inert-Galois count of §9 is not directly applicable (the prefactor vanishes), but the **polynomial identity (∗)** — established generically and extended by Zariski-density — continues to hold, giving `Q_line∈rad(D₀,e3_line)` there too.

(Independently re-verified cross-check: the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` with `G` linear in `t` holds as a polynomial identity over `Q(b,u,v,lx,ly)` — remainder `0` on field division over `Q(b,u,v,lx,t)[ly]` — with **no** assumption on `|C|²` vs `b²`; it gives the explicit, denominator-free form of (∗) and confirms the exceptional strata. The present proof's primary certificate is the resultant+Galois argument of §7–9; the saturation identity is recorded only as this cross-check/fallback.)

### 11. Conclusion

Let `(K,L)` satisfy all the hypotheses. Then:
- `e1=e2=e3=0` (the three angle equalities);
- `K≠B` (strict `K∈△BMC`), so by Lemma 1 + (3), `D₀(L)=0` and `K=B+t₀·d(L)` for the real `t₀` fixed by the configuration;
- `e3_line(lx,ly,t₀)=0` (the third angle condition, reduced mod `D₀`);
- `et2>0` at the configuration (Lemma 5), so `et2≠0`, `e3_line` is genuinely quadratic in `t`, and `t₀` is a root of `e3_line` (a genuine root, not the degenerate `L=C,K=B` component of Lemma 6, which is excluded).

The configuration point `(b,u,v,lx,ly,t₀)` lies on the variety `{D₀=0, e3_line=0}`. By (∗) (extended to every triangle in §10), `Q_line` vanishes on this variety; in particular
```
Q_line(lx,ly,t₀) = 0.
```
Since `Q_line` is the field-reduction of `Q` modulo `D₀` (so `Q = Q_line` on `D₀=0`), `Q(K,L)=0`. By the equivalence `OM=ON ⇔ Q=0` of §2 (valid since `det(K,L)≠0`, as `O` is the circumcentre of non-degenerate `△AKL`), we conclude
```
OM = ON.   ∎
```

### Reproducibility note

All algebraic claims are verified in `sympy` with `b,u,v` (and `lx,t`) kept as **free indeterminates**, working over the **field** `Q(b,u,v,lx,t)[ly]` (via `sp.Poly(...,ly,domain=QQ.frac_field(b,u,v,lx,t))`) — not over the ring `Z[b,u,v,lx,t][ly]` (whose pseudo-remainder can mislead). What `sympy` confirms, parameter-free:
- **build** `e1,e2,e3,Q` from the cross/dot formula; **confirm** `c1=c2≡0` (Lemma 1) and `e2|_{(3)}=−t·D` (Lemma 4);
- **factor** `D=−(b/4)|C|²·D₀`; **`D₀` irreducible** over `Q(b,u,v,lx)[ly]` (`factor` returns unfactored);
- **Lemma 3** by DIRECT SUBTRACTION: `et2−((b³/2)|C|²(v−ly)|L−C|² − b²·D)≡0` over `Q(b,u,v,lx,t)`;
- **Proposition 7** resultant: `sp.factor(sp.resultant(...))` gives the displayed `D₀²·R` factorisation; field-division of `res` by `D₀²` leaves remainder `0`; field-division of `R` by `D₀` leaves a **nonzero** remainder (exact multiplicity `2`); prefactor and `et2` each not divisible by `D₀`;
- **Lemma 9(a)** `Δ_red≡Δ mod D₀ ≢0` (field-reduction remainder nonzero); **Lemma 9(b)** non-square: at `b=1,u=0,v=2,lx=−2`, `D₀` is `2ly³−6ly²+12ly−12` (real root `ly₀∈(1,2)` by IVT), `Δ_red=−101ly²/4+89ly−175/2` (discriminant `−1833/2<0`, leading coeff `<0`, hence `<0` for all real `ly`);
- **Lemmas 5,6** by `sympy` evaluation at `L=C` and the barycentric sign argument;
- **Norm identity** (NORM): `res_t(f,g)=lc(f)^{deg g}∏g(t_i)` is the standard resultant theorem (KB *resultants*); `Q_line(t₁)Q_line(t₂)=Norm_{L/F}(Q_line(t₁))` holds because `σ(t₁)=t₂` and `σ(Q_line(t₁))=Q_line(t₂)`.

The symbolic computation over the field is parameter-free, so every verified identity holds simultaneously for all non-degenerate triangles (`b>0, v>0, |C|²>0`); the generic-to-all extension (§10) covers the exceptional strata.

## Promotable lemmas
- **`analytic-target-line`** (imported from `analytic-branch-cert`, re-verified): *With `A` at the origin, `OM=ON ⇔ O·(C−B)=(|C|²−|B|²)/4 ⇔ Q=0` (for `det(K,L)≠0`).* — proved in §2.
- **`angle-linearity-cubic-reduction`** (imported, re-verified): *`e1,e2` homogeneous-linear in `K−B`; `D(L)=−(b/4)|C|²·D₀(L)`; `K=B+t·d(L)`; on `D₀=0`, `e1≡0`, `e2=−t·D`.* — proved in §3–4.
- **`et2-on-D-zero-relation`** (imported, re-verified): *`et2=(b³/2)|C|²(v−ly)|L−C|² − b²·D`, strictly positive on `△BNC` (on `D₀=0`).* — proved in §5–6.
- **`resultant-D0-square-factor`** (NEW, this round, primary new contribution): *Over `Q(b,u,v,lx,ly)`, `res_t(e3_line,Q_line)=(b⁸/16)v²|C|²(|C|²−b²)·D₀²·R` with `D₀²` exact (multiplicity 2; `R mod D₀≠0`). Consequently on `D₀=0`, `e3_line` and `Q_line` share a common root in `t` (over the algebraic closure).* — proved in §7 (field-verified).
- **`D0-irreducible`** (NEW, this round): *`D₀` is irreducible over `Q[b,u,v,lx,ly]`; `(D₀)` is a height-one prime, `v_{D₀}` is a well-defined discrete valuation.* — proved in §4 (Lemma 2).
- **`e3line-splitting-nonsplit-at-D0`** (NEW, this round, the key structural fact): *The discriminant `Δ=et1²−4·et2·et0` of `e3_line`, reduced mod `D₀`, is **not a square** in `κ=Q(b,u,v,lx,ly)/(D₀)`, and `D₀∤Δ`. Hence the prime `(D₀)` is **inert** in the splitting field `L=F(√Δ)` of `e3_line.* — proved in §8 (Lemma 9) by a concrete specialization (`b=1,u=0,v=2,lx=−2`) at which `Δ_red<0` at a real point of `D₀=0`.
- **`resultant-galois-both-roots-shared`** (NEW, this round, the closing certificate): *For the generic triangle, the inert-Galois valuation symmetry forces `Q_line` to vanish at **both** roots of `e3_line` along `D₀=0` (the norm `res/et2²=Norm(Q_line(t₁))` has `v_{D₀}=2`; conjugation gives `w(Q_line(t₁))=w(Q_line(t₂))`, so each `=1>0`). By polynomiality this extends to every triangle. Hence at any configuration point `Q_line(t₀)=0 ⟹ Q=0 ⟹ OM=ON`.* — proved in §9–11. (This is the genuinely different certificate vs the saturation quotient `G`; it uses the resultant's exact `D₀²`-multiplicity + the non-split Galois argument, not an explicit `G`.)
