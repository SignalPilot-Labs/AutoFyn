## Status
solved

## Approaches tried
- (new, round 1) Coordinate/complex bash on the whole 1-parameter family: place BC on the x-axis
  so MN is horizontal, and prove O_x ≡ (M+N)_x/2 as an algebraic identity in the free parameter. —
  ENGINE WORKED but round-1 write-up OVERCLAIMED: the two remaining angle conditions **decouple**
  (each depends on only one of K, L after cancelling the positive ray-length factor), giving two
  independent quadratics FK(u)=0, FL(v)=0, and T lies in the ideal ⟨FK,FL⟩ via an *exact* polynomial
  identity aK·aL·T = aL·QK·FK + QL·FL (residual exactly 0). The load-bearing gap was that the
  DIRECTED equations FK=FL=0 were justified numerically, not proved from interiority.
- (revise, round 2) Install a rigorous **Orientation Lemma** (barycentric half-plane + ray-betweenness
  sign chain, coordinate-free) that upgrades the three UNSIGNED angle hypotheses to the DIRECTED
  equalities (sign ε=+1), converting the problem's unsigned angle equalities to FK=FL=0 with no
  numerics and no global continuity. — WORKED. This closes the round-1 gap; the algebraic engine
  (§1,§2,§4,§5) is imported verbatim (certified). Status: **solved**.

## Current best
Complete proof below. Load-bearing facts, all now rigorous:
1. OM=ON ⟺ T:=det1−(M_x+N_x)·det2 = 0 (equal-height circumcentre reduction; certified,
   `lemmas/reduction-OMeqON.md`).
2. **Orientation Lemma** (`lemmas/orientation-sign.md`): interiority + betweenness pin
   cross(BK,BL)=cross(NC,NL)<0 and cross(CL,CK)=cross(MB,MK)>0, hence the unsigned hypotheses
   ∠LBK=∠LNC, ∠LCK=∠BMK become the DIRECTED equalities, i.e. FK=FL=0 with ε=+1.
3. The exact polynomial identity aK·aL·T = aL·QK·FK + QL·FL in ℤ[a,p,q,h,c,s,u,v]; hence FK=FL=0
   and aK·aL≠0 force T=0.
4. aK,aL vanish only at isolated parameter values; continuity of T over the connected admissible
   family closes those (this continuity is scoped ONLY to the finite aK·aL=0 zero-set, not to
   orientation).

## Full proof

Throughout, points of the plane are identified with complex numbers z=x+iy; for w∈ℂ we write
Re w, Im w, w̄. For real plane vectors u=(u₁,u₂), v=(v₁,v₂) put cross(u,v)=u₁v₂−u₂v₁, and for
points P,Q,R put cross(PQ,PR):=cross(Q−P,R−P) and [PQR]:=½cross(PQ,PR) (signed area, alternating
and cyclic). "Directed angle from ray PX to ray PY" means arg((Y−P)/(X−P)). The symbolic
computations of §4–§5 are exact (rational arithmetic) polynomial identities, reproducible with the
scripts noted at the end; each is an equality of polynomials verifiable by direct expansion.

### 1. Coordinates and the reduction of OM=ON to a determinant identity

Since M, N are the midpoints of AB, AC, the segment MN is the A-midline, so MN ∥ BC and
|MN|=|BC|/2 (Midline theorem, KB "Triangle centres / midlines"). Place BC on the x-axis, A above it,
and fix the plane orientation so that △ABC is positively oriented (WLOG; the two orientations of the
plane are interchangeable). Concretely:
  B=(−p,0), C=(q,0) with p,q>0 (so p+q=|BC|), and A=(a,h) with h>0.
Then [ABC]=½cross(B−A,C−A)=½·h(p+q)>0, consistent with the convention. Also
  M=((a−p)/2, h/2), N=((a+q)/2, h/2),
so **M_y=N_y=h/2**: M and N have equal height. Consequently the perpendicular bisector of MN is the
vertical line x=(M_x+N_x)/2, and for the circumcentre O of △AKL,
  OM=ON ⟺ O lies on that perpendicular bisector ⟺ O_x=(M_x+N_x)/2.        (1)

