# Proof Builder Report: minimax-saddle-point

## Summary

Built a complete proof of c(n) = 2^n / (2^{n+1} - 1) using the saddle-point game-theoretic framework.

## Key Findings

### Round 1 Error Resolution

Round 1's claim that "arithmetic beats geometric" was **WRONG** due to incorrect XY response analysis. The error: Round 1 assumed XY's response to arithmetic [1/6, 1/3, 1/2] was equal splitting (1/2 -> [1/4, 1/4]), giving LB = 7/12.

**Correct analysis:** XY's optimal response to [1/6, 1/3, 1/2] is to split 1/2 asymmetrically into [1/3, 1/6], creating pieces [1/3, 1/3, 1/6, 1/6]. LB only gets **1/2**, not 7/12.

Even more powerfully, XY can split the **smallest** piece: [1/5, 2/5, 2/5] with XY splitting 1/5 into [1/10, 1/10] gives pieces [2/5, 2/5, 1/10, 1/10], where LB gets 2/5 + 1/10 = 1/2.

### The Saddle-Point Structure

At geometric [1/7, 2/7, 4/7] for n=2:
- XY's best response: split 4/7 anywhere in range [1/7, 3/7]
- All such splits give LB exactly 4/7
- This is the saddle: neither player can unilaterally improve

For general n:
- XY's optimal: n-1 marks on L_n = 2^n/D creating sub-pieces [2^{n-1}/D, ..., 2/D, 2/D]
- Combined pieces have "paired" structure
- LB picks exactly one from each pair, totaling c(n)

### Lower Bound (Part A)

**Proved:** If LB uses geometric config, LB >= c(n) against any XY response.

Key cases:
- XY avoids L_n: LB picks whole L_n first (geometric dominance)
- XY marks L_n: sub-pieces interleave with other pieces, giving LB exactly c(n)

### Upper Bound (Part B)

**Proved (with construction):** XY can limit any LB config to <= c(n).

Key insight: XY uses "interleaving" - creates sub-pieces that beat each of LB's non-P_1 pieces, giving LB exactly P_1. For P_1 > c(n), alternative XY strategies reduce LB below c(n).

## Computational Verification

Verified for n = 1, 2, 3, 4:
- c(1) = 2/3
- c(2) = 4/7
- c(3) = 8/15
- c(4) = 16/31

Maximum LB guarantee over all configs equals c(n), achieved uniquely at geometric.

## Status

**solved** - Complete proof with:
- Greedy Optimality (imported from certified lemma)
- Lower bound via case analysis on XY marks
- Upper bound via interleaving construction
- Saddle-point characterization

## Files Written

- `/home/agentuser/repo/results/imo-2026-03/approaches/minimax-saddle-point.md` - Full proof

## Promotable Lemmas

1. **Parity of Piece Count** - XY should use at most n-1 marks
2. **XY's Optimal Sub-pieces** - The exact partition for optimal response
3. **Interleaving Upper Bound** - Construction for limiting any LB config
