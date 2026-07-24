## imo-2026-03

- **Distinct openings** (all deliberately avoiding the `M(P) = measure{t : #pieces>t odd}`
  layer-cake reduction that all three round-1 approaches share):

  1. **Discrete domination / "power dominates the rest" invariant (closest analog to a
     genuinely different technique).** Instead of `f(P) = ∫ 1[c(t) odd] dt`, work directly
     with the *recursive* identity `f(P) = a_1 − f(P∖{a_1})` (true for any multiset — this
     is just "remove the max, recurse", no integral needed) and the elementary fact
     `0 ≤ f(Q) ≤ Σ(Q)` for any `Q`. Together these give, for **any** final multiset `P`,
     `f(P) ≥ 2·max(P) − Σ(P)`. I verified this numerically (20000 random multisets, 0
     violations) — see Small-case notes. This is exactly the identity Case 1 of
     `self-similar-recursion.md` already uses, but stated as a **standalone global fact**,
     independent of the threshold/measure machinery. The open question is whether a
     *recursive strengthening* of this same inequality (applied at every level of the
     dyadic hierarchy, tracked turn-by-turn as XY's cuts arrive one at a time in an
     adversarially-chosen order, rather than casework on "how many cuts hit the top") can
     close Case 2. This mirrors the crux move in `aimo-0117` (see below): maintain an
     explicit *invariant* — "the largest not-yet-disturbed dyadic value dominates the sum
     of everything smaller" — turn by turn, rather than computing a global integral once
     at the end.
  2. **Self-similar scaling / strategy-stealing on the sub-stick.** Treat the top dyadic
     piece `2^n/D_n` together with the "rest" `D_{n-1}/D_n` as two coupled sub-games, and
     ask directly: is the whole-game value a *fixed point* of a scaling recursion
     `c(n) = φ(c(n-1))` proved by strategy-stealing (LB's play on the sub-stick of relative
     size `D_{n-1}/D_n` literally **is** an instance of the budget-`(n-1)` game, scaled)?
     This is the natural "different top-level target": prove a **recursion in `c(n)`
     directly** instead of proving two extremal bounds on `M`. I looked for the obstruction
     and found it immediately: **XY's budget is a single pool of `n` cuts usable anywhere
     on the stick**, not partitioned in advance between "top piece" and "rest". So the
     sub-game on the remainder is NOT a clean independent copy of the `(n-1)`-budget
     problem — XY can choose adaptively how many of his `n` cuts to spend on the top vs.
     the rest, *after* seeing what happens in one region. This cross-region budget-sharing
     is (I believe) the actual reason GAP-LB/GAP-UB resist a one-shot certificate in every
     approach so far: it is a genuine game-theoretic coupling, not an artifact of the
     layer-cake formalism. Worth flagging to the outliner explicitly as **the real
     obstruction**, so a new approach must show budget-sharing never helps XY (a "budget
     tax" or "adaptivity gains nothing" lemma) rather than just re-deriving the reduction.
  3. **Kraft-inequality / binary-tree (prefix-code) reformation.** Since the extremal
     configuration is exactly dyadic (`2^0,...,2^n`), consider modeling the whole cut
     process as a rooted binary tree (each bisection = one level down), with leaf `i`'s
     length `= 2^{-depth(i)}` relative to its subtree. Kraft's equality
     `Σ 2^{-depth(i)} = 1` for a full binary tree is suggestive of the dyadic weight
     structure, and might give a clean **combinatorial** (not measure-theoretic) accounting
     of "odd vs even rank" in terms of tree depth parity. I did not find a clean
     correspondence between *sorted rank parity* (which is what `Odd(P)` needs) and *tree
     depth parity* for a non-uniform tree (LB's/XY's cuts need not bisect), so this
     framing looks promising in spirit but requires the depths to be forced to align with
     ranks — an open translation step, not yet a working reduction. Flag as a candidate but
     unverified; likely absorbs into (1)/(2) once formalized.
  4. **LP-duality / minimax certificate directly on cut positions (not on the resulting
     multiset).** Treat LB's choice of `≤n` real numbers in `[0,1]` and XY's `≤n` real
     numbers as a two-stage zero-sum game with a continuous, piecewise-linear payoff
     (`Odd(P)`); von Neumann's minimax theorem applies (compact convex-ish decision sets,
     but payoff is **not** jointly concave/convex — the "take-the-largest" endgame makes
     `Odd` piecewise linear but not concave in XY's cuts), so a **clean LP duality
     certificate is not obviously available** — the value function has combinatorial kinks
     from re-sorting, which is exactly why a measure/threshold trick was invented in round
     1. I do not recommend pursuing bare LP duality without first linearizing via some
     combinatorial encoding (i.e. it likely collapses back into the layer-cake or the
     matching reformulation already in the population).

- **Candidate technique(s) for the outliner:** (1) is the most promising *and* the most
  clearly distinct from all three current approaches: an explicit, turn-by-turn dominance
  invariant (`current max strictly exceeds sum of all smaller pieces so far`), proved by
  strong induction over the *sequence* of XY's cuts (processed one at a time, in whatever
  order is worst for LB), directly analogous to the `aimo-0117` strategy — rather than
  integrating a parity indicator over a continuum of thresholds. (2)'s framing ("prove a
  recursion in `c(n)` via strategy-stealing on the sub-stick") is valuable **even if it
  fails**, because pinpointing the budget-sharing obstruction explicitly is itself useful:
  it tells the outliner the two current GAPs are not an artifact of layer-cake, they are
  the genuine combinatorial content of the problem, so any correct proof (any framing) must
  confront "XY's shared budget across regions."

