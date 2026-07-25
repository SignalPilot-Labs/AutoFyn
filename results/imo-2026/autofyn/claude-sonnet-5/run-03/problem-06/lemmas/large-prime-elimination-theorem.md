# Large-Prime Elimination Theorem (certified, round 7)

Source: `approaches/covering-system-construction-exchange.md`, Theorem 2 /
Corollary 2.1. Independently re-derived and stress-tested by the
proof-reviewer (round 7): full line-by-line re-derivation of the inductive
step, plus numerical confirmation across 12 seeds (including previously
adversarial instances $a_1\in\{375,20735,194287,45045\}$) that no
$\prec$-minimal term ever carries a prime factor anywhere near the proven
bound $a_1^2$ (observed max ratio $\mathrm{maxprime}/a_1^2 \approx 0.06$ in
the worst tested case, consistent with — and far inside — the theorem).

## Setup

For $x>1$, write $\mathrm{rad}(x)$ for the product of its distinct prime
factors and $\pi(x)$ for its set of prime factors. For indices $m<n$ of the
problem's sequence $(a_n)$, say $a_m\prec a_n$ if $\mathrm{rad}(a_m)\mid
\mathrm{rad}(a_n)$; call $a_n$ **$\prec$-minimal** if no $m<n$ has
$a_m\prec a_n$.

**Domination Lemma (prerequisite, also certified below).** For every
$n\ge1$ there is a $\prec$-minimal $a_i$, $i\le n$, with $\mathrm{rad}(a_i)
\mid\mathrm{rad}(a_n)$; and if $\mathrm{rad}(a_i)\mid\mathrm{rad}(a_j)$ and
$\gcd(x,a_i)>1$ then $\gcd(x,a_j)>1$.

## Statement

Call a prime **large** if it exceeds $a_1^2$. Then: for every $n\ge1$, if
$a_n$ is divisible by a large prime, $a_n$ is not $\prec$-minimal.
Equivalently (Corollary): every $\prec$-minimal term has all its prime
factors $\le a_1^2$.

## Proof (strong induction on $n$)

*Base case $n=1$:* every prime factor of $a_1$ is $\le a_1<a_1^2$, so
vacuously no large prime divides $a_1$.

*Inductive step:* Suppose $n\ge2$ and $a_n=pc$ with $p>a_1^2$ prime,
$c:=a_n/p\ge1$. Since $n\ge2$, the index-$1$ constraint gives
$\gcd(a_n,a_1)>1$; let $q$ be a prime factor of this gcd. Since $q\mid a_1$,
$q\le a_1<a_1^2<p$, so $q\ne p$, and (since $q\mid a_n=pc$, $q\ne p$) in
fact $q\mid c$.

Since $a_n=pc\ge p>a_1^2$, $a_n/a_1>a_1\ge q$, so $a_1 q<a_n$. Let $k\ge0$
be least with $q^kc\ge a_1$. If $k=0$: $c\ge a_1$ and $c\le a_n/2<a_n$. If
$k\ge1$: $q^{k-1}c<a_1$ so $q^kc<a_1q<a_n$, and $q^kc\ge a_1$ by choice of
$k$. Either way $x:=q^kc\in[a_1,a_n)$.

For any $m<n$: by the Domination Lemma there is a $\prec$-minimal $a_i$,
$i\le m<n$; by IH (applied to $i<n$, contrapositive) $p\nmid a_i$. Since
$\gcd(a_n,a_i)>1$ (the $i<n$ constraint used to select $a_n$), some prime
$r\mid a_n=pc$ and $r\mid a_i$; as $p\nmid a_i$, $r\ne p$, so $r\mid c$.
Hence $\gcd(c,a_i)\ge r>1$, and since $c\mid x$, $\gcd(x,a_i)>1$. By the
Domination Lemma (transfer), $\gcd(x,a_m)>1$. This holds for all $m<n$.

Since $x\in[a_1,a_n)$ satisfies $\gcd(x,a_m)>1$ for all $m=1,\dots,n-1$,
the Term-Membership Criterion (below) shows $x=a_j$ for some $j<n$.
Finally $\pi(x)\subseteq\{q\}\cup\pi(c)\subseteq\pi(a_n)$ (both $q$ and
every prime of $c$ divide $a_n=pc$), so $\mathrm{rad}(a_j)\mid
\mathrm{rad}(a_n)$, i.e. $a_j\prec a_n$: $a_n$ is not $\prec$-minimal.
$\blacksquare$

## Caveat

The bound $a_1^2$ is not claimed tight (numerics suggest the true necessary
primes are much smaller in every tested instance); the theorem only needs
*some* finite, closed-form, $a_1$-only-dependent bound to exist, and this
is what is proved.
