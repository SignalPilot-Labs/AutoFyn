## imo-2026-02

- Distinct openings surfaced this round (route: "genuinely orthogonal framing"
  per dispatch, ideas 1-4):

  1. **O-locus-is-a-line reframe (numerically confirmed, but shown to be a
     re-statement of the already-proven gap-1 identity, not a new escape).**
     I built an independent numeric solver (own `scipy.fsolve` pipeline, own
     `arccos`-based angle equalities for hypotheses 1-3, own in-triangle
     test, own circumcenter formula — no code reused from any approach file)
     that tracks `K(θ), L(θ)` as the free hypothesis-1 angle `θ=∠KBA=∠ACL`
     varies continuously (continuation: each `fsolve` seeded from the
     previous solution). Computed `O(θ)` = circumcenter of `A,K,L` for three
     independent triangles. **Finding**: restricted to the θ-range where `K∈
     △BMC` and `L∈△BNC` (containment satisfied), the locus `{O(θ)}` is
     collinear to machine precision (SVD second singular value `~1e-15`
     relative to the first `~0.3`, on all three triangles) — i.e. `O` sweeps
     a single fixed straight line as `θ` varies over the whole valid
     sub-range. Tracked past the containment boundary (still same
     continuation branch, residuals stay `<1e-9`): the locus **smoothly
     peels off the line exactly where containment first fails** (deviation
     grows continuously from `θ≈0.90` onward for one test triangle, not a
     jump) — so this fixed line is *not* a raw polynomial identity valid on
     the whole algebraic branch, only on the geometrically-genuine sub-range.
     **Diagnosis**: "O lies on a fixed line" is *exactly* the statement
     `O·(C−B)=(|C|²−|B|²)/4` (the central identity), already proved in full
     generality on the `G2a=G3a=0` branch since round 3
     (`lemmas/symbolic-genericity-certificate.md`). The observed peeling-off
     is simply the `G2a/G3a` branch losing geometric validity — i.e. this
     numeric experiment **independently re-confirms, from an entirely
     different angle (literal geometric visualization of the locus), that
     branch selection (not the central identity) is the sole remaining
     obstruction**, and that the coordinate route's own diagnosis (round 3-7)
     is correct. It does **not** open a new escape route — full disclosure,
     this is a negative/confirmatory result for "recast as a line-locus
     problem," not a new opening.
  2. **Positivstellensatz / SOS on Ψ(τ,A,C) — not completed this round, flagged
     concretely for next round.** Time did not permit building Ψ's full
     six-coefficient closed form (per `ptolemy-trig-identity.md` round 6,
     the coefficients did not even fully extract in a tractable closed form
     there). Recommend: attempt a numeric SOS/Schur-type certificate search
     directly (e.g. `scipy.optimize` minimizing a Lagrangian slack, or
     `sympy` + a manual Schur-like ansatz `Ψ = Σ λ_i·(square)·(positive
     boundary term)`) using Ψ's already-certified boundary value
     `Ψ(0,A,C)=4sin³A sinB sinC` as the anchor term — a genuinely different
     *technique* (positivity certificate vs. resultant/parity counting) even
     if targeting the identical polynomial. Not attempted numerically this
     round due to time; a real gap in this report, not a negative result.
  3. **Directed-angle/phase framing — already effectively the current best of
     `fixed-point-concyclic` (Theorem 6/7), and its remaining gap has the
     same "branch selection" shape.** That approach already replaced squared
     coordinates with a bilinear complex-number computation and derived a
     closed-form `χ=−D₀/D₁` with *zero* nested-radical/branch content
     (Theorem 7). The catch: (H1)-(H3) as currently encoded are "ratio ∈
     ℝ_{>0}" conditions, which retain only the *sign* of each hypothesis
     angle, not its magnitude — exactly the same kind of information loss
     that produces branch-selection problems elsewhere. The open
     `Rem(H1,H2,H3,B,C̄,C,C̄)=0` gap (verified nonzero as a bare polynomial
     identity, round 7) needs the *actual geometric* definitions of
     `H1,H2,H3` (not just their positivity) — i.e. it needs the same kind of
     "prove a sign/positivity pattern survives using the true, not merely
     relaxed, hypotheses" argument as every other route. This is a precise,
     independently-reasoned confirmation (not new numerics) that idea 3
     (directed angles) has *already* been tried by the population and hits
     the identical plateau shape — do not re-attempt as if it were untried.
  4. **Inversion at A (untried framing for the concyclic(A,K,L,Q) target).**
     `fixed-point-concyclic` proves `A,K,L,Q` concyclic via a cross-ratio-
     real criterion. An inversion centered at `A` (any radius) sends this to
     "the images `K*,L*,Q*` are collinear" — literally the same fact, but a
     **degree-1 (linear/determinant) target** instead of a "ratio ∈ ℝ"
     realness target. This substitution has not been explicitly tried by any
     approach file (checked: none of `fixed-point-concyclic`'s six rounds
     mention inversion). It is *not* obviously easier — cross-ratio realness
     and post-inversion collinearity are classically equivalent formulations
     of the same fact (a circle through the center of inversion maps to a
     line) — but the resulting determinant/linear-algebra form might combine
     more directly with `fixed-point-concyclic`'s own already-bilinear
     Cramer's-rule machinery (Theorem 6/7) than the cross-ratio form does,
     since both would then be pure determinant identities. Flagged as a
     concrete, cheap thing to try next round (adapt Theorem 6/7's row-vector
     construction to `K*,L*,Q*` collinearity directly) — not attempted here
     due to time.

