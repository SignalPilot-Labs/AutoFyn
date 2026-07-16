# Lemma (Top-band decomposition identity, INC branch, R = G_{n−1})

**Status:** CERTIFIED (proof-reviewer, round 6). Proposed by `ll-inclusion-gap`. Reviewer re-derived
(a)–(d) from scratch and machine-verified the identity `A(G_{n−1}) − A(Q) = deficit_top + M` with both
terms `≥ 0` over all n=3 (R=G_2) and n=4 (R=G_3) budget-valid INC configs (0 failures; min margin 1).
The identity is proven; the resulting inequality `deficit_top + M ≥ 1` (G-INC-1) is NOT closed.

## Statement
Assume the INC branch `S_Q ⊆ S_{G_{n−1}}`, `n ≥ 2`, with `Q` partitioning `2^n`. Put `thr := 2^{n−2}`,
`I_{n−1} := [thr, 2^{n−1})`, split `Q` at `thr` into `Q_hi = {parts ≥ thr}` (`h := |Q_hi|`) and
`Q_lo = {parts < thr}`, and set `δ_top := measure(S_Q ∩ I_{n−1})`. Then:
- **(a)** `h` is even;
- **(b)** `A(Q) = A(Q_lo) + δ_top`;
- **(c)** `A(Q_lo) ≤ 2^{n−2} − A(G_{n−2})`;
- **(d)** `A(G_{n−1}) − A(Q) = deficit_top + M`, where `deficit_top := 2^{n−2} − δ_top ≥ 0` and
  `M := 2^{n−2} − A(G_{n−2}) − A(Q_lo) ≥ 0`.

## Proof
**(a)** The band `I_{n−2} = [2^{n−3}, 2^{n−2})` is forbidden (`N_{G_{n−1}} = 2`); by (P2) of the
Parity-Condition Lemma (`lemmas/parity-condition-inc.md`), `#{parts ≥ 2^{n−2}} = h` is even. (For
`n = 2` read the band as `I_0` with `N = 2`.)

**(b)** All `h` high parts exceed every `x < thr`, so on `[0,thr)`, `N_Q(x) = h + N_{Q_lo}(x) ≡
N_{Q_lo}(x) (mod 2)` (`h` even), giving `S_Q ∩ [0,thr) = S_{Q_lo}`, measure `A(Q_lo)`. On `I_{n−1}` the
contribution is `δ_top`; above `2^{n−1}` there is no `S_Q`-mass (Forcing Lemma). Sum gives (b).

**(c)** On `[0,thr)`, `G_{n−1} = G_{n−2} ∪ {2^{n−1}}` and `2^{n−1} > x`, so
`N_{G_{n−1}} = N_{G_{n−2}} + 1`, i.e. `S_{G_{n−1}} ∩ [0,thr) = [0,thr) ∖ S_{G_{n−2}}`. From INC,
`S_{Q_lo} = S_Q ∩ [0,thr) ⊆ S_{G_{n−1}} ∩ [0,thr)`, so
`A(Q_lo) ≤ measure([0,thr) ∖ S_{G_{n−2}}) = 2^{n−2} − A(G_{n−2})`.

**(d)** `S_{G_{n−1}} ∩ I_{n−1} = I_{n−1}` (there `N_{G_{n−1}} = 1`), so
`A(G_{n−1}) = 2^{n−2} + (2^{n−2} − A(G_{n−2})) = 2^{n−1} − A(G_{n−2})`. Subtract (b):
`A(G_{n−1}) − A(Q) = (2^{n−2} − δ_top) + (2^{n−2} − A(G_{n−2}) − A(Q_lo)) = deficit_top + M`.
`deficit_top ≥ 0` since `δ_top ≤ measure(I_{n−1}) = 2^{n−2}`; `M ≥ 0` by (c). ∎

## Scope
Reduces the general-n INC "+1" target (`A(Q) ≤ A(G_{n−1}) − 1`, equivalently `A(Q∪R) ≥ 1`) to the
single scalar inequality **(G-INC-1)** `deficit_top + M ≥ 1`, both summands `≥ 0`, the unit excess
`ΣQ − ΣG_{n−1} = 1` distributing between them. G-INC-1 is OPEN. The identity holds only for
`R = G_{n−1}` (unrefined); refined R (G-INC-2) needs `S_R`'s own level structure and is also open.
