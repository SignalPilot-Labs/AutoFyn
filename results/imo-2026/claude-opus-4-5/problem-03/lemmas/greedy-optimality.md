# Greedy Optimality Lemma

**Statement:** In a piece-claiming game where players alternate taking pieces and each wants to maximize their total length, greedy play (always take the largest available piece) is optimal for both players.

**Precise formulation:** Let {a_1, ..., a_m} be pieces with positive lengths. Under alternating greedy play starting with player 1, player 1 takes odd positions from the decreasing-sorted order. No deviation improves either player's total.

**Proof:** By backward induction on the number of remaining pieces.

*Base case:* When one piece remains, there is no choice.

*Inductive step:* Suppose the claim holds for at most k pieces. With k+1 pieces, suppose player A deviates by taking piece x when a larger piece y > x is available. The opponent then takes y. Compared to the strategy of taking y first:
- A's immediate gain changes by x - y < 0.
- The remaining game (with k pieces, opponent to move) is identical in both cases (same remaining pieces).

Thus A is strictly worse off. By induction, greedy play is optimal for both players.

**Certified:** Round 3
