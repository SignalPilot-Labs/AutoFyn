## imo-2026-03

### Plateau assessment (task 1)

**Verdict: round 14 was genuine but narrow/incremental — the SECOND consecutive
round (13, 14) with no closure of either core remaining gap. The
discharging/charge-conservation plateau-break should be opened this round,
but NOT with the literal weight `w(v,s)=v·2^{-|log2 v - s|}` — that specific
proposal is numerically falsified as a conserved invariant (see below), so
it must be redesigned, not built as-is.**

Reasoning, checked against `current.md` / `run_state.md` directly rather than
taken on trust:

- **Gap (a), GT(m) general m** (lower bound, `self-similar-induction-on-n`):
  open since round 4 (the Case A/B/middle-regime trichotomy). Round 12 closed
  the shared window at `l=1..4` via GT(m) for `m=0..3` — a real closure.
  Round 13 closed the large-sum scope restriction unconditionally for
  `m<=3` and *simplified* the case architecture (Rank-Shift Identity
  replacing 4 ad hoc lemmas), but did **not** advance `m>=4` itself — it
  only re-stated the open residual as two named sub-cases. Round 14's
  Small-Sum Reduction Theorem is explicitly **not certified** (self-reported
  gap at a tie boundary) and its actual effect is to identify that the
  small-sum branch reduces to `Case-B(m,k)` — an object that has been open
  since round 4, i.e. round 14 glued one 10-round-old open gap onto another
  already-open sub-case rather than closing anything. Net: **`GT(m)` for
  `m>=4` is exactly as open today as it was after round 13**, only
  re-packaged.
- **Gap (b), Σ-shape / fragment-vs-fragment tying** (upper bound,
  `global-lp-vertex-sufficiency`): open since round 10 (after `Q_region`
  closed). Round 14 ran two cheap-kills as instructed: cyclic pairwise-tie
  chain is cleanly refuted (real negative result, prunes search space) but
  descending fragment chain is "mixed" — no closed-form selection rule
  found, exhaustive search matches `V(p)` at only 2/3 known hard points and
  is as expensive as computing `V(p)` directly. **No progress toward an
  actual bound on `|Σ(n,k)|` or a provable selection rule.** This is the
  fourth consecutive round (11, 12, 13, 14) in which this gap only produces
  refutations of specific mechanisms, never a positive closure.
- The `lp-duality-split-polytope` Chain-Correction Floor Theorem is real and
  certified, but it proves a floor value `V(e_0)=1/2` and corrects an
  overclaim — it does not touch either open gap's actual target
  (`GT(m)` general-`m`, or a bound/selection-rule for `Σ(n,k)`).

So by the letter of the round-14 dispatch's own trigger ("if both stall
again next round, open it"): **both did stall.** GT(m) general-`m` is
unchanged in substance since round 13; Σ-shape/fragment-tying is unchanged
in substance since round 13 (a cheap-kill executed, not a closure). This is
also independently a violation of CLAUDE.md's "3+ rounds on the same gap is
a sign the direction is wrong" rule — `GT(m)`/Case-B(m,k) has now gone
unclosed for **11 rounds** (round 4 through round 15) under the same
peel-max-case-split mechanism, and Σ-shape/tying for **5 rounds** under the
same vertex-enumeration mechanism. **Recommendation: open a new-mechanism
approach this round.**

### Mandatory cheap-kill: numeric falsification of `w(v,s)=v·2^{-|log2 v - s|}`

