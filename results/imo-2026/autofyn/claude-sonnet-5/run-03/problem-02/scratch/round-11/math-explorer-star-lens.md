## imo-2026-02

- Distinct openings:
  1. **Boundary-reduction attack on (⋆) directly.** The numeric global-min
     finding (inf of `(1+cosB)^2X0 - RHS^2 = 0`, attained ONLY at the corner
     `γ→β0`) strongly suggests (⋆) is not a global-SOS fact but a
     **boundary-extremal** fact: the two-variable domain (A,B) has its
     minimum on the codim-1 curve `γ=β0` (i.e. `B=(π-A)/3`), and on that
     curve the minimum-over-the-curve itself sits at one further point
     (giving the reported codim-2 corner). This suggests splitting the
     problem into (a) prove (⋆) restricted to the curve `B=(π-A)/3` (a
     genuine 1-variable trig inequality in `A` alone — tractable, since
     `β0` is then eliminated as a function of `A` only, and `X0`, RHS all
     become closed forms in `A`), and (b) prove a transverse-monotonicity
     lemma showing moving `B` away from `β0` (increasing the domain width
     `γ-β0`) only increases the slack `(1+cosB)^2X0-RHS^2`. This is the
     standard "reduce to boundary of the domain, then handle the boundary
     as a 1-variable problem" pattern (see knowledge_base.md's Extreme Value
     Theorem entry, line ~47, on reducing to a compact-manifold argument) —
     concretely here it would mean computing `∂/∂B [(1+cosB)^2 X0 - RHS^2]`
     at fixed `A` and showing its sign matches "moving away from the
     β0-curve increases slack." I did NOT attempt this derivative
     computation — it is a concrete, well-defined next step, not a proof.
  2. **Tangent-line-at-the-boundary-equality-point trick applied to X0 or
     RHS individually.** Since equality is only approached at one specific
     point, a natural device (see crux `aimo-0005` below) is to replace one
     of the messy trig quantities (e.g. `X0` or `cos²β0`) by a *linear*
     (in some convenient variable, e.g. `cos A` or `t=B-β0`) under/over-bound
     that is exact at the corner and provably one-sided elsewhere — then the
     resulting inequality becomes polynomial/linear and easier to certify.
     This mirrors exactly the "MVT/Lipschitz" mechanism already used to
     produce (⋆) itself (bounding `f'` by a constant, tight only in a
     limit) — i.e. (⋆) is *already* a first tangent-line-type bound; the
     recommendation is a **second** application of the same idea to the
     leftover radical-free inequality, this time using the corner point
     itself as the tangency point rather than an arbitrary constant bound.
  3. **Substitution `t := B - β0` (domain-width variable) with Taylor
     expansion around `t=0`.** Since the corner is exactly `t→0` (jointly
     with a specific `A`), expanding `(1+cosB)^2X0-RHS^2` to first order in
     `t` at fixed `A`, then checking that (i) the zeroth-order term vanishes
     only at the specific `A_0≈0.4064` and (ii) the first-order term's sign
     matches "increasing away from the corner," could turn (⋆) into a
     manageable one-variable-plus-perturbation argument instead of a raw
     2-variable global inequality. Not attempted; a concrete computational
     step (symbolic Taylor expansion) for a future round.
  4. **Attack the T-factorization sign instead, but restricted to the true
     (P>0∧E<0) domain, not the full (A,B) square.** I numerically checked
     (see below) whether `4dst·q1+c·r0` (the sign-determining combination
     for `T≥0`) is sign-definite on the FULL `(A,B)` domain (`A∈(0,π/2)`,
     `B∈(0,π)`, `A+B<π`): it is not (≈45% violations). This matches the
     file's own finding that q1, r0 alone lack fixed sign. But the actual
     claim only needs to hold on the *much smaller* `P>0∧E<0` sub-case
     (≈4.5% of Case (b)) — I did not have closed forms for `P,E` in terms of
     `(A,B)` on hand to re-test restricted to that sub-case; this is a
     concrete, cheap next check (rerun the same numeric sweep, but filtering
     samples to `P>0∧E<0` using the exact `P,E` formulas from
     `case-b-p-le-0-and-e-ge-0-closed.md`) that could reveal the combination
     IS sign-definite once properly restricted — worth doing before
     concluding "no combined-sign relation exists."

