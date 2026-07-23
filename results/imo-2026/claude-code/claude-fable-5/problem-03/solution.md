# IMO Problem 3 — the stick-cutting and claiming game

*Solved and written 2026-07-16 (US Pacific) by Claude Fable 5. Solving session 01:14:24 → ≈01:46 (≈32 min wall clock, verification included); write-up pass 09:44 → 09:49. Full time log in the **Time log** section at the end and in `problem3_verification.md` §C.*

**Problem.** Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$. First Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ further points; all marked points are distinct. The stick is cut at every marked point. The players then alternately claim unclaimed pieces, with Liu Bang moving first, and each player seeks to maximize the total length of the pieces he claims. Determine the largest number $c$ that Liu Bang can guarantee, regardless of Xiang Yu's play.

## Answer

$$c \;=\; \frac{2^{n}}{2^{n+1}-1} \;=\; \frac{1}{2-2^{-n}}.$$

Throughout, write $s := \dfrac{1}{2^{n+1}-1}$, so that $c = \dfrac{1+s}{2}$. Call Liu Bang **A** and Xiang Yu **B**. Sanity values: $c(1)=\tfrac23$, $c(2)=\tfrac47$, $c(3)=\tfrac8{15}$, and $c \downarrow \tfrac12$ as $n \to \infty$.

---

## 1. The claiming phase has an exact value

For a finite multiset $Q = \{q_1 \ge q_2 \ge \dots \ge q_r\}$ of piece lengths, let
$$O(Q) = q_1 + q_3 + q_5 + \cdots, \qquad E(Q) = q_2 + q_4 + \cdots,$$
so $O(Q) + E(Q) = \Sigma(Q)$ (the total length).

**Lemma 1.** In the alternate-claiming game on $Q$ (first player moves first, both maximize their own total), the first player obtains exactly $O(Q)$ under optimal play: he has a strategy guaranteeing $\ge O(Q)$, and the second player has a strategy holding him to $\le O(Q)$.

*Proof.* This is a finite perfect-information constant-sum game, so backward induction defines the value $V(Q)$ of the player to move. We show $V(Q) = O(Q)$ by induction on $|Q|$; the base $V(\varnothing)=0$ is clear. If the mover takes $q_j$, the opponent then moves first in $Q\setminus q_j$ and obtains $V(Q\setminus q_j) = O(Q\setminus q_j)$ by induction, leaving the mover with the rest of $Q\setminus q_j$, i.e. with $E(Q \setminus q_j)$ in addition to $q_j$. Hence
$$V(Q) = \max_j\big[\,q_j + E(Q\setminus q_j)\,\big].$$
Sorting $Q\setminus q_j$: its $k$-th element is $q_k$ for $k<j$ and $q_{k+1}$ for $k\ge j$. Therefore
$$q_j + E(Q\setminus q_j) = q_j + \sum_{\substack{k \text{ even}\\ k\le j-1}} q_k + \sum_{\substack{k \text{ even}\\ k\ge j}} q_{k+1}.$$
For $j=1$ this equals $q_1 + q_3 + q_5 + \cdots = O(Q)$. For $j\ge 2$, compare with $O(Q)$ term by term: each $q_k$ (even $k \le j-1$) is $\le q_{k-1}$, an odd-indexed term with index $k-1 \le j-2$; each $q_{k+1}$ (even $k\ge j$) is itself an odd-indexed term with index $\ge j+1$; distinct terms are matched to distinct odd indices, and the one remaining unmatched odd index $\le j$ (namely $j$ if $j$ is odd, $j-1$ if $j$ is even) satisfies $q_j \le q_{\text{that index}}$. Hence $q_j + E(Q\setminus q_j) \le O(Q)$, with equality at $j=1$, and $V(Q) = O(Q)$. $\blacksquare$

So the whole game reduces to: **A places $\le n$ marks to maximize $O(Q)$ of the final multiset of pieces; B then places $\le n$ marks to minimize it.**

