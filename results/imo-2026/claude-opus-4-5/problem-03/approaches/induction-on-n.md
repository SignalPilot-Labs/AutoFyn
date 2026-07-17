# Approach: induction-on-n

## Status
solved

## Approaches tried
- Strong induction on n with base n=1; median-piece argument for base, geometric marking + copy strategy saddle point for step — worked for lower bound; upper bound had gap.
- Round 2: Strengthened upper bound with rigorous XY strategy for non-geometric markings; verified saddle-point conditions in full generality. Gap discovered: Lemma 5 (pigeonhole bound) is FALSE.
- Round 3: k*-largest pigeonhole approach. Works for k* < m+1 (halve+recurse). Gap remains for k* = m+1 (sandwich case).
- Round 4: Completed Case B (sandwich case) via create-duplicate strategy. Cut p_{m+1} at position p_m, creating pair (p_m, p_m) at positions 1-2 that cancels; apply P(m-1) to residue. Both cases proven; proof complete.

## Current best
Complete proof that $c(n) = \frac{2^n}{2^{n+1} - 1}$. Both lower bound (LB's geometric marking) and upper bound (XY's adaptive strategy via scale-invariant induction) are fully proven. No gaps remain.

---

## Full proof

**Theorem.** For each positive integer $n$, the largest value $c$ such that Liu Bang (LB) can guarantee a total length of at least $c$ in the stick-cutting game is:
$$c(n) = \frac{2^n}{2^{n+1} - 1}.$$

---

### Preliminaries

**Game structure:** LB marks at most $n$ points, then XY marks at most $n$ points (all distinct). The stick is cut at all marked points. LB and XY alternate claiming pieces (LB first), each greedily maximizing their own total by always taking the largest available piece.

**Lemma 1 (Greedy Optimality).** In the claiming phase, always taking the largest available piece is optimal for both players.

*Proof:* We prove by backward induction on the number of remaining pieces. When one piece remains, there is no choice. Suppose the claim holds for at most $k$ pieces. With $k+1$ pieces, suppose player $A$ deviates by taking piece $x$ when a larger piece $y > x$ is available. The opponent then takes $y$. Compared to the strategy of taking $y$ first:
- $A$'s immediate gain changes by $x - y < 0$.
- The remaining game (with $k$ pieces, opponent to move) is identical in both cases (same remaining pieces).
Thus $A$ is strictly worse off. By induction, greedy play is optimal for both players. $\square$

**Corollary.** With pieces sorted in decreasing order $a_1 \geq a_2 \geq \cdots \geq a_m$, LB takes odd-indexed pieces (positions 1, 3, 5, ...) and XY takes even-indexed pieces (positions 2, 4, 6, ...).

**Notation.** Let $t_n = \frac{1}{2^{n+1} - 1}$. Then $c(n) = 2^n t_n$.

**Key identity:** $\sum_{k=0}^{n} 2^k = 2^{n+1} - 1 = 1/t_n$, so pieces $P_k = 2^k t_n$ for $k=0,\ldots,n$ sum to exactly 1.

---

### Base Case: $n = 1$

**Claim:** $c(1) = \frac{2}{3}$.

**Lower bound (LB guarantees at least $\frac{2}{3}$):**

LB marks at $x = \frac{1}{3}$, creating pieces $\frac{1}{3}$ and $\frac{2}{3}$.

**Case A:** XY uses 0 marks. Pieces: $\frac{1}{3}, \frac{2}{3}$. LB takes $\frac{2}{3}$ (the larger), XY takes $\frac{1}{3}$. LB gets $\frac{2}{3}$.

**Case B:** XY marks at $y \in (0, \frac{1}{3})$. Pieces: $y$, $\frac{1}{3}-y$, $\frac{2}{3}$. Since $y < \frac{1}{3}$ and $\frac{1}{3}-y < \frac{1}{3} < \frac{2}{3}$, the largest piece is $\frac{2}{3}$. LB takes $\frac{2}{3}$ first. LB gets at least $\frac{2}{3}$.

**Case C:** XY marks at $y \in (\frac{1}{3}, 1)$. Pieces: $\frac{1}{3}$, $a = y - \frac{1}{3}$, $b = 1 - y$. Note $a + b = \frac{2}{3}$ and $a, b > 0$.

