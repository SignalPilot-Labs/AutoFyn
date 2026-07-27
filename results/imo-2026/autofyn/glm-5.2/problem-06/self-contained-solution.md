# IMO 2026 Problem 6 — Self-contained solution

> **Purpose of this document.** This is a single, fully self-contained proof of IMO 2026 Problem 6. Every lemma used in the argument is proved *inside* this document; there are no imports from `lemmas/*.md` or `approaches/*.md`. The only external reference is to the repo's generic theorem source `knowledge_base.md` (cited by name for results such as the Chinese Remainder Theorem), which is a reference catalogue, not a proof-step import. A reader who opens only this file can verify the whole proof.

---

## 1. Problem statement

Let $a_1,a_2,a_3,\ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that
$$\gcd(a_{n+1},a_i)>1\qquad\text{for every }i=1,2,\ldots,n.$$
Prove that there exist positive integers $T$ and $L$ such that
$$a_{n+T}=a_n+L\qquad\text{for every positive integer }n.$$

(The task is `proof_only`, `answer_type: none`; no numerical answer is demanded, but the constructive pair $(T,L)$ is exhibited explicitly in §7.)

---

## 2. Setup and the partial order

For an integer $m>1$ write
$$P(m)=\{p:\;p\text{ prime},\;p\mid m\}$$
for its set of prime divisors and $\mathrm{rad}(m)=\prod_{p\in P(m)}p$ for its radical (squarefree kernel). Note the equivalence
$$P(m)\subseteq P(n)\iff \mathrm{rad}(m)\mid\mathrm{rad}(n).$$

Define an **index-ordered radical partial order** on the terms of the sequence:
$$a_m\prec a_n \iff m<n\;\text{and}\;\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)\quad(\text{equivalently }P(a_m)\subseteq P(a_n),\;m<n).$$
A term $a_n$ is **$\prec$-minimal** if no earlier term $a_m$ (with $m<n$) satisfies $a_m\prec a_n$; equivalently, there is no $m<n$ with $P(a_m)\subseteq P(a_n)$.

The sequence is strictly increasing by definition ($a_{n+1}>a_n$), hence for indices $i,n$:
$$i<n\iff a_i<a_n.$$
This equivalence is used throughout (it is what lets "below $a_n$" be read as "with index $<n$"). The sequence is also unbounded: since each gap $a_{n+1}-a_n\ge 1$, we have $a_n\ge a_1+(n-1)\to\infty$.

Call a prime **large** if $p>a_1^2$, **small** otherwise. Set
$$P_0=\{p:\;p\text{ prime},\;p\le a_1^2\}$$
(finite). An integer is **$a_1^2$-smooth** if every prime dividing it is $\le a_1^2$, i.e. $P(\cdot)\subseteq P_0$.

Let
$$\mathcal F=\{P(a_i):i\ge 1\}$$
be the family of all term-supports, and let
$$\mathcal M=\min(\mathcal F)$$
be the family of its $\subseteq$-minimal elements (the *minimal-support family*). The eventual period conclusion is phrased around $\mathcal M$.

---

## 3. Lemma A (Piece A, unconditional) — the appears-criterion

> **Lemma A (Piece A, unconditional).** *For every integer $x\ge a_1$, the following are equivalent:*
> (i) *$x$ appears in the sequence (i.e. $x=a_n$ for some $n$);*
> (ii) *$\gcd(x,a_i)>1$ for every $i$ with $a_i<x$;*
> (iii) *$\gcd(x,a_i)>1$ for every $\prec$-minimal term $a_i$ with $a_i<x$.*

**This lemma uses no finiteness hypothesis of any kind.** In particular it does not invoke any of the lemmas of §6 (which are conditional on $\mathcal M$ being finite); invoking them here would be circular, since the finiteness of $\mathcal M$ is exactly what the descent of §4–§5 establishes.

**Proof of (i)$\iff$(ii).** The forward direction is immediate: if $x=a_n$, then $a_n$ was chosen admissible against $a_1,\ldots,a_{n-1}$, so $\gcd(a_n,a_i)>1$ for every $i<n$; and $a_i<x=a_n\iff i<n$ by strict increase.

