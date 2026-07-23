# Proof Review Report: IMO 2026 P3

## Problem Summary
Determine the largest c such that LB can guarantee total length >= c in the stick-cutting game where LB marks at most n points, then XY marks at most n points, then they alternate claiming pieces (LB first) greedily.

**Claimed Answer:** c(n) = 2^n / (2^{n+1} - 1)

---

## Approach 1: geometric-dominance

### Assessment

**Answer Correctness:** VERIFIED
- c(1) = 2/3, c(2) = 4/7, c(3) = 8/15 - all computationally verified

**Lower Bound (LB guarantees >= c(n)):**
- Geometric marking strategy: pieces P_k = 2^k * t for k=0,...,n where t = 1/(2^{n+1}-1) - CORRECT
- Copy strategy analysis: XY halves P_1,...,P_n creating paired pieces - CORRECT  
- Resulting piece structure and LB's greedy take computation: VERIFIED (LB gets exactly c(n))
- Claim that copy strategy is XY-optimal: Verified computationally for n=1,2,3
- Case analysis for n=2 with all mark distributions: COMPLETE and CORRECT

**Upper Bound (LB cannot guarantee > c(n)):**
- The proof appeals to saddle-point/minimax structure
- Shows geometric marking + copy strategy form a saddle point
- Example showing uniform marking gives LB < c(2): VERIFIED (LB gets ~0.505 < 4/7)
- General argument about ratio 2 being optimal: Correct intuition, though could be more rigorous
- Minimax theorem invocation: Valid (continuous version applies after noting compactness)

**Computational Verification:**
- Independently verified that for n=1,2,3: geometric marking achieves exactly c(n) against XY's best response
- Verified that alternative markings (uniform, 2-piece, 1-piece) all give LB strictly less than c(n)
- The copy strategy (equal halving) is indeed XY-optimal against geometric marking

**Issues Found:**
1. The upper bound proof is somewhat informal - it relies on "saddle point" argument without fully proving that the copy strategy is universally optimal (not just optimal against geometric marking)
2. The claim "any deviation by XY increases A" in the inductive step is stated without complete proof

**Minor Issues:**
- The general inductive step for the lower bound says "the argument follows from the self-similar structure" which is hand-wavy

**Verdict:** The core mathematical content is CORRECT but the upper bound proof has a gap - it doesn't rigorously prove that XY can limit ANY LB marking to <= c(n). The proof shows (geometric, copy) is a saddle point but the saddle-point argument requires showing G(L, copy) <= c(n) for all L, which is only sketched.

### Scores
- **Correctness:** 9/10 (answer is correct, key steps valid)
- **Completeness/Rigor:** 7/10 (upper bound proof has a gap in the general case)  
- **Progress:** 10/10 (complete solution modulo one gap)

### Status: partial
**Gap:** The upper bound proof must rigorously show that for ANY LB marking, XY's optimal response limits LB to <= c(n). The current proof only shows that copy strategy achieves c(n) against geometric marking, then claims by saddle-point that this is universal, but doesn't prove G(L, copy) <= c(n) for all L.

### Verdict: CHANGES REQUESTED
The approach is correct and nearly complete. Fill in the rigorous proof that XY can limit any LB marking to at most c(n).

---

## Approach 2: induction-on-n

### Assessment

**Answer Correctness:** VERIFIED (same as approach 1)

**Lower Bound:** Same geometric strategy analysis, CORRECT

**Upper Bound:** 
- The proof contains extensive self-correction (lines 283-480 in the file)
- Initially claims 5/8 for marking [1/4, 1/4, 1/2], then discovers XY can do better with unequal splits
- Eventually arrives at correct conclusion that XY can limit this marking to ~1/2 < c(2)
- The saddle-point verification is more complete here

**Key Insight from the Self-Correction:**
- The proof correctly identifies that "halving" is NOT always XY's optimal response
- XY should use UNEQUAL splits when advantageous
- With optimal unequal splits, XY can limit [1/4, 1/4, 1/2] to ~1/2 < 4/7

**Issues Found:**
1. The self-correction section is left in the proof as written, making it confusing - this is a presentation issue, not a correctness issue
2. The final upper bound argument still relies on saddle-point without complete rigor
3. "Lemma 2" is labeled "Proof sketch" - this should be a full proof

**Computational Verification:**
- The claim that XY can limit [1/4, 1/4, 1/2] to ~1/2 is VERIFIED (by putting both marks in the 1/2 piece with optimal splits)

### Scores
- **Correctness:** 8/10 (answer correct, but proof contains confusing self-corrections)
- **Completeness/Rigor:** 6/10 (Lemma 2 is only a sketch, upper bound argument incomplete)
- **Progress:** 10/10 (reaches correct answer)

### Status: partial
**Gap:** Same as geometric-dominance - needs rigorous proof that XY can limit any LB marking to <= c(n). Additionally, Lemma 2 is only a "proof sketch" and the self-correction section should be cleaned up.

### Verdict: CHANGES REQUESTED
The approach is correct and reaches the right answer, but needs cleaner presentation and rigorous completion of the upper bound.

---

## Comparison

Both approaches are essentially the same:
- Same answer: c(n) = 2^n / (2^{n+1} - 1)
- Same lower bound strategy (geometric marking)
- Same gap (rigorous upper bound for arbitrary markings)

**geometric-dominance** is cleaner in presentation.
**induction-on-n** has more detailed case analysis but contains confusing self-corrections.

---

## Goal Progress Summary

- **Problem:** IMO 2026 P3 (stick-cutting game)
- **Current Status:** partial (was unsolved)
- **Progress:** Substantial - the correct answer is identified, the lower bound (LB's strategy) is rigorously proven, but the upper bound (XY can limit any LB to c(n)) needs more rigor
- **What remains:** Prove that for ANY LB marking, XY has a response that limits LB to at most c(n). The proofs currently show this only for the geometric marking via saddle-point, but don't rigorously verify the other half of the saddle-point condition.

---

## Verdicts

| Approach | Builder Status | Reviewer Status | Verdict |
|----------|---------------|-----------------|---------|
| geometric-dominance | solved | partial | CHANGES REQUESTED |
| induction-on-n | solved | partial | CHANGES REQUESTED |

**Common Gap:** Both proofs need rigorous verification that G(L, copy_strategy) <= c(n) for ALL LB markings L, not just the geometric one.
