# Approach: ratio-based-induction

## Status
partial

## Approaches tried
- Ratio-based recursion: XY's strategy depends on ratio a_{n+1}/a_n (threshold 2). In progress.

## Current best
Clean n=1 proof complete. Inductive step outlined but not rigorous.

## Full proof

**Theorem.** For each positive integer n, the largest value c such that Liu Bang (LB) can guarantee a total length of at least c is
$$c(n) = \frac{2^n}{2^{n+1} - 1}.$$

**Notation.** Let $t_n = \frac{1}{2^{n+1} - 1}$. Then $c(n) = 2^n t_n$.

---

### Preliminaries

**LB's share formula.** With $m$ sorted pieces $p_1 \geq p_2 \geq \cdots \geq p_m$, LB takes odd positions. LB's share is $(1+A)/2$ where $A = \sum_i (-1)^{i+1} p_i$ is the alternating sum.

**Key reduction:** LB $\leq c(n)$ iff $A \leq t_n$.

---

### Lower Bound (from geometric-dominance approach)

LB's geometric marking achieves exactly $c(n)$ against XY's optimal response. Proved in geometric-dominance.md.

---

### Upper Bound via Ratio-Based Recursion

**Core idea:** The geometric marking has $a_{k+1}/a_k = 2$ for all $k$. This ratio 2 is a threshold:
- If the largest ratio exceeds 2, XY exploits by halving.
- If all ratios are $\leq 2$, XY exploits by cloning.

**n=1 Base Case (COMPLETE):**

LB creates pieces $a_1 \leq a_2$ with $a_1 + a_2 = 1$. XY has 1 mark.

**Case 1: $a_2/a_1 > 2$ (equivalently, $a_1 < 1/3$).**

XY halves $a_2$. Pieces: $a_2/2, a_2/2, a_1$.

Since $a_2 > 2a_1$, we have $a_2/2 > a_1$. Sorted: $a_2/2, a_2/2, a_1$.

Alternating sum: $A = a_2/2 - a_2/2 + a_1 = a_1 < 1/3 = t_1$. $\checkmark$

**Case 2: $a_2/a_1 \leq 2$ (equivalently, $a_1 \geq 1/3$).**

XY marks inside $a_2$ at distance $a_1$ from one end, creating pieces $a_1$ and $a_2 - a_1$.

Since $a_1 \geq 1/3$ and $a_2 \leq 2a_1$, we have $a_2 - a_1 \leq a_1$.

Sorted: $a_1, a_1, a_2 - a_1$.

Alternating sum: $A = a_1 - a_1 + (a_2 - a_1) = a_2 - a_1 = 1 - 2a_1 \leq 1/3 = t_1$. $\checkmark$

Both cases give $A \leq t_1$, so LB $\leq c(1)$. Equality when $a_1 = 1/3$, i.e., $a_2/a_1 = 2$.

---

**Inductive Setup:**

**Strengthened hypothesis:** For any $m \leq n+1$ pieces summing to $S$ with smallest piece $\leq S \cdot t_{m-1}$, XY (with $m-1$ marks) can achieve $A \leq S \cdot t_{m-1}$.

This is scale-invariant: scaling all pieces by $\lambda$ scales both $A$ and $S$ by $\lambda$, preserving the bound.

**Inductive step for $n+1$ pieces summing to 1:**

Let $a_1 \leq a_2 \leq \cdots \leq a_{n+1}$ with $\sum a_i = 1$. XY has $n$ marks.

Consider the ratio $r = a_{n+1}/a_n$.

**Case r > 2:**

XY halves $a_{n+1}$. The pair $(a_{n+1}/2, a_{n+1}/2)$ contributes 0 to $A$.

Remaining configuration: pieces $a_1, \ldots, a_n$ plus the pair, with $n-1$ XY marks.

The pair, being equal, occupies consecutive sorted positions and contributes 0 to any alternating sum.

The "effective" residual problem has $n$ pieces $a_1, \ldots, a_n$ summing to $S' = 1 - a_{n+1}$, with $n-1$ XY marks.

By induction (if $a_1 \leq S' \cdot t_{n-1}$), XY achieves $A' \leq S' \cdot t_{n-1}$.

Total $A = A'$ (since the pair contributes 0).

**GAP:** Must verify $a_1 \leq S' \cdot t_{n-1}$ follows from the given constraints. Also, the pair may interleave with residual pieces, changing the sorted structure.

**Case r <= 2:**

XY clones $a_n$ inside $a_{n+1}$: mark at distance $a_n$ from one end, creating pieces $a_n$ and $a_{n+1} - a_n$.

The two copies of $a_n$ contribute 0 when they're adjacent in sorted order.

Remaining configuration: pieces $a_1, \ldots, a_{n-1}, a_n, a_n, a_{n+1}-a_n$, with $n-1$ XY marks.

**GAP:** The cloned pieces may not be adjacent in the sorted order (if $a_{n+1} - a_n < a_{n-1}$). The alternating sum analysis requires care.

---

### What Remains

The inductive argument is promising but not complete. The gaps are:

1. **Sorted order after the first XY move:** The halved/cloned pieces may interleave with the residual pieces in a way that changes the inductive structure.

2. **Residual problem satisfies IH:** Must verify the residual configuration satisfies the inductive hypothesis.

3. **Combining A contributions:** The total alternating sum is not simply the sum of contributions from the pair and the residual.

**Alternative approach:** Instead of induction on $n$, use the pigeonhole case analysis from geometric-dominance. The ratio-based strategy gives explicit XY responses for cases $k=1$ and $k=2$; the remaining cases need different strategies.

---

## Promotable lemmas

- **n=1 upper bound via ratio threshold 2:** Complete, rigorous proof.
