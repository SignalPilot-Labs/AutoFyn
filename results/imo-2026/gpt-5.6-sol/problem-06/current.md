## Status
solved

## Approaches tried
- Direct recursive classification and small-prime-mask compression (`small-prime-mask-compression`) — worked. A minimal-counterexample argument proves that the classification depends only on divisibility by primes at most $a_1$, giving exact primorial periodicity.
- Small-witness kernel (`small-witness-kernel`) — worked. Compression plus extremal descent proves every pair of good integers shares a prime at most $a_1$, from which mask invariance and periodicity follow.

## Current best
Both independently written candidates give complete proofs. With $k=a_1$ and $L$ the product of all primes at most $k$, membership in the recursively defined good set is invariant under translation by $L$. If $T$ counts the good integers in $[k,k+L-1]$, translation shifts the increasing enumeration by exactly $T$ indices.

## Full proof
Put $k=a_1$; the hypothesis gives $k>1$. Recursively classify every integer $m\ge k$ as follows: $m$ is *good* if there is no good integer $r$ with $k\le r<m$ and $\gcd(r,m)=1$, and it is *bad* otherwise. This is a well-defined strong-induction recursion. Thus a bad integer has a smaller good integer coprime to it, whereas a good integer has no such witness. In particular, any two good integers have gcd greater than $1$.

There are infinitely many good integers: every positive multiple of $k$ that is at least $k$ is good. Indeed, if such a multiple were bad, it would have a smaller good witness coprime to it and hence coprime to the good integer $k$, contradicting pairwise non-coprimality of good integers.

We claim that the given sequence is precisely the increasing enumeration $g_1<g_2<\cdots$ of the good integers. We have $g_1=k=a_1$. If $a_i=g_i$ for $1\le i\le n$, then $g_{n+1}$ has gcd greater than $1$ with every $g_i$, so it is eligible for the greedy rule. Every integer $m$ strictly between $g_n$ and $g_{n+1}$ is bad, and therefore has a good coprime witness below it. Since no good integer lies between $g_n$ and $g_{n+1}$, that witness is among $g_1,\dots,g_n$, so $m$ is ineligible. Hence $a_{n+1}=g_{n+1}$, proving the claim by induction.

Call a prime *small* if it is at most $k$. Two integers at least $k$ are *similar* if they have exactly the same small prime divisors. We first prove a compression lemma: if $b\ge k$ has a small prime divisor, there is an $x\in[k,b]$ similar to $b$ all of whose prime divisors are small.

If $b$ has no prime divisor greater than $k$, take $x=b$. Otherwise choose a prime $q>k$ dividing $b$. Let $A$ be the product of all distinct small prime divisors of $b$, choose a prime $p\mid A$, and let $e\ge0$ be least such that $x=p^eA\ge k$. Then $x$ has exactly the small prime divisors of $b$. If $e=0$, then $x=A\mid b$. If $e>0$, minimality gives $p^{e-1}A<k$, and therefore
\[
x=p^eA<pk\le Ak<Aq\le b.
\]
Here $p\le A$, $k<q$, and $Aq\mid b$. The compression lemma follows.

We next prove, by the extremal principle, that every two good integers share a small prime. Suppose not, and choose a violating pair $b<b'$ of good integers for which $b'$ is least. Since $b$ and $k$ are good, $b$ has a small prime divisor. Compress $b$ to an $x\in[k,b]$ supported only on small primes and having the same small-prime mask as $b$. Then $\gcd(x,b')=1$: any common prime would be small and, by similarity, would also divide $b$, contrary to the choice of $b,b'$. Since $x<b'$ and $b'$ is good, $x$ cannot be good; hence it is bad and has a good witness $b^*<x$ coprime to $x$. Every small prime dividing $b$ divides $x$, so $b^*$ and $b$ have no common small prime. But $b^*<x\le b<b'$, making $(b^*,b)$ a violating pair with smaller maximum, a contradiction.

It follows that similar integers have the same status. Otherwise label two similar integers so that $a$ is bad and $b$ is good. There is a good $r<a$ with $\gcd(r,a)=1$. The two good integers $r,b$ share a small prime $p$. Similarity of $a,b$ then gives $p\mid a$, contradicting $p\mid r$ and $\gcd(r,a)=1$.

Now set
\[
L=\prod_{\substack{p\le k\\p\text{ prime}}}p.
\]
This is a positive integer. For every $m\ge k$ and every small prime $p$, the congruence $m+L\equiv m\pmod p$ shows that $p\mid m+L$ exactly when $p\mid m$. Thus $m$ and $m+L$ are similar, so
\[
m\text{ is good}\quad\Longleftrightarrow\quad m+L\text{ is good}.
\]
Let $G$ be the set of good integers and let
\[
T=|G\cap[k,k+L-1]|.
\]
This is positive because $k$ is good. Translation by $L$ is an order-preserving bijection from $G$ onto $G\cap[k+L,\infty)$: the displayed equivalence proves the forward direction, and applying it to $h-L\ge k$ proves surjectivity for every good $h\ge k+L$. Exactly $T$ good integers precede this tail. Therefore translation sends the $n$th good integer to the $(n+T)$th good integer. Since $a_n=g_n$, we conclude
\[
a_{n+T}=a_n+L
\]
for every positive integer $n$, as required. $\square$
