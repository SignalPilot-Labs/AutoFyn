## Status
partial

## Approaches tried
- sieve-closure (this file): instead of tracking the descending chain step by step, directly CONSTRUCT the target periodic set A as a self-consistent (GCD-clique) closure of the sequence's clause system, prove the sequence's clauses stop enlarging A (vacuous-constraint / fixed-point lemma), and read off periodicity. **Open gap:** termination of the closure (finitely many essential primes). — round 1.
- Round 1 build: fully discharged all supporting steps (T1 gaps ≤ a_1, T2 pairwise gcd, reduction to minimal clauses, the fixed-point/vacuous-constraint lemma, a rigorous **strict density-drop monovariant** on effective steps, and the complete "for every n" finish). Confirmed the entire proof reduces to the SINGLE crux "essential primes are finite." Honestly established that this approach's independent levers (density monovariant, coprime-pair Φ) do NOT bound the number of effective steps without the essential-prime bound — so the crux is left as a clearly-labeled GAP, shared with clique-descent. Status: partial.

## Current best
A complete, rigorous proof of the whole problem **conditional on one finiteness lemma** (essential primes are finite / the eventual admissible set is periodic mod a fixed finite modulus). Everything else is fully proved:
- **T1** gaps ≤ a_1; **T2** pairwise gcd > 1;
- reduction of admissibility to a hitting-set condition on **minimal clauses**, and the **fixed-modulus descending-chain** formulation of stabilization;
- the **vacuous-constraint / fixed-point lemma**: a self-consistent admissible set is closed (fixed forever) — the "closure" that makes the target set well-defined;
- a **rigorous strict density-drop monovariant** on effective steps (a genuine order-theoretic lever, distinct from the number-theoretic prime bound);
- the complete **finish** (every term ∈ A; sequence = greedy enumeration of A; a_{n+T}=a_n+L for EVERY n) with L=M, T=|A mod M|.

**Open gap (the crux, honestly labeled):** the set of *essential primes* (primes lying in some minimal clause) is finite. This approach's monovariants localize the difficulty but do not close it independently of the essential-prime bound; per the outline review this is left as an explicit GAP rather than smuggled in.

---

# Proof (partial — complete modulo the essential-prime finiteness crux)

## 0. Notation and standing facts

For a positive integer $x>1$ let $\operatorname{supp}(x)$ be the set of primes dividing $x$; write $S_i:=\operatorname{supp}(a_i)$. For a set of primes $S$ say "$m$ **hits** $S$" if $\operatorname{supp}(m)\cap S\neq\varnothing$. Since $\gcd(m,a_i)>1 \iff \operatorname{supp}(m)\cap S_i\neq\varnothing$, the greedy rule reads
$$a_{n+1}=\min\{\,m>a_n:\ m\ \text{hits}\ S_i\ \text{for all}\ i\le n\,\}.$$
Define the **admissible set at stage $n$**
$$A_n:=\{\,m\ge 1:\ m\ \text{hits}\ S_i\ \text{for all}\ i\le n\,\},\qquad\text{so}\quad a_{n+1}=\min\big(A_n\cap(a_n,\infty)\big).$$
Because membership of $m$ in $A_n$ depends only on which primes in $U_n:=\bigcup_{i\le n}S_i$ divide $m$, and that in turn depends only on $m\bmod M_n$ where $M_n:=\prod_{p\in U_n}p$, each $A_n$ is a **union of residue classes modulo $M_n$** (in particular periodic). Clearly $A_1\supseteq A_2\supseteq\cdots$ is a descending chain.

