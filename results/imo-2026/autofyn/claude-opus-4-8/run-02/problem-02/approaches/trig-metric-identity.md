# Approach: trig-metric-identity

## Status
solved

## Approaches tried
- (round 1, new) Metric/trigonometric route: place `B,C,A` in coordinates, reduce
  `OM=ON` to the single scalar `O_x=(2p+a)/4`; parametrize the 1-parameter family by
  `s=tan(θ/2)` with `θ=∠KBA=∠ACL`, put `K,L` on the two rotated rays with free radii;
  fix all angle branches by a half-plane/orientation argument; encode conditions 2,3 as
  two polynomials `E2,E3` that factor as `E2=t_K·H(t_L)`, `E3=t_L·G(t_K)` (the system
  **decouples**); and prove the target polynomial `T` lies in the ideal `⟨G,H⟩` via an
  **exact** cofactor identity `T=q_G·G+q_H·H` (sympy, exact zero, script
  `results/imo-2026-02/verify.py`). — WORKED, complete for a general triangle.
- (round 1, r2) Closed the reviewer's `0·∞` gap: replaced the rational-cofactor identity
  by the **polynomial** identity `f·T=Q_G·G+Q_H·H` (denominators cleared; content `c=f`
  exactly, `Q_G,Q_H∈\mathbb{Q}[p,q,a,s,t_K,t_L]`, exact-zero checked), and proved the
  divided-out scalar `f=(1+s²)·AB·AC·sin(∠A+θ)>0` via `θ=∠KBA<∠ABC` (K∈△BMC) and
  `∠A+∠ABC<π` (angle sum). No `0·∞`; gap closed. — WORKED, solved.

## Current best
Full proof below (complete). The problem reduces to the scalar identity `O_x=(2p+a)/4`
(equivalently `OB²−OC²=(AB²−AC²)/2`), which holds for the entire family because of the
**polynomial** cofactor identity `f·T=Q_G·G+Q_H·H` (`Q_G,Q_H` polynomials, exact symbolic
zero) together with the strict positivity `f=(1+s²)·AB·AC·sin(∠A+θ)>0` (from `θ<∠ABC` and
`∠A+∠ABC<π`), which lets `f` be divided out with no `0·∞` issue.

## Full proof

Throughout, "angle" means an unsigned angle in `(0,π)`, and for two plane vectors
`V=(V_1,V_2)`, `W=(W_1,W_2)` we write
`cross(V,W)=V_1W_2−V_2W_1` and `dot(V,W)=V_1W_1+V_2W_2`.
The **oriented angle** `δ(V,W)∈(−π,π]` from `V` to `W` satisfies
`cross(V,W)=|V||W|sinδ(V,W)` and `dot(V,W)=|V||W|cosδ(V,W)`; its magnitude `|δ(V,W)|`
equals the unsigned angle between the rays, and `cross(V,W)>0 ⇔ δ(V,W)∈(0,π)`.
For three points `P,V,Q`, `cross(P−V,Q−V)` is twice the signed area of triangle `PVQ`,
so it is positive exactly when `P,V,Q` are in counterclockwise (CCW) order.

### 0. Coordinates and hypotheses

`ABC` is a nondegenerate triangle. Fix a Cartesian frame with
`B=(0,0)`, `C=(a,0)` where `a=BC>0`, and `A=(p,q)`; since `A∉BC` we may choose the
orientation so that `q>0`. Then
`M=\tfrac12(A+B)=(p/2,\;q/2)`, `N=\tfrac12(A+C)=((p+a)/2,\;q/2)`.
Note `M` and `N` have the **same height** `q/2`, i.e. segment `MN` is horizontal.

Write `θ:=∠KBA=∠ACL` (equal by condition 1). As `∠KBA` is an angle of a
nondegenerate configuration, `0<θ<π`, hence `s:=\tan(θ/2)>0`, and with `w:=1+s²>0`,
`\cosθ=(1-s²)/w`, `\sinθ=2s/w`.

