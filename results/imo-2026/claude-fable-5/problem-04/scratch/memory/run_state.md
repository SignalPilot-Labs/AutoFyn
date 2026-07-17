# Run State

## Goal
Solve problem **imo-2026-04** (Mulan's triangle game): determine all θ ∈ (0°,180°) for which Mulan can guarantee producing a triangle with an angle exactly θ, no matter how Shan-Yu plays. Full characterization + rigorous prose proof (both directions).

- Metric: `results/imo-2026-04/current.md` `## Status` + approach ranking.
- Eval: proof-reviewer verdict each round; solved = APPROVE with complete proof.
- Baseline (round 1): no workspace, Status unsolved, zero approaches.
- Constraints: prose Markdown proof, CLAUDE.md rigor rules.
- Note: problem is difficulty_level "medium" but was explicitly requested by user — user request overrides the hard-only default.

## Goal Updates
- [2026-07-17 round 1] User: "solve the problem imo-2026-04." (initial task)

## Eval History
- Round 0 baseline: unsolved, no approaches.
- Round 1: SOLVED — BREAKTHROUGH. Answer: Mulan wins iff θ = 180°/n, integer n ≥ 2 (≤ n−1 cuts). Two APPROVEd independent proofs: `circle-group-quotient` (certified Full proof in current.md) and `residue-divisibility-characterization` (independent verification). Reviewer re-verified via exact-fraction search (necessity at θ = 55, 80, 100, 170, 179, 270/7) and exhaustive game-tree simulation (n = 2..12, bound n−1 attained). Explorers' initial conjecture "θ ≤ 90°" was refuted by the outliner's mod-θ residue invariant (θ = 80° is a Shan-Yu survival).

## Rules
- ALWAYS: distrust discretized-grid game simulations for exact-hit games; verify conjectures with exact-fraction arithmetic (grid rounding produced the false "θ ≤ 90°" conjecture, round 1).

## State
### Done
- Round 1: full pipeline (3 explorers → outliner → outline-reviewer → 2 builders → reviewer). imo-2026-04 solved; current.md Status solved with certified Full proof; lemmas L0–L3 certified into lemmas/.
### Broken
- Nothing.
### Next
- Goal achieved; session ended round 1.
