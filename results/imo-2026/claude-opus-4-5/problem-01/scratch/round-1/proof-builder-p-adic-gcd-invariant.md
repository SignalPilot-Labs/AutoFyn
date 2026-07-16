# Proof Builder Report: p-adic-gcd-invariant

## Problem
IMO 2026 P1: 2026 integers > 1 on a blackboard. Move: (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)). Prove (a) termination with exactly one M > 1; (b) M is unique.

## Approach
p-adic-gcd-invariant: Lexicographic monovariant (P, k) for termination; p-adic invariant G_p = gcd(v_p(a_i)) for uniqueness.

## Status
**solved**

## Gaps Closed

1. **Gap 1 (Three-case exhaustion)**: Verified explicitly. Cases A (m=n), B (m!=n, gcd=1), C (m!=n, gcd>1) are mutually exclusive and exhaustive. Every pair (m, n) with m, n > 1 falls into exactly one case.

2. **Gap 2 (Euclidean identity)**: Proved rigorously in Step 6. For non-negative integers a, b with a >= b: the set of common divisors of {a, b} equals the set of common divisors of {b, a-b}, because d | a and d | b iff d | b and d | (a-b). Hence gcd(a, b) = gcd(b, a-b) = gcd(min(a,b), |a-b|).

3. **Gap 3 (lcm/gcd > 1 in Case C)**: Proved in the Case C analysis. If m != n and gcd(m,n) = g > 1, write m = ga, n = gb with gcd(a,b) = 1. Since m != n, we have a != b. Since a, b >= 1 and a != b, we have ab >= 2. Thus lcm(m,n)/gcd(m,n) = ab >= 2 > 1.

## Key Derivations

- **Monovariant computation**: In Case A, P drops by factor m; in Case B, P unchanged but k drops; in Case C, P drops by factor g. All cases decrease (P, k) lexicographically.

- **p-adic valuation computation**: v_p(gcd(m,n)) = min(v_p(m), v_p(n)); v_p(lcm(m,n)/gcd(m,n)) = |v_p(m) - v_p(n)|. Verified via standard formulas.

- **Terminal state analysis**: At termination, board = {M, 1, ..., 1}. Then G_p = gcd(v_p(M), 0, ..., 0) = v_p(M). Hence M = prod_p p^{G_p} is determined by initial data.

## Final Answer
M = product over all primes p of p^{gcd(v_p(a_1), ..., v_p(a_{2026}))}.

## Output
Full proof written to `/home/agentuser/repo/results/imo-2026-01/approaches/p-adic-gcd-invariant.md`.
