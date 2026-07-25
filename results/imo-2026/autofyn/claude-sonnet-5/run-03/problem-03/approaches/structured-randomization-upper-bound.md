# Approach: structured (non-i.i.d.) randomized-construction upper bound

## Status
unsolved

## Approaches tried

- Naive i.i.d.-uniform randomized cut placement (round 12 pre-check, by the
  `plateau-check` math-explorer) — **dead end, refuted numerically but
  decisively**: at the balanced test point $p=(0.35,0.34,0.31)$ ($n=2$),
  200,000 trials of "assign each of the $n$ cuts to a uniformly random
  piece, split that piece with i.i.d. uniform breakpoints" give
  $\mathbb E[\mathrm{OddSum}]\approx0.6035$, strictly *above*
  $c(2)=4/7\approx0.5714$. Retained from the pre-round check, not repeated
  this round.

- **Random-matching $k$-Anchor-Merge (round 12, this build).** Design:
  apply the certified General $k$-Anchor-Merge Lemma (Theorem 10,
  `lemmas/singleton-interleaving-and-k-anchor-merge.md`) — which gives, for
  *any* choice of $k$ disjoint index pairs $(i_m,j_m)$,
  $\mathrm{OddSum}=\tfrac12(1-\sum_m\ell_m)+\mathrm{OddSum}(\{\ell_m\})$
  where $\ell_m=p_{i_m}-p_{j_m}$ — but instead of searching for the best
  pairing (a hard combinatorial choice other approaches already struggle
  with), *randomize* the pairing: draw a uniformly random perfect matching
  of a random $2k$-subset of the $n+1$ pieces, and take
  $\mathbb E[\mathrm{OddSum}]$. Tested at the documented $n=6$
  "large-gaps-everywhere" survivor point
  $p=(0.3306,0.2791,0.1501,0.1162,0.0904,0.0208,0.0128)$ (from
  `global-lp-vertex-sufficiency.md` §5, where $c(6)=64/127\approx0.503937$
  and the *named* single-tool family — $k\le2$ merges plus one Subset-Tie
  at $i=1$ — apparently fails at $\approx0.503983$). Exact `Fraction`-free
  but double-precision Monte Carlo, $3000$ random matchings per $k\in
  \{1,2,3\}$: $\mathbb E[\mathrm{OddSum}]\approx0.572,\,0.557,\,0.576$
  respectively for $k=1,2,3$ — **all far above** $c(6)$, by a margin
  $10$–$40\times$ larger than the gap the deterministic tools were even
  trying to close. Cross-checked against **exhaustive** search over every
  disjoint pairing (all $\binom{7}{2k}(2k-1)!!$ choices) for $k=1,2,3$:
  best exhaustive values $\approx0.5040,\,0.5041,\,0.5081$ — consistent
  with (independently reproducing) round 11's Anchor-Merge-family
  non-monotonicity finding that even the *best* pairing at this point
  narrowly fails to beat $c(6)$ for $k=1,2$ and gets worse at $k=3$. **Dead
  end**: random-matching averaging is not merely insufficient, it is
  wildly worse than even the (already-insufficient) best deterministic
  pairing — confirms that "which pairing" is not a nuisance parameter safe
  to randomize over; it is exactly where all the signal lives.

