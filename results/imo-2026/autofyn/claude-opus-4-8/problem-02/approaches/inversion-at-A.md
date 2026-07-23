## Build report

Approach **inversion-at-A** (diversity anchor, round 2). Goal: pin the image line
`ℓ*=ι(ω)` from E1–E3 and thereby prove the certified core identity.

**Headline finding (rigorous, new this round).** Carrying the inversion reformulation
through cleanly PINS the image line exactly: with `A` at the origin and inversion radius
`1`,
> `ℓ* = ι(ω)` is the line `2O·Y = 1`, where `O` is the circumcentre of `△AKL`.
This is the polar of `A` with respect to `ω`. Its intercepts on `AB`, `AC` are
`p = AP* = 1/(2O_x)` and `q = AQ* = 1/(2 O·\hat{AC})`, and the certified core identity
`pow(B)−pow(C)=(AB²−AC²)/2` is EXACTLY equivalent to
`AB/p − AC/q = (AB²−AC²)/2`, which — once `p,q` are substituted — collapses back
**identically** to `O·(B−C)=(|B|²−|C|²)/4`, i.e. to `OM=ON` itself.

**Honest structural consequence (a genuine result for the field, matching the
outline-reviewer's adversarial read).** The circle→line simplification is real and the
reformulation is exact, but the line `ℓ*` is the polar of `A`, so *pinning `ℓ*` is
equivalent to pinning `O`* — there is no free lunch: the inversion step alone does NOT
inject E1–E3. The angle conditions must still enter by locating the intercepts
`p=AP*`, `q=AQ*` **directly from the images `K*,L*`** (via the two cevian directions),
independently of `O`. I reduce that to an explicit closed form
`1/p = (AK sinψ_L − AL sinψ_K)/sin(ψ_L−ψ_K)` in the two apex directions `ψ_K=∠KAB`,
`ψ_L=∠LAB` (and the mirror for `q`), and reduce `ψ_K,ψ_L,AK,AL` to `θ,β,γ` via Law of
Sines. The residual is the same scalar identity the other approaches hit — but now
carried by a **strictly 2-DOF object (`p,q`)** with a clean geometric meaning, and with
the exact point where E2,E3 (the K–L coupling) must enter isolated. This confirms the
reviewer's prediction that this route can bottom out in a scalar identity; the value is
the exact reformulation + the localisation of where E1–E3 are unused.

Spec concerns: none. Imports only certified lemmas. All numeric checks below are guides,
not proof steps; every asserted identity is derived in prose.

## Status
partial

## Approaches tried
- inversion-at-A (round 2, NEW): opened the circle→line framing. **Proved rigorously**
  (a) `ℓ*=ι(ω)` is the line `2O·Y=1` (polar of `A`); (b) intercepts `p=1/(2O_x)`,
  `q=1/(2O·\hat{AC})`; (c) the certified core identity is *exactly equivalent* to
  `AB/p−AC/q=(AB²−AC²)/2`; (d) that expression collapses identically to `OM=ON`.
  **New honest finding:** the inversion reformulation is exact but *tautological* — `ℓ*`
  is the polar of `A`, so pinning it ≡ pinning `O`; E1–E3 are not injected by the
  inversion step. Reduced the genuine residual to the explicit intercept formula
  `1/p=(AK sinψ_L−AL sinψ_K)/sin(ψ_L−ψ_K)` with `ψ_K,ψ_L,AK,AL` given by Law of Sines
  from `θ,β,γ`. OPEN GAP: the K–L coupling E2 (`∠LBK=β`), E3 (`∠LCK=γ`) forces a scalar
  identity in `θ,β,γ,α,b,c` — the same wall, in a cleaner 2-DOF object. Not closed.
- (prior-round entries for other slugs live in current.md / their own files.)

## Current best

A **complete, gap-free inversion reformulation** of the problem, plus the certified
shared reduction, plus the exact localisation of where E1–E3 remain to be injected.
Everything in "Rigorous progress" below is proven in full; the single named gap (G-scalar)
is stated precisely.

Setup fixed throughout: place `A` at the origin `O_2:=(0,0)`. Let `\hat{AB}` be the unit
vector along `AB` (take it as the `x`-axis), `\hat{AC}` the unit vector along `AC`, and
`α=∠BAC` so `\hat{AC}=(cosα,sinα)`. Write `b=AC`, `c=AB`, so `B=(c,0)`, `C=b\hat{AC}`.
Let `ι` be inversion centred at `A` with radius `1`: for `X≠A`, `X*:=ι(X)=X/|X|²`, so
`X*` lies on ray `AX` with `AX·AX*=1` (this is the definition; see knowledge_base.md
§Geometry "Synthetic toolkit: … inversion").

### Rigorous progress

**Import (certified).** From `lemmas/reduction-power-to-core.md` and
`lemmas/cevian-lengths.md`:
- `OM=ON ⟺ pow(B,ω)−pow(C,ω)=(AB²−AC²)/2` ("core identity"), `ω=⊙(AKL)`, centre `O`.
- Along secant `AB`, `pow(B)=AB²(1−f)` with `f=AA'/AB`, `A'=AB∩ω` the second
  intersection; mirror `pow(C)=AC²(1−g)`, `g=AA''/AC`, `A''=AC∩ω`.
  *(Derivation of `pow(B)=AB²(1−f)`: on line `AB` with `A` at `0`, `B` at `c=AB`,
  `A'` at `fc`, the signed power is `\vec{BA}·\vec{BA'}=(-c)((f-1)c)=c²(1-f)`; this is
  the same `pow(B)` as in L1 since `pow(M)=(-c/2)(fc-c/2)=c²(1/4-f/2)=pow(B)/2-AB²/4`,
  matching L1 exactly. Hence the core identity is
  `AB²(1-f)-AC²(1-g)=(AB²-AC²)/2`, i.e. `AB²(f-½)=AC²(g-½)`.)* — call this **(Core-fg)**.

**Lemma I1 (inversion of a circle through the centre is a line; its equation).**
Since `A=0∈ω`, the circle `ω` has an equation of the form `|X|²−2O·X=0` (a circle
through the origin with centre `O`: `|X−O|²=|O|²` expands to `|X|²−2O·X=0`). For any
`X∈ω`, `X≠A`, its image `X*=X/|X|²` satisfies
`2O·X* = 2O·X/|X|² = |X|²/|X|² = 1`, using `2O·X=|X|²` on `ω`.
Conversely any point `Y` with `2O·Y=1` is the image of `X=Y/|Y|²∈ω` (reverse the
computation). Therefore
> `ℓ*:=ι(ω\{A})` is exactly the line `{Y : 2O·Y=1}`.
Since `A,K,L∈ω`, we get `K*,L*∈ℓ*`, so `ℓ*` is the line `K*L*`. `A` is not on `ℓ*`
(`2O·0=0≠1`). ∎

*Remark (this is the polar of `A`).* `2O·Y=1` is precisely the polar line of `A`
w.r.t. `ω`, confirming `ℓ*` is intrinsically `O`-dependent. Numeric check (guide only):
`2O·K*−1` and `2O·L*−1` are `~10⁻¹⁶`.

**Lemma I2 (second intersections are inverse images of line–line meets).**
The line `AB` passes through the centre `A` of `ι`, hence `ι(AB)=AB` and `ι` restricts
to an involution of `AB`. Because `ι` is a bijection off `A` and `A'∈ω∩AB` with `A'≠A`,
`ι(A')∈ι(ω)∩ι(AB)=ℓ*∩AB`. Set `P*:=ℓ*∩AB` (a single point since `A∉ℓ*` so `ℓ*∦`… in
fact `ℓ*` is not parallel to `AB` unless `A'` is the point at infinity, i.e. `AB`
tangent to `ω` at `A`, excluded as `A'≠A` exists). Then `ι(A')=P*`, so
`A'=ι(P*)` and `AA'·AP*=1`, giving `AA'=1/AP*`. Mirror on `AC`: `Q*:=ℓ*∩AC`,
`A''=ι(Q*)`, `AA''=1/AQ*`. ∎

**Lemma I3 (intercepts of `ℓ*`).** Write `p:=AP*`, `q:=AQ*` (signed lengths along
rays `AB`, `AC`). Intersecting `ℓ*:2O·Y=1` with the `x`-axis `Y=(p,0)` gives
`2O_x·p=1`, so
> `1/p = 2O_x = 2O·\hat{AB}`.
Intersecting with `AC` (`Y=q\hat{AC}`) gives `2(O·\hat{AC})q=1`, so
> `1/q = 2O·\hat{AC}`.
(Numeric check, guide only: `p=1/(2O_x)` and `q=1/(2O·\hat{AC})` agree to `~10⁻¹⁵`.) ∎

**Proposition R (inversion reformulation of the core identity).**
Combining I2 with **(Core-fg)**: `f=AA'/AB=1/(AB·AP*)=1/(c·p)`, `g=1/(b·q)`. Substitute
into **(Core-fg)** `AB²(f-½)=AC²(g-½)`:
`c²(1/(cp)-½)=b²(1/(bq)-½)` ⟺ `c/p - c²/2 = b/q - b²/2` ⟺
> **`AB/p − AC/q = (AB²−AC²)/2`.**   (Core*)
Thus `OM=ON ⟺ (Core*)`. This is a rigorous, self-contained reformulation on the single
line `ℓ*` and its two intercepts. ∎

**Proposition T (the reformulation is exact but returns to `OM=ON`).**
Substitute the intercepts of I3 into (Core*):
`AB/p = c·(1/p)=2c\,O·\hat{AB}=2\,O·(c\hat{AB})=2\,O·B`, and
`AC/q = b·(1/q)=2b\,O·\hat{AC}=2\,O·(b\hat{AC})=2\,O·C`. Hence
`AB/p-AC/q=2O·(B-C)`, and `(AB²-AC²)/2=(|B|²-|C|²)/2` (as `|B|=c,|C|=b`). So (Core*)
reads `2O·(B-C)=(|B|²-|C|²)/2`, i.e. `O·(B-C)=(|B|²-|C|²)/4`. But directly
`OM²-ON²=|O-B/2|²-|O-C/2|² = -O·B+|B|²/4+O·C-|C|²/4 = -O·(B-C)+(|B|²-|C|²)/4`,
so `OM=ON ⟺ O·(B-C)=(|B|²-|C|²)/4` — **identical** to (Core*)-after-substitution.
(Numeric check, guide only: `AB/p-AC/q-(AB²-AC²)/2 = 2[O·(B-C)-(|B|²-|C|²)/4]` to
`~10⁻¹⁵` on a random config.)

*Interpretation.* The inversion step is an exact change of coordinates, not an injection
of E1–E3: because `ℓ*` is the polar of `A` (`(u,v)=2O`), locating `p,q` from `O` and
computing (Core*) is logically the same statement as `OM=ON`. **To make progress the
intercepts `p,q` must be obtained from the geometry of the images `K*,L*` — i.e. from
E1–E3 — without reference to `O`.** That is the genuine residual, isolated next. ∎

**Reduction of the residual to an explicit scalar identity.**
Because `K*,L*` determine `ℓ*` (Lemma I1), and `K*=(1/AK)\hat K`, `L*=(1/AL)\hat L`
with `\hat K=(cosψ_K,sinψ_K)`, `\hat L=(cosψ_L,sinψ_L)`, `ψ_K:=∠KAB`, `ψ_L:=∠LAB`,
the `x`-intercept of the line `K*L*` is (collinearity determinant
`(K*-P*)×(L*-P*)=0` with `P*=(p,0)` gives `p=(K*×L*)/(L*_y-K*_y)`):
`K*×L* = \frac{1}{AK·AL}\sin(ψ_L-ψ_K)`, `L*_y-K*_y=\frac{\sinψ_L}{AL}-\frac{\sinψ_K}{AK}`,
so
> **`1/p = 2O·\hat{AB} = (AK\,\sinψ_L − AL\,\sinψ_K)/\sin(ψ_L−ψ_K)`,**
and, by the same computation on `AC` with the angles measured from `\hat{AC}` (i.e.
replace `ψ_·` by `ψ_·−α` in the numerator/denominator and swap the roles), the mirror
formula for `1/q`. (Both verified numerically to `~10⁻¹⁵`.)

Finally, `ψ_K,ψ_L,AK,AL` are fixed by E1 + the cevian lengths via Law of Sines:
in `△ABK`, `∠ABK=θ` (E1), `∠BAK=ψ_K`, `AB=c`, so `BK=c\sinψ_K/\sin(θ+ψ_K)`; equating
with the certified cevian length `BK=(c/2)\sinγ/\sin(θ+γ)` gives the **defining
relation for `ψ_K`**:
> `\sinψ_K/\sin(θ+ψ_K) = \tfrac12\,\sinγ/\sin(θ+γ)`,  and  `AK=c\,\sinθ/\sin(θ+ψ_K)`.
Mirror in `△ACL` (`∠ACL=θ`, `∠CAL=φ_L=α−ψ_L`, `AC=b`, `CL=(b/2)\sinβ/\sin(θ+β)`):
> `\sinφ_L/\sin(θ+φ_L) = \tfrac12\,\sinβ/\sin(θ+β)`,  `AL=b\,\sinθ/\sin(θ+φ_L)`,
`ψ_L=α−φ_L`.
(Both defining relations verified numerically to `~10⁻¹⁵`.)

Substituting these into (Core*) yields a scalar identity in `(θ,β,γ,α,b,c)`. It becomes
an identity — hence `OM=ON` — only after the remaining, still-unused angle conditions
**E2 (`∠LBK=β`)** and **E3 (`∠LCK=γ`)**, the *coupling* between the `K`-side and
`L`-side, are imposed. These pin `β,γ` as functions of `θ` (given `α,b,c`).

### Open gap (G-scalar) — precisely scoped
Impose E2 (`∠LBK=β`) and E3 (`∠LCK=γ`) as two equations relating `β,γ,θ,α,b,c`, and
prove that (Core*) — equivalently `2O·(B-C)=(|B|²-|C|²)/2` — holds identically on the
solution locus. Concretely: E2/E3 written at `B` and `C` couple the two cevian
directions (`∠LBK=∠LBA-∠KBA=∠LBA-θ`, and `∠LCK=∠KCA-∠LCA=∠KCA-θ`), which fixes
`∠LBA,∠KCA` and hence closes the system. This is the SAME scalar wall the other
approaches reach; the contribution of this approach is to have (i) proven the inversion
reformulation exactly, (ii) shown `ℓ*` is the polar of `A` so the reformulation alone is
tautological, and (iii) reduced the residual to the explicit determinate object
`1/p=(AK\sinψ_L-AL\sinψ_K)/\sin(ψ_L-ψ_K)` with the E1/cevian reductions of
`ψ_K,ψ_L,AK,AL`, leaving only the E2/E3 coupling identity open. No hand-waving: the gap
is exactly "prove the trig identity in `θ,β,γ` forced by E2,E3."

## Full proof
(Not present — Status is `partial`; the residual scalar identity G-scalar is open.)

## Promotable lemmas
- **Lemma I1 (polar image).** With `A` at the origin and unit inversion radius,
  `ω=⊙(AKL)` (through `A`) inverts to the line `ℓ*:\,2O·Y=1` (the polar of `A`),
  which is the line `K*L*`. Proved in full above from `|X|²−2O·X=0` on `ω`. Reusable.
- **Lemma I2 (second-intersection = inverse of line∩polar).** `A'=AB∩ω` and
  `A''=AC∩ω` satisfy `A'=ι(ℓ*∩AB)`, `A''=ι(ℓ*∩AC)`, so `AA'·AP*=1`, `AA''·AQ*=1`
  where `P*=ℓ*∩AB`, `Q*=ℓ*∩AC`. Proved in full (involution fixing lines through the
  centre). Reusable.
- **Proposition R (inversion form of the core identity).** `OM=ON ⟺ AB/p−AC/q=
  (AB²−AC²)/2`, `p=AP*`, `q=AQ*` the intercepts of the polar of `A` on `AB,AC`.
  Proved in full. Reusable as an equivalent statement of the target.

  (These three are candidates for certification; the final scalar identity G-scalar is
  NOT proved and must not be certified.)
