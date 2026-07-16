# Lemma (Gap-case Case A.A closure — subtract-all chain, upper bound)

**Status:** CERTIFIED (proof-reviewer, round 7). Proposed by `geometric-selfsimilar`. Reviewer verified
`A(final) = 2p₁ − Σ` for the subtract-all chain (0 anomalies / 9098 distinct-piece configs with
`p₁ > Σ/2`) and the exact threshold identity `2τ − Σ = Σ/D_b` (b = 1..7, 0 bad).

## Statement
Let `X = {p₁ > p₂ > ⋯ > p_m}` be distinct positive pieces with `|X| ≤ b + 1` (the budget invariant of
the sum-bound induction), `Σ = Σ(X)`, `D_b = 2^{b+1} − 1`, `τ := Σ·2^b/D_b`. If `p₁ > Σ/2` and
`p₁ < τ` (a gap case), then
```
μ(X, b) ≤ 2p₁ − Σ < Σ/D_b   (strict).
```

## Proof
Since `p₁ > Σ/2 = ½Σ_j p_j`, we have `p₁ > p₂ + ⋯ + p_m`, so `p₁ > p₂ + ⋯ + p_j` for every `j ≤ m`.
Xiang Yu performs the **subtract-all chain**: for `j = 2,…,m`, cut the current leftover
`L_{j−1} := p₁ − (p₂ + ⋯ + p_{j−1})` (with `L_1 = p₁`) at interior offset `p_j` into `(p_j, L_{j−1} − p_j)`.
The step-`j` cut is legal exactly when `L_{j−1} > p_j`, i.e. `p₁ > p₂ + ⋯ + p_j`, which holds. The chain
uses `m − 1` cuts, and `m − 1 ≤ b` by the budget invariant `|X| ≤ b + 1`, so it is within budget; all cut
points are strictly interior to descendants of `p₁`, hence a legal placement.

The resulting multiset is the `m − 1` spectators `{p₂,…,p_m}` together with the `m` carved subpieces
`{p₂,…,p_m, L_m}`, where `L_m = p₁ − (p₂ + ⋯ + p_m) = 2p₁ − Σ > 0`. Each `p_j` (2 ≤ j ≤ m) occurs an even
number of times (parity-invisible, Lemma R1 mechanism), so `N_final(x) ≡ 𝟙[L_m > x] (mod 2)`, whence
`A(final) = measure[0, L_m) = L_m = 2p₁ − Σ` (Lemma M0). Finally, `p₁ < τ` and the exact identity
`2τ − Σ = Σ/D_b` give `A(final) = 2p₁ − Σ < 2τ − Σ = Σ/D_b`, strictly. ∎

## Scope
Closes the gap-case sub-window `p₁ ∈ (Σ/2, τ)` of the sum-bound induction (a thin sliver, width
`Σ/(2D_b)`). The bulk `p₁ ≤ Σ/2` remains open (see `lemmas/sb-obstruction.md` for why no SB-monotone
reduction reaches it).
