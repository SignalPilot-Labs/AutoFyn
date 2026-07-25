# outline-reviewer report — round 12, imo-2026-03

## Scope

Reviewed the outliner's round-12 field: 4 revised approaches
(`global-lp-vertex-sufficiency`, `self-similar-induction-on-n`,
`greedy-reduction-geometric`, `lp-duality-split-polytope`) plus the newly
opened plateau-break approach `structured-randomization-upper-bound`.
Read `current.md`, every file in `approaches/`, the relevant
`lemmas/*.md` certifications referenced by the round-12 target sections,
and `/tmp/round-12/proof-outliner.md`.

## Verdict on `structured-randomization-upper-bound`: KEEP, genuinely viable and concrete

This is not a hand-wave. It clears the bar for a real population member:

- It already contains **real, checked negative content**: the naive
  i.i.d.-uniform baseline was actually implemented (200,000 trials,
  reported numbers) and shown to fail decisively
  ($\mathbb E[\mathrm{OddSum}]\approx0.6035 > c(2)\approx0.5714$ at
  $p=(0.35,0.34,0.31)$), which is exactly the discipline CLAUDE.md wants:
  a documented dead end so nobody re-pays that cost, not an unverified
  claim of promise.
- The proposed structured design is **specific, not generic**: randomize
  the *discrete* tie-target choice of an already-certified construction
  (Theorem 12 / `lemmas/generalized-subset-tie-theorem12.md`) rather than
  continuous breakpoints — a concrete combinatorial object with a
  stated mechanism (linearity of OddSum on a fixed order type, summed
  against a distribution instead of optimized over cells).
- It has a **mandatory, falsifiable gate** before any proof writing: compute
  $\mathbb E[\mathrm{OddSum}]$ exactly (closed form or exact-`Fraction`
  Monte Carlo, explicitly banning float optimizers per the project's
  standing rule) at $n=2,3,4,6,8$ against $c(n)$, including the two
  already-catalogued hard points ($e_0$, the naive-form failure point).
  If it fails there too, the file already commits to recording it as a
  dead end rather than persisting — this is the right shape for a
  plateau-break slug: cheap to falsify, not a research program with no
  exit condition.
- It is **genuinely far from the shared machinery**: no cell arrangement,
  no vertex enumeration, no affine-on-a-cell argument used as the
  *mechanism* (it appears only as an internal computational aid, not as
  the closing argument) — it fails independently of whether the
  vertex/tie/affine-cell lineage has a fundamental limitation, which is
  the entire point of opening it. This satisfies CLAUDE.md's plateau-break
  requirement in substance, not just in name.

**Conclusion: approved into the population**, registered at cold-start
Elo 1500 (`register_approach`). Correctly `unsolved` this round; the
build-set task for it (design + numeric check only, no proof) matches
what a proof-builder can actually deliver.

## Revised approaches: targets checked, none circular

- **`global-lp-vertex-sufficiency`** (Region-Boundary Monotonicity,
  primary): well-posed. It is a genuine *new* claim (a consistent-sign
  monotonicity argument across cells), not a restatement of the
  already-closed Boundary Continuity Theorem or region classification —
  the gap it isolates (sign consistency before knowing the cell, or a
  monotonicity-preserving version of the certified Lemma 4.2 continuity
  technique) is concrete and non-circular: it does not assume the thing
  it sets out to prove. Secondary fragment-vs-fragment target is honestly
  demoted on a stated soft-negative numeric signal, not oversold.
- **`self-similar-induction-on-n`** Target 1 and **`greedy-reduction-
  geometric`**'s target: these are now, by the round's own (independently
  reviewer-traceable) symbol-for-symbol equivalence, **the same open
  statement** — the Branch-I.A-restricted window / Theorem N residual.
  This is not circular reasoning; it is an honest discovery that two
  previously separate lines of work share one gap, correctly reported as
  such in both files, each with an explicit "coordinate, don't duplicate"
  instruction pointing at the other's file for the shared dichotomy plan.
  I checked this is real, not asserted: both tail sections state the
  identical target formula
  ($c_1\in[2^{\ell-1},2^{\ell-1}+1-\varepsilon)$, etc.) verbatim. The risk
  is wasted duplicate proof-writing if both builders attack it
  independently without reading each other's file — mitigated by the
  explicit cross-references already in place, and in fact a legitimate
  outcome: two independent attempts at the single hardest remaining
  lower-bound gap, in the framing each owns best (self-similar owns
  Theorem W / Lemma TPI; greedy owns the Level-Absorption-side framing),
  raises the odds of closing it this round rather than being pure waste.
  Not cut.
  `self-similar-induction-on-n` Target 2 (import Rank-Pinning technique
  into Middle-Regime Vertex Reduction) is well-posed and independent of
  Target 1 — no overlap, no circularity.
- **`lp-duality-split-polytope`**: correctly redirected off a dead
  transfer (explicitly ruled out: its own machinery does not bridge to
  the lower-bound window, stated plainly rather than forced) and onto
  `global-lp-vertex-sufficiency`'s demoted Opening 1
  (fragment-vs-fragment tying) at the exactly-characterized hard vertex
  $e_0$. This is **not duplicative** with `global-lp-vertex-sufficiency`'s
  own target: the latter's primary target is Region-Boundary Monotonicity
  (a reduction-side argument), with fragment-tying only secondary/
  deprioritized there; `lp-duality-split-polytope` is the one file
  actually assigned to attempt it, playing to its stated strength
  (explicit proved constructions, not searched ones). Well-posed, single
  owner, no overlap.

No approach in the round-12 field is doomed by wrong technique, an
unjustified leap, a missing case, or circular reasoning. All five targets
are concrete enough for a proof-builder to act on directly.

## Ranking

Registered `structured-randomization-upper-bound` (cold start, Elo 1500,
`expanded=0`, no outcome yet). Folded round-11 pairwise comparisons among
the four revised approaches into Elo via `update_ranking` (all `stale`
cleared): `lp-duality-split-polytope` and `global-lp-vertex-sufficiency`
edge `self-similar-induction-on-n` (both closed/proved sharper results —
an all-$n$ exact witness theorem, and two closed soundness gaps plus a
scoped impossibility theorem — against `self-similar-induction-on-n`'s
more modest small-instance closures); `greedy-reduction-geometric` draws
with all three (its Theorem N unification is real positive content, but
built on a refuted "quick win" premise this round). Resulting order:
`greedy-reduction-geometric` (1633) > `lp-duality-split-polytope` (1607)
> `global-lp-vertex-sufficiency` (1536) > `self-similar-induction-on-n`
(1492) > `structured-randomization-upper-bound` (1500, unranked by
outcome yet) > `universal-halving-adversary` (1500) >
`layer-cake-parity-reframing` (1398) > `dyadic-potential-invariant`
(1333, dead-end). The three untouched/deprioritized approaches were left
alone per the outliner's no-new-lead instruction.

## Build set

All five: the four revised approaches have concrete, non-circular,
non-duplicative (or intentionally, transparently shared-and-coordinated)
targets ready to build, and the new plateau-break approach's first step
(design + exact-arithmetic numeric sanity check) is squarely
buildable work this round even though it is not yet a proof attempt.

build set: global-lp-vertex-sufficiency, self-similar-induction-on-n, greedy-reduction-geometric, lp-duality-split-polytope, structured-randomization-upper-bound
