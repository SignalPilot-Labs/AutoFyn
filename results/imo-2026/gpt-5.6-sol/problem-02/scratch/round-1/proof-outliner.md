## imo-2026-02

oriented-determinant-elimination: new
Target: Prove that the circumcentre O of triangle AKL satisfies OM = ON.
Technique: Similarity normalization, oriented trigonometric coordinates, and a 2-by-2 circumcircle/determinant elimination (Knowledge Base: Coordinates / complex / barycentric; Trig identities; Reformulate). This is the most concrete end-to-end route and does not assume any auxiliary cyclic quadrilateral.
Skeleton:
  1. Normalize A=(0,0), B=(1,0), C=q(cos gamma,sin gamma), with q>0, and set alpha=angle KBA=angle ACL, beta=angle LBK=angle LNC, delta=angle LCK=angle BMK — by direct similarity and the stated interior/ray-order hypotheses.
  2. Intersect the rays from B and C with the rays from the midpoints to obtain
     K=B-r e_{-alpha}, r=sin(delta)/(2 sin(alpha+delta)), and
     L=C-u e_{gamma+alpha}, u=q sin(beta)/(2 sin(alpha+beta)) — by the sine rule in the two ray-intersection triangles.
  3. Encode the two remaining incidences by q=F(delta) and q^{-1}=F(beta), where
     F(t)=[cos gamma-cos t cos(gamma+2alpha+t)]/[2 sin^2(alpha+t)] — by taking oriented cross products with the prescribed ray directions.
  4. Write the circle through A,K,L as X·X-U X_x-V X_y=0. Its centre is O=(U/2,V/2), and passage through K,L is the linear system U K_x+V K_y=|K|^2, U L_x+V L_y=|L|^2 — by the standard Cartesian circle equation.
  5. Linearize the conclusion as O·(C-B)=(q^2-1)/4, equivalently
     2(|K|^2[C-B,L]+|L|^2[K,C-B])=(q^2-1)[K,L] — by expanding OM^2-ON^2 and Cramer's rule.
  6. Substitute the formulas from Steps 2-3 into the determinant identity and reduce its numerator to zero using q=F(delta), qF(beta)=1 — by a finite trigonometric factorization, organized with 2 sin x sin y=cos(x-y)-cos(x+y).
  7. Conclude the linearized equality and hence OM=ON — since distances are nonnegative.
Key lemmas (claim + the one-line mechanism that makes it true):
  - The oriented coordinate formulas in Step 2 are branch-correct — because K and L lie in the specified interiors and inside the specified angles, so every relevant ray parameter and sin(alpha+beta), sin(alpha+delta) is positive.
  - The incidence function is exactly F(t) — because the identity 2 sin(alpha+t)sin(gamma+alpha+t)-sin t sin(gamma+2alpha+t)=cos gamma-cos t cos(gamma+2alpha+t) compresses each cross-product equation.
  - The residual determinant in Step 6 vanishes under the two incidence equations — because after clearing the positive sine denominators, terms can be paired into the two defining numerators q-F(delta) and q^{-1}-F(beta) (the builder must exhibit the full factorization, not cite a CAS).
Open gaps: Step 6 is the main unproved computation; Steps 2-3 also require a complete directed-ray derivation. A CAS may discover the grouping, but the submitted proof must display a human-checkable algebraic identity.
Cases to cover: q=1 versus q≠1 is not intrinsically needed; cover all admissible alpha,beta,delta and verify [K,L]≠0 from nondegeneracy of triangle AKL. If a cleared factor could vanish, dispose of it using interiority before division.
Watch out for: Unsigned acos introduces supplementary branches. Do not infer beta=delta except in a separately proved symmetric special case. The numerical configuration from the explorers disproves B,C,K,L concyclic, so the structural report's proposed circle and all consequences (3)-(5) must not be used. Cheap structural reductions retained here are the linearization of OM=ON and the origin-centred circle equation; no still cheaper valid cyclicity was found.