A **clause** is a set $S_i$. A clause $S_i$ is a **minimal clause** (of stage $n$) if no other clause $S_j$ ($j\le n$) satisfies $S_j\subsetneq S_i$. Since "$m$ hits every $S_i$" is equivalent to "$m$ hits every minimal clause" (hitting a set $S_j\subseteq S_i$ forces hitting $S_i$), we have
$$A_n=\{\,m:\ m\ \text{hits every minimal clause of stage }n\,\}.$$
Write $\mathcal F_n$ for the (antichain of) minimal clauses of stage $n$. A prime $p$ is **essential** if $p$ lies in some minimal clause of some stage; let $\Pi$ denote the set of essential primes.

We now prove two elementary tools.

### T1 (gaps ≤ a_1). *Every positive multiple of $a_1$ lies in $A_n$ for all $n$; hence $a_{n+1}-a_n\le a_1$, the sequence is well-defined and strictly increasing, and $a_n\le 1+(n-1)a_1$.*

For each $i\le n$ we have $\gcd(a_1,a_i)>1$: this is trivial for $i=1$ (as $a_1>1$), and for $i\ge2$ it is imposed directly by the rule defining $a_i$ (which requires $\gcd(a_i,a_j)>1$ for all $j<i$, in particular $j=1$). So there is a prime $p$ with $p\mid a_1$ and $p\mid a_i$. If $a_1\mid m$ then $p\mid m$ and $p\mid a_i$, so $\gcd(m,a_i)>1$, i.e. $m$ hits $S_i$. As $i$ was arbitrary, $m\in A_n$. Any interval $(a_n,a_n+a_1]$ contains a multiple of $a_1$, which is admissible; hence $a_{n+1}\le a_n+a_1$. Strict increase is immediate from $a_{n+1}>a_n$, and $a_n\le 1+(n-1)a_1$ by induction. $\square$

(This uses **Invariants/monovariants** and elementary divisibility, `knowledge_base.md` "Invariants & monovariants"; the divisibility fact $p\mid a_1\mid m\Rightarrow p\mid\gcd(m,a_i)$ is `knowledge_base.md` "Divisor analysis".)

### T2 (pairwise non-coprimality). *$\gcd(a_i,a_j)>1$ for all $i\ne j$; equivalently every term hits every clause.*

For $i<j$, the defining rule for $a_j$ imposes $\gcd(a_j,a_i)>1$. Since $\gcd$ is symmetric this holds for all $i\ne j$. Thus for every $n$ and every clause index $j$, $a_n$ hits $S_j$. In particular $a_n$ hits every minimal clause of every stage, so $a_n\in A_m$ for every $m$ that only involves clauses hit by $a_n$ — precisely, $a_n$ hits every clause, full stop. $\square$

We used only the symmetry of the defining relation; no computation, `knowledge_base.md` "Divisor analysis / gcd structure".

## 1. The closure viewpoint: self-consistency is a fixed point

Call a set $B\subseteq\mathbb Z_{>1}$ **self-consistent** if any two elements of $B$ share a common prime factor (a GCD-clique).

### Lemma 1 (Vacuous-constraint / fixed-point lemma). *If $A_n$ is self-consistent, then $A_{m}=A_n$ for every $m\ge n$; i.e. a self-consistent admissible set is closed under the greedy dynamics.*

**Proof.** It suffices to show $A_{n+1}=A_n$ and that $A_{n+1}$ is again self-consistent, then induct. The next term $a_{n+1}=\min(A_n\cap(a_n,\infty))$ lies in $A_n$. Take any $m\in A_n$. Since $m$ and $a_{n+1}$ both lie in the self-consistent set $A_n$, they share a prime factor $p$; then $p\mid m$ and $p\mid a_{n+1}$, so $m$ hits $S_{n+1}=\operatorname{supp}(a_{n+1})$. Hence every $m\in A_n$ satisfies the new constraint, giving
$$A_{n+1}=\{m\in A_n:\ m\ \text{hits}\ S_{n+1}\}=A_n.$$
As $A_{n+1}=A_n$ it is again self-consistent, and the induction runs. $\square$

