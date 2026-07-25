# Run State — imo-2026-01

## Goal
Produce a complete, rigorous prose proof of IMO 2026 Problem 1 (both parts).
Problem: 2026 integers >1 on a board. A move takes m,n>1 from different places and
replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n). Repeat while possible.
(a) Prove that after finitely many moves exactly one integer M>1 remains.
(b) Prove that M does not depend on the choices of Confucius.

Metric: proof-reviewer verdict on results/imo-2026-01/current.md.
Eval: proof-reviewer dispatch (APPROVE + Status `solved` = done).
Baseline: no proof exists (unsolved).
Target: Status `solved`, APPROVE on both (a) and (b).
Constraint: full rigor per CLAUDE.md rigor rules; both parts complete.

## Goal Updates
- [Round 1] User: solve imo-2026-01 (a medium problem, not on the hard list; user override).

## Eval History
- [Round 1] SOLVED (BREAKTHROUGH). proof-reviewer: APPROVE on BOTH approaches
  (per-prime-gcd-invariant, strong-induction-descent), Status `solved`.
  Ranking (Elo): per-prime-gcd-invariant 1531 > strong-induction-descent 1500 >
  confluence-normal-form 1469. Answer M = ∏_p p^{g_p}, g_p = gcd of prime-p
  exponents over all entries. Independently brute-verified 20000 random boards:
  always exactly one survivor, always = closed form, 0 mismatches.

## Rules
- ALWAYS: for gcd/lcm-move board problems, decouple primewise — the move is the
  subtractive-Euclid step (a,b)->(min, max-min) on each prime's exponent; g_p=gcd
  of a prime's whole exponent multiset is an EXACT invariant (round 1).
- NEVER: use the global product as a part-(b) invariant — it is only monotone
  (divides by gcd(m,n) each move), not preserved; use it only for termination (round 1).

## State
### Done
- Round 1: Solved imo-2026-01 (both parts). 3 approaches opened; 2 built & APPROVED;
  full proof in results/imo-2026-01/current.md; 3 lemmas certified.
### Broken
- (none) — goal achieved.
### Next
- Goal complete. If continued: harden/cross-check proofs or attempt a hard-list problem.
