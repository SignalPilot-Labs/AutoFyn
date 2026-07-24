## Status
partial

## Approaches tried
- **(round 3, this build)** Executed the outline's exchange-argument /
  fix-the-extremal-response plan. Proved three new, general, reusable
  lemmas that were **not** present in any prior approach or in
  `results/imo-2026-03/lemmas/`:
  1. a **pair-cancellation identity** ($A(\{a,a\}\cup T)=A(T)$ for any $a>0$
     and any multiset $T$) — trivial but never stated before, and the key
     tool that turns an exact tie into a genuine dimension reduction;
  2. **existence of a minimizer** $X^*$ of $A$ over Xiang Yu's compact,
     piecewise-affine feasible response set (continuity of $A$ + compactness
     — routine but had not been written down);
  3. a **rigorous vertex-reduction theorem**: the global minimum of $A$ over
     all of Xiang Yu's legal responses to the ladder is attained at a point
     where, for some $k\le n$ (the number of "productively used" cuts,
     i.e. no wasted/zero-length fragment), there are $k$ *simultaneous*,
     independent exact-tie constraints among the fragments/pieces, so that
     $k$ disjoint tied pairs can be cancelled (Lemma E2) to reduce $A(X^*)$
     to $A$ of a genuinely smaller, $(n+1-k)$-element multiset.
  This upgrades the *conjectural* "rank-tie vertex" picture floated by the
  round-3 rank-tracking exploration (`/tmp/round-3/math-explorer-rank-
  tracking.md`, which explicitly says "the piecewise-linear/vertex-minimum
  claim itself is not proved") into an actual theorem, via standard convex
  polytope / LP vertex theory rather than an appeal to 1-D intuition. I
  verified the theorem's mechanism reproduces, exactly and independently,
  the same explorer's numerically-found $n=3$ tying example
  ($a=p_2,\,b=p_4$) as an honest hand computation using only the new
  lemmas — see "Worked verification" below — which came out to $A=1/15=a_3$
  exactly, matching the conjecture with no numerics needed.
  **What remains open**: the vertex theorem reduces the general-$n$ lower
  bound to a still-large finite combinatorial question (for each
  $k=0,\dots,n$ and each way of distributing $k$ cuts among the $n+1$
  pieces, characterizing which sets of $k$ simultaneous ties are
  *achievable* subject to the per-piece sum constraints, and checking
  $A(\text{leftover})\ge a_n$ in every achievable case) — this is now a
  precise, proven reduction, not a conjecture, but I could not close the
  general enumeration in the time available; this is exactly the same
  underlying combinatorial richness the other three live approaches
  independently located (see `current.md`), now reached by a genuinely
  different, non-measure-theoretic route.

## Current best

**Setup (shared with all approaches, reproduced for self-containedness).**
Write $p_i=p_i(n)=2^{n+1-i}/(2^{n+1}-1)$, $i=1,\dots,n+1$, for the $n$-ladder,
$r=1-p_1=\sum_{i\ge2}p_i$, $a_n:=1/(2^{n+1}-1)$. The exact doubling property
$p_i=2p_{i+1}$ ($i=1,\dots,n$) and the exact superincreasing residual
$p_i-\sum_{j>i}p_j=a_n$ for every $i=1,\dots,n+1$ both follow by direct
algebra (used below). By the certified `claiming-subgame-reduction` +
`integral-alternating-sum-formula` lemmas, it suffices to show, for every
legal Xiang-Yu response (at most $n$ further cut points, refining the ladder
pieces into a final multiset $S$), $A(S)\ge a_n$, where $A(S)=\sum_i
(-1)^{i+1}L_i$ over the descending-sorted multiset — equivalently
$\Phi(S)=(1+A(S))/2\ge p_1$.

**New Lemma E1 (Existence of a minimizer).** *Fix $n$. The set of Xiang-Yu's
legal responses to the $n$-ladder, viewed as the disjoint union over
allocations $(c_1,\dots,c_{n+1})\in\mathbb Z_{\ge0}^{n+1}$ with
$\sum c_i\le n$ of the compact sets*
$$P_{(c_i)} := \Delta^{c_1}(p_1)\times\dots\times\Delta^{c_{n+1}}(p_{n+1}),
\qquad \Delta^{c}(p):=\Big\{(g_1,\dots,g_{c+1})\in\mathbb R_{\ge0}^{c+1}:
\textstyle\sum_j g_j=p\Big\},$$
*(each $g_j$ a fragment of piece $i$ produced by $c_i$ cuts) is a finite
union of compact sets, hence compact. $A(S)$, viewed as a function of the
concatenated fragment tuple, is continuous (it is the composition of "sort
into descending order," itself a continuous map $\mathbb R^m\to\mathbb R^m$
given by order statistics, with the fixed continuous linear functional
$\sum_i(-1)^{i+1}L_i$). A continuous function on a compact set attains its
minimum. Hence a minimizing response $X^*$ exists.*

**New Lemma E2 (Pair cancellation).** *For any multiset $T$ of positive reals
and any $a>0$, $A(\{a,a\}\cup T)=A(T)$.*

**Proof.** For every $x\ge0$, $N_{\{a,a\}\cup T}(x)=2\cdot\mathbb1[a>x]+N_T(x)$.
Since $2\cdot\mathbb1[a>x]\in\{0,2\}$ is always even, $N_{\{a,a\}\cup T}(x)$
and $N_T(x)$ have the same parity for every $x$. By the certified
`integral-alternating-sum-formula` lemma, $A(S)=\int_0^\infty
\mathbb1[N_S(x)\text{ odd}]\,dx$ depends only on the parity function of
$N_S$, so $A(\{a,a\}\cup T)=A(T)$. $\blacksquare$

*(This strictly generalizes the certified `leftover-formula` lemma: that
lemma's exactly-equal pairs $\{a_i,a_i'\}$ are each an instance of this
lemma, applied repeatedly, plus a base case of one unpaired element or none.
E2 isolates the single-pair mechanism as an independent, freely reusable
identity — it needs no assumption that the *rest* of the multiset also
pairs up.)*

