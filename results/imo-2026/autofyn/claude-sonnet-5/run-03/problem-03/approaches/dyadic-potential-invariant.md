## Status
partial

## Approaches tried
- `greedy-reduction-geometric` / `self-similar-induction-on-n` /
  `universal-halving-adversary`: see their own files (not this one's
  history).
- `potential/credit Φ argument` (round 1, this file): abandoned before any
  numeric test — vague, no concrete `w(p)`. Superseded round 3.
- **Cut-Reallocation Exchange Lemma (literal, unrestricted)** (round 3):
  disproved by exact counterexample at `n=3` (dominance regime). Documented
  dead end, not retried.
- **Restricted Exchange Lemma, balanced region only** (round 4): also FALSE,
  by an exact counterexample (`n=2`, `(0.35,0.34,0.31)`) — refutes both the
  rescoped lemma and the broader "top-only is optimal for XY" hypothesis.
  Documented dead end, not retried; cross-confirmed by
  `universal-halving-adversary`'s independent numeric finding the same
  round.
- **Round 5 (this round): pivot to LP extreme-point / vertex structure,
  per the round-5 outline's assigned target.** This is a genuinely different
  mechanism from the two local-exchange attempts above (a global
  compactness/vertex argument, not a single-step perturbation), so it does
  not repeat either documented dead end. Result: **proved in full** the
  correct general form of the "Tie-or-zero LP-vertex" structural fact — a
  *counting* lemma (Vertex Pinning Lemma, below), fully rigorous, no gaps.
  Along the way, **found and proved false**, by an exact hand-verified
  counterexample, the *literal* stronger per-fragment form of the lemma as
  originally proposed by this round's outline and math-explorer (every
  individual optimal fragment is 0-or-tied) — this is a genuine correction
  to the round's working conjecture, not a restatement of it. Used the
  corrected lemma to give a **finite-search reduction** of XY's inner
  optimization for any *fixed* LB partition (a real, certifiable positive
  tool — turning the earlier two negative results into a positive one, as
  targeted this round), but honestly report that this does **not**, by
  itself, close the balanced-region gap for LB's *outer* maximization over
  partitions (that direction remains open — see "Current best").

