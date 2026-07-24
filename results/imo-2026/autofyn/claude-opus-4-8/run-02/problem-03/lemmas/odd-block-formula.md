# Lemma: odd-block-formula (Block formula BF)

**Certified round 5** (self-similar-recursion). Verified 0/20000.

## Statement
For any finite multiset `P` of positive reals, group equal values into tie-blocks `C_1,…,C_p` of
distinct values `w_1>…>w_p`, block `j` of size `μ_j` occupying consecutive descending ranks
`[a_j, a_j+μ_j−1]`. Then the alternating sum is
```
    f(P) = Σ_{j : μ_j odd} σ_{a_j} w_j ,      σ_r = (−1)^{r+1}.
```
Even-size tie-blocks are `f`-invisible.

## Proof
Consecutive signs alternate, so block `j` contributes `w_j Σ_{i=a_j}^{a_j+μ_j−1} σ_i`. A run of
`μ_j` consecutive alternating `±1` starting at sign `σ_{a_j}` sums to `σ_{a_j}` if `μ_j` is odd and
`0` if `μ_j` is even. Summing over blocks gives the formula. (Equivalently, a matched even
sub-block is P1-invisible.) ∎

## Notes
Unconditional. Immediate corollary of layer-cake / matched-pair invisibility.
