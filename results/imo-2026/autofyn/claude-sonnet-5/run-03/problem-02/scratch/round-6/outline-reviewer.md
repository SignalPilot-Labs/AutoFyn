# Outline review — imo-2026-02, round 6

## Context
Two independent live routes to a full solve remain (established since round
3-5): (a) the coordinate/rotation-parametrization route
(`coordinate-bash-resultant-boundary`), now split into a sibling and a copy
attacking the SAME algebraic gap cluster with two different closing
architectures; (b) the Ptolemy/trig route (`ptolemy-trig-identity`), reduced
to sextic positivity. `fixed-point-concyclic` and
`ptolemy-trig-identity-synthetic` are left untouched this round (no build) —
correctly, per prior rounds' documented exhaustion/subsumption.

## coordinate-bash-resultant-boundary: advance — APPROVE

Skeleton (steps 1-4 certified, steps 5-8 new this round) is sound and
well-scoped. Assessment of the new content:

- **Step 5 (magnitude bound t1<t1max(β))**: correctly identified as
  structurally identical to Lemma 11.5/11.7's "affine function crossed with
  a quadratic ⟹ Vieta sign trick" — the magnitude-lens explorer verified
  the affine-linearity claim (`cross(C-M,K-M)` affine in `t1`) is the right
  shape and that this test is a genuinely different, non-redundant
  condition from Theorem 11.8's `cross(BK,BL)` test (touches M/edge-MC,
  not just direction from B). Flagged, correctly, as unproved — evidenced
  only by existing multi-triangle sweeps, not new computation. This is a
  lemma-with-mechanism, not a bare label: acceptable to build.
