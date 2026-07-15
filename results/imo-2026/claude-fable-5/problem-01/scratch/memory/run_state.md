## Goal

Solve **imo-2026-01** (IMO 2026 P1, number theory, proof_only, answer_type none).
Statement: 2026 integers >1 on a blackboard; a move picks two entries m>1, n>1 and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n); moves continue while possible. (a) Prove the process always terminates with exactly one integer M>1 left. (b) Prove M is independent of the choices.

- Metric: `## Status` in `results/imo-2026-01/current.md` (unsolved → partial → solved) + approach ranking in `results/imo-2026-01/approaches/.ranking.json`.
- Eval: read `results/imo-2026-01/current.md` Status + `.ranking.json`; solved = proof-reviewer APPROVE on a complete proof of BOTH (a) and (b).
- Baseline (round 1): workspace did not exist — unsolved, no approaches.
- Target: Status `solved`.
- Constraints: CLAUDE.md rigor rules. Prose Markdown, no Lean.
- Note: problem is difficulty_level `medium` (rating 5); user explicitly named it, overriding the hard-only default.

## Goal Updates

- [2026-07-15 05:40] Initial user message: solve imo-2026-01. (recorded)

## Eval History

- Round 0 baseline: unsolved, no workspace.
- Round 1: **SOLVED — BREAKTHROUGH.** current.md Status = solved. Both built approaches APPROVED by proof-reviewer (recorded verified-milestone): prime-gcd-invariant (primary Full proof) and star-monoid-product-descent (certified alternative). Ranking: star-monoid-product-descent 1516.8, prime-gcd-invariant 1514.5, newman-confluence 1468.7 (live, unbuilt). Reviewer independently re-derived the key identity and exhaustively checked all move orders on 87 boards + 25,000 random-move checks: zero violations. M = ∏_p p^{gcd of p-adic exponents of the initial board}.

## Rules

- ALWAYS: give each math-explorer a distinct lens and each proof-builder exactly one slug with explicit "do not touch rival files" (worked cleanly, round 1).
- NEVER: rely on Σ(entries) as a monovariant for this move type — coprime moves increase it; use lex (P, N) or W = N + ΣΩ instead (explorer finding, round 1).

## State

- Done: Round 1 — full flow (3 explorers → outliner → outline-reviewer → 2 builders → proof-reviewer). imo-2026-01 SOLVED: both parts (a) and (b), two independent certified proofs, 4 lemmas certified, current.md carries the Full proof.
- Broken: nothing.
- Next: nothing — goal achieved; end session.
