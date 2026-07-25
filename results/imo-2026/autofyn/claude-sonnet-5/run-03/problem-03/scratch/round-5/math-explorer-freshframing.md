## imo-2026-03

- Distinct openings (routes distinct from the 5 current framings):
  1. **LP/convex-duality on the finite-support relaxation.** The certified
     reduction (`lemmas/reduction-to-multiset-minimax.md`) is a max-min of
     `OddSum` over LB's simplex choice and XY's refinement choice. For a
     *fixed* combinatorial split-pattern `(m_1,...,m_k)` (which piece gets
     how many of XY's cuts), `OddSum` of the resulting sorted multiset is a
     piecewise-linear (not smooth, due to sorting) function of the
     continuous split variables; the inner minimization over split lengths
     for fixed pattern is a linear program over a polytope (the simplex of
     each piece's fragments) intersected with the region defining a fixed
     sort order — i.e. XY's problem decomposes into finitely many small LPs
     (one per combinatorial sort-order region), and the true inner min is
     the min over that finite union of LP optima. This gives an opening
     genuinely different from peeling or layer-cake: treat XY's move as
     "choose an order-type, then solve the LP for that order-type," and use
     LP duality/complementary slackness on each piece to characterize the
     optimal fragment lengths (the KKT/duality conditions on a
     piecewise-linear order-statistics objective are exactly the kind of
     structure that gives clean closed-form multipliers). This has NOT been
     tried by any of the 5 approaches — all five reason case-by-case or via
     potential functions, none invoke LP duality on the split-polytope
     directly.
  2. **Symmetric/exchangeability argument via a majorization / Schur-convexity
     lens.** `OddSum` restricted to a fixed cardinality multiset is a
     Schur-concave-ish functional of the sorted vector (taking odd-ranked
     entries) — actually neither convex nor concave globally because rank
     order changes with the vector, but on a fixed sort-order region it is
     linear. A majorization argument ("does XY's optimal fragment vector
     majorize/get majorized by some canonical vector") could characterize
     the optimal split without going through explicit case enumeration.
     This is adjacent to opening 1 but pursued via rearrangement-type
     inequalities instead of raw LP variables — worth flagging as a second,
     related but not identical, opening if the outliner wants a softer
     version of LP-duality without full KKT machinery.
  3. **A genuinely different top-level target: characterize XY's globally
     optimal strategy as a fixed point of a "greedy bisect the current
     max, recompute, repeat" process** (a discrete dynamical system on
     multisets) and prove a monotonicity/exchange argument about *when*
     this greedy process needs to "reset" to a non-max piece — since the
     numerics below show the true optimum sometimes splits a *non-maximal*
     piece (see intuition notes), a fixed-point/dynamical characterization
     might explain exactly which piece gets split without needing an
     exhaustive multi-piece argument.

- **Answer to Task 1 (is top-only/single-piece insufficiency now
  structural?).** My numerics (see below) show it is **at least a broader
  phenomenon than the one hand-found `n=2` counterexample**: at `n=3`,
  several distinct balanced partitions have their TRUE numerically-optimal
  XY response (found by combinatorial-search-over-split-patterns +
  continuous optimization within each pattern) split **two different
  original pieces**, using genuine (non-degenerate) fractions of the
  budget on each — not confined to `p_1`. This is a second, independent,
  broader body of evidence (beyond the two approaches' single worked
  examples) for "multi-piece needed," but it is still **numerical/
  conjectural**, not a proof that EVERY optimal XY response in the balanced
  region must be multi-piece — I did not find or attempt a general proof
  of that positive characterization in the time available (it would need a
  genuine structural argument, e.g. via opening 1's LP-duality
  complementary-slackness conditions, showing the KKT multiplier structure
  forces >1 piece to be active whenever `p_1<1/2`). This would indeed be
  valuable content if provable (a clean "why" for the plateau), but I flag
  it as **open, not closed** — the outliner should treat "prove multi-piece
  necessity via LP duality" as a candidate lemma to attempt, not an
  established fact.

- **Candidate technique(s):** LP duality / KKT on a piecewise-linear
  order-statistics objective (opening 1); majorization/Schur-type argument
  (opening 2, softer version of 1); discrete dynamical-system / greedy
  fixed-point characterization (opening 3).

- **Cheap-kill candidates:** None found that immediately close the gap.
  One useful cheap structural check that *did* pay off: enumerating XY's
  combinatorial split-patterns is a finite search (partitions of the
  cut-budget among the `k` pieces), so for small `n` the *entire* inner
  minimization is a finite union of small LPs — this is cheap to brute
  force exactly for `n≤3` (used below) and should be exploited by the
  outliner as a verification tool for any proposed multi-piece
  construction, not just a discovery tool.

- **Knowledge-base entries to use:** `knowledge_base.md` does not contain
  any entry with "duality," "minimax," "linear program," or
  "rearrangement" in its text (checked by direct grep) — there is no
  directly-named LP-duality or rearrangement-inequality entry to cite.
  This means opening 1/2, if pursued, must be developed from scratch
  (standard LP duality is citable as a generic mathematical fact, but
  isn't a named KB entry here) — flag this to the outliner so it doesn't
  waste time searching for a KB shortcut that doesn't exist.

- **Analogous past problems (cruxes):** Searched the crux corpus
  (`crux_moves_documentation.md` schema followed: `domain`, `subtopic`
  fields) under `combinatorics` / `games-and-strategy` (39 entries) and
  by keyword (`stick`, `claim`, `alternately`, `take turns`, `pieces of
  length`, `cut the`) across `past_problems_database.json`. **None are
  genuinely analogous.** The closest keyword hits (`aimo-0074`,
  `aimo-0596`, `aimo-0663`, `aimo-0779`) are alternating-turn games but
  over discrete combinatorial objects (coins, cards, integers), not a
  continuous stick-cutting-then-claiming game with a two-phase
  adversarial marking structure; none involve a max-min over a continuous
  simplex with combinatorial refinement, and none use LP-duality or
  rearrangement as their crux move. I recommend **not forcing a match**
  here — report "none" to the outliner rather than a weak analogy.

- **Prior progress:** See `results/imo-2026-03/current.md` for the full
  state (reduction lemma, greedy-optimality lemma, closed-form conjecture
  `c(n)=2^n/(2^{n+1}-1)`, both gaps as of round 4). Not re-summarized here
  in full; my contribution is the fresh framing + new numerics below.

- **Dead ends (do not retry):** (from current population, verified
  consistent with my own numerics, not just copied) static Q-priority /
  tail-priority strategies; literal and balanced-region-restricted
  Cut-Reallocation Exchange Lemma (both disproved by exact counterexample);
  "peel technique at violation depth 1 or even depth" (proved to fail);
  "Suffix-Match construction optimized over `t` alone" (proved
  numerically insufficient); "independent per-cut marginal bound" for the
  layer-cake framing (proved impossible by the Coupling Obstruction, and
  my own optimization runs are consistent with this — the optimal
  split-pattern is never simply "the biggest single cut applied
  independently").

- **Small-case / intuition notes (labeled conjecture — from a Python
  brute-force-over-split-patterns + Nelder-Mead-within-pattern numerical
  optimizer; code and full output kept in this session, not committed to
  the repo):**
  - For `n=2` (`k=3` pieces, budget 2), across 8 balanced test partitions
    (e.g. `(0.35,0.34,0.31)`, `(0.4,0.4,0.2)`, `(0.48,0.45,0.07)`), the
    **true numerically-optimal** XY response never needs both cuts — one
    cut suffices, and it is **not always on `p_1`**: e.g. for
    `(0.35,0.34,0.31)` and `(0.4,0.4,0.2)`, the optimal single cut splits
    `p_3` (the smallest piece), not `p_1`. Values found were consistently
    well below `c(2)=4/7≈0.571` (margins `0.05`–`0.07`), consistent with
    `T(2)` already being closed with real slack in the balanced region —
    this matches the certified status (`T(2)` fully closed) and gives no
    new obstruction there, but is a clean illustration that "split the
    largest piece" is not even the right heuristic in general, let alone
    "split only the largest piece."
  - For `n=3` (`k=4` pieces, budget 3), across balanced partitions (e.g.
    `(0.3,0.3,0.25,0.15)`, `(0.4,0.3,0.2,0.1)`, `(0.45,0.25,0.2,0.1)`),
    the numerically-optimal XY response **genuinely splits two different
    original pieces** in several cases (e.g. `(0.4,0.3,0.2,0.1)`: split
    `p_1` into `(0.2,0.2)` AND split `p_2` into `(0.2,0.1)`, using 2 of the
    3 available cuts on two different pieces; `(0.45,0.25,0.2,0.1)`: split
    `p_1` into `(0.25,0.2)` AND split `p_4` into `(0.05,0.05)`) — this is
    independent numerical confirmation, at `n=3` and via a different
    (brute-force/optimization) method than either
    `dyadic-potential-invariant`'s or `layer-cake-parity-reframing`'s
    hand-built examples, that **multi-piece coordination is a broad
    phenomenon in the balanced region, not an isolated worked example**.
    All values found (`~0.50`–`0.52`) stayed comfortably below
    `c(3)=8/15≈0.533`, again suggesting real slack rather than
    razor-thin tightness.
  - A 25-trial random search over balanced partitions (`p_1<0.5`) at `n=3`
    found no partition whose optimal-XY-response value exceeded
    `~0.518 < 8/15`, i.e. **no counterexample to the upper-bound
    conjecture was found** — this is weak positive evidence (not proof)
    that the closed form and the balanced-region upper bound both hold,
    and that the difficulty is a missing *proof technique* (a uniform
    argument covering the whole simplex) rather than the statement being
    close to false or numerically fragile.
  - Near the boundary `p_1→1/2⁻` (e.g. `(0.499,0.3,0.15,0.051)`), the
    optimal response reverts to a genuine top-only single-piece split
    (`p_1` alone, using both remaining cuts on it) with margin
    `~0.023`–`0.032` below `c(3)` — not vanishing — suggesting the
    boundary `p_1=1/2` is a regime-change point for *which mechanism* XY
    uses, not a point of vanishing slack; the truly delicate case is more
    likely near LB's actual optimum (the geometric partition itself, where
    margin is exactly 0), not at the region's edge.
