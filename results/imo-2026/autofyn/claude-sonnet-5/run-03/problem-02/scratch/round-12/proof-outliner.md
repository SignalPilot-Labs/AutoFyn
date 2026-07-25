## imo-2026-02

coordinate-bash-resultant-boundary: advance
Target: OM=ON for the full family of valid (K,L) — reduces (via the certified central identity + branch-selection machinery + Case-(b) reduction) to the residual claim `q1(σ,τ)<0 ∧ r0(σ,τ)<0` on the true (transcendentally-defined) restricted sub-domain `Case-(b) ∧ P>0 ∧ E<0`.
Technique: resultant/Weierstrass elimination + this round's new β1-elimination (q1r0lens) turning the transcendental domain description into a purely algebraic one, then direct sign/positivity analysis (Gröbner/resultant, or interval bounding on the now-narrow (A,B) window).
Skeleton:
  1. Import certified facts unchanged: central identity (symbolic-genericity-certificate.md), Case-(b) P≤0/E≥0 branches closed (case-b-p-le-0-and-e-ge-0-closed.md), T-factorization T=c(dQ1−cR0)/(4sin²(A+B)) (case-b-e-lt-0-t-factorization.md), and round 11's numeric finding q1<0∧r0<0 individually on the restricted sub-domain.
  2. Splice in q1r0lens's Steps 1–5 verbatim as the new symbolic reduction of the domain description:
     (a) exact trig identity sin(A+3β1) = s(4X0−3)x + c(4X0−1)y with x=√X0,y=√(1−X0) (derivation via cos3β1,sin3β1 triple-angle formulas + x²→X0,y²→1−X0 substitution — an exact algebraic identity, not numeric, since it only uses x,y≥0).
     (b) On the true sub-domain, γ=min(B,C)=B identically (needs: C≫B always there) — prove this directly from the already-pinned window A∈(0.407,0.537), B∈(0.912,1.091) (so C=π−A−B∈(1.51,1.82)) via an explicit inequality argument (e.g. show B<(π−A)/2 follows from the certified E<0/Case-(b) constraints), not just cite the numeric window.
     (c) β1<γ=B ⟺ X0>d² (d=cosB) via cos-monotonicity on (0,π/2), valid since x,d≥0 (d>0 already certified this sub-domain).
     (d) GIVEN sign facts p:=s(4X0−3)<0, q:=c(4X0−1)>0 (i.e. X0∈(1/4,3/4)) — the new Step 4 target — squaring px+qy<0 (both sides same-signed after negation) gives the fully rational equivalence sin(A+3β1)<0 ⟺ X0 > q²/(p²+q²).
  3. Prove Step 4 (X0∈(1/4,3/4) on {X0>d²}∩{E<0}) via resultant/Gröbner elimination of the remaining c,s,d,t (mod c²+s²=1, d²+t²=1) — X0, d, E are all explicit rational functions of these, so this is a concrete elimination-ideal computation of the same style as the certified T-factorization.
  4. With the domain now fully polynomial (X0>d² and X0>q²/(p²+q²), no arccos/β1 anywhere), re-attempt q1<0, r0<0 as a semialgebraic positivity claim in (σ,τ) directly — likely via Sturm-sequence/sign-variation counting on univariate slices (fix A, since the sub-domain is narrow in A) or a further resultant elimination reusing the T-factorization machinery.
  5. Conclude: Case-(b)∧E<0 residual T≥0, completing Case (b), completing branch selection, completing OM=ON.
Key lemmas (claim + mechanism):
  - sin(A+3β1)=s(4X0−3)x+c(4X0−1)y — because triple-angle cos/sin formulas plus the licit substitution x²→X0 (x=√X0≥0 by construction).
  - β1<B ⟺ X0>d² — because cos is strictly decreasing on (0,π/2) and both cosβ1=x, cosB=d are ≥0 there.
  - sin(A+3β1)<0 ⟺ X0>q²/(p²+q²) — because once p<0,q>0 are known, qy<|p|x has both sides ≥0, so squaring is a valid iff.
Open gaps: Step 4 (X0∈(1/4,3/4) on the residual locus) — unproved, now purely algebraic; γ=B identically on the sub-domain — needs an explicit inequality proof, not just the numeric window; the final q1<0,r0<0 on the resulting polynomial domain.
Cases to cover: none beyond the existing P≤0/E≥0/E<0 case split (already closed for the first two).
Watch out for: do not silently assume γ=B without proving C>B on the sub-domain first (this was exactly the kind of missing-hypothesis bug that made round-9's Case (b) statement false as literally written — round 10's correction). Keep the squaring steps' validity conditions (signs of x,y,d,p,q) explicit at every iff.

