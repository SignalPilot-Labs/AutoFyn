## Lemma: Single-Piece-Split Vertex Lemma (finite exact reduction of the best single-piece XY response)

**Statement.** Fix positive reals $q_1,\dots,q_r$ (the untouched pieces of
LB's partition) and $T>0$ (the piece to be split). For $2\le m\le n+1$
define
$$f_m(x_1,\dots,x_m):=\mathrm{OddSum}\bigl(\{q_1,\dots,q_r\}\cup\{x_1,\dots,x_m\}\bigr),\qquad x_i>0,\ \textstyle\sum x_i=T.$$
Let $\mathcal V$ be the finite set of vectors obtained, for each $m$ from
$2$ to $n+1$ and each set partition $\{B_1,\dots,B_g\}$ of $\{1,\dots,m\}$
and each choice of one "free" block $B_{i_0}$, by assigning every other
block $B_i$ ($i\ne i_0$) a value in $\{0\}\cup\{q_1,\dots,q_r\}$, and
solving the free block's common value from $\sum x_i=T$, keeping only
vectors with all coordinates $\ge0$. Then
$$\min_{\substack{2\le m\le n+1\\ x_i>0,\ \sum x_i=T}} f_m(x) = \min_{x\in\mathcal V} f_m(x),$$
and this minimum is attained by a vector in $\mathcal V$ with all
coordinates strictly positive (a genuine $\le n$-cut split of $T$) — any
minimizer in $\mathcal V$ with a zero coordinate reduces, by discarding
that coordinate, to a smaller-$m$ vector in $\mathcal V$ achieving the same
value.

**Proof.** For fixed $m$, $f_m$ is linear on each sort-order region (a
polytope obtained by intersecting the closed simplex $\{x\ge0,\sum
x_i=T\}$ with order half-spaces between pairs of the $m+r$ elements — the
$r$ elements $q_j$ being fixed constants, so an order constraint against
$x_i$ is a linear inequality on $x_i$ alone). A linear functional on a
bounded polytope attains its minimum at an extreme point (Krein–Milman for
polytopes: every point is a convex combination of finitely many extreme
points, and a linear functional's value on the combination is the same
combination of its extreme-point values). A point of a sort-order region is
an extreme point iff its active constraints (nonnegativity $x_i\ge0$,
order-tightness $x_i=x_j$ or $x_i=q_j$, together with $\sum x_i=T$) have
rank $m$; the active order-tightness constraints partition
$\{1,\dots,m\}$ into blocks forced equal by chains of ties, using $m-g$
independent constraints for $g$ blocks, and reaching rank $m$ (given
$\sum x_i=T$ already present) requires exactly $g-1$ further active
constraints, each pinning one block to $0$ or to a specific $q_j$ — this is
exactly the construction of $\mathcal V$. Every extreme point of every
sort-order region arises this way, and every vector so constructed with all
coordinates $\ge0$ is such an extreme point, so the two minima are equal.
The zero-coordinate reduction is immediate: discarding a length-$0$
"fragment" from a multiset does not change any other element's value or
sort order, hence not $\mathrm{OddSum}$, and the reduced vector is exactly
the $m-1$ analogue of the same block/pin structure. $\blacksquare$

**Independent verification.** Applied exactly (exact rational arithmetic)
to two instances — LB partition $(2/5,3/10,1/5,1/10)$ at $n=3$, and
$(1/3,4/15,1/5,2/15,1/15)$ at $n=4$ — and cross-checked at the first
instance against an independent continuous (Nelder–Mead) numerical
optimizer: both methods found the identical optimal value $11/20$, at
different (both valid) vertices in $\mathcal V$, confirming the finite
candidate set is complete in practice as well as in the proof.

**Source.** Proved in `approaches/lp-duality-split-polytope.md` (round 5,
Section 2, "Single-Piece-Split Vertex Lemma").

**Reuse.** A general-purpose, self-contained tool (independent of, and
much narrower/more tractable than, `dyadic-potential-invariant`'s
still-open general multi-piece Tie-or-Zero Lemma) for computing or
bounding — exactly, via a finite mechanical enumeration — the best
achievable $\mathrm{OddSum}$ when XY is restricted to splitting only one
named piece of a fixed LB partition. Directly used to prove Multi-Piece
Necessity instances at $n=3,4$ (same file, Sections 3–4): explicit balanced
partitions ($p_1<1/2$) for which every single-piece XY response fails to
reach $c(n)$ while a two-piece response succeeds, upgrading prior hand-built
single counterexamples to an exhaustively-verified elimination of the
entire single-piece response family for those instances. Reusable by any
future approach needing to (a) rule out single-piece sufficiency for a
family of LB partitions, or (b) compute the exact single-piece floor as a
baseline/subroutine inside a larger multi-piece construction.
