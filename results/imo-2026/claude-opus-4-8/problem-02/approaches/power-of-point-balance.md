## Status
partial

## Approach: Power-of-a-point balance (secants through A + trig cevians)

**Top-level target:** OM = ON, O = circumcenter of ⊙AKL.

**Round-1 build result.** The whole chain from OM=ON down to a single explicit
trigonometric identity in the angle data is now proven rigorously and with no gaps.
The one remaining step is a self-contained coupled trig identity (♦5) below, forced by
the two configuration constraints (I),(II); it is numerically exact to 1e-14 across
several triangles and all α, and is provably a polynomial consequence of (I),(II)
(a CAS cofactor certificate exists but is not human-presentable). That single identity
is the only gap.

## Approaches tried
- Power-of-a-point + inscribed-angle ratio (this round): reduced OM=ON to the closed
  trig identity (♦5)/(★★) via a clean vector computation of the second intersections
  A′,A″; all synthetic/trig lemmas proven. Remaining: prove (♦5) from (I),(II).
  Outcome: strong partial — complete reduction, one residual identity open.

## Current best

Notation. Put A at the origin. Let u = unit vector along AB, v = unit vector along AC,
so the angle ∠(u,v) = A (angle of triangle ABC at A). Then B = c·u, C = b·v with
c = AB, b = AC, and M = B/2, N = C/2. Let R be the circumradius of ABC, so
c = 2R sinC, b = 2R sinB, and BC = a = 2R sinA (Law of Sines, knowledge_base.md
"Synthetic toolkit / Law of Sines"). Write A,B,C for the triangle's angles
(A+B+C = π). Let O, ρ be the center and radius of ⊙AKL.

Set α = ∠KBA = ∠ACL, β = ∠LBK = ∠LNC, γ = ∠LCK = ∠BMK (the three given equalities).
Let φ = ∠KAB, ψ = ∠LAC, and put k = AK, l = AL.

### Step 1 — Power reduction (Power of a Point).
For any point X, pow(X,⊙AKL) = |XO|² − ρ² (knowledge_base.md "power of a point").
Hence OM² − ON² = (pow(M)+ρ²) − (pow(N)+ρ²) = pow(M) − pow(N), so

  **OM = ON ⟺ pow(M) = pow(N).**

### Step 2 — Secants through A.
A ∈ ⊙AKL. Line AB meets ⊙AKL a second time at A′; line AC meets it a second time at A″.
Parametrize line AB by signed arc length from A (unit speed): A at coordinate 0, B at c,
M at c/2; the circle meets the line at coordinates 0 (=A) and d := signed AA′. For X at
coordinate x on the line, pow(X) = (x−0)(x−d) (product of signed distances to the two
intersection points, arc-length parametrization — Power of a Point). Thus
pow(M) = (c/2)(c/2 − d) = c²/4 − (c/2)d. Likewise on line AC with e := signed AA″,
pow(N) = b²/4 − (b/2)e. Therefore

  pow(M) = pow(N) ⟺ c² − 2cd = b² − 2be ⟺ **cd − be = (c² − b²)/2.**   ...(T)

(If line AB is tangent at A then A′=A, d=0 and the identity pow(M)=c²/4 still holds;
the algebra of (T) is uniform in the sign and value of d, so there is no case split.)

### Step 3 — The chord formula for d, e.
The second intersection of the circle (center O) with the line through A in unit
direction w is A + 2(w·(O−A))w: the midpoint of the chord AA′ is the foot of the
perpendicular from O to the line, i.e. A + (w·(O−A))w, and A′ is its reflection of A.
With A = 0 and w = u: A′ = 2(u·O)u, so d = 2u·O; with w = v: e = 2v·O. Hence
  cd − be = 2c(u·O) − 2b(v·O) = 2O·(cu − bv) = 2O·(B − C).   ...(3)

### Step 4 — Compute 2O·(B−C) from the circumcenter relations (no need to solve for O).
Because O is the circumcenter of A(=0),K,L: |O| = |O−K| = |O−L| gives
  O·K = |K|²/2 = k²/2,  O·L = |L|²/2 = l²/2.   ...(4)
Write B − C = μK + νL (K,L are linearly independent as long as A,K,L are not collinear,
which holds since ⊙AKL is a genuine circle). By Cramer/2D determinants, with
det(P,Q)=P_xQ_y−P_yQ_x,
  μ = det(B−C, L)/det(K,L),  ν = det(K, B−C)/det(K,L).
