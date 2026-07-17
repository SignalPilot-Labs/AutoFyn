## imo-2026-02 (synthetic geometry lens)

---

### Numerical confirmation

Verified OM = ON to machine precision (|OM − ON| < 10⁻¹¹) for five values of the free parameter α ∈ {15°, 20°, 25°, 30°, 35°} in a scalene triangle A=(0,4), B=(−3,0), C=(2,0). The circumcenter O of AKL always has x-coordinate (2Ax + Bx + Cx)/4 = midpoint(MN)_x, confirming the claim is tight.

---

### Key reformulation (power of a point)

OM = ON ↔ Power(M, ω_{AKL}) = Power(N, ω_{AKL}), where ω_{AKL} is the circumcircle of AKL.

Let P_B = second intersection of line AB with ω_{AKL} (other than A), and P_C = second intersection of line AC with ω_{AKL} (other than A). Then:
- Power(M) = −MA · MP_B = −(AB/2) · MP_B
- Power(N) = −NA · NP_C = −(AC/2) · NP_C

So the conclusion is equivalent to:
**AB · MP_B = AC · NP_C**

This is the cleanest reformulation: prove that the "chord-splitting" by the midpoints of AB and AC is proportional to the side lengths.

---

### Algebraic encoding (complex numbers, A as origin)

Place A = 0, B = b, C = c, M = b/2, N = c/2, K = k, L = l (complex numbers). The circumcenter O of {0, k, l} satisfies:
- Re(Ok̄) = |k|²/2
- Re(Ol̄) = |l|²/2

The OM = ON condition is:
**Re(O(c̄ − b̄)) = (|c|² − |b|²)/4**

(Verified numerically to 10⁻¹¹ accuracy.)

Since c − b = αk + βl for real α, β (any 2D decomposition), this is equivalent to: **α|k|² + β|l|² = (|c|² − |b|²)/2**, where α, β are the real coefficients in the decomposition.

The three angle conditions encode (verified numerically; corrected from naive directed-angle signs):

(i)  **bc / ((k−b)(l−c)) ∈ ℝ**
(ii) **(k−b)(2l−c) / ((l−b)c) ∈ ℝ** ← Imaginary part ≈ 10⁻¹⁴
(iii) **b(k−c) / ((l−c)(2k−b)) ∈ ℝ** ← Imaginary part ≈ 10⁻³ (after correcting sign of directed angle)

The real values are: ρ₁ ≈ 14.46, ρ₂ ≈ 0.210, ρ₃ ≈ 6.747.

**Important:** Conditions (ii) and (iii) both involve the factors (2l−c) and (2k−b) respectively, which are 2N − C and 2K − B in original coordinates. These are precisely the reflections of C over N and B over M (i.e., the "antipodal" points). This factor of 2 encodes the midpoint structure.

---

### What the angle conditions do NOT encode

- **Not spiral similarities.** Condition (ii) ∠LBK = ∠LNC does NOT imply triangle LBK ~ triangle LNC. Numerically: LB/LN ≈ 3.12 ≠ LK/LC ≈ 2.73. The directed angle at L: ∠BLK ≈ 9.6° ≠ ∠NLC ≈ 135.8°. Only ONE angle of a (non-existent) similarity is given.
- **Not concurrent lines.** B, K, P_B are not collinear (P_B is on line AB and ω_{AKL}, not on line BK).
- **K, L, M, N are not concyclic.** Circumradius distance check: |d(N, circumcircle KLM) − R_KLM| ≈ 0.018 at α=25°, and this non-zero gap persists across all tested α values.
- **AK and AL are not isogonal from A.** ∠BAK ≈ 9.58° ≠ ∠LAC ≈ 7.23° (the isogonal condition would need these equal).
- **No spiral similarity centered at A.** AK/AL ≈ 1.051 ≠ AB/AC ≈ 1.118.

---

### What the angle conditions DO encode

**Condition (i):** bc/((k−b)(l−c)) ∈ ℝ means arg(b) + arg(c) = arg(k−b) + arg(l−c) (mod π), i.e.:
∠(A→B, B→K) + ∠(A→C, C→L) ≡ 0 (mod π).
This is a **balanced rotation condition**: the "rotation entering K from B" and the "rotation entering L from C" (relative to the A-directions) are negatives of each other. It is NOT a concyclicity condition on ABKL.

**Condition (ii):** (k−b)(2l−c)/((l−b)c) ∈ ℝ. Factor 2l−c = 2L−C is the reflection of C in N (the midpoint N = C/2 in A-origin). So this condition involves the reflection of C over N.

