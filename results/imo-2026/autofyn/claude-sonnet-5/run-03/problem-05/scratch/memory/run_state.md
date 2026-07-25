## Goal

Solve IMO 2026 P5, problem_id `imo-2026-05`.

Statement: Determine all functions f: R_{>0} -> R_{>0} such that
sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x f(y))
for every x, y in R_{>0}.

Domain: algebra. difficulty_rating 8, difficulty_level hard. task: compute_and_prove, answer_type: characterization.

Eval: Status field in results/imo-2026-05/current.md must reach `solved` with a proof-reviewer APPROVE verdict on a complete, rigorous proof (characterization of all f — must prove the candidate(s) satisfy the inequalities AND prove no other function works, per CLAUDE.md rigor rules for characterization/find-all problems).

Baseline: unsolved, no approaches yet (fresh run, round 1 setup).

Target: solved, APPROVE.

Constraint: Follow CLAUDE.md workflow strictly (math-explorer -> proof-outliner -> outline-reviewer -> proof-builder -> proof-reviewer, per-approach routing, one problem per run: imo-2026-05).

## Goal Updates
(none — goal unchanged since round 1 start)

## Eval History

Round 1: Status went unsolved -> solved. Answer: f(x) = x + c for arbitrary constant c >= 0.
All 4 build-set approaches (extremal-sup-inf, cross-substitution-fixed-point,
orbit-telescoping-aimo0710, monotonicity-order) independently produced complete, correct proofs;
proof-reviewer APPROVEd all four after adversarial verification (hand + sympy cross-checks,
numerical spot-checks of sufficiency). current.md Full proof synthesized from the
cross-substitution-fixed-point closing argument (cleanest: finite telescoping/partition bound,
no continuity/monotonicity/orbit machinery needed). BREAKTHROUGH — full solve in round 1.

## Rules

- ALWAYS verify the "obvious" answer (e.g. f(x)=x alone) isn't the full solution set before locking
  in an approach's target — round 1 explorers initially expected f(x)=x but the true answer is the
  family f(x)=x+c, c>=0; an approach assuming uniqueness of the identity would have been wrong.
  (round 1)
- ALWAYS have explorers/outliners re-verify shared "proven" base-layer claims (e.g. algebraic
  collapses from key substitutions) independently/symbolically (sympy) rather than trusting the
  first explorer's derivation — cheap insurance against a shared-gap trap propagating through the
  whole field. (round 1)
- NOTE: parallel builders can leave sibling hints in /tmp/memory/proof-builder.md within the same
  round that meaningfully help each other close gaps faster (observed round 1: a hint about a
  two-sided pointwise bound let one builder replace a partial orbit/pigeonhole argument with a
  full finite-telescoping closure). Encourage builders to check that file mid-build. (round 1)

## State

### Done (round 1)
- Setup: installed numpy/scipy/sympy, created results/imo-2026-05/{approaches,lemmas}/ + current.md.
- 3 math-explorers (substitution, bounding, extremal lenses) converged independently on: x=f(y)
  substitution collapses sandwich to exact FE f(f(y))=2f(y)-y; g(y):=f(y)-y >= 0; injectivity;
  orbit-invariance g(f(y))=g(y); true answer family is f(x)=x+c for c>=0 (verified via SOS
  identity (x-y-c)^2>=0), not just f(x)=x.
- proof-outliner opened 4 approaches sharing the verified base layer, diverging on how to close
  the "g is a global constant" gap: extremal-sup-inf, cross-substitution-fixed-point,
  orbit-telescoping-aimo0710, monotonicity-order.
- outline-reviewer re-verified base layer + new cross-inequality tool by hand/sympy; APPROVEd 3,
  CHANGES REQUESTED on monotonicity-order (found numeric counterexample to its step-3 mechanism);
  build set was all 4 (with monotonicity-order builder told to fix the flagged gap first).
- All 4 proof-builders independently produced complete proofs; monotonicity-order builder fixed
  its flagged mechanism using both inequalities + a 3-point/limiting argument.
- proof-reviewer adversarially verified all 4 (hand + sympy re-derivation of every identity,
  numerical spot-checks of sufficiency/failure cases) and APPROVEd all 4. Updated
  results/imo-2026-05/current.md to Status: solved with a complete Full proof (chosen from
  cross-substitution-fixed-point's closing argument as cleanest).

### Broken
(none)

### Next
Problem is solved (Status: solved, APPROVE). Per CLAUDE.md "never re-attempt a solved problem" —
no further rounds needed for imo-2026-05 unless the user requests re-verification or a different
problem. Ready to end_session.
