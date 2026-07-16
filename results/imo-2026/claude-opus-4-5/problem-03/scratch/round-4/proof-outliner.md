## imo-2026-03

geometric-direct: advance
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Strong induction on n, with the **Pairing Cancellation Lemma** as the key tool for the upper bound
Skeleton:
  1. Import Greedy Optimality Lemma (CERTIFIED) — by lemmas/greedy-optimality.md
  2. Import Geometric Dominance Lemma (CERTIFIED) — by Part 1
  3. Lower bound via geometric config — by Part 3 (already complete)
  4. **Upper bound via Pairing Cancellation Lemma + induction** — this is the gap to close:
     a. State Pairing Cancellation Lemma: For any multiset S and any v > 0, LB's greedy score from {v, v} ∪ S equals v + LB's greedy score from S — by parity argument (shift-by-2 preserves alternating structure)
     b. Base case n=1: If P_2 <= c(1) = 2/3, XY uses 0 marks, LB gets P_2 <= c(1). If P_2 > 2/3, XY splits P_2 evenly; LB gets (1+P_1)/2 < 2/3. — by Part 4 Case A/B
     c. Inductive step n >= 2: If P_1 <= c(n), XY uses 0 marks, LB gets at most P_1 <= c(n). If P_1 > c(n), XY splits P_1 into {P_1/2, P_1/2} (1 mark), then applies (n-1)-case strategy to {P_2,...,P_{n+1}} (n pieces, n-1 marks). — by Pairing Cancellation + induction hypothesis (scaled by 1-P_1)
     d. Algebraic identity: c(n-1) = c(n) / (2·(1-c(n))) — by fraction arithmetic
     e. Conclusion: LB <= P_1/2 + c(n-1)·(1-P_1) <= c(n) when P_1 >= c(n), with equality iff P_1 = c(n). — by d + monotonicity
  5. c(n) = 2^n/(2^{n+1}-1) — by Parts 3 + 4
Key lemmas (claim + the one-line mechanism that makes it true):
  - **Pairing Cancellation Lemma**: For any multiset S and v > 0, LB_score({v, v} ∪ S) = v + LB_score(S) — because the two copies of v insert at consecutive positions in sorted order; shift-by-2 preserves all parities, and one v goes to each player, canceling in the alternating sum
  - **Algebraic identity**: c(n-1) = c(n)/(2·(1-c(n))) — because 2^{n-1}/(2^n-1) = (2^n/D) / (2·(2^n-1)/D) = c(n) / (2·(1-c(n))) where D = 2^{n+1}-1
  - **Monotonicity of LB bound**: f(P_1) = P_1/2 + c(n-1)·(1-P_1) is linear in P_1 with slope (1/2 - c(n-1)) < 0 since c(n-1) > 1/2; thus f(P_1) decreases as P_1 increases beyond c(n), and f(c(n)) = c(n) exactly
Open gaps: The Pairing Cancellation Lemma needs a rigorous parity proof (the explorer verified computationally; now formalize). The algebraic identity and monotonicity are straightforward.
Cases to cover:
  - Case P_1 <= c(n): XY uses 0 marks
  - Case P_1 > c(n): XY uses 1 mark (split P_1), then recurses
Watch out for:
  - The sub-game has n pieces {P_2,...,P_{n+1}} and n-1 XY marks; verify this matches the (n-1)-case hypothesis (n-1 marks on n-1+1=n pieces, which is correct)
  - The scaling: sub-game pieces sum to 1-P_1, not 1; the induction hypothesis gives LB <= c(n-1)·(1-P_1) (scaled bound)
  - Edge case P_1 = c(n): equality holds (this is the geometric config)

---

