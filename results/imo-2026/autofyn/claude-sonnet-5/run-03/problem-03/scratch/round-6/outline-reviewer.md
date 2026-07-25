# Outline review — round 6 — imo-2026-03

Read: `/tmp/round-6/proof-outliner.md`, `results/imo-2026-03/current.md`,
`results/imo-2026-03/approaches/*.md`, `results/imo-2026-03/approaches/.ranking.json`.

No new slugs proposed this round — all six existing approaches are either
`revise`, `advance`, or `retire` (deprioritize). No `register_approach` or
`copy_approach` calls needed; ranking updated head-to-head below.

## Per-approach verdicts

### self-similar-induction-on-n — CHANGES REQUESTED (proceed)
Target: prove Theorem 2' (parametrized sliver closure, `G(m,k;V)` with
`V=2^{m-1}+eps`) by recursing the same tail-untouched dichotomy one level
down, claiming the excess `eps` exactly halves per recursion level.
- The mechanism (recursive dichotomy mirroring Theorem 2's own proof, one
  level down) is a real, checkable inductive step, not a bare "then it
  follows" — good.
- The outline itself flags the risk correctly: round 5's structurally
  similar "Two-Level Half-Bound Lemma" looked plausible numerically
  (matched at low precision) and failed to close the sliver. The outline
  explicitly tells the builder not to trust the eps/2 pattern from m=4,5,6
  numerics alone and to produce an actual induction. This is the right
  discipline — approved with that condition enforced.
- Per the standing memory rule (three-way-tie edge cases at every
  recursion level, not just the top), the outline calls this out
  explicitly ("Watch out for"). Good.
No fatal flaw. Proceed.

### greedy-reduction-geometric — CHANGES REQUESTED (proceed)
Target: Theorem 7'(m,k;L), extending Theorem 7 to allow the top tail level
to be split, tracking leftover mass L via the same Companion-Peeling
mechanism used to build Theorem 7.
- Mechanism stated (peel b1, then peel the surviving top fragment μ1 as
  new max, absorb leftover L into a smaller instance) is a genuine
  extension of an already-certified technique, not hand-waved.
- Correctly identifies this is UNPROVEN and gives the builder a concrete
  first task (numerically pin down f(L) before attempting the proof) —
  same discipline the memory rules require for any "believed true"
  mechanism (rules on stress-testing algorithmic/exchange claims before
  building on them).
Proceed.

### Overlap risk: self-similar's G(m,k;V) vs greedy's Theorem 7'(m,k;L)
This is the flagged concern (point 2 in the dispatch). Read both outline
sections closely: they are parametrizing genuinely different objects.
Self-similar's V parametrizes a *target value* shift (how much slack is
still needed on Case-B(m,k), tail untouched by construction). Greedy's L
parametrizes *leftover mass diverted by splitting the top tail level*,
which is a structurally different perturbation (the tail is no longer
untouched — this is precisely the extension Theorem 7 needed and lacked).
They could converge to the same underlying single-parameter recursion
under a variable rename (the outline itself flags this and instructs an
explicit STOP-and-import check), but at the level of the current outline
they are NOT literally the same lemma — self-similar's target is a
`(m-1)`-level sub-instance of the tail-untouched Case-B; greedy's target
is the interleaved case Case-B never reaches (tail is split). This is
legitimate intentional convergence per CLAUDE.md's cross-approach
unification precedent (round 5) and memory rule #8 (two different
mechanisms that would jointly close a gap is not automatically the
single-gap trap), not duplicated work — approved, with the outline's own
explicit dedup instruction kept as a hard requirement for both builders.

