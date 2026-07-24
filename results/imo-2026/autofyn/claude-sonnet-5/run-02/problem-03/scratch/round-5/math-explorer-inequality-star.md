## imo-2026-03 — inequality (*) reconnaissance

- Distinct openings:
  1. **(Recommended, new this round) Collapse to a single-multiset extremal
     problem with a FIXED reference sequence.** Numerically (exact `Fraction`,
     300k random-partition trials per n, n=3,4,5 — see verification below),
     when the tail is left completely untouched (`G' = {p_2,...,p_{n+1}}`,
     the original ladder tail, unrefined) and Xiang Yu spends **all** n cuts
     splitting `p_1` into an arbitrary partition `F` (any number of parts,
     any sizes), the minimum of `A(F ∪ tail)` over **every** such partition
     is *exactly* `a_n = 1/(2^{n+1}-1)`, matching the target with equality,
     for every n tested. This reproduces (from a completely different,
     narrower search — vary only `F`, hold `G'` fixed at the untouched tail —
     rather than searching jointly over `F` and arbitrary tail refinements)
     the same finding both `greedy-halving-adversary` (Prop. 13's numeric
     scan) and `rank-pigeonhole-budget` (§4, Case B) already reported: the
     global worst case sits at `c=n`. What is new here is the clean
     **reformulation**: the truly hard remaining fact splits into exactly
     two independent claims, and the *first* one is now a single-multiset
     optimization against a FIXED finite superincreasing sequence, not a
     joint two-multiset problem:
     - **(A) Fixed-tail claim:** `min_{F: partition of p_1} A(F ∪ T) = a_n`,
       where `T = {p_2,...,p_{n+1}}` is fixed (not searched over) and
       superincreasing (`p_i > p_{i+1}+...+p_{n+1}`, and `p_1 = 2p_2`).
       This is dramatically more tractable than the general problem: `T` is
       a single, explicit, finite geometric sequence, and only the *shape*
       of `F` (an arbitrary partition of one number `p_1`) is free. The
       achievability half is already certified
       (`rescaled-ladder-c-equals-n-achievability`, Lemma B1); what's needed
       is the matching lower bound over *all* partitions `F`, which is a
       finite-dimensional (per fixed part-count k) LP/vertex problem against
       one fixed background sequence — squarely in scope for
       `vertex-minimum-theorem` + `odd-run-reduction-lemma` applied to this
       narrower target (fix `T`, vary only `F`'s cut positions — a strictly
       smaller polytope than the general problem's, since `G'` is no longer
       a free variable).
     - **(B) Tail-refinement-is-never-helpful claim:** for any fixed `F`
       (in particular the optimal one from (A)), spending any of the n cuts
       refining the tail *instead of* fragmenting `p_1` further can only
       weakly *increase* `A(F∪G')` (never decrease it below the c=n value).
       I re-confirmed numerically (n=4, mixed random c from 0 to n, 200k
       trials) that the minimum over *all* cut-budget splits is attained
       exactly at c=n, consistent with both (A) and (B) holding.
     Together (A)+(B) would fully close the lower bound for every n. This
     decomposition is strictly sharper than the current "Missing
     Inequality"/(★) framing because it isolates *which* half is the truly
     novel combinatorial fact (A, about one fixed geometric sequence) from
     the half that is "just" a monotonicity/exchange argument (B).
  2. **Exchange-smoothing on the merged sorted sequence** (crux analog,
     see below): treat `A(F∪T)` as a weighted sum over sorted rank
     positions with alternating ±1 coefficients, and ask whether a unit
     of "mass" moved from one part of `F` to another (keeping total `p_1`
     fixed) can only move `A` in a controlled direction — i.e., prove
     claim (A) above by a smoothing/exchange argument on `F`'s shape
     directly, rather than full vertex enumeration. This is the natural
     technique match for `aimo-0146`'s crux (see Candidate technique below).
  3. **Surrogate/domination argument for claim (B)**: replace "Xiang Yu
     may refine the tail with cut i" by a pointwise-worse surrogate move
     that is provably at least as good for Xiang Yu as *not* touching the
     tail (i.e. construct an explicit refinement-to-no-refinement reduction
     showing any tail cut can be "undone" without hurting Xiang Yu, then
     induct on the number of tail cuts down to 0). This is the crux move
     from `aimo-0560` (see below) adapted to a monotonicity argument instead
     of a strategy-transfer argument — genuinely different from the
     integral/cross-term machinery already tried four times.

- Candidate technique(s):
  - For claim (A): direct vertex/LP analysis restricted to "vary only `F`,
    `T` fixed" (a strict specialization of `vertex-minimum-theorem` +
    `odd-run-reduction-lemma` to a much smaller polytope — worth trying
    exhaustively for small k = |F| by hand, since `T` is now fixed and
    explicit, before reaching for full generality).
  - Exchange-smoothing on sorted weighted sums (`aimo-0146`'s crux, see
    below) — adapt "move a unit toward the higher-coefficient position
    until profiles equalize" to `F`'s fragment sizes; the fixed +1/-1
    rank-coefficient structure here is a genuine but harder analog (ranks
    depend on where `F`'s elements land relative to `T`'s superincreasing
    gaps, not fixed coefficients as in `aimo-0146`).
  - Surrogate-adversary domination (`aimo-0560`'s crux) for claim (B).
  - Generating-function idea (not yet found a direct hit in the corpus):
    since `T` is geometric with ratio 2, `N_T(x)` (count of tail pieces
    exceeding x) is a step function with dyadically-spaced jumps; the
    parity of `N_{F∪T}(x)` on each of `T`'s `n` dyadic bands is determined
    by how many of `F`'s pieces land in that band — worth trying to write
    `A(F∪T)` as an explicit sum over `T`'s n bands, one term per band
    (a finite, explicit formula in the band-occupancy counts of `F`), then
    directly minimize that discrete functional over all ways to distribute
    `F`'s p_1 units of "mass" across the n+1 bands (0 through n). This
    looks like the cleanest way to actually execute opening 1(A) — not
    attempted here (out of scope: reconnaissance only), but is a concrete
    next step for the outliner.

- Cheap-kill candidates: none obvious for closing (A)/(B) themselves, but a
  useful cheap sanity check before investing in the band-occupancy formula:
  verify by hand for small n (n=2,3) that the "one band, one term" formula
  reproduces the already-certified Odd-Run-Reduction-Lemma vertex values —
  this is cheap (symbolic, no search) and would validate the reformulation
  before the outliner commits an approach to it.

- Knowledge-base entries to use: **Piecewise-concavity smoothing** (algebra
  section) — the general pattern of minimizing/maximizing a function by
  reducing to finitely many templates via smoothing, structurally the same
  shape needed for claim (A)'s "F-shape" optimization; **Invariants &
  monovariants** (combinatorics section) — for claim (B)'s
  "refining the tail can only increase A" monotonicity; **Extreme value
  theorem / Lagrange multipliers on a compact manifold** (Linear Algebra
  section) — formal justification that the min over F's partition simplex
  is attained (already effectively used via `vertex-minimum-theorem`, but
  worth citing directly for claim (A)'s restricted polytope). Do **not**
  reach for **Pigeonhole/extremal principle** generically — already tried
  and refuted (see Dead ends).

- Analogous past problems (cruxes):
  - `aimo-0146` (combinatorics, `extremal-principle`/`double-counting`,
    2017-mathematicians dinner problem): crux move "maximize a fixed
    weighted sum of a sorted sequence under a sum constraint by
    exchange-smoothing weight toward the higher-coefficient positions
    until the free coordinates equalize, then enumerate the few surviving
    profiles." Genuinely analogous *in spirit* to claim (A) above — both
    are "maximize/minimize an alternating- or rank-weighted linear
    functional of a sorted sequence subject to a fixed total" — but not a
    literal transplant: `aimo-0146`'s weights are **fixed** integers
    `1,2,...,63` independent of the sequence's own values, whereas here the
    "weight" (odd vs. even sorted rank) of each of `F`'s fragments is
    *determined by where it falls relative to T's fixed values*, i.e., the
    coefficient structure is itself a function of the unknown. Adapting the
    exchange step (`move a unit from a lower- to a higher-coefficient slot,
    show it strictly/weakly improves the objective, iterate to a few
    extremal profiles`) requires re-deriving, from scratch, how a small
    perturbation of one fragment's size moves it across T's dyadic
    thresholds — real new work, not a citation, but the closest technique
    match found in the corpus for claim (A).
  - `aimo-0560` (combinatorics, `games-and-strategy`, gardener/lumberjack
    IMO 2022 problem): crux move "replace the adversary with a strictly
    stronger surrogate whose reply is pointwise at least as damaging, so a
    win against the surrogate transfers down." Analogous in spirit to claim
    (B): if one can build a "surrogate" tail-refinement move that is
    provably pointwise at least as good for Xiang Yu as *not* refining
    (dominance, not equality), a win against the surrogate (i.e., a proof
    that even the surrogate can't beat the c=n bound) transfers down to the
    real, unconstrained refinement. Structurally different game (one-shot
    static merge here vs. the source's alternating infinite process), so
    again a hint to adapt, not a transplant — but the "surrogate dominance"
    proof pattern is a genuinely different lever than anything the four
    prior approaches have tried.
  - `aimo-0117` (combinatorics, `games-and-strategy`, Jesse/Tjeerd
    dyadic-stones game): **already correctly ruled out** by
    `claiming-order-invariant` (round 4, RETHINK verdict) — its crux
    ("assign values as a two-sided geometric/dyadic sequence so the single
    largest strictly exceeds the sum of all others" + "defer commitment")
    needs a genuine multi-round sequential structure to exploit, which this
    problem's one-shot Stackelberg marking stage does not have. **Do not
    re-suggest this crux** for a defer-commitment framing; it is a
    confirmed dead end. (It remains worth noting only as the source of the
    "largest strictly exceeds sum of rest" dominance idea, which the
    problem's own `dominant-element-removal-identity` and
    `sharp-dominant-removal-identity` already capture more sharply and
    correctly for this problem's actual structure.)

- Prior progress: see `current.md` — full lower bound closed for n=1,2 (both
  directions, no numerics); c=0 case closed for all n
  (`greedy-halving-adversary` Lemma 6); symmetric c=1 split closed
  unconditionally for n=3, conditionally (on the same statement one level
  down) for general n (`tail-self-similarity`,
  `symmetric-split-c1-lower-bound`); Case A of (★) collapsed to one clean
  inequality via `sharp-dominant-removal-identity`
  (`rank-pigeonhole-budget`); c=n achievability proved for all n
  (`general-n-cascade-achievability`/Lemma B1). All of Case A (asymmetric
  c=1, all c≥2) and Case B's minimality remain open before this round;
  this round's numeric work (see above) sharpens the target by isolating a
  fixed-reference-sequence sub-claim (A) that looks more tractable than the
  joint two-multiset problem.

- Dead ends (do not retry):
  - **Generic multiset pigeonhole / majorization restatement of (★)**
    (`rank-pigeonhole-budget` §3): refuted by explicit counterexample
    `F'={10}`, `G'={1^11}` (even-rank sum 6 < 10 = Total(F')). Confirmed
    correct by my own re-check of the arithmetic (Total(F'∪G')=21, sorted
    descending {10,1×11}, even ranks are positions 2,4,...,12, all value 1,
    sum=6). **Do not** propose any version of "even-rank-sum dominates
    Total(F')" as a generic multiset fact — it needs the superincreasing
    structure of the tail specifically, confirmed dead as stated.
  - **"Bisect the global max, n times"** (`greedy-halving-adversary` Lemma
    5): refuted (n=2, Liu Bang marks 0 points, gives Φ=3/4 > 4/7). Do not
    resurrect.
  - **Claiming-order / defer-commitment invariant** transplanted from
    `aimo-0117` (`claiming-order-invariant`, round 4, RETHINK): structurally
    ruled out — no sequential structure in the marking stage for such an
    invariant to exploit. Do not re-attempt.
  - **"c=n endpoint is a free/easy endpoint"** premise
    (`self-similar-bracketing` round 3, Prop. B2): refuted — minimality at
    c=n embeds the identical open obstruction, it is not a free corollary
    of achievability. (This round's numeric confirmation that c=n is
    exactly the worst case makes closing this the single highest-value
    target, not evidence that it's easy — it's exactly as hard as before,
    just now more sharply isolated as claim (A)/(B) above.)
  - **Naive derivative-in-imbalance argument for asymmetric c=1 splits**
    (`greedy-halving-adversary` Prop. 13 discussion): not sign-definite,
    depends on fine local structure of G' at two specific boundary points.
    Do not re-attempt without new structure.

- Small-case / intuition notes (all conjecture, backed only by exact-Fraction
  numerics, not proof):
  - **New this round:** for n=3,4,5, `min_F A(F ∪ T)` over ALL partitions F
    of `p_1` (T = original untouched ladder tail, 300k random-partition
    trials per n) equals `a_n` exactly, matching the target with equality —
    i.e. the achievability construction (Lemma B1) is apparently also the
    true minimizer, not just *a* minimizer. Strongly suggests claim (A)
    above is true and is the right sub-target.
  - **New this round, cross-check:** mixing the cut budget freely between
    "fragment p_1 further" and "refine the tail" (n=4, 200k trials,
    c ranging 0..n) still finds the global minimum exactly at c=n (all
    cuts on p_1, tail untouched) — consistent with claim (B) (refining the
    tail is never advantageous for Xiang Yu) and with the two independent
    round-4 findings (`greedy-halving-adversary` Prop. 13's numeric note;
    `rank-pigeonhole-budget` §4). Three independent numeric checks now
    agree on this, which is reasonably strong evidence but still not a
    proof.
