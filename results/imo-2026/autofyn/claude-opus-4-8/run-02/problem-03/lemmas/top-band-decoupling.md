# Lemma: Top-band localization and half-threshold decoupling for W_n

**Certified round 2 (proof-reviewer).** Both parts re-derived; the decoupling identity
`f(P) = u + f(Q)` verified numerically (top-only-cut refinements of `W_n`, n≤4, 0 violations).

## Setup
Fix `n ≥ 1`. Let `P` be any refinement of `W_n = {2^0, …, 2^n}` (Xiang Yu has cut the pieces
arbitrarily). Let the sub-pieces of the top piece `2^n` be `s_1 ≥ s_2 ≥ …` (`Σ s_i = 2^n`),
and let `R'` be the multiset of sub-pieces of the block `{2^0, …, 2^{n−1}}` (total `2^n − 1`).
Every piece of `R'` is `≤ 2^{n−1}`. Put `u := (s_1 − 2^{n−1})^+`.

## Lemma A (top-band localization)
```
    ∫_{2^{n-1}}^{∞} 1[c_P(t) odd] dt = u.
```
*Proof.* For `t ≥ 2^{n−1}`, no piece of `R'` exceeds `t` (each is `≤ 2^{n−1} ≤ t`). At most
one `s_i` exceeds `2^{n−1}` (two would sum to `> 2^n = Σ s_i`), and if one does it is `s_1`.
So `c_P(t) = 1[s_1 > t]` there, odd exactly on `2^{n−1} ≤ t < s_1`; integrate. ∎

## Lemma B (half-threshold decoupling)
Let `Q := {min(s_i, 2^{n−1})}_i ∪ R'`. Then
```
    f(P) = u + f(Q),
```
with `Σ(Q) = D_n − u` and every piece of `Q` at most `2^{n−1}`.
*Proof.* For `t < 2^{n−1}`, `min(s_i, 2^{n−1}) > t ⇔ s_i > t`, and `R'` is unchanged, so
`c_P(t) = c_Q(t)`; hence `∫_0^{2^{n-1}} 1[c_P odd] = ∫_0^{2^{n-1}} 1[c_Q odd] = M(Q)` (as all
of `Q` is `≤ 2^{n−1}`). With Lemma A and `f = M` (layer-cake): `f(P) = M(P) = u + M(Q) =
u + f(Q)`. ∎

## Consequence (Corollary C, the u≥1 reduction)
`f(Q) = M(Q) ≥ 0`, so if `u ≥ 1` then `f(P) ≥ 1`. Hence the lower-bound floor `f(P) ≥ 1`
can fail only when `u < 1`, i.e. `s_1 ≤ 2^{n−1} + 1` (top genuinely and finely cut). This
unifies round-1's Case 1 (top uncut) and Case 2 into one identity and isolates the extremal
regime. It does NOT by itself prove `f(P) ≥ 1` in the `u < 1` regime.
