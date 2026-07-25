# math-explorer report — fresh framing / plateau check / cross-pollination (round 7)

Lens: is the 5-approach field secretly one shared wall, is `layer-cake-parity-reframing`
still pulling weight, and does the crux corpus offer an unexplored top-level idea.

## 1. Single-gap-trap check: verdict — partially yes, but not fatally

Read all six files' obstruction language. Every approach that has produced a genuine
negative result names essentially the *same* mechanism, just discovered independently
in its own coordinate system:

- `layer-cake-parity-reframing`'s **Coupling Obstruction** (proved, exact `n=3`
  counterexample): a single cut's marginal `ΔAltSum` has no fixed sign — it depends on
  the parity of the background threshold-count contributed by *other, simultaneously
  present* cuts. No per-cut/piece-local bound can work; only a joint bound over the
  whole configuration can.
- `self-similar-induction-on-n`'s **Proposition C** (Case A of the trichotomy): explicitly
  flagged (lines ~115, ~172, ~204-225) as circular for the same underlying reason — the
  recursive reduction reintroduces an instance of the same size/shape it started from.
- `greedy-reduction-geometric`'s **Leftover-Fragment Obstruction** / Insertion-Robustness
  & Level-Absorption sub-problems: explicitly cross-checked against Proposition C (line 59)
  and confirmed "not a same-size recursive loop" but the file itself states the two
  residual sub-problems are "honestly reported as open" and of comparable difficulty
  (line 63) — i.e. still a joint-interaction obstruction, just in a different guise
  (interleaving of top-piece and tail cuts rather than cross-piece threshold parity).
- `universal-halving-adversary` explicitly cites "coupling mechanisms catalogued by this
  round's math-explorer" (line 118) when framing why $k\ge3$ merges aren't monotonically
  better than $k=2$ — again a joint (not additive) effect of simultaneous merge choices.

So: **four of five live approaches (all but `lp-duality-split-polytope`, whose remaining
gap is a number-theoretic non-monotonicity in the triangular family, a genuinely
different flavor of obstruction) are bottlenecked on the same underlying phenomenon** —
whatever the encoding (peel/top-piece asymmetry, self-similar recursion, threshold-count
parity, anchor-merge choice), no bound decomposable into independent per-element/per-cut
terms survives; the true dependence is joint across the whole configuration. This is
real corroboration, not just five people hitting a wall independently and calling it new
names — the layer-cake framing's contribution this round was precisely to *prove*, via a
clean exact counterexample with no combinatorial baggage, that this joint-dependence is
unavoidable *in principle* for the natural "additive budget" plan, which retroactively
explains why the peel-based approaches' analogous plans keep stalling too.

**This is useful information, not just a discouraging pattern**: it tells next round's
outliner that any approach proposing a per-cut / per-fragment / per-anchor independent
bound (additive budget, union bound, "sum of local damages") is very likely to hit the
identical wall and should be deprioritized in favor of approaches that already work with
a *global* invariant (LP-vertex extreme-point structure, which is inherently a joint/global
argument over the whole configuration, not additive) — i.e. `lp-duality-split-polytope`
and the Vertex Pinning Lemma machinery are structurally the right kind of tool for this
wall, and deserve more weight, while any newly proposed additive-budget mechanism should
be laughed out of the room at outline-review time unless it has a specific answer to the
Coupling Obstruction.

## 2. Should `layer-cake-parity-reframing` be retired? — Yes, recommend retiring from the
active build rotation (do not dispatch a builder to it next round), for these reasons:

- It has been idle two rounds (round 5, round 6) with zero new content — round 6's
  math-explorer presumably already flagged it idle once; this round confirms nothing has
  moved.
- Its unique deliverable, the Coupling Obstruction, is a **completed, proved negative
  result** — there is no half-finished thread left hanging in the file that a builder
  could pick up. The file itself says (line 222-234) that closing it requires either (a) a
  genuinely joint/telescoping potential argument, or (b) a restricted-order contradiction
  argument, and "neither has been carried out" — but also gives no lead on how to attempt
  either. Nothing distinguishes this from simply being stuck, and it's been stuck longer
  than the still-live approaches' residual gaps (which shrank measurably every round).
- Its *reusable* content (Lemma 1 layer-cake identity, Lemma 2 per-piece additivity,
  Lemma 3 single-cut marginal formula) is already marked "Promotable lemmas" and is
  generic/elementary — worth keeping as a certified lemma file if any other approach ever
  wants a threshold-count identity, but that's a one-time promotion, not a reason to keep
  paying for a builder round on this slug.
- No other approach depends on it (checked: none of the other four files reference
  `layer-cake-parity-reframing` by name or cite its lemmas as inputs) — retiring it costs
  nothing structurally.