For the backward direction, suppose $x\ge a_1$ satisfies $\gcd(x,a_i)>1$ for every $i$ with $a_i<x$; we show $x$ appears. Because the sequence is strictly increasing and unbounded and $a_1\le x$, there is a (unique) largest index $n$ with $a_n\le x$; then
$$a_n\le x<a_{n+1}.$$

If $a_n=x$, then $x$ already appears (as $a_n$) and we are done. So suppose, for contradiction, that $a_n<x$, i.e. $a_n<x<a_{n+1}$. We claim $x$ is admissible against $a_1,\ldots,a_n$: for every $i\le n$ we have $a_i\le a_n<x$ (strict increase gives $i\le n\Rightarrow a_i\le a_n$), so by hypothesis $\gcd(x,a_i)>1$. Hence $x$ is an admissible integer strictly greater than $a_n$. But $x<a_{n+1}$, contradicting the greedy choice of $a_{n+1}$ as the *smallest* admissible integer $>a_n$. Therefore $a_n=x$ was forced (the case $a_n<x$ is impossible), and $x$ appears. ∎ (of (i)$\iff$(ii))

**Proof of (ii)$\iff$(iii).** Since every $\prec$-minimal term is a term, (iii)$\Rightarrow$(ii) is immediate. For (ii)$\Rightarrow$(iii) we must show: validity of $x$ against every term below $x$ follows from validity against the $\prec$-minimal terms below $x$. Take any term $a_j<x$. If $a_j$ is $\prec$-minimal there is nothing to prove. Otherwise, by definition of $\prec$-minimal, there exists $m<j$ with $a_m\prec a_j$, i.e. $m<j$ and $P(a_m)\subseteq P(a_j)$. Iterating this (indices strictly decrease, so the iteration terminates), we obtain a chain
$$j=j_0>j_1>j_2>\cdots>j_t$$
with each $a_{j_{s+1}}\prec a_{j_s}$, terminating at a $\prec$-minimal $a_{j_t}$. The chain terminates because the indices are nonnegative integers strictly decreasing. Then
$$P(a_{j_t})\subseteq P(a_j)\quad\text{and}\quad a_{j_t}<a_j<x.$$
So if $\gcd(x,a_{j_t})>1$, pick a prime $s\mid\gcd(x,a_{j_t})$; then
$$s\in P(x)\cap P(a_{j_t})\subseteq P(x)\cap P(a_j),$$
so $s\mid\gcd(x,a_j)$, giving $\gcd(x,a_j)\ge s>1$. Hence validity against the $\prec$-minimal $a_{j_t}<x$ implies validity against $a_j$. ∎

This completes the proof of Lemma A. ∎

---

## 4. Lemma B (Direction B) — $\mathcal M$ lies in the supports of $\prec$-minimal terms

> **Lemma B (Direction B).** *Every $M\in\mathcal M$ is the support $P(a_i)$ of some $\prec$-minimal term $a_i$.*

**Proof.** Let $M\in\mathcal M$. Since $\mathcal M\subseteq\mathcal F$, $M$ is itself a term-support: $M=P(a_j)$ for some $j$. Let $i$ be the *smallest* index with $P(a_i)=M$ (well-defined: the set $\{j:P(a_j)=M\}$ is nonempty). We claim $a_i$ is $\prec$-minimal.

Suppose not: then some $m<i$ has $a_m\prec a_i$, i.e. $P(a_m)\subseteq P(a_i)=M$. Because $M\in\mathcal M$ is $\subseteq$-minimal in $\mathcal F$ and $P(a_m)\in\mathcal F$ with $P(a_m)\subseteq M$, we must have $P(a_m)=M$. But then $m<i$ also has support $M$, contradicting the minimality of $i$. So $a_i$ is $\prec$-minimal, with $P(a_i)=M$. ∎

> **Remark (Direction A is FALSE; not used).** The reverse inclusion — "every $\prec$-minimal support lies in $\mathcal M$" — is **false** in general. A later term can appear with a support *strictly smaller* than an earlier $\prec$-minimal term's support, demoting the latter's support out of $\mathcal M$. We do **not** attempt Direction A; the descent of §5 transfers its conclusion to $\mathcal M$ via Direction B alone.

---

## 5. Theorem (Large-prime descent) and the Corollary ($\mathcal M$ finite)

