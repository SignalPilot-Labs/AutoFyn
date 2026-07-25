## imo-2026-02

fixed-point-concyclic: new
Target: OM = ON, for every valid (K,L) in the hypothesis's 1-parameter family.
Technique: Reduce equal-distance goal to a fixed-point concyclicity (A,K,L,Q
concyclic for a Q depending only on A,B,C), then directed-angle chasing
(knowledge_base.md Synthetic toolkit: angle chasing + concyclicity converse).
Skeleton:
  1. Define Q = reflection of A across perp-bisector(MN) (point depends only
     on A,B,C) — by construction.
  2. Reduction lemma: A,K,L,Q concyclic ⟹ O equidistant from A,Q ⟹ O on
     perp-bisector(AQ) = perp-bisector(MN) ⟹ OM=ON — elementary vector check
     (no gap).
  3. Main gap: prove A,K,L,Q concyclic via directed angles, chasing through
     auxiliary triangles ABK/ACL (hyp.1), LBK/LNC (hyp.2), KCL/KMB (hyp.3),
     tying both chains to Q's fixed angle signature relative to B,C,M,N.
  4. Conclude OM=ON.
Key lemmas (claim + mechanism):
  - Reduction lemma — because Q is defined so that AQ ⊥ perp-bisector(MN)
    passes through its midpoint; a 3-line vector verification.
  - Concyclicity lemma (∠(QA,QK)=∠(LA,LK)) — because the three hypothesis
    equalities are exactly the data threading a directed-angle chain from Q
    through B,C,M,N to L,K; unproved, the crux gap.
Open gaps: step 3 entirely open (the directed-angle chase); Q's explicit
angle signature vs B,C,M,N not yet derived.
Cases to cover: none (single configuration up to containment-fixed branch).
Watch out for: (a) valid (K,L) form a genuine 1-parameter family — concyclicity
must hold identically along it, not at an isolated point; (b) must use signed
(directed) angles, not magnitudes — the containment hypotheses fix the branch,
and a magnitude-only chase risks "proving" a false generic statement.

coordinate-bash: new
Target: OM = ON, for every valid (K,L).
Technique: Full symbolic coordinate/trig computation (knowledge_base.md
"Coordinates / complex / barycentric") using sympy in this environment;
algebraic safety net independent of synthetic insight.
Skeleton:
  1. A = origin ⟹ M=B/2, N=C/2.
  2. Vector reduction (free, no gap): OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4, by
     expanding |O−B/2|²−|O−C/2|².
  3. Parametrize K,L via the three hypothesis angle equations (one shared
     angle β=∠KBA=∠ACL plus two radius unknowns solving the other two
     equations) — encode as polynomial (not transcendental) relations via
     unit-vector/tan-half-angle substitutions.
  4. Solve circumcenter O of A,K,L in closed form (linear system O·K=|K|²/2,
     O·L=|L|²/2 since A=0).
  5. Substitute and simplify O·(C−B) via sympy, verify it collapses to
     (|C|²−|B|²)/4 identically (crux computational gap — the free parameter
     must cancel).
  6. Conclude via step 2.
Key lemmas (claim + mechanism):
  - Vector reduction (step 2) — polarization identity, |O|² cancels; no gap.
  - Circumcenter formula (step 4) — A=0 linearizes OA=OK, OA=OL to dot-product
    equations; standard Cramer's-rule solve.
  - Elimination identity (step 5, hard gap) — must show algebraic cancellation
    removing the free parameter; mechanism not yet found.
Open gaps: step 3's parametrization (must avoid transcendental obstructions);
step 5's symbolic cancellation is fully open.
Cases to cover: none beyond generic scalene position; degenerate/isoceles
cases handled by continuity, not separate casework.
Watch out for: signed angles vs magnitudes when encoding directions for K, L
— wrong branch produces an internally-consistent but wrong identity that sympy
won't flag; use this approach also as a numerical/symbolic cross-check of the
other approaches' conjectured lemmas (e.g. verify fixed-point-concyclic's Q
concyclicity claim symbolically).

