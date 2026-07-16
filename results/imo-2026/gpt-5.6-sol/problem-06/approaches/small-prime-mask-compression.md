## Status
solved

## Approaches tried
- Direct good/bad recursion followed by small-prime-mask compression — worked: strong induction identifies the greedy sequence with the good integers, a threshold-power construction removes all primes greater than the initial term without changing the small-prime mask, and a minimal-counterexample argument proves that this mask determines goodness. The resulting periodic mask gives the required translated enumeration.

## Current best
The complete proof below establishes that, with $k=a_1$ and $L$ equal to the product of all primes at most $k$, goodness is invariant under translation by $L$. If $T$ is the number of good integers in $[k,k+L-1]$, the order-preserving bijection $g\mapsto g+L$ then proves $a_{n+T}=a_n+L$ for every $n\ge 1$.

## Full proof
Put $k=a_1$. We use **strong induction** (the Induction entry of the knowledge base), the **minimal-counterexample/extremal principle** (the Pigeonhole/extremal entry), **divisor analysis**, and **modular arithmetic with periodic residue masks** (the corresponding Number Theory entries).

### 1. A recursive classification

We classify every integer $m\ge k$ as *good* or *bad*, recursively in increasing order. Declare $k$ good. Once all integers from $k$ through $m-1$ have been classified, declare $m$ good if

\[
\gcd(m,g)>1\qquad\text{for every good integer }g\text{ with }k\le g<m,
\]

and declare $m$ bad otherwise. This is well-defined because only finitely many already classified integers occur in the test.

Thus the recursion gives both of the following statements, not merely one implication:

* if $m$ is bad, then there is a good integer $g$ with $k\le g<m$ and $\gcd(m,g)=1$;
* if $m$ is good, then no good integer $g$ with $k\le g<m$ is coprime to $m$.

In particular, any two good integers have greatest common divisor greater than $1$: after ordering them as $g<h$, the definition of goodness of $h$ gives $\gcd(g,h)>1$.

We next prove that the given sequence is exactly the increasing enumeration of the good integers. This is a strong-induction argument on the number of listed good integers. The first good integer is $k=a_1$. Suppose that $a_1<\cdots<a_n$ are precisely the first $n$ good integers. Let $c$ be the least integer greater than $a_n$ such that

\[
\gcd(c,a_i)>1\quad(1\le i\le n).
\]

Such a $c$ exists: for example, any multiple of $a_1a_2\cdots a_n$ exceeding $a_n$ satisfies all these inequalities. Every good integer smaller than $c$ is among $a_1,\ldots,a_n$, by the induction hypothesis together with the minimality of $c$. Hence $c$ is non-coprime to every smaller good integer, so the recursive definition declares $c$ good. On the other hand, if $a_n<d<c$, then the minimality of $c$ supplies some $i\le n$ for which $\gcd(d,a_i)=1$. Since $a_i$ is a smaller good integer, $d$ is bad. Therefore $c$ is precisely the next good integer. The defining greedy rule of the problem also says that this same least $c$ is $a_{n+1}$. The induction is complete.

Consequently the sequence terms are all the good integers in increasing order.

### 2. Compression to small prime factors

Call a prime *small* if it is at most $k$, and *large* if it is greater than $k$. Say that two integers at least $k$ are *similar* if they have exactly the same small prime divisors.

We prove the following compression lemma by divisor analysis.

**Compression lemma.** If $b\ge k$ has at least one small prime divisor, then there is an integer $x$ such that

\[
k\le x\le b,
\]

$x$ is similar to $b$, and every prime divisor of $x$ is small.

**Proof.** If $b$ has no large prime divisor, take $x=b$. It meets all the requirements, including $k\le x\le b$.

Now suppose that $b$ has a large prime divisor $q$. Let

\[
A=\prod_{\substack{s\mid b\\ s\text{ prime},\ s\le k}}s,
\]

the product of all distinct small prime divisors of $b$. The hypothesis that $b$ has a small prime divisor ensures that this is a nonempty product. Choose one small prime divisor $p$ of $b$, so $p\mid A$. Let $e\ge0$ be the least integer for which

\[
x=p^eA\ge k.
\]

Such an exponent exists because $p\ge2$. The prime divisors of $x$ are exactly those of $A$, so they are all small and $x$ is similar to $b$.

It remains to prove $x\le b$. If $e=0$, then $x=A$. Since $A$ is a product of distinct prime divisors of $b$, it divides $b$, and hence $x=A\le b$.

If $e>0$, minimality of $e$ gives $p^{e-1}A<k$, and multiplication by $p$ yields

\[
x=p^eA<pk.
\]