Write ⊙AKL as x²+y²+Dx+Ey+F=0; its centre is (−D/2,−E/2), so O_x=−D/2. Plugging A,K,L into the
circle equation gives a linear system for (D,E,F); by Cramer's rule (the coefficient determinant is
det2:=det[[x_A,y_A,1],[x_K,y_K,1],[x_L,y_L,1]], nonzero because A,K,L are not collinear — they lie on
a genuine circle),
  D = −det1/det2,  det1:=det[[x_A²+y_A²,y_A,1],[x_K²+y_K²,y_K,1],[x_L²+y_L²,y_L,1]].
Hence O_x=det1/(2·det2), and (1) becomes
  OM=ON ⟺ det1=(M_x+N_x)·det2 ⟺  **T:=det1−(M_x+N_x)·det2 = 0.**        (2)

So it suffices to prove the scalar identity T=0 for the configuration. (This is the certified
"equal-height circumcentre reduction", `lemmas/reduction-OMeqON.md`.)

### 2. Parametrisation of K and L (rotation signs justified, not assumed)

Let θ:=∠KBA=∠ACL (the equal angles of the first hypothesis); θ∈(0,π). We claim
  K = B + u·e^{−iθ}(A−B),   L = C + v·e^{+iθ}(A−C),   u:=λ_K>0, v:=λ_L>0.   (3)
The magnitudes are immediate: |K−B|=u|A−B| with u=|BK|/|BA|>0, and ∠KBA=θ forces the direction
K−B to be (A−B) rotated by ±θ; likewise for L with ∠ACL=θ. The **sign** of each rotation is fixed by
interiority, via the Orientation Lemma (§3, facts (i),(i′)): K∈int△BMC lies on the C-side of line AB,
so cross(BA,BK)<0, which means K−B is (A−B) rotated *clockwise* (by −θ); indeed
cross(A−B, e^{−iθ}(A−B))=|A−B|²·sin(−θ)<0 for θ∈(0,π). Symmetrically L∈int△BNC lies on the B-side of
line AC, so cross(CA,CL)>0, i.e. L−C is (A−C) rotated *counter-clockwise* (by +θ). This pins (3).
Write c:=cosθ, s:=sinθ.

### 3. Orientation Lemma: the unsigned hypotheses become directed equalities

We prove the load-bearing sign facts. All of §3 is the coordinate specialisation of the certified
coordinate-free lemma `lemmas/orientation-sign.md`; we reproduce it here for self-containedness.

**Two elementary sub-lemmas.**

*Lemma B (betweenness sign).* If y,z are linearly independent plane vectors and w=βy+γz with
β,γ>0, then cross(y,w)=γ·cross(y,z) and cross(w,z)=β·cross(y,z); hence cross(y,w), cross(w,z),
cross(y,z) are all nonzero and share one sign.
*Proof.* Bilinearity of cross with cross(y,y)=cross(z,z)=0 gives the identities; cross(y,z)≠0 by
independence and β,γ>0, so all three equal a positive multiple of cross(y,z). ∎

*Lemma I (interior ⟹ positive combination).* If X is strictly interior to nondegenerate △VYZ then
X−V=β(Y−V)+γ(Z−V) with β,γ>0.
*Proof.* Take signed-area barycentrics α=[XYZ]/[VYZ], β=[VXZ]/[VYZ], γ=[VYX]/[VYZ]. The signed-area
identity [XYZ]+[VXZ]+[VYX]=[VYZ] gives α+β+γ=1, and expansion gives X=αV+βY+γZ. X strictly interior
means X is on the interior side of each edge-line, i.e. [XYZ],[VXZ],[VYX] all share the sign of
[VYZ]; hence α,β,γ>0. Subtracting V=(α+β+γ)V yields X−V=β(Y−V)+γ(Z−V). ∎
"Ray VX strictly between rays VY, VZ" *means* X−V=β(Y−V)+γ(Z−V) with β,γ>0, and by Lemma I this holds
whenever X∈int△VYZ; it is also the literal meaning of "X inside the nonreflex angle ∠YVZ".

**Fixed reference signs.** By Fact 0 below, [NBC]=½[ABC] and [MBC]=½[ABC]. Hence, using
[PQR]=½cross(PQ,PR) and the cyclic/alternating reorderings,
  cross(BA,BC)=cross(A−B,C−B)=2[BAC]=−2[ABC]<0,       cross(CA,CB)=cross(A−C,B−C)=2[CAB]=+2[ABC]>0,
  cross(NB,NC)=cross(B−N,C−N)=2[NBC]=+[ABC]>0,          cross(MB,MC)=cross(B−M,C−M)=2[MBC]=+[ABC]>0.
