# Lemma Floor (analytic floor for a single dyadic perturbation): A({a}∪G_j) ≥ A(G_{j−1}), = iff a=2^j

**Status:** CERTIFIED (round 12, reviewer-verified). Numerically verified 0-violation `j = 1..6`
(reviewer re-verified with exact Fractions: min at `a=2^j`, value `A(G_{j-1})`, equality only at `a=2^j`).
The proof (measure form `S_W = S_{G_j} △ [0,a)`, band-slope count `f'=∓1`, strictly-decreasing minima
`f(2^{i+2})−f(2^i)=−2^i<0`, value `2^j−A(G_j)=A(G_{j−1})`) was re-derived from scratch and is rigorous.

## Notation (imported)
`N_P(x) = #{parts of P exceeding x}`, `S_P = {x ≥ 0 : N_P(x) odd}`,
`A(P) = measure(S_P) = Σ_i(−1)^{i+1}p_i` (parts sorted `p_1 ≥ p_2 ≥ …`; certified `alt-sum-integral`).
`G_j = {2^0,…,2^j}`, `A(G_j) = (2^{j+1}+(−1)^j)/3` (odd, `≥ 1`; certified `set-identity-selfsimilar`).

## Statement
For every integer `j ≥ 1` and every real `a > 0`:
`A({a}∪G_j) ≥ A(G_{j−1})`, with equality **iff** `a = 2^j`.

In particular (at `j = n−3`) `A({a}∪G_{n−3}) ≥ A(G_{n−4}) ≥ 1`, equality iff `a = 2^{n−3}`; and
`A(G_{n−4}) = 1` iff `n ∈ {4,5}` (else `≥ A(G_2) = 3`).

## Proof
Let `W := {a}∪G_j`, `f(a) := A(W) = measure(S_W)`. Adding the single part `a` flips the parity of
`N_W` relative to `N_{G_j}` exactly on `[0,a)`, so `S_W = S_{G_j} △ [0,a)`. By
`measure(X△Y) = measure(X) + measure(Y) − 2·measure(X∩Y)`,
```
f(a) = A(G_j) + a − 2·g(a),   g(a) := measure(S_{G_j} ∩ [0,a)).
```
**Band structure of `S_{G_j}`.** With `B_0 := [0,1)`, `B_i := [2^{i−1},2^i)` (`1 ≤ i ≤ j`),
`N_{G_j} = j+1` on `B_0`, `= j+1−i` on `B_i`, `= 0` on `[2^j,∞)`. So `B_i ⊆ S_{G_j}` iff `i ≡ j (mod 2)`
("allowed"); `measure(B_0)=1`, `measure(B_i)=2^{i−1}`.

**Slope of `f`.** `g` has slope `1` on allowed bands, `0` on forbidden bands and on `(2^j,∞)`; hence
`f' = 1 − 2g'` equals `−1` on allowed bands, `+1` on forbidden bands and on `(2^j,∞)`. So `f` decreases
across allowed bands, increases across forbidden bands; its local minima are exactly at `a = 2^i` for
allowed `i` (a decreasing-then-increasing corner), i.e. `i ∈ {j, j−2, j−4, …}`.

**Minima strictly decrease toward `i = j`.** For allowed `i ≤ j−2`, between `2^i` and `2^{i+2}` sit the
forbidden band `B_{i+1}` (slope 0) and the allowed band `B_{i+2}` (measure `2^{i+1}`), so
`g(2^{i+2}) − g(2^i) = 2^{i+1}` and
`f(2^{i+2}) − f(2^i) = (2^{i+2}−2^i) − 2·2^{i+1} = 3·2^i − 4·2^i = −2^i < 0`.
Thus the smallest local minimum is at `a = 2^j`. For `a > 2^j`, `f(a) = a − A(G_j)` strictly increasing;
as `a → 0⁺`, `f → A(G_j) > A(G_{j−1})`. Hence the global minimum on `(0,∞)` is uniquely at `a = 2^j`.

**Value at `a = 2^j`.** `W = {2^j,2^j} ∪ {2^{j−1},…,1}`; the two leading `2^j` (positions 1,2, signs
`+,−`) cancel, and the remainder `{2^{j−1},…,1}` keeps its own alternating sum, so `f(2^j) = A(G_{j−1})`.
(Check: `2^j − A(G_j) = (2^j − (−1)^j)/3 = A(G_{j−1})`.)

Therefore `f(a) ≥ A(G_{j−1})` for all `a > 0`, equality iff `a = 2^j`. ∎

## Scope
The analytic floor underpinning Opening C for G-INC-2nt `a ≥ 1` in `ll-inclusion-gap`: after one
Gen-Decomp step the sub-base is `R_lo = {a}∪G_{n−3}`, and this lemma gives `A(R_lo) ≥ 1` unconditionally,
pinning the tight case to `a = 2^{n−3}`, `n ∈ {4,5}`. It does NOT by itself close `a ≥ 1`: bounding
`A(Q_lo)` against `A(R_lo)` (the DFB `A(R_lo)−A(Q_lo) ≥ min(σ_lo,2−σ_lo)`, equiv. `O_{Q_lo} ≤ O_{R_lo}+a_v`)
remains the open crux for general `h=2`.
