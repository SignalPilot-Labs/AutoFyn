# Lemma: cross-piece equal-pair (double-peel) cheap-kill

## Status
PROVED (round 5, by `lp-dual-region`). Certified round 5 by proof-reviewer (independently re-derived the `+2+2` even-parity identity; exact-rational verification 0/3000 failures for n=2,3,4; worst-14 config D=0 exact).

## Statement

> **Lemma (cross-piece equal-pair / double-peel).** Let `S = {p_1, …, p_{n+1}}` be Liu's `(n+1)`-piece multiset (sum 1). Suppose three distinct indices `k, i, j` satisfy `p_k = p_i + p_j` (so `p_k` is the largest of the three, and `p_i, p_j` are existing pieces). Xiang Yu splits `p_k` into `p_i + p_j` (one mark; legal since `p_i + p_j = p_k`). Then the final multiset contains two copies of `p_i` and two copies of `p_j` — two cross-piece equal pairs, each parity-neutral — and
> `D_final = D_rest`,  where `rest := S \ {p_k, p_i, p_j}`  (an `(n−2)`-piece multiset of total `1 − 2 p_k`).
> Xiang retains `n − 1` marks for the rest.

## Proof (via the parity-integral lemma)

Let `j_old, j_new, j_rest` be the `j`-functions before the split, after, and on the rest. After splitting `p_k → p_i + p_j`, the multiset is `(S \ {p_k}) ∪ {p_i (new), p_j (new)}`, so the original copies of `p_i` and `p_j` remain and there are now two copies of each. Hence

`j_new(t) = j_old(t) − [p_k ≥ t] + [p_i ≥ t] + [p_j ≥ t]`.

The rest removes `p_k`, one copy of `p_i`, and one copy of `p_j`:

`j_rest(t) = j_old(t) − [p_k ≥ t] − [p_i ≥ t] − [p_j ≥ t]`.

Subtracting:

`j_new(t) − j_rest(t) = 2 [p_i ≥ t] + 2 [p_j ≥ t]`.

This difference is **even for every `t`** (a multiple of 2), so `j_new(t)` and `j_rest(t)` have the **same parity** for every `t`. By the parity-integral lemma (`D = ∫ [j odd]`),

`D_final = ∫ [j_new odd] dt = ∫ [j_rest odd] dt = D_rest`. ∎

**Total of the rest.** `∑ rest = 1 − p_k − p_i − p_j = 1 − 2 p_k` (since `p_k = p_i + p_j`).

**Comparison with the (single) peeling lemma.** The certified `peeling` lemma splits `p_k → p_j + (p_k − p_j)`, creating one equal pair `(p_j, p_j)` and a leftover `(p_k − p_j)`. The double-peel is the degenerate case `p_k − p_j = p_i` (the leftover equals an existing piece): then the leftover also forms an equal pair, so one mark kills two pairs. This is the lever no within-piece finite family can reach: those families equal-halve *within* pieces; the double-peel equalizes *across* pieces.

**Regime independence.** `D_rest` is the alternating sum of the descending sort of the rest multiset — a function of the multiset alone. So `D_final = D_rest` is a single formula, valid in every sort regime.

## Verification

Exact-rational (`fractions`), n ∈ {2,3,4}, 3000 random configs each with one piece forced to equal the sum of two others: **0 failures** for all n. The worst-14 round-4 config `(5/11, 3/11, 2/11, 1/11)` (where `p_1 = p_2 + p_3 = 5/11`) gives `D_final = 0` exactly via this one mark.
