## Goal

Solve IMO 2026 Problem 5 (problem_id: `imo-2026-05`), a "hard" difficulty
functional-inequality problem (task: compute_and_prove, answer_type:
characterization). Statement: determine all f: R>0 -> R>0 such that
sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) for all x,y in R>0.

Metric: `results/imo-2026-05.md` exists with `## Status` = `solved`
(complete rigorous proof, answer stated and verified).
Eval command: `cat results/imo-2026-05.md | grep -A1 '^## Status'`
Baseline: no results file exists (0 solved).
Target: 1/1 (this problem) solved, per repo rigor rules in CLAUDE.md.
Constraint: user explicitly asked for this single problem — focus all
rounds on it exclusively, not the broader 39-hard-problem benchmark, unless
told otherwise.

## Goal Updates

## Eval History

- Round 1: math-explorer conjectured & numerically confirmed answer family
  f(x)=x+c (c>=0), proved FE lemma f(f(y))=2f(y)-y and f(x)>=x via orbit
  argument. proof-outliner closed the remaining gap (global constancy of
  d(x)=f(x)-x) via a quadratic-defect inequality + Archimedean telescoping
  squeeze; outline-reviewer independently verified all algebra with sympy
  and APPROVED. proof-builder wrote the full rigorous prose proof, marked
  solved. proof-reviewer independently re-derived every step from scratch
  (including sympy verification of the key polynomial identity and 20k-trial
  numeric checks of sufficiency) and APPROVED. Verdict: solved, 1/1.
  BREAKTHROUGH — solved in a single round end-to-end (explore -> outline ->
  outline-review -> build -> review, no CHANGES REQUESTED / RETHINK loops).

## Rules

- ALWAYS numerically stress-test a conjectured answer family before locking
  in a narrower guess (e.g. f(x)=x alone would have been wrong here — the
  true answer is the family f(x)=x+c, c>=0; found by 200k-trial random
  numeric checks in round 1).
- ALWAYS look for a "collapse the mean-inequality (QM/AM/GM) chain to
  equality" substitution first on sandwich-type functional inequalities
  (e.g. x=f(y) here) — it tends to yield a clean functional equation for
  free (round 1).
- ALWAYS independently re-derive load-bearing algebraic identities with
  sympy (not just trust the outline/builder's claimed expansion) at both
  the outline-review and proof-review stages — this repo's reviewers doing
  so caught nothing wrong here, but it is the mechanism that makes APPROVE
  trustworthy, per outline-reviewer/proof-reviewer round-1 memory notes.

## State

### Done
- Round 1: Solved imo-2026-05 (IMO 2026 P5) end-to-end. Answer:
  f(x) = x + c for x in R_{>0}, arbitrary constant c >= 0. Full rigorous
  proof (necessity + sufficiency) in results/imo-2026-05.md, Status: solved,
  reviewed and APPROVED by proof-reviewer.

### Broken
(none)

### Next
Goal (solve imo-2026-05) is achieved and verified. No further work planned
unless the user provides a new problem/goal.
