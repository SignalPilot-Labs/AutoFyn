# Lemma: Small Common Prime Lemma (SCPL)

**Status:** CERTIFIED by proof-reviewer (round 3). Statement correct, proof sorry-free, no stronger than proved.

**Setting.** $(a_n)$ the greedy sequence; $\sigma(m) = \{p \text{ prime} : p \mid m,\ p \le a_1\}$; $W_n = \{m > 1 : \gcd(m, a_i) > 1 \ \forall i \le n\}$; greedy rule $a_{n+1} = \min(W_n \cap (a_n, \infty))$ ($\ast$). Depends on: `clique.md`, `valid-below-are-terms.md`, `companion.md`.

**Statement.** For all $i < j$, the terms $a_i$ and $a_j$ share a prime factor $\le a_1$; i.e. $\sigma(a_i) \cap \sigma(a_j) \neq \emptyset$.

**Proof.** Strong induction on $j$; $S(j)$: "$\sigma(a_i) \cap \sigma(a_j) \neq \emptyset$ for all $i < j$". $S(1)$ vacuous. Fix $j \ge 2$, assume $S(j')$ for all $j' < j$; suppose some $i < j$ has $\sigma(a_i) \cap \sigma(a_j) = \emptyset$ and take $i$ minimal.

- (6.1) For every $s < i$: $\sigma(a_s) \cap \sigma(a_j) \neq \emptyset$ (minimality of $i$).
- (6.2) $\gcd(a_i, a_j) > 1$ (Clique) gives a common prime $q$; $q \le a_1$ would put $q \in \sigma(a_i) \cap \sigma(a_j)$, so $q > a_1$.
- $i \ge 2$: if $i = 1$, a common prime $r$ of $a_1, a_j$ (Clique) satisfies $r \in P(a_1) = \sigma(a_1)$ and $r \in \sigma(a_j)$, contradiction.

**Step 1.** By (6.2) and the Companion lemma applied to $a_i$: there is $x$ with $P(x) = \sigma(a_i)$, $a_1 \le x < a_i$ (6.3).

**Step 2 ($x \in W_{i-1}$).** $i < j$, so $S(i)$ holds by the strong IH. For each $i' \le i - 1$ pick $r \in \sigma(a_{i'}) \cap \sigma(a_i)$; then $r \mid a_{i'}$ and $r \mid x$ (as $r \in \sigma(a_i) = P(x)$), so $\gcd(x, a_{i'}) > 1$. Also $x > 1$.

**Step 3 ($x$ is an earlier term).** $i - 1 \ge 1$. If $a_{i-1} < x < a_i$: $x \in W_{i-1} \cap (a_{i-1}, \infty)$ with $x < a_i$ contradicts ($\ast$) at $n = i-1$. Hence $a_1 \le x \le a_{i-1}$, and by valid-below-are-terms (with $n = i-1$), $x = a_s$ for some $s \le i-1$.

**Step 4 (contradiction).** By (6.1) applied to $s < i$: pick $r' \in \sigma(a_s) \cap \sigma(a_j)$. Then $r' \mid a_s = x$, so $r' \in P(x) = \sigma(a_i)$; also $r' \in \sigma(a_j)$. So $\sigma(a_i) \cap \sigma(a_j) \neq \emptyset$ — contradiction. $\square$

**Proved in:** `approaches/small-prime-core.md`, Lemma 6 (with all details).
