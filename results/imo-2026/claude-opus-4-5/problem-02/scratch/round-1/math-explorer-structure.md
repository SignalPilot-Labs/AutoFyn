## imo-2026-02

### Problem restatement
Triangle ABC, M = midpoint(AB), N = midpoint(AC). K inside triangle BMC, L inside triangle BNC with:
- (Cond 1) ∠KBA = ∠ACL (= φ, say)
- (Cond 2) ∠LBK = ∠LNC (= μ, say)
- (Cond 3) ∠LCK = ∠BMK (= ν, say)
O = circumcenter of AKL. Prove OM = ON.

---

### Key structural reduction

**OM = ON ⟺ O lies on the perpendicular bisector of MN.**

Since MN is the midline of ABC parallel to BC, the perpendicular bisector of MN is the unique line perpendicular to BC passing through midpoint(MN) = (2A+B+C)/4.

In vector form (A at origin): the condition is O·(C−B) = (|C|²−|B|²)/4.

Combined with the two circumcenter equations 2O·K = |K|², 2O·L = |L|², the condition reduces — via Cramer — to the algebraic identity:

  [(C−B)×L]·|AK|² − [(C−B)×K]·|AL|² = ((|AC|²−|AB|²)/2)·(AK×AL)

where × denotes the 2D cross product. This identity is what the three angle conditions must force.

**Numerically verified** for a non-isosceles triangle A=(1,2), B=(−1,0), C=(2,0) at α = 10°,15°,20°,25°,30°,35°: O_x = 0.750000 exactly (= midpoint(MN)_x) in every case. Residual < 10⁻¹².

---

### Structural observations

**1. Cross-pairing structure.**
Condition 2 pairs vertex B with N = midpoint(AC); condition 3 pairs vertex C with M = midpoint(AB). This is the "cross" pairing: each vertex is linked to the midpoint of the opposite vertex's adjacent side. This is exactly the medians BN and CM of triangle ABC.

**2. Parameterization via Law of Sines.**
Conditions 2 and 3 yield — via Law of Sines in triangles BMK and LNC — explicit formulas:
- BK = (AB/2) · sinν / sin(φ+ν)
- CL = (AC/2) · sinμ / sin(φ+μ)
where φ = ∠ABK = ∠ACL, μ = ∠LBK = ∠LNC, ν = ∠LCK = ∠BMK.

Triangles BMK and LNC have:
- ∠KBM = φ = ∠LCN (condition 1, since M on BA and N on CA)
- ∠BMK = ν = ∠LCK (condition 3)
- ∠BKM = π−φ−ν = ∠NLC (condition 2)

This near-symmetry is the key: the triangles BMK and LNC are related by the cross-pairing.

**3. One-parameter family, fixed O-x.**
The three conditions define a 1-parameter family of (K,L) pairs (parameterized by φ or equivalently by α = ∠ABK). Despite K and L moving continuously, the circumcenter O of AKL stays fixed on the vertical line x = (2A_x+B_x+C_x)/4 for ALL members of the family.

**4. Power condition reformulation.**
OM = ON ⟺ Power of M = Power of N w.r.t. circumcircle of AKL, i.e.:
   MA · MA' = NA · NA''
where A' (resp. A'') is the second intersection of line AB (resp. AC) with circumcircle(AKL). 
Numerically: MA'/NA'' = AC/AB for all test cases (verified to 6 decimal places).

**5. No simple concyclicities.** Checked extensively:
- B, K, L, N are NOT concyclic.
- C, K, L, M are NOT concyclic.  
- No spiral similarity sends K→L or B→N and K→C simultaneously.

**6. Isosceles case is obvious.** When AB = AC, M and N are symmetric about the perpendicular bisector of BC. If the conditions are satisfied, K and L are mirror images, triangle AKL is isosceles, O lies on the axis of symmetry, which IS the perpendicular bisector of MN. The general case requires work.

---

### Candidate techniques

**Primary (most promising):**

