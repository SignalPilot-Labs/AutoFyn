## imo-2026-02

inversion-collinearity: new
Target: Prove OM = ON, where O is circumcenter of triangle AKL, M = midpoint(AB), N = midpoint(AC)
Technique: Inversion centered at A' (radius |A'B| = |A'C|), converting the Key Lemma (A' on circumcircle(AKL)) to collinearity (A*, K*, L* collinear), then Menelaus or directed-angle argument in the inverted picture
Skeleton:
  1. Define A' = (1/2, b) in coordinates B=(0,0), C=(1,0), A=(a,b). A' is the reflection of A over perp-bisector(MN). — by direct computation (already proved)
  2. Key Reduction: A' on circumcircle(AKL) => OM = ON — by symmetry (already proved)
  3. Inversion setup: Let iota be the inversion centered at A' with radius r = |A'B| = |A'C| = sqrt(1/4 + b^2). Under iota: B -> B, C -> C (fixed points on inversion circle), A -> A*, K -> K*, L -> L*. — by inversion definition
  4. Key Lemma transformed: A' on circumcircle(AKL) <=> A*, K*, L* collinear — by inversion property (circle through center maps to line)
  5. Angle preservation at B and C: Since B and C are fixed by iota, angles at B and C are preserved. So angle(K*BA*) = phi (from C1), angle(L*BK*) = mu (from C2), angle(K*CL*) = nu (from C3). — by conformality of inversion at fixed points
  6. Ray construction: K* lies on the ray from B at angle (beta - phi) from BC. L* lies on the ray from C at angle (gamma - phi) from CB. The distances |BK*| and |CL*| are determined by inverting BK and CL. — by geometry + Law of Sines (already have BK, CL formulas)
  7. A* position: A* = A' + r^2 * (A - A') / |A - A'|^2 lies on the horizontal line y = b, at x-coordinate determined by the inversion formula. — by inversion formula
  8. Collinearity proof: Show that A* lies on line K*L* using Menelaus on a suitable triangle, or by computing slopes and showing equality. The angle conditions at N* and M* (transformed from C2 and C3) provide the constraints that force this collinearity. — GAP (the core new work)
  9. Conclude: By step 4, A' on circumcircle(AKL). By step 2, OM = ON. — done
Key lemmas (claim + one-line mechanism):
  - A*, K*, L* collinear under inversion at A' — because the circumcircle through A' maps to a line, and A, K, L are on that circle iff their images are collinear
  - Angles at B and C are preserved under inversion — because B and C are fixed points of the inversion (they lie on the inversion circle)
  - BK* = r^2 / BK (inversion distance formula) — by definition of inversion
Open gaps: Step 8 (proving collinearity in the inverted picture from the angle conditions)
Cases to cover: none (general position triangle)
Watch out for: The Menelaus condition must use both C2 and C3 constraints on N* and M* — the inverted picture at N and M involves circle-circle tangent angles, not line angles; this requires careful handling of conformality

---

trig-identity-direct: new
Target: Prove OM = ON by establishing the Key Lemma via explicit trigonometric identity
Technique: Express K and L explicitly in terms of (alpha, beta, gamma, phi, mu, nu) using the Law of Sines and the trig constraints (*) and (**) from the explorer, then verify the cross-ratio Im[(A-K)(A'-L)/((A-L)(A'-K))] = 0 algebraically
Skeleton:
  1. Coordinates: B = (0,0), C = (1,0), A = (a, b) where a = cos(beta)/sin(alpha), b = sin(beta)/sin(alpha) (from Law of Sines with BC = 1). M = A/2, N = (A+C)/2, A' = (1/2, b). — by setup
  2. Key Reduction: A' on circumcircle(AKL) <=> OM = ON. — already proved
  3. Position of K: K is on ray from B at angle (beta - phi) from positive x-axis, at distance BK = (AB/2) * sin(nu)/sin(phi+nu). So K_x = BK * cos(beta - phi), K_y = BK * sin(beta - phi). — by Law of Sines in triangle BMK (proved)
  4. Position of L: L is on ray from C at angle (pi - gamma + phi) from positive x-axis, at distance CL = (AC/2) * sin(mu)/sin(phi+mu). So L_x = 1 - CL * cos(gamma - phi), L_y = CL * sin(gamma - phi). — by Law of Sines in triangle LNC (proved)
  5. Constraint (*) from C3: 2 sin(alpha) sin(gamma - phi - nu) sin(phi + nu) = sin(gamma) sin(nu) sin(alpha + 2phi + nu). This determines nu given (alpha, beta, gamma, phi). — by explorer (numerically verified)
  6. Constraint (**) from C2: 2 sin(alpha) sin(beta - phi - mu) sin(phi + mu) = sin(beta) sin(mu) sin(alpha + 2phi + mu). This determines mu given the other parameters and the coupling through K's position. — by explorer (numerically verified)
  7. Cross-ratio condition: The Key Lemma is Im[(A-K)(A'-L)/((A-L)(A'-K))] = 0. Substitute the explicit formulas from steps 3-4, using constraints (*) and (**) to eliminate mu and nu. — GAP (algebraic simplification)
  8. The identity should factor or simplify to 0 using product-to-sum trig identities and the constraints. — GAP (the computational core)
  9. Conclude: Key Lemma holds, so OM = ON. — done
