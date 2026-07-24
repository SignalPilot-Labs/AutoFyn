# Lemma: mu3-shared-leaf-cut-cost (Lemma CUT3)

**Certified round 8** (self-similar-recursion). Reviewer-verified.

## Statement
Let `P` be any refinement of `W_n={2^0,…,2^n}` (`n≥1`). Suppose some piece `2^k` is split into
exactly three equal sub-pieces `{v,v,v}` with `v=2^k/3`, and the value `v` also occurs as a sub-piece
of a DIFFERENT piece `2^m` (`m≠k`) — i.e. `v` is *shared* (its tie-block has even total size). Then
`P` uses at least `3` cuts.

## Proof
Splitting piece `2^k` into three sub-pieces uses `r_k−1=2` cuts on that piece. Consider the donor
piece `2^m`, which contains a sub-piece equal to `v`. If `2^m` were uncut (`r_m=1`), its unique
sub-piece would be the whole piece of value `2^m`, forcing `2^m=v=2^k/3`, i.e. `2^k/2^m=3`. But a
ratio of two powers of two is a power of two and `3` is not a power of two — contradiction. Hence
`r_m≥2`, i.e. piece `2^m` uses `≥1` cut. Since `k≠m` these are distinct pieces, so
`N=Σ_j(r_j−1)≥2+1=3`. ∎

## Corollary (Gap B is vacuous at low budget)
No refinement of `W_n` using `≤2` cuts contains a `μ=3` shared even-block piece-leaf. Consequences:
- **`n=2`:** budget `N≤n=2<3`, so Gap B never occurs — the `n=2` lower bound has no Gap-B obstruction.
- **Every `n`:** the induction steps `N∈{0,1,2}` of Claim(N) are Gap-B-free; a `μ=3` even leaf can
  first appear only at `N≥3`, i.e. only for `n≥3`. Any surviving Gap-B minimizer spends `≥3` of its
  `≤n` cuts on leaf+donor, leaving `≤n−3` for the remaining pieces.

## Companion (cycle cut-cost floor, same mechanism)
A cycle `Z` through `r` distinct pieces with a degree-`≥3` cycle-piece has cycle-piece sub-piece
count `≥2r+1`, contributing `≥r+1≥3` cuts. So a Gap-A′ cycle also costs `≥3` cuts, vacuous for `N≤2`.

## Verification
Arithmetic checked on the `n=3` witness `piece8={8/3,8/3,8/3}, piece4={8/3,4/3}, piece2={2},
piece1={1}` (`Σ=15`, `f=5/3`, `N=2+1+0+0=3`). The impossibility `2^k/2^m=3` is exact.
(`/tmp/verify8.py`.)
