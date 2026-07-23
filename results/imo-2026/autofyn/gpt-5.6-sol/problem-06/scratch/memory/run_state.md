## Goal
Solve `imo-2026-06` with a complete rigorous prose proof recorded in `results/imo-2026-06/current.md` and independently approved by the proof-reviewer.

Metric: approach population ranking and proof-review verdict. Eval: read `results/imo-2026-06/approaches/.ranking.json` plus `results/imo-2026-06/current.md` `## Status`; target is `solved` with at least one APPROVE and a gap-free `## Full proof`. Constraints: one complete attempt per slug; consult both knowledge resources; no skipped cases, hand-waving, or unproved claims.

Baseline (round 1): no `results/imo-2026-06/` workspace, no ranking entries, no proof, status effectively unsolved.

## Goal Updates

## Eval History
- Round 1 baseline: workspace absent; approach population empty; Status `unsolved`; no reviewer verdict.
- Round 1 — BREAKTHROUGH: `p-position-small-prime-classification` Elo 1516, outcome `verified-milestone`; `translation-equivariant-greedy-set` Elo 1484, unbuilt; `current.md` Status `solved`. Proof-reviewer Goal Progress: "The problem is fully solved. The proof supplies explicit positive T,L, establishes the exact recurrence for all positive indices, and leaves no unresolved case or lemma."

## Rules
- ALWAYS: separate finite-state periodicity from the missing finite-basis/finite-witness theorem; bounded gaps alone do not imply periodicity (because all three round-1 scouts identify stabilization as the genuine bottleneck, round 1).
- NEVER: assume all terms share one prime or that primes of `a_1` alone witness every pair (because seed 15 is a counterexample, round 1).
- NEVER: infer stabilization merely from monotonicity of constraints or per-stage periodicity (because infinitely many constraints or primes may enter, round 1).
- ALWAYS: when identifying a recursively generated greedy set with P-positions, prove the least candidate has no intervening P-position before invoking the P/N recursion (because compatibility with earlier P-positions alone does not identify the next one, round 1).
- ALWAYS: re-derive strict stripping/descent inequalities and test both mixed-status orientations (because these are the load-bearing steps of the approved proof, round 1).

## State
Done:
- Read project instructions, benchmark documentation, knowledge base, and crux corpus documentation; installed required scientific packages.
- Scouted three distinct framings, outlined four rival approaches, and ranked them.
- Built `p-position-small-prime-classification`: reformulated the sequence as P-positions in a decreasing coprimality game, proved the small-common-prime theorem by prime stripping and descent, established small-prime-signature invariance, and deduced exact translation by the primorial.
- Proof-reviewer independently verified every load-bearing step, returned APPROVE with 10/10 scores, updated `current.md` to solved, recorded the ranker outcome, and certified two reusable lemmas.
- Added `.claude/worktrees/` to `.gitignore` so subagent worktrees are not committed as artifacts.

Broken:
- None. The target is achieved with an approved complete proof.

Next:
- End the session; no further mathematical work is needed.
