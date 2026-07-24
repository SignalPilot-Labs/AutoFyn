## imo-2026-03 (lens: Xiang Yu's counter / upper bound c(n))

### Setup recap
Liu Bang (LB) marks ≤n points, Xiang Yu (XY) sees them and marks ≤n more distinct
points, stick is cut, then they alternately claim pieces (LB first). Since pieces
are just numbers with no positional constraint, optimal alternating claiming is
provably greedy: sort all final pieces descending, LB gets ranks 1,3,5,…, XY gets
ranks 2,4,6,…. (This "greedy = optimal for alternating pick from a fixed multiset"
fact should be stated as a short lemma in the proof — it needs a one-line
exchange-argument justification, not asserted, but it is standard and not hard.)
c(n) = max over LB's ≤n-point markings of [ min over XY's ≤n-point responses of
LB's greedy-descending-odd-rank sum ].

### Distinct openings (for the upper-bound / Xiang-Yu side)
1. **"Clone the leader" response rule.** XY's tool: whenever one piece p is
   strictly the largest, split it into two equal halves p/2, p/2 using ONE point.
   This can convert a "LB monopolizes the top piece" situation into a tie the
   moment the two new p/2's are compared against the next-largest existing piece.
   Verified exactly for n=1 (turns {1/3,2/3} into {1/3,1/3,1/3}) and for n=2
   (turns {2/7,4/7,1/7} into {2/7,2/7,2/7,1/7}), in both cases achieving XY's
   optimum with *fewer than the full n points* — XY does not need to use all of
   his budget.
2. **Parity control as a hidden lever.** XY can choose how many of his ≤n points
   to actually use (0 up to n). This changes the total piece count's parity,
   which changes how many pieces LB gets to keep (⌈m/2⌉ out of m). A naive
   "always use all n points, split into 2n+1 equal pieces" strategy (which would
   suggest c(n) = (n+1)/(2n+1)) is demonstrably NOT optimal for XY: numerically,
   using only 1 of 2 available points to bisect LB's biggest piece can beat the
   "split into 2n+1 equal pieces" response by a wide margin (see below). This is
   the single most important correction this lens surfaced — the "equalize to
   2n+1 equal pieces" idea (a natural first guess) is a **dead end** for the
   upper bound; XY does strictly better with a more surgical response.
3. **Splitting the smallest piece is provably bad for XY.** Whenever XY splits a
   piece that is NOT currently the largest (or not tied for largest), LB's total
   only goes up (proved exactly in the n=1 case: splitting the untouched small
   piece 1/3 into s,1/3−s gives LB total 2/3+min(s,1/3−s) > 2/3 for any s in
   (0,1/3)). This gives a monotonicity/exchange principle: **XY should only ever
   split (one of) the currently-largest piece(s)**. This is a strong structural
   constraint that should sharply cut down the search space for the real proof —
   candidate for a clean lemma ("splitting a non-maximal piece never helps XY").
4. **Self-similar / recursive structure of LB's extremal marking.** For n=1 the
   extremal LB split is (1/3, 2/3) — i.e. proportional to (1,2). For n=2 the
   numerically-located extremal LB split is proportional to (1,2,4) (in some
   order, i.e. pieces of relative size 4:2:1, total denominator 7 = 2^3−1). This
   suggests LB's optimal marking is a **geometric/binary progression** of piece
   sizes 2^0, 2^1, …, 2^n (as fractions of 2^{n+1}−1), i.e. LB repeatedly bisects
   the "remaining" mass. This is only a conjecture from n≤2 data (see below) but
   is a clean enough shape to be worth trying to prove is extremal by an exchange
   argument (any non-geometric LB split can be improved by XY more cheaply).

### Candidate technique(s)
- Rearrangement / exchange argument bounding a greedy-alternating-pick sum given
  structural constraints on the multiset (majorization-flavored).
- Extremal/monovariant argument: track the multiset of pieces, show a single
  well-chosen split move by XY can only decrease (never increase) LB's
  guaranteed total, then argue by induction on the number of "levels" in LB's
  marking.
