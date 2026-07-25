# Lemma L0 — Claiming lemma (greedy optimal, value = odd-rank sum)

**Status:** CERTIFIED (proof-reviewer, round 2). Numerically re-verified: 0/300 mismatches
against brute-force minimax.

**Statement.** Fix a finite multiset P = {p_1 ≥ … ≥ p_m} of nonnegative reals. Two players
alternately claim one remaining item (player 1 first), each maximizing the sum of items it
claims. Under optimal play, player 1's total equals the odd-rank sum
Σ_odd(P) = p_(1) + p_(3) + p_(5) + …, and taking a currently-largest item is optimal for the
player to move.

**Proof.** The game is constant-sum (total T fixed), so maximizing one's own total equals
minimizing the opponent's. Let V(P) be the mover's optimal total. If the mover takes item i,
the opponent then faces P∖{p_i} and gets V(P∖{p_i}); the mover gets the rest, so
V(P) = T − min_i V(P∖{p_i}).   (∗)

Induct on m; both m=0 (V=0) and m=1 (V=p_1) hold. For the step, by IH V(P∖{x}) is the
odd-rank sum of P∖{x}. Removing the larger of two adjacent-rank items minimizes this: if
i, i+1 are adjacent ranks, M∖{p_(i+1)} is obtained from M∖{p_(i)} by raising one element from
p_(i+1) to p_(i) ≥ p_(i+1); by order-statistic monotonicity (raising one element weakly
increases every order statistic, since N_B(t) ≥ N_R(t) at each threshold t and
x_(j) = sup{t : N(t) ≥ j}), every order statistic weakly increases, so the odd-rank sum
weakly increases: V(P∖{p_(i+1)}) ≥ V(P∖{p_(i)}). Chaining, i=1 minimizes (∗), giving
V(P) = T − Σ_even(P) = Σ_odd(P), and taking a largest item is optimal. ∎

Reusable by every approach; foundational.