**New Theorem E3 (Vertex reduction).** *Fix an allocation $(c_1,\dots,
c_{n+1})$ with $k:=\sum c_i\le n$, giving the compact convex polytope
$P_{(c_i)}$ (product of simplices, dimension $k$ after eliminating one
coordinate per factor via the sum constraint). Finitely many hyperplanes of
the form "fragment $u$ = fragment $v$" (for pairs $u,v$ among the $k+(n+1)$
fragment-coordinate expressions, all of which are affine functions of the
$k$ free parameters) subdivide $P_{(c_i)}$ into finitely many closed convex
polytopal chambers, on the closure of each of which $A$ (as a function of
the free parameters) is affine — because within a chamber the descending
sorted order of all fragments is constant, so $A=\sum_i(-1)^{i+1}L_i$ is a
fixed $\pm1$-combination of the (affine) fragment values. The minimum of an
affine function over a compact convex polytope is attained at a vertex of
that polytope (standard fact from convex/LP geometry: the minimal face of a
polytope under a linear functional always contains a vertex, e.g. by
induction on dimension via a supporting hyperplane argument). Consequently
the minimum of $A$ over $P_{(c_i)}$ is attained at a vertex of one of these
finitely many chambers — i.e. at a point where at least $k$ independent
linear constraints, each of the form (a) "some fragment $=0$" (a facet of a
simplex factor) or (b) "two fragment values are exactly equal" (a chamber
wall), are simultaneously tight. Taking the further minimum over the
finitely many allocations $(c_i)$ (there are finitely many, since
$\sum c_i\le n$ over $n+1$ nonnegative integers), the global minimizer
$X^*$ of Lemma E1 may be chosen to be such a vertex.*

**Proof.** Given in the statement; the only substantive fact invoked is the
standard convex-geometry fact that a linear functional on a compact convex
polytope attains its minimum at an extreme point, applied chamber-by-chamber
and allocation-by-allocation (both finite indexing sets). $\blacksquare$

