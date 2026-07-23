## Status
solved

## Approaches tried
- Round 2 (outline): fixed the finite prime universe $Q$ in advance and reduced everything to the Small Common Prime Lemma (SCPL); crux left as a gap. — outcome: correct scaffolding (Clique, Bounded gaps, Reduction, mod-$M$ collapse, periodic enumeration), crux open.
- Round 3 (this round): threshold corrected to $z = a_1$ (the $\mathrm{rad}(a_1)$ and $p_{\max}$ thresholds fail for non-squarefree $a_1$, e.g. $a_1 = 48$, term $56$); the SCPL crux closed by a minimal-counterexample descent (Companion Lemma + valid-below-are-terms + double minimality). — outcome: **complete proof written below**; every lemma proved in full; numerical verification of SCPL, the companion construction, and the membership characterization for $a_1 \in \{15, 26, 32, 48, 49, 77, 105\}$ (300 terms each) passed.

## Current best
Complete proof of the full claim. See `## Full proof`.

## Full proof

**Problem.** Let $a_1, a_2, a_3, \dots$ be an infinite sequence of integers greater than $1$ such that for every positive integer $n$, $a_{n+1}$ is the smallest integer greater than $a_n$ satisfying $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, \dots, n$. Prove that there exist positive integers $T$ and $L$ with $a_{n+T} = a_n + L$ for every positive integer $n$.

### Notation

Fixed throughout:

- $P(m)$ — the set of prime factors of an integer $m > 1$.
- $Q = \{p \text{ prime} : p \le a_1\}$ — the **small primes**. Since $a_1 > 1$, we have $2 \in Q$, so $Q \neq \emptyset$.
- $\sigma(m) = P(m) \cap Q = \{p \text{ prime} : p \mid m,\ p \le a_1\}$ — the small prime factors of $m$.
- $M = \prod_{p \in Q} p$ — the product of all primes $\le a_1$ (a positive integer $\ge 2$).
- $B = \mathrm{rad}(a_1) = \prod_{p \in P(a_1)} p$.
- $W_n = \{m \in \mathbb{Z} : m > 1 \text{ and } \gcd(m, a_i) > 1 \text{ for all } 1 \le i \le n\}$ — the $n$-th constraint set (note: no lower bound on $m$ beyond $m > 1$).
- $V_\infty = \{m \in \mathbb{Z} : m > 1 \text{ and } \gcd(m, a_i) > 1 \text{ for all } i \ge 1\}$.
- $A = \{a_1, a_2, a_3, \dots\}$ — the set of terms of the sequence.

The defining rule of the sequence restates as: for every $n \ge 1$,
$$a_{n+1} = \min\bigl(W_n \cap (a_n, \infty)\bigr). \tag{$\ast$}$$
(The condition $m > 1$ in $W_n$ is automatic for $m > a_n \ge a_1 > 1$, so $(\ast)$ is literally the rule in the problem statement.) In particular the sequence is strictly increasing, so $a_n \ge a_1 + (n-1)$ and $a_n \to \infty$; consequently every integer $x \ge a_1$ satisfies exactly one of: $x \in A$, or $a_n < x < a_{n+1}$ for a (unique) $n \ge 1$.

### Lemma 1 (Clique)

*For all $m \neq n$, $\gcd(a_m, a_n) > 1$.*

**Proof.** Without loss of generality $m > n$ (gcd is symmetric). By $(\ast)$, $a_m \in W_{m-1}$, and $n \le m - 1$, so $\gcd(a_m, a_n) > 1$. $\square$

### Lemma 2 (Bounded gaps)

*For every $n \ge 1$: every multiple of $B = \mathrm{rad}(a_1)$ exceeding $1$ lies in $W_n$, and consequently $a_{n+1} \le a_n + B$.*

**Proof.** Let $m > 1$ with $B \mid m$, and let $1 \le i \le n$. By Lemma 1 (or trivially if $i = 1$), $\gcd(a_i, a_1) > 1$, so some prime $p$ divides both $a_i$ and $a_1$. Since $p \mid a_1$ we have $p \mid B \mid m$, hence $p \mid \gcd(m, a_i)$, so $\gcd(m, a_i) > 1$. As $i \le n$ was arbitrary and $m > 1$, we get $m \in W_n$.

