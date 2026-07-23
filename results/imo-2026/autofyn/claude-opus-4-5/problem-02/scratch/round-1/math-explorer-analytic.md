## imo-2026-02 — Analytic/Coordinate Lens Report

### Setup and Verified Angle Encoding

**Coordinate system:** B = 0, C = 1, A = a (complex, Im(a) > 0). Then M = a/2, N = (1+a)/2. The target is OM = ON ⟺ Re(circumcenter of AKL) = (2Re(a)+1)/4 (since M and N share the same imaginary part, so OM = ON iff O lies on the vertical line x = midpoint of M and N in the real direction).

**The three angle conditions — CORRECT algebraic encoding (verified numerically):**

- **C1 (∠KBA = ∠ACL):** `a*(a-1) / (K*(L-1)) ∈ ℝ₊`
  — Encodes: signed angle from BK to BA equals signed angle from CA to CL. In polynomial form: Im(a*(a-1) · conj(K*(L-1))) = 0 with positive ratio.

- **C2 (∠LBK = ∠LNC):** `K*(L-N) / (L*(C-N)) ∈ ℝ₊`
  — Encodes: signed angle from BL to BK equals signed angle from NL to NC. With N=(1+a)/2, C-N=(1-a)/2. In polynomial form: Im(K*(L-N) · conj(L*(C-N))) = 0 with positive ratio. (Degree 3 in K, L coordinates.)

- **C3 (∠LCK = ∠BMK):** `(K-1)*(-a/2) / ((L-1)*(K-a/2)) ∈ ℝ₊`
  — Encodes: signed angle from CL to CK equals signed angle from MB to MK. In polynomial form: Im((K-1)*(-a/2) · conj((L-1)*(K-a/2))) = 0 with positive ratio. (Degree 3.)

**Critical sign convention:** The angles are SIGNED (directed), consistent with the positional ordering: K lies in the angular sector at B between BL and BA (so arg(L) < arg(K) < arg(A) from B), and L lies in the sector at C between CA and CK (so arg(A-C) < arg(L-C) < arg(K-C) from C). Using unsigned angles gives a DIFFERENT system that does NOT satisfy OM = ON.

**Numerical verification:** Tested 4 distinct non-equilateral triangles. In each case, all valid (K, L) pairs satisfying C1, C2, C3 with correct positional constraints yield OM = ON to machine precision (diff < 1e-10). Re(circumcenter) matches (2Re(a)+1)/4 exactly.

---

### Structure of the Solution Space

**Key derived constraint:** Combining C1 and C2 eliminates K and imposes a condition on L alone:
```
a*(a-1)*(L-N) / ((L-1)*L*(C-N)) ∈ ℝ₊
```
Simplifying (with N=(1+a)/2, C-N=(1-a)/2):
```
-a*(2L-1-a) / ((L-1)*L) ∈ ℝ₊
```
This is a **cubic curve** for L: `Im(a*(2L-1-a) · conj(L*(L-1))) = 0` (one polynomial equation in Re(L), Im(L), degree 3).

**Parameterization:** For each L on this cubic curve, K = t₁ · a*(a-1)/(L-1) for some t₁ > 0 determined by C3. The solution set is a 1D curve parameterized by L ∈ cubic curve.

**Equivalent reformulation:** The target Re(O) = (2Re(a)+1)/4 is equivalent to:
```
F(A)*(ky-ly) + F(K)*(ly-ay) + F(L)*(ay-ky) = 0
```
where F(P) = |P|² - Re(P)*(2Re(a)+1)/2 (a "shifted power" function).

---

### Complexity Estimate for Pure Coordinate Bash

- **Degrees:** C1 is degree 2; C2, C3 are degree 3 in (Re K, Im K, Re L, Im L).
- **The target identity** is degree ~4–5 overall.
- **Direct Gröbner basis:** in 4 variables over ℝ (with symbolic a), this is computationally feasible with a CAS (sympy/Mathematica) but extremely messy by hand.
- **After reduction** (using C1 to express K as a ray from 0 parameterized by L, then C2 restricts L to the cubic curve, C3 fixes the scaling t₁): the circumcenter x-coordinate reduces to a rational function of L and t₁, and one must verify this equals (2Re(a)+1)/4 using the cubic condition. This is degree 3–4 and plausible but painful.
- **Verdict:** A pure coordinate bash is POSSIBLE but requires a CAS for the algebraic computation or very clever simplifications. NOT suitable for a clean written proof.