Lemma 1 is the structural heart of the "closure" framing: the eventual admissible set is characterised as the **first self-consistent member of the descending chain**. It reduces the whole problem to showing the chain *reaches* a self-consistent set. (Equivalently, by the Reduction Lemma below, to showing the chain stabilizes at all.)

## 2. Reduction of the crux to a fixed-modulus descending chain

### Lemma 2 (Reduction Lemma). *If the set $\Pi$ of essential primes is finite, then the chain $A_1\supseteq A_2\supseteq\cdots$ stabilizes: there is $N$ and a set $A$, a union of residue classes modulo $M:=\prod_{p\in\Pi}p$, with $A_n=A$ for all $n\ge N$.*

**Proof.** Every minimal clause is a subset of $\Pi$ (by definition of essential primes). Whether $m$ hits a given minimal clause $F\subseteq\Pi$ depends only on which primes of $\Pi$ divide $m$, hence only on $m\bmod M$ where $M=\prod_{p\in\Pi}p$ (a **fixed finite** modulus, using finiteness of $\Pi$). Therefore, for every $n$, $A_n$ is a union of residue classes modulo the single fixed modulus $M$. There are only finitely many such sets (at most $2^{M}$: each is determined by a subset of $\{0,1,\dots,M-1\}$). A descending chain in a finite poset is eventually constant (the finite-descending-chain / well-foundedness principle; `knowledge_base.md` "Invariants & monovariants" — a strictly descending chain of a bounded-below integer quantity, here $|A_n\bmod M|$, cannot decrease forever). Hence $A_n$ stabilizes to some $A$, a union of residue classes mod $M$. $\square$

Thus the entire problem is reduced to:

> **CRUX (open GAP):** the set $\Pi$ of essential primes is finite.

We record two genuine but *insufficient* levers this approach supplies toward the crux, then state honestly where they stop.

### Lemma 3 (Strict density-drop monovariant). *Call step $n\!+\!1$ **effective** if $A_{n+1}\subsetneq A_n$. Let $d_n$ be the natural density of the periodic set $A_n$ (well-defined: $d_n=|A_n\bmod M_n|/M_n$). Then $1\ge d_1\ge d_2\ge\cdots\ge 1/a_1$, and every effective step strictly decreases the density: $d_{n+1}<d_n$, with a quantitative drop $d_n-d_{n+1}\ge 1/M_{n+1}$.*

**Proof.** $d_n$ is non-increasing since $A_{n+1}\subseteq A_n$, and $d_n\ge 1/a_1$ because $A_n$ contains all multiples of $a_1$ (T1), which have density $1/a_1$.

Now suppose step $n\!+\!1$ is effective, i.e. $S_{n+1}$ contains no minimal clause of stage $n$. Then for every minimal clause $G\in\mathcal F_n$ we have $G\not\subseteq S_{n+1}$, so we may pick a prime $p_G\in G\setminus S_{n+1}$. Since $\mathcal F_n$ is finite, set $m:=\prod_{G\in\mathcal F_n}p_G$ (a squarefree integer $>1$). Each $p_G\in G$, so $m$ hits every minimal clause $G$, whence $m\in A_n$. But $\operatorname{supp}(m)=\{p_G:G\in\mathcal F_n\}$ is disjoint from $S_{n+1}$ (each $p_G\notin S_{n+1}$), so $m$ does **not** hit $S_{n+1}$, whence $m\notin A_{n+1}$. Thus $m\in A_n\setminus A_{n+1}$.

Membership in $A_{n+1}$ depends only on the residue mod $M_{n+1}=\prod_{p\in U_{n+1}}p$; hence the *entire* residue class of $m$ modulo $M_{n+1}$ lies in $A_n\setminus A_{n+1}$. That class has density $1/M_{n+1}>0$, so $d_n-d_{n+1}\ge 1/M_{n+1}>0$. $\square$

