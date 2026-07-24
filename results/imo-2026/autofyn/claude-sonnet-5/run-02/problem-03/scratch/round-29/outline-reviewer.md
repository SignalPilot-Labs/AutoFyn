# Outline review — round 29, imo-2026-03

Reviewed against `results/imo-2026-03/current.md` (round-28 state: all 3
fronts partial, no overclaims found last round), the three live approach
files' most recent sections, and the cited certified lemma files. All
three revised outlines target the SAME three long-standing fronts as
round 28 (h(m) q1-cut branch / greedy-halving-adversary; (star_3) residual
6 shapes / rank-pigeonhole-budget; n=4 upper bound / lp-duality-certificate)
— this is legitimate continued narrowing, not a shared-gap plateau (each
front is at a different, independently-diagnosed obstruction), so no new
framing is demanded this round.

## 1. rank-pigeonhole-budget — single-insert-point breakpoint sweep for (star_3)'s 6 residual shapes

**Verdict: CHANGES REQUESTED.**

The overall plan (peel every unconditionally-dominant piece via
`sharp-dominant-removal-identity`, then reduce the 2-3 remaining free
coordinates per shape to a finite breakpoint list, then evaluate exactly
via `odd-run-reduction-lemma`) is methodologically sound in spirit and
correctly declines to claim a "uniform" argument — it commits to checking
all 6 shapes individually, which is the right level of rigor here.

