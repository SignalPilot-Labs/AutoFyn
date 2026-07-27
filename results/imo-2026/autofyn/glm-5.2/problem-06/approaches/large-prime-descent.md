# IMO 2026 Problem 6 — approach `large-prime-descent`

**Problem.** Let $a_1,a_2,\ldots$ be an infinite sequence of integers $>1$ such that for every $n\ge 1$, $a_{n+1}$ is the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every $i=1,\ldots,n$. Prove there exist positive integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge 1$.

**Framing of this approach.** We reproduce the published IMO 2026 P6 solution (Evan Chen's notes, 2026-07-23). The proof has three pieces:
- **Piece A** (an unconditional elementary lemma): "$x\ge a_1$ appears $\iff$ $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$." Proved inline from the greedy rule; **no finiteness hypothesis** (this addresses the reviewer's circularity concern C1).
- **Piece B** (the large-prime descent — the new wall-closer): every $\prec$-minimal term is $a_1^2$-smooth, by induction on $n$.
- **Piece C** (imported from δ): once the minimal-support family $\mathcal M$ is finite, the certified `post-stabilization-theorem` delivers $a_{n+T}=a_n+L$.

Only Pieces A and B are proved here; Piece C is imported (cite, do not re-prove).

---

## Status
solved

## Approaches tried
- `large-prime-descent` (round 130) — Built the published solution end-to-end. Piece A proved unconditionally (no-skip greedy + $\prec$-minimal reduction; no finiteness, no circularity). Direction B ($\mathcal M\subseteq\{$$\prec$-minimal supports$\}$) proved; Direction A explicitly noted false and unused (C2). Crux 1 (large-prime descent) proved by induction on $n$ with the four load-bearing sub-lemmas (landing, index-descent, shared-prime transfer, rad-divisibility) all discharged; IH phrased per-index as "no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime." Corollary: $\mathcal M$ finite. Piece C (period $a_{n+T}=a_n+L$) imported from certified `post-stabilization-theorem`. Sanity-checked on $a_1=15$. Outcome: SOLVED.

## Current best
The full proof below. Every step is rigorous and elementary (radical, induction, geometric-step counting); no open conjectures; no regime split; no analytic estimates. The wall "$\mathcal M$ finite" is closed by the descent; the period conclusion is the certified δ finish.

## Full proof

### 1. Setup and the partial order

For an integer $m>1$ write $P(m)=\{p:\;p\text{ prime},\;p\mid m\}$ for its set of prime divisors and $\mathrm{rad}(m)=\prod_{p\in P(m)}p$ for its radical (squarefree kernel). Note $P(m)\subseteq P(n)\iff\mathrm{rad}(m)\mid\mathrm{rad}(n)$.

Define an index-ordered radical partial order on the terms of the sequence:
$$a_m\prec a_n \iff m<n\;\text{and}\;\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)\quad(\text{equivalently }P(a_m)\subseteq P(a_n),\;m<n).$$
A term $a_n$ is **$\prec$-minimal** if no earlier term $a_m$ (with $m<n$) satisfies $a_m\prec a_n$; equivalently, there is no $m<n$ with $P(a_m)\subseteq P(a_n)$.

The sequence is strictly increasing by definition ($a_{n+1}>a_n$), hence for indices $i,n$:
$$i<n\iff a_i<a_n.$$
This equivalence is used throughout (it is what lets "below $a_n$" be read as "with index $<n$").

Call a prime **large** if $p>a_1^2$, **small** otherwise. Set $P_0=\{p:\;p\text{ prime},\;p\le a_1^2\}$ (finite). An integer is **$a_1^2$-smooth** if every prime dividing it is $\le a_1^2$, i.e. $P(\cdot)\subseteq P_0$.

---

### 2. Piece A — the unconditional "appears $\iff$ valid against all $\prec$-minimal terms below $x$" lemma

> **Lemma A (Piece A, unconditional).** *For every integer $x\ge a_1$, the following are equivalent:*
> (i) *$x$ appears in the sequence (i.e. $x=a_n$ for some $n$);*
> (ii) *$\gcd(x,a_i)>1$ for every $i$ with $a_i<x$;*
> (iii) *$\gcd(x,a_i)>1$ for every $\prec$-minimal term $a_i$ with $a_i<x$.*

**This lemma uses no finiteness hypothesis of any kind** (in particular it does not invoke `universal-membership-no-transient` or `transversal-residue-characterization`, which are conditional on GAP — invoking them here would be circular, since GAP is what the descent proves).

**Proof of (i)$\iff$(ii).** The forward direction is trivial: if $x=a_n$, then $a_n$ was chosen admissible against $a_1,\ldots,a_{n-1}$, so $\gcd(a_n,a_i)>1$ for every $i<n$; and $a_i<x=a_n\iff i<n$ by strict increase.

For the backward direction, suppose $x\ge a_1$ satisfies $\gcd(x,a_i)>1$ for every $i$ with $a_i<x$; we show $x$ appears. Because the sequence is strictly increasing and unbounded ($a_{n+1}>a_n$ with integer gaps $\ge 1$, so $a_n\to\infty$), and $a_1\le x$, there is a (unique) largest index $n$ with $a_n\le x$; then $a_n\le x<a_{n+1}$.

If $a_n=x$, then $x$ already appears (as $a_n$) and we are done. So assume $a_n<x$, i.e. $a_n<x<a_{n+1}$. We claim $x$ is admissible against $a_1,\ldots,a_n$: for every $i\le n$ we have $a_i\le a_n<x$ (strict increase, $i\le n\Rightarrow a_i\le a_n$), so by hypothesis $\gcd(x,a_i)>1$. Hence $x$ is an admissible integer strictly greater than $a_n$. But $x<a_{n+1}$, contradicting the greedy choice of $a_{n+1}$ as the *smallest* admissible integer $>a_n$. Therefore $a_n=x$ was forced (the case $a_n<x$ is impossible), and $x$ appears. ∎ (of (i)$\iff$(ii))

**Proof of (ii)$\iff$(iii).** Since every $\prec$-minimal term is a term, (iii)$\Rightarrow$(ii) is immediate. For (ii)$\Rightarrow$(iii) we must show: validity of $x$ against every term below $x$ follows from validity against the $\prec$-minimal terms below $x$. Take any term $a_j<x$. If $a_j$ is $\prec$-minimal there is nothing to prove. Otherwise, by definition of $\prec$-minimal, there exists $m<j$ with $a_m\prec a_j$, i.e. $m<j$ and $P(a_m)\subseteq P(a_j)$. Iterating this (indices strictly decrease, so the iteration terminates), we obtain a chain $j=j_0>j_1>j_2>\cdots>j_t$ with each $a_{j_{s+1}}\prec a_{j_s}$, terminating at a $\prec$-minimal $a_{j_t}$. (The chain terminates because the indices are nonnegative integers strictly decreasing.) Then $P(a_{j_t})\subseteq P(a_j)$ and $a_{j_t}<a_j<x$. So if $\gcd(x,a_{j_t})>1$, pick a prime $s\mid\gcd(x,a_{j_t})$; then $s\in P(x)\cap P(a_{j_t})\subseteq P(x)\cap P(a_j)$, so $s\mid\gcd(x,a_j)$, giving $\gcd(x,a_j)\ge s>1$. Hence validity against the $\prec$-minimal $a_{j_t}<x$ implies validity against $a_j$. ∎

This completes the proof of Lemma A. ∎

---

### 3. Direction B — $\mathcal M$ is contained in the supports of $\prec$-minimal terms

Let $\mathcal F=\{P(a_i):i\ge 1\}$ be the family of all term-supports, and $\mathcal M=\min(\mathcal F)$ the family of its $\subseteq$-minimal elements (the *minimal-support family*; this is the object δ's `post-stabilization-theorem` is phrased around).

> **Lemma B (Direction B only).** *Every $M\in\mathcal M$ is the support $P(a_i)$ of some $\prec$-minimal term $a_i$.*

**Proof.** Let $M\in\mathcal M$. Since $\mathcal M\subseteq\mathcal F$, $M$ is itself a term-support: $M=P(a_j)$ for some $j$. Let $i$ be the *smallest* index with $P(a_i)=M$ (well-defined: the set $\{j:P(a_j)=M\}$ is nonempty). We claim $a_i$ is $\prec$-minimal.

Suppose not: then some $m<i$ has $a_m\prec a_i$, i.e. $P(a_m)\subseteq P(a_i)=M$. Because $M\in\mathcal M$ is $\subseteq$-minimal in $\mathcal F$ and $P(a_m)\in\mathcal F$ with $P(a_m)\subseteq M$, we must have $P(a_m)=M$. But then $m<i$ also has support $M$, contradicting the minimality of $i$. So $a_i$ is $\prec$-minimal, with $P(a_i)=M$. ∎

> **Remark (Direction A is FALSE; not used).** The reverse inclusion — "every $\prec$-minimal support lies in $\mathcal M$" — is **false** in general. A later term can appear with a support *strictly smaller* than an earlier $\prec$-minimal term's support, demoting the latter's support out of $\mathcal M$. The reviewer verified violations at $a_1=30,429,273,210,46189,323,385$ (e.g. $a_1=429$: eight $\{3,5,p\}$ $\prec$-minimal supports are later subsumed by the appearance of $\{3,5\}$, which removes them from $\mathcal M$). We do **not** attempt Direction A; the descent below transfers its conclusion to $\mathcal M$ via Direction B alone.

---

### 4. Crux 1 — the large-prime descent

> **Theorem (Large-prime descent).** *If $a_n$ is divisible by a large prime $p>a_1^2$, then $a_n$ is **not** $\prec$-minimal.*

Equivalently (contrapositive): **every $\prec$-minimal term is $a_1^2$-smooth.**

**Proof by induction on $n$.** We use the induction hypothesis

> **(IH$_n$)** *Every $\prec$-minimal term $a_i$ with $i<n$ is $a_1^2$-smooth* (equivalently: no $\prec$-minimal $a_i$ with $i<n$ is divisible by a large prime).

**Base case $n=1$.** There is no $\prec$-minimal term with $i<1$, so (IH$_1$) is vacuous. Moreover the conclusion of the theorem is vacuous for $n=1$ as well: if $p\mid a_1$ then $p\le a_1<a_1^2$ (since $a_1>1$, so $a_1^2>a_1$), so $a_1$ carries no large prime. Hence the implication "$a_1$ carries a large prime $\Rightarrow$ $a_1$ is not $\prec$-minimal" holds vacuously (the antecedent never holds). So the base case is sound.

**Inductive step.** Assume (IH$_n$) for some $n\ge 1$. Suppose $a_n$ is divisible by a large prime $p>a_1^2$. We must show $a_n$ is not $\prec$-minimal. The argument has four sub-steps; we discharge each rigorously.

**Step 4a — choose $q$ and locate $q^k c\in[a_1,a_n)$.** Write $a_n=p\,c$ with $p$ large. Because $a_n$ appears in the sequence, by Lemma A (with $x=a_n$), $\gcd(a_n,a_i)>1$ for every $\prec$-minimal $a_i<a_n$; in particular $\gcd(a_n,a_1)>1$ (note $a_1<a_n$ since the sequence is strictly increasing and $a_1<a_n$ — for $n=1$ there is nothing to prove since $a_1$ carries no large prime, so assume $n>1$; even for $n=1$, $\gcd(a_1,a_1)=a_1>1$ trivially). Pick any prime $q\mid\gcd(a_1,a_n)$. Then:
- $q\le a_1$, since $q\mid a_1$;
- $q\neq p$: indeed $p>a_1^2\ge a_1\ge q$ (the inequality $a_1^2\ge a_1$ uses $a_1\ge 2$; strictness $p>a_1^2$ is by "large"), so $p>q$, hence $p\neq q$;
- $q\mid c$: since $q\mid a_n=pc$ and $q\neq p$ (a prime), $q$ does not divide $p$, so $q\mid c$.

Consider the geometric chain $c,\,qc,\,q^2c,\,\ldots$. We claim some term of this chain lies in $[a_1,a_n)$. Because
$$\frac{a_n}{a_1}=\frac{pc}{a_1}\ge\frac{p}{a_1}>a_1\ge q,$$
where the strict inequality $p/a_1>a_1$ is exactly $p>a_1^2$ (the "large" threshold) and $a_1\ge q$ was established above. So $a_n/a_1>q$. Let $k$ be the smallest nonnegative integer with $q^k c\ge a_1$ (well-defined: $q^k c\to\infty$ as $k\to\infty$, so some $k$ qualifies). Then:
- $q^k c\ge a_1$ by choice of $k$;
- if $k=0$, then $c\ge a_1$, and we need $c<a_n$: since $a_n=pc$ and $p>1$, $c<a_n$ — so $c\in[a_1,a_n)$ and we may take $k=0$. (This corner case is consistent with the argument below; we keep $k$ general.)
- if $k\ge 1$, by minimality $q^{k-1}c<a_1$, hence $q^k c=q\cdot q^{k-1}c<q\cdot a_1\le a_1\cdot a_1=a_1^2<a_n$ (the last inequality $a_1^2<a_n$ is $a_1^2<pc$; since $p>a_1^2$ and $c\ge 1$, $pc\ge p>a_1^2$, and $a_n=pc>a_1^2$). So $q^k c\in[a_1,a_n)$.

(In the $k=0$ case the bound $q^k c=c<a_n$ was shown directly; in both cases $q^k c\in[a_1,a_n)$.) This is the **landing sub-lemma**: a power of $q$ lifts $c$ into $[a_1,a_n)$. The load-bearing inequality is $a_n/a_1>q$, which is exactly $p>a_1^2$ — the threshold is tight.

**Step 4b — $q^k c$ appears, via Lemma A and (IH$_n$).** By Lemma A, to show $q^k c$ appears it suffices to show $\gcd(q^k c,a_i)>1$ for every $\prec$-minimal $a_i<q^k c$. Since $q^k c<a_n$, strict increase gives $a_i<q^k c<a_n\Rightarrow i<n$. By (IH$_n$), every $\prec$-minimal $a_i$ with $i<n$ is $a_1^2$-smooth, hence is **not** divisible by the large prime $p$ (which exceeds $a_1^2$); in particular $p\nmid a_i$.

Now $a_n$ appears after $a_i$ (as $i<n$), so by admissibility $\gcd(a_n,a_i)>1$; pick any prime $r\mid\gcd(a_n,a_i)$. Since $p\nmid a_i$ (just shown) while $p\mid a_n$, we have $r\neq p$. From $r\mid a_n=pc$ and $r\neq p$ (a prime), $r\mid c$, and hence $r\mid q^k c$ (as $q^k c$ is a multiple of $c$). Therefore
$$\gcd(q^k c,a_i)\ge r>1.$$
This holds for every $\prec$-minimal $a_i<q^k c$, so by Lemma A, $q^k c$ appears in the sequence. This is the **shared-prime transfer sub-lemma**: the large prime $p$ is invisible to $a_i$ (since $p\nmid a_i$ by IH), so every prime shared between $a_n$ and $a_i$ lies in $c$ and is inherited by $q^k c$.

**Step 4c — $q^k c$ appears strictly before $a_n$, and $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$.** Let $\mathrm{idx}(q^k c)$ denote the index with $a_{\mathrm{idx}(q^k c)}=q^k c$. Since $q^k c<a_n$ and the sequence is strictly increasing, $\mathrm{idx}(q^k c)<n$.

For the radical divisibility: $P(q^k c)=P(c)$, because $q\mid c$ (Step 4a), so multiplying $c$ by $q^k$ introduces no new prime. And $P(a_n)=P(pc)=P(c)\cup\{p\}$. Hence $P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$, i.e.
$$\mathrm{rad}(q^k c)=\mathrm{rad}(c)\mid\mathrm{rad}(pc)=\mathrm{rad}(a_n).$$
This is the **rad-divisibility sub-lemma**: $q\mid c$ is what makes it work (multiplying by $q^k$ adds no new prime), and $q\mid c$ followed from $q\neq p$ and $q\mid a_n=pc$.

**Step 4d — conclude $a_n$ is not $\prec$-minimal.** Combining Steps 4b–4c: $\mathrm{idx}(q^k c)<n$ and $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$, i.e. $\mathrm{idx}(q^k c)<n$ and $P(a_{\mathrm{idx}(q^k c)})\subseteq P(a_n)$. By definition of $\prec$ this says
$$a_{\mathrm{idx}(q^k c)}\prec a_n.$$
So there exists an earlier term ($a_{\mathrm{idx}(q^k c)}$, with index $<n$) subsuming $a_n$ rad-wise; $a_n$ is **not** $\prec$-minimal.

**Closing the induction.** We have shown: under (IH$_n$), if $a_n$ carries a large prime then $a_n$ is not $\prec$-minimal. Contrapositively, if $a_n$ *is* $\prec$-minimal, then $a_n$ carries no large prime, i.e. $a_n$ is $a_1^2$-smooth. Hence (IH$_{n+1}$) holds: every $\prec$-minimal term $a_i$ with $i<n+1$ (i.e. $i\le n$) is $a_1^2$-smooth — the terms with $i<n$ by (IH$_n$), the term $i=n$ (if $\prec$-minimal) by what we just proved. The induction proceeds. ∎

---

### 5. Corollary — the wall is closed: $\mathcal M$ is finite

> **Corollary.** *Every member $M\in\mathcal M$ is a subset of $P_0=\{p:p\le a_1^2\}$; equivalently $P_{\mathrm{ess}}:=\bigcup\mathcal M\subseteq P_0$ is finite, and $\mathcal M\subseteq 2^{P_0}$ is finite.*

**Proof.** By the Large-prime descent (Theorem of §4), every $\prec$-minimal term is $a_1^2$-smooth. By Lemma B (Direction B), every $M\in\mathcal M$ is the support $P(a_i)$ of some $\prec$-minimal term $a_i$; since $a_i$ is $a_1^2$-smooth, $M=P(a_i)\subseteq P_0$. Hence $\bigcup\mathcal M\subseteq P_0$, which is a finite set of primes. Consequently $\mathcal M\subseteq 2^{P_0}$, a finite power set, so $\mathcal M$ is finite. ∎

This closes the stabilization wall (the hypothesis GAP of approach δ): the minimal-support family $\mathcal M=\min\{P(a_i):i\ge 1\}$ is finite.

---

### 6. Finish — import the certified `post-stabilization-theorem` (Piece C)

With $\mathcal M$ finite (Corollary of §5), we invoke the certified theorem `post-stabilization-theorem` (approach `transversal-single-cycle-finish`, Lemma "Theorem A"; reviewer-certified; file `results/imo-2026-06/lemmas/post-stabilization-theorem.md`):

> **`post-stabilization-theorem` (imported).** *Assume $\mathcal M=\min\{P(a_i):i\ge 1\}$ is finite. Set $P=\bigcup\mathcal M$, $L=\prod_{p\in P}p$ (squarefree by construction), and $V=\{r\in\{0,\ldots,L-1\}:\{p\in P:p\mid r\}\text{ is a transversal (hitting set) of }\mathcal M\}$, $T=|V|$. Then*
> $$a_{n+T}=a_n+L\qquad\text{for every }n\ge 1.$$

The hypothesis is satisfied by the Corollary of §5. The theorem composes the certified lemmas `transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle` (and `pairwise-intersection`), each proved in full in `results/imo-2026-06/lemmas/`; we cite them, we do not re-prove them. (Lemma 2 of that chain — `universal-membership-no-transient` — is what delivers *zero transient*: every $a_n\bmod L\in V$, so the cyclic dynamics hold from $n=1$.)

Applying the theorem yields positive integers $T=|V|$ and $L=\prod_{p\in\bigcup\mathcal M}p$ with $a_{n+T}=a_n+L$ for every $n\ge 1$. ∎

---

### 7. Sanity check on $a_1=15$

For $a_1=15=3\cdot 5$: the sequence begins $15,18,20,24,30,36,40,42,45,\ldots$ The minimal-support family (computed in approach δ) is
$$\mathcal M=\bigl\{\{2,3\},\{2,5\},\{3,5\}\bigr\},\qquad\text{all subsets of }P_0=\{p:p\le 15^2=225\}.$$
Indeed every prime in every member of $\mathcal M$ is $\le 5\le 225=a_1^2$ (and even $\le 15=a_1$, consistent with the descent's $a_1^2$ bound; the tightened $\le a_1$ bound is Chen's Remark, not needed here). The structural prime set is $P=\bigcup\mathcal M=\{2,3,5\}$, $L=2\cdot 3\cdot 5=30$ (squarefree), and $V=\{0,6,10,12,15,18,20,24\}$ gives $T=|V|=8$. The descent's corollary ($\mathcal M\subseteq 2^{\{p\le 225\}}$ finite) holds; `post-stabilization-theorem` delivers $a_{n+8}=a_n+30$, matching the known sequence. (Also verified in δ on $a_1=429\to T=908,L=4290$, and $a_1=30\to T=1,L=2$.) These checks confirm the lemmas; they are not proof steps (the proofs above stand on their own).

---

### Summary of theorems invoked

- **Lemma A** (Piece A, this file, §2) — unconditional "appears $\iff$ valid against $\prec$-minimals below $x$"; elementary, no finiteness.
- **Lemma B** (Direction B, this file, §3) — $\mathcal M\subseteq\{$$\prec$-minimal supports$\}$; first-appearance argument. Direction A explicitly noted false and unused.
- **Large-prime descent** (Crux 1, this file, §4) — induction on $n$; large prime $p\mid a_n\Rightarrow a_n$ not $\prec$-minimal; sub-lemmas: landing ($q^k c\in[a_1,a_n)$ via $a_n/a_1>q$), index-descent ($q^k c<a_n\Rightarrow\mathrm{idx}<n$), shared-prime transfer ($r\neq p$ via IH $\Rightarrow r\mid c\mid q^k c$), rad-divisibility ($q\mid c\Rightarrow P(q^k c)=P(c)\subseteq P(a_n)$).
- **Corollary** (this file, §5) — $\mathcal M\subseteq 2^{\{p\le a_1^2\}}$ finite.
- **`post-stabilization-theorem`** (imported, `lemmas/post-stabilization-theorem.md`) — composes `transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle` (and `pairwise-intersection`); reviewer-certified, conditional on $\mathcal M$ finite (which the Corollary supplies).

No regime split (freeze/saturated); no SPT/$p^*$; no $W_1$/$W_2$; no Cov-monovariant; no mtp-window; no analytic density; no Dickson/Bertrand. The descent is uniform and elementary.

The proof is complete: every case covered (the induction's base and step; the trichotomy-free Piece A; the chain-termination in Piece A's (ii)$\Rightarrow$(iii); the $k=0$ corner of the landing), every lemma proved, every invoked theorem named and located, and (the problem being `answer_type: none`, `proof_only`) no numerical final answer is required — the constructive pair $(T,L)=(|V|,\prod_{p\in\bigcup\mathcal M}p)$ is explicitly exhibited by the `post-stabilization-theorem`. ∎

## Promotable lemmas

- **Lemma A (Piece A)** — *For $x\ge a_1$, $x$ appears in the greedy sequence $\iff$ $\gcd(x,a_i)>1$ for every $\prec$-minimal term $a_i<x$*, where $a_m\prec a_n\iff m<n\wedge\mathrm{rad}(a_m)\mid\mathrm{rad}(a_n)$. **Unconditional** (no finiteness). Proved in §2 of this file (`results/imo-2026-06/approaches/large-prime-descent.md`). This is the elementary, non-circular form of the membership criterion; it is importable wherever a finiteness-free criterion is needed (it should NOT be confused with the GAP-conditional `universal-membership-no-transient`).
- **Lemma B (Direction B)** — *Every $M\in\mathcal M=\min\{P(a_i)\}$ is the support of a $\prec$-minimal term.* Proved in §3 of this file. (Direction A is false; see remark.) Importable wherever a one-way transfer from $\mathcal M$ to $\prec$-minimal supports is needed.
- **Large-prime descent** — *If $a_n$ is divisible by a prime $p>a_1^2$, then $a_n$ is not $\prec$-minimal* (equivalently, every $\prec$-minimal term is $a_1^2$-smooth). Proved in §4 by induction on $n$. Corollary (§5): $\mathcal M\subseteq 2^{\{p\le a_1^2\}}$ finite. Importable as the wall-closer: any approach conditional on "$\mathcal M$ finite" (GAP) is made unconditional by composing with this descent.