- **Random-index Generalized Subset-Tie (round 12, this build).** Design:
  apply the certified Theorem 12 (Generalized Subset-Tie,
  `lemmas/generalized-subset-tie-theorem12.md`) — $\mathrm{OddSum}=
  \tfrac12(1+p_i-T)$ where $T$ is the tied subset's sum — at a *randomly*
  chosen index $i$ (uniform over $\{1,\dots,n+1\}$), instead of committing
  to a fixed $i$ (round 8 tested only $i=1$). At each $i$, $T$ was computed
  two ways for comparison: the exact optimal subset sum $\le p_i$ (brute
  force over all $2^n$ subsets — exact, feasible for $n=6$) and the greedy
  largest-first heuristic. **A genuine, unexpected finding**, orthogonal to
  the randomization idea itself: $\min_i$ of this exact-subset-sum value at
  the same $n=6$ survivor point is $\approx0.500000$ (attained at $i=1$,
  i.e. $p_2$ in 1-indexed notation, $T$ exactly matching a subset of the
  smaller pieces) — comfortably **below** $c(6)\approx0.503937$. On first
  inspection this looked like it might already refute the "survivor" at
  this point via a *deterministic* argument using Theorem 12's full
  any-index freedom (round 8's negative finding tested only the $i=1$-fixed
  special case, Theorem 11). **This was checked for being a rounding
  artifact and found to be exactly that at the literal quoted point** — the
  quoted coordinates are given to only $4$ decimal places, and
  $0.1501+0.1162+0.0128=0.2791$ *exactly* at that precision, a coincidence
  of the truncated decimal representation, not a genuine feature of the
  true (irrational-precision) numerically-optimized survivor. Re-testing
  under $1376$ independent small perturbations of the point (uniform noise
  $\pm3\times10^{-4}$ per coordinate, renormalized, re-sorted, filtered to
  stay in the balanced region) shows the effect is **robust to the
  perturbation, not an artifact of it**: $\min_i$ of the exact-subset-sum
  value stays $\le0.5027$ in every single one of $1376$ trials (mean
  $\approx0.5004$), and the **greedy** heuristic (no exact subset-sum
  search needed) gives the identical qualitative result ($555/555$
  perturbed trials, mean $\approx0.50041$, max $\approx0.5027$, all beating
  $c(6)$). So: **at this specific survivor's neighborhood, taking the best
  of Theorem 12 over *all* $n+1$ indices (not just $i=1$) already beats
  $c(6)$ by a comfortable, perturbation-robust margin, using only the
  already-certified Theorem 12 and no new machinery.** This is a genuine
  by-product finding, flagged below for other approaches (it is NOT part
  of this approach's own deliverable, and NOT proved for general $n$; see
  "Handoff" below) — but note it is a **minimum** over the $n+1$ choices of
  $i$, not an expectation.
  **The expectation itself fails**: $\mathbb E_i[\text{best-of-}i]$ over
  the uniform distribution on $i\in\{1,\dots,7\}$ at the original quoted
  point is $\approx0.5072$, **above** $c(6)$ — driven by two bad indices
  ($i=4$ giving $\mathrm{OddSum}\approx0.5284$, $T$ can only reach a small
  fraction of $p_i$ there). So even though *some* index is excellent, a
  uniform-average argument over indices does not see it — the good index
  is outvoted by the mediocre ones. **This is also a dead end for the
  expectation mechanism specifically**, despite the interesting min-based
  by-product.

- **Broad sweep: does $\min_i$ Theorem-12(greedy) generalize?** To check
  whether the min-over-index by-product above is a real route to the
  general Existence Theorem (as opposed to a coincidence of one point),
  swept $3000$ random balanced-region points per $n\in\{2,\dots,9\}$
  (Dirichlet/exponential sampling, rejected outside the balanced region:
  $p_1<1/2$, every gap $>\gamma(n)$), computing $\min_i$ of the greedy
  Theorem-12 value at each. **Result: fails broadly, especially at small
  $n$** — $100\%$ of $3000$ trials fail at $n=2$ (worst-case margin
  $c(n)-v\approx-0.0116$), with failure rates $6$–$44\%$ at $n=3,\dots,9$
  (worst-case margin always strictly negative, $-0.003$ to $-0.012$
  depending on $n$). So the min-over-index Theorem-12 family, by itself,
  is **not** a general closure of the balanced region — it happened to
  work at the one specific survivor instance tested above, consistent with
  (not contradicting) round 8's finding that the named-tool survivor rate
  does not shrink to zero with $n$: it just shows the *specific*
  already-catalogued survivor is not survivor to the *slightly* larger
  any-index family either, while plenty of *other* points still are.

