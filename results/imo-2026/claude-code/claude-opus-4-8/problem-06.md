Time: 1h 48m 20s

I've done extensive exploration and verification. Let me now write up the complete solution. This is a
genuinely hard problem, and I have verified every structural claim computationally across hundreds of starting
values.

---
Solution

Setup and notation

For a positive integer $m>1$ let $R(m)$ denote its set of prime divisors, and write $R(m)\cap
R(m')\neq\varnothing \iff \gcd(m,m')>1$. Throughout, $(a_n){n\ge1}$ is the given sequence: $a_1>1$, the 
sequence is strictly increasing, and $a{n+1}$ is the least integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for all
$i\le n$.

Let $R_1=R(a_1)={p_1,\dots,p_k}$ and $M=p_1p_2\cdots p_k=\operatorname{rad}(a_1)$ (the product of the distinct
primes dividing $a_1$; so $M\mid a_1$ and $M\le a_1$).

For a finite set $P$ of primes write $n_P=\prod_{p\in P}p$ (a squarefree integer).

---
Step 1. Any two terms are non‑coprime

For $i<j$, the defining property of $a_j$ (applied to the constraint $i\le j-1$) gives $\gcd(a_j,a_i)>1$.
Hence:

$$\gcd(a_i,a_j)>1 \qquad\text{for all } i\ne j. \tag{1}$$

Step 2. The sequence enumerates a fixed set $S$

Define
$$S={m\in\mathbb Z_{>0}: \gcd(m,a_i)>1 \text{ for every } i\ge 1}.$$
By $(1)$ every term lies in $S$. Note $S$ is radical‑determined ($m\in S$ depends only on $R(m)$) and upward 
closed under divisibility ($m\in S,\ m\mid m'\Rightarrow m'\in S$), since $R(m)\subseteq R(m')$.

Claim. ${a_n:n\ge1}=S\cap[a_1,\infty)$, listed in increasing order.

Proof. Let $A_n={m:\gcd(m,a_i)>1\ \forall i\le n}\supseteq S$. By definition
$a_{n+1}=\min\big(A_n\cap(a_n,\infty)\big)$. Since $a_{n+1}\in S$ (by $(1)$) and $S\subseteq A_n$, we get
$$a_{n+1}=\min\big(A_n\cap(a_n,\infty)\big)\le \min\big(S\cap(a_n,\infty)\big),$$
while $a_{n+1}\in S\cap(a_n,\infty)$ forces the reverse inequality. Hence
$a_{n+1}=\min\big(S\cap(a_n,\infty)\big)$. Also $a_1=\min\big(S\cap[a_1,\infty)\big)$ trivially. Thus the
sequence is exactly the increasing enumeration of $S\cap[a_1,\infty)$, with no element of $S$ skipped.
$\qquad\blacksquare$

Consequence. If $S$ is periodic — i.e. there is $L\ge1$ with $m\in S\iff m+L\in S$ for all $m\ge1$ — then the 
desired conclusion holds for every $n\ge 1$. Indeed, put $T=#\big(S\cap[a_1,a_1+L)\big)\ge1$ (nonempty as
$a_1\in S$). Periodicity gives, for every integer $x\ge a_1$, $x\in S\iff x+L\in S$; so the shift $x\mapsto
x+L$ is an order isomorphism $S\cap[a_1,\infty)\to S\cap[a_1+L,\infty)$. The set $S\cap[a_1+L,\infty)$ equals
$S\cap[a_1,\infty)$ with its first $T$ elements $a_1,\dots,a_T$ removed, i.e. equals ${a_{T+1},a_{T+2},\dots}$;
its $n$‑th element is $a_{T+n}$. On the other hand, being the image of the shift, its $n$‑th element is
$a_n+L$. Therefore
$$a_{n+T}=a_n+L\qquad\text{for all } n\ge1.$$

So it suffices to prove that $S$ is periodic.

Step 3. Bounded gaps, and the structure of $S$

Every multiple of $M$ lies in $S$ (a multiple of $M=\prod R_1$ is divisible by each $p_j\in R_1$, and every
$a_i$ is divisible by some $p_j$, so shares that factor). Consequently the elements of $S\cap[a_1,\infty)$ have
gaps at most $M$:
$$a_{n+1}-a_n\le M\qquad\text{for all }n, \tag{2}$$
because the next multiple of $M$ above $a_n$ lies in $S$ and is $\le a_n+M$.

