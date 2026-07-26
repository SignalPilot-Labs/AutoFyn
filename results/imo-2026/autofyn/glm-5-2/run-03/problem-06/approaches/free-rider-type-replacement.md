# free-rider-type-replacement

## Status
partial

## Approaches tried
- (round 1) type-competition among free-riders — crux Gap F (same-type replacement) computationally **REFUTED** on $a_1=385$ (no-lock rich case): free-riders $2$ and $3$ have identical type $(A=\{5\},B=\{5,7,11\})$ and both remain non-redundant through $n\ge600$ with no replacement. Further refuted on $a_1=715$: $91$ free-riders of the *same* type $(A=\{5\},B=\{5\})$ with distinct insertion times coexist (transiently, before the sequence locks at $5^5=3125$). The "one free-rider per type" bound is false; the approach cannot yield a proof via same-type replacement. The finiteness wall this approach must cross is *identical* to `transversal-saturation`'s Gap A; the free-rider framing renames it without supplying a new mechanism.

## Current best
Proved foundation (shared with all approaches): linchpin (every $a_n$ is divisible by some prime $p\mid a_1$), gap bound $d_n\le M_1=\operatorname{rad}(a_1)$, pairwise-intersecting supports, hitting-set reformulation $\mathcal B_n=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{\operatorname{rad}(T)\mid m\}$. Type classification of free-riders defined and shown finite ($\le 4^{|P_1|}$ types). Conditional endgame proved: *if* $\operatorname{MT}(\mathcal F_n)$ stabilizes to $\operatorname{MT}_\infty$ (Gap A, unproved) *and* the greedy always lands in $\mathcal B_\infty$ from $n=1$ (Gap B, unproved), then the cyclic-successor map on $A=\mathcal B_\infty\bmod L$ is a bijection whose every orbit is a cycle, giving $a_{n+T}=a_n+L$ for all $n\ge1$. **Open gap that kills the approach:** Gap F (same-type replacement) is *false*; no per-type finiteness bound is available, so the approach provides no route to Gap A distinct from `transversal-saturation`.

## Full proof
Not present (Status: partial). The foundation and the conditional endgame are proved below; the approach-specific crux (Gap F) is refuted, so the spine does not close.

---

### 1. Foundation (proved)

Let $S(m)$ denote the set of prime divisors of $m$, $P_1:=S(a_1)$, and $M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$.

**Lemma 1 (linchpin).** *For every $n\ge1$, $a_n$ is divisible by some prime $p\in P_1$.*

*Proof.* For $n=1$ this is the definition of $P_1$. For $n\ge2$, the admissibility condition defining $a_n$ includes the index $i=1$, so $\gcd(a_n,a_1)>1$; hence $a_n$ shares a prime factor with $a_1$, i.e. some $p\in P_1$ divides $a_n$. $\square$

**Lemma 2 (gap bound).** *$d_n:=a_{n+1}-a_n\le M_1$ for all $n\ge1$.*

*Proof.* Set $m:=a_n+M_1$. Then $m>a_n$, and $M_1\mid m$ means every $p\in P_1$ divides $m$. By Lemma 1, each $a_i$ ($i\le n$) is divisible by some $p_i\in P_1$; since $p_i\mid M_1\mid m$, we have $\gcd(m,a_i)\ge p_i>1$. Thus $m$ is admissible at step $n$. As $a_{n+1}$ is the *smallest* admissible integer exceeding $a_n$, $a_{n+1}\le m=a_n+M_1$, i.e. $d_n\le M_1$. $\square$

**Lemma 3 (pairwise-intersecting supports).** *The family $\mathcal F_n:=\{S(a_1),\dots,S(a_n)\}$ is pairwise-intersecting: $S(a_i)\cap S(a_j)\ne\varnothing$ for all $i,j\le n$.*

*Proof.* For $i<j$, $a_j$ was chosen admissible at step $j-1$, so $\gcd(a_j,a_i)>1$, i.e. $S(a_i)\cap S(a_j)\ne\varnothing$. $\square$

**Lemma 4 (hitting-set reformulation).** *An integer $m>a_n$ is admissible at step $n$ iff $S(m)$ is a transversal (hitting set) of $\mathcal F_n$. Consequently*
$$\mathcal B_n:=\{m:S(m)\text{ hits every }S(a_i),\,i\le n\}=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{m\in\mathbb Z_{>0}:\operatorname{rad}(T)\mid m\},$$
*where $\operatorname{MT}(\mathcal F_n)$ is the family of minimal transversals of $\mathcal F_n$.*

*Proof.* $\gcd(m,a_i)>1\Leftrightarrow S(m)\cap S(a_i)\ne\varnothing$, so admissibility is exactly the transversal condition. If $S(m)$ is a transversal, it contains a minimal transversal $T\subseteq S(m)$; then $\operatorname{rad}(T)\mid\operatorname{rad}(S(m))\mid m$ (the last divisibility because every prime of $S(m)$ divides $m$). Conversely, if $\operatorname{rad}(T)\mid m$ for some minimal transversal $T$, then $T\subseteq S(m)$, so $S(m)$ is a transversal. $\square$

