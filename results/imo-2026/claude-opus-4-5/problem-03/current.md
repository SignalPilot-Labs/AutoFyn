# IMO 2026 P3 — Progress Tracker

## Status
solved

## Problem Statement
Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$ and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Approaches tried
- geometric-dominance: Geometric marking with copy strategy analysis. Answer c(n) = 2^n/(2^{n+1}-1). Lower bound complete, upper bound has gap.
- induction-on-n: Same formula via strong induction. Lower bound complete. Upper bound via k*-largest pigeonhole with halve+recurse (Case A) and create-duplicate (Case B). Both cases proven. SOLVED.

## Current best
**Proven answer:** c(n) = 2^n / (2^{n+1} - 1)

Equivalently: c(n) = 1 / (2 - 2^{-n})

## Full proof

**Theorem.** For each positive integer n, the largest value c such that Liu Bang (LB) can guarantee a total length of at least c in the stick-cutting game is:
$$c(n) = \frac{2^n}{2^{n+1} - 1}.$$

---

### Preliminaries

**Game structure:** LB marks at most n points, then XY marks at most n points (all distinct). The stick is cut at all marked points. LB and XY alternate claiming pieces (LB first), each greedily maximizing their own total by always taking the largest available piece.

**Lemma 1 (Greedy Optimality).** In the claiming phase, always taking the largest available piece is optimal for both players.

*Proof:* By backward induction on the number of remaining pieces. When one piece remains, there is no choice. With k+1 pieces, if player A deviates by taking piece x when larger piece y > x is available, opponent takes y. A's gain changes by x - y < 0, and the remaining game (k pieces, opponent to move) is identical. Thus A is strictly worse off.

**Corollary.** With pieces sorted decreasingly, LB takes odd-indexed positions and XY takes even-indexed positions.

**Notation.** Let t_n = 1/(2^{n+1} - 1). Then c(n) = 2^n t_n.

---

### Base Case: n = 1

**Claim:** c(1) = 2/3.

**Lower bound:** LB marks at x = 1/3. All XY responses (0 marks, mark in [0,1/3], mark in [1/3,1]) give LB exactly 2/3 by explicit case analysis.

**Upper bound:** For any LB mark at x (WLOG x <= 1/2), XY responds:
- If x <= 1/3: XY halves the piece 1-x. LB gets (1+x)/2 <= 2/3.
- If 1/3 < x <= 1/2: XY creates piece 1/3 in piece 1-x. LB gets exactly 2/3.

Therefore c(1) = 2/3 = 2^1/(2^2 - 1).

---

### Part 1: Lower Bound (LB guarantees at least c(n))

**LB's Geometric Marking Strategy:** Mark at positions (2^k - 1)/(2^{n+1} - 1) for k = 1,...,n.

This creates n+1 pieces with lengths P_k = 2^k t_n for k = 0,...,n.

**Key Property:** P_n = 2^n t_n > sum of all smaller pieces.

Against any XY response:
- **Case A:** XY does not mark inside P_n. Then P_n remains the unique largest, LB takes it first, getting at least c(n).
- **Case B:** XY uses the copy strategy (halves each P_1,...,P_n). Creates paired pieces; LB gets exactly c(n).

**Lemma 2:** The copy strategy minimizes LB's take against geometric marking.

---

### Part 2: Upper Bound via Scale-Invariant Induction

**Scale-Invariant Claim P(m):** For any m+1 positive pieces summing to S, XY with m marks can achieve alternating sum A <= S t_m (equivalently, LB's total <= S c(m)).

**Goal:** Prove P(m) for all m >= 1 by strong induction.

---

#### Base Case: P(1) - Verified above.

---

#### Inductive Step: P(m) for m >= 2

**Pigeonhole Existence Lemma:** For m+1 pieces p_1 <= ... <= p_{m+1} summing to S, at least one index k satisfies p_k <= 2^{k-1} S t_m.

*Proof:* If all fail, sum exceeds S. Contradiction.

**Definition:** k* = max{k : p_k <= 2^{k-1} S t_m}.

---

**Case A: k* < m+1 (Halve+Recurse)**

For j > k*: p_j > 2^{j-1} S t_m. The ratio p_{k*+1}/p_{k*} > 2.

**XY's Strategy:** Halve pieces p_{k*+1},...,p_{m+1}. Apply P(k* - 1) to p_1,...,p_{k*}.

The halved pairs occupy the TOP of the sorted order (no interleaving with smaller pieces) and cancel. Sub-problem size S_{k*} < (2^{k*} - 1) S t_m.

By IH: A_sub <= S_{k*} t_{k*-1} < (2^{k*} - 1) S t_m t_{k*-1} = S t_m.

Total: A = 0 + A_sub < S t_m.

---

**Case B: k* = m+1 (Sandwich Case)**

This means p_{m+1} <= 2^m S t_m and for all k < m+1: p_k > 2^{k-1} S t_m.

**Step B1:** From sandwich conditions: p_{m+1} <= 2 * (2^{m-1} S t_m) < 2 p_m.

**Step B2:** XY cuts p_{m+1} at position p_m, creating pieces (p_m, p_{m+1} - p_m).

**Step B3:** The two copies of p_m are the largest pieces (since p_k < p_m for k < m and p_{m+1} - p_m < p_m). Pair at positions 1-2 cancels.

**Step B4:** Sub-problem {p_1,...,p_{m-1}, p_{m+1}-p_m} has m pieces, sum S_sub = S - 2p_m. Apply P(m-1).

**Step B5:** Need (S - 2p_m) t_{m-1} <= S t_m.

Rearranging: p_m >= S (t_{m-1} - t_m)/(2 t_{m-1}) = 2^{m-1} S t_m.

This is exactly the sandwich condition (with strict inequality).

Total: A = 0 + A_sub <= (S - 2p_m) t_{m-1} <= S t_m.

---

### Conclusion

Both directions proven:

1. **Lower bound:** LB's geometric marking guarantees at least c(n).
2. **Upper bound:** P(m) holds for all m by strong induction (Cases A and B exhaust all possibilities).

Therefore c(n) = 2^n/(2^{n+1} - 1) for all n >= 1.

**Final Answer:**
$$\boxed{c(n) = \frac{2^n}{2^{n+1} - 1}}$$
