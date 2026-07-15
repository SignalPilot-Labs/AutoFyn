## imo-2026-02
- Distinct openings:
  1. **The determinant implication is symbolically true, not refuted.** With the live normalization
     \(A=0\), \(B=1\), \(C=q(\cos\gamma,\sin\gamma)\), put
     \[
       r=\frac{\sin\delta}{2\sin(\alpha+\delta)},\qquad
       u=\frac{q\sin\beta}{2\sin(\alpha+\beta)},
     \]
     \[
       K=(1-r\cos\alpha,r\sin\alpha),\qquad
       L=q e_\gamma-u e_{\gamma+\alpha}.
     \]
     I recomputed the signed determinant residual
     \[
       R=2\bigl(|K|^2[C-B,L]+|L|^2[K,C-B]\bigr)-(q^2-1)[K,L].
     \]
     It is a rational trigonometric expression and, before imposing incidences, is generically nonzero. It is a polynomial of degree three in \(q\), with zero constant term. Thus the desired identity is not a tautology of the first two ray intersections; both remaining incidences really are load-bearing.

     Define
     \[
       F(t)=\frac{\cos\gamma-\cos t\cos(\gamma+2\alpha+t)}{2\sin^2(\alpha+t)}.
     \]
     Under the first incidence \(q=F(\delta)\), exact rational symbolic reduction gives
     \[
       R\big|_{q=F(\delta)}=\bigl(F(\delta)F(\beta)-1\bigr)\,Q(\alpha,\beta,\delta,\gamma),
       \tag{E}
     \]
     for a rational trigonometric function \(Q\). Consequently the second incidence \(q^{-1}=F(\beta)\) does force \(R=0\). This was checked as an exact polynomial divisibility, not numerically: I substituted
     \(x=\tan(\alpha/2),y=\tan(\beta/2),z=\tan(\delta/2),w=\tan(\gamma/2)\), cleared rational denominators, and SymPy factored the numerator of \(R|_{q=F(\delta)}\); its remaining large factor is exactly the numerator of \(F(\delta)F(\beta)-1\). Dividing the two rational expressions leaves zero remainder. This is computational evidence for an identity and a reliable discovery, not yet a human proof of (E).

  2. **A cleaner incidence formula may compress the quotient.** Expanding only the \(\gamma\)-dependence gives the exact elementary rewrite
     \[
       2F(t)=\left(1+\frac{\sin^2\alpha}{\sin^2(\alpha+t)}\right)\cos\gamma
       +\left(\cot(\alpha+t)+\frac{\sin^2\alpha}{\sin^2(\alpha+t)}\cot\alpha\right)\sin\gamma.
       \tag{L}
     \]
     This follows from
     \(1-\cos t\cos(2\alpha+t)=\sin^2(\alpha+t)+\sin^2\alpha\) and
     \(\cos t\sin(2\alpha+t)=\tfrac12(\sin2(\alpha+t)+\sin2\alpha)\).
     Formula (L) makes each incidence linear in \((\cos\gamma,\sin\gamma)\), unlike the original compressed \(F\). It is the best opening found for turning the CAS divisibility into a short hand identity: use the two linear forms rather than expand all shifted trigonometric functions.

  3. **Polynomial-division certificate rather than an alleged telescoping.** Since \(R=q(P_2q^2+P_1q+P_0)\), one can always separate it algebraically as
     \[
       R=(q-F(\delta))S+R|_{q=F(\delta)}.
     \]
     The exact divisibility (E) then separates the two genuine incidence residuals. This validates the conceptual claim in the live coordinate approach, but the raw half-angle quotient is far too large for olympiad prose: its unfactored final factor has hundreds of monomials. Therefore “product-to-sum and terms pair” is not presently credible without first discovering a better choice of auxiliary variables, likely those in (L), or a geometrically meaningful factorization of \(Q\).

  4. **Reparameterize by midpoint-ray ratios.** Let
     \(p_t=\sin\alpha/\sin(\alpha+t)\). Then (L) reads
     \(2F(t)=(1+p_t^2)\cos\gamma+(\cot(\alpha+t)+p_t^2\cot\alpha)\sin\gamma\).
     The already-used ray length also satisfies
     \(2r_t=\sin t/\sin(\alpha+t)=\cos\alpha-p_t\cos(\alpha+t)/\sin\alpha\).
     Thus the same variables control both the coordinates of \(K,L\) and the two incidence equations. This is a distinct algebraic opening from tangent-half-angle expansion and looks more likely to reveal a quadratic-form or determinant cancellation.

