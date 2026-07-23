## Status
unsolved

## Approaches tried
- (round 1, outline) Two local spiral-similarity/Miquel-type claims motivated by
  the "crossing" structure of conditions ∠LBK=∠LNC (pairs vertex B with vertex
  N) and ∠LCK=∠BMK (pairs vertex C with vertex M) — proposed as a mechanism
  distinct from the already-refuted global BMK~CNL similarity and MKNL
  concyclicity.
- (round 1, this build pass) Numerically tested BOTH key lemmas the outline
  named, on two independent generic scalene triangles, across the whole valid
  branch of the 1-parameter family (t ranging over ~8-10 sample values per
  triangle, filtered to the branch satisfying all containment/betweenness
  hypotheses, where OM=ON is confirmed to hold to ~1e-9–1e-14 as expected).
  **Both lemmas are refuted — dead end, recorded below with the numeric
  evidence.**

## Current best
(No correct progress established by this approach; the two proposed
mechanisms are both false as stated. See "Full diagnosis" below for the
numeric evidence and reasoning, kept for the record so no future round
re-attempts these specific claims.)

### Setup used for the numeric test
Coordinates $B=(-1,0)$, $C=(1,0)$, $A=(p,q)$ (two triangles tried:
$(p,q)=(0.3,1.7)$ and, independently, $B=(-1.3,0)$, $C=(0.9,0)$, $A=(-0.5,2.1)$
— i.e. a second triangle not even symmetric in the $B,C$ labelling scale, to
rule out an artifact of the first choice). $M=(A+B)/2$, $N=(A+C)/2$. For a
free parameter $t=\angle KBA=\angle ACL$, $K=(K_x,K_y)$ and $L=(L_x,L_y)$ were
solved as the common zero of the four equations
$$\angle KBA - t = 0,\quad \angle ACL - t = 0,\quad \angle LBK-\angle LNC=0,\quad \angle LCK-\angle BMK=0$$
via Newton's method (`scipy.optimize.fsolve`), started from an interior guess
(centroid of $\triangle BMC$ for $K$, centroid of $\triangle BNC$ for $L$) and
refined to residuals below $10^{-9}$. For each solution the branch was
filtered to require $K\in\operatorname{int}\triangle BMC$, $L\in
\operatorname{int}\triangle BNC$ (via the standard same-side/barycentric-sign
point-in-triangle test), $K$ inside $\angle LBA$ and $L$ inside $\angle ACK$
(via a cross-product betweenness-of-rays test). On the surviving branch,
$OM-ON$ was confirmed $\approx 0$ (order $10^{-9}$ to $10^{-14}$, i.e.
numerical-precision zero) at every sampled $t$, consistent with the problem
statement and with the independent explorer reports already on file for this
problem — so the family and the target identity are correctly reproduced;
the test rig is trustworthy.

### Lemma 1 (outline's step 1): spiral similarity $\triangle BKL \sim \triangle NLC$
The outline's claim was that $\angle LBK=\angle LNC$ (already forced by the
hypotheses) could be promoted to a full spiral similarity taking $(K,L)$ at
$B$ to $(L,C)$ at $N$, PROVIDED the side ratio $BK/BL = NL/NC$ also holds.

Numeric test (triangle 1, $(p,q)=(0.3,1.7)$), on the valid branch:

| $t$ | $BK/BL$ | $NL/NC$ | difference |
|---|---|---|---|
| 0.20 | 0.486386 | 0.348568 | +0.1378 |
| 0.35 | 0.421481 | 0.530011 | −0.1085 |
| 0.40 | 0.399732 | 0.582386 | −0.1827 |
| 0.45 | 0.377777 | 0.631719 | −0.2539 |
| 0.50 | 0.355536 | 0.678426 | −0.3229 |
| 0.55 | 0.332937 | 0.722844 | −0.3899 |

Triangle 2 ($B=(-1.3,0), C=(0.9,0), A=(-0.5,2.1)$) shows the same pattern
(difference $+0.19$ at $t=0.20$ decreasing continuously through $0$ near
$t\approx0.32$ down to $-0.41$ at $t=0.60$).

