# Outline review — round 19, imo-2026-03

## greedy-halving-adversary: revise — APPROVE (with one required fix before build)

Target: close the residual middle band `v2 ∈ (p2-v1, s)`, `v1 ∈ (s,p2)` of
Claim B's `ℓ(F)=2` sub-case (b) — the single bottleneck identified over 4+
rounds.

**Cut-budget correction (step 1) — verified sound, not just plausible.**
I independently traced the mass/cut accounting: producing `F = {v1,v2}∪P`
with `P` an exactly-paired, ≥2-element family from splitting `p1` requires
≥3 cuts (1 to split off `v1`, ≥2 more to carve the remainder into `v2` plus
at least one matched pair) — so with a total Xiang-Yu budget of `n`, at
most `n-3` cuts remain for `R'` (the tail refinement), not `n-2` as
Theorem 34's stated hypothesis (line 3561-3564 of the approach file) uses.
This is a real bug, not cosmetic: the round-19 explorer's counterexample
(`n=3`, `R'` using exactly 1 cut — i.e. exactly the old `n-2=1` cap —
gives `A(F∪G')≈0.0061 < f(3)=1/15`) is a genuine violation of Theorem 34
*as literally stated*, because that configuration actually costs 4 cuts
total (1+2+1) against a budget of only 3 — the old cap silently allowed an
illegal `R'`. The proposed fix (`≤n-3`) is strictly tighter than what
Theorem 34's proof already uses (invoking IH at level `n-2`, which only
needs `R'` to have `≤n-2` cuts — a weaker, still-satisfied requirement),
so tightening the cap does not invalidate anything already proved; it only
removes the illegal configurations that broke the naive `n-2` framing.
**Verdict: this correction is mechanically sound and must be applied before
any further build on Theorem 34 or the middle band — do not let the
builder skip straight to step 3 without first re-deriving Theorem 34 under
the correct cap as step 1/2 require.**

**Δ(n,v) vertex-enumeration mechanism (steps 3-6)** is honestly scoped as
the genuinely new, unproved content ("Open gaps" is explicit about this).
It correctly avoids retrying the two confirmed-dead mechanisms for this
band (per-cut value-charging, LP-floor-as-extra-constraint) and instead
proposes direct vertex evaluation via already-certified machinery
(Vertex-Minimum Theorem, Odd-Run-Reduction Lemma) restricted to the
tighter `n-3`-cut vertex family — a real mechanism change, not a
relabeling. The self-similarity rescaling claim (step 4, citing
`tail-self-similarity`) is a legitimate reuse (already certified,
previously used identically by Theorem 34 itself).

No RETHINK-level issue found. **CHANGES REQUESTED-style outline
(instructive gaps, not fatal)** — approve to build, with the note above as
a mandatory first step.

## lp-duality-certificate: advance — APPROVE

This round's job is bookkeeping/consolidation (re-confirm case (a)/(b1)
scoping is unaffected by the round-19 explorer's "argmax tail ratio
drifts, not a universal constant" finding, and certify the
surrogate/majorization dead end as a formal negative-result lemma). Both
steps are sound and low-risk. I independently re-read the round-19
surrogate-lens explorer report: the finding that the ladder-tail-as-
"worst-case" surrogate is refuted (argmax ratio empirically 1.4–2.0,
drifting with `(p1,p2)`, confirmed at 4 points not 1) is a real,
non-circular negative result distinct from the four prior dead
mechanisms (peel/bisect/recurse, weighted-combination, boundary-
continuity, Danskin/concavity) — correctly diagnosed as a 5th confirmed-
dead family. Certifying this as a dead-end lemma is appropriate and keeps
future rounds from re-trying it. No new mechanism attempted on (b2) itself
this round in this slug, correctly routed to the new slug below — no
overclaim, no gap.

## minimax-lp-response-polytope: new — APPROVE, with a mandatory guardrail already built in

