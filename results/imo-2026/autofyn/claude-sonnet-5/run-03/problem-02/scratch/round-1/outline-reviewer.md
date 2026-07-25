# Outline review — imo-2026-02, round 1

Verified independently: the vector reduction shared by fixed-point-concyclic
(step 2) and coordinate-bash (step 2) — `OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4`
with A at the origin — is algebraically correct (checked symbolically with
sympy: `OM²-ON² - (O·(C-B) - (|C|²-|B|²)/4)` simplifies to 0). This load-bearing
free lemma, used by two of the four approaches, is sound. Trust in the
1-parameter-family / OM=ON numeric claim rests on three independent
math-explorer reports agreeing to 10+ digits; reasonable to proceed on that
basis but not itself re-derived here (cheap for a builder to re-check once,
not urgent).

## fixed-point-concyclic — APPROVE

- Technique (reduce OM=ON to a fixed-point concyclicity, then directed-angle
  chase) is exactly the standard move for this problem shape and matches
  knowledge_base.md's synthetic toolkit.
- Reduction lemma (step 2) verified correct above; Q's defining property
  (perp-bisector(AQ) = perp-bisector(MN) by construction as a reflection) is
  immediate, no issue.
- Main gap (step 3, the concyclicity chase) is real and squarely the hard
  part of the problem — appropriately flagged as unproved rather than
  hand-waved. The outline correctly identifies that all three hypothesis
  clauses must be threaded through, and correctly flags the directed-vs-
  undirected angle trap (the containment hypotheses fix a branch; a
  magnitude-only chase can "prove" a false generic statement). No fatal flaw.
- Change to make while building: before committing to the chase, derive Q's
  angle signature relative to B, C, M, N explicitly in closed form (the
  outline notes this is not yet done) — do this first since the whole chase
  target (∠(QA,QK)=∠(LA,LK)) depends on it.

## coordinate-bash — APPROVE

- Sound as an algebraic safety net: reduction lemma verified (see above);
  circumcenter-as-linear-system step is standard and correct once A=0.
- The one real risk — parametrizing K, L from three angle equations without
  hitting a transcendental (non-polynomial) system — is flagged, with a
  reasonable mitigation (unit-vector/tan-half-angle substitution) named in
  the outline itself. No circular reasoning; step 5's cancellation is
  honestly labeled unproved rather than asserted.
- Change to make while building: set up the parametrization with the correct
  signed-angle branch from the start (per its own "Watch out for" — sympy
  will not catch a wrong-branch identity), and use it, as the outline
  suggests, to numerically cross-check fixed-point-concyclic's Q-concyclicity
  claim early — this is cheap and de-risks the other approach too.

## power-of-point-secants — CHANGES REQUESTED

- Technique (power of a point / radical axis) is valid and legitimately
  distinct in shape from the Q-concyclicity route: it tries to avoid one
  monolithic angle chase by anchoring M and N separately.
- However steps 1 and 2 do not yet name even a *candidate* secant line
  through M or N ("TO BE DETERMINED which secant is natural") — this is more
  underdeveloped than the other three outlines, where at least a concrete
  claim is stated even if unproved. This is not fatal (power-of-a-point
  problems often require exactly this kind of construction hunt), but it is
  a step below the others in readiness.
- Real risk, correctly self-flagged: this approach may converge to needing
  the same point Q as fixed-point-concyclic, which would make it not an
  independent line but a restatement of the same wall (anti-single-gap-trap).
- Required before/while building: (a) nail a concrete candidate secant
  through M and through N (the outline's own suggestions — line MK with MA,
  or circle (BMK) radical axis — are reasonable starting points), (b) make
  hypothesis 1 (∠KBA=∠ACL) actually enter the argument, since it is currently
  unused in steps 1–2 and the outline admits step 3 needs it but doesn't say
  how, (c) report immediately, without grinding further, if the secant hunt
  converges to a Q-equivalent point — that's a signal to reviewers, not proof
  of infeasibility.

## spiral-similarity-bootstrap — RETHINK

Fatal flaw, self-admitted in the outline: the approach's own "Identification
lemma" (step 5: O = h(A,1/2) applied to a fixed point like O_ABC or the
nine-point center) is flagged by the outline itself as "likely FALSE" — since
O demonstrably *moves* along the line ℓ = perp-bisector(MN) as the family
parameter varies (confirmed by all three explorers), no single fixed point's
homothety image can equal O identically. The only clean, correct content in
the whole outline is step 6, the elementary fact that h(A,1/2) maps
perp-bisector(BC) to perp-bisector(MN) — but that alone does not show O ∈ ℓ,
it only restates what the target line looks like (already visible from the
vector reduction shared by the other two synthetic-adjacent approaches).

Steps 1–4 (the "one-angle circle-membership" lemmas) have no stated
mechanism beyond "test whether," "needs care," and an explicit prior
falsification of the naive full-triangle-similarity reading (△LBK~△LNC,
△KCL~△KMB numerically false per math-explorer-computational). Unlike the
other three outlines, there is no candidate identity here with even an
unproved-but-concrete target statement — it is a research direction, not a
skeleton a builder can execute. Building this now would spend a round
re-deriving the free step 6 and then stalling exactly where the outline
itself predicts.

**Recommendation for next round's outliner:** do not build this as stated.
Either (a) replace it with a genuinely worked-out alternative mechanism for
"O ∈ ℓ without a fixed point Q" — e.g., express O·(C−B) directly via whatever
circle-membership facts steps 2–3 can actually prove once corrected to
single-angle (not full-similarity) form, and show algebraically it collapses
to (|C|²−|B|²)/4, mirroring coordinate-bash's target but via synthetic
circle-power relations instead of raw trig — or (b) retire this framing in
favor of a fourth genuinely distinct route (e.g., a trigonometric
Law-of-Sines identity approach, or a projective/cross-ratio argument) so the
field keeps real diversity rather than a fourth slot that's actually empty.
Not registered in the ranker per protocol (RETHINK approaches are never
seeded).

## Diversity assessment

Two real routes are present: (1) fixed-point-concyclic and
power-of-point-secants both ultimately chase circle-membership facts tied to
one new configuration on/around circle (AKL) — genuine risk they collapse to
the same wall, explicitly flagged by both outlines' own authors. (2)
coordinate-bash is a structurally independent brute-force cross-check,
valuable regardless of what happens to (1) and useful for numerically
sanity-checking (1)'s conjectured lemmas cheaply. spiral-similarity-bootstrap
was intended as a third independent framing but, as outlined, does not
deliver one — its correct content is a strict subset of what's already
visible from the vector reduction. If both routes in (1) stall next round on
the same directed-angle/circle-membership obstruction, that should be read
as one wall, not two failures, and the next outliner should be pushed toward
a fourth framing genuinely far from both (e.g. trig/Law-of-Sines identity,
or projective).

## Ranking

Cold-start round; no empirical outcomes yet, so ranking reflects outline
readiness/soundness only:
- fixed-point-concyclic > power-of-point-secants (concrete Q, verified
  reduction, standard technique vs. undetermined secant construction)
- coordinate-bash > power-of-point-secants (guaranteed-terminating brute
  force vs. undetermined construction)
- fixed-point-concyclic > coordinate-bash (more insight-bearing route, likely
  to yield a cleaner write-up if the chase closes; coordinate-bash is the
  fallback/cross-check by its own framing)

Resulting Elo: fixed-point-concyclic 1532, coordinate-bash 1499,
power-of-point-secants 1469. spiral-similarity-bootstrap not registered
(RETHINK).

build set: fixed-point-concyclic, coordinate-bash, power-of-point-secants
