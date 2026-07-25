# Outline review — imo-2026-04 (Mulan's Triangle Game), round 1

Note for the record: `problems.jsonl` lists this entry's `difficulty_level` as
`"medium"` (rating 7), not `"hard"` — CLAUDE.md scopes runs to the 39 `hard`
entries. This is an orchestrator-level problem-selection question, not
something the outline can fix; flagging it but reviewing the outline on its
merits since the run is already committed to this problem.

## Sanity check performed before reviewing content

Verified the target characterization ("Mulan wins iff θ=180°/n, n≥2") is not
obviously false with a bounded-depth backward-induction minimax (exact
`Fraction` arithmetic, θ-aware t-grid) in `/tmp/check_mulan.py`:
- θ=60° (n=3, divisor), equilateral start, depth 4: Mulan wins. ✓
- θ=36° (n=5, divisor), scalene (70,60,50) start, depth 5: Mulan wins. ✓
- θ=50° (non-divisor), equilateral start, depth 4: Mulan does NOT win. ✓
- θ=70° (non-divisor, <90°), equilateral start, depth 5: Mulan does NOT win. ✓
The θ=70° case is the important one — it's ≤90° so the θ>90° pigeonhole
defense doesn't apply, yet Mulan still can't force a win in the search,
consistent with the outline's claim that a genuinely new (non-size-based)
Shan-Yu invariant is needed there. This is not a proof, but it clears the
outline of targeting a false statement before four builders spend a round on
it.

Also hand-verified the two claimed anchor mechanisms algebraically (both
check out, no gap):
- **90° lemma**: for the vertex A with both other angles B,C<90°, cutting at
  t=90°−B (valid since 0<90°−B<A, using C<90°) gives child1={B,90°−B,90°}
  and child2={C,90°−C,90°} — both contain 90° exactly. Confirms this is the
  altitude construction, correctly derived, not just asserted.
- **Shave lemma**: cutting vertex X (angle X>θ) at t=θ gives child1=
  {Y,θ,180°−Y−θ} (always contains θ by construction — t IS one angle of
  child1) and child2={Z,X−θ,Y+θ}. Since the game checks for angle=θ *before*
  the next move, Shan-Yu is genuinely forced to discard child1 (keeping it
  is an immediate loss) — this is a real forced move, not hand-waved.

## Per-approach verdicts

### shave-and-halve-forcing — CHANGES REQUESTED
Sound technique, most concretely developed of the four. The Shave and
Bisection lemmas are proven mechanisms (verified above), not bare labels —
each has an explicit algebraic reason. Issues to close, not fatal:
- Step 2 (the induction driving an arbitrary triangle to all-integer-
  multiples-of-θ form) is described narratively but the interaction between
  simultaneously reducing multiple slots (each shave perturbs a "recipient"
  slot) is not yet nailed into a clean monovariant/induction — the outline
  itself flags this as open, correctly, rather than claiming it's done. Not
  circular, just incomplete; builder should locate an explicit monovariant
  (e.g. Σ⌊angle/θ⌋ or number of non-multiple slots) before writing prose.
- The "only if" θ≤90° non-divisor direction has only an obstruction to one
  Mulan algorithm (Shave-based), honestly labeled as insufficient for a
  universal Shan-Yu strategy. This is the correctly-identified hard core of
  the whole problem — not a flaw in the outline, just unfinished work.
No missing cases, no circularity, no wrong technique. Approve for building
with the two open gaps explicitly assigned to the builder.

### mod-theta-invariant — CHANGES REQUESTED
Genuinely different top-level framing (classical invariant/monovariant vs.
explicit algorithm) even though it imports the same cut formulas and the
θ>90° defense (legitimate — that defense is already fully proved and cited
as shared infrastructure, not smuggled as an unproven gap). The residue-sum
invariant ρ(A)+ρ(B)+ρ(C)≡180 (mod θ) is trivial and correctly labeled
trivial. The load-bearing new claim — a "distance-to-nearest-multiple"
invariant Shan-Yu can maintain — is explicitly marked open/conjectural, not
asserted as proved; good discipline. One thing to push the builder on: the
outline itself flags the subtlety that "δ→0 but never exactly 0" needs an
argument ruling out non-monotone attacks reaching exactly 0 despite average
shrinkage — make sure the builder doesn't wave this away with "clearly."
No missing cases, no circularity.

