# Lemma: Layer-cake parity identity for the alternating sum

**Certified round 1 (proof-reviewer).** Independently verified numerically on 300 random
multisets (alternating sum vs. odd-parity measure; 0 mismatches to 1e-4).

## Statement
For a finite multiset `P` of nonnegative reals, let `c_P(t) = #{pieces of P that are > t}`
and `f(P) = a_1 - a_2 + a_3 - ...` (sorted descending). Then
```
    f(P) = measure{ t >= 0 : c_P(t) is odd } =: M(P).
```

## Proof (verified sound)
Each piece `a_i = ∫_0^∞ 1[a_i > t] dt`. For fixed `t`, the pieces exceeding `t` are exactly
ranks `1,...,c_P(t)`, so `Σ_i (-1)^{i+1} 1[a_i>t] = Σ_{i=1}^{c_P(t)} (-1)^{i+1}` = 1 if
`c_P(t)` odd, 0 if even. Integrating: `f(P) = ∫_0^∞ 1[c_P(t) odd] dt`. ∎

## Consequences (all certified)
- `Odd(P) = (1 + f(P))/2`; with total 1, LB's payoff is `(1 + M(P))/2`.
- **Reduction:** `c(n) = (1 + max_LB min_XY M)/2`, and since `2·(2^n/D_n) - 1 = 1/D_n`
  (with `D_n = 2^{n+1}-1`), the claim `c(n) = 2^n/D_n` is **equivalent** to
  `max_LB min_XY M = 1/D_n`.
- **Single-cut action:** cutting a length-`p` piece at offset `x <= p/2` flips the parity
  of `c(t)` exactly on `[0,x) ∪ [p-x, p)`; a bisection flips it on all of `[0,p)` (so a
  bisection creates a matched pair invisible to `M`). Verified.
- **Matched-pair invisibility (P1):** adjoining two equal pieces of value `v` leaves `M`
  unchanged (adds 2 to `c(t)` for `t<v`). Verified.
