## imo-2026-02
- Distinct openings:
  1. **Quadratic ray-length certificate (strongest complete algebraic opening).** Retain the certified whole-problem route: positive-ray reconstruction of \(K,L\), closure at the opposite vertex, and oblique-circle linearization. Change only the elimination variables. Put
     \[
     t=BK=\frac{c\sin z}{2\sin(x+z)},\qquad s=CL=\frac{b\sin y}{2\sin(x+y)}.
     \]
     Eliminating \(z\), respectively \(y\), between the midpoint formula and the corresponding closure gives the two quadratic residuals
     \[
     Q_t=bc\sin x-c^2\sin(\alpha+x)+ct\{2\sin\alpha+\sin(\alpha+2x)\}-2t^2\sin(\alpha+x),
     \]
     \[
     Q_s=bc\sin x-b^2\sin(\alpha+x)+bs\{2\sin\alpha+\sin(\alpha+2x)\}-2s^2\sin(\alpha+x).
     \]
     If \(F\) denotes “left side minus right side” of the current determinant target
     \[
     2\bigl(|K|^2[L,C-B]-|L|^2[K,C-B]\bigr)-(c^2-b^2)[K,L],
     \]
     exact symbolic collection found the compact displayed certificate
     \[
     \boxed{\begin{aligned}
     2\sin(\alpha+x)F={}&-\bigl(2bc\sin\alpha+2s[b\sin x-c\sin(\alpha+x)]\bigr)Q_t\\
     &-\bigl(-2bc\sin\alpha+2t[b\sin(\alpha+x)-c\sin x]\bigr)Q_s.
     \end{aligned}}
     \]
     This was checked coefficient-by-coefficient as a polynomial in \(s,t\); after expanding angle sums every coefficient is zero. It is a genuinely human-checkable certificate: both sides have total degree at most three in \(s,t\), so one may display the eight coefficients or state direct expansion using the sine addition formulas. This closes the decisive identity once the derivation \(Q_t=Q_s=0\) is written. It supports a complete whole-problem approach when appended to the already certified ray and circle steps, rather than being treated as a standalone sublemma.
  2. **Coefficient-table verification of the same certificate.** For maximal auditability, collect \(F\) in \(t,s\). Its nonzero coefficients are
     \[
     \begin{array}{c|c}
     t^2s&2b\sin x-2c\sin(\alpha+x)\\
     ts^2&2b\sin(\alpha+x)-2c\sin x\\
     t^2&2bc\sin\alpha\qquad s^2=-2bc\sin\alpha\\
     ts&(c^2-b^2)\{2\sin\alpha+\sin(\alpha+2x)\},
     \end{array}
     \]
     with the four lower coefficients obtainable by one expansion of \(K=B-t(\cos x,-\sin x)\), \(L=C-s(\cos(\alpha+x),\sin(\alpha+x))\). Matching this table against the boxed right side is an alternative displayed certificate if a reviewer dislikes an asserted “direct expansion.”
  3. **Original \(y,z\)-residual factorization (inferior fallback).** One can substitute the midpoint expressions for \(s,t\) into the boxed identity and multiply by \(\sin^2(x+y)\sin^2(x+z)\) to obtain a certificate in the old cross-multiplied residuals. This is likely much longer and recreates the round-1 wall; use only if the builder insists on eliminating \(s,t\) completely. The quadratic residuals are preferable because they absorb the midpoint equations before expansion.
- Candidate technique(s): Introduce ray-length variables before trigonometric elimination; tangent/cotangent elimination of the auxiliary angles; polynomial reduction modulo two quadratic closure relations; explicit low-degree ideal-membership certificate; oblique circle coefficients and equal powers for the whole-problem conclusion.
- Cheap-kill candidates: The cheap structural reduction remains \(OM=ON\iff\operatorname{Pow}_{(AKL)}(M)=\operatorname{Pow}_{(AKL)}(N)\), already certified. For the remaining algebra, eliminate \(y,z\) separately rather than expanding them: from \(2t\sin(x+z)=c\sin z\), division by \(\sin z>0\) gives \(\cot z=(c-2t\cos x)/(2t\sin x)\), and similarly \(\cot y=(b-2s\cos x)/(2s\sin x)\). This turns each closure into one quadratic immediately. No parity/pigeonhole argument applies.
- Knowledge-base entries to use: **Resultants / “transform the roots”** (the boxed identity is exactly the recommended explicit identity \(gP=Q\), not a CAS assertion); **Minimal-polynomial reduction** (reduce in \(t,s\) by \(Q_t,Q_s\)); **Coordinates / complex / barycentric**; **Synthetic toolkit: Sine Law and power of a point**; **Introduce a substitution / change of variables**; **Reformulate**. Gröbner ideal membership is relevant only as discovery machinery; the final proof should use the displayed certificate, not cite a black-box normal form.
- Analogous past problems (cruxes): `aimo-0266` — converts circumcentre equidistance into equality of powers and a midpoint-driven product identity; this is the closest geometric analogue and validates the whole-problem framing. `aimo-0949` — defines a remainder and reduces it modulo a lower-degree polynomial relation; analogous specifically to replacing the large trigonometric identity by reduction modulo \(Q_t,Q_s\), though its composition setting is otherwise different. `aimo-0635` — certifies a difficult global assertion by an explicit displayed decomposition into manifest pieces; analogous in proof-audit style, not geometry. The documentation confirms there are no extracted geometry crux records, so no closer schema-filtered geometry crux exists.
- Prior progress: Status is `partial`. Both sampled approaches are live but stale after round-1 `advanced` outcomes. `trig-sine-factorization` (Elo 1516) and `oblique-circle-linearization` (Elo 1484) have reviewer-certified branch control, ray reconstruction, closure equations, circle nonsingularity, second-intersection/oblique coefficient formulas, and midpoint-power reduction. Four certified lemmas are available. Their sole shared gap was the displayed derivation of \(F=0\); the quadratic certificate above appears to close exactly that gap.
- Dead ends (do not retry): Do not claim “exponential-polynomial/Gröbner computation shows ideal membership”; round 1 correctly rejected that as non-human-checkable. Do not expand directly in \(y,z\) and seek a huge factorization by the original residuals unless necessary. Do not use raw Cartesian angle equations, which obscure branch signs. Do not divide by \([K,L]\) without invoking nondegeneracy of \(AKL\), or by any sine/cosine without the obligations below.
- Small-case / intuition notes: **Exact-computation evidence, not yet a prose proof:** the boxed certificate was verified symbolically coefficient-by-coefficient after sine-angle expansion, and numerically at generic values. The key simplification is structural: each auxiliary angle occurs in only one midpoint equation and one closure, so it leaves behind an independent quadratic in its ray length. **Branch/denominator obligations for the builder:** \(0<x<\min(\beta,\gamma)\), \(0<y<\beta-x\), \(0<z<\gamma-x\); hence \(\sin x,\sin y,\sin z,\sin(x+y),\sin(x+z),\sin(\alpha+x)>0\). Also \(s,t>0\). Thus division by \(2t\sin x\), \(2s\sin x\), \(\sin y\), \(\sin z\), and the certificate factor \(2\sin(\alpha+x)\) is legal. If deriving quadratics without cotangents, multiply out first to avoid divisions. The Sine-Law denominators \(\sin(\alpha+2x+y)\), \(\sin(\alpha+2x+z)\) remain positive as angles of nondegenerate triangles. Finally \([K,L]\ne0\) follows because the stated circumcentre of triangle \(AKL\) presupposes a nondegenerate triangle; this is needed only in the circle-coefficient criterion, not in the polynomial certificate.