The smallest multiple of $B$ strictly greater than $a_n$ is $B\lceil (a_n+1)/B \rceil \le a_n + B$, and it exceeds $a_n \ge a_1 > 1$, so it lies in $W_n \cap (a_n, \infty)$. By $(\ast)$, $a_{n+1} \le a_n + B$. $\square$

(Lemma 2 also confirms that $W_n \cap (a_n, \infty) \neq \emptyset$, so the greedy rule never gets stuck; the problem grants the sequence exists, but it costs nothing to note this.)

### Lemma 3 (Reduction)

*(i) $A \subseteq V_\infty$.*
*(ii) For every $n \ge 1$, $a_{n+1} = \min\bigl(V_\infty \cap (a_n, \infty)\bigr)$.*
*(iii) $A = V_\infty \cap [a_1, \infty)$; that is, the sequence $(a_n)_{n\ge1}$ is exactly the increasing enumeration of $V_\infty \cap [a_1, \infty)$.*

**Proof.** (i) Fix $k \ge 1$; we show $a_k \in V_\infty$. Certainly $a_k > 1$. For any $i \ge 1$: if $i = k$ then $\gcd(a_k, a_k) = a_k > 1$; if $i \neq k$ then $\gcd(a_k, a_i) > 1$ by Lemma 1. So $a_k \in V_\infty$.

(ii) First, $V_\infty \subseteq W_n$ for every $n$ (the defining condition of $V_\infty$ quantifies over all $i \ge 1$, hence over all $i \le n$). Therefore
$$\min\bigl(V_\infty \cap (a_n, \infty)\bigr) \ \ge\ \min\bigl(W_n \cap (a_n, \infty)\bigr) \ \overset{(\ast)}{=}\ a_{n+1},$$
provided $V_\infty \cap (a_n, \infty) \neq \emptyset$ — which it is, because $a_{n+1} \in V_\infty$ by (i) and $a_{n+1} > a_n$. The same membership gives $\min\bigl(V_\infty \cap (a_n, \infty)\bigr) \le a_{n+1}$. Hence equality.

(iii) ($\subseteq$) By (i) and $a_n \ge a_1$ for all $n$. ($\supseteq$) Let $v \in V_\infty$ with $v \ge a_1$, and suppose $v \notin A$. Since the sequence is strictly increasing and unbounded with $a_1 \le v$, there is $n \ge 1$ with $a_n < v < a_{n+1}$. But then $v \in V_\infty \cap (a_n, \infty)$ and $v < a_{n+1}$, contradicting (ii). So $v \in A$. Finally, since $A \subseteq V_\infty \cap [a_1, \infty) \subseteq A$ and the sequence lists $A$ in increasing order, the sequence is the increasing enumeration of $V_\infty \cap [a_1, \infty)$. $\square$

### Lemma 4 (Valid-below-are-terms)

*For every $n \ge 1$: $W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$.*

**Proof.** By induction on $n$.

*Base $n = 1$.* The interval $[a_1, a_1]$ contains the single integer $a_1$, and $a_1 \in W_1$ since $\gcd(a_1, a_1) = a_1 > 1$. So both sides equal $\{a_1\}$.

*Step.* Assume $W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$; we prove $W_{n+1} \cap [a_1, a_{n+1}] = \{a_1, \dots, a_{n+1}\}$.

($\supseteq$) Each $a_k$ with $k \le n+1$ lies in $[a_1, a_{n+1}]$ (the sequence is increasing) and lies in $W_{n+1}$: indeed $a_k > 1$, and for each $i \le n+1$, $\gcd(a_k, a_i) > 1$ (Lemma 1 if $i \neq k$; trivially if $i = k$).

($\subseteq$) Let $x \in W_{n+1} \cap [a_1, a_{n+1}]$. Note $W_{n+1} \subseteq W_n$ (more constraints). Three exhaustive, disjoint cases by position of $x$ relative to $a_n < a_{n+1}$:

- $x = a_{n+1}$: then $x \in \{a_1, \dots, a_{n+1}\}$. Done.
- $a_n < x < a_{n+1}$: then $x \in W_n \cap (a_n, \infty)$ and $x < a_{n+1}$, contradicting $(\ast)$ (minimality of $a_{n+1}$). This case is impossible.
- $a_1 \le x \le a_n$: then $x \in W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$ by the induction hypothesis. Done. $\square$

### Lemma 5 (Companion Lemma)

