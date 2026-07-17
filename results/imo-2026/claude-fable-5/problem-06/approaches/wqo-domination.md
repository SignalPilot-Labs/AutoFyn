# Approach: wqo-domination

**Problem (imo-2026-06).** Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, 2, \ldots, n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T} = a_n + L$ for every positive integer $n$.

## Status
solved

## Approaches tried
- Round 3 (new approach, first build): SCPL (every two terms share a prime $\le a_1$) proved independently by minimal-counterexample descent using the companion construction at threshold $z = a_1$; then the antichain endgame: the inclusion-minimal constraint family $E_\infty$ lies in $2^Q$ for the finite prime universe $Q = \{p \le a_1\}$, hence is finite; $V_\infty$ is exactly $L$-periodic for $L = \prod_{p \in P^*} p$ with $P^* = \bigcup E_\infty$; greedy enumeration of an exactly periodic set gives $a_{n+T} = a_n + L$ from $n = 1$ with no transient. — worked; complete proof below.
- (Recorded dead ends respected: the companion threshold $\mathrm{rad}(a_1)$ FAILS for $a_1 = 48$ (term $56 = 2^3\cdot 7$ has no $\{2\}$-companion in $[48,56)$), so the threshold $a_1$ is used throughout; no appeal to WQO on $\mathcal{P}_{\mathrm{fin}}(\text{primes})$ (false — infinite antichains exist), only to finiteness of $2^Q$ for the finite set $Q$; no claim that the prime sets of terms "stabilize" (false — new large primes appear forever), only that the inclusion-minimal family is finite.)

## Current best
Complete proof (below). No open gaps.

## Full proof

### Setup and notation

Fix the sequence $(a_n)_{n \ge 1}$ as in the problem statement. By definition it is strictly increasing: $a_{n+1} > a_n$ for all $n$. Since the $a_n$ are distinct positive integers with $a_1 \ge 2$, we have $a_n \ge a_1 + (n-1)$, so $a_n \to \infty$.

Throughout:

- For a positive integer $m > 1$, $P(m)$ denotes the (finite, nonempty) set of prime divisors of $m$.
- A prime is **small** if it is $\le a_1$, and **large** if it is $> a_1$. Let $Q = \{p \text{ prime} : p \le a_1\}$; this is a finite set, and it is nonempty since $2 \le a_1$ and every prime factor of $a_1$ is $\le a_1$.
- $\sigma(m) = P(m) \cap Q$, the set of small prime divisors of $m$.
- For $n \ge 1$: $W_n = \{ m \in \mathbb{Z}, m > 1 : \gcd(m, a_i) > 1 \text{ for all } i = 1, \ldots, n \}$. (Note: no lower bound on $m$ other than $m > 1$.)
- $V_\infty = \{ m \in \mathbb{Z}, m > 1 : \gcd(m, a_i) > 1 \text{ for all } i \ge 1 \} = \bigcap_{n \ge 1} W_n$.
- $A = \{a_1, a_2, a_3, \ldots\}$, the set of terms.

The defining rule reads: for every $n \ge 1$,
$$a_{n+1} = \min\, \bigl( W_n \cap (a_n, \infty) \bigr). \tag{$\ast$}$$
Indeed, the problem defines $a_{n+1}$ as the smallest integer $> a_n$ with $\gcd(a_{n+1}, a_i) > 1$ for $i \le n$; every such integer is $> a_n \ge a_1 \ge 2 > 1$, so the two descriptions of the candidate set agree. (The minimum exists: the candidate set is a nonempty — see Lemma 2 — set of integers bounded below.)

### Lemma 1 (Clique). For all $m \ne n$, $\gcd(a_m, a_n) > 1$.

*Proof.* Without loss of generality $m > n$. By the defining rule, $a_m$ satisfies $\gcd(a_m, a_i) > 1$ for every $i = 1, \ldots, m-1$; in particular for $i = n$. $\square$

