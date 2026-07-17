## imo-2026-02
- Distinct openings:
  1. **Invert at the distinguished vertex \(A\), and replace the circumcenter metric claim by a fixed collinearity.** Identify the plane with \(\mathbb C\), put \(A=0\), and use inversion \(I(Z)=Z'=Z/|Z|^2=1/\overline Z\) (the radius is immaterial). If \(\omega=(AKL)\) has center \(O=o\), then its image is the line \(K'L'\), with exact equation
     \[
     \Re(\overline o\,z)=\frac12.
     \]
     For \(b=AC\ne c=AB\), define the fixed point
     \[
     P=\frac{2(C-B)}{b^2-c^2}.
     \]
     Directly from the preceding line equation,
     \[
     OM=ON\iff \Re(\overline o(C-B))=\frac{b^2-c^2}{4}
     \iff P\in K'L'.
     \]
     Thus the whole problem becomes the incidence statement \(P,K',L'\) collinear, rather than the existing closure/determinant identity. This equivalence is exact and independent of the parametrization of \(K,L\). In the exceptional isosceles case \(b=c\), the exact transformed target is \(K'L'\parallel BC\).
  2. **Give the fixed point \(P\) a synthetic inversion meaning.** Since \(M'=2B/c^2\) and \(N'=2C/b^2\), one checks
     \[
     P\in M'N',\qquad AP\parallel BC\parallel MN.
     \]
     The inverse of line \(MN\) is the circle \(\Gamma=(AM'N')\), whose tangent at \(A\) is parallel to \(MN\). Hence \(P\) is exactly the intersection of chord \(M'N'\) with the tangent to \(\Gamma\) at \(A\). This supplies tangent-chord and power relations at \(P\), and suggests looking for a spiral-similarity or radical-axis interpretation that forces the inverse points \(K',L'\) onto the same fixed line. This is genuinely farther from the current circle-coefficient elimination target.
  3. **Complex-coordinate version of the inversion opening.** Reuse the certified angle variables and ray reconstruction only as a diagnostic. With
     \[
     r=\frac{\sin z}{2\sin(x+z)},\qquad q=\frac{\sin y}{2\sin(x+y)},
     \]
     the inverse points have the relatively low-degree forms
     \[
     K'=\frac1{c(1-r e^{ix})},\qquad
     L'=\frac{e^{i\alpha}}{b(1-qe^{-ix})}.
     \]
     The desired transformed statement is simply
     \[
     \Im\frac{K'-P}{L'-P}=0
     \]
     (with the positive/negative real ratio determined afterward if useful). Numerical probes on three non-isosceles valid configurations gave residuals below \(10^{-12}\) and this imaginary part below \(10^{-12}\), supporting the exact reduction. A direct complex proof should seek an argument equality for \(K'-P\) and \(L'-P\), not expand the imaginary part into the old determinant identity.
- Candidate technique(s): Inversion centered at \(A\); circle-through-inversion-center \(\leftrightarrow\) line; tangent-chord theorem on \(\Gamma=(AM'N')\); spiral similarity or radical-axis interpretation at the fixed tangent/chord intersection \(P\); alternatively complex arguments after inversion. The promising top-level target is fixed collinearity \(P,K',L'\), not another formula for the center of \((AKL)\).
- Cheap-kill candidates: Split \(b=c\) immediately: the fixed point moves to infinity and the transformed claim is only \(K'L'\parallel BC\). For \(b\ne c\), exploit the two elementary incidences \(P\in M'N'\) and \(AP\parallel BC\) before introducing trigonometry. Also test whether tangent-chord at \(A\) converts each given angle equality into one angle at \(P\); this could prove collinearity with no closure-equation elimination. No parity/size pruning applies.
- Knowledge-base entries to use: **Synthetic toolkit** — inversion, spiral similarity, power of a point, radical axes/radical center, and angle chasing; **Coordinates / complex / barycentric** for the exact inverse-line equation and argument criterion; **Reformulate** and **Introduce a substitution / change of variables** for replacing the circumcenter metric statement by inverse collinearity. The existing knowledge-base circle toolkit is relevant; no specialized inversion lemma is currently recorded there.
- Analogous past problems (cruxes): The crux database has no geometry crux records, so these were retrieved from the geometry solutions in `past_problems_database.json` as permitted by the documentation. **aimo-0878** — inversion at a power-defined point maps one circumcircle to another and turns a relation between their centers into membership of both centers on a common perpendicular bisector; genuinely analogous because inversion linearizes a center claim after constructing the correct fixed inversion geometry. **aimo-0266** — an equal-distance-to-circumcenter conclusion is replaced by equality of powers/products; analogous to changing the metric target before attacking the angle data, though it does not use inversion. **aimo-0205** — converts \(OP=OI\) into concyclicity with a circle already known to be centered at \(O\); analogous at the level of replacing a circumcenter-distance goal by a simpler incidence target. Of these, aimo-0878 is the strongest transformation analogue.
- Prior progress: Status is partial. Both sampled live approaches (`trig-sine-factorization`, Elo 1516; `oblique-circle-linearization`, Elo 1484) rigorously established the angle ranges, oriented ray reconstruction, the two closure equations, circle nonsingularity, and midpoint-power/circle-coefficient reductions, but both stop at the same determinant cancellation. Four reviewer-certified lemmas are safe to reuse: `oriented-ray-reconstruction.md`, `circle-second-intersection-through-origin.md`, `directed-midpoint-power-formula.md`, and `oblique-circle-coefficient-criterion.md`. For the inversion route, only the branch/ray facts and possibly the reconstruction formulas are useful; the circle-coefficient and midpoint-power lemmas should be treated as independent verification, not as the route's main engine.
- Dead ends (do not retry): Do not merely substitute the inverse formulas into \(\Im((K'-P)/(L'-P))=0\) and perform unrestricted trigonometric expansion: that is algebraically equivalent to the current shared cancellation wall and would only rename it. Do not rely on a CAS ideal-membership check; round 1 review explicitly requires a displayed human-checkable certificate. Do not discard positive-ray/interiority information when translating angles under inversion. An inversion centered at the circumcenter \(O\) is also unpromising because \(O\) is the unknown object and the defining circle does not linearize as cleanly.
- Small-case / intuition notes: **Conjectural geometric picture, numerically supported:** after inversion at \(A\), the angle conditions force the variable inverse chord \(K'L'\) through the fixed tangent/chord point \(P\) of \(\Gamma=(AM'N')\). Three numerical valid configurations support exact collinearity. The isosceles degeneration predicts a parallel family \(K'L'\parallel BC\), which is a useful sanity check. **Likely bottleneck:** finding the short synthetic translation from the three original angle equalities to the line through \(P\); inversion sends the relevant non-\(A\) lines to circles through \(A\), so careless angle translation can become more complicated. The tangent-chord characterization of \(P\) is the most plausible mechanism for controlling those transformed circle angles without invoking the old closure equations.
