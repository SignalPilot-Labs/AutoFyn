# Proof Review: Round 17

## Summary

Two approaches were built this round to address the n=5 interior coverage gap identified in Round 16:
1. **n5-lp-direct**: LP coverage verification approach
2. **n5-convex-coverage** (revised from n5-five-mark): Convexity-based coverage argument

Both approaches correctly identify and remove the false "max of piecewise linear at vertex" claim. Both correctly state the LB convexity lemma. However, **neither closes the interior coverage gap**.

---

## Approach: n5-lp-direct

### Verdict: CHANGES REQUESTED
### Status: partial

### What is verified correct:

1. **LB Convexity Lemma**: CORRECT. For each fixed (2,1,1) template T, LB(x,T) = sum of 5 largest of 10 linear functions = max over C(10,5) = 252 subsets. Maximum of linear functions is convex. QED.

2. **31 Z-Type Vertex Coverage**: VERIFIED with exact rational arithmetic. All 31 Z-type vertices (v_0 = 0, r_alpha = 0, wrs in {35,...,41}) satisfy LB(v, T_v) <= c(5) for some "copy" (2,1,1) template.
   - **However, the claimed minimum margin is WRONG**: The proof claims minimum margin 1/2520 at wrs=40. My independent computation shows the minimum margin is **1/378** at wrs=36, perm=(0,2,1,3,4,5). This is a conservative error (1/378 > 1/2520), so the coverage claim remains valid.

3. **wrs=35 Exact Proof**: VERIFIED. The construction creates 5 perfect pairs:
   - Pieces: [1/63, 16/315, 11/105, 8/45, 17/63, 8/21]
   - Strategy: 2 cuts on P_4 at {P_1, P_1+P_2}, 1 cut on P_6 at P_5, halve P_3
   - Output: {1/63, 1/63, 16/315, 16/315, 11/210, 11/210, 1/9, 1/9, 17/63, 17/63}
   - LB = 1/2 exactly, margin = 1/126. **CORRECT**.

### Critical Gap:

**The interior coverage is NOT proven.** The proof explicitly acknowledges this:

> "Status is `partial` - the Z-type vertex verification is complete, but interior coverage via LP is not yet rigorous."

**CORRECTION to initial review:** My earlier testing generated INVALID configurations (sum of pieces != 1 due to incorrect constraint handling). After fixing the generation to properly satisfy 21*v_0 + wrs*g = 42:

- 66 valid Tier 3 interior points tested (wrs in {35,...,41}, g in valid range, all pairwise diffs > 1)
- ALL 66 points COVERED by "copy" (2,1,1) templates
- Minimum margin: 173/29400 = 0.00588 (positive)

This computational evidence SUPPORTS the interior coverage claim but does not constitute a rigorous proof. The proofs' claimed sampling results appear consistent with correct sampling.

**The LP coverage verification promised in the approach title was NOT executed.** The proof describes what an LP verification *would* look like but does not provide one.

### Issues to fix:

1. Correct the minimum margin claim: 1/378, not 1/2520.
2. Execute the LP coverage verification (or equivalent rigorous argument) to prove interior coverage rigorously. Computational sampling (66/66 covered) supports the claim but is not a proof.

---

## Approach: n5-convex-coverage (revised n5-five-mark)

### Verdict: CHANGES REQUESTED
### Status: partial

### What is verified correct:

1. **LB Convexity Lemma**: CORRECT (same as n5-lp-direct).

2. **Coverage Sets are Convex**: CORRECT. C_T = {x : LB(x,T) <= c(5)} is a sublevel set of a convex function, hence convex.

3. **AP-type vertices are Tier 2**: CORRECT. At g=1, the sorted shifted params form an arithmetic progression with gap 1. Adjacent-rank params differ by exactly 1, so some pairwise diff = 1 exactly. Tier 2 applies.

4. **31 Z-type vertices are boundary of Tier 3**: CORRECT. V_0 = 0 with r_alpha = 0 gives these vertices.

5. **wrs=35 Exact Construction**: CORRECT (same verification as n5-lp-direct).

### Critical Gap:

Same as n5-lp-direct: **interior coverage is not proven**.

The proof correctly states:

> "**What REMAINS (gap):** The interior coverage of the Tier 3 polytope."

and lists options (LP verification, full algebraic enumeration, template coverage analysis) but does not execute any of them.

### Issues to fix:

1. Execute one of the stated options for interior coverage. Computational sampling (66/66 covered with min margin 0.00588) supports the claim but is not a rigorous proof.

---

## Comparison of Approaches

Both approaches are essentially the same proof with different framing:
- n5-lp-direct emphasizes the LP approach to interior coverage
- n5-convex-coverage emphasizes the convexity structure

Both correctly remove the false "max at vertex" claim and correctly state the LB convexity lemma. Both fail to close the interior coverage gap.

---

## Promotable Lemmas

### LB(x,T) Convexity (n=5)

**Status: CERTIFIABLE**

*Statement:* For n=5 and any fixed (2,1,1) template T creating 10 output pieces as linear functions of (P_1,...,P_6), the function LB(x,T) = sum of 5 largest pieces is convex in x.

*Proof:* Each piece after XY's cuts is linear in P_1,...,P_6. LB = max over C(10,5)=252 subsets of (sum of pieces in subset). Each sum is linear. Maximum of linear functions is convex.

*Verification:* Mathematically sound. The maximum of affine functions is convex is a standard result.

### 31 Z-Type Vertex Coverage (n=5)

**Status: CERTIFIABLE with correction**

*Statement:* All 31 Z-type vertices (v_0=0, r_alpha=0, wrs in {35,...,41}) of the Tier 3 bounded region satisfy LB(v, T_v) <= c(5) for some "copy" (2,1,1) template T_v.

*Correction needed:* Minimum margin is **1/378** (at wrs=36), not 1/2520 as claimed.

*Verification:* Independently verified with exact rational arithmetic for all 31 vertices.

### wrs=35 Z-Type Exact Construction

**Status: Already CERTIFIED in Round 16, re-verified**

---

## Verdict Summary

| Approach | Status | Verdict | Key Gap |
|----------|--------|---------|---------|
| n5-lp-direct | partial | CHANGES REQUESTED | Interior coverage not proven (LP not executed) |
| n5-convex-coverage | partial | CHANGES REQUESTED | Interior coverage not proven |

---

## Specific Corrections Needed

1. **Minimum margin**: Both proofs claim various minimum margins (1/2520 in n5-lp-direct, 0.0046 in n5-convex-coverage). The actual minimum across all 31 Z-type vertices is **1/378 = 0.00265** at wrs=36, perm=(0,2,1,3,4,5). This is a conservative error (actual margin is LARGER than claimed).

2. **Interior coverage**: Both proofs correctly state this as a gap. My corrected computational testing (66 valid interior points, 100% covered, min margin 0.00588) SUPPORTS the claim but is not a proof. The LP verification or algebraic argument is still needed.

---

## Current.md Updates

The current.md Status remains **partial**. The gap identified in Round 16 (interior coverage) remains OPEN.

New certified lemma: **LB(x,T) Convexity (n=5)** - promotes from n5-lp-direct and n5-convex-coverage.

Correction: Minimum Z-type vertex margin is 1/378, not 1/2520.