*Fact 0 (midpoint halving).* N=½(A+C) ⟹ N−B=½(A−B)+½(C−B), so cross(N−B,C−B)=½cross(A−B,C−B)=[ABC],
i.e. [NBC]=½[ABC]; identically M=½(A+B) ⟹ M−C=½(A−C)+½(B−C) ⟹ cross(M−C,B−C)=½cross(A−C,B−C)=[ABC],
i.e. [MBC]=½[ABC]. (In the coordinates of §1: cross(BA,BC)=−h(p+q), cross(CA,CB)=+h(p+q),
cross(NB,NC)=cross(MB,MC)=+h(p+q)/2 — all verified exactly in sympy, zero residual.)

**Target signs.**

- *cross(BK,BL)<0.* (i) K∈int△BMC; edge BM⊂line AB (M∈AB), opposite vertex C. By Lemma I at B,
  K−B=β(M−B)+γ(C−B) with β,γ>0; since M−B=½(A−B), this is a positive combination of A−B and C−B, so
  by Lemma B (y=A−B, z=C−B) cross(BA,BK) shares the sign of cross(BA,BC)=−2[ABC]<0. Thus
  cross(BA,BK)<0. (ii) "K inside ∠LBA" ⟹ ray BK strictly between rays BA, BL, i.e.
  K−B=β′(A−B)+γ′(L−B), β′,γ′>0; by Lemma B (y=A−B, z=L−B) cross(BA,BK) and cross(BK,BL) share the
  sign of cross(BA,BL). Hence cross(BK,BL) has the same sign as cross(BA,BK)<0, so **cross(BK,BL)<0**.

- *cross(NC,NL)<0.* L∈int△BNC. By Lemma I at N, L−N=β(B−N)+γ(C−N) with β,γ>0; by Lemma B
  (y=B−N, z=C−N), cross(NB,NL), cross(NL,NC), cross(NB,NC) share one sign, that of
  cross(NB,NC)=+[ABC]>0. So cross(NL,NC)>0, and by antisymmetry **cross(NC,NL)=−cross(NL,NC)<0**.

- *cross(CL,CK)>0.* (i′) L∈int△BNC; edge CN⊂line AC (N∈AC), opposite vertex B. By Lemma I at C,
  L−C=β(N−C)+γ(B−C), β,γ>0; N−C=½(A−C) makes this a positive combination of A−C and B−C, so by
  Lemma B cross(CA,CL) shares the sign of cross(CA,CB)=+2[ABC]>0, giving cross(CA,CL)>0. (ii′)
  "L inside ∠ACK" ⟹ ray CL strictly between rays CA, CK, i.e. L−C=β′(A−C)+γ′(K−C), β′,γ′>0; by
  Lemma B cross(CA,CL) and cross(CL,CK) share one sign, so **cross(CL,CK)>0**.

- *cross(MB,MK)>0.* K∈int△BMC. By Lemma I at M, K−M=β(B−M)+γ(C−M), β,γ>0; by Lemma B
  cross(MB,MK), cross(MK,MC), cross(MB,MC) share one sign, that of cross(MB,MC)=+[ABC]>0, so
  **cross(MB,MK)>0**.

(The map σ:(B↔C,M↔N,K↔L) is a *reflection*, hence reverses plane orientation; that is precisely why
the second pair of target signs is + while the first is −. To avoid any sign-flip bookkeeping we
derived the second pair directly, by the same two sub-lemmas at C and M, rather than transporting the
first pair through σ.)

**No reflex reading.** The hypotheses "K inside ∠LBA", "L inside ∠ACK" are read with the nonreflex
angles: ∠LBA,∠ACK∈(0,π), because the bounding rays are never opposite (B,L,A and A,C,K are
non-collinear triples in an admissible configuration), so "strictly between" is the literal reading
with no +π alternative.

**Directed upgrade.** For nonzero z₁,z₂∈ℂ, sign(Im[z₂·conj(z₁)])=sign(arg(z₂/z₁)), and |arg(z₂/z₁)|
is the unsigned angle between z₁,z₂, a value in [0,π].

