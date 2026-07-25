## imo-2026-03 — fresh-framing / plateau check

### 1. Is Proposition C structural, or an artifact of setup?

Verified the proof of Proposition C (in `approaches/self-similar-induction-on-n.md`)
line by line; it is a genuinely correct, fairly *robust* obstruction, but its scope
is narrower than "any induction whatsoever" — it kills exactly the mechanism:
**"peel the single current maximum, reduce OddSum(whole) to a scalar EvenSum-bound
on the rest, and try to close that bound by re-applying the same peeling step."**
The mechanism is: Peeling Lemma (`OddSum(M)=max(M)+EvenSum(M\{max})`) + Lemma Z
(z-trick, `EvenSum(X)=OddSum({z}∪X)-z` for `z≥max(X)`) together force the
residual bound `U(m,k)` to be *literally* an instance of `G(m,k;V)` with one
**more** fragment, not fewer — so **any** proof that goes through "peel top,
bound the rest by a single scalar (its own OddSum/EvenSum value), recurse" hits
this same wall, regardless of which specific approach or which specific
tail-structure lemma is used to try to close the residual. This is because the
argument only uses two facts: (a) the residual multiset is exactly `B'∪S` for a
strictly larger fragment set `B'`, and (b) Lemma Z is an *identity*, so there is
no freedom to dodge it by proving the residual bound differently — the residual
bound literally *is* the next-fragment-count instance, by definition, not merely
implied by it. So the circularity is a property of the **target quantity**
`OddSum(B∪S)` under "peel one element, track only a scalar sum," not of the
`greedy-reduction-geometric` / `self-similar-induction-on-n` write-ups
specifically. Both of them independently landing on it (from different starting
setups) is real corroborating evidence, not a coincidence of shared bad
technique choice.

**What Proposition C does *not* rule out** (both explicitly noted by the
approach itself as still open routes): (a) peeling while tracking a *richer*
invariant than a scalar bound — e.g. the full sorted order-statistics profile of
the residual, which is exactly how `T(2)`'s `j=2` case was closed by hand
(Theorem 1) — this is not "peel + one scalar," it is direct computation, and it
worked; (b) not peeling the top piece at all — a genuinely different top-level
target. So the honest verdict: **the wall is real and structural to the single-
peel/scalar-bound family specifically**, and 3 rounds of the two live
lower-bound approaches are variants of exactly that family. This satisfies
CLAUDE.md's plateau trigger: the population needs ≥1 approach that is not
"peel the top piece + scalar residual bound" in disguise.

### 2. Two genuinely different top-level framings (not peeling-induction)

**(A) Threshold / layer-cake parity reformulation of OddSum.** For any finite
multiset of positive reals `x_1,...,x_k`, define the level function
`N(t) = #{i : x_i ≥ t}` for `t>0` (a decreasing integer step function, `N(t)=k`
near `t=0`). Standard layer-cake plus a sign-count argument gives, for the
sorted list `x_(1)≥...≥x_(k)`:
$$\mathrm{OddSum}-\mathrm{EvenSum}=\sum_r(-1)^{r+1}x_{(r)}=\int_0^\infty \mathbb 1[N(t)\text{ is odd}]\,dt,$$
because `x_(r) = ∫_0^{x_(r)} dt`, and swapping the sum and integral, the
coefficient of `dt` at threshold `t` is `Σ_{r≤N(t)} (-1)^{r+1}`, which is `1` if
`N(t)` is odd and `0` if even. I verified this identity numerically (5 random
multisets, sizes 1–4, fine numerical integration vs. exact OddSum−EvenSum,
agreement to 4+ significant figures every time; script used
`numpy.linspace` fine-grid threshold counting). Combined with
`OddSum+EvenSum = S` (total, fixed), `OddSum = (S + ∫1[N(t) odd]dt)/2`.

