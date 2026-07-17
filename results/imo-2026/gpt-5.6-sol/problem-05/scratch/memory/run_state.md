## Goal
Solve `imo-2026-05` with a complete rigorous characterization proof in `results/imo-2026-05/current.md`.
Metric: proof-reviewer verdict and workspace status. Eval: inspect `results/imo-2026-05/current.md` `## Status`, inspect `results/imo-2026-05/approaches/.ranking.json`, and run the proof-reviewer on every built approach. Baseline: workspace absent; status unsolved; no ranked approaches. Target: proof-reviewer APPROVE, `current.md` status `solved`, explicit characterization stated and every candidate verified. Constraints: prose Markdown; use both `knowledge_base.md` and the algebra crux corpus; follow all rigor and one-approach-per-slug rules in `CLAUDE.md`.

## Goal Updates

## Eval History
- Round 1 baseline: `results/imo-2026-05/` absent; status unsolved; no ranked approaches.
- Round 1 — BREAKTHROUGH: Raw Goal Progress: 100/100 — complete classification, necessity, and direct sufficiency verification. Proof-reviewer verdict APPROVE; `current.md` status `solved`. Ranking: `orbit-displacement-approximation` Elo 1516, expanded 1, outcome `verified-milestone`; `cone-graph-rigidity` Elo 1484.

## Rules
- ALWAYS: consult both `knowledge_base.md` and the algebra crux corpus before developing approaches (because both retrieval resources are mandatory, round 1).
- ALWAYS: maintain whole-problem rival approaches with genuinely different framings (because technique-only variants create a shared-gap trap, round 1).
- ALWAYS: state and directly verify every candidate function (because this is a characterization problem, round 1).
- NEVER: infer continuity of the function from local-looking inequalities without a proved continuity or open-fiber argument (because no regularity is assumed, round 1).
- ALWAYS: quantify nearest-integer orbit alignment, including eventual nonnegativity of orbit indices (because this is the load-bearing rigidity step, round 1).

## State
### Done
- Round 1 setup: installed numpy, scipy, and sympy; established the absent-workspace baseline.
- Scouted three distinct framings and opened four rival whole-problem approaches.
- Ranked the initial population; selected `orbit-displacement-approximation`.
- Built and adversarially verified a complete proof classifying all solutions as `f(x)=x+c` for `c>=0`.
- Published the proof to `results/imo-2026-05/current.md`; reviewer certified the shared `orbit-cone-rigidity` lemma.

### Broken
- None. Goal achieved.

### Next
- End the session with the solved workspace.