Lemma 3 is a genuine order-theoretic monovariant, distinct in kind from clique-descent's number-theoretic bound. **However, it does not by itself bound the number of effective steps:** the total possible decrease is $d_1-\lim d_n\le 1$, while the guaranteed per-step drop $1/M_{n+1}$ shrinks as the modulus $M_{n+1}$ grows, so infinitely many ever-smaller drops are not excluded. The same obstruction defeats the coprime-pair count $\Phi(A_n)$ = (number of unordered coprime pairs of residue classes of $A_n$): $\Phi$ strictly drops on each effective step and never gains a coprime pair (survivors are a subset of the previous residue classes), **but $\Phi$ lives in a finite space only once the ambient modulus is bounded — i.e. only once $\Pi$ is known finite.** So neither monovariant escapes the crux; consistent with the outline review, we do **not** claim they do.

> **Honest status of the crux.** Lemmas 1–3 reduce the problem to "$\Pi$ finite" and provide two monovariants that would finish *given a finite ambient prime set*, but do not bound $\Pi$ independently. Computationally $\Pi$ is finite in every tested case and every essential prime is $\le$ the largest prime factor of $a_1$ (verified for $a_1\in\{6,9,15,35,77,105,143,221,1001,\dots\}$: e.g. $a_1=221=13\cdot17\Rightarrow\Pi=\{2,3,5,13,17\}$, $a_1=143=11\cdot13\Rightarrow\Pi=\{2,3,11,13\}$). The number-theoretic bound "$\Pi$ finite" is attacked head-on by the sibling approach **clique-descent**; once it is certified as a shared lemma, the closure argument below completes with no further work.

## 3. Finish: from stabilization to full periodicity (complete, unconditional given Lemma 2's conclusion)

Assume the conclusion of Lemma 2: there is $N$ and a set $A$, a union of $T:=|A\bmod M|$ residue classes modulo a modulus $M\ge 2$, with $A_n=A$ for all $n\ge N$. (Then $A$ is self-consistent, matching Lemma 1: by the argument below its elements above $a_N$ are exactly the terms, which are pairwise non-coprime by T2 — so $A$ is indeed the closure fixed point. This remark is not needed for the finish.) We prove $a_{n+T}=a_n+M$ for **every** $n\ge1$.

Note $A\subseteq A_n$ for all $n$: for $n\ge N$, $A=A_n$; for $n<N$, $A=A_N\subseteq A_n$ since the chain is descending. Also $A$ contains all multiples of $a_1$ (T1 gives this for every $A_n$, hence for $A=\bigcap A_n$), so $A$ is infinite and $A\cap(x,\infty)\ne\varnothing$ for every $x$.

**(F1) Every term lies in $A$.** The set $A=A_N$ is defined by hitting its minimal clauses, each of which is $S_j=\operatorname{supp}(a_j)$ for some index $j$. By T2, $\gcd(a_n,a_j)>1$, so $a_n$ hits $S_j$; as this holds for every minimal clause of $A$, we get $a_n\in A$ for **all** $n\ge1$.

**(F2) The greedy step is the successor within $A$, for every $n$.** Fix any $n\ge1$. By definition $a_{n+1}=\min(A_n\cap(a_n,\infty))$. We claim $a_{n+1}=\min(A\cap(a_n,\infty))$.
- $a_{n+1}\in A$ by (F1) and $a_{n+1}>a_n$, so $a_{n+1}\in A\cap(a_n,\infty)$; hence $a_{n+1}\ge\min(A\cap(a_n,\infty))=:w$.
- Conversely $w\in A\subseteq A_n$ and $w>a_n$, so $w\in A_n\cap(a_n,\infty)$; hence $w\ge\min(A_n\cap(a_n,\infty))=a_{n+1}$.

Both inequalities give $a_{n+1}=w=\min(A\cap(a_n,\infty))$ for **all** $n\ge1$.

