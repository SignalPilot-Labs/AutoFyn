## Goal
Solve `imo-2026-06` with a complete rigorous prose proof. Metric: proof-reviewer verdict and workspace status/ranking. Eval: read `results/imo-2026-06/current.md` `## Status` and `results/imo-2026-06/approaches/.ranking.json`, with a proof-reviewer APPROVE required. Baseline: workspace absent; status unsolved, no registered approaches/ranking. Target: `current.md` status `solved` with a complete proof and proof-reviewer APPROVE. Constraints: follow `CLAUDE.md`; consult both `knowledge_base.md` and the crux corpus; one complete rival solution per slug; no unproved gaps or skipped cases.

## Goal Updates

## Eval History
- Round 1 baseline — status: unsolved (workspace absent); approaches: 0; ranking: absent.
- Round 1 Goal Progress — The original problem asks only for existence of positive integers $T,L$ satisfying $a_{n+T}=a_n+L$ for every $n\ge1$. Both built approaches prove this with $L=\prod_{p\le a_1}p$ and $T=|G\cap[a_1,a_1+L-1]|$, where $G$ is the recursively defined set of integers having no smaller good coprime witness. Both candidates are complete. The reviewer-owned `results/imo-2026-06/current.md` has Status `solved` and a certified full proof. BREAKTHROUGH.
- Round 1 ranking — `small-prime-mask-compression`: Elo 1516.0, `verified-milestone`; `small-witness-kernel`: Elo 1500.736306793522, `verified-milestone`; `multiplicative-color-descent`: Elo 1483.263693206478, unbuilt. Both built slugs received APPROVE, correctness/completeness/progress 10/10.

## Rules
- ALWAYS: Consult both `knowledge_base.md` and the number-theory crux corpus before proposing approaches (required by project instructions, round 1).
- NEVER: Treat a slug as merely a sublemma; every approach must target the full problem claim (required by project instructions, round 1).
- ALWAYS: In periodic-enumeration arguments, prove translation is an order-preserving bijection and count the inclusive initial block explicitly (prevents endpoint ambiguity, round 1).
- ALWAYS: For small-prime compression, separate the no-large-prime, exponent-zero, and positive-exponent cases and display the strict bound (load-bearing verified detail, round 1).

## State
### Done
- Round 1 setup installed numpy, scipy, and sympy and baselined the absent workspace.
- Three independent explorer lenses consulted the knowledge base and crux corpus.
- Outlined and ranked three rival whole-problem approaches.
- Built `small-prime-mask-compression` and `small-witness-kernel` as complete proofs.
- Independent proof review APPROVED both candidates and certified shared lemmas.
- `results/imo-2026-06/current.md` now records Status `solved` and a complete rigorous proof.

### Broken
- None.

### Next
- Goal achieved; end the session when the time lock permits.