## Current best

No positive result. This approach's own mechanism (expectation over a
structured discrete randomization) is shown below to be **structurally
incapable** of proving the upper-bound direction for large $n$, for a
precise, general, provable reason — not merely "the schemes tried so far
didn't happen to work." This is the round's main content.

## Theorem (Expectation Obstruction) — why averaging over discrete tie
## choices cannot close the balanced-region residual for large $n$

**OddSum Floor Lemma.** For every nonempty finite multiset $M$ of positive
reals, $\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$.

*Proof.* List $M$ sorted descending as $x_1\ge x_2\ge\cdots\ge x_k$. Then
$$\mathrm{OddSum}(M)-\mathrm{EvenSum}(M)=\sum_{i\text{ odd}}x_i-\sum_{i\text{ even}}x_i
=(x_1-x_2)+(x_3-x_4)+\cdots\ (+\,x_k\text{ alone if }k\text{ odd}),$$
and every bracket (and the possible lone final term) is $\ge0$ since the
$x_i$ are sorted descending. So $\mathrm{OddSum}(M)\ge\mathrm{EvenSum}(M)$,
and since $\mathrm{OddSum}(M)+\mathrm{EvenSum}(M)=\mathrm{sum}(M)$,
$\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$. $\blacksquare$ (Elementary;
independently confirmed numerically, $20{,}000$ random multisets of size
$1$–$15$, minimum observed ratio $\mathrm{OddSum}/\mathrm{sum}\approx0.50008$,
consistent with the bound being tight only in the limit.)

Applied to any legal XY response on a partition summing to $1$:
$\mathrm{OddSum}\ge\tfrac12$ **always**, regardless of $p$ or the response
chosen.

**Expectation Obstruction Theorem.** Fix $\delta,\varepsilon\in(0,\tfrac12)$
independent of $n$. Suppose a "structured randomization" scheme assigns, at
every balanced-region $p$ (of every $n$), a finite candidate set of legal
XY-responses $\mathcal R(p)$ and a distribution $\mu_p$ on it, with the
property that
$$\mu_p\bigl(\{\,r\in\mathcal R(p):\mathrm{OddSum}(r)\ge\tfrac12+\delta\,\}\bigr)\ \ge\ \varepsilon
\qquad\text{for every such }p.$$
(I.e. a fixed, $n$-independent fraction of the distribution's mass sits on
responses bounded a fixed constant $\delta$ above the absolute floor
$\tfrac12$ — "there are always some mediocre candidates with non-vanishing
weight.") Then for every $n$ with
$$2^{n+1}-1\ >\ \frac1{2\delta\varepsilon}\qquad\Bigl(\text{i.e. }n\ >\ \log_2\!\Bigl(1+\tfrac1{2\delta\varepsilon}\Bigr)-1\Bigr),$$
$\mathbb E_{\mu_p}[\mathrm{OddSum}]>c(n)$ for every balanced-region $p$ of
that $n$ — so the expectation argument $V(p)\le\mathbb E_{\mu_p}
[\mathrm{OddSum}]\le c(n)$ **cannot** be used to certify the upper bound at
that $n$, via this scheme, at any point.

*Proof.* Split $\mathcal R(p)$'s mass into the "mediocre" part (weight
$\ge\varepsilon$, each with $\mathrm{OddSum}\ge\tfrac12+\delta$) and the
rest (weight $\le1-\varepsilon$, each with $\mathrm{OddSum}\ge\tfrac12$ by
the Floor Lemma, no better bound assumed). Then
$$\mathbb E_{\mu_p}[\mathrm{OddSum}]\ \ge\ (1-\varepsilon)\cdot\tfrac12+\varepsilon\cdot\bigl(\tfrac12+\delta\bigr)=\tfrac12+\varepsilon\delta.$$
By the certified closed form (all approaches agree),
$c(n)=\dfrac{2^n}{2^{n+1}-1}=\dfrac12+\dfrac1{2(2^{n+1}-1)}$. So
$\mathbb E_{\mu_p}[\mathrm{OddSum}]>c(n)$ exactly when
$\varepsilon\delta>\dfrac1{2(2^{n+1}-1)}$, i.e. $2^{n+1}-1>\dfrac1{2\delta\varepsilon}$,
which is the stated threshold. $\blacksquare$

