## Valuation-GCD Invariance

**Statement:** For the operation (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) on integers m, n > 0, the quantity

d_p = gcd(v_p(x_1), v_p(x_2), ..., v_p(x_k))

where x_1, ..., x_k are all integers on the board, is preserved for each prime p.

**Proof:** The operation sends p-adic valuations as:
(v_p(m), v_p(n)) -> (min(v_p(m), v_p(n)), |v_p(m) - v_p(n)|)

Let alpha = v_p(m), beta = v_p(n). The Euclidean identity gives:
gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta)

Since replacing two elements (alpha, beta) with (min(alpha, beta), |alpha - beta|) preserves their gcd, and the overall gcd of a multiset can be computed as gcd(gcd(a_1, a_2), a_3, ...), the overall gcd d_p is unchanged. QED

**Certified by:** proof-reviewer, round 1
