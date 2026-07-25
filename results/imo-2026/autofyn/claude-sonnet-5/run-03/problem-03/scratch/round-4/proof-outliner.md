## imo-2026-03

### Shared setup (imported by every approach, all certified)
`lemmas/reduction-to-multiset-minimax.md`, `lemmas/greedy-optimality-oddsum.md`:
value is `c(n) = max_{p1≥...≥pk>0, sum=1, k≤n+1} min_{refinement, ≤n cuts} OddSum`.
Conjectured/target closed form `c(n) = 2^n/(2^{n+1}-1)`, proved for `n=0,1`.
Unnormalized geometric partition `Γ_m = (2^m,...,1)`, total `2^{m+1}-1`.
`T(m,k)`: every refinement of `Γ_m` with `≤k` cuts has `OddSum ≥ 2^m`.

Plateau diagnosis this round (both lower-bound explorer and fresh-framing
explorer independently confirm): **Proposition C is a proved, structural
obstruction specifically to the "peel current max, bound rest by a single
scalar OddSum/EvenSum value, recurse" mechanism** — not to induction in
general. Two live approaches (`self-similar-induction-on-n`,
`greedy-reduction-geometric`) are variants of exactly this family and have
independently hit it for 2 straight rounds. Per CLAUDE.md's plateau rule,
this round opens a genuinely different top-level route
(`layer-cake-parity-reframing`, new) that does **not** peel a max element at
all, and retargets the two stuck approaches' next gap toward mechanisms that
are not "one more scalar-bound peel."

---

self-similar-induction-on-n: revise
Target: `T(m)` for all `m≥0` (the lower-bound half of `c(n)`, geometric
construction), building on certified `T(0),T(1),T(2)`, Lemma Z, and
Proposition C (the certified dead end for peel+scalar on Case A).
Technique: strong induction on `m`, but the *inductive step's mechanism* for
`j≥2` (top piece split into `≥3` fragments) is retargeted away from
"peel + z-trick + scalar EvenSum bound" (proved circular) toward the
**global amortized AltSum-budget argument** surfaced this round by the
lower-bound explorer (opening 1 in `math-explorer-lowerbound.md`).
Skeleton:
  1. (imported, certified) Reduce `T(m,k)` to `AltSum(refinement of Γ_m) ≥ 1`
     via the identity `OddSum = (total+AltSum)/2` with `total=2^{m+1}-1`
     fixed — this is an elementary algebraic reformulation (proved by direct
     computation from the definitions; explorer verified it numerically on
     2000 random instances, exact match), not a new axiom, and it is
     equivalent to `T(m,k)`, not a weaker corollary.
  2. Bound the total AltSum drop over the `≤m` cuts XY spends, using a
     **structure-aware per-cut bound** (not the naive `Δ≥-x` bound, which
     the explorer showed is individually too weak — summed over `m` cuts it
     can exceed the whole slack `(2/3)2^m`). The needed sharper bound: when a
     cut splits the element currently sitting at sorted rank `r` (value `x_r`)
     into fragments that land at ranks `r,...,r+t`, the resulting AltSum change
     is *exactly* computable from the fragments' relation to the *neighboring*
     ranks `x_{r-1}` and `x_{r+t+1}` (not from `x_r`'s raw value) — because
     AltSum is a signed sum of an exactly-sorted sequence, a local
     reordering only changes the signs/values in the affected window. State
     and prove this exact local-change formula (a direct generalization of
     the Peeling Lemma's telescoping, but tracking signs instead of a single
     scalar), then bound the *sum* of these local losses across `≤m`
     sequential cuts, using that `Γ_m`'s ratios (`2:1` between consecutive
     ranks) bound how far any single cut's fragments can fall below their
     rank's predecessor.
  3. Show the total bound (summed loss) is `< AltSum(Γ_m) - 1 =
     (2/3)2^m - o(2^m)`, closing `T(m)` for every `m`.
