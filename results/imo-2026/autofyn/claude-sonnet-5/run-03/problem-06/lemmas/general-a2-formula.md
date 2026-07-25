## Lemma (General $a_2$ formula)

For every $a_1>1$, writing $p:=\min R(a_1)$ (the smallest prime factor of
$a_1$), $a_2=a_1+p$.

### Proof
By definition, $a_2$ is the least integer exceeding $a_1$ with
$\gcd(a_2,a_1)>1$ (the defining property at $n=1$ has the single
constraint index $i=1$). For $1\le t\le p-1$: if some prime $q$ divided
both $t$ and $a_1$, then $q\in R(a_1)$, so $q\ge p$ by minimality of $p$;
but $q\mid t$ with $0<t\le p-1<p\le q$ forces $q\le t<p\le q$, a
contradiction. Hence $\gcd(t,a_1)=1$ for every such $t$, so
$\gcd(a_1+t,a_1)=\gcd(t,a_1)=1$: $a_1+t$ is invalid, for every
$t=1,\dots,p-1$. Since $p\in R(a_1)$, $p\mid a_1$ and $p\mid p$, so
$p\mid(a_1+p)$; hence $\gcd(a_1+p,a_1)\ge p>1$: $a_1+p$ is valid. As every
integer strictly between $a_1$ and $a_1+p$ has just been shown invalid,
minimality gives $a_2=a_1+p$. $\blacksquare$

### Corollary (odd seeds)
If $a_1$ is odd, then $p:=\min R(a_1)$ is odd (every prime factor of an odd
number is odd), and $a_2=a_1+p$ is a sum of two odd numbers, hence even;
also $p\mid a_2$ (shown in the proof above). Since $\gcd(2,p)=1$ ($p$
odd), $2p\mid a_2$. So for every odd seed, the second term of the sequence
is automatically divisible by $2p$.

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md`, §8.1–8.2,
round 6 (generalizing the special cases previously proved in §3 and §4.1
of the same file). Independently re-derived and numerically spot-checked
by the proof-reviewer (elementary, no gap; matches $a_1=35\Rightarrow
a_2=40=2^3\cdot5$ and $a_1=65\Rightarrow a_2=70=2\cdot5\cdot7$, both
divisible by $2p=10$).
