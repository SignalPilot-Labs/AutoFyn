# Lemma: euclid-step-invariant

Status: CERTIFIED (proof-reviewer, round 1). Statements (A)-(D) verified correct,
proofs sorry-free, all edge cases (a=0, b=0, a=b) checked and identities confirmed
computationally for all a,b in [0,30). No claim is stronger than what is proved.
Proved in: results/imo-2026-01/approaches/valuation-gcd.md (Lemmas 0, 1, 2 and the
d_p-invariance Claim in Part (b)); independently reproved in omega-count-monovariant
(Lemmas 0.1-0.3, 7) and product-count-monovariant (Lemmas 5-7).

## Conventions
gcd is extended to non-negative integers with gcd(0,0) = 0 and gcd(0,k) = k for
k >= 1. Then gcd is commutative, associative, gcd(a,0) = a, and the gcd of a finite
multiset of non-negative integers is 0 iff every member is 0. v_p(x) denotes the
p-adic valuation of a positive integer x (Fundamental Theorem of Arithmetic).

## Statement

**(A) Valuation action of a gcd/lcm move.** For positive integers m, n and a prime
p, with a = v_p(m), b = v_p(n):
- v_p(gcd(m,n)) = min(a,b);
- v_p(lcm(m,n)) = max(a,b);
- v_p(lcm(m,n)/gcd(m,n)) = max(a,b) - min(a,b) = |a - b|.
Consequently a move (m,n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) acts on the multiset of
p-valuations by the substitution (a,b) -> (min(a,b), |a-b|), simultaneously for
every prime p.

**(B) Arithmetic identity.** For all non-negative integers a,b:
min(a,b) + |a-b| = max(a,b) = a + b - min(a,b).

**(C) Subtractive Euclidean invariant.** For all non-negative integers a,b:
gcd(min(a,b), |a-b|) = gcd(a,b).

**(D) Whole-multiset invariance.** Let a finite multiset of non-negative integers
have gcd D. Replacing two members a,b by min(a,b) and |a-b| (all other members
fixed) leaves the gcd equal to D. In particular, for a board of positive integers,
d_p = gcd(v_p(x_1), ..., v_p(x_N)) is invariant under every gcd/lcm move, for every
prime p.

## Proof

**(A)** By unique factorization m = prod_p p^{v_p(m)}, n = prod_p p^{v_p(n)}. A
prime power p^k divides m iff k <= v_p(m); the largest power of p dividing both m
and n is p^{min(a,b)}, and since primes act independently gcd(m,n) =
prod_p p^{min(v_p m, v_p n)}. Dually lcm(m,n) = prod_p p^{max(v_p m, v_p n)}. Since
min <= max at every prime, gcd | lcm and lcm/gcd is a positive integer with
v_p(lcm/gcd) = max(a,b) - min(a,b) (v_p is additive under multiplication). Finally
max - min = |a-b| by cases a >= b and a < b.

**(B)** If a >= b: min = b, |a-b| = a-b, sum = a = max, and a+b-min = a+b-b = a. If
a < b: min = a, |a-b| = b-a, sum = b = max, and a+b-min = b. Also a+b = min+max
always.

**(C)** By symmetry take a >= b, so min = b, |a-b| = a-b; show gcd(b, a-b) =
gcd(a, b). Any common divisor D of a,b divides a-b, hence divides b and a-b;
conversely any common divisor of b and a-b divides b + (a-b) = a, hence divides a
and b. So {a,b} and {b, a-b} have identical common-divisor sets, hence identical
gcd (the maximum common divisor; the all-zero case gives gcd 0 on both sides).
Edge cases: a=b gives gcd(a,0)=a=gcd(a,a); b=0 gives gcd(0,a)=a=gcd(a,0);
a=b=0 gives 0=0.

**(D)** Let R be the multiset of the untouched members with r = gcd(R) (r = 0 if R
empty). By associativity/commutativity of gcd, gcd(before) = gcd(r, gcd(a,b)) and
gcd(after) = gcd(r, gcd(min(a,b),|a-b|)). By (C) the inner gcds are equal, so the
two are equal. Applying this in each E_p gives d_p invariance. ∎
