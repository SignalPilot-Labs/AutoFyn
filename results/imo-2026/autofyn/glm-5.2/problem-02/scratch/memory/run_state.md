## Goal

Solve IMO 2026 Problem 2 (geometry): the OM=ON problem. Repo problem_id is
`imo-2026-02` (the geometry entry; imo-2026-01=NT, imo-2026-02=geo, imo-2026-03=combo).
Produce a complete rigorous proof in `results/imo-2026-02.md` with Status=solved.

Metric: solved count of hard problems. Eval: `grep -rl '^solved$' results/ 2>/dev/null | wc -l`.
Baseline: 0. Target: +1 (this problem solved). Constraint: rigorous proof (no gaps, all cases).

User also requests (final deliverable, at session end): a LaTeX file and a separate
Markdown file with a nicely formatted solution + commentary; branch named
`glm5.2-imo2026-03` per user (note: geometry is Problem 2 / repo id 02; user labelled it 03).

## Goal Updates

- [Round 1] User: "solve imo-2026-03" but pasted the GEOMETRY Problem 2 statement
  (ABC triangle, M,N midpoints of AB,AC; K inside BMC, L inside BNC with angle
  conditions; O circumcentre of AKL; prove OM=ON). Statement is dispositive =>
  solve the geometry problem. Repo id for it is imo-2026-02. Branch name per user:
  glm5.2-imo2026-03 (recorded; harness handles git).

## Eval History

- [Round 1] SOLVED imo-2026-02 (geometry, OM=ON). Eval `grep -rl '^solved$' results/ | wc -l` = 1.
  Baseline 0 -> 1. BREAKTHROUGH (full rigorous proof in one round). Reviewer verdict APPROVE.
  Proof: antipode reduction OM=ON<=>|A'B|=|A'C| + Direction Lemma
  measuredangle(BC,BA')=90-A-alpha (polynomial certificate g=C*T, remainder 0,
  signed +theta) + B<->C orientation-reversal gives counterpart -theta => A' on
  perp-bis(BC). Cross-checked algebraically + numerically + by coordinates.

## Rules

- ALWAYS: when a user names a problem id but pastes a conflicting statement, the
  pasted statement wins (round 1). Verify the repo problem_id mapping before writing
  the results file.
- ALWAYS: for a "circumcentre + midpoint" conclusion, reduce via the ANTIPODE
  A'=2O-A (Thales gives A'K perp AK, A'L perp AL) and a homothety at A (midpoints)
  converting O-equidistant-from-midpoints to A'-equidistant-from-endpoints (round 1).
- PREFER: when a distance-squared identity lives only in a RADICAL ideal (no direct
  polynomial certificate), switch to the DIRECTION (angle/tangent = rational)
  identity, which admits a clean polynomial divisibility certificate g=C*T with
  zero remainder (round 1). Distance (degree-2, radical) vs direction (rational).
- ALWAYS: directed-angle lemmas are SIGNED and certified only in a chosen
  orientation; a relabeling that reverses triangle orientation (CCW->CW, e.g.
  swapping B<->C) needs a reflection to re-apply the lemma, flipping the sign.
  Do NOT then add a spurious sign flip for line CB<->BC (same line mod pi).
  Two compensating sign errors cancel by coincidence -> verify signs independently (round 1).
- NEVER: trust a free-ring ideal-membership certificate F=L1*conK+L2*conL when the
  forms are independent (det!=0) — it generates the maximal ideal trivially and is
  vacuous. Check g and C are nonzero at free-indeterminate values (round 1).

## State

Done: Round 1 SOLVED imo-2026-02 (geometry). Full rigorous proof in
  results/imo-2026-02.md (Status=solved). Deliverables produced:
  imo-2026-02-solution.tex (LaTeX), imo-2026-02-commentary.md (solution+commentary).
  Explorer->outliner->outline-review->builder->proof-review (x3, last APPROVE).
Broken: (none)
Next: goal achieved for this problem. If further rounds, pick a fresh unsolved hard
  problem. Deliverable branch name per user: glm5.2-imo2026-03.