- Candidate technique(s): MVT/Lipschitz boundary reduction (already applied
  once to get (⋆) — recommend applying a second, sharper instance targeting
  the corner directly, i.e. a genuine "extremize over the compact domain,
  reduce to the boundary" argument per the Extreme-Value-Theorem entry in
  knowledge_base.md); tangent-line trick (SOS-adjacent, KB's "Sum of squares
  / completing the square" entry, line ~17-18) engineered so the tangent
  point IS the identified degenerate corner rather than a symmetric point;
  Sturm-sequence / resultant sign-counting (KB's resultants entry, line ~13)
  as a fallback if a clean closed-form monotonicity argument in `B` (for
  fixed `A`) cannot be found by hand.

- Cheap-kill candidates: check whether `(1+cosB)^2X0-RHS^2` is monotone in
  `B` for fixed `A` throughout Case (b)'s domain (a single partial-derivative
  sign check) — if so, the whole 2-variable problem collapses to checking
  one endpoint (`B=β0` or `B=γ`'s boundary), which is exactly the reduction
  suggested in opening 1. This is cheap (one symbolic derivative + sign
  argument) and should be tried before any heavier SOS/Sturm machinery.

- Knowledge-base entries to use: "Resultants / transform the roots" (line
  13); "Sum of squares (SOS) / completing the square" (line 17-18);
  "Extreme value theorem / Lagrange multipliers on a compact manifold"
  (line 47-49, for the boundary-reduction framing); "Standard inequalities:
  AM-GM, Cauchy-Schwarz, QM-AM, Schur — equality cases pin down the
  extremal configuration" (line 33-34, directly relevant since the found
  corner IS the equality/extremal configuration and should be used to
  reverse-engineer the right SOS/tangent decomposition).

- Analogous past problems (cruxes): **`aimo-0005`** (algebra,
  `inequalities-SOS-and-convexity`) is genuinely analogous in mechanism, not
  just subtopic: its crux move is "bound each nonlinear term below by the
  line tangent at the equality point, choosing the tangent so it ALSO passes
  through the value at the boundary equality point, then verify the bound
  by factoring the difference" — i.e. a tangent-line bound deliberately
  pinned to a boundary corner (there, `b=2` interior AM-GM point plus a
  `b=0` boundary check simultaneously), exactly the flavor of construction
  suggested in opening 2/3 above for `(⋆)`'s corner at `γ=β0`,
  `A≈0.4064`. No other crux in the `inequalities-SOS-and-convexity`
  subtopics sampled matches as closely (most are AM-GM/Cauchy-Schwarz-based
  symmetric bounds, not boundary-pinned tangent constructions). The corpus
  has no geometry subtopic at all (per `crux_moves_documentation.md`), so no
  direct geometric crux exists for this problem's actual synthetic content —
  the analogy here is purely at the level of the residual trig-inequality
  sub-problem, which is legitimately algebra-flavored at this point in the
  proof (no geometry left in `(⋆)` itself).

- Prior progress: `(⋆)`: `(1+cosB)^2X0 ≥ RHS^2` (100% of Case (b), via
  `lemmas/mvt-lipschitz-reduction-case-b.md`) is the most general open
  target — proving it closes the whole shared gap. The narrower
  `T≥0` factorization (`lemmas/case-b-e-lt-0-t-factorization.md`, ≈4.5% of
  Case (b)) is subsumed by `(⋆)` if the latter is proved, so `(⋆)` should be
  the priority (as round 10's current.md already recommends).

- Dead ends (do not retry): the "cruder domain-width bound"
  (`G(β0)≥(1+cosB)(γ-β0)`, dropping the dependence on `β1` itself) is
  FALSE — confirmed independently by global optimization (violation
  ≈-0.078, away from any degenerate corner) both by the builder and the
  round-10 proof-reviewer. Do not re-attempt a version of `(⋆)` that
  replaces `cosβ1`/`β1-β0` with the raw domain width `γ-β0` — this loses
  too much precision. Also: the round-8 midpoint-evaluation route for the
  `Y<0` case's `σ_N` sign (via the messy Vieta midpoint `m_0`, requiring an
  uncertified triple-angle trig fit) was superseded by the cleaner
  "evaluate at the sibling's own zero" method in round 9 — not relevant to
  `(⋆)` directly but a reminder that "evaluate at a distinguished point
  with a clean closed form" beats "evaluate at the generic algebraic
  midpoint" as a general technique in this population.

- Small-case / intuition notes: (conjecture, not proved) `q1` and `r0`
  (from the `T`-factorization) do NOT have a sign-definite linear
  combination `4dst·q1+c·r0` when tested over the FULL `(A,B)` domain
  (own fresh 1.5M-sample sweep, `A∈(0,π/2)`, `B∈(0,π)`, `A+B<π`: `val≤0`
  — i.e. `T≥0` — holds only ≈54.7% of the time, i.e. genuinely false
  outside the narrow `P>0∧E<0` sub-case, as expected). I did **not** have
  the exact `P,E` formulas on hand to re-restrict this sweep to the true
  sub-case; a fresh check restricted to `P>0∧E<0` (using
  `case-b-p-le-0-and-e-ge-0-closed.md`'s definitions) is a cheap, valuable
  next step that could still reveal a clean sign-definite combination once
  properly scoped, but this was not established in this exploration. On the
  `q1,r0` pairwise-sign census alone (2M samples over `(σ,τ)∈(0,1)^2`, no
  domain restriction): `q1>0` in ≈25.6%, `r0>0` in ≈54.9% (matching the
  certified lemma's own figures), `q1·r0>0` in ≈68.4%, `q1+r0>0` in ≈50.3%
  — neither simple combination is obviously sign-definite even on the full
  unit square, so if a clean combined-sign fact exists it likely needs the
  genuine sub-case restriction (in `A,B`, not merely `σ,τ`) to be visible.