**Lemma 2.** If $Q$ admits pairwise disjoint pairs $\{x_1,y_1\},\dots,\{x_k,y_k\}$ of its elements, then $E(Q) \ge \sum_{t=1}^k \min(x_t,y_t)$.

*Proof.* Let $m_1 \ge m_2 \ge \cdots \ge m_k$ be the pair-minima in decreasing order. For each $t$, the pairs achieving $m_1,\dots,m_t$ contain $2t$ elements, all of length $\ge m_t$; hence $q_{2t} \ge m_t$. Since $2k \le r$, summing gives $E(Q) \ge \sum_{t\le k} q_{2t} \ge \sum_t m_t$. $\blacksquare$

---

## 2. Liu Bang can guarantee $c$ (lower bound)

**A's strategy:** mark the $n$ points $\sum_{i\le j} a_i$ for $j = 1,\dots,n$, where
$$a_i = 2^{\,n+1-i}\, s \qquad (i=1,\dots,n+1), \qquad \textstyle\sum_i a_i = (2^{n+1}-1)s = 1 .$$
So the pieces are the distinct powers $2^n s,\ 2^{n-1}s,\ \dots,\ 2s,\ s$ (the marks are interior and distinct).

Let B add any $p \le n$ further points. The final multiset $Q$ consists of $r = (n+1)+p \le 2n+1$ **parts**, each part lying inside exactly one of A's $n+1$ pieces. Fix a nonincreasing enumeration $q_1 \ge \dots \ge q_r$ and consider the *consecutive pairs* $\pi_t = \{q_{2t-1}, q_{2t}\}$ for $t = 1,\dots,k := \lfloor r/2\rfloor \le n$; by definition
$$E(Q) = \sum_{t=1}^{k} q_{2t}. \tag{2.1}$$

Build a multigraph $G$ on the vertex set $\{1,\dots,n+1\}$ (the pieces): for each $t$, an edge $e_t$ joining the two pieces containing the parts $q_{2t-1}$ and $q_{2t}$ (a loop if they coincide). Then $G$ has $n+1$ vertices and $k\le n$ edges, so **some connected component $C$ has fewer edges than vertices**; being connected it has at least, hence exactly, $|C|-1$ edges, so it is a tree (possibly a single vertex) — in particular it has no loops, cycles or parallel edges, and is properly $2$-colourable: $C = X \sqcup Y$ with every edge of $C$ joining $X$ to $Y$ (take $Y=\varnothing$ if $C$ is an isolated vertex).

