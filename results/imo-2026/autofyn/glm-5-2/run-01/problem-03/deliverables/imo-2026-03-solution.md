# IMO 2026 Problem 3 — Solution

**Status: PARTIAL.** The value $c(n)=2^n/(2^{n+1}-1)$ is *conjectured*
(strongly supported numerically for $n=1,\dots,5$) and is *rigorously proved*
only for $n=1$ (both directions). For general $n$, the lower bound is proved in
Case A and reduced to an open interleaving gap in Case B; the upper bound is
open. Every gap is flagged explicitly. Nothing unproved is presented as
established.

---

## 1. Problem

Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length $1$
and want to divide it between themselves. Liu Bang marks at most $n$ points on
the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked
points are distinct. Then the stick is cut at all marked points, creating a
number of pieces. Afterwards, they take turns claiming any unclaimed piece, with
Liu Bang going first. Each player maximises the total length of their own
pieces. For each $n$, determine the largest value $c$ such that Liu Bang may
guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## 2. Answer

> **Conjecture (strongly confirmed, $n=1..5$; proved for $n=1$):**
> $$c(n)=\frac{2^n}{2^{n+1}-1}.$$
> Equivalently, writing $S_n:=2^{n+1}-1$, the minimax alternating-sum value is
> $D^\star=1/S_n$, and $c(n)=\tfrac12(1+1/S_n)=2^n/S_n$.

| $n$ | $S_n=2^{n+1}-1$ | $D^\star=1/S_n$ | $c(n)=2^n/S_n$ | status |
|---|---|---|---|---|
| 1 | 3  | 1/3   | **2/3**  | proved (both directions) |
| 2 | 7  | 1/7   | 4/7  | numerically confirmed |
| 3 | 15 | 1/15  | 8/15 | numerically confirmed |
| 4 | 31 | 1/31  | 16/31 | numerically confirmed |
| 5 | 63 | 1/63  | 32/63 | numerically confirmed |

The values decrease to $1/2$ as $n\to\infty$.

## 3. Key idea

**Geometric partition.** LB plays the partition $1:2:4:\cdots:2^n$ (rescaled to
total $1$). The total is $S_n=2^{n+1}-1$. This is the natural extremum because
of the **"+1 gap" identity**:
$$2^k = (1+2+\cdots+2^{k-1}) + 1 \qquad\text{for every } k\ge 1. \tag{$\dagger$}$$
Each geometric piece exceeds the sum of *all* smaller geometric pieces by
exactly $1$. In particular, the largest piece $2^n$ exceeds the sum of all the
others ($2^n-1$) by exactly $1$ — the target value $D^\star=1$ (in integer
units). The geometric config is the *tightest* superincreasing sequence:
$2^j=\sum_{i<j}2^i+1$.

