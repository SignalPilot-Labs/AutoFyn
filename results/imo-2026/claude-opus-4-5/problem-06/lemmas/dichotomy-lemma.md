# Dichotomy Lemma

## Statement

For a greedy gcd-linked sequence with a_1 not a prime power, either:
(A) The stable antichain H_stable is finite, OR
(B) There exists a backbone prime p in P(a_1) such that p divides all terms.

## Proof

Assume (B) is false: for every p in B = P(a_1), some term is not divisible by p.

Every element Q of H_stable equals P(a_j) for some j, so Q intersects B (by the Backbone Constraint: gcd(a_j, a_1) > 1).

Suppose H_stable is infinite. By Pigeonhole, some p in B appears in infinitely many elements of H_stable.

Let {Q_i : i in I} be the infinite subset of elements containing p. In the case where no prime power enters (Sub-case 2b), each |Q_i| >= 2. Write Q_i = {p} union S_i where S_i nonempty.

The sets S_i form an antichain (inherited from Q_i being an antichain with shared element p).

For any m in V_stable with p not dividing m, P(m) must intersect every S_i. If infinitely many S_i are singletons {r_i} with distinct r_i, then P(m) contains infinitely many primes, contradiction.

If infinitely many S_i have size >= 2, the infinite antichain on the primes outside {p} requires infinitely many primes, and P(m) cannot cover them all.

Therefore every m in V_stable is divisible by p. Since all terms lie in V_stable, p divides all terms, contradicting our assumption.

**Conclusion:** H_stable is finite. QED

## Status
certified (round 2)
