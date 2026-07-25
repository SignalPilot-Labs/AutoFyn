# Monotonicity Reduction Lemma and the Unified Threshold-Pair-Peeling Lemma

Certified round 13, from `approaches/self-similar-induction-on-n.md`,
"Round 13: Monotonicity Reduction ... and the Unified Threshold-Pair-Peeling
Lemma" section. Independently re-derived and re-verified by the
proof-reviewer with fresh exact-`Fraction` scripts (not the builder's own
scripts), thousands of trials per fact, zero violations. Both results are
reusable independent of whether the open $\mathrm{GT}(m)$, $m\ge4$ gap
below ever closes.

## Monotonicity Reduction Lemma

**Statement.** Fix $m\ge0$, a fixed count $k\ge0$, and a fixed finite
multiset $T$ of positive reals. Let $D$ be any finite multiset of positive
reals with $|D|=k$ and $\max(D)\le2^m$, and let $S_0\le\mathrm{sum}(D)$ be
any target value with $S_0>0$. Then there exists $D'$ with $|D'|=k$,
$\max(D')\le\max(D)$, $\mathrm{sum}(D')=S_0$, and
$$\mathrm{OddSum}(D\cup T)\ \ge\ \mathrm{OddSum}(D'\cup T).$$

**Proof.** By the certified Elementwise Monotonicity Lemma
(`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`), for
any fixed finite multiset $N$, $x\mapsto\mathrm{OddSum}(N\cup\{x\})$ is
non-decreasing on $(0,\infty)$. Drain $D$'s coordinates one at a time
(always keeping every coordinate $>0$; e.g. repeatedly shrink the current
largest coordinate toward $0$, moving to the next once negligible) until
the cumulative reduction equals $\mathrm{sum}(D)-S_0$; this is always
possible by the intermediate value theorem, since the running total is a
continuous, strictly decreasing function of the amount drained, ranging
from $\mathrm{sum}(D)$ down to $0^+$. At each single-coordinate shrink
step, applying the Elementwise Monotonicity Lemma with $N$ = the fixed
rest of $D\cup T$ shows $\mathrm{OddSum}$ is non-increasing; chaining over
all steps gives $\mathrm{OddSum}(D\cup T)\ge\mathrm{OddSum}(D'\cup T)$.
Coordinates only ever decrease, so $\max(D')\le\max(D)$. $\blacksquare$

**Reviewer re-verification** (fresh script, exact `Fraction`): 2554 random
trials, $m=1,\dots,6$, $k=1,\dots,m+1$, $D$ random with
$\mathrm{sum}(D)\ge2^m=S_0$, drained via the greedy largest-coordinate
construction: zero violations of $\mathrm{OddSum}(D\cup T)\ge
\mathrm{OddSum}(D'\cup T)$ or of $\max(D')\le\max(D)$.

**Corollary used downstream (scope, stated precisely).** If
$\mathrm{GT}(m)$ (the General Peeling Theorem,
`lemmas/general-peeling-theorem-and-window-endpoint-closure.md`) is known
for the single boundary value $\mathrm{sum}(D)=2^m$ exactly (already
inside the certified safe zone $\mathrm{sum}(D)<3\cdot2^{m-1}$ for every
$m\ge0$, since $2^m<3\cdot2^{m-1}\iff2<3$), then applying this Lemma with
$S_0=2^m$, $T=\Gamma_{m-1}$ extends $\mathrm{GT}(m)$ to **every**
$D$ with $|D|\le m+1$, $\max(D)\le2^m$, and $\mathrm{sum}(D)\ge2^m$ — with
no upper bound on $\mathrm{sum}(D)$. Concretely, for $m=0,1,2,3$ (where
the certified safe-zone $\mathrm{GT}(m)$ already covers $\mathrm{sum}(D)=
2^m$ as an ordinary interior instance), this **removes in full the
reviewer's round-12 scope restriction** (the "$p\ge3$"/large-sum caveat)
on $\mathrm{GT}(m)$: combined with the certified safe-zone statement
(which covers $\mathrm{sum}(D)<3\cdot2^{m-1}$, in particular every
$\mathrm{sum}(D)<2^m$), every $\mathrm{sum}(D)\ge0$ is now covered for
$m=0,1,2,3$. For $m\ge4$, $\mathrm{GT}(m)$ itself (even at the single
boundary value) is not yet established, so the corollary here is
**conditional and does not by itself extend $\mathrm{GT}(m)$ to
$m\ge4$** — it only guarantees that *whenever* a future round proves the
bounded/boundary-sum case for some $m\ge4$, the large-sum case follows
automatically at no extra cost.

## Rank-Shift Identity

**Statement.** For any finite multiset $N$ sorted descending
$x_1\ge\cdots\ge x_n$ and any $0\le q\le n$, writing
$\mathrm{top}_q=(x_1,\dots,x_q)$, $\mathrm{rest}_q=(x_{q+1},\dots,x_n)$:
$$\mathrm{OddSum}(N)=\Bigl(\sum_{i\text{ odd},\,i\le q}x_i\Bigr)+
\begin{cases}\mathrm{OddSum}(\mathrm{rest}_q)&q\text{ even}\\
\mathrm{EvenSum}(\mathrm{rest}_q)&q\text{ odd.}\end{cases}$$

**Proof.** $\mathrm{rest}_q$'s local rank $j$ corresponds to $N$'s global
rank $q+j$; these agree in parity iff $q$ is even. Splitting $N$'s
odd-global-rank terms into (odd ranks $\le q$) and (odd ranks $>q$,
reindexed via the parity relation above) gives the displayed identity.
$\blacksquare$

**Reviewer re-verification** (fresh script, exact `Fraction`): 18000
random trials, $n=1,\dots,12$, all $q\in\{0,\dots,n\}$: zero violations.

## Unified Threshold-Pair-Peeling Lemma

**Setting.** $M=D\cup\Gamma_{k-1}$, $D$ sorted descending,
$q:=\#\{a_i\in D:a_i>2^{k-1}\}$ (so the top $q$ elements of $M$ are
exactly $D$'s $q$ elements exceeding $2^{k-1}$), $R:=D\setminus
\mathrm{top}_q$ (so every element of $R$ and of $\Gamma_{k-1}$ is
$\le2^{k-1}$), $\sigma_q:=\sum_{i\text{ odd},i\le q}a_i$.

**Statement ($q\ge2$ closes unconditionally).** For any $q\ge2$ (either
parity), any $k\ge1$, and any finite multiset $R$ of positive reals
$\le2^{k-1}$ (no bound on $|R|$ or $\mathrm{sum}(R)$):
$$\mathrm{OddSum}(M)>2^k.$$

**Proof.** By the Rank-Shift Identity: if $q$ is even,
$\mathrm{OddSum}(M)=\sigma_q+\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge
\sigma_q+2^{k-1}$ (the last step by Global-max Peeling,
`lemmas/dominant-piece-lower-bound.md`, on $\max(R\cup\Gamma_{k-1})=
2^{k-1}$, plus $\mathrm{EvenSum}\ge0$); since each of the $q/2$
odd-ranked top elements exceeds $2^{k-1}$, $\sigma_q>2^{k-1}\cdot q/2$, so
$\mathrm{OddSum}(M)>2^{k-1}(q/2+1)\ge2^k$ for $q\ge2$. If $q$ is odd,
$\mathrm{OddSum}(M)=\sigma_q+\mathrm{EvenSum}(R\cup\Gamma_{k-1})\ge
\sigma_q>2^{k-1}\cdot(q+1)/2\ge2^k$ for $q\ge3$ (the only odd values
$\ge2$). $\blacksquare$ In both parities the bound uses only $\sigma_q$
and $2^{k-1}$, never $R$'s count/sum/structure beyond the standing cap
$\le2^{k-1}$.

**Reviewer re-verification** (fresh script, exact `Fraction`, adversarial):
12600 random trials, $k=1,\dots,7$, $q=2,\dots,7$, with $R$'s count and
sum deliberately stressed (up to 10 extra elements, sum up to
$\approx2^{k-1}\cdot97$): zero violations of $\mathrm{OddSum}(M)>2^k$.

**$q\in\{0,1\}$ (not closed by this Lemma; recorded here for completeness,
matching the approach file).**
- $q=0$: $\mathrm{OddSum}(M)=2^{k-1}+\mathrm{EvenSum}(D\cup\Gamma_{k-2})$
  — no progress, descends one level with the same target.
- $q=1$: $\mathrm{OddSum}(M)=a_1+\mathrm{OddSum}(R\cup\Gamma_{k-2})$
  (Companion Peeling) — recurses into a $\mathrm{GT}(k-1)$-shaped
  instance on $R$.

## Scope note: what this does and does not close

These two results are general-purpose and fully proved; they **do not by
themselves establish $\mathrm{GT}(m)$ for $m\ge4$**. Two sub-cases remain
open (see `approaches/self-similar-induction-on-n.md`, round-13 section,
for the full honest diagnosis, not repeated here): (i) the $q=1$
sub-case when the running excess $e:=|D|-(k+1)\ge1$, whose target
$2^k-a_1$ is not yet reduced to a previously-closed family; (ii) the
"small-sum" regime of $\mathrm{GT}(k-1)$ itself (needed even at $e=0$),
i.e. $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge\mathrm{sum}(R)$ for
$\mathrm{sum}(R)<2^{k-1}$, not covered by the boundary-value family
studied here. $\mathrm{GT}(m)$ for $m\ge4$, and hence gap (a) of the
shared Branch-I.A window for $\ell\ge5$, remains open.
