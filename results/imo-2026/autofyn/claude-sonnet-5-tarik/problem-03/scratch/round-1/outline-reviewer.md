# Outline review — imo-2026-03, round 1

## Independent verification performed before judging

Before trusting the outliner's numeric claims, I re-derived/re-checked the core facts myself:

- **n=1 hand derivation.** For a 2-piece LB partition {s, 1−s} with 1 point each, I worked
  out XY's best 1-cut response in closed form: if XY splits the larger piece s into (t,s−t)
  with t ≤ s/2, then (i) if the untouched piece r=1−s satisfies r > s−t (i.e. r > s/2), L stays
  exactly s (the two sub-pieces land at odd ranks 1,3); (ii) if r ≤ s/2, XY's optimum is exact
  bisection t=s/2, giving L = s/2 + r. Minimizing s over LB's choice of s in each regime gives a
  maximum exactly at the crossover r = s/2, i.e. **s = 2r**, giving c(1) = s/2+r = 2/3 with
  s=2/3, r=1/3 — exactly the dyadic partition and exactly the "a_1 = 2a_2" case-boundary that
  `dyadic-cascade-induction` Step 4 and `elementary-exchange-smoothing` Step 3 both identify as
  the critical ratio. This is a real, independent confirmation that ratio-2 is the correct
  critical point, not just a numeric coincidence at n=2.
