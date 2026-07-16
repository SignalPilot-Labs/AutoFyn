# Proof Builder Report: geometric-direct (Round 4)

## Summary

Revised the upper bound proof in `geometric-direct.md` with the correct case structure based on P_1 vs L_0 threshold.

## Changes Made

1. **Deleted invalid claims:**
   - Removed "XY uses 0 marks" case for n >= 2 (this was nonsensical as shown by outline-reviewer)
   - Removed "always split P_1" strategy (fails when P_1 < c(n) and sub-game is geometric)

2. **Added Case A proof (COMPLETE):**
   - Threshold: P_1 <= L_0 = 1/(2^{n+1}-1)
   - XY Strategy: Use n marks on P_{n+1} to create sub-pieces {P_n, ..., P_2, r, r} where r = (2P_{n+1} - 1 + P_1)/2
   - Key steps verified algebraically:
     - Sub-pieces sum to P_{n+1}
     - r > P_1 (so P_1 is unique minimum)
     - LB picks one from each of n pairs plus P_1
     - LB total = 1/2 + P_1/2 <= c(n) when P_1 <= L_0
   - Formula imported from explorer's Case 2b lemma

3. **Documented Case B (PARTIAL):**
   - Threshold: P_1 > L_0
   - Verified computationally for n=2 (exhaustive grid search, denominator up to 30)
   - Verified computationally for n=3 (20,000 random trials)
   - Strategies that work: halving P_{n+1}, creating pairs via targeted splits
   - **Gap:** No closed-form XY strategy or algebraic proof for general n

4. **Verified n=1 base case:**
   - Case A (P_1 < 1/3): XY halves P_2, giving LB = (1+P_1)/2 < 2/3 = c(1)
   - Case B (P_1 >= 1/3): Forces P_2 <= 2/3 = c(n), so XY uses 0 marks
   - Both cases give LB <= c(1)

## Status

**partial**

- Lower bound: PROVED (complete for all n)
- Upper bound Case A (P_1 <= L_0): PROVED (complete for all n)
- Upper bound Case B (P_1 > L_0): Computationally verified for n=2,3 only

## Remaining Gap

The Case B upper bound for general n lacks a closed-form strategy and algebraic proof. The computational evidence strongly suggests the bound holds, but a rigorous argument is needed.

Possible directions:
1. Prove that for P_1 > L_0, simple halving of P_{n+1} suffices
2. Use the observation that P_1 > L_0 forces pieces to be "balanced" enough that halving works
3. LP/saddle-point analysis showing geometric is the unique maximum

## Promotable Lemmas

1. **Case A Pairing Lemma:** For P_1 <= L_0 and P_{n+1} > c(n), XY's n-mark pairing on P_{n+1} gives LB = 1/2 + P_1/2 <= c(n).

2. **Algebraic Identity:** 2c(n) - 1 = L_0 = 1/(2^{n+1}-1).

## Files Modified

- `/home/agentuser/repo/results/imo-2026-03/approaches/geometric-direct.md` (updated)