pairing-cancellation-induction: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Direct induction on n using Pairing Cancellation as the sole mechanism (cleaner formulation than geometric-direct's Case A/B)
Skeleton:
  1. Define c(n) = 2^n/(2^{n+1}-1) and the recurrence c(n) = 2·c(n-1)·(1-c(n)) / (1 + 2·c(n-1)·(1-c(n)/c(n-1)))... actually simpler: c(n-1) = c(n)/(2(1-c(n)))
  2. Import Greedy Optimality — LB's score = sum of odd-indexed pieces in sorted descending order
  3. State Pairing Cancellation Lemma: Adding {v, v} to any multiset increases LB's score by exactly v
  4. **Lower bound by induction**: Base n=1: config {1/3, 2/3} gives LB = 2/3. Inductive step: config {P_1,...,P_n, L_n} where L_n = c(n), P_k = c(k-1)/sum for k=1,...,n (suitably scaled geometric). XY's any mark in L_n creates {t, L_n-t}; by Pairing Cancellation-like analysis, LB >= L_n. (This mirrors the old Part 3.)
  5. **Upper bound by induction**: Base n=1 as above. Inductive step: XY's strategy is "always split the largest LB piece in half." If P_1 > c(n): XY splits P_1 into {P_1/2, P_1/2}, LB_score = P_1/2 + LB_score({P_2,...,P_{n+1}}) by Pairing Cancellation. By IH, XY can limit the sub-game to c(n-1)·(1-P_1). Total = P_1/2 + c(n-1)·(1-P_1) <= c(n). If P_1 <= c(n): XY uses 0 marks, LB <= P_1 <= c(n).
  6. Both bounds = c(n) at geometric config => c(n) is the value.
Key lemmas (claim + the one-line mechanism that makes it true):
  - Same as geometric-direct
Open gaps: Formally prove Pairing Cancellation (parity shift argument)
Cases to cover: P_1 <= c(n) vs P_1 > c(n)
Watch out for: Same as geometric-direct

---

two-strategy-cover: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Case split on P_1 vs L_0 = 1/(2^{n+1}-1) + explicit XY strategy for each case (from LP/convex explorer)
Skeleton:
  1. Import certified lemmas (Greedy Optimality, Geometric Dominance, Parity)
  2. Lower bound via geometric config — same as geometric-direct Part 3
  3. **Upper bound Case 2b (P_{n+1} > c(n) and P_1 <= L_0)**: XY uses n marks on P_{n+1} creating n+1 sub-pieces {P_n, P_{n-1},..., P_2, r, r} where r = (P_{n+1} - sum_{k=2}^n P_k)/2 = (2P_{n+1}-1+P_1)/2. The 2n+1 pieces form P_1 (singleton) + n pairs. LB = P_2 + ... + P_n + r + P_1 = 1/2 + P_1/2 <= c(n) since P_1 <= L_0 = 2c(n)-1. — by induction explorer's explicit formula
  4. **Upper bound Case 2a (P_{n+1} > c(n) and P_1 > L_0)**: XY uses 1 mark to split P_{n+1} in half; LB = 1 - P_1 - P_{n+1}/2 <= c(n) since P_1 + P_{n+1}/2 >= L_0 + c(n)/2 = 1 - c(n). — by sum constraints
  5. **Upper bound Case 1 (P_{n+1} <= c(n))**: XY uses 0 marks; LB gets <= P_{n+1} <= c(n) — trivial
  6. Combine all cases => XY limits any LB to <= c(n)
Key lemmas (claim + the one-line mechanism that makes it true):
  - **Case 2b pairing formula**: LB = 1/2 + P_1/2 — because the n pairs contribute one copy each to LB (pairing argument), and sum(one from each pair) + P_1 = (P_2+...+P_n+r) + P_1 = 1/2 + P_1/2
  - **Case 2a sum constraint**: P_1 > L_0 and P_{n+1} > c(n) imply P_1 + P_{n+1}/2 > 1-c(n) — because L_0 + c(n)/2 = 1/(D) + 2^{n-1}/(D) = (1+2^{n-1})/D = (2^n-1+2)/(2D) = ... (verify algebra)
Open gaps: Case 2a algebraic verification for general n (proved for n=2, conjectured for n>=3)
Cases to cover: P_1 <= L_0 vs P_1 > L_0, crossed with P_{n+1} > c(n) vs P_{n+1} <= c(n)
Watch out for: Case 2a is only computationally verified for n=3; needs algebraic proof

---

minimax-saddle-point: advance
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n
Technique: Game-theoretic saddle-point analysis; geometric config is where all XY strategies equalize
Skeleton:
  1. Same lower bound as geometric-direct
  2. Upper bound via concavity: V(P) = min_{XY response} LB_greedy_value is concave (minimum of linear functions). Max of concave over simplex is at the unique critical point = geometric config.
  3. At geometric config, all XY strategies (shadow-b, split-halves, pairing) give LB = c(n) exactly => complementary slackness => geometric is the saddle.
  4. For non-geometric configs, at least one XY strategy gives LB < c(n).
Key lemmas (claim + the one-line mechanism that makes it true):
  - **Concavity of V**: V(P) = min_sigma f_sigma(P) where f_sigma is linear in P => V is concave — standard convex-analysis fact
  - **Saddle-point characterization**: geometric config is where multiple XY strategies achieve the same value c(n) — verified computationally for n=1,2,3
Open gaps: Making the concavity argument rigorous (defining the strategy space, verifying continuity, etc.)
Cases to cover: none (structural argument)
Watch out for: This approach gives intuition but the "uniqueness of critical point" needs a rigorous proof (may be harder than direct induction)

---

## Build Set

**build set: geometric-direct**

The geometric-direct approach should be advanced with the new **Pairing Cancellation Lemma** upper bound proof from the interleaving explorer. The builder should:

1. **Replace Part 4 (Upper Bound)** with the clean inductive proof:
   - State and prove the Pairing Cancellation Lemma (parity argument)
   - Base case n=1 (already present)
   - Inductive step: P_1 <= c(n) => use 0 marks; P_1 > c(n) => split P_1 in half, apply (n-1)-IH to sub-game, use Pairing Cancellation to conclude LB <= c(n)
   - Prove the algebraic identity c(n-1) = c(n)/(2(1-c(n)))
   - Conclude monotonicity of f(P_1) = P_1/2 + c(n-1)(1-P_1)

2. **Verify the sub-game reduction is valid**: The sub-game has n pieces {P_2,...,P_{n+1}} summing to 1-P_1, and XY has n-1 marks remaining. The IH applies to this (n-1)-mark game, giving LB from sub-game <= c(n-1)·(1-P_1).

3. **Update the status to solved** once the proof is complete.

The other approaches (pairing-cancellation-induction, two-strategy-cover, minimax-saddle-point) are conceptually similar and don't need separate building this round; the Pairing Cancellation proof is the cleanest and geometric-direct already has the complete lower bound.
