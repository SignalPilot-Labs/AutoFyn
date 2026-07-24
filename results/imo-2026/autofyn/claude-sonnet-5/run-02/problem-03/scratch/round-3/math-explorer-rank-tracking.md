# Math-explorer report — lens: RANK-TRACKING (round 3)

## Summary verdict

Rank-tracking is not a new idea layered on top of the existing machinery —
**it is already the native language of the whole problem**: the reduction
functional $\Phi(S)=\Sigma_{\text{odd sorted rank}}$ and its twin $A(S)$
(Lemma 1/2 in `greedy-halving-adversary.md`) are *defined* by rank parity,
and Lemma 8's cross term $\int_0^r u v\,dx$ is already exactly "does an
odd-rank-count coincidence occur between the two groups." So the open gap
is not "we forgot to track rank, only mass" — the existing approaches DO
track rank, via an integral encoding. What is missing is a genuinely
different way to *bound* that same rank-parity correlation: not a mass
estimate (proved too weak, `self-similar-potential-certificate.md`,
`greedy-halving-adversary.md` Prop 10) but a **structural/positional**
argument. Below I lay out the most promising structural idea I found, with
concrete $n=3$ numerics supporting it, plus what a closing lemma would need
to state, and what I could **not** get to work.

## The plausible mechanism: extremal configurations are rank-tie points

**Key observation.** For a fixed composition of Xiang Yu's cut budget (which
pieces get cut, how many times each), $\Phi$ is a **piecewise-linear**
function of the free cut positions (the sorted order only changes across
finitely many hyperplanes where two fragment values become equal — a rank
collision). A piecewise-linear function on a compact polytope attains its
minimum either on the polytope's boundary (a fragment shrinking to $0$ or a
cut budget going unused — already the territory of the `untouched-top-piece`
/ $c{=}0$ case) **or at a vertex of the linear-region decomposition**, i.e.
at a point where two fragments (possibly from *different* original pieces —
exactly the "interleaving" configurations that are the open gap) are
**exactly equal**.

This matches every piece of hard evidence already on file:

- **$n=2$, composition $(1,1,0)$** (`smoothing-compactness-certificate.md`,
  lines ~169-238): the infimum $\Phi\to 4$ (units of $1/7$) is approached
  exactly as $p_1\to p_2$ — a rank-tie between the two fragments of the cut
  pieces.
- **$n=1$** (`greedy-halving-adversary.md`, Open gap §3, the worked example):
  the optimal Liu Bang point $x=1/3$ is exactly the value where "bisect"
  and "pair with the small piece" tie ($\,(1+x)/2 = 1-x\iff x=1/3\,$), and at
  that tie point *every* single cut of the big piece gives exactly $\Phi=2/3$
  — a flat degenerate vertex.
- **My own $n=3$ experiment** (composition: 1 cut on $p_1$ giving fragments
  $a, p_1{-}a$; 1 cut on $p_2$ giving $b, p_2{-}b$; $p_3,p_4$ untouched — a
  genuinely *interleaving* case, not the closed $c=0$ case): a fine grid
  search ($200\times200$, exact `Fraction` arithmetic) over $a\in(0,p_1)$,
  $b\in(0,p_2)$ finds the **global minimum of this composition is exactly**
  $\Phi = 8/15 = c(3)$, attained at
  $$a = p_2 = 4/15,\qquad b = p_4 = 1/15,$$
  i.e. exactly at the point where the fragment of $p_1$ **matches $p_2$
  exactly** and the fragment of $p_2$ **matches $p_4$ exactly** — a double
  rank-tie / exact-pairing configuration. At that exact point, the
  configuration is $\{p_2, p_1-p_2, p_4, p_2-p_4, p_3, p_4\}$
  $=\{4/15,4/15,4/15,3/15,2/15,1/15\}$ (three copies of $4/15$!), and one can
  check directly this is a `leftover-formula` (Lemma 3) instance up to the
  repeated-value edge case. The minimum is **attained exactly**, not just
  approached, and it **exactly equals the target** $c(3)$ — no violation,
  consistent with the conjecture, and structurally at a matching vertex, not
  in the "generic" interior of the interleaving region where the failed mass
  bounds were being tested.

## What the closing lemma would need to state

If the vertex-minimum picture is right, the general lower bound reduces from
"a min-of-continuum inequality, hard to bound by mass" to a genuinely
different and more tractable-looking claim:

**Candidate Lemma (Rank-tie reduction).** *For a fixed composition of Xiang
Yu's cut budget (which of the $n{+}1$ ladder pieces are cut, and how many
times each), the infimum of $\Phi$ over all legal free cut positions is
attained in the limit at a boundary point of the parameter polytope at which
either (a) some cut is not used (fragment $\to 0$), or (b) two fragments —
possibly belonging to two different original pieces — become exactly equal.
Consequently it suffices to check $\Phi\ge c(n)$ only at this finite
(though combinatorially large, see below) set of exact-matching
configurations, each of which reduces via the `leftover-formula` /
`dominant-element-removal-identity` machinery to an **algebraic identity in
the $p_i$'s**, not an optimization.*

This would replace "prove a positive-correlation/anti-concentration
inequality on two independently-optimized parity indicator functions"
(the currently-stated open gap) with "enumerate the finitely many ways
fragments of the ladder's pieces can be forced into exact equalities
consistent with a fixed cut budget, and check the resulting leftover value
in each case" — a combinatorial statement in the same spirit as (and
possibly literally equivalent to) the `greedy-halving-adversary.md` Open
gap §1 "subset-sum / matching residual-minimization" framing, but now
justified as the *actual* extremal locus (via a rank-collision/vertex
argument) rather than merely a numerically-observed pattern.

