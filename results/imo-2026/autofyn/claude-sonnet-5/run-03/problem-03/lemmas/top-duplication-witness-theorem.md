# Top-Duplication Witness Theorem

Certified round 11. Proved in `approaches/lp-duality-split-polytope.md`
(round 11, Section 11.2).

**Statement.** For every integer $n\ge0$, LB's geometric partition
$p_i=2^{n+1-i}/(2^{n+1}-1)$ ($i=1,\dots,n+1$) admits a legal XY response
using exactly $n$ cuts ($0$ for $n=0$): split only the top landmark $2^n$
(piece $p_1$) into the fragments $2^{n-1},2^{n-2},\ldots,2^1,1,1$, leaving
every other landmark unsplit. This response achieves
$$\mathrm{OddSum}=c(n)=\frac{2^n}{2^{n+1}-1}\quad\text{exactly}.$$

**Proof.** $n=0$: the multiset is $\{1\}$, $\mathrm{OddSum}=1=c(0)$.

For $n\ge1$: the dimensionless multiset (landmark units, sum $D=2^{n+1}-1$)
is $X=\{2^0,\dots,2^{n-1}\}\cup\{2^1,\dots,2^{n-1},1,1\}$. For each
$j=1,\dots,n-1$, $2^j$ occurs exactly twice (once unsplit, once as a split
fragment) — an isolated tied pair (by the certified Even-Block-Neutrality /
Bottom-Block-Doubling machinery,
`lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`), each
contributing $0$ to $\mathrm{AltSum}(X)$ and not disturbing the rank parity
of any other element. The remaining three elements — the unsplit landmark
$1$ plus the two split fragments valued $1$ — form the unique minimum value
of $X$, occupying the bottom three ranks $2n-1,2n,2n+1$ of the $|X|=2n+1$
total elements (all other elements strictly exceed $1$). Since $2n$ is even,
these three ranks are odd, even, odd, so their $\mathrm{AltSum}$ contribution
is $1-1+1=1$. Hence $\mathrm{AltSum}(X)=1$ for every $n\ge0$ (including
$n=0$: $\mathrm{AltSum}(\{1\})=1$). By the elementary identity
$\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$ applied in dimensionless
units, actual $\mathrm{OddSum}=(D+1)/(2D)=2^{n+1}/(2(2^{n+1}-1))
=2^n/(2^{n+1}-1)=c(n)$. $\blacksquare$

**Reviewer verification.** Independently re-implemented the construction
from scratch (literal fragment list, not the closed-form shortcut) and
computed $\mathrm{OddSum}$ by direct sort-and-sum in exact `Fraction`
arithmetic for $n=0,\dots,14$: exact fraction equality with $c(n)$ in all 15
instances (e.g. $n=9$: both sides $512/1023$ identically). Also
independently re-verified, by a from-scratch exact script, the companion
negative result (Section 11.1) that the direct multi-landmark transplant of
round 10's Multi-Piece Sufficiency construction fails at LB's geometric
partition, with shortfall growing from $\approx1.4\times10^{-7}$ at $n=2$
to $\approx0.123$ at $n=8$ — matched the file's table to the reported
precision at every tested $n$.

**Consequence.** $V(p_{\mathrm{LB}})\le c(n)$ for every $n\ge0$,
unconditionally — a single-point result for the upper-bound direction at
LB's own (conjectured extremal) partition. It does **not** prove
$V(p_{\mathrm{LB}})\ge c(n)$ (the separately-tracked open lower-bound
direction), and does not by itself extend to any other point of the
balanced region.