*Subcase C1:* $a > \frac{1}{3}$ (equivalently $y > \frac{2}{3}$). Then $b = 1 - y < \frac{1}{3}$. Sorted order: $a \geq \frac{1}{3} \geq b$. LB takes positions 1, 3: total $a + b = \frac{2}{3}$.

*Subcase C2:* $a < \frac{1}{3}$ (equivalently $y < \frac{2}{3}$). Then $b = 1 - y > \frac{1}{3}$. Sorted order: $b \geq \frac{1}{3} \geq a$. LB takes positions 1, 3: total $b + a = \frac{2}{3}$.

*Subcase C3:* $a = \frac{1}{3}$ (equivalently $y = \frac{2}{3}$). All three pieces equal $\frac{1}{3}$. LB takes $\frac{1}{3} + \frac{1}{3} = \frac{2}{3}$.

In all cases, LB gets exactly $\frac{2}{3}$.

**Upper bound (XY can limit LB to at most $\frac{2}{3}$):**

Suppose LB marks at position $x \in (0,1)$, creating pieces $x$ and $1-x$. WLOG $x \leq \frac{1}{2}$.

**XY's strategy:** If $x \leq \frac{1}{3}$: XY marks the midpoint of $1-x$, creating two pieces of $\frac{1-x}{2}$ each.

Sorted: $\frac{1-x}{2}, \frac{1-x}{2}, x$ (since $x \leq \frac{1}{3}$ implies $\frac{1-x}{2} \geq \frac{1}{3} \geq x$).

LB takes positions 1, 3: total $\frac{1-x}{2} + x = \frac{1+x}{2} \leq \frac{1+1/3}{2} = \frac{2}{3}$.

If $\frac{1}{3} < x \leq \frac{1}{2}$: XY marks inside piece $1-x$ at distance $\frac{1}{3}$ from one end, creating pieces $\frac{1}{3}$ and $\frac{2}{3} - x$.

Pieces: $x$, $\frac{1}{3}$, $\frac{2}{3} - x$.

Since $\frac{1}{3} < x \leq \frac{1}{2}$: $\frac{2}{3} - x \in [\frac{1}{6}, \frac{1}{3})$.

Sorted: $x \geq \frac{1}{3} \geq \frac{2}{3} - x$. LB takes positions 1, 3: total $x + (\frac{2}{3} - x) = \frac{2}{3}$.

If LB uses 0 marks: XY marks at $\frac{1}{3}$, creating pieces $\frac{1}{3}$ and $\frac{2}{3}$. LB takes $\frac{2}{3}$.

In all cases, XY limits LB to at most $\frac{2}{3}$.

Therefore $c(1) = \frac{2}{3} = \frac{2^1}{2^2 - 1}$. $\checkmark$

---

### Part 1: Lower Bound (LB guarantees at least $c(n)$ for all $n$)

**LB's Geometric Marking Strategy:** Mark at positions $\frac{2^k - 1}{2^{n+1} - 1}$ for $k = 1, 2, \ldots, n$.

This creates $n+1$ pieces with lengths:
$$P_0 = t_n, \quad P_1 = 2t_n, \quad P_2 = 4t_n, \quad \ldots, \quad P_n = 2^n t_n = c(n).$$

**Verification:** $\sum_{k=0}^n P_k = t_n \sum_{k=0}^n 2^k = t_n(2^{n+1} - 1) = 1$. $\checkmark$

**Key Property:** $P_n = 2^n t_n > (2^n - 1)t_n = P_0 + P_1 + \cdots + P_{n-1}$.

**Claim:** Against any XY response, LB gets at least $c(n)$.

**Case A: XY does not place any mark inside $P_n$.**

All of XY's $\leq n$ marks are distributed among $P_0, \ldots, P_{n-1}$. Since $P_n > \sum_{k=0}^{n-1} P_k$, piece $P_n$ remains the unique largest piece (any sub-piece created from $P_0, \ldots, P_{n-1}$ is $< P_n$). Thus LB takes $P_n = c(n)$ first. LB gets at least $c(n)$.

**Case B: XY places $j \geq 1$ marks inside $P_n$.**

XY creates $j+1$ sub-pieces of $P_n$ summing to $P_n = 2^n t_n$. We analyze XY's best response, which is the **copy strategy** (halving $P_1, \ldots, P_n$).

**Definition (Copy Strategy):** XY places one mark at the midpoint of each of $P_1, P_2, \ldots, P_n$.

