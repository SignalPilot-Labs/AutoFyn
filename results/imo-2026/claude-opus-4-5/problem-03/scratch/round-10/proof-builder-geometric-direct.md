# Proof Builder Report — geometric-direct, Round 10

## Summary

Revised the geometric-direct approach to address the B_small sub-case issues identified by the outline reviewer and explorers.

## Key Findings

### 1. Critical Correction: B_small Sum Constraint Direction

The B_small region (P_1 > L_0 AND P_{n+1} < c(n)) has the **REVERSED** sum constraint compared to B_large:
- B_large: 5*alpha + 4*beta + 3*gamma + 2*delta + epsilon < 16 (for n=5)
- B_small: 5*alpha + 4*beta + 3*gamma + 2*delta + epsilon > 16 (for n=5)

The original 11 strategies were tested on B_large, not B_small. This explains why the "0/500k failures" claim was misleading.

### 2. Counterexample for 11 Strategies

The explorer found a B_small configuration where ALL 11 Singleton-Pair strategies fail:
- (alpha, beta, gamma, delta, epsilon) = (2.641, 2.594, 0.206, 0.253, 4.913)
- P_6 = 0.292 < c(5) = 0.508 (in B_small)
- All d_j > L_0 (all shifted params > 0)
- Min |condition| = 2.27 >> 1 (all 11 strategies fail)

### 3. New Strategies Identified

I identified and verified 4 additional strategies for B_small:

1. **S_vertical_last** (halve P_1,...,P_4, singletons {P_5, P_6}):
   - Condition: |6*alpha + 5*beta + 4*gamma + 3*delta + 2*epsilon - 43| <= 1
   - Works when P_5 ~ P_6 (the two largest pieces are nearly equal)

2. **Cut-P6-at-P3** (cut P_6 at P_3, halve P_1, P_2, P_5):
   - Creates pairs {P_1/2}, {P_2/2}, {P_3, P_3}, {P_5/2}
   - Singletons {P_4, P_6-P_3}
   - Condition: |7*alpha + 6*beta + 5*gamma + 3*delta + epsilon - 41| <= 1
   - Works at the original counterexample (condition = 0.25 < 1)

3. **Cut-P6-at-P5** (cut P_6 at P_5, halve P_1, P_3, P_4):
   - Creates pairs {P_1/2}, {P_3/2}, {P_4/2}, {P_5, P_5}
   - Singletons {P_2, P_6-P_5}
   - Condition: |7*alpha + 6*beta + 4*gamma + 3*delta + 2*epsilon - 41| <= 1

4. **Cut-P4-at-P1** (cut P_4 at P_1, halve P_3, P_5, P_6):
   - Creates pairs {P_1, P_1}, {P_3/2}, {P_5/2}, {P_6/2}
   - Singletons {P_2, P_4-P_1}
   - Condition: |2 + gamma + delta - alpha| <= 1
   - Works when alpha ~ gamma + delta + 2 (P_1 ~ P_4 - P_1)

### 4. Computational Verification

With 15 strategies (original 11 + 4 new):
- Random sampling: 99.46% coverage of B_small region (50k samples)
- Max min-condition: ~1.87 (still some uncovered points)
- Optimization search found points with min-condition ~ 2.35

### 5. Remaining Gap

The 15 strategies do NOT provide 100% coverage. The remaining uncovered region has configurations where:
- alpha ~ beta (P_1 ~ d_1)
- gamma, delta small (d_2, d_3 barely above L_0)
- epsilon large (d_4 >> L_0)

More strategies (O(n^2) total for n pieces) are needed, or an alternative proof technique.

## Status

**partial** — Complete proof for n=1,2,3,4. For n=5, the strategy enumeration approach shows 99.5%+ coverage but complete algebraic proof remains open.

## Files Updated

- `/home/agentuser/repo/results/imo-2026-03/approaches/geometric-direct.md` — Updated with B_small corrections, new strategies, and computational verification results
- `/home/agentuser/repo/results/imo-2026-03/current.md` — Updated to reflect Round 10 progress

## Recommended Next Steps

1. **Enumerate more strategies for n=5:** The pattern suggests O(n^2) = O(25) strategies may be needed. Each singleton pair (P_i, X_j) where X_j is a piece created by cutting gives one strategy.

2. **Alternative approach:** Try to prove that the sum constraint prevents all strategy conditions from failing simultaneously via LP/sum-slack argument, similar to n=4 BPP Range Bound.

3. **Gap-overlap generalization:** The gap-width = alpha - 1 < 0 argument from n=4 should extend, but the "deepest Case A" where all d_j are doubly large needs to be characterized for B_small.
