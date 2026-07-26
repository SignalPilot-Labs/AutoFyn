## Goal

Solve `imo-2026-05`: Determine all functions `f : R_{>0} -> R_{>0}` such that
`sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x f(y))` for every `x,y > 0`.

- Metric: proof-reviewer verdict on the problem workspace.
- Eval: status in `results/imo-2026-05/current.md` (`## Status`) + ranking in `results/imo-2026-05/approaches/.ranking.json`.
- Baseline: no approaches exist yet (round 1) — Status `unsolved`, empty population.
- Target: `solved` (proof-reviewer APPROVE) — a complete, rigorous proof characterizing all such `f`, with every case covered and the answer verified by substitution.
- Constraints: prose Markdown proof, no Lean; rigor rules in CLAUDE.md enforced (name tools, verify final answer, prove upper bound + construction).

Domain: algebra (functional equation, QM-AM-GM sandwich). answer_type: characterization.

## Goal Updates

- [2026-07-25] Task started: solve `imo-2026-05`. (Round 1.)

## Eval History

- Round 1 (baseline): No approaches yet. Status `unsolved`. Population empty.
- Round 1 (final): BREAKTHROUGH — Status `solved`. Answer: f(x)=x+c, c>=0. Three approaches built:
  - `diagonal-diophantine-kill` — APPROVE (verified-milestone). (L+R,L−R) sign-decomp → master bound (★); irrational Kronecker + rational Frobenius kills; d1=0 edge closed via maximal-zero-interval + boundary perturbation. Elo 1546.
  - `lipschitz-connectedness` — APPROVE (verified-milestone). (★) as estimate → limit-at-∞ via Dirichlet (|g(a)−β|≤9β²/16a) → value set {0,β} → both level sets open (Z via O(h²); P via quadratic-sign) → connectedness. Elo 1515.
  - `swap-cross-inequalities` — CHANGES REQUESTED (partial, dead-end diagnosed). Cross-inequalities derived non-circularly (universal QM≥AM, not swapped hypothesis) but forcing step strictly weaker than (★): no amplifying linear factor. Subsumed by 1/2. Elo 1485.
  - `algebraic-sos-elimination` — registered, not built (long shot). Elo 1454.
  - Full proof written to `results/imo-2026-05/current.md`; 6 lemmas certified in `lemmas/`.

## Rules

- ALWAYS: one problem per run — `imo-2026-05` fixed for the whole run (CLAUDE.md).
- ALWAYS: read `results/imo-2026-05/current.md` + live `approaches/<slug>.md` + `knowledge_base.md` before attempting (CLAUDE.md working rule).
- ALWAYS: rank every round via outline-reviewer; no fast-path skip (CLAUDE.md).
- NEVER: split one proof across slugs — each slug is a whole rival attempt end-to-end (CLAUDE.md single-gap trap).
- ALWAYS: push diversity of *framing* across the field, not technique variations on one framing (CLAUDE.md single-gap trap).

## State

### Done
- Round 1 setup: read CLAUDE.md, problem statement, knowledge_base.md; created `results/imo-2026-05/` workspace.
- Round 1 full cycle: 3 explorers (parallel, distinct framings) → outliner (5-slug field) → outline-reviewer (ranked, build set of 3) → 3 builders (parallel) → proof-reviewer. Result: SOLVED — 2 APPROVE proofs (diagonal-diophantine-kill, lipschitz-connectedness), 1 partial dead-end (swap-cross-inequalities, subsumed). Full proof in `current.md`.

### Broken
(none)

### Next
- Goal achieved (solved). If a future round is forced: harden/strengthen the winning proofs if any hidden gap surfaces on re-read; otherwise attempt `algebraic-sos-elimination` for an independent confirmation, or stop.