**Concrete gap found (verified numerically, not just suspected):** the
outline's Key Lemma — "Nested single-variable breakpoint reduction" —
proposes applying the certified `single-insert-point-vertex-lemma`
"one free coordinate at a time" to reduce shapes like (2,0,1,0), where the
free coordinates are **f1, f2 coupled by mass conservation** (f3 =
p1−f1−f2, a *shared* two-variable constraint, not an independent box) plus
g1 (a genuinely independent box coordinate). `single-insert-point-vertex-
lemma` is proved *only* for a single coordinate `b` inserted into a
**fixed** rest `T` (slope exactly ±1 on each sub-interval, per its own
proof). I tested this directly: freezing f1 and varying f2 with f3 = C−f2
(a fixed-sum pair, exactly the (2,0,1,0)-shape situation) gives A as a
function of f2 with **slope ±2, not ±1** (confirmed by exact-Fraction
sampling — see script output below), because both f2 (rising) and f3
(falling by the same amount) contribute to the alternating sum with
reinforcing signs. This is a different function than the one
`single-insert-point-vertex-lemma` proves anything about; citing it
verbatim for f1,f2 is a mismatch (the same "cites a lemma vs. the lemma
actually proves this new claim" trap flagged in prior rounds, e.g. Rule
#24 in `/tmp/memory/outline-reviewer.md`).

```
f1 fixed; f2 in [0,C], f3=C-f2; rest fixed:
f2=0.5 -> A=2.7; f2=1.5 -> A=1.3 (slope between: -2 per unit)
f2=2.0 -> A=0.3 -> f2=2.5 -> A=1.3 (slope +2)
```

The qualitative *conclusion* (minimum over the coupled pair still occurs
only at an endpoint or a rank-crossing/tie breakpoint, since the function
is still piecewise-affine with nonzero slope on each sub-interval) is
plausible and likely provable, but it is **not** what
`single-insert-point-vertex-lemma` establishes as written, and the outline
does not flag this — it treats the lemma as directly reusable for f1,f2
jointly. The already-certified, more general `vertex-minimum-theorem`
*does* correctly handle exactly this situation (an arbitrary polytope/
simplex of coupled free coordinates, not just an independent box) — the
builder should either (a) invoke `vertex-minimum-theorem` directly for any
coordinate-group that shares a mass-conservation constraint (f1,f2 here),
reserving `single-insert-point-vertex-lemma` only for genuinely independent
box coordinates like g1, or (b) prove a coupled-pair variant of the
insert-lemma from scratch (slope ±2, breakpoints at the pair's own box
ends {0,C} or ties to existing values) before using it. Either fix is
cheap and does not change the overall plan's viability.

Everything else in the outline (case coverage — all 6 shapes explicitly
listed; the backup Iterated Insert-Element Identity mechanism; the
"watch out" about the numeric boundary-only attainment) is sound and
should proceed unchanged. Build with the above caveat made explicit to
the builder.

## 2. greedy-halving-adversary — h(m) Anchor-Switching Lemma trichotomy

**Verdict: CHANGES REQUESTED.**

The core algebra is correct and I independently verified it: for the unit
m-ladder (q1=2q2), x<q1/2 ⟹ q1−x>q2=max(tail) strictly (elementary,
confirmed). `general-anchored-tie-bound` (Lemma A, round-28 certified)
requires only w>max(X) — not the stronger w>Total(X) — so it is the
correct tool to cite here, and I ran a fresh 400×800-point exact-Fraction
grid search on the m=3 unit-scaled ladder (q=(8,4,2,1), tail untouched,
single cut on q1) confirming A never drops below the target 1 in this
sub-case (min found ≈1.01, matching the claimed closure), consistent with
—not proof of, but not contradicting — the outline's claim.

**Gap:** Lemma A's hypothesis requires t* to be an **already-existing
element of X** (you're bounding the effect of inserting *one more copy* of
a value already present). In the outline's branch (a) ("Lemma A applies
with anchor w=q1−x… for the appropriate t* via Lemma A's statement"), `c`
is described as "the free coordinate" ranging over a continuum — Lemma A
does *not* apply to an arbitrary c unless c is first shown to be pinned,
at the extremal configuration, to one of the values already in X (x, or a
tail element). The approach file's own earlier "Well-posedness" discussion
(§ h(m) definition) *does* establish this pinning via `vertex-minimum-
theorem` (c=0, or c tied to another fragment, at the true minimizer) — so
the mechanism is available — but the outline's step 2 does not explicitly
invoke it before applying Lemma A, leaving "for the appropriate t*" as an
unjustified hand-off. Additionally, two boundary sub-cases are not
addressed by Lemma A at all and need separate (easy) treatment: **c=0**
(trivial — A unchanged, reduces to `sharp-dominant-removal-identity`
directly) and **c=w=q1−x** (a tie between c and the anchor itself, not "an
element of X" — a direct two-element-tie computation via
`odd-run-reduction-lemma`, not Lemma A verbatim) and similarly **c=q1**
(the other box endpoint). None of these are hard, but the outline must
name them as explicit sub-cases rather than leaving the reader to assume
Lemma A "just works" for all c in each half of the trichotomy.

Everything else (the trichotomy itself c≤q1−x vs c>q1−x is exhaustive
given the boundary x=q1/2 handled separately; the honest scoping of
"simultaneous cuts on q1 and tail, m≥3" as still open; the "watch out"
against reviving the single fixed-ratio anchor) is sound. Build with the
instruction to (i) explicitly cite the vertex-pinning argument before
invoking Lemma A with t*=c, and (ii) enumerate c=0, c=w, c=q1 as separate
mini-cases.

## 3. lp-duality-certificate — n=4 free-transplant sequencing + bisect-subset-lemma coverage check

**Verdict: APPROVE.**

This is the most conservative and best-scoped of the three outlines: steps
1(i)-(iii) are pure instantiation of already-general-n certified lemmas
(`unconditional-p2-threshold-closure`, `generalized-peel-identity`/Theorem
B_k combined with round-27's fully-closed n=3 c(3)≤8/15 result, and
round-28's own `p1-geq-half-closure-n4`) — no new proof content, and I
independently checked the threshold arithmetic: a4=2^4/(2^5−1)=16/31,
a4·T/2=8T/31, T/D_4=T/31, matching the outline's stated thresholds exactly.
Step 2 correctly restates the genuinely-open residual as the *intersection*
p1<T/2 AND T/31<p2<8T/31 — a real narrowing versus "all of p1<T/2," and
consistent with round 26/28's own residual-tracking discipline (a pattern
this project has gotten wrong before, e.g. Rule about the p1≥T/2/T/15<p2<
4T/15 n=3 residual — here it is stated correctly by analogy).

Step 4 (measure numeric coverage of the residual box by the 30
Bisect-Subset chambers **before** hand-deriving new chamber types) mirrors
the round-24 methodology that worked well for n=3, and is explicitly
labeled as a coverage *measurement*, not a proof — the outline does not
overclaim numeric coverage as closure, satisfying the project's repeated
lesson (rounds 24-26) about not trusting sampling as proof. Step 5's
expectation that the n=3 chamber count will not transplant 1:1 (an
explicit non-assumption, flagged from the 28%→64% density-growth signal)
is appropriately cautious.

No fatal or fixable gap found. Approve as-is.

## Diversity check

The three fronts remain genuinely different sub-problems of the overall
lower/upper bound decomposition (Claim B's h(m) q1-cut residual; Claim A's
(star_3) residual shapes; the general upper bound's n=4 chamber census) —
not three variations of one framing. No shared-gap-plateau signal this
round; each front has its own, independently-diagnosed obstruction and
made distinct genuine progress last round with no overclaim. Continuing
to advance all three in place (no new slug, no RETHINK) is appropriate.

## Ranking

All three slugs are established population members (built and ranked
every round since round 6/19/24 respectively); no new slugs to register
this round. Comparing the current field: `rank-pigeonhole-budget` and
`greedy-halving-adversary` are past-verified serial contributors with
`lp-duality-certificate` slightly ahead on approve-cleanliness this round
(zero-gap outline vs. two fixable-but-real gaps caught in the siblings).
Anchoring to round-28 outcomes (all 3 CHANGES REQUESTED, no dead-ends) and
this round's outline quality:

- lp-duality-certificate: cleanest outline, zero gaps found — treat as
  slightly ahead this round.
- rank-pigeonhole-budget vs greedy-halving-adversary: both have one
  concrete, fixable, non-fatal citation-mismatch gap caught before build;
  roughly even.

```
update_ranking(imo-2026-03, comparisons=[
  {"winner": "lp-duality-certificate", "loser": "rank-pigeonhole-budget"},
  {"winner": "lp-duality-certificate", "loser": "greedy-halving-adversary"},
  {"winner": "rank-pigeonhole-budget", "loser": "greedy-halving-adversary", "draw": true}
])
```

build set: rank-pigeonhole-budget, greedy-halving-adversary, lp-duality-certificate
