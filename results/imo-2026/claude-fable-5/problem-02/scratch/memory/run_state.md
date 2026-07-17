## Goal

Solve IMO 2026 Problem 2 (problem_id: imo-2026-02, geometry, hard, rating 8).
Statement: Triangle ABC; M, N midpoints of AB, AC. K inside triangle BMC, L inside triangle BNC, with K inside angle LBA, L inside angle ACK, and ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. O = circumcentre of triangle AKL. Prove OM = ON.

- Metric: `## Status` in results/imo-2026-02/current.md (unsolved → partial → solved), plus approach-population Elo in results/imo-2026-02/approaches/.ranking.json.
- Eval: read results/imo-2026-02/current.md Status + .ranking.json each round; headline = proof-reviewer APPROVE (Status solved).
- Baseline (round 1): no workspace existed — Status unsolved, 0 approaches.
- Target: Status = solved (complete rigorous prose proof, reviewer-approved).
- Constraints: prose Markdown proof, rigor rules in CLAUDE.md; one problem for whole run.

## Goal Updates
- [2026-07-17 01:09] Initial task: solve imo-2026-02.

## Eval History
- Round 0 baseline: unsolved, no approaches.
- Round 1: **Status: solved — BREAKTHROUGH.** Proof-reviewer Goal Progress: two independent fully verified proofs APPROVED — `secant-trig-identity` (trig elimination + Key Identity via interpolation, Elo ~1515 tier) and `complex-certificate` (polynomial certificate 2sinA·G = α·ℓ_K + β·ℓ_L, Fourier tables verified symbolically; canonical proof in current.md). `midpoint-reflection-isogonal` partial (Lemmas 1–4 correct, synthetic gap (I) open, CHANGES REQUESTED, frozen). `family-invariance-boundary` unbuilt (Elo 1454). 5 lemmas certified into lemmas/. current.md Status = solved with ## Full proof.

## Rules
- ALWAYS: verify claimed structural conjectures numerically before spending proof effort (round 1: ~15 tempting concyclicity/spiral-similarity guesses refuted cheaply, saved builders from dead ends).
- NOTE: crux corpus has zero geometry entries — don't send geometry agents there (round 1).

## State
- Done: Round 1 — full cycle (3 explorers, outliner opened 4 approaches, reviewer ranked + build set of 3, 3 builders, reviewer). Problem imo-2026-02 SOLVED: two APPROVEd proofs, current.md Status solved, full proof recorded, 5 certified lemmas.
- Broken: nothing.
- Next: nothing — goal achieved. If run continues, optional polish only (e.g. close synthetic gap (I) in midpoint-reflection-isogonal for elegance; not required).
