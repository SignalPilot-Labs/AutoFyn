# outline-reviewer report — round 16 (imo-2026-02)

## What was read

`CLAUDE.md`, `results/imo-2026-02/current.md` (full round-15 adjudication,
sign-error finding), `/tmp/round-16/proof-outliner.md`, and the three
`### Round 16 outline` sections appended to `coordinate-bash-resultant-
boundary-pointwise-tangent.md`, `coordinate-bash-resultant-boundary-
pointwise-sos.md`, and `coordinate-bash-resultant-boundary.md`. Sampled the
ranker state (`mcp__approach-ranker__sample_approaches`, k=13, all 13
approaches) to confirm current Elo/stale status before ranking.

## Per-approach review

**`coordinate-bash-resultant-boundary-pointwise-tangent`** (Elo 1699
pre-round, stale). The round-16 skeleton is sound: it correctly diagnoses
*why* the direct 2-D value sweep chokes near the corner (a vanishing-target
degeneracy at a point of exact equality, not a real ambiguity) and proposes
sweeping a genuinely different, non-vanishing quantity (the directional
quotient `q(ε,t)`, bounded away from 0 by the already-certified `δ≈3.5`
directional-derivative margin) instead. This is not a new unjustified leap —
it reuses only already-certified machinery (Theorem A's exact `𝒞_lo`
parametrization, Theorems B/C's interval-sweep style, New result 9's
directional derivative) and explicitly derives the exact `t_lo(ε),t_hi(ε)`
from the certified curve parametrizations rather than the idealized
tangent-cone interval — the right level of rigor. The claim "any `r₀≥5×10⁻⁸`
suffices" is itself already established by round 15's own quadtree
resolution floor, so Step 2's generous `r₀` choice is conservative, not
hand-wavy. A concrete fallback is specified. No missing cases, no circular
reasoning. **Keep — strongest outline this round**, closest to a full glue
of Open gap 5 with no remaining open sub-target once the quotient sweep
succeeds.

**`coordinate-bash-resultant-boundary-pointwise-sos`** (Elo 1576 pre-round,
stale). Two clearly separated sub-goals, correctly prioritized (self-
contained exact-extraction sub-goal A first, larger joint-SDP sub-goal B
second). Sub-goal A's round-then-project procedure (diagnose rank →
rational-round Gram entries → compute exact residual → correct via linear
algebra in the affine null-space → re-verify PSD) is a standard, sound
technique for turning a converged numeric SDP into an exact certificate;
it is honestly flagged as possibly failing only at a PSD-boundary rank
deficiency, which the already-logged comfortable slacks (`t*≈0.24–8.5`,
none near 0) make unlikely. Sub-goal B correctly builds in the
ideal-membership multiplier `μ·(cosB²+sinB²−1)` from the start (a
previously-identified silent-bug class) and correctly deprioritizes the
constant-λ sanity check (expected to fail, per round 15's own widely-
varying pointwise `t*`). Both sub-goals reuse certified Theorem 4 and the
round-15 SDP infrastructure without re-derivation. No gaps in the outline
itself. **Keep.** Somewhat lower near-term certainty than `-tangent`
(sub-goal A yields "only" a pointwise lemma even on success; sub-goal B is
a genuinely larger, riskier undertaking that could still fail to converge),
which is reflected in the ranking below.

**`coordinate-bash-resultant-boundary`** (Elo 1701 pre-round, stale). Step 0
is the correct and necessary first move — mechanically fixing the confirmed
round-15 sign error (`-B_{G_0N}=(G_0·Num)_{00}` is the true sign-definite
generator, not the erroneously-signed `B_{G_0N}`) before any new search, so
the LP rerun in Step 1 is not built on a known-wrong premise. Step 1 is a
legitimate escalation (rerun the same 9-variant sweep with the corrected
generator, since literally none of round 15's runs used it) with the
correct methodological safeguard carried over (non-homogeneous degree
padding at every sub-degree, not just the top degree — round 15's own
corrected lesson). Step 2's escalation to a joint Putinar/SDP is the right
move if Step 1 fails again: LP infeasibility with a hand-picked generator
basis never rules out a certificate's existence, only that specific basis,
so escalating from a fixed finite generator list to a genuine SOS-multiplier
search is a real methodological upgrade, not a repeat of prior work. Step 3
(explicit case-split, Schur-domination adaptation) is correctly deprioritized
as a fallback only. No hand-waving, no skipped cases. **Keep.** Ranked
third of the three build-set approaches only because it starts this round
strictly behind (Step 0 is a repair, not new ground, and Steps 1–2 have not
yet been shown to close anything — the round-15 outcome for this approach
was the weakest of the trio, "partial" with a confirmed bug, versus the
other two's "advanced").

## `ptolemy-trig-identity-synthetic` (not opened this round)

Endorsed the outliner's decision not to dispatch a builder here. The
file/explorer correctly documents the auxiliary-circle route as an
exhausted structural dead end (K, L trace non-conic transcendental loci)
while flagging one untried, genuinely different lever (direct
monotonicity/convexity comparison of `α(θ)` vs `β_L(θ)`) for a future
round if the trio stalls. The population retains adequate framing diversity
this round (five distinct families per the outliner's count); no acute
collapse risk yet. No action needed from this review.

## Ranking

Submitted three pairwise comparisons via `update_ranking` to clear the
stale flags and reflect round-15's independently-adjudicated outcomes
(`-tangent` and `-sos` both "advanced" with certified new lemmas; `-boundary`
"partial" with a confirmed sign bug, the weakest of the three):
`-tangent` > `-boundary`, `-sos` > `-boundary`, `-tangent` > `-sos`.

Post-update Elo: `coordinate-bash-resultant-boundary-pointwise-tangent`
1725.8 (was 1699), `coordinate-bash-resultant-boundary` 1664.1 (was 1701),
`coordinate-bash-resultant-boundary-pointwise-sos` 1585.9 (was 1576). All
three now `stale: false`. No other approaches were touched this round (none
of their outcomes changed), so no further comparisons were submitted.

## Cuts

None. All three round-16 outlines are well-scoped, reuse certified
machinery correctly, contain no unjustified leaps, no missing cases, and
no circular reasoning. No approach is doomed as set up.

## Build set

Same three approaches the outliner put up skeletons for — each has a
concrete, dispatch-ready next step with no blocking defect found in review.

build set: coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos, coordinate-bash-resultant-boundary