antipode-quarter-turn: new
Target: Prove that the circumcentre O of triangle AKL satisfies OM = ON.
Technique: Factor-2 midpoint homothety, antipode/Thales transformation, and complex quarter-turn equations (Knowledge Base: Synthetic toolkit; Coordinates / complex; Reformulate). This adapts the antipode move seen in past problem aimo-0389, but proves all transferred claims here from scratch.
Skeleton:
  1. Let X be the antipode of A on (AKL). The homothety H_{A,2} sends M,N,O to B,C,X, respectively, so OM=ON is equivalent to XB=XC — by midpoint definitions and X=2O-A.
  2. Normalize complex coordinates a=0, b=1, c=q e^{i gamma}. Retain the six oriented ray descriptions
     k=1-r e^{-i alpha}=1/2+s e^{i delta}=c-w e^{i(gamma+alpha+delta)} and
     l=c-u e^{i(gamma+alpha)}=1-v e^{-i(alpha+beta)}=(c/2)+h e^{i(gamma-beta)},
     with all six coefficients positive — by the angle hypotheses and interiority.
  3. Use the antipode right angles XK perpendicular AK and XL perpendicular AL to write x-k=i lambda k and x-l=i mu l for real lambda,mu; equivalently Re(conj(x)k)=|k|^2 and Re(conj(x)l)=|l|^2 — by Thales' theorem.
  4. Eliminate the positive ray lengths r,s,w,u,v,h in matched pairs, rather than solving for x outright. The three given angle equalities pair the arguments, while BM=BA/2 and CN=CA/2 supply the only scale factors — by taking imaginary parts of quotients of the ray equations.
  5. Establish Re(conj(x)(c-b))=(q^2-1)/2, equivalently |x-b|^2=|x-c|^2 — by the quarter-turn telescoping lemma below.
  6. Infer XB=XC and apply the inverse homothety to obtain OM=ON.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Antipode reduction: OM=ON iff XB=XC — because H_{A,2} multiplies both distances by 2 and maps (O,M,N) to (X,B,C).
  - Quarter-turn telescoping lemma: for the six positive ray equations in Step 2 and a point x satisfying the two Thales equations in Step 3, Re(conj(x)(c-b))=(|c|^2-|b|^2)/2 — because successive imaginary-part equations cancel the unknown ray lengths cyclically, and the uncancelled endpoint multipliers are 2BM/AB=2CN/AC=1.
Open gaps: The quarter-turn telescoping lemma is the load-bearing unproved step; the builder must write the exact ordered equations and cancellation. This route must not silently revert to the determinant factorization of oriented-determinant-elimination.
Cases to cover: lambda or mu equal to 0; possible right-angle special positions; all signs of directed angles allowed by the stated interiors. No separate isosceles case should be assumed.
Watch out for: One angle equality determines only a rotation argument, not a similarity scale. Do not claim an unsupported direct similarity maps K to L. The analogy to aimo-0389 licenses trying an antipode, not importing any conclusion from that problem.

sine-product-antipode: new
Target: Prove that the circumcentre O of triangle AKL satisfies OM = ON.
Technique: Pure synthetic antipode reduction followed by a cyclic product of sine-rule ratios and directed-angle cancellation (Knowledge Base: Synthetic toolkit; similar triangles; sine rule; Work backward). This is deliberately independent of the coordinate determinant lemma.
Skeleton:
  1. Introduce the A-antipode X on (AKL), and reduce OM=ON to XB=XC by the factor-2 homothety at A.
  2. Label alpha=angle KBA=angle ACL, beta=angle LBK=angle LNC, delta=angle LCK=angle BMK. Translate XK perpendicular AK and XL perpendicular AL into directed angles involving X in triangles XBK, XBL, XCK, XCL — by Thales' theorem and angle addition, with no assertion that B,C,K,L are cyclic.
  3. Apply the sine rule to the four triangles XBK, XBL, XCK, XCL to express XB/XC as a product of ratios involving BK,BL,CK,CL and sines of alpha,beta,delta and the two angles at A.
  4. Apply the sine rule in the midpoint triangles BMK and CNL, and in the triangles cut out by the rays BK,BL,CK,CL, to replace the four side-length ratios in Step 3. Arrange the substitutions in the same cyclic order as the three given angle equalities.
  5. Cancel the repeated sine factors. The remaining metric factor is (2BM/AB)(AC/2CN)=1, yielding XB/XC=1 — by BM=AB/2 and CN=AC/2.
  6. Hence XB=XC, and the homothety gives OM=ON.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Four-triangle sine-product lemma: the quotient XB/XC can be written so that every non-midpoint sine and every K,L side length occurs once in numerator and once in denominator — because the four triangles around X share XK or XL, and the perpendiculars rotate AK,AL by the same quarter-turn.
  - Midpoint closure of the product: after inserting the three given equal angles, the sole uncancelled factors are 2BM/AB and AC/2CN — because beta closes the B-to-N pair, delta closes the C-to-M pair, and alpha closes the B-to-C pair.