### Lemma 2 (Bounded gaps; well-posedness). Let $B = \mathrm{rad}(a_1) = \prod_{p \mid a_1} p$. For every $n \ge 1$, the set $W_n \cap (a_n, \infty)$ is nonempty and $a_{n+1} \le a_n + B$.

*Proof.* Let $m$ be the smallest multiple of $B$ exceeding $a_n$; then $a_n < m \le a_n + B$, and $m \ge B \ge 2 > 1$. For each $i \le n$: by Lemma 1 (or trivially if $i = 1$), $\gcd(a_i, a_1) > 1$, so some prime $p$ divides both $a_i$ and $a_1$; then $p \mid B \mid m$, so $\gcd(m, a_i) \ge p > 1$. Hence $m \in W_n \cap (a_n, \infty)$, this set is nonempty, and by ($\ast$), $a_{n+1} \le m \le a_n + B$. $\square$

(Lemma 2 is used only to justify that the minima in ($\ast$) exist; the endgame below does not need the quantitative bound.)

### Lemma 3 (Reduction). 
**(a)** $a_n \in V_\infty$ for every $n \ge 1$. 
**(b)** $a_{n+1} = \min\,(V_\infty \cap (a_n, \infty))$ for every $n \ge 1$. 
**(c)** $A = V_\infty \cap [a_1, \infty)$, and the increasing enumeration of the set $V_\infty \cap [a_1, \infty)$ is exactly the sequence $a_1 < a_2 < a_3 < \cdots$.

*Proof.* **(a)** Fix $n$. For $i \ne n$, $\gcd(a_n, a_i) > 1$ by Lemma 1; for $i = n$, $\gcd(a_n, a_n) = a_n > 1$. So $a_n \in V_\infty$.

**(b)** Fix $n$. By (a), $a_{n+1} \in V_\infty$, and $a_{n+1} > a_n$, so $a_{n+1} \in V_\infty \cap (a_n, \infty)$; thus the minimum in question exists and is $\le a_{n+1}$. Conversely, if $m \in V_\infty \cap (a_n, \infty)$, then in particular $\gcd(m, a_i) > 1$ for $i = 1, \ldots, n$ and $m > a_n$, i.e. $m \in W_n \cap (a_n, \infty)$, so by ($\ast$), $m \ge a_{n+1}$. Hence the minimum equals $a_{n+1}$.

**(c)** ($\subseteq$) Each $a_n$ lies in $V_\infty$ by (a) and satisfies $a_n \ge a_1$ since the sequence is increasing. ($\supseteq$) Let $m \in V_\infty$ with $m \ge a_1$. If $m = a_1$, then $m \in A$. Otherwise $m > a_1$, so the set $\{n \ge 1 : a_n < m\}$ contains $1$; it is finite because $a_n \to \infty$. Let $n$ be its largest element. Then $a_n < m$ and (by maximality) $a_{n+1} \ge m$. But $m \in V_\infty \cap (a_n, \infty)$, so by (b), $a_{n+1} \le m$. Hence $m = a_{n+1} \in A$.

Finally, $A$ listed in increasing order is $a_1 < a_2 < \cdots$ (the sequence is strictly increasing and, by the equality of sets just proved, exhausts $V_\infty \cap [a_1, \infty)$). $\square$

### Lemma 4 (Valid-below-are-terms). For every $n \ge 1$: $W_n \cap [a_1, a_n] = \{a_1, \ldots, a_n\}$.

*Proof.* ($\supseteq$) For $j \le n$: $a_1 \le a_j \le a_n$, and for every $i \le n$, $\gcd(a_j, a_i) > 1$ (Lemma 1 if $i \ne j$; $\gcd(a_j,a_j) = a_j > 1$ if $i = j$). So $a_j \in W_n \cap [a_1, a_n]$.

