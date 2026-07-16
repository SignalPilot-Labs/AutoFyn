# Run State — imo-2026-05

## Goal
Solve IMO 2026 P5 (imo-2026-05), a `hard` algebra functional-equation problem.
Statement: Find all functions f: R_{>0} -> R_{>0} such that
  sqrt((x^2 + f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y))   for all x,y > 0.
Task type: compute_and_prove, answer_type: characterization.

Metric: proof-reviewer verdict on the leading approach in results/imo-2026-05/.
Eval: proof-reviewer judges approaches/<slug>.md; Status in current.md (unsolved|partial|solved).
Baseline (round 1): no approach yet -> Status unsolved.
Target: a `solved` approach = complete rigorous proof that (a) characterizes ALL such f
  (must prove upper AND matching construction — likely f(x)=x is the only solution),
  (b) settles every case, names every tool.
Constraints: rigor rules in CLAUDE.md (no skipped cases, no hand-waving, name tools,
  verify final answer by substitution).

## Goal Updates

## Eval History
- Round 1 baseline: no results dir; Status unsolved. Ranking empty.
- Round 1 explore: ALL 3 lenses converge. ANSWER = f(x)=x+c for any c>=0 (NOT just x).
  Sufficiency: SOS, both slacks = (x-f(y))^2/4. Necessity: sub x=f(y) => f(f(y))=2f(y)-y;
  hard part = force h=f-id constant (orbit/density argument OR derivative argument).
- Round 1 build+review: SOLVED. BREAKTHROUGH. TWO independent APPROVE proofs.
  Ranking: modulus-telescope (flagship, telescope limit) + two-sided-orbit (calculus-free hedge)
  both verified-milestone. proof-reviewer APPROVE both; sympy-checked every load-bearing step.
  Answer f(x)=x+c (c>=0) stated & verified by substitution. current.md Status=solved w/ Full proof.
  Certified lemmas: pinch-identity, orbit-nonnegativity, quadratic-modulus.

## Rules
- ALWAYS attack the problem's actual claim end-to-end per slug (single-line trap, CLAUDE.md).
- ALWAYS run explorers in parallel with distinct lenses; rank every round (no fast-path).
- NEVER subtract the two given inequalities to form a "combined inequality" (invalid; outliner
  flagged it round 1) — use only one-sided bounds from each inequality separately.

## State
### Done
- Round 1: setup env; explored (3 lenses); outlined 3 rival approaches; built & reviewed 2.
  SOLVED: two independent APPROVE proofs (modulus-telescope, two-sided-orbit).
  Answer f(x)=x+c, c>=0. current.md Status=solved with Full proof.
### Broken
- (none) — problem solved.
### Next
- Goal achieved. If continuing: could build modulus-derivative for a 3rd independent proof,
  or polish exposition. No open gaps.