### ngon-arc-reduction — CHANGES REQUESTED
The most structurally distinct approach — reduces to a genuinely discrete
finite game (compositions of n into 3 parts) rather than working with real
angles directly. Correctly and explicitly refuses to reuse crux `aimo-0225`'s
actual proof/mechanics, treating it only as a "reduce-to-normal-form-then-
recurse" template to be reproved from scratch — this is the right way to use
the crux corpus per CLAUDE.md (a hint to adapt, not a citation). The
"discrete n-gon divider game is a Mulan win for all n≥2" claim is correctly
flagged as wholly open, new content, with the sensible instruction to work
n=2..5 by hand first rather than jumping to a general induction. The "no
closing necklace" argument for the only-if direction is only sketched — flag
to the builder that it must either be made fully rigorous or shown to
literally reduce to the residue argument (the outline already suggests this
cross-check, good). No missing cases, no circularity.

### maximal-safe-set-fixedpoint — CHANGES REQUESTED
Legitimate different framing (safety-game fixed point vs. explicit strategy
construction); the well-definedness argument (Knaster–Tarski on a power set,
valid for any complete lattice including a continuum) is standard and
correctly caveated — the outline explicitly warns the builder to keep
finiteness claims grounded in the Wₖ="win in ≤k moves" increasing union
rather than an abstract fixed point, which is the right thing to watch for
in a continuum-state game. The θ=180/n direction's "descent-to-contradiction
via a monovariant on Shave-forced membership in S" is a real new idea but
the monovariant itself is unnamed/unproved — flagged as open, correctly.
Weakest of the four in terms of concrete progress toward new content (it
repackages proved facts and proposes, but does not yet advance, new
mechanism), which is reflected in giving it the lowest initial rating below
— but the framing itself is not unsound and is worth keeping in the
population as a genuinely different route.

## Diversity assessment

All four target the full characterization end-to-end (both directions), not
fragments of one proof — none is a sub-lemma masquerading as a rival
approach, so no RETHINK-for-fragmentation issue. They differ in real
top-level framing: explicit forced algorithm / classical invariant-potential
/ discrete combinatorial reduction / formal safety-game fixed point. Sharing
the four already-proven anchor lemmas (90° lemma, Bisection lemma, θ>90°
defense, Shave lemma) across all four is legitimate reuse of established
infrastructure, not the "single-gap trap" — these are fully proved, not
open gaps being hidden behind a shared label.

The real risk to flag for the orchestrator: **three of the four
(shave-and-halve-forcing's gap (b), mod-theta-invariant's central gap, and
maximal-safe-set-fixedpoint's step 4) all reduce to the same unproved hard
fact** — a universal Shan-Yu defense for θ≤90°, θ≠180/n, valid against every
Mulan strategy, not just one algorithm. If all three stall on this exact
wall for multiple rounds, that is the signal to invoke CLAUDE.md's
"break a shared-gap plateau" guidance next round: push a genuinely different
framing at that specific sub-problem (ngon-arc-reduction's discrete
"closing necklace" idea is the best candidate already on the table, since it
doesn't reduce to the same residue computation by construction — worth
prioritizing builder effort there if a plateau appears). This is not a
reason to cut any approach now — round 1, no signal yet — but it is the
thing to watch in round 2's ranking.

No dead ends from `current.md` are being repeated (file is empty/fresh).
No small-case contradiction found (see sanity check above).

## Ranking

No prior population existed (fresh problem, all four newly registered at
cold-start Elo 1500). Ranked by my own assessment of mechanism maturity and
promise, per dispatch instructions: shave-and-halve-forcing rated highest
(most concrete, already-proven forcing mechanism with the clearest path to
completing the "if" direction), mod-theta-invariant and ngon-arc-reduction
next (comparable maturity, genuinely different framings, drawn against each
other), maximal-safe-set-fixedpoint lowest (soundest framing on paper but
least concrete new mechanism content so far — mostly repackaging proved
facts plus one unnamed monovariant).

Resulting Elo after `update_ranking`: shave-and-halve-forcing 1531,
mod-theta-invariant 1512, ngon-arc-reduction 1503, maximal-safe-set-
fixedpoint 1453.

## Build set

Round 1, no prior population, all four approaches are sound (right
technique, no circularity, no missing cases, gaps honestly flagged rather
than hand-waved) and genuinely diverge in framing — build all four in
parallel this round to get real comparative signal on which framing cracks
the shared hard core (or the θ=180/n induction) fastest, per the
orchestrator's round-1 broad-population guidance.

build set: shave-and-halve-forcing, mod-theta-invariant, ngon-arc-reduction, maximal-safe-set-fixedpoint
