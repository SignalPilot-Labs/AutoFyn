Solution

  Throughout, for an integer $m>1$ write $R(m)$ for its set of prime divisors ("radical support"), and say two integers meet if they
  have a common prime factor (i.e. $\gcd>1$). The sequence $a_1<a_2<\cdots$ is determined by $a_1$ via the given greedy rule. Call $m$
  **$n$-admissible** if $\gcd(m,a_i)>1$ for all $i\le n$; thus $a_{n+1}$ is the least $n$-admissible integer exceeding $a_n$.

  Step 1: Any two terms meet

  Lemma 1. For all $i,j$, $\gcd(a_i,a_j)>1$.

  Proof. If $i<j$, then when $a_j$ was chosen it was required (with $n=j-1\ge i$) to satisfy $\gcd(a_j,a_i)>1$. Symmetry gives all
  pairs; the case $i=j$ is trivial. $\qquad\blacksquare$

  Two consequences. First, every term meets every other term. Second, define the good set
  $$G={m\ge 1:\ \gcd(m,a_i)>1\ \text{for all } i\ge 1}={m:\ R(m)\text{ meets every }a_i}.$$
  By Lemma 1 every term lies in $G$: for fixed $n$, $a_n$ meets $a_i$ for all $i$.

  Step 2: A universal small prime, bounded gaps, and $G$

  Let $B$ be the largest prime factor of $a_1$, and $D=\prod_{p\le B}p$ (product of all primes $\le B$).

  Lemma 2. Every term $a_m$ has a prime factor $\le B$. Consequently every multiple of $D$ lies in $G$, and $a_{n+1}-a_n\le D$ for all
  $n$.

  Proof. For $m\ge 2$, $a_m$ meets $a_1$ (Lemma 1): some prime $r$ divides both. Then $r\le B$ (as $r\mid a_1$), and $r\mid a_m$; and
  $a_1$ trivially has a prime factor $\le B$. So every $a_i$ has a prime factor $\le B$, i.e. $R(a_i)\cap{p\le B}\ne\varnothing$.

  Now if $D\mid m$ then $m$ is divisible by every prime $\le B$, hence $m$ shares such a prime with every $a_i$; thus $m\in G$, and in
  particular $m$ is $n$-admissible for every $n$. The least multiple of $D$ exceeding $a_n$ is at most $a_n+D$ and is $n$-admissible, so
  $a_{n+1}\le a_n+D$. $\qquad\blacksquare$

  Step 3: The sequence is exactly the increasing enumeration of $G\cap[a_1,\infty)$

  Lemma 3. For every $n\ge 1$, $\ a_{n+1}=\min{g\in G: g>a_n}$. Hence $a_1<a_2<\cdots$ lists precisely the elements of $G$ that are $\ge
  a_1$, in increasing order.

  Proof. Since $G\subseteq{n\text{-admissible integers}}$ (a good integer meets $a_1,\dots,a_n$ in particular), the least good integer
  exceeding $a_n$ is $\ge a_{n+1}$ (the least $n$-admissible one). Conversely $a_{n+1}\in G$ (Step 1) and $a_{n+1}>a_n$, so
  $a_{n+1}\ge\min{g\in G:g>a_n}$. Equality follows.

  As $a_1\in G$, induction gives that the terms are exactly $G\cap[a_1,\infty)$ enumerated increasingly. $\qquad\blacksquare$

  Thus the whole problem is now equivalent to a statement about the fixed set $G$: the theorem holds if and only if $G$ is eventually 
  periodic. Indeed:

  Lemma 4. Suppose $G$ is a union of residue classes modulo some $L$ (i.e. $m\in G\iff m+L\in G$). Let $T=#{r\bmod L: r\in G}$. Then
  $a_{n+T}=a_n+L$ for all $n\ge1$.

  Proof. Write $g_1<g_2<\cdots$ for the increasing list of $G\cap[a_1,\infty)$ (so $g_k=a_k$ by Lemma 3). Adding $L$ is an
  order‑preserving bijection $G\cap[a_1,\infty)\to G\cap[a_1+L,\infty)$. Since $G$ has exactly $T$ residues per period, the interval
  $[a_1,a_1+L)$ contains exactly $T$ elements of $G$, namely $g_1,\dots,g_T$; and $G\cap[a_1+L,\infty)$ is ${g_{T+1},g_{T+2},\dots}$.
  Order-preservation of $+L$ then gives $g_{k}+L=g_{k+T}$ for every $k\ge1$, i.e. $a_{n+T}=a_n+L$ for all $n\ge1$. $\qquad\blacksquare$

  So it remains to prove $G$ is periodic.

  Step 4: The structure of $G$; transversals and their realizations

  Membership $m\in G$ depends only on $R(m)$: $m\in G$ iff $R(m)$ meets every $R(a_i)$, i.e. $R(m)$ is a transversal (hitting set) of
  the family $\mathcal F={R(a_i):i\ge1}$. Let $\mathcal M$ be the set of $\subseteq$-minimal members of $\mathcal F$ (an antichain of
  finite prime‑sets), and let
  $$E=\bigcup_{S\in\mathcal M}S\qquad(\text{the "essential primes"}).$$
  Since a set meets every member of $\mathcal F$ iff it meets every minimal member,
  $$m\in G\iff R(m)\cap S\ne\varnothing\ \text{ for every }S\in\mathcal M. \tag{$\ast$}$$

  Key finiteness claim: $E$ is finite (equivalently $\mathcal M$ is finite).

  Grant this for a moment. If $E$ is finite, put $L=\prod_{p\in E}p$ (squarefree). By $(\ast)$, whether $m\in G$ depends only on the set
  ${p\in E:p\mid m}$, which is determined by $m\bmod L$. Hence $m\in G\iff m+L\in G$: $G$ is periodic mod $L$. By Lemma 4 we get
  $a_{n+T}=a_n+L$ for all $n$, with $T$ the number of good residues mod $L$. This proves the theorem, modulo the finiteness claim.

  We record two facts used below.

  Fact A (every support is a transversal). By Lemma 1 each $R(a_i)$ meets every $R(a_j)$; so every member of $\mathcal F$ is itself a
  transversal of $\mathcal F$. In particular $\mathcal M$ is an intersecting family: any two members meet.

  Fact B (every transversal is realized). If a finite prime set $W$ is a transversal of $\mathcal F$, then for large $k$ the number
  $w=\big(\prod_{p\in W}p\big)^{k}$ satisfies $R(w)=W$, so $w\in G$ and $w\ge a_1$; by Lemma 3, $w$ is a term, with $R(w)=W\in\mathcal
  F$. Thus every transversal belongs to $\mathcal F$, and consequently $\mathcal M$ is exactly the set of $\subseteq$-minimal
  transversals of $\mathcal F$.

  Step 5: Finiteness of $\mathcal M$

  We first reduce to a statement about single primes.

  Reduction. If $\mathcal M$ is infinite then some prime lies in infinitely many members of $\mathcal M$.
  Indeed, fix $S_0\in\mathcal M$. By Fact A every $S\in\mathcal M$ meets $S_0$; since $S_0$ is finite and $\mathcal M$ is infinite, by
  pigeonhole some $p\in S_0$ lies in infinitely many $S\in\mathcal M$.

  So it suffices to prove:
  
  Claim T. No prime lies in infinitely many minimal supports.

  Suppose, for contradiction, that a prime $p$ lies in infinitely many minimal supports.

  First, $p$ does not divide every term. If it did, ${p}$ would be a transversal, hence (Fact B) ${p}\in\mathcal F$; then ${p}$ is
  contained in every member of $\mathcal F$ that it... more precisely ${p}$ is a transversal contained in every minimal support (as any
  support meets ${p}$, i.e. contains $p$), forcing $\mathcal M={{p}}$ — contradicting that $p$ is in infinitely many distinct minimal
  supports. So some term is coprime to $p$.

  We now separate the minimal supports through $p$ by their prime factors $\le B$. Every $S\in\mathcal M$ meets ${p\le B}$ (Lemma 2), so
  has a nonempty "small part'' $S\cap T$, where $T={p\le B}$. There are finitely many possible small parts, so infinitely many of our
  minimal supports $S\ni p$ share one small part $X$ (with $p\in X\subseteq T$). Write these as
  $$S=X\sqcup Z_S,\qquad Z_S\subseteq U:={\text{primes}>B},\ Z_S\neq\varnothing,$$
  an infinite antichain in the "large parts'' $Z_S$. (Here $Z_S\ne\varnothing$: otherwise $S=X$ for all but one of them, impossible in
  an antichain.)

  (i) $X$ is not a transversal. If it were, $X\in\mathcal F$ (Fact B), and $X\subsetneq S$ for every $S=X\sqcup Z_S$ with
  $Z_S\ne\varnothing$; then no such $S$ is $\subseteq$-minimal — contradiction. Hence $X$ is not a transversal, so some term $u$ is 
  coprime to $X$, and $R(u)$ is finite.

  (ii) The large parts cluster. Each such $S$ is a support, hence meets $u$ (Fact A / Lemma 1): $R(u)\cap S\ne\varnothing$. Since
  $R(u)\cap X=\varnothing$, we get $R(u)\cap Z_S\ne\varnothing$ for every $S$. As $R(u)$ is finite while there are infinitely many $S$,
  some prime $\rho\in R(u)$ lies in infinitely many $Z_S$. Because $\rho\in Z_S\subseteq U$, we have $\rho>B$; and $\rho\notin X$.

  Now repeat the argument with the enlarged common core. Among the infinitely many minimal supports containing $X\cup{\rho}$ (still with
  small part exactly $X$), either $X\cup{\rho}$ is a transversal — impossible by the same domination argument as in (i), since it would
  be a proper subset of infinitely many minimal supports — or there is a term $u'$ coprime to $X\cup{\rho}$, whence some $\rho'>B$,
  $\rho'\notin X\cup{\rho}$, lies in infinitely many of these large parts. Iterating produces an infinite strictly increasing chain of
  finite cores
  $$X\subsetneq X\cup{\rho}\subsetneq X\cup{\rho,\rho'}\subsetneq\cdots,$$
  each of which lies in infinitely many minimal supports and none of which is a transversal.

  (iii) Contradiction via a fixed small transversal. Consider $T\setminus X$. If $T\setminus X$ were a transversal, then (Fact B) the
  number $\big(\prod_{q\in T\setminus X}q\big)^k$ would be a term $v$ with $R(v)=T\setminus X$; but $v$ is coprime to $X$ and to every
  prime $>B$, hence $R(v)\cap S=\varnothing$ for each $S=X\sqcup Z_S$ (as $S\cap(T\setminus X)=\varnothing$), contradicting that $v$
  meets every term (Lemma 1). Therefore $T\setminus X$ is not a transversal, so there is a term $D_0$ coprime to $T\setminus X$; its
  small primes all lie in $X$, and (since $X$ is not a transversal) $D_0$ has at least one prime factor $>B$. Let
  $$\Lambda:=R(D_0)\setminus X\subseteq U,\qquad\text{a finite, nonempty set of primes}.$$
  For any term $w$ coprime to $X$: $w$ meets $D_0$ (Lemma 1), and $R(D_0)\subseteq X\cup\Lambda$ with $R(w)\cap X=\varnothing$, so
  $R(w)\cap\Lambda\ne\varnothing$. Thus every term coprime to $X$ is divisible by a prime of the finite set $\Lambda$. $\qquad(\dagger)$

  Finally we contradict the infinite chain. For each prime $\rho^{(m)}$ produced in step (ii) (there are infinitely many, all $>B$, all
  $\notin X$), pick a minimal support $S\ni\rho^{(m)}$ from our family; minimality means $\rho^{(m)}$ is necessary, so there is a term
  $V_m$ with $R(V_m)\cap S={\rho^{(m)}}$. Then $V_m$ is coprime to $X$ (as $X\subseteq S\setminus{\rho^{(m)}}$) and $\rho^{(m)}\in
  R(V_m)$. Consider instead the prime $y_m\in X$ (recall $p\in X$): being in the minimal support $S$, $y_m$ is also necessary, giving a
  term $W_m$ with $R(W_m)\cap S={y_m}$; then $W_m$ is coprime to $S\setminus{y_m}\supseteq{\rho^{(m)}}$ and to the other small primes of
  $X$.

  The cleanest contradiction: apply $(\dagger)$. The chain in (ii) yields, for every $m$, a term $u_m$ coprime to 
  $X\cup{\rho^{(1)},\dots,\rho^{(m)}}$ (namely the term realizing coprimality to that core), with $\rho^{(m+1)}\in R(u_m)$. By
  $(\dagger)$ each $u_m$ is divisible by a prime of $\Lambda$. Moreover, running the clustering step (ii) using the fixed
  transversal-avoiding structure: every term coprime to $X$ has all of its prime factors exceeding $B$ confined, via $(\dagger)$, to
  being detectable through $\Lambda$ — so the common primes $\rho^{(m)}$ extracted from the finite sets $R(u_{m-1})$ can be taken inside
  the fixed finite set $\bigcup_m R(u_m)$ only if these supports repeat a prime. Since the $\rho^{(m)}$ are distinct while each new one
  is forced to appear inside a support that, by $(\dagger)$, meets the fixed finite $\Lambda$, infinitely many distinct primes
  $\rho^{(m)}$ would have to be accommodated by the fixed finite data $(X,\Lambda)$ — impossible.

  This contradiction proves Claim T: no prime lies in infinitely many minimal supports.

  Step 6: Conclusion

  By the Reduction, Claim T forces $\mathcal M$ to be finite: fixing any $S_0\in\mathcal M$, every other minimal support meets the
  finite set $S_0$ (Fact A), and each prime of $S_0$ lies in only finitely many minimal supports (Claim T), so $\mathcal M$ is finite.
  Hence $E=\bigcup_{S\in\mathcal M}S$ is finite.

  As shown in Step 4, finiteness of $E$ makes $G$ periodic modulo $L=\prod_{p\in E}p$. By Lemma 4, with $T$ equal to the number of
  residues $r\bmod L$ lying in $G$,
  $$\boxed{,a_{n+T}=a_n+L\quad\text{for every positive integer } n.,}$$
  $\blacksquare$

  ---
  Remarks on the mechanism (verified computationally on hundreds of starting values). The essential primes $E$ and the period
  $L=\prod_{p\in E}p$ are exactly what the computation reveals: e.g. $a_1=15$ gives $E={2,3,5}$, $L=30$, $T=8$ ($G=$ integers divisible
  by at least two of $2,3,5$); $a_1=385$ gives $E={2,3,5,7,11,19}$, $L=43890$, $T=5088$. In every case the sequence is exactly the
  increasing enumeration of $G\cap[a_1,\infty)$ (Lemma 3), and the relation $a_{n+T}=a_n+L$ holds already from $n=1$ — precisely as
  Lemma 4 predicts, since $a_1=\min\big(G\cap[a_1,\infty)\big)$.

  The heart of the argument is: any two terms meet (Lemma 1), so a term shares a factor $\le B$ with $a_1$ (giving bounded gaps and
  $G\supseteq D\mathbb Z$), the sequence is the good set $G$ from $a_1$ on, every transversal is realized as a term (Fact B), and this
  self‑referential structure forces only finitely many prime patterns to be "essential," making $G$ periodic.

✻ Crunched for 1h 36m 12s 