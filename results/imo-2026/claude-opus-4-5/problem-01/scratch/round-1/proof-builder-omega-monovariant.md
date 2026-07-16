# Proof Builder Report: omega-monovariant (IMO 2026 P1)

## Summary

Built a complete, rigorous proof for the omega-monovariant approach to IMO 2026 P1. The proof addresses both parts (a) and (b) with all gaps closed.

## Gaps Closed

### Gap 1: Prove Omega formula

Proved that Omega(n) = sum of prime exponents is fully additive: Omega(ab) = Omega(a) + Omega(b). This follows directly from v_p(ab) = v_p(a) + v_p(b) for all primes p.

Used this to derive:
- Omega(mn/g^2) = Omega(mn) - Omega(g^2) = Omega(m) + Omega(n) - 2*Omega(g)
- Hence after the move: Omega(g) + Omega(mn/g^2) = Omega(m) + Omega(n) - Omega(g)
- So S_new = S_old - Omega(g)

### Gap 2: k decreases by 1 when gcd = 1

Proved explicitly: when gcd(m,n) = 1 with m, n > 1:
- The outputs are (1, mn)
- Since m > 1 and n > 1, mn > 1
- Two entries > 1 are replaced by one entry > 1 and one entry = 1
- Net change: k decreases by 1

## Structure of Proof

### Part (a): Termination with exactly one M > 1

1. Defined monovariant: (S, k) where S = sum of Omega over all entries, k = count of entries > 1
2. Case 1 (g > 1): S strictly decreases by Omega(g) >= 1
3. Case 2 (g = 1): S unchanged, k decreases by 1
4. Lexicographic decrease implies termination
5. k <= 1 at termination (else move possible)
6. k >= 1 at termination (by G_p invariant from part b)

### Part (b): M is uniquely determined

1. Defined G_p = gcd of v_p over all board entries
2. Proved Euclidean identity: gcd(min(a,b), |a-b|) = gcd(a,b)
3. Proved operation on valuations is (a,b) -> (min(a,b), |a-b|)
4. Proved G_p invariant under any move
5. At termination: v_p(M) = G_p for all primes p
6. Therefore M = prod_p p^{G_p} depends only on initial configuration

## Rigor Checklist

- [x] All cases covered (gcd > 1 and gcd = 1)
- [x] All lemmas proved in full (Omega additivity, Euclidean identity, G_p invariance)
- [x] Theorems named (Euclidean identity, standard valuation properties)
- [x] No "clearly" or "it follows" without justification
- [x] Final answer for M explicitly given and verified

## Status

**solved** - Complete proof written to `/home/agentuser/repo/results/imo-2026-01/approaches/omega-monovariant.md`

## Promotable Lemmas

Two lemmas suitable for certification:
1. **Euclidean identity on pairs:** gcd(min(a,b), |a-b|) = gcd(a,b)
2. **G_p invariant:** The gcd of a multiset is preserved when replacing (a,b) with (min(a,b), |a-b|)

These may be useful for other problems involving gcd-lcm operations or Euclidean algorithms on multisets.
