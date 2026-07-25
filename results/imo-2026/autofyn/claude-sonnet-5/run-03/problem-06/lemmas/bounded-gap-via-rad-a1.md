## Lemma (Unconditional bounded gap / linear growth)

Let $(a_n)$ be the problem's greedy sequence and let $R := \mathrm{rad}(a_1)$
(the product of the distinct primes dividing $a_1$). Then for every $n \ge 1$,
$$a_{n+1} - a_n \le R,$$
and consequently $a_n \le a_1 + (n-1)R$ for all $n \ge 1$ (i.e. $a_n = O(n)$).

### Proof
Let $P$ be the set of distinct prime factors of $a_1$, so $R = \prod_{p \in
P} p$.

**Fact.** For every $n \ge 1$, $a_n$ is divisible by some prime of $P$.
Indeed, for $n=1$ this is immediate ($P$ is exactly the prime factors of
$a_1$). For $n \ge 2$, the defining property applied at step $n-1 \ge 1$
requires $\gcd(a_n, a_1) > 1$ (taking $i=1$, valid since $1 \le n-1$), so
$a_n$ shares a prime factor with $a_1$, i.e. a prime of $P$.

Fix $n \ge 1$. Let $M$ be the smallest multiple of $R$ exceeding $a_n$, i.e.
$M = R\cdot(\lfloor a_n/R \rfloor + 1)$; then $M \le a_n + R$ (rounding up to
the next multiple of a fixed modulus never overshoots by more than the
modulus). For every $i = 1,\ldots,n$, by the Fact, $a_i$ is divisible by some
$p \in P$; since $R$ (and hence $M$, a multiple of $R$) is divisible by every
prime of $P$, in particular by $p$, we get $p \mid \gcd(M, a_i)$, so
$\gcd(M,a_i) \ge p > 1$. Thus $M$ is a valid candidate for $a_{n+1}$ ($M > a_n$
and satisfies all $n$ gcd constraints), so by minimality
$$a_{n+1} \le M \le a_n + R.$$

Summing over $n = 1,\ldots,N-1$ gives $a_N \le a_1 + (N-1)R$. $\blacksquare$

### Numerical confirmation (round 1)
Verified computationally for $a_1 \in \{6,15,21,35,105\}$ that the maximum gap
over the first 150+ terms never exceeds $\mathrm{rad}(a_1)$ (e.g. $a_1=15$:
$R=15$, observed max gap $=6 \le 15$; $a_1=35$: $R=35$, observed max gap
$=10 \le 35$), consistent with (and not violating) the bound.

### Provenance
Proved in `approaches/growth-rate-contradiction.md` ("Key Lemma" and its
Corollary, under "Full argument, Part 1"). Certified by the proof-reviewer,
round 1: the derivation is non-circular (uses only that $a_1$ is always a
live constraint, i.e. $1 \le n$ for all $n\ge1$) and independently verified by
the reviewer both algebraically and by direct computation of the sequence for
several values of $a_1$.

### Caveat (do not overclaim from this lemma)
This lemma alone does **not** resolve the central open gap of the problem
(finiteness of $S = \{p : p \mid a_n \text{ infinitely often}\}$). The
"growth-rate-contradiction" approach attempted to combine this bound with a
counting argument on freshly-recruited primes and found that mechanism does
not close (a fresh large prime dividing $a_{n+1}$ need not be the cause of a
large gap, since the gap is already controlled by $R$ regardless). Use this
lemma only as an $O(n)$ growth estimate, not as a step toward finiteness of
$S$ by itself.