> **Theorem (Large-prime descent).** *If $a_n$ is divisible by a large prime $p>a_1^2$, then $a_n$ is **not** $\prec$-minimal.*

Equivalently (contrapositive): **every $\prec$-minimal term is $a_1^2$-smooth.**

**Proof by induction on $n$.** We use the induction hypothesis

> **(IH$_n$)** *Every $\prec$-minimal term $a_i$ with $i<n$ is $a_1^2$-smooth* (equivalently: no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime).

**Base case $n=1$.** There is no $\prec$-minimal term with $i<1$, so (IH$_1$) is vacuous. Moreover the conclusion of the theorem is vacuous for $n=1$ as well: if $p\mid a_1$ then $p\le a_1<a_1^2$ (since $a_1>1$, so $a_1^2>a_1$), so $a_1$ carries no large prime. Hence the implication "$a_1$ carries a large prime $\Rightarrow$ $a_1$ is not $\prec$-minimal" holds vacuously (the antecedent never holds). So the base case is sound.

**Inductive step.** Assume (IH$_n$) for some $n\ge 1$. Suppose $a_n$ is divisible by a large prime $p>a_1^2$. We must show $a_n$ is not $\prec$-minimal. The argument has four sub-steps; we discharge each rigorously. (For $n=1$ there is nothing to prove since $a_1$ carries no large prime, so assume $n>1$.)

**Step 5a — choose $q$ and locate $q^k c\in[a_1,a_n)$.** Write $a_n=p\,c$ with $p$ large. Because $a_n$ appears in the sequence, by Lemma A (with $x=a_n$), $\gcd(a_n,a_i)>1$ for every $\prec$-minimal $a_i<a_n$; in particular $\gcd(a_n,a_1)>1$ (note $a_1<a_n$ since the sequence is strictly increasing; for $n=1$ there is nothing to prove since $a_1$ carries no large prime). Pick any prime $q\mid\gcd(a_1,a_n)$. Then:
- $q\le a_1$, since $q\mid a_1$;
- $q\neq p$: indeed $p>a_1^2\ge a_1\ge q$ (the inequality $a_1^2\ge a_1$ uses $a_1\ge 2$; strictness $p>a_1^2$ is by "large"), so $p>q$, hence $p\neq q$;
- $q\mid c$: since $q\mid a_n=pc$ and $q\neq p$ (a prime), $q$ does not divide $p$, so $q\mid c$.

Consider the geometric chain $c,\,qc,\,q^2c,\,\ldots$. We claim some term of this chain lies in $[a_1,a_n)$. Because
$$\frac{a_n}{a_1}=\frac{pc}{a_1}\ge\frac{p}{a_1}>a_1\ge q,$$
where the strict inequality $p/a_1>a_1$ is exactly $p>a_1^2$ (the "large" threshold) and $a_1\ge q$ was established above. So $a_n/a_1>q$. Let $k$ be the smallest nonnegative integer with $q^k c\ge a_1$ (well-defined: $q^k c\to\infty$ as $k\to\infty$, so some $k$ qualifies). Then:
- $q^k c\ge a_1$ by choice of $k$;
- **if $k=0$**, then $c\ge a_1$, and we need $c<a_n$: since $a_n=pc$ and $p>1$, $c<a_n$ — so $c\in[a_1,a_n)$ and we may take $k=0$. (This corner case is consistent with the argument below; we keep $k$ general.)
- **if $k\ge 1$**, by minimality $q^{k-1}c<a_1$, hence
$$q^k c=q\cdot q^{k-1}c<q\cdot a_1\le a_1\cdot a_1=a_1^2<a_n,$$
where the last inequality $a_1^2<a_n$ is $a_1^2<pc$; since $p>a_1^2$ and $c\ge 1$, $pc\ge p>a_1^2$, and $a_n=pc>a_1^2$. So $q^k c\in[a_1,a_n)$.

In both cases $q^k c\in[a_1,a_n)$. This is the **landing sub-lemma**: a power of $q$ lifts $c$ into $[a_1,a_n)$. The load-bearing inequality is $a_n/a_1>q$, which is exactly $p>a_1^2$ — the threshold is tight.

