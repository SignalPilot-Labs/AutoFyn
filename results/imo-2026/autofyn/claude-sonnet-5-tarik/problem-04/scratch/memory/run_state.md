## Goal

Solve IMO 2026 Problem 4 (`problem_id: imo-2026-04`, the Shan-Yu/Mulan triangle-cutting
game — "for which θ can Mulan guarantee victory"). User explicitly named this problem,
overriding the repo's default "hard difficulty_level only" scoping (this problem is
labeled `difficulty_level: medium`, `difficulty_rating: 7` in problems.jsonl, but the
user's direct request takes priority per orchestrator instructions).

Metric: `results/imo-2026-04.md` exists with `## Status` = `solved`, containing a full,
rigorous, proof-reviewer-approved characterization of all θ for which Mulan wins,
including both the winning strategy (for θ in the winning set) and the proof that
Shan-Yu can force a draw/loss for Mulan (for θ outside it).

Eval command: `cat results/imo-2026-04.md | grep -A1 '^## Status'`
(solved iff Status line reads `solved` AND proof-reviewer's last verdict was APPROVE)

Baseline: no results/ file exists. Status: unsolved.

**STATUS AS OF ROUND 3: SOLVED, APPROVED. Goal achieved.**

## Goal Updates

- [2026-07-16] Initial user task: solve IMO 2026 P4 (imo-2026-04), the Mulan/Shan-Yu
  triangle game. Full statement in problems.jsonl under problem_id imo-2026-04.

## Eval History

- Round 1: unsolved. math-explorer did reconnaissance only — derived the angle-split
  formulas L(t)=(t,β,α+γ−t), R(t)=(α−t,γ,β+t) and a "guaranteed-bisection lemma"
  (bisecting angle 2θ forces θ into both children). No case split of θ attempted yet.
  Round ended before outliner produced a strategy.
- Round 2: unsolved, PLATEAU/no artifact change — proof-outliner went idle for 919s
  (likely a hanging/long-running Bash or sympy computation) and was force-interrupted,
  ending the round early with no new progress recorded in results/imo-2026-04.md.
- Round 3: SOLVED — BREAKTHROUGH. math-explorer found a stronger "forced-move" lemma
  (attacking any angle α>θ with split t=θ forces Shan-Yu into a deterministic
  complementary branch (α−θ,γ,β+θ), since he must avoid the θ-containing branch to
  avoid instant loss) and noticed this preserves residues mod θ — the key structural
  clue. proof-outliner used this to conjecture and outline the full characterization:
  **Mulan wins iff θ = 180°/n for some integer n ≥ 2**; otherwise Shan-Yu survives
  forever via a residue-mod-θ invariant. outline-reviewer verdict: CHANGES REQUESTED
  (technique sound, 4 fixable gaps: room-condition reapplication, explicit Shan-Yu
  initial-triangle construction, symmetry of congruence lemma across vertices,
  immateriality of β/γ labeling). proof-builder closed all 4 gaps, caught and fixed a
  real termination bug in a naive re-implementation via simulation (592 + 200k random
  trials, 0 counterexamples), wrote the full rigorous proof with worked examples
  (θ=90°,60° winning; θ=50°,180/√2 survival), set Status=solved. proof-reviewer
  independently re-derived every identity (sympy + ~185k + ~25k Monte Carlo trials in
  exact Fraction arithmetic, including simulating the actual winning algorithm to
  confirm termination), found only 2 minor non-blocking presentation notes. Verdict:
  **APPROVE, solved**.

## Rules

- ALWAYS treat a user-named specific problem_id as in-scope for the round even if its
  difficulty_level is not "hard" — user messages override default CLAUDE.md scoping
  (round 1).
- ALWAYS instruct math-explorer / proof-outliner / proof-builder to keep any Bash/sympy
  verification scripts short (a few lines, seconds to run) and avoid open-ended
  simulations or searches — a proof-outliner hung for 15+ minutes on (presumably) a
  long-running computation in round 2 and was force-interrupted, losing the round.
  Builders/reviewers CAN and productively do use larger Monte-Carlo verification passes
  (round 3's builder and reviewer both ran tens/hundreds of thousands of randomized
  trials successfully without hanging) — the risk is specifically *unbounded/open-ended*
  loops or interactive waits, not "large but finite and scripted" verification.
  Recommend agents write a script to a file and run it with a Bash timeout rather than
  an inline unbounded loop.
- For two-player pursuit/combinatorial-game problems on a continuous parameter (angles,
  reals), look for a "forced move" — a move where one branch is an instant win, so the
  opponent has no real choice — before assuming the game is fully adversarial at every
  step. This was the key unlock in round 3 for imo-2026-04 and may generalize to other
  game-theory problems in the benchmark.
- Residue/invariant-mod-constant arguments (tracking a quantity mod θ, mod n, etc.) are
  a strong tool for the "impossibility/survival" half of two-sided characterization
  problems — confirmed productive in round 3.

## State

### Done
- Round 1: math-explorer reconnaissance on imo-2026-04 (angle-split formulas,
  bisection lemma, crux corpus search — no analogue found).
- Round 2: attempted proof-outliner on imo-2026-04; force-interrupted (stuck), no
  artifact progress.
- Round 3: Solved imo-2026-04 end-to-end. math-explorer (forced-move lemma) →
  proof-outliner (full characterization outline, θ=180°/n) → outline-reviewer
  (CHANGES REQUESTED, 4 gaps) → proof-builder (closed all gaps, Status=solved) →
  proof-reviewer (APPROVE). results/imo-2026-04.md now contains the complete,
  reviewer-approved proof.

### Broken
(none — imo-2026-04 is solved and approved)

### Next
The user's explicitly-named goal (imo-2026-04) is achieved and approved. If further
rounds are run, default back to CLAUDE.md's standard scope: pick 1-3 of the 39
`difficulty_level: "hard"` problems from problems.jsonl not yet solved, and run the
math-explorer → proof-outliner → (outline-reviewer) → proof-builder → proof-reviewer
pipeline on each in parallel. Check results/ for existing partial/unsolved hard-problem
files before choosing which to attack first.