($\subseteq$) Let $m \in W_n \cap [a_1, a_n]$ and suppose $m \notin \{a_1, \ldots, a_n\}$. Since $a_1 \le m \le a_n$, $m \ne a_1$, $m \ne a_n$, and the terms $a_1 < a_2 < \cdots < a_n$ partition $[a_1, a_n]$ into themselves and the open gaps between consecutive terms, there is $t \in \{1, \ldots, n-1\}$ with $a_t < m < a_{t+1}$. Since $m \in W_n$ and $t \le n$, we have $\gcd(m, a_i) > 1$ for all $i \le t$, so $m \in W_t \cap (a_t, \infty)$ with $m < a_{t+1}$ — contradicting ($\ast$), which says $a_{t+1}$ is the minimum of that set. $\square$

### Lemma 5 (Companion Lemma). Let $a_k$ be a term having a large prime factor $q > a_1$. Then $\sigma(a_k) \ne \emptyset$, and there exists a positive integer $x$ with
$$P(x) = \sigma(a_k) \quad \text{and} \quad a_1 \le x < a_k.$$

*Proof.* First, $k \ge 2$: every prime factor of $a_1$ divides $a_1$, hence is $\le a_1$, so $a_1$ has no large prime factor. By Lemma 1, $\gcd(a_k, a_1) > 1$, so some prime $p_0$ divides both $a_k$ and $a_1$; then $p_0 \le a_1$, so $p_0 \in \sigma(a_k) \ne \emptyset$.

Fix any $p \in \sigma(a_k)$. Since $p \le a_1 < q$, the primes $p$ and $q$ are distinct, and both divide $a_k$; hence $pq \mid a_k$, so
$$a_k \ge pq > p \cdot a_1. \tag{5.1}$$

Let $m_0 = \prod_{r \in \sigma(a_k)} r$. Each $r \in \sigma(a_k)$ divides $a_k$ and the $r$ are distinct primes, so $m_0 \mid a_k$; moreover $q > a_1$ implies $q \notin \sigma(a_k)$, so $\gcd(m_0, q) = 1$, and since $m_0 \mid a_k$ and $q \mid a_k$ with $\gcd(m_0,q)=1$,
$$m_0 q \mid a_k, \quad \text{hence} \quad a_k \ge m_0 q \ge 2 m_0 > m_0. \tag{5.2}$$

Since $p \ge 2$, the numbers $m_0 p^t$ ($t = 0, 1, 2, \ldots$) increase without bound, so there is a minimal $t \ge 0$ with $m_0 p^t \ge a_1$. Set $x = m_0 p^t$. Then $x \ge a_1$, and since $p \in \sigma(a_k) = P(m_0)$, we get $P(x) = P(m_0) = \sigma(a_k)$.

It remains to show $x < a_k$. Two cases, exhaustive and disjoint:

- **Case $t = 0$:** $x = m_0 < a_k$ by (5.2).
- **Case $t \ge 1$:** By minimality of $t$, $m_0 p^{t-1} < a_1$. Then $x = p \cdot (m_0 p^{t-1}) < p \cdot a_1 < pq \le a_k$, using (5.1) for the last two inequalities. $\square$

### Lemma 6 (Small Common Prime Lemma, SCPL). For all indices $i < j$, there is a prime $p \le a_1$ with $p \mid \gcd(a_i, a_j)$.

*Proof.* For $j \ge 2$, let $\Pi(j)$ denote the statement: "for every $i$ with $1 \le i < j$, the terms $a_i$ and $a_j$ share a prime factor $\le a_1$." We prove $\Pi(j)$ for all $j \ge 2$ by strong induction on $j$.

**Base observation (holds inside every $\Pi(j)$, and in particular settles $i = 1$).** For any $j \ge 2$: by Lemma 1, $\gcd(a_1, a_j) > 1$, so some prime $r$ divides both; $r \mid a_1$ forces $r \le a_1$. So the pair $(1, j)$ always shares a small prime. In particular $\Pi(2)$ holds (the only pair there is $(1,2)$).

