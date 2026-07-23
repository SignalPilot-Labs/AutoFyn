## imo-2026-02

antipode-rotation-chain: new
Target: Prove for every configuration satisfying the hypotheses that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Synthetic antipode construction; directed rotations and spiral similarities with scale tracking (Knowledge Base: Synthetic toolkit; Reformulate). This is the cheap structural route, replacing the centre by one point on the circle.
Skeleton:
  1. Let \(P\) be the antipode of \(A\) on \((AKL)\); then \(KP\perp KA\), \(LP\perp LA\), and \(O\) is the midpoint of \(AP\) — by Thales and the definition of antipode.
  2. Reduce the desired equality to \(PB=PC\): from midpoint vectors, \(2\overrightarrow{OM}=\overrightarrow{PB}\) and \(2\overrightarrow{ON}=\overrightarrow{PC}\) — by the midpoint identities for \(O,M,N\).
  3. Put \(x=\angle KBA=\angle ACL\), \(y=\angle LBK=\angle LNC\), \(z=\angle LCK=\angle BMK\), retaining directed ray order from the interior hypotheses — by directed-angle bookkeeping.
  4. Build the spiral similarities/rotations determined by the ordered ray pairs \((BA,BK)\leftrightarrow(CL,CA)\), \((BK,BL)\leftrightarrow(NC,NL)\), and \((CK,CL)\leftrightarrow(MK,MB)\); express their dilation factors by sine law — by the Synthetic toolkit's similar-triangle and spiral-similarity methods.
  5. Prove the rotation-chain lemma: after inserting \(BA/BM=CA/CN=2\), the product of the three dilation factors is \(1\), and the composed direction change identifies the two vectors \(P-B\) and \(P-C\) up to a rotation — this is the load-bearing scale-compatible concatenation, adapting the factor-two/spiral discovery move of past problem `aimo-0705`.
  6. Conclude \(PB=PC\), then \(OM=ON\) — by Steps 2 and 5.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Antipode reduction: \(OM=ON\iff PB=PC\) — because doubling vectors from the respective midpoints gives \(2(M-O)=B-P\) and \(2(N-O)=C-P\).
  - Rotation-chain lemma: the three angle correspondences yield a composition with unit scale taking the \(PB\)-direction to the \(PC\)-direction — because sine-law scale factors telescope after the midpoint ratios \(BA/BM=CA/CN=2\) are inserted.
Open gaps: Step 5 is unproved and is the decisive gap; the builder must exhibit the actual intermediate triangles/vectors and the telescoping scale formula rather than merely asserting a rotation chain. Step 4 must also verify each spiral correspondence has two justified directed angles.
Cases to cover: Both orientations of triangle \(ABC\) via directed angles; all legal positions of the antipode and all possible locations of the feet defining the perpendicular lines. No division by a vanishing sine.
Watch out for: One equal angle does not prove triangle similarity; direction matching without scale matching is insufficient. Do not assume \(AB=AC\), \(AK=AL\), or symmetry under \(B\leftrightarrow C\).

equal-power-second-intersections: new
Target: Prove for every configuration satisfying the hypotheses that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Power of a point, directed second intersections, half-turns about the midpoints, and radical axes (Knowledge Base: Power of a point; radical axes; similar triangles). This adapts the decisive equal-power move of `aimo-0266` and the auxiliary second-intersection move of `aimo-0245`.
Skeleton:
  1. Let \(\omega=(AKL)\). Replace \(OM=ON\) by \(\operatorname{Pow}_\omega(M)=\operatorname{Pow}_\omega(N)\) — because \(\operatorname{Pow}_\omega(X)=OX^2-R^2\).
  2. Let \(D\ne A\) and \(E\ne A\) be the intersections of \(\omega\) with the oriented lines \(AB\) and \(AC\). Rewrite the target as \(MA\cdot MD=NA\cdot NE\) in directed lengths — by power of a point.
  3. Apply the half-turns about \(M,N\), which send \(A\) to \(B,C\), to the relevant rays through \(M,N\). Use the equalities at \(M,N\) together with those at \(B,C\) to construct companion points/circles containing \(D,E\) — by preservation of angles and lengths under half-turns.
  4. Prove the second-intersection lemma: those companion circles identify \(MD/NE\) as \(NA/MA=AC/AB\), with the correct directed signs — by two similar triangles or a radical-axis power chain.
  5. Substitute Step 4 into Step 2 to obtain equal powers, hence \(OM=ON\) — by Step 1.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Equal-power reduction: equal distances from the centre are equivalent to equal powers — because the same squared radius is subtracted from both squared distances.
  - Second-intersection lemma: \(MA\cdot MD=NA\cdot NE\) — because half-turning at the midpoints converts the factors \(MA,NA\) into vertex-side factors and the three angle equalities should create a pair of similar triangles or a common radical-axis chain.
