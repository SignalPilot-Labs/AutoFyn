# Pairwise Intersection Lemma

## Statement

For any i, j >= 1 in a greedy gcd-linked sequence, we have P(a_i) intersect P(a_j) != empty.

## Proof

Without loss of generality, assume i < j. By the defining rule of the sequence, a_j was chosen so that gcd(a_j, a_i) > 1. This means there exists a prime p dividing both a_j and a_i, so p is in P(a_j) intersect P(a_i). QED

## Status
certified (round 2)