- Knowledge base: **Invariants & monovariants**, **Pigeonhole/extremal
  principle** (KB "Combinatorics" section), **Piecewise-concavity smoothing**
  style argument (KB "Algebra") is a structurally similar flavor (min/max of a
  sum of simple pieces via a breakpoint argument) — worth adapting even though
  it was written for a trig-sum problem, the "concave sum ⇒ extremum at
  breakpoint" idea maps onto "each additional cut is a `move a boundary` type
  operation."

### Cheap-kill candidates
- The "split into 2n+1 equal pieces gives XY's best response" idea is falsified
  by direct computation (see numerics) — flag this explicitly so the outliner
  does not waste a round re-deriving it.
- "XY should always use all n of his points" is also false (n=2 case: using 1
  of 2 points beats using both in the naive equal-split scheme) — budget is not
  monotonically helpful without care about *how* it's spent; do not assume more
  cuts always help XY.
- Splitting a non-maximal piece is dominated (see opening 3) — restricts the
  XY strategy space to "only touch current maxima," a real pruning tool.

### Knowledge-base entries to use
- Invariants & monovariants (Combinatorics section).
- Pigeonhole / extremal principle.
- Constructive vs. existence: "find all / largest n" needs upper bound AND
  matching construction — both sides (LB lower-bound construction, XY
  upper-bound response) are required; this lens only covers the upper-bound
  half.
- Piecewise-concavity smoothing (Algebra section) — analogous "breakpoint /
  extremal at boundary" flavor, worth trying to adapt to the cut-point movement
  argument.

### Analogous past problems (cruxes)
Checked `combinatorics` subtopic `games-and-strategy` (and also
`extremal-principle`, `invariants-and-monovariants`) in the crux corpus per
`crux_moves_documentation.md`'s field names (`technique`, `how_used`, `domain`,
`subtopic`, joined via `problem_id` to `past_problems_database.json`'s
`problem`/`solutions`). I did not find an entry that matches this problem's
exact structure (adversarial two-phase marking + alternating greedy claim of a
continuum stick) — most `games-and-strategy` cruxes in the corpus are discrete
combinatorial games (token/graph games) rather than continuous-interval
division games. **None found that are genuinely analogous** — the "split the
stick, alternately claim pieces" structure appears to be sui generis in this
corpus; do not force-fit a discrete-game crux onto it. (If the outliner wants,
a second explorer pass specifically querying `subtopic=processes-and-algorithms`
or `extremal-principle` in `combinatorics` might turn up a fair-division /
cake-cutting analogue, but I did not locate one that matches on the actual
mechanic of "sort descending, alternate picks" — that particular fact ["greedy
= optimal for alternating claim of numbers"] is elementary enough it likely
doesn't need a named crux, just a one-paragraph exchange-argument lemma.)

### Prior progress
None — no existing workspace/approaches for imo-2026-03 before this round.

### Dead ends (do not retry)
- **"XY equalizes all pieces to 1/(2n+1) using all n points" ⇒ c(n) =
  (n+1)/(2n+1).** Falsified numerically for n=2: with LB pieces (1/5,1/5,3/5),
  this scheme gives LB = 3/5, but XY can instead spend only 1 of his 2 points to
  bisect the big piece (0.6 → 0.3,0.3), giving pieces {0.3,0.3,0.2,0.2} and LB
  total = 0.3+0.2 = **0.5**, strictly better for XY. So this "natural first
  guess" formula is wrong and should not be re-derived.
- Do not assume XY benefits from splitting the currently-smallest piece — every
  test case makes LB's total strictly worse (larger) when XY does this.

### Small-case / intuition notes (all labeled conjecture unless stated as hand-verified)
- **n=1: c(1) = 2/3 — hand-verified rigorously (not just numeric).** LB marks
  a single point at x=1/3 (WLOG x ≤ 1/2, by symmetry). Full case analysis over
  all of XY's single-point responses (splitting either the 1/3-piece or the
  2/3-piece, at any ratio) shows LB's total is always ≥ 2/3, with equality
  achieved by XY splitting the 2/3-piece (any way at all — the result is
  invariant to how it's split!) or by XY not moving at all. For any x ≠ 1/3,
  LB's guaranteed total is strictly below 2/3 (worked out closed forms:
  (1+x)/2 for x<1/3, 1−x for x>1/3, both maximized at x=1/3 giving 2/3). This
  is a complete result for n=1, both directions established by hand.
- **n=2: c(2) ≈ 4/7 (numeric/conjectural, not proven).** Extensive random +
  local-refinement search over LB's 2-point markings (parametrized as 3 pieces
  p1,p2,p3) and XY's full response space (all ways to distribute ≤2 further
  cuts among the pieces, sampled) converges to LB pieces proportional to
  (2,4,1)/7 [i.e. (2/7, 4/7, 1/7)] with resulting value ≈ 0.5714 = 4/7 exactly.
  Manually checked that XY's near-optimal response is exactly "bisect the
  largest piece (4/7 → 2/7,2/7)," giving pieces {2/7,2/7,2/7,1/7} and LB total
  = 2/7+2/7 = 4/7 — matching. XY's second available point does not seem to
  improve on this (tested several ways to spend it: splitting a 2/7 further,
  or the 1/7 further — both leave the total at 4/7 or make it worse for XY).
  Numeric outer-search over LB configs shows (2/7,4/7,1/7) is a local (and
  likely global, within the class of 3-piece configs) maximizer.