*Let $a \in A$ be a term having a prime factor $q > a_1$. Then there exists an integer $x$ with*
$$P(x) = \sigma(a) \quad \text{and} \quad a_1 \le x < a.$$

**Proof.** First, $\sigma(a) \neq \emptyset$: by Lemma 1 (or trivially if $a = a_1$), $\gcd(a, a_1) > 1$, so some prime $p_0$ divides both $a$ and $a_1$; then $p_0 \le a_1$ (a prime factor of $a_1$ is at most $a_1$), so $p_0 \in \sigma(a)$.

Fix any $p \in \sigma(a)$. Then $p \le a_1 < q$, so $p \neq q$; both are primes dividing $a$, so $pq \mid a$, whence
$$a \ \ge\ pq. \tag{5.1}$$

Let $m_0 = \prod_{r \in \sigma(a)} r$ (a squarefree integer $> 1$ with $P(m_0) = \sigma(a)$). Since $p \mid m_0$ and $p \ge 2$, the numbers $m_0 p^t$ ($t = 0, 1, 2, \dots$) increase without bound, so we may choose $t \ge 0$ **minimal** with $m_0 p^t \ge a_1$, and set
$$x = m_0 \, p^t.$$
Since $p \in \sigma(a) = P(m_0)$, multiplying by powers of $p$ introduces no new primes: $P(x) = P(m_0) = \sigma(a)$. And $x \ge a_1$ by the choice of $t$. It remains to prove $x < a$; we split on $t$.

- **Case $t = 0$:** here $x = m_0$. Every prime in $\sigma(a)$ divides $a$, and these primes are pairwise distinct, so $m_0 \mid a$ — indeed $m_0$ is squarefree, so $m_0 \mid \mathrm{rad}(a) \mid a$. Moreover $q > a_1 \ge p'$ for every $p' \in \sigma(a)$, so $q \nmid m_0$; hence $\gcd(m_0, q) = 1$ and $m_0 q \mid a$. Therefore $a \ge m_0 q > m_0 = x$ (as $q \ge 2$). ✓
- **Case $t \ge 1$:** by minimality of $t$, $m_0 p^{t-1} < a_1$, so
$$x = p \cdot \bigl(m_0 p^{t-1}\bigr) < p \, a_1 < p q \ \overset{(5.1)}{\le}\ a,$$
where the middle inequality uses $a_1 < q$ and $p > 0$. ✓

In both cases $a_1 \le x < a$ and $P(x) = \sigma(a)$. $\square$

**Remark (the threshold $z = a_1$ is load-bearing).** Defining "small" by any smaller threshold such as $z = \mathrm{rad}(a_1)$ or $z = \max P(a_1)$ breaks Lemma 5 for non-squarefree $a_1$: for $a_1 = 48$ ($\mathrm{rad} = 6$) the sequence begins $48, 50, 52, 54, 56, \dots$, and the term $56 = 2^3 \cdot 7$ has "large" prime $7 > 6$ and small signature $\{2\}$, but no integer with prime set exactly $\{2\}$ lies in $[48, 56)$ (since $32 < 48 \le 64$). With $z = a_1 = 48$ the prime $7$ is small and no companion is needed for $56$. All that matters downstream is that $Q$ is finite, so we use $z = a_1$ throughout and make no sharpness claim.

### Lemma 6 (Small Common Prime Lemma — SCPL)

*For all indices $i < j$, the terms $a_i$ and $a_j$ share a prime factor $p \le a_1$; equivalently, $\sigma(a_i) \cap \sigma(a_j) \neq \emptyset$.*

(Note: a common prime $p$ of $a_i, a_j$ with $p \le a_1$ is by definition an element of $\sigma(a_i) \cap \sigma(a_j)$, and conversely — so the two formulations are indeed equivalent.)

**Proof.** Strong induction on the larger index $j$. Let $S(j)$ denote the statement: *for every $i < j$, $\sigma(a_i) \cap \sigma(a_j) \neq \emptyset$.*

$S(1)$ is vacuous (no $i < 1$).