This reframes the **entire** lower-bound problem (not just the geometric
piece) as: LB picks an initial step function `N_0` (height `k` near `0`,
dropping to `0` at `t=1`, `k≤n+1` steps); a "split" of piece `p_i` into `j+1`
fragments does *not* touch `N(t)` for `t>p_i` at all, and on `(0,p_i]` it
refines the single unit drop into up to `j+1` finer drops (a "staircase"
replacing a single step) — a purely **local, per-piece, additive**
modification to the level function, independent of which piece is largest.
XY's whole strategy becomes: distribute an `n`-cut budget across the pieces to
choose staircases minimizing `∫1[N(t) odd]dt`, where `N(t) = Σ_i (contribution
of piece i's own staircase at t)`. This is symmetric in "top piece vs. others"
by construction — it sidesteps the very asymmetry (top piece is special) that
Proposition C's peeling exploits and gets stuck on. It is also the natural home
for a **generating-function** argument: `(-1)^{N(t)} = ∏_i (-1)^{[\text{piece }i
\text{'s staircase is still "up" at }t]}`, so `1[N(t)\text{ odd}] =
(1-∏_i s_i(t))/2` with `s_i(t)=±1` per-piece signs — a product structure over
independent pieces, which is exactly the shape generating-function techniques
exploit (expand the product, each cross-term corresponds to a subset of pieces
"simultaneously above threshold `t`" — matches the dispatch's suggested
generating-function angle). This is new; no approach in the population has
used this reformulation. It is a genuine reduction (proved above, not a
conjecture) but turning it into a proof of the lower bound is unstarted work —
report it as an opening, not a result.

**(B) Adversary-strategy-first / explicit-formula framing.** Rounds 2–3 found
(numerically, via full integer-partition-of-cut-budget sweeps with
random-restart local search) that XY's *actual* optimal responses to the
geometric partition concentrate cuts near the top, sometimes recursing into
the 2nd-largest piece, and that these responses hit exactly the target value
on a whole face/plateau, not a point (see rules in `/tmp/memory/math-explorer.md`
entries on this). Framing (B) is: stop inducting on "smaller instance of the
same problem" at all — instead conjecture an **explicit closed-form recursive
formula** for XY's optimal cut-allocation-and-split rule as a function of
`(m,k)` directly (using the numeric plateau/tie structure already mapped out
as data), prove that this *specific* strategy achieves exactly `OddSum=2^m` on
the nose for every `(m,k)` by a direct computation (in the flavor of Theorem
1's `m=2` hand computation, generalized), and *separately* prove no other
allocation can do better, via a **global exchange/majorization argument
directly on cut-allocations** (not on multiset structure) — e.g., show that
moving one cut from a non-optimal-rule location to the rule's location can only
decrease OddSum, argued once, globally, over the whole allocation space, rather
than by peeling one piece and inducting on what remains. This treats `c(n)` (or
`T(m,k)`) as a genuine **recursive sequence in `k`** at fixed structure, closer
to the dispatch's "recursive sequence" suggestion, and is a different
organizing variable (cut-budget `k`, not fragment-count-after-peeling `j`)
from what Proposition C's obstruction is about.

### 3. Crux corpus check (broadened beyond games-and-strategy)

Read `crux_moves_documentation.md` for schema; queried `combinatorics` domain,
`games-and-strategy` (39 hits) plus a keyword scan (`threshold`, `layer`,
`tail-count`) across all cruxes.

- **`aimo-0127`** (combinatorics, `double-counting`) — technique: *"Rewrite a
  weighted total as a sum over weight thresholds of tail-counts (number of
  items of weight ≥ the threshold), so a per-threshold cap can be applied."*
  The problem statement (`past_problems_database.json`) is Alice/Bob
  alternately building a spanning tree on `n` labeled vertices, edge weight
  `|i-j|`, Alice maximizes / Bob minimizes total weight `W` — structurally
  close in *spirit* (alternating max/min game on a sum, threshold/tail-count
  decomposition as the crux move) to framing (A) above. Caveat: the
  `solutions` field returned for this `problem_id` in the corpus is visibly
  mismatched (it's about a GCD/polynomial construction, unrelated to the
  spanning-tree statement) — a data-quality issue in this corpus entry, so I
  could **not** verify the actual worked proof, only the `problem` statement +
  `technique` string. Treat as a **structural hint that the threshold/tail-
  count decomposition is a known, load-bearing technique in exactly this kind
  of alternating-game-on-a-weighted-sum setting**, not as a verified worked
  example to imitate step-by-step.
- **`aimo-0596`** (games-and-strategy) — alternating card-claiming game with a
  symmetric-difference (mod-2 XOR) invariant and pairing/involution strategy.
  Superficially close (alternating claim of items from a fixed set to
  optimize a final tally) but the underlying algebra is `GF(2)` set-XOR, not
  real-valued sums with an order-statistics payoff — I judge this **not
  genuinely analogous** beyond the shallow "alternating claim game" framing;
  do not force it.
- **`aimo-0560`** (surrogate-adversary substitution) — already surfaced round
  2, still the closest game-theoretic crux on file (replace the real opponent
  by a provably-at-least-as-damaging surrogate whose reply reduces to a finite
  menu); still worth keeping in mind for framing (B)'s "prove no allocation
  beats the explicit rule" half, but not new this round.
- No crux in the corpus directly matches "alternately claim items from a
  known finite multiset, sorted-descending odd/even-rank payoff" — this
  confirms round 2's finding (the reduction to `OddSum` is the problem's own
  literal structure, not a technique borrowed from elsewhere); the closest
  genuine technique match is `aimo-0127`'s threshold/tail-count decomposition,
  which independently supports framing (A) as a real, previously load-bearing
  idea in this exact problem shape, not just something I invented in
  isolation.

