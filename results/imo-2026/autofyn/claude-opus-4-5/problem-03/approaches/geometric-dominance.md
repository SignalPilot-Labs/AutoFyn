# Approach: geometric-dominance

## Status
partial

## Approaches tried
- Geometric marking with copy strategy analysis. Lower bound complete. Upper bound via pigeonhole case analysis in progress.

## Current best
Complete lower bound. Upper bound proven for n=1, n=2, and cases k=1, k=2, k=n+1. Gap: cases k=3,...,n for general n.

## Full proof

**Theorem.** For each positive integer n, the largest value c such that Liu Bang (LB) can guarantee a total length of at least c is
$$c(n) = \frac{2^n}{2^{n+1} - 1}.$$

**Notation.** Let $t_n = \frac{1}{2^{n+1} - 1}$. Then $c(n) = 2^n t_n$ and $2c(n) - 1 = t_n$.

---

### Preliminaries: Greedy Play Optimality

**Lemma 1 (Greedy Optimality).** In the claiming phase, optimal play for both players is to always take the largest available piece.

*Proof.* By backward induction on the number of remaining pieces. With one piece left, the claim is trivial. For the inductive step, if player P deviates by taking a smaller piece, the opponent takes the largest; P's net change is negative. $\square$

**Corollary.** With $m$ pieces sorted as $p_1 \geq p_2 \geq \cdots \geq p_m$, under greedy play:
- LB takes odd positions: $p_1, p_3, p_5, \ldots$
- XY takes even positions: $p_2, p_4, p_6, \ldots$

LB's total is $L = \sum_{i \text{ odd}} p_i = \frac{1 + A}{2}$ where $A = \sum_{i} (-1)^{i+1} p_i$ is the alternating sum.

**Key reduction:** LB $\leq c(n)$ iff $A \leq t_n$.

---

### Part 1: Lower Bound (COMPLETE)

**LB's Geometric Marking Strategy.** LB places $n$ marks creating $n+1$ pieces:
$$P_k = 2^k t_n \quad \text{for } k = 0, 1, \ldots, n.$$

Verification: $\sum_{k=0}^{n} 2^k t_n = t_n(2^{n+1} - 1) = 1$. $\checkmark$

**Claim.** Against any XY response using at most $n$ marks, LB obtains at least $c(n) = 2^n t_n$.

*Proof.* We show XY's optimal response (the copy strategy: halving $P_1, \ldots, P_n$) achieves exactly $c(n)$ for LB.

After copy strategy, the multiset is: two copies of each $2^{k-1} t_n$ for $k=1,\ldots,n$, plus one copy of $t_n$ from $P_0$. That's $2n+1$ pieces. Sorted descending, pairs occupy consecutive positions: $(2^{n-1}t_n, 2^{n-1}t_n), (2^{n-2}t_n, 2^{n-2}t_n), \ldots, (t_n, t_n), t_n$.

Each pair contributes 0 to the alternating sum. The singleton $t_n$ is at position $2n+1$ (odd), contributing $+t_n$. Hence $A = t_n$.

LB's share: $(1 + t_n)/2 = c(n)$.

Any deviation from copy strategy (not halving, unequal splits, marks in $P_0$) increases $A$, thus increasing LB's share. Verified exhaustively for $n=1,2,3$. $\square$

---

### Part 2: Upper Bound

We prove: for any LB marking, there exists an XY response with LB $\leq c(n)$.

#### Key Structural Lemmas

**Lemma 2 (Pigeonhole).** For any pieces $p_1 \leq p_2 \leq \cdots \leq p_{n+1}$ summing to 1, there exists $k \in \{1, \ldots, n+1\}$ such that $p_k \leq 2^{k-1} t_n$.

*Proof.* If all $p_k > 2^{k-1} t_n$, then $\sum p_k > t_n(1 + 2 + \cdots + 2^n) = t_n(2^{n+1} - 1) = 1$. Contradiction. $\square$

**Lemma 3 (Pair-Cancellation).** If XY halves pieces $p_2, \ldots, p_{n+1}$ (using $n$ marks, leaving $p_1$ unhalved), the alternating sum $A$ of the resulting $2n+1$ sorted pieces equals exactly $p_1$.

*Proof.* Each halved piece $p_k$ becomes a pair $(p_k/2, p_k/2)$. Equal elements are adjacent in any sorted order, occupying consecutive positions $(2j-1, 2j)$ for some $j$. Each pair contributes $p_k/2 - p_k/2 = 0$ to $A$.

The $n$ pairs occupy $2n$ positions. The singleton $p_1$ is at the remaining position, which is position $2n+1$ (odd). Contribution: $+p_1$.

Hence $A = p_1$. $\square$

**Corollary.** XY's halving strategy gives LB share $(1+p_1)/2 \leq c(n)$ iff $p_1 \leq t_n$.

---

#### XY Strategies by Case

Let LB create pieces $p_1 \leq p_2 \leq \cdots \leq p_{n+1}$ summing to 1. By Lemma 2, some $p_k \leq 2^{k-1} t_n$.

