## Status
solved

## Approaches tried
- **trig-metric-identity** — Metric/coordinate route. Reduces `OM=ON` to the scalar
  `O_x=(2p+a)/4`; parametrizes the family by `s=tan(θ/2)`, places `K,L` on two rotated
  rays with free radii `t_K,t_L`; fixes all branches by a region/orientation argument;
  encodes conditions 2,3 as `E2=t_K·H(t_L)`, `E3=t_L·G(t_K)` (the system decouples); proves
  the target polynomial `T` lies in the ideal `⟨G,H⟩` via the EXACT **polynomial** cofactor
  identity `f·T=Q_G·G+Q_H·H` (sympy, exact symbolic zero, `Q_G,Q_H` genuine polynomials);
  and divides out the shared leading content `f=(1+s²)·AB·AC·sin(∠A+θ)>0` (positivity from
  `θ=∠KBA<∠ABC` since `K∈△BMC`, and `∠A+∠ABC=π−∠ACB<π`). **SOLVED** — reviewer re-verified
  the identity as an exact symbolic zero and re-derived the positivity chain independently.
- **equal-power-secants** — Power-of-a-point framing. L1 (power reformulation) proved and
  promoted. The distinctive engine (secant through `K`/`L`) is refuted: no spiral similarity
  or invariant concyclicity carries the second intersection; it collapses onto the shared
  reduction. Dead-end engine.