The greedy rule is $a_{n+1}=\min\bigl(\mathcal B_n\cap(a_n,\infty)\bigr)$.

### 2. Type classification of free-riders (defined; finite)

Call a prime $q$ a *free rider* at step $n$ if $q\notin P_1$ and $q$ belongs to some minimal transversal of $\mathcal F_n$ (i.e. $q$ is non-redundant and not a prime of $a_1$). Let $i(q)$ be the index of the first term with $q\mid a_{i(q)}$ (the *witnessing term*). Define the *type* of $q$ at step $n$:
$$\tau_n(q)=\bigl(A(q),\,B_n(q)\bigr),\quad A(q):=S(a_{i(q)})\cap P_1\subseteq P_1,\quad B_n(q):=\{p\in P_1:\exists\,T\in\operatorname{MT}(\mathcal F_n),\ q\in T,\ p\notin T\}\subseteq P_1.$$

**Lemma 5 (finite type set).** *There are at most $4^{|P_1|}$ distinct types.*

*Proof.* Both components lie in $2^{P_1}$, so $|\{(\cdot,\cdot)\}|\le |2^{P_1}|^2=4^{|P_1|}$. $\square$

This is the only point where the framing yields finiteness for free: the type *labels* are finite in number. The crux was to be a *replacement lemma* showing at most one free-rider per type persists — which would bound the active free-rider set. That crux is false.

### 3. Gap F (same-type replacement) — REFUTATED

**Conjectured lemma (Gap F, FALSE).** *If $q_1<q_2$ (in insertion order) are two non-redundant free-riders at step $n$ with $\tau_n(q_1)=\tau_n(q_2)$, then $q_1$ becomes redundant after $q_2$'s insertion.*

**Refutation on $a_1=385$.** Take $a_1=385=5\cdot7\cdot11$, so $P_1=\{5,7,11\}$. The sequence begins
$$385,\ 390,\ 392,\ 396,\ 399,\ 406,\ 418,\ 420,\ 434,\ 448,\ 450,\ 462,\dots$$
A direct computation (verified by the prime-set intersection criterion of Lemma 4 and by checking each $a_{n+1}$ is minimal admissible) shows:

- *No lock:* among the first $600$ terms, none is a prime power (no term has $|S(a_n)|=1$); the minimal-transversal family stabilizes at $n=38$ to $7$ transversals with $L=\operatorname{lcm}\{\operatorname{rad}(T)\}=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$, and the sequence follows the cyclic successor on $A=\mathcal B_\infty\bmod 43890$ (period $T=5088$) from $n=38$ onward. This is a genuine no-lock rich case.
- The stabilized non-redundant prime set is $\{2,3,5,7,11,19\}$; the free-riders are $\{2,3,19\}$, stable through $n\ge600$.
- Both $2$ and $3$ are non-redundant at every step $n\ge38$, and at every such step they have the *identical* type
$$\tau(2)=\tau(3)=\bigl(A=\{5\},\ B=\{5,7,11\}\bigr)$$
  (witnessing term $a_2=390=2\cdot3\cdot5\cdot13$, so $A(2)=A(3)=\{5\}$; for both, every $p\in P_1$ is avoided by some minimal transversal containing the prime, so $B=\{5,7,11\}$).
- Yet *neither* makes the other redundant: both persist as non-redundant through $n\ge600$.

This directly falsifies Gap F. The two same-type free-riders are *complementary*, not mutually replacing: each is the unique hitter of a different collection of terms, so each is essential to a different minimal transversal. The type $(A,B)$ is too coarse to detect this — it records only the $P_1$-interaction pattern, which is identical for $2$ and $3$, even though the two primes hit genuinely different sets of historical terms.

**Further refutation on $a_1=715=5\cdot11\cdot13$.** Before this sequence locks (it eventually reaches $3125=5^5$, a prime power, and locks at $L=5$), the non-redundant free-rider set grows monotonically to $91$ members at $n=400$, *all of the single type* $(A=\{5\},B=\{5\})$, with distinct insertion times spanning $n=1$ to $n=348$. No same-type replacement occurs at any point during the growth — the later same-type free-riders do *not* make the earlier ones redundant. (The growth terminates only because the sequence locks, a mechanism unrelated to type replacement.)

**Conclusion.** Gap F is false in both the no-lock rich regime ($a_1=385$) and the transient-growth regime ($a_1=715$). The "at most one free-rider per type" bound does not hold, so step 4 of the outline (active free-rider set bounded by number of types) fails. No per-type finiteness argument is available from this framing.

### 4. Why the approach collapses to `transversal-saturation`'s wall