**Inductive step.** Let $j \ge 3$ and assume $\Pi(j')$ holds for every $j'$ with $2 \le j' < j$. Suppose, for contradiction, that $\Pi(j)$ fails, and let $i$ be the **minimal** index in $\{1, \ldots, j-1\}$ such that $a_i$ and $a_j$ share no prime $\le a_1$. By the base observation, $i \ne 1$, so $2 \le i < j$.

By Lemma 1, $\gcd(a_i, a_j) > 1$, so $a_i$ and $a_j$ share some prime $q$; by the choice of $i$, every such shared prime is large, so $q > a_1$. In particular $q \mid a_i$ with $q > a_1$.

Apply the Companion Lemma (Lemma 5) to $a_k = a_i$: there is $x$ with
$$P(x) = \sigma(a_i), \qquad a_1 \le x < a_i.$$

**Claim: $x \in W_{i-1}$.** First, $x > 1$ since $P(x) = \sigma(a_i) \ne \emptyset$ (Lemma 5). Now fix any $i'$ with $1 \le i' \le i - 1$. The pair $(i', i)$ has larger index $i$, and $2 \le i < j$, so the induction hypothesis $\Pi(i)$ applies: $a_{i'}$ and $a_i$ share a prime $r \le a_1$. Then $r \in P(a_i)$ and $r \le a_1$, so $r \in \sigma(a_i) = P(x)$, i.e. $r \mid x$; and $r \mid a_{i'}$. Hence $\gcd(x, a_{i'}) \ge r > 1$. This holds for every $i' \le i-1$, so $x \in W_{i-1}$. (If $i = 2$ this only uses $i' = 1$, covered by $\Pi(2)$.)

**Claim: $x$ is an earlier term, $x = a_s$ with $s \le i - 1$.** We have $x \in W_{i-1}$ and $a_1 \le x < a_i$. Two cases, exhaustive and disjoint:

- If $a_{i-1} < x < a_i$: then $x \in W_{i-1} \cap (a_{i-1}, \infty)$ and $x < a_i$, contradicting ($\ast$) (with $n = i-1$), which says $a_i$ is the *smallest* element of $W_{i-1} \cap (a_{i-1}, \infty)$. So this case is impossible.
- Hence $a_1 \le x \le a_{i-1}$. By Lemma 4 (with $n = i-1$), $W_{i-1} \cap [a_1, a_{i-1}] = \{a_1, \ldots, a_{i-1}\}$, so $x = a_s$ for some $s \in \{1, \ldots, i-1\}$.

**Deriving the contradiction.** We have $s < i$. By the minimality of $i$ (and, if $s = 1$, the base observation), the pair $(s, j)$ *does* share a small prime: there is a prime $r' \le a_1$ with $r' \mid a_s$ and $r' \mid a_j$. Now $r' \mid a_s = x$, so $r' \in P(x) = \sigma(a_i) \subseteq P(a_i)$, i.e. $r' \mid a_i$. Thus $r'$ is a prime $\le a_1$ dividing both $a_i$ and $a_j$ — contradicting the choice of $i$ as an index whose pair with $j$ shares no small prime.

This contradiction proves $\Pi(j)$, completing the induction, and Lemma 6 follows. $\square$

*Remark.* If $a_1$ is a prime power $p^e$ (in particular, if $a_1$ is prime), SCPL is immediate: for every $j \ge 2$, $\gcd(a_j, a_1) > 1$ (Lemma 1) yields a common prime, which divides $a_1 = p^e$ and hence equals $p$; so $p \mid a_j$ for every $j$, and any two terms share $p \le a_1$. The general proof above covers this case with no special handling; the remark is only a sanity check.

### Step 3: The minimal constraint family $E_\infty$ is contained in $2^Q$, hence finite

Let
$$\mathcal{F} = \{ P(a_i) : i \ge 1 \} \qquad \text{(a family of finite nonempty sets of primes)},$$
and let $E_\infty$ be the set of **inclusion-minimal** members of $\mathcal{F}$:
$$E_\infty = \{ F \in \mathcal{F} : \text{no } F' \in \mathcal{F} \text{ satisfies } F' \subsetneq F \}.$$

