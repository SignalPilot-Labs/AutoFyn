## Status
partial

## Approaches tried
- `layer-cake-parity-reframing` (round 4, new — the plateau-break attempt).
  Built the threshold/layer-cake reformulation of the lower-bound half of
  `c(n)` from scratch (a framing that never peels a maximum element, unlike
  the two stuck peel-based approaches). Fully proved, from first
  principles: the Layer-cake identity (`AltSum(X)=∫1[N_X(t) odd]dt`), the
  per-piece additivity of the threshold-count function `N`, the exact
  equivalence of `T(n)` to an `AltSum≥1/(2^{n+1}-1)` budget statement, and
  a single-cut marginal-effect formula. Numerically validated the
  reformulation reproduces the known target at `n=0,1,2,3` (exact rational
  arithmetic, not floating point). Then, following the outline's explicit
  mandate to verify (not assume) that the "additive over pieces/thresholds"
  intuition survives contact with a real multi-cut example, constructed an
  **exact, fully rigorous counterexample** (not a numeric spot-check but a
  hand-verified rational computation) showing that a single fixed cut's
  marginal contribution to `AltSum` can have **opposite sign** depending on
  which other cuts have already been made elsewhere on the stick. This
  refutes, rigorously rather than just diagnostically, the specific
  mechanism the outline proposed for closing steps 4–5 (a "structure-aware
  per-cut bound" depending only on the cut's own piece and its geometric
  neighbors) — the true dependence is genuinely joint across all cuts, not
  decomposable into independent per-cut terms. `T(n)` for `n≥3` remains
  open under this framing; the obstruction is now a *proved* coupling
  phenomenon (analogous in spirit, but not mechanism, to the peel-based
  approaches' Proposition C) rather than an untested hope.

## Current best

**Setup.** Throughout, for a finite multiset $X=\{x_1\ge x_2\ge\cdots\ge x_k\}$
of positive reals (sorted descending) write
$$\mathrm{OddSum}(X)=\sum_{i\text{ odd}}x_i,\quad \mathrm{EvenSum}(X)=\sum_{i\text{ even}}x_i,\quad \mathrm{AltSum}(X)=\mathrm{OddSum}(X)-\mathrm{EvenSum}(X).$$
Since $\mathrm{OddSum}(X)+\mathrm{EvenSum}(X)=\mathrm{sum}(X)$ definitionally,
$$\mathrm{OddSum}(X)=\tfrac12\bigl(\mathrm{sum}(X)+\mathrm{AltSum}(X)\bigr).\tag{$\ast$}$$
By the certified Reduction Lemma (`lemmas/reduction-to-multiset-minimax.md`)
and Greedy-Optimality Lemma (`lemmas/greedy-optimality-oddsum.md`), the
lower-bound claim $T(n)$ for LB's geometric partition
$p_i=2^{n+1-i}/D$ ($i=1,\dots,n+1$, $D:=2^{n+1}-1$) reads:
$$\mathrm{OddSum}(M)\ge c(n)=\frac{2^n}{D}\quad\text{for every multiset }M\text{ obtained by refining }(p_1,\dots,p_{n+1})\text{ with }\textstyle\sum m_i\le n\text{ cuts.}$$
Since $\mathrm{sum}(M)=\sum p_i=1$ always, $(\ast)$ makes this exactly
equivalent (see the Corollary below) to a statement about $\mathrm{AltSum}$.

### Lemma 1 (Layer-cake identity)

**Statement.** For any finite multiset $X=\{x_1\ge\cdots\ge x_k\}$ of
positive reals, define $N_X(t):=\#\{i:x_i\ge t\}$ for $t>0$. Then
$$\mathrm{AltSum}(X)=\int_0^\infty \mathbf 1[N_X(t)\text{ is odd}]\,dt.$$

**Proof.** Each $x_i=\int_0^\infty \mathbf 1[t\le x_i]\,dt$ (the integral
of the indicator of $[0,x_i]$). Hence, since the sum defining $\mathrm{AltSum}$
is finite, we may swap sum and integral:
$$\mathrm{AltSum}(X)=\sum_{i=1}^k(-1)^{i+1}x_i=\sum_{i=1}^k(-1)^{i+1}\int_0^\infty\mathbf 1[t\le x_i]\,dt=\int_0^\infty\Bigl(\sum_{i=1}^k(-1)^{i+1}\mathbf 1[t\le x_i]\Bigr)dt.$$
Fix $t>0$. Because $X$ is sorted descending, $\{i:x_i\ge t\}$ is exactly a
prefix $\{1,\dots,N_X(t)\}$: if $x_i\ge t$ and $j<i$ then $x_j\ge x_i\ge t$.
So the inner sum is $\sum_{i=1}^{N_X(t)}(-1)^{i+1}$, which telescopes to $1$
if $N_X(t)$ is odd and $0$ if $N_X(t)$ is even (partial sums of $1,0,1,0,\dots$).
Substituting gives the claim. (The integral has bounded support since
$N_X(t)=0$ for $t>x_1$, so all manipulations are over a finite interval —
no convergence issues.) $\blacksquare$

**Independent numeric check.** Verified to high precision on 5 random
multisets (sizes 2–5, values in $(0,5)$) by direct fine-grid numerical
integration against the closed-form $\mathrm{AltSum}$; agreement to
discretization error in every case (also independently reproduced by the
outline-reviewer this round).

### Lemma 2 (Per-piece additivity of the threshold count)

**Statement.** Let $p_1,\dots,p_k>0$ sum to $1$, and let a refinement split
each $p_i$ into a multiset $F_i$ of positive reals with $\mathrm{sum}(F_i)=p_i$
(so $|F_i|=m_i+1$ for some $m_i\ge0$). Let $M=F_1\cup\cdots\cup F_k$ (multiset
union). Then for every $t>0$,
$$N_M(t)=\sum_{i=1}^k n_i(t),\qquad n_i(t):=\#\{y\in F_i:y\ge t\},$$
and $n_i(t)=0$ whenever $t>p_i$.

**Proof.** Multiset union is disjoint concatenation, so counting elements
$\ge t$ across $M$ is exactly the sum of the counts within each $F_i$,
giving the additivity. For the second claim: every element $y\in F_i$
satisfies $0<y\le p_i$ (each part of a partition of $p_i$ into positive
parts is at most the total $p_i$, with equality only when $m_i=0$), so no
element of $F_i$ can be $\ge t$ when $t>p_i$. $\blacksquare$

### Corollary (exact reduction of $T(n)$ to an AltSum-budget statement)

Combining $(\ast)$, Lemma 1, and Lemma 2, with $\mathrm{sum}(M)=1$ fixed:
$$\mathrm{OddSum}(M)=\frac12\Bigl(1+\int_0^\infty\mathbf 1\Bigl[\textstyle\sum_i n_i(t)\text{ odd}\Bigr]dt\Bigr).$$
Hence $T(n)$ (LB's geometric partition guarantees $\mathrm{OddSum}(M)\ge 2^n/D$
against every refinement using $\le n$ total cuts) is **exactly equivalent**
(an if-and-only-if restatement, not a relaxation) to:
$$\int_0^\infty \mathbf 1\Bigl[\textstyle\sum_{i=1}^{n+1} n_i(t)\text{ is odd}\Bigr]dt\ \ge\ \frac1D\qquad\text{for every }(n_i)\text{ arising from }\textstyle\sum m_i\le n\text{ cuts.}\tag{T$'$(n)}$$
This equivalence is exact because $(\ast)$, Lemma 1, and Lemma 2 are all
identities (no inequality is used to derive it), so proving $\mathrm{T}'(n)$
for every admissible refinement is both necessary and sufficient for
$T(n)$. No information about XY's move is discarded in this step — this
directly answers the outline's mandated check (step 3's claimed
equivalence, not a relaxation).

**Numeric sanity check (exact rational arithmetic, not floating point).**
For $n=0,1,2,3$ the baseline (no cuts) and known optimal responses were
recomputed via $\mathrm{T}'(n)$ and checked against the previously
certified values of $c(n)$:
- $n=0$: baseline $\mathrm{AltSum}=1=1/D$ ($D=1$): matches $c(0)=1$ with $0$
  cuts, consistent with the already-certified $T(0)$.
- $n=1$: baseline $\mathrm{AltSum}=1/3=1/D$ ($D=3$): matches $c(1)=2/3$
  with $0$ cuts used — consistent with the certified fact (Element Bound
  family) that XY's best response to the $n=1$ geometric partition is to
  do nothing.
- $n=2$: baseline $\mathrm{AltSum}=3/7 > 1/7=$ target; bisecting only $p_1$
  (one of the two available cuts) into $2/7,2/7$ gives exactly
  $\mathrm{AltSum}=1/7$, matching the certified $T(2)$ value exactly.
- $n=3$: baseline $\mathrm{AltSum}=1/3$, target $1/15$; bisecting $p_1$
  alone gives $\mathrm{AltSum}=1/5>1/15$ (does not reach the target with
  one cut, consistent with $T(3)$ not being closeable by a single cut);
  bisecting both $p_1$ and $p_2$ (two of the three available cuts) gives
  exactly $\mathrm{AltSum}=1/15$, matching the target. (All values computed
  in exact `Fraction` arithmetic; see the worked computation in the
  Coupling Obstruction below for the same numbers with full derivation
  shown.)

These checks confirm $\mathrm{T}'(n)$ correctly reproduces every previously
certified value of $c(n)$ it can be compared against, with no discrepancy —
the reformulation is a faithful restatement of the original problem, not an
accidentally-weaker relaxation.

### Lemma 3 (Single-cut marginal-effect formula)

**Statement.** Suppose a currently-whole piece of length $p$ (contributing
$n(t)=\mathbf 1[0<t\le p]$ to the running threshold-count function) is cut
into two fragments $a\ge b>0$ with $a+b=p$. The new contribution is
$$n'(t)=\begin{cases}2,&0<t\le b\\ 1,& b<t\le a\\ 0,& a<t\end{cases}$$
so $\Delta n(t):=n'(t)-n(t)$ equals $+1$ on $(0,b]$, $0$ on $(b,a]$, $-1$
on $(a,p]$, and $0$ elsewhere. In particular the two nonzero regions
$(0,b]$ and $(a,p]$ have **equal length** $b=p-a$.

**Proof.** Direct case computation: for $t\le b$ both $a,b\ge t$ (since
$b\le a$), giving $n'=2$ versus the old $n=1$ (as $t\le b\le p$), so
$\Delta=+1$. For $b<t\le a$, only $a\ge t$, giving $n'=1=n$ (since $t\le a\le p$),
so $\Delta=0$. For $t>a$, neither fragment is $\ge t$, giving $n'=0$;
if additionally $t\le p$ then $n=1$, so $\Delta=-1$ on $(a,p]$; if $t>p$
then $n=0=n'$ too. The interval lengths are $|(0,b]|=b$ and $|(a,p]|=p-a=b$,
equal by $a+b=p$. $\blacksquare$

**Consequence (marginal $\Delta\mathrm{AltSum}$ of one cut).** If, at the
moment this cut is made, the running total threshold count from *all other*
current fragments is $N_{\text{rest}}(t)$, then flipping this one piece's
own contribution by $\Delta n(t)=\pm1$ flips the parity of the *total*
count $N(t)=N_{\text{rest}}(t)+n(t)$ on exactly $(0,b]\cup(a,p]$ (and leaves
it unchanged elsewhere), so by Lemma 1
$$\Delta\,\mathrm{AltSum}=\int_0^b \sigma(t)\,dt+\int_a^{p}\sigma(t)\,dt,\qquad \sigma(t):=\begin{cases}+1,&N(t)\text{ even before the cut}\\-1,&N(t)\text{ odd before the cut.}\end{cases}$$

### Proposition (Coupling Obstruction — no fixed sign for a cut's marginal effect)

**Statement.** There exist a refinement scenario and a single admissible
cut such that this cut's marginal $\Delta\mathrm{AltSum}$ (as given by
Lemma 3's consequence) is strictly positive if applied to one background
configuration, and strictly negative — of exactly the same magnitude — if
applied after a different, specific other cut has already been made
elsewhere on the stick. Consequently **no bound on a cut's marginal effect
that depends only on the cut's own piece (and its fixed neighbors in the
original geometric sequence), independent of which other cuts have been
made, can be correct** — any valid budget-to-measure bound must be a joint
function of the whole configuration of cuts, not a sum of independently
bounded per-cut terms.

