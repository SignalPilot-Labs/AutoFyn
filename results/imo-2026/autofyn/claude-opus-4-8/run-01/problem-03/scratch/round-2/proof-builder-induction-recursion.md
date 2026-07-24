# proof-builder report — induction-recursion (imo-2026-03), round 2

**Status: partial.** Core mechanism (H2) refuted; two lemmas proven.

## H2 separation check — FAILED (this was the required front-load)
Tested "isolate P_0=1/D, play scaled (n−1) strategy on remainder R, invoke (n−1) IH" on n=2 and n=3 via XY best-response search.

- The tempting fact c(n−1)·|R| = c(n) is TRUE (verified) but does NOT license the reduction.
- **F1 (budget non-decrement):** XY keeps all n marks; it can place all n inside R, exceeding the (n−1) IH's budget, so the IH is inapplicable. The induction never legitimately steps n→n−1.
- **F2 (global re-ranking):** OddSum/AltSum is a global functional of the merged sorted list. n=3 optimal XY response = bisect 8/15→(4/15,4/15) + cut 4/15→(3/15,1/15), sorted {4,4,3,2,1,1}/15; sub-pieces from both sides of any boundary interleave, and P_0's parity depends on how many pieces XY makes above it. No rank-invariant boundary ⇒ no independent (n−1)-subgame.

Conclusion: the clean n→(n−1) game separation is a numerical coincidence, not a decomposition. Skeleton Steps 2–4 all rest on it and cannot be written. RETHINK-level concern for the separation mechanism.

## What I closed (rigorous)
1. **Step 1** — recursion ⇔ closed form: r(n)=1/c(n)=2−2^{−n} ⟹ c(n)=2^n/(2^{n+1}−1). Airtight.
2. **Step 1′ (NEW, promotable)** — AltSum reformulation: OddSum=(1+AltSum)/2 with AltSum=Σ(−1)^{i+1}q_i, so c(n)=(1+A*)/2 and the target is equivalent to A*(n)=1/(2^{n+1}−1). Independent of any separation; usable by all three approaches to simplify the objective.

## Salvage note for the outliner
Halving the largest piece is an optimal XY first move (verified n=1,2,3), matching 1/c(n)=1+1/(2c(n−1)). But after halving LB's 2^n/D the residual has three equal top pieces 2^{n−1}/D and is NOT a scaled (n−1)-geometric instance, so the halving recursion hits the same F2 obstacle. If the recursion is kept, justify it by a monovariant on the merged sorted list (via AltSum), not by isolating a sub-stick.

## Remaining gaps (both open in this route)
- Lower bound: LB-geometric ⟹ AltSum ≥ 1/D against any XY cuts.
- Upper bound: XY holds AltSum ≤ 1/D against any LB marking (field-wide hard core).

## Recommendation to orchestrator
Route this slug's separation mechanism to RETHINK (H2 is false, not patchable). Keep Status partial because Step 1 + AltSum reformulation are solid, promotable, and shared. Consider commissioning the AltSum reformulation as a certified shared lemma and pointing the next outliner at a monovariant-on-merged-list framing for the upper bound rather than another n→(n−1) separation.
