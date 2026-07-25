## Status
solved

## Approaches tried
- Round 7 (opening entry): adaptive construction of $Q^\star$ + exchange/local-optimality,
  flagged by the outliner/outline-reviewer as needing a genuinely new termination
  mechanism (not a rehash of jacobsthal-covering-bound's un-derived $K(a_1)$ bound or
  active-set-stabilization's Contamination Dichotomy), on pain of self-reporting RETHINK.
- Round 7 (this build): found and fully verified a **genuinely new, closed-form
  termination mechanism** that is provably distinct in kind from both flagged
  mechanisms: instead of trying to bound $|\mathrm{Nec}|$ directly (jacobsthal) or
  chasing a per-prime "uncontaminated witness" bound (Contamination Dichotomy), we
  construct the fixed, fully explicit candidate set
  $$Q^\star := \{\text{primes} \le a_1^2\}$$
  directly from $a_1$ alone (no reference to the sequence's asymptotic behavior, no
  per-prime density argument, no adaptive obstruction-resolution loop), and prove via
  a **minimality/domination argument on a partial order $\prec$** (the "exchange"
  argument, using minimality of the greedy rule as its sole engine) that $Q^\star$ is
  self-sufficient: every term shares a $Q^\star$-prime with every other term. This
  closes the population's shared central gap completely. **Outcome: full, complete,
  rigorous proof of the whole problem (Status: solved).**

## Current best
Superseded — see Full proof below; the entire problem is closed.

## Target
The problem's full claim: there exist positive integers $T,L$ with $a_{n+T}=a_n+L$
for every positive integer $n \ge 1$ (no transient needed — see Theorem 4 below, which
gives an *exact*, not merely eventual, periodicity).

## Full proof

Throughout, $(a_n)_{n\ge1}$ denotes the sequence defined by the problem: $a_1>1$ is
given, and for $n\ge1$, $a_{n+1}$ is the smallest integer greater than $a_n$ with
$\gcd(a_{n+1},a_i)>1$ for every $i=1,\dots,n$. We use freely that the sequence is
well-defined (some valid $a_{n+1}$ always exists) and strictly increasing; this is the
content of the certified lemma `existence.md`, which we do not re-derive.

For a positive integer $x$, write $\mathrm{rad}(x)$ for the product of the distinct
primes dividing $x$ (so $\mathrm{rad}(x)=1$ iff $x=1$; here always $x>1$ so
$\mathrm{rad}(x)>1$), and $\pi(x) := \{p \text{ prime} : p \mid x\}$ for its prime
support, so $\mathrm{rad}(x)=\prod_{p\in\pi(x)}p$.

### Step 0: The domination relation $\prec$ and the minimal-term reduction

**Definition.** For indices $m<n$, write $a_m \prec a_n$ if $\mathrm{rad}(a_m) \mid
\mathrm{rad}(a_n)$ (equivalently $\pi(a_m)\subseteq\pi(a_n)$). Call $a_n$
**$\prec$-minimal** if there is no $m<n$ with $a_m\prec a_n$.

**Lemma 0.1 (Domination is transitive and dominators exist below every term).** For
every $n\ge1$ there is a $\prec$-minimal $a_i$ with $i\le n$ and $\mathrm{rad}(a_i)\mid
\mathrm{rad}(a_n)$.

*Proof.* Divisibility of radicals is transitive: if $\mathrm{rad}(a_k)\mid
\mathrm{rad}(a_m)$ and $\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$ then
$\mathrm{rad}(a_k)\mid\mathrm{rad}(a_n)$ (divisibility of integers is transitive). Now
argue by strong induction on $n$. If $a_n$ is itself $\prec$-minimal, take $i=n$. If not,
there is $m<n$ with $a_m\prec a_n$, i.e. $\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$; by
the induction hypothesis applied to $m<n$, there is a $\prec$-minimal $a_i$ with $i\le m$
and $\mathrm{rad}(a_i)\mid\mathrm{rad}(a_m)$; by transitivity $\mathrm{rad}(a_i)\mid
\mathrm{rad}(a_n)$, and $i\le m<n\le n$. $\blacksquare$

**Lemma 0.2 (Domination transfers gcd-legality).** If $\mathrm{rad}(a_i)\mid
\mathrm{rad}(a_j)$ and $\gcd(x,a_i)>1$ for some integer $x$, then $\gcd(x,a_j)>1$.

*Proof.* $\gcd(x,a_i)>1$ means some prime $p$ divides both $x$ and $a_i$, i.e.
$p\in\pi(a_i)$. Since $\pi(a_i)\subseteq\pi(a_j)$ (as $\mathrm{rad}(a_i)\mid
\mathrm{rad}(a_j)$), $p\in\pi(a_j)$ too, i.e. $p\mid a_j$. So $p$ divides both $x$ and
$a_j$, giving $\gcd(x,a_j)>1$. $\blacksquare$

**Lemma 0.3 (Reduction to $\prec$-minimal constraints, finite-prefix form).** Fix
$N\ge1$ and an integer $x\ge1$. Then
$$\gcd(x,a_i)>1 \text{ for all } i=1,\dots,N \iff \gcd(x,a_i)>1 \text{ for all
$\prec$-minimal } i\le N.$$

*Proof.* ($\Rightarrow$) Immediate, the right side is a sub-collection of constraints
on the left. ($\Leftarrow$) Suppose $\gcd(x,a_i)>1$ for all $\prec$-minimal $i\le N$.
Fix any $j\le N$. By Lemma 0.1 there is a $\prec$-minimal $a_i$ with $i\le j\le N$ and
$\mathrm{rad}(a_i)\mid\mathrm{rad}(a_j)$. By hypothesis $\gcd(x,a_i)>1$ (since $a_i$ is
$\prec$-minimal and $i\le N$), so by Lemma 0.2, $\gcd(x,a_j)>1$. As $j\le N$ was
arbitrary, the claim follows. $\blacksquare$

### Step 1: A global membership characterization

**Lemma 1 (Term-membership criterion).** For an integer $x\ge a_1$, the following are
equivalent:
(a) $x=a_n$ for some $n\ge1$ (i.e. $x$ is a term of the sequence);
(b) $\gcd(x,a_i)>1$ for every $i\ge1$;
(c) $\gcd(x,a_i)>1$ for every $i\ge1$ with $a_i<x$;
(d) $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i$;
(e) $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i$ with $a_i<x$.

*Proof.*

**(a)$\Rightarrow$(b).** Say $x=a_n$. For $i<n$: by definition of the sequence,
$\gcd(a_n,a_i)>1$ (this is exactly the defining constraint used to select $a_n$ as the
successor of $a_{n-1}$, applied with this $i\le n-1$). For $i=n$: $\gcd(a_n,a_n)=a_n>1$.
For $i>n$: by definition of the sequence, $a_i$ was chosen so that $\gcd(a_i,a_j)>1$
for all $j\le i-1$; taking $j=n\le i-1$ gives $\gcd(a_i,a_n)>1$, i.e.
$\gcd(x,a_i)=\gcd(a_n,a_i)>1$. So (b) holds for all $i\ge1$.

**(b)$\Rightarrow$(c).** Immediate (fewer constraints).

**(c)$\Rightarrow$(a).** Since $a_n\to\infty$ (the sequence is strictly increasing and
unbounded — standard, as each step adds at least $1$), and $x\ge a_1$, there is a
largest index $n_0\ge1$ with $a_{n_0}\le x$ (finite since $a_n\to\infty$; note
$n_0\ge1$ as $a_1\le x$). If $a_{n_0}=x$ we are done ((a) holds with $n=n_0$). Otherwise
$a_{n_0}<x$; by maximality of $n_0$, $a_{n_0+1}>x$ (else $a_{n_0+1}\le x$ would
contradict maximality, since $a_{n_0+1}>a_{n_0}$). The set $\{i\ge1 : a_i<x\}$ equals
exactly $\{1,\dots,n_0\}$ (by definition of $n_0$ as the largest index with
$a_{n_0}\le x$ and $a_{n_0}<x$ in this case, together with the sequence being strictly
increasing, so $a_i<x$ for $i\le n_0$ and $a_i\ge a_{n_0+1}>x$ for $i>n_0$). By
hypothesis (c), $\gcd(x,a_i)>1$ for all $i=1,\dots,n_0$. But $x$ satisfies $x>a_{n_0}$
and $x<a_{n_0+1}$ while meeting all the constraints against $a_1,\dots,a_{n_0}$ — this
contradicts the defining minimality of $a_{n_0+1}$ as the *smallest* integer exceeding
$a_{n_0}$ meeting these constraints. Hence this case is impossible, and $a_{n_0}=x$
must hold, giving (a).

**(b)$\Rightarrow$(d) and (d)$\Rightarrow$(e).** Both immediate (fewer constraints in
each implication's conclusion, i.e. (d) is a sub-collection of (b)'s constraints, and
(e) a sub-collection of (d)'s).

**(e)$\Rightarrow$(c).** Suppose (e) holds. Fix any $j$ with $a_j<x$. By Lemma 0.1
there is a $\prec$-minimal $a_i$ with $i\le j$ and $\mathrm{rad}(a_i)\mid
\mathrm{rad}(a_j)$; since $i\le j$ and the sequence is strictly increasing,
$a_i\le a_j<x$, so $a_i<x$. By (e), $\gcd(x,a_i)>1$. By Lemma 0.2 (domination
transfers legality), $\gcd(x,a_j)>1$. As $j$ was an arbitrary index with $a_j<x$, (c)
holds.

Chaining: (a)$\Rightarrow$(b)$\Rightarrow$(c)$\Rightarrow$(a) and
(b)$\Rightarrow$(d)$\Rightarrow$(e)$\Rightarrow$(c)$\Rightarrow$(a)$\Rightarrow$(b)
establishes all five are equivalent. $\blacksquare$

### Step 2: The Large-Prime Elimination Theorem (the new termination mechanism)

Define $P := \{p \text{ prime} : p \le a_1^2\}$, a **fixed, finite** set determined by
$a_1$ alone (this is the explicit, closed-form candidate $Q^\star$; note $P$ is not
grown adaptively step by step and is not a per-prime density argument — it is simply
"all primes up to the fixed threshold $a_1^2$"). Call a prime **large** if it exceeds
$a_1^2$, and **small** otherwise (small primes are exactly the elements of $P$).

**Theorem 2 (Large-Prime Elimination).** For every $n\ge1$: if $a_n$ is divisible by a
large prime, then $a_n$ is not $\prec$-minimal.

*Proof.* Strong induction on $n$.

*Base case $n=1$.* Every prime factor of $a_1$ is at most $a_1$ (a prime dividing a
positive integer cannot exceed it), and $a_1<a_1^2$ since $a_1>1$. So no prime factor
of $a_1$ is large; the statement is vacuously true for $n=1$.

*Inductive step.* Let $n\ge2$, and assume the statement holds for all indices $<n$
(inductive hypothesis, IH). Suppose $a_n$ is divisible by a large prime $p>a_1^2$;
write $c:=a_n/p$ (a positive integer, since $p\mid a_n$). We must produce $j<n$ with
$a_j\prec a_n$.

Since $n\ge2$, index $1\le n-1$ is one of the constraints used to select $a_n$, so
$\gcd(a_n,a_1)>1$; let $q$ be any prime dividing $\gcd(a_1,a_n)$. Since $q\mid a_1$ and
$a_1>1$, $q\le a_1<a_1^2<p$, so $q\ne p$.

**Claim: some term of the geometric sequence $c, qc, q^2c, q^3c,\dots$ lies in the
half-open interval $[a_1,a_n)$.**

Since $a_n=pc\ge p$ (as $c\ge1$), we get $a_n/a_1 \ge p/a_1 > a_1$ (using $p>a_1^2$).
Also $a_1\ge q$. Hence $a_n/a_1 > a_1 \ge q$, so in particular $a_n/a_1>q$, i.e.
$$a_1\cdot q < a_n. \tag{$\ast$}$$
Let $k\ge0$ be the least integer with $q^kc \ge a_1$ (this exists: if $c\ge a_1$ take
$k=0$; otherwise, since $q\ge2$, the sequence $q^kc\to\infty$, so some finite $k$ works).

- If $k=0$: then $c\ge a_1$, and $c<a_n$ (since $a_n=pc$ and $p\ge2$, so $c\le a_n/2<a_n$).
  So $c=q^0c\in[a_1,a_n)$.
- If $k\ge1$: by minimality of $k$, $q^{k-1}c<a_1$, so $q^kc<a_1q<a_n$ by $(\ast)$. And
  $q^kc\ge a_1$ by choice of $k$. So $q^kc\in[a_1,a_n)$.

Either way, $x:=q^kc\in[a_1,a_n)$, proving the claim.

**$x$ satisfies $\gcd(x,a_m)>1$ for all $m=1,\dots,n-1$.** Fix $m<n$. By Lemma 0.1
there is a $\prec$-minimal $a_i$ with $i\le m<n$, so $i<n$; by the induction
hypothesis applied to index $i<n$ (contrapositive: since $a_i$ IS $\prec$-minimal, it
is NOT divisible by any large prime), $p\nmid a_i$. By the defining property of the
sequence, $\gcd(a_n,a_i)>1$ (since $i<n$ was a live constraint when $a_n$ was selected,
using $i\le n-1$); let $r$ be a common prime factor of $a_n=pc$ and $a_i$. Since
$p\nmid a_i$, $r\ne p$, so (as $r\mid a_n=pc$ and $r\ne p$ is prime) $r\mid c$. Thus $r$
divides both $c$ and $a_i$, so $\gcd(c,a_i)\ge r>1$; since $c\mid x=q^kc$, also
$\gcd(x,a_i)\ge\gcd(c,a_i)>1$. By Lemma 0.2 (domination transfers legality, using
$\mathrm{rad}(a_i)\mid\mathrm{rad}(a_m)$ from Lemma 0.1), $\gcd(x,a_m)>1$. As $m<n$ was
arbitrary, $\gcd(x,a_m)>1$ holds for all $m=1,\dots,n-1$.

**$x$ is itself a term $a_j$ with $j<n$.** Since $x<a_n\le a_{n-1}+(\text{gap})$, two
cases: if $x=a_{n-1}$, then trivially $x$ is the term $a_{n-1}$, so $j=n-1<n$. If
$x<a_{n-1}$: let $n_0$ be the largest index with $a_{n_0}\le x$ (exists since $x\ge a_1$
and the sequence is increasing and unbounded; here $n_0\le n-2$ since $x<a_{n-1}$
forces $n_0<n-1$). By the same argument as in the proof of Lemma 1's
(c)$\Rightarrow$(a) implication — applied here using only the constraints
$\gcd(x,a_1)>1,\dots,\gcd(x,a_{n-1})>1$ just established, which is a superset of
$\gcd(x,a_i)>1$ for $i\le n_0\le n-2\le n-1$ — either $a_{n_0}=x$ (done, $j=n_0<n$), or
else $x$ would be a valid candidate strictly between $a_{n_0}$ and $a_{n_0+1}$
satisfying all constraints against $a_1,\dots,a_{n_0}$, contradicting the minimality
that defines $a_{n_0+1}$. So $a_{n_0}=x$ and $j:=n_0<n$.

**Conclusion.** We have shown $x=a_j$ for some $j<n$, with $x=q^kc$. Now
$\pi(x)=\{q\}\cup\pi(c)$. Since $c\mid a_n$ exactly (as $a_n=pc$), $\pi(c)\subseteq
\pi(a_n)$. Also $q\mid a_n$ directly, because $q$ was chosen as a prime factor of
$\gcd(a_1,a_n)$, so in particular $q\mid a_n$. Hence $\pi(x)=\{q\}\cup\pi(c)\subseteq
\pi(a_n)$, i.e. $\mathrm{rad}(a_j)=\mathrm{rad}(x)\mid\mathrm{rad}(a_n)$. Since $j<n$,
this exactly says $a_j\prec a_n$, so $a_n$ is not $\prec$-minimal. This completes the
inductive step, and the theorem. $\blacksquare$

**Corollary 2.1 (Self-sufficiency of the fixed set $P$).** Every $\prec$-minimal term
$a_n$ has all its prime factors in $P$, i.e. $\pi(a_n)\subseteq P$.

*Proof.* Immediate contrapositive of Theorem 2: if $a_n$ is $\prec$-minimal, it cannot
be divisible by a large prime (else Theorem 2 says it is not minimal, contradiction),
so every prime factor of $a_n$ is $\le a_1^2$, i.e. lies in $P$. $\blacksquare$

This is the genuinely new termination mechanism this approach set out to find: a
single **closed-form, a priori bound** ($a_1^2$) on the prime factors that can ever
appear in a $\prec$-minimal term — proved directly by an induction whose engine is
"large prime factors are redundant because a *smaller*, legal, dominating term using
only a small common prime with $a_1$ must already have appeared" — a mechanism that
does not bound $|\mathrm{Nec}|$ by counting distinct witnessing primes (jacobsthal's
and active-set-stabilization's shared framing) and does not require locating an
uncontaminated witness at a bounded index for each individual recruited prime
(Contamination Dichotomy's framing). It bounds the *support* of the minimal terms
directly and uniformly, sidestepping the Nec/contamination bookkeeping entirely.

### Step 3: Reduction to a fixed modulus and exact periodicity

Let $L:=\prod_{p\in P}p=\prod_{p\le a_1^2}p$, a fixed positive integer determined by
$a_1$ alone (finite product since $P$ is finite; $L\ge2$ since $2\in P$ as $a_1^2\ge4$).

For an integer $x\ge1$, let $S(x):=\pi(x)\cap P$ (its set of *small* prime factors).
Note $S(x)$ depends only on $x\bmod L$: since $L=\prod_{p\in P}p$ is squarefree with
prime factors exactly $P$, for a prime $p\in P$, $p\mid x \iff p\mid (x\bmod L)$
whenever we interpret $x\bmod L$ representatively (standard fact: $p\mid L$ so
$x\equiv x'\pmod L\Rightarrow x\equiv x'\pmod p\Rightarrow(p\mid x\iff p\mid x')$).
Hence $x\equiv x'\pmod L\Rightarrow S(x)=S(x')$.

By Corollary 2.1, every $\prec$-minimal term $a_i$ has $\pi(a_i)=S(a_i)\subseteq P$
(all its factors are small). So for such $a_i$ and any integer $x$,
$$\gcd(x,a_i)>1 \iff \pi(x)\cap\pi(a_i)\ne\emptyset \iff S(x)\cap S(a_i)\ne\emptyset,$$
where the last equivalence holds because $\pi(a_i)=S(a_i)\subseteq P$, so a common
prime of $x$ and $a_i$ is automatically a common *small* prime, i.e. lies in
$S(x)\cap S(a_i)$; conversely a shared element of $S(x)$ and $S(a_i)$ is trivially a
shared prime of $x,a_i$.

Let $\mathcal{F}:=\{S(a_i) : a_i \text{ is $\prec$-minimal}\}\subseteq 2^P$ (a family of
subsets of the finite set $P$; note $\mathcal F$ is automatically finite, being a
subset of $2^P$, though we do not even need this finiteness of $\mathcal F$ itself for
the argument — only $P$'s finiteness is used below).

By Lemma 1, criterion (d): for $x\ge a_1$,
$$x \text{ is a term of the sequence} \iff \gcd(x,a_i)>1 \text{ for every
$\prec$-minimal }a_i \iff S(x)\cap A\ne\emptyset \text{ for every } A\in\mathcal F.$$

The right-hand condition depends on $x$ only through $S(x)$, hence only through
$x\bmod L$. Therefore:
$$\textbf{for } x,y\ge a_1 \text{ with } x\equiv y \pmod L: \quad x\text{ is a term}
\iff y \text{ is a term.} \tag{$\dagger$}$$

### Step 4: Assembling $T$ and $L$ — exact periodicity for every $n\ge1$

Let $\mathrm{Term}:=\{a_n : n\ge1\}$ (as a set of integers, all $\ge a_1$). By
$(\dagger)$, for every $x\ge a_1$: $x\in\mathrm{Term} \iff x+L\in\mathrm{Term}$ (taking
$y=x+L\ge a_1$ too, and $x\equiv x+L\pmod L$).

Define $T:=|\mathrm{Term}\cap[a_1,a_1+L)|$. This is a well-defined positive integer:
finite since it's a subset of the finite interval of integers $[a_1,a_1+L)$
(cardinality $\le L$), and positive since $a_1\in\mathrm{Term}\cap[a_1,a_1+L)$
(as $a_1$ is itself a term of the sequence and lies in $[a_1,a_1+L)$).

**Theorem 4.** With $L,T$ as defined above, $a_{n+T}=a_n+L$ for every $n\ge1$.

*Proof.* Define $\varphi:\mathrm{Term}\to\mathbb Z$ by $\varphi(x)=x+L$. By the
periodicity established above ($x\in\mathrm{Term}\iff x+L\in\mathrm{Term}$, for all
$x\ge a_1$, and every element of $\mathrm{Term}$ is $\ge a_1$), $\varphi$ maps
$\mathrm{Term}$ bijectively onto $\mathrm{Term}\cap[a_1+L,\infty)$: it is injective
(adding a constant), its image lies in $\mathrm{Term}\cap[a_1+L,\infty)$ (if
$x\in\mathrm{Term}$ then $x+L\in\mathrm{Term}$ by the forward direction, and
$x+L\ge a_1+L$), and it is onto that set (if $y\in\mathrm{Term}$, $y\ge a_1+L$, then
$y-L\ge a_1$ and $y-L\in\mathrm{Term}$ by the backward direction of the equivalence
applied with $x=y-L$, i.e. $y-L\in\mathrm{Term}\iff y\in\mathrm{Term}$, and the latter
holds).

$\varphi$ is also strictly increasing (adding a positive constant), hence an order
isomorphism from $(\mathrm{Term},<)$ onto $(\mathrm{Term}\cap[a_1+L,\infty),<)$.

Now enumerate $\mathrm{Term}$ in increasing order: since $\mathrm{Term}=\{a_n:n\ge1\}$
and the sequence is strictly increasing, this enumeration is exactly $a_1<a_2<a_3<
\cdots$. The finite initial segment $\mathrm{Term}\cap[a_1,a_1+L)$ has exactly $T$
elements by definition of $T$, and consists exactly of the $T$ smallest elements of
$\mathrm{Term}$, i.e. $\{a_1,\dots,a_T\}$ (every element of $\mathrm{Term}$ below
$a_1+L$ is among the first $T$ in the increasing enumeration, and conversely, since all
other elements of Term are $\ge a_1+L$ by the periodicity structure — indeed if some
$a_m$ with $m\le T$ satisfied $a_m\ge a_1+L$ that would force at least $T+1$ elements
of Term to lie in $[a_1,a_1+L)\cup\{a_1+L,\dots\}$... more directly: $\mathrm{Term}\cap
[a_1,a_1+L)$ and $\mathrm{Term}\cap[a_1+L,\infty)$ partition $\mathrm{Term}$, the first
has exactly $T$ elements, and since $\mathrm{Term}$ is enumerated in increasing order,
the first $T$ elements of the enumeration are exactly those below $a_1+L$, i.e.
$\{a_1,\dots,a_T\}=\mathrm{Term}\cap[a_1,a_1+L)$ and
$\{a_{T+1},a_{T+2},\dots\}=\mathrm{Term}\cap[a_1+L,\infty)$).

Since $\varphi$ is an order isomorphism $\mathrm{Term}\to\mathrm{Term}\cap
[a_1+L,\infty)$, it sends the $n$-th smallest element of $\mathrm{Term}$ (namely $a_n$)
to the $n$-th smallest element of $\mathrm{Term}\cap[a_1+L,\infty)$ (namely
$a_{T+n}$, by the identification of that set with $\{a_{T+1},a_{T+2},\dots\}$ just
established, whose $n$-th element is $a_{T+n}$). That is,
$$\varphi(a_n)=a_n+L=a_{n+T}$$
for every $n\ge1$. $\blacksquare$

### Conclusion

Theorem 4 establishes the full claim of the problem: with
$$L=\prod_{p\le a_1^2, \ p \text{ prime}} p, \qquad T = \big|\{a_n : n\ge1\}\cap[a_1,a_1+L)\big|,$$
both explicit positive integers determined by $a_1$, we have $a_{n+T}=a_n+L$ for
**every** positive integer $n\ge1$ — an exact periodicity from the very first term, not
merely an eventual one (so this also fully resolves, as a free corollary, the
previously-tracked "prefix-extension gap" from earlier rounds: `reduction-lemma-ss1-vs-unified-claim.md`'s
unified target is achieved with $Q=P=\{p\le a_1^2\}$ and no transient at all). $\blacksquare$

### Sanity check against the population's numerics

- $a_1=15$: $P=\{2,3,5,7,11,13\}$ (all primes $\le225$), certainly self-sufficient
  since even the much smaller $\mathrm{Nec}=\{2,3,5\}$ suffices in this case (rounds
  1–6's own hand-computation); $Q^\star=P$ is a (non-minimal, but valid) superset,
  consistent.
- $a_1=375$: $\mathrm{rad}(a_1)=15$, $a_1^2=140625$; the round-7 explorer's recruited
  prime $19$ satisfies $19 < 140625$, consistent with (indeed far inside) the bound of
  Theorem 2 — this is exactly why no *tighter* closed-form threshold (like
  $O(\mathrm{rad}(a_1))$) could ever be made to work uniformly (as the round-6/7
  numerics already showed with the $a_1=194287$ recruit $103>89=\max R(a_1)$), while
  $a_1^2$ still works because it is provably (not just empirically) an upper bound on
  every $\prec$-minimal term's prime factors, however large the true recruited primes
  turn out to be numerically.
- These checks are illustrative only; Theorem 2's proof above is a full, unconditional
  argument, not dependent on any numerical evidence.

## Promotable lemmas

- **Domination Lemma (Lemma 0.1–0.2 above)**: the $\prec$ relation ($a_m\prec a_n$ iff
  $m<n$ and $\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$) is such that every term has a
  $\prec$-minimal dominator at or before its own index, and domination transfers
  gcd-legality. Fully proved above; reusable independent of the rest of this proof.
- **Term-Membership Criterion (Lemma 1)**: for $x\ge a_1$, $x$ is a term of the
  sequence iff $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i$ (equivalently, several
  other equivalent forms). Fully proved above.
- **Large-Prime Elimination Theorem (Theorem 2 / Corollary 2.1)**: every
  $\prec$-minimal term's prime factors are all $\le a_1^2$ — the central closed-form
  bound that closes the problem's long-standing central gap (finiteness of a
  self-sufficient prime set). This is the key new result of this round.
- **Exact Periodicity Theorem (Theorem 4)**: general order-isomorphism argument
  showing that any subset of integers closed under "$x\in S\iff x+L\in S$" for
  $x\ge a_1$, enumerated increasingly as $a_1<a_2<\cdots$, satisfies
  $a_{n+T}=a_n+L$ for every $n\ge1$ with $T:=|S\cap[a_1,a_1+L)|$ — a reusable
  general fact about periodic integer sets, independent of the specific problem.

All four are certified-ready; recommend the proof-reviewer promote them (and mark the
overall problem `solved`, since this file's Full proof is a complete, self-contained,
gap-free solution of the entire IMO 2026/6 statement).