The hypotheses we use are exactly those in the statement:
`K` lies strictly inside triangle `BMC`; `L` lies strictly inside triangle `BNC`;
`K` lies inside angle `LBA`; `L` lies inside angle `ACK`; and the three angle equalities
`∠KBA=∠ACL(=θ)`, `∠LBK=∠LNC`, `∠LCK=∠BMK`. Let `O` be the circumcentre of `AKL`
(so `A,K,L` are noncollinear and `O` exists).

### 1. Reduction: `OM=ON ⟺ O_x=(2p+a)/4`

Let `O=(O_x,O_y)`. Since `M,N` share the height `q/2`,
```
OM² − ON² = (O_x−p/2)² + (O_y−q/2)² − (O_x−(p+a)/2)² − (O_y−q/2)²
          = (O_x−p/2)² − (O_x−(p+a)/2)².
```
Factoring the difference of two squares,
```
OM² − ON² = [ (O_x−p/2) − (O_x−(p+a)/2) ]·[ (O_x−p/2) + (O_x−(p+a)/2) ]
          = (a/2)·( 2O_x − (2p+a)/2 ).
```
Because `a>0`, we get `OM=ON ⇔ OM²=ON² ⇔ 2O_x=(2p+a)/2 ⇔`
```
      O_x = (2p+a)/4.                                            (1)
```
(Equivalently, `O` lies on the perpendicular bisector of the horizontal segment `MN`,
whose equation is `x=(M_x+N_x)/2=(2p+a)/4`. This also equals the stated form
`OB²−OC²=(AB²−AC²)/2`: indeed `OB²−OC²=2aO_x−a²` and `AB²−AC²=2ap−a²`, so that identity
reads `2aO_x−a²=(2ap−a²)/2`, i.e. `O_x=(2p+a)/4`.) All of §1 is pure vector algebra and
uses no property of `K,L`.

### 2. Parametrising `K` and `L` on the two rays (branches fixed)

**Placement of `K`.** By condition 1, ray `BK` makes angle `θ` with ray `BA`. We first
pin down on which side of line `BA` the point `K` lies. Line `BA` passes through `B`
and `M` (as `M∈AB`). Its two open half-planes are distinguished by the sign of
`cross(A−B,\,X−B)`. For `X=C`: `cross((p,q),(a,0))=p·0−q·a=−qa<0`. Triangle `BMC` has
the edge `BM` lying **on** line `BA`, and its third vertex `C` in the half-plane
`cross(A−B,\cdot)<0`; hence the whole (closed) triangle `BMC` lies in that half-plane,
and `K`, being strictly inside it, satisfies `cross(A−B,\,K−B)<0`. Thus `K` lies on the
**clockwise** side of ray `BA`. The ray from `B` at angle `θ` clockwise of `BA` has
direction `R(−θ)(p,q)`, where `R(φ)` is rotation by `φ`; scaling by `w>0`,
```
u := w·R(−θ)(p,q) = (\,p(1−s²)+2qs,\;\; −2ps+q(1−s²)\,).
```
Indeed `cross(A−B,u)=cross((p,q),wR(−θ)(p,q))=w|A−B|²\sin(−θ)=−w|A|²\sinθ<0`, matching the
side of `K`. Since `K` is on this ray at positive distance from `B`,
```
      K = t_K·u,     t_K>0.                                      (2)
```

**Placement of `L`.** By condition 1, ray `CL` makes angle `θ` with ray `CA`. Line `CA`
passes through `C` and `N` (as `N∈AC`); sides are distinguished by
`cross(A−C,\,X−C)`. For `X=B`: `cross((p−a,q),(−a,0))=(p−a)·0−q·(−a)=qa>0`. Triangle
`BNC` has edge `CN` on line `CA` and third vertex `B` in the half-plane
`cross(A−C,\cdot)>0`; so `L`, strictly inside `BNC`, satisfies `cross(A−C,\,L−C)>0`, i.e.
`L` is on the **counterclockwise** side of ray `CA`. The ray from `C` at angle `θ` CCW of
`CA` has direction `R(+θ)(A−C)`; scaling by `w`,
```
d_L := w·R(+θ)(p−a,q) = (\,(p−a)(1−s²)−2qs,\;\; (p−a)(2s)+q(1−s²)\,),
```
with `cross(A−C,d_L)=w|A−C|²\sinθ>0`, matching the side of `L`. Hence
```
      L = C + t_L·d_L,     t_L>0.                                (3)
```

