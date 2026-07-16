# Proof Review — Round 10

## Approach: geometric-direct

### Verdict: CHANGES REQUESTED
### Status: partial

---

## Summary

The Round 10 builder made meaningful progress on the B_small sub-case for n=5, but the review uncovered a **critical gap in the n=4 proof** that was already marked as "FULLY PROVED". This gap does NOT invalidate the claim (the fix is straightforward), but it means the stated proof is incomplete.

---

## Verification Results

### 1. n=5 B_small Counterexample: VERIFIED CORRECT

The counterexample (alpha=2.641, beta=2.594, gamma=0.206, delta=0.253, epsilon=4.913) is valid:
- **P_6 = 0.292 < c(5) = 0.508**: Confirmed (B_small region)
- **P_1 > L_0**: Confirmed (P_1 = 0.058 > L_0 = 0.016)
- **All d_j > L_0**: Confirmed (all shifted params > 0)
- **All 11 original strategies fail**: Verified, minimum condition value = 2.27 >> 1

### 2. New n=5 Strategies: VERIFIED WITH ISSUES

#### Cut-P6-at-P3 Strategy: VERIFIED CORRECT
- **Mark count**: 4 marks (1 cut + 3 halves) <= n=5. Correct.
- **Piece structure**: 10 pieces = 4 pairs + 2 singletons. Correct.
- **Singletons**: {P_4, P_6-P_3}. Correct.
- **Algebraic condition**: |7*alpha + 6*beta + 5*gamma + 3*delta + epsilon - 41| <= 1. **Verified independently**.
- **Works on counterexample**: Condition = 0.247 < 1. Confirmed.
- **LB = 0.502 < c(5) = 0.508**: Confirmed.

#### S_vertical_last Strategy: VERIFIED CORRECT (but doesn't cover counterexample)
- **Mark count**: 4 marks. Correct.
- **Piece structure**: 10 pieces. Correct.
- **Singletons**: {P_5, P_6}. Correct.
- **Condition on counterexample**: |cond| = 2.775 > 1. Strategy FAILS here.

#### Cut-P6-at-P5 Strategy: VERIFIED CORRECT (but doesn't cover counterexample)
- Condition on counterexample: 4.46 > 1. Strategy FAILS here.

#### Cut-P4-at-P1 Strategy: **ISSUE - CONDITION DOESN'T MATCH CLAIM**
- Builder claims condition: |2 + gamma + delta - alpha| <= 1
- On counterexample: |2 + 0.206 + 0.253 - 2.641| = 0.182 < 1. Would work.
- **However**, I computed |P_2 - (P_4-P_1)|/L_0 = 1.182 > 1. Doesn't work!
- **Discrepancy**: The algebraic formula in the approach file is **WRONG**.
- Correct formula should involve more terms. This strategy needs re-derivation.

### 3. n=3 Case B Small: VERIFIED CORRECT

The proof uses sum constraint P_1 + P_2 + P_3 > 7*L_0 (from P_4 < c(3)), which is the **correct B_small constraint**. The S1/S2/S3 coverage argument is valid.

### 4. n=4 Case B Small: **CRITICAL GAP FOUND**

The proof claims "n=4 Case B is FULLY PROVED" via strategies S6, S4, S5, BPP. However:

**COUNTEREXAMPLE FOR THE STATED 4 STRATEGIES:**
- Config: alpha=1.63, beta=-0.5, gamma=2.95, eta=0.82
- P_1 > L_0: YES (Case B)
- P_5 < c(4): YES (B_small)
- P_5 >= P_4: YES (valid ordering)
- **S6 fails**: |gamma - alpha| = 1.32 > 1
- **S4 fails**: |beta - eta| = 1.32 > 1
- **S5 fails**: |eta - (alpha+beta+1)| = 1.32 > 1
- **BPP fails**: |2+2*alpha+beta - eta| = 3.95 > 1

**BUT XY CAN STILL WIN**: Halving P_3, P_4, P_5 with singletons {P_1, P_2} gives LB = 0.508 < c(4).

