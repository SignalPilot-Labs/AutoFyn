# Lemma: Lock (prime-power term ⇒ $T=1$, $L=p$)

**Statement.** If some term $a_i=p^k$ is a prime power ($p$ prime, $k\ge1$), then $a_{n+1}=a_n+p$ for every $n\ge1$; equivalently $a_n=a_1+(n-1)p$ for all $n\ge1$. Consequently the required constants are $T=1$, $L=p$.

**Proof.** We establish three facts.

(1) $p\mid a_1$. The term $a_i=p^k$ is admissible at step $i-1$, so $\gcd(a_i,a_1)>1$; the only prime divisor of $a_i$ is $p$, so $p\mid a_1$. Hence $p\in P_1$.

(2) $p\mid a_j$ for every $j\ge1$. Three ranges:
- $j=i$: $a_i=p^k$, so $p\mid a_i$.
- $j<i$: $a_i=p^k$ is admissible at step $i-1$, so $\gcd(a_i,a_j)>1$ for every $j<i$. As $p$ is the *only* prime divisor of $a_i$, the only way $\gcd(p^k,a_j)>1$ is $p\mid a_j$.
- $j>i$: $a_j$ is admissible at step $j-1\ge i$, hence $\gcd(a_j,a_i)>1$, and again the only prime of $a_i$ is $p$, forcing $p\mid a_j$.

(3) $a_{n+1}=a_n+p$ for every $n\ge1$. Fix $n\ge1$.
- *Lower bound $a_{n+1}\ge a_n+p$.* By (2), $p\mid a_{n+1}$ and $p\mid a_n$. Both are positive multiples of $p$; since $a_{n+1}>a_n$, we have $a_{n+1}\ge a_n+p$.
- *Upper bound $a_{n+1}\le a_n+p$.* The number $a_n+p$ is a multiple of $p$ (since $p\mid a_n$), and by (2) every $a_i$ ($i\le n$) is a multiple of $p$, so $\gcd(a_n+p,a_i)\ge p>1$ for every $i\le n$. Hence $a_n+p$ is admissible at step $n$, and the greedy rule gives $a_{n+1}\le a_n+p$.

Combining, $a_{n+1}=a_n+p$. Iterating, $a_n=a_1+(n-1)p$, i.e. $a_{n+T}=a_n+L$ with $T=1$, $L=p$. $\square$

**Corollary (coverage).** The lock case covers: $a_1$ even (a power of $2$ is eventually reached along $a_n=a_1+2(n-1)$); $a_1$ divisible by an odd prime $p$ *if* a power of $p$ is eventually reached; $a_1=p$ or $a_1=p^k$ (lock at once).

**Status.** Reviewer-certified (round 1). Unconditional. Verified computationally for $a_1\in\{6,21,33,50\}$ (each locks at $8,27,81,64$ respectively, and $a_n=a_1+p(n-1)$ holds from $n=1$). Importable.