**Step 5b — $q^k c$ appears, via Lemma A and (IH$_n$).** By Lemma A, to show $q^k c$ appears it suffices to show $\gcd(q^k c,a_i)>1$ for every $\prec$-minimal $a_i<q^k c$. Since $q^k c<a_n$, strict increase gives $a_i<q^k c<a_n\Rightarrow i<n$. By (IH$_n$), every $\prec$-minimal $a_i$ with $i<n$ is $a_1^2$-smooth, hence is **not** divisible by the large prime $p$ (which exceeds $a_1^2$); in particular $p\nmid a_i$.

Now $a_n$ appears after $a_i$ (as $i<n$), so by admissibility $\gcd(a_n,a_i)>1$; pick any prime $r\mid\gcd(a_n,a_i)$. Since $p\nmid a_i$ (just shown) while $p\mid a_n$, we have $r\neq p$. From $r\mid a_n=pc$ and $r\neq p$ (a prime), $r\mid c$, and hence $r\mid q^k c$ (as $q^k c$ is a multiple of $c$). Therefore
$$\gcd(q^k c,a_i)\ge r>1.$$
This holds for every $\prec$-minimal $a_i<q^k c$, so by Lemma A, $q^k c$ appears in the sequence. This is the **shared-prime transfer sub-lemma**: the large prime $p$ is invisible to $a_i$ (since $p\nmid a_i$ by IH), so every prime shared between $a_n$ and $a_i$ lies in $c$ and is inherited by $q^k c$.

**Step 5c — $q^k c$ appears strictly before $a_n$, and $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$.** Let $\mathrm{idx}(q^k c)$ denote the index with $a_{\mathrm{idx}(q^k c)}=q^k c$. Since $q^k c<a_n$ and the sequence is strictly increasing, $\mathrm{idx}(q^k c)<n$.

For the radical divisibility: $P(q^k c)=P(c)$, because $q\mid c$ (Step 5a), so multiplying $c$ by $q^k$ introduces no new prime. And $P(a_n)=P(pc)=P(c)\cup\{p\}$. Hence $P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$, i.e.
$$\mathrm{rad}(q^k c)=\mathrm{rad}(c)\mid\mathrm{rad}(pc)=\mathrm{rad}(a_n).$$
This is the **rad-divisibility sub-lemma**: $q\mid c$ is what makes it work (multiplying by $q^k$ adds no new prime), and $q\mid c$ followed from $q\neq p$ and $q\mid a_n=pc$.

**Step 5d — conclude $a_n$ is not $\prec$-minimal.** Combining Steps 5b–5c: $\mathrm{idx}(q^k c)<n$ and $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$, i.e. $\mathrm{idx}(q^k c)<n$ and $P(a_{\mathrm{idx}(q^k c)})\subseteq P(a_n)$. By definition of $\prec$ this says
$$a_{\mathrm{idx}(q^k c)}\prec a_n.$$
So there exists an earlier term ($a_{\mathrm{idx}(q^k c)}$, with index $<n$) subsuming $a_n$ rad-wise; $a_n$ is **not** $\prec$-minimal.

**Closing the induction.** We have shown: under (IH$_n$), if $a_n$ carries a large prime then $a_n$ is not $\prec$-minimal. Contrapositively, if $a_n$ *is* $\prec$-minimal, then $a_n$ carries no large prime, i.e. $a_n$ is $a_1^2$-smooth. Hence (IH$_{n+1}$) holds: every $\prec$-minimal term $a_i$ with $i<n+1$ (i.e. $i\le n$) is $a_1^2$-smooth — the terms with $i<n$ by (IH$_n$), the term $i=n$ (if $\prec$-minimal) by what we just proved. The induction proceeds. ∎

> **Corollary (the wall is closed: $\mathcal M$ is finite).** *Every member $M\in\mathcal M$ is a subset of $P_0=\{p:p\le a_1^2\}$; equivalently $P_{\mathrm{ess}}:=\bigcup\mathcal M\subseteq P_0$ is finite, and $\mathcal M\subseteq 2^{P_0}$ is finite.*

**Proof.** By the Large-prime descent (Theorem of this section), every $\prec$-minimal term is $a_1^2$-smooth. By Lemma B (Direction B), every $M\in\mathcal M$ is the support $P(a_i)$ of some $\prec$-minimal term $a_i$; since $a_i$ is $a_1^2$-smooth, $M=P(a_i)\subseteq P_0$. Hence $\bigcup\mathcal M\subseteq P_0$, which is a finite set of primes. Consequently $\mathcal M\subseteq 2^{P_0}$, a finite power set, so $\mathcal M$ is finite. ∎

