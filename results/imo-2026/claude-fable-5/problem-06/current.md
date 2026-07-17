## Status
solved

## Approaches tried
- `small-prime-core` — SOLVED (proof-reviewer APPROVE, round 3). Fix prime universe Q={p≤a_1}; SCPL by minimal-counterexample descent (companion lemma, threshold z=a_1); collapse constraints mod M=∏Q; greedy enumeration of exactly-periodic set. Complete, no gaps.
- `wqo-domination` — SOLVED (proof-reviewer APPROVE, round 3). Independent SCPL descent; minimal constraint family E_∞ ⊆ finite 2^Q; V_∞ exactly L-periodic for L=∏(⋃E_∞); greedy enumeration of periodic set from n=1. Complete, no gaps.
- `greedy-clique-closure` — earlier scaffold (round 2), superseded; SCPL crux left open there.

Both solved approaches were independently verified by the reviewer: the SCPL descent (crux) is well-founded (strong induction on the larger index j; minimal-counterexample on the smaller index i; companion x lands as an earlier term by valid-below-are-terms + greedy minimality, forcing a small shared prime). SCPL, the companion construction, and periodicity-from-n=1 were confirmed computationally for a_1 ∈ {2,3,15,26,30,32,48,49,77,105,210} (including the non-squarefree case a_1=48, term 56=2^3·7, where the threshold z=a_1 is load-bearing).

## Current best
Complete rigorous proof of the full claim (below), with explicit T,L.

## Full proof

**Problem.** Let $a_1, a_2, a_3, \dots$ be an infinite sequence of integers greater than $1$ such that for every positive integer $n$, $a_{n+1}$ is the smallest integer greater than $a_n$ satisfying $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, \dots, n$. Prove that there exist positive integers $T$ and $L$ with $a_{n+T} = a_n + L$ for every positive integer $n$.

### Notation

- $P(m)$ — the set of prime factors of an integer $m > 1$.
- $Q = \{p \text{ prime} : p \le a_1\}$ — the **small primes**. Since $a_1 > 1$, $2 \in Q$, so $Q \neq \emptyset$; $Q$ is finite.
- $\sigma(m) = P(m) \cap Q = \{p \text{ prime} : p \mid m,\ p \le a_1\}$ — the small prime factors of $m$.
- $M = \prod_{p \in Q} p$ ($\ge 2$).
- $B = \mathrm{rad}(a_1) = \prod_{p \in P(a_1)} p$.
- $W_n = \{m \in \mathbb{Z} : m > 1,\ \gcd(m, a_i) > 1 \text{ for all } 1 \le i \le n\}$ (no lower bound beyond $m > 1$).
- $V_\infty = \{m \in \mathbb{Z} : m > 1,\ \gcd(m, a_i) > 1 \text{ for all } i \ge 1\}$.
- $A = \{a_1, a_2, \dots\}$.

The defining rule restates as: for every $n \ge 1$,
$$a_{n+1} = \min\bigl(W_n \cap (a_n, \infty)\bigr). \tag{$\ast$}$$
(For $m > a_n \ge a_1 > 1$ the condition $m>1$ is automatic, so $(\ast)$ is literally the rule.) The sequence is strictly increasing, so $a_n \ge a_1 + (n-1)$ and $a_n \to \infty$; every integer $x \ge a_1$ is either a term or lies in a unique gap $a_n < x < a_{n+1}$.

### Lemma 1 (Clique). For all $m \neq n$, $\gcd(a_m, a_n) > 1$.
*Proof.* WLOG $m > n$. By $(\ast)$, $a_m \in W_{m-1}$ and $n \le m-1$, so $\gcd(a_m, a_n) > 1$. $\square$

### Lemma 2 (Bounded gaps / well-posedness). For every $n$, every multiple of $B$ exceeding $1$ lies in $W_n$; hence $W_n \cap (a_n,\infty)\neq\emptyset$ and $a_{n+1} \le a_n + B$.
*Proof.* Let $m>1$, $B\mid m$, $i\le n$. By Lemma 1 (trivial if $i=1$), $\gcd(a_i,a_1)>1$, so a prime $p$ divides $a_i$ and $a_1$; then $p\mid B\mid m$, so $\gcd(m,a_i)>1$. Thus $m\in W_n$. The least multiple of $B$ above $a_n$ is $\le a_n+B$ and exceeds $a_n\ge a_1>1$, so lies in $W_n\cap(a_n,\infty)$; by $(\ast)$, $a_{n+1}\le a_n+B$. $\square$

