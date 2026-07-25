## imo-2026-03 — lens: the general upper-bound gap (arbitrary LB partition)

### Setup recap (verified against current.md / lemmas, not re-derived)
Reduced problem: LB picks a multiset of k<=n+1 positive reals summing to 1; XY
then performs <=n further splits; payoff to LB = OddSum of final multiset
(sum of odd-ranked pieces, descending sort). Need: for every LB partition, XY
has a response forcing OddSum<=c(n)=2^n/(2^{n+1}-1). Only the geometric LB
partition (2^n,...,2,1)/(2^{n+1}-1) is proved to have an exact-equality XY
response ("duplicate-the-rest", `lemmas/duplicate-the-rest-exact-response.md`).

### What I did
Wrote an exact numeric minimax solver (`/tmp/round-2/probe*.py`, not part of
repo): for a given LB piece list and cut-budget n, it enumerates every way to
distribute the n cuts among the k pieces (as an integer composition), and for
each distribution runs many random-restart Nelder-Mead optimizations over the
free split points (parametrized by a softmax so split fractions of a
multi-cut piece stay valid), minimizing OddSum. Taking the min over
distributions gives XY's true (numerically) optimal response value for that
LB partition. Sanity-checked against the *already fully proved* n=1 formula
(threshold t=2/3, V(t)=t below threshold, 1-t/2 above) — exact match to 4-5
decimal places across t=0.5..0.9, confirming the solver is correct.

### Distinct openings surfaced

1. **"LB never wants to deviate from geometric" reduction (variational/exchange framing).**
   Ran a 1-parameter sweep at n=2: fix p3=1/7, vary p1 (with p2=6/7-p1) through
   the geometric point p1=4/7. XY's optimal value f(p1) is **NOT unimodal** —
   it dips at p1=0.5143 (f=0.5143) below neighboring points p1=0.4714
   (f=0.5286) and p1=0.6 (f=0.5571), then spikes sharply to exactly 4/7 at the
   true geometric point p1=4/7=0.5715, then falls off again. This rules out a
   naive single smooth "exchange/smoothing always increases toward geometric"
   argument — the landscape has multiple regimes (kinks where XY's optimal
   cut-distribution combinatorially switches), and f is only maximized right
   at the isolated geometric point, not moving monotonically toward it. A
   variational proof of the upper bound is still conceivable but would need
   to handle several regime-boundary cases explicitly, not one global
   inequality. This is a genuinely different top-level target than "find a
   universal algorithm for XY": instead prove directly max_p f(p) is attained
   only at the geometric p via case-by-case local-optimality / KKT-style
   conditions on the (piecewise-smooth, piecewise-linear) function f.

2. **Regime-dependent optimal cut allocation (structural pattern, conjectural).**
   Across many random and hand-picked configurations (n=2,3; see numeric log
   below) XY's optimal cut allocation is either "spend all/most cuts
   splitting the current top piece p1 down" (when p1 is a clear outlier,
   e.g. (0.6,0.3,0.1), (0.7,0.2,0.1)) or "spend cuts splitting a *small*
   piece" when the top pieces are already near-tied (e.g. (0.45,0.45,0.1) ->
   XY splits p3, not p1/p2, because Tie-neutrality already neutralizes the
   near-tied top pair for free). This suggests the right general lemma is not
   "always attack the max" (already refuted) nor a fixed threshold, but
   something like: **XY should spend cuts to create as many
   Tie-neutrality-eligible matched pairs as possible** — i.e. generalize
   "duplicate-the-rest" from "replicate the whole tail against the top piece"
   to "match whichever piece is currently un-neutralized against a
   same-size replica carved out of the current max, recursively." This is
   consistent with, and would generalize, the certified
   `tie-neutrality-and-first-mover-half.md` lemma. NOTE: solutions found by
   the optimizer are highly non-unique (multiple cut-distributions/split
   points achieve the identical optimal value — see e.g. the geometric n=2
   case, where a 1-cut split reaches the exact same 4/7 as the canonical
   2-cut duplicate-the-rest), so don't over-trust any single numerically-
   found "canonical" rule; only the achieved *value* is a solid fact, not
   the specific split reported by one local optimum.

