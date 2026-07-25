## imo-2026-03

self-similar-induction-on-n: revise
Target: `T(m)` for all `m≥3` — the full lower-bound direction (LB's geometric
partition guarantees `OddSum ≥ c(n)` against every XY response).
Technique: exchange/smoothing (majorization) proof of the new target
`Case-B(m,k)`, extending the already-certified Reduction B, using the
crux template from `aimo-0146` (exchange-smoothing weight toward
higher-coefficient positions until the free coordinates equalize) and
`aimo-0119` (single-transfer exchange at an assumed extremal configuration).
Skeleton:
  1. Import certified **Reduction B**: whenever the top fragment `b1<μ:=max(S)`,
     `OddSum(B∪S)≥2^m ⟺ OddSum(B∪S')≤2^m-1` where `S'=S∖{μ}` — by
     `Global-max Peeling` on `μ` (already proved in full, this file).
  2. **Specialize to TOP-ONLY** (`S=Γ_{m-1}` untouched): then `μ=2^{m-1}`
     *exactly* (not merely `≤`), so `S'=Γ_{m-2}` exactly and the trichotomy's
     "middle regime" (`μ≤b1<2^{m-1}`) is **vacuous** here — TOP-ONLY splits
     cleanly into just Case A (`b1≥2^{m-1}`, already closed by
     `greedy-reduction-geometric`'s **Dominant-Chain Theorem**, a genuinely
     non-circular closure distinct from Proposition C's dead single-peel
     route — cross-check this distinction explicitly, do not conflate the
     two) and Case B (`b1<2^{m-1}`, reduces via step 1 to the single clean
     target below, uniformly over all violation depths `d≥1`, not case-by-case).
  3. **Target: `Case-B(m,k)`:** for every partition `B` of `2^m` into `≤m`
     positive parts with `max(B)<2^{m-1}`, `OddSum(B∪Γ_{m-2})≤2^m-1`.
  4. Prove the extremal shape: numerics (this round's lowerbound explorer)
     find the near-extremizer `B_ε=(2^{m-1}-ε,\,2^{m-2},\ldots,2,\,1+ε)`
     (i.e. `Γ_{m-1}` itself with its top nudged down by `ε` and the freed
     mass parked on the bottom element), with `OddSum(B_ε∪Γ_{m-2})→2^m-1`
     from below as `ε→0^+` — a supremum, never attained (consistent with
     the strict hypothesis `max(B)<2^{m-1}`).
  5. Prove `Case-B(m,k)` via a single-transfer exchange argument (the
     `aimo-0119` template): assume `B` is a maximizer; use the certified
     **Single-Insertion Lemma** to compute the *exact* `ΔOddSum` of moving
     one unit of mass from a non-extremal coordinate of `B` toward the
     nearest "geometric slot" `2^i`; show this move is weakly
     non-decreasing toward the conjectured `B_ε` shape, forcing every
     maximizer to converge to it; then verify the bound directly at the
     limit shape via the already-certified `AltSum(Γ_m)` closed-form
     machinery (telescoping geometric series).
  6. Combine: TOP-ONLY is now fully closed for every `m` (Case A via
     Dominant-Chain, Case B via `Case-B(m,k)`). Report honestly that the
     fully general Case 2 (tail *also* cut, so `μ<2^{m-1}` strictly and
     the middle regime is genuinely non-vacuous) remains completely open —
     hand this off explicitly to `greedy-reduction-geometric`'s revised
     target below, do not attempt both in this file.
Key lemmas (claim + mechanism):
  - Reduction B (certified) — because peeling the tail's true max `μ`
    converts an `OddSum≥` target into an `OddSum≤` target on a one-smaller
    tail, via the Global-max Peeling identity.
  - `Case-B(m,k)` extremal shape — because among sorted vectors of fixed
    sum and a max-cap, the rank-weighted `OddSum` functional is maximized
    by pushing mass toward the boundary "as geometric as possible" shape,
    provable by a single-transfer exchange (moving mass toward `2^i` never
    decreases `OddSum`, by the exact `ΔOddSum` formula from the
    Single-Insertion Lemma).
Open gaps: step 5 (the exchange argument closing `Case-B(m,k)`) is the
real target this round — everything before it is already proved or newly
diagnosed as reducible. The fully general (non-TOP-ONLY) middle regime is
explicitly out of scope for this file this round.
Cases to cover: `Case-B(m,k)`'s exchange argument must handle (a) ties
among `B`'s coordinates during the transfer, (b) the boundary behavior as
`b1→(2^{m-1})^-` where the bound is tight (no slack to exploit there,
per the explorer's numerics — `d=1`-adjacent instances need a sharp, not
generous, argument), (c) `B` with fewer than `m` parts (budget not fully
used).
Watch out for: do NOT re-derive Proposition C's circular single-peel route
by accident inside the exchange argument — the transfer step must move
mass *within* `B`, not re-invoke the peeling-on-`B'` recursion; also verify
Dominant-Chain Theorem's Case A closure is independent of Proposition C
(it is, by construction, but state this cross-check explicitly since two
different "Case A" arguments now coexist in the population).

greedy-reduction-geometric: revise
Target: the fully general lower-bound Case 2 — XY spends cuts on **both**
LB's top piece `r_n` *and* the tail `r_0,\ldots,r_{n-1}` simultaneously
(not just TOP-ONLY, which is being closed by `self-similar-induction-on-n`
above) — i.e. close `self-similar-induction-on-n`'s genuinely open "middle
regime" (`μ≤b1<2^{m-1}`, arising only when the tail is itself cut so
`μ<2^{m-1}` strictly).
Technique: extend the certified **Dominance-Chain property** and
**Prefix-Run Peeling Decomposition** to a *joint* chain spanning both the
top-piece fragments and the tail's own fragments in their true merged sort
order, rather than treating "top fragments vs. exact `Γ_{m-1}`" as two
separate objects.
Skeleton:
  1. Import (once certified this round) `self-similar-induction-on-n`'s
     `Case-B(m,k)` and `greedy-reduction-geometric`'s own **Dominant-Chain
     Theorem** — together these close TOP-ONLY completely; treat this as
     the base case (`c=0` tail cuts) of the induction below.
  2. Set up the joint problem: `B={b_1\ge\cdots\ge b_{j+1}}` partitions
     `2^m` (`j` cuts spent on top), `S$ is an *actual* refinement of
     `Γ_{m-1}` using `c\ge1` further cuts (`j+c\le m`), so
     `μ:=max(S)<2^{m-1}` strictly whenever the tail's own top piece
     `2^{m-1}` itself got split.
  3. Define a **Joint Dominance-Chain property**: extend the existing
     definition (currently only over `B`'s own fragments vs. powers of
     `2`) to the *actual merged descending sequence* of `B\cup S`,
     requiring each successive element to dominate at least half of the
     remaining total mass — the natural generalization of "`a_1\ge
     2^{m-1}`" to a setting where the comparison target is no longer a
     fixed power of `2` but the *actual* running sum of `B\cup S` at each
     peel step.
  4. Attempt the peeling induction on this joint chain: at each step, peel
     the current joint-maximum (whichever of `B` or `S`'s remaining
     elements is largest), and show the residual invariant ("removed mass
     from the max element is `\ge` half the residual total") propagates —
     this is a genuine strengthening of Theorem 5's proof, not a restatement,
     since the "opponent" at each step can now come from either side.
  5. Identify precisely where (if anywhere) this joint induction breaks —
     honestly diagnose a new obstruction if the invariant fails, in the
     same spirit as Proposition C, rather than asserting success.
Key lemmas (claim + mechanism):
  - Joint Dominance-Chain closure (candidate) — because the original
    Theorem 5's telescoping peel argument used only "current max dominates
    half the remaining total," a property that does not inherently care
    whether the max comes from `B` or `S`, so the same telescoping *might*
    extend — but this must be checked, not assumed, since the tail's
    contribution is no longer the fixed sequence `Γ_{m-2},\ldots` after the
    first peel (it can itself be an arbitrary sub-refinement).
Open gaps: the entire middle regime — this is a fresh, previously
unattempted target, not a rescoping of a killed lemma. Everything in the
skeleton beyond step 1 (import) is new work.
Cases to cover: `j` (top cuts) and `c` (tail cuts) range independently
subject to `j+c\le m`; must cover every split of the budget, including
`c=1` (single tail cut) as the base non-trivial case before attempting
general `c`.
Watch out for: this is the natural place the joint induction could
silently rediscover Proposition C's circularity (peel-and-recurse into an
equally-hard instance) — explicitly check, at each induction step, that
the residual sub-problem has *strictly fewer* total fragments or a
*strictly smaller* scale than the original, not just "looks similar."

universal-halving-adversary: revise
Target: the full upper-bound direction, specifically closing the balanced
region `p1<1/2` **and** `p_{n+1}>1/(2^{n+1}-1)`.
Technique: explicit multi-piece coordinated construction combining the two
coupling mechanisms this round's coupling-lens explorer catalogued —
**self-bisection** (split one piece exactly in half, using certified
Tie-neutrality to guarantee an exact 1-1 split of its own value) and
**shave-below** (split a larger piece into fragments each tuned to sit
just below a *distinct* untouched anchor piece, landing at even/wasted
ranks) — guided by the (conjectural, to be used as a design heuristic
here and proved rigorously by `dyadic-potential-invariant` below) tie-or-
zero structure of optimal responses.
Skeleton:
  1. Import certified Doubling Lemma, General Insertion Lemma, and
     Subadditivity Lemma (all already proved, this file).
  2. Formalize the **shave-below** move precisely: splitting a piece `p`
     into `(t-\varepsilon,\,p-t+\varepsilon)` for a chosen anchor value
     `t<p` (an untouched piece elsewhere in the multiset) places the
     smaller fragment `\varepsilon`-below `t` in sort order; in the exact
     limit `\varepsilon\to0^+`, this is a genuine tie-block computable via
     the certified Tie-neutrality Lemma (no limiting argument actually
     needed if `t` is chosen so the fragment lands exactly at rank
     "just after" the anchor — verify this is achievable at `\varepsilon=0$
     itself, i.e. set the smaller fragment to literally equal an existing
     value one rank below the anchor, sidestepping the limit).
  3. Build the general construction: given a balanced sorted partition
     `p_1\ge\cdots\ge p_{n+1}`, designate a subset of pieces as "anchors"
     (left untouched) and pair each remaining piece with a distinct anchor
     via shave-below, self-bisecting any leftover pieces that have no
     anchor to pair with. Reproduce the two worked examples found by this
     round's explorers exactly as a correctness check: `n=2`,
     `(0.35,0.34,0.31)` (bisect `p_3` alone, or the two-cut mixed move,
     both giving `0.505`); `n=3`, `(0.3605,0.2782,0.2013,0.16)` (shave `p1`
     against two distinct anchors `p3,p4` plus self-bisect `p2`, giving
     `≈0.5004`).
  4. Derive the general achieved-value formula for this construction (a
     closed form in terms of which pieces are anchors vs. shaved vs.
     self-bisected) using the Single-Insertion Lemma (certified,
     `self-similar-induction-on-n`) to track each shave's exact rank
     contribution.
  5. Prove a **matching/counting rule** for how to choose the anchor
     assignment given a budget of `n` cuts, and prove the resulting value
     is `\le c(n)` for *every* balanced partition, not just the worked
     examples — likely via an inductive assignment (largest unpaired piece
     gets shaved against the largest available anchor smaller than it,
     ties broken by self-bisection) with an explicit worst-case bound.
