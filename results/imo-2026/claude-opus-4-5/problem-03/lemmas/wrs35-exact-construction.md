# Lemma: wrs=35 Z-type Exact Construction (n=5)

## Statement

For the wrs=35 Z-type vertex of the bounded "all pairwise > 1" region with n=5:
- Piece sizes: P_1 = 1/63, P_2 = 16/315, P_3 = 11/105, P_4 = 8/45, P_5 = 17/63, P_6 = 8/21
- Sum: P_1 + ... + P_6 = 1

The 4-mark strategy:
- 2 cuts on P_4 at positions P_1 and P_1 + P_2
- 1 cut on P_6 at position P_5
- 1 halve on P_3

achieves LB = 1/2 exactly, with margin c(5) - 1/2 = 32/63 - 1/2 = 1/126 > 0.

## Proof

**Step 1: Verify piece sizes.**

The wrs=35 Z-type vertex has:
- v_0 = 0 (minimum shifted parameter)
- g = 42/35 = 6/5 (common gap in sorted order)
- Permutation: (r_alpha, r_beta, r_gamma, r_delta, r_epsilon, r_zeta) = (0, 1, 2, 3, 4, 5)
- Shifted params: alpha = 0, beta = 6/5, gamma = 12/5, delta = 18/5, epsilon = 24/5, zeta = 6

With L_0 = 1/63:
- P_1 = (1 + 0)/63 = 1/63
- d_1 = (1 + 6/5)/63 = 11/315; P_2 = P_1 + d_1 = 16/315
- d_2 = (1 + 12/5)/63 = 17/315; P_3 = P_2 + d_2 = 33/315 = 11/105
- d_3 = (1 + 18/5)/63 = 23/315; P_4 = P_3 + d_3 = 56/315 = 8/45
- d_4 = (1 + 24/5)/63 = 29/315; P_5 = P_4 + d_4 = 85/315 = 17/63
- d_5 = (1 + 6)/63 = 1/9; P_6 = P_5 + d_5 = 24/63 = 8/21

Sum check: 1/63 + 16/315 + 11/105 + 8/45 + 17/63 + 8/21 = 5/315 + 16/315 + 33/315 + 56/315 + 85/315 + 120/315 = 315/315 = 1. VERIFIED.

**Step 2: Apply the strategy.**

From P_4 = 8/45, cutting at P_1 = 1/63 and P_1 + P_2 = 1/63 + 16/315 = 1/15 creates:
- Piece of size 1/63 (matching P_1)
- Piece of size 16/315 (matching P_2)  
- Remainder: 8/45 - 1/63 - 16/315 = 56/315 - 5/315 - 16/315 = 35/315 = 1/9

From P_6 = 8/21, cutting at P_5 = 17/63 creates:
- Piece of size 17/63 (matching P_5)
- Remainder: 8/21 - 17/63 = 24/63 - 17/63 = 7/63 = 1/9

From P_3 = 11/105, halving creates:
- Two pieces of size 11/210 each

**Step 3: Enumerate all 10 pieces.**

| Source | Pieces |
|--------|--------|
| P_1 (uncut) | 1/63 |
| P_2 (uncut) | 16/315 |
| P_3 (halved) | 11/210, 11/210 |
| P_4 (2 cuts) | 1/63, 16/315, 1/9 |
| P_5 (uncut) | 17/63 |
| P_6 (1 cut) | 17/63, 1/9 |

**Step 4: Identify pairs.**

The 10 pieces form exactly 5 pairs:
- {1/63, 1/63}
- {16/315, 16/315}
- {11/210, 11/210}
- {17/63, 17/63}
- {1/9, 1/9}

**Step 5: Compute LB.**

Sorted descending: 17/63, 17/63, 1/9, 1/9, 11/210, 11/210, 16/315, 16/315, 1/63, 1/63

LB picks positions 1, 3, 5, 7, 9 (greedy alternating):
LB = 17/63 + 1/9 + 11/210 + 16/315 + 1/63

Converting to common denominator 630:
= 170/630 + 70/630 + 33/630 + 32/630 + 10/630
= 315/630 = 1/2

**Step 6: Verify margin.**

c(5) = 32/63 = 320/630
LB = 1/2 = 315/630
Margin = 320/630 - 315/630 = 5/630 = 1/126 > 0

QED.

## Certified

Round 16, proof-reviewer verified via independent rational arithmetic computation.