- **n=2 grid re-check.** I wrote a fresh exact-`Fraction` script (not reusing the outliner's),
  searching all 1-cut and 2-cut XY responses (both cuts in one piece, one cut in each of two
  pieces) against {4/7,2/7,1/7} on a fine rational grid (denominator 60 within each piece). Min
  L found = exactly 4/7, matching the target. (Script: `/tmp/check_n2.py`.)

This gives me good confidence that **c(n) = 2^n/(2^{n+1}-1) is the right target** and that the
"pair down to ratio 2 / a_1 vs 2a_2" mechanism used across all four approaches is mathematically
real, not a mirage from a single data point.

I also hand-verified **Lemma G** (greedy-take-max is optimal for both players in an alternating
pick from a common value pool) and **Lemma P** (duplicate-pair invariance) on small examples
(e.g. {5,3,3,1} → removing the pair {3,3} changes L by exactly −3, as claimed). Both are correct
and the mechanisms given are the right ones — not hand-waved despite still needing a written-out
inductive proof.

## Per-approach verdicts

### dyadic-cascade-induction — APPROVE
Whole attempt, both directions targeted end-to-end. Lemma G and Lemma P are correctly stated
with real mechanisms (verified above) — not bare labels. The lower-bound induction (Step 3) has
a genuine self-similarity argument (peeling the top piece of the dyadic sequence reproduces the
rescaled (n−1)-sequence) that I find plausible and specific, not generic. The upper-bound
induction (Step 4) case split at a_1 vs 2a_2 is **exactly the crossover point my n=1 hand
derivation found**, which is strong evidence the case split is the right one, not an arbitrary
guess. The open gap (Case (i): accounting when a_1's internal sub-pieces interleave in rank with
the untouched tail a_2,…,a_k) is real and honestly flagged as "the single biggest gap," not
hidden behind "then it follows." No fatal flaw found. Proceed to build.
Note for builder: also needs the small separate lemma that using fewer than the full n points
never helps either player (flagged as a watch-out item, not yet proved) — don't let this sneak
in as an unstated assumption in the induction.

### elementary-exchange-smoothing — CHANGES REQUESTED
Whole attempt, genuinely different mechanism (local two-piece smoothing directly on LB's
partition rather than an explicit XY counter-strategy). This is the most "elementary" framing on
the table and my independent n=1 computation is essentially a hand-worked instance of exactly
this approach's Step 3 two-sided slope claim (I found the crossover at s=2r explicitly, with L=s
on one side and L=s/2+r on the other — matching the outline's two-regime description). That's a
real, independent data point beyond the n=2-only evidence the outline itself flags as its
weakness, which raises my confidence this line has a real chance. Still, Step 3 (the two-sided
improving-shift lemma) is honestly flagged as "entirely conjectural" beyond n=2, and Step 2's
"locally-constant active pattern" genericity claim is unproved. These are real, load-bearing
gaps — not fatal, but the builder must (a) verify the two-sided slope claim symbolically for a
general 3-piece configuration (not just the n=1/n=2 special cases already checked) before
committing to the full induction, and (b) address the boundary case (fewer than n+1 positive
pieces) which is currently just asserted as "probably easy."

### potential-weighting-upper-bound — CHANGES REQUESTED
Legitimate technique (potential/monovariant), correctly scoped as a hedge on
dyadic-cascade-induction's hardest step, and honest that it's exploratory: the weight sequence is
undetermined and the outline itself flags that "a uniform per-move decrease may not exist as a
single clean bound at all," with an explicit self-imposed 1–2 round abandonment criterion if so.
This is appropriately cautious, not hand-wavy — no fatal flaw, but genuinely underdeveloped
relative to the other three (no candidate weight has even been tested against the n=1,2 exact
values yet). Keep in the population; not selected for this round's build set — the two more
concrete approaches should go first, and this can be picked up once the shared Lemma G/Lemma P
are certified (it needs to import Lemma G) or if the top two stall.

### concavity-minimax-duality — CHANGES REQUESTED (deprioritized, not a RETHINK)
Technique (convex analysis / minimax, Sion's theorem for existence) is legitimate in principle
and not a wrong tool for a game with a compact strategy space, but the outline is honest that it
is the highest-risk entry: Step 3's "finitely many combinatorial response patterns" claim (needed
for g to be a finite infimum of affine functions, hence concave in a usable way) is asserted but
not justified, and Step 4's actual stationarity algebra "is not carried out at all." This is not
circular reasoning or a wrong technique, but it is the least load-bearing of the four — closer to
a research direction than a scoped proof step. I agree with the outliner's own risk flag: keep it
registered (worth revisiting if the case-split and smoothing approaches stall), but do not spend
a build round on it yet since no concrete algebra exists to check.

## Diversity-of-thought note (per CLAUDE.md anti-single-gap-trap)

All four approaches share the same Lemma G reduction (alternating-pick → order-statistic sum)
and target the same conjectured value/construction. This is **not** a fragmentation problem —
each approach still targets the whole problem end-to-end and (once Lemma G is certified) can
import it as a shared lemma rather than re-deriving it — and Lemma G is a nearly-forced, low-risk
reduction (I verified it directly; it is a standard fact, not a risky assumption), so sharing it
does not create a meaningful single-point-of-failure.

The real risk is narrower: **three of the four approaches (concavity-minimax-duality,
elementary-exchange-smoothing, and implicitly potential-weighting-upper-bound) all lean on the
same underlying structural fact** — that XY's optimal response, as a function of LB's partition,
is piecewise-affine/finitely-patterned (only `dyadic-cascade-induction`'s explicit case-split
induction avoids this altogether by construction). If that structural fact turns out false or
much harder than expected, three of the four approaches could stall on the same wall. This is
worth flagging to the orchestrator now: if by round 2–3 both `elementary-exchange-smoothing` and
`concavity-minimax-duality` are stuck on their genericity/finite-pattern claims, that is the
signal the shared wall is real, and the next explorer round should be told to find a route to the
upper bound that does NOT go through characterizing XY's response as finitely-patterned at all
(e.g. a purely inductive/recursive argument in the style of `dyadic-cascade-induction`, or a
direct combinatorial bijection/injection argument) — not just another smoothing variant.

## Minor issues to flag to builders

- `potential-weighting-upper-bound.md` and `concavity-minimax-duality.md` both reference a file
  `majorization-smoothing-general-optimum.md` that does not exist among the four approach files
  in this round — this almost certainly should refer to `elementary-exchange-smoothing.md`. Flag
  to builders so they don't waste time looking for a nonexistent file.
- All four approaches should certify Lemma G and Lemma P once, in `lemmas/greedy-reduction.md`
  and `lemmas/duplicate-pair-invariance.md`, and every other approach should import rather than
  re-derive — this is the correct use of the shared-lemma cache per CLAUDE.md, not a
  fragmentation of the proof.

## Ranking (round 1, cold start)

Registered all four as new approaches (all APPROVE/CHANGES REQUESTED, none RETHINK — no slug
excluded). Ranked head-to-head based on outline concreteness, correctness of stated mechanisms,
and risk, anchored to my independent hand/numeric verification above:

1. dyadic-cascade-induction (Elo 1546) — most concrete, both lemmas verified, case-split boundary
   independently confirmed.
2. elementary-exchange-smoothing (Elo 1517) — genuinely elementary alternate route, crossover
   independently confirmed at n=1, but central lemma still conjectural beyond n=1/n=2.
3. potential-weighting-upper-bound (Elo 1485) — legitimate hedge, but no concrete weight choice
   yet, least developed of the three "concrete" approaches.
4. concavity-minimax-duality (Elo 1453) — highest risk, most abstract, central algebra not
   started.

build set: dyadic-cascade-induction, elementary-exchange-smoothing