Key lemmas (claim + mechanism):
  - **AltSum reformulation** (already certified-quality, elementary):
    `OddSum(X) = (sum(X) + AltSum(X))/2` for any sorted finite multiset —
    because `OddSum-EvenSum=AltSum` and `OddSum+EvenSum=sum` are both
    definitional, solve the 2x2 linear system.
  - **Local AltSum-change formula for a single split** (new, to prove): if
    element at rank `r` splits into fragments occupying ranks `r,...,r+t`
    (t≥1 new elements inserted), the resulting `ΔAltSum` is a signed
    telescoping sum determined entirely by the fragment values and the two
    boundary neighbors `x_{r-1}, x_{r+t+1}` — because inserting `t` new
    values into a sorted sequence only re-signs the elements strictly
    between the old and new positions of everything from rank `r` onward,
    and AltSum is linear in the (correctly re-signed) values.
  - **Aggregate budget bound** (new, to prove, the actual open content):
    summed over `≤m` sequential cuts applied to `Γ_m`, total `|ΔAltSum| <
    AltSum(Γ_m) - 1`. Mechanism: each cut's local loss (per the formula
    above) is controlled by the *ratio gap* to the neighboring rank, and
    `Γ_m`'s dyadic ratio `2` bounds this gap uniformly at every level, so a
    telescoping/geometric-series sum over `≤m` cuts stays under the slack.
Open gaps: the Local AltSum-change formula is unproved (elementary but
unfinished); the Aggregate budget bound is the genuinely hard, unproved
step — the explorer flagged this as a real open sub-problem distinct in
kind from Proposition C's obstruction, and it is where this approach's
build effort should concentrate. `T(2)`, Lemma Z, Proposition C stay
certified/documented as-is (Proposition C is now explicitly a *dead end for
peel+scalar only*, not evidence against this new route).
Cases to cover: none new (the argument is meant to be uniform in `j,k`); if
the aggregate bound fails uniformly, fall back to identifying the worst-case
`j` (likely `j` maximal, i.e. top piece split into `m+1` fragments) as a
reduced target.
Watch out for: do not re-derive Proposition C's peel+scalar mechanism under
a new name inside the "local change formula" step — the local formula must
track the *full sign pattern* of the affected window, not collapse it back
to a single OddSum/EvenSum scalar (that collapse is exactly what made the
old mechanism circular).

---

greedy-reduction-geometric: revise
Target: TOP-ONLY lower bound outside the Dominant-Chain regime, and general
Case 2 (per lowerbound explorer's finding #2, these are the same open
problem, not two separate ones) — building on certified Dominant-Chain
Theorem (Thm 5) and the Prefix-Run Peeling Decomposition (Lemma 6).
Technique: extend the exact Lemma 6 recursion (a true identity, not an
inequality — its content is not invalidated by Proposition C, which killed
only the different, later attempt to close the residual by a scalar bound)
using the certified **EvenSum-superadditivity dual** found this round
(`EvenSum(A∪B) ≥ EvenSum(A)+EvenSum(B)`, immediate from Lemma S in
`universal-halving-adversary` via `Odd+Even=sum`) as the tool for the
residual term, restricted to the sub-case where it is provably sufficient.
Skeleton:
  1. (certified) Apply Lemma 6 at the maximal valid prefix-run depth `d` to
     any split `A` of `2^n` violating Dominant-Chain, splitting into the
     known `OddSum(Γ_{[n-d,n-1]})` term plus `Odd/EvenSum(A∪Γ_{n-d-1})`
     (parity depends on `d` mod 2).
  2. For the residual term, instead of trying a single further scalar bound
     (the mechanism Proposition C shows is circular one level down), apply
     EvenSum-superadditivity *only* when the peeled-off tail block
     `Γ_{[n-d,n-1]}` itself already accounts for enough mass to make the
     residual inequality's threshold trivially met — i.e. carve out and
     close the **sub-case where `d` (the violation depth) is large relative
     to `j` (fragment count)**, honestly as a partial regime, rather than
     claiming the fully general complementary regime.
  3. Document, precisely, why the residual step still fails outside that
     sub-case (per the explorer's confirmation that superadditivity alone
     is insufficient when `B'` — the peeled fragment remainder — is small
     in cardinality), so the boundary of what's closed vs. open is exact.
Key lemmas (claim + mechanism):
  - **Prefix-Run Peeling Decomposition (Lemma 6, certified)**: exact
    identity splitting `OddSum(A∪Γ_{m-1})` into a known top block plus an
    `Odd/EvenSum` of a smaller residual — because the top `d` tail values
    strictly dominate `A` and the rest strictly dominates the remaining
    tail, so the sort factors cleanly.
  - **EvenSum superadditivity (new import, to apply carefully)**:
    `EvenSum(A∪B) ≥ EvenSum(A)+EvenSum(B)` — dual of certified Lemma S via
    `Odd+Even=sum` on both sides. Confirmed this round to be **necessary but
    not sufficient alone** (explorer: fails when `B'` has few elements) —
    use only in the large-`d` sub-case where the peeled block already
    supplies most of the needed mass.