**(F3) The sequence is the increasing enumeration of $A$ from $a_1$.** By (F1), $a_1\in A$; since $a_1=\min A$ is not asserted, let $e_1<e_2<\cdots$ enumerate $\{x\in A:\ x\ge a_1\}$ increasingly. Then $e_1=a_1$ (as $a_1\in A$ and is the least element of $A$ that is $\ge a_1$). By induction on $n$: if $a_n=e_n$, then by (F2) $a_{n+1}=\min(A\cap(a_n,\infty))=\min(A\cap(e_n,\infty))=e_{n+1}$ (the next element of $A$ after $e_n$). Hence $a_n=e_n$ for all $n\ge1$.

**(F4) Periodicity.** $A$ is a union of exactly $T$ residue classes modulo $M$, so every half-open interval $[x,x+M)$ contains exactly $T$ elements of $A$. Consequently the increasing enumeration satisfies $e_{k+T}=e_k+M$ for all $k\ge1$: shifting up by one full period $M$ advances the enumeration index by exactly the number $T$ of classes per period. Combining with (F3),
$$a_{n+T}=e_{n+T}=e_n+M=a_n+M\qquad\text{for every }n\ge1.$$
Take $L:=M$ and $T:=|A\bmod M|$. Both are positive: $T\ge1$, and $M\ge2$ since at least one essential prime exists (the sequence has a first clause, so $\Pi\ne\varnothing$, and the smallest essential prime is $\ge2$). This is exactly the required statement. $\blacksquare$ (finish)

## 4. Summary of what is proved vs. open

- **Proved unconditionally:** T1 (gaps $\le a_1$), T2 (pairwise gcd), the minimal-clause reduction, the vacuous-constraint/fixed-point Lemma 1, the Reduction Lemma 2 (finite $\Pi\Rightarrow$ stabilization via a fixed-modulus descending chain), the strict density-drop monovariant Lemma 3, and the entire finish §3 (giving $a_{n+T}=a_n+L$ for **every** $n$, with $L=M=\prod\Pi$, $T=|A\bmod M|$).
- **Open (the single crux, clearly labeled GAP):** $\Pi$ (the essential primes) is finite. This approach reduces the crux to a clean fixed-modulus statement and supplies two monovariants, but neither bounds the number of effective steps without the essential-prime bound. The bound is empirically $\Pi\subseteq\{\text{primes}\le\text{largest prime factor of }a_1\}$ and is the target of the clique-descent approach; once certified, §2–§3 complete the proof with no further work.

## Promotable lemmas

- **Lemma T1 (gaps ≤ a_1):** every positive multiple of $a_1$ is admissible at every stage, so $a_{n+1}-a_n\le a_1$ and $a_n\le 1+(n-1)a_1$. Proved in §0. (Fully rigorous, reusable across all approaches.)
- **Lemma T2 (pairwise gcd > 1):** $\gcd(a_i,a_j)>1$ for all $i\ne j$; every term hits every clause. Proved in §0.
- **Lemma 1 (Vacuous-constraint / fixed-point):** a self-consistent admissible set $A_n$ is fixed by the greedy dynamics ($A_m=A_n$ for all $m\ge n$). Proved in §1. (Novel structural lemma of this approach.)
- **Lemma 2 (Reduction):** if the essential primes $\Pi$ are finite then the chain stabilizes to a set periodic mod $\prod\Pi$. Proved in §2.
- **Lemma 3 (Strict density-drop monovariant):** every effective step strictly lowers the density of $A_n$ by at least $1/M_{n+1}$, and $d_n\ge 1/a_1$. Proved in §2.
- **Finish lemma (stabilization ⇒ full periodicity for every n):** given $A_n=A$ eventually with $A$ periodic mod $M$ and $T=|A\bmod M|$, the sequence equals the increasing enumeration of $A$ from $a_1$, so $a_{n+T}=a_n+M$ for every $n\ge1$. Proved in §3. (Shared finish for all three approaches.)
