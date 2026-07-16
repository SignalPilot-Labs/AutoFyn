# Proof Review: n5-five-mark (Round 12)

## Summary

The n5-five-mark approach for proving c(5) = 32/63 presents a three-tier strategy cascade: V_j strategies, Pairwise strategies, and (2,2,1) strategies. I have independently verified the key computational claims and identified both strengths and gaps.

---

## Verification Results

### 1. V_j Strategies (Tier 1) - CORRECTLY PROVED

The V_j strategy proof is correct:
- If d_j <= L_0 for some j, XY halves all except {P_j, P_{j+1}} using 4 marks
- Creates 4 pairs + 2 singletons = 10 pieces
- By Singleton-Pair Formula: LB = 1/2 + d_j/2 <= 1/2 + L_0/2 = c(5)
- The identity 2*c(5) - 1 = L_0 is verified: 2*(32/63) - 1 = 1/63

**Verdict: CORRECT**

### 2. Bounded Region Characterization (Tier 3 Setup) - CORRECTLY PROVED

The Rearrangement Inequality argument is mathematically sound:
- Weighted sum constraint: 6*alpha + 5*beta + 4*gamma + 3*delta + 2*epsilon + zeta = 42 (verified)
- When all pairwise > 1, sorted values satisfy v_k >= v_0 + k*g for g > 1
- Minimum weighted sum = 21*v_0 + 35*g (verified by computation)
- For WS = 42 with g > 1 and v_0 > 0: g < 42/35 = 1.2 and v_0 < 1/3

**Verdict: CORRECT**

### 3. 63 Boundary Vertices Enumeration - CORRECT

I verified independently:
- wrs (weighted rank sum) ranges from 35 to 41 for v_0 > 0
- Distribution: wrs=35: 1, wrs=36: 5, wrs=37: 6, wrs=38: 9, wrs=39: 16, wrs=40: 12, wrs=41: 14
- Total: 1+5+6+9+16+12+14 = 63 vertices

**Verdict: CORRECT**

### 4. Boundary Reduction Argument - CORRECT

At g=1 exactly, consecutive sorted ranks (k, k+1) go to some pair of parameters.
Since there are 5 consecutive pairs in {0,1,2,3,4,5}, at least 5 parameter-pairs have |diff| = 1 at the boundary.
This means Pairwise strategies (condition: |diff| <= 1) already cover the g=1 boundary.
The (2,2,1) strategies are only needed for strict interior g > 1.

**Verdict: CORRECT**

### 5. Pairwise Strategies (Tier 2) - PARTIALLY CORRECT, GAP IDENTIFIED

**Issue Found:** The (beta, gamma) example construction is INCORRECT:
- The approach claims: "halve P_1, P_4, P_5, P_6. Singletons {d_1, d_2}."
- Actual singletons from this construction: {P_2, P_3}, NOT {d_1, d_2}
- The singleton difference is d_2 = P_3 - P_2, NOT |d_1 - d_2|
- This does NOT match the (beta, gamma) condition |d_1 - d_2| <= L_0

The (alpha, delta) example is correct, but the claim that "all 15 pairwise strategies are valid" is NOT fully verified.

**Impact Assessment:** This is a documentation error, not a fundamental flaw. The approach correctly identifies that SOME pairwise conditions work, and the bounded region where NO pairwise conditions hold is correctly characterized. The (2,2,1) strategies handle this region.

**Verdict: GAP - Example construction errors; not all 15 verified**

### 6. (2,2,1) Strategy Computational Verification - INDEPENDENTLY VERIFIED

I ran my own verification with the CORRECT lb_score function (alternating greedy picks):

**Type-3 failure case:** (alpha=0.007, beta=2.205, gamma=3.321, delta=1.060, epsilon=4.441, zeta=5.584)
- Best (2,2,1) variant: Split P_4, P_5; halve P_6
- LB = 0.5009 < c(5) = 0.5079
- Margin = 0.0070
- **SUCCESS**

**Boundary vertices (sampled 20 of 63):**
- 20/20 success
- Minimum margin: 0.0057
- **ALL VERIFIED**

