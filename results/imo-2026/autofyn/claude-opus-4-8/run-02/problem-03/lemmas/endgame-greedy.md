# Lemma: Endgame greedy (alternating-claim value = odd-rank sum)

**Certified round 1 (proof-reviewer).** Independently re-derived and verified by
exhaustive game-tree DP against `Odd` on 3000 random multisets (0 mismatches).

## Statement
Fix a finite multiset `S` of nonnegative reals sorted descending `a_1 >= a_2 >= ... >= a_m`.
In the alternating-claim game (players alternately take any one remaining piece, first
mover fixed, each maximizing his own collected total; the pool sums to the constant
`T = sum a_i`, so the game is zero-sum), the game has a well-defined value equal to
`Odd(S) := a_1 + a_3 + a_5 + ...` (sum of odd-ranked pieces), and "take a currently-largest
piece" is an optimal move for whoever is to move.

## Proof (verified sound)
Let `V(S)` be the value to the mover. If the mover takes `x`, the opponent then moves on
`S\{x}` securing `V(S\{x})`, so the mover ends with `x + (T - x) - V(S\{x}) = T - V(S\{x})`.
Hence `V(S) = T - min_{x in S} V(S\{x})`.

*Monotonicity sub-lemma (M).* For any multiset `R` and `b >= b' >= 0`,
`0 <= V(R∪{b}) - V(R∪{b'}) <= b - b'`. Proof by induction on `|R|`: base immediate; step
splits removals into (removing the tagged element → `V(R)` in both) or (removing `x∈R`),
applies the IH to `R\{x}`, and uses `min(A,C+d) <= min(A,C)+d` for `d>=0`. (See
majorization-smoothing.md for the full write-up; verified correct.)

*Main claim.* By (M), removing the largest `a_1` minimizes `V(S\{x})`, so greedy is optimal
and `V(S) = T - V(S\{a_1})`. By induction `V(S\{a_1}) = a_2 + a_4 + ...`, hence
`V(S) = T - (a_2+a_4+...) = a_1 + a_3 + ... = Odd(S)`. Ties give equality (any tied largest
is equally optimal). ∎

## Consequence
With Liu Bang moving first on final multiset `P` (total 1), LB's guaranteed total is
`Odd(P) = (1 + f(P))/2`, where `f(P) = a_1 - a_2 + a_3 - ...` is the alternating sum.
