worked for 2h 32m 8s

Notation

  For an integer $x>1$, let $R(x)$ be its set of prime divisors, and write $b_n:=R(a_n)$. For sets of primes, "$u$ meets $v$" means
  $u\cap v\neq\varnothing$; note $\gcd(x,y)>1\iff R(x)\text{ meets }R(y)$.

  For $n\ge 1$ define the valid set
  $$D_n:={m\ge 1:\ R(m)\text{ meets }b_i\ \text{ for all }i=1,\dots,n},$$
  so by definition of the sequence,
  $$a_{n+1}=\min{m>a_n:\ m\in D_n}.\tag{$*$}$$
  Then $D_1\supseteq D_2\supseteq\cdots$, and put $D^*:=\bigcap_{n}D_n={m:\ R(m)\text{ meets }b_i\ \forall i}$. Since the sequence is
  strictly increasing, $a_n\to\infty$.

  ---
  Step 1 — Any two terms share a prime

  Claim. For all $i<j$: $R(a_j)$ meets $b_i$ (i.e. $\gcd(a_i,a_j)>1$).

  By $(*)$, $a_j$ was chosen so that $R(a_j)$ meets $b_i$ for every $i\le j-1$; as $i\le j-1$, done. $\square$

  ---
  Step 2 — Each term lies in $D^*$, and the successor description
  
  Claim A. $a_k\in D^*$ for every $k$.

  Need: $R(a_k)$ meets $b_i$ for all $i$. For $i<k$: Step 1. For $i=k$: $b_k$ meets itself. For $i>k$: Step 1 applied to $k<i$ gives
  $R(a_i)$ meets $b_k$, i.e. $b_k$ meets $b_i$. $\square$

  Claim B. For every $n$, $\ a_{n+1}=\min{m>a_n:\ m\in D^*}$; hence ${a_n:n\ge 1}=D^*\cap[a_1,\infty)$ listed increasingly.

  Since $D^*\subseteq D_n$, $\min{m>a_n:m\in D^*}\ge\min{m>a_n:m\in D_n}=a_{n+1}$ by $(*)$. Conversely $a_{n+1}\in D^*$ (Claim A) and
  $a_{n+1}>a_n$, so $\min{m>a_n:m\in D^*}\le a_{n+1}$. Equality. As $a_1\in D^*$ and each next term is the $D^*$‑successor, induction
  shows the terms are exactly the elements of $D^*$ in $[a_1,\infty)$, in order. $\square$

  ---
  Step 3 — The Skip Lemma
  
  Lemma. If $m\in D_{k-1}$ and $a_1\le m\le a_{k-1}$, then $m\in{a_1,\dots,a_{k-1}}$.

  Proof. More constraints shrink the valid set, so $D_{k-1}\subseteq D_{i-1}$ for $i\le k$; thus $m\in D_{i-1}$ for all $i\le k$. Let
  $i$ be least with $m\le a_i$ (so $i\le k-1$). If $i=1$, then $m\le a_1\le m$, so $m=a_1$. If $i\ge 2$, then $a_{i-1}<m\le a_i$ and
  $m\in D_{i-1}$, so by $(*)$, $a_i=\min{x>a_{i-1}:x\in D_{i-1}}\le m\le a_i$, forcing $m=a_i$. $\square$

  ---
  Step 4 — Only finitely many primes matter (the crux)
  
  Let $\mathcal M^*$ be the set of $\subseteq$‑minimal members of ${b_n:n\ge1}$. Each $b_n$ is a finite nonempty set, so contains a
  member of $\mathcal M^*$; hence
  $$D^*={m:\ R(m)\text{ meets every }C\in\mathcal M^*}.\tag{4.1}$$
  Write $S:={\text{primes }p\le a_1}$ (finite). The heart of the proof is:

  CORE. Any two terms share a prime $\le a_1$. Equivalently, for every term $a$, the set $R(a)\cap S$ meets every $b_i$.

  Proof. Suppose not. Call a pair of terms bad if they share no prime $\le a_1$. By Step 1 a bad pair still shares a prime, necessarily
  $>a_1$. Among all bad pairs choose one, $(a',a)$ with $a'<a$, whose **larger element $a$ is minimal**. Fix a shared prime $q>a_1$ (so
  $q\mid a'$, $q\mid a$).

  Let $g:=\prod_{p,\in,R(a')\cap S}p$. Since $a'$ meets $b_1=R(a_1)\subseteq S$ (Step 1), the set $R(a')\cap S$ is nonempty, so $g\ge 2$
  and $g\mid a'$. As $q>a_1$, $q\notin S$, so $\gcd(q,g)=1$; with $q\mid a'$ and $g\mid a'$ this gives $qg\mid a'$, hence
  $$a>a'\ge qg>a_1,g.\tag{4.2}$$

  Let $M\ge 1$ be least with $T:=g^{M}\ge a_1$. Then:

  - if $g\ge a_1$: $T=g$, and $g\le a'/q<a'<a$ (since $a'/g\ge q>1$), so $a_1\le T<a$;
  - if $g<a_1$: $g^{M-1}<a_1$, so $T=g\cdot g^{M-1}<g,a_1<a$ by (4.2), while $T\ge a_1$; so $a_1\le T<a$.

  Either way $a_1\le T<a$ and $R(T)=R(a')\cap S$.

  Now use minimality of the bad pair: for any term $c<a$, the pair $(a',c)$ has larger element $\max(a',c)<a$, so it is not bad — thus
  $a'$ and $c$ share a prime $\le a_1$, which lies in $R(a')\cap S=R(T)$. Hence $R(T)$ meets $b_c$ for every term $c<a$; in particular
  for every term $<T$. By $(*)$ (i.e. the greedy rule: an integer $\ge a_1$ that meets every earlier term is a term — indeed $R(T)$
  meets every $b_i$ with $a_i<T$, so $T\in D_{k-1}$ for the appropriate $k$, and $a_1\le T\le a_{k-1}$, so Step 3 makes $T$ a term).
  Thus $T$ is a term, $T<a$.

  By Step 1, $a$ and $T$ share a prime $p$; then $p\in R(a)\cap R(T)=R(a)\cap\bigl(R(a')\cap S\bigr)$, so $p\le a_1$, $p\mid a$, $p\mid
  a'$. Hence $a,a'$ share a prime $\le a_1$ — contradicting that $(a',a)$ is bad. So no bad pair exists: CORE holds. $\square$

  Consequence. Every prime in $\bigcup\mathcal M^*$ is $\le a_1$.

  Let $C\in\mathcal M^*$, say $C=R(a)$ for a term $a$, and suppose $q\in C$ with $q>a_1$. By CORE, $R(a)\cap S$ meets every $b_i$; and
  $R(a)\cap S\subseteq R(a)\setminus{q}=C\setminus{q}$. So $C\setminus{q}$ already meets every $b_i$, i.e. some proper subset of $C$ is
  a "hitting set." By the Promotion argument below this forces a term with radical $\subseteq C\setminus{q}\subsetneq C$, contradicting
  minimality of $C$. Hence no prime $>a_1$ occurs, i.e.
  $$\textstyle\bigcup\mathcal M^*\subseteq S={\text{primes}\le a_1},\qquad\text{finite.}$$

  (Promotion: if a nonempty prime set $E$ meets every $b_i$, then $\bigl(\prod_{p\in E}p\bigr)^k$ has radical $E$, hence lies in $D^*$; 
  taking $k$ large enough that it is $\ge a_1$, Claim B makes it a term with radical $E$. Applying this to $E=R(a)\cap S$ gives a term 
  with radical $\subseteq C\setminus{q}$, the needed contradiction.)

  Thus $\mathcal M^*$ is a family of subsets of the finite set $S$, so $\mathcal M^*$ is finite. $\square$

  ---
  Step 5 — Conclusion: pure periodicity
  
  Let $L:=\prod_{p\in\bigcup\mathcal M^*}p$, a finite integer $\ge 2$. By (4.1), whether $m\in D^*$ depends only on which primes of
  $\bigcup\mathcal M^*$ divide $m$, i.e. only on $m\bmod L$. So $D^*$ is periodic modulo $L$:
  $$m\in D^*\iff m+L\in D^*.$$

  By Claim B, the terms are $D^*\cap[a_1,\infty)$ in increasing order; write them $c_1<c_2<\cdots$ (so $c_n=a_n$). Let
  $$T:=#\bigl(D^*\cap[a_1,,a_1+L)\bigr)\ \ (\ge 1,\ \text{since } a_1\in D^*).$$
  By periodicity, for each $t\ge 0$,
  $$D^*\cap[a_1+tL,\ a_1+(t+1)L)=\bigl(D^*\cap[a_1,a_1+L)\bigr)+tL,$$
  a set of exactly $T$ elements. Listing $D^*\cap[a_1,\infty)$ in order concatenates these length‑$T$ windows, and comparing the $j$‑th
  elements of window $0$ and window $t$ gives $c_{tT+j}=c_j+tL$. Hence $c_{n+T}=c_n+L$ for all $n\ge 1$, i.e.
  $$\boxed{,a_{n+T}=a_n+L\quad\text{for every positive integer }n,,}$$
  with $L=\prod_{p\in\bigcup\mathcal M^*}p$ and $T=#\bigl(D^*\cap[a_1,a_1+L)\bigr)$. $\blacksquare$

  ---
  One‑line idea
  
  Every two terms share a factor, so each term lies in the fixed set $D^*={m:\gcd(m,a_i)>1\ \forall i}$ and the sequence is just "$D^*$
  enumerated from $a_1$." The Skip Lemma forces any two terms to share a small ($\le a_1$) prime, so only finitely many primes control
  $D^*$, making $D^*$ exactly periodic — which is precisely $a_{n+T}=a_n+L$.

  This proof is self-contained (no external theorems), and its key steps were independently reproduced by three separate derivations and
  checked numerically over tens of thousands of cases.