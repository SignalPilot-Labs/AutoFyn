## Status
solved

## Approach
Completed the whole threshold-parity route. The layer-cake and single-cut toggle identities are proved with endpoint conventions and current-daughter provenance. The dyadic lower bound is established by pairing final sorted fragments, forming a provenance multigraph on the original dyadic parents, selecting a tree component, and using its bipartition to extract a nonzero integer signed sum bounded by the alternating discrepancy. This handles arbitrary real cuts, repeated cuts, and fewer than n cuts.

For the universal upper bound, closest subset sums give two disjoint groups of Liu intervals whose total masses differ by at most 1/(2^{n+1}-1). A greedy transport splits actual intervals into equal cross-group fragment pairs; all unused intervals are bisected. Exact fragment and cut accounting shows this uses at most n legal positive cuts, and deleting equal pairs leaves total residual mass at most the target. If Liu used fewer than n marks, the spare cut capacity bisects all residuals and forces discrepancy zero.

The drafting minimax argument, ties, odd/even piece counts, legal distinct marks, fewer marks/cuts, n=1, and the final algebraic verification are all included.

## Output
The complete proof was written to `results/imo-2026-03/approaches/threshold-parity-toggles.md` with Status `solved`.

## Promotable lemmas
- Dyadic refinement lemma via a provenance multigraph tree component.
- Universal refinement lemma via closest subset sums and realizable greedy transport.
- Single-cut threshold-toggle identity.