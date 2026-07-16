# Run State

## Goal

Solve problem **imo-2026-04** (IMO 2026 P4, combinatorics/game, `compute_and_prove`, answer_type: characterization) with a complete rigorous prose proof.

- Metric: `results/imo-2026-04/current.md` `## Status` reaches `solved` (proof-reviewer APPROVE); interim signal = approach ranking in `results/imo-2026-04/approaches/.ranking.json`.
- Eval: read `results/imo-2026-04/current.md` Status + `.ranking.json` each round.
- Baseline (round 1): no workspace, Status = unsolved, 0 approaches.
- Target: Status `solved` — the characterization of all θ must include BOTH directions (Mulan wins for exactly those θ; Shan-Yu survives forever otherwise), per rigor rules.
- Constraints: prose Markdown proof, rigor rules in CLAUDE.md, consult knowledge_base.md + crux corpus (via crux_moves_documentation.md).

Problem statement: Shan-Yu and Mulan play. θ ∈ (0°, 180°) known to both. Shan-Yu makes an arbitrary triangle T. Repeat: if T has an angle exactly θ, Mulan wins. Otherwise Mulan picks P on the perimeter (not a vertex), cuts from P to the opposite vertex, splitting T into two triangles; Shan-Yu discards one; the other becomes T. For which θ can Mulan guarantee victory in finitely many steps?

## Goal Updates

- [2026-07-16 07:34] User: solve imo-2026-04 (explicit id — overrides hard-only default; this problem is difficulty_level medium, rating 7).

## Eval History

- Round 1 baseline: unsolved, no approaches yet. (Round died early: math-explorer stuck 15 min idle, no artifacts.)
- Round 2: **SOLVED — BREAKTHROUGH.** Status: solved. Answer: Mulan wins iff θ = 180°/n, integer n ≥ 2 (within n−1 cuts). Verdicts: remainder-forcing APPROVE (Elo 1516, verified-milestone; cut formula re-derived from coordinates, forcing/descent simulated adversarially n=2..9, 4-case closure checked on 436,422 exact-rational cuts, 0 failures), descending-chain APPROVE (Elo 1484, verified-milestone; independent 3-phase strategy, simulated n=2..12). Lemma `safe-piece-exists` certified. Full proof = remainder-forcing in current.md; descending-chain recorded as independent verified alternative.

## Rules

- ALWAYS: give math-explorers explicit anti-stall instructions (write report incrementally, short Bash calls < 60 s with printed output, no open-ended loops) (because a round-1 explorer was force-killed after 15 min of silence, round 1→2).
- NEVER: revive the doubling-orbit invariant S = {2^k θ} for this problem — refuted by counterexample θ = 40°, T = (120°, 25°, 35°) (recorded in outline-reviewer round 2).

## State

- Done: Round 2 — full pipeline (3 explorers → outliner → outline-reviewer → 2 builders → proof-reviewer). imo-2026-04 SOLVED with two independently verified proofs; both directions of the characterization θ = 180°/n proved; shared lemma certified.
- Broken: nothing.
- Next: nothing — goal achieved; session ended round 2.