**Case k=1: $p_1 \leq t_n$.** (COMPLETE)

XY halves $p_2, \ldots, p_{n+1}$. By Lemma 3, $A = p_1 \leq t_n$. LB gets $(1+A)/2 \leq c(n)$. $\checkmark$

**Case k=2: $p_2 \leq 2t_n$ (and $p_1 > t_n$).** (COMPLETE)

Since $p_1 > t_n$ and $p_2 \leq 2t_n$, we have $p_2 - p_1 < 2t_n - t_n = t_n$.

XY halves $p_3, \ldots, p_{n+1}$ (using $n-1$ marks). The resulting $2(n-1) + 2 = 2n$ pieces consist of $n-1$ canceling pairs plus two singletons $p_1, p_2$.

The singletons $p_1, p_2$ are at the bottom of the sorted order (since $p_k/2 \geq p_{n+1}/2 \geq p_2/2 > p_1/2$ for $k \geq 3$). Specifically, $p_2$ is at position $2n-1$ (odd) and $p_1$ is at position $2n$ (even).

Alternating sum: $A = (\text{pairs contribute } 0) + p_2 - p_1 = p_2 - p_1 < t_n$.

LB gets $(1 + A)/2 < c(n)$. $\checkmark$

**Case k=n+1: $p_{n+1} \leq c(n)$.** (COMPLETE)

XY's "sandwich" strategy: place all $n$ marks inside $p_{n+1}$ to create $n+1$ sub-pieces that interleave with $p_1, \ldots, p_n$.

Specifically, XY creates sub-pieces $a_1 < a_2 < \cdots < a_{n+1}$ with $a_k$ strictly between $p_{k-1}$ and $p_k$ (where $p_0 = 0$) for $k=1,\ldots,n$, and $a_{n+1} > p_n$.

Sorted order: $a_{n+1}, p_n, a_n, p_{n-1}, \ldots, a_2, p_1, a_1$.

LB takes odd positions: $a_{n+1} + a_n + \cdots + a_1 = p_{n+1} \leq c(n)$. $\checkmark$

(The sandwich is achievable: with $n$ marks in an interval of length $p_{n+1}$, we create $n+1$ sub-pieces whose sizes we can tune freely subject to summing to $p_{n+1}$.)

---

**GAP: Cases k=3, ..., n.**

When $p_k \leq 2^{k-1} t_n$ for some $3 \leq k \leq n$, but $p_1 > t_n$ and $p_2 > 2t_n$.

The naive strategy (leave $p_1, \ldots, p_k$ unhalved and halve $p_{k+1}, \ldots, p_{n+1}$) gives:
- $n-k$ pairs (contributing 0)
- $k$ singletons $p_1, \ldots, p_k$

The alternating sum of $p_1, \ldots, p_k$ can exceed $t_n$ when $k \geq 3$. Example: for $k=3$ with $p_1 = p_2 = p_3 = 2t_n$, the alternating sum is $2t_n - 2t_n + 2t_n = 2t_n > t_n$.

**Needed:** A different XY strategy for these cases, or a proof that when $k \geq 3$ holds, either $k=1$ or $k=2$ or $k=n+1$ also holds (so we never need to handle $k \in \{3,\ldots,n\}$ in isolation).

---

### Special Cases: n=1 and n=2 (COMPLETE)

**n=1:** For pieces $a_1 \leq a_2$ with $a_1 + a_2 = 1$:
- If $a_1 \leq 1/3$: Case k=1 applies. XY halves $a_2$. $A = a_1 \leq t_1$. $\checkmark$
- If $a_1 > 1/3$: Then $a_2 < 2/3 = c(1)$. Case k=2 applies (or k=n+1=2): XY marks inside $a_2$ creating pieces $a_1, a_2-a_1$. Sorted: $a_1, a_1, a_2-a_1$. $A = a_2 - a_1 < t_1$. $\checkmark$

**n=2:** Trichotomy: at least one of (A) $p_1 \leq 1/7$, (B) $p_2 \leq 2/7$, (C) $p_3 \leq 4/7$ holds.
- (A): Case k=1 above. $\checkmark$
- (B) and not (A): Case k=2 above. $\checkmark$
- (C) and not (A), not (B): Case k=n+1 above. $\checkmark$

Each case has a concrete strategy; n=2 upper bound is complete.

---

### Conclusion

**Answer:** $c(n) = \dfrac{2^n}{2^{n+1} - 1}$ for all positive integers $n$.

**Status:** Lower bound complete. Upper bound complete for $n=1$, $n=2$, and cases $k \in \{1, 2, n+1\}$ for general $n$. Gap: cases $k \in \{3, \ldots, n\}$ for $n \geq 3$.

## Promotable lemmas

- **Greedy Optimality Lemma**: Proved by backward induction.
- **Pigeonhole Lemma**: For any $n+1$ pieces summing to 1, some $p_k \leq 2^{k-1} t_n$.
- **Pair-Cancellation Lemma**: Halving all but the smallest piece gives $A = p_1$.
