# Lemma G (greedy reduction for alternating-pick games)

**Certified by:** proof-builder, approach `dyadic-cascade-induction`, round 2.

## Statement

Let `x_1 ≥ x_2 ≥ … ≥ x_K ≥ 0` be a fixed multiset of real numbers (piece lengths). Consider
the finite, deterministic, perfect-information game in which two players alternately claim
one currently-unclaimed element of the multiset (mover 1 first), each trying to maximize
the total value of the elements they personally claim. By Zermelo's theorem this game has a
well-defined value under optimal (backward-induction) play for both sides.

Then:
1. Under optimal play, mover 1's total equals `x_1 + x_3 + x_5 + …` (the sum of the
   odd-ranked elements in sorted-descending order) and mover 2's total equals
   `x_2 + x_4 + …` (the even-ranked elements).
2. **"Always claim the currently-largest unclaimed element" is an optimal strategy for
   whichever player is on move**, at every point in the game (this holds even in the
   presence of ties among the largest remaining elements — claiming *any* maximal element
   is optimal).

## Proof

Define, for a finite multiset `S` of nonnegative reals, `v(S)` = the payoff to the player
about to move on `S`, under optimal play by both sides (well-defined by backward induction /
Zermelo's theorem — KB "General Proof Methods: Induction", the finite game has no infinite
play so backward induction terminates). Since every element of `S` is eventually claimed by
one player or the other, the opponent's payoff is `sum(S) − v(S)`.

**Recursion.** If the mover claims element `x ∈ S`, they receive `x` immediately, and the
game continues on `S \ {x}` with the *other* player to move; the mover's total future
winnings from that subgame equal `sum(S\{x}) − v(S\{x})` (total remaining minus what the
subgame's value gives the new mover, i.e. the opponent). So claiming `x` nets the mover
`x + sum(S\{x}) − v(S\{x}) = sum(S) − v(S\{x})`. Since the mover picks `x` to maximize this,
and `sum(S)` is fixed:
```
v(S) = sum(S) − min_{x ∈ S} v(S\{x}),        v(∅) = 0.
```

**Claim (proved by strong induction on `K = |S|`).** For `S` sorted descending as
`x_1≥…≥x_K`, `v(S) = x_1+x_3+x_5+…`, and the minimizing choice of element to remove in the
recursion above is (any of) the largest element(s) `x_1`.

*Base case `K=0`:* `v(∅)=0`, matches the empty sum. ✓.

*Inductive step.* Assume the claim for all multisets of size `< K`. Fix `S = {x_1≥…≥x_K}`.
For each `j = 1,…,K`, removing `x_j` leaves the sorted list
`x_1,…,x_{j-1},x_{j+1},…,x_K` (still sorted, since deleting one entry from a sorted list
keeps it sorted). By the induction hypothesis (size `K-1 < K`),
```
v(S\{x_j}) = (sum of odd-ranked entries of this (K−1)-list).
```
Entries at original rank `< j` keep their rank (odd/even unchanged); entries at original
rank `> j` shift down by exactly 1 (so an original odd rank becomes even and vice versa).
Hence, writing `O_j := Σ_{i<j, i odd} x_i` and `E_j := Σ_{i>j, i even} x_i`,
```
v(S\{x_j}) = O_j + E_j.
```
We must show `min_j (O_j+E_j)` is attained at `j=1`, with value `E := x_2+x_4+…`
(the full even-indexed sum of `S`), since then `v(S) = sum(S) − E = x_1+x_3+…`, completing
the induction, and `j=1` (i.e. removing the largest element `x_1`) is a minimizer, i.e. an
optimal move.

At `j=1`: `O_1 = 0` (no indices `<1`) and `E_1 = Σ_{i>1,i even} x_i = x_2+x_4+…= E`, so
`O_1+E_1 = E`.

For general `j`, write `E − E_j = Σ_{i even, i ≤ j} x_i` (the even-indexed terms with index
`≤ j` that are *not* counted in `E_j`, since `E_j` only sums even indices `> j`). So
`O_j + E_j ≥ E` is equivalent to
```
O_j ≥ Σ_{i even, i≤j} x_i,     i.e.     Σ_{i odd, i<j} x_i ≥ Σ_{i even, i≤j} x_i.
```
Let `t = ⌊j/2⌋` (equivalently: this is exactly the number of even indices `≤ j`, for both
parities of `j` — checked directly: if `j=2t` the even indices `≤j` are `2,4,…,2t`, `t` of
them; if `j=2t+1` the even indices `≤j` are still `2,4,…,2t`, `t` of them). In both cases the
odd indices `<j` are exactly `1,3,…,2t-1` (`t` of them: if `j=2t` these are `1,…,2t-1`; if
`j=2t+1` these are again `1,…,2t-1`). So the inequality to prove is
```
x_1+x_3+…+x_{2t-1}  ≥  x_2+x_4+…+x_{2t}.
```
This follows termwise: since `x_1≥…≥x_K` is non-increasing, `x_{2i-1} ≥ x_{2i}` for every
`i=1,…,t` (consecutive entries in a sorted list), so summing over `i=1,…,t` gives exactly the
claimed inequality. Hence `O_j+E_j ≥ E` for every `j`, with equality at `j=1`, so `j=1`
(removing the largest element) minimizes `v(S\{x_j})`, establishing both the value formula
and the optimality of the greedy ("take the current max") move. If several elements tie for
the maximum value, the argument treats them as interchangeable (the formula for
`v(S\{x_j})` only depends on the *value* at each rank, not on which tied copy is labeled
`x_1`), so claiming any one of the tied maximal elements is optimal. ∎

## Consequence used elsewhere

Applying this with `S` = the final multiset of pieces after all cuts (LB's and XY's) are
made, mover 1 = Liu Bang (who moves first in the claiming phase): Liu Bang's guaranteed
total is exactly `L := x_1+x_3+…` (odd ranks) and Xiang Yu's is `X := x_2+x_4+…` (even
ranks), under optimal alternating claiming — this reduces the whole problem to the two-stage
cutting optimization described in the parent approach file.