Open gaps: the general complementary regime (small `d`, small `j`) is not
closed by this route; the exact "large enough `d`" threshold where
superadditivity suffices needs to be pinned down and proved, not just
asserted.
Cases to cover: partition by `d` (violation depth) vs `j` (fragment count);
prove the large-`d` sub-case in full, state precisely where it stops
covering and hand off the rest as still-open (do not claim full generality).
Watch out for: this is explicitly *not* a route around Proposition C's wall
in the same framing — using an exact identity (Lemma 6) plus a genuinely
different tool (superadditivity, not a re-derived scalar peel bound) for a
scoped sub-case is legitimate; do not let the builder quietly fall back to
"peel again and bound by a single number" for the residual, that is the
already-dead mechanism.

---

universal-halving-adversary: revise
Target: the single remaining upper-bound region `p1<1/2 AND
p_{n+1}>1/(2^{n+1}-1)` (balanced/near-uniform partitions), building on
certified Doubling Lemma, General Insertion Lemma (Thm 4), Subadditivity
(Lemma S), Perfect-Pairing (Thm 3), and the conditional Thm 5.
Technique: extend the exact-identity family (Doubling/Insertion) to a new
**Partial-Match / Suffix-Insertion** construction, specifically motivated by
this round's upper-bound explorer finding that optimal top-only splits of
`p1` in the balanced region numerically duplicate a *suffix* of the tail
`R=(p2,...,p_{n+1})`, not all of it and not a symmetric bisection.
Skeleton:
  1. For `p1<S` (balanced regime, Theorem 2/4's hypothesis fails), consider
     splitting `p1` into `t` fragments that exactly duplicate the smallest
     `t` values of `R` (a "suffix match", `t` chosen by XY) plus one
     leftover fragment `ℓ = p1 - (\text{sum of matched suffix})`, using
     `≤ t` cuts (`t-1` if `ℓ=0`).
  2. Derive a closed-form `OddSum` formula for this construction by the same
     rank/parity block-counting technique as Theorem 2/4's proof (each
     duplicated suffix value now has an *odd* total multiplicity — original
     copy in `R` plus the new copy from `p1`'s split — the same odd-block
     rank-counting argument applies, generalized to a *partial* rather than
     *total* duplication of `R`).
  3. Optimize over `t∈{0,...,n}` (subject to budget) to find the choice
     minimizing the resulting `OddSum`, and show the minimum over `t` is
     always `≤ c(n)` throughout the balanced region — this is the genuinely
     open computational/algebraic core.
Key lemmas (claim + mechanism):
  - **Suffix-Match Insertion Lemma** (new, to prove): for `R` a multiset,
    `t≤|R|` its smallest `t` values (multiset `R_t`), and `ℓ = p1 -
    sum(R_t) ≥0`: splitting `p1` into `R_t ∪ {ℓ}` gives
    `OddSum(R ∪ R_t ∪ {ℓ}) = sum(R) + [\text{contribution of the doubled
    suffix block, by the same odd/even-block parity argument as Theorem 4}]`
    — mechanism: exactly as in Theorem 4's proof, each duplicated value in
    `R_t` now has multiplicity 2 (even) except possibly matching `ℓ`
    (odd-block case), and the *undoubled* remainder of `R` (values not in
    `R_t`) keeps its own single-copy rank contribution unchanged in parity
    since duplicating only the bottom `t` values shifts ranks below the
    duplicated block by an even amount. State and prove the exact formula
    (a genuine generalization of Theorem 2/4, not yet done for partial `t`).
  - **Top-only optimality restricted to the balanced region** (scoped-down
    conjecture from `dyadic-potential-invariant`, imported as a working
    hypothesis, not assumed proved): numerically confirmed by this round's
    explorer specifically inside the balanced region at `n=2,3` (ties the
    true global minimum in every targeted test) — use as a guide for where
    to search, not as a citable fact until `dyadic-potential-invariant`
    proves it.
Open gaps: the Suffix-Match Insertion formula's proof; the optimization over
`t` and the region-wide inequality `min_t OddSum(t) ≤ c(n)`.
Cases to cover: `t=0` (no match, reduces to a bisection-type move — check it
degenerates correctly), `t=|R|` (full match, reduces to existing Theorem
2/4 when applicable), and the interior optimum.
Watch out for: exactly-uniform partitions are NOT the hard sub-case (explorer
confirmed they hit the floor `1/2` trivially via a parity-fix, needing ≤1
cut) — don't spend builder effort there; focus on `p1` moderately below
`1/2` with comparably large `p_{n+1}`.

