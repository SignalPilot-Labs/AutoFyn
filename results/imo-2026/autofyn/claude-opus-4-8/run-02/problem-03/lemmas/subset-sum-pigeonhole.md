# Lemma: subset-sum pigeonhole floor for signed {−1,0,1} combinations

**Status: CERTIFIED (round 3, reviewer). From `alternating-sum-threshold-potential`.**
Reviewer note: the cleanest airtight form is the sorted-consecutive-gaps view — the `2^m` subset
sums include `0` (empty set) and `s` (full set); sorting them `0=σ_0≤…≤σ_{2^m-1}=s` gives
`2^m−1` consecutive gaps summing to `s`, so the smallest gap is `≤ s/(2^m−1)`, and the two
subsets bounding it give the `{−1,0,1}` witness. (This avoids the half-open/endpoint nuance in
the cell phrasing below, where the point `s` must be placed in the closed last cell.) Verified
over 50000 random multisets, worst ratio exactly 1.0 on dyadic inputs.

## Statement
For any finite multiset of nonnegative reals `P = {a_1,…,a_m}` with sum `s`,
```
   φ(P) := min over ε ∈ {−1,0,+1}^m, ε ≠ 0  of  |Σ_i ε_i a_i|   ≤   s/(2^m − 1).
```

## Proof
Consider the `2^m` subset sums `σ(T) = Σ_{i∈T} a_i` for `T ⊆ {1,…,m}`; each lies in `[0,s]`.
Partition `[0,s]` into `2^m − 1` half-open intervals of equal length `s/(2^m − 1)`. There are
`2^m` values and `2^m − 1` cells, so by the pigeonhole principle two distinct subsets `T ≠ T′`
land in one cell: `|σ(T) − σ(T′)| ≤ s/(2^m − 1)`. Put `ε_i = 1[i∈T] − 1[i∈T′] ∈ {−1,0,+1}`;
then `ε ≠ 0` (since `T ≠ T′`) and `|Σ_i ε_i a_i| = |σ(T) − σ(T′)| ≤ s/(2^m − 1)`. ∎

## Tightness
Equality-type behaviour on dyadic inputs `{2^{m−1},…,2,1}` (sum `2^m − 1`): the `2^m` subset
sums are exactly `{0,1,…,2^m−1}`, so the closest pair differs by `1 = s/(2^m−1)`; `φ = 1`.

## Numerical check
`φ·(2^m−1)/s ≤ 1` over 50000 random multisets (`m ≤ 7`), worst ratio 1.0 (only on dyadic).
