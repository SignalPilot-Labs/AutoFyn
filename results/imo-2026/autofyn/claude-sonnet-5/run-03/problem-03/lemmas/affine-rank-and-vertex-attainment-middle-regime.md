# Affine-Rank Lemma, Vertex-Attainment Lemma, and the Feasibility Fact for the middle regime

Certified round 11. Proved in `approaches/self-similar-induction-on-n.md`
(round 11, "Round 11: the Affine-Rank Lemma and Vertex Reduction").

## Affine-Rank Lemma

**Statement.** Let $c_1,\dots,c_q>0$ be fixed reals (a frozen multiset $F$)
and $x=(x_1,\dots,x_p)\in\mathbb R^p$ free coordinates. For a strict order
type $\tau$ on the $p+q$ labels $\{x_1,\dots,x_p,c_1,\dots,c_q\}$ (consistent
with the fixed numeric order among the $c_i$), let
$\Omega_\tau:=\{x:\text{pairwise order of all labels matches }\tau\}$ (an
open convex polyhedral cone). Then there exist $I_\tau\subseteq\{1,\dots,p\}$
and a constant $K_\tau$ (depending only on $\tau$) such that for every
$x\in\Omega_\tau$,
$$\mathrm{OddSum}(\{x_1,\dots,x_p\}\cup\{c_1,\dots,c_q\})=K_\tau+\sum_{i\in I_\tau}x_i.$$

**Proof.** A strict total order on $p+q$ reals determines a unique rank for
each element, itself determined only by the pairwise comparisons. Fix
$x\in\Omega_\tau$: every pairwise comparison matches $\tau$, so the rank of
each label is exactly the permutation determined by $\tau$, the same for
every $x\in\Omega_\tau$ (moving within $\Omega_\tau$ never crosses a
comparison boundary). Hence the set of $x_i$-labels landing at odd rank
($I_\tau$) and of $c_l$-labels landing at odd rank ($J_\tau$, giving
$K_\tau:=\sum_{l\in J_\tau}c_l$) are fixed, and
$\mathrm{OddSum}=\sum_{i\in I_\tau}x_i+K_\tau$ for every $x\in\Omega_\tau$.
$\blacksquare$

## Vertex-Attainment Lemma

**Statement.** For $P\subseteq\mathbb R^p$ a nonempty compact convex
polytope and $f$ affine, $\max_Pf$ and $\min_Pf$ are attained at a vertex
of $P$.

**Proof.** Extrema exist by compactness/continuity. If a minimizer $x^*$ is
not a vertex, it is a nontrivial convex combination of two distinct points
$y,z\in P$; affineness forces $f(y)=f(z)=f(x^*)$ (else one of them would
beat the minimum). Extend the segment $[y,z]$ within $P$ until it exits in
both directions; the new endpoints stay in $P$ (closedness/convexity) with
the same $f$-value, and each satisfies at least one more defining
inequality of $P$ with equality than $x^*$ did. Repeating (finitely many
defining inequalities) terminates at a $0$-dimensional point of $P$, i.e. a
vertex, with the same $f$-value. $\blacksquare$

*(Standard "LP optimum is at a vertex" fact, independently re-derived here
for this approach's own object — free real coordinates merged with frozen
values, no fragment-sum elimination step needed, unlike the sibling
approach `global-lp-vertex-sufficiency`'s version.)*

## Feasibility Fact for the middle regime

**Statement.** The middle regime $\mu\le b_1<2^{m-1}$ (comparing $B$'s top
fragment $b_1$ to $\mu:=\max(S)$, for a top-split $B$ of $2^m$ against a
refinement $S$ of $\Gamma_{m-1}$) is nonempty only if the cut producing $S$
splits $S$'s own top piece $2^{m-1}$.

**Proof.** If no cut touches $\Gamma_{m-1}$'s top piece $2^{m-1}$, then
$2^{m-1}\in S$ exactly, and every other piece of $\Gamma_{m-1}$ (cut or not)
has value $\le2^{m-1}$ (a cut only ever produces fragments strictly less
than the piece cut), so $\mu=2^{m-1}$. The middle regime requires
$b_1<2^{m-1}=\mu$ and $b_1\ge\mu$ simultaneously — impossible. $\blacksquare$

## Reviewer verification

All three statements independently re-derived from scratch and confirmed
correct (elementary order-theory / polytope geometry / pigeonhole,
respectively). The three worked instances built on top of these lemmas in
the approach file were independently hand-verified by the reviewer:

- $m=3$: $B\cup S=\{4,2,2\}\cup\{4,0,2,1\}$, sorted $4,4,2,2,2,1,0$,
  $\mathrm{OddSum}=4+2+2+0=8=2^3$. Exact match.
- $m=4$: $B\cup S=\{6,6,4\}\cup\{4,4,4,2,1\}$, sorted $6,6,4,4,4,4,2,1$,
  $\mathrm{OddSum}=6+4+4+2=16=2^4$. Exact match.
- $m=5$: $B\cup S=\{12,12,8\}\cup\{8,8,8,4,2,1\}$, sorted
  $12,12,8,8,8,8,4,2,1$, $\mathrm{OddSum}=12+8+8+4+1=33>32=2^5$. Exact
  match (strict slack).

## What this does and does not resolve

These lemmas give a **structural** reduction (the Middle-Regime Vertex
Reduction Theorem): the true minimum of $\mathrm{OddSum}(B\cup S)$ within
any fixed regime and order-type cell is attained at a vertex, reducing each
fixed $(j,c,m)$ instance to (in principle) a finite check. This round
applies it only to exhibit exact closures at three small instances of the
smallest nonempty middle-regime family $(j,c)=(2,1)$, $m=3,4,5$ — **not** a
proof for general $m$, nor for the middle regime, `Case-B(m,k)`, or gap
(b)(ii) in general: the vertex candidates used were located by numerical
search, not by a completed exhaustive enumeration of the full hyperplane
arrangement (which also requires checking ties against individual elements
of $\Gamma_{m-2}$). The middle regime, `Case-B(m,k)`, and gap (b)(ii) remain
open in general.