### universal-halving-adversary — CHANGES REQUESTED (proceed)
Target: retarget from a single closed-form rule (exhaustively refuted
this round per the outline's own report) to an Existence Theorem: for
every large-gap balanced partition, SOME pair (i,j) achieves a good
2-piece split via a to-be-proved Two-Piece-Split Vertex Lemma.
- Correctly abandons the single-rule family after real refutation
  (merge-chain/two-largest/largest-smallest/closest-pair, all killed) —
  this is the right response to a documented dead end, not a repeat.
- The Two-Piece-Split Vertex Lemma is a straightforward mechanical
  generalization of the certified Single-Piece-Split Vertex Lemma (same
  LP-vertex/piecewise-linear argument, one more free pair of dimensions)
  — sound technique, correctly cross-referenced to
  `lp-duality-split-polytope`'s certified lemma, with an explicit
  dedup instruction (assign to whichever builds first, other imports).
- The Existence Theorem itself is honestly scoped as "supported by 25/25
  random numeric evidence, no proof" — this is an ambitious ask for one
  round (a covering/counting argument over O(n^2) candidate pairs proving
  non-emptiness for every partition shape is a real theorem, not a small
  lemma) but the outline does not overclaim it as anything but a
  deliverable-in-progress, and gives concrete prioritized candidate
  families to check first. Acceptable scope for CHANGES REQUESTED.
Proceed.

### lp-duality-split-polytope — CHANGES REQUESTED (proceed)
Target: generalize the triangular-family Multi-Piece Necessity result
(currently only n=3,4, exact-arithmetic verified) to general n via the
Single-Piece-Split Vertex Lemma's finite candidate set applied
symbolically to the AP-structured landmark family.
- Sound continuation of a certified mechanism; the outline is honest that
  this is exactly the "natural next step, not attempted due to time" the
  round-5 builder already flagged, so it is not a fresh unverified leap.
- Cross-supply instruction for the Two-Piece-Split Vertex Lemma correctly
  coordinated with universal-halving-adversary (same lemma, don't
  duplicate) — good, matches memory rule on shared-crux assignment.
Proceed.

### dyadic-potential-invariant — CHANGES REQUESTED (proceed, well-scoped)
Target (point 3 in dispatch): spend first effort on a CHEAP numeric
feasibility check of the majorization/suffix-domination monotonicity claim
(aimo-0287 analogy) before any further proof effort; only proceed to the
exchange argument if it survives; explicit fallback (feed Vertex Pinning
Lemma to universal-halving-adversary's Existence Theorem) if it fails.
This is exactly the discipline the standing memory rules mandate (rule:
"ALWAYS numerically stress-test an abstract dual/exchange lemma... BEFORE
building a proof on it") and the outline states, unprompted, the honest
reason the analogy may NOT transfer (OddSum picks alternating RANKS of a
sorted multiset, not a chosen subset sum of a fixed sequence — the
aimo-0287 mechanism is for a different object). This is well-scoped for
one round: cheap test first (bounded effort, checkable in minutes), with
a real fallback path so the round is not wasted if it fails. No changes
needed to the plan itself. Proceed as written — this is a model of how to
scope a speculative lead, not a gap to flag.

### layer-cake-parity-reframing — retirement/deprioritization: JUSTIFIED
(point 1 in dispatch). Checked the outliner's claim directly: the
self-similar-induction-on-n approach file does contain, fully proved and
certified, both **Lemma AS** (`OddSum(X)=(sum(X)+AltSum(X))/2`, i.e. the
"AltSum ≥ 1" reformulation layer-cake also derives) and the **Single-
Insertion Lemma** (exact Δ-AltSum formula for inserting a value at an
arbitrary sorted position — strictly generalizes layer-cake's per-piece
bisection-only additivity to arbitrary single-value insertions). This
does substantively subsume layer-cake's unique content as claimed. The
Coupling Obstruction (layer-cake's own proved negative result) blocks
only "independent per-cut, piece-local" bounds — no live approach this
round uses that mechanism (self-similar uses the more general recursive
dichotomy; greedy uses Companion Peeling; universal/lp-duality/dyadic are
upper-bound, unrelated). This is round 2 of idling (round 5 idle, round 6
idle) — the outline correctly holds off from *formal* full retirement
(reserved for a 3rd idle round) while still correctly excluding it from
this round's build set. No objection; the 4 certified lemmas remain on
disk as an importable measure-theoretic resource per the outline's note.
Approved as written.

## Diversity check
The field still splits cleanly across the two genuine top-level gaps
(lower bound: self-similar + greedy; upper bound: universal + lp-duality +
dyadic), with the lower-bound pair's V/L parametrization overlap addressed
above as legitimate convergence (not the single-gap trap), and the
upper-bound triple correctly redirected to three distinct sub-tasks
(existence-via-2-piece-vertex, general-n necessity theorem, and a
genuinely different non-LP mechanism as dyadic's first cheap check) — this
is exactly the response called for by the round-5 plateau watch (memory
rule #13/WATCH note): if dyadic's majorization check also collapses into
LP-vertex machinery, that will be the signal for a real 4th framing next
round; for now the redirection is a legitimate attempt to break the
plateau, not a repeat of it.

## Ranking
Ran `update_ranking` with round-5-evidence-anchored comparisons: each of
the 5 continuing/active approaches beats `layer-cake-parity-reframing`
(idle 2 rounds, deprioritized, not rebuilt) reflecting its non-selection
into the build set; `universal-halving-adversary` (highest-value certified
closed-form result, Anchor-Merge) beats `dyadic-potential-invariant`
(real tool, but admittedly does not close anything alone); `lp-duality-
split-polytope` (concrete exact-arithmetic necessity instances) drawn
against `dyadic-potential-invariant` (comparable-tier positive tool,
neither closes its gap). Resulting order (best-first): universal-halving-
adversary (1652), greedy-reduction-geometric (1551), self-similar-
induction-on-n (1527), lp-duality-split-polytope (1503), layer-cake-
parity-reframing (1417, correctly dropped despite being spared full
retirement), dyadic-potential-invariant (1349, lowest but still live and
correctly still selected into the build set this round for its
well-scoped cheap check).

## Build set
All 5 approaches the outliner marked `revise`/`advance` are approved as
scoped, with the V/L-parametrization overlap and the majorization
cheap-check flagged above as watch items (not fatal). `layer-cake-parity-
reframing` stays out of the build set this round (correctly, per its own
2-round idle status) but remains registered/ranked, not deleted.

build set: self-similar-induction-on-n, greedy-reduction-geometric, universal-halving-adversary, lp-duality-split-polytope, dyadic-potential-invariant
