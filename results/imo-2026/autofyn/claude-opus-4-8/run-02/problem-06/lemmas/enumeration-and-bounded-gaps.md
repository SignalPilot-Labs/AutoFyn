# Certified lemmas: static admissible set, enumeration, bounded gaps

Certified round 1 (proof-reviewer), from `admissible-set-periodicity` (Lemmas 1–3)
and `essential-prime-counting` (Lemmas A–B). Sorry-free, statements match proofs.

Setup: integers $a_1<a_2<\cdots$ the greedy sequence; $a_{n+1}=\min\{x>a_n:\gcd(x,a_i)>1\ \forall i\le n\}$.
$R=\operatorname{rad}(a_1)=\prod_{p\mid a_1}p$. Admissible set
$A=\{x\in\mathbb Z_{>1}:\gcd(x,a_i)>1\ \forall i\ge1\}$.

## Lemma 1 (pairwise non-coprimality; every term admissible)
For all $m\ne n$, $\gcd(a_m,a_n)>1$; hence every term $a_n\in A$.
*Proof:* WLOG $m>n$; the rule makes $a_m$ share a prime with all $a_i$, $i<m$, in particular $a_n$; symmetric. Then for fixed $n$, $\gcd(a_n,a_i)>1$ for all $i\ne n$ and $\gcd(a_n,a_n)=a_n>1$, so $a_n\in A$. $\square$

## Lemma 2 (enumeration)
$a_{n+1}=\min(A\cap(a_n,\infty))$ for all $n$; equivalently $A\cap[a_1,a_n]=\{a_1,\dots,a_n\}$, so $(a_n)$ is the strictly increasing enumeration of $A\cap[a_1,\infty)$ and no element of $A$ lies strictly between consecutive terms.
*Proof:* $A\subseteq\{x:\gcd(x,a_i)>1\ \forall i\le n\}$ gives $\min(A\cap(a_n,\infty))\ge a_{n+1}$; and $a_{n+1}\in A\cap(a_n,\infty)$ (Lemma 1) gives the reverse. Union over $n$ (terms $\to\infty$ by Lemma 3) lists $A\cap[a_1,\infty)$. $\square$

## Lemma 3 (bounded gaps, linear growth)
Every multiple $m>1$ of $R$ lies in $A$; hence $a_{n+1}-a_n\le R$ and $a_1+(n-1)\le a_n\le a_1+(n-1)R$.
*Proof:* each $a_i$ shares a prime $q\in\operatorname{supp}(a_1)$ (Lemma 1), $q\mid R\mid m$, so $\gcd(m,a_i)>1$; thus $m\in A$. The interval $(a_n,a_n+R]$ holds a multiple of $R$, so $a_{n+1}\le a_n+R$ by Lemma 2. $\square$
