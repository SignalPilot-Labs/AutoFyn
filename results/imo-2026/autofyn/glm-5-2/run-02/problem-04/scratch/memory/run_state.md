## Goal

Solve IMO 2026 Problem 4 (Mulan's triangle game): characterize all real θ ∈ (0°, 180°) for which Mulan can guarantee victory in finitely many steps regardless of Shan-Yu's play. Problem id: `imo-2026-04`. answer_type=characterization, task=compute_and_prove.

- Metric: proof-reviewer verdict on `results/imo-2026-04/current.md` (solved = APPROVE with complete characterization + proof of both directions).
- Eval command: read `results/imo-2026-04/current.md` `## Status` + `results/imo-2026-04/approaches/.ranking.json`.
- Baseline: round 1 — no approaches yet, Status `unsolved`.
- Target: Status `solved` — complete rigorous proof: the set of θ explicitly stated, Mulan winning-strategy construction, AND Shan-Yu defense for the complement, both proven.
- Constraints: prose Markdown, no Lean; rigor rules (no skipped cases, name tools, verify final answer, prove both directions of characterization).

## Goal Updates

- [2026-07-25] Task: solve imo-2026-04 (user). Problem is medium difficulty_rating 7 but explicitly requested by user — solve it.

## Eval History

- Round 1 baseline: Status `unsolved`, no approaches registered, Elo pool empty.
- Round 1 result: BREAKTHROUGH — Status `solved`. proof-reviewer APPROVED `mod-theta-descent` (verified-milestone): full both-directions proof, no gaps. Answer: Mulan wins ⇔ θ = 180°/N for integer N ≥ 2. IF: create-move + k-descent, ≤N−1 moves, all N≥2 (incl. non-integer-degree θ). ONLY: four-case mod-θ obstruction "no angle ≡ 0 mod θ" invariant, exhaustive, covers rational-non-unit & irrational θ. `geometric-anchor` = partial (dyadic IF only, CHANGES REQUESTED — non-blocking). Leader Elo 1546. Field: 4 approaches registered (mod-theta-descent, fixpoint-attractor, torsion-subgroup, geometric-anchor); 3 share one wall.

## Rules

- ALWAYS: this is a math repo — `pip install numpy scipy sympy`, no package.json/pyproject (CLAUDE.md).
- ALWAYS: one problem per run (`imo-2026-04`), workspace `results/imo-2026-04/` (CLAUDE.md).
- ALWAYS: full flow every round: math-explorer ×(1–3) → proof-outliner ×1 → outline-reviewer ×1 → proof-builder ×(1–N) → proof-reviewer ×1.
- ALWAYS: outline-reviewer ranks every round; no fast-path skip (CLAUDE.md).
- ALWAYS: explorers scout genuinely different framings (different routes to the whole problem), not just different lenses on one.
- ALWAYS: report paths canonical — `/tmp/round-{N}/<agent-name>.md`; explorers write `/tmp/round-{N}/math-explorer-<lens>.md`.
- ALWAYS (round 1): for continuous-strategy angle games, the reliable engine is the least-fixpoint attractor with modular θ-arithmetic (180/θ ∈ ℤ), NOT fixed degree-grid search — grids cannot represent non-integer θ (e.g. 180/7) and mislabel it (the defense explorer's grid produced the WRONG "3-smooth only" answer; the exact integer-grid attractor was reliable only because it tested integer θ).
- ALWAYS (round 1): for triangle-cut games the angle-triple transform on a cut from vertex A to point on BC is child1=(α,B,180−α−B), child2=(A−α,C,B+α) — verify numerically before using (the naive {α,B,180−β} form does NOT sum to 180).
- ALWAYS (round 1, reviewer finding): the field COLLAPSED to one framing — 3 of 4 approaches (mod-theta-descent, fixpoint-attractor, torsion-subgroup) are the same proof re-skinned around the shared create-move + four-case-obstruction wall. Next round's outliner must put ≥1 approach on a genuinely different framing (independent route to the ONLY direction) if any strengthening is attempted; copying is the single-gap trap.
- NEVER (round 1, pruned): re-propose "3-smooth reciprocals 180/(2^a·3^b)" or "θ=36 is a loss" — DISPROVEN outlier; solved answer is θ=180/N for all integer N≥2.

## State

### Done
- Round 1 setup: installed numpy/scipy/sympy; created workspace `results/imo-2026-04/{approaches,lemmas}`; seeded `current.md`.
- Round 1 flow: 3 explorers (constructive/defense/retrieval, parallel, disagreeing) → outliner (4 approaches) → outline-reviewer (ranked, build set = mod-theta-descent + geometric-anchor) → 2 builders (parallel) → proof-reviewer.
- Round 1 RESULT: `mod-theta-descent` APPROVED → Status `solved`. Answer: θ = 180°/N, integer N ≥ 2. Full proof in `current.md` `## Full proof`; shared lemmas in `lemmas/{mod-theta-obstruction,dyadic-if}.md`. Pruned 2 incorrect defense-explorer rules from `/tmp/memory/math-explorer.md`.

### Broken
- `geometric-anchor`: partial, CHANGES REQUESTED (dyadic IF only; defers non-dyadic IF + entire ONLY direction). Non-blocking — can import certified obstruction + create-move to extend, or leave as scoped insurance.

### Next
- Problem is SOLVED. If `end_session` is still time-locked, next round = light verification/strengthening pass (e.g., close `geometric-anchor`'s gaps via the certified lemmas, or add an independent ONLY-direction framing to de-risk the single-wall field) — do NOT perturb the certified `mod-theta-descent` proof. Re-attempt `end_session` once time-lock releases.

## Round 2

### Eval History (append)
- Round 2: Status `solved` (held). mod-theta-descent APPROVED (verified-milestone), Elo 1546, stale. Field stable: 4 approaches (1 solved workhorse + 1 dyadic-IF partial + 2 insurance re-skins). Time-lock released → `end_session` accepted. No perturbation to certified proof.

### Done (append)
- Round 2: Re-verified solved state (current.md Status=solved, full both-directions proof intact; ranking intact). Time-lock released; called `end_session` — run concluded. Answer: Mulan wins ⇔ θ = 180°/N, integer N ≥ 2.