3. **Surrogate-adversary framing (from crux corpus, `aimo-0560`).** That
   problem's crux move: "replace the real adversary with a strictly stronger
   surrogate whose reply is pointwise at least as damaging, so a win against
   the surrogate transfers down and collapses to a finite per-region menu."
   Possible analogous move here: define a surrogate XY who is allowed a
   *slightly larger* budget or a *simplified* move set (e.g., XY may only
   cut pieces to exactly duplicate an existing piece value, an operation
   closed under recursion), show the surrogate always achieves <=c(n)
   against every LB partition (a smaller, more tractable strategy space),
   and then show the real XY (superset of surrogate moves) is only better.
   This has NOT been tried in prior rounds and is untested — flagging as an
   unexplored angle, not a verified path.

4. **Direct confirmation the conjecture itself is very robust.** Random
   Dirichlet search, n=2 (60 trials) and n=3 (40 trials, budget-limited runs
   due to compute cost), found **no violation** of OddSum<=c(n): max found
   values were 0.5674 (n=2, target 4/7=0.5714) and 0.5217 (n=3, target
   8/15=0.5333), both strictly below target and both attained near
   configurations close to (but not exactly, due to optimizer/sampling noise)
   the geometric shape. This is strong (but still numeric-only, not a proof)
   support that geometric is the unique maximizer and c(n) is correct.

### Candidate technique(s)
- Piecewise/case-based variational argument (opening 1) — likely needs KKT-
  style local-optimality conditions on the piecewise function f(p), handling
  regime boundaries explicitly (not a single smooth inequality).
- Generalized Tie-neutrality matching argument (opening 2) — extend
  `tie-neutrality-and-first-mover-half.md` from single equal pairs to a
  recursively-constructed maximal matching of pieces via splits; likely needs
  an inductive/greedy-matching lemma bounding the "unmatched residual."
- Surrogate/domination argument (opening 3, crux-inspired, untested here).