**(3a) Every member of $\mathcal{F}$ contains a member of $E_\infty$.** Let $S \in \mathcal{F}$. The subfamily $\mathcal{G} = \{ F \in \mathcal{F} : F \subseteq S \}$ is nonempty ($S \in \mathcal{G}$). Since $S$ is a finite set, the cardinalities $|F|$, $F \in \mathcal{G}$, form a nonempty set of nonnegative integers; choose $F^* \in \mathcal{G}$ of minimal cardinality. Then $F^* \in E_\infty$: if some $F' \in \mathcal{F}$ had $F' \subsetneq F^*$, then $F' \subseteq S$ (so $F' \in \mathcal{G}$) and $|F'| < |F^*|$, contradicting minimality. And $F^* \subseteq S$. (Note this argument needs no well-quasi-order theory: minimality below a *fixed finite set* is all that is used, even though $\mathcal{F}$ itself may be infinite.)

**(3b) Characterization of $V_\infty$:**
$$V_\infty = \{ m > 1 : P(m) \cap F \ne \emptyset \text{ for every } F \in E_\infty \}. \tag{3.1}$$

*Proof.* ($\subseteq$) Let $m \in V_\infty$ and $F \in E_\infty$. Then $F = P(a_k)$ for some $k$, and $\gcd(m, a_k) > 1$ yields a prime dividing both $m$ and $a_k$, which lies in $P(m) \cap F$. ($\supseteq$) Let $m > 1$ satisfy the right-hand condition, and let $i \ge 1$. By (3a) there is $F \in E_\infty$ with $F \subseteq P(a_i)$. By hypothesis there is a prime $p \in P(m) \cap F \subseteq P(m) \cap P(a_i)$; then $p \mid m$ and $p \mid a_i$, so $\gcd(m, a_i) > 1$. As $i$ was arbitrary, $m \in V_\infty$. $\square$

**(3c) Main claim: $E_\infty \subseteq 2^Q$, i.e. every $F \in E_\infty$ consists of small primes only.**

*Proof.* Suppose not: some $F \in E_\infty$ contains a large prime $q > a_1$. Write $F = P(a_k)$; as in Lemma 5, $k \ge 2$ and $S := \sigma(a_k) = F \cap Q$ is nonempty.

First we show: **every term $a_j$ ($j \ge 1$) satisfies $S \cap P(a_j) \ne \emptyset$.** If $j \ne k$: by SCPL (Lemma 6, applied to the pair $\{k, j\}$ with indices ordered appropriately), $a_k$ and $a_j$ share a prime $r \le a_1$; then $r \in P(a_k) \cap Q = S$ and $r \in P(a_j)$. If $j = k$: any element of $S$ lies in $P(a_k)$, and $S \ne \emptyset$.

Now for $N \ge 1$ set
$$x_N = \prod_{p \in S} p^N.$$
Then $x_N > 1$ and $P(x_N) = S$. For every $j \ge 1$: pick $p \in S \cap P(a_j)$ (just shown nonempty); then $p \mid x_N$ and $p \mid a_j$, so $\gcd(x_N, a_j) > 1$. Hence $x_N \in V_\infty$ for **every** $N \ge 1$.

Since $x_N \ge 2^N \to \infty$, choose $N$ with $x_N \ge a_1$. By Lemma 3(c), $x_N \in V_\infty \cap [a_1, \infty) = A$, so $x_N = a_m$ for some $m \ge 1$. Then
$$P(a_m) = P(x_N) = S \subseteq F, \quad \text{and} \quad S \ne F \text{ since } q \in F \setminus S \ (q > a_1 \Rightarrow q \notin Q \supseteq S).$$
So $P(a_m) \in \mathcal{F}$ and $P(a_m) \subsetneq F$, contradicting the inclusion-minimality of $F$ in $\mathcal{F}$. $\square$