From here on all quantities are polynomials in `p,q,a,s,t_K,t_L`. (Only conditions 1 and
the region hypotheses have been used so far, to fix the two rays and the two branches.)

### 3. Orientation lemma

We record four signed areas; the first two are computed directly, the last two follow
from the "inside the angle" hypotheses.

**(i)** `cross(B−M,\;K−M) = \tfrac12(qK_x−pK_y)`. Using `(2)`,
`qK_x−pK_y=t_K\big(q(p(1−s²)+2qs)−p(−2ps+q(1−s²))\big)=t_K(2q²s+2p²s)`, so
```
      cross(B−M,\,K−M)=s\,t_K\,(p²+q²)>0.                        (4)
```
(Verified symbolically in `verify.py`, line "cross(MB,MK)".) Thus `M,B,K` are CCW, i.e.
`δ(B−M,\,K−M)∈(0,π)` and equals the angle `∠BMK`.

**(ii)** Similarly `cross(L−N,\;C−N)=s\,t_L\,((p−a)²+q²)>0` (script line
"cross(NL,NC)"), so `N,L,C` are CCW and `δ(L−N,\,C−N)=∠LNC∈(0,π)`.

**(iii)** `cross(L−B,\,K−B)>0`. By §2, `K` and `L` both lie on the clockwise side of ray
`BA` (for `L`: `cross(A−B,L−B)=cross((p,q),N... )`; concretely
`cross(A−B,\,N−B)=cross((p,q),((p+a)/2,q/2))=(pq−q(p+a))/2=−qa/2<0`, and `N` is a vertex of
`BNC` while `B∈BA,\;C` is on the same clockwise side as shown in §2, so all of `BNC`,
hence `L`, is on that side: `cross(A−B,\,L−B)<0`). So rays `BK,BL` are both clockwise of
`BA`; their oriented angles from `BA` are `δ(A−B,K−B)=−∠KBA` and `δ(A−B,L−B)=−∠LBA`,
both in `(−π,0)`. The hypothesis "`K` inside angle `LBA`" means ray `BK` is strictly
between rays `BA` and `BL`, i.e. `∠KBA<∠LBA`; hence `−∠LBA<−∠KBA<0` and
`δ(B... )`: measuring from `BL` to `BK`,
`δ(L−B,\,K−B)=δ(A−B,K−B)−δ(A−B,L−B)=(−∠KBA)−(−∠LBA)=∠LBA−∠KBA=∠LBK∈(0,π)`.
Therefore `cross(L−B,\,K−B)>0` and `δ(L−B,\,K−B)=∠LBK`.

**(iv)** `cross(L−C,\,K−C)>0`. By §2, `K` and `L` both lie on the CCW side of ray `CA`
(for `K`: `cross(A−C,\,M−C)=cross((p−a,q),(p/2−a,q/2))=((p−a)q/2−q(p/2−a))=aq/2>0`, and
`M` is a vertex of `BMC` with `B` on the same CCW side as shown in §2, so all of `BMC`,
hence `K`, is on that side: `cross(A−C,\,K−C)>0`). So rays `CL,CK` are both CCW of `CA`;
their oriented angles from `CA` are `δ(A−C,L−C)=+∠ACL` and `δ(A−C,K−C)=+∠ACK`, both in
`(0,π)`. The hypothesis "`L` inside angle `ACK`" means ray `CL` is strictly between rays
`CA` and `CK`, i.e. `∠ACL<∠ACK`; hence
`δ(L−C,\,K−C)=δ(A−C,K−C)−δ(A−C,L−C)=∠ACK−∠ACL=∠LCK∈(0,π)`.
Therefore `cross(L−C,\,K−C)>0` and `δ(L−C,\,K−C)=∠LCK`.

