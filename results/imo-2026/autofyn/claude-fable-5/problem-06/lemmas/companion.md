# Lemma: Companion

**Status:** CERTIFIED by proof-reviewer (round 3). Statement correct, proof sorry-free, no stronger than proved.

**Setting.** $(a_n)$ the greedy sequence; $P(m)$ = set of prime factors of $m$; $\sigma(m) = \{p \text{ prime} : p \mid m,\ p \le a_1\}$. Depends on: `clique.md` (only for $\sigma(a) \neq \emptyset$).

**Statement.** Let $a$ be a term having a prime factor $q > a_1$. Then there exists an integer $x$ with $P(x) = \sigma(a)$ and $a_1 \le x < a$.

**Proof.** $\sigma(a) \neq \emptyset$: $\gcd(a, a_1) > 1$ (Clique; trivial if $a = a_1$), so a prime $p_0$ divides both $a$ and $a_1$; then $p_0 \le a_1$, so $p_0 \in \sigma(a)$.

Fix $p \in \sigma(a)$; then $p \le a_1 < q$, so $p \neq q$ and $pq \mid a$, giving $a \ge pq$ (5.1). Let $m_0 = \prod_{r \in \sigma(a)} r$ ($> 1$, squarefree, $P(m_0) = \sigma(a)$). Choose $t \ge 0$ minimal with $m_0 p^t \ge a_1$ (exists since $m_0 p^t \to \infty$), and set $x = m_0 p^t$. Then $P(x) = P(m_0) = \sigma(a)$ (multiplying by $p \in P(m_0)$ adds no primes) and $x \ge a_1$.

$x < a$:
- $t = 0$: $x = m_0$. $m_0$ is squarefree with all prime factors dividing $a$, so $m_0 \mid a$; and $q > a_1 \ge$ every element of $\sigma(a)$, so $q \nmid m_0$, hence $m_0 q \mid a$ and $a \ge m_0 q > m_0 = x$.
- $t \ge 1$: minimality gives $m_0 p^{t-1} < a_1$, so $x = p (m_0 p^{t-1}) < p\, a_1 < pq \le a$ by (5.1) and $a_1 < q$. $\square$

**Warning (threshold is load-bearing).** The threshold "$p$ small $\iff p \le a_1$" cannot be weakened to $p \le \mathrm{rad}(a_1)$ or $p \le \max P(a_1)$: for $a_1 = 48$ the term $56 = 2^3 \cdot 7$ has $\sigma_{\mathrm{rad}}(56) = \{2\}$ and no integer with prime set $\{2\}$ lies in $[48, 56)$.

**Proved in:** `approaches/small-prime-core.md`, Lemma 5.