This is the fresh mechanism this round opens for case (b2), and I checked
specifically whether it is a repackaging of the already-dead
Convex-Combination-Futility Theorem family (that theorem forecloses any
WEIGHTED COMBINATION of primal strategy VALUES). The proposed mechanism is
different in kind: it puts multipliers (`λ_i`, `μ`) on the polytope's
defining CONSTRAINTS (per-piece cut-budgets, mass conservation) and
constructs an explicit dual-feasible point, invoking weak LP duality
(primal max ≤ any dual-feasible value) — this is standard LP theory
applied to a genuinely different object (a constraint dual, not a value
combination) and is not automatically subsumed by the Convex-Combination-
Futility result. The outline itself states the correct guardrail (step 3,
"Watch out for"): if the dual construction reduces algebraically to a
weighted sum of the known explicit strategies' outcomes, that is a sign
the mechanism has NOT escaped the dead family and must be reported as such
— this self-check is already present and appropriately placed before the
builder can force a false claim through.

The real open risk, honestly flagged in "Open gaps": the true feasible
region is piecewise-linear (a union of vertex cells, not one global LP),
so a literal single dual point valid across all cells may not exist; the
outline explicitly requires the builder to state which of (i) single dual
/ (ii) per-cell duals + boundary-consistency is attempted, and to prove
the boundary-consistency step if (ii) is chosen, rather than silently
picking the easy option and calling it done. This is properly scoped, not
overclaimed.

**One process gap, not a math gap:** the outliner did not actually write
`results/imo-2026-03/approaches/minimax-lp-response-polytope.md` (only the
outline text exists in `/tmp/round-19/proof-outliner.md`). Per the
approach-file contract, the builder should create this file from the
outline's skeleton before starting (this is legitimate — builders own
their own approach file — but flag it explicitly so the dispatched builder
doesn't wait for a pre-seeded file that doesn't exist).

Registered via `register_approach` (new slug, cold-start Elo 1500).

## rank-pigeonhole-budget: advance (optional cross-check) — APPROVE

Legitimate, low-risk: reuses already-certified exchange-smoothing-vertex-
maximization machinery as an independent second mechanism on the same
Δ(n,v) middle-band target greedy-halving-adversary is attacking via direct
vertex enumeration. This is valuable cross-verification in the same spirit
as rounds 3/7/8's independent-mechanism convergence checks, not a
duplicate. Correctly flagged optional/lower-priority by the outliner.

## Diversity check

Two independent fronts remain (lower bound: greedy-halving-adversary +
rank-pigeonhole-budget cross-check; upper bound: lp-duality-certificate +
new minimax-lp-response-polytope) — these are genuinely different halves
of the problem, not variations of one framing, so no shared-gap-plateau
concern this round. Within the upper-bound front, minimax-lp-response-
polytope is confirmed (above) to be a mechanism change from lp-duality-
certificate's now-5x-dead-ended case-(b2) value-combination attempts, so
fielding both is legitimate diversity, not redundant.

## Ranking

Registered `minimax-lp-response-polytope` (cold start). Ran
`update_ranking` with: greedy-halving-adversary beats lp-duality-
certificate (more concrete, active narrowing each round vs. repeated
mechanism deaths); greedy-halving-adversary draws rank-pigeonhole-budget
(both strong, different fronts, pigeonhole idle this round); lp-duality-
certificate draws minimax-lp-response-polytope (established track record
vs. untested-but-promising new mechanism, anchoring the newcomer against
an established peer on the same front); rank-pigeonhole-budget beats
minimax-lp-response-polytope (established milestone-holder vs. cold-start
newcomer); greedy-halving-adversary beats rank-tie-vertex-reduction
(active progress vs. parked approach). This clears `stale` flags on all
touched slugs and anchors the newcomer to real opponents.

build set: greedy-halving-adversary, minimax-lp-response-polytope, lp-duality-certificate, rank-pigeonhole-budget
