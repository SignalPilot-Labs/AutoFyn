# Run State

## Goal
Problem: `imo-2026-01` — Confucius gcd/lcm blackboard game.

**Statement:** 2026 integers > 1 on a blackboard. Move: choose m > 1, n > 1 from different places, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Prove:
(a) After finitely many moves, exactly one integer M > 1 remains.
(b) M does not depend on the choices of Confucius.

**Metric:** Status in `results/imo-2026-01/current.md` — `solved` with a complete, rigorous two-part proof.
**Eval command:** `cat results/imo-2026-01/current.md | grep -A1 "## Status"`
**Baseline:** `unsolved` (no workspace yet)
**Target:** `solved` — proof-reviewer APPROVE on both parts (a) and (b).
**Constraint:** Rigor rules from CLAUDE.md; name theorems, no hand-waving.

## Goal Updates
(none)

## Eval History
- Round 1: Baseline — workspace empty, status `unsolved`.
- Round 1: SOLVED. Both approaches (p-adic-gcd-invariant, omega-monovariant) received APPROVE verdicts. Elo: p-adic 1516, omega 1515.3. Full proof in current.md.

## Rules
(none yet)

## State

### Done
- Round 1: Full workflow complete. 3 explorers (structural, computational, crux) → outliner (3 approaches) → outline-reviewer (ranked, build set: 2) → 2 builders → proof-reviewer (both APPROVE). Status: solved.

### Broken
(none)

### Next
- Goal achieved. End session.