### Report

- Distinct openings: (A) threshold/layer-cake parity reformulation
  `OddSum-EvenSum = ∫1[N(t) odd]dt` (proved above, numerically verified),
  turning the lower bound into a per-piece-additive, non-peeling problem —
  potentially connects to a generating-function/product argument over pieces;
  (B) adversary-strategy-first framing: conjecture-then-verify an explicit
  closed-form optimal XY response as a function of cut-budget `k` (not
  fragment-count `j`), proved via a *global* exchange argument on allocations,
  organizing the induction on `k` instead of on "smaller instance after
  peeling."
- Candidate technique(s): layer-cake/threshold decomposition (crux
  `aimo-0127`'s technique name, structurally close); generating functions
  (`combinatorics` subtopic, via the sign-product `(-1)^{N(t)}=∏ s_i(t)`
  identity in framing (A)); global exchange/majorization argument on cut
  allocations (framing (B)).
- Cheap-kill candidates: before investing in framing (A), numerically check
  whether the *aggregate* per-piece staircase optimization (min over
  independent per-piece choices of `∫1[N(t) odd]dt`, budget-constrained across
  pieces) actually reaches the conjectured `c(n)` value at small `n` — if the
  reformulation's numeric optimum doesn't match `2^n/(2^{n+1}-1)`, something
  in the reformulation's game-theoretic bookkeeping (order of moves, LB's
  outer choice) needs fixing before it's worth writing up as an approach.
- Knowledge-base entries to use: check `knowledge_base.md` for any existing
  layer-cake / order-statistics / generating-function entries (not
  independently re-read this round beyond what's cited in the approach files
  above — the outliner should cross-check against the KB's exact entry names
  before citing).
- Analogous past problems (cruxes): `aimo-0127` (threshold/tail-count
  decomposition of a weighted sum under an alternating max/min game — best
  structural match, but its corpus `solutions` field is corrupted/mismatched,
  so only the technique name + problem statement are usable, not a verified
  worked proof); `aimo-0560` (surrogate-adversary reduction, already known,
  relevant to framing (B)); `aimo-0596` judged NOT genuinely analogous (XOR
  invariant, different algebra) — flagging so no future round forces it.
- Prior progress: see `current.md` — reduction to
  `max_partition min_refinement OddSum` fully proved; `c(0),c(1)` fully
  solved; `T(2)` (lower bound `n=2`) fully closed; Dominant-Chain regime
  closed for all `n`; upper bound closed except the balanced/near-uniform
  region `p1<1/2, p_{n+1}>1/(2^{n+1}-1)`. Both remaining gaps are precisely
  characterized (see current.md "Open" section) — this report does not
  change that characterization, it adds two candidate *routes around* the
  lower-bound gap's proved circularity.
- Dead ends (do not retry, confirmed this round by re-reading the proof, not
  just trusting the label): static Q-priority strategy (round 2); static
  tail-priority strategy (round 3); literal single-step Cut-Reallocation
  Exchange Lemma (round 3); Lemma X′ (rounds 2–3, disproved by explicit
  counterexample); **and now, more precisely stated**: any "peel the current
  maximum, bound the rest by its own scalar OddSum/EvenSum value, recurse"
  mechanism for Case A (`b1≥2^{m-1}`) of the lower bound — this is not merely
  "unclosed," it is *proved circular* (Proposition C), so re-deriving another
  scalar-bound variant of it (under a new name) should not be attempted again
  without first checking it against Proposition C's z-trick argument.
- Small-case / intuition notes (conjectural unless stated proved above): the
  layer-cake identity itself is proved (elementary, not conjectural) and
  numerically spot-checked (5 random multisets, agreement to 4+ sig figs).
  Whether framing (A)'s per-piece-additive reformulation actually makes the
  minimax *easier* to close (vs. just being an equivalent restatement) is
  untested this round — flagged as the first thing to check numerically
  before committing an approach slug to it.