Tested exactly as instructed, BEFORE any proof investment. Script:
`/tmp/round-15/test_discharge.py`. Setup: for a sorted-descending multiset
`(x_1,...,x_N)`, define total charge `Σ w(x_i, s(i))` for several natural
candidate scale assignments `s(i)` (the proposal left `s` underspecified —
it is meant to be "the rank/scale a piece is expected to occupy," so the
natural readings are `s=-i`, `s=i`, `s=-(i-1)`, all tested), and check
whether this total is **exactly conserved under a single legal cut**
(one piece of value `v` replaced by two positive fragments summing to `v`,
multiset re-sorted) — the property the proposal explicitly requires
("conserved exactly under every single-cut move, provable by a local,
one-cut computation").

Results, **all three natural scale conventions**:
- Structured example, geometric partition `(8,4,2,1)/15` (n=3), splitting
  the **top** piece `8 -> 4.8+3.2`: `s=-i` gives `Δ=+0.03125`; `s=i` gives
  `Δ=+0.9988` (huge, ~15% of the piece value); `s=-(i-1)` gives `Δ=+0.0625`.
  None is zero.
- Same partition, splitting a **middle** piece (`2 -> 1+1`): `s=-i` gives
  `Δ=+0.03125`; `s=i` gives `Δ=-0.34375`; `s=-(i-1)` gives `Δ=+0.0625`.
  Sign even flips between top-split and middle-split under `s=i` — not a
  constant offset, not a small perturbation.
- **3000 random single-cut trials** (random multiset size 2–6, random
  values, random split point, random split ratio): max `|Δ|` over all
  trials is `0.31` (`s=-i`), `2.78` (`s=i`), `0.61` (`s=-(i-1)`) — these
  are **order-of-magnitude comparable to the piece values themselves**
  (e.g. the `s=-i` worst case has values `~2.47, 0.12` and `Δ=0.31`, i.e.
  ~12% of the larger piece), not numerical noise from floating point.

**Conclusion: the literal weight is decisively falsified as a conserved
invariant under all three natural scale conventions**, exactly as the
dispatch anticipated as the likely outcome (framed as "kill it immediately
... per the discipline the population has already established for this
failure mode"). This is now the **third** documented failure in the
"single-cut-local invariant on OddSum/AltSum" family, after
`dyadic-potential-invariant`'s Cut-Reallocation Exchange Lemma (rounds 3–4)
and `layer-cake-parity-reframing`'s per-cut-additive decomposition
(round 4) — both also killed by exact counterexample. **Do not build a
proof on this specific formula, or on any other single fixed closed-form
potential evaluated purely on a piece's own `(value, rank)` pair** — three
independent members of that narrow family have now failed for structurally
similar reasons (a single cut changes not just the split piece's own charge
but every other piece's rank, and no simple rank-local formula absorbs
that shift exactly).

### What a genuinely different discharging mechanism would need

The failure mode above is specific and diagnostic: single-cut local
invariants fail because splitting one piece changes the RANK of every
piece below it in sorted order, and no charge formula depending only on
`(value, own rank)` can compensate for a rank shift it doesn't see. Real
discharging arguments (e.g. Four-Color-Theorem style) do not use a single
closed-form potential — they define an explicit **charge-transfer rule**
between neighboring/adjacent objects and prove conservation by summing
transfers, not by evaluating one formula per object. The genuinely untried
variant is: define charge transfer **between a piece and its immediate
sorted-order neighbors** (charge flows to/from the pieces on either side of
a cut, not just accounted locally at the cut site), with the transfer rule
itself (not a value formula) proved to net to zero. This is a real,
buildable target distinct from what's been tried, but it needs the
outliner/builder to design the transfer rule — it is not reducible to a
30-minute numeric spot check the way the fixed-formula version was.

### Distinct openings

1. **Open the discharging approach this round, but scoped to the neighbor-
   transfer-rule variant, not the falsified fixed-weight formula.** First
   buildable target: define an explicit charge-transfer rule for a single
   cut (piece `v` at rank `i` split into `v1,v2`) that redistributes charge
   only among the pieces whose rank changes (the split piece and everything
   originally ranked below it), and check by direct algebra (not a closed
   formula search) whether some such rule makes total charge exactly
   invariant. If even this fails a first sanity check (e.g. on the n=2,3
   geometric partition, hand or short script), do not pursue further — this
   keeps the mandatory-cheap-kill discipline alive one level deeper rather
   than abandoning the family after only the naive variant.
2. **Stay-the-course option**: keep pushing GT(m)'s two sharply-diagnosed
   sub-cases directly — (i) `q=1, e>=1` (target `2^k - a_1`, not yet
   reduced to a known family) and (ii) the small-sum `GT(k-1)`-mirror
   (needed even at `e=0`) — since round 13 already reduced the entire
   general-`m` gap to exactly these two objects and they have not
   individually been attacked yet (only jointly diagnosed). This is lower
   risk than a new mechanism but has now had a full round (14) with no
   direct attempt.
3. **Push the `Σ`-shape gap's one live positive lead**: round 14's
   descending-fragment-chain is "mixed," matching `V(p)` at 2/3 known hard
   points — worth one more round determining whether the failing 1/3 point
   is a genuine counterexample or a search-depth artifact (the file itself
   flags this as unresolved), before deciding whether the mechanism is
   salvageable with a better selection rule or dead like its siblings.

### Candidate technique(s)

- Neighbor-transfer discharging (see above) — genuinely new, not yet built.
  KB: "Invariants & monovariants" (combinatorics section, line 117).
- Continuing: peel-max case-split induction (`self-similar-induction-on-n`,
  GT(m)); LP/hyperplane-arrangement vertex enumeration
  (`global-lp-vertex-sufficiency`, Σ-shape). Both stuck per above.

### Cheap-kill candidates

- Done this round: `w(v,s)=v·2^{-|log2 v - s|}` (all 3 natural `s(rank)`
  conventions) — **falsified**, deltas 12%+ of piece value, not noise. See
  `/tmp/round-15/test_discharge.py`.
- Recommended next cheap-kill (before full proof investment on opening 1):
  hand-check whether ANY neighbor-transfer rule can zero out the `s=-i`
  variant's `Δ=0.03125` residual on the `(8,4,2,1)/15` top-split example by
  moving charge only to the ranks that shifted (ranks 2,3,4 in the
  post-split ordering) — a 10-minute algebra check, not a new script,
  before the outliner commits a full approach file to it.

### Knowledge-base entries to use

- "Invariants & monovariants" (combinatorics section) — for opening 1, if
  pursued with the neighbor-transfer redesign.
- No new NT/geometry entries apply; nothing else in `knowledge_base.md`
  offers an untried top-level mechanism for this problem (already checked
  in prior rounds — LP-duality, layer-cake, generating functions,
  majorization/Schur, probabilistic method all tried or ruled thin).

### Analogous past problems (cruxes)

Re-checked the `combinatorics`/`invariants-and-monovariants` subtopic
(181 entries) directly for anything resembling a true discharging/
charge-transfer argument on a rank-weighted or alternating-sign sum. None
matches closely:
- `aimo-0019` — bounds a family of dyadic-length pieces by twice the
  largest via a geometric-series argument, and maintains a linear potential
  bounded by a constant times progress. Closest in *flavor* (dyadic pieces,
  potential-vs-progress) but its potential is a simple additive bound, not
  a redistribution/conservation argument, and its objective isn't rank-
  alternating. Inspiration only, as round 14 already flagged.
- `aimo-0146` — exchange smoothing on a weighted sum of a monotone bounded
  sequence (already cited and partially used by `greedy-reduction-geometric`
  in round 9 for Level-Absorption). Not a discharging argument, and already
  in use elsewhere in the field.
- `aimo-0281` — "assign position-dependent weights to cells, choose them so
  every allowed move leaves the weighted total invariant" is the closest
  *structural template* to what a genuine discharging argument here would
  need (position-dependent weight + move-invariance), but it's a discrete-
  grid/cell process, not a continuous split-a-piece game; no step
  transfers directly. Worth a closer look if opening 1 is pursued (not yet
  read in full — flagged as a lead, not verified).
- **No exact match found**; confirms round 14's own conclusion — this
  problem's objective (OddSum on sorted refinements under a cut budget) has
  no close analogue in the sampled corpus. Report honestly: the field must
  design the discharging mechanism from scratch, not adapt one.

### Prior progress

See `current.md`: Branch-I.A-restricted window closed `l=1..4`; `Q_region`
fully closed; `Chain-Correction Floor Theorem` certified (`V(e_0)=1/2` for
`n>=6`); AltSum Corollary + Growth Lemma certified (elementary, reusable,
but not gap-closing). Both core gaps (`GT(m)` `m>=4`; `Σ`-shape
classification/fragment-tying) remain open as of round 14, in substance
unchanged since round 13.

### Dead ends (do not retry)

- `w(v,s)=v·2^{-|log2 v - s|}` as a literal single-formula, single-cut-
  conserved charge — falsified this round under all 3 natural scale
  conventions (`Δ` up to 12%+ of piece value on structured examples, up to
  huge deltas on `s=i` even sign-flipping between top- and middle-splits).
  This is now the third failed single-formula/single-cut-local-invariant
  attempt (with Cut-Reallocation Exchange Lemma and per-cut-additive
  layer-cake) — any future discharging attempt MUST use a real
  transfer-between-neighbors rule, not a fixed value/rank formula, or it
  will almost certainly repeat this failure.
- All prior dead ends listed in round 14's report stand unchanged
  (region-geometry/exchange-mechanism class for Σ-shape; bounded-`s_0`
  named constructions; Cut-Reallocation Exchange; per-cut-additive
  layer-cake; majorization/Schur; structured-randomization).

### Small-case / intuition notes

- (Conjecture, unchanged) `c(n)=2^n/(2^{n+1}-1)`.
- (New numeric observation, this round) the failure pattern of the fixed-
  weight discharging attempt is itself diagnostic, not just negative: the
  delta is driven almost entirely by the RANK-SHIFT of pieces below the
  split point, not by the split piece's own charge change (verified by
  inspecting the `s=i` middle-split example, where the sign of `Δ` flips
  depending on whether the split piece is at the top or in the middle,
  something a rank-shift-blind formula cannot capture) — this is why a
  neighbor-transfer redesign (opening 1) is the natural next step rather
  than tweaking the formula's constants.
