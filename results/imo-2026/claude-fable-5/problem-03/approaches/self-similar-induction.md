# Approach: self-similar-induction

## Status
solved

## Approaches tried
- (round 1, outline) Skeleton opened. The k = 1 case of the lower-bound induction step was fully worked (threshold accounting at M = 2^{n−1}/D); the strip-pairs upper-bound induction was checked to be exactly calibrated. Gaps: L1 (k ≥ 2 lower bound), U1 (feasibility branch of strip-k).
- (round 1, review) Outline-reviewer found a REAL HOLE in the upper-bound exhaustion: at n = 3, q = (0.35, 0.245, 0.235, 0.17) the stated k-selection rule offers no move (threshold holds only for k = 2, 3, where feasibility q_1 ≥ q_2 + … + q_{k+1} fails), and the U1 fallback fails too; a 3-mark cascade nevertheless holds Liu Bang to 0.52. **Recorded: the prefix strip-k exhaustion "no usable k ⇒ Σq < 1" is FALSE as stated — do not retry it.**
- (round 1, build) **Both hard gaps eliminated by a change of mechanism.** The upper bound is rebuilt on a subset-sum pigeonhole (some nonzero signed combination x·q of the ORIGINAL pieces is ≤ S/(2^{m+1}−1)) plus a superposition realization lemma (any signed combination is realizable as "equal pairs + leftover of total |x·q|" with ≤ m marks). The lower bound is rebuilt on a home-graph tree argument: any refinement of the m+1 pieces by ≤ m cuts has defect Δ ≥ min nonzero |x·q|; at the geometric configuration this minimum is 1/D by uniqueness of binary representation. Both new lemmas verified numerically (3000+ random instances, m ≤ 6) before proving. The reviewer's counterexample is now handled: x = (0, +1, −1, 0) gives |x·q| = 0.01 ≤ 1/15, realized by halving q_1, q_4 and cutting a copy of q_3 out of q_2 (3 marks) — worked example included in the proof. The old self-similar induction (k = 0, 1 cases) is superseded and retained only in git history. **Outcome: complete proof, both bounds, no gaps.**

## Current best
Complete proof below of **c(n) = 2^n/(2^{n+1} − 1)**: lower bound via the geometric marking + home-graph tree lemma; upper bound via subset-sum pigeonhole + superposition realization. No open gaps.

## Full proof

**Answer.** For every positive integer n,
$$c(n) = \frac{2^n}{2^{n+1}-1}.$$
Throughout write $D = 2^{n+1}-1$ and $u = 1/D$.

We must prove two statements:

- **(Lower bound)** Liu Bang has a marking such that, whatever Xiang Yu does, Liu Bang's claiming total is at least $2^n/D$.
- **(Upper bound)** For every Liu Bang marking, Xiang Yu has a reply holding Liu Bang's total to at most $2^n/D$.

Together these say the largest guaranteeable value is exactly $2^n/D$.

### 0. Conventions

