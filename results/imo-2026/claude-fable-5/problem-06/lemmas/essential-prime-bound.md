# Lemma: essential-prime-bound (with Exclusion Principle and Quantitative Witness)

Certification: **CERTIFIED** (round 1, proof-reviewer). Proved in full in `approaches/crt-window-small-prime-lockin.md` Steps 4–6 (reproduced in `current.md`); every step re-derived independently by the reviewer, descent logic checked case by case, and the necessity of the weakened bound confirmed computationally (a_1 = 385: A = {2,7}, g = 14, yet {2,11,19} ∈ M with 19 > g; and 19 < a_1·g).

## Setting

Notation as in `terms-equal-valid-set.md` and `dodging-and-witness.md`: greedy sequence, terms, types P(·), valid set V, hitting family H\*, minimal antichain M; fix A ∈ M and g := ∏_{p∈A} p.

## Statements

**(EP) Exclusion Principle** (= (L1.5) restated): if m > a_1 is not a term, there is a term t < m with gcd(t, m) = 1.

**(QW) Quantitative Witness.** Let Y ∈ M with |Y| ≥ 2, ρ ∈ Y, and let m be any integer with m ≥ a_1 and P(m) = Y ∖ {ρ}. Then there is U ∈ M with ρ ∈ U, U ∩ Y = {ρ}, and ∏_{p∈U} p < m; in particular ρ < m.

**(EPB) Essential prime bound.** No member of M contains a prime ρ ≥ a_1·g. Hence E := ∪M ⊆ {primes < a_1·g} is finite, and M is finite (M ⊆ 2^E).

## Proofs

**(EP).** This is (L1.5) of `terms-equal-valid-set.md` (certified there); non-terms m ≥ a_1 are exactly the m ∉ V by (L1.2).

**(QW).** X := Y ∖ {ρ} is nonempty and, by minimality of Y, X ∉ H\*. Since P(a_1) ∈ H\*, m ≠ a_1, so m > a_1; and m is not a term (terms have types in H\* by (L1.3)). By (EP) there is a term t < m with gcd(t, m) = 1, i.e. P(t) ∩ X = ∅. P(t) ∈ H\* meets Y (L1.4b), and P(t) ∩ Y ⊆ Y ∖ X = {ρ}, so P(t) ∩ Y = {ρ}. By (L1.4c) pick U ∈ M with U ⊆ P(t); then ∅ ≠ U ∩ Y ⊆ {ρ}, so U ∩ Y = {ρ} and ρ ∈ U, and ∏_{p∈U} p ≤ ∏_{p∈P(t)} p ≤ t < m; also ρ ≤ ∏_{p∈U} p < m. ∎

**(EPB).** Suppose ρ ≥ a_1·g is a prime in some Y_1 ∈ M. Then ρ > g ≥ every element of A, so ρ ∉ A; and every Z ∈ M containing ρ meets A (L1.4b), hence has |Z| ≥ 2. Recursively, with X_i := Y_i ∖ {ρ} (nonempty), c_i := ∏_{p∈X_i} p ≥ 2, and s_i ∈ Y_i ∩ A ⊆ X_i (so s_i ≤ g):

- If c_i ≥ a_1: apply (QW) with m = c_i (note P(c_i) = X_i) to get Y_{i+1} ∈ M with ρ ∈ Y_{i+1} and ρ·c_{i+1} = ∏_{p∈Y_{i+1}} p < c_i, so c_{i+1} < c_i/2 < c_i.
- If c_i < a_1: let j ≥ 1 be minimal with s_i^j c_i ≥ a_1 and set m := s_i^j c_i. Then P(m) = X_i, m ≥ a_1, and m = s_i·(s_i^{j−1} c_i) < s_i·a_1 ≤ g·a_1 ≤ ρ; but (QW) gives ρ < m — contradiction.

The first case strictly decreases the positive integer c_i, so it cannot repeat forever (well-ordering); hence the second case is reached and yields the contradiction. ∎

## Remark (sharpness)

The strict lock-in "∪M ⊆ {p ≤ g}" is FALSE: for a_1 = 385 (computed round 1), A = {2,7}, g = 14, but {2, 11, 19} ∈ M contains 19 > g. The bound 19 < a_1·g = 5390 of (EPB) holds. So (EPB)'s weakened bound is necessary, not cosmetic.