- **spiral-involution** — Synthetic route via the involution `σ:(B↔C,M↔N,K↔L,A↦A)`. L1
  (σ-invariance) and L2 (`∠LBA+∠NLC=π`, σ-image `∠KCA+∠MKB=π`) proved and promoted. The
  spiral-similarity engine is refuted (triangles' angle multisets differ). Dead-end engine.

## Current best
Full proof below (complete, from the `trig-metric-identity` approach). `OM=ON` is proved
for the entire admissible 1-parameter family via the exact polynomial cofactor identity
`f·T=Q_G·G+Q_H·H` together with the strict positivity `f=(1+s²)·AB·AC·sin(∠A+θ)>0`.

## Full proof

Throughout, "angle" means an unsigned angle in `(0,π)`. For plane vectors `V=(V_1,V_2)`,
`W=(W_1,W_2)` write `cross(V,W)=V_1W_2−V_2W_1`, `dot(V,W)=V_1W_1+V_2W_2`. The **oriented
angle** `δ(V,W)∈(−π,π]` from `V` to `W` satisfies `cross(V,W)=|V||W|sinδ(V,W)`,
`dot(V,W)=|V||W|cosδ(V,W)`; `|δ(V,W)|` equals the unsigned angle between the rays and
`cross(V,W)>0 ⇔ δ(V,W)∈(0,π)`. For points `P,V,Q`, `cross(P−V,Q−V)` is twice the signed
area of `PVQ`, positive exactly when `P,V,Q` are counterclockwise (CCW).

### 0. Coordinates and hypotheses
`ABC` is nondegenerate. Fix `B=(0,0)`, `C=(a,0)` with `a=BC>0`, `A=(p,q)`, choosing the
orientation so `q>0`. Then `M=(p/2,q/2)`, `N=((p+a)/2,q/2)`; `M,N` share height `q/2`, so
`MN` is horizontal. Write `θ:=∠KBA=∠ACL` (condition 1); `0<θ<π`, so `s:=tan(θ/2)>0`,
`w:=1+s²>0`, `cosθ=(1−s²)/w`, `sinθ=2s/w`. The hypotheses used are exactly those in the
statement: `K` strictly inside `△BMC`; `L` strictly inside `△BNC`; `K` inside `∠LBA`;
`L` inside `∠ACK`; and `∠KBA=∠ACL(=θ)`, `∠LBK=∠LNC`, `∠LCK=∠BMK`. Let `O` be the
circumcentre of `AKL`.

### 1. Reduction: `OM=ON ⟺ O_x=(2p+a)/4`
With `O=(O_x,O_y)` and `M,N` at height `q/2`,
`OM²−ON²=(O_x−p/2)²−(O_x−(p+a)/2)²=(a/2)(2O_x−(2p+a)/2)`. Since `a>0`,
`OM=ON ⇔ O_x=(2p+a)/4`.  (1)
(Equivalently `O` lies on the perpendicular bisector of the horizontal segment `MN`; and
`OB²−OC²=2aO_x−a²`, `AB²−AC²=2ap−a²`, so (1) is the stated form `OB²−OC²=(AB²−AC²)/2`.)
This uses no property of `K,L`.

### 2. Parametrising `K,L` on the two rays (branches fixed)
Line `BA` passes through `B,M`; sides are separated by the sign of `cross(A−B,X−B)`. For
`X=C`: `cross((p,q),(a,0))=−qa<0`. Triangle `BMC` has edge `BM` on line `BA` and third
vertex `C` on the side `cross(A−B,·)<0`, so all of `△BMC`, hence `K`, has
`cross(A−B,K−B)<0`: `K` is clockwise of ray `BA`. The ray at angle `θ` clockwise of `BA`
has direction (scaling by `w`) `u=w·R(−θ)(p,q)=(p(1−s²)+2qs,\,−2ps+q(1−s²))`, with
`cross(A−B,u)=−w|A|²sinθ<0`. Hence `K=t_K·u`, `t_K>0`.  (2)
Symmetrically, line `CA` passes through `C,N`; for `X=B`, `cross(A−C,B−C)=qa>0`, so
`△BNC` and `L` satisfy `cross(A−C,L−C)>0`: `L` is CCW of ray `CA`. With
`d_L=w·R(+θ)(p−a,q)=((p−a)(1−s²)−2qs,\,(p−a)2s+q(1−s²))`, `cross(A−C,d_L)>0`, so
`L=C+t_L·d_L`, `t_L>0`.  (3)
All quantities are now polynomials in `p,q,a,s,t_K,t_L`.

### 3. Orientation lemma
(i) `cross(B−M,K−M)=s\,t_K(p²+q²)>0`, so `δ(B−M,K−M)=∠BMK∈(0,π)`.
(ii) `cross(L−N,C−N)=s\,t_L((p−a)²+q²)>0`, so `δ(L−N,C−N)=∠LNC∈(0,π)`.
(iii) Both `K,L` are clockwise of `BA` (for `L`: `cross(A−B,N−B)=−qa/2<0`, and `△BNC` lies
on that side). Their oriented angles from `BA` are `−∠KBA,−∠LBA∈(−π,0)`. "`K` inside
`∠LBA`" means `∠KBA<∠LBA`, so `δ(L−B,K−B)=(−∠KBA)−(−∠LBA)=∠LBA−∠KBA=∠LBK∈(0,π)`.
(iv) Both `K,L` are CCW of `CA` (for `K`: `cross(A−C,M−C)=aq/2>0`, and `△BMC` lies on that
side). Their oriented angles from `CA` are `+∠ACK,+∠ACL∈(0,π)`. "`L` inside `∠ACK`" means
`∠ACL<∠ACK`, so `δ(L−C,K−C)=∠ACK−∠ACL=∠LCK∈(0,π)`.

### 4. Encoding conditions 2,3 and the decoupling
Set `E2=cross(L−B,K−B)dot(L−N,C−N)−cross(L−N,C−N)dot(L−B,K−B)` and
`E3=cross(L−C,K−C)dot(B−M,K−M)−cross(B−M,K−M)dot(L−C,K−C)`. By the sine-subtraction
formula, `E2=|L−B||K−B||L−N||C−N|·sin(δ(L−B,K−B)−δ(L−N,C−N))` and similarly for `E3`. By
§3 each `δ` equals the named unsigned angle in `(0,π)`, so each `sin`-argument lies in
`(−π,π)`, where `sin` vanishes only at `0`; length factors are nonzero. Hence
`E2=0 ⇔ ∠LBK=∠LNC` (cond 2) and `E3=0 ⇔ ∠LCK=∠BMK` (cond 3).
**Decoupling.** Since `K−B=t_K u`, `E2=t_K·H` with `H` independent of `t_K` (quadratic in
`t_L`); since `L−C=t_L d_L`, `E3=t_L·G` with `G` independent of `t_L` (quadratic in `t_K`).
As `t_K,t_L>0`: `E2=0 ⇔ H(t_L)=0`, `E3=0 ⇔ G(t_K)=0`.  (5)

### 5. The circumcentre identity and its ideal membership
For `A=(p,q),K,L`, the circumcentre `O` of `AKL` has `O_x=num_x/D` with
`D=2(A_x(K_y−L_y)+K_x(L_y−A_y)+L_x(A_y−K_y))` (`≠0`, `AKL` noncollinear) and
`num_x=(A_x²+A_y²)(K_y−L_y)+(K_x²+K_y²)(L_y−A_y)+(L_x²+L_y²)(A_y−K_y)`. By (1) the goal is
`T:=4\,num_x−(2p+a)D=0`.  (6)
Treating `G∈ℚ(p,q,a,s)[t_K]`, `H∈ℚ(p,q,a,s)[t_L]`, direct computation gives their leading
coefficients `lc_{t_K}(G)=\tfrac12(1+s²)²(p²+q²)f`, `lc_{t_L}(H)=\tfrac12(1+s²)²((p−a)²+q²)f`,
where `f:=2s(p²+q²)−2aps+aq(1−s²)`.  (7)
Reducing `T` modulo `⟨G,H⟩` (division by `G` in `t_K`, remainder by `H` in `t_L`) yields
cofactors whose only denominator is a power of these leading coefficients; clearing that
denominator — whose content equals `f` exactly — gives an EXACT identity with **polynomial**
cofactors `Q_G,Q_H∈ℚ[p,q,a,s,t_K,t_L]`:
`f·T=Q_G·G+Q_H·H`  (identically in `p,q,a,s,t_K,t_L`).  (8)
This is verified as an exact symbolic zero in `results/imo-2026-02/verify.py`
(`expand(f·T−(Q_G·G+Q_H·H))=0`, with `denom(Q_G)=denom(Q_H)=1` and the content `c−f=0`
asserted; the reduction remainder is also `0`). Because every coefficient is a polynomial in
`p,q,a,s`, (8) holds for every triangle and every `θ`, and in particular gives `f·T=0` at any
configuration with `G=H=0`, with no denominators anywhere.

**Positivity of `f`.** With `AB=\sqrt{p²+q²}>0`, `AC=\sqrt{(p−a)²+q²}>0` and apex angle
`∠A∈(0,π)`, the identities `AB·AC·cos∠A=dot(B−A,C−A)=p²+q²−ap` and
`AB·AC·sin∠A=|cross(B−A,C−A)|=qa` combined with `cosθ=(1−s²)/(1+s²)`, `sinθ=2s/(1+s²)` and
the sine-addition formula give
`f=(1+s²)·AB·AC·sin(∠A+θ)`.  (9)
(Also checked as an exact symbolic zero in `verify.py`.) Here `1+s²,AB,AC>0`; it remains to
show `∠A+θ∈(0,π)`. Since `∠A,θ>0`, `∠A+θ>0`. The point `M` is the midpoint of `AB`, so ray
`BM`=ray `BA` and the angle of `△BMC` at `B` equals `∠ABC`; as `K` is strictly inside
`△BMC`, ray `BK` lies strictly between sides `BM(=BA)` and `BC`, so `θ=∠KBA<∠ABC`. By the
angle sum, `∠A+∠ABC=π−∠ACB<π` (`∠ACB>0`). Hence `0<∠A+θ<∠A+∠ABC<π`, so `sin(∠A+θ)>0`, and
by (9), `f>0`.  (10)

### 6. Conclusion
By the hypotheses and §4, conditions 2,3 give `E2=E3=0`, hence by (5) `G(t_K)=H(t_L)=0`.
Substituting into (8), `f·T=Q_G·G+Q_H·H=0`. By (10), `f>0`, so `T=0`, i.e. `O_x=(2p+a)/4`,
which by §1 is `OM=ON`. The potential `0·∞` pitfall is entirely avoided: (8) has polynomial
cofactors valid unconditionally, and the single scalar `f` divided out is proven strictly
positive. The region hypothesis `K∈△BMC` enters the metric argument exactly here (forcing
`θ<∠ABC`, hence `f>0`). As the only inputs were the problem's seven hypotheses, this holds
for every admissible `(K,L)`. Hence `OM=ON`. ∎

**Verification artifact.** `results/imo-2026-02/verify.py` certifies, as exact symbolic
zeros: the cofactor residual `T−(q_G·G+q_H·H)=0`, the polynomial-identity residual
`f·T−(Q_G·G+Q_H·H)=0` with `denom(Q_G)=denom(Q_H)=1`, the content `c−f=0`, and
`f−(1+s²)·AB·AC·sin(∠A+θ)=0`.
