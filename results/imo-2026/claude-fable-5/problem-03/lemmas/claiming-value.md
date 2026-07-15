# Lemma: claiming-value (certified, round 1)

**Statement.** In the alternating claiming game on a finite multiset P of nonnegative reals (players alternately claim one unclaimed element, first player moves first, each maximizes his own total), the first player can guarantee at least Odd(P) = p_1 + p_3 + ⋯ and the second at least Even(P) = p_2 + p_4 + ⋯ (sorted decreasingly, any tie-breaking). Since the totals sum to ΣP, under optimal play the first player's total is exactly Odd(P).

**Proof.** Simultaneous strong induction on |P| for the two one-sided guarantees.

(i) *First player ≥ Odd(P).* For |P| ≤ 1 clear. Otherwise claim p_1 and follow the strategy of (ii) as second player on P′ = P ∖ {p_1} (sorted p_2 ≥ p_3 ≥ ⋯), collecting in addition at least Even(P′) = p_3 + p_5 + ⋯. Total ≥ p_1 + p_3 + ⋯ = Odd(P).

(ii) *Second player ≥ Even(P).* For |P| ≤ 1, Even(P) = 0. Suppose the first player claims p_j.
- If j = 1: reply p_2; by induction on Q = P ∖ {p_1, p_2}, collect in addition ≥ Even(Q) = p_4 + p_6 + ⋯. Total ≥ p_2 + p_4 + ⋯ = Even(P).
- If j > 1: reply p_1; let Q = P ∖ {p_1, p_j} with sorted list q_i = p_{i+1} for i ≤ j−2 and q_i = p_{i+2} for i ≥ j−1; in both cases q_i ≥ p_{i+2}. Hence Even(Q) = Σ_{i even} q_i ≥ p_4 + p_6 + ⋯ = Even(P) − p_2, and by induction the total is ≥ p_1 + Even(Q) ≥ p_1 + Even(P) − p_2 ≥ Even(P), since p_1 ≥ p_2. ∎

**Notes.** Covers zeros and ties (zeros sort last and contribute 0, so appending zero-length pieces changes neither value). Reviewer verification: brute-force game-tree search on 300 random multisets (with ties and zeros) matches Odd(P) exactly.
