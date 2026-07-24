# Proof-outliner report — round 3, imo-2026-03

## Summary

Read `current.md`, all 4 files in `approaches/`, all 14 files in `lemmas/`,
and the 3 round-3 explorer reports. All three live approaches
(`greedy-halving-adversary`, `smoothing-compactness-certificate`,
`self-similar-potential-certificate`) remain converged on the same
reviewer-verified obstruction: a cross-term/interleaving inequality for
Xiang Yu's budget split $c\ge1$ that no purely mass-based bound can prove
(confirmed independently from at least two directions). Per CLAUDE.md's
shared-gap-plateau rule, this round's job was to put genuinely different
mechanisms on the table, not another mass-accounting variant. Did not find
a genuine new *proof* to add to the 3 live approaches (their proved content
is sound and unchanged); added light cross-reference notes to each pointing
forward to the new approaches, and opened **3 new approaches**, one per the
most promising, mutually-distinct leads the round-3 explorers surfaced.

## Revisions to the 3 live approaches

No new lemmas or proof content added to any of the three — nothing false in
them, and no genuine new proof step was found this round. Appended a short
"## Outline update (round 3, proof-outliner)" section to the bottom of each
file (their existing Status/Approaches tried/Current best/Full proof/Open
gaps/Promotable lemmas sections are untouched):

- `greedy-halving-adversary.md`: flagged that its Open gap 0 (the cross-term
  inequality) is now cross-confirmed dead-end-as-mass-bound from 3 angles;
  pointed to the new `rank-tie-vertex-reduction`,
  `exchange-argument-extremal-response`, `self-similar-bracketing` approaches
  as the round's attempt at genuinely different mechanisms for the same gap.
- `self-similar-potential-certificate.md`: noted the new $c=n$ exact closed
  form (found this round by the integer-lattice explorer) complements its
  own $c=0$ closure and seeds the new `self-similar-bracketing` approach,
  which reuses this file's Lemma A/B.
- `smoothing-compactness-certificate.md`: noted its own "slot decomposition"
  sketch and the new `rank-tie-vertex-reduction` approach appear to be the
  same underlying idea from two independent directions — flagged for future
  coordination rather than duplicated derivation.

## New approaches opened (round 3), each a genuinely different mechanism

1. **`rank-tie-vertex-reduction`** (Lead: rank-tie/vertex framing). Claims
   the minimum of $\Phi$ for a fixed Xiang-Yu cut-budget composition is a
   piecewise-linear function of the free cut positions, hence attained at a
   rank-tie "vertex" (two fragments exactly equal) or a degenerate boundary
   — reducing the continuum optimization to a finite exact-matching check
   via the certified `leftover-formula`, never bounding the cross-term
   integral at all. Seeded by a concrete, reproducible $n=3$ exact-tie
   computation (the round-3 rank-tracking explorer's grid search: minimum at
   $a=p_2$, $b=p_4$, multiset with three copies of $4/15$). Main open risk,
   stated in the file: the piecewise-linear-vertex-minimum lemma itself is
   not yet proved, and even granting it, the resulting tie-configuration
   enumeration is not obviously small (same difficulty flagged from two
   other angles — itself evidence this is the real crux of the problem).

2. **`exchange-argument-extremal-response`** (Lead: exchange argument on the
   extremal minimizer, crux-inspired by `aimo-0119`/`aimo-0425`/`aimo-0146`).
   Fixes a hypothetical Xiang-Yu response minimizing $A(S)$ against the
   ladder (exists by compactness), derives local single-cut and two-cut
   re-pairing "no strict improvement" conditions, and aims to show these
   conditions force a rigid pairing shape unrealizable with only $n$ cuts
   (the resource-deficit fact already on record). Never writes down the
   integral/alternating-sum formula for a generic response, so it structurally
   cannot inherit the "mass bound too weak" failure mode. Entirely open —
   the two-cut exchange condition (the crux of the whole approach) is not
   yet even stated precisely; flagged as the first concrete builder task,
   with a suggested $n=3$ sanity check against the rank-tie explorer's
   already-found tie example.

3. **`self-similar-bracketing`** (Lead: monotonicity-in-budget-split /
   deferred-commitment induction, crux-flavor `aimo-0117`). Brackets Xiang
   Yu's cut-budget split $c\in\{0,\dots,n\}$ between two now-**exact**
   endpoints: $c=0$ (already certified, `untouched-top-piece-lower-bound`)
   and $c=n$ (new this round — a rescaled copy of the ladder fragmenting
   $p_1$ entirely, proved via a rigid strict-alternation merge-order
   argument that I re-derived and checked algebraically before writing the
   outline: $q_i>p_{i+1}\iff 2^{n+1}>2^{n+1}-1$ always true, $p_{i+1}>q_{i+1}
   \iff 2^{n+1}-1>2^n$ true for $n\ge1$ — both endpoints give exactly
   $\Phi=p_1=2^n/(2^{n+1}-1)$, the target itself). Proposes an induction on
   Xiang Yu's cut count (processed one at a time in a prover-chosen order,
   tracking a "ladder-top dominance" invariant) as the primary mechanism to
   close the interior, with a monotonicity/exchange argument as fallback.
   Entirely open beyond the two endpoint computations — the invariant is not
   yet stated.

## Not built / flagged for outline-reviewer's attention

- **`integer-lattice-reduction`**: registered in the ranker (elo 1454,
  expanded 0) from round 2 but **no approach file was ever written for it**
  — an inconsistency in the workspace (ranker entry with no corresponding
  file). The round-3 integer-lattice explorer tested this framing directly
  (exhaustive lattice search at $n=2,3$) and found it **not viable as
  originally scoped**: the LP-vertex reduction is real but buys no leverage
  (the optimum is highly degenerate — many tied lattice configurations — and
  the resulting finite search is exactly as combinatorially hard as the
  continuous problem). Recommend the outline-reviewer formally retire this
  slug (it has no file to rank/build against, and the one explorer who
  tested its premise found it a dead end) rather than carry a ghost entry
  forward. Do not dispatch a builder to create a file for it.
- **`induction-first-move-reduction.md`**: exists on disk but has **no
  ranker entry at all** (orphaned from round 1 — never registered). Status
  `unsolved`, and its own outline already flags a fatal arithmetic error in
  its core recursion ($2^n+2^{n-1}\ne 2^n$) that was never resolved. Not
  revised this round (nothing new to add, and it's not live in the ranker
  regardless). Recommend the outline-reviewer either formally register-and-
  immediately-retire it for bookkeeping cleanliness, or simply continue
  ignoring it — either is fine, but flagging so it isn't rediscovered as a
  "mystery file" later.

## Build set recommendation

Given the plateau-break instruction, recommend the build set include **at
least the 3 new approaches** this round (to actually test whether any
different mechanism gains traction), alongside continued expansion of
whichever live approach(es) the outline-reviewer judges highest-value:
`rank-tie-vertex-reduction`, `exchange-argument-extremal-response`,
`self-similar-bracketing`, plus the outline-reviewer's own pick among
`greedy-halving-adversary` / `self-similar-potential-certificate` /
`smoothing-compactness-certificate` for continued work (none had a genuine
new proof step to build this round beyond what's already recorded, so
re-building them verbatim would likely just repeat round 2's stall — the
outline-reviewer may reasonably deprioritize them this round in favor of the
new field, per the plateau rule).