### Lemma 3 (Reduction). (i) $A \subseteq V_\infty$. (ii) $a_{n+1} = \min(V_\infty \cap (a_n, \infty))$. (iii) $A = V_\infty \cap [a_1, \infty)$, and the sequence is its increasing enumeration.
*Proof.* (i) $a_k>1$; for $i=k$, $\gcd(a_k,a_k)=a_k>1$; for $i\neq k$, Lemma 1. (ii) $V_\infty\subseteq W_n$, so $\min(V_\infty\cap(a_n,\infty))\ge\min(W_n\cap(a_n,\infty))=a_{n+1}$; and $a_{n+1}\in V_\infty\cap(a_n,\infty)$ by (i) gives $\le a_{n+1}$. (iii) ($\subseteq$) by (i) and $a_n\ge a_1$. ($\supseteq$) If $v\in V_\infty$, $v\ge a_1$, $v\notin A$, then $a_n<v<a_{n+1}$ for some $n$ (increasing, unbounded), so $v\in V_\infty\cap(a_n,\infty)$ with $v<a_{n+1}$, contradicting (ii). $\square$

### Lemma 4 (Valid-below-are-terms). For every $n$: $W_n \cap [a_1, a_n] = \{a_1, \dots, a_n\}$.
*Proof.* Induction on $n$. Base $n=1$: $[a_1,a_1]=\{a_1\}$, $a_1\in W_1$. Step: assume for $n$. ($\supseteq$) each $a_k$, $k\le n+1$, is in $[a_1,a_{n+1}]$ and $W_{n+1}$ (Lemma 1). ($\subseteq$) $x\in W_{n+1}\cap[a_1,a_{n+1}]\subseteq W_n$: if $x=a_{n+1}$ done; if $a_n<x<a_{n+1}$ then $x\in W_n\cap(a_n,\infty)$, $x<a_{n+1}$, contradicting $(\ast)$; if $a_1\le x\le a_n$ then $x\in W_n\cap[a_1,a_n]=\{a_1,\dots,a_n\}$ by IH. $\square$

### Lemma 5 (Companion). Let $a\in A$ have a prime factor $q>a_1$. Then $\sigma(a)\neq\emptyset$ and there is an integer $x$ with $P(x)=\sigma(a)$ and $a_1\le x<a$.
*Proof.* $\sigma(a)\neq\emptyset$: $\gcd(a,a_1)>1$ (Lemma 1, trivial if $a=a_1$) gives a prime $p_0\mid a,a_1$, and $p_0\le a_1$, so $p_0\in\sigma(a)$. Fix $p\in\sigma(a)$; $p\le a_1<q$, so $p\neq q$, $pq\mid a$, whence $a\ge pq$ (5.1). Let $m_0=\prod_{r\in\sigma(a)}r$ (squarefree, $P(m_0)=\sigma(a)$). Choose $t\ge0$ minimal with $m_0p^t\ge a_1$, set $x=m_0p^t$; then $P(x)=\sigma(a)$ and $x\ge a_1$. If $t=0$: $x=m_0\mid\mathrm{rad}(a)\mid a$, and $q\nmid m_0$ (as $q>a_1$) so $m_0q\mid a$, giving $a\ge m_0q>m_0=x$. If $t\ge1$: minimality gives $m_0p^{t-1}<a_1$, so $x=p(m_0p^{t-1})<p\,a_1<pq\le a$ by (5.1). $\square$

*(Threshold is load-bearing: with $z=\mathrm{rad}(a_1)$ or $z=\max P(a_1)$ the lemma fails for $a_1=48$, term $56=2^3\cdot7$; with $z=a_1$ the prime $7$ is small and no companion is needed. Only finiteness of $Q$ is used downstream.)*

