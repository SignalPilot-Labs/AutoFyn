# Outline Review: IMO 2026 P3

## Problem Summary
For each n, determine the largest c such that Liu Bang can guarantee total length at least c in the stick-cutting game where both players mark at most n points, then take turns claiming pieces greedily.

**Conjectured answer:** c(n) = 2^n / (2^{n+1} - 1)

**Sanity check passed:** Verified c(1) = 2/3, c(2) = 4/7 computationally. The geometric marking strategy and optimal XY response both check out numerically.

---

## Approach 1: geometric-dominance

**Verdict: APPROVE**

**Assessment:**
- **Technique viable:** Yes. The geometric marking creating pieces t, 2t, ..., 2^n t is the right construction. The "dominance" property (2^n > 2^{n-1} + ... + 1) is sound.
- **Skeleton sound:** Steps 1-3 are rigorous. Case A (XY doesn't split largest) is straightforward. 
- **Load-bearing lemmas identified with mechanism:** 
  - "Largest piece dominates" - geometric sum, correct.
  - "Greedy claiming optimal" - exchange argument is standard and fillable.
- **Gaps appropriate:** 
  - Gap 1 (Case B): XY splits the largest piece. This requires analyzing how sub-pieces interleave with remaining pieces. Fillable with careful casework on j marks inside vs n-j outside.
  - Gap 2 (upper bound for arbitrary LB): This is the hard gap. Need to show XY can always limit LB to <= c(n) regardless of LB's marking. The approach correctly identifies this but doesn't propose a mechanism.
  - Gap 3 (greedy optimality): Standard exchange argument, fillable.

**Issues to address during build:**
- Step 4 (Case B) needs explicit sorted-order analysis. When XY puts j marks inside P_n, the resulting sub-pieces must be shown to interleave with remaining pieces such that LB still captures >= c(n).
- Step 6 (upper bound): This is the crux. The builder should prove: for any LB marking creating pieces a_1 <= ... <= a_{n+1}, XY can respond so that LB gets at most the geometric guarantee. One approach: show geometric marking maximizes min over XY responses.

---

## Approach 2: induction-on-n

**Verdict: APPROVE**

**Assessment:**
- **Technique viable:** Yes. Induction with base n=1 is sound. The reciprocal recurrence 1/c(n) = 2 - 2^{-n} is algebraically correct.
- **Skeleton sound:** Base case n=1 analysis is complete and correct (median piece argument).
- **Load-bearing lemmas identified with mechanism:**
  - "n=1 median property" - verified: exactly one of (y-1/3) and (1-y) exceeds 1/3.
  - "Reciprocal recurrence" - algebraic identity, correct.
  - "Reduction to (n-1)-game" - stated but mechanism unclear.

**Gaps:**
- Gap 1 (reduction to (n-1)-game): This is the crux. The outline claims after first-round picks the game reduces to an (n-1)-game, but doesn't explain how marks are "consumed." This needs a game-theoretic argument: after both players pick their best pieces, the remaining sticks plus remaining marks form a smaller game.
- Gap 2 (upper bound induction): Same issue - need to show XY's strategy induces the recurrence.
- Gap 3 (game-theoretic meaning): Why does the reciprocal recurrence arise from game dynamics?

**Issues to address during build:**
- The reduction claim (step 6) is the hard part. The builder must make precise: what does "reduced game relates to (n-1) case" mean operationally? One idea: after LB takes the largest piece and XY responds, the effective mark count decreases and the remaining game has value c(n-1) relative to what's left.

---

## Approach 3: pairing-interleave

**Verdict: CHANGES REQUESTED**

**Assessment:**
- **Technique viable:** Yes, but the execution has a calculation error.
- **Skeleton:** Step 5 contains an acknowledged error: "Sum = P_{n-1} + P_{n-2} + ... + P_1 + P_1 = sum_{k=1}^{n-1} P_k + P_1... wait, this seems wrong." This self-flagged error needs correction.
- **Load-bearing lemmas:**
  - "Copies interleave with originals" - plausible but needs verification.
  - "LB's sum = c(n) exactly" - claimed but calculation is wrong.
  - "Copy strategy is XY-optimal" - needs proof.

**Specific issues:**
1. **Step 5 calculation error:** The sum of LB's take is computed incorrectly. With geometric pieces P_k = 2^k t and XY's copy strategy, the interleaved structure needs careful enumeration. The largest piece P_n = 2^n t gets halved by XY, so the resulting pieces are two copies of P_{n-1} = 2^{n-1} t, not contributions to LB's sum in the way described.
2. **Step 3 description unclear:** "Result: pairs {P_{k-1}, P_{k-1}} at each tier" - this needs precise piece enumeration.

**What to fix:**
- Correct the calculation in Step 5. After XY halves P_n, P_{n-1}, ..., P_2 (n-1 marks) and creates a near-copy of P_1 (1 mark), enumerate all 2n+1 pieces explicitly, sort them, and compute LB's greedy take.
- Gap 3 (upper bound) is shared with geometric-dominance - same hard gap.

---

## Diversity Assessment

**WARNING: All three approaches share the same critical gap.**

The upper bound ("for arbitrary LB marking, XY can limit LB to <= c(n)") appears as:
- geometric-dominance Gap 2
- induction-on-n Gap 2  
- pairing-interleave Gap 3

This is concerning. If this gap cannot be closed, all three approaches fail together. However:
- geometric-dominance attacks it via case analysis on XY's adversarial response
- induction-on-n attempts to embed it in the inductive structure
- pairing-interleave frames it via dyadic structure

These are three framings of the same reduction, not three independent routes. The field has collapsed to one wall. For future rounds: consider an entirely different approach, such as a potential/value function argument, or a minimax game tree analysis, or exploiting symmetry to show geometric is the unique saddle point.

---

## Ranking Justification

1. **induction-on-n** (Elo 1518): Cleanest structure; base case complete; if the reduction works, it's elegant.
2. **geometric-dominance** (Elo 1513): Most direct attack; Case B is complex but tractable; same hard gap.
3. **pairing-interleave** (Elo 1469): Contains a self-acknowledged calculation error; overlaps heavily with geometric-dominance in framing; needs fixes before building.

---

## Build Set

- **geometric-dominance**: Proceed - most direct path, gaps are fillable.
- **induction-on-n**: Proceed - different structural angle, may crack the upper bound via recurrence.
- **pairing-interleave**: Hold until calculation error is fixed.

build set: geometric-dominance, induction-on-n
