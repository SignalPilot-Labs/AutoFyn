## Lemma (Every term is divisible by a "recurring" prime)

Let $(a_n)$ be the problem's greedy sequence, $R(m)$ the set of distinct prime
divisors of $m$, and
$$S := \{\, p \text{ prime} : p \mid a_n \text{ for infinitely many } n \,\}.$$
Then:
(a) $S \neq \emptyset$.
(b) For **every** index $i \ge 1$ (not merely eventually), $R(a_i) \cap S \neq
\emptyset$ — every single term, including transient early terms, is divisible
by at least one prime that recurs infinitely often in the whole sequence.

### Proof
Fix $i \ge 1$. For every $j > i$, the defining property of the sequence
(applied at step $j-1 \ge i$) requires $\gcd(a_j, a_i) > 1$, since $i \le j-1$.
Hence $R(a_j) \cap R(a_i) \neq \emptyset$ for every $j > i$; for each such $j$
pick a witness prime $w(j) \in R(a_j) \cap R(a_i)$.

$R(a_i)$ is finite (a_i has finitely many prime factors) while there are
infinitely many indices $j > i$. By the pigeonhole principle, some single
prime $p \in R(a_i)$ equals $w(j)$ for infinitely many $j$. For each such $j$,
$p \mid a_j$ (since $w(j) = p \in R(a_j)$), so $p$ divides infinitely many
terms of the sequence, i.e. $p \in S$. Since also $p \in R(a_i)$, we conclude
$R(a_i) \cap S \neq \emptyset$. This proves (b) for every $i \ge 1$; taking
$i=1$ gives (a): $S \supseteq R(a_1) \cap S \neq \emptyset$. $\blacksquare$

### Remark
This does not assume, and does not establish, that $S$ is finite — it holds
regardless. Finiteness of $S$ remains the open central gap of the problem as
of round 1.

### Provenance
Proved identically (independently) in `approaches/active-set-stabilization.md`
(Lemma 2, "Every term is covered by the active set") and
`approaches/state-compactness-pigeonhole.md` (Lemma D). Certified by the
proof-reviewer, round 1: both proofs are the same correct pigeonhole argument
depending only on the problem's defining property (no circularity, no
assumption on finiteness of $S$).