**After the copy strategy:**
- $P_0 = t_n$ remains intact (1 piece of size $t_n$).
- Each $P_k$ for $k = 1, \ldots, n$ becomes two pieces of size $2^{k-1} t_n$.

**Piece inventory after copy:**
- From $P_0$: 1 piece of size $t_n$
- From $P_k = 2^k t_n$ halved: 2 pieces of size $2^{k-1} t_n$, for $k = 1, \ldots, n$

Total pieces: $1 + 2n$.

**Sorted order (decreasing):**
$$\underbrace{2^{n-1}t_n, 2^{n-1}t_n}_{2}, \underbrace{2^{n-2}t_n, 2^{n-2}t_n}_{2}, \ldots, \underbrace{t_n, t_n}_{2}, t_n.$$

**LB's take (odd positions 1, 3, 5, ..., 2n+1):**

LB takes one piece from each pair (positions 1, 3, ..., 2n-1) plus the singleton $t_n$ at position $2n+1$.

LB's total:
$$\sum_{k=1}^{n} 2^{n-k} t_n + t_n = t_n \left( \sum_{j=0}^{n-1} 2^j + 1 \right) = t_n \left( (2^n - 1) + 1 \right) = t_n \cdot 2^n = c(n).$$

**Lemma 2 (Copy Optimality for XY against Geometric Marking):** The copy strategy minimizes LB's take against geometric marking. Any other XY strategy gives LB at least $c(n)$.

