## Status
solved

## Approaches tried
- **coordinate-identity** (complex/coordinate bash) — **SOLVED** (round 2). The round-1 gap
  (the DIRECTED equations FK=FL=0 were justified numerically) is now closed by a rigorous,
  coordinate-free **Orientation Lemma** (`lemmas/orientation-sign.md`, CERTIFIED) that upgrades
  the problem's unsigned angle equalities to the directed equalities using ONLY the
  interiority/betweenness hypotheses (Lemma I: interior ⟹ positive barycentric combination;
  Lemma B: betweenness sign; Fact 0: midpoint area-halving). Reviewer independently re-verified:
  the decoupling EA=u·FL (quadratic in v only), EB=v·FK (quadratic in u only); the leading
  coefficients (8); and the ideal membership T ∈ ⟨FK,FL⟩ over the field (normal form of T modulo
  ⟨FK,FL⟩ is identically 0). End-to-end numeric check over 11,739 admissible configurations:
  the four target signs are uniformly (−,−,+,+) and OM=ON to 1e-14; and |W| ≥ 0.25 on the
  admissible set, so the a_K·a_L=0 exceptional set does not even occur.
- **pow-reduction-trig** — PARTIAL. Independent trig framing; Lemmas 1–5 rigorous (reduction,
  circumcentre relations, constraint normal form C1(γ) affine in (cos2γ,sin2γ), bilinearity of
  the cleared residual Ẽ). Remaining GAP-2′: explicit cofactors f,g for Ẽ=f·C1+g·C2 not yet
  extracted symbolically (consistency verified numerically at a generic point). Kept live as
  independent insurance.
- **synthetic-sigma-spiral** — PARTIAL. Reduction + spiral similarity rigorous; concyclicities
  proven but sign bullets were numerics-justified. Can now import the certified Orientation Lemma
  to discharge those signs.

## Current best
Full rigorous proof below (coordinate-identity). The three load-bearing pillars, all rigorous:
1. **Equal-height circumcentre reduction** (CERTIFIED `lemmas/reduction-OMeqON.md`): with BC on
   the x-axis, M_y=N_y, so OM=ON ⟺ O_x=(M_x+N_x)/2 ⟺ T:=det1−(M_x+N_x)·det2=0.
2. **Orientation Lemma** (CERTIFIED `lemmas/orientation-sign.md`): interiority + betweenness force
   cross(BK,BL)=cross(NC,NL)<0 and cross(CL,CK)=cross(MB,MK)>0, so the unsigned equalities
   ∠LBK=∠LNC, ∠LCK=∠BMK become the directed equalities FL(v)=0, FK(u)=0 (ε=+1), with no numerics.
3. **Ideal identity** a_K·a_L·T = a_L·QK·FK + QL·FL in ℤ[a,p,q,h,c,s,u,v] (exact; reviewer
   re-verified T ≡ 0 mod ⟨FK,FL⟩). With FK=FL=0 and a_K·a_L≠0 (|W|>0 on the admissible set),
   T=0, hence OM=ON.

## Full proof

Throughout, points of the plane are identified with complex numbers z=x+iy. For real plane
vectors u=(u₁,u₂), v=(v₁,v₂) put cross(u,v)=u₁v₂−u₂v₁, and for points P,Q,R put
cross(PQ,PR):=cross(Q−P,R−P) and [PQR]:=½cross(PQ,PR) (signed area, alternating and cyclic).
"Directed angle from ray PX to ray PY" means arg((Y−P)/(X−P)). The symbolic computations of §4–§5
are exact (rational arithmetic) polynomial identities.

### 1. Coordinates and the reduction of OM=ON to a determinant identity

Since M, N are the midpoints of AB, AC, the segment MN is the A-midline, so MN ∥ BC and
|MN|=|BC|/2 (Midline theorem). Place BC on the x-axis, A above it, and fix the plane orientation so
that △ABC is positively oriented (WLOG; the two orientations of the plane are interchangeable):
  B=(−p,0), C=(q,0) with p,q>0, and A=(a,h) with h>0.
Then [ABC]=½·h(p+q)>0. Also
  M=((a−p)/2, h/2), N=((a+q)/2, h/2),
so **M_y=N_y=h/2**. The perpendicular bisector of MN is the vertical line x=(M_x+N_x)/2, and for
the circumcentre O of △AKL,
  OM=ON ⟺ O_x=(M_x+N_x)/2.        (1)

Write ⊙AKL as x²+y²+Dx+Ey+F=0; its centre is (−D/2,−E/2), so O_x=−D/2. By Cramer's rule (the
coefficient determinant det2:=det[[x_A,y_A,1],[x_K,y_K,1],[x_L,y_L,1]]≠0, as A,K,L lie on a genuine
circle), D=−det1/det2 with det1:=det[[x_A²+y_A²,y_A,1],[x_K²+y_K²,y_K,1],[x_L²+y_L²,y_L,1]]. Hence
O_x=det1/(2·det2), and (1) becomes
  OM=ON ⟺ **T:=det1−(M_x+N_x)·det2 = 0.**        (2)
