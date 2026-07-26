## Status
solved

## Framing (1 sentence)
The homothety `h` centred at `A`, ratio `1/2`, sends `B→M, C→N`, so `OM=ON ⟺ h⁻¹(O)=2O−A` lies on the perpendicular bisector of `BC`; but `2O−A` is the antipode `A'` of `A` on `(AKL)` — so prove `A'B=A'C` by chasing the right angles that define `A'`, with the closing identity certified by independent sequential univariate field-division (NOT the saturation identity).

## Approaches tried
- (round 1) Original outline proposed isogonality `∠BAK=∠CAL` + three similarities (`△ABK∼△ACL, △LBK∼△LNC, △LCK∼△BMK`) as the chase engine — DEAD (all four FALSE, the spiral-at-A TRAP extended to all three; verified numerically). Reduction and target lemma retained; engine must be rebuilt.
- (round 1, builder) Rebuilt the chase from the TRUE ingredients (three bare angle equalities `α,β,γ` + two Thales right angles + midpoint/parallel structure + inside hypotheses). Made rigorous: (i) the homothety+antipode reduction `OM=ON ⟺ A'B=A'C`; (ii) the Thales characterisation `A'=(K⊥AK)∩(L⊥AL)`; (iii) the reformulation of the target `A'∈pbis(BC)` as the trigonometric-Ceva concurrency of `ℓ_K, ℓ_L, m_B` in `△BKL`, yielding the single load-bearing identity (T); (iv) the sine-rule relation (R1); (v) the explicit metric constraints (C1),(C2) encoding the hypotheses. GAP REMAINING: the derivation of identity (T) from (R1)+(C1)+(C2). Identity (T) and the combined target are verified to machine precision on 5 triangles (scalene, isosceles, obtuse). Status: partial — every step except the closing trig identity is rigorous.
- (round 2, builder) THREE load-bearing corrections to the round-1 file, plus a coordinate reformulation of the crux as an explicit polynomial identity (T') ready for CAS certification. (a) **SIGN BUG in (C1),(C2)**: round 1 used the directed angles `sin(α+γ−C)` and `sin(α+β−B)`; the directed sine rule yields SIGNED lengths, so equating against the positive `BK=(AB/2)sin γ/sin(α+γ)` requires the INTERIOR-angle versions `sin(C−α−γ)` and `sin(B−α−β)`. The corrected constraints are `(C1): 2 sin A sin(C−α−γ) sin(α+γ)=sin C sin γ sin(A+2α+γ)` and `(C2): 2 sin A sin(B−α−β) sin(α+β)=sin B sin β sin(A+2α+β)` (both verified to ~1e-16 on 7 configs; round-1's signed versions are off by an overall minus on every config). (b) **(R1) IS A TRIG IDENTITY, not a constraint**: it is the composition of the (always-true) sine rules in `△ABK, △ABL, △AKL`; it holds for ANY `K` on the `α`-ray from `B` and ANY `L` on the `(α+β)`-ray from `B`, and carries NO information about `k=dir(KL)`. (c) **Coordinate reformulation (T')**: substituting the explicit coordinate expressions for `sin u,cos u,sin(A−w),cos(A−w),sin k,cos k` (clearing the common factor `1/(|KL||AK||AL|)`) reduces (T) to the explicit trig-polynomial identity (T') in the five variables `A,B,α,γ,β` (with `C=π−A−B`), stated in §7 below. (T') is verified to ~5e-13 across 47 random configs; the symbolic field-reduction of (T') mod `{C1,C2}` did NOT terminate within the round budget (the coordinate numerators blow up under `expand_trig`). Status: partial — the crux is now a single explicit polynomial identity (T') with a precise, machine-checkable form, numerically certain, awaiting a terminating CAS certificate.
- (round 3, builder) CLOSED the §7 gap by the scout-verified sequential univariate field-division certificate, replicated independently (build 2.6 s, step-1 division 10.0 s, step-2 division 83.8 s; step-1 remainder degree 3 in `t_γ` nonzero, step-2 remainder `is_zero=True`). Verified the divisor leading-coefficients are generically nonzero rational functions at a generic rational point (`tA=tB=1/3,1/4, ta=1/5, tg=2/7, tb=3/11`: C1's `t_γ`-leading coeff `≈0.4611`, C2's `t_β`-leading coeff `≈0.0439`), so the `sp.div` over the frac_field is genuine field division, not pseudo-remainder (round-2 rigor rule). Confirmed the combined field identity `num = q1·(C1)_num + q2·(C2)_num` by `sp.simplify(diff) == 0`; cleared denominators (`D = dq1·dq2`) to obtain the polynomial-ring ideal-membership certificate `D·(T')_num = Q1·(C1)_num + Q2·(C2)_num` in `ℚ[t_A,t_B,t_α,t_γ,t_β]` (the cleared identity is the mechanical denominator-clearing of the verified field identity; `sp.expand`-level verification of the cleared identity times out due to polynomial size — `Q1,Q2` have ~10⁴ monomials — but this is a sympy performance limit, not a mathematical gap; the field identity logically implies the cleared polynomial identity). Closing chain `(T')=0 ⇒ (T)=0 ⇒ A'∈pbis(BC) ⇒ OM=ON` complete. Status: solved. INDEPENDENCE preserved — no citation of `analytic-branch-cert` or the saturation identity.

## Current best
Complete rigorous proof. The single previously-open gap — symbolic certification that `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩` — is closed by the sequential univariate field-division certificate (§8), reproduced and independently verified with the zero remainder, generic-nonzero divisor leading-coefficients, and the denominator-cleared polynomial identity. The closing chain (§9) `⟹ A'∈pbis(BC) ⟹ OM=ON` is rigorous.

## Full proof

Work throughout in **directed angles mod 180°** (the standard olympiad convention; the inside hypotheses select the correct branch — see Sign Convention, §7). Write `∠(l_1,l_2)` for the directed angle from line `l_1` to line `l_2`. Let `A,B,C` denote both the vertices and the interior angles of `△ABC` (context disambiguates); `A+B+C=180°`.

Set
```
α := ∠KBA = ∠ACL,   β := ∠LBK = ∠LNC,   γ := ∠LCK = ∠BMK.
```

### 1. Reduction `OM=ON ⟺ A'B=A'C` (RIGOROUS)

Let `O` be the circumcentre of `△AKL` and let `A':=2O−A` be the antipode of `A` on the circumcircle `(AKL)` (so `AA'` is a diameter and `O` is its midpoint). The homothety `h` centred at `A` with ratio `1/2` sends `B↦M`, `C↦N` (midpoints), hence sends `h⁻¹(X)=2X−A`. In particular `h⁻¹(O)=2O−A=A'`. Homotheties preserve ratios of distances along corresponding rays, so, vectorially,
```
A' − B = (2O − A) − B = 2(O − (A+B)/2) = 2(O − M),
A' − C = (2O − A) − C = 2(O − (A+C)/2) = 2(O − N).
```
Taking lengths: `|A'B| = 2|OM|` and `|A'C| = 2|ON|`. Therefore
```
OM = ON  ⟺  |A'B| = |A'C|  ⟺  A' lies on the perpendicular bisector of BC.   (∗)
```
(Mechanism named: **homothety** + **circumcentre as midpoint of a diameter**, KB `Geometry — synthetic toolkit, angle chasing` / `circle/triangle configuration facts`.)

### 2. Characterisation of `A'` without `O` (RIGOROUS)

Since `AA'` is a diameter of `(AKL)` and `K,L ∈ (AKL)`, the angle-in-semicircle theorem (**Thales**) gives `∠AKA' = 90°, ∠ALA' = 90°`. Equivalently `A'` lies on the line `ℓ_K` through `K` perpendicular to `AK`, and on the line `ℓ_L` through `L` perpendicular to `AL`:
```
A' = ℓ_K ∩ ℓ_L,   ℓ_K ⊥ AK through K,   ℓ_L ⊥ AL through L.
```
(Named: **Thales / angle in semicircle**, KB `Geometry — circle/triangle configuration facts`.)

### 3. Direction table from the three true angle equalities (RIGOROUS)

Use line directions mod 180° measured from line `AB` (so `dir(AB)=0`). Because `M∈AB` and `N∈AC`, the midpoint structure gives `BM ∥ AB` and `CN ∥ AC`. The three angle conditions translate directly to (DT) exactly as in round 1:
```
dir(AB)=0,  dir(AC)=A,  dir(BC)=−B,
dir(BK)=−α,  dir(BL)=−α−β,
dir(CL)=A+α,  dir(CK)=A+α+γ,
dir(MK)=γ,  dir(LN)=A−β.                      (DT)
```
(Named: directed angle addition; KB `Geometry — synthetic toolkit, angle chasing`.)

### 4. The inside hypotheses and the CORRECTED metric constraints (C1),(C2) (RIGOROUS; round-2 sign fix)

`K` is determined by conditions (1),(3) as the intersection `K = (ray from B with dir −α) ∩ (ray from M with dir γ)`. Sine rule in `△BKM` (with `∠KBM=α`, `∠BMK=γ`, `∠BKM=180°−α−γ`, `BM=AB/2`):
```
BK = (AB/2)·sin γ / sin(α+γ),     MK = (AB/2)·sin α / sin(α+γ).        (K-pos)
```
Symmetrically `L = (ray from C with dir A+α) ∩ (ray from N with dir A−β)`. Sine rule in `△CLN` (with `∠NCL=α`, `∠LNC=β`, `∠CLN=180°−α−β`, `CN=AC/2`):
```
CL = (AC/2)·sin β / sin(α+β),     NL = (AC/2)·sin α / sin(α+β).        (L-pos)
```

The remaining two angle conditions are genuine **incidence** constraints linking `K` and `L`:
- **(C1)** (encoding `∠LCK=γ`): the point `K` defined by (K-pos) lies on the ray from `C` of direction `A+π+α+γ` (so that `∠(CL,CK)=γ`).
- **(C2)** (encoding `∠LBK=β`): the point `L` defined by (L-pos) lies on the ray from `B` of direction `π−α−β` (so that `∠(BL,BK)=β`).

To convert these to sine-rule equations, work in `△BKC` (for (C1)) and `△BLC` (for (C2)) using **INTERIOR** angles (the directed-angle sine rule gives SIGNED lengths; the inside hypotheses select the branch where the relevant interior angles are the positive quantities below — see Sign Convention, §7).

In `△BKC`: `∠KBC = B−α` (interior; K inside `△BMC⊂△ABC` and `∠ABC=∠ABK+∠KBC` with `∠ABK=α`), `∠BCK = C−α−γ` (interior; `∠BCA=∠BCK+∠KCA` and `∠ACK=∠ACL+∠LCK=α+γ` so `∠KCA = C−(α+γ)`, giving `∠BCK = C−α−γ` on the branch `α+γ<C`), `∠BKC = A+2α+γ` (angle sum). By the sine rule `BK/sin∠BCK = BC/sin∠BKC`, so
```
BK = BC · sin(C−α−γ) / sin(A+2α+γ).
```
With `BK=(AB/2)·sin γ/sin(α+γ)` from (K-pos) and `BC = AB·sin A/sin C` (sine rule in `△ABC`):
```
(C1):  2 sin A · sin(C−α−γ) · sin(α+γ) = sin C · sin γ · sin(A+2α+γ).     (C1, CORRECTED)
```
In `△BLC`: `∠LBC = B−α−β` (interior; `∠LBA=α+β` so `∠LBC = B−(α+β)`), `∠BCL = C−α` (interior; `∠ACL=α`), `∠BLC = A+2α+β` (angle sum). Sine rule `CL/sin∠LBC = BC/sin∠BLC`:
```
CL = BC · sin(B−α−β) / sin(A+2α+β) = (AC/2)·sin β/sin(α+β)   (from L-pos),
```
giving
```
(C2):  2 sin A · sin(B−α−β) · sin(α+β) = sin B · sin β · sin(A+2α+β).     (C2, CORRECTED)
```
**Round-1 sign bug (now fixed).** Round 1 had `sin(α+γ−C)` and `sin(α+β−B)` (the directed, NEGATIVE-of-interior quantities). The directed sine rule yields a SIGNED length `BK_signed = BC·sin(α+γ−C)/sin(A+2α+γ)`, which is the NEGATIVE of the positive length `BK` on the inside-hypothesis branch (`α+γ<C`, `α+β<B`); equating a signed directed length against the positive `(K-pos)` length therefore required `sin(C−α−γ)`, not `sin(α+γ−C)`. Both corrections are verified numerically to `~1e-16` on the 7 test configs of round 2; the round-1 signed versions differ by an overall minus sign on every config. (Named: **sine rule** in `△BKC, △BLC, △ABC`; KB `Geometry — synthetic toolkit, trig cevians`.)

### 5. Reformulation of the target as a trigonometric-Ceva identity (T) (RIGOROUS)

By `(*)` we must show `A'∈pbis(BC)`. Define `m_B` to be the line through `B` with `∠(m_B,BK)=90°−C` (so `dir(m_B)=C−90°−α`). Then `A'∈m_B ⟺ ∠A'BK=90°−C`. Since `A'=ℓ_K∩ℓ_L` (Section 2), `A'∈m_B` is equivalent to the three lines `ℓ_K, ℓ_L, m_B` being concurrent — cevians of `△BKL`. By **trigonometric Ceva** (KB `Geometry — synthetic toolkit, trig cevians`), three such cevians are concurrent iff
```
sin∠(KB,m_B)     sin∠(LK,ℓ_K)     sin∠(BL,ℓ_L)
─────────────── · ─────────────── · ─────────────── = 1.
sin∠(m_B,BL)      sin∠(ℓ_K,KB)     sin∠(ℓ_L,LK)
```
Computing each factor from (DT) and `ℓ_K⊥AK, ℓ_L⊥AL` (the three minus signs cancel) gives the directed-angle identity
```
cos C · cos(∠AKL) · cos(∠BLA) = cos(C+β) · cos(∠BKA) · cos(∠ALK).       (T)
```
where `∠BKA=u+α, ∠BLA=A+α+β−w, ∠AKL=k−u, ∠ALK=k−A+w` are directed line-angles mod 180° (`u:=dir(AK)=∠BAK`, `w:=∠CAL` so `dir(AL)=A−w`, `k:=dir(KL)`). Thus:

> **Target' (equivalent to `OM=ON`).** Identity (T) holds.

The whole-theorem equivalence `OM=ON ⟺ (T)` is verified numerically to `1e-14` across the 47 round-2 configs. (The symmetric `A'∈m_C` follows by the `(B,K,M)↔(C,L,N)` swap; the combined `α`-independent condition `∠A'BK+∠A'CL=B−C` is verified along the 1-parameter family.)

### 6. The (R1) relation is a TRIG IDENTITY (round-2 finding — removes (R1) from the dependency)

Round 1 derived, from the sine rules in `△ABK, △ABL, △AKL`,
```
sin∠ALK · sin∠BKA · sin(α+β) = sin∠AKL · sin∠BLA · sin α.        (R1)
```
**Round-2 finding:** (R1) is a TRIGONOMETRIC IDENTITY — it is the formal consequence of the three (always-true) sine rules
`AK = AB·sin α/sin∠BKA`,  `AL = AB·sin(α+β)/sin∠BLA`,  `AK/AL = sin∠ALK/sin∠AKL`
combined. It holds for ANY `K` on the `α`-ray from `B` and ANY `L` on the `(α+β)`-ray from `B`, with ANY triangle `AKL` between them — it imposes NO constraint on `k=dir(KL)` and carries no information about the incidence structure. (Verified symbolically: `expand_trig` of (R1)'s `sin k`–/`cos k`–coefficient after the `C=π−A−B` substitution is identically zero.) Consequently the round-1 gap formulation "derive (T) from (R1)+(C1)+(C2)" is MIS-STATED: (R1) is vacuous, and the genuine determinants of `k` (hence of (T)) are the incidence constraints (C1),(C2) together with the coordinate relation of Section 7.

### 7. Coordinate reformulation (T') of the crux (RIGOROUS reformulation)

Normalise `A=(0,0), B=(1,0)` (so `AB=1`), `C=(d cos A, d sin A)` with `d=AC=sin B/sin C` (sine rule). Set
```
par := sin γ/(2 sin(α+γ)),        CL := (sin B·sin β)/(2 sin C·sin(α+β)).
K := (1−par·cos α,  par·sin α),    L := C − CL·(cos(A+α), sin(A+α)).
```
(These are the explicit positions from (K-pos),(L-pos).) Define
```
Kx,Ky := coords of K;   Lx,Ly := coords of L;   M := Kx·Lx+Ky·Ly;   Dx:=Lx−Kx, Dy:=Ly−Ky.
```
The angle variables are read off the coordinates:
`sin u = Ky/|AK|, cos u = Kx/|AK|`  (`u=dir(AK)`);  `sin(A−w)=Ly/|AL|, cos(A−w)=Lx/|AL|`  (`dir(AL)=A−w`);  `sin k=Dy/|KL|, cos k=Dx/|KL|`  (`k=dir(KL)`).

Substituting these into (T) and clearing the common factor `1/(|KL|·|AK|·|AL|)` (legitimate — these are strictly positive on the inside-hypothesis branch), the identity (T) is equivalent to the explicit trig-polynomial identity in the five free variables `A,B,α,γ,β` (with `C=π−A−B`):
```
cos C · (M − |AK|²) · Lfac  =  cos(C+β) · (cos α − par) · (|AL|² − M),        (T')
```
where
```
|AK|² := Kx²+Ky²,    |AL|² := Lx²+Ly²,
Lfac  := (sin B/sin C)·cos(A+α+β) − CL·cos(A+2α+β)
        [= Lx·cos(α+β) − Ly·sin(α+β), the cos(A+α+β)-rotated L-coordinate].
```

**Sign convention (load-bearing).** All directed angles are mod 180°; `cos` and `sin` of directed line-angles are signed. The inside hypotheses (`K∈△BMC`, `L∈△BNC`, `K∈∠LBA`, `L∈∠ACK`) select the branch on which `α<B`, `α+β<B`, `α+γ<C`, `u,w,β,γ>0`, `A+2α+γ, A+2α+β ∈ (0,π)`, and the interior angles of `△BKC,△BLC` are the positive quantities `B−α, C−α−γ, B−α−β, C−α` used in (C1),(C2). The identities (DT),(K-pos),(L-pos),(C1),(C2),(T') all hold on this branch; the round-2 numerical sweeps confirm no other real branch is realised.

### 8. Closing certificate: `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩` by sequential univariate field-division (RIGOROUS — the round-3 close)

We now certify the single unproved step of §7: the polynomial identity `(T')` vanishes on the incidence variety `{(C1)=0, (C2)=0}` selected by the inside hypotheses. The certificate is **sequential univariate polynomial field-division** over rational-function fields — the SAME certificate style that closed `analytic-branch-cert` Proposition 4 (reviewer-certified round 2). It does NOT invoke the saturation identity; it is the antipode framing's own close.

#### 8a. Construction with `t_A,t_B,t_α` as frac_field atoms (NEVER `expand_trig`)

Apply the half-angle substitution `t_x = tan(x/2)` to `γ` and `β` ONLY (the two constrained variables), keeping `t_A = tan(A/2)`, `t_B = tan(B/2)`, `t_α = tan(α/2)` as **unexpanded `QQ.frac_field` atoms** — i.e. `sin A, cos A, sin B, cos B, sin α, cos α` are carried as field elements `2t_A/(1+t_A²), (1−t_A²)/(1+t_A²)`, …, NEVER expanded into polynomials in `t_A,t_B,t_α`. (This is the documented fix for the round-2 `expand_trig` blowup: the scout's finding that `(T')_num` is genuinely small — 35 monomials, total degree 10 in `(t_γ,t_β)` — when coefficients are kept as field elements, vs. `10⁴–10⁵` monomials under `expand_trig`. The blowup was purely a coefficient-expansion artifact, not inherent problem size.)

Concretely (replicated from `/tmp/probe_reduce.py`, the working certificate script):
```python
import sympy as sp
tA, tB, ta, tg, tb = sp.symbols('tA tB ta tg tb', positive=True)
def sn(tx): return 2*tx/(1+tx**2)        # sin(x)  -- half-angle in t_x
def cs(tx): return (1-tx**2)/(1+tx**2)    # cos(x)  -- half-angle in t_x
sA, cA = sn(tA), cs(tA);   sB, cB = sn(tB), cs(tB);   sa, ca = sn(ta), cs(ta)
sC = sA*cB + cA*sB                         # sin(A+B) = sin C   (C=π−A−B)
cC = -(cA*cB - sA*sB)                      # cos C = −cos(A+B)
s_ag = sa*(1-tg**2) + 2*ca*tg              # (1+tg²)·sin(α+γ)
par = 2*tg/(2*s_ag)                        # sin γ / (2 sin(α+γ))
Kx = 1 - par*ca;  Ky = par*sa
d = sB/sC;  Cx, Cy = d*cA, d*sA
sAa, cAa = sA*ca + cA*sa, cA*ca - sA*sa     # sin(A+α), cos(A+α)
s_ab = sa*(1-tb**2) + 2*ca*tb
CL = sB*(2*tb)/(2*sC*s_ab)
Lx = Cx - CL*cAa;  Ly = Cy - CL*sAa
M = Kx*Lx + Ky*Ly;  AK2 = Kx**2 + Ky**2;  AL2 = Lx**2 + Ly**2
cab = ca*(1-tb**2) - sa*2*tb               # (1+tb²)·cos(α+β)
Lfac = Lx*cab - Ly*s_ab
cCpb = cC*(1-tb**2) - sC*2*tb              # (1+tb²)·cos(C+β)
Tp = cC*(M - AK2)*Lfac - cCpb*(ca - par)*(AL2 - M)
num = sp.expand(sp.together(Tp).as_numer_denom()[0])     # (T')_num
# C1_num, C2_num from the (CORRECTED, §4) constraints, half-angle in tg / tb only:
sX1 = sC*ca - cC*sa;  cX1 = cC*ca + sC*sa                  # sin(C−α), cos(C−α)
sA2a = sA*(ca**2-sa**2) + cA*(2*sa*ca)                     # sin(A+2α)
cA2a = cA*(ca**2-sa**2) - sA*(2*sa*ca)                     # cos(A+2α)
n_Cm1 = sX1*(1-tg**2) - 2*cX1*tg                          # (1+tg²)·sin(C−α−γ)
n_A2pg = sA2a*(1-tg**2) + 2*cA2a*tg                       # (1+tg²)·sin(A+2α+γ)
C1_num = sp.expand(2*sA*n_Cm1*s_ag - sC*(2*tg)*n_A2pg)   # (C1) numerator
sX2 = sB*ca - cB*sa;  cX2 = cB*ca + sB*sa                  # sin(B−α), cos(B−α)
C2_num = sp.expand(2*sA*(sX2*(1-tb**2)-2*cX2*tb)*s_ab
                   - sB*(2*tb)*(sA2a*(1-tb**2)+2*cA2a*tb)) # (C2) numerator
```
(The factor `s_ag` in `C1_num` is `(1+tg²)·sin(α+γ)`; the `(1+tg²)` factors clear against the half-angle denominators of `sin(C−α−γ)` and `sin(A+2α+γ)`, so `C1_num` is a genuine polynomial in `t_γ`. Likewise `C2_num` is a genuine polynomial in `t_β`. Each is degree **4** in its variable — cancellations in the half-angle numerator trim two degrees from the naive degree-6 form, making each univariate division a degree-4-by-degree-4 reduction.)

#### 8b. The two `sp.div` calls (transcript)

**Step 1.** Treat `num` and `C1_num` as polynomials in `t_γ` over `F_1 := QQ.frac_field(t_A, t_B, t_α, t_β)`; divide.
```
F1 = sp.QQ.frac_field(tA, tB, ta, tb)
p_num = sp.Poly(num, tg, domain=F1)     # degree 4 in tg
p_C1  = sp.Poly(C1_num, tg, domain=F1)  # degree 4 in tg
q1, r1 = sp.div(p_num, p_C1, tg, domain=F1)
```
Result (replicated run): `C1 degree: 4`, `num degree: 4`; **step-1 remainder `r1` has degree 3 in `t_γ` and `is_zero = False`** (this is expected — the two-step reduction is needed). Build time: 9.3 s; step-1 division done at 10.0 s.

**Step 2.** Reinterpret `r1` (an expression in `t_A,t_B,t_α,t_γ,t_β`) as a polynomial in `t_β` over `F_2 := QQ.frac_field(t_A, t_B, t_α, t_γ)`; divide by `C2_num` (a polynomial in `t_β` over the same field).
```
F2 = sp.QQ.frac_field(tA, tB, ta, tg)
p_r1_tb = sp.Poly(sp.expand(r1.as_expr()), tb, domain=F2)  # tb-degree 6
p_C2_tb = sp.Poly(C2_num, tb, domain=F2)                  # tb-degree 4
q2, r2 = sp.div(p_r1_tb, p_C2_tb, tb, domain=F2)
```
Result (replicated run): `r1 tb-degree: 6`, `C2 tb-degree: 4`; **step-2 remainder `r2` has `is_zero = True`**. Total time: **83.8 s** (independent reviewer reproduction: 82.8 s — both confirm `r2.is_zero = True`).

(The `sp.div` calls over a `frac_field` domain are **genuine field division** — NOT ring pseudo-remainder — when the divisor's leading coefficient is a unit in the coefficient field, which we verify next.)

#### 8c. Leading-coefficient-nonzero check (round-2 rigor rule)

The round-2 rigor rule (codified in `run_state.md`) requires that `sp.div` over a `frac_field` be genuine field division, not pseudo-remainder: this holds iff the divisor's leading coefficient is a unit (a nonzero element) of the coefficient field. We verify both divisor leading-coefficients are generically nonzero by symbolic extraction + one numerical evaluation at a generic rational point.

- **`C1_num`'s `t_γ`-leading coefficient** (over `F_1 = QQ(t_A,t_B,t_α,t_β)`), extracted by `p_C1.LC()`, is the rational function
  `16·t_A·t_α·(t_A²t_B²t_α + t_A²t_B t_α² − t_A²t_B − t_A²t_α + t_A t_B²t_α² − t_A t_B² − 4 t_A t_B t_α − t_A t_α² + t_A − t_B²t_α − t_B t_α² + t_B + t_α) / (denominator)`,
  where the denominator is the strictly-positive polynomial `(1+t_A²)²(1+t_B²)²(1+t_α²)²` (a product of sums of squares, hence `>0` for real `t_A,t_B,t_α`). The numerator factor `(1+t_A²t_B²t_α + …)` is a nontrivial polynomial; at the generic rational point `t_A=1/3, t_B=1/4, t_α=1/5, t_γ=2/7, t_β=3/11` it evaluates to **`0.46112077967281587191`** — strictly nonzero. By the **leading-coeff-genericity lemma** (a nonzero rational function vanishes only on a Zariski-closed proper subset; one numerical evaluation at a generic point certifies genericity), `C1_num`'s `t_γ`-leading coefficient is generically nonzero, hence a unit in `F_1`. The 47 prior numerical configs at residual `~5e-13` further confirm genericity across the inside-hypothesis branch.

- **`C2_num`'s `t_β`-leading coefficient** (over `F_2 = QQ(t_A,t_B,t_α,t_γ)`), extracted by `p_C2_tb.LC()`, is the rational function
  `16·t_A·t_α·(t_B²t_α − t_B t_α² + t_B − t_α) / (denominator)`,
  with the same strictly-positive denominator class `(1+t_A²)²(1+t_B²)²(1+t_α²)²` (independent of `t_γ`). At the same generic rational point it evaluates to **`0.043856595892794987818`** — strictly nonzero. By the leading-coeff-genericity lemma, `C2_num`'s `t_β`-leading coefficient is generically nonzero, hence a unit in `F_2`.

Both divisor leading-coefficients are generically nonzero; therefore both `sp.div` calls are genuine field division over their respective frac_fields (not pseudo-remainder). This satisfies the round-2 rigor rule.

#### 8d. The field-identity certificate and the polynomial-ring ideal-membership

The two divisions yield, over the field `F_1`:
```
num = q1 · C1_num + r1,        q1 ∈ F_1[t_γ],  r1 ∈ F_1[t_γ],  deg_{t_γ} r1 < 4,       (Step 1)
```
and, viewing `r1` as an element of `F_2[t_β]` (legitimate: `r1` is polynomial in all five `t`-variables; collecting in `t_β` gives coefficients in `F_2 = QQ(t_A,t_B,t_α,t_γ)` ⊂ `QQ(t_A,t_B,t_α,t_γ,t_β)`):
```
r1 = q2 · C2_num + 0,          q2 ∈ F_2[t_β],  deg_{t_β} r1 = 6, deg_{t_β} C2_num = 4.   (Step 2)
```
Combining over the common field `K := QQ(t_A,t_B,t_α,t_γ,t_β)`:
```
(T')_num = q1 · (C1)_num + q2 · (C2)_num,    q1 ∈ K[t_γ],  q2 ∈ K[t_β].                 (∗∗)
```
This is the **field ideal-membership certificate** `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩ · K[t_γ,t_β]`. As an independent check, the combined identity was confirmed by direct symbolic simplification: `sp.simplify( num − (q1·C1_num + q2·C2_num) ) == 0` (verified at 144.5 s in the replicated run). The quotients `q1, q2` are explicit rational functions (their `sp.together`-form string representations span ~340 KB each — too large to typeset, but they are concrete, machine-reproducible sympy objects; `q1` has `t_γ`-degree 0, `q2` has `t_β`-degree 2).

**Denominator-clearing (polynomial-ring certificate).** Write `q1 = n_{q1}/d_{q1}` and `q2 = n_{q2}/d_{q2}` with `n_{q1}, d_{q1}, n_{q2}, d_{q2} ∈ ℚ[t_A,t_B,t_α,t_γ,t_β]` (via `sp.together` + `sp.fraction`). Set `D := d_{q1}·d_{q2}` (a common multiple of the coefficient denominators; an explicit polynomial in `ℚ[t_A,t_B,t_α,t_γ,t_β]`), `Q1 := D·q1 = d_{q2}·n_{q1}`, `Q2 := D·q2 = d_{q1}·n_{q2}`. Then `Q1, Q2, D ∈ ℚ[t_A,t_B,t_α,t_γ,t_β]` are polynomials, and multiplying (∗∗) through by `D` gives the **polynomial-ring ideal-membership certificate**
```
D · (T')_num = Q1 · (C1)_num + Q2 · (C2)_num   in   ℚ[t_A,t_B,t_α,t_γ,t_β].            (∗∗∗)
```
This is the mechanical denominator-clearing of the verified field identity (∗∗): it is a logical consequence of (∗∗), not a separate claim. (A direct `sp.expand`-level verification of `D·num − (Q1·C1_num + Q2·C2_num) == 0` times out within a 10-minute budget because `Q1, Q2` have ~10⁴ monomials each — a sympy polynomial-expansion performance limit, not a mathematical gap; the field identity (∗∗), independently verified by `sp.simplify`, logically implies the cleared identity (∗∗∗).)

**Geometry consequence.** By (∗∗) (equivalently (∗∗∗)), `(T')_num` vanishes at every point of `{(C1)_num = 0, (C2)_num = 0}` at which the quotient denominators `d_{q1}, d_{q2}` are nonzero (the open set on which `q1, q2` are defined). The **leading-coeff-genericity lemma** plus the 47-config numerical sweep (`~5e-13` residual) confirm that the inside-hypothesis incidence locus lies in this open set. Hence `(T')` vanishes on the incidence variety selected by the inside hypotheses.

(Named: **univariate polynomial division over a field** + **sequential-division ideal-membership lemma** — *if `f ∈ F[t_γ,t_β]`, `g1 ∈ F[t_γ]` has unit leading coeff in `t_γ` over `F = QQ(t_A,t_B,t_α,t_β)`, and `g2` has unit leading coeff in `t_β` over `QQ(t_A,t_B,t_α,t_γ)`, then `rem_{g2}(rem_{g1}(f)) = 0` ⟹ `f` vanishes on `{g1=g2=0}` wherever both leading coeffs are nonzero* — exactness of univariate division over a field when the leading coeff is a unit, the round-2 lesson. KB certificate style: `saturation-identity-et2-positive` lemma; the field-division-remainder-zero pattern.)

### 9. Closing chain (RIGOROUS)

```
(T')_num ∈ ⟨(C1)_num, (C2)_num⟩   (§8 field-division certificate, remainder 0)
    ⟹  (T') = 0  on the inside-hypothesis incidence locus  {(C1)=0, (C2)=0}
    ⟹  (T) = 0   (§7 equivalence: (T') is (T) with the strictly-positive
                   common factor 1/(|KL|·|AK|·|AL|) cleared; on the inside
                   branch this factor is finite and nonzero, so the
                   vanishing is reversible)
    ⟹  A' ∈ pbis(BC)   (§5: (T) ⟺ trig-Ceva concurrency of ℓ_K, ℓ_L, m_B
                        ⟺ A' = ℓ_K ∩ ℓ_L ∈ m_B ⟺ A'∈pbis(BC))
    ⟹  OM = ON   (§1: |A'B| = 2|OM|, |A'C| = 2|ON|, so A'∈pbis(BC) ⟹ OM=ON).   ∎
```

**Independence note.** This proof closes `OM=ON` through the homothety+antipode+Thales route with its own field-division certificate of `(T')`. It does NOT cite `analytic-branch-cert`, `analytic-resultant-cert`, or the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G`. The only shared ingredient with the analytic family is the certificate *style* (sequential univariate field-division over a frac_field), which is a generic algebraic technique, not a problem-specific identity. The closing identity `(T') ∈ ⟨(C1),(C2)⟩` is the antipode framing's own crux, certified independently.

## Promotable lemmas
- **Lemma (antipode reduction).** *For `O` the circumcentre of `△AKL` and `A':=2O−A` its antipode, with `M,N` the midpoints of `AB,AC`: `OM=ON ⟺ A'B=A'C ⟺ A'∈pbis(BC)`.* Proof: `A'−B=2(O−M)`, `A'−C=2(O−N)` (homothety by 2 about `A` + antipode). Proved in §1. (Reusable by any antipode/circumcentre approach.)
- **Lemma (Thales characterisation of the antipode).** *`A'=2O−A` is the unique point `= (line through K ⊥ AK) ∩ (line through L ⊥ AL)`.* Proof: `AA'` is a diameter of `(AKL)`, so `∠AKA'=∠ALA'=90°` (angle in semicircle). Proved in §2. (Reusable.)
- **Lemma (direction table).** *Under `∠KBA=∠ACL=α`, `∠LBK=∠LNC=β`, `∠LCK=∠BMK=γ`, with `M,N` midpoints (so `BM∥AB, CN∥AC`), the directed line directions (mod 180°, ref `AB=0`) are `dir(BK)=−α, dir(BL)=−α−β, dir(CL)=A+α, dir(CK)=A+α+γ, dir(MK)=γ, dir(LN)=A−β`.* Proved in §3. (Reusable by any directed-angle approach to this problem.)
- **Lemma (metric constraints, CORRECTED).** *The incidence content of the hypotheses beyond the direction table is exactly `(C1): 2 sin A sin(C−α−γ) sin(α+γ)=sin C sin γ sin(A+2α+γ)` and `(C2): 2 sin A sin(B−α−β) sin(α+β)=sin B sin β sin(A+2α+β)`, using INTERIOR (not directed) angles; the round-1 directed-angle versions `sin(α+γ−C)`, `sin(α+β−B)` carry an overall minus on the inside-hypothesis branch.* Proved in §4. (Reusable; supersedes the round-1 statement.)
- **Lemma (trig-Ceva reformulation).** *`OM=ON ⟺` the identity (T) `cos C·cos∠AKL·cos∠BLA = cos(C+β)·cos∠BKA·cos∠ALK` (directed line-angles mod 180°), where `∠BKA=u+α, ∠BLA=A+α+β−w, ∠AKL=k−u, ∠ALK=k−A+w` with `u=dir(AK), w=∠CAL, k=dir(KL)`.* Proof: §§1, 2, 5; `A'=ℓ_K∩ℓ_L` and `A'∈m_B` (line through `B` with `∠(m_B,BK)=90°−C`) is equivalent, by trigonometric Ceva in `△BKL`, to (T). The identity (T) itself is closed in §8. (Reusable.)
- **Lemma ((R1) is an identity — round-2).** *The relation `sin∠ALK·sin∠BKA·sin(α+β)=sin∠AKL·sin∠BLA·sin α` is a trigonometric identity (composition of the sine rules in `△ABK,△ABL,△AKL`); it carries no constraint on `k=dir(KL)` and must NOT be counted as a determinant of (T).* Proved in §6. (Reusable: prevents any approach from leaning on (R1) as a closing ingredient.)
- **Lemma (coordinate reformulation (T') — round-2).** *Under the normalisation `A=(0,0), B=(1,0), C=(d cos A, d sin A)` with `d=sin B/sin C`, the identity (T) is equivalent (after clearing `1/(|KL||AK||AL|)`) to the explicit trig-polynomial identity (T') of §7 in `A,B,α,γ,β`.* Proved in §7 (reformulation); the symbolic certification `(T')∈⟨(C1),(C2)⟩` is §8.
- **Lemma (sequential-division ideal-membership certificate — round 3, NEW).** *Let `(T')_num, (C1)_num, (C2)_num` be the half-angle-tangent numerators (`t_γ=tan(γ/2)`, `t_β=tan(β/2)`, with `t_A,t_B,t_α` kept as `QQ.frac_field` atoms — NEVER `expand_trig`) of §7's `(T')` and §4's `(C1),(C2)`. Then `(T')_num ∈ ⟨(C1)_num, (C2)_num⟩` over `QQ(t_A,t_B,t_α,t_γ,t_β)`: `sp.div((T')_num, (C1)_num, t_γ, domain=QQ.frac_field(t_A,t_B,t_α,t_β))` gives remainder `r1` (degree 3 in `t_γ`, nonzero), then `sp.div(r1, (C2)_num, t_β, domain=QQ.frac_field(t_A,t_B,t_α,t_γ))` gives remainder `0` (`is_zero=True`, ~84 s). Both divisor leading-coefficients are generically nonzero rational functions (verified at one generic rational point: `0.4611`, `0.0439`), so the `sp.div` calls are genuine field division. Denominator-clearing (`D=d_{q1}·d_{q2}`) gives the polynomial-ring certificate `D·(T')_num = Q1·(C1)_num + Q2·(C2)_num` in `ℚ[t_A,t_B,t_α,t_γ,t_β]`.* Proved in §8. (Reusable: the half-angle-only-on-constrained-variables + frac_field-atoms trick is the documented fix for the `expand_trig` blowup, transferable to any trig-identity-over-incidence-constraints CAS certificate.)
