## imo-2026-02

### Lens: Analogy / Known Configurations

---

- **Distinct openings:**

  **Opening A — Power-of-a-Point Reduction (cleanest known path).**
  OM = ON iff O lies on the perpendicular bisector of MN. Since MN is parallel to BC (midline), the perpendicular bisector of MN is perpendicular to BC. The midpoint of MN is (2A+B+C)/4. The condition OM = ON translates cleanly via two elementary steps:
  (i) Midpoint-power identity: If A lies on circle ⊙AKL with center O, radius R, and M = midpoint(AB), then pow(M, ⊙AKL) = (pow(B, ⊙AKL) − AB²/2) / 2. Likewise pow(N, ⊙AKL) = (pow(C, ⊙AKL) − AC²/2) / 2. (Verified numerically: pow(B)−pow(C) = 9.38 − 3.38 = 6.00 = (AB² − AC²)/2.) 
  (ii) So OM = ON iff pow(M) = pow(N) iff pow(B, ⊙AKL) − pow(C, ⊙AKL) = (AB² − AC²)/2.
  The outliner should try to derive pow(B) − pow(C) = (AB² − AC²)/2 directly from the three angle conditions.

  **Opening B — Complex Number Computation (algebraically complete).**
  Place A = 0 in the complex plane. Let b, c, k, l denote B, C, K, L as complex numbers (with M = b/2, N = c/2). The circumcenter of {0, k, l} is O = (k|l|² − l|k|²) / (2i Im[kl̄]). The three angle conditions translate to:
  - (C1) bc / ((k−b)(l−c)) ∈ ℝ  [∠KBA = ∠ACL; verified: ratio = 26.07+0i].
  - (C2) (k−b)(2l−c) / (c(l−b)) ∈ ℝ  [∠LBK = ∠LNC; verified: ratio = 0.218+0i].
  - (C3) b(k−c) / ((l−c)(2k−b)) ∈ ℝ  [∠LCK = ∠BMK; verified: ratio = 12.02+0i].
  The goal OM = ON becomes Im[(k|l|² − l|k|²)(c̄−b̄)] = Im[kl̄] · (|c|²−|b|²)/2.
  This is a polynomial-in-coordinates identity that holds exactly when (C1), (C2), (C3) hold. A direct algebraic derivation from C1, C2, C3 is a complete proof. The outliner should attempt this (it may be long but is mechanical).

  **Opening C — Angle-Chasing to Inscribed Angle / Concyclicity.**
  Conditions (C2) and (C3) directly involve M and N. Condition (C2): ∠(BL, BK) = ∠(NL, NC) (directed angles). Condition (C3): ∠(CL, CK) = ∠(MB, MK) (directed angles). Each of these is a "spiral similarity angle condition" that may imply that a specific auxiliary point lies on a known circle. Look for an auxiliary point P (e.g., second intersection of BK with ⊙AKL) satisfying a clean angle identity with M or N that eventually forces the pow(B)−pow(C) balance. Numerically: the second intersection of BK with ⊙AKL is P_BK ≈ (2.874, 1.491) and ∠P_BK-B-A = ∠KBA = α (i.e., P_BK sees the same angle at B as K relative to BA). This could be the key concyclicity seed.

  **Opening D — Inversion through A.**
  Invert through A. The circumcircle ⊙AKL maps to the line K'L'. The midpoints M, N don't invert nicely in general, but the power condition pow(B)−pow(C) = (AB²−AC²)/2 might become a simple collinearity or ratio after inversion. Worth exploring if the other openings get stuck.

---

- **Candidate technique(s):**
  Primary: Power of a point + angle-chasing (Opening A). Secondary: Direct complex-number algebra (Opening B). Both reach the same numerical destination.

- **Cheap-kill candidates:**
  - **Parity/symmetry kill:** If ABC is isoceles (AB = AC), then K and L are forced by symmetry to be reflections across the perpendicular bisector of BC, so O lies on that bisector and OM = ON trivially. The general case cannot be killed this way.
  - **Size bound:** None obvious.
  - **Injection:** None obvious.

- **Knowledge-base entries to use:**
  - "Power of a Point" (Synthetic toolkit section): directly powers Opening A.
  - "Radical Axis": OM = ON is the radical axis condition; M and N have equal power iff they are on the radical axis of {circle} and a degenerate circle.
  - "Directed Angles (mod 180°)": essential for the complex number conditions C1, C2, C3 and for any inscribed-angle argument.
  - "Spiral Similarity": conditions C2 and C3 are precisely "two points see a transformation at equal angles," which is the spiral similarity setup.
  - "Inscribed Angle Theorem": standard tool for any angle-chasing in ⊙AKL.
  - "Complex Numbers in Geometry": directly supports Opening B.

