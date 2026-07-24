# Approach: admissible-set-periodicity

## Status
solved

## Approaches tried
- (round 1, outline) static reformulation A = {x>1 : gcd(x,a_i)>1 ∀i}; enumerate A, prove A periodic mod ∏S for finite essential S — outline only, crux flagged.
- (round 1, build) Fully proved (a) enumeration, (b) bounded gaps + linear growth, (c) the **entire periodicity machine**: reduced the WHOLE problem, exactly from n=1, to a single self-contained statement **(HS): a finite set of primes hits every pair of terms**. Reduction airtight; certified into `lemmas/enumeration-and-bounded-gaps.md` and `lemmas/finite-hitting-set-periodicity.md`. Only (HS) left open. Round-1 counting/density (Σ1/p²) shown insufficient.
- (round 2, build) **Closed (HS)** by a non-counting greedy-minimality argument. Proved the **spine (SP): any two distinct terms share a prime ≤ a₁**, via a static "bad-has-a-move" bridge (★)/(G3), a compression witness (Step C), and a minimal-counterexample pair-descent on max(pair) (Step D). Hence S = {primes ≤ a₁} is a finite hitting set ⇒ (HS) ⇒ (by the certified machine) a_{n+T}=a_n+L for all n≥1. **Complete proof — Status solved.**

## Current best
Full proof below. The certified reduction (Lemmas 1–6) is reused verbatim; the new content (Steps A–E) proves (HS) with the explicit hitting set S = {primes ≤ a₁}, closing the last gap. No remaining gaps.

---

## Setup and notation

Fix the sequence $a_1<a_2<a_3<\cdots$ of the problem: all $a_i>1$, and for every $n\ge 1$,
$$a_{n+1}=\min\{x>a_n:\gcd(x,a_i)>1\ \text{for all }i\le n\}. \tag{Rule}$$
(The minimum exists — Lemma 3 exhibits an eligible $x$.) In particular the sequence is strictly increasing, so every term satisfies $a_n\ge a_1$.

For an integer $m>1$ write $\operatorname{supp}(m)$ for the set of primes dividing $m$. Two integers are **coprime** iff their supports are disjoint. Put
$$S_0=\operatorname{supp}(a_1),\qquad R=\operatorname{rad}(a_1)=\prod_{p\in S_0}p .$$
Call a prime **small** if $p\le a_1$ and **big** if $p>a_1$. Every prime dividing $a_1$ is small.

Define the **admissible set**
$$A=\{\,x\in\mathbb Z_{>1} : \gcd(x,a_i)>1\text{ for every }i\ge 1\,\}.$$
"Term" always means a member of the sequence.

We freely use the following three certified lemmas (proved in round 1, certified by the proof-reviewer; see `results/imo-2026-06/lemmas/enumeration-and-bounded-gaps.md`).

**Lemma 1 (pairwise non-coprimality; every term admissible).** For all $m\ne n$, $\gcd(a_m,a_n)>1$; hence every term $a_n\in A$.

**Lemma 2 (enumeration).** For every $n\ge1$, $a_{n+1}=\min\bigl(A\cap(a_n,\infty)\bigr)$; equivalently $A\cap[a_1,a_n]=\{a_1,\dots,a_n\}$. Thus $(a_n)$ is the strictly increasing enumeration of $A\cap[a_1,\infty)$, and no element of $A$ lies strictly between two consecutive terms.

**Lemma 3 (bounded gaps, linear growth).** Every integer multiple $m>1$ of $R$ lies in $A$; hence $a_{n+1}-a_n\le R$ for all $n$, and $a_1+(n-1)\le a_n\le a_1+(n-1)R$. In particular $a_n\to\infty$.

We also use the certified **periodicity machine** (see `results/imo-2026-06/lemmas/finite-hitting-set-periodicity.md`). Call a finite set of primes $S$ a **hitting set** if every pair of distinct terms has a common prime factor lying in $S$.

**Periodicity Machine (Lemmas 4–6, certified).** If $S$ is a finite hitting set and $L=\prod_{p\in S}p$, then with $T=|A\cap[a_1,a_1+L)|\ge 1$ one has
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge 1.$$
The machine accepts **any** finite hitting set $S$ (it need not be minimal).