Fix $j \ge 2$ and assume $S(j')$ holds for all $j' < j$; we prove $S(j)$.

Suppose, for contradiction, that some $i < j$ has $\sigma(a_i) \cap \sigma(a_j) = \emptyset$, and among all such indices choose $i$ **minimal**. Two immediate consequences:

- **(Minimality of $i$)** For every $s < i$: $\sigma(a_s) \cap \sigma(a_j) \neq \emptyset$. $\tag{6.1}$
- **(A large common prime exists)** By Lemma 1, $\gcd(a_i, a_j) > 1$, so some prime $q$ divides both $a_i$ and $a_j$. If $q \le a_1$ then $q \in \sigma(a_i) \cap \sigma(a_j)$, contradicting the choice of $i$. Hence $q > a_1$. $\tag{6.2}$

**Claim: $i \ge 2$.** If $i = 1$: every prime factor of $a_1$ is $\le a_1$, so $P(a_1) = \sigma(a_1)$. By Lemma 1, $\gcd(a_1, a_j) > 1$, so some prime $r$ divides both; $r \in P(a_1) = \sigma(a_1)$, and $r \mid a_j$ with $r \le a_1$ gives $r \in \sigma(a_j)$. So $\sigma(a_1) \cap \sigma(a_j) \ni r \neq \emptyset$ — contradicting the choice of $i = 1$. Hence $i \ge 2$. (In particular $S(2)$ can have no counterexample at all, since there $i = 1$ is forced; so the induction genuinely starts.)

**Step 1 — build the companion of $a_i$.** By (6.2), the term $a_i$ has the prime factor $q > a_1$, so Lemma 5 applies to $a = a_i$: there is an integer $x$ with
$$P(x) = \sigma(a_i), \qquad a_1 \le x < a_i. \tag{6.3}$$

**Step 2 — $x \in W_{i-1}$.** Since $i < j$, the induction hypothesis gives $S(i)$: for every $s < i$, $\sigma(a_s) \cap \sigma(a_i) \neq \emptyset$. Now fix any $i'$ with $1 \le i' \le i-1$. Pick $r \in \sigma(a_{i'}) \cap \sigma(a_i)$. Then $r \mid a_{i'}$, and $r \in \sigma(a_i) = P(x)$ so $r \mid x$; hence $\gcd(x, a_{i'}) \ge r > 1$. Also $x \ge a_1 > 1$. As $i' \le i-1$ was arbitrary, $x \in W_{i-1}$.

**Step 3 — $x$ is an earlier term.** By (6.3), $a_1 \le x < a_i$; note $i - 1 \ge 1$ by the Claim. Two exhaustive, disjoint cases:

- If $a_{i-1} < x < a_i$: then $x \in W_{i-1} \cap (a_{i-1}, \infty)$ and $x < a_i$. But by $(\ast)$ (with $n = i-1$), $a_i = \min\bigl(W_{i-1} \cap (a_{i-1}, \infty)\bigr)$, so no element of $W_{i-1}$ lies strictly between $a_{i-1}$ and $a_i$. Contradiction — this case is impossible.
- Hence $a_1 \le x \le a_{i-1}$, so $x \in W_{i-1} \cap [a_1, a_{i-1}] = \{a_1, \dots, a_{i-1}\}$ by Lemma 4 (with $n = i-1 \ge 1$).

So $x = a_s$ for some $s \le i - 1 < i$.

**Step 4 — contradiction.** Apply (6.1) to $s < i$: there is a prime $r' \in \sigma(a_s) \cap \sigma(a_j)$. Then:

- $r' \mid a_s = x$ and $r'$ is prime, so $r' \in P(x) = \sigma(a_i)$ by (6.3); in particular $r' \le a_1$ and $r' \mid a_i$.
- $r' \in \sigma(a_j)$, so $r' \mid a_j$.

Hence $r' \in \sigma(a_i) \cap \sigma(a_j)$ — contradicting $\sigma(a_i) \cap \sigma(a_j) = \emptyset$, the defining property of $i$.

This contradiction shows no counterexample $i < j$ exists, i.e. $S(j)$ holds. By strong induction, $S(j)$ holds for all $j \ge 1$, which is the lemma. $\square$

**Remark ($a_1$ a prime or prime power).** If $a_1 = p^e$, then every term shares a prime with $a_1$ (Lemma 1), i.e. is divisible by $p \le a_1$, and SCPL is immediate with the single prime $p$. The proof above covers this case without special handling; the remark is only to note it is not exceptional. Likewise, "no clique edge is carried only by large primes" (Lemma 6) must not be confused with the false statement "terms have no large prime factors" — terms with prime factors $> a_1$ occur (e.g. $a_1 = 48$, term $56 = 2^3\cdot 7$); Lemma 6 says only that such large primes are never the *sole* link between two terms.

### Lemma 7 (Every term has a nonempty small signature)

*For every $a \in A$: $\sigma(a) \neq \emptyset$.*

**Proof.** If $a = a_1$: $P(a_1) = \sigma(a_1) \neq \emptyset$ since $a_1 > 1$. If $a = a_j$ with $j \ge 2$: apply Lemma 6 to the pair $(a_1, a_j)$. $\square$

### Step 5: The term set is determined by residues mod $M$

Let $\mathcal{F} = \{\sigma(a) : a \in A\}$. By Lemma 7, $\mathcal{F}$ is a family of **nonempty** subsets of the finite set $Q$; hence $\mathcal{F}$ is finite (it is a subset of the power set $2^Q$, of size $\le 2^{|Q|}$), even though $A$ is infinite and no "stabilization in time" is claimed or needed.

**Lemma 8 (Membership characterization).**
$$A \;=\; \bigl\{\, m \in \mathbb{Z} : m \ge a_1 \ \text{ and } \ \sigma(m) \cap S \neq \emptyset \ \text{for every } S \in \mathcal{F} \,\bigr\}.$$

**Proof.** ($\subseteq$) Let $m \in A$, say $m = a_k$; then $m \ge a_1$. Let $S \in \mathcal{F}$, say $S = \sigma(a_\ell)$. If $\ell \neq k$, Lemma 6 gives $\sigma(a_k) \cap \sigma(a_\ell) \neq \emptyset$, i.e. $\sigma(m) \cap S \neq \emptyset$. If $\ell = k$, then $\sigma(m) \cap S = \sigma(a_k) \neq \emptyset$ by Lemma 7.

($\supseteq$) Let $m \ge a_1$ satisfy $\sigma(m) \cap \sigma(a) \neq \emptyset$ for every $a \in A$. Then $m \ge a_1 \ge 2 > 1$, and for every $i \ge 1$ there is a prime $p \in \sigma(m) \cap \sigma(a_i)$; since $p \mid m$ and $p \mid a_i$, $\gcd(m, a_i) \ge p > 1$. Hence $m \in V_\infty \cap [a_1, \infty) = A$ by Lemma 3(iii). $\square$

**Lemma 9 (The condition depends only on $m \bmod M$).** For each prime $p \in Q$ we have $p \mid M$, so $m \equiv m' \pmod M$ implies $m \equiv m' \pmod p$, hence $p \mid m \iff p \mid m'$. Therefore $m \equiv m' \pmod M \implies \sigma(m) = \sigma(m')$. Consequently, defining for a residue class $r \in \mathbb{Z}/M\mathbb{Z}$ the set $\sigma(r) = \{p \in Q : m \equiv 0 \pmod p \text{ for } m \in r\}$ (well-defined by the above), and
$$R \;=\; \bigl\{\, r \in \mathbb{Z}/M\mathbb{Z} \ :\ \sigma(r) \cap S \neq \emptyset \ \text{for every } S \in \mathcal{F} \,\bigr\},$$
Lemma 8 becomes
$$A \;=\; \{\, m \ge a_1 \ :\ (m \bmod M) \in R \,\}. \tag{9.1}$$
$R$ is a well-defined subset of the finite set $\mathbb{Z}/M\mathbb{Z}$ because $\mathcal{F}$ is a fixed finite family (Step 5 preamble). Moreover $R \neq \emptyset$: $a_1 \in A$, so by (9.1) read left-to-right, $(a_1 \bmod M) \in R$. $\square$

### Step 6: Conclusion — exact periodicity of the enumeration

Set
$$T = |R| \quad (\ge 1 \text{ by Lemma 9}), \qquad L = M = \prod_{p \le a_1,\ p \text{ prime}} p \quad (\ge 2).$$
Both are positive integers. We claim $a_{n+T} = a_n + L$ for every $n \ge 1$.

**Counting per window.** Fix $n \ge 1$ and consider the half-open window $(a_n,\ a_n + M]$ of $M$ consecutive integers. For each residue class $r \in \mathbb{Z}/M\mathbb{Z}$, the window contains **exactly one** integer congruent to $r$ (any $M$ consecutive integers form a complete residue system mod $M$). Every integer in the window exceeds $a_n \ge a_1$, hence is $\ge a_1$. Therefore, by (9.1),
$$\bigl|A \cap (a_n, a_n + M]\bigr| \;=\; |R| \;=\; T. \tag{6.a}$$

**The right endpoint is a term.** $a_n \in A$, so $(a_n \bmod M) \in R$ by (9.1); and $a_n + M \equiv a_n \pmod M$ with $a_n + M > a_1$. By (9.1) again, $a_n + M \in A$. $\tag{6.b}$

**Identifying positions.** By Lemma 3(iii), the sequence $(a_k)$ enumerates $A$ in increasing order; hence the elements of $A$ strictly greater than $a_n$, listed increasingly, are exactly $a_{n+1} < a_{n+2} < a_{n+3} < \cdots$. By (6.a), exactly $T$ of them lie in $(a_n, a_n + M]$, and since the enumeration is increasing these are precisely the first $T$ of them:
$$A \cap (a_n, a_n + M] \;=\; \{a_{n+1}, a_{n+2}, \dots, a_{n+T}\},$$
with $a_{n+T}$ the largest element of $A$ in the window. By (6.b), $a_n + M \in A \cap (a_n, a_n + M]$, and $a_n + M$ is the largest integer in the window altogether; hence it is the largest element of $A$ in the window, i.e.
$$a_{n+T} \;=\; a_n + M \;=\; a_n + L.$$

Since $n \ge 1$ was arbitrary, $a_{n+T} = a_n + L$ for every positive integer $n$, with the explicit values
$$T = |R| \ \ge 1, \qquad L = \prod_{\substack{p \le a_1 \\ p \text{ prime}}} p \ \ge 2 .$$
$\blacksquare$

### Dependency summary (for the reviewer)

- Lemma 1 uses only the defining rule $(\ast)$.
- Lemma 2 uses Lemma 1.
- Lemma 3 uses Lemma 1 and $(\ast)$.
- Lemma 4 uses Lemma 1 and $(\ast)$.
- Lemma 5 uses Lemma 1 only (via $\sigma(a) \neq \emptyset$); it is pure elementary number theory otherwise.
- Lemma 6 (crux) uses Lemmas 1, 4, 5 and $(\ast)$; strong induction on the larger index, minimal-counterexample descent on the smaller.
- Lemmas 7–9 use Lemmas 3, 6.
- Step 6 uses Lemmas 3(iii) and 9.

No external theorems are invoked; the whole argument is elementary (greedy minimality, strong induction, complete residue systems). Numerical sanity checks (not part of the proof): SCPL, the companion construction, and the membership characterization (Lemma 8) verified for $a_1 \in \{15, 26, 32, 48, 49, 77, 105\}$ over 300 terms each.

## Gaps remaining
None. Every lemma is proved in full; the casework (Lemma 4's three positions, Lemma 5's $t = 0$ vs $t \ge 1$, Lemma 6's $i = 1$ exclusion and Step 3's two positions of $x$) is exhaustive and disjoint; the final claim is derived for all $n \ge 1$ with explicit $T$ and $L$. (`answer_type` is none — no numerical final answer required.)

## Promotable lemmas
All proved in full above; proposed files written to `results/imo-2026-06/lemmas/` pending reviewer certification:
- **clique** (`lemmas/clique.md`): $\gcd(a_m, a_n) > 1$ for all $m \neq n$. Proved as Lemma 1.
- **reduction** (`lemmas/reduction.md`): $a_{n+1} = \min(V_\infty \cap (a_n, \infty))$ and $A = V_\infty \cap [a_1, \infty)$. Proved as Lemma 3.
- **valid-below-are-terms** (`lemmas/valid-below-are-terms.md`): $W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$ (with $W_n$ the unbounded constraint set). Proved as Lemma 4.
- **companion** (`lemmas/companion.md`): a term with a prime factor $> a_1$ has a companion $x$ with $P(x) = \sigma(a)$, $a_1 \le x < a$. Proved as Lemma 5. Threshold $z = a_1$ load-bearing.
- **scpl** (`lemmas/scpl.md`): any two terms share a prime $\le a_1$. Proved as Lemma 6.
- **periodic-enumeration** (`lemmas/periodic-enumeration.md`): the increasing enumeration $(x_n)$ of $\{m \ge a_1 : m \bmod M \in R\}$ (with $x_1 = a_1$ in the set, $R \neq \emptyset$) satisfies $x_{n+|R|} = x_n + M$ for all $n$. Proved as Step 6.
