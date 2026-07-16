# Lemma BR — bottom-restriction (max|g|-agnostic BYPASS)

**Status:** CERTIFIED by proof-reviewer, round 13. Proposed by `ll-dyadic-symdiff` (§R13.1). The proof is a
one-line measure-monotonicity argument; reviewer re-derived it and confirms it is a genuine bypass — it
uses NO bound on `max|g|`, no reflection identity, and no Sub-3a hypothesis.

## Notation (imported, `alt-sum-integral`)
`N_P(x) = #{parts of P exceeding x}`, `g := N_Q − N_R`, `A(Q∪R) = measure{x≥0 : g(x) odd}` (Lemma M0).

## Statement
For finite positive multisets `Q, R` and any `τ > 0`,
```
A(Q∪R) ≥ measure{x∈[0,τ) : g(x) odd}.
```
In particular, taking `τ = min(Q)`: for all `x∈[0,min(Q))` every part of `Q` exceeds `x`, so `N_Q(x)=|Q|`
and `g(x)=|Q|−N_R(x)`; hence
```
A(Q∪R) ≥ B := measure{x∈[0,min(Q)) : N_R(x) ≢ |Q| (mod 2)}.
```

## Proof
`{x≥0 : g(x) odd} ⊇ {x∈[0,τ) : g(x) odd}`, so by monotonicity of Lebesgue measure
`A(Q∪R) = measure{x≥0 : g(x) odd} ≥ measure{x∈[0,τ) : g(x) odd}`. For `x∈[0,min(Q))`, `N_Q(x)=|Q|`
constant, so `g(x)=|Q|−N_R(x)` is odd iff `N_R(x) ≢ |Q| (mod 2)`. ∎

## Downstream (Q-top reduction, §R13.2–3, also verified by reviewer)
For **Q-top** configs (`min(Q) ≥ 2^{n−2}`): `|Q|∈{3,4}` (sum/interval count), and (BR-top) with the
within-bottom parity identity gives `A(Q∪R) ≥ 1` REDUCES to the R-only inequality (★R):
`|Q|=4 ⟹ A_R^{bot}≥1`; `|Q|=3 ⟹ A_R^{bot}≤2^{n−2}−1`, where `A_R^{bot}=measure{x∈[0,2^{n−2}):N_R odd}`.
(★R) is verified (0 violations, n=3,4,5, both tight) but **NOT proved** — this is the honest open residual.
