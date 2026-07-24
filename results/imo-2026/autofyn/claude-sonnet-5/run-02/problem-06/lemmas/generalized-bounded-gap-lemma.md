## Lemma: Generalized Bounded Gap Lemma (certified)

**Source.** `greedy-exchange-cost-potential`, round 2 ("Lemma A"). A strict
generalization of the certified `bounded-gap-lemma.md` (which is the special case
c = a_1): the bound holds for ANY positive integer modulus divisible by every prime of
Q, not just a_1 itself. Useful whenever a future approach wants a legal candidate that
is guaranteed to also be divisible by some extra fixed prime p (e.g. a recruited
witness prime), at the cost of a correspondingly larger (but still O(1) in n) gap bound.

**Statement.** Let Q = P(a_1). For any positive integer c divisible by every prime of
Q, a_{n+1} ≤ a_n + c for every n ≥ 1. In particular, for any prime p (in Q or not),
taking c = a_1·p gives a_{n+1} ≤ a_n + a_1·p.

**Proof.** Let r be the smallest multiple of c strictly exceeding a_n; since among any
c consecutive integers exactly one is a multiple of c, r ≤ a_n + c. Legality of r as a
candidate for a_{n+1}: for i = 1, pick any q ∈ Q; q | a_1 (since Q = P(a_1)) and
q | c | r, so q | gcd(r, a_1), giving gcd(r, a_1) > 1. For 2 ≤ i ≤ n, by the Free Facts
lemma gcd(a_i, a_1) > 1, so some prime q_i divides both a_i and a_1; since q_i | a_1
and Q = P(a_1), q_i ∈ Q, hence q_i | c | r, so q_i | gcd(r, a_i), giving gcd(r,a_i) > 1.
So r satisfies gcd(r, a_i) > 1 for every i = 1,...,n, i.e. r is a legal candidate for
a_{n+1}; by minimality of the actual (smallest legal) a_{n+1}, a_{n+1} ≤ r ≤ a_n + c.
Taking c = a_1·p (a_1 | c, and every prime of Q divides a_1 hence c) gives the
corollary. ∎

**Status.** Correct, complete, no gaps. Self-contained (uses only the Free Facts
lemma and the definition of the greedy rule); does not depend on any open gap.