Open gaps: Steps 3–4 are open: the builder must name the companion points/circles and prove all incidences. If no clean description of \(D,E\) emerges, this route should be marked partial rather than replacing the gap with trigonometric computation.
Cases to cover: \(D,E\) may lie on extensions rather than segments, so use directed products throughout; exclude tangency only after showing it cannot cause a degenerate denominator, or handle it separately.
Watch out for: Independent half-turns do not preserve cross-conditions automatically. The product identity must be proved with signs, not unsigned lengths.

trig-sine-factorization: new
Target: Prove for every configuration satisfying the hypotheses that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Controlled directed-angle parametrization, sine law, power of a point, and a targeted trigonometric factorization (Knowledge Base: trig identities; similar triangles/trig cevians; Introduce a substitution). This is an analytic whole-proof fallback, not a raw coordinate bash.
Skeleton:
  1. Set \(a=BC,b=CA,c=AB\), \(\alpha=\angle A,\beta=\angle B,\gamma=\angle C\), and define positive \(x,y,z\) by the three given equalities — by the interior ray order.
  2. Record the exhaustive branch restrictions \(0<x<\min(\beta,\gamma)\), \(0<y<\beta-x\), \(0<z<\gamma-x\) — by \(K,L\) lying inside the stated triangles and angles.
  3. Derive the two separated closure constraints
  \[
  \frac c2\frac{\sin z}{\sin(x+z)}=a\frac{\sin(\gamma-x-z)}{\sin(\alpha+2x+z)},
  \quad
  \frac b2\frac{\sin y}{\sin(x+y)}=a\frac{\sin(\beta-x-y)}{\sin(\alpha+2x+y)}
  \]
  — by sine law first in \(BMK,CNL\), then in \(BKC,BLC\).
  4. Let \((AKL)\) meet \(AB,AC\) again at \(D=pB,E=qC\). Derive explicit formulas for \(p,q\) in terms of \(\alpha,\beta,\gamma,x,y,z\) using only directed sine law and the known rays of \(K,L\) — by cyclic-angle equalities and sine law.
  5. Translate the conclusion to \(c^2(1-2p)=b^2(1-2q)\) — by directed power at the midpoints.
  6. Factor the difference in Step 5 as explicit sine prefactors times the left sides of the two closure constraints in Step 3 — by sine addition/subtraction identities (tangent-half-angle variables may be used to discover, but the final identity must be displayed and verifiable).
  7. Use Step 3 to make the factorization vanish, proving equal powers and hence \(OM=ON\) — by power of a point.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Separated closure equations — because \(K\) can be measured independently from \(BMK\) and \(BCK\), while \(L\) can be measured independently from \(CNL\) and \(BCL\).
  - Target factorization — because the conjectured target numerator is the difference of the \(y\)-closure and \(z\)-closure contributions after sine addition formulas.
Open gaps: Explicit formulas for \(p,q\) in Step 4 and the complete factorization in Step 6 are unproved. These are concrete symbolic tasks; the builder should test algebra computationally but present a human-checkable identity.
Cases to cover: The single positive interior branch described in Step 2; possible second intersections on side extensions are covered by directed parameters \(p,q\). Check every denominator sine is nonzero.
Watch out for: The angle of \(BK\) versus \(BC\), and of \(CL\) versus \(CB\), depends on ray order. No squaring or inverse-tangent step may introduce reflected branches.

