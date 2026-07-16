## imo-2026-02

directed-angle-concyclic: new
Target: Prove OM = ON by showing circumcircle(AKL) passes through A' = reflection of A over perp-bisector(MN)
Technique: Directed angle chase — prove angle(KAL) = angle(KA'L) (mod pi), hence A,K,L,A' concyclic
Skeleton:
  1. Define A' = reflection of A over perp-bisector(MN) = intersection of perp-bisector(BC) with line through A parallel to BC — by construction, |A'B| = |A'C|
  2. Reduce to concyclicity: A,K,L,A' concyclic => circumcircle(AKL) symmetric under reflection => O on perp-bisector(MN) => OM = ON — by reflection symmetry
  3. Express angle(KA'L) = angle(KA'B) + angle(BA'C) + angle(CA'L) — by angle addition
  4. Use condition (2) angle(LBK) = angle(LNC) to relate angle(KA'B) to angles in triangle BMK — by inscribed angle / Law of Sines chain
  5. Use condition (3) angle(LCK) = angle(BMK) to relate angle(CA'L) to angles in triangle LNC — by inscribed angle / Law of Sines chain  
  6. Use condition (1) angle(KBA) = angle(ACL) = phi to establish cross-symmetry — by direct substitution
  7. Combine to show angle(KAL) = angle(KA'L), hence concyclic — by directed angle calculation
Key lemmas (claim + the one-line mechanism that makes it true):
  - A' on circumcircle(AKL) — because the angle conditions (1)-(3) force angle(KAL) = angle(KA'L) via the symmetric structure |A'B| = |A'C|
Open gaps: Steps 4-5 (expressing angles at A' in terms of conditions 2,3); Step 7 (final angle equality)
Cases to cover: none (single configuration)
Watch out for: Sign conventions in directed angles; the chain from angles at B,C to angles at A' may require intermediate points

power-of-point: new
Target: Prove OM = ON by showing pow(B, omega) - pow(C, omega) = (AB^2 - AC^2)/2 where omega = circumcircle(AKL)
Technique: Power of a point + Law of Sines in multiple triangles
Skeleton:
  1. Set phi = angle(KBA) = angle(ACL), mu = angle(LBK) = angle(LNC), nu = angle(LCK) = angle(BMK) — notation
  2. Express pow(B, omega) via second intersection P of line AB with omega: pow(B) = BA * BP — by power of point formula
  3. Express pow(C, omega) via second intersection Q of line AC with omega: pow(C) = CA * CQ — by power of point formula
  4. Use Law of Sines in triangle BMK: BK = (AB/2) sin(nu) / sin(phi+nu) — by sine rule with condition (3)
  5. Use Law of Sines in triangle LNC: CL = (AC/2) sin(mu) / sin(phi+mu) — by sine rule with condition (2)
  6. Use Law of Sines in triangles ABK, ACL to express AK, AL in terms of phi and the triangle — by sine rule
  7. Compute pow(B) - pow(C) using the expressions for P, Q positions on circumcircle — by algebraic manipulation
  8. Verify pow(B) - pow(C) = (AB^2 - AC^2)/2, then use midpoint relations M = (A+B)/2, N = (A+C)/2 to conclude OM = ON — by direct calculation
Key lemmas (claim + the one-line mechanism that makes it true):
  - BK = (AB/2) sin(nu) / sin(phi+nu) — because in triangle BMK, BM = AB/2, angle(MBK) = phi, angle(BMK) = nu, apply sine rule
  - pow(B) - pow(C) = (AB^2 - AC^2)/2 — because the "cross-pairing" (B-N, C-M) in conditions (2)-(3) produces factor 1/2 via the midpoint structure
Open gaps: Step 7 (main power computation); Step 8 (translation to OM = ON via midpoint identities)
Cases to cover: none
Watch out for: The second intersections P, Q lie on different sides of A depending on configuration — handle signs carefully

spiral-similarity: new
Target: Prove OM = ON via composition of spiral similarities induced by conditions (2) and (3)
Technique: Spiral similarity — conditions (2) and (3) encode spiral similarity angles; compose to find fixed structure
Skeleton:
  1. Interpret condition (2) as spiral similarity angle: angle(LBK) = angle(LNC) = mu means directions from L toward B,K relate to directions from L toward N,C — by directed angle interpretation
  2. Let sigma_L = spiral similarity centered at L with rotation angle mu — by definition
  3. Interpret condition (3) as spiral similarity angle: angle(LCK) = angle(BMK) = nu — by directed angle interpretation
  4. Let sigma_K = spiral similarity centered at K with rotation angle nu — by definition
  5. Compute the composition tau = sigma_K . sigma_L — by spiral similarity composition formula
  6. Determine fixed points of tau and relationship to perp-bisector(MN) — by fixed point analysis
  7. Show tau fixes A' or maps A -> A', forcing A' on circumcircle(AKL) — by spiral similarity properties
  8. Conclude OM = ON from A' on circumcircle — by reflection symmetry
Key lemmas (claim + the one-line mechanism that makes it true):
  - The composition tau has the perp-bisector(MN) as an axis of symmetry or fixed line — because the midpoint structure (M on AB, N on AC) and the cross-pairing (B-N, C-M) combine under composition
Open gaps: Steps 1-4 (precise identification of spiral similarity point maps); Steps 5-7 (composition analysis and fixed point structure)
Cases to cover: none
Watch out for: The naive guess sigma_L(B) = N with K -> C is numerically false (per explorer); need careful analysis of what the spiral similarities actually map

complex-coords: new
Target: Prove OM = ON by algebraic verification that A' lies on circumcircle(AKL) in complex coordinates
Technique: Complex coordinate calculation with perp-bisector(MN) as imaginary axis; verify cross-ratio is real
Skeleton:
  1. Place origin at midpoint(MN), imaginary axis = perp-bisector(MN). Then M = -d (real), N = d (real), A = a (complex), B = -2d - a, C = 2d - a — by coordinate setup
  2. A' = -Re(a) + i*Im(a) (reflection of A over imaginary axis) — by reflection formula
  3. Translate condition (1) to complex form: arg((A-B)/(K-B)) = arg((L-C)/(A-C)) (mod pi) — by angle-argument correspondence
  4. Translate conditions (2), (3) similarly — by angle-argument correspondence
  5. Parameterize K = B + t * e^{i*theta_K}, L = C + s * e^{i*theta_L} where theta_K, theta_L determined by phi and triangle — by ray parameterization
  6. Apply conditions (2), (3) to constrain t, s, theta_K, theta_L — by substitution into complex equations
  7. Check concyclicity: cross-ratio (A, K; L, A') = ((A-L)(K-A'))/((A-A')(K-L)) is real iff A,K,L,A' concyclic — by cross-ratio criterion
  8. Verify Im(cross-ratio) = 0 using constraints from step 6 — by algebraic calculation
  9. Conclude O on imaginary axis (= perp-bisector(MN)), hence OM = ON — by circumcenter symmetry
Key lemmas (claim + the one-line mechanism that makes it true):
  - Cross-ratio (A,K;L,A') is real — because the three angle constraints (1)-(3) are polynomial conditions that imply Im(cross-ratio) = 0 identically
Open gaps: Step 6 (deriving explicit constraints on t, s, angles); Step 8 (algebraic verification of cross-ratio being real)
Cases to cover: none
Watch out for: The algebra may be heavy; may need sympy or careful by-hand manipulation. Ensure directed angle signs match complex argument conventions.