**Greedy alternating pick.** Once all cuts are made, the two players pick pieces
alternately (LB first), each taking the largest remaining piece. This greedy
play is optimal for *both* (Lemma A below), and LB's take is
$$\text{LB's take}=\frac{1+D}{2},\quad D=b_1-b_2+b_3-b_4+\cdots$$
the alternating sum of the final pieces sorted descending. So the whole game
reduces to: **LB picks a partition; XY adds $\le n$ cuts; payoff to LB is
$(1+D)/2$. LB maximises the guaranteed $D$, XY minimises it.**

**XY's extremal response.** Against the geometric config, XY's best play is
*full halving*: split every piece $2^j$ into $2^{j-1}+2^{j-1}$, producing
$2^{n-1}(\times2),2^{n-2}(\times2),\dots,1(\times3)$, whose alternating sum is
exactly $1$ (every consecutive pair cancels, leaving a single unit). This
certifies the value $D^\star=1/S_n$ is *achievable* by XY; the conjecture is
that XY can do no better (i.e. $D$ cannot be driven below $1$), and that no LB
config other than geometric does better for LB.

## 4. Rigorous parts

### Lemma A — Greedy is optimal in the alternating item-picking game

**Statement.** Let $v_1\ge v_2\ge\cdots\ge v_m>0$. Two players pick alternately,
player 1 first, each maximising their own total. Then greedy play (always take
the largest remaining item) is a subgame-perfect equilibrium for both; player 1
gets $v_1+v_3+v_5+\cdots$ and player 2 gets $v_2+v_4+\cdots$.

**Proof (strong induction on $m$).** Cases $m\le2$ immediate. For $m\ge3$,
suppose player 1's first pick is $v_j$; write $R_j$ for the remaining multiset.
After player 1 takes $v_j$, player 2 moves first on $R_j$; by the induction
hypothesis (player 2 now in the "first player" role), player 2 gets the
odd-position sum of sorted $R_j$ and player 1 gets the even-position sum. So
player 1's payoff is $v_j + (\text{even-position sum of sorted }R_j)$.

We claim this is maximised at $j=1$. Sort $R_j$: it is
$v_1,\dots,v_{j-1},v_{j+1},\dots,v_m$ (decreasing, $v_j$ removed). Its
even-position elements are:
- if $j=2k+1$ odd: $\{v_2,v_4,\dots,v_{2k}\}\cup\{v_{2k+3},v_{2k+5},\dots\}$;
- if $j=2k$ even: $\{v_2,v_4,\dots,v_{2k-2}\}\cup\{v_{2k+1},v_{2k+3},\dots\}$.

In the odd case $j=2k+1$:
$$\text{payoff}(j)=v_{2k+1}+(v_2+v_4+\cdots+v_{2k})+(v_{2k+3}+v_{2k+5}+\cdots),$$
$$\text{payoff}(1)=v_1+(v_3+\cdots+v_{2k-1})+v_{2k+1}+(v_{2k+3}+\cdots).$$
Subtracting,
$$\text{payoff}(1)-\text{payoff}(j)=(v_1-v_2)+(v_3-v_4)+\cdots+(v_{2k-1}-v_{2k})\ge0,$$
since the sequence is decreasing. The even case $j=2k$ is analogous and gives
the same non-negative telescoping sum. So player 1's optimal first move is
$v_1$ (greedy); the induction hypothesis then forces greedy thereafter. The
same argument with player 2 as first mover on $R_1$ shows greedy is optimal
for player 2. ∎

**Corollary (reduction).** With total length $1$, LB's take is $(1+D)/2$ where
$D$ is the alternating sum of the final sorted pieces; LB's guaranteed payoff is
$\tfrac12(1+\min_{XY}D)$. The game reduces to the alternating-sum minimax:
LB maximises guaranteed $D$, XY minimises $D$.

Two reformulations: (i) $D=1-2\cdot(\text{XY's even-position sum})$, so
minimising $D$ = maximising XY's take; (ii) *parity-integral identity*
$D=\int_0^{b_1}\mathbf{1}_{r(t)\text{ odd}}\,dt$, where $r(t)=\#\{\text{pieces
of size}\ge t\}$.

### Lower bound, $n=1$ — fully proved

Scale to integer units: LB plays $G_1=(1,2)$, total $3$, target $D\ge1$. XY has
1 cut.

- **Cut $2$ into $(a,2-a)$, $0<a<2$.** Pieces $\{1,a,2-a\}$. By symmetry
  assume $a\ge1$; sorted $a,1,2-a$; $D=a-1+(2-a)=1$. (At $a=1$: halving
  $\{1,1,1\}$, $D=1$.)
- **Cut $1$ into $(a,1-a)$, $0<a<1$.** Pieces $\{2,a,1-a\}$; sorted (assume
  $a\ge1/2$) $2,a,1-a$; $D=2-a+(1-a)=3-2a>1$ (since $a<1$).

So $D\ge1$ always, equality iff XY halves the piece $2$. ∎

### Lower bound, Case A — proved for all $n$

**Lemma (Case A).** If XY uses $0$ cuts on the piece $2^n$ (so $2^n$ is intact,
all $\le n$ cuts fall on the tail $(1,\dots,2^{n-1})$), then $D\ge1$.

**Proof.** Then $b_1=2^n$ alone at position 1 (every other piece $\le
2^{n-1}<2^n$). Writing $D_{\text{tail}}$ for the alternating sum of the refined
tail (positions $2,3,\dots$), $D=2^n-D_{\text{tail}}$. Now
$D_{\text{tail}}\le(\text{sum of all tail pieces})=2^n-1$, so
$$D\ge 2^n-(2^n-1)=1.$$
(Case A does not even use the inductive hypothesis — only that the tail mass
is $2^n-1$. It shows XY is *forced* to cut $2^n$ to approach the bound.) ∎

### Upper bound, $n=1$ — fully proved (boundary fixed)

LB makes $\le2$ pieces; largest $L\ge1/2$, rest total $R=1-L\le1/2$. (Single
piece: $L=1,R=0$.) XY has 1 cut. Target $D\le1/3$.

- **$L\ge2/3$:** XY halves $L\to(L/2,L/2)$. Since $L\ge2/3$, $L/2\ge1/3\ge R$;
  sorted $L/2,L/2,R$; $D=L/2-L/2+R=R=1-L\le1/3$. Equality at $L=2/3$.
- **$1/2\le L<2/3$** ($R>1/3$, $2L-1<1/3$): XY shaves a sliver $t$ off $L$ with
  $0<t\le\min(R,2L-1)$ (exists since $R>1/3>0$ and $2L-1\ge0$). Since $t\le R$
  and $t\le2L-1\le L-t$, sorted $(L-t),R,t$; $D=(L-t)-R+t=L-R=2L-1<1/3$.
- **Boundary $L=1/2$ exactly** ($R=1/2$, two equal pieces; the shaving argument
  degenerates since $2L-1=0$): XY cuts one $1/2$-piece into $(a,1/2-a)$ with
  $0<a\le1/4$. Pieces $1/2,1/2-a,a$; sorted $1/2,1/2-a,a$;
  $D=1/2-(1/2-a)+a=2a$. XY picks $a\le1/6$, so $D\le1/3$.

All three branches give $D\le1/3=1/S_1$, equality at $L=2/3$ (geometric) and at
$L=1/2$ with the $(1/3,1/6)$ cut. Combined with $L(1)$: **$c(1)=2/3$ proved.** ∎

## 5. Open gaps (conjectures, not proved)

### Gap 1 — General lower bound, Case B (the interleaving gap)

**Setup.** XY uses $k\ge1$ cuts on $2^n$, producing fragments
$F=(f_1\ge\cdots\ge f_{k+1}>0)$, $\sum f_i=2^n$ (consuming $k$ cuts), and
refines the tail $G_{n-1}$ with $\le n-k\le n-1$ cuts into a multiset $T$ of
total $2^n-1$. The final multiset is the sorted merge of $F$ and $T$.

**Intended induction.** $T$ is a refinement of $G_{n-1}$ by $\le n-1$ cuts, so
$L(n-1)$ gives $D(T)\ge1$ as a standalone game. The intended mechanism: cutting
the dominant $2^n$ sends its fragments to favourable positions *unless* XY
interleaves a fragment between the top ranks of the merge; any such
interleaving consumes a cut, and the remaining $\le n-k$ cuts then face the
smaller geometric instance $G_{n-1}$, to which $L(n-1)$ applies. Equality case:
full halving, giving $D=1$.

**What is settled.** $L(1)$ proved. $L(2)$ verified exhaustively over continuous
cut positions ($D$ piecewise-linear in the two cuts; breakpoints where two
pieces coincide; min $D=1$ uniquely at full halving $\{2,2,1,1,1\}$). Same
check confirms $L(3),L(4),L(5)$.

**Why the general step is open.** The bold inequality
"$D(\text{merge})\ge\sum F-\sum T=1$" is **false** for arbitrary multisets
(counterexample: $F=\{5,5,5,5\}$, $T=\{4,4,4,4\}$; sorted merge
$5,5,5,5,4,4,4,4$ has $D=0<4$). The merge lemma is **true** ($0$ violations in
$20\,000$ trials, $n=2..5$) when $T$ is an *actual* refinement of $G_{n-1}$
(the real inductive hypothesis), but **false** for general tails with $D(T)\ge1$
alone (thousands of violations, min $D\approx0.03$). So the induction must
carry the *dyadic/geometric structure* of the tail (each piece a fragment of
some $2^j$, $j\le n-1$), not merely the numeric bound $D(T)\ge1$.

A clean invariant formalising "the $+1$ gap survives refinement under $\le n$
cuts" — e.g. a parity/rank-function argument via $D=\int\mathbf{1}_{r(t)\text{
odd}}\,dt$ (each cut of size $s$ into $(m,M)$ changes $r(t)$ by $+1$ on $(0,m]$
and $-1$ on $(M,s]$) — was **not** found. This is the **open lower-bound gap**.

