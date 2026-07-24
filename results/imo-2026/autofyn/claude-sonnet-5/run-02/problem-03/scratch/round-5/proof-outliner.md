## imo-2026-03

Context driving this round's field: two independent round-5 explorers converge on
a single decomposition of the open gap (formerly "(★)"/"Missing Inequality") into
**two independent claims** about the global worst case "Xiang Yu spends all n cuts
on p_1, tail untouched":

- **(A) Fixed-tail claim:** `min_F A(F ∪ T) = a_n` where `T = {p_2,...,p_{n+1}}`
  is the FIXED, untouched ladder tail (superincreasing, `p_1=2p_2`) and `F` ranges
  over all partitions of `p_1`. Single-multiset optimization against one explicit
  geometric background — strictly more tractable than the joint two-multiset
  problem every prior approach has been stuck on.
- **(B) Tail-refinement-never-helps claim:** for fixed optimal `F`, spending any
  cut refining the tail instead of fragmenting `p_1` further can only weakly
  *increase* `A`. Numerically confirmed jointly with (A) (three independent
  numeric checks now agree the global min sits exactly at c=n).

Independently, the induction-on-c explorer's exhaustive vertex search (n=3,4,
complete, not sampled) shows the winning vertex at every c≥1 is *always* the
already-certified `R_{n-1}` cascading-family member (bisect p_1 symmetrically into
two copies of p_2, then recurse on the tail), never a genuinely new cross-tie —
reframing the whole lower bound as **induction on n via a domination lemma**:
"any allocation of Xiang Yu's budget to p_1 other than one symmetric bisection is
weakly dominated by that bisection + optimal recursive tail play." This sidesteps
casework on c entirely, and is a different top-level architecture from every live
approach's current "prove (★) for fixed c" framing.

Both findings point at the SAME underlying fact stated two ways: the domination
lemma (induction-on-n framing) is essentially "the global minimizer over all
vertices is R_{n-1}/R_n, uniquely" — which is exactly claim (A)+(B) restricted to
the achieved vertex. This round sharpens four live approaches with this shared
target, assigning each a distinct sub-piece it is best positioned to close (so
they stay genuinely different routes, not restatements), plus one new approach
using a fresh technique (explicit dyadic-band formula) not yet tried by anyone.

---

greedy-halving-adversary: advance
Target: `c(n) = 2^n/(2^{n+1}-1)` for all n (lower bound direction; this approach
owns the cross-term/integral machinery).
Technique: mass/cross-term integral bound, now retargeted specifically at claim
**(B)** — "refining the tail is never advantageous for Xiang Yu" — via a
surrogate-domination argument (crux `aimo-0560`: replace an adversary's move by a
pointwise-at-least-as-damaging surrogate, transfer the bound down).
Skeleton:
  1. Fix the optimal `F` from claim (A) (import from `rank-pigeonhole-budget`/
     `dyadic-band-occupancy` once available, or assume it provisionally as the
     achieving cascading-halving configuration already certified).
  2. Construct, for any single tail-refining cut, an explicit "surrogate" move —
     spend that cut instead on further fragmenting `F` (or leaving it unspent) —
     and show via the certified `sharp-dominant-removal-identity` +
     `odd-run-reduction-lemma` that the surrogate's `A`-value is ≤ the real tail
     cut's `A`-value (i.e. the real cut is at least as good for Xiang Yu... wait,
     dualize correctly: show the *no-refinement* alternative is weakly BETTER for
     Xiang Yu, i.e. `A` does not increase when the tail-cut is "undone" — by
     `tail-self-similarity`'s exact rescaling of the tail as an (n-1)-ladder).
  3. Induct on the number of tail cuts spent (finite, ≤ n): repeatedly undo one
     tail cut without hurting Xiang Yu, until 0 tail cuts remain — reaching
     exactly the c=n configuration analyzed by claim (A).
  4. Conclude (B), hence combined with (A): `min over all compositions = a_n`.
Key lemmas (claim + mechanism):
  - Surrogate-undo inequality: undoing a single tail cut (merging two tail
    fragments back to their pre-cut value) does not increase `A` — because
    `tail-self-similarity` shows the tail's own recursive structure is exactly
    the (n-1)-ladder, so any cut inside it either helps Liu Bang more or is
    neutral by the certified `odd-run-reduction-lemma`'s rank-shift bookkeeping.
