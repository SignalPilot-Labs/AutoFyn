# Outline Review: imo-2026-03 Round 4

## Approach: induction-on-n (revise)

### Skeleton Summary
The outliner proposes completing the sandwich case (Case B, k* = m+1) via a "create-duplicate" strategy:
1. XY uses 1 mark to cut p_{m+1} at position p_m, creating two copies of p_m
2. The pair sits at positions 1-2 (since all sub-pieces < p_m)
3. Pair cancellation: contribution 0 to alternating sum
4. Apply P(m-1) to sub-problem {p_1,...,p_{m-1}, p_{m+1}-p_m} with m-1 marks
5. Bound: (S-2p_m)*t_{m-1} < S*t_m via sandwich condition p_m > 2^{m-1}*S*t_m

### Lemma Verification

**Lemma: p_{m+1} < 2*p_m in sandwich case**
- Mechanism: p_m > 2^{m-1}*S*t_m and p_{m+1} <= 2^m*S*t_m = 2*(2^{m-1}*S*t_m) < 2*p_m
- Status: SOUND. Verified algebraically.

**Lemma: Sub-problem pieces are all < p_m**
- Mechanism: p_k < p_m for k < m (sorted order), and p_{m+1}-p_m < p_m (from above)
- Status: SOUND. The sorted order is given, and the subtraction bound follows.

**Lemma: Pair sits at positions 1-2**
- Mechanism: Both copies equal p_m, which exceeds all sub-problem pieces
- Status: SOUND with caveat. See edge case below.

**Lemma: (S-2p_m)*t_{m-1} < S*t_m**
- Mechanism: Rearranges to p_m > 2^{m-1}*S*t_m, the sandwich condition
- Status: PARTIALLY SOUND. The algebraic identity is correct:
  ```
  (t_{m-1} - t_m) / (2*t_{m-1}) = 2^{m-1} * t_m
  ```
  Verified for m=2,3,4,5. BUT the strict inequality requires p_m > threshold strictly.

### Edge Cases

**m=1 (Base case):**
- The sandwich case framework is for m >= 2. Base case P(1) is already proven separately with explicit casework. No issue.

**Ties within sub-problem:**
- If p_1 = p_{m+1} - p_m, both are still strictly < p_m, so the pair (p_m, p_m) stays at positions 1-2. Verified numerically. No issue.

**Boundary: p_m = 2^{m-1}*S*t_m exactly**
- This is NOT a true sandwich case (k* = m, not m+1), so it falls under Case A. No issue.

**Boundary: p_{m+1} = 2*p_m exactly (geometric configuration)**
- At the geometric piece set p_k = 2^{k-1}*S*t_m, we have p_{m+1} = 2*p_m exactly.
- Then p_{m+1} - p_m = p_m, giving THREE copies of p_m, not two.
- The pair cancellation still works, but A = S*t_m exactly (equality, not strict <).
- **Issue:** The outline claims "(S-2p_m)*t_{m-1} < S*t_m" (strict), which fails here.
- **Fix:** Change to "<=" for the bound. P(m) claims A <= S*t_m (not strict), so equality is fine.

**Mixed Case B: k* = m+1 but some k' < m satisfies threshold**
- The reduction explorer raised this concern.
- Analysis: If k* = m+1, then p_{m+1} <= threshold. For the create-duplicate to work, we only need p_m > threshold_m (to get p_{m+1} < 2*p_m).
- If p_m <= threshold_m, then k* >= m, so k* = m+1 requires p_{m+1} satisfies AND is max. This can happen.
- BUT: if p_m <= threshold_m and p_{m+1} <= threshold_{m+1}, then at the boundary p_{m+1} = 2*p_m. The strategy still works (see boundary case above).
- **Conclusion:** Mixed Case B is handled by the same strategy. No separate treatment needed.

### Small-Case Sanity Check

Verified numerically:
- m=2, pieces (0.145, 0.29, 0.565): A_total = 0.13 < 1/7 = 0.143. PASS.
- m=2, geometric (1/7, 2/7, 4/7): A_total = 1/7 exactly. PASS (equality allowed).
- m=2, mixed case (0.14, 0.30, 0.56): A_total = 0.12 < 1/7. PASS.

### Issues Found

1. **Step 5f bound is too strict:** The outline says "(S-2p_m)*t_{m-1} < S*t_m" but at the geometric configuration this is equality. Change "<" to "<=".

2. **Step 5a claim needs caveat:** "p_{m+1} < 2p_m" is strict only when p_m > threshold strictly. At exact threshold, p_{m+1} = 2p_m (equality). The proof still works because P(m) allows equality.

### Verdict: CHANGES REQUESTED

The technique is correct and the skeleton is sound. The create-duplicate strategy closes the gap. However, two minor issues need fixing during build:

1. **Step 5f:** Change "bound (S-2p_m)*t_{m-1} < S*t_m" to "bound (S-2p_m)*t_{m-1} <= S*t_m" and note that equality holds at the geometric configuration.

2. **Step 5a:** Note that p_{m+1} <= 2*p_m (not strict) when p_m equals its threshold exactly, but the proof still works since we only need p_{m+1} - p_m <= p_m.

These are straightforward fixes that the builder can incorporate while writing the proof. The overall strategy is verified.

---

## Population Management

### Ranking Update

The induction-on-n approach has made significant progress: Case A was completed in R3, and the sandwich case fix now closes the remaining gap. This is a major advance over the other approaches which remain static.

Comparisons:
- **induction-on-n > geometric-dominance:** induction-on-n now has a complete proof skeleton; geometric-dominance has the same gap with no path to close it.
- **induction-on-n > ratio-based-induction:** The ratio-based approach is subsumed (Case A uses ratio > 2; sandwich uses create-duplicate).
- **induction-on-n > exchange-argument:** exchange-argument was exploratory and never built.
- **induction-on-n > n2-explicit-casework:** n2-explicit has never been built; induction-on-n is further along.
- **induction-on-n > pairing-interleave:** pairing-interleave insights absorbed into induction-on-n.

### Archives

The outliner correctly marked geometric-dominance, pairing-interleave, and ratio-based-induction as archived/superseded. These should be deprioritized but remain in the population for diversity.

---

## Build Set

**build set: induction-on-n**

The builder should:
1. Add Case B (sandwich case) to the Full Proof section of `approaches/induction-on-n.md`
2. Use the create-duplicate strategy as outlined
3. Fix the two minor issues noted above (strict to non-strict bounds)
4. Mark the approach as complete and ready for reviewer verification