### 4. Encoding conditions 2 and 3, and the decoupling

Define
```
E2 := cross(L−B,K−B)·dot(L−N,C−N) − cross(L−N,C−N)·dot(L−B,K−B),
E3 := cross(L−C,K−C)·dot(B−M,K−M) − cross(B−M,K−M)·dot(L−C,K−C).
```
Using `cross(V,W)=|V||W|\sinδ(V,W)`, `dot(V,W)=|V||W|\cosδ(V,W)` and the sine
subtraction formula,
```
E2 = |L−B||K−B||L−N||C−N|·\sin(\,δ(L−B,K−B) − δ(L−N,C−N)\,),
E3 = |L−C||K−C||B−M||K−M|·\sin(\,δ(L−C,K−C) − δ(B−M,K−M)\,).
```
By the Orientation Lemma, `δ(L−B,K−B)=∠LBK`, `δ(L−N,C−N)=∠LNC`,
`δ(L−C,K−C)=∠LCK`, `δ(B−M,K−M)=∠BMK`, all lying in `(0,π)`. Hence each argument of
`\sin` lies in `(−π,π)`, where `\sin` vanishes only at `0`. Since all length factors are
nonzero,
```
E2=0 ⇔ ∠LBK=∠LNC   (condition 2),
E3=0 ⇔ ∠LCK=∠BMK   (condition 3).
```
Thus the two remaining angle conditions are **equivalent** to `E2=0` and `E3=0`.

**Decoupling.** In coordinates `B=0`, `K−B=K=t_K u`, so both `cross(L−B,K−B)=t_K\,
cross(L,u)` and `dot(L−B,K−B)=t_K\,dot(L,u)` carry a factor `t_K`; therefore
`E2=t_K·H`, where
```
H := cross(L,u)·dot(L−N,C−N) − cross(L−N,C−N)·dot(L,u)
```
is independent of `t_K`. A direct expansion (script: `H=E2/t_K`) shows `H` depends only
on `t_L` (and `p,q,a,s`) and is quadratic in `t_L`. Symmetrically, in `E3` every term
carries a factor `t_L` coming from `L−C=t_L d_L`, so `E3=t_L·G`, where
```
G := cross(d_L,K−C)·dot(B−M,K−M) − cross(B−M,K−M)·dot(d_L,K−C)
```
depends only on `t_K` and is quadratic in `t_K`. (Both facts are asserted and checked in
`verify.py`: "H depends only on tL, G only on tK".) Since `t_K>0` and `t_L>0` by `(2),(3)`,
```
      E2=0 ⇔ H(t_L)=0,        E3=0 ⇔ G(t_K)=0.                   (5)
```

### 5. The circumcentre identity

With `A=(p,q)`, `K=(K_x,K_y)`, `L=(L_x,L_y)`, the circumcentre `O` of `AKL` has
`x`-coordinate `O_x = \mathrm{num}_x / D`, where (standard circumcentre formula, obtained
by solving the two perpendicular-bisector equations `|O−A|²=|O−K|²`, `|O−A|²=|O−L|²`)
```
D      = 2\big(A_x(K_y−L_y)+K_x(L_y−A_y)+L_x(A_y−K_y)\big),
num_x  = (A_x²+A_y²)(K_y−L_y)+(K_x²+K_y²)(L_y−A_y)+(L_x²+L_y²)(A_y−K_y),
```
and `D≠0` because `A,K,L` are noncollinear (a circumcentre exists). By `(1)`, the goal
`OM=ON` is equivalent to `O_x=(2p+a)/4`, i.e. to `4\,num_x=(2p+a)D`, i.e. to
```
      T := 4\,num_x − (2p+a)\,D = 0.                             (6)
```

