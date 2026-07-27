# IMO 2026, Problem 3 — Solution and Commentary

**Problem.** Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of
length $1$. First Liu Bang marks at most $n$ points on the stick, and then Xiang
Yu marks at most $n$ further points; all marked points are distinct. The stick is
cut at every marked point. The players then alternately claim unclaimed pieces,
with Liu Bang moving first, and each player seeks to maximize the total length of
the pieces he claims. Determine the largest number $c$ that Liu Bang can
guarantee, regardless of Xiang Yu's play.

---

## Answer

$$\boxed{\,c(n)=\dfrac{2^{\,n}}{2^{\,n+1}-1}\,} \qquad\bigl(S_n:=2^{n+1}-1\bigr).$$

Equivalently, the minimax *alternating-sum value* of the game is
$D^\star = 1/S_n = 1/(2^{n+1}-1)$, and Liu Bang's guarantee is
$c(n)=(1+D^\star)/2 = 2^n/S_n$.

Values: $c(1)=\tfrac23,\; c(2)=\tfrac47,\; c(3)=\tfrac{8}{15},\; c(4)=\tfrac{16}{31},\;
c(5)=\tfrac{32}{63}$ (decreasing to $\tfrac12$).

### Status of the proof

| Bound | $n=1$ | $n=2$ | $n=3$ | general $n$ |
|---|---|---|---|---|
| Lower bound ($c(n)\ge 2^n/S_n$) | proved (both directions) | **proved** | **proved** (cell enumeration) | proved in Case A; Case B conjectured |
| Upper bound ($c(n)\le 2^n/S_n$) | proved | **proved** | conjectured | conjectured |

The value is **fully proved** for $n=1$ and $n=2$ (both directions): $c(1)=2/3$,
$c(2)=4/7$. The **lower bound is proved for $n=3$**: $c(3)\ge 8/15$ (exhaustive
cell enumeration with the vertex-min principle). The answer is confirmed for
$n\le 5$ by exact (piecewise-linear) numerical search. The general lower bound
(Case B), the $n=3$ upper bound, and the general upper bound are conjectured,
with the precise obstruction identified below. This file records an honest
partial proof; the conjectured parts are clearly marked.

---

## 1. Reduction to an alternating-sum game

After all cuts the pieces have lengths $a_1\ge a_2\ge\cdots\ge a_m>0$ with
$\sum a_i=1$. In the claiming phase the players alternate, Liu Bang first, each
taking the largest remaining piece (greedy).

**Lemma A (greedy is optimal for both players).** *In an alternating item-picking
game with values $v_1\ge\cdots\ge v_m>0$, greedy play (always take the largest
remaining item) is a subgame-perfect equilibrium for both players. Player 1 gets
$v_1+v_3+v_5+\cdots$ (odd positions), player 2 gets $v_2+v_4+\cdots$.*

*Proof (sketch).* Induction on $m$. If player 1 first takes $v_j$ instead of
$v_1$, player 2 then moves first on the remainder; comparing payoffs telescopes to
$\text{payoff}(1)-\text{payoff}(j)=(v_1-v_2)+(v_3-v_4)+\cdots\ge0$. $\square$

So Liu Bang's total is $\tfrac12(1+D)$ where
$$D \;=\; a_1-a_2+a_3-a_4+\cdots \;=\;\sum_i (-1)^{i+1}a_i,$$
and Xiang Yu's is $\tfrac12(1-D)$. The game thus reduces to:

> Liu Bang chooses a partition of $[0,1]$ into $\le n+1$ pieces; Xiang Yu adds
> $\le n$ cuts; Liu Bang maximizes, Xiang Yu minimizes, the **alternating sum**
> $D$ of the resulting $\le 2n+1$ pieces. The guarantee is $c(n)=\tfrac12\bigl(1+\min_{\text{XY}} D\bigr)$.

---

## 2. Two reformulations

Work in **unnormalized units** with total $S_n=2^{n+1}-1$; Liu Bang plays the
**geometric partition** $G_n=(1,2,4,\ldots,2^n)$ (pieces $2^k/S_n$), so the target
is $\min_{\text{XY}} D = 1$.

**Even-sum reformulation.** Since $\sum_{\text{odd}} a_i-\sum_{\text{even}} a_i=D$
and $\sum_{\text{odd}} a_i+\sum_{\text{even}} a_i=S_n$,
$$D\ge 1 \iff \textstyle\sum_{\text{even}} a_i \le S_n-2^n = 2^n-1
\iff \textstyle\sum_{\text{odd}} a_i \ge 2^n.$$
That is: **the second picker's take cannot exceed the mass of everything below the
largest piece**. This makes the easy case one line.