Open gaps: the surrogate-undo inequality itself (step 2) — not yet proved, only
numerically supported (three independent checks, see explorer reports).
Cases to cover: tail cuts landing at ties vs. strict interior positions (the
undo-move must be well-defined and rank-preserving in both).
Watch out for: don't silently assume `F` is already optimal when analyzing tail
cuts — claim (B) must hold for the *specific* optimal `F`, or (better) be shown
to hold for every `F` simultaneously (monotone in the tail-refinement variable
alone), which is the stronger and cleaner target to aim for.

rank-pigeonhole-budget: advance
Target: same overall claim (lower bound for all n), this approach owns claim
**(A)** — the fixed-tail single-multiset optimization.
Technique: discrete band-occupancy decomposition (new, per this round's
explorer) rather than continuum LP — write `A(F ∪ T)` as an explicit sum over
`T`'s n dyadic bands (the intervals `[p_{k+1}, p_k)` induced by `T`'s
superincreasing gaps), one term per band, depending only on how many of `F`'s
parts fall in each band and their total mass there; then minimize this discrete
functional directly.
Skeleton:
  1. Fix `T = {p_2,...,p_{n+1}}` (untouched ladder tail). For any partition `F`
     of `p_1`, sort `F ∪ T` and evaluate `A` via the certified
     `odd-run-reduction-lemma`.
  2. Show `A(F∪T)` decomposes as a sum of n+1 band-contributions, where band `j`
     (elements of `F` landing between `p_{j+1}` and `p_j`, using `T`'s own
     values as thresholds) contributes a term depending only on `T`'s already-
     known geometric values plus the count/mass of `F`-parts in that band — by
     direct application of the sharp-dominant-removal identity band-by-band
     (already collapses Case A per round 4).
  3. Minimize the resulting explicit discrete functional over all ways to
     distribute `p_1`'s mass across the n+1 bands (a finite-dimensional, fully
     explicit optimization — no longer a continuum LP over arbitrary cut
     positions) — show the minimum is `a_n`, attained by concentrating all of
     `F`'s mass into the single band adjacent to `p_2` (i.e., bisecting into two
     copies of `p_2` — reproducing the certified `R_{n-1}` cascading-family
     vertex, consistent with `cascading-halving-family-characterization`).
Key lemmas (claim + mechanism):
  - Band decomposition formula: `A(F∪T) = Σ_j A_j(F,T)` where each `A_j` is
    computable in closed form from `T`'s dyadic ratios and `F`'s per-band mass —
    because `sharp-dominant-removal-identity` lets each band's contribution be
    peeled off independently once the previous (larger) bands' contributions are
    fixed by `T`'s known structure.
  - Minimality at "bisect into next rung": because concentrating `F`'s mass at
    the band boundary closest to `p_2` maximizes the number of `F`-fragments
    tied (not exceeding) `T`'s own odd-rank structure — the geometric series
    closed form `T(L)=(2^{L+1}+(-1)^L)/3` from `cascading-halving-family-
    characterization` gives the exact value to match against.
Open gaps: the band decomposition formula itself (step 2) is not yet derived
explicitly for general partition shapes of `F` within a band (only sketched by
the explorer); the discrete minimization (step 3) needs a genuine combinatorial
argument (not just "matches the numerics"), e.g. an exchange argument moving
mass between adjacent bands.
Cases to cover: `F` with many small fragments spread across multiple bands vs.
concentrated in one; boundary cases where an `F`-fragment exactly ties a `T`
value.
Watch out for: this is a strict restriction of the general problem (T is fixed,
not searched) — do not let the builder accidentally re-import the refuted
generic-multiset pigeonhole restatement; the band formula must use `T`'s
specific geometric ratio-2 structure throughout.

rank-tie-vertex-reduction: advance
Target: same overall claim, this approach owns the **domination/uniqueness**
half of the picture: proving the global minimizer over ALL feasible tie-vertices
(every composition, every n) is exactly the certified `R_{n-1}`/`R_n` cascading
family member, and no other vertex — including cross-ties — beats it.
Technique: exact vertex enumeration (Vertex-Minimum Theorem +
Odd-Run-Reduction-Lemma), now guided by this round's exhaustive computational
finding (n=3,4 complete search: every winning vertex at every c≥1 collapses,
after removing zero-length padding, to `R_{n-1}` — no genuine cross-tie ever
wins) to conjecture and prove the **domination lemma**: any tie-vertex not of
the `R_{n-1}`/`R_n` shape is strictly dominated.
Skeleton:
  1. Import `cascading-halving-family-characterization` (already gives the exact
     value at `R_{n-1}`, `R_n`, and shows every *shallower* cascading member
     strictly exceeds it).
  2. Extend the enumeration argument beyond the cascading family: for a general
     feasible tie-vertex (any subset of "fragment=0"/"fragment=fragment"
     constraints, per `vertex-minimum-theorem`), show it can be transformed into
     a cascading-family member (or something worse) by a finite sequence of
     "un-tie and re-tie" moves that never increase `A` — an induction on the
     number of non-cascading ties present at the vertex.
  3. Conclude uniqueness: the minimum over all vertices, all n, all compositions
     equals `a_n`, attained exactly at `R_{n-1}`/`R_n`.