Thus it remains only to produce **one** finite hitting set. We prove:

> **(HS).** $S=\{\text{primes }p\le a_1\}$ is a (finite) hitting set.

$S$ is finite because there are finitely many primes not exceeding the fixed integer $a_1$. So (HS) is equivalent to the spine statement

> **(SP).** Any two distinct terms have a common prime factor $\le a_1$ (a small common prime).

Steps A–D prove (SP); Step E assembles the theorem. Throughout, the only use of the greedy Rule beyond Lemmas 1–3 is the bridge (★)/(G3) in Step A.

---

## Step A — The bridge (★) and its corollary (G3)

**Lemma A (★).** For an integer $n\ge a_1$: $n$ is a term $\iff$ $\gcd(n,m)>1$ for every term $m<n$.

*Proof.* ($\Rightarrow$) If $n$ is a term, then for every term $m<n$ the two terms $m,n$ are distinct, so $\gcd(m,n)>1$ by Lemma 1.

($\Leftarrow$) Assume $\gcd(n,m)>1$ for every term $m<n$.

*Case $n=a_1$.* Then $n$ is a term. (There is no term smaller than $a_1$, so the hypothesis is vacuous; this case needs nothing further.)

*Case $n>a_1$.* By Lemma 3 the terms are strictly increasing to $\infty$, and $a_1<n$, so the set $\{k:a_k<n\}$ is nonempty and finite; let $j$ be its maximum. Then
$$a_j<n\le a_{j+1},$$
and the terms strictly below $n$ are exactly $a_1,\dots,a_j$ (strict monotonicity). The hypothesis therefore gives $\gcd(n,a_i)>1$ for all $i\le j$. Hence $n$ is an eligible value in the Rule for $a_{j+1}$: $n>a_j$ and $\gcd(n,a_i)>1$ for all $i\le j$, so
$$a_{j+1}=\min\{x>a_j:\gcd(x,a_i)>1\ \forall i\le j\}\ \le\ n .$$
Combined with $n\le a_{j+1}$ from maximality of $j$, we get $a_{j+1}=n$; so $n$ is a term. $\square$

**Corollary G3.** If $x\ge a_1$ is **not** a term, then there is a term $b^*<x$ with $\gcd(b^*,x)=1$.

*Proof.* This is the contrapositive of the ($\Leftarrow$) direction of Lemma A. If, on the contrary, every term $m<x$ satisfied $\gcd(x,m)>1$, then by Lemma A (applicable since $x\ge a_1$) $x$ would be a term, contradicting the hypothesis. Hence some term $b^*<x$ has $\gcd(b^*,x)=1$. $\square$

---

## Step B — Every term has a small prime factor

**Lemma B.** Every term $b$ has a prime factor $\le a_1$.

*Proof.* If $b=a_1$, then any prime $p\mid a_1$ satisfies $p\le a_1$, and $a_1>1$ has such a prime. If $b\ne a_1$, then $b$ and $a_1$ are distinct terms, so by Lemma 1 $\gcd(b,a_1)>1$; a prime $p\mid\gcd(b,a_1)$ divides $b$ and divides $a_1$, whence $p\le a_1$. In either case $b$ has a small prime factor. $\square$

---

## Step C — The compression witness

**Lemma C.** For every term $b$ there is an integer $x$ with
$$\operatorname{supp}(x)=\{\text{small primes dividing }b\},\qquad a_1\le x\le b,$$
and $x$ has no big prime factor.

*Proof.* Let $\alpha=\prod\{p:p\text{ small},\ p\mid b\}$ be the product of the **distinct** small primes dividing $b$. By Lemma B this product is over a nonempty set, so $\alpha>1$; $\alpha$ is squarefree, $\operatorname{supp}(\alpha)=\{\text{small primes dividing }b\}$, and $\alpha\mid b$ (a product of distinct primes each dividing $b$ divides $b$), so $\alpha\le b$.