Key lemmas (claim + one-line mechanism):
  - BK = (AB/2) sin(nu)/sin(phi+nu) — by Law of Sines in triangle BMK with angle sum phi + nu + angle(BKM) = pi
  - CL = (AC/2) sin(mu)/sin(phi+mu) — by Law of Sines in triangle LNC with angle sum phi + mu + angle(NLC) = pi
  - Constraint (*) — comes from applying Law of Sines in triangle BCK and using the midpoint condition BM = AB/2
  - The factor "2" in constraints (*) and (**) comes from BM = AB/2 and CN = AC/2 — the midpoint is essential
Open gaps: Steps 7-8 (algebraic verification of the trig identity)
Cases to cover: none
Watch out for: The constraints (*) and (**) are coupled (mu depends on K's position, which depends on nu); must solve for nu first then mu. Sign conventions in angle arguments.

---

directed-angle-concyclic: advance
Target: Prove OM = ON via proving A, K, L, A' concyclic through directed angle chase
Technique: Directed angles mod pi, using the symmetric pairing structure (B<->N, C<->M, A<->A')
Skeleton: (as in existing approach, with these additions from explorer insights)
  1-3. Setup and Key Reduction — already proved
  4. NEW: Use the symmetric pairing structure explicitly. C2 says angle(LBK) = angle(LNC) = mu, pairing B with N. C3 says angle(LCK) = angle(BMK) = nu, pairing C with M. The Key Lemma pairs A with A'. — by explorer observation
  5. NEW: Decompose angle(KAL) - angle(KA'L) into contributions from B and C. The "lift" from {B,C} to {M,N} via C2 and C3, then from {M,N} to {A,A'} via the midpoint structure. — GAP (the detailed angle chain)
  6. NEW: The cross-pairing creates a "twist" that C1 (angle(KBA) = angle(ACL) = phi) "untwists". Without C1, the Key Lemma fails by ~1%. — by numerical verification
  7. Conclude: angle(KAL) = angle(KA'L) => A,K,L,A' concyclic => OM = ON. — done
Key lemmas (claim + one-line mechanism):
  - A' is the midpoint-level analog of A — because A' = reflection of A over perp-bisector(MN), just as N is midpoint-level for C and M is midpoint-level for B
  - The "two-step lift" from {B,C} to {M,N} to {A,A'} — C2 gives B<->N, C3 gives C<->M, and the Key Lemma gives A<->A'
Open gaps: Step 5 (detailed directed angle chain using the symmetric pairing)
Cases to cover: none
Watch out for: The chain must use all three conditions C1, C2, C3 in load-bearing ways — no subset suffices

---

power-of-point: advance
Target: Prove OM = ON via power identity pow(B,w) - pow(C,w) = (AB^2 - AC^2)/2
Technique: Law of Sines + algebraic identity from angle conditions
Skeleton: (as in existing approach, with explicit trig constraints added)
  1-3. Power identity reduction — already proved
  4. BK and CL formulas — already proved
  5. NEW: Use constraint (*) to express nu in terms of (alpha, beta, gamma, phi), and constraint (**) to express mu. — from explorer
  6. NEW: Substitute into the algebraic identity 2[(B-C) x L] |K|^2 - 2[(B-C) x K] |L|^2 = (|B|^2 - |C|^2)(K x L). — GAP (simplification)
  7. The identity should reduce to 0 = 0 after using the trig constraints. — GAP
  8. Conclude: pow(B,w) - pow(C,w) = (AB^2-AC^2)/2 => OM = ON. — done
Key lemmas (claim + one-line mechanism):
  - The power identity is equivalent to O on perp-bisector of MN — by the pow(X,w) = |XO|^2 - R^2 formula and perpendicular bisector characterization
  - The algebraic identity in step 6 is numerically verified to 10^{-12} — by explorer
Open gaps: Steps 6-7 (algebraic simplification using trig constraints)
Cases to cover: none
Watch out for: The identity is complicated; symbolic algebra may be needed. The coupling between mu and nu must be handled.

---

complex-coords: advance
Target: Prove OM = ON via complex cross-ratio being real
Technique: Complex number algebra, showing Im[(A-K)(A'-L)/((A-L)(A'-K))] = 0
Skeleton: (as in existing approach, with new algebraic form)
  1-3. Setup and cross-ratio formulation — already done
  4. NEW: Express C2 in complex form: K(N-L)/(L(A-1)) is real. Express C3 in complex form: A(C-K)/((C-L)(K-M)) is real. — from explorer
  5. NEW: The product C2 * C3 is real (verified: approx -0.888). Both conditions together kill two degrees of freedom in Im[...]. — from explorer
  6. NEW: Show that the two "real" conditions from C2 and C3 together with C1 (which gives s*t real positive where K = sA, L = 1 + t(A-1)) force the Key Lemma's Im[...] = 0. — GAP (the algebraic derivation)
  7. Conclude: cross-ratio real => A,K,L,A' concyclic => OM = ON. — done
Key lemmas (claim + one-line mechanism):
  - s*t is real positive from C1 alone — because arg(s) = -phi and arg(t) = +phi, so arg(s*t) = 0
  - C2 and C3 each kill one imaginary-part degree of freedom — the Im[...] = 0 conditions are two equations
Open gaps: Step 6 (showing three conditions force the Key Lemma)
Cases to cover: none
Watch out for: The algebraic path from two real-ratio conditions to a third is not obvious; may need to find the right combination/quotient

---

spiral-similarity: DEAD
Reason: The spiral similarity centered at L mapping B->N, K->C is NUMERICALLY FALSE (error 1.95). Similarly for spiral at K. The round 1 rejection stands. Do not revive.
