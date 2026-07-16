# Proof Review: IMO 2026 P2

## Problem Statement

Let ABC be a triangle with midpoints M (of AB) and N (of AC). Points K inside BMC, L inside BNC satisfy:
- (Cond 1) angle(KBA) = angle(ACL) = phi
- (Cond 2) angle(LBK) = angle(LNC) = mu
- (Cond 3) angle(LCK) = angle(BMK) = nu

Let O be the circumcenter of triangle AKL. Prove OM = ON.

---

## Approach 1: directed-angle-concyclic

**Builder Status:** partial  
**Reviewer Status:** partial

### What is proven (verified correct):

1. **A' characterization (Step 1):** A' = reflection of A over perp-bisector(MN) is equivalently described as the intersection of (i) the perpendicular bisector of BC and (ii) the line through A parallel to BC. In coordinates with B, C on the real axis and origin at midpoint of BC, this gives A' = Im(A) * i.

   **Verification:** I re-derived this independently. With A = (a, b), B = 0, C = 1: M = (a/2, b/2), N = ((a+1)/2, b/2). The perpendicular bisector of MN is x = (2a+1)/4. Reflecting A gives A' = (1/2, b), which lies on the perpendicular bisector of BC (x = 1/2) and the horizontal line through A.

2. **Reduction (Step 2):** If A, K, L, A' are concyclic, then O (circumcenter of AKL) lies on the perpendicular bisector of MN, hence OM = ON.

   **Verification:** Correct reasoning. The circumcircle passes through A and A' = rho(A), so the center O lies on the perpendicular bisector of AA', which equals the perpendicular bisector of MN (since both pass through the same reflection axis). Since M = rho(N) under this reflection, points on the axis are equidistant from M and N.

3. **Concyclicity criterion (Step 3):** A, K, L, A' concyclic iff angle(KAL) = angle(KA'L) (inscribed angle theorem).

   **Verification:** Standard application of inscribed angle theorem. Correct.

### The Gap (Step 4):

