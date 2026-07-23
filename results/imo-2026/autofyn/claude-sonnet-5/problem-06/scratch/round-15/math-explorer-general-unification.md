## imo-2026-06

### IMPORTANT cross-reference (found by a parallel explorer this round, not by me)
`/tmp/round-15/math-explorer-alternative-mechanism.md` and
`/tmp/round-15/math-explorer-structural-obstruction.md` both independently
surfaced crux `aimo-0030` (IMO-SL 2013 N5, "Ana and Banana"), whose own
recursive rule is a **verbatim, character-for-character match** to
imo-2026-06's rule, and whose official solution's similarity-dichotomy +
mod-`P` (`P=∏_{p≤a_1}p`) periodicity corollary, if re-derived from scratch
for this problem, would give an EXPLICIT `(T,L)` pair satisfying the
headline conclusion **for every `a_1`** — potentially resolving the whole
problem, bypassing the entire FCBC/(JW)/(WCE)/Corollary-MSF apparatus this
report and 14 rounds of work sit inside. This is flagged there as
numerically checked but NOT yet re-derived from scratch (not a proof yet).
**If the outliner pursues this, my report below (a numerical calibration
of the MSF/Chaining-Sufficiency-based sub-program) becomes secondary —
read the other two reports first.** I did not verify this finding myself
(different lens); treat their claim with the same "not proof until
re-derived and reviewed" caution CLAUDE.md always requires.

### Scope of this lens
Assigned to survey what's common across the 5 already-solved instances'
closures (15, 247, 4199, 2747, 4087) and look for a falsifiable general
pattern governing whether Corollary MSF / the Chaining Sufficiency Theorem
closes a disjoint core pair. Built independent tooling (fast antichain-based
generator + a Chaining-Sufficiency witness-collection search, both
validated against brute force) and ran it fresh against known instances,
the known-hard `a_1=21528751`, and several NOT-previously-tried `a_1`
values. All code in `/tmp/round-15/{gen.py,wce_search3.py}`.

