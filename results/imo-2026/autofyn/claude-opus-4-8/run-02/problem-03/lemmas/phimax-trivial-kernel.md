# Lemma: phimax-trivial-kernel (Lemma S-core)

**Certified round 5** (self-similar-recursion). Salvaged sound half of the rejected Lemma S.

## Statement
Let `f` be a functional that is affine on each sort-chamber of a multiset of positive reals
(e.g. the alternating sum `f(P)=Σσ_i a_i`). Consider a global minimizer of `f` over a
product-of-simplices domain `K=∏_k Δ_k` (`Δ_k` fixes the sum of piece `k`'s sub-pieces), and among
all minimizers pick `P*` maximizing the strictly convex `Φ(P)=Σ_i x_i^2`. Let `w_1>…>w_p` be the
distinct sub-piece values, `C_j` the value class of `w_j`, and `U` the piece–value incidence matrix
`(Uw)_k=Σ_j μ_{k,j}w_j = 2^k` (`μ_{k,j}` = # sub-pieces of piece `k` with value `w_j`). Then
`ker U = {0}` (equivalently `U` has full column rank, so `p ≤ #pieces`).

## Proof
Suppose `d≠0`, `Ud=0`. Shift `w_j(δ)=w_j+δ d_j` (add `δ d_j` to every sub-piece of `C_j`). Since
`Ud=0`, each piece's sum is preserved, so this is a feasible line in `K`; for `|δ|` small all
lengths stay positive and the distinct values stay distinct and ordered, so the point stays in one
sort-chamber where `f(δ)=m+γδ` is affine.
- If `γ≠0`, one sign of `δ` gives `f<m`, contradicting minimality.
- If `γ=0`, the whole small segment lies in the minimizer set. The shift rates `c_i=d_{j(i)}` are
  not all zero (some `d_j≠0` and `C_j≠∅`), so `Φ(δ)=Σ_i(x_i+δc_i)^2` is strictly convex in `δ`
  (leading coefficient `Σc_i^2>0`); hence `δ=0` (interior to the feasible segment) is not the max,
  so some `δ≠0` gives `Φ>Φ(P*)`, contradicting `Φ`-maximality.
Either way a contradiction, so `ker U={0}`. ∎

## Notes
Unconditional (does not rest on any open gap). Reusable by any approach that selects a
`Φ`-maximal minimizer. Does NOT by itself force the incidence multigraph to be a forest (see
open Gap A — `[[1,2],[2,1]]` has trivial kernel yet is a double-edge 2-cycle).