oblique-circle-linearization: new
Target: Prove for every configuration satisfying the hypotheses that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Oblique affine coordinates and linear circle coefficients (Knowledge Base: Coordinates / complex / barycentric; Reformulate). This avoids computing the centre and keeps the target linear.
Skeleton:
  1. Put \(A=0\), use \((B,C)\) as an oblique basis, and write \(X=rB+sC\), where \(AB=c,AC=b,\angle A=\alpha\) — by affine normalization.
  2. Write every circle through \(A\) as
  \[
  c^2r^2+b^2s^2+2bc\cos\alpha\,rs-\lambda r-\mu s=0
  \]
  — by expanding \(|rB+sC|^2-U\cdot(rB+sC)=0\).
  3. Since \(M=(1/2,0),N=(0,1/2)\), reduce the goal to \(\lambda-\mu=(c^2-b^2)/2\) for \(\omega=(AKL)\) — by evaluating the two powers in the circle equation.
  4. Parametrize the rays \(BK,BL,CK,CL,MK,NL\) by positive scalar multiples of rotations through \(x,x+y,x+z\); solve each pair of ray equations for the affine coordinates of \(K,L\) while retaining positivity — by two-dimensional determinant intersection formulas.
  5. Substitute \(K,L\) into the circle equation and use Cramer's rule to express \(\lambda-\mu\) as a rational determinant in their coordinates — by the nonsingularity of the \(2\times2\) system (noncollinearity of \(A,K,L\)).
  6. Prove the determinant identity that the three angle equations force the value in Step 3; simplify using \(M=(1/2,0),N=(0,1/2)\) before expansion — by determinant bilinearity and sine addition identities.
  7. Conclude equal powers and therefore \(OM=ON\) — by Steps 2–3.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Circle-coefficient criterion: \(OM=ON\iff\lambda-\mu=(c^2-b^2)/2\) — because substituting the two midpoint coordinates makes all mixed terms vanish and power difference is linear in \(\lambda,\mu\).
  - Determinant identity — because ray intersections are quotients of oriented \(2\times2\) determinants and the three equal angle rotations impose exactly the two incidence closures.
Open gaps: Steps 4 and 6 need explicit formulas and simplification. The builder must show a reasonably short determinant cancellation, not appeal to a computer black box.
Cases to cover: Both orientations handled by signed determinants; positivity of all ray scalars from interiority; noncollinearity of \(A,K,L\), implicit in the stated circumcentre, must be noted.
Watch out for: Raw tangent equations obscure signs. Squaring dot/cross relations creates extraneous branches. Keep the conclusion linear and do not solve for \(O\).

doubled-homothety-locus: new
Target: Prove for every configuration satisfying the hypotheses that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Factor-two homothety, one-parameter reconstruction, direct similarity, and fixed circumcentre locus (Knowledge Base: spiral similarity; Invariant; Reformulate). This adapts the moving-triangle crux of `aimo-1007` and midpoint doubling of `aimo-0705`.
Skeleton:
  1. Dilate by factor \(2\) about \(A\), writing \(K'=2K,L'=2L,O'=2O\). Then \(O'\) is the circumcentre of \(AK'L'\) and \(OM=ON\iff O'B=O'C\) — by homothety and \(2M=B,2N=C\) in vectors based at \(A\).
  2. Reconstruct each admissible \(K,L\) from \(x,y,z\) using the rays at \(B,M,C,N\); identify the one free parameter after the two closure conditions — by ray intersection and the three given angle equalities.
  3. Compare an admissible doubled triangle \(AK'L'\) with the limiting member \(ABC\) corresponding to \(K=M,L=N\) (used as a limiting reference, not asserted admissible) — by continuity of ray intersections as \(x\to0\).
  4. Prove the moving-similarity lemma: the two doubled triangles are linked by a direct similarity (or a pair of spiral similarities with a common fixed axis) whose induced map sends their circumcentres along the perpendicular bisector of \(BC\) — by the closure equalities among \(x,y,z\) and the factor-two midpoint relations.
  5. Since the reference circumcentre lies on the perpendicular bisector of \(BC\), infer \(O'B=O'C\) for every admissible member — by Step 4's fixed-locus statement.
  6. Scale back to obtain \(OM=ON\) — by Step 1.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Homothety reduction: the midpoint target becomes \(O'B=O'C\) — because dilation sends \((M,N,O)\) to \((B,C,O')\) and sends the circumcircle of \(AKL\) to that of \(AK'L'\).
  - Moving-similarity lemma: all admissible circumcentres lie on the fixed perpendicular bisector of \(BC\) — because the closure rotation chain should produce direct similarities whose centre/axis is fixed by the doubled endpoint pair \(B,C\).
Open gaps: Step 4 is wholly unproved and Step 2's parameter count must be replaced by explicit reconstruction. The limit in Step 3 requires continuity and cannot itself prove the invariant. This route should advance only if the builder finds a precise similarity centre or fixed axis.
Cases to cover: Legal parameter interval and its endpoints as limits; possible coincidence of similarity centres; both orientations of the configuration.
Watch out for: Parameter counting and numerical collinearity are not proof. A generic direct similarity does not preserve a fixed perpendicular bisector; its centre/axis and action on \(B,C\) must be established explicitly.