---

dyadic-potential-invariant: revise
Target: retarget from the (stalled, general-domain) "top-only allocation is
always ≥ as good as any allocation of the same budget" aggregate claim to a
**scoped version restricted to the balanced region** `p1<1/2,
p_{n+1}>1/(2^{n+1}-1)` — exactly upper-bound's remaining open region, where
this round's explorer found top-only *ties* the true numeric minimum at
every tested point (stronger, more targeted evidence than round 3's
unrestricted spot checks).
Technique: exchange/majorization argument on cut allocations, restricted to
the sub-case with no dominant piece — attempt a **rank-preserving swap
argument** exploiting the absence of a dominant piece (the mechanism that
killed the literal Cut-Reallocation Exchange Lemma relied on a dominance
structure between ranks near the top; in the balanced region no single
piece dominates, so the failure mode found in round 3's counterexample may
not recur — this must be checked, not assumed).
Skeleton:
  1. Restate the target narrowly: for `p1<1/2` (`k=n+1` pieces, balanced),
     and any allocation of `≤n` cuts split between `p1` and the rest, show
     the top-only allocation (all cuts on `p1`) achieves `OddSum` no worse
     than any other allocation of the same budget.
  2. Attempt a **local 1-cut exchange restricted to the balanced regime**:
     take any allocation with `≥1` cut on a non-top piece, and show moving
     that cut onto `p1` weakly decreases `OddSum`, using that in the
     balanced region every piece is comparable in size (no rank-boundary
     ties near the very top the way round 3's counterexample exploited a
     dominance gap between `8,4` and the small fragments).
  3. If step 2 fails again (test it numerically FIRST, before writing any
     proof, per the standing rule), fall back to the **global comparison**
     (not step-by-step): directly compare top-only's closed form (via
     `universal-halving-adversary`'s Suffix-Match Insertion formula, once
     proved) against the numeric global minimum found by the upper-bound
     explorer, to see if top-only's formula *is* the closed-form minimum
     algebraically, sidestepping the exchange-argument mechanism entirely.
