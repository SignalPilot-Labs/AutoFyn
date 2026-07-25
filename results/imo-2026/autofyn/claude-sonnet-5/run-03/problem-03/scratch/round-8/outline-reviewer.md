## Round 8 outline review — imo-2026-03

Reviewed: `lp-duality-split-polytope` (revise), `self-similar-induction-on-n`
(revise), `greedy-reduction-geometric` (revise), `universal-halving-adversary`
(revise, narrowed scope), `global-lp-vertex-sufficiency` (new).

### lp-duality-split-polytope — APPROVE

Independently re-derived every load-bearing claim before approving:

- **Verified the outline's central factual claim** — that the previously-
  conjectured closed form `⌊(N-3)/2⌋` for the `idx=1` (top-piece-split)
  minimizer is **false for `N≥11`**. Ran my own exact-`Fraction` vertex
  search (vertex candidates: fragments pinned to `0`, to a landmark integer,
  or equally splitting the leftover — the same vertex shapes the project's
  certified Single-Piece-Split Vertex Lemma uses), independent of the
  approach file's own script: true minimum at `N=11` is exactly `3`
  (`⌊(11-3)/2⌋=4`). Confirmed for `N=4..16` (matches the file's own reported
  pattern exactly). **The outliner correctly dropped `⌊(N-3)/2⌋` as a proof
  target** and correctly redirects to the actually-needed, much weaker
  claim `A(N,N,y)≥1` — this is the right call, not a hand-wave; re-targeting
  a disproved-but-unneeded closed form to the true minimal sufficient
  statement is exactly right, and the outline explicitly instructs builders
  not to resurrect it ("Watch out for" section).
- **Verified the Odd-multiplicity reduction** `AltSum(T)=AltSum(Odd(T))`
  by 2000 random-multiset trials (up to multiplicity 4, values 1-6): zero
  mismatches. Sound, as claimed "elementary."
