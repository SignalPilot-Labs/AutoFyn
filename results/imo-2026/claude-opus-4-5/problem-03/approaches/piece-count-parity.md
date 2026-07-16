# Approach: piece-count-parity

## Status
partial

## Target
Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.

## Overview
Focus on the piece-count parity to understand XY's optimal number of marks. This approach emphasizes WHY XY uses exactly n-1 marks (not n), and derives c(n) from this structural insight.

## Technique
Parity analysis of piece count + greedy selection analysis.

---

## Skeleton

### Part 1: Piece Count and Pick Allocation

**Setup.** Let m = (LB marks) + (XY marks). Total pieces = m + 1.

LB picks ceil((m+1)/2) pieces; XY picks floor((m+1)/2) pieces.

**Key observation:** 
- If m+1 is even (m odd), both pick (m+1)/2 pieces each.
- If m+1 is odd (m even), LB picks (m+2)/2 pieces and XY picks m/2 pieces. LB gets one extra piece.

**Consequence:** XY prefers m to be odd, so m+1 is even. Since LB uses exactly n marks (to maximize guarantee), XY should use n-1 marks (m = n + (n-1) = 2n-1, which is odd, giving 2n pieces and each picks n).

If XY uses n marks: m = 2n, m+1 = 2n+1 (odd). LB picks n+1, XY picks n. Bad for XY.

---

### Part 2: Why LB Uses All n Marks

**Claim.** LB should use all n marks.

**Reasoning:** Using fewer marks creates fewer pieces, and XY can then equalize them more effectively.

If LB uses k < n marks: LB creates k+1 pieces. XY can use up to n marks to create up to n+k+1 pieces.

Example (n=2, LB uses 1 mark at 1/2):
- LB pieces: {1/2, 1/2}.
- XY marks at 1/4 and 3/4: pieces {1/4, 1/4, 1/4, 1/4}.
- 4 pieces, each picks 2. LB gets 1/4 + 1/4 = 1/2 < 4/7.

So using fewer marks hurts LB.

---

### Part 3: Optimal Strategy Pair

**LB's optimal:** n marks at geometric positions, creating pieces {1, 2, 4, ..., 2^n} / D.

**XY's optimal:** n-1 marks inside the largest piece, creating the "paired" configuration where sorted pieces are (2^{n-1}, 2^{n-1}, 2^{n-2}, 2^{n-2}, ..., 2, 2, 2, 1) / D.

With 2n pieces and alternating picks, LB gets positions 1, 3, 5, ..., 2n-1.

**Claim.** LB's total from this configuration = c(n).

**GAP:** Prove the exact value of the alternating sum.

---

### Part 4: Lower Bound - XY Cannot Do Better

**Claim.** Against LB's geometric marking, XY cannot limit LB to < c(n).

**Sub-claim:** Any XY response other than the (n-1)-mark strategy gives LB >= c(n).

**Case 1: XY uses fewer than n-1 marks.**
Fewer than n-1 + n = 2n-1 total marks means <= 2n-1 pieces. 
If 2n-1 pieces (odd), LB picks n and XY picks n-1. LB benefits from the extra pick.
The greedy selection on the geometric configuration gives LB >= c(n).

**Case 2: XY uses exactly n-1 marks, but not all in L_n.**
If some XY marks land in smaller pieces L_0, ..., L_{n-1}, then L_n remains larger, and LB picks L_n plus other pieces. 
Since L_n > sum of others, LB gains.

**Case 3: XY uses n marks.**
2n+1 pieces (odd). LB picks n+1, XY picks n. The extra pick for LB compensates for any equalization XY achieves.

**GAP:** Formalize each case rigorously.

---

### Part 5: Upper Bound - LB Cannot Do Better

**Claim.** No LB strategy guarantees > c(n).

**Approach:** For any LB configuration {p_1, ..., p_{k+1}} with k <= n marks, XY responds to limit LB.

If LB creates unequal pieces, XY cuts the largest to equalize.
If LB creates equal pieces, XY cuts one to create a slightly smaller piece that shifts the pick order.

**Key lemma:** For any LB configuration, XY can use n-1 marks to create a configuration where LB's alternating sum <= c(n).

**GAP:** Prove this general upper bound lemma.

---

## Key Lemmas (with mechanism)

1. **Parity principle:** XY prefers to create an even number of pieces (2n) so both pick n, rather than 2n+1 where LB picks n+1. This is because LB picks first, so an odd piece count always favors LB.

2. **Greedy is optimal (exchange argument):** In alternating selection, both players should always take the largest available. Deviating loses: if LB takes a smaller piece, that piece is replaced by a larger one in XY's picks.

3. **Geometric dominance (from crux aimo-0117):** In the geometric configuration {1, 2, 4, ..., 2^n}, the largest piece 2^n > sum of all others = 2^n - 1. This property ensures LB's first pick dominates.

4. **XY's (n-1)-mark optimality:** Using exactly n-1 marks maximizes XY's equalization while keeping piece count even (2n pieces). Using n marks creates 2n+1 pieces and backfires.

---

## Open Gaps

1. **Exact alternating sum for the optimal configuration:** Calculate LB's total when pieces are (2^{n-1}, 2^{n-1}, ..., 1)/D.

2. **Lower bound cases 1, 2, 3:** Rigorously prove LB >= c(n) in each case.

3. **Upper bound lemma:** Prove XY can limit ANY LB configuration to <= c(n).

---

## Cases to Cover

- XY uses j marks for j = 0, 1, 2, ..., n
- For each j, case by where marks are placed (inside L_n vs outside)

---

## Watch out for

- The piece count after both marking phases is (LB marks) + (XY marks) + 1, not 2n+1.
- The alternating sum depends on the exact sorted order, which can vary.
- LB marks and XY marks must be distinct, but this is rarely a binding constraint.