This is decisive: the ratio $BK/BL - NL/NC$ is not identically zero — it
varies smoothly and monotonically-ish over a range of about $0.5$ in
magnitude and even changes sign within the family (it is not, e.g., a
constant nonzero offset that could be an artifact of a mislabeled angle). A
genuine spiral similarity would force this difference to vanish identically
for every $t$ on the family, since $\angle LBK=\angle LNC$ (the angle
condition) already holds by hypothesis at every $t$ — so equal angle PLUS
equal ratio, if it were a real geometric identity, would hold at every
sampled point, not just possibly one accidental crossing where the sign
flips. **Conclusion: $\triangle BKL$ and $\triangle NLC$ are NOT spiral
similar in general along the family. Lemma 1 is false.**

### Lemma 2 (outline's step 2): $C,K,M$ concyclic with a 4th point $X\in\{L,B,\ldots\}$
The outline proposed that $\angle LCK=\angle BMK$ might be exactly the
inscribed-angle condition for $\{C,K,M,X\}$ concyclic for some natural
$X$ (candidates named: $X=L$, $X=B$, or an auxiliary intersection point).

A general concyclicity test was run: for four points $P_1,\dots,P_4$,
concyclicity is equivalent to the vanishing of the determinant
$$\det\begin{pmatrix}x_i & y_i & x_i^2+y_i^2 & 1\end{pmatrix}_{i=1}^4$$
(the standard "power of a point" / circle-through-3-points determinant test,
knowledge_base.md "coordinates" section — a real number is concyclic to
$O(10^{-9})$ relative scale if and only if this determinant vanishes to
that tolerance, given the points have $O(1)$ coordinates as here). This was
computed for every 4-point subset of $\{A,B,C,M,N,K,L\}$ that includes $K$
(the point common to the hypothesis $\angle LCK=\angle BMK$), across every
sampled $t$ on the valid branch, on triangle 1. None of the $\binom{6}{3}=20$
such subsets gives a determinant near zero at even a single tested $t$, let
alone identically across the family — the smallest magnitudes among the
outline's named candidates were, e.g., $\det[C,M,K,L]\approx 0.28$–$0.39$ and
$\det[M,K,B,L]\approx 0.45$–$0.83$ (in the coordinate scale where $B,C$ are
unit distance from the origin), both far from zero and both drifting
monotonically with $t$ rather than sitting near a fixed value. Triangle 2
reproduces the same picture ($\det[C,M,K,L]$ ranging smoothly from $0.83$ to
$1.43$, $\det[M,K,B,L]$ from $0.57$ to $0.78$, over $t\in[0.2,0.6]$, never
approaching zero). **Conclusion: no 4-point subset of $\{A,B,C,M,N,K,L\}$
containing $K,C,M$ is concyclic in general along the family. Lemma 2, in
every form the outline named (and every other natural 4-subset), is false.**

### Why this rules out the approach as stated
Both of the outline's proposed local rigid-map mechanisms (spiral similarity
linking $\triangle BKL$ to $\triangle NLC$; a Miquel-type concyclicity through
$C,K,M$ and a natural 4th point) fail to hold along the family, and fail
robustly — not marginally or only at a single triangle, but on two
independently-chosen scalene triangles, over a spread of parameter values,
with differences an order of magnitude larger than the $\sim10^{-9}$
numerical noise floor of the solver. There is no indication of a nearby
"almost-true" variant (e.g. a different vertex correspondence for the
similarity, or a different 4th point for the concyclicity) that the data
suggests fixing — the deviations are large, smooth, and monotonic in $t$
rather than small perturbations of an otherwise-correct identity. Per the
explicit instruction in the outline itself ("if both numeric checks fail...
this approach should be marked dead-end quickly rather than forced"), this
approach is retired rather than papered over.

This is consistent with (and reinforces) the outline-reviewer's diversity
note that this approach and `nine-point-link` occupy the same
"rigid-map/spiral-similarity search" family: both were looking for a fixed
local transformation forcing $O$ onto line $\ell=$ perp-bisector$(MN)$, and
in this instance the two specific candidate transformations proposed do not
exist. A future attempt in this family would need a genuinely different
candidate rigid map (not a variant of BKL~NLC or a C,K,M,X concyclicity),
which this build pass does not supply.

## Full proof
(Not applicable — Status is `unsolved`; no proof to present.)

## Promotable lemmas
None. (Both candidate lemmas investigated this round were numerically
refuted, not proven — nothing to promote to the shared cache. The general
concyclicity determinant test and the point-in-triangle / betweenness-of-rays
test rig used here are reusable numeric-verification *tools*, not proven
lemmas, and are not knowledge-base-citable facts about this problem.)
