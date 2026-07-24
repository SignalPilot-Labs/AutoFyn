## Statement

Fix an arbitrary marking $p_1,\dots,p_m>0$ ($T=\sum p_i$) and a legal
cut-composition $(c_1,\dots,c_m)$, $c_i\ge0$ integers, $\sum_ic_i\le n$.
Xiang Yu's legal responses under this composition form the polytope
$$\mathcal Q := \prod_{i=1}^m \Delta_i,\qquad
\Delta_i:=\Big\{(f_{i,1},\dots,f_{i,c_i+1}):f_{i,j}\ge0,\ \textstyle\sum_j
f_{i,j}=p_i\Big\}.$$
$\mathcal Q$ is compact and $\Phi$ (equivalently $E$, since
$\Phi=(T+A)/2=(T+(T-2E))/2=T-E$ is affine decreasing in $E$ at fixed $T$)
is continuous on it, so a global minimizer
$F^\ast=(F_1^\ast,\dots,F_m^\ast)\in\mathcal Q$ of $\Phi$ (maximizer of $E$)
exists. For every $i$ with $c_i\ge1$, let $\tau_i$ be the reference
multiset formed by all coordinates of $F_j^\ast$ for $j\ne i$. Then
$F_i^\ast$ is itself a maximizer of $E(F_i\cup\tau_i)$ over
$F_i\in\Delta_i$ — i.e. $F_i^\ast$ solves the Simplex Vertex-Maximization
problem with reference multiset $\tau_i$, mass $p_i$, budget $c_i+1$.
Consequently, by the certified (corrected) `simplex-exchange-smoothing-
vertex-maximization`, $F_i^\ast$ is of pinned+tied vertex form relative to
$\tau_i$'s values and $0$.

## Proof

See `results/imo-2026-03/approaches/lp-duality-certificate.md`, §R11.4.
Existence: standard compactness/continuity (extreme value theorem,
identical argument to the certified `vertex-minimum-theorem`, transplanted
to a product of simplices — neither compactness of a finite product of
compact sets nor continuity of the sort-and-sum functional depends on
there being only one factor). Per-piece optimality: if some $F_i^\ast$
were not itself $E$-maximizing relative to $\tau_i$, a strictly-improving
deviation $F_i'$ would produce a legal global point $F'\in\mathcal Q$
(pieces' legal moves are mutually independent — no constraint couples
different pieces' fragment choices beyond the shared cut-count budget,
which is already fixed by the composition) whose final multiset is
literally $\tau_i\cup F_i'$, strictly increasing $E$ and contradicting
global maximality of $F^\ast$.

## Certification note

**CERTIFIED — proof-reviewer, round 11.** A standard "each block of a
jointly-optimal product-space point is itself optimal given the rest"
argument; the reviewer independently re-verified the logic (no gap: the
mutual independence of pieces' legal move spaces, which is exactly what
makes $\mathcal Q$ a literal product $\prod_i\Delta_i$, is the only fact
needed for the contradiction step, and it holds by the problem's own rules
— Xiang Yu cannot move mass between original pieces) and spot-checked it
numerically on a 3-piece marking with a mixed composition (piece 1: 1 cut,
piece 2: 1 cut, piece 3: 0 cuts), confirming via a multi-start global
optimizer that the piece-1 split found at the joint global minimizer of
$\Phi$ is also individually $E$-maximizing relative to the rest of the
final multiset (`/tmp/round-11` verification, matches to numerical
precision). This is a genuine, general, marking- and composition-agnostic
structural result; its *evaluation* against $a_nT$ for a specific marking
remains open and is NOT part of what is certified here — only the finite
vertex-characterization itself.