This closes the stabilization wall: the minimal-support family $\mathcal M=\min\{P(a_i):i\ge 1\}$ is finite.

---

## 6. The Finish — proved in full (no imports)

From this point on we use *only* the finiteness of $\mathcal M$ (Corollary of §5). All lemmas below are proved inside this document. Set
$$P=\bigcup\mathcal M,\qquad L=\prod_{p\in P}p\;(\text{squarefree by construction}),$$
and
$$V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ is a transversal (hitting set) of }\mathcal M\}.$$
(Here a set $S\subseteq P$ is a *transversal* of $\mathcal M$ if $S\cap M'\neq\emptyset$ for every $M'\in\mathcal M$.) Note $0\in V$: every prime divides $0$, so $\{p\in P:p\mid 0\}=P$ meets every $M'\subseteq P$, i.e. $P$ is a transversal. Hence $V$ is nonempty. Since $L$ is finite, $V\subseteq\{0,\ldots,L-1\}$ is finite.

### 6.1 Lemma (Pairwise intersection, unconditional)

> **Lemma (Pairwise intersection).** *For all $i,j\ge 1$, $P(a_i)\cap P(a_j)\neq\emptyset$. In particular the family $\{P(a_i):i\ge 1\}$ is pairwise intersecting, and every $a_n$'s support hits every member of $\mathcal M=\min\{P(a_i):i\ge 1\}$.*

**This lemma is unconditional — no finiteness hypothesis.**

**Proof.** Take $i\ne j$, WLOG $i<j$. When $a_j$ was chosen, the rule required $\gcd(a_j,a_i)>1$ (as $i\le j-1$), i.e. $P(a_j)\cap P(a_i)\neq\emptyset$. The case $i=j$ is trivial: $P(a_i)\cap P(a_i)=P(a_i)\neq\emptyset$ since $a_i>1$. Each $M'\in\mathcal M$ equals $P(a_j)$ for some $j$ (minimal elements are members of the family $\mathcal F$), so $P(a_n)\cap M'=P(a_n)\cap P(a_j)\neq\emptyset$. ∎

### 6.2 Lemma (Transversal residue characterization)

> **Lemma (Transversal residue characterization).** *Assume $\mathcal M$ is finite. With $P,L,V$ as above, an integer $m>1$ satisfies $\gcd(m,a_i)>1$ for every $i\ge 1$ if and only if $m\bmod L\in V$. In particular, admissibility against the entire past depends only on $m\bmod L$; primes $q\mid m$ with $q\notin P$ ("free-riders") are invisible to the hitting condition.*

**Proof.** We chain equivalences:
$$\gcd(m,a_i)>1\ \forall i\iff P(m)\cap P(a_i)\neq\emptyset\ \forall i\iff P(m)\text{ is a transversal of }\mathcal F.$$
The last phrase means $P(m)$ meets every member of $\mathcal F$. This is equivalent to $P(m)$ being a transversal of $\mathcal M=\min\mathcal F$: a set hits every member of $\mathcal F$ iff it hits every *minimal* member (every non-minimal member of $\mathcal F$ contains a minimal one, so hitting the minimal one hits it).

Since each $M'\in\mathcal M$ lies in $2^P$ (as $\bigcup\mathcal M=P$),
$$P(m)\cap M'=(P(m)\cap P)\cap M'=\{p\in P:p\mid m\}\cap M'.$$
A prime $q\mid m$ with $q\notin P$ lies in no $M'$, so it cannot help hit anything; transversality of $P(m)$ over $\mathcal M$ depends only on $\{p\in P:p\mid m\}$.

Now invoke the **Chinese Remainder Theorem** (knowledge_base.md, "Number Theory — Modular arithmetic, CRT": solve/count solutions mod $n$ by factoring $n=\prod p_i^{e_i}$ and combining residues; here $L$ is squarefree, so $e_i=1$ for each prime factor). By CRT, the map
$$\mathbb Z/L\mathbb Z\;\xrightarrow{\;\sim\;}\;\prod_{p\in P}\mathbb Z/p\mathbb Z,\qquad r\bmod L\;\mapsto\;(r\bmod p)_{p\in P}$$
is a ring isomorphism, and the condition $p\mid m$ depends only on $m\bmod p$. Hence the whole set $\{p\in P:p\mid m\}$ depends only on $m\bmod L$. Therefore transversality of $P(m)$ over $\mathcal M$ depends only on $m\bmod L$, which is exactly the condition $m\bmod L\in V$. ∎