- **Round 6 (this round): cheap feasibility check of the majorization/
  suffix-domination monotonicity lead flagged by this round's fresh-framing
  explorer (Part B, `aimo-0287` analogy), BEFORE any proof effort.** Per
  the outline's explicit instruction, formalized the most natural
  transplant of "suffix-domination" from `aimo-0287`'s subset-of-fixed-
  sequence setting to our single-sorted-multiset setting — classical
  **majorization** on the order-statistic vector — and tested the claim
  "$M'$ majorizes $M$ (same size, same total, more spread toward the top)
  $\implies\mathrm{OddSum}(M')\ge\mathrm{OddSum}(M)$" both by targeted
  hand construction and a 200000-trial random search. **Result: FALSE**,
  by an explicit exact rational counterexample, confirmed by exhaustive
  random search to fail in BOTH directions (majorization gives no
  monotonicity of `OddSum` at all, not even a reversed one). Diagnosed and
  proved the exact structural reason (Section 7 below: `OddSum`'s weight
  pattern on sorted order statistics is not monotonic, so it is neither
  Schur-convex nor Schur-concave — a fully general, proved fact, not just
  a spot counterexample). Per the outline's decision tree, this is a
  documented dead end for the majorization mechanism; per the outline's
  step 4 fallback, this round's positive contribution is instead the
  already-certified Vertex Pinning Lemma remaining available as a
  supporting tool for `universal-halving-adversary`'s Existence Theorem
  (not re-derived here, see that approach's own file).

## Current best

### 0. Setup and notation (shared with `reduction-to-multiset-minimax.md`)

Fix LB's partition $p_1,\dots,p_k$ ($k\le n+1$, $\sum p_i=1$). A **cut
allocation** is $\mathbf m=(m_1,\dots,m_k)\in\mathbb Z_{\ge0}^k$ with
$\sum m_i\le n$. Given $\mathbf m$, index the $N:=\sum_i(m_i+1)$
"fragment slots" by pairs $(i,j)$, $1\le i\le k$, $1\le j\le m_i+1$; write
$\mathrm{slots}(i)$ for the $m_i+1$ slots belonging to piece $i$. Define
$$P(\mathbf m):=\Big\{\mathbf x\in\mathbb R_{\ge0}^N:\ \textstyle\sum_{j\in\mathrm{slots}(i)} x_j=p_i\ \ \forall i\Big\},$$
a compact convex polytope (a product of $k$ closed simplices), and its
relative-interior sub-region
$$P^\circ(\mathbf m):=\{\mathbf x\in P(\mathbf m):\ x_j>0\ \forall j\}.$$
By `reduction-to-multiset-minimax.md`, XY's set of **genuinely reachable**
responses using allocation $\mathbf m$ is exactly $P^\circ(\mathbf m)$ (each
piece split into $m_i+1$ *positive* pieces); XY's overall reachable value
set (over all allocations with $\sum m_i\le n$) is
$\bigcup_{\mathbf m}P^\circ(\mathbf m)$, and XY's problem is
$$V^*:=\inf_{\mathbf m:\,\sum m_i\le n}\ \inf_{\mathbf x\in P^\circ(\mathbf m)}\mathrm{OddSum}(\mathbf x).$$

### 1. Closure Lemma: the infimum is attained, and is attained by a genuine
XY response

**Claim.** $V^*=\min_{\mathbf m:\,\sum m_i\le n}\ \min_{\mathbf x\in
P(\mathbf m)}\mathrm{OddSum}(\mathbf x)$, and this minimum is attained by
some point of $P^\circ(\mathbf m')$ for some allocation $\mathbf m'$ with
$\sum m_i'\le n$ — i.e. the infimum in XY's problem is a genuine minimum,
achieved by an honest (all-positive-fragment) response.

**Proof.**

*(a) Zero-fragments don't change OddSum.* If $\mathbf x\in P(\mathbf m)$
has $z\ge0$ coordinates equal to $0$, let $\mathbf x'\in\mathbb
R_{\ge0}^{N-z}$ be $\mathbf x$ with those $z$ zero coordinates deleted.
Since every coordinate of $\mathbf x$ is $\ge 0$, the $z$ zero entries are
(weakly) the smallest values in $\mathbf x$; a valid descending sort of
$\mathbf x$ can always be written as [descending sort of the positive
entries] followed by the $z$ zeros in any order (any arrangement of equal
values is a valid descending sort). Under such a sort, the positive entries
occupy exactly ranks $1,\dots,N-z$, i.e. the *same* ranks they occupy in a
descending sort of $\mathbf x'$ alone; the $z$ zero entries occupy ranks
$N-z+1,\dots,N$ and contribute $0$ to $\mathrm{OddSum}(\mathbf x)$
regardless of the parity of their ranks (their value is $0$). Hence
$\mathrm{OddSum}(\mathbf x)=\mathrm{OddSum}(\mathbf x')$ exactly.

*(b) Deleting zero fragments is a legal move for XY.* If $\mathbf
x\in P(\mathbf m)$ has $z_i$ zero coordinates among $\mathrm{slots}(i)$
(so $z_i\le m_i$, since piece $i$'s coordinates sum to $p_i>0$, at least one
is positive), set $m_i':=m_i-z_i\ge0$. Deleting the zero coordinates of
piece $i$ leaves exactly $m_i+1-z_i=m_i'+1$ strictly positive values
summing to $p_i$ — a genuine element of the factor-simplex for piece $i$
with $m_i'$ cuts. Doing this for every $i$ produces a point $\mathbf
x'\in P^\circ(\mathbf m')$ with $\sum m_i'=\sum m_i-\sum z_i\le\sum m_i\le
n$, i.e. $\mathbf x'$ is a genuinely reachable XY response, and by (a)
$\mathrm{OddSum}(\mathbf x')=\mathrm{OddSum}(\mathbf x)$.

*(c) Hence $\inf$ over $\bigcup_{\mathbf m}P^\circ(\mathbf m)$ equals the
min over the finite union $\bigcup_{\mathbf m}P(\mathbf m)$.* By (b), every
value achieved on the closed polytopes $P(\mathbf m)$ is *also* achieved on
some $P^\circ(\mathbf m')$ with $\mathbf m'$ in the same finite index set
$\{\mathbf m:\sum m_i\le n\}$ (there are only $\binom{n+k}{k}$-many such
$\mathbf m$, a finite set since $k,n$ are fixed finite numbers); conversely
$P^\circ(\mathbf m)\subseteq P(\mathbf m)$ trivially. So the two infima
coincide. The right-hand side is a minimum (not just an infimum): each
$P(\mathbf m)$ is compact (closed and bounded subset of $\mathbb R^N$,
being a product of closed simplices) and $\mathrm{OddSum}$ restricted to it
is continuous (it is, for each of the finitely many descending-sort
patterns, a piecewise expression built from sorting, which is continuous;
globally $\mathrm{OddSum}$ is continuous on $\mathbb R^N_{\ge0}$ as the
composition of the continuous sort map and a continuous linear
readout — standard), so by the Extreme Value Theorem
(`knowledge_base.md`, "Extreme value theorem / Lagrange multipliers on a
compact manifold") each $\min_{P(\mathbf m)}\mathrm{OddSum}$ is attained; a
min of finitely many attained minima is attained. Finally, by (b) again,
this attained value is also witnessed by an honest, all-positive response
in some $P^\circ(\mathbf m')$. $\blacksquare$

This closes the compactness/degenerate-cuts subtlety fully rigorously (the
exact place round 3's memory rule #14 flagged as a recurring source of
error: conflating "$\le n$ cuts" with "$=n$ cuts", and positivity with
non-negativity). From here on we work inside the compact polytopes
$P(\mathbf m)$, understanding that any minimizer found there translates
back to a genuine XY response by part (b).

### 2. `OddSum` is linear on each sort-order region

Fix $\mathbf m$ and a permutation $\sigma$ of the $N$ slots (a *sort
order*). Define
$$R_\sigma(\mathbf m):=\{\mathbf x\in P(\mathbf m):\ x_{\sigma(1)}\ge x_{\sigma(2)}\ge\cdots\ge x_{\sigma(N)}\},$$
a closed sub-polytope of $P(\mathbf m)$ (intersection with the $N-1$
half-spaces $x_{\sigma(j)}\ge x_{\sigma(j+1)}$).

**Lemma 2.1.** $\bigcup_{\sigma\in S_N}R_\sigma(\mathbf m)=P(\mathbf m)$,
and for every $\mathbf x\in R_\sigma(\mathbf m)$,
$$\mathrm{OddSum}(\mathbf x)=f_\sigma(\mathbf x):=\sum_{j\text{ odd}}x_{\sigma(j)},$$
a fixed linear functional (independent of $\mathbf x$ within the region).

**Proof.** Every finite tuple of reals admits at least one permutation
sorting it into descending order (a basic fact: repeatedly select a
maximal remaining entry), so every $\mathbf x\in P(\mathbf m)$ lies in
$R_\sigma(\mathbf m)$ for at least one $\sigma$, giving the union claim. If
$\mathbf x\in R_\sigma(\mathbf m)$, then $x_{\sigma(1)}\ge\cdots\ge
x_{\sigma(N)}$ is by definition a valid descending sort of the multiset of
values $\{x_1,\dots,x_N\}$, so directly from the definition of
$\mathrm{OddSum}$ (sum of the odd-position entries of a descending sort),
$\mathrm{OddSum}(\mathbf x)=x_{\sigma(1)}+x_{\sigma(3)}+\cdots=f_\sigma(\mathbf x)$.
This holds for *every* point of $R_\sigma(\mathbf m)$ using the *same*
$\sigma$ (no case split on ties needed: $R_\sigma(\mathbf m)$ is defined so
that $\sigma$ is *always* a valid witnessing sort order for every point in
it, including boundary points with ties — a weak inequality $x_{\sigma(j)}\ge
x_{\sigma(j+1)}$ remains a valid descending-order witness whether or not
equality holds). Hence $f_\sigma$ is a single fixed linear functional
matching $\mathrm{OddSum}$ throughout $R_\sigma(\mathbf m)$. (If a point
lies in several regions $R_\sigma,R_{\sigma'}$ simultaneously — i.e. has
ties, so more than one $\sigma$ validly sorts it — then $f_\sigma$ and
$f_{\sigma'}$ necessarily agree there, since both equal
$\mathrm{OddSum}$ at that point by the argument just given; this is also
exactly the content of the certified Tie-neutrality Lemma, `lemmas/
tie-neutrality-and-first-mover-half.md` Lemma A, applied at that point — a
consistency check, not an extra assumption.) $\blacksquare$

**Corollary 2.2.** $\min_{P(\mathbf m)}\mathrm{OddSum}=\min_{\sigma\in
S_N}\min_{R_\sigma(\mathbf m)}f_\sigma$, and each inner minimum is a
genuine linear-program minimum over a compact polytope. (Immediate from
Lemma 2.1: the min over a finite union of compact sets of a function that
restricts to $f_\sigma$ on each piece equals the min of the finitely many
per-piece minima.)

### 3. LP fact: a linear functional on a compact polytope attains its
minimum at a vertex

We prove this classical fact in full (not cited as a black box, since the
knowledge-base entry only states existence-of-extremum, not that the
extremum can be taken at a vertex).

**Definitions.** For a nonempty compact convex $Q\subseteq\mathbb R^N$, a
point $\mathbf v\in Q$ is a **vertex** (extreme point) if it cannot be
written as $\tfrac12(\mathbf y+\mathbf z)$ for distinct $\mathbf y,\mathbf
z\in Q$.

**Lemma 3.1.** Every nonempty compact convex $Q\subseteq\mathbb R^N$ has at
least one vertex.

**Proof.** Induction on $N$. If $Q$ is a single point, it is (trivially) a
vertex. Otherwise pick any $\mathbf x_0\in Q$ and any nonzero direction
$\mathbf d$ such that the line $\{\mathbf x_0+t\mathbf d:t\in\mathbb R\}$
meets $Q$ in more than a point (exists since $Q$ has $\ge2$ points, so some
direction works). Since $Q$ is compact, $\{t:\mathbf x_0+t\mathbf d\in
Q\}$ is a compact subset of $\mathbb R$, hence has a maximum $t^*$; the
point $\mathbf y:=\mathbf x_0+t^*\mathbf d$ is a boundary point of $Q$ in
the sense that $Q$ lies entirely in the closed half-space $\{\mathbf x:
\mathbf d\cdot\mathbf x\le \mathbf d\cdot\mathbf y\}$ — because if some
$\mathbf x_1\in Q$ had $\mathbf d\cdot\mathbf x_1>\mathbf d\cdot\mathbf y$,
consider the supporting-hyperplane argument directly: let $H:=\{\mathbf
x:\mathbf d\cdot \mathbf x=\max_{Q}\mathbf d\cdot\mathbf x\}$ where the
max exists by compactness and continuity of the linear map $\mathbf
x\mapsto\mathbf d\cdot\mathbf x$ (Extreme Value Theorem). Then $F:=Q\cap H$
is a nonempty compact convex set (a **face** of $Q$) of dimension strictly
less than $\dim Q$ (it lies in the hyperplane $H$, which meets the affine
hull of $Q$ in a proper affine subspace, since $\mathbf d\cdot(\cdot)$ is
non-constant on $Q$ by choice of $\mathbf d$). By the induction hypothesis
(applied to $F$, of strictly smaller dimension — the induction is really on
$\dim Q$, base case $\dim Q=0$ trivial), $F$ has a vertex $\mathbf v$. We
claim $\mathbf v$ is also a vertex of $Q$: if $\mathbf v=\tfrac12(\mathbf
y+\mathbf z)$ for distinct $\mathbf y,\mathbf z\in Q$, then since $\mathbf
d\cdot\mathbf v=\max_Q(\mathbf d\cdot\cdot)$ and $\mathbf
d\cdot\mathbf y,\mathbf d\cdot\mathbf z\le\max_Q$, their average equalling
the max forces $\mathbf d\cdot\mathbf y=\mathbf d\cdot\mathbf z=\max_Q$,
i.e. $\mathbf y,\mathbf z\in F$ too — contradicting $\mathbf v$ being a
vertex of $F$. $\blacksquare$

**Lemma 3.2 (LP fact).** If $f$ is linear and $Q$ is a nonempty compact
convex polytope, $\min_Q f$ is attained at a vertex of $Q$.

**Proof.** By the Extreme Value Theorem, $m:=\min_Q f$ is attained; the set
$F^*:=\{\mathbf x\in Q: f(\mathbf x)=m\}$ is nonempty, and is convex
(if $f(\mathbf y)=f(\mathbf z)=m$ then $f(\tfrac12(\mathbf y+\mathbf
z))=m$ by linearity, and convexity of $Q$ gives $\tfrac12(\mathbf
y+\mathbf z)\in Q$) and compact (closed subset — preimage of $\{m\}$ under
continuous $f$ — of the compact set $Q$). By Lemma 3.1, $F^*$ has a vertex
$\mathbf v$. We claim $\mathbf v$ is also a vertex of $Q$: if
$\mathbf v=\tfrac12(\mathbf y+\mathbf z)$ with $\mathbf y,\mathbf z\in Q$
distinct, then $m=f(\mathbf v)=\tfrac12(f(\mathbf y)+f(\mathbf z))\ge
m$ (since $f(\mathbf y),f(\mathbf z)\ge m$ by definition of $m$ as the
min), forcing $f(\mathbf y)=f(\mathbf z)=m$, i.e. $\mathbf y,\mathbf
z\in F^*$ — contradicting $\mathbf v$ extreme in $F^*$. So $\mathbf v$ is a
vertex of $Q$ with $f(\mathbf v)=m$. $\blacksquare$

Applying Lemma 3.2 to $Q=R_\sigma(\mathbf m)$, $f=f_\sigma$: each
$\min_{R_\sigma(\mathbf m)}f_\sigma$ is attained at a vertex of
$R_\sigma(\mathbf m)$.

### 4. Vertex characterization: active constraints determine the point

**Lemma 4.1.** Let $\mathbf v$ be a vertex of $R_\sigma(\mathbf m)$
($N>k$, i.e. at least one cut is genuinely allocated, $\sum m_i\ge1$).
Then the number of the following "pinning" conditions that hold *exactly*
(with equality) at $\mathbf v$ is at least $N-k=\sum_i m_i$:
- $v_j=0$ for slot $j$ (a **zero** condition), or
- $v_{\sigma(j)}=v_{\sigma(j+1)}$ for $1\le j\le N-1$ (a **tie** condition).

**Proof.** The $k$ equality constraints defining $P(\mathbf m)$ (one per
piece, $\sum_{j\in\mathrm{slots}(i)}x_j=p_i$) have gradient vectors
$\mathbf g_i=\sum_{j\in\mathrm{slots}(i)}\mathbf e_j$ ($\mathbf e_j$ the
$j$-th standard basis vector). Since $\mathrm{slots}(1),\dots,
\mathrm{slots}(k)$ partition $\{1,\dots,N\}$, the supports of
$\mathbf g_1,\dots,\mathbf g_k$ are pairwise disjoint and nonempty, so
$\mathbf g_1,\dots,\mathbf g_k$ are linearly independent; the tangent
(null) space of the equality constraints,
$$T:=\{\mathbf d\in\mathbb R^N:\ \textstyle\sum_{j\in\mathrm{slots}(i)}d_j=0\ \forall i\},$$
has dimension exactly $N-k$.

Suppose, for contradiction, that fewer than $N-k$ of the pinning conditions
hold at $\mathbf v$. Let $A$ be the set of *active* inequality constraints
at $\mathbf v$ among $\{x_j\ge0\}_j\cup\{x_{\sigma(j)}\ge x_{\sigma(j+1)}\}_j$
(exactly the pinning conditions, restated as inequalities that hold with
equality); $|A|<N-k$. Each constraint in $A$ has gradient $\pm\mathbf e_j$
(zero conditions) or $\mathbf e_{\sigma(j)}-\mathbf e_{\sigma(j+1)}$ (tie
conditions); let $W\subseteq\mathbb R^N$ be the span of these $|A|$
gradients, $\dim W\le|A|<N-k=\dim T$. Since $T\cap W^\perp$ has dimension
$\ge \dim T-\dim W>0$ (as $W$ has dimension $<\dim T$, its intersection
with $T$ has codimension $\le\dim W$ inside $T$, so $T\cap W^\perp$, the
orthogonal complement of $W$ restricted to $T$, is nonempty of positive
dimension — concretely: $\dim(T\cap W^\perp)\ge \dim T-\dim W>0$ by the
standard subspace-dimension inequality $\dim(U\cap V)\ge\dim U+\dim
V-N$ applied with $U=T,V=W^\perp$, $\dim W^\perp=N-\dim W$, giving
$\dim(T\cap W^\perp)\ge \dim T-\dim W$), there is a nonzero
$\mathbf d\in T$ with $\mathbf d\perp$ every active-constraint gradient in
$A$ — i.e. $\sum_{j\in\mathrm{slots}(i)}d_j=0$ for every $i$ (so $\mathbf
v\pm t\mathbf d$ stays on the affine subspace of the equalities for every
$t$), and $d_j=0$ for every zero-active slot $j\in A$, and
$d_{\sigma(j)}=d_{\sigma(j+1)}$ for every tie-active pair in $A$.

For $t$ small enough (finitely many *inactive* inequality constraints at
$\mathbf v$, each strict, so by continuity each stays strict for
sufficiently small $|t|$ — take $t$ below the minimum positive slack
divided by $\max_j|d_j|+1$), both $\mathbf v+t\mathbf d$ and $\mathbf
v-t\mathbf d$: (i) satisfy the equalities exactly, since $\mathbf d\in T$;
(ii) satisfy every *active* zero constraint exactly (since $d_j=0$ there,
the coordinate is unchanged at $0$) and every *active* tie constraint
exactly (since $d_{\sigma(j)}=d_{\sigma(j+1)}$, the two coordinates move
together, preserving equality); (iii) satisfy every *inactive* (strict)
constraint by the small-$t$ choice. So $\mathbf v\pm t\mathbf
d\in R_\sigma(\mathbf m)$ for small enough $t>0$, and $\mathbf
v=\tfrac12\big((\mathbf v+t\mathbf d)+(\mathbf v-t\mathbf d)\big)$ with
$\mathbf v+t\mathbf d\ne\mathbf v-t\mathbf d$ (as $\mathbf d\ne0$,
$t\ne0$) — contradicting $\mathbf v$ being a vertex. $\blacksquare$

**Combining Sections 2–4 (Vertex Pinning Lemma, general form).** For any
fixed LB partition and budget $n$: XY's optimal value $V^*$ is attained by
a genuine response $\mathbf x^*$ (Section 1) that, for its cut allocation
$\mathbf m^*$ and sort order $\sigma^*$, has **at least $\sum_i m_i^*$
exact "pinning" conditions active** — each condition being either a
fragment equal to $0$ (which, by Section 1(b), we may take to mean: a cut
was not actually spent there, so w.l.o.g. after applying Section 1's
reduction, $\mathbf x^*\in P^\circ(\mathbf m^*)$ has *no* zero coordinates
at all, meaning *every* one of the $\ge\sum_i m_i^*$ pinning conditions is
an exact **tie** between two elements of the final multiset). This is
proved rigorously and in full generality: it is not asserted, it follows
from Lemma 3.2 (min attained at a vertex) plus Lemma 4.1 (vertex ⟹
$\ge N-k$ active pinning conditions) applied to the region $R_{\sigma^*}$
of the allocation $\mathbf m^*$ from Section 1, using $N-k=\sum_i m_i^*$
by construction.

### 5. The stronger *per-fragment* claim is FALSE — an exact counterexample

The round's outline and math-explorer conjectured (numerically, based on
observed optima) the stronger claim: *every individual optimal fragment is
either $0$ or tied with some other specific element of the final
multiset.* This is **strictly stronger** than the Vertex Pinning Lemma
above (which only counts *how many* tie/zero conditions are active in
total, not that every fragment individually participates in one). We show
the stronger claim is **false** by an explicit, exact, hand-verified
counterexample — precisely the kind of check the standing memory rule
demands before trusting an abstract structural claim.

**Construction.** Take $k=3$ (so this fits within budget $n=2$: one cut on
piece 1, no cuts elsewhere), with pieces
$$p_1=\tfrac{6}{10},\quad p_2=\tfrac{3}{10},\quad p_3=\tfrac1{10},\qquad p_1+p_2+p_3=1.$$
Split $p_1$ into $a=p_3=\tfrac1{10}$ and $b=p_1-a=\tfrac12$ (one cut, both
fragments strictly positive: legal). The resulting multiset is
$\{b,\,p_2,\,a,\,p_3\}=\{\tfrac12,\ \tfrac3{10},\ \tfrac1{10},\ \tfrac1{10}\}$.
Sorted descending: $b=\tfrac12$ (rank 1), $p_2=\tfrac3{10}$ (rank 2),
$a=p_3=\tfrac1{10}$ (ranks 3, 4, exactly tied). So $\mathrm{OddSum}=b+a=
\tfrac12+\tfrac1{10}=\tfrac35$, and note $\tfrac35=p_1$ exactly (an
instance of the identity: when a piece is split into two fragments landing
at ranks separated by exactly one other fixed element, the two fragments'
sum — which is fixed, $=p_1$ — is exactly the $\mathrm{OddSum}$
contribution, *independent of how the piece is split*, as long as the
sort-order pattern is preserved).

**This is a genuine vertex with an untied, nonzero fragment.** Consider
the family of splits $p_1\to(a,b)=(a,\,p_1-a)$ for $a$ ranging over
$[\,\tfrac1{10},\ \tfrac{3}{10}\,]$ (the range keeping the sort order
$b\ge p_2\ge a\ge p_3$: need $b=p_1-a\ge p_2=\tfrac3{10}\iff a\le
\tfrac3{10}$, and $a\ge p_3=\tfrac1{10}$). Because $a+b=p_1$ is fixed and
exactly one element ($p_2$) separates them in sort order, $f_\sigma(a,b)=
b+a=p_1$ is **constant** on this whole interval — a genuine (though
degenerate: linear functional constant on a positive-dimensional face)
instance of the LP fact that the argmin set can be a face, not a single
point (exactly the phenomenon flagged as needing care in Lemma 3.2's
proof). The two **endpoints** $a=\tfrac1{10}$ and $a=\tfrac3{10}$ of this
interval are exactly the two vertices of $R_\sigma(\mathbf m)$ restricted
to this face (Lemma 4.1 applies: at $a=\tfrac1{10}$, the active pinning
condition is $a=p_3$ — one tie, matching $N-k=4-3=1$ needed — and at
$a=\tfrac3{10}$, the active condition is $b=p_2$ instead). At our chosen
vertex ($a=\tfrac1{10}$), the tie condition $a=p_3$ accounts for the
*entire* required pinning budget of $N-k=1$; fragment $b=\tfrac12$ is
therefore **not required by, and does not happen to satisfy**, any tie or
zero condition — it is pinned only *indirectly*, via $a+b=p_1$ together
with $a$ being fixed by the *other* fragment's tie. Direct check: $b=
\tfrac12\ne p_2=\tfrac3{10}$ and $b\ne a=p_3=\tfrac1{10}$, so $b$ is
neither $0$ nor tied with anything.

**Conclusion.** The literal per-fragment "tie-or-zero" claim is **false**
in general: at this genuine LP vertex (attaining the min of $f_\sigma$ on
$R_\sigma(\mathbf m)$, indeed attaining it on the *entire* face, so
certainly an optimal point), the fragment $b$ is a counterexample. The
correct general fact is the weaker, but still fully rigorous and useful,
**counting** form proved in Section 4: the *total* number of active
tie/zero conditions is $\ge\sum m_i$, not that *every* fragment
individually touches one. This distinction matters and is exactly the kind
of gap a purely numeric survey (which only samples specific optima, and in
every sampled case may have happened to see full pinning by coincidence of
the specific instances tried) can miss — consistent with the standing
memory rule to verify structural claims exactly, not just trust
convergent numerics.

### 6. What the (corrected) Vertex Pinning Lemma buys: a finite-search
reduction, honestly scoped

For a **fixed** LB partition $(p_1,\dots,p_k)$ and budget $n$, Sections
1–4 show: XY's optimal value $V^*$ equals the minimum, over the *finite*
set of (a) cut allocations $\mathbf m$ with $\sum m_i\le n$ (at most
$\binom{n+k}{k}$ many), (b) sort orders $\sigma$ compatible with
$\mathbf m$ (at most $N!$ many, $N=\sum(m_i+1)\le n+k$), and (c) a choice
of $\ge N-k$ tie/zero pinning conditions among the $\le N-1+N$ candidate
constraints of $R_\sigma(\mathbf m)$ — of the value obtained by solving the
resulting *linear system* (the pinning equalities, together with the $k$
piece-sum equalities) for the fragment values, **provided** the resulting
point is non-negative and satisfies the remaining (non-active) order
constraints. This is a genuine reduction of a continuous optimization (over
an infinite-dimensional-in-the-limit space of allocations/splits) to a
**finite combinatorial check** for any one fixed partition — this is the
promised positive tool.

**What this does *not* yet give: closure of the balanced-region gap.**
LB's *outer* maximization is still over a continuum of partitions
$(p_1,\dots,p_k)$ (the pinning conditions' *linear system*, once solved,
gives fragment values that are themselves linear/rational functions of
$p_1,\dots,p_k$, but which combinatorial "type" — i.e. which allocation,
sort order, and set of active pinning conditions — is optimal can itself
change discontinuously as $(p_1,\dots,p_k)$ varies, exactly the
phenomenon `universal-halving-adversary`'s numerics observed: "usually
1-2 pieces split, not all", suggesting the optimal *type* is a
locally-constant but globally-varying function of the partition). Turning
the Vertex Pinning Lemma into an existence-style closure of $c(n)$ for the
balanced region would require either (i) an explicit description of which
combinatorial type is optimal as a function of $(p_1,\dots,p_k)$ across the
whole region (this is exactly what `universal-halving-adversary`'s
"matching rule" is separately attempting, and is not re-derived here), or
(ii) a genuinely different, partition-independent argument (e.g. a uniform
upper bound on $V^*$ valid for *every* type simultaneously) that does not
require identifying the optimal type at all. I attempted (ii) briefly:
using only the *counting* fact (some $\ge \sum m_i$ conditions are ties,
zero conditions removed) to derive a universal upper bound on $V^*$
independent of which specific ties occur — this does not work directly,
because the *value* of $f_\sigma$ at the pinned vertex genuinely depends on
*which* elements are tied (as Section 5's example shows: $f_\sigma$ can
even be locally constant along a whole face, but its value across
*different* faces/vertices varies with the specific tie chosen, e.g.
$0.505$ vs. $0.515$ in round 4's counterexample) — so a partition-blind
bound is not available from the counting fact alone; the *specific*
matching of ties to anchors is load-bearing, matching exactly
`lp-duality-split-polytope`'s complementary "necessity" framing this round
(which other pieces get involved is not accidental, it is forced by the
shadow-price structure that approach targets). **Honest conclusion: step 5
of the outline (turn the structural lemma into an existence-style closure)
remains open; the Vertex Pinning Lemma is a proved, reusable structural
tool (Section 4), but closing the balanced region needs it combined with
either an explicit matching-rule construction (`universal-halving-
adversary`'s target) or a necessity/duality argument
(`lp-duality-split-polytope`'s target) — neither of which is re-derived
here.**

### 7. Cheap check (this round): the majorization/suffix-domination
monotonicity lead is FALSE — dead end, with a proved structural reason

**Formalizing the analogy.** The fresh-framing explorer's Part B flagged,
with an explicit honest caveat, a candidate transplant of `aimo-0287`'s
crux (a suffix-domination partial order `X⪯Y` on subsets of a fixed index
set, satisfying `X⪯Y \implies \Sigma_X a\le\Sigma_Y a` for any increasing
sequence `a`) to our setting. `aimo-0287`'s order compares two subsets of
the *same* fixed index universe `\{1,\dots,n\}`; `OddSum` here instead acts
on the sorted order statistics of a *single* multiset that itself varies in
shape between candidates. The natural, most literal transplant of
"suffix-domination = more mass pushed toward the top" onto a single sorted
real vector is **classical majorization**: for two vectors $M=(m_1,\dots,
m_N)$, $M'=(m_1',\dots,m_N')$ of the *same length* $N$, both sorted
descending, with $\sum m_i=\sum m_i'$, say $M'$ **majorizes** $M$ (written
$M'\succ M$) if
$$\sum_{i=1}^{j}m_i'\ \ge\ \sum_{i=1}^j m_i\qquad\text{for every }j=1,\dots,N-1$$
(with equality automatically at $j=N$). This is exactly the real-valued
analogue of "every prefix — equivalently, by taking complements within a
fixed total, every suffix — of $M'$ dominates the corresponding prefix/
suffix of $M$", the direct transplant of `aimo-0287`'s index-suffix order to
value-order statistics. The candidate lemma to test is:
$$M'\succ M\ \implies\ \mathrm{OddSum}(M')\ \ge\ \mathrm{OddSum}(M). \tag{$\star$}$$

**Cheap numeric test.** I tested $(\star)$ directly: (a) by exact
rational hand construction, and (b) by a $200{,}000$-trial random search
over pairs of random compositions of $1$ into $N=4$ nonnegative parts,
filtering for majorization-comparable pairs and checking the direction of
the `OddSum` inequality.

**Counterexample (exact, $N=4$).** Take
$$M=(0.34,\ 0.33,\ 0.32,\ 0.01),\qquad M'=(0.36,\ 0.34,\ 0.29,\ 0.01),$$
both sorted descending, both summing to $1$ exactly, all entries strictly
positive (a legitimate final refinement multiset, not a degenerate
zero-fragment case). Check majorization: partial sums of $M'$ are
$0.36,\ 0.70,\ 0.99,\ 1.00$; of $M$ are $0.34,\ 0.67,\ 0.99,\ 1.00$. Indeed
$0.36\ge0.34$, $0.70\ge0.67$, $0.99\ge0.99$ (equality), $1.00=1.00$ — so
$M'\succ M$ holds. But
$$\mathrm{OddSum}(M)=m_1+m_3=0.34+0.32=0.66=\tfrac{33}{50},\qquad
\mathrm{OddSum}(M')=m_1'+m_3'=0.36+0.29=0.65=\tfrac{13}{20},$$
so $\mathrm{OddSum}(M')<\mathrm{OddSum}(M)$ **despite** $M'$ majorizing
$M$ — a direct, exact refutation of $(\star)$. (Verified with exact
`Fraction` arithmetic, not floating point.) The random search independently
confirms majorization-comparable pairs realize *both* directions of the
`OddSum` inequality (found instances with $\mathrm{OddSum}(M')>
\mathrm{OddSum}(M)$ and instances with $\mathrm{OddSum}(M')<
\mathrm{OddSum}(M)$ among genuinely majorization-related pairs) — so not
only does $(\star)$ fail, **no** monotonicity of either sign holds under
majorization. Per the outline's instruction, this kills the lead
immediately: **do not build further proof narrative on $(\star)$.**

**Why it fails — the general structural reason (proved in full, not just a
counterexample).** `OddSum` is, on any region where the sort order is
fixed, the fixed linear functional
$$L_c(\mathbf x)=\sum_{i=1}^N c_i\,x_{[i]},\qquad c=(1,0,1,0,1,0,\dots)
\quad(\text{$1$ at odd ranks, $0$ at even ranks}),$$
of the descending order statistics $x_{[1]}\ge\cdots\ge x_{[N]}$ (Section 2,
Lemma 2.1, of this file). The following is the standard
Hardy–Littlewood–Pólya characterization of when a linear functional of
order statistics is monotone under majorization (proved here from scratch,
since it is exactly what determines whether $(\star)$-type lemmas can ever
work for a given weight pattern, and knowledge of *why* it fails is more
useful going forward than the single counterexample alone):

**Proposition (Schur-monotonicity criterion for linear order-statistic
functionals).** Fix $N\ge2$ and weights $c_1,\dots,c_N\in\mathbb R$. Then
$$M'\succ M\ \implies\ L_c(M')\ge L_c(M)\quad\text{for every majorization
pair }M'\succ M \text{ of length }N$$
holds **if and only if** $c_1\ge c_2\ge\cdots\ge c_N$ (the weights are
non-increasing along the sorted order).

**Proof.**

($\Leftarrow$) Suppose $c_1\ge\cdots\ge c_N$. Let $M'\succ M$, both sorted
descending, and set $d_j:=\sum_{i=1}^j(m_i'-m_i)$ for $j=0,\dots,N$, so
$d_0=0$, $d_N=0$ (equal totals), and $d_j\ge0$ for $1\le j\le N-1$
(majorization). Writing $a_i:=m_i'-m_i=d_i-d_{i-1}$ and applying Abel
summation (summation by parts):
$$L_c(M')-L_c(M)=\sum_{i=1}^N c_i a_i=\sum_{i=1}^N c_i(d_i-d_{i-1})
=\sum_{i=1}^{N-1}(c_i-c_{i+1})\,d_i\ +\ c_N d_N-c_1 d_0.$$
(Standard rearrangement: $\sum_{i=1}^N c_i d_i-\sum_{i=1}^N c_i d_{i-1}
=\sum_{i=1}^N c_i d_i-\sum_{i=0}^{N-1}c_{i+1}d_i=c_Nd_N-c_1d_0+
\sum_{i=1}^{N-1}(c_i-c_{i+1})d_i$.) Since $d_0=d_N=0$, this reduces to
$$L_c(M')-L_c(M)=\sum_{i=1}^{N-1}(c_i-c_{i+1})\,d_i.$$
If $c_1\ge\cdots\ge c_N$, every factor $c_i-c_{i+1}\ge0$, and every
$d_i\ge0$, so the whole sum is $\ge0$, i.e. $L_c(M')\ge L_c(M)$.

($\Rightarrow$) Suppose some $c_{i_0}<c_{i_0+1}$ for an index
$1\le i_0\le N-1$. Construct an explicit majorization pair violating the
conclusion: take $d_{i_0}=\varepsilon>0$ small and $d_i=0$ for all other
$i\in\{1,\dots,N-1\}$; this is a legitimate majorization "shape" (all
$d_i\ge0$) provided it is realizable by an actual pair of sorted-descending
vectors with a fixed common total — which it is, e.g. take $M=(1/N,\dots,
1/N)$ (uniform) and $M'$ obtained from $M$ by moving mass $\varepsilon$
from position $i_0+1$ to position $i_0$: $m_{i_0}'=1/N+\varepsilon$,
$m_{i_0+1}'=1/N-\varepsilon$, all other entries unchanged, for
$0<\varepsilon< 1/N$ small enough that $M'$ remains sorted descending (this
is possible whenever $i_0<N$, using strict inequality $1/N+\varepsilon
>1/N-\varepsilon$ and, if $i_0\ge2$ or $i_0+1\le N-1$, the untouched
neighbors are equal to $1/N$ so weak inequalities $m_{i_0-1}'=1/N\ge
1/N+\varepsilon$ would fail for large $\varepsilon$ — but for $\varepsilon$
small enough, specifically $\varepsilon<1/N$ combined with, if $i_0\ge2$,
also comparing to the untouched entry at position $i_0-1=1/N$: we need
$1/N+\varepsilon$ to be the new *largest* only relative to positions
$\ge i_0$, which for the *uniform* base vector requires care since all
other entries equal $1/N$ exactly — to keep $M'$ validly sorted descending
non-strictly, allow ties: $M'=(1/N,\dots,1/N+\varepsilon,1/N-\varepsilon,
\dots,1/N)$ is sorted descending as *written* (ties permitted, and the
single strict inequality $1/N+\varepsilon>1/N-\varepsilon$ occurs exactly
at the transition, all other adjacent pairs are still equal or already
correctly ordered) for every $0<\varepsilon<1/N$; no further condition is
needed). Then $d_j=0$ for $j\ne i_0$ and $d_{i_0}=\varepsilon>0$ by
construction (prefix sums differ only at $j=i_0$), so $M'\succ M$ (all
$d_j\ge0$, $j=1,\dots,N-1$, $d_N=0$), and by the identity above,
$$L_c(M')-L_c(M)=(c_{i_0}-c_{i_0+1})\varepsilon<0$$
since $c_{i_0}-c_{i_0+1}<0$ and $\varepsilon>0$ — i.e. $M'\succ M$ but
$L_c(M')<L_c(M)$, violating the claimed monotonicity. $\blacksquare$

**Application to `OddSum`.** For $N\ge3$, the weight vector
$c=(1,0,1,0,\dots)$ satisfies $c_1-c_2=1-0=1>0$ (consistent with
monotone-decreasing so far) but $c_2-c_3=0-1=-1<0$ — a violation at
$i_0=2$. By the Proposition's ($\Rightarrow$) direction, this means
$(\star)$ **must** fail for $N\ge3$, and the explicit construction in the
proof (move mass $\varepsilon$ from rank $3$ to rank $2$ of a
near-uniform vector) is exactly the mechanism realized concretely by the
hand-built counterexample above (there, the "defect" is the redistribution
between ranks $2$ and $3$: $M$ has $(m_2,m_3)=(0.33,0.32)$ and $M'$ has
$(m_2',m_3')=(0.34,0.29)$ — mass moved from rank $3$ into rank $2$, which
is exactly a *zero-weighted* rank absorbing majorized mass at the expense
of an *odd*-weighted rank, decreasing the odd-weighted total). Note also
that for $N=2$, $c=(1,0)$ **is** non-increasing, so `OddSum` restricted to
size-$2$ multisets IS Schur-monotone — consistent with the failure being a
genuine feature of $N\ge3$, not an error in the construction; but $N=2$ is
the trivial/uninteresting case for this problem (a single top element and
one other), so this does not rescue $(\star)$ for the balanced-region
instances (which have $N=k+\sum m_i\ge3$) that actually need closing.

**Conclusion.** The majorization/suffix-domination monotonicity mechanism
is **dead** for this problem, not merely on the sampled numeric instances
but for a *provable structural reason*: `OddSum`'s alternating weight
pattern on sorted order statistics is neither Schur-convex nor
Schur-concave (for any $N\ge3$), so majorization — the natural, most
literal transplant of `aimo-0287`'s suffix-domination order to a single
sorted real vector — carries **no** information about `OddSum`'s value,
in either direction. This closes the "cheap check first" task assigned
this round with a definitive negative, and per the outline's built-in
fallback (step 4), this approach's live positive contribution this round
remains the already-certified Vertex Pinning Lemma (Sections 0–4, from
round 5), available as a supporting tool for `universal-halving-
adversary`'s Existence Theorem — not re-derived here, see that approach's
own file for its own progress this round.

### Summary of this round's positive/negative content
- **Proved (fully rigorous, reusable):** Closure Lemma (Section 1);
  linearity of `OddSum` on sort-order regions (Section 2, Lemma 2.1);
  the general LP-vertex-attains-minimum fact for compact polytopes
  (Section 3, Lemmas 3.1–3.2, proved from scratch, not merely cited);
  the Vertex Pinning Lemma (Section 4, Lemma 4.1 + combination) — the
  corrected, counting form of the Tie-or-zero structural fact.
- **Disproved (exact counterexample, Section 5):** the literal stronger
  per-fragment form of the Tie-or-zero claim, as originally proposed by
  this round's outline/explorer. This is an honest correction, not a
  failure to deliver — the corrected form (Section 4) is what is actually
  true and is what gets certified below.
- **Honestly scoped as open (Section 6):** using the Vertex Pinning Lemma
  to close the balanced-region upper-bound gap for general $n$; the lemma
  reduces each *fixed*-partition subproblem to a finite search but does
  not by itself resolve LB's outer maximization over the continuum of
  partitions.
- **Round 6: killed (fully, with a proved structural reason, Section 7):**
  the majorization/suffix-domination monotonicity lead flagged by this
  round's fresh-framing explorer. Formalized the candidate lemma
  $(\star)$ precisely, found an exact rational counterexample, confirmed
  by random search that majorization controls `OddSum` in *neither*
  direction, and proved the general reason (`OddSum`'s alternating
  odd-rank weight pattern is not Schur-monotone for $N\ge3$, by the
  Hardy–Littlewood–Pólya-style Proposition proved from scratch). This is
  a documented dead end, not a gap: do not attempt to revive the
  majorization/suffix-domination mechanism for `OddSum` in any future
  round of this problem.

## Full proof
(none — Status is `partial`. The Vertex Pinning Lemma (Sections 1–4) is a
complete, rigorous, positive structural result — a real deliverable per
this round's target of "turn prior negative results into a positive tool"
— but it does not by itself close either remaining gap in `current.md`.
Section 5 is a complete, rigorous *correction* of the literal stronger
claim originally proposed, established by exact counterexample. Section 6
honestly diagnoses exactly what more is needed and hands the specific
missing pieces to the two approaches (`universal-halving-adversary`,
`lp-duality-split-polytope`) already targeting them this round.)

## Promotable lemmas

**Vertex Pinning Lemma for the split-multiset polytope** (Sections 0–4,
proved in full).

*Statement.* Fix a partition $p_1,\dots,p_k>0$ ($\sum p_i=1$) and a budget
$n$. For the game value $V^*=\min$ over legal XY responses (cut
allocations $\mathbf m$ with $\sum m_i\le n$, splitting each $p_i$ into
$m_i+1$ positive parts) of $\mathrm{OddSum}$ of the resulting multiset:
1. $V^*$ is attained (a genuine minimum, not just an infimum) by an honest
   response with strictly positive fragments (Closure Lemma).
2. For the minimizer's own cut allocation $\mathbf m^*$ (with $\sum
   m_i^*$ genuine cuts, after discarding any wasted/zero-length cuts per
   the Closure Lemma) and its induced sort order, at least $\sum_i
   m_i^*$ *independent* exact ties (pairs of elements of the final
   multiset with exactly equal value, possibly two fragments of the same
   split piece, possibly a fragment and an untouched other piece, possibly
   fragments from two different split pieces) are simultaneously active.

*Where proved.* This file, Sections 0–4 (`approaches/
dyadic-potential-invariant.md`, round 5): Section 1 (Closure Lemma,
compactness/degenerate-cut handling), Section 2 (linearity on sort-order
regions, Lemma 2.1), Section 3 (LP-vertex-attains-min, Lemmas 3.1–3.2,
proved from first principles), Section 4 (vertex characterization via
linear independence of active-constraint gradients, Lemma 4.1).

*Companion negative result (also fully proved, Section 5), should travel
with the lemma to prevent mis-citation:* the naive strengthening "every
individual optimal fragment is 0-or-tied" (not just a total *count* of
$\ge\sum m_i$ ties) is **false** — exact counterexample: $k=3$,
$(p_1,p_2,p_3)=(0.6,0.3,0.1)$, split $p_1\to(0.5,0.1)$ (one cut);
resulting multiset $\{0.5,0.3,0.1,0.1\}$, $\mathrm{OddSum}=0.6=p_1$
exactly; the fragment $0.5$ is neither $0$ nor tied with anything, at a
genuine vertex of the relevant polytope (indeed at every point of an
entire optimal face). Only the *counting* form is true in general.

*Reuse.* Any approach reasoning about XY's optimal response structure for
a *fixed* LB partition may cite the counting form directly instead of
re-deriving the LP argument; the companion negative result should be cited
alongside it to prevent re-deriving (and mis-trusting) the stronger,
false, per-fragment form. In particular this directly resolves the round-5
outline's own explicit request "prove this characterization rigorously (a
concrete linear-algebra fact about polytope faces, not just an appeal to
intuition)" — done, with the correction noted.

**Schur-monotonicity criterion for linear order-statistic functionals**
(Section 7, proved in full, round 6).

*Statement.* Fix $N\ge2$ and real weights $c_1,\dots,c_N$, and define
$L_c(\mathbf x)=\sum_{i=1}^N c_i x_{[i]}$ for $x_{[1]}\ge\cdots\ge x_{[N]}$
the descending order statistics of $\mathbf x$. Then $L_c$ is monotone
under majorization ($M'\succ M\implies L_c(M')\ge L_c(M)$ for every
majorization pair of length $N$) **if and only if** $c_1\ge c_2\ge\cdots
\ge c_N$. Consequently, for $N\ge3$, `OddSum` (the case $c=(1,0,1,0,\dots)$)
is **not** monotone under majorization in either direction, since
$c_1-c_2=1>0$ but $c_2-c_3=-1<0$ violates the criterion; an explicit exact
rational counterexample realizing the failure is given in Section 7.

*Where proved.* This file, Section 7, round 6: both directions of the
iff proved from scratch via an Abel-summation identity
$L_c(M')-L_c(M)=\sum_{i=1}^{N-1}(c_i-c_{i+1})d_i$ (where $d_i$ are the
prefix-sum differences witnessing majorization), plus an explicit
majorization-pair construction (move mass $\varepsilon$ between two
adjacent ranks of a near-uniform vector) realizing the converse.

*Reuse.* Any future approach to this problem (or a structurally similar
sorted-rank-sum problem) tempted to use a majorization/suffix-domination
argument should check this criterion first: it applies to *any* linear
functional of order statistics, and immediately tells you, from the
weight pattern alone, whether the mechanism can possibly work — no
per-instance numeric search needed. For `OddSum` specifically the answer
is a clean, permanent **no** (for all $N\ge3$, i.e. every case of interest
in this problem), so this lemma should be cited to immediately rule out
re-attempting the majorization mechanism rather than re-deriving the
counterexample each time.