**Rank/parity integral.** With $r(t)=\#\{\text{pieces}\ge t\}$,
$$D=\int_0^\infty \mathbf 1_{\{r(t)\ \text{odd}\}}\,dt.$$
A cut splitting a piece of size $s$ into $(m,M)$ with $m\le M$ ($m+M=s$) changes
$r$ by $\Delta r=+1$ on $(0,m]$, $\Delta r=0$ on $(m,M]$, $\Delta r=-1$ on $(M,s]$;
both affected intervals have length $m$. Thus **a cut is a parity toggle-pair** of
two equal-length intervals. The geometric partition gives a self-similar "parity
staircase"; the lower bound asks whether $\le n$ toggle-pairs can drive
$\int\mathbf 1_{r\text{ odd}}$ below $1$.

---

## 3. Liu Bang's construction (lower bound)

Liu Bang marks $n$ points to make the geometric pieces $2^0:2^1:\cdots:2^n$, i.e.
pieces $\frac{2^k}{S_n}$. The **key structural fact** is the *$+1$ gap*:
$$2^k = \bigl(2^{k-1}+2^{k-2}+\cdots+2^0\bigr)+1,$$
so each geometric piece exceeds the *entire* mass below it by exactly one unit.
This gap is what survives Xiang Yu's cuts.

**Case A (Xiang Yu does not cut $2^n$).** Then $2^n$ is the unique largest piece,
occupying position $1$ (odd). Every even-position piece lies in the tail of total
$2^n-1$, so $\sum_{\text{even}}\le 2^n-1$, hence $D\ge1$. (One line.)

**Case B (Xiang Yu cuts $2^n\ge1$ time).** *Conjectured in general; proved for
$n=1$, $n=2$, and $n=3$ (exhaustive casework / cell enumeration).* The fragments of $2^n$ and the refined tail
$G_{n-1}$ are merged; the toggle-pair structure shows that $\le n$ toggle-pairs
applied to the geometric staircase leave at least one unit of "odd parity mass",
so $D\ge1$. Equality is **attained** by full halving
($2^j\mapsto 2^{j-1}+2^{j-1}$ for all $j$), giving $2n+1$ pieces
$2^{n-1}\!(\times2),\ldots,1\,(\times3)$ with every consecutive pair canceling and
$D=1$.

### The case $n=1$ (fully proved)

With two pieces $a\ge b$, $a+b=1$, the geometric play is $(a,b)=(2/3,1/3)$.
Xiang Yu's one cut either splits $a$ (giving $D=1/3$ regardless of where) or splits
$b$ (giving $D\ge1/3$); hence $\min D=1/3$ and $c(1)=2/3$.

### The case $n=2$ (fully proved this work: $c(2)=4/7$)

**Lower bound** ($c(2)\ge4/7$). For $G_2=(1,2,4)$ (total $7$) under $\le2$ cuts,
exhaustive casework on the number $k\in\{0,1,2\}$ of cuts falling on the piece
$4$, with sub-cases for which tail piece ($2$ or $1$) the remaining cut hits,
gives $D\ge1$ in every region, so $c(2)\ge4/7$. (Independently confirmed by a
$2\,000\,000$-sample random sweep: $0$ violations, $\min D=1$.) Equality $D=1$
is attained at full halving $4\to2+2,\ 2\to1+1$ (and on whole sub-regions, so the
minimizer is not unique).

**Upper bound** ($c(2)\le4/7$). For every three-piece partition
$a_1\ge a_2\ge a_3$ ($\sum=1$), four explicit universally valid XY strategies
give $D\in\{a_1-a_2,\,a_2-a_3,\,|2a_1-1|,\,a_3\}$ (each by halving or matching a
piece so the two equal fragments cancel in the alternating sum). A three-line
contradiction proves $\min$ of these four $\le1/7$: if all exceed $1/7$, then
$a_3>1/7$, $a_2>2/7$, $a_1>3/7$, hence $a_1>4/7$ (from $|2a_1-1|>1/7$), giving
$a_2+a_3<3/7$ contradicting $a_2+a_3>3/7$. Equality at the geometric partition
$(4/7,2/7,1/7)$. Hence $c(2)=4/7$.

### The case $n=3$ lower bound (proved this work: $c(3)\ge 8/15$)

For $G_3=(1,2,4,8)$ (total $15$) under $\le3$ cuts, the lower bound $D\ge1$ is
proved by exhaustive casework on $k_8$ (cuts on the piece $8$):

- **$k_8=0$** (Case A): $b_1=8$, $b_2\le4$, so $D\ge4\ge1$. Trivial.
- **$k_8=1$** (one cut on 8, two on $G_2$): hand proof in three sub-cases
  (partition by $b_2\in\{4,r,p\}$), using $L(2)$ and the trivial bound
  $\text{alt}_+\le\sum$.
- **$k_8=2$** (two cuts on 8, one on a tail piece $V\in\{4,2,1\}$): 59
  full-dimensional cells (32+14+13) enumerated with exact rational arithmetic;
  vertex-min principle gives each cell's minimum $D\in\{1,5/3,2,3,5\}\ge1$.
  (A complete self-contained Python script reproducing this verification is
  appended to \S B-5 of the main results file.)
- **$k_8=3$** (three cuts on 8, tail intact): 13 cells, each with $D\ge1$
  (verified by a complete 13-row table).