- **Cheap-kill candidates:** none new found (the `2·max − Σ` inequality gives a **quick
  correct partial re-derivation** of Case 1 — consistent with round 1 — but is confirmed
  numerically too weak alone for Case 2, since after XY cuts the top piece the new
  `max(P)` can be much smaller than `2^n`, so `2·max(P) − Σ(P)` goes negative/useless).
  Do not resubmit this as a fix for Case 2 without a recursive strengthening.

- **Knowledge-base entries to use:** "Invariants & monovariants" (combinatorics section) —
  the natural home for framing (1)'s turn-by-turn dominance invariant. "Extreme value
  theorem" / minimax entries are not really present in `knowledge_base.md` for game values;
  the KB has no dedicated LP-duality-for-games entry, consistent with framing (4) being a
  weak match. "Constructive vs. existence" heuristic under General Proof Methods supports
  framing (2)'s need for both an upper *and* lower bound construction regardless of framing.

- **Analogous past problems (cruxes):**
  - **`aimo-0117`** (Jesse/Tjeerd stone-in-boxes game, Dutch olympiad) — genuinely
    analogous in spirit: two players alternately affect a growing multiset of real-valued
    "tokens" split across two collections, with one player (Jesse) choosing values and
    initial placement and the other (Tjeerd) allowed to move one token per round; Jesse's
    winning strategy is **exactly** the dyadic-domination construction: play
    `2^0, 2^1, 2^2, ...` (doubling every round) and maintain the invariant that the
    largest power-of-two played is in the favorable box, using a two-case argument
    (opponent displaced it → immediately promote the next larger power in; opponent did
    something else → play the next *smaller* power, doesn't matter where). The crux move
    (`technique` field): *"Assign the played values as a two-sided geometric (dyadic)
    sequence so that the single largest value strictly exceeds the sum of all the
    others."* This is the same core arithmetic fact (`2^j > Σ_{i<j} 2^i`) driving our
    dyadic marking `W_n = {2^0,...,2^n}`, but proved there via an explicit **turn-by-turn
    invariant maintained against an adaptive adversary**, not via a global measure
    computation — worth adapting the *proof technique* (not the result) to attack GAP-LB.
  - Searched `games-and-strategy` (combinatorics, 39 entries) broadly; other candidates
    (`aimo-0461` cycle-pairing placement game, `aimo-0663` pigeonhole-on-components game)
    are pairing/parity-invariant arguments for *discrete* combinatorial games (graphs,
    boards) and don't transfer structurally to a continuous stick-cutting payoff — noted
    but not recommended.
  - No corpus entry directly matches "cut a continuous stick, then alternately claim
    pieces" as a compound two-phase game; `aimo-0117` is the best available analog for the
    *dyadic-domination proof technique*, not for the problem's literal structure.

- **Prior progress:** (from `current.md`) Lemma 0 (endgame greedy, `Odd(P) = a_1+a_3+...`)
  and the layer-cake reduction `f(P)=M(P)` are both fully certified and — importantly for
  this report — **are forced facts about the game itself**, not artifacts of one framing;
  any alternative approach still needs `Odd(P)` as the payoff (that's the actual game
  rule). The real "shared wall" the orchestrator flagged is **downstream** of that: the two
  extremal inequalities GAP-LB (Case 2, XY cuts the top piece) and GAP-UB (dyadic is the
  unique maximizing LB marking). `n=1` fully solved by all three; dyadic marking pinned as
  the presumptive extremizer for `n=2..5` (numeric).

- **Dead ends (do not retry):** "XY duplicate-the-top recursion" (overspends, fails from
  `n=3`); "XY bisects a subset of LB pieces alone" (insufficient, `≈0.167 > 1/7` at `n=2`);
  "XY always top-matches alone" (fails on top-heavy configs); "blanket non-max-cut
  domination" (proven FALSE, 28k counterexamples per outline-reviewer). New from this
  report: **do not resubmit the bare inequality `f(P) ≥ 2·max(P) − Σ(P)` as a fix for
  Case 2/GAP-LB** — verified numerically true in general but provably too weak once the
  top piece itself is subdivided (the new max shrinks, the bound goes slack); it only
  closes Case 1 (already done). Also: a bare LP/minimax-duality argument on cut positions
  (framing 4) is unlikely to give a clean certificate without first re-encoding through a
  combinatorial linearization (the payoff `Odd(P)` is not concave/convex in the cut
  positions due to re-sorting kinks) — don't spend a round on "raw" LP duality without that
  translation step.

- **Small-case / intuition notes (conjecture unless noted "verified"):**
  - **Verified** (20000 random multisets, 0 violations): `f(P) ≥ 2·max(P) − Σ(P)` for any
    finite multiset `P` — a clean one-line consequence of `f(P)=a_1−f(P∖{a_1})` and
    `0≤f(Q)≤Σ(Q)`. Useful as a standalone lemma (already implicit in Case 1) but insufficient
    alone for Case 2.
  - **Conjecture** (structural, not yet checked computationally this round): the
    obstruction to a clean recursion `c(n) ↔ c(n-1)` is that XY's total cut-budget `n` is
    *fungible* across the "top dyadic piece" region and the "rest" region — an adaptive
    adversary can under-spend on one region having watched what LB's marking does in the
    other, which is exactly the self-similar/Case-2 difficulty already flagged by all three
    approaches. If true, closing GAP-LB/GAP-UB likely requires an explicit "adaptivity
    doesn't help XY beyond spending greedily on the current largest piece" lemma — a genuine
    piece of new content, not obtainable by re-deriving the reduction in a different
    language.
