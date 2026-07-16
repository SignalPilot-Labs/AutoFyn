# Pairing Cancellation Lemma

## Statement

For a multiset S of positive reals and any v > 0, let lb_score(T) denote the sum of elements at odd positions (1, 3, 5, ...) in the sorted (descending) ordering of T. Then:

lb_score({v, v} + S) = v + lb_score(S)

## Proof

Sort S as s_1 >= s_2 >= ... >= s_m. Insert the two copies of v into this sorted list. Since they are equal, they must occupy two consecutive positions. Call these positions i and i+1 (where i is the position of the first copy in the merged list).

**Case 1 (i is odd):** LB picks the copy at position i (getting v), XY picks the copy at position i+1. The remaining elements of S fill positions 1, ..., i-1 and i+2, ..., m+2.

**Case 2 (i is even):** XY picks the copy at position i, LB picks the copy at position i+1 (getting v). The remaining elements of S fill the same positions.

In either case, LB gets exactly one copy of v (contributing v to the score), and the remaining elements of S contribute exactly lb_score(S) to LB's total. This is because removing the pair {v, v} from positions i and i+1 leaves the parity structure of the remaining positions unchanged.

Therefore lb_score({v, v} + S) = v + lb_score(S). QED.

## Certified

This lemma is certified by the proof-reviewer (Round 5). Independently verified computationally with multiple test cases.