spiral-similarity-bootstrap: new
Target: OM = ON, for every valid (K,L).
Technique: Structural spiral-similarity/homothety argument (knowledge_base.md
Synthetic toolkit: spiral similarity), trying to express O via the fixed
homothety h(A,1/2) (which sends B↦M, C↦N) rather than via a second fixed point
Q on the circle.
Skeleton:
  1. Test candidate similarity at A (from ∠KBA=∠ACL: △ABK, △ACL spiral-similar
     centered at A?) — needs a ratio condition not directly given; test
     whether hypotheses 2,3 jointly supply it.
  2. Test candidate similarity at K (from ∠LCK=∠BMK) — full △KCL~△KMB is
     numerically FALSE (recorded dead end from math-explorer-computational);
     must instead extract a weaker one-angle/circle-membership fact.
  3. Test candidate similarity at L (from ∠LBK=∠LNC) — symmetric, same
     caveat.
  4. Combine one-angle relations into two auxiliary circles; relate to
     circle (AKL) via radical axis.
  5. Attempt to identify O via these auxiliary circles and the elementary
     homothety fact (step 6) — flagged as likely to collapse to nothing more
     than step 6 unless steps 1–4 produce real content.
  6. Free elementary fact (no gap): h(A,1/2)(perp-bisector BC) =
     perp-bisector MN, since h(A,1/2) sends B↦M,C↦N and homothety preserves
     the equidistant-locus map.
Key lemmas (claim + mechanism):
  - Homothety fact (step 6) — elementary, no gap.
  - One-angle circle-membership lemmas (steps 2–3) — mechanism: inscribed-
    angle converse applied NOT as full triangle similarity (falsified) but as
    a weaker point-on-circle fact; unproved.
  - Identification of O (step 5) — likely the wrong framing since O actually
    moves along the line as the parameter varies, so no single fixed point
    equals O; this lemma as originally conceived is probably FALSE and needs
    correction to a line-level (not point-level) statement.
Open gaps: everything past step 6 is open; step 5 may need reframing entirely
(this is flagged explicitly as the highest-risk approach).
Cases to cover: none identified; note if step 1's ratio-completion needs an
orientation choice.
Watch out for: do not re-derive the already-falsified full triangle
similarities △LBK~△LNC / △KCL~△KMB (recorded dead end, math-explorer-
computational.md); if steps 1–5 cannot be completed, report this honestly as
a RETHINK candidate rather than padding with only the free step 6.

power-of-point-secants: new
Target: OM = ON, for every valid (K,L).
Technique: Power of a point / radical axis (knowledge_base.md Synthetic
toolkit), anchoring M and N SEPARATELY via the two hypothesis clauses that
mention them directly (∠LCK=∠BMK for M, ∠LBK=∠LNC for N), avoiding a single
monolithic angle chase to one new point.
Skeleton:
  1. Build an explicit secant of circle (AKL) through M using ∠BMK=∠LCK
     (candidate lines: MK combined with MA, or with the midline MN) —
     compute pow(M;⊙AKL) in terms of this hypothesis.
  2. Symmetric construction anchored at N via ∠LNC=∠LBK, compute pow(N;⊙AKL).
  3. Show the two power expressions equal, using hypothesis 1 (∠KBA=∠ACL,
     not yet used in steps 1–2) as the linking relation between the two
     otherwise-symmetric computations.
  4. Conclude OM=ON from equal powers with common radius R — elementary
     (pow(P) = PO²−R²), no gap.
Key lemmas (claim + mechanism):
  - Power-distance identity (step 4) — standard definition, no gap.
  - Secant-at-M / secant-at-N lemmas (steps 1–2, real gap) — mechanism:
    inscribed-angle theorem relating ∠BMK (resp. ∠LNC) to an arc of a circle
    sharing a chord with (AKL); exact secant not yet identified.
  - Equality-of-powers via hypothesis 1 (step 3, real gap) — mechanism: the
    two power expressions, both functions of the shared parameter
    β=∠KBA=∠ACL, must cancel to the same value; not yet shown.
Open gaps: steps 1–2 (identifying the natural secants) and step 3 (the
matching argument) are all open.
Cases to cover: none beyond generic position; flag degenerate tangent-secant
edge cases as continuity limits, not separate casework.
Watch out for: if the secant hunt in steps 1–2 converges to needing a point
equivalent to Q from fixed-point-concyclic.md, that is a genuine signal the
two approaches share one underlying wall — report this convergence explicitly
rather than treating both as independent evidence of feasibility (anti-
single-gap-trap, CLAUDE.md). Track signed powers/lengths carefully (M, N may
lie inside or outside circle (AKL) depending on the parameter).

build set: fixed-point-concyclic, coordinate-bash, spiral-similarity-bootstrap, power-of-point-secants