---

### Key Algebraic Simplifications

1. **C1 is "isogonal":** a*(a-1)/(K*(L-1)) = t₁ gives K = a*(a-1)/(t₁*(L-1)). This means K is on the ray from B in direction a*(a-1)/(L-1).

2. **C2 combined with C1** forces L onto a cubic curve (the formula above). This cubic factors or simplifies in special cases.

3. **The circumcenter x-coordinate** (with K expressed in terms of L and t₁) reduces, after C3 substitution, to a function of L that should be identically (2Re(a)+1)/4 on the cubic curve.

4. **In the equilateral case** (Re(a) = 1/2): the cubic curve for L is symmetric about Re = 1/2, and K and L are reflections of each other about the line Re = 1/2. This gives immediate proof by symmetry for the equilateral case.

5. **The condition Im(a*(2L-1-a) · conj(L*(L-1))) = 0** can be interpreted as: the cross-ratio [a, (1+a)/2; L, L-1] is real, i.e., these four points are concyclic (or collinear).

---

### Distinct Openings for the Outliner

1. **Direct complex-number bash:** Use C1 to write K = a*(a-1)/(t₁*(L-1)), substitute into C2 to get the cubic condition on L, use C3 to determine t₁, then compute Re(O) and verify algebraically. This requires CAS but is mechanical.

2. **Spiral similarity approach:** C2 says arg(K/L) = arg((C-N)/(L-N)), which means the spiral similarity at B taking the ray BL to BK has the same argument as the spiral similarity at N taking the ray NL to NC. This is a condition about how B and N "see" the ratio K/L vs C/L. Could lead to a Miquel-point or pencil-of-circles argument.

3. **Power of a point:** The condition OM = ON means M and N have equal power with respect to the circumcircle of AKL. This can be expressed using the radical axis / power formula, and might reduce to one of the angle conditions.

4. **Trigonometric ceva / sin-rule argument:** Use the sine rule in all the relevant triangles to convert angle conditions into ratio conditions, then show the circumcenter lands at the correct position.

5. **Reflection principle:** The perpendicular bisector of MN is a specific line. Show directly that the circumcircle of AKL is symmetric under reflection across this line (i.e., the circle maps to itself), which forces the center to lie on the line. This would require showing that if K is on the circle, then its reflection K' is also on the circle — but the reflection K' may not be L in general.

---

### Candidate Techniques (from knowledge_base.md)

- **Coordinates/complex/barycentric** (Geometry section): confirmed as applicable
- **Spiral similarity** (Synthetic toolkit): C2 and C3 have spiral similarity interpretations
- **Power of a point** (Geometry): OM = ON ↔ equal powers with respect to circumcircle of AKL
- **Trig cevians / Ceva's theorem** (Geometry): angle conditions could be expressed via sin-rules

---

### Analogous Past Problems (from crux corpus)

The crux corpus does not include geometry problems (only number theory, combinatorics, algebra). No analogous problems found.

---

### Prior Progress

None (round 1, no approaches yet).

---

### Dead Ends (do not retry)

- **Unsigned angle encoding:** Using |arg(K/A)| = |arg((L-1)/(A-1))| (unsigned) leads to a DIFFERENT condition that does NOT satisfy OM = ON. The signed version is essential.
- **Incorrect sign branch:** The first attempt found solutions on the "wrong branch" of the angle conditions (K outside BMC, L outside BNC). The correct branch requires all three ratios to be positive real.

---

### Small-Case / Intuition Notes (conjecture)

- In the equilateral triangle, the valid (K, L) pairs are exactly those where K and L are reflections of each other about the axis of symmetry x = 1/2. This forces the circumcenter of AKL onto that axis. (Verified numerically, obvious by symmetry.)
- For general triangles, K and L are NOT reflections of each other about x = (2Re(a)+1)/4, yet the circumcenter still falls there. This suggests a non-trivial algebraic identity rather than a simple symmetry argument.
- The cubic curve for L (Im(a*(2L-1-a)*conj(L*(L-1))) = 0) appears to be the key constraint. Understanding the geometry of this curve might be key to a synthetic proof.
- The sign conditions (all three ratios positive) combined with the positional constraints (K inside BMC, L inside BNC, K inside angle LBA, L inside angle ACK) appear to select a specific connected component of the cubic curve. Along this component, OM = ON is verified to hold.

