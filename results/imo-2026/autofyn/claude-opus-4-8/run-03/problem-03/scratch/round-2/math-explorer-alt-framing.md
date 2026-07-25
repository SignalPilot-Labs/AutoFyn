## imo-2026-03 (lens: alternative upper-bound framing, avoiding the shared match/bisect primitive)

- Distinct openings (new framings for the upper bound c(n) ≤ 2^n/D_n, D_n=2^{n+1}-1):

  1. **Matching/dual-certificate framing (verified identity, genuinely new tool — not used by any of the 3 current approaches).**
     Claim (checked numerically on random 3–5 element lists, exact to floating point):
     for sorted descending y_1≥…≥y_m≥0, the alternating sum S=Σ(-1)^{i+1}y_(i) equals
     **the MINIMUM, over all ways to pair up the m elements into disjoint pairs (with one
     leftover element if m is odd), of Σ_{pairs}|y_i−y_j| + y_leftover**, and this minimum
     is attained by pairing consecutive elements in sorted order. (This is the classical
     "minimum-cost matching of points on a line = adjacent pairing" fact, provable by a
     standard uncrossing/exchange argument — cite as an exchange-argument / rearrangement
     lemma, kin to the "exchange-smoothing" technique in crux aimo-0146.)
     Consequence: **to prove S ≤ V for XY's actual final configuration, XY does NOT need
     to determine ranks or parity of any piece.** He only needs to exhibit ONE explicit
     pairing (of his choice, not necessarily optimal) of the pieces he creates, with total
     cost ≤ V — since the true S is the MINIMUM over all pairings, any witness pairing
     upper-bounds it automatically. This converts the "hardest gap" (Lemma B/D/F in all
     three current approaches — proving a precise claim about which rank a given piece
     lands at) into a much lighter combinatorial task: construct a cutting scheme AND a
     matching certificate, no rank/parity bookkeeping at all.
     **Key inequality needed:** exhibit, for arbitrary LB partition a_1≥…≥a_k (k≤n+1,
     sum 1), a set of ≤n cuts and an explicit pairing of the resulting pieces (one
     leftover) with Σ|pair diffs| + leftover ≤ 2^n/D_n.
     **Why it might avoid the wall:** the current approaches all get stuck precisely on
     proving an exact rank-position / parity claim under adversarial cutting (see "Watch
     out" sections of all three approach files — slivers, parity of final count, "which
     rank"). The matching-certificate reduces the proof burden to "produce A witness",
     which is existential, not "prove THE actual rank assignment has property X".
     **What stays a gap (be honest):** the natural witness pairing is essentially the same
     "carry a leftover, match it against the next piece down, else bisect" construction
     already used by all three approaches — I re-simulated a naive greedy version of this
     (see numeric notes below) and it is easy to get the case split wrong (I found and
     fixed a genuine bug: matching the *next* original piece whenever carry≥q is WRONG,
     the correct move is a=max(carry/2, min(carry,q)), i.e. match only when q≥carry/2,
     else bisect — exactly the round-1 explorer's rule). So this framing likely still
     needs the SAME core case-split (match-when-q-large / bisect-when-q-small) — it is a
     genuine **proof-technique simplification** (no rank tracking, no parity-of-final-
     count case split, no "slivers sort to the global bottom" worry) rather than a fully
     independent escape from the wall. Recommend the outliner try it as approach #4: same
     underlying strategy, different (lighter) certificate machinery — worth a shot since
     the current three are stuck on the bookkeeping, not the strategy itself.

  2. **Probabilistic/existence framing (unexplored, speculative).** Instead of an
     explicit deterministic XY strategy, define a randomized cutting rule (e.g. random
     dyadic-style subdivision of the current largest piece) and show E[S] ≤ 1/D_n for
     every LB partition; since XY moves with full information (not actually randomized),
     existence of a cut sequence with S ≤ E[S] follows and suffices — a probabilistic
     existence argument standing in for an explicit strategy (kin to `probabilistic-
     method` subtopic in the combinatorics corpus). I did NOT verify this computationally
     (no natural random rule was obvious in the time budget) — flag as open, not validated.

  3. **Convexity-of-order-statistics framing (unexplored, more speculative).** T_k(x) =
     sum of the top-k order statistics of a vector x is a max of linear functionals (over
     k-subsets), hence convex in x. Odd-rank sum = Σ_k (-1)^{k+1} T_k(final pieces)
     (telescoping T_k−T_{k-1}=p_(k)). This recasts the whole problem in terms of a fixed
     alternating combination of convex functions of the (cut-created) piece vector. I did
     not find a clean way to exploit this alternation (differences of convex functions
     aren't generally convex) inside the time budget — flagging as a possible tool for
     the outliner to explore, not a working argument.

  4. **LP relaxation / dropping the "≤ n+1 parts, ≤ n cuts" combinatorial constraint and
     solving the CONTINUOUS relaxation first** (a smoothing/extremal-principle move akin
     to aimo-0146's "exchange-smoothing weight toward the higher-coefficient position").
     Treat LB's choice as any nonneg. vector summing to 1 with unboundedly many parts
     and ask: what continuous LB profile maximizes worst-case odd-rank-sum against best
     XY response with n cuts, INDEPENDENT of parts-count constraints? If the relaxed
     optimum is provably the dyadic profile via smoothing/exchange (majorization-style,
     as in aimo-0146), the ≤n+1-part constraint can be shown non-binding at the optimum,
     converting the discrete "hardest gap" into a smoothing argument. Not attempted
     numerically — flagged as an opening, unverified.

- Candidate technique(s): matching/assignment-problem duality (opening 1, most concrete);
  probabilistic method (opening 2); convexity of top-k order-statistic sums (opening 3);
  majorization/exchange-smoothing as in aimo-0146 (opening 4).

- Cheap-kill candidates: none new found beyond what's already in the population (tied
  pieces cancel free; slivers sort to global bottom, cannot flip local parity — both
  already flagged by prior approaches and still valid).

- Knowledge-base entries to use: no entry in `knowledge_base.md` is named for "minimum
  matching of points on a line" or "order-statistics convexity" — these would need to be
  proved from scratch as elementary exchange-argument lemmas (the KB's general "Standard
  inequalities" AM-GM/rearrangement entry, line 33, and the "General Proof Methods"
  extremal-principle framing, lines ~177-196, are the closest generic pointers; cite the
  exchange/uncrossing argument explicitly since no KB entry names it directly).

- Analogous past problems (cruxes):
  - `aimo-0117` (already flagged round 1): dyadic top-heavy geometric sequence
    (largest > sum of rest) as the extremal construction in a turn-based value game —
    still the best structural analog for WHY dyadic is optimal, but it's a win/lose
    threshold game, not a value-optimization game, so its proof technique (deferred
    commitment to an invariant slot) doesn't transfer to the upper bound directly.
  - `aimo-0146` (extremal-principle, combinatorics): "maximize a fixed weighted sum of a
    sorted sequence under a sum constraint by exchange-smoothing weight toward higher-
    coefficient positions" — a genuinely relevant TECHNIQUE analog (majorization/exchange
    smoothing on a weighted-sorted-sequence functional, exactly our odd-rank-sum
    functional's shape) even though the underlying problem (dinner-cost maximization) is
    unrelated in content. Worth reading for the mechanics of an exchange argument on a
    sorted-sequence weighted sum, which is structurally what opening 4 would need.
  - No crux in `games-and-strategy` (searched all 40 combinatorics entries) is a genuine
    continuous value-optimization analog; all are discrete win/lose pairing games
    (dominoes, parity-of-legal-move games) — confirms round-1's finding that the corpus
    has no close match for the actual upper-bound mechanism needed here.

- Prior progress: `results/imo-2026-03/current.md` is still Status=unsolved (round 1 just
  produced the 3 approach files; no lemmas certified yet, no round-1 build happened in
  what I can see — only outline-review APPROVE was issued for induction-peel and
  alternating-sum-potential, "explicit-certificate" sent back CHANGES REQUESTED). All
  three share the L0/L1 reduction (multiset game via alternating claiming) and the
  lower-bound mechanism (superincreasing dyadic forces small parts to even ranks); the
  upper bound is open in all three, and the reviewer already warned they may share one
  wall (match/bisect per-cut recursion / rank tracking).

- Dead ends (do not retry):
  - `explicit-certificate`'s Lemma F(a) "XY should concentrate cuts on the largest part,
    never spread" — REFUTED by round-1's reviewer (counterexample {0.428,0.410,0.162} at
    n=2: concentrating stays ≥ 4/7, true optimum needs spreading/slivering to reach
    ≈0.5101). Confirmed this stands; do not resurrect concentrate-only as a strategy.
  - My own first "greedy match if carry≥q" simulation (this round) initially looked
    badly wrong (worst case →1.0), but this was because it matched whenever carry≥q
    (wrong direction) instead of a=max(carry/2, min(carry,q)); once fixed to the correct
    rule the failures were all traceable to my simulation forcing XY to use ALL n cuts
    even when a cut doesn't help (e.g. LB plays a single unmarked piece — XY should
    bisect ONCE and stop, not keep bisecting; using both allowed cuts when only one
    helps drove the simulated value to 0.75 > target). This is a simulation artifact, not
    a refutation of match/bisect — but it is a genuine warning: **any builder's argument
    must explicitly handle "XY need not use all n cuts"** (all three approach files
    already say "≤n cuts" but a builder could easily make this exact bug — forcing full
    cut usage overshoots the bound). Flag this as a concrete pitfall to watch for.

- Small-case / intuition notes (all CONJECTURE / simulation, not proof):
  - Confirmed (numerically, exact-arithmetic small cases, m=3..5 random floats): the
    min-cost-matching identity for S holds exactly to floating-point precision — this is
    a real, checkable, provable-from-scratch fact (standard exchange argument), a solid
    foundation for opening 1.
  - Re-confirmed round-1's finding: the correct per-step XY rule is a = max(C/2,
    min(C,q)) (match when next piece q ≥ carry/2, else bisect); a naive "always match
    when possible" rule is wrong in both directions (matching tiny q wastes the cut and
    is bad, matching without the max/min clamp when q huge is also wrong) — the clamp is
    essential and any approach (old or new framing) needs it stated exactly this way.