### Lemma 6 (Small Common Prime Lemma, SCPL). For all $i<j$: $\sigma(a_i)\cap\sigma(a_j)\neq\emptyset$.
*Proof.* Strong induction on $j$; $S(j)$: "$\sigma(a_i)\cap\sigma(a_j)\neq\emptyset$ for all $i<j$." $S(1)$ vacuous. Fix $j\ge2$, assume $S(j')$ for all $j'<j$. Suppose some $i<j$ has $\sigma(a_i)\cap\sigma(a_j)=\emptyset$; take $i$ **minimal**.
- (6.1) For $s<i$: $\sigma(a_s)\cap\sigma(a_j)\neq\emptyset$ (minimality of $i$).
- (6.2) $\gcd(a_i,a_j)>1$ (Lemma 1) gives a common prime $q$; $q\le a_1$ would contradict the choice of $i$, so $q>a_1$.
- $i\ge2$: if $i=1$, a common prime $r$ of $a_1,a_j$ lies in $P(a_1)=\sigma(a_1)$ and in $\sigma(a_j)$, contradiction.

**Step 1.** By (6.2), Lemma 5 applied to $a_i$ gives $x$ with $P(x)=\sigma(a_i)$, $a_1\le x<a_i$ (6.3).
**Step 2 ($x\in W_{i-1}$).** Since $i<j$, $S(i)$ holds by the IH: for $i'\le i-1$ pick $r\in\sigma(a_{i'})\cap\sigma(a_i)$; then $r\mid a_{i'}$ and $r\mid x$ (as $r\in\sigma(a_i)=P(x)$), so $\gcd(x,a_{i'})>1$. Also $x>1$.
**Step 3 ($x$ is an earlier term).** $i-1\ge1$. If $a_{i-1}<x<a_i$: $x\in W_{i-1}\cap(a_{i-1},\infty)$, $x<a_i$, contradicting $(\ast)$. Hence $a_1\le x\le a_{i-1}$, so by Lemma 4, $x=a_s$, $s\le i-1$.
**Step 4 (contradiction).** By (6.1) with $s<i$: pick $r'\in\sigma(a_s)\cap\sigma(a_j)$. Then $r'\mid a_s=x$ so $r'\in P(x)=\sigma(a_i)$ (so $r'\le a_1$, $r'\mid a_i$); and $r'\mid a_j$. Hence $r'\in\sigma(a_i)\cap\sigma(a_j)$, contradiction. Thus $S(j)$ holds. $\square$

### Lemma 7. For every $a\in A$, $\sigma(a)\neq\emptyset$.
*Proof.* $a=a_1$: $P(a_1)=\sigma(a_1)\neq\emptyset$. $a=a_j$, $j\ge2$: Lemma 6 on $(a_1,a_j)$. $\square$

### Step 5: The term set is determined by residues mod $M$
Let $\mathcal{F}=\{\sigma(a):a\in A\}$, a finite family of nonempty subsets of $Q$ (Lemma 7; $\mathcal{F}\subseteq2^Q$).

**Lemma 8.** $A = \{m\ge a_1 : \sigma(m)\cap S\neq\emptyset\text{ for every }S\in\mathcal{F}\}$.
*Proof.* ($\subseteq$) $m=a_k\ge a_1$; for $S=\sigma(a_\ell)$: if $\ell\neq k$, Lemma 6; if $\ell=k$, Lemma 7. ($\supseteq$) $m\ge a_1$ with the property: for each $i$, a prime $p\in\sigma(m)\cap\sigma(a_i)$ gives $\gcd(m,a_i)>1$, so $m\in V_\infty\cap[a_1,\infty)=A$ by Lemma 3(iii). $\square$

**Lemma 9.** $m\equiv m'\pmod M\Rightarrow\sigma(m)=\sigma(m')$ (each $p\in Q$ divides $M$). Defining $\sigma(r)$ for $r\in\mathbb{Z}/M\mathbb{Z}$ and $R=\{r:\sigma(r)\cap S\neq\emptyset\ \forall S\in\mathcal{F}\}$,
$$A = \{m\ge a_1 : (m\bmod M)\in R\}. \tag{9.1}$$
$R$ is a well-defined subset of the finite set $\mathbb{Z}/M\mathbb{Z}$, and $R\neq\emptyset$ since $a_1\in A\Rightarrow(a_1\bmod M)\in R$.

### Step 6: Conclusion
Set $T=|R|\ (\ge1)$, $L=M=\prod_{p\le a_1}p\ (\ge2)$. Fix $n\ge1$. The window $(a_n,a_n+M]$ has $M$ consecutive integers, hence exactly one per residue class mod $M$, all $\ge a_1$; by (9.1), $|A\cap(a_n,a_n+M]|=|R|=T$. Also $a_n+M\equiv a_n\pmod M$ with $a_n\in A$ and $a_n+M>a_1$, so $a_n+M\in A$. Since $(a_k)$ enumerates $A$ increasingly, $A\cap(a_n,a_n+M]=\{a_{n+1},\dots,a_{n+T}\}$ with $a_{n+T}$ its largest element; and $a_n+M$ is the largest integer in the window, hence the largest element of $A$ there. Therefore
$$a_{n+T}=a_n+M=a_n+L\qquad\text{for every }n\ge1,$$
with $T=|R|\ge1$ and $L=\prod_{p\le a_1,\ p\text{ prime}}p\ge2$. $\blacksquare$

*(The identity holds from $n=1$: no transient, since the enumeration of the exactly-periodic set $A$ begins at $a_1\in A$. `answer_type` is none; no numeric answer to verify. An independent second proof — `wqo-domination` — reaches the same conclusion via the inclusion-minimal constraint family $E_\infty\subseteq2^Q$ and $L=\prod(\bigcup E_\infty)$.)*
