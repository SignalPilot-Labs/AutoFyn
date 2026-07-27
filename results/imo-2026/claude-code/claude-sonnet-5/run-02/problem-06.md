Setup and elementary facts

  Throughout, $(a_n){n\ge1}$ is the given sequence. Since $a{n+1}$ is required to be strictly greater than $a_n$, the sequence is
  strictly increasing.

  Fact 1 (global pairwise non‑coprimality). For all $i\neq j$, $\gcd(a_i,a_j)>1$.

  Proof. By definition, for every $n$ and every $i\le n$, $\gcd(a_{n+1},a_i)>1$. Given any $i<j$, apply this with $n=j-1$:
  $\gcd(a_j,a_i)>1$. Symmetry of $\gcd$ gives the claim for all $i\ne j$. $\blacksquare$

  Notation. Let $P={\text{primes }p: p\le a_1}$, a fixed finite set. For a positive integer $m$, let
  $$\sigma(m):={p\in P: p\mid m}\quad(\text{the "small signature" of }m),\qquad s(m):=\prod_{p\in\sigma(m)}p.$$
  Since the $p\in\sigma(m)$ are distinct primes each dividing $m$, $s(m)\mid m$.

  Fact 2. For every $n\ge1$, $\sigma(a_n)\neq\varnothing$.

  Proof. For $n=1$ this is clear ($a_1>1$ has a prime factor, automatically $\le a_1$). For $n\ge2$, Fact 1 gives $\gcd(a_1,a_n)>1$; any
  prime factor of this gcd divides $a_1$, hence lies in $P$, and divides $a_n$. $\blacksquare$

  Fact 3 (bounded gaps). For all $n\ge1$, $a_{n+1}-a_n\le s(a_1)$.

  Proof. Let $L_0=s(a_1)=\prod_{q\in\sigma(a_1)}q$. If $c$ is any multiple of $L_0$, then for each $i\le n$, Fact 2 gives some
  $q\in\sigma(a_i)\cap\sigma(a_1)$ — wait, more directly: Fact 2 applied via Fact 1 with $a_1$ shows some prime $q\mid a_1$ also divides
  $a_i$; this $q\in\sigma(a_1)$, so $q\mid L_0\mid c$, giving $\gcd(c,a_i)\ge q>1$. So every multiple of $L_0$ that exceeds $a_n$ is an
  admissible candidate for $a_{n+1}$. The least such multiple is at most $a_n+L_0$, so by minimality $a_{n+1}\le a_n+L_0$.
  $\blacksquare$

  Part I: No large prime is ever a necessary witness

  Claim F. For all $i\ne j$, $\sigma(a_i)\cap\sigma(a_j)\ne\varnothing$ — i.e. every pairwise gcd is witnessed by a prime $\le a_1$,
  even though the terms may (and do) carry extra prime factors exceeding $a_1$.

  This is the heart of the problem. We first isolate a clean recognition tool.

  Lemma 1 (term recognition). If $m>a_1$ and $\gcd(m,a_i)>1$ for every term $a_i<m$, then $m$ is itself a term of the sequence.

  Proof. The set ${i: a_i<m}$ contains $1$ (as $m>a_1$) and is finite (since $a_i\to\infty$); let $j$ be its largest element. Since the
  sequence increases, $a_i<m$ for every $i\le j$, so by hypothesis $\gcd(m,a_i)>1$ for all $i\le j$; also $m>a_j$. Thus $m$ is an
  admissible candidate at the step defining $a_{j+1}$, so $a_{j+1}\le m$ by minimality. On the other hand $j$'s maximality gives
  $a_{j+1}\ge m$. Hence $a_{j+1}=m$. $\blacksquare$

  Proof of Claim F. Suppose not, and call a pair of distinct terms ${u,v}$ bad if $\sigma(u)\cap\sigma(v)=\varnothing$. Among all bad
  pairs, choose one, ${a,b}$ with $a<b$, for which $b$ is as small as possible. Minimality of $b$ gives:
  $$(\ast)\qquad \sigma(u)\cap\sigma(v)\ne\varnothing\ \text{ for every pair of distinct terms } u,v<b.$$

  Step 1: a large witness forces room below $a$. By Fact 1, $\gcd(a,b)>1$; since ${a,b}$ is bad, no prime of this gcd lies in $P$, so
  some prime $r>a_1$ divides both $a$ and $b$. As $s(a)$ is composed only of primes $\le a_1$, $\gcd(s(a),r)=1$; since both divide $a$,
  so does their product: $s(a),r\mid a$. Hence
  $$b>a\ge s(a),r> s(a),a_1.$$

  Step 2: build a small competitor. Let $p_0=\min\sigma(a)$ (so $p_0\le a_1$, and $p_0\mid s(a)$, so $s(a)/p_0$ is a positive integer).
  Let $e\ge0$ be the largest integer with $p_0^{,e}\le a_1$ (so $p_0^{,e+1}>a_1$). Set
  $$m:=s(a)\cdot p_0^{,e}.$$
  Multiplying by more copies of the prime $p_0$ (already present in $s(a)$) introduces no new prime factors, so $\Pi(m)=\sigma(a)$
  exactly. Moreover:
  $$m = s(a)p_0^{,e} > s(a)\cdot\frac{a_1}{p_0} ;\ge; a_1 \qquad(\text{using } s(a)/p_0\ge 1),$$
  $$m = s(a)p_0^{,e}\le s(a)\cdot a_1 < a \qquad(\text{by Step 1}).$$
  So $a_1<m<a<b$.

  Step 3: $m$ is a term. Let $a_i$ be any term with $a_i<m$. Then $a_i<m<a<b$, so $a_i$ and $a$ are distinct terms both less than $b$;
  by $(\ast)$ there is a prime $p\in\sigma(a_i)\cap\sigma(a)$. Since $\sigma(a)=\Pi(m)$, $p\mid m$, and $p\mid a_i$, so $\gcd(m,a_i)\ge
  p>1$. This holds for every term below $m$, so Lemma 1 applies: $m$ is a term.

  Step 4: contradiction. Since $\Pi(m)=\sigma(a)$ consists only of primes $\le a_1$, any prime common to $m$ and $b$ would lie in
  $\sigma(a)\cap\sigma(b)=\varnothing$ (badness of ${a,b}$). Hence $\gcd(m,b)=1$. But $m$ and $b$ are distinct terms ($m<a<b$), so Fact
  1 forces $\gcd(m,b)>1$. Contradiction. $\blacksquare$

  Part II: Eventual periodicity

  For $n\ge1$ let $\mathcal F_n:={\sigma(a_1),\dots,\sigma(a_n)}$, a finite set of nonempty subsets of $P$. Since $\mathcal
  F_n\subseteq\mathcal F_{n+1}$ always, and all $\mathcal F_n$ live inside the fixed finite lattice $2^P\setminus{\varnothing}$, the
  sizes $|\mathcal F_n|$ are non-decreasing and bounded, so they stabilize: there is $N$ with $\mathcal F_n=\mathcal F_N=:\mathcal F$
  for all $n\ge N$.

  Define $S:={m\in\mathbb Z_{>a_1}: \sigma(m)\cap S'\ne\varnothing \text{ for every } S'\in\mathcal F}$. For $n\ge N$, since
  ${\sigma(a_1),\dots,\sigma(a_n)}=\mathcal F$, membership of a candidate $c$ in $S$ is exactly the condition "$\gcd(c,a_i)$ has a
  witness $\le a_1$ for every $i\le n$." By Claim F, the true next term $a_{n+1}$ does satisfy this (it's not merely a sufficient
  condition that happens to be satisfiable — the actual minimal valid $c=a_{n+1}$ itself lies in $S$). Since membership in $S$ trivially
  implies the full validity condition $\gcd(c,a_i)>1$ (a shared prime is a shared prime), and $a_{n+1}$ is the least fully-valid
  candidate while also lying in $S$, we get for all $n\ge N$:
  $$a_{n+1}=\min{m\in S: m>a_n}.$$

  Membership in $S$ depends only on $m\bmod P^#$, where $P^#:=\prod_{p\in P}p$: it is a union of residue classes mod $P^#$. It is
  nonempty — every multiple of $s(a_1)$ lies in $S$, since $s(a_1)$ shares a prime with every $\sigma(a_i)$ (Fact 2/3's argument) and
  hence with every $S'\in\mathcal F$. Let $T:=$ the number of residues mod $P^#$ lying in $S$ (so $T\ge1$), and $L:=P^#$. Listing the
  elements of $S$ in increasing order as $x_1<x_2<\cdots$, periodicity of the residue pattern gives $x_{i+T}=x_i+L$ for all $i$.

  For $n> N$, $a_n\in S$ (it was chosen as the least element of $S$ exceeding $a_{n-1}\ge a_N$), so the tail $(a_{N+1},a_{N+2},\dots)$
  is literally a tail of $(x_i)$; hence
  $$a_{n+T}=a_n+L\qquad\text{for all } n\ge N+1.$$

  Part III: Upgrading to periodicity from $n=1$

  We now show: if $a_{n+T}=a_n+L$ holds for all $n\ge m+1$ (any fixed $m\ge1$, positive integers $T,L$), then there exist positive 
  integers $T',L'$ with $a_{n+T'}=a_n+L'$ for all $n\ge m$. Iterating this $N$ times collapses the threshold from $N+1$ down to $1$,
  finishing the proof.

  Multiplicity-correction lemma. Let $c:=\prod{p\text{ prime}: p\mid a_1a_2\cdots a_m,\ p\nmid L}$ (a finite product; possibly empty,
  giving $c=1$). Put $T'=cT,\ L'=cL$. Then:
  (i) $a_{n+T'}=a_n+L'$ for all $n\ge m+1$;
  (ii) every prime factor of every $a_i$ with $i\le m$ divides $L'$.

  Proof. (i) By induction on $k=0,\dots,c$: $a_{n+kT}=a_n+kL$ for $n\ge m+1$ (step: $n+(k-1)T\ge m+1$, so the base relation applies
  Proof of Claim F. Suppose not, and call a pair of distinct terms ${u,v}$ bad if $\sigma(u)\cap\sigma(v)=\varnothing$. Among all bad
  pairs, choose one, ${a,b}$ with $a<b$, for which $b$ is as small as possible. Minimality of $b$ gives:
  $$(\ast)\qquad \sigma(u)\cap\sigma(v)\ne\varnothing\ \text{ for every pair of distinct terms } u,v<b.$$

  Step 1: a large witness forces room below $a$. By Fact 1, $\gcd(a,b)>1$; since ${a,b}$ is bad, no prime of this gcd lies in $P$, so
  some prime $r>a_1$ divides both $a$ and $b$. As $s(a)$ is composed only of primes $\le a_1$, $\gcd(s(a),r)=1$; since both divide $a$,
  so does their product: $s(a),r\mid a$. Hence
  $$b>a\ge s(a),r> s(a),a_1.$$

  Step 2: build a small competitor. Let $p_0=\min\sigma(a)$ (so $p_0\le a_1$, and $p_0\mid s(a)$, so $s(a)/p_0$ is a positive integer).
  Let $e\ge0$ be the largest integer with $p_0^{,e}\le a_1$ (so $p_0^{,e+1}>a_1$). Set
  $$m:=s(a)\cdot p_0^{,e}.$$
  Multiplying by more copies of the prime $p_0$ (already present in $s(a)$) introduces no new prime factors, so $\Pi(m)=\sigma(a)$
  exactly. Moreover:
  $$m = s(a)p_0^{,e} > s(a)\cdot\frac{a_1}{p_0} ;\ge; a_1 \qquad(\text{using } s(a)/p_0\ge 1),$$
  $$m = s(a)p_0^{,e}\le s(a)\cdot a_1 < a \qquad(\text{by Step 1}).$$
  So $a_1<m<a<b$.

  Step 3: $m$ is a term. Let $a_i$ be any term with $a_i<m$. Then $a_i<m<a<b$, so $a_i$ and $a$ are distinct terms both less than $b$;
  by $(\ast)$ there is a prime $p\in\sigma(a_i)\cap\sigma(a)$. Since $\sigma(a)=\Pi(m)$, $p\mid m$, and $p\mid a_i$, so $\gcd(m,a_i)\ge
  p>1$. This holds for every term below $m$, so Lemma 1 applies: $m$ is a term.

  Step 4: contradiction. Since $\Pi(m)=\sigma(a)$ consists only of primes $\le a_1$, any prime common to $m$ and $b$ would lie in
  $\sigma(a)\cap\sigma(b)=\varnothing$ (badness of ${a,b}$). Hence $\gcd(m,b)=1$. But $m$ and $b$ are distinct terms ($m<a<b$), so Fact
  1 forces $\gcd(m,b)>1$. Contradiction. $\blacksquare$

  Part II: Eventual periodicity

  For $n\ge1$ let $\mathcal F_n:={\sigma(a_1),\dots,\sigma(a_n)}$, a finite set of nonempty subsets of $P$. Since $\mathcal
  F_n\subseteq\mathcal F_{n+1}$ always, and all $\mathcal F_n$ live inside the fixed finite lattice $2^P\setminus{\varnothing}$, the
  sizes $|\mathcal F_n|$ are non-decreasing and bounded, so they stabilize: there is $N$ with $\mathcal F_n=\mathcal F_N=:\mathcal F$
  for all $n\ge N$.
  
  Define $S:={m\in\mathbb Z_{>a_1}: \sigma(m)\cap S'\ne\varnothing \text{ for every } S'\in\mathcal F}$. For $n\ge N$, since
  ${\sigma(a_1),\dots,\sigma(a_n)}=\mathcal F$, membership of a candidate $c$ in $S$ is exactly the condition "$\gcd(c,a_i)$ has a
  witness $\le a_1$ for every $i\le n$." By Claim F, the true next term $a_{n+1}$ does satisfy this (it's not merely a sufficient
  condition that happens to be satisfiable — the actual minimal valid $c=a_{n+1}$ itself lies in $S$). Since membership in $S$ trivially
  implies the full validity condition $\gcd(c,a_i)>1$ (a shared prime is a shared prime), and $a_{n+1}$ is the least fully-valid 
  candidate while also lying in $S$, we get for all $n\ge N$:
  $$a_{n+1}=\min{m\in S: m>a_n}.$$

  Membership in $S$ depends only on $m\bmod P^#$, where $P^#:=\prod_{p\in P}p$: it is a union of residue classes mod $P^#$. It is
  nonempty — every multiple of $s(a_1)$ lies in $S$, since $s(a_1)$ shares a prime with every $\sigma(a_i)$ (Fact 2/3's argument) and
  hence with every $S'\in\mathcal F$. Let $T:=$ the number of residues mod $P^#$ lying in $S$ (so $T\ge1$), and $L:=P^#$. Listing the
  elements of $S$ in increasing order as $x_1<x_2<\cdots$, periodicity of the residue pattern gives $x_{i+T}=x_i+L$ for all $i$.

  For $n> N$, $a_n\in S$ (it was chosen as the least element of $S$ exceeding $a_{n-1}\ge a_N$), so the tail $(a_{N+1},a_{N+2},\dots)$
  is literally a tail of $(x_i)$; hence
  $$a_{n+T}=a_n+L\qquad\text{for all } n\ge N+1.$$

  Part III: Upgrading to periodicity from $n=1$

  We now show: if $a_{n+T}=a_n+L$ holds for all $n\ge m+1$ (any fixed $m\ge1$, positive integers $T,L$), then there exist positive
  integers $T',L'$ with $a_{n+T'}=a_n+L'$ for all $n\ge m$. Iterating this $N$ times collapses the threshold from $N+1$ down to $1$,
  finishing the proof.

  Multiplicity-correction lemma. Let $c:=\prod{p\text{ prime}: p\mid a_1a_2\cdots a_m,\ p\nmid L}$ (a finite product; possibly empty,
  giving $c=1$). Put $T'=cT,\ L'=cL$. Then:
  (i) $a_{n+T'}=a_n+L'$ for all $n\ge m+1$;
  (ii) every prime factor of every $a_i$ with $i\le m$ divides $L'$.

  Proof. (i) By induction on $k=0,\dots,c$: $a_{n+kT}=a_n+kL$ for $n\ge m+1$ (step: $n+(k-1)T\ge m+1$, so the base relation applies
  there). Take $k=c$.
  (ii) If $p\mid a_i$ ($i\le m$): either $p\mid L\mid L'$, or $p\nmid L$, in which case $p$ divides the defining product, so $p\mid
  c\mid L'$. $\blacksquare$

  Proposition (push the threshold down by one). With $T',L'$ as above, in fact $a_{m+T'}=a_m+L'$, so $a_{n+T'}=a_n+L'$ holds for all
  $n\ge m$.

  Proof. Suppose not; by trichotomy consider the two possible strict cases.

  Case $a_{m+T'}>a_m+L'$. Let $x=a_{m+T'}-L'>a_m$. For each $i\le m$: since $i<m+T'$, Fact 1 gives $\gcd(a_i,a_{m+T'})>1$; any prime $p$
  dividing this gcd divides $a_i$ ($i\le m$), so by (ii) $p\mid L'$, hence $p\mid a_{m+T'}-L'=x$. Thus $\gcd(x,a_i)>1$ for all $i\le
  m$, and $x>a_m$: so $x$ is admissible at the step defining $a_{m+1}$, giving $a_{m+1}\le x=a_{m+T'}-L'$, i.e.
  $$a_{m+1}+L'\le a_{m+T'}.\tag{I}$$
  But applying the known relation at $n=m+1$: $a_{(m+1)+T'}=a_{m+1}+L'$, and since $(m+1)+T'=(m+T')+1$ and the sequence is strictly
  increasing,
  $$a_{m+1}+L'=a_{(m+1)+T'}>a_{m+T'}.\tag{II}$$
  (I) and (II) contradict each other.

  *Case $a_{m+T'}<a_m+L'$.* Let $y=a_m+L'>a_{m+T'}$. For $r\le m+T'$ with $r\ne m$: Fact 1 gives $\gcd(a_m,a_r)>1$; any prime $p$
  dividing this divides $a_m$, so by (ii) $p\mid L'$, hence $p\mid a_m+L'=y$; so $\gcd(y,a_r)>1$. For $r=m$: $\gcd(y,a_m)=\gcd(L',a_m)$,
  and any prime $q\mid a_m$ divides $L'$ by (ii), so $\gcd(y,a_m)\ge q>1$. So $y$ is admissible at the step defining $a_{m+T'+1}$,
  giving $a_{m+T'+1}\le y=a_m+L'$. Since $m+T'+1=(m+1)+T'$ and the known relation gives $a_{(m+1)+T'}=a_{m+1}+L'$, this reads
  $a_{m+1}+L'\le a_m+L'$, i.e. $a_{m+1}\le a_m$ — contradicting strict monotonicity. $\blacksquare$

  Iterating the Proposition $N$ times (from threshold $N+1$ down to threshold $1$) produces positive integers $T_\star,L_\star$ with
  $$a_{n+T_\star}=a_n+L_\star\qquad\text{for every positive integer }n,$$
  which is exactly the desired conclusion. $\blacksquare$

  Summary of the logical structure

  1. Fact 1: all pairs of terms are non-coprime — immediate from the definition.
  2. Facts 2–3: every term shares a prime factor $\le a_1$ with $a_1$; consequently gaps $a_{n+1}-a_n$ are bounded by $s(a_1)$.
  3. Claim F (Part I): despite terms carrying arbitrarily large "bystander" prime factors, every pairwise gcd is always witnessed by a
  prime $\le a_1$. Proved by taking a minimal counterexample ${a,b}$ and constructing, from $a$'s small part and the size gap forced by
  $b$'s reliance on a large prime, a genuinely new, smaller term $m$ that is simultaneously forced (by minimality of $b$) to intersect
  every earlier term's signature, yet forced (by badness of ${a,b}$) to be fully coprime to $b$ — contradicting Fact 1 applied to the
  two terms $m,b$.
  4. Part II: Claim F reduces the recursive rule to a finite-state process (tracking only which subsets of the primes $\le a_1$ have
  appeared), which stabilizes and yields exact periodicity $a_{n+T}=a_n+L$ from some finite point on.
  5. Part III: a two-sided minimality-squeeze (using a finite correction factor to make $L$ absorb the prime factors of finitely many
  early terms) pushes this periodicity back one index at a time, all the way to $n=1$.

  Together these prove the existence of positive integers $T,L$ with $a_{n+T}=a_n+L$ for every positive integer $n$. $\blacksquare$

✻ Brewed for 1h 51m 2s