A) **Trigonometric cevian / Law of Sines cascade.** Use the parameterization BK = (c/2)sinν/sin(φ+ν), CL = (b/2)sinμ/sin(φ+μ), then derive AK and AL via Law of Sines in triangles ABK, ACL, and BKL. The target condition [(C−B)×L]|AK|² = [(C−B)×K]|AL|² + (|AC|²−|AB|²)/2 · (AK×AL) might follow from repeated use of the sine rule. The "cross" pairing in conditions 2 and 3 should produce the precise ratio AC/AB = sin(∠ABK)/sin(∠ACL)... that is already condition 1.

B) **Complex number in the natural coordinate system.** Place the perpendicular bisector of MN as the imaginary axis (origin at midpoint(MN)). In these coordinates A = a (with Re(a) ≠ 0), B = −2d−a, C = 2d−a, M = −d (real), N = d (real). The circumcenter O is purely imaginary iff f(K) = f(L) where f(P) = (4|P|² + 2Re(P·(B−C)/|B−C|·2d)) / Im(P). The conditions translate to angle equalities in this system; deriving f(K) = f(L) might be cleaner here.

C) **Directed angle chase to concyclicity.** Find a cyclic quadrilateral that forces O onto the perpendicular bisector of MN. The conditions are angle equalities at B, N, C, M — perhaps there is a circle through {B, K, some fourth point} that interacts with a circle through {C, L, same or related fourth point} to imply OM = ON via radical axis.

D) **The key algebraic identity.** Attempt to verify
   [(C−B)×L]|AK|² = [(C−B)×K]|AL|² + ((|AC|²−|AB|²)/2)(AK×AL)
directly from: K = B + t·e_K(φ), L = C + s·e_L(φ), BK = (c/2)sinν/sin(φ+ν), CL = (b/2)sinμ/sin(φ+μ), and the cross-conditions ∠LBK = μ, ∠LCK = ν. This is a computation-heavy but complete path.

---

### Cheap-kill candidates
None obvious. The three conditions genuinely interact non-trivially. No simple parity/size/symmetry argument kills the problem.

---

### Knowledge-base entries to use
- **Synthetic toolkit**: angle chasing, power of a point, spiral similarity, Ceva/Menelaus — specifically the Law of Sines form.
- **Coordinates / complex / barycentric**: complex numbers with the perpendicular bisector as the imaginary axis; or A at origin with clean circumcenter equations.
- **Trig identities & interval intersection** — the sine rule in multiple triangles.

---

### Analogous past problems (cruxes)
No geometry cruxes in the corpus (documented as "not yet extracted"). The `past_problems_database.json` has geometry solutions but no searchable crux moves for this domain.

---

### Prior progress
None (round 1, no approaches yet).

---

### Dead ends (do not retry)
- **B,K,L,N concyclic**: not true (directed angle check ∠LBK ≠ ∠LNK).
- **C,K,L,M concyclic**: not true (numerically verified).
- **Spiral similarity K(B→M) maps C→L**: not true (numerically verified).
- **Midpoint of KL on perp bisector of MN**: false (x ≈ 0.739 not 0.75).
- **BL∩CK on perp bisector**: false (x ≈ 0.697–0.732 not 0.75).
- **BK∩CL on line AO**: false (numerically non-collinear).

---

### Small-case / intuition notes (labeled conjecture)

CONJECTURES (numerical evidence only, not proved):

1. For all valid (K,L): MA'/NA'' = AC/AB where A', A'' are second intersections of lines AB, AC with circumcircle of AKL. This is equivalent to OM = ON but may be more tractable to prove by Law of Sines.

2. The conditions 2 and 3 together (given condition 1) uniquely determine t=BK and s=CL as: BK = (c/2)sinν/sin(φ+ν) and CL = (b/2)sinμ/sin(φ+μ), with μ and ν determined by the cross-conditions ∠LBK = μ and ∠LCK = ν. The constraint on (μ, ν) from these cross-conditions may factor cleanly via the sine rule in triangle BKL or CKL.

3. **The cleanest proof path** (conjecture based on structure): In triangles BMK and LNC, the angles are related by (φ, ν) and (φ, μ) respectively. The conditions 2 and 3 say ∠LBK = μ = ∠LNC and ∠LCK = ν = ∠BMK. The Law of Sines in triangles BKL and CKL (using the three conditions together) might directly yield the ratio MA'/NA'' = AC/AB — i.e., the condition OM = ON falls out of a two-step Law of Sines calculation in specific triangles.
