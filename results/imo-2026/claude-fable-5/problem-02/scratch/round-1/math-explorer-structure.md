## imo-2026-02

### Problem recap
Triangle ABC, M = midpoint AB, N = midpoint AC. K inside triangle BMC, L inside triangle BNC, with K inside angle LBA, L inside angle ACK, and:
- Cond 1: ∠KBA = ∠ACL = α  
- Cond 2: ∠LBK = ∠LNC = β  
- Cond 3: ∠LCK = ∠BMK = γ  

O = circumcenter of AKL. Prove OM = ON.

---

### Distinct openings

**Opening A — Power-of-a-point via sine rule (most promising).**  
The condition OM = ON is equivalent to pow(M, ω) = pow(N, ω) where ω = circumcircle(AKL).  
From condition 3 (∠BMK = γ, ∠MBK = α in triangle BMK with MB = AB/2):  
  BK = (AB/2)·sinγ/sin(α+γ),  MK = (AB/2)·sinα/sin(α+γ).  
From condition 2 (∠LNC = β, ∠NCL = α in triangle LNC with NC = AC/2):  
  LC = (AC/2)·sinβ/sin(α+β),  NL = (AC/2)·sinα/sin(α+β).  
These are confirmed numerically. Using chord MK: |pow(M)| = MK · MK*, and chord NL: |pow(N)| = NL · NL*. Condition 2 (∠LBK = β) supplies the linking equation between K and L needed to show MK·MK* = NL·NL*. This route stays entirely in angle/metric space and avoids complex coordinates.

**Opening B — Directed angle conditions as a triple "reality" system.**  
In complex numbers, the three conditions encode exactly:  
  (K−B)(L−C)/((A−B)(A−C)) is real … (Cond 1)  
  (L−B)(C−N)/((K−B)(L−N)) is real … (Cond 2)  
  (L−C)(K−M)/((K−C)(B−M)) is real … (Cond 3)  
(All confirmed numerically with imaginary part < 1e-10.)  
Each condition says a specific directed-angle pair is equal. The circumcenter O satisfies Re[O·conj(A−K)] = (|A|²−|K|²)/2 and Re[O·conj(A−L)] = (|A|²−|L|²)/2. OM = ON iff Re[O·conj(C−B)] = (2A+B+C)/4·Re(conj(C−B)/|C−B|), i.e., Re[O·conj(C−B)] is a fixed constant. This follows iff the three reality conditions force the circumcenter's BC-component to be (2Ax+Bx+Cx)/4. The algebraic route: multiply and chain the three real-ratio conditions to extract this identity.

**Opening C — Circumcircles of ABK and ACL share angle α.**  
By the sine rule in the circumcircle of ABK (where ∠ABK = α): AK = 2R₁ sinα.  
By the sine rule in the circumcircle of ACL (where ∠ACL = α): AL = 2R₂ sinα.  
So AK/AL = R₁/R₂. The circumcircles of ABK and ACL both see their respective chords AK, AL at angle α. This "isogonal" condition (Cond 1 encodes arg((K−B)/(A−B)) = −arg((L−C)/(A−C))) links the two sub-configurations. The circumcenter O of AKL can be expressed in terms of the centers of these two circumcircles; showing it lies on the perp bisector of MN may reduce to a simpler metric identity involving R₁, R₂, and the triangle sides.

**Opening D — Work backwards from the perp-bisector condition.**  
OM = ON iff O ∈ perp bisector of MN. The perp bisector of MN:  
- passes through mid(MN) = (2A+B+C)/4 (midpoint of the median from A);  
- is perpendicular to BC (since MN ∥ BC);  
- passes through the nine-point center N₉ of ABC (since M,N both lie on the nine-point circle).  
Goal: show the circumcircle of AKL has its center on this line. The algebraic form: the coefficient of BC-direction in O equals Ax/2 + (Bx+Cx)/4. From perp bisectors of AK and AL: if e₁ (BC direction) = λ(A−K)+μ(A−L) with real λ,μ, then O·e₁ = λ(|A|²−|K|²)/2 + μ(|A|²−|L|²)/2 must equal (2Ax+Bx+Cx)/4. Numerically confirmed. The goal is thus to prove this linear-algebraic identity using the angle conditions.

**Opening E — Reduction to an isogonal / spiral similarity argument.**  
Condition 3 in directed angles: ∠(CK, CL) at C = ∠(KM, KB) at K. This is NOT the standard inscribed angle theorem for concyclicity of C, K, L, M (since those four are not concyclic). However, it says: the spiral similarity at K that maps the direction KB to KM also maps the angle CL to... something. Conditions 2 and 3 both give such "angle-transport" equalities via midpoints. A combined spiral similarity argument using all three conditions and fixing A might directly give a circle through A,K,L with center on the perp bisector of MN.

