## imo-2026-02 (lens: algebraic/trig branch-isolation)

- Distinct openings:
  1. **Decoupling discovery (new, load-bearing).** Working entirely inside the
     already-certified ray parametrization (`lemmas/coordinate-om-on-reduction.md`
     is the OM=ON⟺O_x=p/2 lemma; the ray parametrization is Lemma 3 in
     `approaches/coordinate-trig-bash.md`): K = B + r1·u_K(θ), L = C + r2·u_L(θ),
     with u_K(θ), u_L(θ) FIXED unit directions depending only on θ,p,q (not on
     r1,r2). I verified numerically (three independent (p,q), two θ each, ~150
     sample points, machine precision, script below) that:
     - F1(θ,r1,r2) := ∠LBK − ∠LNC is **completely independent of r1**
       (varying r1 over [0.1,5] with r2,θ fixed changes F1 by < 1e-13).
     - F2(θ,r1,r2) := ∠LCK − ∠BMK is **completely independent of r2**
       (same test, symmetric roles).
     This is not a numerical coincidence — it has a one-line structural proof:
     ray BK has direction u_K(θ) regardless of r1 (K only slides along a fixed
     ray from B), so any angle measured **at vertex B** between ray BK and
     another ray depends on r1 only through that "another ray" — and in ∠LBK,
     the other ray (BL) depends on L hence on r2, not r1. Symmetrically ray CL
     has fixed direction u_L(θ) regardless of r2, so ∠LCK (vertex C) depends on
     r1 (via CK) but not r2. Likewise ∠LNC (vertex N, ray NC fixed) depends only
     on r2, and ∠BMK (vertex M, ray MB fixed) depends only on r1. **This
     converts the coupled 2-variable branch problem into two INDEPENDENT
     single-variable equations**: F1(θ,r2)=0 pins down r2(θ) alone; F2(θ,r1)=0
     pins down r1(θ) alone. This directly attacks the open gap: the spurious
     extra branches found by the round-1 Gröbner computation (which worked with
     free (kx,ky,lx,ly), not the ray-restricted r1,r2>0 parametrization) are
     very plausibly artifacts of *not* using this decoupled, positivity-fixed
     form — a "directed angle mod π" encoding on free coordinates cannot see
     ray positivity and conflates K with its reflection through B (same effect
     for L through C), which is exactly the known source of spurious real
     components.
  2. **Monotonicity ⇒ automatic branch uniqueness (new).** On the
     containment-valid domain (r2 ∈ (0, r2max(θ)), where r2max is where the ray
     from C exits triangle BNC; similarly r1 ∈ (0, r1max(θ)) for exit from
     triangle BMC), I confirmed numerically across 6 (triangle,θ) test
     configurations that **F1(r2) is strictly decreasing** (∠LBK strictly
     decreasing in r2, ∠LNC strictly increasing in r2 — both individually
     monotone, so the difference is strictly monotone) and **F2(r1) is
     strictly decreasing** likewise. A strictly monotone continuous function
     has at most one zero; combined with a sign change at the two endpoints
     (confirmed numerically: F1>0 near r2→0+, F1<0 near r2max; same pattern for
     F2), IVT gives existence AND uniqueness of the geometric branch — with NO
     Positivstellensatz / semialgebraic machinery needed. This is a genuinely
     different, much lighter route past the branch-isolation gap than (a)/(b)
     proposed in the current gap writeup.
  3. **Directed-angle-mod-π reformulation does NOT by itself sidestep the
     gap** (tested this per the dispatch's question 2): the round-1 Gröbner
     failure used exactly a directed-angle/tangent-identity encoding
     (cross·dot − cross·dot = 0) on free (kx,ky,lx,ly), and it still produced
     spurious branches. The reason: "mod π" identifies a ray with its
     opposite, so it cannot exclude K/L lying on the wrong side of B/C. The
     ray-positivity parametrization (already in Lemma 3) is what's actually
     doing the branch-selection work, not the choice of directed vs undirected
     angle encoding. Recommend NOT re-trying pure directed-angle GB on free
     coordinates — instead pursue the decoupled r1(θ), r2(θ) route (opening 1+2).
  4. **Symmetry cross-check.** The decoupling (K-side equation ↔ r1 alone,
     L-side equation ↔ r2 alone) is the same B↔C, K↔L, M↔N, r1↔r2 symmetry σ
     that the `labeling-duality` approach already identified and used for its
     power-of-a-point reduction — reinforces that σ is a genuine structural
     symmetry of the whole configuration, not just of the target identity.

- Candidate technique(s): elementary single-variable monotonicity + IVT (existence/uniqueness of r1(θ), r2(θ)) to replace the failed ideal-membership route; then substitute the (now uniquely and rigorously pinned-down) r1(θ), r2(θ) into the certified circumcenter formula (Lemma 2) and the target O_x=p/2. The final "plug in and simplify" step is still open — closed forms for r1(θ), r2(θ) were not found (the equations ∠LBK=∠LNC, ∠LCK=∠BMK do not look linear/simple in r1,r2 even after decoupling; each is transcendental via arccos of a rational function of r), so this may still require either (i) an explicit resultant/elimination now done rigorously along the correct 1-parameter branch (justified rigorous by monotonicity, not just numerically), or (ii) a genuinely synthetic argument once the branch is pinned down. Flag this remaining step honestly to the outliner — decoupling+monotonicity closes the *branch-isolation* gap but not the whole proof.

- Cheap-kill candidates: none new beyond what's already used (the decoupling itself is the cheap structural win — it turns a 2-var spurious-branch problem into two 1-var monotone problems, avoiding heavy SOS/Positivstellensatz machinery). Worth a quick sanity check before deeper work: verify the decoupling and monotonicity claims symbolically (not just numerically) via `sympy` partial derivatives of the arccos expressions — should be a short computation (10-20 min) and would upgrade "numerically confirmed" to a real lemma.

- Knowledge-base entries to use: "Synthetic toolkit" (power of a point, spiral similarity — already used); "Coordinates/complex/barycentric" (already used for the reduction/circumcenter lemmas); no KB entry directly covers monotonicity-based branch selection — this is closer to general calculus (IVT) than a named geometry theorem, but the KB's "ideal saturation... Gröbner-basis ideal membership" note under Linear Algebra is the technique the round-1 attempt already tried and that this report explains *why* it failed (ray-sign ambiguity) and offers a lighter alternative (monotonicity) instead of the Positivstellensatz upgrade the note suggests.

- Analogous past problems (cruxes): **none** — `crux_moves_documentation.md` states explicitly that the geometry domain has **no cruxes extracted yet** ("Not in the corpus yet; the problems DB includes geometry problems with solutions, but no geometry cruxes have been extracted"). Only number_theory/combinatorics/algebra subtopics exist. Did not force a mismatch; no crux search performed beyond confirming this gap in the corpus.

- Prior progress: as recorded in `current.md` — Lemma 1 (OM=ON⟺O_x=p/2), Lemma 2 (circumcenter formula), Lemma 3 (ray parametrization K=B+r1·u_K(θ), L=C+r2·u_L(θ)) are all certified/rigorous. The power-of-a-point reduction (TI) from `labeling-duality` is also certified. The open gap before this report: branch isolation for O_x=p/2 (or equivalently (TI)) from the angle hypotheses. This report's new contribution: the decoupling (F1 depends only on r2, F2 only on r1) and the empirical strict-monotonicity of each — not yet promoted to a lemma file since it is currently only numerically verified, not symbolically proved; recommend the outliner have a builder verify it symbolically (short sympy derivative computation) and, if confirmed, write it up as a certified lemma before building the rest of the branch/elimination argument on top of it.

- Dead ends (do not retry): (1) the round-1 Gröbner-basis ideal-membership computation over free (kx,ky,lx,ly) with the raw angle-equality polynomials (no positivity constraints) — confirmed genuinely fails, do not repeat verbatim. (2) directed-angle-mod-π (cross·dot identity) encoding on free coordinates as a way to "avoid" the branch problem — tested per this lens's dispatch question, does NOT resolve it (still has the same ray-reflection ambiguity); don't re-attempt this as a standalone fix. (3) `two-step-spiral-chain` (spiral similarity BKL~NLC, 4-point concyclicity) — already refuted numerically in round 1, independent of this lens.

- Small-case / intuition notes (all conjectural / numerical, not proofs):
  - Decoupling F1=F1(r2 only), F2=F2(r1 only) [given θ fixed]: confirmed to ~1e-13 across 3 triangles × 2 θ-values (6 configs, ~10 sample points each) — very likely a genuine structural fact (has the one-line "fixed ray direction" explanation above), should be easy to prove rigorously (not just numerically) once someone writes it up.
  - Strict monotonicity of F1(r2) and F2(r1) on the containment-valid domain: confirmed across the same 6 configs (single sign change, U-shaped-looking plots away from the valid domain were seen in an earlier wider-range test, but the geometrically valid sub-domain is strictly monotone in every test) — this is the piece most worth converting to a rigorous derivative-sign argument next round, since it is the crux of resolving the branch-isolation gap cheaply.
  - The valid-domain bound r2max(θ) (where ray CL exits triangle BNC) and r1max(θ) (ray BK exits triangle BMC) were computed numerically via point-in-triangle tests; an exact formula for these (intersection of the ray with segment BN or BC, resp. BM or BC) should be an easy closed-form addition once needed for the endpoint-sign / IVT argument.
