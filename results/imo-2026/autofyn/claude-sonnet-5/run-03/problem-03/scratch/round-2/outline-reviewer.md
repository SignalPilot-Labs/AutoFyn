## imo-2026-03 — outline review, round 2

All four approaches share the certified reduction and greedy-optimality
lemma; the outliner's revisions correctly stay inside that reduction (the
freshframing explorer confirmed it's forced by the problem's rules, not a
technique choice) and each attacks one of the two remaining shared gaps
(lower-bound Case 2 / general upper bound), with one speculative fourth
line. Reviewed all four; verdicts below.

### greedy-reduction-geometric — CHANGES REQUESTED (build)

Technique (exchange argument to reduce "any cut allocation" to "all cuts
on r_n," then piecewise-linear/tie-block analysis of that reduced problem)
is sound and well-matched to the numerics. I independently re-ran the
exchange claim in Python (moving cuts off the top piece r_n onto lower
pieces): at n=3, all-cuts-on-top gives exactly c(3)=8/15=0.5333, and every
tested reallocation of one or more cuts to lower pieces strictly increases
OddSum (0.590, 0.622, 0.756) — confirms the Exchange Lemma's claimed
direction and consequence numerically, consistent with the lowerbound
explorer's point 2.

Issues:
- Step 1 (Exchange Lemma) is honestly flagged as "not yet proven, only
  motivated" — acceptable at outline stage since it's an explicit open
  gap, not asserted as done, but the mechanism sketch ("a cut on r_i only
  perturbs ranks strictly below r_n's own rank") needs the Peeling Lemma
  applied carefully; when r_n's own split interleaves with r_i's split
  fragments, ranks below r_n's rank in the ORIGINAL sort can still cross
  above r_n's split fragments after both are refined — the outline should
  make the builder verify this interleaving explicitly, not just assert
  "only perturbs ranks below."
- Step 3's induction ("all other breakpoint faces reduce ... to an
  (n-1)-level instance") is the crux and is correctly flagged as needing
  the reduction "made precise at every face, not just the two extremes" —
  good, this is exactly right given the explorer found a whole plateau of
  extremal allocations, not an isolated point. Builder must not shortcut
  this to "check the two endpoints."
- No circular reasoning found; no repeated dead end (does not retry
  convexity/aggregate shortcuts, correctly flagged as refuted).

### self-similar-induction-on-n — CHANGES REQUESTED (build)

Technique (peeling recursion + two-sided induction) is a genuine and
valuable discovery this round: recognizing that a one-sided lower-bound
induction is structurally insufficient (needs an upper bound on the
peeled remainder to lower-bound EvenSum) correctly diagnoses why round 1
stalled at j>=2 rather than papering over it.

Issues:
- Step 1 (closing the j=1 tie via the certified generalized Tie-neutrality
  block lemma) is a correct, mechanical application — approve as written.
- Step 3's two-sided induction is entirely open, and I want to flag a risk
  the outline doesn't fully call out: the required upper bound U(m') on
  the peeled remainder is, in the worst case, exactly as hard as
  `universal-halving-adversary`'s general upper-bound gap (an upper bound
  on OddSum of an arbitrary sub-multiset). If the remainder after peeling
  turns out to be an *arbitrary* multiset rather than one with forced
  geometric-like structure, this approach silently becomes "prove the
  general upper bound as a sub-step," duplicating universal-halving-
  adversary's work under a different name — not a single-gap-trap
  violation (it's a different route: recursive peeling vs. recursive
  matching) but the builder must verify the remainder retains enough
  structure (e.g., a known ratio to the tail's own geometric shape) to
  make U(m') tractable, or else explicitly report the collapse per the
  outline's own instruction in "Open gaps."
- Correctly grounds base cases (j=0 proved, n=0,1 proved).

### universal-halving-adversary — CHANGES REQUESTED (build)

Technique (recursive tie-matching generalizing duplicate-the-rest, backed
by a surrogate-adversary fallback from crux aimo-0560) is well-targeted
at the real gap and grounded in this round's numeric finding (regime-
dependent optimal cut allocation: attack the outlier top piece vs. attack
a small piece to complete ties).

Issues:
- Step 1 (pruning lemma: LB always uses full budget k=n+1) is flagged as
  unproven "despite being obviously true numerically" — correctly not
  taken on faith; cheap and should be tractable, good to front-load.
- Step 2's exact target value for each cut is explicitly marked "the open
  design parameter" — this is honest but means the real content of the
  approach is still undesigned. The outline correctly requires it be
  numerically stress-tested against the known counterexamples
  ((0.5,0.3,0.2) at n=2, (0.45,0.45,0.1)) *before* being written up as a
  lemma — good discipline, keep this requirement.
- Step 4 (surrogate-adversary backup) is appropriately deprioritized
  ("only if step 2-3 stalls") — fine as documented fallback, not a
  distraction this round.
- Correctly avoids retrying "look only at p1" (twice-refuted).

### dyadic-potential-invariant — CHANGES REQUESTED, NOT in build set this round

The outliner itself already demoted this to "lowest-priority... drop for
good next round if it produces no concrete inequality," and I agree with
that assessment but go further: the revised target (minimax-duality
certificate) has literally zero concrete content yet — step 2 (the
coupling/majorization inequality) is "entirely unproven... no candidate
inequality has been written down or numerically checked," and step 3 is
explicitly "not new work," just re-deriving what's already proved. This
is design-stage exploration, not an outline a builder can make progress
against this round. Given CLAUDE.md's build-set guidance ("the few
strongest, normally 1-3") and that the other three approaches have
concrete, partially-verified mechanisms with well-defined next steps, I'm
holding this one out of the active build set to concentrate builder
effort on the three approaches with real traction. It stays registered in
the population (Elo intact) and can be revived if a future round produces
an actual candidate inequality — per the outliner's own instruction, if
it produces nothing concrete this round it should not survive further.
No new registration needed (already in population from round 1).

### Diversity assessment

The three active approaches attack different sub-gaps with different
mechanisms (exchange + piecewise-linear tie-block analysis; peeling +
two-sided induction; recursive tie-matching + surrogate adversary), which
is appropriate diversity *within* the forced reduction — the freshframing
explorer's investigation this round confirms no genuinely gap-avoiding
framing exists, so continuing to diversify *inside* the reduction (rather
than searching for an escape from it) is the right call, not a plateau
symptom. Flag for the orchestrator: self-similar-induction-on-n's step 3
risk (noted above) means two of the three approaches could converge onto
"prove a general OddSum upper bound" as a hidden shared sub-gap — if both
report that collapse next round, that is the real signal to invest in a
structurally different upper-bound technique (e.g., develop the surrogate-
adversary backup in universal-halving-adversary, or revisit dyadic-
potential-invariant's certificate idea with real content).

### Ranking

Ranked via `update_ranking` (evidence-anchored): all three active
approaches beat dyadic-potential-invariant (no concrete content yet, vs.
each of the three having reviewer-certified rigorous partial progress).
Within the active three: greedy-reduction-geometric and self-similar-
induction-on-n drawn (both have a rigorous core plus one well-diagnosed
remaining sub-gap); universal-halving-adversary ranked slightly below
self-similar-induction-on-n (its remaining gap — an entirely undesigned
recursive rule — is currently less concretely specified than self-
similar's precisely-stated two-sided-induction requirement), though it
beats dyadic-potential-invariant clearly. Resulting Elo order (highest
first): greedy-reduction-geometric (1542), self-similar-induction-on-n
(1525), universal-halving-adversary (1518), dyadic-potential-invariant
(1415).

build set: greedy-reduction-geometric, self-similar-induction-on-n, universal-halving-adversary