### Cheap-kill candidates
None found that shortcut the whole gap. But a useful pruning fact confirmed
numerically: LB's outer maximization is essentially never improved by using
fewer than n+1 pieces (k<n+1 strictly worse in every case checked, consistent
with current.md's "reduction to k=n+1" open sub-lemma) — worth certifying as
a standalone lemma since it shrinks the search space (only need to handle
k=n+1 exactly, not all k<=n+1) for whichever upper-bound argument is chosen.

### Knowledge-base entries to use
`knowledge_base.md` was checked; no problem-specific entry beyond generic
game-theory/extremal-principle framing exists yet for this problem (the KB
here mostly holds this run's own certified lemmas under `results/imo-2026-03/lemmas/`).
Repo `knowledge_base.md` should be (re-)checked by the outliner for generic
"minimax value = value of extremal configuration" or "smoothing/exchange"
technique entries if any were added since round 1 — I did not find new
generic entries relevant beyond what's already cited (Tie-neutrality,
First-mover-half, Greedy-optimality) which are this problem's own certified
lemmas, not generic KB entries.

### Analogous past problems (cruxes)
Filtered `past_crux_moves_database.json` by domain=combinatorics,
subtopic=games-and-strategy (39 entries), read all technique/how_used
fields plus full problem statements for the closest matches:
- **`aimo-0117`** (Jesse/Tjeerd stone-boxes game) — genuinely analogous
  *structurally* to the LOWER-bound side: the crux move is "assign played
  values as a two-sided geometric/dyadic sequence so the single largest
  value strictly exceeds the sum of all others," exactly the same
  "geometric-with-ratio-2 beats everything" phenomenon underlying LB's
  optimal construction here. Useful confirmation that "dyadic/geometric
  extremal sequence" is a recurring, provable pattern in this genre of game,
  but it does not directly supply the missing upper-bound technique (that
  problem's second crux, deferred-commitment invariant maintenance, is
  problem-specific and doesn't transfer).
- **`aimo-0560`** (gardener/lumberjack majestic trees) — analogous in
  *technique*, not statement: its "surrogate adversary" crux (see opening 3
  above) is the one clearly transferable idea I found in the corpus for
  attacking a "does a bounded-budget adversary have a response against every
  configuration" question. Worth the outliner's attention as an untried
  angle.
- No other entry in the games-and-strategy subtopic matched closely; the
  rest are pairing/mirroring strategies on discrete combinatorial boards
  (knights, dominoes, cards), not continuous-length partition games, so I
  do not report them as analogous.

### Prior progress
As stated in `current.md`: reduction to multiset-minimax (proved), Greedy-
optimality (proved), Tie-neutrality + First-mover-half (proved), n=0,1 fully
solved both directions, dominant-piece lower bound (proved for LB's side),
duplicate-the-rest exact response against LB's own geometric construction
(proved, all n). This exploration adds no new proof, only terrain-mapping and
numeric confirmation.

### Dead ends (do not retry)
Confirmed (via re-derivation, not just trusting the file) that the following,
already documented in `universal-halving-adversary.md`, are correctly
refuted and should not be retried as universal rules:
- "Bisect current max always" — fails on near-balanced top pieces (e.g.
  raises LB's value on (0.5,0.5) at n=1 from 0.5 to 0.75).
- "Duplicate-the-rest unconditionally" (i.e. always replicate the full tail
  against p1 regardless of shape) — fails badly on skewed configs
  (p1 near 1, tiny rest): duplicating a tiny rest barely dents an already-
  huge p1.
- "Threshold on p1 alone" (p1>sum(rest), or p1>c(n)) — refuted at n=2 by
  (0.5,0.3,0.2): p1 already below both thresholds, yet unsplit LB value 0.7
  is far above c(2)=4/7, because XY must act on a piece other than p1 (here
  the optimizer found the actual fix uses one cut on p1 splitting it into
  exactly the two remaining pieces' values, i.e. p1's split reconstructs the
  rest — a genuine "duplicate-the-rest"-flavored move, but triggered even
  though p1 alone doesn't cross any single-piece threshold).
I additionally re-ran this exact (0.5,0.3,0.2) case through the independent
numeric solver: confirmed optimal value 0.500 < 4/7, achieved by splitting p1
into (0.2,0.3) (matching the other two pieces exactly) — consistent with the
approach file's account, not a discrepancy.

### Small-case / intuition notes (all conjecture / numeric evidence, not proof)
- max over all tried/random LB partitions of XY's optimal response value
  equals c(n) exactly at (and, in every check, ONLY at) the geometric
  partition, for n=1,2,3 — strong numeric support for LB's optimum being
  uniquely geometric, but the value landscape has kinks/regime-switches (see
  opening 1), so this is not yet a clean inductive/variational proof.
- XY's optimal move is not literally "always cut p1" nor literally "always
  duplicate the rest" — it is regime-dependent on how close the top pieces
  are to already being tied (see opening 2), and optimal responses are
  frequently non-unique (multiple cut patterns reach the identical optimal
  value), so numerically-observed "canonical" strategies should be treated
  as one witness among possibly several, not necessarily the cleanest one to
  write up.
- The "reduce to k=n+1 pieces" sub-lemma (LB should always use its full
  point budget) — mentioned as an open sub-lemma in `universal-halving-
  adversary.md` — continues to look true and cheap to certify separately in
  all cases checked this round; recommend the outliner assign it as an
  independent, likely-tractable lemma regardless of which top-level
  upper-bound framing is chosen.
