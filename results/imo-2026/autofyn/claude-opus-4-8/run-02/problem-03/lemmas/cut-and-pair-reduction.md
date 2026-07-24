# Lemma: Cut-and-pair reduction (Xiang Yu upper-bound recursion) + dominant-regime dichotomy

**Certified round 2 (proof-reviewer).** Recursion and both atomic moves re-derived via the
certified matched-pair-invisibility (P1); the resulting invariant `g_b(P) ≤ Σ/D_b` verified
numerically true and tight (worst ratio 1.0 over random configs, b≤4, via the atomic-move
recursion).

## Setup
For a multiset `P` (sorted `a_1 ≥ … ≥ a_m`, sum `s`) and cut budget `b`, let
`g_b(P) := min over Xiang Yu's ≤ b cuts of f(final)`.

## Lemma 4 (cut-and-pair, one-step recursion)
Xiang Yu can, with one cut, reach a state whose alternating sum equals `f(R)`, where `R` is
one of:
- **Bisect-top:** cut `a_1 → (a_1/2, a_1/2)`; `R = {a_2, …, a_m}`, `Σ(R) = s − a_1`.
- **Top-match:** cut `a_1 → (a_2, a_1 − a_2)`; `R = {a_1 − a_2, a_3, …, a_m}`, `Σ(R) = s − 2a_2`.
In both, `|R| = m − 1`, and hence
```
    g_b(P) ≤ g_{b-1}(R).
```
*Proof.* Each move creates an equal pair (`a_1/2, a_1/2` resp. the new `a_2` and the old
`a_2`). By matched-pair invisibility (P1, certified), adjoining that equal pair leaves `f`
unchanged, so `f(final) = f(R_final)` where `R_final` is `R` after the remaining `≤ b−1`
cuts. Take the minimum over Xiang Yu's play on `R`. Uses P1 as an upper bound only. ∎

## Lemma H (dominant-regime dichotomy)
If `a_1 ≥ Σ(rest) =: σ`, then under every refinement `ρ'` of the rest, every piece is
`≤ σ ≤ a_1`, so `a_1` stays a maximum; when it is the unique maximum,
`f({a_1} ∪ ρ') = a_1 − f(ρ') ≥ a_1 − σ`. Hence Xiang Yu cannot push `f` below `a_1 − σ`
without spending a cut on `a_1`.
*Proof.* Peel identity `f = a_1 − f(ρ')` (Lemma of `alt-sum-two-max-minus-total`) plus
`f(ρ') ≤ Σ(ρ') = σ`. ∎

## Use
These drive Xiang Yu's upper-bound recursion for GAP-U. The geometric step closes when
`max(a_1, 2a_2) ≥ (2^b/D_b)·s` (removed mass `≥ 2^b/D_b·s`, so `Σ(R) ≤ D_{b-1}/D_b·s`, and
the IH `g_{b-1}(R) ≤ Σ(R)/D_{b-1}` gives `g_b(P) ≤ s/D_b`). The "middle regime"
`f(P) > s/D_b` AND `max(a_1, 2a_2) < (2^b/D_b)·s` is NOT covered by this one-step recursion.