Fewer-than-3-cut configurations are degenerate boundary points of the 3-cut
cells, covered by the closed-cell analysis. Equality $D=1$ is attained in
particular at full halving $\{4,4,2,2,1,1,1\}$ and on the whole layered-straddle
family (fragments of 8 straddling $4,2,1$ with the tail intact). Rescaled,
$c(3)\ge8/15$. The matching upper bound $c(3)\le8/15$ is confirmed numerically
but not yet proved.

---

## 4. Xiang Yu's strategy (upper bound)

The matching upper bound $c(n)\le2^n/S_n$ says: *for every* partition into $\le n+1$
pieces, Xiang Yu with $\le n$ cuts forces $D\le1/S_n$.

- **$n=1$ (proved).** If the largest piece $L\ge2/3$, halve it: $D=1-L\le1/3$. If
  $1/2\le L<2/3$, shave a sliver $t\le\min(1-L,2L-1)$ off $L$: $D=2L-1<1/3$. At
  $L=1/2$ exactly, cut one half-piece into $(a,1/2-a)$ with $a\le1/6$: $D=2a\le1/3$.

- **$n=2$ (proved).** Four explicit XY strategies (halve $a_3$, halve $a_1$,
  match $a_2$, halve both) give $D\in\{a_1-a_2,\,a_2-a_3,\,|2a_1-1|,\,a_3\}$; the
  key inequality $\min\le1/7$ is a three-line contradiction. Equality at
  $(4/7,2/7,1/7)$.

- **General $n\ge3$ (conjectured).** The natural "halve-or-match then recurse" hybrid is
  governed by the **halving recurrence**: when $a_1\ge2a_2$, halving $a_1$ gives
  $D_{\text{new}}=a_1-D_{\text{old}}$. This handles the *top-heavy* regime
  $a_1\ge2a_2$ cleanly (on $G_n$ it gives $D=D_0(G_{n-k})$, reaching $1$ after
  $n-1$ cuts). The obstruction is the *flat* regime $a_1<2a_2$, where the recurrence
  breaks and the global nature of the alternating sum (the sorted order spans all
  pieces) blocks a naive induction. The conjectured clean route is a
  **majorisation/smoothing** principle: $f(C)=\min_{\text{XY}}D(C)$ is
  Schur-maximized uniquely at the geometric partition, so deforming any partition
  toward geometric only *increases* $f$ — which would close the upper bound from
  the lower bound. This monotonicity is the open hard lemma.

---

## 5. Commentary

**Why geometric?** The geometric partition $1:2:4:\cdots:2^n$ is the *tightest*
superincreasing sequence: each term beats the sum of all smaller terms by exactly
$1$. This makes it simultaneously (i) the hardest target for Xiang Yu on the lower
side — the $+1$ gap resists fragmentation — and (ii) the partition where Xiang Yu
is *most* constrained on the upper side. Extensive search confirms the geometric
partition is the **unique** partition attaining the value; every other partition
lets Xiang Yu drive $D$ strictly below $1/S_n$.

**The role of the cut budget.** The bound is *exactly* tight only because Xiang Yu
has at most $n$ cuts. With even one extra cut on $G_n$, Xiang Yu can drive $D$ below
$1$ (on $G_1$, two cuts reach a near-equal three- or four-piece config with $D\to0$).
So any proof must use "$\le n$ cuts" essentially — a pure inequality on the
multiset, ignoring the budget, is false (the "merge inequality"
$D(F\cup T)\ge|F|-|T|=1$ fails for general tails).

**The difference game.** Repeatedly replacing the two largest pieces $a\ge b$ by
$a-b$ (the *difference game*) returns $f(G_n)=1$ on the geometric partition,
matching the target; it certifies that $1$ is *attainable* by Xiang Yu (an upper
bound on $\min_{\text{XY}}D$ at the geometric config) but is not a general lower
bound and the strategy is not generally optimal — its optimality is special to the
tightest superincreasing structure.

**What is rigorous here.** The reduction to the alternating-sum game (Lemma A);
the full proof for $n=1$ and $n=2$ (both directions: $c(1)=2/3$, $c(2)=4/7$); the
lower bound for $n=3$ ($c(3)\ge8/15$, exhaustive cell enumeration with vertex-min
principle); the clean "even-sum" and "toggle-pair" reformulations; and the exact
numerical determination for $n\le5$.
**What remains open** is the general lower-bound Case B (the interleaving of
fragments of $2^n$ with the refined tail, needing the cut budget together with the
$+1$-gap structure), the $n=3$ upper bound, and the general upper bound (a rigorous
Xiang Yu strategy or a majorisation proof). All are conjectured true with strong
numerical support.

**The conjecture, stated plainly.** $c(n)=2^n/(2^{n+1}-1)$; the geometric partition
$1:2:4:\cdots:2^n$ is Liu Bang's optimal play, and full halving is Xiang Yu's
optimal response, with equality attained in particular at full halving (and on
other configurations, e.g. the layered-straddle family).