### 6.3 Lemma (Universal membership / no transient)

> **Lemma (Universal membership / no transient).** *Assume $\mathcal M$ is finite. With $P,L,V$ as above, for every $n\ge 1$, $a_n\bmod L\in V$; equivalently $P(a_n)$ is a transversal of $\mathcal M$. (No transient: the cyclic dynamics below hold from $n=1$.)*

**Proof.** Fix $M'\in\mathcal M$. Since $M'$ is minimal in $\mathcal F=\{P(a_i):i\ge 1\}$, it is a member of $\mathcal F$: $M'=P(a_j)$ for some $j\ge 1$. We use a trichotomy on $j$ vs $n$:

- **$j<n$:** $a_n$ was chosen admissible against $a_1,\ldots,a_{n-1}\ni a_j$, so $\gcd(a_n,a_j)>1$, i.e. $P(a_n)\cap M'\neq\emptyset$.
- **$j>n$:** $a_j$ was chosen admissible against $a_1,\ldots,a_{j-1}\ni a_n$, so $\gcd(a_j,a_n)>1$, i.e. $M'\cap P(a_n)\neq\emptyset$.
- **$j=n$:** $P(a_n)\cap M'=P(a_n)\neq\emptyset$ (as $a_n>1$).

In all three cases $P(a_n)\cap M'\neq\emptyset$. This holds for every $M'\in\mathcal M$, so $P(a_n)$ is a transversal of $\mathcal M$. (Equivalently, by the pairwise-intersection lemma of §6.1, $P(a_n)$ meets every $P(a_j)$, hence every $M'\in\mathcal M$ since each $M'$ is some $P(a_j)$.) By the transversal residue characterization of §6.2, $a_n\bmod L\in V$. ∎

### 6.4 Lemma (Greedy = cyclic successor)

> **Lemma (Greedy = cyclic successor).** *Assume $\mathcal M$ is finite. With $P,L,V$ as above, let $\varphi:V\to V$ be the cyclic successor: $\varphi(r)=\min\{v\in V:v>r\}$ if nonempty, else $\min V$ (wrap). Then for every $n\ge 1$,*
> $$a_{n+1}=\min\{m>a_n:m\bmod L\in V\},\qquad r_{n+1}=\varphi(r_n),$$
> *where $r_n=a_n\bmod L\in V$. Corollary: $a_{n+1}-a_n\le L$ (the next multiple of $L$ above $a_n$ has residue $0\in V$).*

**Proof.** Let $V_n=\{m:P(m)\text{ hits }\mathcal M_n\}$, where $\mathcal M_n=\min\{P(a_i):1\le i\le n\}$ is the time-$n$ minimal-support family; by the greedy rule (Lemma A applied at time $n$),
$$a_{n+1}=\min\{m\in V_n:m>a_n\}.$$
(Indeed at time $n$, a candidate $m>a_n$ is admissible iff $P(m)$ hits every $P(a_i)$, $i\le n$, iff $P(m)$ hits the $\subseteq$-minimal members $\mathcal M_n$ of $\{P(a_i):i\le n\}$; this is the time-$n$ analogue of the transversal characterization, with $L$ replaced by the time-$n$ analogue — but the *set* $V_n$ is what matters, and the greedy rule is the source of truth.)

We prove two containments.

- **$V\subseteq V_n$ (final minimal family is coarser than the time-$n$ one):** Take $M'\in\mathcal M_n$. In the full family $\mathcal F$, either $M'$ stays minimal (so $M'\in\mathcal M$; a $V$-element, which hits $\mathcal M$, hits $M'$), or some $M\in\mathcal M$ has $M\subsetneq M'$ (a member of $\mathcal M$ strictly contained in $M'$); a $V$-element, which hits $M$, then also hits $M'\supsetneq M$. In either case hitting $\mathcal M$ implies hitting $M'$, so $V\subseteq V_n$. Hence
$$\min(V_n\cap(a_n,\infty))\le\min(V\cap(a_n,\infty)),$$
i.e.
$$a_{n+1}\le\min\{m>a_n:m\bmod L\in V\}.$$