- **Analogous past problems (cruxes):**
  Note: geometry is NOT in the crux corpus (documented in crux_moves_documentation.md). The analogues below come from the past_problems_database.json.

  1. **aimo-0068** (USA TSTST 2023, closest structural analogue): Triangle ABC, centroid G; ∠ABS = ∠ACR = 180° − ∠BGC; prove concyclicity. Crux move: from the angle condition, deduce that a midpoint M of a side satisfies MA² = MG · MR (power-of-a-point at M from a key circle), giving concyclicity. **Why analogous:** the angle conditions force a POWER-OF-A-POINT equality at a midpoint (as in Opening A here). The move "angle condition → point has equal powers wrt two circles → lies on radical axis" is exactly what Opening A proposes.
  
  2. **aimo-0021** (IMO-SL 2013): M = midpoint AB, N = midpoint AC; circumcircles of AMT and ANT intersect the perpendicular bisectors at specific points. Crux move: reflection symmetry about the perpendicular bisector of MN. **Why analogous:** M and N are midpoints of AB and AC (same setup as our problem), and the goal involves showing equidistance from these midpoints; the nine-point center lies on the perpendicular bisector of MN in both problems.
  
  3. **aimo-0125** (IMO 2025): Circumcenter lies on the circumcircle of a specific triangle; angle-chasing via inscribed angles. **Why analogous (weakly):** circumcenter equidistance argument and inscribed angle toolkit.

- **Prior progress:**
  None (Status: unsolved, no approaches tried yet).

- **Dead ends (do not retry):**
  - **K, L, M, N concyclic:** Ruled out numerically; concyclicity error ≈ 0.016 (radius 2.02), confirming these four points are NOT concyclic across the 1-parameter family.
  - **B, K, L, N concyclic:** Error ≈ 1.56. Not concyclic.
  - **M, L, C, K concyclic:** Error ≈ 1.34. Not concyclic.
  - **A, B, K, P_BK concyclic** (P_BK = second intersection of BK with ⊙AKL): Error ≈ 2.47. Not concyclic; so the second intersection of BK with ⊙AKL does NOT lie on ⊙ABK.
  - **P_BK = Q_CL** (hoping second intersections of BK and CL with ⊙AKL coincide): Error 4.63. They are distinct.

- **Small-case / intuition notes:**

  **Conjectured (numerically verified, not proved):**
  - For the scalene triangle A=(1,4), B=(−3,0), C=(3,0), and K=(−1.5, 0.381), L=(2.472, 0.339) satisfying all three conditions: O = circumcenter(AKL) ≈ (0.500, 1.672), and the perpendicular bisector of MN is x = 0.5. So OM = ON exactly (to 6 decimal places). Verified for kx ∈ {−1.5, −1.3, −1.1, −0.9, −0.7} (all give O_x = 0.5000 exactly).
  - The complex conditions C1 = 26.07 (real), C2 = 0.218 (real), C3 = 12.02 (real) are all verified to 8 decimal places.
  - The product r1·r2·r3 = 68.31 is real but shows no obvious factorization in terms of the triangle's elements.

  **Key structural insight (verified):** The reformulation pow(B,⊙AKL) − pow(C,⊙AKL) = (AB²−AC²)/2 holds exactly and is equivalent to OM = ON. This follows from the midpoint-power identity: for A on circle, M=midpoint(AB): pow(M) = (pow(B) − AB²/2)/2.

  **Geometric characterization:** OM = ON iff the circumcenter O of AKL lies on the line through the nine-point center of ABC perpendicular to BC. (The nine-point center is at (0.5, 1.5) in our example; O ≈ (0.5, 1.672); same x-coordinate.) This is a more elegant restatement but not yet easier to prove.

  **Structural observation on conditions 2 and 3:** These conditions directly involve M and N (midpoints), which is why they are the "key" conditions linking K, L to M, N. Condition 2 says ∠LBK = ∠LNC (angle at B from L to K = angle at N from L to C). Condition 3 says ∠LCK = ∠BMK (angle at C from L to K = angle at M from B to K). These look like "B and N see equal angles" and "C and M see equal angles," but the reference rays differ (so they're NOT inscribed-angle concyclicity conditions directly).
