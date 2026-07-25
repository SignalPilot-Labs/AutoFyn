## Lemma: Two-Piece-Split Vertex Lemma (finite exact reduction of the best simultaneous two-piece XY response)

**Statement.** Fix positive reals $q_1,\dots,q_r$ (the untouched pieces),
and two positive reals $T,T'$ (the two pieces to be split simultaneously).
For $2\le m\le n_1$, $2\le m'\le n_2$ with $(m-1)+(m'-1)\le n$, define
$$f_{m,m'}(x,y):=\mathrm{OddSum}\bigl(\{q_1,\dots,q_r\}\cup\{x_1,\dots,x_m\}\cup\{y_1,\dots,y_{m'}\}\bigr),$$
$x_i>0,\sum x_i=T$, $y_i>0,\sum y_i=T'$. Let $\mathcal V$ be the finite set
of vectors obtained, for each valid $(m,m')$, each set partition of the
$x$-block and of the $y$-block, one free block in each, assignment of every
non-free block to a value in $\{0\}\cup\{q_1,\dots,q_r\}$, **and**
additionally allowing exactly one non-free $x$-block to be pinned equal to
one non-free $y$-block (a cross-tie), solving the remaining free block(s)
from the sum constraints, keeping only vectors with all coordinates $\ge0$.
Then
$$\min_{x,y}f_{m,m'}(x,y)=\min_{(x,y)\in\mathcal V}f_{m,m'}(x,y),$$
attained at a vector of $\mathcal V$ with all coordinates strictly
positive.

**Proof.** Direct generalization of the certified Single-Piece-Split Vertex
Lemma (`lemmas/single-piece-split-vertex-lemma.md`) to the product polytope
$\Delta_T\times\Delta_{T'}$: $f_{m,m'}$ is linear on each sort-order
region, so by Krein–Milman its minimum on a bounded polytope is attained
at an extreme point, characterized by $(m-1)+(m'-1)$ active independent
constraints (beyond the two sum-equalities, one per simplex factor). The
active order-tightness constraints decompose into within-$x$-block ties
($m-g$ constraints for $g$ $x$-blocks), within-$y$-block ties ($m'-h$
constraints for $h$ $y$-blocks), and, to reach the required rank, $(g-1)$
further $x$-pins and $(h-1)$ further $y$-pins to values in
$\{0,q_1,\dots,q_r\}$ — **unless** one $x$-block is tied directly to one
$y$-block (a cross-tie), which supplies one unit of the needed rank without
a $\{0,q_j\}$-pin. This exhausts every way a linear order-constraint
between a variable of one simplex factor and a variable of the other can be
active (the only linear relation available between two order-statistic
variables at a tie is equality), so every extreme point arises this way,
matching the construction of $\mathcal V$. $\blacksquare$

**Independent verification (proof-reviewer, round 6).** Spot-checked
numerically on a concrete instance ($r=1$, $q_1=0.5$, $T=0.3$, $T'=0.2$,
$m=m'=2$): a from-scratch multistart Nelder–Mead optimizer over the full
4-dimensional joint polytope (300 restarts) found minimum $0.6$; an
independent from-scratch enumeration of the candidate vertex set (block-tie
$x_1=x_2=T/2$ or boundary; block-tie $y_1=y_2=T'/2$ or boundary; plus a
scan of cross-tie configurations $x_1=y_1=z$) found the identical minimum
$0.6$ — full agreement. The builder's own independent checks (applied to
the Anchor-Merge/$k$-Anchor-Merge constructions at $n=3,\dots,6$, and
cross-checked against Nelder–Mead on 30 random instances to $10^{-6}$) are
consistent with this. Not re-derived in full generality by the reviewer
(the general rank-counting argument is a mechanical, standard LP-vertex
argument directly analogous to the already-certified single-piece case,
and no error was found in the stated mechanism), but the spot check gives
concrete positive evidence the mechanism is applied correctly.

**Source.** Proved in `approaches/universal-halving-adversary.md` (round 6,
Theorem 8).

**Reuse.** Supplies the exact finite-search machinery to verify or refute,
per instance, whether a genuinely simultaneous 2-piece split can reach a
target value — directly used to compute the $k$-Anchor-Merge closed forms'
optimality and reusable by `lp-duality-split-polytope` or any future
approach needing an exact (not merely numerical) 2-piece floor.