**Case 1: $b$ has no big prime factor.** Then every prime factor of $b$ is small, so $\operatorname{supp}(b)=\{\text{small primes dividing }b\}$. Take $x=b$. Then $\operatorname{supp}(x)=\operatorname{supp}(b)$ is exactly the set of small primes dividing $b$, $x$ has no big prime factor, and $a_1\le b=x\le b$. Done.

**Case 2: $b$ has a big prime factor $q$** (so $q>a_1$, $q\mid b$). Pick a small prime $p\mid b$ (Lemma B); then $p\mid\alpha$, so $p\le\alpha$. Let $N\ge0$ be the least integer with $p^{N}\alpha\ge a_1$, and set
$$x=p^{N}\alpha .$$
Since $\operatorname{supp}(x)=\{p\}\cup\operatorname{supp}(\alpha)=\operatorname{supp}(\alpha)$ (as $p\mid\alpha$), $x$ has support equal to the small primes dividing $b$ and no big prime factor. By choice of $N$, $x\ge a_1$. It remains to show $x\le b$; we split on $N$.

- **Subcase $N=0$.** Then $x=\alpha$, and $\alpha\mid b$ gives $x=\alpha\le b$.

- **Subcase $N\ge1$.** Minimality of $N$ gives $p^{N-1}\alpha<a_1$, hence
$$x=p\cdot p^{N-1}\alpha<p\,a_1 .$$
Now chain the following:
$$x<p\,a_1\ \overset{(p\le\alpha)}{\le}\ \alpha\,a_1\ \overset{(a_1<q)}{<}\ \alpha\,q\ \overset{(\alpha q\mid b)}{\le}\ b .$$
Here $p\le\alpha$ because $p\mid\alpha$ with $\alpha\ge p$; $a_1<q$ because $q$ is big; and $\alpha q\mid b$ because $\alpha$ is a product of distinct small primes dividing $b$ while $q$ is a big prime dividing $b$, so $q\notin\operatorname{supp}(\alpha)$ and $\alpha q$ is a product of distinct primes each dividing $b$, giving $\alpha q\mid b$ and $\alpha q\le b$. Thus $x<b$, so $x\le b$.

In every case $a_1\le x\le b$ with $\operatorname{supp}(x)=\{\text{small primes dividing }b\}$ and no big factor. $\square$

(This is the "bound a search by size" divisor argument of `knowledge_base.md`, "Divisor analysis / bounding by size".)

---

## Step D — The spine (SP) by minimal-counterexample descent

**Lemma D (SP).** Any two distinct terms have a common prime factor $\le a_1$.

