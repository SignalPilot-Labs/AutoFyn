# Euclidean Identity on GCD

## Statement

For non-negative integers a and b:
```
gcd(min(a, b), |a - b|) = gcd(a, b)
```

## Proof

Without loss of generality, assume a >= b >= 0. Then min(a, b) = b and |a - b| = a - b.

We need to show gcd(b, a - b) = gcd(a, b).

By the defining property of gcd: for any integer d > 0,
d | a and d | b if and only if d | b and d | (a - b).

This is because:
- If d | a and d | b, then d | (a - b).
- If d | b and d | (a - b), then d | (b + (a - b)) = a.

Therefore the set of common divisors of {a, b} equals the set of common divisors of {b, a - b}, which equals the set of common divisors of {min(a,b), |a-b|}. The greatest common divisor is therefore the same.

This is precisely the subtraction step of the Euclidean algorithm for computing gcd.

## Convention

We use the standard convention gcd(k, 0) = k for k >= 0, since every integer divides 0.

## Source

Certified from proof of IMO 2026 P1 (p-adic-gcd-invariant approach), Round 1.
