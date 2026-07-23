## imo-2026-02

oblique-circle-linearization: revise
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Directed ray reconstruction plus oblique circle coefficients, closed by an explicit low-degree polynomial certificate (Knowledge Base: Sine Law/power of a point, coordinates, substitution, minimal-polynomial reduction, and the resultants-style identity \(gP=Q\)). This adapts the explicit-certificate move of `aimo-0635` and the remainder-reduction move of `aimo-0949`; unlike the former CAS-only attempt, the final identity is displayed and auditable.
Skeleton:
  1. Introduce \(x=\angle KBA=\angle ACL\), \(y=\angle LBK=\angle LNC\), \(z=\angle LCK=\angle BMK\), and import the certified oriented-ray reconstruction lemma to obtain the strict angle ranges, positive ray lengths \(t=BK,s=CL\), formulas for \(K,L\), and the two closure relations — by directed determinant intersections and the Sine Law.
  2. Eliminate \(z\) alone from \(2t\sin(x+z)=c\sin z\) and the \(K\)-closure relation, and eliminate \(y\) alone from \(2s\sin(x+y)=b\sin y\) and the \(L\)-closure relation, using \(a/\sin\alpha=b/\sin\beta=c/\sin\gamma\), to derive
     \[
     Q_t=bc\sin x-c^2\sin(\alpha+x)+ct\{2\sin\alpha+\sin(\alpha+2x)\}-2t^2\sin(\alpha+x)=0,
     \]
     \[
     Q_s=bc\sin x-b^2\sin(\alpha+x)+bs\{2\sin\alpha+\sin(\alpha+2x)\}-2s^2\sin(\alpha+x)=0.
     \]
  3. Import the certified oblique circle-coefficient criterion: with \(d=C-B\), it suffices to prove
     \[
     F:=2(|K|^2[L,d]-|L|^2[K,d])-(c^2-b^2)[K,L]=0.
     \]
  4. Substitute \(K=B-t(\cos x,-\sin x)\), \(L=C-s(\cos(\alpha+x),\sin(\alpha+x))\), and verify the displayed certificate
     \[
     \begin{aligned}
     2\sin(\alpha+x)F={}&-\bigl(2bc\sin\alpha+2s[b\sin x-c\sin(\alpha+x)]\bigr)Q_t\\
     &-\bigl(-2bc\sin\alpha+2t[b\sin(\alpha+x)-c\sin x]\bigr)Q_s.
     \end{aligned}
     \]
     Make this human-checkable by collecting both sides in the monomials \(1,t,s,t^2,ts,s^2,t^2s,ts^2\) and displaying the coefficient comparison after only the sine addition formulas; do not cite CAS or ideal membership.
  5. Since \(Q_t=Q_s=0\) and \(\sin(\alpha+x)>0\), infer \(F=0\), then apply the oblique criterion/power identity to conclude \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - The closure data are equivalent to the two independent quadratics \(Q_t=Q_s=0\) — because each auxiliary angle appears in one midpoint ray equation and one opposite-vertex closure, and substituting its cotangent plus the triangle Sine Law removes it without mixing \(s,t\).
  - The determinant target lies in the span of those two quadratics with the displayed linear multipliers — because direct collection in the eight monomials of total degree at most three matches coefficients via \(\sin(u+v)\) addition formulas.
  - \(F=0\) is equivalent to \(OM=ON\) — because the certified oblique circle coefficient system converts equal midpoint powers into exactly this determinant equation.
Open gaps: Steps 2 and especially the full coefficient-table verification in Step 4 must be written out; also repair the existing file's malformed LaTeX/control characters and remove its empty `## Full proof` section while partial.
Cases to cover: All admissible scalene and isosceles triangles are covered uniformly; reflection used to orient \([B,C]>0\) must be stated; no division by \(b-c\).
Watch out for: Explicitly justify \(s,t>0\), \(\sin x,\sin y,\sin z,\sin(x+y),\sin(x+z),\sin(\alpha+x)>0\), every Sine-Law denominator, and \([K,L]\ne0\). Do not replace the displayed coefficient audit by “CAS verifies.”