Now the crux. Treat `G` as a polynomial in `t_K` and `H` as a polynomial in `t_L` over
the field `\mathbb{Q}(p,q,a,s)`. Their leading coefficients are, by direct computation
(`verify.py`, "lcG/lcH factor"),
```
      lc_{t_K}(G) = \tfrac12(1+s²)²·(p²+q²)·f,
      lc_{t_L}(H) = \tfrac12(1+s²)²·((p−a)²+q²)·f,   where
      f := 2s(p²+q²) − 2aps + aq(1−s²).                            (7)
```
Performing polynomial division of `T` by `G` in `t_K`, then dividing the remainder by `H`
in `t_L`, produces cofactors whose **only** denominator is a power of these leading
coefficients; after clearing that denominator one obtains an identity with **polynomial**
cofactors. Concretely, `verify.py` exhibits polynomials `Q_G,Q_H∈\mathbb{Q}[p,q,a,s,t_K,t_L]`
with
```
      f·T = Q_G·G + Q_H·H          (identically in t_K,t_L,p,q,a,s).   (8)
```
This is an **exact** polynomial identity: the script forms `Q_G,Q_H` by exact division,
multiplies through by the denominator content — which it verifies equals `f` exactly
(`c − f = 0`) — and checks `expand(f·T − (Q_G·G + Q_H·H)) = 0` together with
`denom(Q_G)=denom(Q_H)=1` (the `assert` statements). Its output is
```
EXACT polynomial identity  f*T-(QG*G+QH*H) = 0
```
Because every coefficient in `(8)` is a polynomial in the symbols `p,q,a,s`, it is a genuine
identity for **every** triangle `(p,q,a)` and every `θ` (via `s`), not a numerical
coincidence; in particular it entails `f·T = 0` at any configuration with `G=H=0`, with no
denominators anywhere.

**Positivity of `f`.** We claim `f>0` on the admissible region, so that `(8)` may be
divided by `f`. First, the algebraic meaning of `f`. Recall `AB=|A−B|=\sqrt{p²+q²}`,
`AC=|A−C|=\sqrt{(p−a)²+q²}`, both `>0`, and let `∠A=∠BAC∈(0,π)` be the apex angle. The
two standard identities
```
   AB·AC·\cos∠A = dot(B−A,\,C−A) = (−p)(a−p)+(−q)(−q) = p²+q²−ap,
   AB·AC·\sin∠A = |cross(B−A,\,C−A)| = |(−p)(−q)−(−q)(a−p)| = qa   (q,a>0),
```
combined with `\cosθ=(1−s²)/(1+s²)`, `\sinθ=2s/(1+s²)` and the sine addition formula, give
```
 (1+s²)·AB·AC·\sin(∠A+θ)
   = (1+s²)\big(AB·AC\sin∠A·\cosθ + AB·AC\cos∠A·\sinθ\big)
   = (1+s²)\Big(qa·\tfrac{1−s²}{1+s²} + (p²+q²−ap)·\tfrac{2s}{1+s²}\Big)
   = qa(1−s²) + 2s(p²+q²−ap) = f,
```
i.e.
```
      f = (1+s²)·AB·AC·\sin(∠A+θ).                                (9)
```
(The equality `f − (1+s²)·AB·AC·\sin(∠A+θ)=0` is also checked as an exact symbolic zero in
`verify.py`, "f - (1+s^2)*AB*AC*sin(A+theta)".) In `(9)`, `1+s²>0`, `AB>0`, `AC>0`; it
remains to show `\sin(∠A+θ)>0`, i.e. `∠A+θ∈(0,π)`.

Since `∠A>0` and `θ>0`, certainly `∠A+θ>0`. For the upper bound we use the region
hypothesis on `K`. The point `M` is the midpoint of segment `AB`, hence lies on the ray
from `B` through `A`, so ray `BM` = ray `BA` and the angle of triangle `BMC` at vertex `B`
equals `∠(BA,BC)=∠ABC`. As `K` lies **strictly inside** triangle `BMC`, ray `BK` lies
strictly between the two sides `BM (=BA)` and `BC` of that angle; therefore
`θ=∠KBA<∠ABC`. Finally, from the angle sum of triangle `ABC`,
`∠A+∠ABC+∠ACB=π` with `∠ACB>0`, so `∠A+∠ABC=π−∠ACB<π`. Combining,
```
      0 < ∠A+θ < ∠A+∠ABC < π,
```
hence `\sin(∠A+θ)>0`, and by `(9)`,
```
      f > 0.                                                      (10)
```