Using the frame u=(1,0), v=(cosA,sinA), and K = k(cosφ,sinφ),
L = l(cos(A−ψ),sin(A−ψ)) (K makes angle φ with u; L makes angle ψ with v, i.e. angle
A−ψ with u; this uses φ=∠KAB, ψ=∠LAC), one computes:
  det(K,L) = kl·sin((A−ψ)−φ) = kl·sin(A−φ−ψ),
  det(B−C,L) = c·det(u,L) − b·det(v,L) = c·l sin(A−ψ) − b·(−l sinψ) = l·[c sin(A−ψ)+b sinψ],
  det(K,B−C) = c·det(K,u) − b·det(K,v) = −k[c sinφ + b sin(A−φ)].
Now the two bracketed sums simplify by a product-to-sum identity (Lemma S below):
  c sin(A−ψ)+b sinψ = 2R sinA sin(C+ψ),   c sinφ + b sin(A−φ) = 2R sinA sin(B+φ).
Therefore
  μ = 2R sinA sin(C+ψ)/(k·sin(A−φ−ψ)),   ν = −2R sinA sin(B+φ)/(l·sin(A−φ−ψ)),
and by (3),(4):
  cd − be = 2O·(B−C) = 2(μ·O·K + ν·O·L) = μk² + νl²
         = (2R sinA / sin(A−φ−ψ))·[ k sin(C+ψ) − l sin(B+φ) ].   ...(5)

### Step 5 — Reduction to (★★).
Combining (T) with (5) and (c²−b²)/2 = 2R²(sin²C−sin²B) = 2R² sinA sin(C−B):

  **OM = ON  ⟺  k sin(C+ψ) − l sin(B+φ) = R sin(C−B) sin(A−φ−ψ).**   ...(★★)

This is exact and fully rigorous. (★★) is verified to 1e-14 on the solved
configurations (results/imo-2026-02/scratch_pop.py).

### Lemma S (product-to-sum).  With A = π−B−C, c=2R sinC, b=2R sinB, for any θ:
  c sin(A−θ) + b sinθ = 2R sinA sin(C+θ).
Proof. c sin(A−θ)+b sinθ = 2R[sinC sin(A−θ)+sinB sinθ]. Product-to-sum:
sinC sin(A−θ)=½[cos(C−A+θ)−cos(C+A−θ)], sinB sinθ=½[cos(B−θ)−cos(B+θ)]. Since
C+A−θ = π−B−θ, cos(C+A−θ) = −cos(B+θ), so the −cos(C+A−θ) and −cos(B+θ) terms cancel,
leaving ½[cos(C−A+θ)+cos(B−θ)] = cos((B+C−A)/2)·cos((C−A−B)/2+θ)
= cos(π/2−A)·cos(C−π/2+θ) = sinA·sin(C+θ). ∎  (The second identity of Step 4 is Lemma S
with B↔C, θ→φ.)

### The trig-cevian data (deriving k, l, φ, ψ and the constraints (I),(II)).
- Triangle BMK: M on segment AB so ray BM = ray BA, ∠MBK = ∠KBA = α, ∠BMK = γ,
  BM = c/2, hence ∠BKM = π−α−γ and (Law of Sines) BK = (c/2)·sinγ/sin(α+γ).   ...(a)
- K seen from C: ∠ACL = α, ∠LCK = γ ⟹ ∠ACK = α+γ ⟹ ∠KCB = C−α−γ; and ∠KBC = B−α.
  Triangle BKC: ∠BKC = A+2α+γ, and (Law of Sines, BC=a) BK = a·sin(C−α−γ)/sin(A+2α+γ). ...(b)
  Equating (a),(b) with a=2R sinA, c=2R sinC gives
  **(I): sinC·sinγ·sin(A+2α+γ) = 2 sinA·sin(C−α−γ)·sin(α+γ).**
- Triangle ABK: ∠ABK=α, ∠BAK=φ, so AK = c·sinα/sin(α+φ) = k and BK = c·sinφ/sin(α+φ). ...(c)(d)
  From (a),(d): 2 sinφ sin(α+γ)=sinγ sin(α+φ); expanding sin(α+φ) and dividing by sinφ
  yields **cotφ = cotα + 2cotγ.**
- Symmetrically (the configuration is invariant under B↔C, M↔N, K↔L, which swaps
  conditions 2 and 3, hence β↔γ, b↔c, φ↔ψ): l = AL = b·sinα/sin(α+ψ),
  **cotψ = cotα + 2cotβ**, and
  **(II): sinB·sinβ·sin(A+2α+β) = 2 sinA·sin(B−α−β)·sin(α+β).**
  (Derivations: triangle CNL gives CL=(b/2)sinβ/sin(α+β); triangle BLC gives
  CL=a sin(B−α−β)/sin(A+2α+β); equate → (II). Triangle ACL gives AL=b sinα/sin(α+ψ).)