The theorem's load-bearing fact is: *the set $\bigcup_n\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}T$ of primes that ever enter a minimal transversal is finite.* This is exactly `transversal-saturation`'s Gap A. The free-rider framing partitions this set by type and seeks a per-type bound via replacement; since the replacement lemma (Gap F) is false, the partition yields no bound, and one is left having to prove the finiteness directly — i.e., to cross the same wall as `transversal-saturation`, by the same antichain-shrink / no-lock-structure mechanism. The framing supplies no new mechanism for that wall.

### 5. Conditional endgame (proved, modulo the shared gaps)

The following is rigorous *once* the two shared gaps (Gap A: stabilization of $\operatorname{MT}$; Gap B: pure-from-start) are closed. I record it because it is the clean combinatorial core the whole population converges on, and it is independent of the (now-refuted) Gap F.

**Lemma 6 (cyclic successor is a bijection).** *Suppose $\operatorname{MT}(\mathcal F_n)$ stabilizes for $n\ge N_0$ to a fixed family $\operatorname{MT}_\infty$. Set $L:=\operatorname{lcm}\{\operatorname{rad}(T):T\in\operatorname{MT}_\infty\}$ and $A:=\mathcal B_\infty\bmod L\subseteq\mathbb Z/L\mathbb Z$. The map $f:A\to A$, $f(r)$ = the least residue $r'\in A$ strictly after $r$ in the cyclic order on $\mathbb Z/L\mathbb Z$, is a bijection; hence every orbit of $f$ is a cycle (no tail).*

*Proof.* Since each $\operatorname{rad}(T)\mid L$, each set $\{m:\operatorname{rad}(T)\mid m\}$ is a union of residue classes mod $L$; hence $\mathcal B_\infty$ is $L$-periodic ($m\in\mathcal B_\infty\Leftrightarrow m+L\in\mathcal B_\infty$), and $A$ is well defined. $A\ne\varnothing$ (any $\operatorname{rad}(T)$ is in $A$). For $r\in A$, $f(r)$ exists because $A$ is nonempty finite. The map $g:A\to A$ sending $r$ to the greatest residue of $A$ strictly before $r$ cyclically is a well-defined two-sided inverse: the predecessor of the successor is the original, and vice versa. Thus $f$ is a bijection. A bijection on a finite set decomposes $\mathbb Z/L\mathbb Z$-orbits into disjoint cycles, so the forward orbit of every $r\in A$ under $f$ returns to $r$ after finitely many steps (the orbit has no tail). $\square$

**Lemma 7 (periodicity, conditional on Gap B).** *Suppose Gap A holds (so $\mathcal B_\infty$ exists) and Gap B holds: the greedy always lands in $\mathcal B_\infty$, i.e. $\min(\mathcal B_n\cap(a_n,\infty))=\min(\mathcal B_\infty\cap(a_n,\infty))$ for every $n\ge1$, and $a_1\in\mathcal B_\infty$. Then there exist $T,L'$ with $a_{n+T}=a_n+L'$ for all $n\ge1$.*

*Proof.* By Gap B, $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ for all $n\ge1$, so the residue sequence $r_n:=a_n\bmod L$ evolves as $r_{n+1}=f(r_n)$ where $f$ is the cyclic successor of Lemma 6. Since $f$ is a bijection on the finite set $A$, the orbit of $r_1=a_1\bmod L\in A$ (using $a_1\in\mathcal B_\infty$) is a cycle: there is $T\ge1$ with $r_{n+T}=r_n$ for every $n\ge1$. The gap $d_n=a_{n+1}-a_n$ depends only on $r_n$ (it is the distance from $a_n$ to the next element of $\mathcal B_\infty$, determined by $r_n$ and the fixed set $A$), so $d_{n+T}=d_n$; hence the per-period increment $L':=\sum_{i=1}^{T}d_i=a_{n+T}-a_n$ is a positive constant independent of $n$. Therefore $a_{n+T}=a_n+L'$ for all $n\ge1$. $\square$

Both gaps A and B remain open in the whole population; Lemma 7 is conditional.

---

## Promotable lemmas
- **Lemma 1 (linchpin)**: every $a_n$ is divisible by some prime $p\mid a_1$; proved in §1. (Shared foundation; certifiable.)
- **Lemma 2 (gap bound)**: $d_n\le\operatorname{rad}(a_1)$; proved in §1. (Shared foundation; certifiable.)
- **Lemma 4 (hitting-set reformulation)**: $\mathcal B_n=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{\operatorname{rad}(T)\mid m\}$; proved in §1. (Shared foundation; certifiable.)
- **Lemma 6 (cyclic-successor bijection)**: on $A=\mathcal B_\infty\bmod L$, the cyclic successor is a bijection, so every orbit is a cycle with no tail; proved in §5. (Shared endgame; certifiable, conditional on $\mathcal B_\infty$ existing.)
- **Counterexample to Gap F (dead-end record)**: on $a_1=385$, the free-riders $2,3$ have identical type and coexist permanently without replacement; on $a_1=715$, $91$ same-type free-riders coexist transiently. The same-type-replacement lemma is false; do not retry this framing.
