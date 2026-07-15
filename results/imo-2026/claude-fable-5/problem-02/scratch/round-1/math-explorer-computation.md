## imo-2026-02

### Problem restatement
Triangle ABC, M = midpoint AB, N = midpoint AC. K inside triangle BMC, L inside triangle BNC.
Conditions:
1. angle_KBA = angle_ACL (= α, say)
2. angle_LBK = angle_LNC (= β, say)
3. angle_LCK = angle_BMK (= γ, say)
O = circumcenter(AKL). Prove OM = ON.

### Degrees of freedom
K and L have 4 dof, subject to 3 angle equalities. Generic system has 1-parameter family. Numerically confirmed: fixing K_x and solving (K_y, L_x, L_y) from the 3 conditions gives isolated solutions (a 1-param curve in K). The family is real and has multiple members.

### Primary numerical finding (strongest invariant)
Across all triangles tested and all members of the 1-parameter family:

**pow(M, circumcircle(AKL)) = pow(N, circumcircle(AKL))** (exact, to machine precision ~10^{-14}).

This is exactly equivalent to OM = ON (since pow(P, omega) = |PO|^2 - R^2, and OM^2 - R^2 = ON^2 - R^2 iff OM = ON).

Equivalent formulations verified numerically:
- O_x = (2*A_x + B_x + C_x)/4 = midpoint(MN)_x [in coordinates where BC is horizontal, O lies on the perpendicular bisector of MN = line through midpoint(MN) perpendicular to BC].
- MA * MP = NA * NQ where P = second intersection of line AB with circumcircle(AKL), Q = second intersection of line AC with circumcircle(AKL). Both MA * MP = |pow(M)| and NA * NQ = |pow(N)| equal the same value for every pair.
- pow(B, circumcircle(AKL)) - pow(C, circumcircle(AKL)) = (AB^2 - AC^2)/2. [The key "reduced" claim.]

### Which conditions are responsible?
Tested using pairs of conditions only (fixing K, solving for L from 2 of 3 conditions, checking the 3rd):
- Conditions 1+2 alone: pow(M) != pow(N) in general. C3 not satisfied.
- Conditions 1+3 alone: no solutions found (over-constrained for L).
- Conditions 2+3 alone: pow(M) != pow(N) in general. C1 not satisfied.
Conclusion: all three conditions are jointly needed; no pair suffices.

### Spiral similarity structure (key structural finding)
Working in complex coordinates with B = 0, C = a (real), A = d + ie:

Condition 1 (angle_KBA = angle_ACL = alpha) + Condition 3 (angle_BMK = gamma) give:
**K = p_K * exp(-i*alpha) * A**
where p_K = sin(gamma)/(2*sin(alpha + gamma)).

Derivation: In triangle BMK, angle_KBM = alpha, angle_BMK = gamma, BM = AB/2.
Law of sines: BK = (AB/2)*sin(gamma)/sin(alpha+gamma). K lies on ray from B at CW angle alpha from BA.
In complex: K = BK * exp(-i*alpha) * A/|A| = p_K * exp(-i*alpha) * A. Verified numerically (error < 2*10^{-15}).

Condition 1 (angle_ACL = alpha) + Condition 2 (angle_LNC = beta) give:
**L = C + p_L * exp(+i*alpha) * (A - C)**
where p_L = sin(beta)/(2*sin(alpha + beta)).

Derivation: In triangle CNL, angle_LCN = alpha, angle_LNC = beta, CN = AC/2.
Law of sines: CL = (AC/2)*sin(beta)/sin(alpha+beta). L lies on ray from C at CCW angle alpha from CA.
In complex: L = C + p_L * exp(+i*alpha) * (A-C)/|A-C| * |A-C| = C + p_L * exp(+i*alpha) * (A-C). Verified numerically (error < 3*10^{-15}).

**CRUCIAL STRUCTURE: K uses exp(-i*alpha) (CW rotation at B), L uses exp(+i*alpha) (CCW rotation at C). Same angle magnitude, OPPOSITE directions. Both determined by the single angle alpha from condition 1.**

The cross-conditions (not yet built into the K, L formulas above):
- angle_LBK = beta (from condition 2 applied to the K-side)
- angle_LCK = gamma (from condition 3 applied to the L-side)
These two constrain (alpha, beta, gamma): given alpha, beta(alpha) and gamma(alpha) are determined by these cross-conditions, giving the 1-parameter family.

### Key reduced claim for the proof
Show: pow(B, circumcircle(AKL)) - pow(C, circumcircle(AKL)) = (AB^2 - AC^2)/2.

This is equivalent (via |BO|^2 - |CO|^2 = pow(B) - pow(C) and the perpendicular bisector formula) to:
**O_x = (2d + a)/4 = midpoint(MN)_x** (where d = A_x, a = C_x, B_x = 0).

In coordinate-free terms: (4O - 2A - B - C) perpendicular to (C - B), i.e., the circumcenter of AKL has the same projection onto line BC as the midpoint of MN.

