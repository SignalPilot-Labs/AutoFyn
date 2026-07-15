## imo-2026-02
- **Problem metadata:** Domain `geometry`; task `proof_only`; answer type `none`. The workspace is absent and the run state marks the problem unsolved.

- **Distinct openings:**
  1. **Three-angle trigonometric parameterization.** Normalize by a direct similarity
     \[
     A=0,\qquad B=1,\qquad C=q(\cos\gamma,\sin\gamma),\quad q=AC/AB>0,
     \]
     and introduce the three positive angles
     \[
     \alpha=\angle KBA=\angle ACL,
     \quad \beta=\angle LBK=\angle LNC,
     \quad \delta=\angle LCK=\angle BMK.
     \]
     The inside assumptions select the ray orientations unambiguously. Writing
     \(e_\theta=(\cos\theta,\sin\theta)\), the two points have the exact forms
     \[
     K=B-r e_{-\alpha},\qquad
     r=\frac{\sin\delta}{2\sin(\alpha+\delta)},
     \]
     \[
     L=C-u e_{\gamma+\alpha},\qquad
     u=\frac{q\sin\beta}{2\sin(\alpha+\beta)}.
     \]
     These formulas come just from intersecting the relevant rays with the midpoint rays. The remaining ray incidences are equivalent to the two scalar equations
     \[
     q=F(\delta),\qquad q^{-1}=F(\beta),
     \]
     where
     \[
     F(t)=\frac{\cos\gamma-\cos t\cos(\gamma+2\alpha+t)}{2\sin ^2(\alpha+t)}.
     \tag{T}
     \]
     An equivalent unsimplified form, often easier for sine-rule derivations, is
     \[
     \sin(\gamma+\alpha+t)-
     \frac{\sin t}{2\sin(\alpha+t)}\sin(\gamma+2\alpha+t)
     =F(t)\sin(\alpha+t).
     \]
     The compact numerator in (T) follows from the exact identity
     \[
     2\sin(\alpha+t)\sin(\gamma+\alpha+t)
     -\sin t\sin(\gamma+2\alpha+t)
     =\cos\gamma-\cos t\cos(\gamma+2\alpha+t).
     \]
     Thus the entire configuration is encoded by \((\alpha,\beta,\delta,\gamma,q)\) and two short trigonometric equations. This is the strongest analytic opening found.

  2. **Vector/determinant reduction of the conclusion.** With the same normalization,
     \(M=B/2\) and \(N=C/2\). If \(O\) is the circumcenter of \(0,K,L\), then
     \[
     2O\cdot K=|K|^2,\qquad 2O\cdot L=|L|^2.
     \]
     More importantly, the desired quadratic-looking equality is actually the linear condition
     \[
     OM=ON
     \iff O\cdot(C-B)=\frac{q^2-1}{4}.
     \tag{V}
     \]
     For the planar cross product \([X,Y]=X_xY_y-X_yY_x\), eliminating \(O\) converts (V) into the explicit identity
     \[
     2\bigl(|K|^2[C-B,L]+|L|^2[K,C-B]\bigr)
       =(q^2-1)[K,L].
     \tag{D}
     \]
     Here
     \[
     |K|^2=1-2r\cos\alpha+r^2,
     \qquad |L|^2=q^2-2qu\cos\alpha+u^2,
     \]
     with \(r,u\) as above. Formula (D), together with (T), is a finite trigonometric identity target; it is suitable either for hand factorization or a CAS-guided factorization into the two incidence relations. No claim is made here that the factorization has already been completed.

  3. **Circle-coefficient coordinates.** Since the circumcircle passes through \(A=0\), write it as
     \[
     X\cdot X-U X_x-V X_y=0.
     \]
     Then \(O=(U/2,V/2)\), while passage through \(K,L\) gives the linear system
     \(U K_x+V K_y=|K|^2\), \(U L_x+V L_y=|L|^2\). The target becomes
     \[
     U(q\cos\gamma-1)+Vq\sin\gamma=\frac{q^2-1}{2}.
     \]
     This is the same determinant identity as (D), but its algebra may be cleaner because no circumcenter coordinates need be displayed.

  4. **Complex-number formulation.** Put \(a=0,b=1,c=qe^{i\gamma}\). The complete oriented-ray data are
     \[
     k=1-r e^{-i\alpha}=\frac12+s e^{i\delta}
       =qe^{i\gamma}-w e^{i(\gamma+\alpha+\delta)},
     \]
     \[
     l=qe^{i\gamma}-u e^{i(\gamma+\alpha)}
       =1-v e^{-i(\alpha+\beta)}
       =\frac q2e^{i\gamma}+h e^{i(\gamma-\beta)},
     \]
     for positive real \(r,s,w,u,v,h\). Eliminating the positive lengths gives (T). If the circle through \(0,k,l\) has center \(o\), its equation is
     \[
     |z|^2=2\operatorname{Re}(\bar o z),
     \]
     and the target is simply
     \[
     \operatorname{Re}(\bar o(c-b))=(q^2-1)/4.
     \]
     This formulation retains angle orientation automatically and may expose conjugate cancellations obscured by Cartesian expansion.

  5. **Isosceles diagnostic.** For \(q=1\), the two incidence equations become \(F(\beta)=F(\delta)=1\). Numerical experiments in the admissible interval suggest the relevant root is unique, hence \(\beta=\delta\); the configuration then appears reflection-symmetric across the angle bisector of \(A\), making the conclusion natural. This is only intuition: global injectivity of \(F\) has not been checked and should not be assumed in the general case.