**ROOT CAUSE**: The proof's "Non-Case-A" branch only checks `gamma < alpha+1 OR eta < beta+1`. It **MISSES** the case where `beta < 0` (d_1 < L_0).

**FIX**: Add V1 strategy: "If d_1 <= L_0, halve P_3, P_4, P_5, singletons {P_1, P_2}." Similarly for V2/V3/V4. The proof structure should be:
1. If any d_j <= L_0, use V_j strategy. Done.
2. If all d_j > L_0 (all shifted params >= 0), use the S6/S4/S5/BPP coverage argument.

This is **fixable** but the current stated proof is **incomplete**.

### 5. Sum Constraint Direction: **ERROR IN APPROACH FILE**

The approach file states for n=4: "Sum constraint: 4*alpha + 3*beta + 2*gamma + eta < 5."

This is **WRONG for B_small**. The correct constraint from P_5 < c(4) is:
4*alpha + 3*beta + 2*gamma + eta > 5 (REVERSED!)

Similarly, the claim "6*alpha + 4*beta < 2, so alpha < 1/3" is **backwards**. The correct derivation gives 6*alpha + 4*beta > 2.

However, this error doesn't break the proof IF the V1/V2/V3/V4 strategies are added, because the "Case A" branch (all d_j > L_0) is a subset of the valid parameter space that CAN be covered by S6/S4/S5/BPP with the correct bounds.

### 6. 99.5% Coverage Claim for n=5: REASONABLE BUT NOT A PROOF

The computational verification showing 99.5% coverage is evidence that the strategy set is close to complete, but:
- The remaining ~0.5% may require additional strategies
- Algebraic proof of 100% coverage is NOT provided
- This is real progress but does NOT upgrade to "solved"

---

## Scores

| Criterion | Score | Notes |
|-----------|-------|-------|
| Correctness | 6/10 | n=4 proof has a gap; n=5 strategy formula error |
| Completeness | 5/10 | n=4 gap, n=5 algebraic proof open |
| Progress | 7/10 | Found B_small counterexample, identified new strategies |

---

## True Status

**partial** — The claim "COMPLETE PROOF for n=1,2,3,4" is INCORRECT. The n=4 proof as stated is incomplete (missing V1/V2/V3/V4 strategies). The fix is straightforward but not yet applied.

---

## Gaps Requiring Closure

1. **[HIGH] n=4 proof gap**: Add V1/V2/V3/V4 strategies and expand "Non-Case-A" condition to include any shifted param < 0.

2. **[MEDIUM] Sum constraint direction**: Fix the erroneous "< 5" and "< 2" claims to "> 5" and "> 2".

3. **[MEDIUM] Cut-P4-at-P1 formula**: Re-derive the correct algebraic condition.

4. **[LOW] n=5 algebraic coverage**: 15 strategies cover ~99.5%; need either more strategies or a sum-slack proof that prevents all from failing simultaneously.

---

## Promotable Lemmas

### Pairing Cancellation Lemma: CERTIFIED
Statement and proof are correct. Already in lemmas folder.

### Halve-All Strategy (Case A): CERTIFIED
Correct for all n >= 1.

### Halve + IH Strategy: CERTIFIED
Correct for all n >= 2.

### Singleton-Pair Formula: CERTIFIED
Correct when applied to proper (n-1) pairs + 2 singletons structure.

### n=4 Gap-Width Lemma: **NOT CERTIFIED**
The derivation relies on the incorrect sum constraint direction. Needs re-proof.

### BPP Unified Construction: **NOT CERTIFIED**
Same issue — needs verification with corrected constraints.

---

## Verdict: CHANGES REQUESTED

The builder found the B_small counterexample and identified new strategies, which is valuable progress. However:

1. The n=4 proof has a gap that must be fixed
2. The n=5 strategy formulas have errors
3. The sum constraint direction is wrong in the approach file

These issues are **fixable** in the next round. The approach is sound; the execution needs correction.

---

## Outcome for Ranker

- **Slug**: geometric-direct
- **Outcome**: partial
- **Note**: n=4 proof gap found (V1-V4 strategies missing); n=5 progress but formulas need correction
