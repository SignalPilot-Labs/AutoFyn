## Status
partial

## Approaches tried
- Directed angle chase to A' concyclicity — established key reduction and final step, but the main angle chase (showing the conditions force the inscribed angle equality) has a gap (Round 1)
- Cross-ratio reformulation with computational verification — reduced Key Lemma to an algebraic identity; verified to machine precision (10^{-14}) across many configurations, but formal algebraic proof not complete (Round 3)

## Current best

**Summary:** The proof is complete except for one algebraic step that has been verified computationally but not proved algebraically. The computational verification is robust and leaves no doubt about correctness, but the formal derivation requires showing that a certain polynomial identity holds on a variety.

---

### Established Results (Rigorous)

**1. Definition of A':**
In coordinates B = 0, C = 1, A = a + bi:
- A' = (1/2) + bi = reflection of A over perpendicular bisector of MN
- M = A/2 (midpoint of AB)
- N = (A+1)/2 (midpoint of AC)

*Proof:* The perpendicular bisector of MN is vertical at x = (2a+1)/4. Reflecting A = (a, b) gives x-coordinate 2*(2a+1)/4 - a = 1/2, y-coordinate b unchanged.

**2. Key Reduction:**
If A' lies on the circumcircle of triangle AKL, then OM = ON.

*Proof:* Let rho be reflection over the perpendicular bisector of MN. Since A' = rho(A), if the circumcircle omega contains both A and A', then omega is symmetric under rho. Therefore its center O lies on the axis of rho, which is the perpendicular bisector of MN. Since rho(M) = N, we have OM = ON.

**3. Condition C1 in complex form:**
- K = r_K * e^{i*theta_K} where theta_K = beta - phi (beta = angle ABC)
- L = 1 + r_L * e^{i*theta_L} where theta_L = pi - gamma + phi (gamma = angle BCA)

This constrains K and L to specific rays from B and C respectively, leaving r_K, r_L as free parameters.

**4. Conditions C2 and C3 in complex form:**
- C2: Im[(K-B)(L-N) / ((L-B)(C-N))] = 0
- C3: Im[(K-C)(B-M) / ((L-C)(K-M))] = 0

*Proof:* C2 states angle(LBK) = angle(LNC). Using arg((L-B)/(K-B)) = angle from BK to BL at B, the condition becomes arg((K-B)/(L-B)) = arg((C-N)/(L-N)), i.e., (K-B)(L-N)/((L-B)(C-N)) is real. Similarly for C3.

**5. Cross-ratio reformulation of Key Lemma:**
A' on circumcircle(AKL) iff CR = (A-K)(A'-L)/((A-L)(A'-K)) is real.

*Proof:* By the inscribed angle theorem / cross-ratio characterization of concyclicity.

**6. Angular shift identity:**
Since A - A' = (a - 1/2) is purely real, the condition Im(CR) = 0 is equivalent to:

Im(u)|v|^2 - Im(v)|u|^2 = d * Im(conj(u)*v)

where u = A' - K, v = A' - L, d = a - 1/2.

*Proof:* Write A - K = u + d, A - L = v + d. Then CR = (u+d)v / (u(v+d)). For CR to be real, arg(u+d) - arg(u) = arg(v+d) - arg(v). Using the formula for angular shift by adding real d, this becomes the stated identity.

---

### The Gap: Algebraic Proof of Key Lemma

**Statement:** On the C1 rays (K and L parametrized by r_K, r_L), the conditions C2 = 0 and C3 = 0 imply the Key Lemma identity Im(CR) = 0.

**Computational Verification:**
- Tested across 50+ configurations with varying (a, b, phi)
- At every solution of C2 = C3 = 0, the Key Lemma identity holds to 10^{-14} precision
- Perturbations violating C2 or C3 cause the identity to fail
- The function F(a, b, phi) = Im(CR) at the solution is identically 0 to numerical precision

**Why Algebraic Proof is Difficult:**
The coefficients in C2, C3, and the Key Lemma identity involve cos(beta - phi), sin(gamma + phi), etc., which depend on the triangle geometry. A direct Groebner basis computation with floating-point coefficients accumulates numerical errors. A fully symbolic approach would require eliminating the angle parameters, leading to very high-degree polynomials.

**What Would Complete the Proof:**
Either:
1. A coordinate-free synthetic argument relating the inscribed angles
2. A symbolic algebra verification with exact arithmetic
3. A continuity argument from the isoceles special case (where A = A' and the result is trivial) combined with a proof that the identity is constant

---

### Special Case: Isoceles Triangle

When a = 1/2, we have A = A' = (1/2, b). The cross-ratio becomes:
CR = (A-K)(A-L) / ((A-L)(A-K)) = 1

which is trivially real. This provides a "base case" for any continuity/deformation argument.

---

### Conclusion

**Proved rigorously:**
1. Setup and characterization of A'
2. Key Reduction: A' on circumcircle => OM = ON
3. Condition reformulations in complex coordinates
4. Cross-ratio characterization of concyclicity
5. Angular shift identity for the Key Lemma

**Verified computationally but not proved algebraically:**
6. C1 + C2 + C3 imply the Key Lemma (Im(CR) = 0)

**Status:** The proof is partial because Step 6 relies on computational verification rather than algebraic derivation. However, the verification is robust (10^{-14} precision across diverse configurations), and the reduction in Steps 1-5 is complete.

---

## Promotable lemmas

**Angular Shift Lemma:**
For complex numbers u, v with Im(u), Im(v) > 0 and real d:
The cross-ratio (u + d) * v / ((v + d) * u) is real if and only if
Im(u) * |v|^2 - Im(v) * |u|^2 = d * Im(conj(u) * v)

*Proof:* The cross-ratio is real iff arg((u+d)/u) = arg((v+d)/v). For z = x + iy with y > 0, we have arg(z+d) - arg(z) = arctan(yd / (|z|^2 + xd)). Setting these equal and cross-multiplying yields the identity.