- **Candidate technique(s):** Normalize by similarity; oriented trigonometric coordinates; sine rule in the small triangles at the midpoints; complex rays; circumcircle equation through the origin; two-dimensional determinant elimination. A CAS could be used only to discover/factor the residual identity after tangent-half-angle substitution, with any resulting identity subsequently checked algebraically from scratch.

- **Cheap-kill candidates:**
  - Linearize \(OM=ON\) immediately as (V); do not expand two distances or compute \(O\) by perpendicular bisectors.
  - Scale to \(AB=1\) and encode \(AC=q\), reducing the base triangle to two parameters \((q,\gamma)\).
  - Use \(A=0\), so the circumcircle has no constant term and its center is obtained from a 2-by-2 linear system.
  - Use the three given repeated angles as \(\alpha,\beta,\delta\); all six relevant ray directions then become explicit. Positivity/interiority should be retained to avoid supplementary-angle branches.
  - No parity, pigeonhole, or size obstruction is relevant.

- **Knowledge-base entries to use:**
  - `Coordinates / complex / barycentric`: place coordinates to exploit the midpoint structure and normalize by similarity.
  - `Trig identities & interval intersection`: the angle incidences reduce to exact scalar trigonometric identities; interval/interiority information controls branches.
  - `Circle/triangle configuration facts`: principally elementary circumcircle equations and potentially the sine rule in the ray-intersection triangles.
  - `Synthetic toolkit`: angle chasing and similar triangles/sine-rule computations are candidates for deriving the coordinate formulas without hidden orientation assumptions.
  - `Reformulate` and `Introduce a substitution / change of variables`: geometry-to-algebra translation and, if needed, tangent-half-angle variables.
  - `Solve a simpler / special case first` and `Check the answer`: the \(q=1\) reflection case and numerical checks are useful diagnostics.
  - `Resultants / transform the roots` is a possible fallback if the tangent-half-angle equations are polynomialized and the target polynomial must be shown to lie in their ideal, though this looks heavier than necessary.

- **Analogous past problems (cruxes):** None. `crux_moves_documentation.md` states that the extracted crux corpus covers only number theory, combinatorics, and algebra; geometry has no extracted cruxes yet. Filtering by the required `domain` field therefore yields no geometry candidates, and forcing an algebra crux match would be misleading. The full past-problems database may contain geometry solutions, but it is not a documented geometry-crux index.

- **Prior progress:** None. The target workspace `results/imo-2026-02/` is absent, and no approaches or certified lemmas exist.

- **Dead ends (do not retry):** No prior approaches exist. Potential analytic pitfalls discovered during probing:
  - Unsigned `acos` angle equations introduce spurious supplementary branches. Use oriented rays plus positivity/interiority.
  - Directly solving for both Cartesian coordinates of \(O\) creates avoidable algebra; (V), (D), or the circle-coefficient form is substantially shorter.
  - Do not infer \(\beta=\delta\) outside the special case \(q=1\); generic numerical samples have unequal values.

- **Small-case / intuition notes:**
  - **Reproducible numerical evidence, not proof.** Solving (T) and reconstructing \(K,L,O\) produced the following samples; the last entry is \(OM-ON\):
    \[
    (q,\gamma,\alpha;\delta,\beta;OM-ON)
    \]
    \[
    (1.2,0.8,0.12;0.3852769941,0.6325565507;5.6\cdot10^{-17}),
    \]
    \[
    (1.5,1.1,0.20;0.2884535110,0.7773319338;2.2\cdot10^{-16}),
    \]
    \[
    (0.9,1.4,0.10;0.5323376937,0.4337492219;1.1\cdot10^{-16}),
    \]
    \[
    (1.8,0.65,0.08;0.1998812715,1.0955836871;1.0\cdot10^{-14}).
    \]
    The reconstruction used
    \[
    K=(1-r\cos\alpha,r\sin\alpha),
    \quad L=q e_\gamma-u e_{\gamma+\alpha},
    \]
    then solved \(2O\cdot K=|K|^2\), \(2O\cdot L=|L|^2\). Barycentric coordinates were checked positive in triangles \(BMC\) and \(BNC\).
  - For one concrete base triangle \(B=(1,0), C=(0.65,1.35)\), setting \(\alpha=0.1\) yielded approximately
    \(\delta=0.3224112909\), \(K=(0.61548588,0.03858010)\),
    \(L=(0.41637377,0.70743252)\), and
    \(O=(0.28979094,0.30568654)\), with \(OM-ON\approx-5.6\cdot10^{-14}\).
  - **Conjectural algebraic shape:** after substituting \(r,u\) into (D), its difference from zero should factor or reduce using exactly the two relations \(q-F(\delta)=0\) and \(q^{-1}-F(\beta)=0\). This has strong numerical support but has not been symbolically certified in this reconnaissance.
