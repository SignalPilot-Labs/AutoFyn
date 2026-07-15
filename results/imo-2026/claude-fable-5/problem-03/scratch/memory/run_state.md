## Goal

Solve problem `imo-2026-03` (Math Contests 2026 benchmark, IMO 2026 P3, combinatorics game, difficulty 9).
- Metric: `results/imo-2026-03/current.md` `## Status` reaching `solved` (proof-reviewer APPROVE) with the explicit answer c(n) stated and both bounds proven (strategy for Liu Bang achieving c AND strategy for Xiang Yu preventing more than c).
- Eval: read `results/imo-2026-03/current.md` Status + `results/imo-2026-03/approaches/.ranking.json` each round.
- Baseline (round 1): no workspace, Status effectively `unsolved`, 0 approaches.
- Target: Status `solved`.
- Constraint: answer_type = expression — must state c as an explicit expression in n and verify small cases (n=1, n=2) by computation.

## Goal Updates

- [2026-07-15 round 1] Initial user message: solve imo-2026-03.

## Eval History

- Round 0 baseline: unsolved, no approaches.
- Round 1: **SOLVED — BREAKTHROUGH.** c(n) = 2^n/(2^{n+1}−1). Reviewer Goal Progress: pairing-defect-strategy-family APPROVE (solved, Elo 1517, outcome verified-milestone), self-similar-induction APPROVE (solved, verified-milestone), exact-value-function CHANGES REQUESTED (partial, gaps E2/E3′ subsumed by solved siblings, Elo 1469). current.md Status = solved with Full proof; 5 certified lemmas in lemmas/. Reviewer independently re-derived every load-bearing step and verified computationally (exact rationals n=1..4, minimax grid n=1 → 2/3).

## Rules

- ALWAYS: verify small cases computationally before committing to a conjectured formula — three independent explorer lenses converging on c(n)=2^n/(2^{n+1}−1) made the round efficient (round 1).

## State

- Done: Round 1 — full pipeline (3 explorers → outliner → outline-reviewer → 3 builders → proof-reviewer). Problem SOLVED with two independently verified complete proofs; answer c(n) = 2^n/(2^{n+1}−1). Workspace results/imo-2026-03/ complete (current.md solved + full proof, 3 approach files, 5 certified lemmas, .ranking.json).
- Broken: —
- Next: nothing — goal achieved; end session.
