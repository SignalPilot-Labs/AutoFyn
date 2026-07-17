# Goal

**Problem:** imo-2026-01 (gcd/lcm blackboard; number_theory; task=proof_only).
Statement: 2026 integers >1 on a board. A move: pick m>1, n>1 from different places, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Repeat while possible.
(a) Prove that after finitely many moves exactly one integer M>1 remains.
(b) Prove M is independent of the choices.

**Metric:** proof-reviewer verdict on results/imo-2026-01/current.md.
**Eval:** dispatch proof-reviewer; target Status=solved (APPROVE), a complete rigorous proof of BOTH (a) and (b).
**Baseline (round 1):** no approaches yet, Status=unsolved.
**Target:** solved.
**Constraint:** both parts (a) and (b) fully proved, no skipped cases, rigor rules enforced.
Note: user explicitly chose imo-2026-01 (medium), overriding the "hard only" default.

# Goal Updates

# Eval History

## Round 1 — BREAKTHROUGH (solved)
- current.md Status: solved. Both approaches APPROVE from proof-reviewer.
- Ranking: global-lex-monovariant (~1516) marginal leader, per-prime-valuation-descent (~1484); both solved.
- M = ∏_p p^{g_p}, g_p = gcd of all initial p-adic valuations across the 2026 entries. Verified by exhaustive identity check + 2000-board×15-play simulation.
- Part (a): terminate via lex monovariant (#entries>1, product) [approach 1] and (Ω, N) [approach 2]; terminal N=0 excluded since some g_p>0. Part (b): g_p invariant via gcd(min(a,b),|a-b|)=gcd(a,b).

# Rules
- ALWAYS: for gcd/lcm board-move problems, decompose per prime — move sends valuation pair (a,b)->(min(a,b),|a-b|) (subtractive Euclid); g_p=gcd of valuations is the invariant (round 1).
- ALWAYS: exclude the empty (all-1) terminal state explicitly via some g_p>0 when proving a survivor exists (round 1).

# State

## Done
- Round 1: SOLVED imo-2026-01 both parts (a) and (b). Two independent complete proofs (global-lex-monovariant, per-prime-valuation-descent), both proof-reviewer APPROVE. current.md Status=solved with full proof.

## Broken
- None.

## Next
- Goal achieved. If run continues, could tighten exposition or add a third genuinely-different framing, but the problem is fully solved and reviewed.