- **Lower bound (universal membership):** By the universal-membership lemma of §6.3, $a_{n+1}\bmod L\in V$ and $a_{n+1}>a_n$, so $a_{n+1}$ is itself a member of $\{m>a_n:m\bmod L\in V\}$, giving
$$a_{n+1}\ge\min\{m>a_n:m\bmod L\in V\}.$$

Combining the two inequalities yields equality:
$$a_{n+1}=\min\{m>a_n:m\bmod L\in V\}.$$
The smallest $m>a_n$ with $m\bmod L\in V$ is, by the CRT decomposition of $V$ into residue classes, the cyclic successor of $r_n=a_n\bmod L$ in the natural cyclic order on $V$: the next $V$-element in the current block $\{a_n-a_n\bmod L+1,\ldots,a_n-a_n\bmod L+L\}$, or, if there is none larger than $r_n$ in this block, the wrap to $\min V$ in the next block (which is $0$ residues ahead, i.e. exactly $L$ minus the current offset). Thus $r_{n+1}=\varphi(r_n)$.

**Corollary ($a_{n+1}-a_n\le L$).** The next multiple of $L$ strictly above $a_n$ has residue $0\in V$; it is admissible in the $V$-sense, so the *smallest* admissible integer $>a_n$ is at most this next multiple, which is within $L$ of $a_n$. ∎

### 6.5 Lemma (Cyclic successor is a single cycle, period-sum $L$)

> **Lemma (Cyclic successor is a single cycle, period-sum $L$).** *Assume $\mathcal M$ is finite. With $V\subseteq\{0,\ldots,L-1\}$ finite nonempty and $\varphi$ the cyclic successor, list $V=\{v_0<v_1<\cdots<v_{k-1}\}$ with $v_0=0$, $k=|V|$. Then $\varphi$ is a **single $k$-cycle** visiting every element of $V$:*
> $$\varphi(v_i)=v_{i+1}\;(i<k-1),\qquad \varphi(v_{k-1})=v_0.$$
> *The sum of increments over one full period is exactly $L$:*
> $$\sum_{i=0}^{k-1}\bigl[(\varphi(v_i)-v_i)\bmod L\bigr]=L.$$

**Proof.** By the definition of $\varphi$ as the cyclic successor, it walks $V$ in increasing cyclic order:
$$v_0\to v_1\to\cdots\to v_{k-1}\to v_0,$$
which is a single cycle of length $k$ visiting every element of $V$ (every element has a unique successor, the cycle closes at $v_{k-1}\to v_0$ since $v_0=0=\min V$ is the wrap target). The increments telescope:
$$(v_1-v_0)+(v_2-v_1)+\cdots+(v_{k-1}-v_{k-2})+(L-v_{k-1}+v_0)=L,$$
using $v_0=0$; the middle terms cancel, leaving $v_{k-1}+(L-v_{k-1})=L$. ∎

### 6.6 Conclusion of the Finish

We now combine the lemmas of §6.1–§6.5.

By the **universal-membership lemma** (§6.3), for every $n\ge 1$,
$$a_n\bmod L\in V$$
— so the cyclic dynamics hold from $n=1$ (no transient).

By the **greedy-equals-cyclic-successor lemma** (§6.4), the residue $r_n=a_n\bmod L$ evolves by
$$r_{n+1}=\varphi(r_n),$$
where $\varphi$ is the cyclic successor on $V$.

By the **cyclic-successor-single-cycle lemma** (§6.5), $\varphi$ is a single $|V|$-cycle and the sum of increments over one full period equals $L$. Hence, writing $T=|V|$, after $T$ applications of $\varphi$ the residue returns to its starting value, and the total integer increment is $L$:
$$r_{n+T}=r_n,\qquad a_{n+T}-a_n=L,\qquad\text{for every }n\ge 1.$$
(The first equality is the single-cycle property; the second is the period-sum $L$. Together they give $a_{n+T}=a_n+L$.)