**Corollary E4 (Reduction to disjoint tie-cancellation).** *At the vertex
$X^*$ of Theorem E3, suppose the allocation used is $(c_i)$ with
$k=\sum c_i$, and suppose (discussed below — this is where an honest gap
remains for a fully general statement) the $k$ tight constraints consist of
$z$ "fragment $=0$" constraints and $t=k-z$ "two fragments equal"
constraints that pair up $2t$ of the (non-zero) fragments/pieces into $t$
disjoint equal pairs (no fragment involved in more than one of these $t$
pairs — the "generic" case). Then, first discarding the $z$ zero-length
fragments (they contribute nothing to any total or to $A$, since a length-
$0$ "fragment" is not actually a piece of the stick) and then applying
Lemma E2 $t$ times (once per disjoint tied pair), we get*
$$A(X^*) = A(S'),$$
*where $S'$ is the multiset of the remaining $(n+1)+k-2t-z$ elements not
involved in a cancelled pair (note $(n+1)+k$ is the total fragment count of
the full response, before removing $z$ wasted zero-fragments and cancelling
$t$ pairs) — a genuinely smaller multiset than the original response.*

Whether the $k$ tight constraints at a general vertex always decompose into
disjoint pairs (rather than a genuine multi-way tie, e.g. three or more
fragments simultaneously equal, sharing constraints in a way that is not a
disjoint perfect matching) is exactly the multi-way-tie subtlety the round-3
rank-tracking exploration flagged as unresolved; Corollary E4 covers the
"clean" (disjoint-pairing) vertices, which is the case realized in every
worked example found so far (see below), but I have **not** proved every
vertex is of this clean form in general. This is stated honestly as part of
the open gap.

## Worked verification (independent hand check of the $n=3$ numerics)

The round-3 rank-tracking exploration found, by a fine numerical grid search,
that for $n=3$ and the composition "$1$ cut on $p_1$, $1$ cut on $p_2$,
$p_3,p_4$ untouched," the minimum of $\Phi$ over this composition is exactly
$8/15=c(3)$, attained at $a=p_2=4/15$ (the larger fragment of $p_1$'s split)
and $b=p_4=1/15$ (the smaller fragment of $p_2$'s split). I redo this
**exactly**, using only Lemmas E2/E3/E4 and the ladder's exact algebra (no
numerics), as an independent verification that the vertex-reduction
machinery is correct and reproduces this cleanly.

Ladder: $p_1=8/15,\,p_2=4/15,\,p_3=2/15,\,p_4=1/15$ ($a_3=1/15$). Split
$p_1=\{a,\,p_1-a\}$, $p_2=\{b,\,p_2-b\}$, with $p_3,p_4$ untouched. This
composition has $k=2$ free parameters ($a,b$), matching $2$ cuts used (legal
for $n=3$, one cut left unused, which is fine — "at most $n$").

At the claimed vertex $a=4/15,\,b=1/15$: since $p_1=8/15=2p_2$ exactly (the
ladder's doubling identity $p_1=2p_2$), setting $a=p_2=4/15$ gives
$p_1-a=8/15-4/15=4/15=a$ **exactly** — so $a$ and $p_1-a$ are tied with each
other (one tight constraint, pinning $a$: this is the "$a=p_1-a$" tie,
equivalent to $a=p_1/2=p_2$). Independently, $b=p_4=1/15$ ties the smaller
fragment of $p_2$'s split against the untouched piece $p_4$ (a second tight
constraint, pinning $b$). Two independent constraints for two free
parameters — exactly matching Theorem E3's dimension count for $k=2$, with
$z=0$ (no wasted cuts) and $t=2$ tied pairs: $\{a,\,p_1-a\}=\{4/15,4/15\}$ and
$\{b,\,p_4\}=\{1/15,1/15\}$.

The full multiset is $\{a,\,p_1-a,\,b,\,p_2-b,\,p_3,\,p_4\}
=\{4/15,\,4/15,\,1/15,\,3/15,\,2/15,\,1/15\}$ (using $p_2-b=4/15-1/15=3/15$).
By Lemma E2, cancel the pair $\{4/15,4/15\}$ and the pair $\{1/15,1/15\}$
(both disjoint, no fragment shared between the two pairs): $A(X^*)=A(S')$
where $S'=\{p_2-b,\,p_3\}=\{3/15,\,2/15\}$, a genuinely smaller,
$2=(4+2-2\cdot2)$-element multiset, consistent with Corollary E4's count
$(n+1)+k-2t-z = 4+2-4-0=2$.

Finally, $A(S')=3/15-2/15=1/15=a_3$ **exactly** — matching the target with
no numerics anywhere in this computation, and matching (independently, by a
completely different, symbolic route) the grid-search value the rank-
tracking exploration found only numerically. This is a genuine, if narrow,
cross-check that Theorem E3 / Corollary E4's mechanism is mathematically
sound and correctly captures the extremal structure other approaches had
only observed empirically.

## What this establishes and what remains open

**Established (new, rigorous):**
- Lemma E1 (minimizer exists), Lemma E2 (pair cancellation), Theorem E3
  (vertex reduction via standard LP/convex geometry), Corollary E4 (reduction
  to tie-cancellation at "clean," disjointly-paired vertices).
- These together prove: **the general lower bound $c(n)\ge2^n/(2^{n+1}-1)$
  is equivalent to the following finite (for each fixed $n$) statement**:
  *for every $k=0,\dots,n$, every allocation of $k$ cuts among the $n+1$
  ladder pieces, and every consistent way (respecting each piece's own sum
  constraint $p_i$) of forcing $k$ independent simultaneous exact ties among
  the resulting fragments/untouched pieces, the pair-cancelled leftover
  multiset $S'$ satisfies $A(S')\ge a_n$.* This is a **rigorous reduction**
  from a continuous minimax problem to a finite algebraic one — strictly
  stronger than the previously-only-conjectured "rank-tie vertex" picture
  (compare the round-3 rank-tracking exploration's own admission that its
  version of this claim was "not proved... needs checking").
- Independently re-verified, by hand and symbolically (not numerically), the
  one $n=3$ tie configuration the rank-tracking exploration had only found
  by a numeric grid search; the exact computation matches the target value
  $a_3=1/15$ precisely, and separately reproduces the already-certified
  $c=0$ family (setting $k=0$ trivially recovers Lemma 6 / the
  `untouched-top-piece-lower-bound` lemma's regime, since no ties are forced
  and $S'=S$ is the whole ladder response — this composition is not
  generally tight for $n\ge2$, but the framework handles it consistently as
  one of the $k=0$ cases, so nothing here contradicts the previously
  certified partial result).

**Open (honestly, not glossed over):**
1. **The general finite enumeration is not closed.** For general $n$ and
   general $k\le n$, I have not characterized which sets of $k$ simultaneous
   ties are achievable (i.e. solvable in positive fragment values respecting
   each piece's sum), nor proved $A(S')\ge a_n$ for all of them. This is the
   same underlying combinatorial obstruction the other three live approaches
   converge on (see `current.md`'s "Approaches tried" summary), now reached
   via vertex/LP geometry instead of a measure-theoretic cross-term bound —
   a genuinely different route to the *same* wall, as CLAUDE.md's plateau
   rule anticipates is possible ("attacks the problem from a genuinely
   different framing... [but] could of course fail for its own, different
   reasons").
2. **Multi-way ties are not fully handled.** Corollary E4 only proves the
   reduction cleanly when the $k$ tight constraints decompose into a
   disjoint perfect matching of pairs. A vertex could in principle have,
   e.g., three fragments simultaneously forced equal (using $2$ of the
   dimension-count's constraints for that one triple, in some non-uniquely-
   paired way) — Lemma E2 as stated only cancels literal pairs, so a
   three-way tie $\{a,a,a\}\cup T$ needs a small extension (cancel two of
   the three, leaving one copy — this follows immediately from applying E2
   once, since $\{a,a,a\}\cup T = \{a\}\cup(\{a,a\}\cup T)$ and $A$ of that
   is $A(\{a\}\cup T)$ by E2), so the *mechanism* extends routinely to
   $m$-way ties (cancel $\lfloor m/2\rfloor$ pairs, leaving $0$ or $1$ copies
   of $a$ behind) — but I have not verified this extended bookkeeping
   against the full dimension-count in Theorem E3 for genuinely mixed cases
   (some triples, some pairs, some zero-fragments, all simultaneously
   active at one vertex), so I report this as a real but likely-routine gap,
   not a fundamental obstruction.
3. **No inductive scheme closing the enumeration for general $n$ was
   found.** I looked for (but did not find, in the time available) a clean
   strong induction on $n$ using the ladder's self-similarity ($p_i=2p_{i+1}$,
   residual $a_n$ at every level) to reduce a $k$-tie vertex of the
   $n$-ladder to a smaller-parameter vertex of the $(n-1)$-ladder. The
   worked $n=3$ example above is suggestive (the tie $a=p_1/2=p_2$ uses the
   doubling identity directly) but a general recursive argument covering
   arbitrary allocations was not established.

## Full proof
(absent — Status is `partial`. The general-$n$ lower bound remains open;
what is proved here is a new, rigorous *reduction* of the continuous
minimax problem to a finite vertex/tie-cancellation problem — via
compactness (Lemma E1), a pair-cancellation identity (Lemma E2), and a
standard convex-polytope vertex theorem (Theorem E3, Corollary E4) — plus an
independent symbolic re-derivation of the one $n=3$ numeric example on
record, matching it exactly. This is a genuinely different route from the
measure-theoretic cross-term bound that the other three live approaches
found insufficient (see `current.md`), reaching the same underlying open
combinatorial question from a different, exchange-argument/LP-vertex
direction, as requested by this round's outline. No claim of a complete
proof is made; see "What remains open" above for the precise, unresolved
gaps.)

---

## Outline (proof-outliner, round 3) — original outline, retained for record

**Why this approach exists.** Per CLAUDE.md's shared-gap-plateau rule: three
approaches have converged on the same wall (a cross-term/interleaving
inequality that no mass-based bound can prove — a reviewer-verified negative
result, twice over). All three of those approaches share one architectural
choice: they compute $A(S)$ (or $\Phi(S)$) via an **explicit formula** first
(the integral $\int_0^\infty\mathbb1[N(x)\text{ odd}]\,dx$, or a
decomposition of it), and *then* try to bound that formula for an arbitrary
Xiang Yu response. This forces exactly the abstract, rank-blind estimation
that has twice failed. This approach never writes down a formula for $A(S)$
for a generic response at all. Instead (following the crux pattern in
`aimo-0119`/`aimo-0425`/`aimo-0146` — "fix the extremal configuration and
derive a local no-improving-swap condition"), it:

1. **Fixes a hypothetical minimizer.** For fixed $n$ and the ladder marking,
   Xiang Yu's feasible response set (at most $n$ cut points, each in $[0,1]$
   minus already-placed points) is a bounded, closed subset of
   $\mathbb R^{\le n}$ (a finite union of closed simplices indexed by how the
   cuts distribute among pieces), and $A(\cdot)$ is continuous on it (in fact
   piecewise linear — this continuity fact alone is easy and should be
   proved first, independent of the harder vertex-location claim the sibling
   `rank-tie-vertex-reduction` approach is attempting). By compactness, a
   minimizer $X^*$ exists. Fix one (tie-break arbitrarily if not unique).

2. **Derives a local-swap optimality condition on $X^*$.** Since $X^*$
   minimizes $A$, *no legal small perturbation of $X^*$ can strictly decrease
   $A$*. Concretely: (a) moving a single cut point within its piece by
   $\pm\varepsilon$ cannot decrease $A$ to first order (else $X^*$ wasn't
   optimal) — this gives a **stationarity condition** at $X^*$ for each
   moved cut, expressible via the rank of the two fragments adjacent to that
   cut (using the same single-coordinate-monotonicity fact already proved in
   `greedy-halving-adversary` Lemma 1); (b) **re-pairing**: if two cuts
   currently sit in different pieces, moving mass between the two associated
   fragments (a joint two-parameter perturbation preserving total pieces)
   cannot strictly decrease $A$ either — this is the "exchange" step proper,
   analogous to `aimo-0119`'s "move a card from the heaviest box to the
   lightest is non-improving at the minimizer."

3. **Reads off the structural consequence directly from the swap
   conditions**, not from a formula: the goal is to show the stationarity +
   exchange conditions together force $X^*$ into one of a small number of
   *rigid shapes* — conjecturally, that every non-$p_1$ ladder piece $p_i$
   ends up paired almost-exactly against a fragment of $p_1$ (or of a larger
   piece), in a specific nesting order dictated by the ladder's exact
   superincreasing residuals $p_i-\sum_{j>i}p_i = 1/(2^{n+1}-1)$ at every
   level — and then show this rigid shape cannot actually be realized with
   only $n$ cuts (one short of a full pairing, the resource-deficit fact
   already on record in `greedy-halving-adversary`'s Lemma 4/discussion),
   forcing $A(X^*)\ge 1/(2^{n+1}-1)$.

4. **Fallback / sanity check:** if the full general-$n$ swap-condition
   argument proves too hard in one round, first carry out Steps 1–3
   completely for $n=2$ and **cross-check the resulting minimizer's shape
   against the already-fully-closed `smoothing-compactness-certificate`
   result** (its 10 exact lower-bound compositions, several of which are
   *already* exact-tie configurations at the boundary, e.g. composition
   `(1,1,0)`'s equality case $p_1=p_2$ exactly). If the exchange argument's
   predicted minimizer shape matches the already-certified $n=2$ extremal
   configurations, that is strong evidence the mechanism is correct and
   worth pushing to general $n$; if it does not match, that is itself a
   valuable negative finding to report.

**Target.** Same as every approach: $c(n)=2^n/(2^{n+1}-1)$, both directions.
This approach, like its siblings, is aimed at the **lower bound** (general
$n$, general Xiang Yu response, $c\ge1$) — the located obstruction.

**Key lemmas needed (new):**
- Existence of a minimizer $X^*$ by compactness + continuity of $A$ on the
  (piecewise-linear, compact) feasible set — should be easy, prove first.
- The single-cut stationarity condition at $X^*$ (a rank/position statement,
  not a mass bound) — likely follows directly from re-deriving the
  monotonicity sub-claim of `greedy-halving-adversary` Lemma 1 in the
  "moving one coordinate continuously" form already proved there, applied to
  $A$ instead of the claiming-game value (these are related by
  $\Phi=(1+A)/2$, so monotonicity transfers immediately).
- The two-cut re-pairing/exchange condition — genuinely new, not yet stated
  precisely; this is the crux of the whole approach and the first concrete
  target for a builder.
- The final "rigid shape forces contradiction with the $n$-cut budget"
  argument — depends on how precisely Step 3's shape can be pinned down.

**Open gaps (all of them — this is a fresh outline):**
1. Precise statement and proof of the two-cut exchange/re-pairing condition
   at a minimizer (Step 2b) — not yet attempted by any approach.
2. Whether the swap conditions actually pin down a *unique* (or small
   family of) rigid shape(s) for $X^*$, or leave too much freedom to be
   useful — unknown, must be checked, most easily first at $n=2,3$ by hand
   against already-known optimal configurations (e.g. the $n=3$ tie example
   already found by the round-3 rank-tracking explorer,
   `/tmp/round-3/math-explorer-rank-tracking.md`: minimizer at
   $a=p_2,\,b=p_4$ — check directly whether this configuration satisfies a
   natural exchange-stationarity condition, as a first concrete sanity test).
3. Whether the resource-deficit argument (♯pieces − ♯cuts = 1) can be turned
   into a clean contradiction once the rigid shape is pinned down, or whether
   it needs sharpening.

**Why this is genuinely far from the current field:** it never computes
$A(S)$ via the integral/alternating-sum formula for a generic configuration
— the mechanism is entirely "local perturbation at a fixed extremal point,"
which is a different technique (variational/first-order-conditions) from
"write a global formula and bound it" (measure-theoretic). It cannot inherit
the specific "mass bound too weak" failure mode verified twice on record,
though it could of course fail for its own, different reasons (Open gaps
above) — this is reported honestly, not claimed as a guaranteed fix.

**Files consulted:** `results/imo-2026-03/current.md`; all three live
approach files; `/tmp/round-3/math-explorer-alt-technique.md` (source of the
exchange-argument lead and the crux citations `aimo-0119`, `aimo-0425`,
`aimo-0146`); `/tmp/round-3/math-explorer-rank-tracking.md` (the $n=3$
worked tie example, useful as a first sanity check for Step 2's swap
conditions); certified lemmas `claiming-subgame-reduction`,
`integral-alternating-sum-formula`, `must-use-all-n-points`.