Key lemmas (claim + mechanism):
  - Un-tie/re-tie reduction: because `odd-run-reduction-lemma` evaluates any
    vertex in closed form as a function of which values are tied, a non-cascading
    tie can be replaced by a cascading one via a local swap that is shown (using
    the certified `pair-cancellation-identity`) to weakly decrease or preserve
    `A`, never increase Xiang Yu's cost below `a_n`.
Open gaps: step 2's induction is the new content — not yet proved, only
evidenced by exhaustive computation at n=3,4 (not n≥5, where exhaustive vertex
search timed out). The reduction move itself needs to be defined precisely and
shown to terminate (strictly decrease some potential, e.g. number of
non-cascading ties) at every step.
Cases to cover: vertices with multiple simultaneous non-cascading ties (not just
one); degenerate (zero-length) fragments interacting with genuine ties.
Watch out for: the round-3 "cross-tie" example that looked new was shown by this
round's explorer to actually just be `R_{n-1}` in different notation — do not
let the builder treat superficially different-looking ties as new cases without
first checking they aren't the same vertex relabeled.

induction-first-move-reduction: revise
Target: same overall claim, via **induction directly on n** (distinct top-level
architecture from the "fixed-c casework" framing shared by the other three
approaches above).
Technique: strong induction on n, now correctly reformulated using this round's
finding — the previous outline's naive recursion (`c(n) = p + c(n-1)(1-p)`,
peel-off-top-piece-then-rescale) was shown arithmetically FALSE
(`3·2^{n-1} ≠ 2^n`) and must NOT be reused. The correct recursive mechanism,
per the round-5 induction-on-c explorer's exhaustive finding, is:
  - Xiang Yu's globally optimal response spends *exactly one* unit of budget as
    a symmetric bisection of `p_1` into two copies of `p_2` (never a different
    split, never more real cuts on `p_1`);
  - the tail `p_2,...,p_{n+1}` is, by `tail-self-similarity`, EXACTLY the
    (n-1)-ladder rescaled — so after the bisection, the resulting merged
    multiset `{p_2,p_2,p_3,...,p_{n+1}}` is precisely the certified
    `R_{n-1}` cascading-family vertex, whose value is already known in closed
    form (`cascading-halving-family-characterization`) to equal `a_n` exactly —
    **no further recursive algebra is needed on the achievability side**, only
    on the "no other allocation beats it" (domination) side.
Skeleton:
  1. Base case n=1: already fully proved (c(1)=2/3, both directions).
  2. Achievability side (replaces old Steps 4+6 entirely): the ladder
     construction plus Xiang Yu's symmetric-bisection response gives exactly
     `A = a_n`, by direct substitution into
     `cascading-halving-family-characterization`'s closed form at `L=1`
     (`k=n-1`) — a clean, non-recursive computation, not an inductive one. (This
     removes the false arithmetic step entirely; the "induction" is now only
     needed for the domination direction below.)
  3. Domination side (replaces old Step 5): prove — by strong induction on n,
     using the inductive hypothesis that `c(n-1)` is the exact value for the
     (n-1)-game — that ANY Xiang Yu response other than the symmetric bisection
     of `p_1` followed by recursively-optimal tail play gives `A ≥ a_n`. This is
     the domination lemma jointly targeted by `rank-tie-vertex-reduction`
     (general vertex form) and `greedy-halving-adversary` (claim (B), tail
     side); import whichever is certified first rather than re-deriving.
  4. Conclude `c(n) = a_n` for all n by induction, both directions.
