# Lemma: greedy-alternating claim

## Statement

Let `m ≥ 1` pieces of lengths `a_1 ≥ a_2 ≥ … ≥ a_m ≥ 0` (sorted descending, ties allowed) be claimed alternately by two players, Liu Bang first, each maximizing their own total. (The total need not be 1.) Under optimal play by both:

- Liu Bang's payoff is `S_odd := a_1 + a_3 + a_5 + …` (the odd-position sum of the descending sort).
- Xiang Yu's payoff is `S_even := a_2 + a_4 + … = T − S_odd`, where `T = Σ a_i`.
- The greedy strategy "always take the largest remaining piece" is optimal for **both** players (an equilibrium attaining these payoffs).

**Corollary (universal floor).** `S_odd ≥ T/2`, since `a_{2k−1} ≥ a_{2k}` pairwise gives `S_odd − S_even = Σ_k (a_{2k−1} − a_{2k}) ≥ 0`. Equality iff `a_{2k−1} = a_{2k}` for every pair.

## Proof (strong induction on m; source: dyadic-induction §1, the most explicit version)

Base `m ∈ {0, 1}`: trivial (`m = 1`, Liu takes `a_1 = S_odd`).

Inductive step. Assume the claim for all multisets of size `< m`; consider size `m ≥ 2`. If Liu's first move takes `a_i`, the remaining `m − 1` pieces (still sorted descending after deletion) are played with **Xiang moving first**; by the induction hypothesis applied to that `(m−1)`-piece subgame, Xiang gets its odd-position sum and Liu gets its even-position sum. Write `b_1 ≥ … ≥ b_{m−1}` for the remainder (`b_j = a_j` for `j < i`, `b_j = a_{j+1}` for `j ≥ i`). Then

> Liu's total after first taking `a_i` = `a_i + E_i`, where `E_i := b_2 + b_4 + b_6 + …` (even positions of the remainder).

Compare `E_i` to `E_1` by parity. Let `k = ⌊i/2⌋` (for `i = 1`, take `k = 0`).

- **`i = 1` (k = 0):** `E_1 = a_3 + a_5 + a_7 + …`, so Liu's total `= a_1 + a_3 + … = S_odd`.
- **`i = 2k` (k ≥ 1, even i):** the even-indexed `b`'s are `b_2, b_4, …, b_{2k−2} = a_2, a_4, …, a_{2k−2}` (since `2j < 2k ⟺ j < k`) followed by `b_{2k}, b_{2k+2}, … = a_{2k+1}, a_{2k+3}, …` (since `2j ≥ 2k ⟺ j ≥ k`). Hence
  `E_{2k} = (a_2 + a_4 + … + a_{2k−2}) + (a_{2k+1} + a_{2k+3} + …)`,
  and `S_odd − (a_{2k} + E_{2k}) = Σ_{j=1}^{k} (a_{2j−1} − a_{2j}) =: Δ_k ≥ 0`, because `a_{2j−1} ≥ a_{2j}` (sorted). So `total(2k) = S_odd − Δ_k ≤ S_odd`.
- **`i = 2k+1` (k ≥ 1, odd i ≥ 3):** the even-indexed `b`'s are `b_2, …, b_{2k} = a_2, …, a_{2k}` (since `2j ≤ 2k < 2k+1 ⟺ j ≤ k`) followed by `b_{2k+2}, b_{2k+4}, … = a_{2k+3}, a_{2k+5}, …`. Hence
  `E_{2k+1} = (a_2 + … + a_{2k}) + (a_{2k+3} + a_{2k+5} + …)`,
  and `S_odd − (a_{2k+1} + E_{2k+1}) = Σ_{j=1}^{k} (a_{2j−1} − a_{2j}) = Δ_k ≥ 0`. So `total(2k+1) = S_odd − Δ_k ≤ S_odd`.

Thus for every `i ≥ 2`, Liu's total after first taking `a_i` is `S_odd − Δ_k ≤ S_odd`, with `Δ_k ≥ 0` (equality iff `a_{2j−1} = a_{2j}` for all `j ≤ k`, which is consistent with ties). The maximum over `i` is attained at `i = 1`, value `S_odd`: taking `a_1` (greedy) is optimal for Liu. By the induction hypothesis the same greedy principle governs every subsequent move of both players. ∎

## Verification

Independently checked by exhaustive computation of `total(i)` for `i = 1, …, m` against `S_odd − Δ_k` on random sorted multisets with ties — the exchange deficit `Δ_k = Σ_{j=1}^{k} (a_{2j−1} − a_{2j})` reproduces `S_odd − total(i)` exactly in every case. (See proof-reviewer round 1 verification script.)

## Certification

Reviewer-certified round 1 (proof-reviewer, imo-2026-03). The statement is proved `sorry`-free, every case (even `i`, odd `i`, ties) is handled by the explicit `Δ_k` formula, and the conclusion is no stronger than what the proof establishes. Importable by any approach instead of re-proving; the sibling approaches (`pairing-charging`, `alternating-potential`, `surrogate-adversary`) may replace their greedy-lemma sections with a reference to this file.