- **Step 6 (G2b exclusion)**: this round's g2b-lens explorer found the
  needed mechanism is NOT "B2's sign is fixed" (dead, confirmed varies) but
  a *joint* containment+sign criterion on G2b's true (non-supplementary)
  root, stress-tested at 4500+ trials with zero counterexamples. The
  outline correctly incorporates this exact reframing (not the stale
  B2-sign lever). The claimed mechanism ("mirrors exactly how Theorem 11.8
  isolated G2a's genuine root... shown to always fail instead of succeed")
  is an analogy, not yet a proof — appropriately flagged as an open gap in
  the outline's own "Open gaps" section, not overclaimed as closed. Good.
- **Step 7 (pointwise-supersedes-continuity reframing)**: explicitly
  self-flagged as needing verification that it actually retires the F3/F3'
  question rather than silently reintroducing it via σ-symmetry/hyp-3
  combination — this is honest hedging, not circular reasoning. Acceptable.
- Case coverage: sign(b) case-split (mirroring Lemma 11.7) and
  true-vs-supplementary root case for G2b are both explicitly listed.
  Adequate for an outline stage (full case handling is the builder's job).
- Watch-outs (i)-(iii) correctly warn against conflating the two
  independent sign tests and against assuming σ-invariance for free
  (previously shown false in round 2) — good, no repeat of a known pitfall.

No RETHINK-worthy flaw found. Real algebraic content, mechanisms named,
gaps honestly scoped. **APPROVE.**

## coordinate-bash-resultant-boundary-pointwise: new (copy) — APPROVE

This is a genuine architectural fork, not a fragment of the sibling's proof
nor a cosmetic relabeling: it targets the exact same whole-problem claim
(OM=ON) via the same certified reduction/parametrization, but commits to a
*different* closing logic (prove branch selection holds independently at
every fixed β, with no continuity/IVT step at all) that, if it succeeds,
makes the sibling's still-unresolved F3/F3'-crossing question (open since
round 4) structurally irrelevant rather than merely resolving it — a
materially different proof obligation (steps 5-6's same algebra, but no
range-connectedness argument needed; instead a new "no β admits two
simultaneously-valid candidate tuples" non-degeneracy check). This is
exactly the kind of "two viable ways to fill the remaining gap" the
copy_approach tool is for, not a same-framing variation CLAUDE.md warns
against (the two siblings differ in what must be proved, not just how it's
presented). The outline itself is appropriately self-aware of the risk
that it could collapse back into the sibling's framing, and instructs
future rounds to treat that as informative rather than wasted — good
practice, no fatal flaw. **APPROVE.** Registered via `copy_approach`
(inherits the sibling's Elo/counts, per tool semantics — will diverge on
its own merits from next round's outcome).

## ptolemy-trig-identity: advance — APPROVE

The reframing from "global Ψ>0" (now conclusively refuted — sextic-lens
explorer found explicit counterexamples with Ψ<0 for τ outside the
geometric domain in ~29% of sampled points, confirmed 1176/4000) to a
domain-restricted root-count + boundary-sign IVT argument is the correct
response to genuinely new negative information, not a cosmetic pivot. The
outline's watch-out section explicitly forbids re-attempting the dead
global-SOS route — good, matches the explorer's finding and this round's
memory rule.

- Step 4(b) (≤1 positive real root, "generically"): correctly flagged as
  needing an actual sign-pattern/Descartes/Sturm argument on the
  coefficients as functions of A,C, not just the 6-sample numeric pattern
  the explorer found. This is the outline's weakest link — "generically"
  is doing real work here and the outline does not yet specify what
  happens if a triology of A,C ever produces ≥2 positive roots with one
  inside the domain (a scenario not ruled out, only not yet observed).
  This is correctly listed as an open gap, not asserted as proved — no
  overclaiming, so not RETHINK-worthy, but the builder must either (i)
  prove a genuine, sign-pattern-based bound (not just check more samples)
  or (ii) design step 4(c)'s boundary-substitution argument to be robust
  even if occasionally >1 positive root occurs (e.g. by directly bounding
  Ψ at the boundary combined with monotonicity, rather than relying on
  "exactly one root" as a load-bearing assumption). Flag this explicitly
  to the builder as the sharpest remaining risk in the plan.
- Step 4(c) (boundary substitution at τ=tan(min(B,C))): correctly
  identified as a substitution, not a search — tractable, uses the same
  rational-parametrization technique already validated this round by the
  sextic explorer's independent rebuild. Sign(B−C) case split is listed.
  Sound.
- Degenerate-case watch (A→0, Ψ→0) is correctly flagged as needing care,
  not swept under "generic" — good.

No fatal flaw; real, well-evidenced progress with one precisely-identified
weak link (the word "generically" in 4(b)) that the builder must resolve
or route around. **APPROVE**, with the explicit note above passed to the
builder.

## fixed-point-concyclic, ptolemy-trig-identity-synthetic: leave alone — no objection

Both correctly left unbuilt this round per prior rounds' documented
exhaustion (fixed-point-concyclic: structural dimension-count retirement,
round 5) and subsumption (ptolemy-trig-identity-synthetic: all three
synthetic searches closed negative, its one live contribution already
folded into the sibling). No new idea surfaced by this round's explorers
for either — correctly not force-fed a build slot. Not registering any
change (already registered, ranked below).

## Diversity check

The population still maintains two genuinely independent live routes
(coordinate algebra vs. Ptolemy/trig algebra) plus two documented-exhausted
alternatives kept as population record. The new pointwise copy does not
reduce diversity — it is a fork within one route's gap cluster, explicitly
justified as materially different in proof obligation, not a rubber-stamp
variation. No shared-gap plateau newly detected this round: the two live
routes' gaps (branch-selection cluster; sextic positivity) are structurally
distinct pieces of algebra, not the same wall restated.

## Ranking

Registered `coordinate-bash-resultant-boundary-pointwise` via
`copy_approach` (source: `coordinate-bash-resultant-boundary`). Ran
`update_ranking` with comparisons anchoring the two live routes against
each other and against the exhausted/stagnant approaches:
`coordinate-bash-resultant-boundary` > `ptolemy-trig-identity` (slightly
ahead: has a fully closed, independently-reproduced Theorem 11.8 this
cycle) > `fixed-point-concyclic` / `ptolemy-trig-identity-synthetic`
(exhausted/subsumed); `coordinate-bash-resultant-boundary` >
`coordinate-bash-resultant` > `coordinate-bash`; `fixed-point-concyclic` and
`coordinate-bash` both > `power-of-point-secants` (stagnant since round 1).
Resulting order (best-first): coordinate-bash-resultant-boundary (1620) =
coordinate-bash-resultant-boundary-pointwise (1594, inherited, not yet
re-ranked on own merit) > ptolemy-trig-identity (1557) >
coordinate-bash-resultant (1538) > coordinate-bash (1506) >
fixed-point-concyclic (1496) > ptolemy-trig-identity-synthetic (1445) >
power-of-point-secants (1351).

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise, ptolemy-trig-identity
