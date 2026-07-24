# Lemma: uncut-survivor (cut-budget Lemma 5.1)

**Certified round 5** (cut-budget-jacobsthal-recursion).

## Statement
Every refinement `Q` of `W_n = {2^0,…,2^n}` obtained with at most `n` extra cuts leaves at least
one of the `n+1` original pieces uncut (present intact in `Q`).

## Proof
If piece `2^i` is cut into `r_i ≥ 1` sub-pieces, the number of cuts is `Σ_{i=0}^n (r_i−1) ≤ n`, so
`Σ_{i=0}^n r_i ≤ 2n+1`. With `n+1` summands each `≥1`, if every `r_i ≥ 2` then
`Σ r_i ≥ 2(n+1) = 2n+2 > 2n+1`, a contradiction. Hence some `r_i = 1`. ∎

## Notes
Unconditional pigeonhole. Reusable for any ≤n-cut refinement argument on W_n.