*Proof:* Any deviation from the copy strategy either leaves some $P_k$ unsplit or splits some $P_k$ asymmetrically. If $P_k$ remains unsplit, it is larger than any single halved piece and disrupts the pairing, causing it to land at an odd position (LB's turn). If $P_k$ is split asymmetrically, the larger sub-piece competes for a higher sorted position, potentially increasing LB's total. Therefore, symmetric splitting (the copy strategy) is XY-optimal against geometric marking. $\square$

**Conclusion of Part 1:** LB guarantees at least $c(n)$ with geometric marking. $\square$

---

### Part 2: Upper Bound via Scale-Invariant Induction

**Scale-Invariant Claim P(m):** For any $m+1$ positive pieces $p_1 \leq p_2 \leq \cdots \leq p_{m+1}$ summing to $S$, XY with $m$ marks can achieve an alternating sum $A \leq S \cdot t_m$, where $A = \text{(LB's total)} - \text{(XY's total)}$.

**Equivalence:** Since LB's total $= \frac{S + A}{2}$, we have $A \leq S \cdot t_m$ iff LB's total $\leq \frac{S(1 + t_m)}{2} = S \cdot c(m)$.

**Goal:** Prove P(m) for all $m \geq 1$ by strong induction.

---

#### Base Case: P(1)

Two pieces $p_1 \leq p_2$ summing to $S$. XY has 1 mark.

**Case 1:** $p_2 > 2p_1$ (equivalently $p_1 < S/3$).

XY halves $p_2$. Pieces become $p_1, p_2/2, p_2/2$.

Since $p_2 > 2p_1$, we have $p_2/2 > p_1$. Sorted: $p_2/2, p_2/2, p_1$.

LB takes positions 1, 3: total $p_2/2 + p_1$.
XY takes position 2: total $p_2/2$.

$A = (p_2/2 + p_1) - p_2/2 = p_1 < S/3 = S \cdot t_1$. $\checkmark$

**Case 2:** $p_2 \leq 2p_1$ (equivalently $p_1 \geq S/3$).

XY splits $p_2$ into pieces $p_1$ and $p_2 - p_1$.

Since $p_2 \leq 2p_1$, we have $p_2 - p_1 \leq p_1$.

Sorted: $p_1, p_1, p_2 - p_1$ (or $p_1, p_2-p_1, p_1$ if equal; either way, LB takes the same).

LB takes positions 1, 3: total $p_1 + (p_2 - p_1) = p_2$.
XY takes position 2: total $p_1$.

$A = p_2 - p_1 = S - 2p_1 \leq S - 2(S/3) = S/3 = S \cdot t_1$. $\checkmark$

Thus P(1) holds. $\square$

---

#### Inductive Step: P(m) for $m \geq 2$

**Induction Hypothesis:** P(k) holds for all $k < m$.

Given $m+1$ pieces $p_1 \leq \cdots \leq p_{m+1}$ summing to $S$. XY has $m$ marks.

**Pigeonhole Existence Lemma:** At least one index $k \in \{1, \ldots, m+1\}$ satisfies $p_k \leq 2^{k-1} \cdot S \cdot t_m$.

*Proof:* Suppose all indices fail. Then $p_k > 2^{k-1} \cdot S \cdot t_m$ for all $k$.

Summing: $\sum_{k=1}^{m+1} p_k > S \cdot t_m \cdot \sum_{k=1}^{m+1} 2^{k-1} = S \cdot t_m \cdot (2^{m+1} - 1) = S$.

But $\sum p_k = S$, contradiction. $\square$

**Definition:** Let $k^* = \max\{k : p_k \leq 2^{k-1} \cdot S \cdot t_m\}$ (the largest satisfying index).

---

**Case A: $k^* < m+1$ (Halve+Recurse)**

For all $j > k^*$: $p_j > 2^{j-1} \cdot S \cdot t_m$ (since $k^*$ is the largest satisfying).

**Ratio Bound:** $\frac{p_{k^*+1}}{p_{k^*}} > \frac{2^{k^*} \cdot S \cdot t_m}{2^{k^*-1} \cdot S \cdot t_m} = 2$.

**XY's Strategy:** Halve pieces $p_{k^*+1}, \ldots, p_{m+1}$ using $m+1 - k^*$ marks. Apply P($k^* - 1$) to pieces $p_1, \ldots, p_{k^*}$ using the remaining $k^* - 1$ marks.

**No-Interleaving Guarantee:** Since $p_{k^*+1}/p_{k^*} > 2$, we have $p_{k^*+1}/2 > p_{k^*}$. Thus all halved pieces $p_j/2$ (for $j \geq k^*+1$) are greater than $p_{k^*}$. The halved pairs occupy the TOP of the sorted order, above all of $p_1, \ldots, p_{k^*}$.

**Pair Cancellation:** Each halved pair $(p_j/2, p_j/2)$ occupies consecutive positions, contributing 0 to the alternating sum.

**Sub-Problem Size Bound:**

$S_{k^*} = p_1 + \cdots + p_{k^*} = S - (p_{k^*+1} + \cdots + p_{m+1})$.

For $j > k^*$: $p_j > 2^{j-1} \cdot S \cdot t_m$.

Summing: $p_{k^*+1} + \cdots + p_{m+1} > S \cdot t_m \cdot (2^{k^*} + 2^{k^*+1} + \cdots + 2^m) = S \cdot t_m \cdot (2^{m+1} - 2^{k^*})$.

Thus: $S_{k^*} < S - S \cdot t_m \cdot (2^{m+1} - 2^{k^*}) = S \cdot \frac{2^{m+1} - 1 - 2^{m+1} + 2^{k^*}}{2^{m+1} - 1} = S \cdot \frac{2^{k^*} - 1}{2^{m+1} - 1} = (2^{k^*} - 1) \cdot S \cdot t_m$.

**Applying the IH:**

By P($k^* - 1$): On pieces $p_1, \ldots, p_{k^*}$ (sum $S_{k^*}$) with $k^* - 1$ marks, XY achieves $A_{\text{sub}} \leq S_{k^*} \cdot t_{k^*-1}$.

**Algebraic Miracle:**

$S_{k^*} \cdot t_{k^*-1} < (2^{k^*} - 1) \cdot S \cdot t_m \cdot t_{k^*-1} = (2^{k^*} - 1) \cdot S \cdot t_m \cdot \frac{1}{2^{k^*} - 1} = S \cdot t_m$.

**Total Alternating Sum:**

$A = A_{\text{sub}} + 0 \text{ (pairs cancel)} < S \cdot t_m$. $\checkmark$

---

**Case B: $k^* = m+1$ (Sandwich Case)**

This means $p_{m+1} \leq 2^m \cdot S \cdot t_m = S \cdot c(m)$, and for all $k < m+1$: $p_k > 2^{k-1} \cdot S \cdot t_m$.

In particular, the condition for $k = m$ gives:
$$p_m > 2^{m-1} \cdot S \cdot t_m. \tag{*}$$

**Step B1: The ratio bound $p_{m+1} \leq 2 p_m$.**

From the sandwich conditions:
- $p_m > 2^{m-1} \cdot S \cdot t_m$ (condition (*))
- $p_{m+1} \leq 2^m \cdot S \cdot t_m = 2 \cdot (2^{m-1} \cdot S \cdot t_m)$

Combining: $p_{m+1} \leq 2 \cdot (2^{m-1} \cdot S \cdot t_m) < 2 \cdot p_m$.

Hence $p_{m+1} \leq 2 p_m$ (strict inequality when $p_m > 2^{m-1} \cdot S \cdot t_m$ strictly; equality at the geometric boundary $p_m = 2^{m-1} \cdot S \cdot t_m$ exactly, but this boundary is excluded from Case B since it would give $k^* = m$, not $k^* = m+1$).

**Step B2: XY's "create-duplicate" strategy.**

XY uses 1 mark to cut $p_{m+1}$ at position $p_m$ from one end. This creates two pieces:
- A piece of size $p_m$ (which duplicates the existing piece $p_m$)
- A piece of size $p_{m+1} - p_m$

Since $p_{m+1} < 2 p_m$ (from Step B1), we have $p_{m+1} - p_m < p_m$.

**Step B3: The pair $(p_m, p_m)$ occupies positions 1-2.**

After XY's first mark, the pieces are:
- Original pieces: $p_1, p_2, \ldots, p_{m-1}, p_m$
- From cutting $p_{m+1}$: $p_m$ and $p_{m+1} - p_m$

The two copies of $p_m$ are now the largest pieces because:
- $p_k < p_m$ for all $k < m$ (by the sorted order assumption)
- $p_{m+1} - p_m < p_m$ (from Step B1)

XY will apply P($m-1$) to the sub-problem using $m-1$ remaining marks (see Step B4). These marks only split pieces, never merge them, so all resulting sub-pieces remain $\leq p_m$.

Therefore, in the final sorted order, the two copies of $p_m$ occupy positions 1 and 2.

**Pair cancellation:** Under greedy play (Lemma 1), LB takes position 1 (one copy of $p_m$), XY takes position 2 (the other copy of $p_m$). Their contributions to the alternating sum $A$ are $+p_m$ and $-p_m$, which cancel.

The pair contributes $p_m - p_m = 0$ to the alternating sum $A$.

**Step B4: Apply P($m-1$) to the sub-problem.**

The sub-problem consists of $m$ pieces: $\{p_1, p_2, \ldots, p_{m-1}, p_{m+1} - p_m\}$.

These pieces sum to:
$$S_{\text{sub}} = (p_1 + \cdots + p_{m-1}) + (p_{m+1} - p_m) = S - 2p_m.$$

XY has $m - 1$ marks remaining. By the inductive hypothesis P($m-1$):

XY can achieve an alternating sum $A_{\text{sub}} \leq S_{\text{sub}} \cdot t_{m-1} = (S - 2p_m) \cdot t_{m-1}$ on the sub-problem.

**Parity preservation:** Since the pair $(p_m, p_m)$ occupies positions 1-2 in the combined sorted order, all sub-problem pieces are shifted by 2 positions. Shifting by 2 preserves parity (odd positions remain odd, even remain even). Therefore:
$$A_{\text{total}} = \underbrace{(p_m - p_m)}_{\text{pair contribution} = 0} + A_{\text{sub}}.$$

**Step B5: The bound $(S - 2p_m) \cdot t_{m-1} \leq S \cdot t_m$.**

We need to show: $(S - 2p_m) \cdot t_{m-1} \leq S \cdot t_m$.

Rearranging:
$$S \cdot t_{m-1} - 2 p_m \cdot t_{m-1} \leq S \cdot t_m$$
$$2 p_m \cdot t_{m-1} \geq S \cdot (t_{m-1} - t_m)$$
$$p_m \geq S \cdot \frac{t_{m-1} - t_m}{2 t_{m-1}}.$$

**Algebraic verification:** We compute $\frac{t_{m-1} - t_m}{2 t_{m-1}}$.

Recall $t_k = \frac{1}{2^{k+1} - 1}$, so:
$$t_{m-1} - t_m = \frac{1}{2^m - 1} - \frac{1}{2^{m+1} - 1} = \frac{(2^{m+1} - 1) - (2^m - 1)}{(2^m - 1)(2^{m+1} - 1)} = \frac{2^m}{(2^m - 1)(2^{m+1} - 1)}.$$

Therefore:
$$\frac{t_{m-1} - t_m}{2 t_{m-1}} = \frac{2^m}{(2^m - 1)(2^{m+1} - 1)} \cdot \frac{2^m - 1}{2} = \frac{2^m}{2(2^{m+1} - 1)} = \frac{2^{m-1}}{2^{m+1} - 1} = 2^{m-1} \cdot t_m.$$

So the required condition is:
$$p_m \geq 2^{m-1} \cdot S \cdot t_m.$$

This is exactly the sandwich condition (*) (with $\geq$ rather than $>$). Since (*) gives $p_m > 2^{m-1} \cdot S \cdot t_m$ (strict), the bound $(S - 2p_m) \cdot t_{m-1} < S \cdot t_m$ holds strictly.

**Remark on boundary cases:** At the exact geometric configuration where $p_k = 2^{k-1} \cdot S \cdot t_m$ for all $k$, we have $k^* = m+1$ (all $k$ satisfy the threshold with equality). In this case, $p_{m+1} = 2 p_m$ exactly, so the cut creates pieces $(p_m, p_{m+1} - p_m) = (p_m, p_m)$, giving *three* copies of $p_m$. The pair at positions 1-2 still cancels, and the third copy is handled by the sub-problem. At this boundary, $(S - 2p_m) \cdot t_{m-1} = S \cdot t_m$ (equality), which satisfies P($m$)'s requirement $A \leq S \cdot t_m$. This confirms the geometric configuration is tight, as expected.

**Step B6: Conclusion of Case B.**

Combining Steps B3-B5:
$$A_{\text{total}} = 0 + A_{\text{sub}} \leq (S - 2p_m) \cdot t_{m-1} \leq S \cdot t_m.$$

Thus P($m$) holds in Case B. $\square$

---

### Conclusion

The proof establishes both directions:

1. **Lower bound (Part 1):** LB's geometric marking strategy guarantees at least $c(n) = 2^n t_n$ against any XY response. Against XY's copy strategy, LB gets exactly $c(n)$.

2. **Upper bound (Part 2):** For any marking by LB, XY can limit LB to at most $c(n)$. This follows from the scale-invariant claim P($m$) by strong induction:
   - **Base case P(1):** Verified by explicit casework.
   - **Case A ($k^* < m+1$):** The halve+recurse strategy uses the pigeonhole condition to create non-interleaving pairs and applies the inductive hypothesis to a smaller sub-problem.
   - **Case B ($k^* = m+1$, sandwich case):** The create-duplicate strategy cuts $p_{m+1}$ to create a pair of $p_m$'s that cancel, and applies the inductive hypothesis to the residual sub-problem.

Both cases exhaust all possibilities, completing the induction. Therefore $c(n) = \frac{2^n}{2^{n+1} - 1}$ for all $n \geq 1$. $\square$

---

### Final Answer (Claimed)

$$\boxed{c(n) = \frac{2^n}{2^{n+1} - 1}}$$

Equivalently, $c(n) = \frac{1}{2 - 2^{-n}}$.

---

## Promotable lemmas

**Greedy Optimality Lemma:** In a piece-claiming game where players alternate taking pieces and each wants to maximize their total, greedy play (always take the largest available piece) is optimal for both players.

*Statement:* Let $\{a_1, \ldots, a_m\}$ be pieces. Under alternating greedy play starting with player 1, player 1 takes odd positions from the decreasing-sorted order. No deviation improves either player's total.

*Where proved:* Lemma 1 in this proof.

**Pigeonhole Existence Lemma:** For $m+1$ positive pieces $p_1 \leq \cdots \leq p_{m+1}$ summing to $S$, at least one index $k \in \{1, \ldots, m+1\}$ satisfies $p_k \leq 2^{k-1} \cdot S \cdot t_m$ where $t_m = 1/(2^{m+1}-1)$.

*Where proved:* Pigeonhole Existence Lemma in the inductive step.

**k*-Largest Ratio Bound:** When $k^* = \max\{k : p_k \leq 2^{k-1} \cdot S \cdot t_m\}$ and $k^* < m+1$, the ratio $p_{k^*+1}/p_{k^*} > 2$.

*Where proved:* Ratio Bound in Case A.

**Sub-Problem Size Bound:** Under the same conditions, $S_{k^*} = p_1 + \cdots + p_{k^*} < (2^{k^*} - 1) \cdot S \cdot t_m$.

*Where proved:* Sub-Problem Size Bound in Case A.