- Candidate technique(s): (a) IVT/continuity-only argument exploiting that
  the central identity is *already proved on the whole G2a/G3a branch*
  (round 3) — so branch selection only needs checking that the containment-
  valid sub-range never crosses off `G2a/G3a` onto `G2b/G3b`, which several
  approaches already frame this way (continuity/IVT mechanism,
  `coordinate-bash-resultant-boundary`); my locus experiment independently
  corroborates that this continuity framing (not pointwise sign-testing) is
  structurally the right shape. (b) SOS/Positivstellensatz on `Ψ` — untried,
  recommend for next round. (c) Inversion-at-A reformation of the
  concyclic(A,K,L,Q) target as `K*,L*,Q*` collinear — untried, recommend for
  next round, likely combinable with `fixed-point-concyclic`'s Theorem 6/7
  determinant machinery.

- Cheap-kill candidates: none obvious beyond what's already found. The
  `(+,+,+)` forbidden pattern (already certified for `Y,B2,Z`) and the
  `G2a`/`G2b` true/supplementary parity lemmas are the existing cheap
  structural facts; no new pigeonhole/parity/injection found this round.

- Knowledge-base entries to use: Geometry / synthetic toolkit — "power of a
  point ... inversion, spiral similarity" (inversion-at-A idea, #4 above);
  "Trig identities & interval intersection" entry (already used by the
  Ptolemy route; relevant if SOS/Positivstellensatz work on `Ψ` proceeds via
  interval-based case splits). No new KB entry identified as a candidate
  beyond what the population already cites.

- Analogous past problems (cruxes): did not query the crux corpus this
  round (time-constrained; my dispatch focused on numeric/structural
  groundwork on the four listed ideas). Recommend a future explorer query
  `crux_moves_documentation.md`'s geometry subtopics for "circumcenter
  locus" / "inversion at a common point" / "cross-ratio realness"
  specifically, since none of those exact phrasings were searched in prior
  rounds' reports as far as I can tell from `current.md`.

- Prior progress: unchanged from `current.md` — gap 1 (central identity) is
  fully closed and certified (`lemmas/symbolic-genericity-certificate.md`);
  isosceles case closed (`lemmas/isosceles-case-symmetry.md`); magnitude
  bound closed (`lemmas/magnitude-bound-and-sign-coincidence.md`); all live
  routes' sole remaining gaps are various "sign/parity survives across
  roots" claims, all numeric-only (thousands of samples, 0
  counterexamples), none proved symbolically.

- Dead ends (do not retry): plain concyclicity search over the natural
  8-point set `{A,B,C,K,L,M,N,Q}` plus `BK∩CL`, `BL∩CK` (round 1, exhaustive,
  found only the two already-known circles) — my inversion-at-A idea (#4) is
  a genuinely different *encoding* of the same known concyclic(A,K,L,Q)
  fact, not a rediscovery attempt of a new hidden circle, so it is not
  redundant with this dead end. Spiral similarity centered at `A` sending
  `B↦C, K↦L` — refuted round 1 (rotation angles `∠(AB,AC)` and `∠(AK,AL)`
  numerically different). Directed-angle/phase reframing as a wholesale
  replacement for the coordinate routes — already effectively subsumed by
  `fixed-point-concyclic`'s existing bilinear/Cramer's-rule machinery
  (Theorem 6/7, round 7), which hits the identical plateau shape (see
  opening 3 above) — a fresh "directed angles mod 180°" approach file would
  very likely just re-derive Theorem 6/7 by a different route and land on
  the same `Rem=0`-type gap; not recommended as a new slug unless it can be
  shown to avoid encoding hypotheses as bare "ratio ∈ ℝ_{>0}" (which is
  where the magnitude information gets discarded).

- Small-case / intuition notes (conjectural, numeric only):
  - The circumcenter `O(θ)` traces, empirically, a straight line throughout
    the containment-valid θ-range, for all three tested triangles
    (isosceles-ish and two scalene ones), confirming `OM=ON` at every
    interior `θ`, not just isolated points — consistent with, and a fresh
    visualization of, the already-certified central identity. This
    reinforces (does not newly establish) that a continuity/IVT-style
    argument — checking the boundary of the valid θ-range plus "the branch
    never swaps in the interior" — is the right shape for closing branch
    selection, over any pointwise-sign-testing approach.
  - The deviation of `O(θ)` from the line, once containment fails, is smooth
    (not a jump) in my `arccos`-based continuation — a caution for any
    future numeric branch-tracking: `arccos`-based angle formulations can
    silently redefine which algebraic branch is being solved for once the
    true (signed) angle passes through a boundary value, so continuation
    results just past a containment boundary should not be trusted as
    "the same algebraic branch" without an unsquared, sign-aware
    reformulation (e.g. `arg`, not `arccos`) — a methodological note worth
    passing to builders using numeric continuation for branch-selection
    checks.
