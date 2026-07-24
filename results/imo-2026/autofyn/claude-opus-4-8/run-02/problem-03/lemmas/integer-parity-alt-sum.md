# Lemma: Integer parity of the alternating sum

**Certified round 2 (proof-reviewer).** Proof re-derived and verified numerically
(100000 trials, 0 violations of `0 ≤ f` and of the parity congruence).

## Statement
For any multiset `P` of nonnegative **integers**, sorted descending, the alternating sum
`f(P) = a_1 - a_2 + a_3 - …` satisfies
```
    f(P) ≡ Σ(P) (mod 2),   and   f(P) is a nonnegative integer.
```

## Proof
`f(P) = Σ_{i} a_i − 2·Σ_{i even} a_i = Σ(P) − 2·Σ_{i even} a_i`. The subtracted term is an
even integer, so `f(P) ≡ Σ(P) (mod 2)`. Nonnegativity: grouping
`f(P) = (a_1−a_2) + (a_3−a_4) + …` (append a phantom `0` if the count is odd), each bracket
is `≥ 0` since the list is sorted descending. ∎

## Consequence (GAP-L for integer cut placements of W_n)
Let `W_n = {2^0, …, 2^n}` (`Σ = D_n = 2^{n+1}−1`, odd). If Xiang Yu cuts only at integer
positions, every final piece is a positive integer and `Σ` is preserved, so
`f(final) ≡ D_n ≡ 1 (mod 2)` is an odd integer that is `≥ 0`, hence `f(final) ≥ 1`. This
settles the lower-bound floor for **all integer (dyadic) adversary cut placements** — but
NOT for non-integer cut positions (parity does not apply there; e.g. a common-denominator
`d` scaling admits `f = 1/3` under the congruence). The non-integer case remains open.