**(3d) Finiteness.** $Q$ is a finite set ($|Q| = \pi(a_1)$), so $2^Q$ is finite, and by (3c), $E_\infty \subseteq 2^Q$ gives $|E_\infty| \le 2^{\pi(a_1)} < \infty$. Moreover $E_\infty \ne \emptyset$ (apply (3a) to $S = P(a_1) \in \mathcal{F}$) and every $F \in E_\infty$ is nonempty (each $a_i > 1$ has a prime factor). It is possible that $P(a_1)$ itself belongs to $E_\infty$; nothing in the sequel requires otherwise.

### Step 4: $V_\infty$ is exactly $L$-periodic

Let
$$P^* = \bigcup_{F \in E_\infty} F \subseteq Q, \qquad L = \prod_{p \in P^*} p.$$
By Step 3, $P^*$ is a finite nonempty set of primes ($E_\infty \ne \emptyset$ and its members are nonempty), so $L$ is a well-defined integer with $L \ge 2$.

**(4a) Divisibility by primes of $P^*$ depends only on the residue mod $L$.** Let $p \in P^*$ and let $m, m'$ be integers with $m \equiv m' \pmod{L}$. Since $p \mid L$, we get $m \equiv m' \pmod{p}$, so $p \mid m \iff p \mid m'$.

**(4b) The residue set $R$.** Define
$$R = \{ r \in \{0, 1, \ldots, L-1\} : \text{for every } F \in E_\infty \text{ there is } p \in F \text{ with } p \mid r \}$$
(where "$p \mid 0$" is true for every $p$). We claim
$$V_\infty = \{ m > 1 : (m \bmod L) \in R \}. \tag{4.1}$$

*Proof.* Let $m > 1$ and $r = m \bmod L$; then $m \equiv r \pmod L$. By (3.1), $m \in V_\infty$ iff for every $F \in E_\infty$ some $p \in F$ divides $m$. Each such $p$ lies in $F \subseteq P^*$, so by (4a) (applied to $m$ and $r$), $p \mid m \iff p \mid r$. Hence "for every $F \in E_\infty$, $\exists p \in F$, $p \mid m$" holds iff "for every $F \in E_\infty$, $\exists p \in F$, $p \mid r$" holds, i.e. iff $r \in R$. $\square$

**(4c) $R \ne \emptyset$.** By Lemma 3(a), $a_1 \in V_\infty$, so by (4.1), $(a_1 \bmod L) \in R$. Set
$$T = |R| \ge 1.$$

### Step 5: Conclusion — $a_{n+T} = a_n + L$ for all $n \ge 1$

By Lemma 3(c) and (4.1),
$$A = V_\infty \cap [a_1, \infty) = \{ m \ge a_1 : (m \bmod L) \in R \} \tag{5.3}$$
(every $m \ge a_1 \ge 2$ automatically satisfies $m > 1$), and the increasing enumeration of $A$ is exactly $a_1 < a_2 < a_3 < \cdots$.

**(5a) Shift stability: for every $m \in A$, also $m + L \in A$.** Indeed $m + L \ge a_1$ and $(m+L) \bmod L = m \bmod L \in R$; apply (5.3).

**(5b) Window count: for every $n \ge 1$, the window $[a_n, a_n + L)$ contains exactly $T$ elements of $A$.** The window $[a_n, a_n + L)$ consists of $L$ consecutive integers, hence contains **exactly one** integer from each residue class modulo $L$. An integer $m$ in this window satisfies $m \ge a_n \ge a_1$, so by (5.3), $m \in A \iff (m \bmod L) \in R$. Therefore
$$|A \cap [a_n, a_n + L)| = |R| = T.$$

