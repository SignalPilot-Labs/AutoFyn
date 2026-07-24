# Lemma: f ≥ 2·a₁ − Σ (and elementary f-bounds)

**Certified round 2 (proof-reviewer).** Verified numerically (100000 trials, 0 violations).

## Statement
For any finite multiset `S` of nonnegative reals with maximum `a_1` and total `Σ`, the
alternating sum `f(S) = a_1 − a_2 + a_3 − …` (sorted descending) satisfies
```
    0 ≤ f(S) ≤ Σ,        f(S) ≥ 2·a_1 − Σ,
```
and, when `a_1` is a (unique) maximum, the peel identity `f(S) = a_1 − f(S∖{a_1})`.

## Proof
`0 ≤ f`: group `(a_1−a_2)+(a_3−a_4)+…`, each bracket `≥ 0` (phantom `0` if odd count).
`f ≤ Σ`: `Σ − f = 2(a_2+a_4+…) ≥ 0`. Peel: removing a maximum leaves `a_2 ≥ a_3 ≥ …`, whose
alternating sum is `a_2 − a_3 + …`, and `a_1 − (a_2−a_3+…) = f(S)`.
`f ≥ 2a_1 − Σ`: `Σ − a_1 = a_2 + a_3 + … ≥ a_2 − a_3 + a_4 − … = a_1 − f` (the dropped terms
`2a_3 + 2a_5 + … ≥ 0`); rearrange. ∎

## Consequence (GAP-L Case 1)
If Xiang Yu never cuts the top piece of `W_n`, then `a_1 = 2^n/D_n`, `Σ = 1`, so
`M = f ≥ 2·2^n/D_n − 1 = 1/D_n`.