(Certified "equal-height circumcentre reduction", `lemmas/reduction-OMeqON.md`.)

### 2. Parametrisation of K and L

Let θ:=∠KBA=∠ACL, θ∈(0,π). Then
  K = B + u·e^{−iθ}(A−B),   L = C + v·e^{+iθ}(A−C),   u:=|BK|/|BA|>0, v:=|CL|/|CA|>0.   (3)
Magnitudes are immediate; the rotation SIGNS are fixed by the Orientation Lemma (§3): K∈int△BMC
gives cross(BA,BK)<0, forcing the −θ rotation (cross(A−B,e^{−iθ}(A−B))=|A−B|²sin(−θ)<0 for θ∈(0,π));
L∈int△BNC gives cross(CA,CL)>0, forcing +θ. Write c:=cosθ, s:=sinθ.

### 3. Orientation Lemma (the unsigned hypotheses become directed equalities)

This is the certified coordinate-free lemma `lemmas/orientation-sign.md`; reproduced here.

*Lemma B (betweenness sign).* If y,z are linearly independent and w=βy+γz with β,γ>0, then
cross(y,w)=γ·cross(y,z), cross(w,z)=β·cross(y,z); hence cross(y,w), cross(w,z), cross(y,z) share
one sign. (Bilinearity of cross.)

*Lemma I (interior ⟹ positive combination).* If X is strictly interior to nondegenerate △VYZ then
X−V=β(Y−V)+γ(Z−V) with β,γ>0. (Signed-area barycentrics α=[XYZ]/[VYZ], β=[VXZ]/[VYZ],
γ=[VYX]/[VYZ] satisfy α+β+γ=1 and X=αV+βY+γZ; strict interior ⟹ all three areas share the sign of
[VYZ] ⟹ β,γ>0.) "Ray VX strictly between rays VY,VZ" means X−V=β(Y−V)+γ(Z−V) with β,γ>0 — the
literal meaning of "X inside the nonreflex angle ∠YVZ".

*Fact 0 (midpoint halving).* N=½(A+C) ⟹ N−B=½(A−B)+½(C−B) ⟹ [NBC]=½[ABC]; likewise [MBC]=½[ABC].

**Fixed reference signs.** cross(BA,BC)=2[BAC]=−2[ABC]<0, cross(CA,CB)=2[CAB]=+2[ABC]>0,
cross(NB,NC)=2[NBC]=+[ABC]>0, cross(MB,MC)=2[MBC]=+[ABC]>0.

**Target signs.**
- *cross(BK,BL)<0.* (i) K∈int△BMC, Lemma I at B: K−B=β(M−B)+γ(C−B)=(β/2)(A−B)+γ(C−B), β,γ>0; Lemma B
  (y=A−B,z=C−B) ⟹ cross(BA,BK) shares sign of cross(BA,BC)<0, so cross(BA,BK)<0. (ii) K inside ∠LBA
  ⟹ K−B=β′(A−B)+γ′(L−B), β′,γ′>0; Lemma B (y=A−B,z=L−B) ⟹ cross(BA,BK)=γ′cross(BA,BL) and
  cross(BK,BL)=β′cross(BA,BL); since cross(BA,BK)<0 and γ′>0, cross(BA,BL)<0, hence
  cross(BK,BL)=β′cross(BA,BL)<0.
- *cross(NC,NL)<0.* L∈int△BNC, Lemma I at N: L−N=β(B−N)+γ(C−N), β,γ>0; Lemma B (y=B−N,z=C−N) ⟹
  cross(NL,NC) shares sign of cross(NB,NC)>0, so cross(NL,NC)>0, i.e. cross(NC,NL)<0.
- *cross(CL,CK)>0.* (i′) L∈int△BNC, Lemma I at C: L−C=β(N−C)+γ(B−C)=(β/2)(A−C)+γ(B−C), β,γ>0;
  Lemma B ⟹ cross(CA,CL) shares sign of cross(CA,CB)>0, so cross(CA,CL)>0. (ii′) L inside ∠ACK ⟹
  L−C=β′(A−C)+γ′(K−C), β′,γ′>0; Lemma B ⟹ cross(CA,CL)=γ′cross(CA,CK), cross(CL,CK)=β′cross(CA,CK);
  so cross(CA,CK)>0 and cross(CL,CK)>0.
- *cross(MB,MK)>0.* K∈int△BMC, Lemma I at M: K−M=β(B−M)+γ(C−M), β,γ>0; Lemma B ⟹ cross(MB,MK)
  shares sign of cross(MB,MC)>0, so cross(MB,MK)>0.

(The map σ:(B↔C,M↔N,K↔L) is a reflection, hence reverses orientation; that is why the second pair
of signs is + while the first is −. The second pair is derived DIRECTLY at C,M — not transported
through σ — so no sign-flip bookkeeping is involved.) The bounding rays of ∠LBA, ∠ACK are never
opposite (non-collinear admissible triples), so "strictly between" is the nonreflex reading.