Key lemmas (claim + mechanism):
  - Shave-below exact value — because tuning a fragment to sit one rank
    below a fixed anchor is a deterministic rank assignment, computable in
    closed form by the certified Single-Insertion Lemma (no continuity
    argument needed once the anchor is fixed).
  - General matching-rule bound (candidate, the real target) — because a
    greedy largest-unpaired-to-largest-smaller-anchor assignment should
    push every piece's contribution toward the `≈1/2` values numerically
    observed by all three explorers this round, echoing the certified
    First-mover-half floor `OddSum\ge W/2` as the natural target, not
    `c(n)` with slack.
Open gaps: step 5 (the general matching rule and its proof) is the whole
remaining content — steps 1-4 are formalization/setup plus a correctness
check against known examples.
Cases to cover: parity of `n+1` (whether every piece can be paired or one
is left over as a lone anchor or lone self-bisect); the boundary as
`p1\to(1/2)^-$ where regime-change to top-only-single-piece was observed
numerically by the fresh-framing explorer.
Watch out for: budget feasibility — each shave-below or self-bisect uses
exactly 1 cut, so the total number of split pieces must be `\le n`; verify
this never over-spends given `k=n+1` pieces and `n` cuts (exactly enough
for every piece but one to be split once, matching the numerically
observed "usually 1-2 pieces split, not all" pattern).

dyadic-potential-invariant: revise
Target: (a) prove in full generality the **Tie-or-zero Lemma** (every
optimal XY response can be taken so each non-anchor fragment is either `0`
or exactly tied with another element of the final multiset); (b) use it,
plus compactness, to give an existence-style closure of the balanced-region
upper bound (not necessarily an explicit universal formula).
Technique: LP extreme-point argument — a linear functional restricted to a
polytope attains its minimum at a vertex; characterize the vertices of the
relevant polytopes explicitly.
Skeleton:
  1. Fix a cut-count allocation `(m_1,\ldots,m_k)` (how many cuts land on
     each of LB's `k` pieces). The space of achievable fragment vectors is
     a product of simplices (one per piece), a compact convex polytope.
  2. Fix additionally a **sort-order region**: a choice of total order on
     all resulting fragments consistent with the piece-sum constraints.
     `OddSum` restricted to this region is a **fixed linear functional**
     (a 0/1-weighted sum of the fragment coordinates, weights determined
     by which rank — odd or even — each coordinate occupies under the
     fixed order) — prove this precisely as an elementary fact (no new
     machinery, direct from the definition of `OddSum` and of a sort-order
     region as an intersection of half-spaces `x_i\ge x_j$ with the
     simplex).
  3. Invoke the standard LP fact (`knowledge_base.md`, "Extreme value
     theorem / Lagrange multipliers on a compact manifold") that a linear
     function on a polytope attains its extremum at a vertex; characterize
     vertices of "simplex `\cap` sort-order half-spaces" precisely: a
     vertex has (number of active constraints) = (dimension), forcing
     either a coordinate `=0` (an unused cut / degenerate split) or two
     order-constraints tight simultaneously (an exact tie between two
     elements of the final multiset). Prove this characterization rigorously
     (a concrete linear-algebra fact about polytope faces, not just an
     appeal to intuition).
  4. Take the min over the *finite union* of such regions (one per
     combinatorial sort-order, for the fixed cut-allocation) — the overall
     minimum is attained at a vertex of *some* region, so it is still
     tie-or-zero. Then take the min over cut-allocations `(m_1,\ldots,m_k)`
     too (a further finite choice, `\sum m_i\le n`) — conclude the
     **global** XY-optimal response (for any fixed LB partition) can always
     be taken tie-or-zero. This is the Tie-or-zero Lemma, proved in full.
  5. Use Tie-or-zero to reduce "does some XY response achieve `\le c(n)`"
     to a *finite combinatorial* search (over which ranks tie / which
     fragments vanish) for each fixed `n` — attempt to turn this into a
     general-`n` closure via a counting/pigeonhole argument on how many
     tie-blocks of each size are needed (an existence argument, distinct
     in kind from `universal-halving-adversary`'s explicit-formula attempt
     — report honestly if this stays existence-only, not explicit, for
     general `n`).
Key lemmas (claim + mechanism):
  - Tie-or-zero Lemma — because `OddSum` is linear on each fixed
    sort-order region, so its minimum over a polytope is attained at a
    vertex, and vertices of a simplex-intersect-order-constraints polytope
    are exactly the configurations with a zero coordinate or an exact tie
    (standard LP vertex-counting: active constraints = dimension).
Open gaps: step 5 (turning the structural lemma into an actual closure of
the balanced region, even in existence form) is the open target; steps
1-4 (the Tie-or-zero Lemma itself) are the concrete, provable-this-round
content and are valuable as a certifiable reusable tool regardless of
step 5's outcome.
Cases to cover: degenerate polytopes (a piece already forced to a single
value by budget exhaustion — dimension-0 "vertex" trivially); multiplicity
in ties (three or more elements tied at once, a higher-codimension face,
still a vertex if it is the unique point satisfying all active
constraints — verify this doesn't break the characterization).
Watch out for: the union-over-regions argument in step 4 needs care — the
sort-order regions can overlap on their boundaries (shared ties), so "min
over a finite union of polytopes is attained at a vertex of one of them"
must be stated and proved correctly (it is a standard fact but must not be
hand-waved: finite union of compact sets attains its min at a point of the
union, and that point is a vertex of whichever region(s) contain it).

lp-duality-split-polytope: new
Target: the full problem (both directions), via LP/convex-duality
formalization of the split polytope — a genuinely new top-level framing,
distinct from all five existing approaches (peel-based x2, algebraic/
AltSum, layer-cake/threshold, tie-vertex-structural), attacking via KKT
duality rather than exchange, peeling, or measure-theoretic identities.
Technique: LP duality / complementary slackness on the piecewise-linear
order-statistics objective (fresh-framing explorer's opening 1), scoped
this round primarily to proving **multi-piece necessity** for the
upper-bound direction as its first concrete deliverable.
Skeleton:
  1. Fix LB's partition `(p_1,\ldots,p_k)`. For a fixed XY combinatorial
     split-pattern `(m_1,\ldots,m_k)` and fixed sort-order region, write
     the inner minimization of `OddSum` as an explicit linear program:
     minimize a fixed linear functional (the designated odd-rank
     fragments) subject to `\{$ each piece's fragments `\ge0`, summing to
     `p_i$, and the order-region's half-space constraints `\}`. This is a
     direct, elementary translation of the already-certified minimax
     reduction (`lemmas/reduction-to-multiset-minimax.md`) into LP form —
     no new content, but the necessary setup.
  2. Write the LP dual for a representative small case (`n=2,3`, matching
     this round's worked balanced-region examples) and verify by direct
     computation that the dual optimal value matches the known primal
     optimum (`0.505`, `\approx0.5004`) — a concrete correctness check
     before attempting the general argument.
  3. Extract the **complementary slackness / KKT conditions**: at an
     optimum, a piece's "sum = `p_i`" constraint has a shadow price
     (Lagrange multiplier) equal to the marginal effect of increasing
     `p_i$ infinitesimally; a piece is "active" (genuinely split, not left
     as a single anchor) iff its own local optimality condition is tight.
  4. **Target: prove Multi-piece Necessity** — whenever `p_1<1/2`, no
     single-active-piece KKT solution can be primal-feasible-and-optimal
     simultaneously; i.e. formalize (not just numerically observe, as this
     round's fresh-framing explorer did) that the balanced region *forces*
     at least two pieces to be split. Attempt via contradiction: assume an
     optimal response splits only one piece; derive, from the other
     pieces' nonzero shadow prices, a strictly-improving alternative move
     that splits a second piece — contradicting optimality.
  5. If step 4 succeeds, hand the resulting structural constraint (`\ge2`
     active pieces, with an explicit description of which) to
     `universal-halving-adversary` as the missing piece of its own
     matching-rule proof (step 5 there) rather than duplicating the
     construction here — this file's job is the *necessity* argument, not
     the explicit construction.
  6. (Secondary, optional this round.) Sketch whether the same
     LP-duality/saddle-point machinery, applied to LB's outer maximization
     over partitions, gives an independent argument that the geometric
     partition is optimal for the lower bound — flagged explicitly as a
     stretch goal, not required for this round's deliverable.
Key lemmas (claim + mechanism):
  - LP formulation of the inner minimization (elementary, step 1) —
    because the certified minimax reduction already presents XY's problem
    as an optimization over a polytope; this is just naming it as an LP.
  - Multi-piece necessity (the real target, step 4) — because the KKT
    stationarity conditions of a single-active-piece solution can be shown
    to leave a strictly-positive shadow price on an untouched piece
    exactly when `p_1<1/2`, giving a directional derivative argument for
    a strictly-improving second move (to be made precise and proved, not
    assumed).
Open gaps: step 4 (the actual necessity proof) is unproved and is this
round's target; step 6 is explicitly out of scope / optional.
Cases to cover: none additional beyond the LP setup's natural finiteness
(finite combinatorial patterns per fixed `n`); step 4's proof must be
general in `n`, not just verified at `n=2,3`.
Watch out for: the number of sort-order regions grows combinatorially with
`n` — do not attempt to enumerate them all for general `n`; the KKT/
duality argument in step 4 must be a *structural* argument (works for
every `n` at once via the shadow-price mechanism), not a per-`n` case
check. Also: this approach must not silently re-derive the already-proven
(and already-refuted, twice) "top-only is optimal" claim in disguise —
multi-piece necessity is the *opposite* claim and should reinforce, not
contradict, `dyadic-potential-invariant`'s and `universal-halving-
adversary`'s existing negative findings.

Build-set guidance for outline-reviewer: all five approaches above have a
concrete, non-duplicated, previously-unattempted target this round. The
two lower-bound approaches (`self-similar-induction-on-n`,
`greedy-reduction-geometric`) are now cleanly partitioned (TOP-ONLY's
Case-B vs. the fully general middle regime) per this round's lowerbound
explorer's unification finding — do not let both attack Case-B(m,k)
simultaneously (assign it solely to `self-similar-induction-on-n`, per
memory rule "assign shared crux to exactly ONE approach"). The three
upper-bound-adjacent approaches (`universal-halving-adversary`,
`dyadic-potential-invariant`, `lp-duality-split-polytope`) are
complementary, not redundant: one builds the explicit construction, one
proves the structural vertex lemma justifying it, one proves a necessity
theorem constraining it — recommend building all three in parallel this
round given the strong three-way corroboration (coupling explorer +
fresh-framing explorer + dyadic-potential-invariant's own prior negative
result all point at the same phenomenon from different angles).
`layer-cake-parity-reframing` remains live (Coupling Obstruction proved,
no new round-5 lead directly advances it) — recommend the outline-reviewer
keep it registered but not necessarily in this round's build set unless
capacity allows, since no approach above duplicates its territory.
