## Goal
Solve `imo-2026-03` with a complete rigorous prose proof and explicit optimal expression for every positive integer n.

Metric: proof-reviewer verdict and approach population ranking. Eval: inspect `results/imo-2026-03/current.md` `## Status` and `results/imo-2026-03/approaches/.ranking.json`, then require a proof-reviewer APPROVE with both guarantee and matching upper-bound strategy verified. Baseline: workspace absent; status unsolved; no ranked approaches. Target: `current.md` status `solved`, complete proof present, at least one candidate receives APPROVE. Constraints: follow CLAUDE.md rigor rules; consult both `knowledge_base.md` and crux corpus; one slug per complete rival route; do not hand-edit ranking sidecar.

## Goal Updates

## Eval History
- Round 1 baseline: `results/imo-2026-03/` absent; status unsolved; no ranked approaches.
- Round 2 BREAKTHROUGH — Raw current Status: `solved`; Raw final expression: `2^n/(2^(n+1)-1)`; Raw ranking record: slug `subset-folding-dyadic-frontier`; Elo `1500.0`; expanded `1`; last outcome `verified-milestone`; last round `2`; stale `true`. Raw ranking note: `Complete minimax proof verified: draft identity, tree-component lower invariant, legal folding cut count, and matching upper bound all check out.` Goal result: complete guarantee and matching obstruction verified; target met.

## Rules
- ALWAYS: Consult both `knowledge_base.md` and the crux corpus before advancing a proof (required by CLAUDE.md, round 1).
- ALWAYS: Prove both Liu Bang's guarantee and Xiang Yu's matching obstruction, and explicitly state the resulting expression (compute-and-prove rigor, round 1).
- NEVER: Hand-edit `approaches/.ranking.json`; only ranking tools may modify it (repository contract, round 1).
- ALWAYS: For split-refinement discrepancy arguments, account for repeated cuts and global rank interleaving explicitly; the certified tree-component multigraph does this (review finding, round 2).
- ALWAYS: For folding constructions, prove interior-mark legality and exact cut counts in all residual/support cases (review finding, round 2).

## State
### Done
- Round 1 setup: installed numpy, scipy, and sympy; identified target statement and confirmed no existing workspace.
- Round 2: explored dyadic, LP-dual, and recursive framings; ranked the field; built `subset-folding-dyadic-frontier`; independently reviewed it twice; obtained APPROVE and status solved.
- Round 2: certified and stored the odd-rank draft, tree-component discrepancy, and consecutive-subset-sum folding lemmas.
- Final proved value: `c_n = 2^n/(2^(n+1)-1)` for every positive integer `n`.

### Broken
- None.

### Next
- Goal achieved; no further proof work required.
