## imo-2026-06 (lens: H2 termination — absence-of-outside-primes mechanism)

- Distinct openings:
  1. **Absence-mechanism gap is real and unaddressed by any certified tool.** The certified
     `bounded-witness-insufficiency-for-containment.md` (round 23) proves precisely that the
     only mechanism in the stack (Bounded Witness Lemma) gives *presence* of a shared prime with
     the core, never *absence* of extra primes outside it. No lemma anywhere in `lemmas/` currently
     bounds `P(a_j)\setminus S` from above for any finite core `S`. An absence mechanism would need
     to show, for `j` past some threshold, that `a_j`'s factorization is *confined* to a fixed finite
     set — structurally the opposite direction from every certified divisibility fact in this
     workspace (all of which are lower bounds: "some prime divides," never upper bounds on the
     support).
  2. **A genuinely different top-level target: attack boundedness of `|P(a_j)|` itself, or of
     `P(a_j)\setminus S_0`'s cardinality, via the problem's own minimality rule** (not via
     FAH/persistent-type machinery at all). Untried in the workspace as its own approach: since
     `a_j` is the *least* integer `>a_{j-1}` legal against the whole history, and legal candidates
     get sparser as more primes must divide them, there may be a size/counting argument bounding
     `ω(a_j)` in terms of `j` and the gap `a_j - a_{j-1}` (already have the certified elementary
     `ω(a_n) ≤ log_2 a_n` bound, `lemmas/elementary-omega-bound.md`, plus the Generalized Bounded
     Gap Lemma) that, combined with a counting/pigeonhole argument on how many *new* primes (never
     seen in `a_1,...,a_{j-1}`) can appear per unit growth of `a_j`, might directly bound the total
     number of "new-type recruitment events" — this is a top-level reduction candidate distinct
     from the S_0-containment framing, worth flagging to the outliner as a genuinely different
     route (a growth/counting argument on the sequence's own magnitude, not on persistent types).
  3. **Treat the two hard seeds as NOT interchangeable** (new finding this round, see below):
     `a_1=4807`'s new-extended-type arrival count looks like it is decelerating toward a finite
     limit, while `a_1=11305`'s looks like genuine unbounded (`~√N`) growth. If this asymmetry is
     real (not a window artifact), it argues H2 may hold for some seeds and be *harder or false*
     for others — a top-level framing shift: maybe H2 should not be attacked as one uniform claim
     but the outliner should consider whether the problem's proof structure needs seed-dependent
     casework (matching the workspace's existing subfamily-by-subfamily strategy for H1's easy
     cases) rather than a single universal absence mechanism.

- Candidate technique(s): No off-the-shelf "eventually no new element of a type appears" tool
  found in `knowledge_base.md` or the crux corpus that fits this greedy/recursive setting. The
  closest analogues (potential/monovariant arguments, closure-process saturation arguments) all
  require either (a) a finite ambient state space a priori (not available here — the "outside
  S_0" prime pool is the very object whose finiteness is in question, `NEVER` rule in memory:
  round 2/17 already ruled out "total prime support stays in a fixed finite set" as circular), or
  (b) a monotone/never-increasing quantity, which nothing in the certified stack currently supplies
  for `P(a_j)\setminus S_0`.

- Cheap-kill candidates: none obvious for constructing the absence mechanism itself. One cheap
  sanity check worth running before investing in machinery: check whether `ω(a_j)` (total number
  of distinct prime factors, not just those outside `S_0`) is itself bounded or slowly growing on
  these seeds — if `ω(a_j)→∞`, then `P(a_j)` cannot ever be confined to a fixed finite core `S_0`
  regardless of any absence mechanism, which would make the literal "S_0 (or any FIXED finite
  core) is eventually fully containing" framing hopeless and force the Monotone Chain family's
  cores `S_M` to grow without bound too — a structural reason H2 (if true) may need indefinitely
  growing cores, not a single fixed one. (Not run this round due to time; flagged as the single
  highest-value next numeric check.)

- Knowledge-base entries to use: none beyond what's already cited in the certified lemma stack
  (`bounded-witness-lemma.md`, `finite-core-theorem.md`, `extended-persistent-type-pigeonhole.md`,
  `monotone-chain-reformulation-lemma.md`, `elementary-omega-bound.md`, `bounded-gap-lemma`/
  "Generalized Bounded Gap Lemma"). `knowledge_base.md`'s general proof-methods section (pigeonhole,
  monovariants) offers no new technique not already tried per the memory rules.

