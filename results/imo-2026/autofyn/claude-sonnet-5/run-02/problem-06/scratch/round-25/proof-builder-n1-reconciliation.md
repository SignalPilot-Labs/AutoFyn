# proof-builder report: n1-periodicity-reconciliation (round 25)

## Task
Fold in the corrected H2 numeric diagnosis from `/tmp/round-25/math-explorer-h2-asymmetry.md`
into `results/imo-2026-06/approaches/n1-periodicity-reconciliation.md`.

## What was found
This approach file did not itself contain round 24's original "11305 flat ~sqrt(N),
H2-threatening" claim (that framing lived in round-24's math-explorer-h2-absence report
and fed the sibling H2 approaches, `core-growth-monotonicity` /
`new-prime-recruitment-rate-bound`). Since this file is the run's H1/H2 reconciliation
and floor-deliverable hub (per its own §0-§9 structure), it is the right place to record
the corrected picture so no future round cites the stale framing.

## Changes made
1. Added a new **§10** ("Round 25: corrected H2 numeric diagnosis") to `## Current best`,
   placed before §E, documenting:
   - What round 24 originally claimed (global power-law fit, `11305` exponent "flat near
     0.51-0.57").
   - What round 25's larger re-simulation with a corrected LOCAL-EXPONENT methodology found:
     `4807` decelerates sharply (local exponent 0.14 plateau -> 0.06-0.09 by n=1M); `11305`
     decelerates mildly (0.26-0.28 -> 0.22 by n=750k), never actually reaching ~sqrt(N)=0.5
     even at its highest reading. So the literal sqrt-growth claim is withdrawn, replaced by
     "both seeds decelerate, at different rates."
   - A plausible (not proved) structural account: `11305`'s Finite-Core-Theorem core is
     larger (|S_0|=12 vs 9), so it needs more runway before deceleration becomes visible,
     by analogy with `4807`'s own collapse only appearing past n~500k.
   - An explicit honesty section: this is numeric DE-THREATENING, NOT evidence FOR H2 in
     any proof-theoretic sense. No amount of simulation bounds (N(S_k))_k. 11305's future
     trajectory (continued deceleration vs. asymptoting to a positive exponent, which would
     actually refute H2 for that seed) remains genuinely unresolved.
   - An explicit assessment of whether this suggests new H2 machinery: concluded NO — the
     one semi-concrete follow-up (a size-normalized statistic T(N)/2^|S_0| for fairer
     cross-seed comparison) is a measurement refinement, not a proof technique, and does not
     evade the already-recorded structural obstruction in this file's own §4.2 (self-absorption
     requires full-factorization containment of early terms, not shared-prime or type-count
     observations). No new H2 mechanism was attempted this round, matching the dispatch's
     instruction to only attempt one if genuinely novel.
2. Added a corresponding entry at the top of `## Approaches tried` summarizing this round's
   work, consistent with the file's history-preservation convention (no prior entries deleted).
3. Status left as `partial` (unchanged) — this was documentation/correction work, not new
   proof progress on H1 or H2, exactly as instructed.

## Status
partial (unchanged). H1 and H2 both remain fully open. This round's contribution is a
corrected, honestly-scoped H2 numeric diagnosis, not new proof content.

File updated: `/home/agentuser/repo/results/imo-2026-06/approaches/n1-periodicity-reconciliation.md`
