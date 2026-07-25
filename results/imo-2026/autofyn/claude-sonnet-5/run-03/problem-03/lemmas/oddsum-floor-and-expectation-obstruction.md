# OddSum Floor Lemma and the Expectation Obstruction Theorem

Certified round 12, from `approaches/structured-randomization-upper-
bound.md`. Independently re-verified by the proof-reviewer (elementary
algebra re-derived from scratch; matches exactly).

## OddSum Floor Lemma (general-purpose)

**Statement.** For every nonempty finite multiset $M$ of positive reals,
$\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$.

**Proof.** Sort $M$ descending $x_1\ge\cdots\ge x_k$.
$\mathrm{OddSum}(M)-\mathrm{EvenSum}(M)=(x_1-x_2)+(x_3-x_4)+\cdots(+x_k
\text{ if }k\text{ odd})\ge0$ (sorted descending). Since
$\mathrm{OddSum}(M)+\mathrm{EvenSum}(M)=\mathrm{sum}(M)$,
$\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$. $\blacksquare$ Applied to any
legal XY response on a partition summing to $1$: $\mathrm{OddSum}\ge
\tfrac12$ always, for every $p$ and every response.

## Expectation Obstruction Theorem

**Statement.** Fix $\delta,\varepsilon\in(0,\tfrac12)$ independent of
$n$. Suppose a randomization scheme assigns, at every balanced-region $p$
(of every $n$), a finite candidate set $\mathcal R(p)$ of legal XY
responses and a distribution $\mu_p$ with
$\mu_p(\{r\in\mathcal R(p):\mathrm{OddSum}(r)\ge\tfrac12+\delta\})\ge
\varepsilon$ for every such $p$. Then for every $n$ with $2^{n+1}-1>
1/(2\delta\varepsilon)$, $\mathbb E_{\mu_p}[\mathrm{OddSum}]>c(n)$ for
every balanced-region $p$ of that $n$ — the expectation argument
$V(p)\le\mathbb E_{\mu_p}[\mathrm{OddSum}]\le c(n)$ cannot certify the
upper bound at that $n$ via this scheme, at any point.

**Proof.** Split $\mathcal R(p)$'s mass into "mediocre" (weight $\ge
\varepsilon$, each $\mathrm{OddSum}\ge\tfrac12+\delta$) and the rest
(weight $\le1-\varepsilon$, each $\ge\tfrac12$ by the Floor Lemma). Then
$\mathbb E_{\mu_p}[\mathrm{OddSum}]\ge(1-\varepsilon)\cdot\tfrac12+
\varepsilon(\tfrac12+\delta)=\tfrac12+\varepsilon\delta$. Since
$c(n)=\tfrac12+\tfrac1{2(2^{n+1}-1)}$ (certified identity), $\mathbb
E_{\mu_p}[\mathrm{OddSum}]>c(n)$ exactly when $\varepsilon\delta>
1/(2(2^{n+1}-1))$, i.e. $2^{n+1}-1>1/(2\delta\varepsilon)$. $\blacksquare$

**Reviewer verification:** algebra independently re-derived from scratch,
matches exactly; the $c(n)$ closed-form substitution checked by direct
computation for $n=2,\dots,10$.

## Scope

This rules out any structured-randomization scheme whose "mediocre-mass"
$(\delta,\varepsilon)$ is bounded away from $0$ uniformly in $n$ — every
scheme tested this round (random-matching $k$-Anchor-Merge, random-index
Generalized Subset-Tie) satisfies this and is shown numerically to fail
exactly as the theorem predicts. It does **not** rule out a scheme that
concentrates $1-o(2^{-n})$ mass specifically on already-near-optimal
candidates — but constructing such a distribution requires solving the
same combinatorial-optimum question the deterministic approaches already
attack, defeating the point of randomizing. Certified as a general,
reusable, negative structural fact about the expectation-over-
randomization proof technique for this problem's upper-bound direction.