Call a finite set $P$ of primes a transversal if it meets $R(a_i)$ for every $i$ (equivalently $n_P\in S$).
Since $R(m)$ is finite, $m\in S\iff R(m)$ is a transversal $\iff R(m)$ contains a minimal transversal (a
transversal no proper subset of which is a transversal). A minimal transversal is squarefree‑indexed by $n_P$,
and $R(m)\supseteq P\iff n_P\mid m$. Hence

$$\boxed{,S=\bigcup_{P\ \text{minimal transversal}} n_P,\mathbb Z.,}\tag{3}$$

The $n_P$ are exactly the divisibility‑minimal elements of $S$: if $q^2\mid n$ then $n/q$ has the same radical,
so $n/q\in S$; thus every minimal element is squarefree, its radical is a transversal that is minimal
(removing a prime removes a divisor, exiting $S$), and conversely.

If there are only finitely many minimal transversals, then $S$ is periodic: by $(3)$, membership $m\in S$
depends only on $m$ modulo $L:=\operatorname{lcm}{n_P}$, so $m\in S\iff m+L\in S$ for all $m\ge 1$. By Step 2
we are done.

Thus everything reduces to:

$$\textbf{Main Claim: } S \text{ has finitely many minimal elements.}$$

Step 4. Two properties of the minimal elements

Let $\mathcal N$ be the set of minimal elements (equivalently, the $n_P$). Write each as its prime set
$P=R(n_P)$.

(A) Saturation. For a finite prime set $K$, if $\prod K\notin S$ then there is a term $a_i$ with $\gcd(\prod K,
a_i)=1$, i.e. a term $a_i$ with $R(a_i)\cap K=\varnothing$. (This is just the definition of $S$.)