---

### Candidate techniques
- **Sine rule in sub-triangles** (BMK and LNC), to get exact metric relations for MK and NL.
- **Power of a point** (pow(M) = pow(N) as the target).
- **Directed angle algebra** in complex numbers (all three conditions are exact "imaginary part = 0" statements).
- **Angle chasing** using the directed-angle formulation.

---

### Cheap-kill candidates
- None via parity or mod arithmetic (continuous geometry problem).
- **Size/Pigeonhole:** Not applicable.
- **Structural pruning:** Check if OM = ON reduces immediately to a known classical theorem about midpoints and circumcenters — specifically the nine-point circle (M,N ∈ nine-point circle of ABC) may give a shortcut if O is shown to be related to the nine-point center. But numerically O is NOT the nine-point center (N₉ = (0.25, 0.917) in our coords, while O varies from (0.25, 1.47) to (0.25, 1.90)). So no cheap kill here.

---

### Knowledge-base entries to use
- **Synthetic toolkit**: angle chasing, power of a point, similar triangles. (KB: Geometry section)
- **Circle/triangle configuration facts**: Sine rule, inscribed angle theorem. (KB: Geometry section)
- **Trig cevians (Ceva/Menelaus)**: sine rule in sub-triangles BMK, LNC, BLK. (KB: Geometry section)
- **Coordinates / complex / barycentric**: the directed angle approach (all conditions = "imaginary part of a complex ratio = 0"). (KB: Geometry section)

---

### Analogous past problems (cruxes)
The crux corpus contains no geometry cruxes (confirmed in crux_moves_documentation.md). No analogues available.

---

### Prior progress
None — this is round 1, workspace is empty.

---

### Dead ends (do not retry)
- **M, K, N, L concyclic**: false. Cross-ratio imaginary part ≈ 0.007–0.008 across all tested α values. Not concyclic.
- **B,K,N,L concyclic**: false.
- **B,L,N,C concyclic**: false (ratio ≈ 0.67–0.92 off).
- **Spiral similarity centered at L mapping B→N, K→C**: does not exist (the two ratios (N−L)/(B−L) and (C−L)/(K−L) are unequal as complex numbers).
- **O = nine-point center of ABC**: false. O varies with α and is always at a different position than N₉.
- **KL ∥ BC**: false. The direction of KL is not horizontal (cross product KL × BC ≈ 0.126 ≠ 0).

---

### Small-case / intuition notes (all conjectures from numerics)

**Conjecture 1 (strongly supported):** OM = ON holds for all valid (K,L) pairs in the 1-parameter family, confirmed at α = 5°, 10°, 15°, 20°, 25°, 30°, 35°, 40° with residual < 1e-10.

**Conjecture 2 (strongly supported):** The three conditions are EXACTLY equivalent in directed angles to:
  - Cond 1: Im[(K−B)(L−C)/((A−B)(A−C))] = 0
  - Cond 2: Im[(L−B)(C−N)/((K−B)(L−N))] = 0
  - Cond 3: Im[(L−C)(K−M)/((K−C)(B−M))] = 0

**Conjecture 3 (strongly supported):** Conditions 2 and 3 together with the sine rule give exact metric relations:
  - MK = (AB/2)·sinα/sin(α+γ)   [from cond 3: triangle BMK with ∠MBK = α, ∠BMK = γ]
  - BK = (AB/2)·sinγ/sin(α+γ)
  - NL = (AC/2)·sinα/sin(α+β)   [from cond 2: triangle LNC with ∠NCL = α, ∠LNC = β]
  - LC = (AC/2)·sinβ/sin(α+β)

**Conjecture 4:** In circumcircle of ABK: AK = 2R₁ sinα (sine rule with inscribed angle α at B). In circumcircle of ACL: AL = 2R₂ sinα. Confirmed: AK/(2R₁) = sin(α) = AL/(2R₂) numerically.

**Key algebraic identity (confirmed, not proved):** Let e₁ = (C−B)/|C−B| (unit vector in BC direction), and write e₁ = λ(A−K) + μ(A−L) with real λ,μ. Then:
  λ(|A|²−|K|²)/2 + μ(|A|²−|L|²)/2 = (2Ax+Bx+Cx)/4
is equivalent to OM = ON and holds for all valid (K,L) pairs. This is the algebraic core to prove.

**Structural note:** ∠KAB + ∠KAL + ∠LAC = ∠BAC exactly (verified numerically). Rays AK and AL partition angle BAC with K closer to AB and L closer to AC, as expected.

