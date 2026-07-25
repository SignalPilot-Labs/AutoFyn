# Rank-Pinning Lemma, and the General Multi-Piece Subset-Tie / Mass-Constraint Theorem

Certified round 11. Proved in `approaches/global-lp-vertex-sufficiency.md`
(round 11, Section 4 and Section 4.5).

## Rank-Pinning Lemma

**Statement.** Fix $n$, $k=n+1$, the finite shape set $\Sigma(n,k)$ of the
Global Vertex Lemma, and for $\sigma\in\Sigma$ let $y_\sigma(p)$ be the full
multiset of fragments-plus-untouched-pieces determining
$f_\sigma(p)=\mathrm{OddSum}(y_\sigma(p))$. Let $L$ be enlarged (beyond the
round-10 list) to also include every pairwise difference
$y_\sigma(p)_a-y_\sigma(p)_b$ among a single shape $\sigma$'s own multiset
coordinates. Then on any open cell $C$ of the resulting (still finite)
hyperplane arrangement, the coordinate of $y_\sigma(p)$ occupying each fixed
sorted rank is the same coordinate index for every $p\in C$; consequently
$f_\sigma(p)$ is a single fixed affine-in-$p$ formula throughout $C$.

**Proof.** Each pairwise difference $y_\sigma(p)_a-y_\sigma(p)_b$ is, by
construction, a member of $L$, hence has constant (nonzero) sign throughout
$C$ (the defining property of an open cell of a finite hyperplane
arrangement). Constant sign of every pairwise difference among a fixed
finite list of coordinates fixes the coordinates' full relative order
(hence which coordinate occupies which sorted rank) for every $p\in C$: no
two labels can swap rank without their difference crossing zero, which
cannot happen inside $C$. Hence the rank assignment is locally constant on
$C$, and $f_\sigma(p)$, the sum of the (now positionally fixed) odd-rank
coordinates, is a single affine-in-$p$ expression on $C$. $\blacksquare$

**What this closes.** Lemma 4.1(b) (round 10, as it stood) correctly pinned
the *ordering between* branches $\sigma,\tau$ via $f_\sigma-f_\tau\in L$, but
implicitly assumed each $f_\sigma$ is itself a single affine formula on a
cell — this lemma supplies that missing first step. Enlarging $L$ with the
boxed pairwise-difference group leaves $L$ finite (finitely many $\sigma$,
each with a bounded-size multiset $y_\sigma$) and does not disturb Lemma
4.1(a), Lemma 4.2, or the Finite-Cell Affine-Vertex Reduction Theorem (all
use only finiteness + affineness of $L$'s members), nor the already-closed
region-only candidate sub-list $Q_{\mathrm{region}}$ (which used only region
functionals, never this boxed group).

**Reviewer verification.** The argument is elementary point-set/order-theory
(constant sign of finitely many pairwise differences on a connected set
fixes a total order), independently re-derived from scratch and confirmed
correct; no numeric check is needed for a purely logical statement of this
kind, but the downstream consequence (Lemma 4.1/4.2 unaffected) was
cross-checked against the file's own statements of those lemmas.

## General Multi-Piece Subset-Tie construction, and the Mass-Constraint Theorem

**Construction.** Let $p_1>\cdots>p_{n+1}>0$ sum to $1$. Choose
$S=\{i_1,\dots,i_s\}\subseteq\{1,\dots,n+1\}$ and a partition of
$U:=\{1,\dots,n+1\}\setminus S$ into $s$ (possibly empty) groups
$J_1,\dots,J_s$ (one per split piece) such that
$T_a:=\sum_{m\in J_a}p_m\le p_{i_a}$ for every $a$. XY's move: split
$p_{i_a}$ into fragments $\{p_m:m\in J_a\}\cup\{r_a\}$,
$r_a:=p_{i_a}-T_a\ge0$; leave every $p_m$, $m\in U$, untouched. (This is the
direct $s$-piece generalization of the certified Generalized Subset-Tie
Lemma, Theorem 12, `lemmas/generalized-subset-tie-theorem12.md`, the special
case $s=1$.)

**Value formula.** Generically (all values distinct except the
by-construction ties), with $\Pi:=\sum_a p_{i_a}$,
$$\mathrm{OddSum}(M)=(1-\Pi)+\mathrm{OddSum}(\{r_1,\dots,r_s\}).$$

*Proof.* $M=B\sqcup L$ with $B=\{p_m,p_m\}_{m\in U}$ (each untouched piece
paired with its equal-valued tied fragment) and $L=\{r_1,\dots,r_s\}$.
$\mathrm{sum}(B)=2\sum_{m\in U}p_m=2(1-\Pi)$ since $\sum_{m\in U}p_m=1-\Pi$.
By the certified Singleton-Interleaving Lemma (Theorem 9,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`),
$\mathrm{OddSum}(M)=\tfrac12\mathrm{sum}(B)+\mathrm{OddSum}(L)=(1-\Pi)+
\mathrm{OddSum}(\{r_1,\dots,r_s\})$. $\blacksquare$

**Theorem (Mass-Constraint).** In any legal instance, $\Pi\ge\tfrac12$.

*Proof.* Summing $T_a\le p_{i_a}$ over $a$: $\sum_aT_a\le\Pi$. But
$\sum_aT_a=\sum_{m\in U}p_m=1-\Pi$ exactly (the $J_a$'s partition $U$).
Hence $1-\Pi\le\Pi$, i.e. $\Pi\ge\tfrac12$. $\blacksquare$

**Corollary (bounded-$s_0$ impossibility at the region vertex $e_0$).** At
$p=e_0$ (the region-only vertex of `finite-cell-vertex-reduction-and-
region-classification.md`, Section 4.1), $M(n):=p_1(e_0)<3/(2(n+1))$ (using
the already-established bound $n(n+1)\gamma(n)<1$), so any legal instance
needs $s\ge1/(2M(n))>(n+1)/3$ split pieces — unboundedly many as
$n\to\infty$. Hence for any fixed $s_0$, once $n>3s_0-1$, no instance of
this construction (splitting $\le s_0$ pieces) is even legal at $e_0$.

**Reviewer verification.** Independently re-derived from scratch: (1) the
value formula's decomposition into $B\sqcup L$ and its use of the certified
Singleton-Interleaving Lemma, confirmed correct; (2) the Mass-Constraint
inequality, a one-line summation, re-checked by hand; (3) the exact
coordinate formula $p_1(e_0)=(2+n(n+1)\gamma(n))/(2(n+1))$, independently
re-derived from the certified Section 4.1 formulas for $p_i(e_0)$ and
matched to the file's claim; (4) the resulting bound
$s>(n+1)/3$, re-derived algebraically and confirmed.

**What this does and does not resolve.** This is a genuine negative result:
it rules out bounded-$s_0$ sufficiency **for this specific construction
family** (tie each split fragment to the value of a whole untouched piece).
It does **not** rule out fragment-vs-fragment tying (ties among fragments of
*different* split pieces, not matched against any whole untouched piece),
nor any non-tie-based mechanism — both explicitly flagged as open in the
approach file. The Existence Theorem for `global-lp-vertex-sufficiency`
remains open.
