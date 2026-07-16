# Lemma (size-2 Q_lo closure for a perturbed dyadic base): A(R_lo) − A(Q_lo) ≥ A(G_{j−1}) ≥ 1

**Status:** CERTIFIED by proof-reviewer, round 13. Reviewer re-derived Regime A (forcing `p₁=p₂` via
`S_{R_lo}⊆[0,2^j)`) and Regime B (`p₂≥2^j` parity forcing + `p₁≤a`, giving `A(Q_lo)≤a−2^j` and
`A(R_lo)−A(Q_lo)≥2^j−A(G_j)=A(G_{j−1})`) by hand; both correct. Independently verified 0 violations over
18386 off-grid (dens 8) configs with `a∈[1,2^{j+1})` (the lemma's stated scope), `j=1,2,3` — 225 tight at
`A(G_{j−1})`. NOTE: violations appear for `a<1` (e.g. `j=1,a=1/8`), which is OUTSIDE this lemma's scope
`a∈[1,2^{j+1})`; the approach's usage (`a∈[1,2^{n−2})`, `j=n−3`) is entirely `a≥1`, so this is not a gap.
Numerically verified 0-violation with exact Fractions:
- `a < 2^j`: 0 non-equal admissible size-2 pairs exist (`j = 1,2,3`, dens to 8) — vacuousness.
- `a ≥ 2^j`: non-equal admissible pairs exist (34 per `j`) but `min(A(R_lo)−A(Q_lo)) = A(G_{j−1})`,
  0 violations (`j = 1,2,3`).
- Formula `A({a}∪G_j) = a − A(G_j)` for `a ∈ [2^j, 2^{j+1})` verified exact (`j = 1..4`, dens to 4).

## Notation (imported)
`N_P(x) = #{parts of P exceeding x}`, `S_P = {x ≥ 0 : N_P(x) odd}`,
`A(P) = measure(S_P)` (certified `alt-sum-integral`). `G_j = {2^0,…,2^j}`,
`A(G_j) = (2^{j+1}+(−1)^j)/3` (odd `≥ 1`; certified `set-identity-selfsimilar`), with the self-similar
identity `2^j − A(G_j) = A(G_{j−1})`.

## Statement
Let `j ≥ 1`, `a ∈ [1, 2^{j+1})`, `R_lo = {a} ∪ G_j` (so `ΣR_lo = a + 2^{j+1} − 1 ≥ 2^{j+1}`). Let
`Q_lo = {p_1, p_2}` (`p_1 ≥ p_2 ≥ 0`) satisfy `S_{Q_lo} ⊆ S_{R_lo}` and `ΣQ_lo > ΣR_lo`. Then
```
A(R_lo) − A(Q_lo) ≥ A(G_{j−1}) ≥ 1.
```

## Proof
`p_1 + p_2 = ΣQ_lo > ΣR_lo ≥ 2^{j+1}` with `p_1 ≥ p_2` gives `p_1 > 2^j`.

**Regime A: `a < 2^j`.** Then `max(R_lo) = 2^j`, so `N_{R_lo}(x) = 0` for `x ≥ 2^j`, i.e.
`S_{R_lo} ⊆ [0, 2^j)`. If `p_1 > p_2`, then `S_{Q_lo} = [p_2, p_1)` (as `N_{Q_lo} = 2` on `[0,p_2)`,
`= 1` on `[p_2,p_1)`, `= 0` above) contains the non-empty interval `(2^j, p_1)`, which is disjoint from
`S_{R_lo} ⊆ [0,2^j)` — contradicting `S_{Q_lo} ⊆ S_{R_lo}`. Hence `p_1 = p_2`, `S_{Q_lo} = ∅`,
`A(Q_lo) = 0`, and `A(R_lo) − A(Q_lo) = A(R_lo) ≥ A(G_{j−1})` by the **Floor Lemma**
(`floor-a-union-Gj`).

**Regime B: `a ∈ [2^j, 2^{j+1})`.** Here `a = max(R_lo) ≥ 2^j ≥` every part of `G_j`, so
`N_{R_lo}(x) = 1` on `[2^j, a)`, `= 0` on `[a,∞)`, and `= N_{G_j}(x) + 1` on `[0,2^j)`. Thus
`S_{R_lo} = ([0,2^j) ∖ S_{G_j}) ∪ [2^j, a)` and `A(R_lo) = (2^j − A(G_j)) + (a − 2^j) = a − A(G_j)`.
- If `p_1 = p_2`: `A(Q_lo) = 0`, `A(R_lo) − A(Q_lo) = A(R_lo) ≥ A(G_{j−1})` (Floor Lemma).
- If `p_1 > p_2`: `S_{Q_lo} = [p_2, p_1)`, `p_1 > 2^j`. Its part above `2^j`, `(\max(p_2,2^j), p_1)`,
  must lie in `S_{R_lo} ∩ (2^j,∞) = (2^j, a)`, forcing `p_1 ≤ a`. And `p_2 ≥ 2^j`: otherwise
  `[p_2,p_1)` meets `[2^{j−1}, 2^j)`, where `N_{R_lo} = N_{G_j}(=1) + 1 = 2` is even, so that portion is
  not in `S_{R_lo}` — a contradiction. Hence `[p_2,p_1) ⊆ [2^j,a)` and `A(Q_lo) = p_1 − p_2 ≤ a − 2^j`,
  so `A(R_lo) − A(Q_lo) ≥ (a − A(G_j)) − (a − 2^j) = 2^j − A(G_j) = A(G_{j−1})`.

In all cases `A(R_lo) − A(Q_lo) ≥ A(G_{j−1}) ≥ 1` (`A(G_{j−1})` odd `≥ 1`). ∎

## Consequence (in ll-inclusion-gap)
For the `a ≥ 1` top cut `2^{n−1}→{a,2^{n−1}−a}` (`j = n−3`), the `h=2` Gen-Decomp branch with a
**size-2** `Q_lo`: `deficit_top = a_v + b ≥ 0`, `A(R_lo)−A(Q_lo) ≥ 1 ≥ 1 − deficit_top`, hence
`A(R)−A(Q) = deficit_top + (A(R_lo)−A(Q_lo)) ≥ 1`. Combined with the certified **Parity-Condition
Lemma** (even `|R_lo|` forces even `|Q_lo|`, excluding odd sizes at even `j`), this closes all
`|Q_lo| ≤ 2` cases for every `n` and every `a ∈ [1,2^{n−2})`.

## Scope / open
Does NOT cover `|Q_lo| ≥ 3` distinct-top configs, which are genuinely **tight** (`A(R)−A(Q)=1` at
`n=6, a=2, Q_lo={8,4,3,3}`) and remain open.