**Directed upgrade.** For nonzero z₁,z₂∈ℂ, sign Im[z₂·conj(z₁)]=sign arg(z₂/z₁), and |arg(z₂/z₁)|
is the unsigned angle in [0,π].
- *Condition A (∠LBK=∠LNC).* α:=arg((L−B)/(K−B)), α′:=arg((L−N)/(C−N)). sign α=sign cross(BK,BL)<0,
  sign α′=sign cross(NC,NL)<0; |α|=∠LBK, |α′|=∠LNC equal by hypothesis, both in (0,π); two numbers
  in (−π,0) with equal absolute value are equal, so α=α′, i.e.
  **EA:=Im[(L−B)(C−N)·conj((K−B)(L−N))]=0** (ε=+1).        (4′)
- *Condition B (∠LCK=∠BMK).* β̂:=arg((K−C)/(L−C)), β̂′:=arg((K−M)/(B−M)). sign β̂=sign cross(CL,CK)>0,
  sign β̂′=sign cross(MB,MK)>0; equal absolute values in (0,π) ⟹ β̂=β̂′, i.e.
  **EB:=Im[(K−C)(B−M)·conj((L−C)(K−M))]=0** (ε=+1).        (5′)

This uses only interiority/betweenness — no numerics, no continuity.

### 4. Decoupling of (4′),(5′) into single-variable quadratics

Substituting (3): K−B=u·e^{−iθ}(A−B), so the positive factor u pulls out of EA:
  EA = u·FL,   FL := Im[(L−B)(C−N)·e^{+iθ}·conj(A−B)·conj(L−N)],       (6)
a **quadratic in v alone**; as u>0, (4′) ⟺ FL(v)=0. Symmetrically
  EB = v·FK,   FK := Im[(K−C)(B−M)·e^{−iθ}·conj(A−C)·conj(K−M)],       (7)
a **quadratic in u alone**, and (5′) ⟺ FK(u)=0. The leading coefficients are
  a_L = ½(c²+s²)·|CA|²·W,   a_K = −½(c²+s²)·|AB|²·W,   W := −[(a²+ap−aq+h²−pq)s + h(p+q)c],   (8)
with |CA|²=(a−q)²+h²>0, |AB|²=(a+p)²+h²>0.

### 5. The circumcentre identity T=0

Substituting (3) into T gives a polynomial of degree ≤2 in each of u,v with coefficients in
ℤ[a,p,q,h,c,s].

> **Lemma (ideal identity).** In ℤ[a,p,q,h,c,s,u,v] there are explicit QK, QL with
>   **a_K·a_L·T = a_L·QK·FK + QL·FL.**            (9)

*Proof.* Pseudo-divide T by FK in u: a_K·T=QK·FK+R1 with R1 linear in u (exact). Pseudo-divide R1
by FL in v: a_L·R1=QL·FL+R2 with **R2=0 exactly**. Multiplying the first by a_L and using the second
gives (9). Equivalently (reviewer's independent check): the normal form of T modulo the ideal
⟨FK,FL⟩ over the field ℚ(a,p,q,h,c,s) — obtained by reducing u²,v² via FK=FL=0 — is identically 0,
so T ∈ ⟨FK,FL⟩. No relation between c,s is needed. ∎

### 6. Conclusion

Fix any admissible configuration, with θ (so c²+s²=1) and u,v>0 from (3). By §3–§4, Conditions A,B
give FL(v)=0 and FK(u)=0; substituting into the right side of (9) makes it vanish, so
  a_K·a_L·T = 0.          (10)
On c²+s²=1, a_K·a_L=−¼·|AB|²·|CA|²·W² with |AB|²,|CA|²>0; W is a nonzero sinusoid in θ (its cosine
coefficient h(p+q)=h·|BC|>0), so W=0 only at isolated θ. Hence a_K·a_L≠0 for all but finitely many
admissible θ, and (10) forces T=0 there. For the finitely many θ with a_K·a_L=0: along each
connected admissible family the geometric points K(θ),L(θ),O(θ) vary continuously, so T(θ) is
continuous and vanishes off a finite set, hence vanishes there too. (This continuity fills only the
finite a_K·a_L=0 set; it plays no role in the orientation step — and in fact |W| is bounded away
from 0 on the admissible set, so this set is empty.) Thus **T=0 for every admissible configuration.**

By (2), O_x=(M_x+N_x)/2, so O lies on the perpendicular bisector of MN (M_y=N_y=h/2), and by (1)
  **OM = ON.**    ∎

### Verification (reviewer, round 2, independent)
- Decoupling EA=u·FL (v-only quadratic), EB=v·FK (u-only quadratic); leading coefficients (8);
  and T ≡ 0 mod ⟨FK,FL⟩ (normal-form reduction) — all exact-zero residual in sympy, re-derived from
  scratch.
- End-to-end over 11,739 admissible configurations: the four target signs are uniformly (−,−,+,+),
  the three unsigned hypotheses hold, and OM=ON to 1e-14. min|W|=0.25 over the admissible set (the
  a_K·a_L=0 case does not occur). Numerics are a cross-check; the proof above is self-contained.