**This theorem is not vacuous — it is exactly what both numerical
experiments above exhibit.** The random-matching Anchor-Merge scheme puts
overwhelming mass ($\gg\varepsilon=0.5$, in fact most of it) on matchings
with $\mathrm{OddSum}\ge0.55$, i.e. $\delta\ge0.05$, $\varepsilon$ close to
$1$ — already past the threshold at $n=6$ ($2\delta\varepsilon\approx0.09
\gg1/(2\cdot127)\approx0.0039$), matching the observed
$\mathbb E\approx0.55$–$0.58\gg c(6)$. The random-index Subset-Tie scheme
puts weight $\varepsilon=2/7$ on two visibly mediocre indices with
$\delta\ge0.024$ ($\mathrm{OddSum}\ge0.5025,0.5284$ observed) — again past
threshold, matching the observed $\mathbb E\approx0.507>c(6)\approx0.5039$.

**Scope of the obstruction (honest, precise).** This does **not** prove
that *no* probabilistic scheme can ever work — only that any scheme whose
"mediocre-candidate mass" $(\delta,\varepsilon)$ is bounded away from $0$
uniformly in $n$ fails once $n$ exceeds an explicit threshold. A scheme
that concentrates probability $1-o\bigl(2^{-n}\bigr)$ specifically on the
already-near-optimal candidates (i.e. $\varepsilon\to0$ fast enough as
$n\to\infty$, or $\delta\to0$) could in principle evade the theorem. But
constructing such a concentrating distribution requires already knowing,
combinatorially, which candidates are near-optimal at each $p$ — exactly
the classification problem (`global-lp-vertex-sufficiency`'s $\Sigma$-shape
residual; the min-over-index by-product's "which index" question) that the
other, non-probabilistic approaches are already directly attacking. In
other words: **the only way to make the expectation mechanism work is to
first solve the underlying combinatorial-optimum problem, which defeats
the point of introducing randomization as a way to avoid it.** This is a
genuine structural reason (via $c(n)\to\tfrac12$ combined with the
universal OddSum floor $\ge\tfrac12$) that the probabilistic-method /
expectation framing is a poor fit for this specific problem's upper-bound
direction, independent of which specific construction family is
randomized over.

## Handoff (not part of this approach's own claim)

The by-product finding above — that $\min_i$ of Theorem 12 (Generalized
Subset-Tie, any index, not just $i=1$) beats $c(6)$ robustly in a
neighborhood of the documented $n=6$ survivor point, via a purely
deterministic minimum, no randomization — is flagged for
`global-lp-vertex-sufficiency` and `universal-halving-adversary` as a
possibly-useful widening of the named-tool family (any-index Subset-Tie
was apparently never swept over all indices in earlier rounds, only
$i=1$). The broad sweep above shows it is **not** a general closure by
itself (fails $100\%$ at $n=2$, $6$–$44\%$ elsewhere), so it is offered
only as a documented lead, not a result to build on within this approach.

## Full proof
(none — Status is `unsolved`; this approach's mechanism is shown above to
be structurally obstructed for large $n$ under any scheme with
$n$-independent mediocre-mass, which every scheme tested this round
satisfies. No proof attempt is warranted without a genuinely different
distribution design that evades the Expectation Obstruction Theorem's
hypothesis, and no such design has been found.)
