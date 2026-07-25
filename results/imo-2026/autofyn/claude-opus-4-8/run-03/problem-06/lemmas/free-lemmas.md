# Certified free lemmas (round 1)

Proved identically and correctly in BOTH `anomaly-count-terminates` and
`redundant-constraint-antichain`. Reviewer-verified round 1. Framing-agnostic.

Notation: F_n=primes(a_n), P=primes(a_1), M=∏_{p∈P}p = rad(a_1) (so M | a_1 ≤ ...).

## L1 (Anchor)
Every term a_n has a prime factor in P.
*Proof.* n=1: a_1 is a product of primes of P. n≥2: the defining clause i=1 gives
gcd(a_n,a_1)>1, a shared prime lies in P. ∎

## L2 (Gap bound / linear growth)
a_{n+1}−a_n ≤ M for all n; hence a_1+(n−1) ≤ a_n ≤ a_1+(n−1)M, so a_n=Θ(n).
*Proof.* Let c be the least multiple of M with c>a_n; a_n<c≤a_n+M. For each i≤n, L1 gives
p∈P with p|a_i, and p|M|c, so gcd(c,a_i)≥p>1. Thus c admissible, a_{n+1}≤c≤a_n+M.
Lower bound from strict monotonicity. ∎

## L3 (Distance–prime)
If prime q | a_i and q | a_j (i≠j) then q | (a_i−a_j), so q ≤ |a_i−a_j|.
*Proof.* q divides the difference; terms distinct so difference ≠0. ∎

## L4 (Pairwise-intersecting)
gcd(a_i,a_j)>1 for all i≠j.
*Proof.* For i<j, defining clause i≤j−1 in a_j's definition. ∎
