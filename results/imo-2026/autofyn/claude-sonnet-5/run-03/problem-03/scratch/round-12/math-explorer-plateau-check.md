# math-explorer: plateau check + fresh-framing scout (round 12)

## 1. Is the field converging into one LP-vertex-polytope framing?

**Yes — confirmed, not just round 11's hunch.** Traced the lineage explicitly
(`grep` across all approach/lemma files for "Vertex Pinning Lemma",
"Single-/Two-Piece-Split Vertex Lemma"):

- The mechanism originates in the now-**retired** `dyadic-potential-invariant`
  (round 5): the Vertex Pinning Lemma ("an optimal XY response, after
  discarding wasted cuts, sits at a point where enough independent ties/zeros
  are active to pin it down to a finite candidate set").
- It is reused verbatim by `universal-halving-adversary` (retired, round 6,
  Two-Piece-Split Vertex Lemma) and by the two live upper-bound approaches
  `lp-duality-split-polytope` (Single-/Two-Piece-Split Vertex Lemma, used
  every round since round 6) and `global-lp-vertex-sufficiency` (Global
  Vertex Lemma, an explicit assembly of the same three lemmas, round 8+).
- **New this round (round 11), and this is the real signal**:
  `self-similar-induction-on-n` — nominally a *lower-bound*, induction-on-`m`
  approach, structurally the furthest from the upper-bound LP approaches —
  independently re-derived the **identical proof shape** (finite hyperplane
  arrangement → cell-wise-affine functional → vertex-attainment) for its own
  Middle-Regime problem, explicitly citing the resemblance to
  `global-lp-vertex-sufficiency`'s machinery in its own round-11 target
  description ("structurally parallel to ... independently re-derived for a
  different polytope"). It even flags the *same class of gap*
  `global-lp-vertex-sufficiency` found and fixed this round (Rank-Pinning
  Lemma, i.e. within-branch pairwise ties not accounted for) as its own open
  loose end, unfixed (see Section 4 below — this is actionable).
- Even `greedy-reduction-geometric`, the one approach that has stayed purely
  combinatorial (peeling, WLOG reductions, stress-testing) all 11 rounds, was
  this round (Theorem N) proved to reduce to *the same open object*
  (TOP-ONLY(m-1)'s complementary regime) that `self-similar-induction-on-n`'s
  Branch-I.A-restricted window already owns.

So: **3 of 4 live approaches now explicitly use vertex/hyperplane-arrangement
reasoning, and the 4th's remaining open target has been proved equivalent to
one of theirs.** This is a real convergence, not superficial — it is the same
underlying fact (OddSum, restricted to a fixed combinatorial "shape," is
affine, hence its constrained extrema are vertices of a polytope) being
rediscovered independently on four different polytopes (varying-`p`
outer-max space; fixed-`p` split-space; the triangular family's
split-space; the middle-regime split-space one level down). If there is a
single deep reason this technique cannot close the last gaps (both files
flag the same obstruction in different clothes: `global-lp-vertex-sufficiency`
has no bound on `|Σ(n,k)|`, i.e. the candidate-vertex-count, as a function of
`n`; `self-similar-induction-on-n`'s vertex enumeration is admittedly
non-exhaustive for the identical reason, missing ties against individual
`Γ_{m-2}` elements) — then all four approaches share one wall, and CLAUDE.md's
single-gap-trap warning applies with full force. I do not have a proof that
this wall is fatal, but the pattern (four independent rediscoveries of the
same lemma, all stalling on "the vertex list isn't proved exhaustive / has no
n-uniform bound") is the textbook symptom the orchestrator rule is written to
catch.

**Recommendation:** the field should not treat "four approaches" as four
independent shots on goal for the *upper bound* direction (and increasingly
the lower bound too) — for ranking/diversity purposes they are closer to one
approach with four write-ups. Next round should put at least one approach on
the table that does NOT touch vertex/tie/affine-cell reasoning at all.

## 2. Search for a genuinely new top-level framing

Tried three candidates, per the dispatch's "at least 3" instruction.

**(a) Layer-cake / generating-function reframing of the alternating sum.**
Already tried and dead-ended: `layer-cake-parity-reframing` (retired) built
the identity `AltSum(X) = ∫ 1[N_X(t) odd] dt` fully rigorously (this is
exactly the generating-function/threshold-count idea one would otherwise
propose fresh) and then found, by an **exact rigorous counterexample** (not
numeric), that a single cut's marginal effect on parity has opposite sign
depending on what other cuts already exist elsewhere — i.e. the natural
per-cut/per-threshold decomposition this framing would need is provably not
additive. This is a real, previously-paid cost; re-proposing "generating
functions" or "roots-of-unity filter on the alternating sum" without a new
idea for the coupling obstruction would just re-pay it. **Not a fresh lead.**

**(b) Probabilistic / random-adversary averaging argument for the upper
bound.** This one is genuinely untried in the population (all upper-bound
work so far is either an explicit deterministic construction — Top-
Duplication, Multi-Piece Sufficiency — or an LP/vertex existence argument).
The idea: have XY respond with a *randomized* cut-allocation, compute
`E[OddSum]` by linearity, and argue `V(p) ≤ E[OddSum] ≤ c(n)` — turning the
existence problem into an averaging identity instead of a case-by-case
vertex search, i.e. a genuinely different mechanism (`probabilistic-method`
in the KB's combinatorics list; also matches the crux corpus's
`games-and-strategy` cluster's occasional Monte-Carlo-flavored arguments,
e.g. aimo-0766's "hide inside the sensor's tolerance" symmetrization). I
**sanity-checked it numerically before reporting it as a lead**, exactly as
instructed. Tested at the concrete balanced point `p=(0.35,0.34,0.31)`
(`n=2`, already on record elsewhere in the project as a point where the
"top-only" heuristic fails), with 200,000 trials of "assign each of the `n`
cuts to a uniformly random piece, split that piece with i.i.d. uniform
breakpoints":

```
c(2)                                    = 0.571428...
E[OddSum] over naive i.i.d.-uniform cuts = 0.603478...
min OddSum found over the same trials    = 0.505003...
```

**Result: the naive version fails outright** — its expectation (0.603) is
*above* `c(2)` (0.571), not below, so a plain Markov/averaging argument gives
nothing (the true optimal deterministic response, glimpsed by the sample
minimum at 0.505, beats the random-strategy average by a wide margin,
consistent with every other approach's finding that the optimal response is
a highly structured tie/duplicate construction, not a generic one). This
rules out the *literal* naive form. It does **not** rule out a smarter
randomized construction (e.g. randomizing only the fine-tuning parameter of
an already-structured family, such as which subset of tail elements to tie
against, analogous to the certified Generalized Subset-Tie Theorem 12 but
with the tied subset chosen randomly and an expectation computed in closed
form) — that variant was not tested (out of scope for a single-round sanity
check) and is a legitimate, still-open, genuinely different mechanism for a
future round to attempt properly, not a dead end on the same footing as (a).

**(c) A different game-tree / backward-induction framing (attack the
2-phase game via LB's *first* move directly, rather than via the certified
static-multiset reduction).** Investigated whether bypassing the
Greedy-Optimality + position-irrelevance reduction (`lemmas/reduction-to-
multiset-minimax.md`) and instead analyzing the game as an explicit
recursive value function on "remaining stick length + move number" could
open a new attack surface. Concluded this is **not** a new framing in
substance: the certified reduction is an *equivalence* (proved both
directions, no information discarded), so any backward-induction argument on
the raw game is provably identical in content to working with `V(p)` — it
would just re-derive the same minimax, with strictly less structure exposed
(the multiset reduction is strictly more tractable, since it forgets
payoff-irrelevant position information the raw game tree still carries).
**Not a fresh lead**, and I would flag it as a documented dead end so a
future round doesn't re-spend time on it.

**Conclusion for Section 2:** no fully new, ready-to-build top-level
framing was found this round with high confidence. The most promising
genuinely-distinct direction is a *refined* probabilistic/averaging
argument (b) — untried in substance, structurally different from all four
live approaches, and not yet shown to fail (only its naive instantiation
was refuted). I recommend the outliner open it as a new approach slug next
round with an explorer/builder tasked specifically to design the smarter
randomization (structured, not i.i.d. uniform) before attempting a proof,
exactly as this round's numeric check was mandated — do not skip straight to
a written proof attempt on an untested random-construction family.

## 3. (Numerically sanity-checked per instructions — see 2(b) above.)

## 4. Cross-approach transfer for the shared TOP-ONLY(m-1) gap

**Yes — a concrete, actionable transfer exists, and it is not the "new
framing" kind (2(b)) but a direct machinery reuse.** `self-similar-
induction-on-n`'s round-11 Middle-Regime Vertex Reduction Theorem is, by its
own admission, built from scratch in the same shape as
`global-lp-vertex-sufficiency`'s Finite-Cell Affine-Vertex Reduction
Theorem, but it was derived **before** this round's fix to that theorem: it
is missing the exact analog of the **Rank-Pinning Lemma**
(`lemmas/rank-pinning-lemma-and-mass-constraint-theorem.md`), which
`global-lp-vertex-sufficiency` needed this round to close a real gap in its
own vertex-attainment argument (the observation that "which coordinate
occupies which sorted rank" is not automatically pinned by validity/branch-
comparison boundaries alone — you also need *within-shape* pairwise-tie
boundaries in the arrangement, or the affine formula for `f_σ` itself isn't
justified on a cell).

`self-similar-induction-on-n`'s own round-11 write-up flags **exactly this
same gap**, independently, as its honest scope statement: "the vertex
candidate list was generated by inspection/search, not by an exhaustive
proof that these are the ONLY vertices ... which would also need
comparisons against every element of `Γ_{m-2}`, not just the coarse
sum/order/regime constraints." That is word-for-word the Rank-Pinning
Lemma's problem statement, transplanted to the middle-regime's own free
coordinates (`B`'s split fragments and `S`'s split fragments) instead of
`global-lp-vertex-sufficiency`'s `p`-space fragments.

**Concrete recommendation for next round:** dispatch a builder on
`self-similar-induction-on-n` to import the *technique* (not the literal
lemma — the objects differ, as both files' round-11 sections already
correctly note) of the Rank-Pinning Lemma: enlarge its own candidate
functional list with all pairwise differences among a fixed shape's own free
coordinates and `Γ_{m-2}`'s elements, closing the middle-regime vertex
enumeration's exhaustiveness gap the same way. This would not close the
middle regime outright (there would still be no `n`-uniform bound on the
resulting candidate count, the same residual `global-lp-vertex-sufficiency`
has), but it would upgrade the two already-computed instances (`m=3,4,5` for
`(j,c)=(2,1)`) from "vertex found by numerical search, not proved
exhaustive" to "vertex proved to be the *only* candidate," which is real,
citable, non-numerical progress and directly reuses this round's
already-certified sibling work instead of re-deriving it.

I did **not** find a similarly direct transfer for `lp-duality-split-
polytope`'s tooling (Multi-Piece Sufficiency, Top-Duplication) into
TOP-ONLY(m-1): that machinery is upper-bound-direction (construct an XY
response beating `c(n)` at a *fixed* LB partition), while TOP-ONLY(m-1) is
lower-bound-direction (prove *every* XY response to LB's own geometric
partition, restricted to splitting only the top piece, stays `≥ 2^m`) — the
objects are dual (min vs. a bound on min-over-all-responses) and I do not see
a formal bridge beyond the general observation (already made in the field)
that both ultimately live on "OddSum of a structured multiset" and both use
peeling/tie mechanics; no concrete lemma transfers.

## Summary for the orchestrator

- The field's apparent diversity is thinner than "4 approaches" suggests:
  3 of 4 explicitly use vertex/hyperplane-arrangement machinery descended
  from one retired approach's Vertex Pinning Lemma, and the 4th's residual
  gap was proved this round to coincide with one of theirs (Theorem N). This
  matches CLAUDE.md's single-gap-trap pattern closely enough to act on.
- No fully-new, validated top-level framing was found. Layer-cake/generating-
  function reframing and raw-game backward induction are both dead ends
  (one already proved, one newly diagnosed this round). A refined
  probabilistic/randomized-construction framing for the upper bound is
  genuinely untried and not yet refuted (its naive form was, numerically,
  this round) — worth opening as a new slug, with explicit instruction to
  design a *structured* (not i.i.d.) randomization before writing a proof.
- One concrete, low-risk, high-confidence cross-transfer is ready to
  dispatch now: give `self-similar-induction-on-n` the Rank-Pinning-Lemma
  technique (not the lemma itself — the objects differ) to close its own
  admitted vertex-exhaustiveness gap in the Middle-Regime Vertex Reduction
  Theorem.