### Gap 2 — General upper bound (no rigorous XY strategy for $n\ge2$)

- **Myopic greedy fails** ($36/400$ failures at $n=2$, $67/400$ at $n=3$; on
  $(0.4,0.35,0.25)$ greedy gives $D=0.25>1/7$, optimal "match" gives $0.05$).
- **"Halve-or-match" hybrid** (halve largest $a_1$ if $a_1\ge2a_2$, else match
  $a_1$ to $a_2$) reduces the config by one piece per cut and gives exactly
  $1/S_n$ on geometric. But the scale-invariant induction $V(C,m)\le T/S_m$
  fails for $m\ge2$: the per-step reduction $\max(a_1,2a_2)\ge2T/(m+2)$, and
  $2T/(m+2)<T\cdot2^m/S_m$ for $m\ge2$; the "flat" regime (both $a_1$ and
  $a_2$ below their sufficient-condition thresholds) is where it breaks.
- **Hall/pairing** (pair pieces into cancelling equal-consecutive pairs leaving
  a leftover $\le1/S_n$) is not forced: tested pairings leave a leftover
  exceeding $1/S_n$ on some random configs for $n\ge3$ ($n=3$: $0.0757>1/15$;
  $n=4$: $0.0407>1/31$; $n=5$: $0.0228>1/63$).