Key lemmas (claim + mechanism):
  - Corrected achievability computation (step 2): direct substitution, not
    recursion — because `R_{n-1}`'s value is already a closed form in terms of
    n alone, not in terms of `c(n-1)` via a linear peel formula.
  - Domination lemma (step 3): any allocation to `p_1` besides one symmetric
    bisection, or any different tail treatment, is weakly dominated — because
    (per this round's exhaustive n=3,4 computation) every alternative either
    fails to protect a full copy of `p_2` at the top of the merged multiset
    (losing an odd-rank slot to Liu Bang) or degenerates back to the same
    bisection with wasted zero-length cuts.
Open gaps: the domination lemma (step 3) is the ENTIRE remaining content —
identical in substance to the gap in `rank-tie-vertex-reduction` and
`greedy-halving-adversary`'s claim (B); this approach's value is the clean
induction-on-n packaging, not a separate proof of the hard fact.
Cases to cover: n=2 spot-check that the corrected achievability computation
(step 2) reproduces the already-fully-closed `c(2)=4/7` exactly, as a sanity
check before trusting it for general n.
Watch out for: do NOT resurrect the old Step 4/5/6 peel-recursion arithmetic —
it is confirmed false and the outline above replaces it entirely, it should not
reappear even as a "simplification."

dyadic-band-occupancy: new
Target: same overall claim (lower bound, all n) — claim **(A)** specifically,
via a fresh technique distinct from every live approach's vertex/LP/integral
machinery: an explicit closed-form generating-function-style formula for
`A(F∪T)` in terms of `F`'s occupancy counts across `T`'s n dyadic bands, then a
direct combinatorial (not LP) minimization.
Technique: generating functions / step-function counting (knowledge base:
piecewise structure of superincreasing sequences), a genuinely different lever
from LP-vertex enumeration — it treats `T`'s dyadic gaps as a fixed "comb" and
asks only how `F`'s total mass `p_1` is distributed across the n+1 resulting
intervals (a discrete composition problem), independent from `rank-pigeonhole-
budget`'s band approach in that it does not fix `F`'s exact partition shape
within a band, only the mass-count pair per band — a coarser, more tractable
reduction that may close (A) even if the finer band-decomposition stalls.
Skeleton:
  1. Fix `T={p_2,...,p_{n+1}}`, `p_i=2^{n+2-i}/(2^{n+1}-1)`. Define, for any
     `x`, `N_T(x) = #{i : p_i > x}` — a step function with jumps exactly at
     `T`'s n values (dyadically spaced by construction).
  2. For a partition `F` of `p_1`, define its occupancy vector `(m_0,...,m_n)`
     where `m_j` = number of `F`-parts (with total mass `μ_j`) landing strictly
     between `p_{j+1}` and `p_j` (`p_{n+2}:=0`, `p_1$ itself is the top band
     boundary `j=0`). Show `A(F∪T)` is an explicit function of
     `(m_0,μ_0),...,(m_n,μ_n)` alone (independent of the fine-grained shape of
     `F` within each band) — via the parity of `N_{F∪T}(x)` on each band being
     constant except at `F`'s own internal fragment boundaries, which the
     certified `odd-run-reduction-lemma` already handles.
  3. Minimize the resulting explicit discrete/combinatorial functional over all
     `(m_j,μ_j)` with `Σμ_j=p_1`, `Σm_j` arbitrary — show the minimum
     `a_n` is achieved exactly when all mass concentrates in `m_0=0, m_1=2`
     (two copies of `p_2`, i.e. bisection) and every other band empty — matching
     `R_{n-1}` again, from a different derivation path than
     `rank-pigeonhole-budget`'s.
Key lemmas (claim + mechanism):
  - Band-invariance formula: `A(F∪T)`'s dependence on `F` reduces to
    `(m_j,μ_j)` per band, because within a fixed band, all of `F`'s parts sit
    strictly between two consecutive `T`-values, so their relative order among
    themselves does not change which `T`-elements they separate — only their
    count and total mass affect the odd/even rank parity flips, by direct
    parity bookkeeping (a corollary-style extension of
    `odd-run-reduction-lemma`).
  - Concentration-minimality: because moving mass from a shallow band (near
    `p_1`) to a deep band (near `p_{n+1}`) strictly changes fewer rank-parities
    per unit mass moved (the "leverage" of a unit of `F`-mass on `A` decreases
    monotonically with band depth, following `T`'s ratio-2 decay) — the
    minimum is at the shallowest possible non-trivial concentration, i.e. band
    `j=1`, exactly the bisection.
Open gaps: both key lemmas (steps 2, 3) are new derivations, not yet written
out in full generality — this is a from-scratch technique, higher risk than
advancing the live approaches, but the explorer's own cheap-sanity-check (verify
the band formula reproduces `odd-run-reduction-lemma`'s vertex values for
n=2,3 by hand) should be done FIRST, before committing to the general
derivation, to catch any error early.
Cases to cover: `F` with a part landing exactly ON a `T`-boundary (tie case,
band ambiguity) — must be resolved consistently with `vertex-minimum-theorem`'s
tie-vertex framework.
Watch out for: this approach must stay genuinely distinct from
`rank-pigeonhole-budget` — if the builder finds the two formulas are secretly
identical after all, merge effort onto whichever is further along rather than
duplicating; report explicitly if this happens.