The proof does not establish that the three angle conditions (Cond 1-3) imply angle(KAL) = angle(KA'L).

**Numerical verification:** I independently verified this claim by:
1. Setting up the coordinate system with B = 0, C = 1, A = a + bi
2. Solving for K, L satisfying all three conditions (using scipy.fsolve)
3. Computing the circumcircle of AKL
4. Checking if A' lies on this circumcircle

**Results across 10 configurations:** Error in |O - A'| - R is < 10^{-10} for all tested cases. The numerical evidence is overwhelming.

**Gap severity:** This is a computational/algebraic gap, not a conceptual one. The proof structure is sound. The missing step is the derivation of the inscribed angle equality from the angle conditions, which requires either:
- A synthetic angle chase using the Law of Sines and the "cross-pairing" structure
- An algebraic computation showing the cross-ratio (A, K; L, A') is real

### Scores:
- **Correctness:** 9/10 (all stated claims are correct; gap is clearly identified)
- **Completeness:** 5/10 (the key lemma is unproven)
- **Progress:** Good (reduction established, geometric characterization complete)

### Verdict: CHANGES REQUESTED
Status: **partial**

Gap to close: Prove angle(KAL) = angle(KA'L) from the three angle conditions (C1)-(C3).

---

## Approach 2: power-of-point

**Builder Status:** partial  
**Reviewer Status:** partial

### What is proven (verified correct):

1. **Claim 1 (Power reduction):** OM = ON iff pow(B, omega) - pow(C, omega) = (AB^2 - AC^2)/2.

   **Verification:** I verified this algebraically. With A at origin:
   - pow(B) - pow(C) = |BO|^2 - |CO|^2 = |B|^2 - |C|^2 + 2O·(C-B)
   - O on perp-bisector of MN iff O·(C-B) = (|C|^2 - |B|^2)/4
   - Substituting: pow(B) - pow(C) = |B|^2 - |C|^2 + (|C|^2 - |B|^2)/2 = (|B|^2 - |C|^2)/2 = (AB^2 - AC^2)/2

   Correct.

2. **Claims 2-3 (Law of Sines):**
   - BK = (AB/2) * sin(nu)/sin(phi+nu)
   - CL = (AC/2) * sin(mu)/sin(phi+mu)

   **Verification:** Standard Law of Sines in triangles BMK and LNC. I verified numerically: formulas match actual distances to 10^{-12}.

3. **Step 3 (Circumcenter equations):** O·K = |K|^2/2 and O·L = |L|^2/2 from the equidistance condition |O| = |O-K| = |O-L|.

   Correct.

### The Gap (Claim 4):

The algebraic identity
$$2[(B-C) \times L] \cdot |K|^2 - 2[(B-C) \times K] \cdot |L|^2 = (|B|^2 - |C|^2)(K \times L)$$
is verified numerically but not proven analytically.

**Gap severity:** Same as directed-angle-concyclic. The proof framework is complete but the final algebraic verification is missing.

### Promotable Lemmas:

1. **Power-Midpoint Reduction:** "OM = ON iff pow(B,omega) - pow(C,omega) = (AB^2 - AC^2)/2" - **CERTIFIED.** This is a general geometric lemma independent of the angle conditions. Proof in Step 1 is complete.

2. **Law of Sines in BMK/LNC:** These are direct applications of the Law of Sines. Not worth caching as they are trivial.

### Scores:
- **Correctness:** 9/10 (all stated claims correct)
- **Completeness:** 5/10 (key identity unproven)
- **Progress:** Good (reduction and Law of Sines established)

### Verdict: CHANGES REQUESTED
Status: **partial**

Gap to close: Same as directed-angle-concyclic (the two approaches converge to the same gap).

---

## Approach 3: complex-coords

**Builder Status:** partial  
**Reviewer Status:** partial

### What is proven (verified correct):

1. **Coordinate setup:** B = (0,0), C = (1,0), A = (a,b). Then M = (a/2, b/2), N = ((a+1)/2, b/2), and A' = (1/2, b).

   **Verification:** Correct and identical to my independent computation.

2. **Lemma 1 (A' on perp-bisector of BC):** |A'B|^2 = |A'C|^2 = 1/4 + b^2.

   **Verification:** Correct by direct calculation.

3. **Main reduction:** If A' on circumcircle(AKL), then O on perp-bisector of MN, hence OM = ON.

   **Verification:** Same as directed-angle-concyclic. Correct.

4. **Cross-ratio formulation:** The concyclicity condition is equivalent to Im[(z_A - z_L)(z_K - z_{A'})/(z_K - z_L)] = 0.

   **Verification:** Standard result. Correct.

### The Gap:

Same as the other approaches: proving that the angle conditions force the cross-ratio to be real (equivalently, that A' lies on the circumcircle of AKL).

### Promotable Lemmas:

1. **A' on perp-bisector of BC:** Lemma 1 is correct and proven. However, this is a trivial coordinate computation, not worth caching.

### Scores:
- **Correctness:** 9/10 (all stated claims correct)
- **Completeness:** 5/10 (key lemma unproven)
- **Progress:** Good (coordinate framework established, numerical verification strong)

### Verdict: CHANGES REQUESTED
Status: **partial**

Gap to close: Algebraic proof that the three angle conditions imply Im[(z_A - z_L)(z_K - z_{A'})/(z_K - z_L)] = 0.

---

## Summary

All three approaches converge to the **same structural result** and the **same gap**:

**Proven (by all three):**
1. Define A' = reflection of A over perp-bisector of MN
2. A' lies on the perpendicular bisector of BC
3. If A' lies on circumcircle(AKL), then OM = ON

**Not proven (by any):**
4. The three angle conditions force A' to lie on circumcircle(AKL)

**Numerical verification:** The key lemma (A' on circumcircle of AKL) is verified to machine precision (error < 10^{-10}) across 10+ configurations. The numerical evidence is overwhelming.

**Assessment:** This is a genuine IMO P2-level difficulty. The reduction is non-trivial and the approaches are sound. The remaining gap is a challenging algebraic or synthetic derivation.

---

## Recommendations for Next Round

1. **Attempt a synthetic angle chase:** The "cross-pairing" structure (B linked to N in Cond 2, C linked to M in Cond 3) suggests a spiral similarity or concyclic quadrilateral that bridges K and L.

2. **Try parametric elimination:** Express mu and nu explicitly in terms of phi and the triangle parameters using Conds 2-3, then substitute into the cross-ratio condition.

3. **Look for intermediate concyclic quadrilaterals:** There may be other points (intersections of BK, CL with MN or the circumcircle) that reveal the structure.

4. **Consider directed angles mod pi:** The standard directed angle chase may simplify the algebra.

---

## Outcomes to Record

- **directed-angle-concyclic:** partial (reduction complete, key lemma unproven)
- **power-of-point:** partial (reduction complete, algebraic identity unproven)
- **complex-coords:** partial (reduction complete, cross-ratio condition unproven)

All approaches made real progress. None are dead ends.

---

## Certify Promotable Lemmas

**Power-Midpoint Reduction (from power-of-point):**
- Statement: Let omega be a circle with center O. Let M = (A+B)/2 and N = (A+C)/2 be midpoints. Then OM = ON iff pow(B,omega) - pow(C,omega) = (|AB|^2 - |AC|^2)/2.
- Proof: Complete (Step 1 of power-of-point approach).
- **CERTIFIED.** Will write to lemmas folder.

Other proposed lemmas are either trivial (Law of Sines applications) or unproven (A' on circumcircle), so not certified.
