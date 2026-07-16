## imo-2026-03

geometric-direct: revise
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n (the actual claim)
Technique: Direct case analysis — Case A (P_1 <= L_0) via halve-all strategy, Case B (P_1 > L_0) via consecutive-difference casework
Skeleton:
  1. Lower bound: LB achieves c(n) with geometric config — by strong induction + Geometric Dominance + Pairing Cancellation (PROVED)
  2. Upper bound Case A (P_1 <= L_0): XY halves P_2, ..., P_{n+1} — by Pairing Cancellation applied n times, LB = 1/2 + P_1/2 <= c(n) (PROVED for all n)
  3. Upper bound Case B trivial (P_{n+1} <= c(n)): XY uses 0 marks, LB <= c(n) (PROVED)
  4. Upper bound Case B nontrivial (P_1 > L_0 AND P_{n+1} > c(n)): XY uses n-1 marks to create 2n pieces with (n-1) pairs + 2 singletons — by singleton-pair formula LB = 1/2 + d_j/2 (PROVED for n=1,2,3; GAP for n>=4)
  5. General n Case B: Prove that when all consecutive differences d_j > L_0, the sum-slack constraint forces max(d_j) < 2*L_0, enabling combination strategy (OPEN GAP)
Key lemmas (claim + the one-line mechanism that makes it true):
  - Halve-All Strategy: LB = 1/2 + P_1/2 — because Pairing Cancellation applied to n pairs {P_k/2, P_k/2} leaves P_1 as sole determinant
  - Singleton-Pair Formula: LB = (1 - s_1 + s_2)/2 — because (n-1) pairs contribute exactly (n-1)/2 to each player, singletons sort to odd/even positions by size
  - Sum-Slack Bound (n=3): d_2 < 2*L_0 when d_1, d_2, P_1 all > L_0 — because 3*P_1 + 2*d_1 + d_2 > 5*L_0 + d_2 must be < 7*L_0
  - General n slack: max_j(d_j) < (2^n - 1 - n(n+1)/2)/(n-1) * L_0 — by averaging bound on sum of n pieces < (2^n-1)*L_0
Open gaps: Step 5 — proving the sum-slack bound for general n >= 4
Cases to cover: n=4 explicitly (verify 4 strategies cover all difference patterns); general n induction on the slack bound
Watch out for: The singleton-pair formula requires n-1 marks creating exactly 2n pieces with n-1 pairs; verify pair construction is always possible

---

## Changes made this round:

1. **Replaced Case A proof** with cleaner halve-all strategy (fills A.1 sub-gap)
2. **Added complete n=3 Case B proof** with three explicit strategies S1, S2, S3
3. **Added complete n=2 Case B proof** with four sub-cases (B2, B1a, B1b, B1c)
4. **Identified the general-n mechanism**: consecutive-difference casework + sum-slack bound
5. **Narrowed the gap**: From "Case B for all n" to "algebraic proof of sum-slack bound for n>=4"

## Build recommendation:

The builder should:
1. Verify the n=3 Strategy S3 algebra more carefully (the P_3 - P_1 vs P_2 sub-case analysis)
2. Attempt the n=4 case explicitly to validate the pattern
3. Formalize the general-n sum-slack lemma: when d_j > L_0 for all j, prove max_j(d_j) < ((2^n-1) - n(n+1)/2)/(n-1) * L_0 < 2*L_0

## Approach status:

- **geometric-direct**: REVISE — major progress, gap narrowed to sum-slack bound for n>=4
- **minimax-saddle-point**: ADVANCE (low priority) — alternative route via LP duality, but geometric-direct is closer
- **induction-on-n**: DEAD END — do not build
- **minimax-value, piece-count-parity**: STALE — not built, low Elo

## Build set recommendation for outline-reviewer:

build set: geometric-direct
