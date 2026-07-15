## Goal

Solve problem `imo-2026-02` (IMO 2026 P2, geometry, difficulty 8/hard) with a complete rigorous prose proof.

- Statement: Triangle ABC, M/N midpoints of AB/AC. K inside triangle BMC, L inside triangle BNC, with K inside angle LBA, L inside angle ACK, and ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK. O = circumcentre of AKL. Prove OM = ON.
- Metric: `results/imo-2026-02/current.md` `## Status` + approach ranking in `results/imo-2026-02/approaches/.ranking.json`.
- Eval: read those two files each round; a proof-reviewer APPROVE (Status: solved) is the win condition.
- Baseline (round 1): unsolved, 0 approaches, no workspace yet.
- Constraints: prose Markdown proof, rigor rules in CLAUDE.md enforced by proof-reviewer. Crux corpus covers NT/combinatorics/algebra only — geometry problem, so rely on knowledge_base.md + first-principles.

## Goal Updates

- [2026-07-15] Initial user message: solve imo-2026-02. (recorded round 1)

## Eval History

- Round 0 baseline: unsolved, no approaches.
- Round 1: **SOLVED — BREAKTHROUGH.** Status: solved. TWO independent complete proofs, both proof-reviewer APPROVE with outcome `verified-milestone`: `fixed-point-t` (Elo 1546; explicit fixed point T = M + (a/4)(1, cot(A+α)) shown to be O via trig identities, T on perp bisector of MN) and `quadratic-ideal-certificate` (Elo 1515; OM=ON as determinant Δ(τ,σ) in ideal(q_K,q_L) with explicit human-checkable cofactors). Reviewer independently re-derived every displayed identity in sympy and reconstructed 18 configurations from the raw hypotheses confirming O=T and OM=ON. 4 lemma files certified. `current.md` has Full proof. Unbuild approaches concyclic-with-w (1485) and power-point-trig (1454) remain live but moot.

## Rules

- ALWAYS: for geometry problems, run a computation-lens explorer that builds numerical instances and hunts invariants before outlining — the decoupled-quadratics + fixed-point-T discovery drove the round-1 solve (round 1).

## State

- Done: Round 1 — full flow (3 explorers → outliner (4 approaches) → outline-reviewer (build set: fixed-point-t, quadratic-ideal-certificate) → 2 builders → proof-reviewer). Problem SOLVED, two APPROVEd proofs, current.md Status solved with Full proof, 4 certified lemmas.
- Broken: —
- Next: Nothing — goal achieved. If run continues, optional polish only (e.g. certify remaining two approaches or prune them); do not re-attempt a solved problem.