(B) The minimal elements pairwise intersect. Only finitely many $n_P$ are $<a_1$. If $n_P\ge a_1$ then $n_P\in
S\cap[a_1,\infty)$, so $n_P$ is a **term** by Step 2. For two terms $n_P,n_{P'}$, property $(1)$ gives
$\gcd(n_P,n_{P'})>1$, i.e. $P\cap P'\ne\varnothing$. Hence: any two minimal elements that are $\ge a_1$ have 
intersecting prime sets.

Step 5. Bounded rank (the key quantitative input)

Lemma (Bounded rank). Every minimal element $n\in\mathcal N$ has all of its proper divisors $<a_1$. 
Consequently $n$ has at most $1+\log_2 a_1$ distinct prime factors.

Proof of the corollary from the first statement. If $n=q_1q_2\cdots q_s$ (distinct primes, $q_1$ smallest) is
minimal, its largest proper divisor is $n/q_1=q_2\cdots q_s$. If this is $<a_1$ then $2^{,s-1}\le q_2\cdots
q_s<a_1$, so $s<1+\log_2a_1$. $\square$

$\qquad\blacksquare$

Consequence. If $S$ is periodic — i.e. there is $L\ge1$ with $m\in S\iff m+L\in S$ for all $m\ge1$ — then the
desired conclusion holds for every $n\ge 1$. Indeed, put $T=#\big(S\cap[a_1,a_1+L)\big)\ge1$ (nonempty as
$a_1\in S$). Periodicity gives, for every integer $x\ge a_1$, $x\in S\iff x+L\in S$; so the shift $x\mapsto
x+L$ is an order isomorphism $S\cap[a_1,\infty)\to S\cap[a_1+L,\infty)$. The set $S\cap[a_1+L,\infty)$ equals
$S\cap[a_1,\infty)$ with its first $T$ elements $a_1,\dots,a_T$ removed, i.e. equals ${a_{T+1},a_{T+2},\dots}$;
its $n$‑th element is $a_{T+n}$. On the other hand, being the image of the shift, its $n$‑th element is
$a_n+L$. Therefore
$$a_{n+T}=a_n+L\qquad\text{for all } n\ge1.$$

So it suffices to prove that $S$ is periodic.

Step 3. Bounded gaps, and the structure of $S$

Every multiple of $M$ lies in $S$ (a multiple of $M=\prod R_1$ is divisible by each $p_j\in R_1$, and every
$a_i$ is divisible by some $p_j$, so shares that factor). Consequently the elements of $S\cap[a_1,\infty)$ have
gaps at most $M$:
$$a_{n+1}-a_n\le M\qquad\text{for all }n, \tag{2}$$
because the next multiple of $M$ above $a_n$ lies in $S$ and is $\le a_n+M$.

Call a finite set $P$ of primes a transversal if it meets $R(a_i)$ for every $i$ (equivalently $n_P\in S$).
Since $R(m)$ is finite, $m\in S\iff R(m)$ is a transversal $\iff R(m)$ contains a minimal transversal (a
transversal no proper subset of which is a transversal). A minimal transversal is squarefree‑indexed by $n_P$,
and $R(m)\supseteq P\iff n_P\mid m$. Hence

$$\boxed{,S=\bigcup_{P\ \text{minimal transversal}} n_P,\mathbb Z.,}\tag{3}$$

The $n_P$ are exactly the divisibility‑minimal elements of $S$: if $q^2\mid n$ then $n/q$ has the same radical,
so $n/q\in S$; thus every minimal element is squarefree, its radical is a transversal that is minimal
(removing a prime removes a divisor, exiting $S$), and conversely.

If there are only finitely many minimal transversals, then $S$ is periodic: by $(3)$, membership $m\in S$
depends only on $m$ modulo $L:=\operatorname{lcm}{n_P}$, so $m\in S\iff m+L\in S$ for all $m\ge 1$. By Step 2
we are done.

Thus everything reduces to:

$$\textbf{Main Claim: } S \text{ has finitely many minimal elements.}$$

This contradiction shows $d<a_1$, proving the Lemma. $\qquad\blacksquare$

(Remark: the mechanism is that a minimal element $n$ cannot have a "large" proper divisor $d\ge a_1$, for then 
the term‑multiples $p^t a_i$ produced above would fill the gap just below $n$, contradicting that $n$ is the 
immediate greedy successor. This was verified computationally for all starting values $a_1$ up to several 
thousand: the largest proper divisor of a minimal element never reaches $a_1$, the observed ratio staying below
$0.64$.)

Step 6. Finiteness of the minimal elements

Suppose, for contradiction, that $\mathcal N$ is infinite. By Step 4(B), the infinitely many $n_P\ge a_1$ are
terms whose prime sets $P$ form an infinite, pairwise‑intersecting antichain. By Step 5 all these $P$ have size
at most $r:=\lfloor 1+\log_2 a_1\rfloor$. Hence infinitely many of them share a common size $s\le r$
(pigeonhole).

Sunflower Lemma (bounded size, self‑contained). An infinite family of sets each of size $\le s$ contains an 
infinite sunflower: an infinite subfamily ${P_j}$ and a fixed "core" $K$ with $P_j\cap P_{j'}=K$ for all $j\ne 
j'$ (so the "petals" $P_j\setminus K$ are pairwise disjoint).

Proof (induction on $s$). For a family of finite sets, either (i) some element lies in infinitely many members,
or (ii) every element lies in finitely many, in which case one greedily extracts an infinite pairwise‑disjoint
$\qquad\blacksquare$

Consequence. If $S$ is periodic — i.e. there is $L\ge1$ with $m\in S\iff m+L\in S$ for all $m\ge1$ — then the
desired conclusion holds for every $n\ge 1$. Indeed, put $T=#\big(S\cap[a_1,a_1+L)\big)\ge1$ (nonempty as
$a_1\in S$). Periodicity gives, for every integer $x\ge a_1$, $x\in S\iff x+L\in S$; so the shift $x\mapsto
x+L$ is an order isomorphism $S\cap[a_1,\infty)\to S\cap[a_1+L,\infty)$. The set $S\cap[a_1+L,\infty)$ equals
$S\cap[a_1,\infty)$ with its first $T$ elements $a_1,\dots,a_T$ removed, i.e. equals ${a_{T+1},a_{T+2},\dots}$;
its $n$‑th element is $a_{T+n}$. On the other hand, being the image of the shift, its $n$‑th element is
$a_n+L$. Therefore
$$a_{n+T}=a_n+L\qquad\text{for all } n\ge1.$$

So it suffices to prove that $S$ is periodic.

Step 3. Bounded gaps, and the structure of $S$

Every multiple of $M$ lies in $S$ (a multiple of $M=\prod R_1$ is divisible by each $p_j\in R_1$, and every
$a_i$ is divisible by some $p_j$, so shares that factor). Consequently the elements of $S\cap[a_1,\infty)$ have
gaps at most $M$:
$$a_{n+1}-a_n\le M\qquad\text{for all }n, \tag{2}$$
because the next multiple of $M$ above $a_n$ lies in $S$ and is $\le a_n+M$.

Call a finite set $P$ of primes a transversal if it meets $R(a_i)$ for every $i$ (equivalently $n_P\in S$).
Since $R(m)$ is finite, $m\in S\iff R(m)$ is a transversal $\iff R(m)$ contains a minimal transversal (a
transversal no proper subset of which is a transversal). A minimal transversal is squarefree‑indexed by $n_P$,
and $R(m)\supseteq P\iff n_P\mid m$. Hence

$$\boxed{,S=\bigcup_{P\ \text{minimal transversal}} n_P,\mathbb Z.,}\tag{3}$$

The $n_P$ are exactly the divisibility‑minimal elements of $S$: if $q^2\mid n$ then $n/q$ has the same radical,
so $n/q\in S$; thus every minimal element is squarefree, its radical is a transversal that is minimal
(removing a prime removes a divisor, exiting $S$), and conversely.

If there are only finitely many minimal transversals, then $S$ is periodic: by $(3)$, membership $m\in S$
depends only on $m$ modulo $L:=\operatorname{lcm}{n_P}$, so $m\in S\iff m+L\in S$ for all $m\ge 1$. By Step 2
we are done.

Thus everything reduces to:

$$\textbf{Main Claim: } S \text{ has finitely many minimal elements.}$$

Step 4. Two properties of the minimal elements

Let $\mathcal N$ be the set of minimal elements (equivalently, the $n_P$). Write each as its prime set
$P=R(n_P)$.

(A) Saturation. For a finite prime set $K$, if $\prod K\notin S$ then there is a term $a_i$ with $\gcd(\prod K,
a_i)=1$, i.e. a term $a_i$ with $R(a_i)\cap K=\varnothing$. (This is just the definition of $S$.)

(B) The minimal elements pairwise intersect. Only finitely many $n_P$ are $<a_1$. If $n_P\ge a_1$ then $n_P\in
S\cap[a_1,\infty)$, so $n_P$ is a **term** by Step 2. For two terms $n_P,n_{P'}$, property $(1)$ gives
$\gcd(n_P,n_{P'})>1$, i.e. $P\cap P'\ne\varnothing$. Hence: any two minimal elements that are $\ge a_1$ have
intersecting prime sets.

Step 5. Bounded rank (the key quantitative input)

Lemma (Bounded rank). Every minimal element $n\in\mathcal N$ has all of its proper divisors $<a_1$.
Consequently $n$ has at most $1+\log_2 a_1$ distinct prime factors.

Proof of the corollary from the first statement. If $n=q_1q_2\cdots q_s$ (distinct primes, $q_1$ smallest) is
minimal, its largest proper divisor is $n/q_1=q_2\cdots q_s$. If this is $<a_1$ then $2^{,s-1}\le q_2\cdots
q_s<a_1$, so $s<1+\log_2a_1$. $\square$

Proof of the first statement. If $n<a_1$ all its divisors are $<a_1$. So let $n\ge a_1$; then $n$ is a term,
say $n=a_J$. It suffices to treat the largest proper divisor $d=n/p$, where $p$ is the smallest prime of $n$
(every proper divisor divides $d$). Suppose, for contradiction, $d\ge a_1$.

Since $d$ is a proper divisor of the minimal element $n$, we have $d\notin S$; and $d\ge a_1$, so $d$ is not a
term. Hence $d$ lies strictly between two consecutive terms. Because the greedy rule skipped $d$, $d$ fails the
acceptance test at that stage: there is a term $a_i$ preceding the position of $d$ (so $a_i<d$) with
$\gcd(d,a_i)=1$. Now $n=p\cdot d\in S$ meets $a_i$, and $\gcd(d,a_i)=1$, so $p\mid a_i$; thus
$$a_i<d,\qquad R(a_i)\cap R(n)={p}. \tag{4}$$

Consider the number $p,a_i$. Since $p\mid a_i$, we have $\operatorname{rad}(p,a_i)=\operatorname{rad}(a_i)$, so
$p,a_i\in S$; and $p,a_i\ge p,a_1\ge 2a_1>a_1$, so $p,a_i$ is a term. From $(4)$,
$\operatorname{rad}(p,a_i)=R(a_i)$ meets $R(n)$ only in ${p}$, so $p,a_i$ is coprime to $d=n/p$. Also $a_i<d$
gives $p,a_i<p,d=n$.

Now compare with the term immediately preceding $n=a_J$. By $(2)$, $a_{J-1}\ge n-M=pd-M$. Because $d\ge a_1\ge
M$ and $p\ge2$, we have $pd-M\ge pd-d=(p-1)d\ge d> a_i$, hence
$$a_i<a_{J-1}<n .$$
The interval $(a_{J-1},n)$ contains no element of $S$ (as $a_{J-1},a_J=n$ are consecutive terms, i.e.
consecutive elements of $S\cap[a_1,\infty)$).

Iterate the multiplication by $p$: the numbers $a_i,\ p,a_i,\ p^2a_i,\dots$ all have radical $R(a_i)$, hence
all lie in $S$, are all terms, and are all $\ge a_1$. Let $p^{t}a_i$ be the largest of them that is $<n$ (this
exists since $a_i<n$, and $p^{t+1}a_i\ge n$). Then $p^{t}a_i<n\le p^{t+1}a_i=p\cdot(p^{t}a_i)$, so
$$p^{t}a_i>\frac{n}{p}=d\ge a_1 .$$
Thus $p^{t}a_i\in S$ and $a_1\le d<p^{t}a_i<n$. If $p^{t}a_i>a_{J-1}$ we already have a contradiction (an
element of $S$ strictly between the consecutive terms $a_{J-1}$ and $n$). And indeed $p^{t}a_i>a_{J-1}$:
otherwise $p^{t}a_i\le a_{J-1}<n\le p^{t+1}a_i$, forcing $a_{J-1}\in[p^{t}a_i,,p^{t+1}a_i)$, whence
$a_{J-1}<p^{t+1}a_i=p\cdot p^{t}a_i$ while $n\le p^{t+1}a_i$ gives
$n-a_{J-1}<p^{t+1}a_i-p^{t}a_i=(p-1)p^{t}a_i$; but $p^{t}a_i>d\ge M$ and $p\ge 2$ make the right side $>M\ge
n-a_{J-1}$ by $(2)$ — no contradiction there, so we argue directly instead:

Take $t$ maximal with $p^{t}a_i<n$; then $p^{t}a_i \in (d,,n)$ as shown. Its successor multiple $p^{t+1}a_i\ge
n>a_{J-1}$. If $p^{t}a_i\le a_{J-1}$, then applying the same skipping argument to $p^{t}a_i$ is unnecessary;
instead note $p^{t}a_i$ is a term lying in $(a_{J-1},n)$ once $p^{t}a_i>a_{J-1}$. To guarantee this, choose $i$
to make $a_i$ as large as possible under $(4)$: among all terms satisfying $(4)$ pick the largest one below
$d$; call it $a_{i^\ast}$. The consecutive term above $a_{i^\ast}$ that is a $p$‑power multiple,
$p,a_{i^\ast}$, is a term $>a_{i^\ast}$; repeating, the largest $p$‑power multiple below $n$ is a term in
$(d,n)\subseteq (a_{J-1},n)$ unless it equals a term $\le a_{J-1}$, which is impossible since $(a_{J-1},n)\cap
S=\varnothing$ would then be violated by the next multiple. In every case we produce an element of $S$ in the
open interval $(a_{J-1},n)$, contradicting that $a_{J-1},n$ are consecutive terms.

This contradiction shows $d<a_1$, proving the Lemma. $\qquad\blacksquare$

(Remark: the mechanism is that a minimal element $n$ cannot have a "large" proper divisor $d\ge a_1$, for then
the term‑multiples $p^t a_i$ produced above would fill the gap just below $n$, contradicting that $n$ is the
immediate greedy successor. This was verified computationally for all starting values $a_1$ up to several
thousand: the largest proper divisor of a minimal element never reaches $a_1$, the observed ratio staying below
$0.64$.)

Step 6. Finiteness of the minimal elements

Suppose, for contradiction, that $\mathcal N$ is infinite. By Step 4(B), the infinitely many $n_P\ge a_1$ are
terms whose prime sets $P$ form an infinite, pairwise‑intersecting antichain. By Step 5 all these $P$ have size
at most $r:=\lfloor 1+\log_2 a_1\rfloor$. Hence infinitely many of them share a common size $s\le r$
(pigeonhole).

Sunflower Lemma (bounded size, self‑contained). An infinite family of sets each of size $\le s$ contains an
infinite sunflower: an infinite subfamily ${P_j}$ and a fixed "core" $K$ with $P_j\cap P_{j'}=K$ for all $j\ne
j'$ (so the "petals" $P_j\setminus K$ are pairwise disjoint).

Proof (induction on $s$). For a family of finite sets, either (i) some element lies in infinitely many members,
or (ii) every element lies in finitely many, in which case one greedily extracts an infinite pairwise‑disjoint
subfamily (each chosen member meets only finitely many others), a sunflower with $K=\varnothing$. For sizes
$\le s$: in case (i) restrict to the infinitely many members containing a fixed element $x$, delete $x$ to get
an infinite family of sets of size $\le s-1$, apply induction to obtain a sunflower with core $K'$, and
re‑insert $x$ to get core $K=K'\cup{x}$. Base $s=0$ is trivial. $\square$

Apply this to our infinitely many size‑$s$ prime sets, obtaining an infinite sunflower ${P_j}$ with core $K$
and pairwise‑disjoint nonempty petals $E_j=P_j\setminus K$. (The petals are nonempty: an antichain contains at
most one set equal to $K$; discard it. They are pairwise disjoint by the sunflower property.) Since the $P_j$
pairwise intersect (Step 4B) and their pairwise intersections all equal $K$, we get $K\neq\varnothing$.

Let $c=\prod_{p\in K}p$. As $K\subsetneq P_j$, $c$ is a proper divisor of the minimal element $n_{P_j}$, so
$c\notin S$. By Saturation (Step 4A) there is a term $\tau$ with
$$R(\tau)\cap K=\varnothing.$$
Now each $n_{P_j}$ is in $S$ and $\tau$ is a term, so $\gcd(n_{P_j},\tau)>1$, i.e. $R(\tau)\cap
P_j\ne\varnothing$. Since $R(\tau)\cap K=\varnothing$ and $P_j=K\sqcup E_j$, we must have
$$R(\tau)\cap E_j\neq\varnothing\qquad\text{for every } j.$$
The petals $E_j$ are pairwise disjoint and there are infinitely many of them, so $R(\tau)$ contains at least
one prime from each of infinitely many disjoint sets — i.e. $\tau$ has infinitely many prime factors. This is
absurd.

Therefore $\mathcal N$ is finite. $\qquad\blacksquare$

Conclusion

By Step 6, $S$ has finitely many minimal elements, so by $(3)$, $m\in S\iff n_P\mid m$ for one of finitely many
$n_P$; this depends only on $m$ modulo $L=\operatorname{lcm}{n_P}$. Hence
$$m\in S\iff m+L\in S\qquad\text{for all }m\ge1,$$
so $S$ is periodic with period $L$. By the Consequence in Step 2, with $T=#\big(S\cap[a_1,a_1+L)\big)\ge 1$, we
obtain positive integers $T,L$ with
$$a_{n+T}=a_n+L\qquad\text{for every positive integer } n.$$

$\blacksquare$

---
A remark on where each hypothesis is used. The value $a_1>1$ and the greedy "smallest larger" rule give (Step
2) that the sequence is exactly the increasing enumeration of the fixed, radical‑determined,
divisibility‑closed set $S$ — this is what turns "eventually periodic" into "periodic for all $n$." Property
$(1)$ (pairwise non‑coprimality) makes $S$'s minimal elements pairwise intersecting, and Saturation together
with the greedy‑minimality bound of Step 5 forbids the only obstruction to finiteness (an infinite sunflower),
via the fact that a single term has only finitely many prime factors.

Let me verify the final conclusion numerically once more across many starting values.

⏺ Bash(cd /private/tmp/claude-501/-Users-adibhasan-Downloads-projects-cc-imo-2026/a281ab24-d7a4-4f5f-87d9-ea04348
    d2dda/scratchpad
    cat << 'EOF' > final_check.py…)
⎿  a1=15: T=8 L=30  holds for ALL n>=1: True
    a1=105: T=58 L=210  holds for ALL n>=1: True
    a1=35: T=34 L=210  holds for ALL n>=1: True
    … +20 lines (ctrl+o to expand)

⏺ I've completed an extensive analysis and verification. Let me give you my honest assessment and the solution.

Summary of what I found

I worked on this for a long time, combining computational exploration (hundreds of starting values) with
theory. I found a clean and complete reduction of the problem, and I verified the full statement holds for all
tested cases. Here is the structure, with an honest flag on the one delicate step.

The complete, rigorous core of the solution:

1. All terms are pairwise non-coprime. For $i<j$, the definition of $a_j$ forces $\gcd(a_j,a_i)>1$.

2. The sequence is exactly the increasing enumeration of a fixed set. Let $S={m:\gcd(m,a_i)>1\ \forall i}$.
Because each $a_{n+1}$ is the least integer $>a_n$ in $A_n\supseteq S$, and $a_{n+1}\in S$ by step 1, one shows
$a_{n+1}=\min\big(S\cap(a_n,\infty)\big)$. Hence ${a_n}=S\cap[a_1,\infty)$ listed increasingly. This is why 
the conclusion holds for every $n$, not just eventually: if $S$ is periodic with period $L$ and
$T=#(S\cap[a_1,a_1+L))$, the order-isomorphism $x\mapsto x+L$ of $S\cap[a_1,\infty)$ gives $a_{n+T}=a_n+L$ for
all $n\ge1$.

3. Bounded gaps + structure. Every multiple of $M=\operatorname{rad}(a_1)$ lies in $S$, so gaps are $\le M$.
Writing minimal transversals $P$ (minimal prime-sets meeting every $R(a_i)$), $;S=\bigcup_P n_P\mathbb Z$. So 
$S$ is periodic ⟺ there are finitely many minimal transversals.

4. Finiteness via a sunflower argument (rigorous given bounded rank). The minimal transversals form a
pairwise-intersecting antichain (step 1), with the saturation property "$\prod K\notin S\Rightarrow$ some term
is coprime to $\prod K$." If there were infinitely many of a common size, the (self-contained, bounded-size)
Sunflower Lemma yields an infinite sunflower with nonempty core $K$ and disjoint nonempty petals $E_j$. Then
$\prod K\notin S$, so a term $\tau$ is coprime to $\prod K$; but $\tau$ must meet each $n_{P_j}\in S$, forcing
$R(\tau)$ to hit every one of the infinitely many disjoint petals — impossible for a single integer $\tau$.
This contradiction is airtight.

The one delicate step I could not fully close. To run the sunflower one needs the minimal elements to have
bounded rank (bounded number of prime factors), equivalently the empirical lemma "every proper divisor of a 
minimal element of $S$ is $<a_1$." I verified this exhaustively — for every starting value up to several
thousand, the largest proper divisor of a minimal element never reaches $a_1$ (observed ratio $\le 0.64$) — and
I verified the final theorem $a_{n+T}=a_n+L$ (holding from $n=1$) for a large sample. But my attempted greedy
proof of this bounded-rank lemma has a genuine gap: it tried to "fill the gap $(a_{J-1},a_J)$," which is
provably empty, so that route cannot work, and I did not find a correct replacement.

Honest conclusion

I did not reach a fully rigorous complete proof: everything reduces cleanly and correctly to "$S$ has finitely
many minimal elements," and the sunflower contradiction settles that given the bounded-rank lemma — but I could
not rigorously prove that lemma (only verify it exhaustively).

Per your instruction to present only a complete verified solution and to report outcomes faithfully, I should
not claim the finiteness step as proven when it isn't. The reduction (steps 1–3) and the sunflower mechanism
(step 4) are solid and, I believe, are the right framework; the missing piece is a correct arithmetic proof
that minimal elements of $S$ have bounded rank. If you'd like, I can keep working specifically on that lemma,
or write up the rigorous partial (reduction + conditional finiteness) in full detail.

✻ Cooked for 1h 48m 20s

※ recap: Goal: prove the greedy gcd sequence is eventually arithmetic-periodic. I reduced it rigorously to 
showing the acceptable set S has finitely many minimal elements, proven via a sunflower argument that needs a 
bounded-rank lemma I couldn't yet prove. Next: prove that bounded-rank lemma. (disable recaps in /config)