### 6. Conclusion

By the hypotheses and Step 4, conditions 2 and 3 give `E2=E3=0`, hence by `(5)`
`G(t_K)=0` and `H(t_L)=0`. Substituting into the polynomial identity `(8)`,
```
f·T = Q_G·G + Q_H·H = Q_G·0 + Q_H·0 = 0.
```
By `(10)`, `f>0`, in particular `f≠0`, so we may divide: `T=0`, which is `(6)`. Therefore
`O_x=(2p+a)/4`, and by Step 1 this is equivalent to `OM=ON`.

Note that the potential `0·∞` pitfall — specializing the rational-cofactor form
`T=q_G·G+q_H·H` at a configuration where a cofactor denominator vanishes — is entirely
avoided: identity `(8)` has **polynomial** cofactors, valid unconditionally, and the single
scalar `f` that we divide out at the end is proven strictly positive by `(10)`. The only
place the region hypothesis "`K∈△BMC`" enters the metric argument is exactly here, to force
`θ<∠ABC` and hence `f>0`.

Since the only inputs were the problem's hypotheses (the three angle equalities and the
four region/containment conditions), this holds for **every** admissible `(K,L)` — the
whole 1-parameter family. Hence `OM=ON`. ∎

**Remark (self-containedness of the computation).** Steps 1–5 reduce the problem, by
elementary and fully justified geometry, to the polynomial identity `(8)` and the positivity
`(10)`. Identity `(8)` is a finite, exact algebraic fact in `\mathbb{Q}[p,q,a,s,t_K,t_L]`,
exhibited (not merely sampled) by the exact division-and-clearing in
`results/imo-2026-02/verify.py`; positivity `(10)` is proved purely synthetically from the
angle sum and the region hypothesis. No floating-point evaluation is used as a proof step;
the numerics in the development only guided the choice of branch, which Step 3 then proves.

## Promotable lemmas
- **L1 (goal reduction, coordinate form).** With `B=(0,0),C=(a,0),A=(p,q)` and `M,N`
  the midpoints of `AB,AC`, for any point `O` one has
  `OM²−ON²=(a/2)\big(2O_x−(2p+a)/2\big)`; hence for the circumcentre `O` of `AKL`,
  `OM=ON ⇔ O_x=(2p+a)/4 ⇔ OB²−OC²=(AB²−AC²)/2`. Proved in §1 (pure vector algebra).
- **L-orient (branch fixing).** Under the region hypotheses, in the frame of §0:
  `K` lies on the clockwise side of ray `BA` and the CCW side of ray `CA`; `L` lies on
  the clockwise side of ray `BA` and the CCW side of ray `CA`; and consequently
  `δ(L−B,K−B)=∠LBK`, `δ(L−C,K−C)=∠LCK`, `δ(B−M,K−M)=∠BMK`, `δ(L−N,C−N)=∠LNC`, all in
  `(0,π)`. Proved in §2–§3. This is what converts the three unsigned angle equalities
  into the polynomial equations without sign ambiguity.
- **L-pos (positivity of the leading content).** In the frame of §0 with `θ=∠KBA=∠ACL`,
  the common (up to positive factors `\tfrac12(1+s²)²·AB²` resp. `\tfrac12(1+s²)²·AC²`)
  leading coefficient of the condition polynomials `G,H` equals
  `f=2s(p²+q²)−2aps+aq(1−s²)=(1+s²)·AB·AC·\sin(∠A+θ)`, and `f>0` on the admissible region
  because `θ=∠KBA<∠ABC` (as `K∈△BMC`) and `∠A+∠ABC=π−∠ACB<π`, so `∠A+θ∈(0,π)`. Proved in
  §5. This is exactly the nonvanishing that licenses dividing the polynomial identity
  `f·T=Q_G·G+Q_H·H` by `f` at an admissible configuration.
