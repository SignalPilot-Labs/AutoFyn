# Domination Lemma + Term-Membership Criterion (certified, round 7)

Source: `approaches/covering-system-construction-exchange.md`, Lemmas 0.1–0.3
and Lemma 1. Independently re-verified by the proof-reviewer (round 7):
straightforward strong induction / set-theoretic argument, no gaps found.

## Domination Lemma

For indices $m<n$, write $a_m\prec a_n$ if $\mathrm{rad}(a_m)\mid
\mathrm{rad}(a_n)$. Call $a_n$ $\prec$-minimal if no $m<n$ has $a_m\prec
a_n$. Then:

(0.1) For every $n\ge1$ there is a $\prec$-minimal $a_i$, $i\le n$, with
$\mathrm{rad}(a_i)\mid\mathrm{rad}(a_n)$. *(Strong induction: if $a_n$ is
itself minimal take $i=n$; else some $a_m\prec a_n$, $m<n$, and apply the
IH to $m$, using transitivity of divisibility.)*

(0.2) If $\mathrm{rad}(a_i)\mid\mathrm{rad}(a_j)$ and $\gcd(x,a_i)>1$ for
some integer $x$, then $\gcd(x,a_j)>1$. *(A common prime of $x,a_i$ has
$p\in\pi(a_i)\subseteq\pi(a_j)$, so $p\mid a_j$ too.)*

(0.3) For fixed $N,x$: $\gcd(x,a_i)>1$ for all $i\le N$ iff $\gcd(x,a_i)>1$
for all $\prec$-minimal $i\le N$. *(Immediate from 0.1–0.2.)*

## Term-Membership Criterion

For an integer $x\ge a_1$, the following are equivalent: (a) $x=a_n$ for
some $n$; (b) $\gcd(x,a_i)>1$ for every $i\ge1$; (c) $\gcd(x,a_i)>1$ for
every $i$ with $a_i<x$; (d)/(e) the analogous statements restricted to
$\prec$-minimal $a_i$.

*Proof sketch.* (a)$\Rightarrow$(b) is the defining recursive property
applied in both directions (index $i<n$ via the choice of $a_n$; index
$i>n$ via the choice of $a_i$). (c)$\Rightarrow$(a): let $n_0$ be the
largest index with $a_{n_0}\le x$ (finite since $(a_n)$ is strictly
increasing and unbounded); if $a_{n_0}\ne x$, then $x$ is a legal candidate
exceeding $a_{n_0}$ meeting all constraints against $a_1,\dots,a_{n_0}$,
contradicting the greedy minimality defining $a_{n_0+1}\le x<a_{n_0+1}$
(impossible), forcing $a_{n_0}=x$. The (d),(e) forms reduce to (b),(c) via
the Domination Lemma. Full chaining gives all five equivalent.
$\blacksquare$

## Use

Both facts are used to prove the Large-Prime Elimination Theorem
(`large-prime-elimination-theorem.md`) and, combined with it, the full
solution's Step 3–4 (self-sufficiency of $P=\{p\le a_1^2\}$ and exact
periodicity from $n=1$; see `current.md`'s Full proof).