- Recommendation: mark it dead in `current.md`'s dead-end list (it already effectively is,
  just not yet folded into that list format), optionally promote Lemmas 1-3 into
  `knowledge_base.md` as a generic "layer-cake / threshold-count parity" technique entry
  (reusable well beyond this problem), and free the round's build-set slot for either a
  genuinely new approach or an additional build pass on one of the four still-shrinking
  gaps.

## 3. Crux corpus search — no exact top-level match found; here's what's there

Searched (`crux_moves_documentation.md` schema, `past_crux_moves_database.json`) by:
- `domain=combinatorics, subtopic=games-and-strategy` (39 cruxes, all skimmed).
- Keyword sweep across `technique`/`how_used` for alternat*, claim, piece, stick, cut,
  greedy, partition, sorted/descending, pairing, odd-index.
- `domain in {combinatorics, algebra}, subtopic in {generating-functions,
  probabilistic-method, linear-algebra-method}` (~35 cruxes skimmed).
- Full-text scan of `past_problems_database.json` problem statements for
  stick/cut-into-pieces/claim/marks/divide-a-segment.

**Findings:**
- The `games-and-strategy` subtopic is dominated by *combinatorial-game* cruxes: pairing/
  mirroring/involution strategies, invariant/monovariant arguments, strategy-stealing,
  parity-of-move-count arguments (aimo-0074, aimo-0225, aimo-0445, aimo-0461, aimo-0596,
  aimo-0631, aimo-0663, aimo-0854, etc.) — these are all about discrete win/lose or
  first-player-advantage games on graphs/boards/tokens, not continuous-value optimal-split
  games. None transfers mechanically.
- The closest structural cousin is **aimo-0369** (a Dutch olympiad "row of $2n$ cards,
  players alternately take from either end, first player scores $\ge$ half" problem). Its
  crux move — strengthen "guarantee $\ge$ average" to "guarantee the ability to force
  *either* the whole odd-indexed set or the whole even-indexed set, player's choice" — is
  conceptually adjacent to our problem's Greedy-Optimality reduction (already certified
  as `lemmas/greedy-optimality-oddsum.md`), but the games are structurally different:
  aimo-0369 restricts moves to the two ends of a *fixed linear order*, forcing an
  inductive two-case (opponent-takes-left / opponent-takes-right) argument; our game lets
  either player claim *any* unclaimed piece, which is why our problem reduces cleanly to
  sorted-order OddSum via a greedy argument already in hand — i.e. our approach already
  captures the one useful idea this crux offers (the "strengthen to forcing a whole
  parity-class" move), just via a cleaner route since there's no adjacency constraint. No
  new mechanism to import here.
- No crux in `generating-functions` or `probabilistic-method` matches the specific
  structure of "adversarially split a weighted partition then read off an alternating-sum
  parity statistic" — the generating-function cruxes found are all about encoding discrete
  combinatorial *counts* via roots-of-unity filters (aimo-0155, aimo-0509, aimo-0685),
  which is essentially the discrete analogue of what `layer-cake-parity-reframing`
  already tried in continuous form (Lemma 1's integral IS a continuous roots-of-unity-style
  parity filter) — already explored and already hit the Coupling Obstruction.
- No full-text match for "stick"/"cut into pieces and claim" as a game in the problems
  database — this appears to be a genuinely novel competition construction with no direct
  crux precedent in the corpus.

**Bottom line on cross-pollination**: the crux corpus does not contain a slicker known
technique that closes either residual gap in one shot. The one adjacent idea
(aimo-0369's "force a whole parity class" strengthening) is already subsumed by this
problem's own certified Greedy-Optimality Lemma. No action item from the corpus this
round beyond the general lesson reinforced in §1: prefer joint/global arguments
(LP-vertex, generating-function/roots-of-unity global identities) over additive per-element
budget arguments, since the latter class has now failed independently in at least four
different encodings.

## Recommendations for next round's outliner

1. Retire `layer-cake-parity-reframing` from the active build rotation (see §2); promote
   its three lemmas to `knowledge_base.md` if convenient.
2. Do not open a new approach proposing an additive/per-cut/per-piece independent budget
   bound without an explicit rebuttal of the Coupling Obstruction — it will very likely
   hit the identical wall (§1).
3. If a genuinely different top-level idea is wanted to satisfy the plateau-break
   instruction, the best untried candidate is *not* from the crux corpus but from within
   the existing field: push more weight onto `lp-duality-split-polytope`'s LP-vertex
   machinery (already the one approach not caught in the shared-wall pattern) as the
   framing most likely to produce a genuinely joint (non-additive) closing argument for
   either gap, rather than opening a sixth slug from scratch.