coordinate-bash-resultant-boundary-pointwise: advance (dormant, no build slot)
Target: same overall OM=ON; this approach's own remaining content is the single inequality (⋆): (1+cosB)²X0 ≥ RHS², covering the ENTIRE Case (b) domain (strictly larger than the sibling's E<0 residual above).
Technique: MVT/Lipschitz reduction (already fully certified, mvt-lipschitz-reduction-case-b.md) — no new lever this round.
Skeleton: (unchanged from round 10/11 — see file) reduces Case (b) to (⋆); (⋆)'s proof is now being pursued by its two forks below.
Key lemmas: mvt-lipschitz-reduction-case-b.md (certified), x0-partial-b-derivative.md (certified).
Open gaps: (⋆) itself — being attacked by -tangent and -sos forks, not by this parent file directly this round.
Cases to cover: none additional.
Watch out for: per round-9 rule, do not dispatch a build slot here directly since its content is fully inherited by the two children below — record any cross-pollination result from them back into this file instead.

coordinate-bash-resultant-boundary-pointwise-tangent: advance
Target: same OM=ON; specifically proves (⋆) via a monotonicity-in-B reduction.
Technique: prove ∂S/∂B≥0 on the Case-(b) domain D (S=(1+cosB)²X0−RHS²), which reduces (⋆) to checking it only on the lower boundary curve X0(A,B)=cos²B — then close that 1-parameter residual.
Skeleton:
  1. Rationalize the whole derivative computation via u=tan(A/6) BEFORE attempting sympy.simplify (starlens's tractability fix — blind trig simplification times out; algebraizing first is the standard Weierstrass move already used successfully elsewhere in this population, e.g. the -sos file's own u=tan(A/6) substitution).
  2. Decompose ∂S/∂B using the already-certified sign fact ∂X0/∂B = sinA cosA/(2sin²(A+B)) > 0 (lemmas/x0-partial-b-derivative.md) as one clean positive piece: ∂S/∂B = 2(1+cosB)[½(1+cosB)∂_BX0 − sinB·X0] − 2·RHS·∂_B RHS. Bound ∂_B RHS explicitly (its own closed form is already in the -tangent file) rather than attempting one monolithic simplify.
  3. Prove the resulting single polynomial-in-u,cosB,sinB inequality is sign-definite on D (starlens's numerics: margin ≈0.178–0.19 throughout, never knife-edge — strong evidence a clean algebraic proof exists, not just a numeric coincidence).
  4. Given ∂S/∂B≥0, reduce (⋆) to S(A,β0(A))≥0-style boundary check along the curve X0=cos²B (the true lower boundary, per round 11's two-curve finding) — a genuinely 1-parameter-in-A residual claim.
  5. Close the residual boundary-curve inequality (own sub-target; if it resists direct proof, fall back to the two-point-pinned construction in the sibling copy below).
Key lemmas (claim + mechanism):
  - ∂X0/∂B>0 (already certified) — reused as the load-bearing positive piece of the decomposition.
  - ∂S/∂B≥0 on D — because (per numerics) the two terms above combine with comfortable margin, not a cancellation; the u=tan(A/6) rationalization should expose why algebraically (e.g. as a sum of manifestly nonnegative terms or a single-sign quadratic in u).
Open gaps: the full ∂S/∂B≥0 symbolic proof (Step 3), and the boundary-curve residual (Step 5) — both currently numeric-only.
Cases to cover: none beyond D's existing two-curve boundary structure (already characterized, round 11).
Watch out for: do not re-attempt the literal single-point tangent-line-in-A construction pinned only at the corner — round 11 showed it fails to eliminate B (dead end, do not retry verbatim); this route is the DERIVATIVE-SIGN mechanism, not the tangent-line-bound mechanism (kept as a separate copy below).

coordinate-bash-resultant-boundary-pointwise-tangent-twopoint: copy-of coordinate-bash-resultant-boundary-pointwise-tangent
Target: same (⋆) inequality, via a genuinely different mechanism than the ∂S/∂B route above — both are worth running in parallel per CLAUDE.md's copy rule (two viable levers on the same gap).
Technique: two-point-pinned tangent/secant construction, adapted from crux aimo-0005's move ("bound a nonlinear term by the tangent line at the equality point, chosen so it also passes through the value at a second boundary point, then verify by factoring the difference") — extended here to 2 variables by forcing a linear-in-A bound through BOTH the corner (A*,B*) AND a second point on the true boundary curve X0(A,B)=cos²B.
Skeleton:
  1. Recall why the single-point tangent (pinned only at the corner) failed: substituting into RHS left B un-eliminated (round 11, -tangent file) — the missing constraint was under-determination (1 pinned point, 2 unknowns in the linear ansatz).
  2. Construct a linear-in-A bound ℓ(A) for the relevant nonlinear piece of S restricted to the boundary curve X0=cos²B, pinned at TWO points: the corner (A*,B*) (where S=0, per round 11) and a second explicit point on the curve X0=cos²B away from the corner (e.g. at a convenient A-value where the curve has a closed-form B, or at a limiting/degenerate value where S's boundary restriction simplifies).
  3. Verify S−ℓ(A)·(appropriate positive weight) ≥0 by factoring the difference (per aimo-0005's verification method), exploiting that both pinning points are exact zeros/knowns of the difference.
  4. If the two-point line does not by itself close the whole curve, use it only on a sub-range near the corner (where round 11's data shows the tightest margins) combined with a cruder bound elsewhere (the ∂S/∂B route's comfortable margin, ~0.178+, away from the corner) — i.e. treat the two mechanisms as complementary, not exclusive.
Key lemmas (claim + mechanism):
  - S=0 exactly at the corner (A*,B*) — because this is the certified domain-boundary cusp point (star-corner-is-boundary-cusp-not-critical-point.md), the natural first pinning point.
  - A second exact evaluation point on X0=cos²B exists in closed form — needs construction (not yet done); if the curve has no closed form globally, use a degenerate/limiting sub-case of it as the second pin.
Open gaps: the whole two-point construction is untried — this is exploratory scaffolding, not a near-complete proof; may fail exactly as the one-point version did if the curve genuinely has no usable second closed-form point.
Cases to cover: near-corner sub-range vs. away-from-corner sub-range (per Step 4's complementary-bound idea), if the single two-point line does not cover the whole curve.
Watch out for: do not conflate this with the retired single-point tangent (explicitly a different, untried lever per starlens); if this also fails to eliminate B, record precisely why (dimension-count / missing second closed form) rather than silently abandoning without diagnosis.

coordinate-bash-resultant-boundary-pointwise-sos: advance
Target: same (⋆) inequality, via a constrained Positivstellensatz/SOS certificate on the domain-restricted numerator.
Technique: since cvxpy is not installed and unavailable this round, pursue a HAND (non-SDP-solver) Positivstellensatz search: express Num (degree-34 in u, over ℚ(√3)[u,cosB,sinB]) as a combination of n1≥0 (deg 10), n2≥0 (deg 6), and sum-of-squares terms, with small-integer/rational multiplier ansätze checked by direct polynomial division/sympy, rather than a numerical SDP solve.
Skeleton:
  1. Retrieve the fully-specified objects from round 11 (Num, n1, n2 — no re-derivation needed, per starlens's note).
  2. Try low-degree ansätze first: Num − λ1·n1·(square) − λ2·n2·(square) − (SOS remainder), starting with λ1,λ2 as low-degree polynomials (degree ≤ deg(Num)−deg(ni)) with a handful of unknown rational coefficients, solved by matching coefficients (a linear system, not an SDP) — check feasibility via sympy.solve on the coefficient-matching equations for small ansatz degrees before escalating.
  3. If a pure hand ansatz doesn't close it directly, try a WEAKER but sufficient decomposition: Num = n1·A(u) + n2·B(u) + C(u) with C(u) itself SOS or manifestly nonnegative on a smaller remaining sub-range, using the already-known numeric fact (round 11) that Num is negative only OUTSIDE the true domain, to guess which of n1,n2 needs the higher-degree multiplier.
  4. As a fallback if hand search stalls, note (for a future round) that installing cvxpy/an SDP solver (network available) would let a proper Positivstellensatz search run mechanically — flag this explicitly as an alternative next step if the hand search in this round is inconclusive, rather than silently declaring the route dead.
Key lemmas (claim + mechanism):
  - Num, n1, n2 are already exactly specified (round 11, certified) — reused verbatim, no re-derivation.
  - A Positivstellensatz certificate Num = Σ λi·(monomial in n1,n2)·(SOS) exists in principle by general theory (compact/regular enough semialgebraic set) — but existence in theory does not give a low-degree constructive certificate; this is exploratory, not a claimed result.
Open gaps: the entire certificate construction — this is a search, may not succeed at low degree in one round; if the search fails, report exactly which ansatz degrees were tried and why they failed (coefficient-matching infeasible / negative Gram matrix), not just "didn't find one."
Cases to cover: none beyond the ansatz-degree escalation described above.
Watch out for: do not re-attempt an UNCONDITIONAL (domain-free) SOS certificate — round 11 proved none exists (~37-50% negative samples without the n1,n2 domain restriction); every ansatz here MUST include n1,n2 as active multipliers.