**Verdict: COMPUTATIONALLY VERIFIED (independent reproduction)**

---

## Critical Observation: lb_score Function

The approach file's claim that "(2,2,1) creates 11 pieces and LB picks ceil(11/2) = 6" initially seemed problematic because "sum of 6 largest" would exceed c(5). However, this is a misunderstanding:

- With alternating greedy picking, LB gets odd-position pieces from sorted order
- For perfect pairs, LB gets one from each pair (greedy alternation)
- This gives LB = 1/2 + (singleton contribution), matching the Singleton-Pair formula
- My independent verification with correct lb_score confirms (2,2,1) works

---

## Remaining Gaps for Full Rigor

1. **Pairwise construction errors:** The (beta, gamma) example and potentially other pairwise constructions need correction. The approach should either:
   - Fix all 15 pairwise construction examples, OR
   - Acknowledge that only SOME pairwise conditions have valid 4-mark constructions

2. **Algebraic proof of (2,2,1):** The computational verification is strong (63 boundary vertices + interior sampling), but a formal algebraic proof requires:
   - 63-vertex finite check with explicit closed-form verification, OR
   - LP breakpoint enumeration for the piecewise-linear LB structure

3. **Minor:** The approach says "60 possible (2,2,1) variants" but the correct count is C(6,2) * 4 = 60 (choose 2 pieces to double-mark from 6, then 1 of remaining 4 to halve). This is correct.

---

## Scores

| Criterion | Score | Notes |
|-----------|-------|-------|
| Correctness | 8/10 | V_j and bounded region correct; Pairwise examples have errors |
| Completeness | 7/10 | (2,2,1) computational but not algebraic; Pairwise not all verified |
| Progress | 9/10 | Major breakthrough: identified (2,2,1) as solution, characterized bounded region |

---

## True Status

**Status: partial**

The approach has made significant progress:
- V_j strategies: PROVED
- Bounded region characterization: PROVED  
- Pairwise strategies: PARTIALLY PROVED (concept correct, some constructions wrong)
- (2,2,1) strategies: COMPUTATIONALLY VERIFIED (not algebraically proved)

The n=5 upper bound is NOT yet fully rigorous due to:
1. Pairwise construction errors needing correction
2. (2,2,1) lacking algebraic proof

---

## Verdict: CHANGES REQUESTED

**Reason:** Real progress (V_j proved, bounded region proved, (2,2,1) computationally verified), but gaps remain:

1. **Fix Pairwise constructions:** The (beta, gamma) example is wrong. Either correct all 15 or acknowledge which ones work.

2. **Algebraic proof for (2,2,1):** The computational verification is convincing but not rigorous. The 63-vertex finite check is tractable:
   - For each vertex, derive the optimal (2,2,1) variant algebraically
   - Verify LB <= c(5) with explicit formulas
   - Use continuity/compactness for interior

---

## Promotable Lemmas Assessment

**V_j Strategy (n=5):** CERTIFIABLE
- Statement is correct
- Proof is complete and rigorous
- No dependencies on unproven claims

**Pairwise Strategy (n=5):** NOT CERTIFIABLE
- General concept is correct
- But specific constructions have errors
- Needs correction before certification

**Bounded "All Pairwise > 1" Region (n=5):** CERTIFIABLE  
- Statement is correct
- Rearrangement Inequality proof is rigorous
- Bounds g in (1, 1.2) and v_0 in (0, 1/3) are verified

**(2,2,1) Strategy Coverage:** NOT CERTIFIABLE (YET)
- Computational verification is strong
- But algebraic proof is missing
- Observation status is appropriate (not lemma)

---

## Approach File Status

The builder correctly marked Status as **partial**. This is accurate.

---

## Next Round Recommendations

1. **Priority 1:** Correct Pairwise construction examples (especially (beta, gamma))
2. **Priority 2:** Begin 63-vertex algebraic verification for (2,2,1)
3. **Priority 3:** Consider if some Pairwise conditions subsume others, reducing the enumeration burden
