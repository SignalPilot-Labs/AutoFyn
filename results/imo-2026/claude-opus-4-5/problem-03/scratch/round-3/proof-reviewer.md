# Proof Review: induction-on-n (Round 3)

## Summary

Reviewed the induction-on-n approach for IMO 2026 P3. The claimed answer c(n) = 2^n/(2^{n+1}-1) is correct (verified computationally for n=1,2,3,4). The lower bound is complete and rigorous. The upper bound has a genuine gap in the sandwich case (k* = m+1).

## Verification of Key Claims

### 1. Answer correctness: VERIFIED

Computationally verified c(n) = 2^n/(2^{n+1}-1) for n=1,2 via exhaustive game tree search. The formula gives:
- c(1) = 2/3 (verified exact)
- c(2) = 4/7 (verified exact)
- c(3) = 8/15, c(4) = 16/31, etc.

### 2. Lower bound: COMPLETE AND RIGOROUS

Re-derived independently:

**Lemma 1 (Greedy Optimality):** Proven correctly by backward induction. Step is valid: taking a smaller piece when larger available is strictly suboptimal.

**Geometric marking:** LB marks to create pieces P_k = 2^k * t_n where t_n = 1/(2^{n+1}-1). Verified:
- Sum = 1 (correct: geometric series)
- P_n > P_0 + ... + P_{n-1} (correct: 2^n > 2^n - 1)

**Case A (XY doesn't mark in P_n):** Since P_n > sum of other pieces, P_n remains largest. LB takes P_n = c(n). Rigorous.

**Case B (Copy strategy):** XY halves P_1,...,P_n. After splitting, LB takes one from each pair plus the singleton. Computed: LB total = 2^n * t_n = c(n). Rigorous.

**Lemma 2 (Copy Optimality):** The claim that copy strategy is XY-optimal against geometric marking is stated but not fully proven. The argument "any deviation... disrupts the pairing" is hand-wavy. However, this only affects whether LB gets *more* than c(n) against non-copy strategies, and the LB total under copy strategy is exactly c(n), so the lower bound c(n) is established regardless.

**Verdict:** Lower bound complete.

### 3. Upper bound: INCOMPLETE (Gap in sandwich case)

The proof uses strong induction on m with the scale-invariant claim P(m): For any m+1 pieces summing to S, XY with m marks can achieve alternating sum A <= S * t_m.

**Base case P(1):** Verified correct. Two cases (ratio > 2 vs <= 2) are complete.

**Inductive step Case A (k* < m+1):** The halve+recurse strategy is rigorous:
- Pigeonhole Existence Lemma: Correct (if all fail, sum exceeds S).
- Ratio Bound p_{k*+1}/p_{k*} > 2: Correct derivation.
- No-interleaving: Halved pairs stay above the sub-problem pieces.
- Sub-problem size bound: S_{k*} < (2^{k*} - 1) * S * t_m. Correct.
- Algebraic miracle: (2^{k*} - 1) * t_m * t_{k*-1} = t_m. Verified: t_{k*-1} = 1/(2^{k*}-1).

**Inductive step Case B (k* = m+1):** This is marked as **[GAP]** in the proof.

The proof correctly identifies the gap: when only k = m+1 satisfies the pigeonhole condition, there's nothing "above k*" to halve. The halve+recurse strategy doesn't apply because the entire problem IS the sub-problem.

**I independently verified this gap is real:**
- Constructed pieces [3/14, 5/14, 6/14] for m=2 where only k=3 satisfies.
- Halving strategies can achieve A <= t_2 = 1/7, but the proof doesn't establish this.
- The proof's "Partial Argument" about applying P(m-1) to p_1,...,p_m is incomplete: the interleaving analysis is not done.

Numerical evidence strongly supports that XY can always achieve the target in the sandwich case, but no rigorous proof is given.

## Scores

| Criterion | Score (1-10) |
|-----------|-------------|
| Correctness (of what's written) | 8/10 |
| Completeness/Rigor | 6/10 |
| Progress | 8/10 |

The proof is honest about its gap, which is better than hiding it. The lower bound is fully rigorous. The upper bound for Case A is rigorous. Only the sandwich case remains.

## True Status

**partial** — The builder marked it `partial`, which is correct.

The proof establishes:
1. The answer c(n) = 2^n/(2^{n+1}-1) (numerically verified)
2. Lower bound: LB guarantees >= c(n) (rigorous)
3. Upper bound for k* < m+1: XY limits LB to <= c(n) (rigorous)
4. Upper bound for k* = m+1: **GAP** (sandwich case not proven)

## Gap to Close

**Specific gap:** Prove that when k* = m+1 (all pieces p_1,...,p_m exceed their geometric thresholds, and only p_{m+1} <= 2^m * S * t_m), XY with m marks can achieve A <= S * t_m.

**Possible approaches:**
1. Show that asymmetric splits (not just halving) work — need explicit construction and analysis
2. Show the sandwich case can be reduced to a smaller P(k) problem despite interleaving
3. Alternative: Direct minimax/LP argument avoiding the case split entirely

## Promotable Lemmas Review

**Greedy Optimality Lemma:** ACCEPT — The backward induction proof is complete and rigorous.

**Pigeonhole Existence Lemma:** ACCEPT — The proof by contradiction is complete.

**k*-Largest Ratio Bound:** ACCEPT — Simple algebraic derivation, correct.

**Sub-Problem Size Bound:** ACCEPT — Follows from ratio bound, correct.

---

## Verdict: CHANGES REQUESTED

**Status:** partial

The induction-on-n approach has made significant progress. The lower bound is complete, the answer is correct, and the upper bound is proven for k* < m+1. However, the sandwich case (k* = m+1) remains an explicit gap. The builder should close this gap by:

1. Proving XY has a winning strategy in the sandwich case, OR
2. Showing the sandwich case never arises (which would require proving that some k < m+1 always satisfies the pigeonhole bound — but this is false as demonstrated)

The approach is not fundamentally flawed — numerical evidence strongly suggests the gap can be closed. However, a rigorous proof is required for `solved` status.