### Additional confirmed numerical invariants
For each valid (K, L):
- pow(B, omega) = (AB/2)*sin(gamma)/sin(alpha+gamma)^2 * ... [varies with the family]
- pow(C, omega) - pow(B, omega) = (AC^2 - AB^2)/2 = CONSTANT across the whole family.
  This follows from O_x = midpoint(MN)_x, and |CO|^2 - |BO|^2 = AC^2/... [a simple formula in O_x].
- MA*MP = NA*NQ for all pairs (second intersections P, Q of lines AB, AC with circumcircle(AKL)).

### Candidate proof approaches

**Approach A (most direct): Power-of-a-point via the spiral formulas.**
Using:
  K = p_K * exp(-i*alpha) * A
  L = C + p_L * exp(+i*alpha) * (A - C)
compute the circumcenter O explicitly from the perp-bisector equations:
  Re(O * (p_K exp(+i*alpha) - 1) * conj(A)) = (p_K^2 - 1) * |A|^2 / 2
  Re(O * (p_L exp(-i*alpha) - 1) * conj(A-C)) = (|L|^2 - |A|^2)/2
and show Re(O) = (2d + a)/4. Likely a direct computation; the conjugate structure (exp(-i*alpha) for K vs exp(+i*alpha) for L) may cause cancellations that give Re(O) = const. Needs the cross-conditions to close.

**Approach B (angle chasing): Show pow(B,omega) - pow(C,omega) = (AB^2 - AC^2)/2.**
pow(B, circumcircle(AKL)) = BA * BP where P is the second intersection of line BA with circumcircle(AKL).
pow(C, circumcircle(AKL)) = CA * CQ where Q is the second intersection of line CA with circumcircle(AKL).
Must show AB * BP - AC * CQ = (AB^2 - AC^2)/2.
Using the law of sines in AKL and the angle conditions to relate BP and CQ to alpha, beta, gamma.

**Approach C (trigonometric ceva): Express OM^2 - ON^2 directly.**
OM^2 - ON^2 = (M - N) . (M + N - 2O). Since MN || BC, (M-N) is in the BC direction. So OM = ON iff O has the same projection onto BC as midpoint(MN). Use the circumcenter formula for AKL and trigonometric identities from the three angle conditions to verify this projection.

**Approach D (synthetic / radical axis):**
Identify two circles whose radical axis passes through midpoint(MN) and is perpendicular to BC, and show the circumcircle of AKL is coaxial with them (so its center has the required BC-projection). The circles involving B, M, K and C, N, L might be candidates, given conditions 2 and 3 respectively.

### Dead ends
- M, K, N, L concyclic: FALSE (normalized determinant 10^{-3} to 5*10^{-3}, not zero).
- B, K, C, L concyclic: FALSE (normalized determinant 10^{-3} to 6*10^{-3}, not zero).
- A is the spiral center mapping K->L and M->N: FALSE (A is the spiral center for B->C and M->N, but AK/AL != AM/AN and angle_KAL != angle_MAN in general).
- MK = NL (implying an isosceles trapezoid): FALSE (diff 10^{-3} to 4*10^{-3}).

### Small-case / intuition notes
- The 1-parameter family is parametrized by alpha = angle_KBA = angle_ACL. As alpha decreases (K moves towards M, L moves towards N), the circumcenter of AKL moves vertically along the perpendicular bisector of MN.
- The angles beta and gamma both increase as alpha decreases (K approaches M and L approaches N). As K -> M, we should have L -> N and AKL degenerates to AMN.
- Isosceles triangle ABC: by symmetry K and L are symmetric about the axis, giving OM = ON trivially. The three angle conditions reduce to K = L' (mirror of L) which is immediate.
- The conjugate rotation structure (exp(-i*alpha) for K at B, exp(+i*alpha) for L at C) is the key algebraic fingerprint of condition 1.

### Knowledge-base entries to use
- Geometry synthetic toolkit: power of a point (and concyclicity converse PA*PB = PC*PD), radical axes.
- Coordinates / complex: place B=0, C=a real, use complex number expressions for K and L.
- Trig cevians (Ceva): the angles alpha, beta, gamma and their law-of-sines relations in BMK and CNL.
- The "Verify final answers" rule: OM = ON must hold exactly, which is why we use pow equality.

### Analogous past problems (cruxes)
The crux corpus covers NT/combinatorics/algebra only (no geometry entries). No matches possible.

### Prior progress
None (round 1, empty workspace).

### Best guess at proof structure
Step 1: Introduce alpha, beta, gamma. Express in complex coordinates.
Step 2: Derive K = p_K exp(-i*alpha) * A and L = C + p_L exp(+i*alpha)*(A-C) from conditions.
Step 3: Compute circumcenter O using perpendicular bisector equations.
Step 4: Show Re(O) = (2*Re(A) + Re(B) + Re(C))/4 = midpoint(MN)_x using the cross-conditions (angle_LBK = beta and angle_LCK = gamma) as algebraic constraints on (alpha, p_K, p_L).
This gives OM = ON.

The cross-conditions are the hardest step; they link p_K, p_L, alpha through the specific positions of K and L relative to each other. Without them (using only p_K and p_L independently), the result would not hold.