*Condition A (∠LBK=∠LNC).* Put α:=arg((L−B)/(K−B)), α′:=arg((L−N)/(C−N))∈(−π,π). Then
sign α = sign Im[(L−B)conj(K−B)] = sign cross(K−B,L−B) = sign cross(BK,BL) < 0, and
sign α′ = sign Im[(L−N)conj(C−N)] = sign cross(C−N,L−N) = sign cross(NC,NL) < 0.
So α,α′ are both negative; |α|=∠LBK and |α′|=∠LNC are equal by hypothesis and lie in (0,π). Two
numbers in (−π,0) with equal absolute value are equal, so α=α′, i.e.
  arg((L−B)/(K−B)) = arg((L−N)/(C−N)).        (4)
Equivalently arg[(L−B)(C−N)/((K−B)(L−N))]=α−α′=0, so this ratio is a positive real and
  EA := Im[(L−B)(C−N)·conj((K−B)(L−N))] = 0,   with ε=+1.        (4′)

*Condition B (∠LCK=∠BMK).* Identically, with β̂:=arg((K−C)/(L−C)), β̂′:=arg((K−M)/(B−M)):
sign β̂ = sign cross(L−C,K−C)=sign cross(CL,CK)>0 and sign β̂′=sign cross(B−M,K−M)=sign cross(MB,MK)>0.
Both positive; |β̂|=∠LCK and |β̂′|=∠BMK are equal by hypothesis in (0,π); so β̂=β̂′, i.e.
  arg((K−C)/(L−C)) = arg((K−M)/(B−M)),        (5)
and
  EB := Im[(K−C)(B−M)·conj((L−C)(K−M))] = 0,   with ε=+1.        (5′)

This is the sole content that was missing in round 1; it uses only interiority/betweenness, no
numerics and no continuity.

### 4. Decoupling of (4′),(5′) into single-variable quadratics

Substitute (3). Since K−B=u·e^{−iθ}(A−B), conj(K−B)=u·e^{+iθ}·conj(A−B); the positive factor u pulls
out of EA:
  EA = u·FL,   FL := Im[ (L−B)(C−N)·e^{+iθ}·conj(A−B)·conj(L−N) ].       (6)
FL contains no u, and since L−B, conj(L−N) are each affine in v, FL is a quadratic polynomial in v
alone. As u>0, (4′) ⟺ **FL(v)=0**. Symmetrically L−C=v·e^{+iθ}(A−C), conj(L−C)=v·e^{−iθ}·conj(A−C),
so
  EB = v·FK,   FK := Im[ (K−C)(B−M)·e^{−iθ}·conj(A−C)·conj(K−M) ],       (7)
a quadratic in u alone, and (5′) ⟺ **FK(u)=0**. Expanding (`/tmp/sym9.py`),
FL(v)=a_L v²+b_L v+c_L and FK(u)=a_K u²+b_K u+c_K, with leading coefficients
  a_L = ½(c²+s²)·((a−q)²+h²)·W,   a_K = −½(c²+s²)·((a+p)²+h²)·W,          (8)
  W := −[(a²+ap−aq+h²−pq)·s + h(p+q)·c],
where (a−q)²+h²=|CA|²>0 and (a+p)²+h²=|AB|²>0 (verified exactly in `/tmp/final.py`).

### 5. The circumcentre identity T=0

Substituting (3) into T (from (2)) gives a polynomial T(u,v) of degree 2 in each of u,v with
coefficients in ℤ[a,p,q,h,c,s] (`/tmp/clean.py`). The algebraic crux is:

> **Lemma (ideal identity).** In ℤ[a,p,q,h,c,s,u,v] there are explicit polynomials QK, QL with
>   **a_K·a_L·T  =  a_L·QK·FK  +  QL·FL.**            (9)

*Proof.* Pseudo-divide T by FK in u (deg_u T=deg_u FK=2, leading coeff a_K):
  a_K·T = QK·FK + R1,   R1 linear in u,          (9a)
an exact polynomial identity (`/tmp/clean.py` verifies a_K·T−(QK·FK+R1)=0 identically). Pseudo-divide
R1 by FL in v (deg_v R1=deg_v FL=2, leading coeff a_L):
  a_L·R1 = QL·FL + R2,          (9b)
