## Goal
Solve problem `imo-2026-01` (user-selected; overrides hard-only default) with a complete, rigorous prose proof.
- Metric: `results/imo-2026-01/current.md` `## Status` = solved (proof-reviewer APPROVE), covering both parts (a) and (b).
- Eval: read `results/imo-2026-01/current.md` Status + `results/imo-2026-01/approaches/.ranking.json` each round.
- Baseline (round 1): workspace empty, Status unsolved, no approaches.
- Constraints: prose Markdown proof, rigor rules in CLAUDE.md; population of rival approaches under `results/imo-2026-01/approaches/`.

Problem: 2026 integers >1 on a blackboard. Move: pick m>1, n>1 from different places, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). (a) Prove termination with exactly one integer M>1. (b) Prove M independent of choices.

## Goal Updates
- [2026-07-17] User: solve imo-2026-01. (Run fixed to this problem.)

## Eval History
- Round 0 baseline: unsolved, empty workspace.
- Round 1: **SOLVED — BREAKTHROUGH.** Both approaches APPROVE (per-prime-gcd-invariant Elo 1516, newman-confluence Elo 1484, both verified-milestone). current.md Status = solved with Full proof (M = ∏_p p^{gcd_i v_p(a_i)} via invariant gcd(a,b)=gcd(min(a,b),|a−b|); termination via lex monovariant). 7 certified lemmas. Reviewer numerical checks: 1200 runs + 5000 overlap triples + 2000 monovariant moves, zero failures.

## Rules
- ALWAYS: for process/invariant problems, run empirical simulation early to pin the conjectured formula before outlining (worked round 1).

## State
Done: Round 1 — full flow (3 explorers → outliner → outline-reviewer → 2 builders → reviewer). Problem solved, both rival approaches independently complete and APPROVED.
Broken: nothing.
Next: nothing — goal achieved; session ended round 1.
