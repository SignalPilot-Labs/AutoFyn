# Outline review — round 16 (imo-2026-03)

Reviewed `/tmp/round-16/proof-outliner.md` against the live approach files
`results/imo-2026-03/approaches/greedy-halving-adversary.md`,
`results/imo-2026-03/approaches/lp-duality-certificate.md`, and
`current.md`. No new approaches proposed this round (correct call — both
fronts have concrete, non-exhausted next steps, so the shared-gap-plateau
"open a new framing" rule is not triggered).

## Front 1 — `greedy-halving-adversary`: APPROVED, no changes required

Checked Proposition 30 (lines ~2955–3044 of the approach file) directly
against the outline's summary: the outline's "Target Q" (bound
$A(R'_{>v})$ for $R'$ an arbitrary legal $(n-2)$-ladder response, $v$
arbitrary) is exactly what Proposition 30's proof isolates — verified
by hand that the outline did not silently sharpen or misstate the
open item. The consistency check against Proposition 24 ($v\ge s$ reduces
correctly) is a real cross-check, not an assertion.

The proposed mechanism (transplant `vertex-minimum-theorem`'s
LP-vertex argument to the truncated functional $S\mapsto A(S_{>v})$) is
**correctly flagged as needing new work, not cited as an automatic
transfer** — this is exactly the round-7-failure-mode check the
orchestrator asked for, and it passes: the outline explicitly says
"New work required, not a citation" and spells out the open question
(does truncation at $v$ introduce a non-convex kink, i.e. do the
existing tie-hyperplanes plus new "fragment $=v$" hyperplanes still give
a piecewise-affine functional). I checked this myself against the
certified `vertex-minimum-theorem` statement (which is proved for $\Phi$
of the *whole* sorted multiset, no truncation): on any cell of the joint
refinement (original tie hyperplanes ∪ new "$=v$" hyperplanes), the
membership set $R'_{>v}$ and the internal sort order of its elements are
both locally constant, so $A(S_{>v})$ is a fixed signed sum of a fixed
coordinate subset there — i.e. affine on the cell, hence the same
convex-polytope vertex argument plausibly goes through. This is a
genuine, non-trivial (a new hyperplane family, a new evaluation via
`odd-run-reduction-lemma`), plausible-but-unverified extension — correctly
scoped as "first thing to nail down" rather than assumed.

Dead ends: all four listed (max-domination-lemma alone; triangle-bound +
max-domination combined; ratio-2-spacing-lemma/last-element-bound
transfer; peel-by-$\ell(S)$/whole-mass/carry/pairing family) match
`current.md`'s own permanent-dead-end record and Proposition 30's own
"why the remaining piece is genuinely hard" computation — none are
silently reintroduced; the explicit non-goals (candidate (b) deferred,
candidate (c) excluded) are correctly carried over from the round-16
truncation-bound explorer's report.

**Verdict: build as scoped.**

## Front 2 — `lp-duality-certificate`: APPROVED with one required addition to Task 2

Task 1 (sign-bug fix) and Task 3 (fallback small-$n$ vertex enumeration)
are both sound, low-risk, and correctly scoped (Task 1 explicitly
disclaims coverage gains; Task 3 is explicitly gated as a fallback only).

**Task 2 needs a mandatory reconciliation step added before the builder
spends effort on the numeric diagnostic.** I traced the two already-certified
round-14 negative lemmas (`peel-zero-slack-dead-end`,
`bisect-containment-dead-end`, in `lemmas/` and the approach file's
R14.2) in detail, since Task 2's mechanism ("peel or bisect $p_1$,
recurse, and ask whether the recursed image lands in case (a)/(b1) one
level down") is built from the *same two primitives* (Theorem
B$_k$/one-step-peel and Theorem C′/bisect) that R14.2 already analyzed.
R14.2 proves, algebraically and with **zero slack**, that substituting
the level-$(n-1)$ ceiling bound $a_{n-1}T'$ (the value that case (a) or
case (b1) actually establish — not a cruder surrogate) into either
recursive identity certifies $\Phi\le a_nT$ **if and only if** the
*top-level* marking already satisfies case (a)'s own condition
($p_2\ge a_nT/2$ for peel, $p_1\ge a_nT$ for bisect) — i.e. this exact
substitution supplies **zero coverage of case (b1) or (b2)**, regardless
of which case the recursed sub-instance itself falls into, because case
(a)/(b1)'s proven bound for the sub-instance is the *same* ceiling value
$a_{n-1}T'$ used in R14.2's worst-case computation (case (a)'s own
extremal witness is what makes that ceiling tight in the first place).
On a first-principles read, this looks like it could make Task 2's
"generic escape" outcome vacuous even if numerically confirmed: knowing
the recursed image lands in a *solved* case one level down does not by
itself supply anything tighter than the $a_{n-1}T'$ ceiling R14.2 already
plugged in and found insufficient.

