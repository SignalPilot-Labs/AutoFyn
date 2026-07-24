## Statement

Fix any Liu Bang configuration $p_1,\dots,p_{n+1}>0$ (no assumption on shape —
this holds for the ladder, an arbitrary marking used in the upper-bound
direction, or any other configuration) and any composition
$(c_1,\dots,c_{n+1})$, $c_i\ge0$, $\sum c_i\le n$, of Xiang Yu's cut budget
among the pieces. Let $\bar\Omega$ be the closed, bounded, convex polytope of
all legal fragmentations of the pieces under this composition (a product of
closed simplices $\bar\Delta^{c_i}(p_i)$, one per piece, each simplex the set
of nonnegative $(c_i+1)$-tuples summing to $p_i$), and let
$\Phi=\pi\circ\sigma\circ\iota$ (equivalently $A$, since $\Phi=(1+A)/2$ is a
fixed affine reparametrization) be the induced continuous function of the
free parameters, where $\iota$ places the fragments, $\sigma$ sorts them into
descending order, and $\pi$ sums the odd-ranked (resp. alternates signs on)
entries. Then:

1. $\min_{\bar\Omega}\Phi$ exists (compactness + continuity).
2. It is attained at a **vertex** of the polyhedral subdivision of
   $\bar\Omega$ induced by the finitely many hyperplanes "fragment $u=$
   fragment $v$" — i.e. at a point pinned by $d$ (the free-parameter count)
   independent tight constraints, each either (I) "some fragment $=0$" (a
   degenerate cut — this vertex belongs to the closure of a *lower*
   composition) or (II) "two fragments are exactly equal" (an exact rank-tie,
   possibly between fragments of different original pieces, possibly
   involving an untouched piece).
3. Ranging additionally over the finitely many legal compositions, the global
   minimum of $\Phi$ over every legal Xiang Yu response is attained at one of
   finitely many such vertex configurations. The symmetric statement for
   $\max_{\bar\Omega}\Phi$ holds by the same argument with $\pi\to-\pi$.

## Proof

See `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`, §1
(Vertex-Minimum Theorem) and, independently,
`results/imo-2026-03/approaches/exchange-argument-extremal-response.md`,
Lemmas E1 and Theorem E3 (Vertex reduction) — two logically independent
derivations of the same fact.

Sketch: (a) *Existence*: $\bar\Omega$ is a finite union of compact simplices,
hence compact; $\Phi$ is continuous as the composition of the affine map
$\iota$, the sort map $\sigma$ (continuous — each order statistic is a finite
max-of-mins of continuous coordinates), and the linear functional $\pi$; a
continuous function on a compact set attains its minimum. (b) *Cell
decomposition*: the finitely many hyperplanes $\{y_{i,j}=y_{k,l}\}$, together
with the simplices' own facet hyperplanes $\{y_{i,j}=0\}$, subdivide
$\bar\Omega$ into finitely many closed convex polytopal cells $K_t$ (a finite
hyperplane arrangement intersected with a convex polytope yields a
polyhedral subdivision — standard fact). On each open cell, the sorted
permutation is constant, so $\Phi$ restricted to that cell is a fixed sum of
a subset of the (affine) fragment coordinates, hence affine; by continuity
of both $\Phi$ and this affine function and density of the open cell in its
closure, $\Phi|_{K_t}$ is affine on the whole closed cell $K_t$. (c) *Vertex
attainment*: the minimum of an affine function on a compact convex polytope
is a convex combination inequality — writing any point as a convex
combination of the (finitely many) vertices of $K_t$ shows $\Phi$ there is
$\ge$ the minimum over the vertices, with equality at a vertex — so
$\min_{K_t}\Phi=\min_l\Phi(v_l)$ (standard LP/convex-geometry fact: a linear
functional on a polytope attains its minimum at an extreme point). Every
vertex of $K_t$ is, by definition of a $0$-dimensional polyhedral face, cut
out by $d$ linearly-independent tight constraints drawn only from the two
available families (I) and (II) — there are no other facets of
$\bar\Omega=\prod\bar\Delta^{c_i}$. Taking the min over the finitely many
cells $K_t$ and then over the finitely many compositions gives the full
statement.

## Certification note (proof-reviewer, round 3)

Proved independently, via essentially the same convex-polytope/LP-vertex
argument, by two round-3 builders working from genuinely different outlines
(`rank-tie-vertex-reduction`'s "Vertex-Minimum Theorem" and
`exchange-argument-extremal-response`'s "Theorem E3") — a valuable
cross-check, not a gap: both derivations invoke only standard, checkable
convex-geometry facts (a bounded polyhedron is the convex hull of its
finitely many vertices; a linear functional on a polytope attains its
extremum at a vertex; a finite hyperplane arrangement subdivides a polytope
into finitely many convex cells), each justified in the source files rather
than asserted by appeal to intuition. Both derivations were exercised on the
same concrete instance — the $n=3$ ladder, composition "1 cut on $p_1$, 1
cut on $p_2$, $p_3,p_4$ untouched" — and independently identified the same
minimizing vertex ($a=p_2$, $b=p_4$, two type-(II) tie constraints),
matching a numeric grid search from this round's math-explorer; no
discrepancy found. Certified correct and fully general (no ladder-specific
or game-specific structure used; applies verbatim to the general upper-bound
direction with an arbitrary Liu Bang marking, and to the max-direction by
symmetry).

**What this does *not* establish (recorded so no future round overclaims):**
this theorem converts the continuous minimax problem into a search over
finitely many *candidate* vertex configurations per composition — it does
not bound how many candidates there are, characterize which are feasible for
the ladder's specific superincreasing values, nor evaluate $\Phi$ at any of
them. Evaluating a given vertex is handled by `odd-run-reduction-lemma`
(rank-ties routinely force several values into odd multiplicity
simultaneously, not just one); characterizing/enumerating the feasible
vertices for general $n$ remains open (see `current.md`).