- Candidate technique(s): Oriented Cartesian/complex coordinates; two-dimensional determinant elimination; exact polynomial remainder/divisibility after a substitution; linearization in \((\cos\gamma,\sin\gamma)\); strategically chosen sine-ratio variables. CAS should be used only to discover the identity or check a proposed certificate; the final proof still needs a displayed hand-verifiable factorization.

- Cheap-kill candidates: First record that \(R\) has degree three in \(q\) and factor \(q\), so coefficient comparison is finite. Substitute only \(q=F(\delta)\) before expanding; then target divisibility by \(F(\delta)F(\beta)-1\), rather than trying simultaneously to express \(R\) as an arbitrary combination of two residuals. Replace shifted cosines in \(F\) by the linear form (L) before any full expansion. Keep \(\sin(\alpha+\beta)\) and \(\sin(\alpha+\delta)\) factored and positive from interiority; do not clear them prematurely. No parity, pigeonhole, or size argument applies.

- Knowledge-base entries to use: **Coordinates / complex / barycentric** (the normalization and circle coefficient system); **Resultants / “transform the roots”** (the exact identity/divisibility viewpoint: reduce a target modulo the incidence relations); **Minimal-polynomial reduction** (reduce the cubic residual in \(q\) using the two scalar relations rather than expanding unrestricted powers); **Trig identities & interval intersection** (product-to-sum plus branch/interiority control); **Introduce a substitution / change of variables** (sine-ratio variables or tangent-half-angle variables); **Reformulate** (distance equality to a determinant residual); **Check the answer** (exact and numerical substitution checks).

- Analogous past problems (cruxes): none genuinely analogous. The required corpus query was performed after reading `crux_moves_documentation.md`: it contains zero records with `domain="geometry"`, as the documentation warns. I also filtered `domain="algebra"`, `subtopic="polynomial-roots-and-factoring"` for factorization/remainder/divisibility moves. Entries such as `aimo-0949` (composition remainder/minimal degree), `aimo-0853` (polynomial divisibility plus degree), and `aimo-0011` (factor identity and coefficient matching) use abstract polynomial divisibility but do not resemble this two-incidence trigonometric determinant closely enough to recommend as geometric analogues.

- Prior progress: The problem is `geometry`, `proof_only`, answer type `none`, and remains `partial`. The sampled population consists of all four current slugs. `oriented-determinant-elimination` has the certified target residual but lacked its factorization; `antipode-quarter-turn` reaches the same algebra without a telescoping certificate; `sine-product-antipode` leaves an extra angular factor; `inverted-circle-intercepts` is unbuilt and lacks its nonlinear intercept lemma. No files exist in `results/imo-2026-02/lemmas/`. Round 2 reconnaissance advances the determinant line computationally: the missing implication is true as an exact rational identity after the two stated incidence equations, but no concise human factorization has yet been found.

- Dead ends (do not retry): Do not retry the false assertion that \(B,C,K,L\) are cyclic; the round-1 numerical counterexample and reviewer warning stand. Do not call the raw coordinate expansion “telescoping”: the half-angle certificate explodes to hundreds of monomials. Do not use only one incidence equation: exact symbolic substitution \(q=F(\delta)\) leaves the nonzero factor \(F(\delta)F(\beta)-1\). Do not present CAS factorization as the proof. Do not divide by \([K,L]\), sine denominators, quarter-turn parameters, or auxiliary factors without the interiority/nondegeneracy arguments requested by the reviewer. Direct tangent-half-angle expansion in all four angles is a discovery tool, not a viable final exposition.

- Small-case / intuition notes: **Exact computational evidence, not a proof:** the residual vanishes identically in the rational function field after imposing both incidence relations via (E), so the live determinant approach is algebraically sound rather than based only on floating-point samples. **Generic diagnostic:** before incidences, the coefficient of \(q^2\) in the cubic residual contains the factor
  \[
    \bigl(4\sin(\alpha+\beta)\sin(\alpha+\delta)-\sin\beta\sin\delta\bigr)
    \bigl(\sin\delta\sin(\alpha+\beta)-\sin\beta\sin(\alpha+\delta)\bigr)\sin\alpha,
  \]
  up to the positive denominator \(4\sin^2(\alpha+\beta)\sin^2(\alpha+\delta)\). This shows visible low-complexity structure survives before full expansion and supports searching in sine-ratio variables. **Conjecture:** the huge quotient \(Q\) in (E) should admit a short geometric/trigonometric interpretation after the linearization (L); no such interpretation is proved yet.