and the computation returns **R2=0 exactly** (`/tmp/clean.py` verifies a_L·R1−QL·FL=0 identically).
Multiplying (9a) by a_L and using (9b),
  a_K·a_L·T = a_L·QK·FK + a_L·R1 = a_L·QK·FK + QL·FL,
which is (9). The single expansion a_K·a_L·T−(a_L·QK·FK+QL·FL)=0 is confirmed directly. ∎
No relation between c,s is needed: (9) is an identity in the free indeterminates a,p,q,h,c,s,u,v.

### 6. Conclusion

Fix any admissible configuration, with parameter θ (so c²+s²=1) and the corresponding u=λ_K>0,
v=λ_L>0 from (3). By §3–§4, Conditions A and B give the directed equalities (4′),(5′), i.e.
  FL(v)=0  and  FK(u)=0.
Substituting into the right-hand side of (9) makes it vanish, so
  a_K·a_L·T = 0.          (10)

*Non-degeneracy.* By (8), on c²+s²=1, a_K·a_L = −¼·|AB|²·|CA|²·W². Now |AB|²,|CA|²>0, and
  W = −[(a²+ap−aq+h²−pq)·sinθ + h(p+q)·cosθ]
is a single sinusoid in θ whose cosine coefficient h(p+q)=h·|BC|>0; hence W is not identically zero and
W(θ)=0 only at isolated θ. So a_K·a_L≠0 for all admissible θ except finitely many, and at every such
θ equation (10) forces **T=0**. For the finitely many θ with a_K·a_L=0: along the connected admissible
family the geometric roots K(θ),L(θ) of FK,FL and hence O(θ) vary continuously, so T(θ) is continuous;
it vanishes on the admissible interval minus a finite set, hence vanishes there too by continuity.
(This continuity argument is used ONLY to fill the finite a_K·a_L=0 zero-set; it plays no role in the
orientation step.) Thus **T=0 for every admissible configuration.**

By (2) this gives O_x=(M_x+N_x)/2, i.e. O lies on the perpendicular bisector of MN (recall
M_y=N_y=h/2), and therefore by (1)
  **OM = ON.**    ∎

### Reproducibility note (algebra only; orientation is proved, not checked numerically)
- `/tmp/verify_engine.py` (this build, from scratch): verifies EA=u·FL, EB=v·FK with FL a quadratic
  in v only and FK a quadratic in u only (decoupling); the leading-coefficient factorisations (8);
  the exact pseudo-division identities (9a),(9b) with R1 linear and **R2=0**; and the ideal identity
  (9) with residual identically 0. (Reproduces the round-1 scripts `/tmp/clean.py`, `/tmp/sym9.py`,
  `/tmp/final.py`.)
- The fixed reference signs and the two half-vector identities of §3 (Fact 0) are exact-zero-residual
  in sympy. The §3 target signs are PROVED (Lemmas B, I); numeric confirmation over interior
  configurations (explorers: 83 and 97 configs; one interior branch in this build) is a cross-check
  only, not a proof step.

## Promotable lemmas
- **Orientation Sign Lemma** (statement in `lemmas/orientation-sign.md`, proof there and in §3 above):
  under the admissible interiority + betweenness hypotheses, cross(BK,BL)=cross(NC,NL)<0 and
  cross(CL,CK)=cross(MB,MK)>0, whence the unsigned equalities ∠LBK=∠LNC, ∠LCK=∠BMK upgrade to the
  directed equalities (4),(5) (ε=+1). Coordinate-free (cross products / signed areas only), so
  importable by synthetic-sigma-spiral to discharge its Steps 3–4 sign bullets. **Proposed for
  certification.**
- **Equal-height circumcentre reduction** (§1): if M,N have equal y-coordinate, then OM=ON ⟺
  det1=(M_x+N_x)·det2. Already certified as `lemmas/reduction-OMeqON.md`.
- **Decoupling of the two secondary angle conditions** (§4): under (3), ∠LBK=∠LNC ⟺ FL(v)=0
  (quadratic in v only), ∠LCK=∠BMK ⟺ FK(u)=0 (quadratic in u only). Structural crux enabling the
  ideal identity (9).
