# Small-prime-mask invariance

## Statement
Fix $k\ge2$. Recursively classify integers $m\ge k$ as good when no earlier good integer is coprime to $m$, and bad otherwise. If $a,b\ge k$ have exactly the same prime divisors at most $k$, then they have the same classification.

## Proof
By the small-witness theorem, every two good integers share a prime at most $k$. Suppose $a,b$ have the same small-prime mask but opposite classifications; label the bad one $a$ and the good one $b$. Since $a$ is bad, some good $r<a$ satisfies $\gcd(r,a)=1$. The good integers $r,b$ share a prime $p\le k$. As $p\mid b$ and $a,b$ have equal small-prime masks, $p\mid a$, contradicting $p\mid r$ and $\gcd(r,a)=1$. $\square$