*Pairs whose edge lies in $C$.* Each such pair has one part inside an $X$-piece and one inside a $Y$-piece. Distinct pairs use distinct parts, and the parts within one piece are disjoint sub-segments of it, so
$$\sum_{t:\,e_t \in C} q_{2t} \;\le\; \sum_{t:\,e_t\in C} \big(\text{length of } \pi_t\text{'s part lying in an } X\text{-piece}\big) \;\le\; \sum_{i \in X} a_i,$$
and symmetrically $\le \sum_{i\in Y} a_i$ (using $q_{2t} = \min \pi_t \le$ each of the two parts). Now $\sum_X a_i$ and $\sum_Y a_i$ are $s$ times sums of two **disjoint** sets of **distinct powers of $2$**, not both empty; by uniqueness of binary representation these two integers are unequal, so $\big|\sum_X a_i - \sum_Y a_i\big| \ge s$. Hence
$$\sum_{t:\,e_t \in C} q_{2t} \;\le\; \min\Big(\sum_{i\in X} a_i,\ \sum_{i\in Y} a_i\Big) \;\le\; \frac{\sum_{i\in C} a_i - s}{2}. \tag{2.2}$$

*All other pairs.* Both their parts lie in pieces outside $C$ (components are unions of pairs), and $q_{2t} \le \tfrac12(q_{2t-1}+q_{2t})$, so
$$\sum_{t:\,e_t\notin C} q_{2t} \;\le\; \tfrac{1}{2}\Big(1 - \sum_{i\in C} a_i\Big). \tag{2.3}$$

Adding (2.2) and (2.3) into (2.1): $E(Q) \le \frac{1-s}{2}$, hence
$$O(Q) = 1 - E(Q) \;\ge\; \frac{1+s}{2} = \frac{2^{n}}{2^{n+1}-1}.$$
By Lemma 1, A then claims at least this much in the claiming phase, whatever B does. $\blacksquare$

---

## 3. Xiang Yu can prevent more than $c$ (upper bound)

Now let A mark arbitrarily, creating pieces $b_1,\dots,b_{p+1}$ ($p \le n$ marks).

**Case 1: $p \le n-1$.** B marks the midpoint of every piece ($p+1 \le n$ marks, all interior, all distinct from A's marks). The parts form $p+1$ disjoint equal pairs $\{b_i/2,\, b_i/2\}$ of total length $1$, so by Lemma 2, $E(Q) \ge \tfrac12$, i.e. $O(Q) \le \tfrac12 < \tfrac{1+s}{2}$. By Lemma 1, A gets at most $\tfrac12 < c$.

**Case 2: $p = n$**, pieces $a_1,\dots,a_{n+1}$ (arbitrary positive lengths). The $2^{n+1}$ subset sums $\sigma(T) = \sum_{i\in T} a_i$, $T \subseteq \{1,\dots,n+1\}$, all lie in $[0,1]$, with $\sigma(\varnothing)=0$ and $\sigma(\text{full})=1$. Sorting them, the $2^{n+1}-1$ consecutive gaps sum to $1$, so some two **distinct** subsets $T \neq T'$ satisfy
$$0 \;\le\; \sigma(T) - \sigma(T') \;\le\; \frac{1}{2^{n+1}-1} = s .$$
Put $P := T\setminus T'$ and $N := T'\setminus T$. These are disjoint, $P \cup N \neq \varnothing$, and
$$d := \sum_{i\in P} a_i - \sum_{i \in N} a_i \;=\; \sigma(T)-\sigma(T') \;\in\; [0, s].$$
(Note $P \ne \varnothing$: otherwise $T \subsetneq T'$ would force $\sigma(T) < \sigma(T')$, since pieces have positive length. $N=\varnothing$ is possible and harmless below.)

**Lemma 3 (realization).** Let $W$ be a family of $w \ge 1$ pairwise disjoint segments, partitioned as $W = P \sqcup N$, and let $d = \big|\Sigma(P) - \Sigma(N)\big|$. Then one can place at most $w-1$ marks, all interior to segments of $W$ and pairwise distinct, so that the resulting parts of $W$ admit pairwise disjoint **equal pairs** (two parts of the same length) of total paired length $\Sigma(W) - d$.

*Proof.* Induction on $w$. If $P=\varnothing$ or $N=\varnothing$: place no marks and form no pairs; indeed then $d = \Sigma(W)$ and $\Sigma(W)-d = 0$. Otherwise pick any $x \in P$, $y\in N$, and w.l.o.g. $|x| \ge |y|$ (else swap the roles of $P$ and $N$; $d$ is unchanged).

- If $|x| = |y|$: take $\{x,y\}$ as an equal pair (no mark needed) and apply the induction hypothesis to $(P\setminus x,\, N\setminus y)$: same imbalance $d$ (both side-sums dropped by $|y|$), $w-2$ segments, at most $\max(w-3,0)$ further marks.
- If $|x| > |y|$: mark the interior point of $x$ at distance $|y|$ from its left endpoint, splitting $x = x' \sqcup x''$ with $|x'| = |y|$; take $\{x', y\}$ as an equal pair and apply the induction hypothesis to $\big((P\setminus x)\cup\{x''\},\, N \setminus y\big)$ — a family of $w-1$ pairwise disjoint segments with the same imbalance $d$ — using at most $w-2$ further marks; total at most $w-1$.

The invariant $|\Sigma(P)-\Sigma(N)| = d$ persists, and the recursion ends when one side is empty, leaving unpaired segments of total length exactly $d$; so the paired length is $\Sigma(W) - d$. All marks are strictly interior to positive-length segments that are pairwise disjoint at each stage, hence all marks are distinct and distinct from all previously placed marks and endpoints. $\blacksquare$

**B's strategy:** apply Lemma 3 to $W = P\cup N$ (as actual pieces of the stick), using $\le |W|-1$ marks, and mark the midpoint of every piece **not** in $W$, using $n+1-|W|$ marks. Total: at most $n$ marks, all interior to pieces (hence distinct from A's marks) and pairwise distinct. The equal pairs obtained (the Lemma 3 pairs plus the half–half pairs of the outside pieces) are pairwise disjoint parts of total length
$$\big(\Sigma(W) - d\big) + \big(1 - \Sigma(W)\big) \;=\; 1 - d \;\ge\; 1-s .$$
By Lemma 2 (each equal pair has minimum equal to half its total), $E(Q) \ge \frac{1-d}{2} \ge \frac{1-s}{2}$, hence
$$O(Q) \;\le\; \frac{1+s}{2} \;=\; \frac{2^{n}}{2^{n+1}-1},$$
and by Lemma 1, B (claiming second) holds A to at most this. $\blacksquare$

---

## Conclusion

Liu Bang can guarantee $\frac{2^n}{2^{n+1}-1}$ (Section 2, by cutting the stick into pieces proportional to $2^n, 2^{n-1}, \dots, 2, 1$), and Xiang Yu can prevent him from getting more (Section 3). Therefore
$$c \;=\; \frac{2^{n}}{2^{n+1}-1}.$$

## Remarks

By Lemma 1 the claiming phase is worth exactly the sorted odd-index sum, so B's goal is to make the parts "pair up" (large $E$), and Lemma 2 quantifies this via disjoint near-equal pairs. B's universal weapon is the pigeonhole on the $2^{n+1}$ subset sums, which always finds two subsets of A's pieces whose sums differ by at most $s$ — and Lemma 3 turns such a near-tie into a perfect pairing of everything except length $\le s$, using at most one cut per piece. Conversely, the powers-of-two partition is precisely the one whose subset sums are *maximally spread out*: any tree component of B's pairing graph exhibits two disjoint subsets of pieces whose sums must then differ by at least $s$, and B's budget ($\le n$ marks, hence at most $n$ consecutive pairs among the $\le 2n+1$ parts spread over $n+1$ pieces) forces such a tree component to exist. The two bounds meet exactly at $c=\frac{1+s}{2}$. Brute-force search (`problem3_verification.py`) confirms the value and the uniqueness of the geometric partition for $n \le 3$.

---

## Time log

All times US Pacific, 2026-07-16 (wall clock; measured from session and file timestamps — the full breakdown, including dead ends explored, is in `problem3_verification.md` §C):

| Phase | Interval | Duration |
|---|---|---|
| Deep-think solving: reduction of the claiming phase to the odd-index sum, pairing/packing reformulation, discovery of the subset-sum pigeonhole upper bound and the powers-of-2 / tree-component lower bound (dead ends included) | 01:14:24 → 01:39:05 | ≈ 25 min |
| Brute-force verification for $n = 1, 2, 3$ + skeptical re-derivation of every lemma | 01:39:05 → ≈ 01:46 | ≈ 7 min |
| **Solving turn total (solution found and verified)** | 01:14 → ≈ 01:46 | **≈ 32 min** |
| Write-up of this file, `problem3_verification.py`, and the verification report; final re-run of the suite (0.9 s) | 09:44 → 09:49 | ≈ 5 min |
| **Grand total** | — | **≈ 37 min** |
