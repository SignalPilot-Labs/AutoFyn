## No-Two-Ones Lemma

**Statement:** The operation (m, n) -> (gcd(m,n), lcm(m,n)/gcd(m,n)) with m, n > 1 never produces two outputs equal to 1.

**Proof:** Write m = da, n = db where d = gcd(m, n) and gcd(a, b) = 1.

The outputs are (d, ab).

Suppose for contradiction that both outputs equal 1, i.e., d = 1 and ab = 1.

From ab = 1 with a, b positive integers: a = b = 1.

From a = b = 1: m = da = 1 * 1 = 1 and n = db = 1 * 1 = 1.

But the operation requires m > 1 and n > 1. This is a contradiction.

Therefore, at least one output is > 1 in every move. QED

**Certified by:** proof-reviewer, round 1
