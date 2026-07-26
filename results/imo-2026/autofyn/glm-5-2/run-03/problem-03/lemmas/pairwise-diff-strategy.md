# Lemma: pairwise-difference strategy (equal-halve the complement)

## Status
PROVED (general n ≥ 2). Certified round 4 by proof-reviewer (verified 9000 checks, error 0).

## Statement

> **Lemma (pairwise-difference realization).** For `n ≥ 2`, let Liu Bang's pieces be `p_1 ≥ p_2 ≥ … ≥ p_{n+1}` summing to 1. For any pair `{i, j}` with `1 ≤ i < j ≤ n+1`, Xiang Yu equal-halves the `n − 1` pieces NOT in `{i, j}` (using `n − 1 ≤ n` marks), leaving `p_i` and `p_j` unsplit. Then
> `D = p_i − p_j`  (regime-independent; the value depends only on the multiset, not the sort order).

Equivalently: Xiang has a strategy using `n − 1` marks attaining `D = p_i − p_j` for any desired pairwise difference, at every `n ≥ 2`.

## Proof

Equal-halving a piece `p_k` into `p_k/2 + p_k/2` creates two equal pieces. In the final multiset, the `n − 1` equal-halved pieces give `n − 1` equal pairs `(p_k/2, p_k/2)` for `k ∉ {i, j}`. The two unsplit pieces `p_i, p_j` remain as singletons.

Sort descending. The `n − 1` equal pairs occupy `2(n−1)` consecutive ranks (each pair at ranks `(r, r+1)` for some `r`); each pair contributes `±(p_k/2 − p_k/2) = 0` to `D` (sign irrelevant). The two singletons `p_i, p_j` occupy the remaining 2 ranks. Since the pairs are parity-neutral (cancel in `D`), the only surviving contribution is from `p_i` and `p_j`, giving `D = ±(p_i − p_j)`. The lone `p_i` (the larger, at the higher rank) is at an odd rank (the pairs, being even-sized blocks, force the two singletons to occupy one odd and one even rank), so `D = +(p_i − p_j)` when `p_i ≥ p_j`. ∎

(Equivalently via the parity-integral / peeling lemma: each equal-halve creates a parity-neutral equal pair (`+2 · 1_{[0, p_k/2)}` is even); removing all `n − 1` pairs leaves `D = D` of `{p_i, p_j}` `= |p_i − p_j| = p_i − p_j` for `p_i ≥ p_j`.)

**Regime independence.** `D` as the alternating sum of the descending sort (or equivalently the parity integral) depends only on the multiset of piece lengths, not the stick positions. The equal-pair-cancels property holds in every sort regime (two equal pieces always occupy adjacent ranks). So `D = p_i − p_j` is a single formula, valid for all `p_1 ≥ … ≥ p_{n+1}`.

## Verification

Sort-computed (Python `fractions`, direct sort) on 3000 random n=3 configs (4 pieces): all 6 pairwise differences `{p_1−p_2, p_1−p_3, p_1−p_4, p_2−p_3, p_2−p_4, p_3−p_4}` match the multiset D-value exactly (max error 0 over 9000 checks). For n=2 this recovers the `C3` strategy of `pairing-charging` §6.3 (EH `p_3` → `D = p_1 − p_2`).

## Import notes

- Reusable by any approach needing a `≤ n`-mark strategy attaining a specific pairwise difference `p_i − p_j` at general n.
- For n=3 this gives 6 explicit 2-mark strategies (one per pair), a key ingredient of the minimax-strategy-family's enriched family.
- The pairwise differences form a lower bound on the achievable D-values; the minimax over them plus `p_{n+1}` (equal-halve-n-largest) and peel-complements gives a clean (but for n ≥ 3 insufficient) family for the upper bound.