- **Verified Claim D** (`M∉C` / `M∈C` two-case discrete floor) by exhaustive
  brute force over all subsets `C⊆{1,...,M}` with `sum(C)≤M+1`, `M=1..13`:
  zero violations for `M≥3` (the operative range, since `n≥3` gives `M=N-1≥3`
  once `N≥4`). **Caught a real edge case not flagged in the outline**: for
  `M=1,2`, `C=B` itself (removing everything, `AltSum(∅)=0<1`) is a genuine
  counterexample — but this is automatically excluded once `M≥3` because
  `sum(B)=M(M+1)/2>M+1` there, so `C=B` never satisfies the budget
  constraint for `M≥3`. Since `n=0,1` are already fully solved elsewhere
  (separate from this theorem's scope), this is not fatal, but flag it as a
  **CHANGE REQUESTED**: the builder should state the `M≥3` (equivalently
  `n≥3`) restriction explicitly in Claim D's statement and note why `M<3`
  is excluded/irrelevant, rather than leaving the boundary unstated.
- The one genuinely open step (stray-block domination, step 6) is honestly
  scoped as unproved with a named candidate mechanism (continuity/exchange
  along a piecewise-linear path) — not a bare label. Acceptable as an open
  gap for a `partial` result.

Verdict: **APPROVE**, with the one CHANGES REQUESTED item above (state the
`M≥3` restriction explicitly in Claim D).

### self-similar-induction-on-n — APPROVE

The strong induction on `ℓ` for Branch II is well-founded (strictly
decreasing `ℓ`, base case `ℓ=1` genuinely vacuous by the stated arithmetic
argument — `sum(C)=2+ε` with `≤2` parts forces `max(C)>1`, contradicting
`c_1<1`, which is correct: with 2 parts summing to `2+ε`, the max is
`≥1+ε/2>1`). The two-step peel-plus-companion-peel identity is exact
(non-lossy), and step 2's claim that `c_1` is provably the max of
`C∪Γ_{ℓ-2}` throughout Branch II's range is a direct consequence of the
window's own definition (`c_1>2^{ℓ-1}-1≥2^{ℓ-2}` for `ℓ≥2`) — checked this
arithmetic myself, it holds. The case split on `max(C')` vs `2^{ℓ-1}` is
exhaustive. Open gaps (boundary behavior as `ε'→0,1`; well-foundedness
double-check) are correctly flagged as open, not hidden. The outline's
explicit warning not to conflate Branch II's closure with the separate
Branch-I.A-restricted window is correct and necessary — the two are
genuinely disjoint residual pieces.

Verdict: **APPROVE**.

### greedy-reduction-geometric — APPROVE

Insertion-Robustness's exchange/telescoping approach explicitly avoids the
already-refuted "single-element `R_1` is worst case" dead end (confirmed
false by 3000-trial counterexample in a prior round) — the outline
correctly reframes the open step as an *additive/telescoped* bound, not a
worst-case-shape claim. The atomic move (Single-Insertion Lemma) is already
certified and reused without re-proof. The one open step (step 3, the
split-vs-single exchange bound) is honestly identified as the sole gap,
with the reduction-to-`m'=1`-base-case induction structure sound (assuming
step 3 holds, telescoping over `m'-1` exchanges is valid induction on
piece count). No circularity found.

Verdict: **APPROVE**.

### universal-halving-adversary — APPROVE (as scoped)

This round's outline is honest and correctly scoped: it explicitly caps
ambition (mechanical generalization of Theorem 11 to any index — a genuine
but cheap corollary of the already-certified Singleton-Interleaving Lemma)
and hands off the actual Existence Theorem closure to the new
`global-lp-vertex-sufficiency` approach, backed by this round's own honest
quantitative finding: survivor rate under unbiased sampling is *growing*
with `n` (1.25-4% at n=4-8 → 8-30% at n=10-15), not shrinking — a real,
data-driven diagnosis that this additive-construction family cannot close
the gap as `n→∞`. This is exactly the right move (per CLAUDE.md's
plateau-break guidance) rather than continuing to add named constructions
that won't scale. The self-critical note about prior undersampled "0/300"
claims being sampling artifacts (not genuine near-closure) is a valuable,
correctly-flagged methodological finding — future numeric claims here must
state sample size/method, as the outline itself now mandates.

Verdict: **APPROVE**.

### global-lp-vertex-sufficiency — APPROVE (new)

**Checked distinctness from `universal-halving-adversary`'s machinery**,
per the dispatch instruction: this is a genuinely different top-level
claim and proof strategy, not a relabeling.
`universal-halving-adversary` proves the Existence Theorem (if at all) by
exhibiting an explicit named construction family and taking best-of; this
approach instead targets a *sufficiency-via-compactness* argument — the
true minimum over ALL cut-patterns and ALL fragment values is `≤c(n)`
everywhere on the simplex, established by (a) piecewise-linearity of
`OddSum` for fixed cut-pattern (LP structure), (b) extreme-point
optimality (a named, correctly-cited standard fact — Fundamental Theorem
of LP), and (c) reducing "for all points, some pattern works" to finitely
many extremal configurations via continuity/compactness. This mirrors how
`lp-duality-split-polytope`'s Theorem A/B closed the *necessity* direction
uniformly in `n`, extended here to the *sufficiency* direction — the same
style of move (existence-over-compact-region) that already worked one
level down, but applied to a different half of the argument
(sufficiency vs necessity) and a different object (the full XY response,
not one fixed family). This satisfies the "diversity of thought" bar: it
is not a variation of universal-halving-adversary's technique, it is a
different mechanism entirely (compactness/LP-duality vs
explicit-construction enumeration).

Steps 1-2 (piecewise-linearity, vertex attainment) are near-immediate
consequences of already-certified lemmas (Vertex Pinning Lemma,
Single-Piece-Split Vertex Lemma) — did not need independent verification,
these are already reviewer-certified. Steps 3-5 (the finite extremal
reduction and its verification) are honestly flagged as the entirely-open
core, with a named open sub-question (can candidate `π` be pruned to a
small dominant family) rather than glossed over. The outline itself
honestly flags the real risk that this could collapse back into needing
exactly the Existence Theorem it's trying to avoid if the vertex-shape
enumeration coincides with best-of-{known constructions} — this is a
legitimate risk disclosure, not a fatal flaw; it should be watched next
round, not blocked now.

**Process note (not fatal, action item for the builder):** no
`results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md` file
exists yet — only the outliner's report describes this approach. Per the
`register_approach` contract the outliner is expected to seed this file;
it did not. The dispatched builder for this slug must create the file
from scratch using this round's outline skeleton as its starting content
(state Status: unsolved, populate Approaches tried / Current best per the
file contract) — flag this so the builder doesn't skip the file-creation
step.

Verdict: **APPROVE** (new approach, registered).

### Diversity check across the field

The field now covers 2 LB approaches (self-similar-induction-on-n,
greedy-reduction-geometric — genuinely different induction mechanisms,
order-statistics/branch dichotomy vs exchange/telescoping) and 3 UB
approaches (lp-duality-split-polytope's peeling/AltSum machinery on the
*necessity* direction; universal-halving-adversary's explicit-construction
family, now explicitly capped; global-lp-vertex-sufficiency's new
compactness/LP-vertex *sufficiency* argument). No single shared wall
across all 5 this round — each has a distinct, precisely-located open
step. The 3 UB approaches all still operate on the same underlying
split-fragment polytope object (flagged as a watch item since round 5),
but this round's addition of an existence/compactness framing (rather than
one more named construction) is exactly the diversification CLAUDE.md
calls for when a family plateaus — not a fourth variation of the same
technique.

### Ranking

Registered `global-lp-vertex-sufficiency` (new, cold-start 1500) via
`register_approach`. Ran `update_ranking` with 6 comparisons spanning the
whole field (anchoring the newcomer against established approaches, not
just against itself):
- lp-duality-split-polytope > universal-halving-adversary (closer to a
  complete theorem — n of n+1 idx cases fully proved, single remaining
  case rigorously isolated and its sub-lemmas independently verified this
  review — vs. universal-halving-adversary's own admission this round that
  its family cannot close the gap).
- lp-duality-split-polytope > self-similar-induction-on-n (narrower,
  better-isolated remaining gap).
- lp-duality-split-polytope > global-lp-vertex-sufficiency (established,
  independently-verified content vs. an all-open new core).
- self-similar-induction-on-n = greedy-reduction-geometric (draw; both
  have comparably-scoped single open steps and comparable recent
  progress).
- universal-halving-adversary > global-lp-vertex-sufficiency (established
  accumulated certified lemmas vs. unproven new core).
- greedy-reduction-geometric > global-lp-vertex-sufficiency (same
  reasoning).

Resulting Elo (post-update): universal-halving-adversary 1666,
greedy-reduction-geometric 1561, lp-duality-split-polytope 1525,
self-similar-induction-on-n 1518, global-lp-vertex-sufficiency 1463.
All `stale` flags cleared.

### Build set

All 5 approaches are live, each with concrete, falsifiable next steps (no
approach is design-stage-only per the round-2/round-3 rule), and they span
genuinely distinct framings/directions per CLAUDE.md's diversity mandate —
consistent with this project's established practice of building the full
live population each round when no approach clearly dominates.

build set: lp-duality-split-polytope, self-similar-induction-on-n, greedy-reduction-geometric, universal-halving-adversary, global-lp-vertex-sufficiency
