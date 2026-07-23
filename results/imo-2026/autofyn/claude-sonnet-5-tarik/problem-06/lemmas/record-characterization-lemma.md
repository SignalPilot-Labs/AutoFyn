# Record Characterization Lemma (𝓥 without reference to 𝓜_n)

## Status

Certified `solved`-quality (sorry-free), unconditional.

## Statement

Call `i≥1` *fresh* if no `k` with `1≤k<i` has `P_k⊊P_i` (vacuous for `i=1`).
Then `𝓥=\{P_i : i≥1\text{ fresh}\}` — i.e. `𝓥` (as defined in
`theorem-V-veto-finite-iff-MRS.md`) equals exactly the set of distinct
radical values realized at "record" positions of the raw sequence `(P_n)`
under `⊊`, with **no reference at all** to the incremental `M_n`/`𝓜_n`
antichain-update process.

## Proof

`(⊇)` Let `i` be fresh. For `k=i`, `P_i⊊P_i` is false; for `1≤k<i`,
`P_k⊄P_i` by freshness. So no `k∈\{1,…,i\}` dominates `P_i`, giving `i∈M_i`,
so `P_i∈𝓜_i⊆𝓥`.

`(⊆)` Let `C∈𝓥`, so `C∈𝓜_n` for some `n`, i.e. `C=P_i` for `i∈M_n` (`i≤n`,
no `k∈\{1,…,n\}` has `P_k⊊C`). For any `k<i`: since `k<i≤n`, `k∈\{1,…,n\}`,
so `P_k⊄C=P_i` by the above. So `i` is fresh, with `P_i=C`. ∎

## Independent re-verification (proof-reviewer, round 5)

Re-derived from scratch; both directions are immediate consequences of the
`n`-minimality definition (Lemma W3) applied at `n=i` versus at the
`n` witnessing `C∈𝓜_n`, using `i≤n` to compare the two index ranges
`\{1,…,i\}⊆\{1,…,n\}`. No gap. Independently spot-checked computationally
(fresh Python) against the direct `𝓜_n`-based definition of `𝓥` for
`a_1=91,247`: exact match in both cases.

## Certification

Certified `solved`-quality, unconditional. Practically useful: reduces any
future `𝓥`-finiteness argument to a single-pass, non-recursive scan of the
raw sequence `(P_n)_{n≥1}` for "records" under `⊊`, rather than requiring
the incremental antichain-maintenance machinery.

## Source

`results/imo-2026-06/approaches/persistent-backbone-monovariant.md` (round
5).