- **Conjectured closed form: c(n) = 2n / (2^{n+1} − 1).** Matches n=1 (2/3) and
  n=2 (4/7) exactly. Consistent with the "geometric/binary" extremal LB
  marking: pieces proportional to 2^n, 2^{n-1}, …, 2^1, 2^0 (sum = 2^{n+1}−1).
  **This is only weakly supported past n=2** — I attempted n=3 with the
  natural binary marking (8,4,2,1)/15 and a hand-constructed cascading XY
  response (repeatedly bisecting the current max: 8→4,4 then 4→2,2 then
  4→2,2, ending at {2,2,2,2,2,2,1}/15), which gives LB total 7/15 ≈ 0.467, NOT
  6/15 = 0.4 as the conjectured formula would predict. Random search on the
  same LB config found an even weaker XY response (only 8/15 ≈ 0.533,
  presumably because random sampling in higher dimensions is unreliable, not
  because 8/15 is actually optimal for XY). **So for n=3 the numeric evidence
  is inconclusive**: I have upper-bound-on-c(3) evidence in the range
  [0.467, 0.533] from my two attempts (neither is a proof of optimality for
  either side), well above the conjectured 0.4. Either (a) the conjectured
  formula 2n/(2^{n+1}−1) is wrong beyond n=2, or (b) neither of my n=3 XY
  strategies is optimal and a smarter response gets down to 0.4, or (c) the
  binary marking itself is not LB's true optimum for n=3 and the real
  extremal marking differs. **Flag this explicitly as unresolved** — the
  outliner should not commit to 2n/(2^{n+1}−1) as the final answer without
  either (i) a real proof of the n=3 case or (ii) reproducing/improving the
  n=3 numerics with a non-random (structured/analytic) search.
- Main obstacle for a full proof: (1) pin down the true extremal LB marking
  for general n (binary/geometric is only weakly evidenced), and (2) prove a
  *universal* XY response rule (working for every possible LB marking, not
  just the conjectured extremal one) that provably caps LB's total at the
  claimed c(n) — the "clone the leader" rule looks promising and provably
  correct in the cases hand-checked, but turning it into a general induction
  (on number of distinct "tiers" of piece sizes, or on n) with a clean
  closed-form bound is unfinished. The high-dimensional numeric search used
  here (random sampling of split ratios) is not reliable evidence beyond
  n=2 — a genuine combinatorial argument (not simulation) is needed for
  general n.
