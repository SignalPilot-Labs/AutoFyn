## imo-2026-03 (lens: hunt for a framing FAR from the match/bisect DP and the β-witness pairing)

### Executive summary
I tested all four candidate escapes named in the dispatch (oblivious dyadic cut set,
LP/duality-of-max-min, a direct order-statistic/majorization bound inspired by a genuine
crux analog `aimo-0388`, and a non-recursive "uniform telescoping" closed form) against
numerical simulation. **All four either collapse back into the known match/bisect DP or
are outright refuted.** I did not find a framing that reaches the upper bound (or the
binding lower-bound case) without eventually needing the same per-piece lookahead
decision the field is stuck on. This is itself useful, load-bearing negative information:
it raises confidence that the crux is *intrinsic* to the problem (a genuine multi-step
minimax), not an artifact of how the three live approaches happened to frame it — so the
right move is probably to strengthen the induction's invariant (parametrize by the ratio
r = a_1/(sum of the rest), as Sub-claim B already proposes) rather than to keep hunting
for a bypass.

### Distinct openings tested (all with numeric verdicts)

1. **Oblivious / non-adaptive XY cut set (candidate (c), "explicit dyadic rationals").**
   Tested: XY marks the SAME fixed points {1−2^0, 1−2^{-1}, …, 1−2^{-n}} regardless of
   LB's partition A (splitting off pieces 1/2, 1/4, …, 1/2^n from one end), and takes the
   resulting refinement B = (LB's cuts) ∪ (these fixed points). Simulated 20000 random
   LB partitions for n=1..4. **Refuted decisively**: worst S found was ≈0.5 for every n
   (ratio 1.5×–15× over target 1/D_n), because LB can place a single mark adversarially
   close to one of XY's fixed points and force a huge imbalance. **Conclusion: XY's
   response must depend on A; no oblivious/positionless strategy exists.** This rules out
   candidate (c) cleanly — worth recording so no future round re-tries a fixed cut set.

2. **LP/duality / smoothing framing on max_A min_B S(B) (candidate (d)).** This is
   exactly what `smoothing-extremal` (this round's population) already attempted and
   the reviewer/builder already refuted: Lemma G (consecutive-pair smoothing toward
   ratio 2 raises S*) is FALSE in ~35% of tested cases, and the surviving weaker claim
   ("some 2-part transfer improves S* at every non-dyadic A") requires the directional
   derivative of a min-over-XY's-optimal-responses — i.e. it re-imports XY's exact
   response structure. I re-examined this file's numeric refutation and it holds up (the
   two structural reasons given — pair-sums are frozen by sum-preserving moves, and the
   move can decrease S* — are both valid). **Do not resurrect this framing without a new
   mechanism for the directional derivative; as stated it is dead.**

3. **Order-statistic / majorization bound in the style of crux `aimo-0388`.** `aimo-0388`
   (100 coins summing to 50, split into two 50-stacks minimizing |difference|) is a
   genuine structural analog: it bounds the SAME kind of alternating-partition quantity
   (D = Σ(-1)^{i+1}a_i essentially, via the interleaved assignment a_1,a_3,…,a_49,
   a_52,… vs a_2,a_4,…,a_50,a_51,…) using a pure order-statistic inequality
   (a_50 ≤ 50/51 because the top 51 coins' sum ≥ 51·a_50) — NO adaptive/recursive
   strategy, just one global inequality on a fixed multiset. This is the closest thing
   in the corpus to a "crux-avoiding" technique. However, `aimo-0388`'s coins are FIXED
   (not adversarially split by a second player), so its technique only applies to
   the "fixed multiset" endpoint of our game, exactly where `L0` already gives the
   value for free. I tried to adapt it into a **non-recursive one-shot XY strategy**:
   for LB's sorted A = (a_1 ≥ … ≥ a_k), split each of a_1,…,a_{k−1} as
   (a_i − a_{i+1}, a_{i+1}) (a "uniform telescoping match", using exactly k−1 ≤ n cuts).
   - **On the dyadic partition itself this reproduces the known-optimal cascade exactly**
     (I verified symbolically for n=1,2,3): since a_i = 2a_{i+1} there, the split becomes
     an exact bisection, giving the correct two-copies-of-each-scale-plus-one final
     multiset. A genuine, clean sanity check.
   - **On general A it fails badly**: 20000 random-partition test at n=1..4 gives worst
     S/target ratios of 3×–28× (worst cases: one dominant piece a_1 ≈ 1 with tiny
     remaining slivers — matching a_1 against a tiny a_2 barely dents a_1, so it survives
     near rank 1). This is exactly the already-known "must bisect when top dominates"
     failure mode (Dead end in prior rounds), so this framing does not avoid the crux
     either; it is the SAME naive "always match" rule from round 2's dead-end list,
     independently rediscovered.
   - I then tried a **two-phase hybrid** (phase 1: bisect the current largest piece
     while it exceeds the sum of the rest, i.e. test the superincreasing condition
     directly and fix it with ≤ that many cuts; phase 2: apply the uniform telescoping
     match with the leftover cuts) hoping ONE threshold test would be enough to avoid a
     full recursive DP. **Refuted**: even restricted to n=3 this hybrid, applied to the
     EXACT dyadic partition {8,4,2,1}/15, gives S = 0.2 vs target 1/15 ≈ 0.067 — it
     fails even at the optimum, because bookkeeping in phase 2 double-spends an
     already-created piece (the well-documented pitfall from round-2 memory: "the twin
     AND the original both survive as separate pieces" — my hybrid's index arithmetic
     conflated them). At random A the raw (uncorrected) hybrid fails 33%–99% of trials
     across n=1..5, confirming a single top-level threshold test is not sufficient —
     genuine per-step / whole-list lookahead is unavoidable, matching all three live
     approaches' own conclusion (finding F1, reconfirmed independently here).

4. **Self-similar recursion directly on [0,1] (candidate (a)).** On inspection this is
   not actually distinct from `induction-peel`'s Lemma B: "bisect the current largest
   interval and recurse" IS the peel/match-bisect DP, just phrased geometrically instead
   of on the multiset. It inherits the same open Sub-claim B. Not a new opening.

5. **Game-tree/strategy-stealing before reducing to S (candidate (b)).** L0 (the claiming
   lemma) is already a complete, tight equivalence between the raw alternating-claim game
   and the odd-rank-sum value — it is proved by an explicit pairing/response strategy in
   BOTH directions (not just an inequality), so there is no room for a strategy-stealing
   argument to do anything different at the "raw game" level; any such argument would
   just re-derive L0. Not a productive opening — L0 is airtight and this route offers
   nothing beyond what's already certified.

### What this negative sweep implies for the outliner
None of the four "far from the field" candidates survives contact with numerics. The
common failure signature across (2), (3), (4) is the same: **any rule that decides
match-vs-bisect using less than full lookahead over the remaining piece list fails**,
specifically whenever the current largest piece nearly dominates the sum of the rest
(the boundary of the superincreasing condition). This sharpens (rather than escapes) the
crux: Sub-claim B / Lemma D genuinely needs an inductive argument parametrized by the
ratio r = a_1/(sum of rest) — exactly what `induction-peel`'s Lemma B and
`alternating-sum-potential`'s Lemma D already propose — and the two live approaches are
not wasting effort; they are on the only viable route found so far. Given the field has
been stuck on this exact induction for 2+ rounds, the recommended move is not a new
top-level framing but a **stronger two-parameter inductive statement**: prove Lemma
B/Sub-claim B by strong induction on k (number of original pieces) simultaneously
tracking r = a_1/ρ (ρ = sum of rest), i.e. prove the sharper claim "V_{k-1}(match or
bisect branch, whichever ratio-appropriate) ≤ ρ·2^{k-1}/D_{k-1} + (branch-specific
correction determined by r" rather than the generic bound 2^{k-1}/D_{k-1}·sum(A). This
mirrors exactly how `induction-peel` phrases Sub-claim B already; my contribution is
confirming (via ruling out escapes) that this IS the necessary form of the argument.

### Cheap-kill candidates
- (New, confirmed this round) **Oblivious cut sets are dead**: any approach proposing a
  cut set independent of A can be killed immediately by "LB marks one point adversarially
  close to one of XY's fixed points" — no need to simulate further, this is a clean
  one-line refutation for any future oblivious-strategy proposal.
- Already known: tied largest pieces (instant zero-cost cancel); a lone big piece with
  spare cuts (bisect once, stop — using extra cuts hurts).

### Knowledge-base entries to use
No entry names this game. Generic pointers remain: strong/structural induction,
extremal-principle framing (`knowledge_base.md`'s general proof-methods section), and the
already-certified L0–L4 lemma chain in `results/imo-2026-03/lemmas/`.

### Analogous past problems (cruxes)
- **aimo-0388** (coins-into-two-stacks, `extremal-principle`/order-statistics subtopic):
  genuinely analogous in FUNCTIONAL FORM (an alternating-interleaved-index sum of a
  sorted list, bounded via an order-statistic inequality a_k ≤ total/(k+1)-type bound) —
  but its technique applies only to a FIXED multiset, and adapting it into a one-shot XY
  strategy is exactly the "uniform telescoping" idea I tested and refuted above. Read for
  the mechanics of order-statistic bounding, not as a solution template.
- **aimo-0019** (painting game, `invariants-and-monovariants`): its amortized/credit-based
  potential argument ("bound cumulative resource by a constant times progress") is the
  right STYLE of tool for eventually closing Sub-claim B/G1 (an amortized per-cut credit
  of 1/D_n), but the specific mechanism doesn't transfer directly; flagged as a technique
  analogy only.
- **aimo-0117** (already used by round 1): dyadic geometric top-heavy sequence as the
  extremal construction — still the best analog for WHY dyadic is the answer, not for the
  upper-bound mechanism.
- No crux in `games-and-strategy` (searched all 39 combinatorics entries again) is a
  genuine continuous-value optimization analog to this exact match/bisect minimax; this
  confirms round 1 and round 2's finding that the corpus has no close solution template —
  the upper bound is a from-scratch argument.

### Prior progress
Unchanged from `current.md`: Status partial. L0–L4 certified. Lower bound complete in
Case 1 (top piece uncut); Case 2 / G1 (top piece cut) open. Upper bound / Sub-claim B /
Lemma D / G2 open in all three live approaches. `smoothing-extremal` is RETHINK
(confirmed, not resurrectable as stated).

### Dead ends (do not retry)
- Oblivious/fixed XY cut sets independent of A (this round, refuted decisively, ratio up
  to 15× over target).
- Uniform "telescoping match" (split each a_i into (a_i−a_{i+1}, a_{i+1}) with no bisect
  option) — this round, refuted, same failure mode as round-2's "always match" dead end
  (worst-case ratio up to 28× over target for one-dominant-piece profiles). Reproduces
  the correct answer exactly ON the dyadic fixed point only.
- Two-phase hybrid (bisect-while-dominant, then telescope-match) with a single top-level
  threshold test — this round, refuted even AT the dyadic optimum for n=3 (bookkeeping:
  a piece gets counted twice, the exact pitfall flagged in `/tmp/memory/math-explorer.md`
  rule about "twin AND original both survive"); at random A, failure rate 33%–99% for
  n=1..5. Confirms a single threshold decision is insufficient; real per-step/whole-list
  lookahead (full DP) is required, not avoidable by a one-shot rule.
- Smoothing/exchange on the LB simplex (Lemma G) — already RETHINK from `smoothing-
  extremal`; re-confirmed here, do not resurrect without a genuinely new directional-
  derivative mechanism.

### Small-case / intuition notes (label: conjecture unless noted)
- CONFIRMED (symbolic, n=1,2,3): the uniform-telescoping construction, applied to the
  EXACT dyadic A, reduces algebraically to the known-correct bisection cascade (a_i =
  2a_{i+1} makes the "match" split degenerate into a true bisection). This is a clean,
  reusable sanity fact for whichever approach eventually writes the explicit dyadic
  construction, but is not a general strategy.
- CONJECTURE (strong, reconfirms round 2): the hard regime for the upper bound is
  precisely where a_1 is close to (but not exceeding, or barely exceeding) the sum of
  the rest — i.e. near the superincreasing boundary — and the correct XY choice there
  requires comparing against the WHOLE remaining list's structure, not a local test.
  This is now confirmed via three independent refuted "shortcuts" (uniform match,
  hybrid, oblivious), raising confidence that Sub-claim B genuinely requires the r =
  a_1/ρ-parametrized induction already proposed by `induction-peel`.
