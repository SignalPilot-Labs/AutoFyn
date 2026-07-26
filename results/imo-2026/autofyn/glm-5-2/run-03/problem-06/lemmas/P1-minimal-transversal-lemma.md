# Lemma: $P_1$ is a minimal transversal for $|P_1|=2$ NON-LOCK

**Statement.** In the **$|P_1|=2$ NON-LOCK** regime ($a_1=p^kq$, $p<q$ odd primes, no prime-power term reached), the two-element set $P_1=\{p,q\}$ is itself a **minimal transversal** of $\mathcal F_\infty=\{S(a_n):n\ge1\}$; i.e. $P_1\in\operatorname{MT}(\mathcal F_\infty)$. In particular both $p$ and $q$ are **governing primes** ($P_1\subseteq G$).

**Sub-result (load-bearing, self-contained).** *If a prime $r\in P_1$ divides $a_n$ for every $n\ge1$, then the sequence LOCKs (a prime-power term is reached, hence `lock-lemma` applies).* Equivalently (contrapositive): in a NON-LOCK sequence, no single $P_1$-prime divides every term.

**Proof of the sub-result.** Suppose $r\mid a_n$ for all $n\ge1$. Then for every $n$, both $a_n$ and $a_{n+1}$ are positive multiples of $r$ with $a_{n+1}>a_n$, so $a_{n+1}-a_n$ is a positive multiple of $r$, hence $a_{n+1}\ge a_n+r$. Conversely, $a_n+r$ is a multiple of $r$ (since $r\mid a_n$), and by assumption $r\mid a_i$ for every $i\le n$, so $\gcd(a_n+r,a_i)\ge r>1$ for every $i\le n$; $a_n+r$ is admissible, and the greedy rule gives $a_{n+1}\le a_n+r$. Hence $a_{n+1}=a_n+r$ for every $n\ge1$, i.e. $a_n=a_1+(n-1)r$. Write $a_1=r\cdot b$ with $b=a_1/r>1$. Choose $j$ with $r^{j-1}\ge b$ (possible since $r^{j-1}\to\infty$); set $n=r^{j-1}-b+1\ge1$. Then $a_n=r\cdot r^{j-1}=r^j$, a prime power. By `lock-lemma`, the sequence LOCKs. $\square$

**Proof of the lemma.** *Transversal:* by `linchpin-and-gap-bound`, every $a_n$ has a $P_1$-factor, so $S(a_n)\cap P_1\ne\varnothing$ for every $n$; $P_1$ meets every member of $\mathcal F_\infty$. *Minimality:* by the sub-result, in a NON-LOCK sequence neither $\{p\}$ nor $\{q\}$ is a transversal (each would force LOCK). So no proper subset of $P_1$ is a transversal; $P_1$ is minimal. $\square$

**Depends on.** `linchpin-and-gap-bound` (linchpin: $P_1$ is a transversal) + `lock-lemma` (the sub-result uses it for the final LOCK step).

**Status.** Reviewer-certified (round 3). Unconditional (within the $|P_1|=2$ NON-LOCK regime). Verified computationally for $a_1\in\{15,35,65,77,91,143,175,847\}$: in every NON-LOCK case, neither $p$ nor $q$ divides all of the first 200 terms. The sub-result "$r\mid a_n\,\forall n\Rightarrow$ LOCK" is the contrapositive engine behind several NON-LOCK arguments and is importable on its own.