However, this is **not** a case of the outline silently reintroducing a
dead end — the file's own round-13/14 authors explicitly flagged "sharpen
case (a)'s conditioning so case (b2)'s recursive sub-instances land in
case (a)/(b1) one level down" as a *distinct*, not-yet-attempted
direction in three places (R13.4, and twice in "Open gaps"), each time
naming it separately from R14.2's dead mechanisms — so there is an
on-file basis for treating it as different in kind (e.g. it may only
need to work for the *specific* joint distribution of $(p_1,p_2,p_3,T)$
that a case-(b2) marking's recursion actually produces, not the
worst-case tail R14.2's universal quantifier covers). I could not fully
resolve this tension from the files alone, and getting it wrong either
way wastes a round: treating it as dead when it isn't loses real
progress; treating it as live when the zero-slack lemma already forecloses
it wastes the round's whole build budget on a numeric diagnostic whose
answer wouldn't matter.

**Required addition to Task 2 (cheap, do this first, before the numeric
diagnostic):** the builder must show, in one short algebraic paragraph,
either (a) why "recursed image lands in case (a)/(b1)" supplies a bound
on $\Phi_{\min}(S')$ *strictly below* the $a_{n-1}T'$ ceiling that R14.2
already ruled insufficient for any case-(b1)/(b2) top-level marking, or
(b) an honest concession that it does not, in which case Task 2 collapses
to R14.2's already-dead mechanism and the round should immediately pivot
its primary effort to Task 3 (or a genuinely different recursive
quantity, e.g. tracking the *joint* feasible region of
$(p_1,p_2,p_3,T)$ rather than a single ceiling substitution). Only after
this reconciliation should the numeric diagnostic (case-(b2) markings at
$n=4,5$, does the recursed image escape) be run — otherwise a "generic
escape" numeric finding risks being reported as progress when it is
mathematically inert.

**Verdict: build, with Task 2 gated on the reconciliation check above.**

## Ranking

Updated via `mcp__approach-ranker__update_ranking` (clears `stale` on the
two active fronts, reflecting round 15's outcomes): `rank-pigeonhole-budget`
beats both active fronts (already-certified milestone, Claim (A) fully
closed, static this round); `greedy-halving-adversary` and
`lp-duality-certificate` scored as a draw — both made comparable,
real, honestly-scoped round-15 progress (Prop 30's exact reduction /
Target-B diagnosis vs. the sign-bug diagnosis + confirmed b2-witness
closures), neither closing its target. New Elo:
`rank-pigeonhole-budget` 1729.4, `greedy-halving-adversary` 1588.8,
`lp-duality-certificate` 1583.7 (all no longer stale). No other
approaches touched — they are dormant/dead-end and not part of this
round's build set.

## Build set

Both fronts are live, non-exhausted, and pass this round's checks (Front 1
clean; Front 2 clean modulo the mandatory Task 2 reconciliation step
above, which the builder should treat as step 0 of its work).

build set: greedy-halving-adversary, lp-duality-certificate
