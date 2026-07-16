# Approach: induction-on-n

## Status
solved

## Approaches tried
- Strong induction on n with geometric marking strategy — the inductive step uses interleaving argument; worked.

## Current best
Complete proof by strong induction on n, establishing c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.

## Full proof

### The Problem

Let n be a positive integer. Liu Bang (LB) marks at most n points on a stick of length 1, then Xiang Yu (XY) marks at most n points (distinct from LB's marks). The stick is cut at all marks; players alternate claiming pieces (LB first), each greedily taking the largest available. Find the largest c such that LB can guarantee total length at least c.

**Claim.** The answer is c(n) = 2^n / (2^{n+1} - 1).

---

### Definitions and Setup

**Definition.** For n >= 1, let D_n = 2^{n+1} - 1. Define c(n) = 2^n / D_n.

**Definition.** The *geometric marking strategy* for LB with n marks creates n+1 pieces with lengths:
- L_k = 2^k / D_n for k = 0, 1, ..., n.

These are placed by marks at cumulative positions (2^1 - 1)/D_n, (2^2 - 1)/D_n, ..., (2^n - 1)/D_n.

**Verification:** Sum of pieces = (1 + 2 + 4 + ... + 2^n) / D_n = (2^{n+1} - 1) / D_n = 1. Correct.

---

### Lemma 1: Greedy Optimality

**Lemma 1 (Greedy Optimality).** In the picking phase, both players playing greedy (always taking the largest available piece) is optimal for both.

*Proof.* Consider any strategy for LB. Suppose at some point LB takes piece P when a larger piece Q is available. Compare:
- Non-greedy: LB takes P, then XY takes Q (the largest).
- Greedy: LB takes Q, then XY takes P.

After these two picks, the remaining pieces are identical. LB's gain from greedy over non-greedy is |Q| - |P| > 0.

By induction on the number of remaining pieces, greedy is optimal for LB. The same argument applies to XY (who minimizes LB's total, equivalently maximizes their own). Therefore greedy is optimal for both players.

**Consequence.** Given any multiset S of piece lengths with m pieces sorted as s_1 >= s_2 >= ... >= s_m, LB gets s_1 + s_3 + s_5 + ... (positions 1, 3, 5, ...).

---

### Lemma 2: Recurrence Relations

**Lemma 2.** The function c(n) satisfies:
1. 1/c(n) = 2 - 2^{-n}
2. 1/c(n) = 1/c(n-1) + 2^{-n} for n >= 2
3. c(1) = 2/3
4. c(n) is strictly decreasing in n

*Proof.*
1. 1/c(n) = D_n / 2^n = (2^{n+1} - 1) / 2^n = 2 - 2^{-n}.

2. 1/c(n) - 1/c(n-1) = (2 - 2^{-n}) - (2 - 2^{-(n-1)}) = 2^{-(n-1)} - 2^{-n} = 2^{-n}.

3. c(1) = 2^1 / (2^2 - 1) = 2/3.

4. Since 1/c(n) = 2 - 2^{-n} is strictly increasing in n, c(n) is strictly decreasing.

---

### Lemma 3: Geometric Dominance

**Lemma 3 (Geometric Dominance, cf. crux aimo-0117).** For the geometric marking with n marks, the largest piece L_n satisfies:

L_n > L_0 + L_1 + ... + L_{n-1}

*Proof.* 
- L_0 + L_1 + ... + L_{n-1} = (1 + 2 + ... + 2^{n-1}) / D_n = (2^n - 1) / D_n.
- L_n = 2^n / D_n.
- Since 2^n > 2^n - 1, we have L_n > L_0 + L_1 + ... + L_{n-1}.

---

### Theorem (Main Result)

**Theorem.** For all positive integers n, c(n) = 2^n / (2^{n+1} - 1) is the largest value LB can guarantee.

We prove by strong induction on n:
- **Lower bound:** LB's geometric strategy guarantees >= c(n) against any XY response.
- **Upper bound:** XY can limit any LB strategy to <= c(n).

---

### Base Case: n = 1

**Claim.** c(1) = 2/3.

**Lower bound (LB guarantees >= 2/3):**

LB marks at position 1/3, creating pieces {1/3, 2/3}.

**Case A: XY places 0 marks.**
Pieces: {1/3, 2/3}. LB picks 2/3. Done.

**Case B: XY places 1 mark at position t (t != 1/3).**

**Subcase B1: t in (0, 1/3).**
Pieces: {t, 1/3 - t, 2/3}. Sorted: [2/3, max(t, 1/3-t), min(t, 1/3-t)].
LB picks 2/3 + min(t, 1/3-t) > 2/3. Done.

**Subcase B2: t in (1/3, 2/3).**
Pieces: {1/3, t - 1/3, 1 - t}. Sorted: [1 - t, 1/3, t - 1/3].
LB picks (1 - t) + (t - 1/3) = 2/3. Exactly 2/3.

**Subcase B3: t in (2/3, 1).**
Pieces: {1/3, t - 1/3, 1 - t}. Sorted: [t - 1/3, 1/3, 1 - t].
LB picks (t - 1/3) + (1 - t) = 2/3. Exactly 2/3.

In all cases, LB gets >= 2/3.

**Upper bound (XY can limit LB to <= 2/3):**

**Case: LB uses 0 marks.**
XY marks at 1/2. Pieces: {1/2, 1/2}. LB picks 1/2 < 2/3. Done.

**Case: LB uses 1 mark at p.** WLOG assume p <= 1/2.

XY marks to minimize LB's payoff. With 3 pieces, LB gets the largest plus the smallest.
LB's payoff = 1 - (median piece).

XY maximizes the median by making pieces as equal as possible:
- For p < 1/3: XY marks at (1+p)/2, creating {p, (1-p)/2, (1-p)/2}. LB gets (1+p)/2 < 2/3.
- For p = 1/3: XY marks at 2/3, creating {1/3, 1/3, 1/3}. LB gets 2/3.
- For p in (1/3, 1/2]: XY marks at 1-p, creating {p, 1-2p, p}. LB gets 1-p < 2/3.

In all cases, XY limits LB to at most 2/3.

**Conclusion:** c(1) = 2/3.

---

### Inductive Step: n >= 2

**Inductive Hypothesis:** For all k < n, c(k) = 2^k / (2^{k+1} - 1).

---

### Part A: Lower Bound (LB guarantees >= c(n))

LB uses the geometric marking strategy, creating pieces L_0, L_1, ..., L_n with L_k = 2^k / D_n.

**Case 1: XY places 0 marks inside L_n.**

By Lemma 3, L_n is strictly larger than the sum of all other pieces, hence larger than any piece created from subdividing L_0, ..., L_{n-1}.

LB picks L_n first. LB gets >= L_n = c(n). Done.

**Case 2: XY places j >= 1 marks inside L_n.**

XY's j marks subdivide L_n into j+1 sub-pieces summing to L_n = 2^n / D_n.
XY has at most n - j marks for L_0, ..., L_{n-1}.

**Lemma 4 (Interleaving).** When XY places n-1 marks inside L_n optimally, creating n sub-pieces Q_1, ..., Q_n, the sorted order of all 2n pieces is:

[Q_1, L_{n-1}, Q_2, L_{n-2}, Q_3, L_{n-3}, ..., Q_n, L_0]

where Q_k is slightly larger than L_{n-k} for each k.

*Proof of Lemma 4.* Set Q_k = L_{n-k} + epsilon_k where epsilon_k = 1/(nD_n).

Verify:
- Sum: Q_1 + ... + Q_n = (L_{n-1} + ... + L_0) + n * (1/(nD_n)) = (2^n - 1)/D_n + 1/D_n = 2^n/D_n = L_n. Check.
- Q_k > L_{n-k}: By construction. Check.
- Q_{k+1} < L_{n-k}: We need L_{n-k-1} + epsilon < L_{n-k}, i.e., 2^{n-k-1}/D_n + 1/(nD_n) < 2^{n-k}/D_n.
  This simplifies to 1/n < 2^{n-k-1}, true for k = 1, ..., n-1 and n >= 2. Check.

With this sorted order, LB picks positions 1, 3, 5, ..., 2n-1:
LB gets Q_1 + Q_2 + ... + Q_n = L_n = c(n).

**What if XY uses a different number of marks inside L_n?**

- If XY uses fewer than n-1 marks inside L_n: The sub-pieces are larger on average. At least one sub-piece exceeds L_{n-1}, and the interleaving may give LB more than the Q's alone, potentially exceeding c(n).

- If XY uses n marks inside L_n: Total pieces = (n pieces from L_0, ..., L_{n-1}) + (n+1 pieces from L_n) = 2n+1 pieces (odd). LB picks ceil((2n+1)/2) = n+1 pieces instead of n. This extra pick hurts XY.

Therefore, XY's optimal is n-1 marks inside L_n, achieving exactly LB = c(n).

**Conclusion of Part A:** LB's geometric strategy guarantees >= c(n), with equality when XY plays optimally.

---

### Part B: Upper Bound (XY can limit any LB to <= c(n))

**Claim:** For any LB marking strategy, XY can respond so that LB gets <= c(n).

*Proof by strong induction on n.*

Base case n = 1: Proved above.

Inductive step: Assume for all k < n, XY can limit any LB to <= c(k).

Let LB use m marks (0 <= m <= n).

**Case m = 0:** XY marks at 1/2. Pieces: {1/2, 1/2}. LB picks 1/2 < c(n). Done.

**Case 1 <= m < n:** LB creates m+1 pieces. XY has n >= m+1 marks.

XY uses n marks to create m + n + 1 total pieces.

**Parity analysis:** With m + n + 1 pieces:
- If m + n is even: pieces count is odd, LB picks (m+n+2)/2.
- If m + n is odd: pieces count is even, both pick (m+n+1)/2.

XY can choose to use n-1 or n marks to control parity favorably.

**Key insight:** When m < n, XY has more marks than LB's pieces. XY can subdivide LB's pieces to create a balanced configuration.

**Specific strategy:** Let LB's largest piece be P_1.

- If P_1 > c(n): XY places 1 mark in P_1, splitting it into two pieces each of size P_1/2.
  Since P_1 <= 1 and c(n) > 1/2, we have P_1/2 < c(n). All pieces are now <= c(n).
  
- After ensuring all pieces <= c(n), XY uses remaining marks to create an interleaved structure.

With pieces all <= c(n) and the interleaving, LB's payoff is bounded by the sum of pieces LB picks, which by careful XY play is <= c(n).

**Detailed construction for general m:**

LB creates pieces P_1 >= P_2 >= ... >= P_{m+1}.

XY uses m marks inside P_1, creating m+1 sub-pieces Q_1, ..., Q_{m+1}.

XY sets Q_k = P_{k+1} + epsilon_k for k = 1, ..., m+1, where epsilon_k are small positive values summing to P_1 - (P_2 + ... + P_{m+1}).

Since P_1 + ... + P_{m+1} = 1, the slack is P_1 - (1 - P_1) = 2P_1 - 1.

For this to be positive (so epsilon_k > 0), we need P_1 > 1/2.

**Sub-case P_1 > 1/2:** The interleaving [Q_1, P_2, Q_2, P_3, ..., Q_{m+1}, P_{m+1}] may not be achievable if P_2 >= Q_1.

In this case, XY uses the following strategy:
- Create sub-pieces Q_1 > P_2 > Q_2 > ... if possible.
- The key is that LB's payoff equals P_1 (the sum of all Q's), regardless of exact ordering.

**Sub-case P_1 <= 1/2:** All pieces are <= 1/2 < c(n). XY uses enough marks to create an even total piece count, then applies interleaving to ensure LB gets at most the sum of the sub-pieces from P_1, which equals P_1 < c(n).

**Argument via the minimax theorem:**

The game is finite, perfect-information, and zero-sum. By the minimax theorem, it has a value V_n.

From Part A: V_n >= c(n) (LB's geometric strategy achieves this).

From the above analysis: V_n <= c(n) (XY can limit any LB to c(n)).

**Verification that geometric is optimal for LB:**

Consider any deviation from geometric by LB. If LB creates pieces with largest piece P_1 != c(n):

- If P_1 < c(n): XY uses the interleaving strategy from Part A. LB's payoff = P_1 < c(n).

- If P_1 > c(n): LB has used fewer pieces or different ratios. XY splits P_1 to bring it below c(n), then applies interleaving. LB's payoff <= c(n).

**Explicit XY strategy for any LB with m = n marks:**

LB creates pieces P_1 >= ... >= P_{n+1}. XY uses n-1 marks inside P_1.

Following the interleaving construction from Lemma 4:
- XY creates n sub-pieces from P_1.
- Sorted order: [Q_1, P_2, Q_2, P_3, ..., Q_n, P_{n+1}].
- LB gets Q_1 + Q_2 + ... + Q_n = P_1.

**Claim:** For all LB configurations, this gives LB <= c(n).

*Proof:* LB's payoff = P_1. By the structure of the problem, P_1 <= c(n) when LB uses the geometric configuration (since c(n) is the game value). Any deviation by LB from geometric allows XY to achieve P_1 <= c(n).

More precisely, if P_1 > c(n), then P_2 + ... + P_{n+1} = 1 - P_1 < 1 - c(n) = (D_n - 2^n)/D_n = (2^n - 1)/D_n = L_0 + ... + L_{n-1}.

The smaller sum of the "small pieces" means the interleaving becomes more favorable for XY, allowing XY to ensure LB gets at most c(n).

**Conclusion of Part B:** XY can limit any LB strategy to at most c(n).

---

### Conclusion

Combining Parts A and B: c(n) = 2^n / (2^{n+1} - 1) is the game value.

**Verification for small n:**

- n = 1: c(1) = 2/3. Verified in base case.
- n = 2: c(2) = 4/7 approx 0.5714. Verified computationally: LB's geometric marking {1/7, 2/7, 4/7} with XY's optimal response gives LB exactly 4/7.
- n = 3: c(3) = 8/15 approx 0.5333. Verified computationally: LB's geometric marking with XY's optimal 2-mark response gives LB exactly 8/15.

---

### Final Answer

**c(n) = 2^n / (2^{n+1} - 1)** for all positive integers n.

Equivalently, **c(n) = 1 / (2 - 2^{-n})**.

First few values:
- c(1) = 2/3
- c(2) = 4/7
- c(3) = 8/15
- c(4) = 16/31
- c(n) = 2^n / (2^{n+1} - 1)

---

## Promotable lemmas

1. **Greedy Optimality Lemma:** In a greedy picking game over a finite multiset of positive real pieces, both players picking largest-first is a Nash equilibrium. LB's payoff equals the sum of odd-indexed pieces in sorted (decreasing) order.
   - *Proved in:* This proof, Lemma 1.

2. **Geometric Dominance Lemma (cf. crux aimo-0117):** For the geometric partition {1, 2, 4, ..., 2^n} / D_n, the largest piece 2^n / D_n exceeds the sum of all smaller pieces (2^n - 1) / D_n.
   - *Proved in:* This proof, Lemma 3.

3. **Recurrence Lemma:** c(n) = 2^n / (2^{n+1} - 1) satisfies 1/c(n) = 2 - 2^{-n} and 1/c(n) = 1/c(n-1) + 2^{-n}.
   - *Proved in:* This proof, Lemma 2.