Open gaps: Steps 3-5 require the exact directed sine-product identity. This is the central builder task; if an uncancelled factor remains, this approach fails and must not be patched by assuming a false cyclic quadrilateral.
Cases to cover: Directed-angle configurations selected by K inside angle LBA and L inside angle ACK; potential obtuse angles where ordinary-angle subtraction changes sign; degenerate sine denominators are excluded only after an explicit interiority argument.
Watch out for: This skeleton is promising but less verified than the determinant route. Generic numerical data falsify B,C,K,L cyclic, MK=NL, and similar naive congruences. The borrowed move from aimo-0124 is only the philosophy of multiplying rotation/scale factors around a chain; its polygon lemma does not directly apply here.

inverted-circle-intercepts: new
Target: Prove that the circumcentre O of triangle AKL satisfies OM = ON.
Technique: Equal power to (AKL), inversion at A, and an affine intercept identity on AB and AC (Knowledge Base: power of a point, inversion, coordinates; Reformulate). This bypasses both the antipode sine-product lemma and any BCKL cyclicity claim.
Skeleton:
  1. Let P≠A and Q≠A be the second intersections of AB and AC with omega=(AKL). Since Pow_omega(Y)=OY^2-OA^2, reduce OM=ON to Pow_omega(M)=Pow_omega(N) — by the circle power formula.
  2. Using directed lengths on AB and AC, rewrite this as
     (AB/2)(AB/2-AP)=(AC/2)(AC/2-AQ), or equivalently
     AB·AP-AC·AQ=(AB^2-AC^2)/2 — by M,A,B and N,A,C collinear.
  3. Invert about A with arbitrary squared radius rho. Then omega becomes the line ell through K'=rho K/AK^2 and L'=rho L/AL^2. The intercepts P'=ell∩AB and Q'=ell∩AC satisfy AP·AP'=AQ·AQ'=rho — by inversion.
  4. Derive the equation of ell directly from the six ray incidences. In dual/intercept form it must imply
     rho AB/AP' - rho AC/AQ'=(AB^2-AC^2)/2 — by taking oriented cross products of K',L' with the two side directions and eliminating the ray parameters.
  5. Convert back with AP=rho/AP', AQ=rho/AQ', obtaining the power equality from Step 2 and hence OM=ON.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Equal-power/intercept reduction in Step 2 — because the secant power at a midpoint is the signed product MA·MP, with M between A and B and N between A and C.
  - Inverted-line intercept lemma: the line through K/AK^2 and L/AL^2 has side intercepts satisfying rho AB/AP' - rho AC/AQ'=(AB^2-AC^2)/2 — because each of K and L has three oriented ray descriptions, and eliminating their positive ray parameters is linear after reciprocal-square inversion.
Open gaps: The inverted-line intercept lemma is unproved and is the route's decisive test. The builder should derive it explicitly before investing in exposition; if inversion leaves nonlinear reciprocal terms that do not cancel, this approach should be marked partial rather than borrowing identities from another slug.
Cases to cover: P or Q coinciding with a midpoint (zero power); P,Q lying on side extensions rather than segments; signed lengths throughout; no division by AP' or AQ' without proving they are finite and nonzero.
Watch out for: Do not use the structure explorer's identities AK^2=AB·BK or AL^2=AC·CL: they arise from the false BCKL cyclicity and fail in the supplied generic numerical sample. Inversion is lower priority than the first three routes, but it genuinely avoids their shared target lemma.
