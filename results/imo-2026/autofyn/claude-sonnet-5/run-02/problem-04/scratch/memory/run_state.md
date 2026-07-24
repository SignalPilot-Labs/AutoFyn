## Goal

Solve IMO 2026 P4 — problem_id `imo-2026-04` (user explicitly requested this problem by name;
note it is tagged `difficulty_level: "medium"` in problems.jsonl, not one of the 39 "hard" ids,
but the user's explicit instruction overrides the default hard-only filter for this run).

Statement: Shan-Yu and Mulan play a game with angle θ (0°<θ<180°) known to both. Shan-Yu picks
a triangle T. Repeat: if T has an angle exactly θ, Mulan wins. Otherwise Mulan picks a point P
on the perimeter (not a vertex) and cuts from P to the opposite vertex, splitting T into two
triangles; Shan-Yu discards one, the other becomes the new T. For which θ can Mulan guarantee
victory in finitely many steps regardless of Shan-Yu's play?

Task type: compute_and_prove / answer_type: characterization — need explicit characterization
of θ plus full proof (winning strategy construction for those θ, and a strategy for Shan-Yu /
invariant showing impossibility for other θ).

Eval command: dispatch proof-reviewer each round on results/imo-2026-04/approaches/<slug>.md;
overall solved status tracked in results/imo-2026-04/current.md ## Status.
Baseline (round 1 start): unsolved, no approaches yet, current.md just initialized.
Target: current.md ## Status = solved with a complete, rigorous ## Full proof (characterization
of θ proven both directions, no gaps, no skipped cases).

**ANSWER (proven, round 2): Mulan can force a win in finitely many moves from every starting
triangle iff θ = 180°/n for some integer n≥2.**

Workspace: results/imo-2026-04/ (approaches/, lemmas/, current.md) created round 1.

## Goal Updates

## Eval History

- Round 1 baseline: current.md Status = unsolved, no approaches registered yet.
- Round 1: explorers + outliner + outline-reviewer ran; build set emitted:
  interval-partition-topological, resonance-lattice-invariant, algebraic-independence-generic.
  Two builders completed (interval-partition-topological, resonance-lattice-invariant both
  self-reported Status: solved) before a third proof-builder (algebraic-independence-generic)
  went stuck/idle 925s and was force-killed, ending the round before proof-reviewer ran.
- Round 2: BREAKTHROUGH — SOLVED. Dispatched proof-reviewer on the two completed round-1
  candidates in parallel with re-dispatching proof-builder for the stuck slug.
  proof-reviewer APPROVEd both interval-partition-topological and resonance-lattice-invariant
  as complete, correct, independently-derived proofs of the same characterization
  (θ=180/n, n≥2 integer) — cross-validated each other. current.md Status set to solved with
  full proof written. Third approach (algebraic-independence-generic) also independently
  completed a full proof reaching the same answer (not yet reviewer-verified, but redundant
  given the two APPROVEs). Goal achieved; session ended round 2.

## Rules

- ALWAYS give proof-builder explicit instructions to avoid unbounded/large random-trial or
  brute-force Bash/sympy searches with no timeout — this caused a stuck-agent force-kill in
  round 1 (925s idle). Prefer small, fast (seconds), exact-candidate sanity checks over
  loose-tolerance grid scanning, which produces spurious counterexamples for measure-zero
  lattice conditions (round 2 proof-reviewer finding).
- ALWAYS check whether prior-round approach files already have Status: solved with content
  written before assuming a round needs fresh building — a round can be interrupted (stuck
  agent) after builders finish but before proof-reviewer runs, leaving completed but
  unreviewed proofs on disk. Check file content/mtimes, not just current.md, before re-scoping.
- Two independently-derived, mutually cross-validating APPROVEd proofs reaching the identical
  characterization is strong evidence of correctness — used as the basis for ending the run.

## State

### Done
- Round 1: set up results/imo-2026-04/{approaches,lemmas}/, current.md initialized (unsolved).
- Round 1: pip installed numpy/scipy/sympy for computational exploration.
- Round 1: math-explorer x3, proof-outliner, outline-reviewer ran; build set of 3 slugs emitted;
  2 of 3 builders completed (self-reported solved) before round ended early (stuck 3rd builder).
- Round 2: proof-reviewer APPROVEd interval-partition-topological and resonance-lattice-invariant
  as complete correct proofs; current.md Status -> solved with full proof written.
- Round 2: proof-builder completed algebraic-independence-generic (also solved, unreviewed
  but redundant/consistent with the two approved proofs).
- Round 2: end_session called — goal achieved.

### Broken
(none)

### Next
(none — problem solved, session ended)