trig-sine-factorization: advance
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Directed second intersections and equal powers, with ray-length quadratic reduction and an explicit factorization certificate (Knowledge Base: circle coordinates, directed power of a point, resultants-style identities, and minimal-polynomial reduction). The geometric finish mirrors the power conversion in `aimo-0266`, while the certificate supplies the formerly missing algebra.
Skeleton:
  1. Retain the verified angle-range, ray-reconstruction, closure, and second-intersection portions of the existing approach; rename the positive lengths \(BK=t\), \(CL=s\).
  2. Derive the two quadratic residuals \(Q_t,Q_s\) stated in the revised oblique approach by eliminating \(z,y\) separately, not by expanding the old residuals \(R_z,R_y\).
  3. Rewrite the existing target identity (8) as the same determinant polynomial \(F=0\) after substituting the circle coefficients (6); explicitly show the sign correspondence so the new certificate really closes the old equation rather than a negated variant.
  4. Verify the boxed identity for \(2\sin(\alpha+x)F\) as a linear combination of \(Q_t,Q_s\), preferably by displaying the complete coefficient table in \(s,t\).
  5. Infer the relation \(c^2(1-2p)=b^2(1-2q)\) for the second intersections \(D=pB,E=qC\), and import the certified directed midpoint-power formula to obtain equal powers of \(M,N\) with respect to \((AKL)\), hence \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - The large old \((y,z)\)-factorization can be replaced without loss by two ray-length quadratics — because the midpoint relations solve \(\cot z,\cot y\) linearly in \(t,s\), absorbing all denominators before closure is expanded.
  - The new determinant \(F\) is precisely the numerator of the old second-intersection identity (8) — because Cramer's formulas for the circle through \(0,K,L\) express \(p,q\) in the same two determinants.
  - Equal directed powers imply equal centre distances — because \(\operatorname{Pow}_\omega(X)=OX^2-R^2\).
Open gaps: Steps 2–4 require prose derivation and the complete human-checkable coefficient audit; all later steps are already rigorous in the live file.
Cases to cover: Second intersections on either segments or extensions are handled by directed parameters; all triangle shapes satisfying the hypotheses are uniform.
Watch out for: Preserve every branch and positivity argument from the current file; do not revive the old exponential-polynomial/ideal-membership assertion; check the exact sign convention relating (8) and \(F\).

midpoint-cross-intersections: new
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Pure synthetic cross-intersections, cyclic quadrilaterals, radical axes, and power of a point (Knowledge Base: directed angle chasing, similar triangles, Miquel/radical-center architecture, midpoint homotheties). This is far from the shared determinant-elimination wall. It adapts `aimo-0245`'s manufacture of second intersections and common perpendicular bisectors, and `aimo-0266`'s conversion of circumcentre equidistance into a midpoint product.
Skeleton:
  1. Define \(U=BK\cap AC\), \(V=CL\cap AB\), and let \(D\ne A,E\ne A\) be the intersections of \(\omega=(AKL)\) with \(AB,AC\), respectively, allowing directed extensions.
  2. Prove \(\triangle ABU\sim\triangle ACV\) from \(\angle KBA=\angle ACL\) and the angle at \(A\), obtaining the directed product identity \(AB\cdot AV=AC\cdot AU\).
  3. Prove the two auxiliary cyclicities \(B,L,N,U\) and \(C,K,M,V\) from \(\angle LBK=\angle LNC\) and \(\angle LCK=\angle BMK\), with directed supplementary-angle conventions.
  4. Establish the synthetic midpoint theorem
     \[
     D=\operatorname{mid}(B,V),\qquad E=\operatorname{mid}(C,U).
     \]
     The planned route is to compare \(\omega\) with \(\Gamma_C=(BLNU)\) and \(\Gamma_B=(CKMV)\): identify the relevant second common points/radical axes by a directed angle chase in the complete quadrilateral \(AB,AC,BK,CL\), then turn the resulting power equalities on \(AB,AC\) into \(BD=DV\), \(CE=EU\). If this identification fails, attempt the same theorem via the factor-2 homotheties about \(M,N\), while retaining the line at infinity so midpoint information is not lost.
  5. Using \(M=\operatorname{mid}(A,B)\), \(D=\operatorname{mid}(B,V)\), compute by directed power
     \(\operatorname{Pow}_\omega(M)=-AB\cdot AV/4\); similarly obtain \(\operatorname{Pow}_\omega(N)=-AC\cdot AU/4\).
  6. Apply Step 2 to equate these powers, then \(OM^2-R^2=ON^2-R^2\) to conclude \(OM=ON\).
