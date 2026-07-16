# p-adic GCD Invariant for (gcd, lcm/gcd) Operation

## Statement

For the operation (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) on a board of positive integers, the quantity

```
G_p = gcd(v_p(a_1), v_p(a_2), ..., v_p(a_n))
```

is invariant under the operation, for every prime p.

Here v_p(n) denotes the p-adic valuation of n (the largest power of p dividing n), with v_p(1) = 0.

## Proof

Let g = gcd(m, n). The outputs are g and lcm(m,n)/g = mn/g^2.

For each prime p, let a = v_p(m) and b = v_p(n).

From the standard formulas for p-adic valuations:
- v_p(gcd(m, n)) = min(v_p(m), v_p(n)) = min(a, b)
- v_p(mn/g^2) = v_p(m) + v_p(n) - 2*v_p(g) = a + b - 2*min(a, b) = |a - b|

So the operation on the p-adic valuations replaces (a, b) with (min(a, b), |a - b|).

By the Euclidean Identity Lemma:
```
gcd(min(a, b), |a - b|) = gcd(a, b)
```

The other entries of the board are unchanged. Therefore:

```
G_p (after) = gcd({all v_p values after move})
            = gcd(gcd(a, b), {unchanged v_p values})
            = gcd(a, b, {unchanged v_p values})
            = gcd({all v_p values before move})
            = G_p (before)
```

## Application

At termination, when the board is {M, 1, 1, ..., 1}, we have:
```
G_p = gcd(v_p(M), 0, 0, ..., 0) = v_p(M)
```

Therefore M is uniquely determined by:
```
M = product over all primes p of p^{G_p}
```

where G_p is computed from the initial configuration.

## Dependencies

- Euclidean Identity on GCD (euclidean-identity-gcd.md)
- Standard p-adic valuation formulas: v_p(gcd) = min, v_p(lcm) = max

## Source

Certified from proof of IMO 2026 P1 (p-adic-gcd-invariant approach), Round 1.
