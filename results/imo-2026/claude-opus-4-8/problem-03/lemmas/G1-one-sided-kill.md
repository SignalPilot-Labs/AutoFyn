# Lemma G1 — one-sided small-discrepancy kill

**Status:** CERTIFIED (round 12, `ll-dyadic-symdiff`; reviewer re-derived + verified). Strictly
generalizes the certified `D1-small-discrepancy-kill` on the upper side.

## Notation (imported)
`N_P(x) = #{parts of P exceeding x}`; `g := N_Q − N_R`; `∫₀^∞ g dx = ΣQ − ΣR` (since `∫N_P = ΣP`);
`A(Q∪R) = measure{x : N_{Q∪R}(x) odd} = measure{x : g(x) odd}` (Lemma M0 / `alt-sum-integral`, using
`N_Q+N_R ≡ N_Q−N_R (mod 2)`); `M_k := measure{x : g(x)=k}`.

## Statement
Let `Q, R` be finite positive multisets with `N_Q(x) ≤ N_R(x) + 1` for every `x ≥ 0`
(equivalently `max g ≤ 1`, with `g` allowed arbitrarily negative). Then
`A(Q∪R) ≥ ΣQ − ΣR`. In bucket (iii) (`ΣQ = 2^n`, `ΣR = 2^n − 1`) this is `A(Q∪R) ≥ 1`.

## Proof
Since `max g ≤ 1`, `M_k = 0` for all `k ≥ 2`, so
`ΣQ − ΣR = ∫g = Σ_k k·M_k = M_1 − Σ_{k≤−1}|k|·M_k ≤ M_1`
(every term of the last sum is `≥ 0`). Hence `M_1 ≥ ΣQ − ΣR`. As `g=1` is odd,
`{g=1} ⊆ {g odd}`, so `A(Q∪R) = measure{g odd} ≥ M_1 ≥ ΣQ − ΣR`. ∎

## Scope / notes
- The hypothesis is one-sided and cannot be flipped: `min g ≥ −1` does NOT give `A ≥ 1` (the `g ≡ 2`
  obstruction has `A = 0` while `∫g = 2`).
- Closes the entire `max g ≤ 1` slice of the bucket-(iii) `Sub-3a`-failing residual, all `n`.
- Reviewer verification: the measure identity `A ≥ M_1 ≥ ∫g` re-checked on 3000 random exact-Fraction
  integer-valued step functions with `max g ≤ 1, ∫g>0` (0 violations); relation is elementary and exact.
