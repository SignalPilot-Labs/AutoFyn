# IMO Problem 6 — Solution

**Problem.** Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, 2, \ldots, n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T} = a_n + L$ for every positive integer $n$.

---

## Notation

For an integer $m \ge 2$, let $P(m)$ denote the set of prime divisors of $m$, and $\operatorname{rad}(m) = \prod_{p \in P(m)} p$. Note $\gcd(m, m') > 1 \iff P(m) \cap P(m') \neq \emptyset$.

Define
$$S := \{\, m \in \mathbb{Z}_{\ge 2} : \gcd(m, a_i) > 1 \text{ for all } i \ge 1 \,\}.$$

The sequence $(a_n)$ is strictly increasing, so $a_n \to \infty$.

## Step 1: The sequence is exactly the enumeration of $S \cap [a_1, \infty)$

**Lemma 1.** $\gcd(a_i, a_j) > 1$ for all $i \neq j$. Consequently $a_j \in S$ for every $j$.

*Proof.* For $i < j$, the term $a_j$ was chosen (at step $n = j-1 \ge i$) so that $\gcd(a_j, a_k) > 1$ for all $k \le j - 1$; in particular for $k = i$. This gives the claim for all $i \ne j$ (the relation is symmetric). Then for any fixed $j$: $\gcd(a_j, a_i) > 1$ for $i \neq j$, and $\gcd(a_j, a_j) = a_j > 1$; hence $a_j \in S$. $\blacksquare$

**Lemma 2 (Structure).** $\{a_n : n \ge 1\} = S \cap [a_1, \infty)$, and $(a_n)_{n\ge1}$ is the increasing enumeration of this set.

*Proof.* By Lemma 1, every term lies in $S \cap [a_1, \infty)$. Conversely, let $m \in S$, $m > a_1$, and suppose $m$ is not a term. Since $a_n \to \infty$ and $a_1 < m$, there is an index $n$ with $a_n < m < a_{n+1}$. But $m \in S$ means $\gcd(m, a_i) > 1$ for **all** $i$, in particular for $i = 1, \dots, n$; since $m > a_n$, the minimality in the definition of $a_{n+1}$ forces $a_{n+1} \le m$, a contradiction. Finally $a_1 \in S \cap [a_1,\infty)$ is the first term. Since the terms are increasing, they enumerate $S \cap [a_1,\infty)$ in increasing order. $\blacksquare$

**Lemma 3 (A coprime term below every non-member).** If $m > a_1$ and $m \notin S$, then there exists a term $s = a_i$ with $s < m$ and $\gcd(s, m) = 1$.

*Proof.* As $m > a_1$ and $m \notin S$ (so $m$ is not a term, by Lemma 1), there is $n$ with $a_n < m < a_{n+1}$; the terms smaller than $m$ are exactly $a_1, \dots, a_n$. If every one of them had a common factor with $m$, then the minimality in the definition of $a_{n+1}$ would force $a_{n+1} \le m < a_{n+1}$, absurd. Hence some $a_i$ with $i \le n$ satisfies $\gcd(a_i, m) = 1$. $\blacksquare$

## Step 2: The family of prime sets of terms is a self-dual intersecting family

Define the family of finite, nonempty prime sets
$$\mathcal{F} := \{\, P(a_n) : n \ge 1 \,\}.$$

Call a set $A$ of primes a **transversal** if $A \cap F \neq \emptyset$ for every $F \in \mathcal{F}$.

**(F1)** *Any two elements of $\mathcal{F}$ intersect, and every element of $\mathcal{F}$ is a transversal.*

Indeed, elements of $\mathcal F$ are the sets $P(a_j)$; for $j \ne i$, $\gcd(a_j, a_i) > 1$ gives $P(a_j) \cap P(a_i) \ne \emptyset$ (Lemma 1), and $P(a_j) \cap P(a_j) \neq \emptyset$ trivially. Thus $P(a_j)$ meets every $P(a_i)$, i.e. it is a transversal.

**(F2)** *$m \in S \iff P(m)$ is a transversal* (for any integer $m \ge 2$).

Indeed, $m \in S \iff \gcd(m, a_i) > 1\ \forall i \iff P(m) \cap P(a_i) \neq \emptyset\ \forall i$.

**(F3)** *Every finite transversal belongs to $\mathcal{F}$.*

Let $A$ be a finite transversal. Since $\mathcal F$ consists of nonempty sets, $A \neq \emptyset$. Choose $k \ge 1$ with $m := \big(\prod_{p \in A} p\big)^k > a_1$. Then $P(m) = A$, so $m \in S$ by (F2); by Lemma 2, $m$ is a term, hence $A = P(m) \in \mathcal{F}$.

Now let
$$\mathfrak{B} := \{\, B \in \mathcal{F} : \text{no } F \in \mathcal{F} \text{ satisfies } F \subsetneq B \,\}$$
be the set of **minimal members** of $\mathcal{F}$.