- Configuration/orientation: K and L lie inside ∠A with rays AB, AK, AL, AC in this
  angular order, so ∠KAL = A − φ − ψ =: λ_A > 0 (confirmed numerically).

### Reduction of (★★) to a polynomial identity (♦5).
Substitute k = c sinα/sin(α+φ) = 2R sinC sinα/sin(α+φ), l = 2R sinB sinα/sin(α+ψ)
into (★★), clear denominators by sin(α+φ)sin(α+ψ), and divide by 2R. Using
sin(α+φ)=2 sinα·sin(α+γ)/N_C and sin(α+ψ)=2 sinα·sin(α+β)/N_B, where (from
cotφ=cotα+2cotγ) sinφ=sinα sinγ/N_C, cosφ=(cosα sinγ+2 sinα cosγ)/N_C with
N_C²=sin²γ+4 sinα cosγ·sin(α+γ) (and symmetrically N_B²=sin²β+4 sinα cosβ·sin(α+β)),
(★★) becomes the polynomial identity (verified to 1e-14, scratch_id.py):

  **(♦5):  sinC·P_C·sin(α+β)·N_C² − sinB·P_B·sin(α+γ)·N_B² = sin(C−B)·W·sin(α+γ)·sin(α+β),**

where P_C = sinC(cosα sinβ+2 sinα cosβ)+cosC·sinα sinβ,
P_B = sinB(cosα sinγ+2 sinα cosγ)+cosB·sinα sinγ,
W = sinA[(cosα sinγ+2 sinα cosγ)(cosα sinβ+2 sinα cosβ) − sin²α sinγ sinβ]
  − cosA[sinα sinγ(cosα sinβ+2 sinα cosβ)+(cosα sinγ+2 sinα cosγ)sinα sinβ],
and A is eliminated by sinA=sin(B+C), cosA=−cos(B+C).

### THE GAP.
Prove **(♦5)** — equivalently (★★) — using the two constraints (I),(II). Facts established:
(♦5) holds to machine precision (1e-14) on the actual solution variety for the tested
scalene triangles and all α, and it is a polynomial consequence of {(I),(II)} together
with the Pythagorean relations (a multivariate-division cofactor certificate exists in
ℚ[sinα,cosα,…], but it is far too large to serve as a human proof). What is missing is a
clean derivation of (♦5) from (I),(II). The identity genuinely couples the two sides
(the term P_C·N_C² mixes the β-data of the B-side with the γ-data of the C-side, and W
mixes both), which is why a term-by-term decoupling does not close it. A promising route:
extract the sin²γ-leading part of (♦5)−[f·(I)] to pin the cofactor f as a function of the
B-side data only, then the residue against (II); this was attempted but the naive
sin(γ)-degree split did not immediately produce the correct f (the Pythagorean reduction
entangles the leading coefficients), so the correct cofactor split remains to be found.

Everything above (Steps 1–5, Lemmas, all trig-cevian derivations, constraints (I),(II))
is complete and rigorous; only (♦5) is unproved.

## Full proof
(Not present — Status is partial. The reduction OM = ON ⟺ (♦5) is complete; the identity
(♦5)⇐(I),(II) is the open step.)

## Promotable lemmas
- **Lemma S (product-to-sum):** For a triangle with angles A=π−B−C, circumradius R,
  sides c=2R sinC, b=2R sinB, and any angle θ: c sin(A−θ)+b sinθ = 2R sinA sin(C+θ)
  (and c sinθ+b sin(A−θ) = 2R sinA sin(B+θ)). Proved in full above (Lemma S).
- **Power-secant reduction (T):** With M,N midpoints of AB,AC and A on a circle Ω of
  center O radius ρ, if line AB meets Ω again at A′ (signed AA′=d) and line AC again at
  A″ (signed AA″=e), then OM=ON ⟺ cd−be=(c²−b²)/2, and moreover cd−be = 2O·(B−C).
  Proved in full above (Steps 1–3).
- **Second-intersection balance (★★):** For O = circumcenter of AKL (A at origin),
  cd−be = (2R sinA/sin(A−φ−ψ))·[k sin(C+ψ) − l sin(B+φ)]; hence OM=ON ⟺ (★★).
  Proved in full above (Step 4–5).
