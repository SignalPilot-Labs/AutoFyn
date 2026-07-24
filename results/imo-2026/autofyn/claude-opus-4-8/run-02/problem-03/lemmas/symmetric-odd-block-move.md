# Lemma: symmetric-odd-block-move (Move M3)

**Certified round 5** (self-similar-recursion). Verified 0 failures over valid samples
(the correct replacement for the refuted round-4 V-kink 3-shift).

## Statement
At a `Φ=Σx_i^2`-maximal minimizer `P*`, if a tie-block `C_j` has ODD size `μ_j` and some piece
`2^k` contributes `μ_{k,j} ≥ 2` copies to it, contradiction. Hence every odd-size tie-block carries
multiplicity `μ_{k,j} ≤ 1` from each piece.

## Proof
Take two of piece `2^k`'s copies of `v:=w_j`; for small `s`, move one to `v+s`, the other to `v−s`,
keep the remaining `μ_j−2` copies at `v`. Choose `|s|` small enough that no other value enters
`[v−s, v+s]`; then the copies still occupy the consecutive block ranks `[a_j, a_j+μ_j−1]`, with
`v+s` at rank `a_j` and `v−s` at rank `a_j+μ_j−1`. The block contribution changes by
`Δf = s(σ_{a_j} − σ_{a_j+μ_j−1})`, where `σ_r=(−1)^{r+1}`. For odd `μ_j`, ranks `a_j` and
`a_j+μ_j−1` differ by the even number `μ_j−1`, so `σ_{a_j}=σ_{a_j+μ_j−1}` and `Δf=0`: `f` is
exactly flat (the point stays a minimizer), while `Φ` gains `(v+s)^2+(v−s)^2−2v^2 = 2s^2 > 0`,
contradicting `Φ`-maximality. ∎

## Notes
Requires `μ_{k,j}≥2` (a single copy cannot be split symmetrically). For EVEN `μ_j`,
`σ_{a_j}−σ_{a_j+μ_j−1}=2σ_{a_j}≠0`, producing a V-kink with `Δf=2σ_{a_j}|s|`, so this move gives
NO contradiction on even blocks — which is exactly why even blocks remain the residual (Gap B).
Unconditional.
