# Lemma G — Greedy optimality of the claiming game (odd-index sum)

**Status:** certified (proof-reviewer, round 2) — proof re-derived and confirmed; value equals Σ_odd verified against brute-force minimax on 2000 random multisets (0 mismatches).

## Statement
Let a finite multiset of nonnegative reals be given, written in sorted order
p_1 ≥ p_2 ≥ … ≥ p_k. Two players alternately remove one remaining element, the first player
moving first, each player maximizing the total of the elements it removes. Then:

1. On every turn, removing a **largest remaining element** is an optimal move; and
2. under optimal play the first mover obtains exactly Σ_{i odd} p_i and the second mover Σ_{i even} p_i.

In particular the game has a well-defined value: whatever the opponent does, the first mover can
guarantee **at least** Σ_odd, and the opponent can hold the first mover to **at most** Σ_odd.

## Proof
Write T = Σ_i p_i. Because the two totals always add up to the constant T, the game is zero-sum with
a finite game tree, hence (backward induction / Zermelo) it has a value and optimal strategies exist.
Let V(S) denote the total the player *to move* secures under optimal play from the sorted multiset S.

For a one-move look-ahead: if the mover removes an element x from S, the opponent then secures
V(S∖{x}) from the remainder, whose total is T(S) − x; the remaining T(S) − x − V(S∖{x}) accrues to
the mover, who in addition already holds x. Hence
  V(S) = max_{x∈S} [ x + (T(S) − x − V(S∖{x})) ] = T(S) − min_{x∈S} V(S∖{x}).    (∗)

We prove, by induction on k = |S|, that V(S) = Σ_{i odd} p_i and that the minimum in (∗) is attained
at x = p_1 (a largest element).

*Base* k = 0: V = 0 = empty sum. k = 1: V = p_1 = Σ_odd. ✓

*Step.* Assume the claim for all multisets of size k−1. Fix S sorted p_1 ≥ … ≥ p_k. Removing the
element in sorted position j leaves the sorted list L_j = (p_1,…,p_{j−1},p_{j+1},…,p_k). By the
induction hypothesis V(S∖{p_j}) = Σ_odd(L_j). In L_j the entries before position j keep their index,
while those after shift down by one; therefore
  Σ_odd(L_j) = Σ_{i<j, i odd} p_i + Σ_{i>j, i even} p_i.
For j = 1 this is Σ_odd(L_1) = Σ_{i≥2, i even} p_i = p_2 + p_4 + … . Subtracting,
  Σ_odd(L_j) − Σ_odd(L_1)
     = Σ_{i<j, i odd} p_i + Σ_{i>j, i even} p_i − Σ_{i≥2, i even} p_i
     = Σ_{i≤j−1, i odd} p_i − Σ_{i≤j, i even} p_i,
because the even-indexed terms with i > j cancel and only the even-indexed terms with 2 ≤ i ≤ j remain
(with a minus sign). Now split on the parity of j:

- **j odd:** the surviving indices are odd 1,3,…,j−2 and even 2,4,…,j−1, so the difference is
  (p_1 − p_2) + (p_3 − p_4) + … + (p_{j−2} − p_{j−1}).
- **j even:** the surviving indices are odd 1,3,…,j−1 and even 2,4,…,j, so the difference is
  (p_1 − p_2) + (p_3 − p_4) + … + (p_{j−1} − p_j).

In both cases every parenthesised term is ≥ 0 because the list is sorted, so
Σ_odd(L_j) ≥ Σ_odd(L_1) for every j. Hence min_x V(S∖{x}) is attained at x = p_1 and equals
Σ_odd(L_1) = Σ_{i≥2, i even} p_i. By (∗),
  V(S) = T − Σ_{i≥2, i even} p_i = p_1 + p_3 + p_5 + … = Σ_{i odd} p_i.
This proves both (1) and (2). ∎

## Consequence used by the approaches
After all cuts, sort the pieces p_1 ≥ … ≥ p_k (they sum to the stick length 1). Liu Bang moves first
in the claiming game, so his guaranteed and optimal share equals **Σ_odd = p_1 + p_3 + …**, and Xiang
Yu's is Σ_even. The lemma is tie-robust: when several pieces are equal, "a largest element" is any of
them and the odd/even split is by sorted position, not by breaking ties.
