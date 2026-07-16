## imo-2026-01

p-adic-gcd-invariant: new
Target: (a) Game terminates with exactly one M > 1; (b) M does not depend on choices.
Technique: p-adic valuation invariant G_p = gcd(v_p(a_i)) combined with lexicographic monovariant (Product, k).
Skeleton:
  1. Define k = count of entries > 1, P = product of all entries.
  2. Case analysis: (A) m=n -> k drops, P drops; (B) gcd=1, m!=n -> k drops, P constant; (C) gcd>1, m!=n -> k constant, P drops.
  3. (P, k) is lexicographic monovariant, bounded below -> termination.
  4. Define G_p = gcd(v_p(a_1), ..., v_p(a_{2026})).
  5. Prove G_p invariant via Euclidean identity: (a,b) -> (min(a,b), |a-b|) preserves gcd.
  6. At termination {M, 1,...,1}: G_p = gcd(v_p(M), 0,...) = v_p(M).
  7. M = prod_p p^{G_p} depends only on initial data.
Key lemmas (claim + mechanism):
  - Euclidean identity: gcd(min(a,b), |a-b|) = gcd(a,b) -- because gcd(a,b) = gcd(a, b-a) is the subtraction step of Euclid's algorithm.
  - G_p invariant: operation on v_p multiset replaces (a,b) with (min(a,b), |a-b|), preserving gcd of multiset.
  - gcd(k,0) = k: every integer divides 0, so gcd picks k.
  - k >= 1 at termination: some initial a_i has prime factor p with v_p(a_i) >= 1, so G_p >= 1, forcing v_p(M) >= 1, hence M > 1.
Open gaps: (1) Verify three-case exhaustion; (2) Prove Euclidean identity; (3) Verify lcm(m,n)/gcd(m,n) > 1 in Case C.
Cases to cover: A (equal), B (coprime unequal), C (non-coprime unequal).
Watch out for: G_p differs from ordinary gcd(a_1,...,a_n); convention gcd(k,0)=k is essential.

omega-monovariant: new
Target: (a) Game terminates with exactly one M > 1; (b) M does not depend on choices.
Technique: Omega(n) = total prime-factor count as primary monovariant; p-adic invariant for uniqueness.
Skeleton:
  1. Define Omega(n) = sum over p of v_p(n), S = sum of Omega(a_i), k = count of entries > 1.
  2. Move analysis: S_after = S_before - Omega(gcd(m,n)).
  3. If gcd > 1: S strictly decreases. If gcd = 1: S constant, k drops by 1.
  4. (S, k) lexicographically decreases -> termination.
  5. G_p invariant gives M = prod_p p^{G_p}.
Key lemmas (claim + mechanism):
  - Omega is subadditive: Omega(g) + Omega(mn/g^2) = Omega(m) + Omega(n) - Omega(g) -- by multiplicativity of Omega on coprime factors.
  - k drops when gcd=1: outputs are (1, mn) with exactly one > 1.
  - G_p invariant: same Euclidean identity argument.
Open gaps: (1) Prove Omega formula; (2) Verify k decreases by 1 in coprime case.
Cases to cover: gcd > 1, gcd = 1 with m != n.
Watch out for: m = n implies gcd = m > 1, handled by first case.

euclidean-reduction: new
Target: (a) Game terminates with exactly one M > 1; (b) M does not depend on choices.
Technique: View operation as parallel Euclidean algorithm on valuation vectors at each prime.
Skeleton:
  1. Reframe: board state = collection of v_p vectors across all primes.
  2. Operation on v_p: (a, b) -> (min(a,b), |a-b|) is Euclidean subtraction step.
  3. Sum of v_p values at each prime decreases by min(a,b) per move.
  4. Total Omega = sum over p of Sigma_p gives global monovariant.
  5. Euclidean identity: gcd(a,b) = gcd(min(a,b), |a-b|) preserves G_p.
  6. At termination, v_p(M) = G_p for all p.
  7. M = prod_p p^{G_p} is uniquely determined.
Key lemmas (claim + mechanism):
  - Operation = Euclidean step: directly from gcd/lcm formulas on valuations.
  - Sum decreases: min(a,b) + |a-b| = max(a,b) < a+b when both positive and unequal.
  - Single-prime case: all a_i = p^{e_i} -> terminal M = p^{gcd(e_i)} by multiset Euclidean algorithm.
  - Analogy to aimo-0440: L1 norm monovariant on coefficient vector mirrors our Sigma_p monovariant.
Open gaps: (1) Prove multiset Euclidean terminates with all but one entry zero; (2) Connect per-prime analysis to global termination.
Cases to cover: single-prime, multi-prime, pairwise coprime.
Watch out for: global termination needs total Omega argument, not just per-prime sums.