Because $p\mid A$, we have $p\le A$; because $q$ is large, $k<q$. Therefore the complete comparison is

\[
x<pk\le Ak<Aq\le b.
\]

The last inequality holds because $Aq$ is a product of distinct prime divisors of $b$, so $Aq\mid b$. Thus $x<b$ in this case. This covers separately the no-large-prime case, the large-prime case with $e=0$, and the large-prime case with $e>0$, and proves the lemma. $\square$

### 3. Goodness depends only on the small-prime mask

We claim that any two similar integers have the same classification.

Suppose otherwise. By the minimal-counterexample form of the extremal principle, choose a similar oppositely classified pair whose maximum is as small as possible. Label its bad member $a$ and its good member $b$; this labeling makes no assumption about whether $a<b$ or $b<a$.

Since $a$ is bad, the recursive classification supplies a good integer $r$ such that

\[
k\le r<a\quad\text{and}\quad \gcd(r,a)=1. \tag{1}
\]

The integers $r$ and $k$ are both good, so the pairwise non-coprimality of good integers gives $\gcd(r,k)>1$. Any prime dividing this gcd is at most $k$, and therefore $r$ has a small prime divisor. The compression lemma may consequently be applied to $r$. It gives an integer $r'$ with

\[
k\le r'\le r,
\]

such that $r'$ is similar to $r$ and every prime divisor of $r'$ is small.

We now show that $r'$ is good. If $r'=r$, this follows because $r$ is good. If $r'<r$ and $r'$ were bad, then the similar pair $(r',r)$ would have opposite classifications, while

\[
\max(r',r)=r<a\le\max(a,b),
\]

contradicting the minimal choice of $(a,b)$. Hence $r'$ is good in every case.

Both $r'$ and $b$ are good, so they have a common prime divisor, say $s$. Every prime divisor of $r'$ is small, hence $s\le k$. Similarity of $r'$ and $r$ implies $s\mid r$. Similarity of $b$ and $a$ implies $s\mid a$. Thus $s$ divides both $r$ and $a$, contradicting $\gcd(r,a)=1$ in (1). This contradiction proves that similar integers always have the same classification.

### 4. Periodicity and the exact index shift

Let

\[
L=\prod_{p\le k,\ p\text{ prime}}p.
\]

This is a positive integer. For every $m\ge k$ and every prime $p\le k$, we have $p\mid L$, and modular arithmetic gives

\[
m+L\equiv m\pmod p.
\]

Therefore $p$ divides $m+L$ if and only if it divides $m$. Thus $m$ and $m+L$ are similar, and the result of the previous section gives

\[
m\text{ is good}\quad\Longleftrightarrow\quad m+L\text{ is good} \qquad(m\ge k). \tag{2}
\]

Let $G$ be the set of good integers and define

\[
T=|G\cap[k,k+L-1]|.
\]

This is a positive integer because $k$ itself is good and belongs to that interval.

By (2), translation by $L$ maps $G$ into $G\cap[k+L,\infty)$. It is also onto that set: if $y\in G$ and $y\ge k+L$, then $y-L\ge k$, and applying (2) to $y-L$ shows that $y-L$ is good. Hence

\[
\tau:G\longrightarrow G\cap[k+L,\infty),\qquad \tau(g)=g+L,
\]

is a bijection. It is order-preserving because $g<h$ implies $g+L<h+L$.

Exactly the $T$ elements of $G\cap[k,k+L-1]$ precede the target set $G\cap[k+L,\infty)$ in the increasing ordering of $G$. Since $a_n$ is the $n$th element of $G$, the order-preserving bijection sends it to the $n$th element of the translated tail, which is the $(n+T)$th element of all of $G$. Therefore

\[
a_n+L=a_{n+T}
\]

for every positive integer $n$. The positive integers $T$ and $L$ constructed above have the required property. $\qed$

## Promotable lemmas
- **Small-prime compression lemma.** For fixed $k\ge2$, every $b\ge k$ having a prime divisor at most $k$ has a number $x\in[k,b]$ with exactly the same prime divisors at most $k$ and no prime divisors greater than $k$. Proved in Section 2.
- **Small-prime-mask invariance for the recursive coprimality kernel.** Under the recursion in Section 1, two integers at least $k$ with the same prime divisors at most $k$ have the same good/bad classification. Proved in Section 3.
- **Periodic-set enumeration lemma (specialized form).** If a subset $G\subseteq[k,\infty)\cap\mathbb Z$ satisfies $m\in G\iff m+L\in G$ for all $m\ge k$, and $T=|G\cap[k,k+L-1]|>0$, then its increasing enumeration $(g_n)$ satisfies $g_{n+T}=g_n+L$ for every $n\ge1$. Proved in Section 4.