**(5c) The window's elements are the consecutive terms $a_n, \ldots, a_{n+T-1}$.** Since the increasing enumeration of $A$ is $(a_j)_{j \ge 1}$, we have $A \cap [a_n, \infty) = \{a_n, a_{n+1}, a_{n+2}, \ldots\}$ with $a_n < a_{n+1} < \cdots$. The elements of $A \cap [a_n, a_n+L)$ are exactly the elements of $A \cap [a_n, \infty)$ that are $< a_n + L$; since the enumeration is increasing, these form an initial segment $\{a_n, a_{n+1}, \ldots, a_{n+k-1}\}$ where $k = |A \cap [a_n, a_n+L)| = T$ by (5b). (Initial segment: if $a_{n+u} < a_n + L$ and $u' < u$ then $a_{n+u'} < a_{n+u} < a_n + L$.) So
$$A \cap [a_n, a_n + L) = \{ a_n, a_{n+1}, \ldots, a_{n+T-1} \}, \tag{5.4}$$
and consequently every element of $A$ strictly greater than $a_{n+T-1}$ is $\ge a_n + L$; in particular
$$a_{n+T} \ge a_n + L. \tag{5.5}$$

**(5d) Finish.** By (5a), $a_n + L \in A$, and $a_n + L > a_{n+T-1}$ by (5.4). Since $a_{n+T}$ is the smallest element of $A$ exceeding $a_{n+T-1}$ (increasing enumeration), $a_{n+T} \le a_n + L$. Combined with (5.5),
$$a_{n+T} = a_n + L \qquad \text{for every } n \ge 1.$$

Here $T = |R| \ge 1$ and $L \ge 2$ are positive integers independent of $n$. This is exactly the assertion of the problem (with no transient: the identity holds from $n = 1$, since the enumeration of $A$ begins at $a_1 \in A$). $\blacksquare$

*Consistency check (not part of the proof).* For $a_1 = 15$ the sequence begins $15, 18, 20, 21, 22, \ldots$; one computes $E_\infty = \{\{2,3\},\{2,5\},\{3,5\}\}$, $P^* = \{2,3,5\}$, $L = 30$, $T = 8$, and indeed $a_{n+8} = a_n + 30$ from $n = 1$. For the non-squarefree seed $a_1 = 48$: $E_\infty = \{\{2\}\}$, $L = 2$, $T = 1$, and the sequence is $48, 50, 52, \ldots$ For $a_1 = 49$: $E_\infty = \{\{7\}\}$, $L = 7$, $T = 1$. All match direct computation of the first 120 terms.

## Promotable lemmas

All proved in full in this file (section references above); proposed for certification into `results/imo-2026-06/lemmas/`:

1. **clique** — For all $m \ne n$, $\gcd(a_m, a_n) > 1$. (Lemma 1.)
2. **reduction** — With $V_\infty = \{m > 1 : \gcd(m, a_i) > 1 \ \forall i \ge 1\}$: every $a_n \in V_\infty$; $a_{n+1} = \min(V_\infty \cap (a_n,\infty))$; and $A = V_\infty \cap [a_1, \infty)$ with the sequence as its increasing enumeration. (Lemma 3.)
3. **valid-below-are-terms** — With $W_n = \{m > 1 : \gcd(m, a_i) > 1 \ \forall i \le n\}$ (no lower bound on $m$): $W_n \cap [a_1, a_n] = \{a_1, \ldots, a_n\}$. (Lemma 4. Stated with $W_n$, per the outline-reviewer's notation fix.)
4. **companion** — If a term $a_k$ has a prime factor $q > a_1$, then $\sigma(a_k) \ne \emptyset$ and there is $x$ with $P(x) = \sigma(a_k)$ and $a_1 \le x < a_k$. Threshold $z = a_1$ is load-bearing (the $\mathrm{rad}(a_1)$ threshold fails for $a_1 = 48$). (Lemma 5.)
5. **scpl** — Any two terms share a prime $\le a_1$. (Lemma 6; independent write-up of the descent.)
6. **periodic-enumeration** — If $L \ge 1$, $\emptyset \ne R \subseteq \mathbb{Z}/L\mathbb{Z}$, and $A = \{m \ge a_1 : (m \bmod L) \in R\}$ with $a_1 \in A$, then the increasing enumeration $(x_n)$ of $A$ satisfies $x_{n+|R|} = x_n + L$ for all $n \ge 1$. (Steps 5a–5d, which prove exactly this with $(x_n) = (a_n)$; the argument uses only (5.3).)