- Analogous past problems (cruxes): Searched `number_theory` subtopics `size-bounding-and-descent`,
  `divisibility-and-gcd`, `pigeonhole`, and `combinatorics` subtopic `processes-and-algorithms` for
  "eventually no new X" / "closure process stabilizes" / "saturates" language (248+102 hits
  scanned). The two closest-sounding hits, `aimo-0421` (gcd-against-fixed-element finite-value
  pigeonhole) and `aimo-0477` (divisor-chain bounded by a fixed integer must stabilize), are BOTH
  already transplanted into this workspace (round 7/9/14, `successor-transport-reduction-lemma.md`,
  `confined-gcd-lemma.md`) and independently confirmed dead at the same wall (Lemma I,
  Non-Exclusivity of Witness Recruitment) — do not re-propose either. `aimo-0916`
  ("stabilize a descending chain of images of a self-map on a FINITE set") and `aimo-1025`
  ("greedy closure-process run gets stuck") both presuppose a finite ambient state space or a
  bounded-branching structure not available here (the prime pool outside any fixed core is exactly
  the unbounded object in question — same obstruction as the `NEVER` rule on "total prime support
  stays in a fixed finite set", round 2/17). **No genuinely analogous crux found** for an absence-
  of-new-elements argument in an unboundedly-branching greedy process; report this as a genuine
  gap in the corpus for this specific need, not a missed citation.

- Prior progress: `direct-s0-self-absorption` (round 23, `partial`) is the most advanced H2 work:
  proved the "direct S_0" framing is exactly the `M=N_0` instance of the certified Monotone Chain
  Reformulation Lemma (no new leverage), proved the Bounded Witness Lemma is provably insufficient
  for the containment target (certified as `lemmas/bounded-witness-insufficiency-for-containment.md`),
  and corrected the round-17 "N(S_0)=0 on 9/9 seeds" citation (that finding was about `S_0=Q`, not
  the enlarged Finite Core Theorem core).

- Dead ends (do not retry): the one-prime-at-a-time chain induction (`core-growth-monotonicity`,
  Prop 3, proved non-constructive); the Bounded Witness Lemma route to full containment (now
  certified-dead, Proposition 3 of `direct-s0-self-absorption`); "total prime support stays
  bounded" as an H2 trivializer (circular, round 2/17); `aimo-0421`/`aimo-0477`-style divisor-chain
  mechanisms (dead at Lemma I).

- Small-case / intuition notes (own fresh simulation, distinct script from all prior rounds'
  — `/tmp/h2explore/mysim.py`, per-prime bitmask legality check, sanity-checked against the known
  `a_1=15` sequence before trusting output): extended the tracked window well past the certified
  20,500-term check.
  - **`a_1=4807`, `S_0={2,3,5,7,11,19,23,73,127}`**: cumulative distinct extended-`S_0`-type count
    at `n=20500,100000,200000,300000,400000` is `129,165,181,192,200`. Increments over successive
    ~100k windows are `36,16,11,8` — a *decreasing*, roughly-geometric-looking sequence (ratio
    ≈0.7 each doubling), and the fitted power-law exponent of `T(N)` vs `N` drifts down from `0.49`
    to `0.41` — **conjecture: consistent with eventual convergence to a finite total type count**
    (i.e. plausibly supportive of H2 at this seed), though only a conjecture from four data points,
    not a proof, and slow decay could still mask a genuinely unbounded but very-slowly-growing tail.
  - **`a_1=11305`, `S_0={2,3,5,7,13,17,19,23,29,37,43,101}`**: cumulative count at
    `n=25000,50000,100000,200000,300000,400000` is `335,402,481,584,651,702`. The fitted exponent
    stays essentially flat near `0.51–0.57` across the whole range (no downward drift) — **conjecture:
    genuinely consistent with `T(N) ~ C√N`, i.e. new never-before-seen extended types keep arriving
    at a rate that does NOT show any sign of tapering to zero out to 400,000 terms** — this is the
    same qualitative "still arriving" finding as round 23's 20,500-term check, now confirmed to
    persist 20x further out, and quantitatively sharper: the growth looks like a genuine (slow)
    power law, not a finite-window artifact. New types keep appearing at the 98th+ percentile of
    the 400,000-term window (5 new singleton types after `n=392,000`).
  - **Novel finding this round**: the two mandated hard seeds behave *qualitatively differently* —
    `4807` looks like it may be converging (H2-supportive), `11305` looks like it may genuinely
    diverge (H2-threatening), at least within the tested range. This asymmetry was not previously
    reported (prior rounds treated the two seeds as giving a uniform verdict) and should be
    flagged to the outliner: a single universal absence mechanism assumed to work identically on
    both seeds may be the wrong target; either the `11305` reading is itself a finite-window
    artifact that a much larger simulation (millions of terms — infeasible in this round's time
    budget with trial-division factorization) would resolve, or the seeds genuinely differ and H2
    (in the "N(S_0) small" sense) needs seed-dependent, not universal, handling.
  - Recommendation on the dispatch's numeric-study question: **a moderate-scale (100k–400k term)
    study was run this round and gives real, if inconclusive, signal — extending to 200k+ was not
    the bottleneck; going to millions of terms would need a faster factorization method (current
    trial-division bitmask approach took 88s for 400k terms on `4807`, ~37s on `11305`; would take
    tens of minutes to reach 2–4 million terms, feasible but not attempted this round) before the
    `11305` divergence-vs-artifact question can be settled with confidence.** This is the single
    highest-value next computational step for H2, more informative than re-deriving structural
    lemmas until this asymmetry is understood.