- **Majorisation/smoothing (most promising, unproved).** Numerics: the function
  $f(C)=\text{XY's optimal }D\text{ against LB partition }C$ appears
  Schur-maximised uniquely at the geometric config (for $n=2,3$, over
  $200$–$800$ random configs the ratio $f(C)/(1/S_n)\le1$, equality only at
  geometric). A smoothing lemma (every LB partition deformable toward geometric
  while only *increasing* $f$) would yield the upper bound from
  $f(\text{geometric})=1/S_n$. This monotonicity is the conjectured but
  **unproved** heart of the upper bound.

## 6. Numerical evidence

A continuous optimal-XY search was run for $n=1..5$. The candidate cut set
$\{\text{fragment}=\text{existing piece}\}\cup\{\text{fragment}=\text{half a
piece}\}$ contains every breakpoint at which the sorted order (hence the
piecewise-linear form $D$) changes slope, so the search returns the exact
piecewise-linear minimum of $D$. This is a *numerical certificate*, not a proof
step.

| $n$ | $\min_{XY}D$ (search) | $1/S_n$ | attaining LB partition |
|---|---|---|---|
| 1 | 1/3  | 1/3  | $(1/3,2/3)$ |
| 2 | 1/7  | 1/7  | $(1/7,2/7,4/7)$ |
| 3 | 1/15 | 1/15 | $(1/15,2/15,4/15,8/15)$ |
| 4 | 1/31 | 1/31 | geometric |
| 5 | 1/63 | 1/63 | geometric |

In every case the minimum is attained *uniquely* by LB = geometric and XY = full
halving. Non-geometric LB configs were searched on a grid ($n=1,2,3$) with
full-lookahead optimal XY: the max guaranteed $D$ is attained *uniquely* at the
geometric config; every other config lets XY drive $D$ strictly below $1/S_n$
(often to $0$). The conjecture is not contradicted.

## 7. Commentary

**Why the geometric config is the natural extremum.** The "+1 gap" identity
$(\dagger)$ says the geometric partition $1:2:4:\cdots:2^n$ is the *tightest*
superincreasing sequence: each piece exceeds the sum of all smaller pieces by
exactly $1$ (the target). Any "looser" superincreasing config (e.g.
$\{5.50,1.99,1.02\}$) has gaps $>1$, and XY can exploit the slack to drive $D$
*below* the difference-game value; the geometric config has *no slack*, which
is exactly why it is hardest for XY and optimal for LB. Numerics confirm the
guaranteed $D$ is maximised *uniquely* at the geometric config.

**The difference-game insight.** Define the *difference game* $f(C)$ by
repeatedly replacing the two largest $a\ge b$ by $a-b$ (ties removed for free).
Then $f(G_n)=1$ for all $n$: matching $2^n\to2^{n-1}$ reduces $G_n$ to $G_{n-1}$
in one cut, so $f(G_n)=f(G_{n-1})=\cdots=1$. Since the match strategy is a legal
XY strategy, $f(G_n)=1$ certifies $\min_{XY}D(G_n)\le1$ (an *upper* bound on
XY's optimum, i.e. the value is achievable). But $f$ is **not** a general lower
bound on $\min_{XY}D$ (e.g. $\{0.7,0.3\}$: $\min D=0.3<f=0.4$), and match is
**not** generally optimal (superincreasing $\{5.50,1.99,1.02\}$ admits
$D\approx0.97<f\approx2.49$). The co-optimality of match *on the geometric
config specifically* is the still-unproved crux of the lower bound.

**Why the merge lemma needs dyadic structure.** The natural inductive step
splits the refined config into $F$ (fragments of $2^n$, sum $2^n=S_{n-1}+1$) and
$T$ (refinement of $G_{n-1}$, sum $S_{n-1}$, $D(T)\ge1$ by $L(n-1)$), and needs
$D(\text{merge of }F,T)\ge1$. This holds ($0$ violations / $20\,000$ trials,
$n=2..5$) when $T$ is an *actual* refinement of $G_{n-1}$, but **fails** for
general tails with $D(T)\ge1$ alone (thousands of violations, min
$D\approx0.03$). The lesson: the induction cannot rest on the numeric bound
$D(T)\ge1$; it must carry the dyadic *structure* of $T$ (each piece a fragment
of some $2^j$, $j\le n-1$). A clean structural invariant capturing "the $+1$
gap survives refinement under $\le n$ cuts" was not found — this is the precise
obstruction.

**Why myopic greedy fails (upper bound).** Greedy "cut to minimise $D$
immediately" fails on $36/400$ ($n=2$) and $67/400$ ($n=3$) random configs.
On $(0.4,0.35,0.25)$, greedy-halve gives $D=0.25>1/7$, whereas the optimal
"match" (split $0.4\to0.35+0.05$, then $0.25\to0.125+0.125$) gives $D=0.05$.
The upper bound requires genuine multi-step planning / a structural argument,
not one-step greed. The "halve-or-match" hybrid is locally sensible and gives
exactly $1/S_n$ on geometric, but its scale-invariant induction fails in the
"flat" regime for $m\ge2$.

**Honest assessment of completeness.** This is a **partial** solution. What is
proved: the greedy-pick reduction; $c(1)=2/3$ in full (lower and upper); the
lower-bound Case A for all $n$. What is conjectured (strongly supported
numerically, not proved): $c(n)=2^n/(2^{n+1}-1)$ for all $n$. The two open gaps
are (a) the general lower-bound Case B (the interleaving of fragments of $2^n$
with the refined tail, needing the dyadic structure of the tail plus the cut
budget $\le n$ and $(\dagger)$), and (b) the general upper bound (a rigorous XY
strategy or a majorisation/smoothing proof that the geometric config
Schur-maximises XY's optimal $D$). The general case is a **conjecture**
supported by numerical evidence, not a complete proof.
