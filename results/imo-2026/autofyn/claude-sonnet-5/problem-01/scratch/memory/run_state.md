## Goal

Solve IMO 2026 Problem 1 (`imo-2026-01`), the "Confucius gcd/lcm blackboard" problem.

Statement: 2026 integers >1 on a blackboard. A move picks two integers m>1, n>1 from different
places and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n). Moves continue while possible.
(a) Prove that after finitely many moves, exactly one integer M on the board is >1.
(b) Prove M does not depend on the choices made.

Metric: `results/imo-2026-01/current.md` `## Status` field (unsolved | partial | solved), gated by
proof-reviewer APPROVE verdict for `solved`.
Eval: read `results/imo-2026-01/current.md` and `results/imo-2026-01/approaches/.ranking.json` each round.
Baseline: unsolved, no approaches yet (round 1 start).
Target: Status = solved, with a complete rigorous proof of both (a) and (b), APPROVE from proof-reviewer.

Constraint note: `problems.jsonl` lists `imo-2026-01` as `difficulty_level: "medium"` (`difficulty_rating: 5`),
not one of the 39 "hard" problems CLAUDE.md scopes runs to by default. The user explicitly named this exact
problem_id in their task instruction, so this run is scoped to it per the user's explicit override of the
default hard-only policy (user messages take highest priority per orchestrator instructions).

## Goal Updates

## Eval History

- Round 1: 3 math-explorers (prime-valuation, majorization, computational lenses) independently
  converged on the same correct core: invariant g_p = gcd of p-adic valuations across the board
  (proven via gcd(min(a,b),|a-b|)=gcd(a,b)), lexicographic (Omega_total, #active) termination
  monovariant, closed form M = prod_p p^{g_p}. Verified against ~2500+ combined random simulations.
  proof-outliner put up 2 diverse approaches (prime-valuation-invariant; confluence-newman via
  Newman's Lemma / rewriting-system confluence). outline-reviewer APPROVEd both into the build set
  (Elo 1516 vs 1484). Both proof-builders produced Status=solved proofs. proof-reviewer
  adversarially reviewed both independently (re-derived key identities, ran Monte Carlo + exhaustive
  small-board simulations) and APPROVEd both as complete and correct. results/imo-2026-01/current.md
  Status = solved, Full proof populated from prime-valuation-invariant (the more direct of the two).
  BREAKTHROUGH: solved in round 1.

## Rules

- ALWAYS treat `imo-2026-01` as the fixed problem for this entire run — user explicitly requested it,
  overriding the repo default of hard-only problems (round 1).
- NEVER re-attempt imo-2026-01 — it is solved (proof-reviewer APPROVE on both approaches, round 1).
  Full proof lives in results/imo-2026-01/current.md.

## State

### Done
- Round 1: read CLAUDE.md, problems.jsonl entry for imo-2026-01, set up results/imo-2026-01/ workspace
  (current.md, approaches/, lemmas/), installed numpy/scipy/sympy, wrote goal to run_state.md.
- Round 1: ran full explore -> outline -> outline-review -> build -> review pipeline once; problem
  imo-2026-01 fully solved and verified. Two independently-correct complete proofs on file
  (prime-valuation-invariant, confluence-newman), two certified lemmas cached in
  results/imo-2026-01/lemmas/ (euclidean-subtraction-identity.md, multiset-gcd-invariance.md).

### Broken
(none)

### Next
- Goal achieved. results/imo-2026-01/current.md Status = solved with complete rigorous proof of
  both (a) and (b), M = prod_p p^{gcd_i v_p(x_i)}. No further rounds needed for this run's goal
  unless the user provides a new target problem.
