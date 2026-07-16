# Lemma MK — μ(k pieces, k−1 cuts) ≤ min(pieces)

**Status:** CERTIFIED (round 11 proof-reviewer). Reviewer re-derived the induction from scratch (bases
k=1,2 + midpoint-halve-then-recurse step; parity-invisibility of the equal pair keeps `A` unchanged;
budget `1+(k-2)=k-1`) — airtight. Corollary MK.1 (δ≤t and d_j≤t easy cases) re-checked: both give
`μ(X,m-1)≤t` at tight budget, uniform in m. Numerically verified: constructive MK strategy attains
`A ≤ min(X)` with 0 violations / 4000 random rational multisets (`k = 1..6`).

## Statement
Let `X` be a finite multiset of `k ≥ 1` positive lengths, and let the cut budget be `b = k − 1`. Then
```
μ(X, k−1) ≤ min(X),
```
where `μ(X, b) = min` over placements of `≤ b` interior cut points of `A(result)`, and
`A(P) = measure{x ≥ 0 : N_P(x) odd}` (Lemma M0, `alt-sum-integral.md`). `min(X)` is the smallest part.

## Proof (induction on k)
Sort `X = {p₁ ≥ p₂ ≥ … ≥ p_k}` descending, so `min(X) = p_k`. We exhibit a legal Xiang-Yu strategy
using at most `k − 1` cuts whose final alternating sum is `≤ p_k`.

Recall the **parity-invisibility** fact (certified, Lemma R1 `sum-bound-reductions.md`): if a multiset
contains two equal parts `{w, w}`, they contribute an even amount `2·𝟙[w > x]` to `N(·)` at every `x`,
so deleting them leaves `A` unchanged; equivalently, cutting a piece `a` at interior offset `w < a` (one
cut) to create a fresh `w` that pairs with an existing `w` leaves an effective piece `a − w` and does not
change `A` relative to the multiset `(X ∖ {a, w}) ∪ {a − w}`.

**Base `k = 1`.** Budget `0`. `A(X) = A({p₁}) = measure[0, p₁) = p₁ = min(X)` (Lemma M0). So
`μ(X, 0) = A(X) = p₁ = min(X) ≤ min(X)`. ✓

**Base `k = 2`.** `X = {p₁ ≥ p₂}`, budget `1`. Cut `p₁` at interior offset `p₂` (legal since
`0 < p₂ ≤ p₁`; if `p₁ = p₂` take the midpoint, offset `p₂ = p₁/2 < p₁`). The fresh `p₂` pairs with the
existing `p₂` (parity-invisible), leaving the single effective piece `p₁ − p₂`, so
`A = measure[0, p₁ − p₂) = p₁ − p₂`. Since `p₁ ≤ p₁ + p₂` gives `p₁ − p₂ ≤ p₂`... more directly, we may
instead cut `p₁` at its **midpoint** into `{p₁/2, p₁/2}` (an equal pair, invisible), leaving effective
`{p₂}`, giving `A = p₂ = min(X)`. Hence `μ(X, 1) ≤ p₂ = min(X)`. ✓

**Inductive step `k ≥ 3`.** Assume the claim for `k − 1`. Xiang Yu first cuts the largest piece `p₁` at
its midpoint into two equal halves `{p₁/2, p₁/2}` (one cut, legal: `0 < p₁/2 < p₁`). This equal pair is
parity-invisible, so for every subsequent play on the remaining pieces `X ∖ {p₁} = {p₂, …, p_k}`,
```
A(final over all physical pieces) = A(play on {p₂, …, p_k}).
```
Xiang Yu now plays the optimal MK strategy on the `k − 1` pieces `{p₂, …, p_k}` with the remaining
budget `k − 2 = (k−1) − 1`. By the induction hypothesis,
```
A(play on {p₂, …, p_k}) ≤ μ({p₂, …, p_k}, k−2) ≤ min({p₂, …, p_k}) = p_k = min(X).
```
The total number of cuts is `1 + (k − 2) = k − 1 = b`, all interior to distinct current pieces (the
midpoint of `p₁`, then the interior MK cuts on `{p₂,…,p_k}`), hence a legal placement. Therefore
`μ(X, k−1) ≤ min(X)`. ∎

## Corollary MK.1 (uniform easy-case tool, tight budget b = m−1)
Let `X = {p₁ > … > p_m}` be `m` distinct pieces, `Σ = Σpᵢ`, budget `b = m − 1`, and `t > 0` a threshold.
Write `d_j = p_j − p_{j+1}` (`1 ≤ j ≤ m−1`) and `δ = p_m`.
- **If `δ ≤ t`:** apply Lemma MK to `X` directly (`m` pieces, `m−1` cuts):
  `μ(X, m−1) ≤ min(X) = δ ≤ t`.
- **If `d_j ≤ t` for some `j`:** Xiang Yu makes the single pairing cut of `p_j` at interior offset
  `p_{j+1}` (legal, `0 < p_{j+1} < p_j`); the fresh `p_{j+1}` pairs with the existing `p_{j+1}`
  (invisible), leaving the `m − 1` effective pieces
  `Y = {p₁, …, p_{j−1}, d_j, p_{j+2}, …, p_m}`. Xiang Yu then applies Lemma MK to `Y` (`m−1` pieces,
  `m−2` remaining cuts), giving `A ≤ min(Y) ≤ d_j ≤ t` (since `d_j ∈ Y`). Total cuts
  `1 + (m−2) = m−1 = b`. Hence `μ(X, m−1) ≤ t`.

In both cases `μ(X, m−1) ≤ t`. This closes **every** residual gap-case instance in which some adjacent
difference `d_j`, or the minimum part `δ`, is `≤ t` — uniformly in `m`.

## Scope
Lemma MK is unconditional. Corollary MK.1 discharges the "easy" sub-cases of the residual gap case at
tight budget for all `m`. It does **not** close the hard sub-case (all `d_j > t` and `δ > t`), which
remains the open frontier of the upper bound for `m ≥ 5`.