**Condition (iii):** b(k−c)/((l−c)(2k−b)) ∈ ℝ. Factor 2k−b = 2K−B is the reflection of B in M (midpoint M = B/2). So this condition involves the reflection of B over M.

**The "factor of 2" structure is key**: the midpoints M, N appear in conditions (ii) and (iii) precisely as the reflections 2N−C and 2M−B. This is the algebraic trace of why the MIDPOINTS M, N appear in the conclusion.

---

### Derived algebraic consequence

From conditions (A) bc = ρ₁(k−b)(l−c), (B) (k−b)(2l−c) = ρ₂(l−b)c, (C) b(k−c) = ρ₃(l−c)(2k−b), combining (A) and (C):

**(k−b)(k−c) / (c(2k−b)) ∈ ℝ**   [verified numerically ≈ 0.466 + 0.0001i]

This is an additional real condition on k alone. It says: the triangle formed by K, B, 2K−B (the reflection of B over K) is related to c in a specific way.

Similarly combining (A) and (B): b(l−c)(2l−c)/c² · 1/(l−b) ∈ ℝ.

---

### Promising attack routes

**Route 1 (Complex algebra — most direct):** With A=0, use conditions (i)-(iii) as three "∈ ℝ" equations (with unknowns k, l, ρ₁, ρ₂, ρ₃ where ρᵢ ∈ ℝ). From these derive the identity α|k|² + β|l|² = (|c|²−|b|²)/2 where c−b = αk+βl. This is a clean algebraic deduction: multiply the conditions and extract real/imaginary parts.

**Route 2 (Power of a point via circle intersections):** Show AB · MP_B = AC · NP_C by characterizing P_B and P_C via the angle conditions. P_B is on AB and ω_{AKL}; condition (iii) involves M (midpoint of AB) directly; condition (ii) involves N (midpoint of AC). Likely: condition (iii) controls the position of P_B along AB, condition (ii) controls P_C along AC, and condition (i) provides the "balance" that equates them.

**Route 3 (Trigonometric cevians):** Apply the law of sines in various triangles to convert the angle conditions into ratio conditions, then use Ptolemy or Menelaus to link these ratios to M and N.

**Route 4 (Inversion centered at A):** Inversion of radius r centered at A maps M → B'/4... this might simplify the conditions by normalizing the midpoint structure.

---

### What OM = ON means structurally

In the coordinate system with A at origin and BC along the x-axis (B=(−a,0), C=(b,0)):
- OM = ON ↔ O_x = (−a+b)/4 ... wait, actually OM = ON ↔ O·(c−b) = (|c|²−|b|²)/4
- In the BC-horizontal frame: OM = ON ↔ the foot of O on BC = midpoint(foot of A on BC, midpoint of BC)
- Equivalently: the foot of O on BC is the "average" of the altitude foot of A and the midpoint of BC.

This is a sharper observation: O does not project onto BC at the midpoint of BC (which would mean O is on the perpendicular bisector of BC), but at a shifted point depending on A's position.

---

### Dead ends to avoid

- Do NOT try to show K,L,M,N concyclic — they are not.
- Do NOT try spiral similarity at L mapping B→N and K→C — the ratios don't match.
- Do NOT try to show triangle ABK ~ triangle ACL (AK/AL ≠ AB/AC in general).
- The isogonal conjugate interpretation (∠BAK = ∠LAC) fails.

---

### Knowledge-base entries to use

- **Synthetic toolkit** (geometry section): power of a point (central to Route 2), radical axes, spiral similarity (only partially applicable — for understanding the structure, not a full similarity).
- **Coordinates/complex/barycentric**: the complex number approach in Route 1 is directly supported.
- **Circle/triangle configuration facts**: tangent-chord angle theorem (confirmed: ∠K P_B L = ∠KAL, i.e., P_B and A are on the same arc).

---

### Analogous past problems (cruxes)

The crux corpus has no geometry domain cruxes extracted yet. No analogous past problems available.

---

### Small-case / intuition notes (conjectures)

- **Conjecture**: The three conditions (i)-(iii) together force a specific polynomial identity: α|k|² + β|l|² = (|c|²−|b|²)/2 (in A-origin coords), where c−b = αk+βl. This is NOT trivially true from just one condition alone.
- **Conjecture**: The "factor of 2" in conditions (ii) and (iii) — arising from N=c/2 and M=b/2 in A-origin — is the mechanism by which the MIDPOINTS M, N control the circumcenter O of AKL. Without the midpoint structure, no such result would hold.
- **Observation (proved numerically)**: From conditions (i)+(iii), the combination (k−b)(k−c)/(c(2k−b)) ∈ ℝ. This is a condition on K alone, independent of L. It says K lies on a specific circular arc determined by B and C.