**(F4)** *Every $F \in \mathcal{F}$ contains some $B \in \mathfrak{B}$; $\mathfrak{B} \ne \emptyset$; $\mathfrak{B}$ is an antichain (no member strictly contains another); and any two members of $\mathfrak B$ intersect.*

Indeed, $F$ is finite, so among the finitely many elements of $\mathcal{F}$ contained in $F$ (there is at least one, $F$ itself) pick one, say $B$, minimal with respect to inclusion; if some $G \in \mathcal{F}$ had $G \subsetneq B$, then $G \subseteq F$ would contradict that choice, so $B \in \mathfrak{B}$. The antichain property is immediate from the definition, and members of $\mathfrak B$ intersect pairwise because $\mathfrak{B} \subseteq \mathcal{F}$ and (F1).

**(F5)** *Every finite transversal contains a member of $\mathfrak{B}$; conversely every $B\in\mathfrak B$ is a transversal.*

By (F3) a finite transversal lies in $\mathcal{F}$, then apply (F4); the converse is (F1).

The heart of the proof is:

> **Main Lemma.** $\mathfrak{B}$ is finite.

Before proving it, we record the key consequence of the greedy rule (Lemma 3) in this combinatorial language.

## Step 3: The descent lemma

For a finite set $A$ of primes write $\pi(A) := \prod_{p \in A} p$ (so $\pi(\emptyset) = 1$).

**Lemma 4 (Descent step).** Let $B \in \mathfrak{B}$ and $p \in B$ be such that $\pi(B \setminus \{p\}) > a_1$. Then there exists $B' \in \mathfrak{B}$ with
$$B' \cap B = \{p\} \qquad \text{and} \qquad \pi(B') < \pi(B \setminus \{p\}) = \frac{\pi(B)}{p}.$$

*Proof.* Put $A := B \setminus \{p\}$ and $m := \pi(A) > a_1$ (in particular $A \ne \emptyset$, $m \ge 2$).

First, $A$ is **not** a transversal: otherwise, $A$ being finite, (F3) would give $A \in \mathcal{F}$ with $A \subsetneq B$, contradicting the minimality of $B \in \mathfrak{B}$.

Since $P(m) = A$ is not a transversal, $m \notin S$ by (F2). As $m > a_1$, Lemma 3 provides a term $s < m$ with $\gcd(s, m) = 1$, i.e. $P(s) \cap A = \emptyset$.