Key lemmas (claim + mechanism):
  - **Restricted Exchange Lemma** (new target, must be numerically
    stress-tested before any proof attempt — per the standing rule that
    burned round 3's literal version): "in the balanced region only, moving
    a cut from any non-top piece onto `p1` weakly decreases `OddSum`" —
    mechanism candidate: without a dominant top piece, cuts on lower pieces
    can only ever affect ranks below where `p1`'s own fragments will sit,
    so no "wasted cut near a tie-boundary" failure mode (round 3's exact
    counterexample) should be reproducible — TEST THIS FIRST on the exact
    counterexample's structure adapted to a balanced instance before
    committing to a proof.
Open gaps: everything — this is a genuine re-scoping of a previously-failed
claim to a narrower domain where the failure mechanism may not apply; the
first builder task is the numeric stress test, not a proof.
Cases to cover: none beyond the balanced-region restriction itself.
Watch out for: do NOT resurrect the literal (unrestricted) Cut-Reallocation
Exchange Lemma — it is a certified dead end. This is a genuinely narrower
claim (different domain), not a repeat.

---

layer-cake-parity-reframing: new
Target: `T(n)` for all `n` (lower-bound direction) — proving the geometric
construction guarantees `OddSum ≥ 2^n`/`(2^{n+1}-1)` against every XY
refinement, by a top-level framing that is **not** peel-the-max-and-recurse,
directly answering the plateau-break requirement.
Technique: threshold/layer-cake decomposition of `OddSum-EvenSum` into a
per-piece-additive, parity-of-count integral (fresh-framing explorer's
framing A), combined with a generating-function (sign-product) expansion
over pieces. Closest crux match: `aimo-0127`'s "rewrite a weighted total as
a sum over weight thresholds of tail-counts" (structural hint, not a
verified worked solution — its corpus `solutions` field is corrupted, so
treat only the technique name as transferable).
Skeleton:
  1. **Layer-cake identity** (prove in full — elementary but not yet
     written up rigorously): for a sorted finite multiset `x_1≥...≥x_k>0`,
     `OddSum-EvenSum = ∫_0^∞ 1[N(t) is odd] dt` where `N(t)=#{i:x_i≥t}`.
     Proof sketch: write `x_r = ∫_0^{x_r} dt`, swap sum and integral; the
     coefficient of `dt` at threshold `t` is `Σ_{r≤N(t)}(-1)^{r+1}`, which
     is `1` if `N(t)` odd, `0` if even. (Explorer numerically verified to
     4+ sig figs on 5 random multisets — this round's job is the rigorous
     proof, which is short and elementary.)
  2. **Per-piece additivity of `N(t)`.** For the final multiset arising from
     LB's partition `p_1,...,p_k` each independently refined by XY,
     `N(t) = Σ_i n_i(t)` where `n_i(t)` = number of fragments of `p_i` that
     are `≥t` (0 if `t>p_i`, since no fragment of `p_i` can exceed `p_i`).
     Each `n_i` is a per-piece, XY-controlled step function on `(0,p_i]`,
     independent of how other pieces are split — this is the key
     structural fact that sidesteps the top-piece-vs-rest asymmetry
     Proposition C exploits: **no piece is privileged**, the decomposition
     treats every piece identically.
  3. **Reduce to a threshold-by-threshold parity/counting problem.** LB's
     target is `∫ 1[N(t) odd] dt ≥ 1` (unnormalized, `T(m,k)` version) for
     every choice of the `n_i` step functions XY can realize with `≤n` total
     cuts (`n_i` uses `(\text{number of steps in }n_i)-1` cuts on piece `i`,
     summed `≤n`). Since `1[N(t) odd]` depends only on `Σn_i(t) mod 2`, XY's
     problem at each threshold reduces to *toggling parity*, not to the full
     merged sort order — this genuinely removes information XY doesn't need,
     which is the concrete sense in which this framing is "easier."
  4. **Budget-to-measure translation.** Show that flipping `N(t) mod 2` on
     an interval of length `ℓ` (i.e. making `1[N(t) odd)]=0` there instead of
     `1`) costs XY at least one cut "used up" over that interval — formalize
     which single-piece splits can flip parity over which threshold ranges,
     and bound how much total measure XY can flip to `0` with `≤n` cuts.
  5. Conclude `∫1[N(t) odd] dt ≥ (\text{measure LB's geometric } N_0
     \text{ leaves odd}) - (\text{max flippable measure with }n\text{ cuts})
     ≥ 1`, closing `T(n)`.
Key lemmas (claim + mechanism):
  - **Layer-cake identity** (elementary, proof above) — reformulates the
    whole target additively; not a new axiom, a direct consequence of
    swapping sum/integral order.
  - **Per-piece additivity** — because a fragment of `p_i` can never exceed
    `p_i`, its indicator contributes only on `(0,p_i]`, so `N(t)`'s value at
    any threshold `t` is determined piece-by-piece, independently of the
    other pieces' internal splits (only the *count* interacts, via parity).
  - **Budget-to-measure translation** (the genuinely open, hard step, not
    yet attempted): the precise quantitative bound on how much measure a
    single cut (a single new breakpoint in one piece's step function `n_i`)
    can flip from odd to even, and how this composes across `≤n` cuts on
    LB's specific geometric `p_i=2^i/(2^{n+1}-1)` sequence — this is where
    the real difficulty of the problem must reappear (it cannot vanish),
    but in a form additive over pieces/thresholds rather than over sorted
    ranks, which is the concrete sense in which this sidesteps Proposition
    C's specific circularity.
Open gaps: steps 1-3 are elementary/structural and should be provable
outright by the builder; step 4-5 (the quantitative budget-to-measure bound)
is the real content and is entirely unstarted — report honestly if it does
not close in the time available, and identify precisely which sub-case (by
analogy with Proposition C, likely "many cuts concentrated near the top
piece's own threshold range") resists the bound.
Cases to cover: none pre-identified; the builder should first verify
numerically (before proving anything) that the reformulated optimization
(minimize flippable measure over per-piece staircases, budget-constrained)
actually reproduces the conjectured `c(n)` value at small `n` — the
fresh-framing explorer flagged this as a cheap sanity check to run before
investing further, since a bookkeeping error in move-order could make the
reformulation's optimum diverge from the true game value.
Watch out for: this framing changes *what information XY's move carries*
(parity vs. exact merged rank) — the builder must double check no
information is illegitimately discarded (i.e. that the reduction in step 3
is a genuine equivalence, not a relaxation) before building anything on top
of it; do this check via the same numeric cross-validation used in step 1.