A *division point* of the stick $[0,1]$ is $0$, $1$, or a marked point. After all cuts, the *pieces* are the (positive-length) segments between consecutive division points. A mark at $0$ or $1$ creates no piece. (If one instead insists that such a mark creates a zero-length piece, Lemma C below is proved for multisets of *nonnegative* reals, and appending zero-length pieces changes neither player's optimal total, since zeros sort to the end and contribute $0$ to every position sum; so both interpretations give the same game value and we may ignore zero pieces.)

For a finite multiset $P = \{p_1 \ge p_2 \ge \dots \ge p_t\}$ of nonnegative reals (sorted, ties broken arbitrarily — all arguments below use only the inequalities $p_1 \ge p_2 \ge \cdots$), define
$$\mathrm{Odd}(P) = p_1 + p_3 + p_5 + \cdots, \qquad \mathrm{Even}(P) = p_2 + p_4 + \cdots, \qquad \Delta(P) = \mathrm{Odd}(P) - \mathrm{Even}(P).$$
Note $\mathrm{Odd}+\mathrm{Even} = \sum_i p_i$, so if the pieces sum to $1$ then $\mathrm{Odd}(P) = \tfrac{1}{2}\bigl(1 + \Delta(P)\bigr)$.

### 1. Lemma C (value of the claiming phase)

**Lemma C.** In the alternating claiming game on a finite multiset $P$ of nonnegative reals (players alternately claim one unclaimed element, the first player — Liu Bang — moves first, each maximizes his own total), the first player can guarantee a total of at least $\mathrm{Odd}(P)$, and the second player can guarantee at least $\mathrm{Even}(P)$. Since the two totals always sum to $\sum P$, under optimal play the first player's total is exactly $\mathrm{Odd}(P)$.

*Proof.* (Exchange induction — knowledge_base.md, Combinatorics: pigeonhole/extremal and exchange arguments.) We prove the two guarantees (i) first player $\ge \mathrm{Odd}(P)$ and (ii) second player $\ge \mathrm{Even}(P)$ simultaneously by strong induction on $t = |P|$.

*Base.* $t = 0$: both totals $0 = \mathrm{Odd} = \mathrm{Even}$. $t = 1$: first player takes $p_1 = \mathrm{Odd}(P)$; second player gets $0 = \mathrm{Even}(P)$.

*Step, claim (i).* The first player takes $p_1$ and thereafter follows the second-player strategy of IH(ii) on $Q = P \setminus \{p_1\}$. Sorted, $Q = (p_2, p_3, \dots, p_t)$, so $\mathrm{Even}(Q) = p_3 + p_5 + \cdots = \mathrm{Odd}(P) - p_1$. By IH(ii) he collects at least $\mathrm{Even}(Q)$ from the remainder, hence at least $p_1 + (\mathrm{Odd}(P) - p_1) = \mathrm{Odd}(P)$ in total.

*Step, claim (ii).* The second player's strategy: whenever it is his turn, take the largest remaining element. Suppose the first player just took $p_i$; the second player takes $p_j$ where $j = 2$ if $i = 1$ and $j = 1$ if $i \ge 2$. Let $P' = P \setminus \{p_i, p_j\}$ ($t-2$ elements). After these two moves it is again the first player's turn, so the second player is again the second player on $P'$; by IH(ii) he collects at least $\mathrm{Even}(P')$ from then on, hence at least $p_j + \mathrm{Even}(P')$ in total. It remains to check, for every $i$:
$$p_j + \mathrm{Even}(P') \;\ge\; \mathrm{Even}(P). \tag{$\ast$}$$

*Case $i = 1$ (so $j = 2$).* $P' = (p_3, p_4, \dots, p_t)$, so $\mathrm{Even}(P') = p_4 + p_6 + \cdots$ and the left side of $(\ast)$ is $p_2 + p_4 + p_6 + \cdots = \mathrm{Even}(P)$. Equality.

*Case $i \ge 2$ (so $j = 1$).* $P' = (p_2, \dots, p_{i-1}, p_{i+1}, \dots, p_t)$; the element $p_l$ sits at position $l-1$ for $2 \le l \le i-1$ and at position $l-2$ for $l \ge i+1$. Hence
$$\mathrm{Even}(P') = \sum_{\substack{3 \le l \le i-1 \\ l \text{ odd}}} p_l \;+\; \sum_{\substack{l \ge i+1 \\ l \text{ even}}} p_l ,$$
and, since $\mathrm{Even}(P) = \sum_{l \le i,\ l \text{ even}} p_l + \sum_{l \ge i+1,\ l \text{ even}} p_l$,
$$p_1 + \mathrm{Even}(P') - \mathrm{Even}(P) \;=\; p_1 + \sum_{\substack{3 \le l \le i-1\\ l \text{ odd}}} p_l \;-\; \sum_{\substack{l \le i \\ l \text{ even}}} p_l .$$
If $i$ is even this equals $(p_1 - p_2) + (p_3 - p_4) + \cdots + (p_{i-1} - p_i) \ge 0$; if $i$ is odd ($i \ge 3$) it equals $(p_1 - p_2) + (p_3 - p_4) + \cdots + (p_{i-2} - p_{i-1}) \ge 0$. In both cases $(\ast)$ holds. This proves (ii).

Finally, the totals of the two players sum to $\sum P = \mathrm{Odd}(P) + \mathrm{Even}(P)$; since each can guarantee his respective sum, under optimal play the first player gets exactly $\mathrm{Odd}(P)$. $\square$

By Lemma C, once the final piece multiset $P$ (of total $1$) is fixed, Liu Bang's total under optimal claiming is exactly $\mathrm{Odd}(P) = \tfrac12(1 + \Delta(P))$. So:

- the lower bound amounts to a marking of Liu Bang with $\Delta(P) \ge 1/D$ for all Xiang Yu replies;
- the upper bound amounts to, for each Liu Bang marking, a Xiang Yu reply with $\Delta(P) \le 1/D$
  (because $\tfrac12(1 + 1/D) = \tfrac{D+1}{2D} = \tfrac{2^{n+1}}{2D} = \tfrac{2^n}{D}$).

### 2. Lemma D (layer-cake identity) and its corollary

**Lemma D.** For a finite multiset $P$ of nonnegative reals let $N(x) = \#\{i : p_i > x\}$. Then
$$\Delta(P) = \bigl|\{x > 0 : N(x) \text{ is odd}\}\bigr| \;\ge\; 0,$$
where $|\cdot|$ is Lebesgue measure.

*Proof.* By the layer-cake formula $p_i = \int_0^\infty \mathbf{1}[p_i > x]\,dx$, so
$$\Delta(P) = \sum_i (-1)^{i+1} p_i = \int_0^\infty \sum_i (-1)^{i+1} \mathbf{1}[p_i > x]\, dx .$$
For fixed $x$, the set $\{i : p_i > x\}$ is exactly $\{1, 2, \dots, N(x)\}$ (the pieces are sorted decreasingly), so the integrand is $\sum_{i=1}^{N(x)} (-1)^{i+1}$, which is $1$ if $N(x)$ is odd and $0$ if even. $\square$

**Corollary D′ (pairs plus leftovers).** Suppose the multiset $P$ can be written as a disjoint union of equal pairs $\{v, v\}$ and a set $L$ of leftover elements. Then
$$0 \le \Delta(P) \le \sum_{\ell \in L} \ell .$$

*Proof.* $N(x) = 2\cdot\#\{\text{pairs of value} > x\} + N_L(x)$, so $N(x) \equiv N_L(x) \pmod 2$. Hence $\{x : N(x)\text{ odd}\} \subseteq \{x : N_L(x) \ge 1\} = (0, \max L)$, of measure $\max L \le \sum_{\ell \in L} \ell$ (and $= 0$ if $L = \emptyset$). Nonnegativity is Lemma D. $\square$

### 3. The key quantity $\delta(q)$

For a tuple $q = (q_1, \dots, q_k)$ of positive reals define
$$\delta(q) \;=\; \min\Bigl\{\,\bigl|\textstyle\sum_i x_i q_i\bigr| \;:\; x \in \{-1, 0, +1\}^k,\ x \ne 0 \Bigr\}.$$
Both bounds will be routed through $\delta$ of Liu Bang's piece vector: Xiang Yu can always force $\Delta \le |x\cdot q|$ for any admissible sign vector $x \ne 0$ (Lemma R), some such $x$ has $|x \cdot q| \le S/(2^k - 1)$ (Lemma P), and conversely no reply can force $\Delta$ below $\delta(q)$ (Lemma T).

### 4. Lemma R (realization of a signed combination)

**Lemma R.** Let $q_1, \dots, q_k$ be the pieces after Liu Bang's cuts (positive reals), and let $x \in \{-1,0,+1\}^k$, $x \ne 0$. Then Xiang Yu can place at most $k - 1$ marks — all at points distinct from each other and from all existing division points — so that the resulting piece multiset $P$ is a disjoint union of equal pairs and leftovers of total exactly $\bigl|\sum_i x_i q_i\bigr|$. Consequently, by Corollary D′,
$$\Delta(P) \;\le\; \Bigl|\sum_i x_i q_i\Bigr|.$$

*Proof.* Let $A = \{i : x_i = +1\}$, $B = \{i : x_i = -1\}$, $Z = \{i : x_i = 0\}$; after replacing $x$ by $-x$ if necessary (which changes nothing), assume $\Sigma_A := \sum_{i \in A} q_i \ \ge\ \Sigma_B := \sum_{i \in B} q_i$. Note $A \ne \emptyset$ (as $x \neq 0$ and $\Sigma_A \geq \Sigma_B$, if $A = \emptyset$ then $B$ consists of pieces of total $\le 0$, impossible for positive pieces unless $B = \emptyset$ too).

**(a) The $Z$-pieces.** Cut each piece $q_i$, $i \in Z$, at its midpoint: one mark per piece, $|Z|$ marks, each strictly interior, producing the equal pair $\{q_i/2, q_i/2\}$.

**(b) The $A$/$B$ superposition.** If $B = \emptyset$, make no further cuts: the $A$-pieces are the leftovers, of total $\Sigma_A = |x\cdot q|$, and the count of marks used is $|Z| \le k - 1$. Now assume $B \ne \emptyset$. Enumerate $A = \{a_1, \dots, a_r\}$ and $B = \{b_1, \dots, b_s\}$ in any order and form partial sums
$$\alpha_0 = 0,\ \alpha_i = q_{a_1} + \cdots + q_{a_i}\ (1 \le i \le r), \qquad \beta_0 = 0,\ \beta_j = q_{b_1} + \cdots + q_{b_j}\ (1 \le j \le s),$$
so $\alpha_r = \Sigma_A \ge \beta_s = \Sigma_B$. Conceptually, lay the $A$-pieces end to end along a tape $[0, \Sigma_A]$ (piece $a_i$ occupying $(\alpha_{i-1}, \alpha_i)$) and the $B$-pieces along $[0, \Sigma_B]$ (piece $b_j$ occupying $(\beta_{j-1}, \beta_j)$). Xiang Yu's cuts:

- in each physical piece $q_{a_i}$: at the points corresponding to those tape positions $\mu \in \{\beta_1, \dots, \beta_s\}$ with $\alpha_{i-1} < \mu < \alpha_i$ (i.e. at offset $\mu - \alpha_{i-1}$ from that piece's left end);
- in each physical piece $q_{b_j}$: at the points corresponding to those $\mu \in \{\alpha_1, \dots, \alpha_{r-1}\}$ with $\beta_{j-1} < \mu < \beta_j$.

Cut count: at most $s$ cuts of the first kind (one per element of $\{\beta_1,\dots,\beta_s\}$) and at most $r - 1$ of the second kind, so at most $r + s - 1$ cuts here and $|Z| + r + s - 1 = k - 1$ in total. All cuts are strictly interior to their pieces, hence distinct from all existing division points; within one piece the offsets are distinct (distinct tape positions), and cuts in different pieces are at different points of the stick — so the marks are pairwise distinct and legal. (If a tape position $\mu$ coincides with an $\alpha_i$ or $\beta_j$ boundary, it is simply not interior to any piece and no cut is made there; the count only drops.)

Resulting fragments. Let $T = \{\alpha_1, \dots, \alpha_{r-1}\} \cup \{\beta_1, \dots, \beta_s\}$ and consider the partition of $(0, \Sigma_A)$ by $T$. By construction the fragments of the $A$-pieces correspond exactly to the intervals of this partition, and the fragments of the $B$-pieces correspond exactly to the intervals of the partition of $(0, \Sigma_B)$ by $T$. Hence for each partition interval $I \subseteq (0, \Sigma_B)$ there is exactly one $A$-fragment and exactly one $B$-fragment of length $|I|$: match them into an equal pair. The remaining fragments are the $A$-fragments corresponding to partition intervals inside $(\Sigma_B, \Sigma_A)$; these are the leftovers, of total length $\Sigma_A - \Sigma_B = |x \cdot q| \ge 0$. (If $\Sigma_A = \Sigma_B$ there are no leftovers.) Together with the $|Z|$ equal pairs from (a), the final multiset is equal pairs plus leftovers of total $|x\cdot q|$, as claimed. Corollary D′ finishes. $\square$

### 5. Lemma P (subset-sum pigeonhole)

**Lemma P.** Let $q_1, \dots, q_k \ge 0$ with $\sum q_i = S$. Then there exists $x \in \{-1,0,+1\}^k$, $x \ne 0$, with
$$\Bigl|\sum_i x_i q_i\Bigr| \;\le\; \frac{S}{2^k - 1}.$$

*Proof.* (Pigeonhole principle — knowledge_base.md, Combinatorics.) The $2^k$ subset sums $\sigma(T) = \sum_{i \in T} q_i$, $T \subseteq \{1,\dots,k\}$, all lie in $[0, S]$. Partition $[0, S]$ into the $2^k - 1$ intervals $\bigl[(l-1)\tfrac{S}{2^k-1},\, l\tfrac{S}{2^k-1}\bigr)$ for $l = 1, \dots, 2^k - 2$, together with $\bigl[(2^k-2)\tfrac{S}{2^k-1},\, S\bigr]$. By pigeonhole, two distinct subsets $T \ne T'$ have $\sigma(T), \sigma(T')$ in the same interval, so $|\sigma(T) - \sigma(T')| \le S/(2^k - 1)$. Put $x = \mathbf{1}_T - \mathbf{1}_{T'} \in \{-1,0,1\}^k$; then $x \ne 0$ and $x \cdot q = \sigma(T) - \sigma(T')$. $\square$

### 6. Upper bound: Xiang Yu holds Liu Bang to at most $2^n/D$

**Theorem U.** For every marking by Liu Bang (at most $n$ points), Xiang Yu has a reply (at most $n$ points, distinct from Liu Bang's) after which Liu Bang's optimal claiming total is at most $2^n/D$.

*Proof.* Suppose Liu Bang's marks produce pieces $q_1, \dots, q_{m+1}$ ($m \le n$ interior marks; marks at $0$ or $1$ produce no pieces and only decrease $m$), positive with sum $1$.

*Case $m < n$.* Xiang Yu cuts every piece at its midpoint: $m + 1 \le n$ marks, all interior and distinct. The final multiset consists of $m+1$ equal pairs, so $\Delta = 0$ by Corollary D′ (no leftovers). By Lemma C, Liu Bang's total is $\tfrac12(1 + 0) = \tfrac12 < \tfrac{2^n}{D}$, since $2^n \cdot 2 = 2^{n+1} > D$.

*Case $m = n$.* Apply Lemma P to $q \in \mathbb{R}_{>0}^{n+1}$ with $S = 1$ and $k = n + 1$: there is a nonzero $x \in \{-1,0,1\}^{n+1}$ with $|x \cdot q| \le \frac{1}{2^{n+1}-1} = \frac1D$. By Lemma R, Xiang Yu realizes it with at most $(n+1) - 1 = n$ legal marks, forcing $\Delta(P) \le 1/D$. By Lemma C, Liu Bang's total is
$$\tfrac12\bigl(1 + \Delta(P)\bigr) \;\le\; \tfrac12\Bigl(1 + \tfrac1D\Bigr) \;=\; \tfrac{D+1}{2D} \;=\; \tfrac{2^{n+1}}{2D} \;=\; \tfrac{2^n}{D}. \qquad \square$$

*Worked example (the round-1 reviewer's counterexample to the old exhaustion).* $n = 3$, $q = (0.35, 0.245, 0.235, 0.17)$: take $x = (0, +1, -1, 0)$, $|x\cdot q| = 0.01 \le 1/15$. Realization: halve $q_1$ and $q_4$ (2 marks), and cut a fragment of length $0.235$ off $q_2$ (1 mark) — pieces $\{0.175, 0.175\}, \{0.235, 0.235\}, \{0.085, 0.085\}$, leftover $0.01$; $\Delta = 0.01$, Liu Bang gets $0.505 \le 8/15$. Three marks, as required.

### 7. Lemma T (no reply beats $\delta(q)$)

**Lemma T.** Let $q_1, \dots, q_k > 0$ be the pieces after Liu Bang's cuts, and let $P$ be the piece multiset after Xiang Yu adds at most $k - 1$ further (interior, distinct) marks. Then
$$\Delta(P) \;\ge\; \delta(q).$$

*Proof.* Say Xiang Yu made $c \le k-1$ cuts interior to pieces (marks at $0$/$1$ create nothing), so $P$ has $t = k + c \le 2k - 1$ pieces. Each piece of $P$ is a subinterval of exactly one original piece $q_i$; call $i$ its *home*. Since the cuts inside $q_i$ partition it, the fragments with home $i$ have lengths summing to exactly $q_i$.

Sort $P$ as $p_1 \ge p_2 \ge \cdots \ge p_t$ and pair consecutively: pairs $(p_{2\iota-1}, p_{2\iota})$ for $1 \le \iota \le \lfloor t/2 \rfloor$, with $p_t$ left unmatched if $t$ is odd. By definition of $\Delta$ as the alternating sum,
$$\Delta(P) \;=\; \sum_{\iota} \bigl(p_{2\iota-1} - p_{2\iota}\bigr) \;+\; \begin{cases} p_t & t \text{ odd}\\ 0 & t \text{ even}\end{cases},$$
where every summand is $\ge 0$.

Form the multigraph $G$ on the vertex set $\{1, \dots, k\}$ of homes with one edge per pair, joining the homes of its two fragments (a loop if they share a home). Then
$$\#E(G) \;=\; \lfloor t/2 \rfloor \;\le\; \Bigl\lfloor \tfrac{2k-1}{2} \Bigr\rfloor \;=\; k - 1 \;<\; k \;=\; \#V(G).$$
Since the number of edges summed over connected components is less than the number of vertices summed over components, some component $C$ satisfies $\#E(C) \le \#V(C) - 1$; being connected, $\#E(C) = \#V(C) - 1$ exactly. Moreover $C$ contains no loop and no pair of parallel edges: otherwise its underlying simple graph would have at most $\#V(C) - 2$ edges, too few to connect $\#V(C)$ vertices. So $C$ is a tree with all edges joining distinct homes.

Properly $2$-color $C$: choose $x_i \in \{+1, -1\}$ for $i \in V(C)$ with opposite signs on adjacent vertices (possible since a tree is bipartite), and set $x_i = 0$ for $i \notin V(C)$. Then $x \ne 0$. Compute, using $q_i = \sum_{\text{fragments } f \text{ with home } i} |f|$:
$$\sum_i x_i q_i \;=\; \sum_{\text{fragments } f} x_{\mathrm{home}(f)}\, |f| \;=\; \sum_{\text{pairs}} \bigl(x_{h_1} |f_1| + x_{h_2} |f_2|\bigr) \;+\; \bigl[t \text{ odd}\bigr]\, x_{\mathrm{home}(p_t)}\, p_t .$$
A pair whose edge lies outside $C$ has both homes outside $C$ (edges never join different components), contributing $0$. A pair whose edge lies in $C$ joins two distinct, oppositely colored homes, contributing $\pm(|f_1| - |f_2|)$, of absolute value equal to that pair's gap $p_{2\iota-1} - p_{2\iota}$. The unmatched piece (if any) contributes $0$ or $\pm p_t$. By the triangle inequality,
$$\Bigl|\sum_i x_i q_i\Bigr| \;\le\; \sum_\iota \bigl(p_{2\iota - 1} - p_{2\iota}\bigr) + \bigl[t \text{ odd}\bigr] p_t \;=\; \Delta(P).$$
Since $x \ne 0$, the left side is at least $\delta(q)$. $\square$

### 8. Lemma G ($\delta$ of the geometric configuration)

**Lemma G.** Let $g = (g_0, g_1, \dots, g_n)$ with $g_j = 2^j u$, $u = 1/D$. Then $\delta(g) = u$.

*Proof.* For nonzero $x \in \{-1,0,1\}^{n+1}$, $\sum_j x_j g_j = u \cdot \sum_j x_j 2^j$, and $\sum_j x_j 2^j$ is a nonzero integer: if it were $0$ with $x \ne 0$, let $j_0$ be the least index with $x_{j_0} \ne 0$; reducing $\sum_{j \ge j_0} x_j 2^j = 0$ modulo $2^{j_0 + 1}$ gives $x_{j_0} 2^{j_0} \equiv 0 \pmod{2^{j_0+1}}$, i.e. $x_{j_0}$ even — contradiction. Hence $|\sum_j x_j g_j| \ge u$ for all admissible $x$, and $x = (1, 0, \dots, 0)$ attains $u$. $\square$

### 9. Lower bound: Liu Bang guarantees $2^n/D$

**Theorem L.** Let Liu Bang mark the $n$ points $\tfrac{2^1 - 1}{D}, \tfrac{2^2-1}{D}, \dots, \tfrac{2^n - 1}{D}$ (distinct interior points), creating the pieces $g_j = 2^j/D$, $j = 0, 1, \dots, n$, of total $1$. Then for every reply of Xiang Yu (at most $n$ further distinct marks), Liu Bang's optimal claiming total is at least $2^n/D$.

*Proof.* Xiang Yu's reply adds at most $n = (n+1) - 1$ interior cuts to the $k = n + 1$ pieces $g = (g_0, \dots, g_n)$. By Lemma T and Lemma G, the final multiset $P$ satisfies $\Delta(P) \ge \delta(g) = 1/D$. By Lemma C, Liu Bang's total is
$$\tfrac12\bigl(1 + \Delta(P)\bigr) \;\ge\; \tfrac12\Bigl(1 + \tfrac1D\Bigr) \;=\; \tfrac{2^n}{D}. \qquad \square$$

### 10. Conclusion and verification

By Theorem L, Liu Bang can guarantee at least $2^n/D$; by Theorem U, he cannot guarantee more than $2^n/D$ (against every marking Xiang Yu has a reply capping him at $2^n/D$). Hence the largest value Liu Bang may guarantee is
$$\boxed{\,c(n) = \frac{2^n}{2^{n+1} - 1}\,}.$$

*Verification.* $n = 1$: $c = 2/3$. Liu Bang marks $1/3$ (pieces $1/3, 2/3$); e.g. Xiang Yu's mark $y \in (1/3, 1)$ gives pieces $\{1/3, y - 1/3, 1 - y\}$ whose two new pieces sum to $2/3$, so the median is exactly $1/3$ and Liu Bang collects $1 - 1/3 = 2/3$ — matching Theorem L; and against any single mark $x \le 1/3$, halving $1 - x$ holds Liu Bang to $(1+x)/2 \le 2/3$ — matching Theorem U. $n = 2$: $c = 4/7$; marks $\{1/7, 3/7\}$, pieces $(1/7, 2/7, 4/7)$; Xiang Yu's best reply (e.g. cut $4/7$ into $2/7, 1/7, 1/7$ with two marks) leaves sorted pieces $(2/7, 2/7, 1/7, 1/7, 1/7)$ with $\mathrm{Odd} = 2/7 + 1/7 + 1/7 = 4/7$ exactly. Equality in Theorem U is attained at the geometric configuration, where the subset sums $\{0, 1, 2, \dots, 2^{n+1}-1\}\cdot u$ are exactly equally spaced (the pigeonhole bound of Lemma P is tight), and equality in Theorem L is attained by the reply just described (leftover exactly $u$). $\blacksquare$

## Promotable lemmas

All proved in full in this file (section numbers refer to `## Full proof` above); each is self-contained and reusable by the sibling approaches:

- **Lemma C (claiming value = Odd)** — §1. In the alternating claiming game on a finite multiset of nonnegative reals, the first mover's optimal total is exactly $\mathrm{Odd}(P)$, the second mover's $\mathrm{Even}(P)$. Proved by simultaneous exchange induction (both one-sided guarantees).
- **Lemma D + Corollary D′ (layer-cake / pairs-plus-leftovers)** — §2. $\Delta(P) = |\{x : N(x)\ \text{odd}\}| \ge 0$; if $P$ = equal pairs $\sqcup$ leftovers $L$ then $\Delta(P) \le \sum L$.
- **Lemma R (realization)** — §4. For pieces $q_1,\dots,q_k$ and any nonzero $x \in \{-1,0,1\}^k$, the second marker can, with $\le k-1$ legal marks, reach a configuration of equal pairs plus leftovers of total $|x\cdot q|$, hence force $\Delta \le |x \cdot q|$. (Midpoint halvings for $x_i = 0$ + superposition matching of the $+$ pieces against the $-$ pieces.)
- **Lemma P (subset-sum pigeonhole)** — §5. $k$ nonnegative reals of sum $S$ admit a nonzero $\{-1,0,1\}$-combination of absolute value $\le S/(2^k - 1)$.
- **Lemma T (tree lower bound)** — §7. Any refinement of $k$ pieces $q$ by $\le k-1$ cuts has $\Delta \ge \delta(q) = \min_{x \ne 0} |x \cdot q|$. (Consecutive pairing, home multigraph with $\le k-1$ edges on $k$ vertices, a loopless tree component, proper 2-coloring.)
- **Lemma G (dyadic dissociation)** — §8. $\delta(u, 2u, \dots, 2^n u) = u$ by uniqueness of binary representation.
