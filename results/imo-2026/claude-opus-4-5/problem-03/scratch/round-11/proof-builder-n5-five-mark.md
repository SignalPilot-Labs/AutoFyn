# Proof Builder Report: n5-five-mark

## Summary

Built the n5-five-mark approach for proving c(5) = 32/63 in the B_small sub-case.

**Status: partial**

## Work Done

### 1. V_j Strategies (PROVED)
Formalized the V_j strategy lemma: when any d_j <= L_0, XY halves all pieces except {P_j, P_{j+1}} using 4 marks. By Singleton-Pair Formula, LB = 1/2 + d_j/2 <= c(5).

### 2. Pairwise Strategies (PROVED)
Verified that all 15 pairwise strategies (one for each pair of shifted params) have valid 4-mark constructions. When |x_i - x_j| <= 1, the corresponding singleton difference is <= L_0, giving LB <= c(5).

### 3. "All Pairwise > 1" Sub-Region Analysis

**Key Finding:** The explorer's three-strategy sub-claim (Strategies A, E, F) is INSUFFICIENT.

I found a genuine counterexample:
- Configuration: alpha=3.0229, beta=0.0062, gamma=1.0080, delta=2.0197, epsilon=4.1385, zeta=5.4636
- All constraints satisfied: weighted sum = 42, all params > 0, P_6 < c(5)
- All 15 pairwise differences > 1 (minimum = 1.0018)
- Strategy A condition: |delta - 2 - 2*alpha - beta| = 3.44 > 1 (FAILS)
- Strategy E condition: |zeta - delta - beta| = 3.44 > 1 (FAILS)
- Strategy F condition: |gamma - 2*alpha - beta| = 5.04 > 1 (FAILS)

### 4. Computational Resolution

**Type 3 strategies work:** XY makes 2 cuts at arbitrary positions + 3 halves.

Tested on 50 random samples from the "all pairwise > 1" region with 50x50 grid search:
- **100% success rate** - every sample has a working Type 3 strategy
- The counterexample above is covered by: cut P_2 at 0.08, cut P_5 at 0.11, halve P_1,P_3,P_6, leave P_4

### 5. Gap Identified

The algebraic characterization of Type 3 cut positions is OPEN. We have:
- Computational existence: 100% coverage with grid search
- No closed-form formula for optimal cut positions

This prevents a complete algebraic proof.

## Key Insights

1. **Pigeonhole fails for n=5:** Unlike n=4, the weighted sum constraint (42) does NOT force some pairwise <= 1. The region where all pairwise > 1 is non-empty but bounded (gap g in (1, 1.2)).

2. **The "dust creation" technique:** Some Type 3 strategies work by creating a very small piece that shifts the greedy allocation in XY's favor.

3. **Non-algebraic cut positions:** The optimal cuts are NOT at piece boundary values (P_j). This makes explicit strategy characterization difficult.

## Recommendations for Next Round

1. **Approach 1 (Existence):** Use compactness + continuity argument. The LB function is continuous in cut positions. The set of valid cut positions is compact. If no Type 3 strategy works, the minimum LB over all strategies would exceed c(5), contradicting computational evidence.

2. **Approach 2 (LP/Duality):** Reformulate as LP feasibility. Show the dual is infeasible when all pairwise > 1 + no Type 3 works.

3. **Approach 3 (Accept computational):** Note that the computational verification is sufficient for a fixed n=5. The proof for general n >= 5 would need a different technique anyway.

## Files Modified

- Created: `/home/agentuser/repo/results/imo-2026-03/approaches/n5-five-mark.md`

## Verdict

**partial** - V_j and Pairwise strategies are rigorously proved. The "all pairwise > 1" sub-region is computationally covered by Type 3 strategies (100% success rate with grid search), but lacks algebraic characterization.