Therefore, with the **constructive pair**
$$T=|V|,\qquad L=\prod_{p\in\bigcup\mathcal M}p\;(\text{squarefree}),$$
we have
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge 1.$$

This completes the proof. ∎

---

## 7. Numerical sanity checks (confirmations, not proof steps)

The proofs above stand on their own; the following computations merely confirm them.

- **$a_1=15=3\cdot 5$.** The sequence begins $15,18,20,24,30,36,40,42,45,\ldots$ The minimal-support family is
$$\mathcal M=\bigl\{\{2,3\},\{2,5\},\{3,5\}\bigr\},\qquad P=\{2,3,5\},\quad L=2\cdot3\cdot5=30,$$
$$V=\{0,6,10,12,15,18,20,24\},\quad T=|V|=8.$$
The descent's corollary ($\mathcal M\subseteq 2^{\{p\le 15^2=225\}}$) holds (every prime in $\mathcal M$ is $\le 5\le 225$). The Finish delivers $a_{n+8}=a_n+30$, matching the known sequence.

- **$a_1=429=3\cdot 11\cdot 13$.** Computation gives $T=908$, $L=4290$; the period $a_{n+908}=a_n+4290$ holds for all $n\ge 1$.

- **$a_1=30=2\cdot 3\cdot 5$.** Computation gives $T=1$, $L=2$; the sequence is eventually an arithmetic progression of common difference $2$.

In all three cases the period $a_{n+T}=a_n+L$ is confirmed to hold for all $n\ge 1$ (no transient), consistent with the universal-membership lemma of §6.3. These checks confirm but are not proof steps.

---

## Summary of theorems invoked

- **Lemma A (Piece A, §3)** — unconditional "appears $\iff$ valid against $\prec$-minimals below $x$"; elementary no-skip greedy + $\prec$-minimal chain reduction; no finiteness.
- **Lemma B (Direction B, §4)** — $\mathcal M\subseteq\{$ $\prec$-minimal supports $\}$; first-appearance argument. Direction A noted false and unused.
- **Large-prime descent (Theorem, §5)** — induction on $n$; large prime $p\mid a_n\Rightarrow a_n$ not $\prec$-minimal; sub-lemmas: landing ($q^k c\in[a_1,a_n)$ via $a_n/a_1>q$), index-descent ($q^k c<a_n\Rightarrow\mathrm{idx}<n$), shared-prime transfer ($r\neq p$ via IH $\Rightarrow r\mid c\mid q^k c$), rad-divisibility ($q\mid c\Rightarrow P(q^k c)=P(c)\subseteq P(a_n)$).
- **Corollary (§5)** — $\mathcal M\subseteq 2^{\{p\le a_1^2\}}$ finite.
- **Pairwise-intersection lemma (§6.1)** — unconditional; from the greedy rule.
- **Transversal residue characterization (§6.2)** — admissibility against the entire past depends only on $m\bmod L$; uses **CRT** (knowledge_base.md, "Number Theory — Modular arithmetic, CRT").
- **Universal membership / no transient (§6.3)** — every $a_n\bmod L\in V$; trichotomy on $j$ vs $n$; the pairwise-intersection fact.
- **Greedy = cyclic successor (§6.4)** — $a_{n+1}=\min\{m>a_n:m\bmod L\in V\}$, $r_{n+1}=\varphi(r_n)$; both containments proved.
- **Cyclic successor is a single cycle, period-sum $L$ (§6.5)** — $\varphi$ one $|V|$-cycle; increments telescope to $L$.

No regime split; no analytic estimates; no Dickson/Bertrand; the descent is uniform and elementary. The composition is non-circular: the descent of §5 establishes $\mathcal M$ finite using only the unconditional Lemma A (not the conditional lemmas of §6); the conditional lemmas of §6 then deliver the period.

The proof is complete: every case covered (the induction's base and step; the chain-termination in Lemma A's (ii)$\Rightarrow$(iii); the $k=0$ corner of the landing; the trichotomy in universal membership), every lemma proved in full inside this document, every invoked theorem named and located (CRT cited to `knowledge_base.md`), and (the problem being `answer_type: none`, `proof_only`) no numerical final answer is required — the constructive pair $(T,L)=(|V|,\prod_{p\in\bigcup\mathcal M}p)$ is explicitly exhibited in §6.6. ∎