### Distinct openings
1. **A reusable, validated "witness-search" tool** (not previously in the
   workspace as far as I found): a fast exact procedure that, given a
   dedup'd pool of low-comp-size witnesses per side, searches increasing
   witness-collection sizes `(r1,r2)` and checks the Chaining Sufficiency
   Theorem's success condition via minimal-hitting-set/choice-function
   enumeration (provably equivalent to, but far faster than, the naive
   `2^|W|` powerset check — verified the reduction is exact: a violating
   pair `(τ,τ')` exists among *all* subsets iff one exists among the
   choice-function-generated candidates, since `T_S(R)` is an up-set and
   minimal elements of an up-set are always realized by a choice function
   over the defining family). This reproduced, from scratch, the exact
   published witness structures for `247` (comps `{2,5},{3,7},{2,3}` vs
   `{2,7},{3,5},{2,3}`, matching Theorem FW2's "3 minimal patterns per
   side, 9-case table" description) and part of `4199` (the `(13,17)` pair
   exactly reproduces Theorem FW1's `W={2,3,83}` witness set). This is a
   concrete, checkable artifact any future builder can reuse directly to
   search for closing witness collections instead of hand-searching.
2. **Density/quality-hub framing**: in every 3-prime case tested, exactly
   one singleton core in `P_1` acts as a "hub" (order-of-magnitude higher
   density, achieving min companion size 1 quickly), while the other cores
   are systematically sparser with a higher minimum companion size — but
   (negative finding, see below) *which* prime becomes the hub is not
   predictable from prime rank (smallest/middle/largest all won in
   different tested instances) — so don't chase a rank-based formula.
3. **Depth-stability test as an invariant probe**: pushing search depth by
   3.3x-100x past the workspace's prior deepest check on `21528751` shows
   both density AND minimum-companion-size are essentially *frozen exactly*
   (not just "no better example found yet") — a sharper, more falsifiable
   form of round 14's finding, now with a specific frozen floor value per
   core, not just "zero occurrences of size ≤2."
4. **A methodological trap surfaced and worth flagging**: naively picking a
   "fresh, skewed" 3-prime `a_1` (small prime × two large, spread-out
   primes, mimicking `21528751`'s shape) can silently collapse to the
   *already-solved* Case I (one prime divides literally every term) rather
   than giving a fresh Case II stress test — this happened for my first
   fresh pick (`a_1=7*101*1009=713363`: literally 100% of the first 60,000
   terms divisible by 7, and the other two singleton/joint-without-7 cores
   had **zero** members in that entire range). Any future round choosing
   "fresh a_1" values for Case-II-style testing should explicitly check
   `min(fraction of terms divisible by p) over p in P_1 < 1` before trusting
   the instance as a genuine multi-core test case.

### Candidate technique(s)
The Chaining Sufficiency Theorem's witness-search (item 1 above) is the
most concrete lever: a bounded, mechanical, checkable search procedure
that already reproduces 100% of published closures I re-tested and closes
5/6 pairs automatically on a brand-new instance (`a_1=20677=23·29·31`, see
below) with a *modest* search bound (dedup pool ≤12, `|R|≤3`/side). This
argues the *existence* question (Conjecture WCE / Bounded Forced-Set
Existence) is very plausibly true and "just" needs either (a) a smarter/
deeper automated search per pair (my bounded search is a weak lower bound
on what's findable, not an upper bound on difficulty), or (b) a genuine
existence *proof* — my numerics can't supply that, only calibrate it.

### Cheap-kill candidates
- Before treating any "fresh" multi-prime `a_1` as a genuine Case-II test
  case, check no single prime of `P_1` divides 100% of a moderate prefix
  (cheap: one pass over the generated radicals) — a_1=713363 is a concrete
  cautionary example that silently degenerates to Case I.
- Do not pursue a "prime rank determines the hub" sub-conjecture (smallest,
  middle, or largest prime of `P_1` is always the density/quality hub) —
  refuted by direct counterexample across 3 tested instances in this
  session alone (`21528751`: smallest prime 103 is hub; `4199`,`2431`:
  middle prime is hub; `20677`: largest prime 31 is hub). Any future
  attempt to derive Bounded Forced-Set Existence from an explicit
  "which prime wins" formula should be abandoned before it starts.

### Knowledge-base entries to use
No new KB entries identified this round beyond what's already cited in
`current.md` (Lemma P′, Lemma XC/NIDF, Theorem CD, Lemma WF, Chaining
Sufficiency Theorem, Corollary MSF) — this lens was purely computational/
pattern-search, not a new-technique search; per standing workspace rules
(round 6/9/11), no analytic-number-theory tool applies to this
deterministic recursive structure, and nothing found here changes that.

### Analogous past problems (cruxes)
Not queried this round (out of scope for this lens — a prior round's
math-explorer already did a thorough crux-corpus sweep per the round-11/12
history in `current.md`, finding no genuinely analogous problem beyond
what's cited there). Deferred to the outliner/other explorers.

### Prior progress
5 solved concrete instances (`15,247,4199,2747,4087`), Corollary MSF (a
general, certified, zero-case-split sufficient mechanism), plus 1 extra
closed channel of `21528751` (`{197}` vs `{103}`). The GENERAL problem
remains open; the sharpest open target per round 14 is the "Bounded
Forced-Set Existence Conjecture" (does every `a_1`/disjoint-core-pair admit
*some* finite closing witness collection, via MSF or the more general
Chaining Sufficiency Theorem — not necessarily MSF's exact singleton-heavy
shape).

### Dead ends (do not retry)
- Do not re-attempt "prime rank predicts the hub core" (see Cheap-kill
  candidates) — refuted by 3 independent counterexamples this session.
- Do not treat a naive "smallest-companion-size pool of ≤12-15 witnesses,
  |R|≤3/side" automated search as a completeness check when it *fails* to
  find a closing `R` (as it did for 3/6 of `4199`'s pairs and 1/6 of
  `20677`'s pairs even though `4199`'s full 6-channel closure is already
  proven in `current.md` via a smarter/deeper choice of witnesses) — a
  search-failure at this bound is evidence of nothing beyond "this specific
  bounded search didn't find it," not evidence the pair is hard or unclosable.

### Small-case / intuition notes (all labeled conjecture/observation, not proof)
- **New fresh instance, never before in this workspace**:
  `a_1=20677=23·29·31` (3 close primes, deliberately chosen after the
  713363 collapse to confirm a genuine Case-II instance). All 3 singleton
  cores nonempty with substantial counts (`{23}`: 7999/40000, `{29}`:
  6286/40000, `{31}`: 23468/40000 — `31`, the *largest* of the three, is
  the density/quality hub here, min companion size 1). My bounded search
  closed 5/6 disjoint pairs automatically (only `{23}` vs `{29}` unresolved
  at this search bound) — consistent with (not proof of) WCE holding here
  too, and gives the outliner/builder a fresh, easy-looking candidate 6th
  instance if a 6th solved concrete example is wanted (would need the
  remaining pair `{23}`/`{29}` closed, plus checking `Lemma SW1`-style
  intersecting-core coverage, before claiming a full instance solve).
- **`a_1=21528751` depth-pushed to N=500,000 (100x the round-14 check for
  `{197}`, previously only to n≈27,832/30,000)**: densities of all 6 proper
  cores are stable to 4+ significant figures between `N=150,000` and
  `N=500,000` (`{103}`: 0.97680 both; `{103,197}`: 0.005027/0.005018;
  `{103,1061}`: 0.000927/0.00092; `{197}`: 0.016947/0.016946; `{1061}`:
  0.0003/0.000296; `{197,1061}`: only 2 members at 150k, 8 at 500k —
  genuinely sparse but not shown finite). The minimum realized companion
  size for the non-hub cores is **exactly frozen** across this 3.3x depth
  increase: `{197}` stays at 3, `{1061}` stays at 4, `{197,1061}` stays at
  3 — zero improvement despite far deeper search than round 14's negative
  finding. This is a materially stronger (though still only numerical,
  not a proof) version of round 14's "no downward trend" result: it is now
  a frozen *exact floor value*, not just an absence of small examples,
  across an order-of-magnitude-deeper, independently-reproduced search.
  This is genuine evidence (not proof) that the Bounded Forced-Set
  Existence Conjecture may be **false in its MSF-singleton-shaped form**
  for these specific classes, exactly as round 14 flagged — but does NOT
  bear on whether the more general Chaining-Sufficiency mechanism (larger,
  non-singleton witness collections, as used for `4199`/`247`) can still
  close these pairs; that remains a live, untested-by-me-at-scale question
  for `21528751`'s 5 still-open channels (all of which touch `{197}` or
  `{1061}`), and is the most concrete next numerical target I'd hand to the
  outliner.
- **`a_1=713363=7·101·1009`**: methodological finding only (see Distinct
  openings #4 and Cheap-kill candidates) — this instance is (at least to
  N=60,000) a Case I instance in disguise, not usable as fresh Case-II
  test data.
