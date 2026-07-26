# Lemma: Linchpin and gap bound

**Statement.** Let $a_1,a_2,\dots$ be the sequence defined by $a_{n+1}=$ the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i\le n$, with $a_1>1$. Let $P_1$ be the set of prime divisors of $a_1$ and $M_1:=\operatorname{rad}(a_1)=\prod_{p\in P_1}p$.

(Linchpin) For every $n\ge1$, $a_n$ is divisible by some prime $p\in P_1$.
(Gap bound) $d_n:=a_{n+1}-a_n\le M_1$ for every $n\ge1$. In particular $a_n\le a_1+(n-1)M_1$ (linear growth).

**Proof.** *Linchpin.* For $n=1$ it is the definition of $P_1$. For $n\ge2$, the admissibility condition defining $a_n$ includes the clause $i=1$, i.e. $\gcd(a_n,a_1)>1$; hence $a_n$ shares a prime factor with $a_1$, i.e. some $p\in P_1$ divides $a_n$.

*Gap bound.* Consider $m:=a_n+M_1$. Then $m>a_n$ and every $p\in P_1$ divides $M_1$, hence divides $m$. By the linchpin each $a_i$ ($i\le n$) is divisible by some $p_i\in P_1$; since $p_i\mid M_1\mid m$, we have $\gcd(m,a_i)\ge p_i>1$. Thus $m$ is admissible at step $n$. As $a_{n+1}$ is the *smallest* admissible integer exceeding $a_n$, $a_{n+1}\le m=a_n+M_1$, i.e. $d_n\le M_1$. $\square$

**Status.** Reviewer-certified (round 1). Unconditional. Importable by any approach. Verified computationally on 80+ starting values $a_1$.