Now $P(s) \in \mathcal{F}$, so by (F4) there is $B' \in \mathfrak{B}$ with $B' \subseteq P(s)$; then $B' \cap A = \emptyset$. By (F4), $B' \cap B \neq \emptyset$; since $B = A \cup \{p\}$ and $B' \cap A = \emptyset$, we get $B' \cap B = \{p\}$ (in particular $p \in B'$).

Finally, $\pi(B') \le \pi(P(s)) = \operatorname{rad}(s) \le s < m = \pi(A)$. $\blacksquare$

**Lemma 5.** For every prime $p$ that lies in some member of $\mathfrak{B}$, there exists $C_p \in \mathfrak{B}$ with
$$p \in C_p \qquad \text{and} \qquad \pi(C_p \setminus \{p\}) \le a_1 .$$

*Proof.* Start with any $B^{(0)} \in \mathfrak{B}$ containing $p$. Iterate: if $\pi(B^{(i)} \setminus \{p\}) \le a_1$, stop and set $C_p := B^{(i)}$. Otherwise apply Lemma 4 to $(B^{(i)}, p)$ — legitimate since $p \in B^{(i)}$ — to get $B^{(i+1)} \in \mathfrak{B}$ with $p \in B^{(i+1)}$ and
$$\pi(B^{(i+1)}) < \frac{\pi(B^{(i)})}{p} < \pi(B^{(i)}).$$
The positive integers $\pi(B^{(i)})$ strictly decrease, so the iteration terminates, yielding the desired $C_p$. $\blacksquare$

## Step 4: Proof of the Main Lemma ($\mathfrak{B}$ is finite)

Suppose, for contradiction, that $\mathfrak{B}$ is infinite. Since all members are finite sets of primes, the union $U := \bigcup_{B \in \mathfrak{B}} B$ must be infinite (a finite $U$ has only finitely many subsets).

For each $p \in U$, Lemma 5 gives $C_p \in \mathfrak{B}$ with $p \in C_p$ and $D_p := C_p \setminus \{p\}$ satisfying $\pi(D_p) \le a_1$. Every prime in $D_p$ is then at most $a_1$, so $D_p$ ranges over the (finitely many) subsets of the finite set $\{\text{primes} \le a_1\}$. Since $U$ is infinite, by the pigeonhole principle there is a fixed set $D$ and an **infinite** set $\mathcal{Q}$ of primes such that
$$C_p = \{p\} \cup D, \qquad p \notin D, \qquad \text{for all } p \in \mathcal{Q}.$$

**Case $D = \emptyset$.** Then $\{p\}, \{p'\} \in \mathfrak{B}$ for two distinct $p, p' \in \mathcal{Q}$, and they are disjoint — contradicting (F4) (members intersect pairwise).

**Case $D \neq \emptyset$.** We claim $D$ is a transversal. Let $F \in \mathcal{F}$ be arbitrary. For every $p \in \mathcal{Q}$ we have $F \cap C_p \neq \emptyset$ by (F1) (both lie in $\mathcal{F}$). If $F \cap D = \emptyset$, this forces $p \in F$ for every $p \in \mathcal{Q}$ — impossible, as $F$ is finite and $\mathcal{Q}$ is infinite. Hence $F \cap D \neq \emptyset$ for all $F \in \mathcal{F}$, i.e. $D$ is a finite transversal.

By (F5), $D$ contains some member $C^* \in \mathfrak{B}$. Fix any $p_0 \in \mathcal{Q}$. Then
$$C^* \subseteq D \subsetneq \{p_0\} \cup D = C_{p_0},$$
where the inclusion $D \subsetneq C_{p_0}$ is strict because $p_0 \notin D$. So $C^* \subsetneq C_{p_0}$ with both $C^*, C_{p_0} \in \mathfrak{B}$ — contradicting that $\mathfrak{B}$ is an antichain (F4).

Both cases are contradictory, so $\mathfrak{B}$ is finite. $\blacksquare$

## Step 5: Conclusion

Let $U := \bigcup_{B \in \mathfrak{B}} B$, a finite nonempty set of primes (finite by the Main Lemma; nonempty since $\mathfrak{B} \neq \emptyset$ by (F4)). Define
$$L := \prod_{p \in U} p \;\ge 2.$$

**Claim.** For $m \ge 2$: $\; m \in S \iff P(m) \cap B \neq \emptyset$ for every $B \in \mathfrak{B}$.

*Proof.* ($\Rightarrow$) If $m \in S$, then $P(m)$ is a transversal by (F2), and $\mathfrak{B} \subseteq \mathcal{F}$, so $P(m)$ meets every member. ($\Leftarrow$) If $P(m)$ meets every $B \in \mathfrak{B}$, then for any $F \in \mathcal{F}$ pick $B \subseteq F$ with $B \in \mathfrak{B}$ (F4); then $P(m) \cap F \supseteq P(m) \cap B \neq \emptyset$. So $P(m)$ is a transversal and $m \in S$ by (F2). $\blacksquare$

The condition "$P(m) \cap B \neq \emptyset$ for all $B \in \mathfrak{B}$" says: for each $B \in \mathfrak{B}$ there is $p \in B$ ($\subseteq U$) with $p \mid m$. Divisibility of $m$ by primes of $U$ depends only on $m \bmod L$. Hence, for all integers $m, m' \ge 2$:
$$m \equiv m' \pmod{L} \implies (m \in S \iff m' \in S). \tag{$\ast$}$$

Now set
$$T := \#\big( S \cap [a_1,\, a_1 + L) \big).$$
Then $T \ge 1$ since $a_1 \in S$, so $T$ is a positive integer.

Fix any $n \ge 1$. By Lemma 2, $(a_k)$ is the increasing enumeration of $S \cap [a_1, \infty)$. Since $a_n \in S$, $(\ast)$ gives $a_n + L \in S$, and $a_n + L \ge a_1$. Count the elements of $S \cap [a_1, \infty)$ that are smaller than $a_n + L$:
$$\#\big(S \cap [a_1, a_n + L)\big) = \#\big(S \cap [a_1, a_1 + L)\big) + \#\big(S \cap [a_1 + L, a_n + L)\big).$$
By $(\ast)$, the map $x \mapsto x - L$ is a bijection from $S \cap [a_1 + L, a_n + L)$ onto $S \cap [a_1, a_n)$ (both directions preserve membership in $S$, and all numbers involved are $\ge a_1 \ge 2$). By Lemma 2, $\#\big(S \cap [a_1, a_n)\big) = n - 1$ (its elements are exactly $a_1, \dots, a_{n-1}$). Therefore
$$\#\big(S \cap [a_1, a_n + L)\big) = T + (n-1),$$
which means $a_n + L$ is preceded by exactly $T + n - 1$ elements in the enumeration, i.e. $a_n + L$ is the $(n+T)$-th element:
$$a_{n+T} = a_n + L .$$

Since $n \ge 1$ was arbitrary, the positive integers $T$ and $L$ satisfy $a_{n+T} = a_n + L$ for every positive integer $n$. $\qquad\blacksquare$
