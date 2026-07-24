## Lemma: Free Facts on pairwise gcd (certified)

**Source.** Independently derived (one line each) in both `amortized-charging-budget`
(Lemma 1) and `covering-system-construction` (Free Facts 1–2). Certified as a single
shared lemma.

**Statement.**
Let (a_n) be the sequence of the problem: a_1 > 1 an integer, and for n ≥ 1, a_{n+1} is
the smallest integer exceeding a_n with gcd(a_{n+1}, a_i) > 1 for every i = 1, ..., n.
Then:

1. For every 1 ≤ i < j, gcd(a_i, a_j) > 1 (the terms are pairwise non-coprime).
2. In particular, for every n ≥ 2, gcd(a_n, a_1) > 1, so P(a_n) ∩ P(a_1) ≠ ∅, where
   P(m) denotes the set of prime divisors of m.

**Proof.** Fix 1 ≤ i < j. Write j = (j-1) + 1. By the defining property of the
sequence applied at index j-1 (i.e., a_j = a_{(j-1)+1} is required to satisfy
gcd(a_j, a_i) > 1 for every i = 1, ..., j-1), and since i ≤ j-1, this gives
gcd(a_j, a_i) > 1 directly. Part 2 is the special case i = 1. ∎

**Status.** Correct, complete, no gaps. Elementary consequence of the problem's
hypothesis; reusable by any approach to this problem.
