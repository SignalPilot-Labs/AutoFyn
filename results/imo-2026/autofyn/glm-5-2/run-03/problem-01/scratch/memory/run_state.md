## Goal

Solve **imo-2026-01** (both parts): 2026 integers >1 on a blackboard; a move replaces a chosen pair (m,n), m,n>1, with (gcd(m,n), lcm(m,n)/gcd(m,n)); repeat while possible.
- (a) Prove the process terminates with exactly one integer M>1 remaining.
- (b) Prove M is independent of the move choices.

- **Metric:** proof rigor + completeness (both parts), judged by `proof-reviewer`.
- **Eval:** `proof-reviewer` verdict on `results/imo-2026-01/current.md` `## Status`. Target: `solved` / APPROVE with complete rigorous proof of (a) and (b).
- **Baseline:** no approaches exist (status unsolved).
- **Target:** `solved` (APPROVE).
- **Constraints:** prose Markdown proof; no skipped cases; name tools (knowledge_base.md); verify invariants. Per-prime exponent dynamics + a global termination potential are the expected core. Note: problem is rated `medium` but user explicitly requested it — user message overrides the "hard only" default.

## Goal Updates

- [2026-07-25 14:02] User: "solve the problem imo-2026-01." (Overrides hard-only default; this problem selected.)

## Eval History

- [Round 1, baseline] No approaches yet. `current.md` does not exist. Status: unsolved.
- [Round 1] BREAKTHROUGH. `proof-reviewer` verdict: `perprime-gcd-lexmonovariant: APPROVE` (Status solved). Both parts (a)+(b) proven: per-prime move (α,β)→(min,|α−β|) preserves d_p=gcd of p-exponents (Euclidean identity); termination via lexicographic monovariant (Ω,K) — Ω drops by Ω(gcd)≥1 when gcd>1, else K drops; all-ones terminus ruled out by d_p invariant; M=∏p^{d_p}, choice-independent. All identities reviewer-rederived + 100k-pair computational check. `confluence-newman: CHANGES REQUESTED` (partial — part (a) solved on this route, part (b) blocked at Newman's-lemma case-B critical-pair joinability; stays live). `current.md` Status = `solved`, full proof recorded. APPROACH RANKING: perprime-gcd-lexmonovariant Elo 1516, confluence-newman Elo 1484.

## Rules

- ALWAYS: One problem per run — imo-2026-01 only (CLAUDE.md).
- ALWAYS: Read `results/imo-2026-01/current.md` and live `approaches/<slug>.md` before attempting; don't repeat dead ends.
- ALWAYS: Consult both `knowledge_base.md` and the crux corpus (`past_crux_moves_database.json`, schema in `crux_moves_documentation.md`) — filter by domain `number_theory` first.
- NEVER: hand-edit `approaches/.ranking.json` — tool-owned.
- ALWAYS: For Ω-drop under the move, derive from `mn=gcd·lcm` and `lcm=gcd·(lcm/gcd)` — correct drop is Ω(gcd), NOT 2Ω(gcd) (skeleton slip, round 1).
- NEVER: try to prove part (a) by running each prime's Euclidean algorithm to completion — whole-number moves couple primes across the board; use the GLOBAL lexicographic monovariant instead (round 1).
- NEVER: present the Dershowitz–Manna multiset-order descent on exponent vectors as a termination proof here — it is FALSE (m=4,n=9 grows the multiset); approach `exponent-multiset-dershowitz` cut round 1 (REMOVED candidate).
- ALWAYS: state Newman's lemma explicitly (terminating+locally confluent⟹confluent⟹unique NF) — it is not in knowledge_base.md (round 1).

## State
### Done
- Round 1 setup: env (numpy/scipy/sympy installed), workspace `results/imo-2026-01/{approaches,lemmas}` created, problem statement located, crux corpus located.
- Round 1 pipeline: 2 explorers (perprime-euclid, termination-monovariant) → outliner (3-approach field) → outline-reviewer (cut dershowitz [false multiset lemma], approved perprime + confluence) → 2 builders → proof-reviewer.
- Round 1 RESULT: `perprime-gcd-lexmonovariant` APPROVE — problem SOLVED. `current.md` carries full proof. Shared lemma `lemmas/perprime-invariant-and-lexmonovariant.md` certified.

### Broken
(none — primary goal achieved. `confluence-newman` is partial by design as a diversity bet, not a blocker.)

### Next
- Problem solved (APPROVE). Confluence-newman's case-B critical-pair joinability remains an open diversity route if the run continues, but is not required for the goal.
