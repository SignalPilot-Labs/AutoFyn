# Proof Builder Report: product-monovariant

## Summary

Built complete proof for IMO 2026-01 using the product-monovariant approach.

## Work Done

1. Defined monovariant Q = P * 2^N where P is the product of all board entries and N is the count of entries > 1.

2. Proved Q decreases by at least factor 2 per move via exhaustive case analysis:
   - Case 1: gcd >= 2 and ab >= 2: Q -> Q/gcd <= Q/2
   - Case 2: gcd >= 2 and ab = 1 (m = n): Q -> Q/(2*gcd) <= Q/4  
   - Case 3: gcd = 1: Q -> Q/2

3. Proved the "no-two-ones" lemma explicitly: if both outputs equal 1, then d = 1 and ab = 1, forcing a = b = 1, hence m = n = 1, contradicting m, n > 1.

4. Proved exactly one M > 1 remains: termination requires N <= 1, but N >= 1 throughout (by no-two-ones), so N = 1.

5. For part (b), proved the p-adic invariant d_p = gcd of all valuations is preserved using the Euclidean identity gcd(min(a,b), |a-b|) = gcd(a,b).

6. Showed M = product of p^{d_p} over all primes p, determined solely by initial configuration.

7. Verified with small example: {6, 4, 3} terminates at M = 6, matching d_2 = d_3 = 1.

## Gaps Closed

- The "no two 1s" lemma flagged by the outline-reviewer is now explicitly proved with a complete contradiction argument.

## Status

**solved** - Complete rigorous proof of both parts (a) and (b).

## Promotable Lemmas

1. Euclidean identity: gcd(min(a,b), |a-b|) = gcd(a,b)
2. No-two-ones: operation on m,n > 1 never outputs two 1s