## Why this is genuinely a different route from what already failed

The three prior approaches all tried to **bound** the cross term
$\int_0^r u'v\,dx$ (or the equivalent "insertion into sorted order" shift)
by a *quantity* — a mass estimate, a monotonicity estimate — and found the
resulting bound too weak. The rank-tie idea instead tries to avoid bounding
the cross term at all: it claims the minimum is not found by making the
cross term small in some averaged/generic sense, but is achieved (or
approached) at isolated points forced by **exact rational coincidences**
between subset sums of the $p_i$'s and of Xiang Yu's chosen cut values — and
at those points $\Phi$ collapses to a clean closed form via Lemma 3
(leftover formula), sidestepping the cross-term integral altogether. This is
an "extreme point of a linear-programming-like feasible region" argument
(the smoothing-compactness-certificate file's round-1 "6 template
strategies + LP-contradiction" already implicitly uses exactly this
philosophy for the *upper* bound at $n=2$ — worth noting the rank-tie idea
is really the natural general-$n$ lower-bound mirror of that already-proven
upper-bound technique).

## What I could NOT establish (open even at the level of a plausible lemma)

1. **The piecewise-linear/vertex-minimum claim itself is not proved.** It is
   geometrically very plausible (min of piecewise-linear function on a
   compact polytope) but the "polytope" here is really a union of polytopes
   glued along rank-collision walls, of complexity that grows with $n$ (the
   number of distinct sorted-order regions for $n$ free cut parameters can
   be large), and I did not verify that the boundary strata are correctly
   characterized as "some pair exactly equal" in every case (there could be
   more exotic vertices, e.g. three-way ties, or non-vertex minima if $\Phi$
   is not strictly convex/concave on some region — this needs checking, not
   just assumed by analogy with 1-D LP intuition).
2. **Even granting the reduction, the resulting finite combinatorial
   problem is not obviously small.** "Which subsets of $p_i$'s and their
   fragments can be forced into exact equalities" is combinatorially rich
   (partitions of a cut budget across $n{+}1$ pieces, times which fragments
   pair with which) — this is structurally the same enumeration difficulty
   flagged in `greedy-halving-adversary.md` Open gap §1 and
   `smoothing-compactness-certificate.md`'s "slot decomposition" sketch
   (see its lines ~344-365, which independently proposes almost exactly this
   idea under the name "slot decomposition": untouched pieces act as fixed
   pivots partitioning the sorted order into slots, with a per-slot
   "median"-like rank correction). **My rank-tracking lens and the
   smoothing-compactness approach's slot-decomposition sketch appear to be
   the same idea approached from two directions** — this convergence is
   itself informative (two independent routes landing on "reduce to a
   finite exact-matching/pivot combinatorics problem") but neither has
   proved it for general $n$.
3. I did not find an inductive scheme (on $n$) for the vertex/tie
   enumeration — this is the natural next step (the ladder's self-similarity,
   already used successfully for the $c=0$ case via `ladder-self-similarity-
   constant`, suggests the tie-configurations at level $n$ should decompose
   into a "top-level tie" plus a tie-configuration for the rescaled
   $(n{-}1)$-tail, but I did not verify this recursion holds even in the one
   $n=3$ example computed above).

## Recommendation for the outliner

This lens is worth a dedicated approach/build slot: **"rank-tie vertex
reduction."** It is not a rehash of the mass-based attempts (it explicitly
avoids bounding the cross-term integral) and it is corroborated by concrete,
independently-reproducible numerics at $n=1,2,3$ (all cited above are either
already-certified results or freshly computed here with exact `Fraction`
arithmetic — script available on request, trivial to reproduce). Concretely
the next builder should attempt, in order:
(a) prove the piecewise-linear-vertex-minimum claim rigorously for a fixed
cut-budget composition (this is a general fact about $\Phi$ as a function of
finitely many linear cut parameters, likely provable directly from Lemma 1's
monotonicity sub-claim — decreasing/increasing a single fragment while
compensating another is exactly a one-parameter deformation whose effect on
$\Phi$ was already analyzed in Lemma 1's proof of `greedy-halving-adversary.md`);
(b) if (a) holds, connect to `smoothing-compactness-certificate.md`'s "slot
decomposition" sketch to try to close the enumeration for general $n$ by
induction using the ladder's self-similarity, rather than raw case-count
(which the smoothing approach already flagged as not scaling).

## Files consulted

- `results/imo-2026-03/current.md`
- `results/imo-2026-03/approaches/greedy-halving-adversary.md` (Lemmas 1-9,
  Proposition 10, Open gaps)
- `results/imo-2026-03/approaches/self-similar-potential-certificate.md`
  (Lemma B, the interleaving negative result)
- `results/imo-2026-03/approaches/smoothing-compactness-certificate.md`
  (the $n=2$ mixed-composition closures and the "slot decomposition" sketch,
  lines ~153-280 and ~344-365)
- `results/imo-2026-03/lemmas/cross-term-identity-threshold.md`,
  `dominant-element-removal-identity.md`, `n2-lower-bound-full-closure.md`
- Fresh computation: exact-`Fraction` grid search, $n=3$ ladder, composition
  (1 cut on $p_1$, 1 cut on $p_2$, $p_3,p_4$ untouched); global minimum found
  exactly at $\Phi=8/15=c(3)$, at the tie point $a=p_2$, $b=p_4$.