**Proof (exact worked example, $n=3$, $D=15$).** LB's geometric partition
is $p=(p_1,p_2,p_3,p_4)=(8/15,\,4/15,\,2/15,\,1/15)$, sum $=1$,
$\mathrm{AltSum}(p)=8/15-4/15+2/15-1/15=5/15=1/3$ (target is $1/15$).

Consider the cut "bisect $p_2$": split $4/15$ into $(2/15,2/15)$.

*Applied alone* (all other pieces untouched, so $F_1=\{8/15\}$, $F_3=\{2/15\}$,
$F_4=\{1/15\}$): the resulting multiset is
$\{8/15,\ 2/15,\ 2/15,\ 2/15,\ 1/15\}$ (sorted descending: $8/15\ge 2/15=2/15=2/15\ge1/15$;
ties broken arbitrarily, $\mathrm{AltSum}$ is unaffected by which tied copy
gets which rank since the values are equal). Its $\mathrm{AltSum}$ is
$8/15-2/15+2/15-2/15+1/15=7/15$. So $\Delta\mathrm{AltSum}=7/15-1/3=7/15-5/15=+2/15$
— this cut, applied alone, **increases** $\mathrm{AltSum}$ (moves away from
XY's goal, toward LB).

*Applied after first bisecting $p_1$* (split $8/15$ into $(4/15,4/15)$;
this alone gives multiset $\{4/15,4/15,4/15,2/15,1/15\}$ — note $p_2=4/15$
ties with the two new fragments — with
$\mathrm{AltSum}=4/15-4/15+4/15-2/15+1/15=3/15=1/5$): now additionally bisect
$p_2=4/15$ into $(2/15,2/15)$. The resulting multiset is
$\{4/15,4/15,2/15,2/15,2/15,1/15\}$, sorted descending, with
$$\mathrm{AltSum}=4/15-4/15+2/15-2/15+2/15-1/15=1/15.$$
So the marginal effect of the *same* bisect-$p_2$ cut, applied in this
context, is $\Delta\mathrm{AltSum}=1/15-1/5=1/15-3/15=-2/15$ — it now
**decreases** $\mathrm{AltSum}$, by exactly the same magnitude as before but
with the opposite sign.

Both computations use only exact rational arithmetic (denominator $15$
throughout) and are independently verifiable by direct summation of the
sorted lists above; both were additionally cross-checked by a symbolic
`Fraction`-arithmetic computation. This exhibits the required example:
identical cut, opposite-sign marginal effect, magnitude $2/15$ in both
directions, depending solely on which other cut (bisecting $p_1$) has
already been made. $\blacksquare$

**Consequence for the proof strategy.** The outline's proposed mechanism
for steps 4–5 (bound $\sum|\Delta\mathrm{AltSum}|$ over the $\le n$ cuts by
a *per-cut* term controlled by the local dyadic ratio to the cut's own
neighboring geometric values, then sum a geometric series) is thereby shown
to be **not directly viable**: the sign — not just the magnitude — of a
cut's contribution depends on the *global* configuration of all other
cuts through $\sigma(t)$ in Lemma 3's consequence, specifically through the
parity of $N_{\text{rest}}(t)$ on the cut's own affected interval, which is
controlled by *other pieces'* fragmentation, not by the cut's own piece or
its fixed geometric neighbors alone. This is the layer-cake framing's
concrete analogue of the coupling that makes the peel-based approaches'
Proposition C circular: eliminating the merged-rank information (as this
framing does) removes *some* of the coupling (there is no longer an
asymmetric "top piece vs. rest" distinction — every piece plays a
structurally identical role, which was the framing's original motivation
and genuinely does hold, see Lemma 2) but not *all* of it — a residual,
order-dependent parity coupling between simultaneously-present cuts on
different pieces survives, and this is the specific new obstruction this
approach has now located and proved.

**What remains open.** A correct budget-to-measure bound (closing $T(n)$
for $n\ge3$ under this framing) must therefore either (a) bound the total
signed effect of $\le n$ cuts *jointly* (e.g. via a potential/telescoping
argument over the actual sequence of thresholds visited, not per-cut), or
(b) restrict to an order/configuration in which the sign is provably
determined (e.g. an argument by contradiction: assume a hypothetical
optimal XY configuration and derive that the aggregate, not cut-by-cut,
effect is bounded) — neither has been carried out. This is a precise,
proved diagnosis of why the natural "additive per-cut budget" plan fails,
parallel in status (a genuine obstruction, not a vague unproved gap) to
Proposition C for the peel-based approaches, but structurally different in
mechanism (order-dependent sign flip from cross-piece parity coupling,
rather than a self-referential peel reduction).

## Full proof
(none — Status is `partial`; the reduction (Lemma 1, Lemma 2, and the
Corollary) is fully proved and exact, but the general budget-to-measure
bound needed to close $T(n)$ for $n\ge3$ remains open, with the specific
obstruction to the outline's proposed mechanism now rigorously proved
above rather than left as an untested hope.)

## Promotable lemmas

- **Lemma 1 (Layer-cake identity).** $\mathrm{AltSum}(X)=\int_0^\infty
  \mathbf1[N_X(t)\text{ odd}]\,dt$ for any finite multiset of positive
  reals. Proved in full above by a swap-sum-and-integral + telescoping
  argument; elementary, general-purpose, reusable for any alternating-claim
  problem, not specific to the geometric partition.
- **Lemma 2 (Per-piece additivity of the threshold count).**
  $N_M(t)=\sum_i n_i(t)$ for any refinement of any partition into
  independently-split pieces, with $n_i(t)=0$ for $t>p_i$. Proved in full
  above; elementary but reusable — gives a clean per-piece decomposition of
  the layer-cake count for any "split each piece independently" game.
- **Lemma 3 (Single-cut marginal-effect formula).** Bisecting a whole piece
  $p$ into $a\ge b$ changes its threshold-count contribution by exactly
  $+1$ on $(0,b]$ and $-1$ on $(a,p]$ (equal-length intervals), giving the
  exact formula for a single cut's marginal $\Delta\mathrm{AltSum}$ in
  terms of the background parity function. Proved in full above by direct
  case computation.
- **Corollary (exact $T(n)\Leftrightarrow \mathrm{T}'(n)$ equivalence).**
  Reduces the geometric-partition lower bound to a threshold-parity-measure
  statement, with no information loss (proved as an identity chain, not an
  inequality). Reusable by any future attempt at this framing.
- **Proposition (Coupling Obstruction).** A worked, exact-rational
  counterexample proving that a single fixed cut's marginal
  $\Delta\mathrm{AltSum}$ can have strictly opposite sign depending on
  other cuts made elsewhere ($n=3$, cut = "bisect $p_2$": $+2/15$ alone vs.
  $-2/15$ after bisecting $p_1$). This is a genuine negative result: it
  rules out (not just "has not yet found") any proof mechanism for the
  layer-cake framing's remaining gap that assigns cuts independent,
  piece-local bounds. Reusable as a documented dead end for this framing,
  analogous to Proposition C for the peel-based framing.
