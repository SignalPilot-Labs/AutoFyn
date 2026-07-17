## Euclidean Identity for Valuation Pairs

**Statement:** For non-negative integers alpha, beta:

gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta)

**Proof:** Without loss of generality, assume alpha <= beta. Then min(alpha, beta) = alpha and |alpha - beta| = beta - alpha.

By the Euclidean algorithm: gcd(a, b) = gcd(a, b - a) for any integers a, b with a >= 0.

Setting a = alpha and b = beta, we obtain:
gcd(alpha, beta - alpha) = gcd(alpha, beta)

This is exactly gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta). QED

**Certified by:** proof-reviewer, round 1