*Proof.* Call an unordered pair $\{b,b'\}$ of **distinct** terms **violating** if $b$ and $b'$ have **no** common small prime factor (equivalently, no prime $\le a_1$ divides both). Suppose, for contradiction, that a violating pair exists.

The maxima $\max\{b,b'\}$ over violating pairs form a nonempty set of positive integers; by the well-ordering principle (`knowledge_base.md`, "extremal principle / minimal witness") choose a violating pair with $\max$ as small as possible. Write it $\{b,b'\}$ with $b<b'$ (the two are distinct, so one is larger); thus $\max=b'$ is minimal.

**(i)** By Lemma B, $b$ has a small prime factor $p$. Since $\{b,b'\}$ is violating and $p$ is a small prime dividing $b$, we have $p\nmid b'$.

**(ii)** Apply Lemma C to $b$: obtain $x$ with $\operatorname{supp}(x)=\{\text{small primes dividing }b\}$ and $a_1\le x\le b$. Every prime of $x$ is a small prime dividing $b$; none of these divides $b'$ (violating hypothesis). Hence $\operatorname{supp}(x)\cap\operatorname{supp}(b')=\emptyset$, i.e.
$$\gcd(x,b')=1 .$$

**(iii)** $x$ is **not** a term. Indeed, suppose $x$ were a term. Since $x\le b<b'$, $x\ne b'$, so $x$ and $b'$ would be two **distinct** terms with $\gcd(x,b')=1$, contradicting Lemma 1. Hence $x$ is not a term. As $x\ge a_1$ and $x$ is not a term, Corollary G3 yields a term $b^*<x$ with
$$\gcd(b^*,x)=1 .$$

**(iv)** We claim $\{b,b^*\}$ is a violating pair with $\max<b'$, contradicting minimality.

- $b^*<x\le b$, so $b^*<b$; in particular $b^*\ne b$, and $b^*,b$ are distinct terms. Also $\max\{b,b^*\}=b<b'$.
- $b$ and $b^*$ are distinct terms, so by Lemma 1 they **do** share some prime factor $r$; hence $\{b,b^*\}$ is a genuine pair with a common prime. We show every common prime of $b,b^*$ is big. Let $r\mid b$ and $r\mid b^*$ be a common prime, and suppose $r$ were small. Then $r$ is a small prime dividing $b$, so $r\in\operatorname{supp}(x)$, i.e. $r\mid x$. But $r\mid b^*$ and $\gcd(b^*,x)=1$ force $r\nmid x$ — a contradiction. Hence every common prime of $b,b^*$ is big; in particular $b,b^*$ share **no** small prime, so $\{b,b^*\}$ is violating.

Thus $\{b,b^*\}$ is a violating pair with $\max=b<b'$, contradicting the minimality of $b'$. This contradiction shows no violating pair exists: any two distinct terms share a small common prime. $\square$

---

## Step E — Conclusion

By Lemma D, any two distinct terms have a common prime factor $\le a_1$, i.e. a prime in the finite set $S=\{\text{primes }\le a_1\}$. Hence every pair of distinct terms has a common prime in $S$: $S$ is a **finite hitting set**, establishing (HS).

Feed $S$ into the certified Periodicity Machine with $L=\prod_{p\in S}p$ and $T=|A\cap[a_1,a_1+L)|\ge1$. The machine (which accepts any finite hitting set) yields
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge1 .$$
Since $T\ge1$ and $L=\prod_{p\le a_1}p\ge1$ are positive integers, this is exactly the required conclusion. $\blacksquare$

---

## Full proof

*(Self-contained; Lemmas 1–3 and the Periodicity Machine are the certified imports, restated in Setup above.)*

Fix the sequence and notation as in **Setup**. We must produce positive integers $T,L$ with $a_{n+T}=a_n+L$ for all $n\ge1$.

**1. Reduction to a finite hitting set.** By the certified **Periodicity Machine**, it suffices to exhibit one finite hitting set $S$ — a finite prime set such that every pair of distinct terms has a common prime factor in $S$. We claim $S=\{\text{primes }\le a_1\}$ works; it is finite. This claim is the spine **(SP)**: *any two distinct terms share a prime $\le a_1$.*

**2. The bridge (Step A).** *For $n\ge a_1$: $n$ is a term iff $\gcd(n,m)>1$ for every term $m<n$.* The forward direction is Lemma 1. For the converse with $n=a_1$, $n$ is a term outright. For $n>a_1$, let $j=\max\{k:a_k<n\}$ (finite, nonempty since $a_k\to\infty$); the terms below $n$ are exactly $a_1,\dots,a_j$, so the hypothesis gives $\gcd(n,a_i)>1$ for all $i\le j$, making $n$ eligible in the greedy Rule for $a_{j+1}$; thus $a_{j+1}\le n$, while maximality of $j$ gives $n\le a_{j+1}$, so $a_{j+1}=n$ is a term. **Corollary (G3):** if $x\ge a_1$ is not a term, then (contrapositive) some term $b^*<x$ has $\gcd(b^*,x)=1$.

**3. Small factor and compression (Steps B, C).**
*Lemma B:* every term $b$ has a small prime factor — from $b=a_1$ directly, or from $\gcd(b,a_1)>1$ (Lemma 1) whose common prime divides $a_1$ hence is $\le a_1$.
*Lemma C:* every term $b$ admits an integer $x$ with $\operatorname{supp}(x)=\{$small primes dividing $b\}$, no big factor, and $a_1\le x\le b$. Let $\alpha$ be the product of distinct small primes dividing $b$ (so $\alpha>1$ by Lemma B, squarefree, $\alpha\mid b$). If $b$ has no big prime factor, take $x=b$ (then $\operatorname{supp}(b)$ is all small and $a_1\le b\le b$). Otherwise pick a big prime $q\mid b$ and a small prime $p\mid b$ ($p\le\alpha$), and set $x=p^{N}\alpha$ with $N\ge0$ least so that $x\ge a_1$. If $N=0$, $x=\alpha\mid b$ so $x\le b$. If $N\ge1$, minimality gives $p^{N-1}\alpha<a_1$, whence $x=p\cdot p^{N-1}\alpha<p\,a_1\le\alpha a_1<\alpha q\le b$, using $p\le\alpha$, $a_1<q$, and $\alpha q\mid b$ (as $\alpha$ is squarefree over small primes of $b$ and $q\notin\operatorname{supp}\alpha$, so $\alpha q$ is a product of distinct primes dividing $b$). In all cases $a_1\le x\le b$ with $\operatorname{supp}(x)=\{$small primes of $b\}$.

**4. The spine by descent (Step D).** Suppose (SP) fails: some pair of distinct terms shares no small prime. Call such pairs *violating*; among them choose one $\{b,b'\}$, $b<b'$, with $b'$ (its max) minimal (well-ordering). By Lemma B pick a small prime $p\mid b$; violating $\Rightarrow p\nmid b'$. Take the compression $x$ of $b$ from Lemma C: all its primes are small primes of $b$, none dividing $b'$, so $\gcd(x,b')=1$, and $a_1\le x\le b<b'$. If $x$ were a term it would be a distinct term coprime to $b'$, contradicting Lemma 1; so $x$ is not a term, and by (G3) there is a term $b^*<x$ with $\gcd(b^*,x)=1$. Now $b^*<x\le b$, so $\max\{b,b^*\}=b<b'$; $b,b^*$ are distinct terms, hence share a prime $r$ (Lemma 1). If $r$ were small it would be a small prime dividing $b$, hence $r\mid x$, contradicting $\gcd(b^*,x)=1$ with $r\mid b^*$; so every common prime of $b,b^*$ is big, and $\{b,b^*\}$ is a violating pair with max $b<b'$ — contradicting minimality of $b'$. Hence no violating pair exists: **(SP) holds.**

**5. Assembly (Step E).** By (SP), every pair of distinct terms has a common prime $\le a_1$, so $S=\{\text{primes}\le a_1\}$ is a finite hitting set: **(HS)** holds. The certified Periodicity Machine, applied to this $S$ with $L=\prod_{p\le a_1}p$ and $T=|A\cap[a_1,a_1+L)|\ge1$, gives $a_{n+T}=a_n+L$ for every $n\ge1$. As $T,L\ge1$ are positive integers, the theorem is proved. $\blacksquare$

---

## Promotable lemmas

Proved in full this round; reusable by the sibling approaches (`profile-class-recruitment`, etc.), which share the spine:

- **Lemma A (bridge ★) and Corollary G3.** For $n\ge a_1$: $n$ is a term $\iff$ $\gcd(n,m)>1$ for every term $m<n$. Contrapositive (G3): every non-term $x\ge a_1$ has a smaller **term** $b^*<x$ with $\gcd(b^*,x)=1$. *Proved in Step A.* (This is the load-bearing greedy-minimality input — the only use of the Rule beyond Lemmas 1–3.)
- **Lemma B (small prime factor).** Every term has a prime factor $\le a_1$. *Proved in Step B.*
- **Lemma C (compression witness).** For every term $b$ there is an integer $x$ with $\operatorname{supp}(x)=\{$small primes dividing $b\}$, no big prime factor, and $a_1\le x\le b$. *Proved in Step C (both cases, both $N$-subcases).*
- **Lemma D (spine SP).** Any two distinct terms share a common prime factor $\le a_1$. *Proved in Step D.* Immediate corollary: **(HS)** — $S=\{\text{primes}\le a_1\}$ is a finite hitting set — which, with the already-certified Periodicity Machine, solves IMO 2026 P6 in full.