Key lemmas (claim + the one-line mechanism that makes it true):
  - \(AB\cdot AV=AC\cdot AU\) — because the cross-intersection triangles have one common directed angle at \(A\) and the equal angle \(\angle KBA=\angle ACL\).
  - \((BLNU)\) and \((CKMV)\) are cyclic — because the other two given angle equalities become equal directed angles subtending \(BL\) and \(CK\), respectively.
  - The second intersections are \(D=(B+V)/2,E=(C+U)/2\) — conjecturally because the auxiliary-circle radical-axis network forces equal adjacent directed segments on the two sidelines; this is the load-bearing lemma to prove, not an established fact.
  - The midpoint theorem immediately gives the desired power equality — because the four directed distances from \(M,N\) become half-products and similarity identifies those products.
Open gaps: Step 4 in full. The builder must first prove the exact second-common-point/radical-axis incidences and then derive the midpoint equalities; numerical agreement is not evidence in the proof.
Cases to cover: Directed locations of \(U,V,D,E\) on side extensions; supplementary representatives in both cyclicity tests; possible parallel cross-lines should be ruled out or handled projectively from the strict interior angle ranges.
Watch out for: Do not assert midpoint descriptions, Miquel incidences, or radical axes from the diagram. A bare projective transformation does not preserve midpoints. Verify all directed product signs before Step 5.

inversion-fixed-collinearity: new
Target: Prove that the circumcentre \(O\) of \(AKL\) satisfies \(OM=ON\).
Technique: Inversion at \(A\) linearizing \((AKL)\) into a line, followed by a tangent-chord/spiral-similarity incidence argument (Knowledge Base: inversion, tangent-chord angle chasing, power and radical axes, complex coordinates for exact reduction). This is a genuinely different top-level target. It adapts `aimo-0878`'s move of choosing an inversion that converts a centre relation into a fixed incidence, but all transformed incidences must be proved here from scratch.
Skeleton:
  1. Put \(A=0\) and invert by \(Z'=Z/|Z|^2\). Prove that if \(\omega=(AKL)\) has centre \(o\), then its image line \(K'L'\) has equation \(\operatorname{Re}(\overline{o}z)=1/2\).
  2. For \(b=AC\ne c=AB\), define \(P=2(C-B)/(b^2-c^2)\) and calculate directly that
     \[
     OM=ON\iff P\in K'L'.
     \]
     For \(b=c\), derive separately the limiting equivalent target \(K'L'\parallel BC\).
  3. Compute \(M'=2B/c^2,N'=2C/b^2\), prove \(P\in M'N'\) and \(AP\parallel BC\), and identify \(P\) as the intersection of chord \(M'N'\) with the tangent at \(A\) to \(\Gamma=(AM'N')\), the inverse of line \(MN\).
  4. Invert the lines \(BK,CL,MK,NL\) into circles through \(A\). Translate each original angle equality into a directed angle equality between these inverse circles/lines. Use the tangent-chord theorem at \(P\), together with the midpoint scale encoded by \(M',N'\), to prove that both \(K'\) and \(L'\) lie on one line through \(P\); equivalently, prove \(P,K',L'\) collinear. The builder should seek a named spiral-similarity or radical-axis point here, not expand the complex collinearity residual into the old determinant identity.
  5. Apply Step 2 to conclude \(OM=ON\); in the isosceles case use the parallel version.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Inversion turns the circumcircle through \(A\) into \(\operatorname{Re}(\overline{o}z)=1/2\) — because substituting \(z=w/|w|^2\) into \(|z-o|^2=|o|^2\) cancels the quadratic term.
  - The metric goal is fixed collinearity (or fixed direction when \(b=c\)) — because \(OM^2-ON^2=\operatorname{Re}(\overline{o}(C-B))+(c^2-b^2)/4\), matching the inverse-line equation at \(P\).
  - \(P\) is a tangent-chord point of \((AM'N')\) — because direct affine computation gives \(P\in M'N'\) and \(AP\parallel MN\), while inversion makes \(AP\) the tangent direction at \(A\) to the inverse of \(MN\).
  - The angle data force \(P,K',L'\) collinear — conjecturally because the transformed angle correspondences compose to the tangent-chord spiral similarity with its ratio fixed by \(M',N'\); this is the load-bearing open lemma.
Open gaps: Step 4 is wholly unproved; Step 2's sign convention and Step 3's tangent identification need clean derivations. This route is exploratory and must not fall back to unrestricted trigonometric expansion.
Cases to cover: \(b\ne c\) and \(b=c\); orientation under inversion; all transformed circles distinct/nondegenerate; directed angles modulo \(\pi\).
Watch out for: Angle matching alone controls only rotation, not similarity ratio. Do not divide by \(b^2-c^2\) in the isosceles case. Do not substitute inverse coordinates and recreate the determinant wall under a new name.
