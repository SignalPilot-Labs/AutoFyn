# Approach: essential-monovariant

## Status
solved

## Approaches tried
- (round 1) Gap-bound monovariant + finite-state mod $L_0$. Proved rigorously: (i) the cheap lemma (every term has a prime divisor of $a_1$); (ii) the **gap bound** $a_{n+1}-a_n \le \operatorname{rad}(a_1)$ via the next-multiple-of-$\operatorname{rad}(a_1)$ candidate — a genuine bounded-gap monovariant; (iii) consecutive terms share *only* primes $\le \operatorname{rad}(a_1)$. Then proved the **full periodicity machinery conditional on the crux** (Lemma 4: every pair of terms shares a prime $\le \operatorname{rad}(a_1)$). The crux Lemma 4's non-consecutive case was the open gap. — partial (sole gap: Lemma 4).
- (round 2) **Closed Lemma 4 via the game-of-numbers descent.** Realized that aimo-0030 ("game of numbers", Italy TST) constructs, in its Comment 2, the increasing sequence of all good numbers by the EXACT greedy rule of P6 (smallest $b>b_n$ coprime to none of the predecessors), with $b_0=k$. Setting $k=a_1$ identifies P6's sequence with the good numbers of the game with parameter $k=a_1$. aimo-0030's Claim 5 (any two good numbers share a SMALL prime $\le k$) is proved by a minimal-counterexample descent using the stripping lemma (Claim 4) and the game's "move" structure (bad $\Rightarrow$ exists coprime move to a good number). The direct port the outline-reviewer flagged (greedy minimality as the "move") hits the transversal wall; the **indirect port through the game equivalence** furnishes the "move" cleanly, because the move is a statement about the *game*, not about greedy minimality. This yields **Lemma 4'** (every pair of P6's terms shares a prime $\le a_1$), which combined with the round-1 periodicity machinery (run with threshold $B=a_1$) closes the theorem unconditionally. The free partial lemma "multiple-of-$R$ $\Rightarrow$ Lemma 4 for $(a_i,a_j)$" certified into `lemmas/`. — solved.

## Current best
The complete proof. The crux Lemma 4' (every pair of terms shares a prime $\le a_1$) is proved by importing the game-of-numbers structure (parameter $k=a_1$), establishing the greedy characterization (P6's sequence = good numbers), and proving Claim 5 (good numbers share a small prime $\le k$) by the stripping descent. The periodicity machinery (round 1, conditional) instantiated with threshold $B=a_1$ then gives $a_{n+T}=a_n+L_0$ for every $n\ge 1$, with $T=|V|$ and $L=L_0=\prod_{p\le a_1}p$. No gaps remain.

## Full proof

### 0. Definitions and notation

Let $a_1,a_2,a_3,\ldots$ be the sequence of the problem: integers $>1$ with $a_{n+1}$ the smallest integer greater than $a_n$ such that $\gcd(a_{n+1},a_i)>1$ for every $i=1,\ldots,n$. Set
$$A:=a_1\;(\ge 2),\qquad Q:=\{p\text{ prime}:p\le A\},\qquad L_0:=\prod_{p\in Q}p.$$
$Q$ is a finite set (primes up to the fixed integer $A$) and $L_0$ is a fixed positive integer. For an integer $m>1$ write $P(m)$ for its set of prime divisors, and define the **$Q$-type** $\tau(m):=P(m)\cap Q$. Because $p\mid L_0$ for every $p\in Q$, the type $\tau(m)$ depends only on $m\bmod L_0$ (with the convention $0\bmod L_0$ divisible by every $p\in Q$).

The proof has two stages. **Stage I** (Sections 1–6) proves the **crux**:

> **Lemma 4' (crux).** *For all $i<j$, the pair $(a_i,a_j)$ shares a prime $q\le A$; equivalently $\tau(a_i)\cap\tau(a_j)\ne\varnothing$.*

Stage I proves Lemma 4' by introducing an auxiliary *game of numbers* (parameter $k=A$), proving (re-deriving from scratch) the relevant game-theoretic facts — most importantly the **stripping descent** showing any two "good" numbers share a small prime $\le k$ — and then transferring to P6's sequence via the **greedy characterization** (the good numbers are exactly P6's terms). **Stage II** (Section 7) runs the round-1 periodicity machinery on Lemma 4' to conclude.

The route is the Route-D descent the outline-reviewer dispatched, executed through the game equivalence rather than the direct (wall-blocking) greedy-minimality port. Every step below is proved from scratch; the game-of-numbers scaffold is an auxiliary construction, not a citation.

---

### 1. The game of numbers (auxiliary construction)

Fix $k\ge 2$ (we will later take $k=A=a_1$). Two players, Ana and Banana, play: initially some integer $n\ge k$ is written; they alternate, Ana first; a *move* replaces the current number $m$ by an integer $m'$ with $k\le m'<m$ and $\gcd(m,m')=1$; the first player unable to move loses. Call $n\ge k$ **good** if Banana (the second player) has a winning strategy when the game starts at $n$, and **bad** otherwise. Because the written number strictly decreases each move, the game terminates, so exactly one player has a winning strategy: every $n\ge k$ is either good or bad.

Write $n\to x$ for a *move* (so $k\le x<n$ and $\gcd(n,x)=1$).

### 2. Good/bad characterization (Lemmas G1, G2)

**Lemma G1 (good-via-only-bad-moves).** *If every move $n\to x$ (i.e. every $x$ with $k\le x<n$ and $\gcd(n,x)=1$) lands at a bad $x$, then $n$ is good.*

*Proof.* Whatever Ana plays first, $n\to x$, lands at a bad $x$; by definition of bad, the player to move from $x$ (now Banana) has a winning strategy. So Banana wins. $\square$

**Lemma G2 (bad-via-good-move).** *If there exists a good $x$ with $k\le x<n$ and $\gcd(n,x)=1$, then $n$ is bad.*

*Proof.* Ana plays $n\to x$ (legal: $x<n$, $\gcd(n,x)=1$, $x\ge k$). Now $x$ is good, so the *second* player to move from $x$ wins. Ana, having just moved, is now the second player from $x$, so Ana wins. Hence $n$ is bad. $\square$

**Corollary G2' (good $\Leftrightarrow$ no good coprime predecessor).** *$n\ge k$ is good iff no good $x$ with $k\le x<n$ and $\gcd(n,x)=1$ exists; $n$ is bad iff such a good $x$ exists.*

*Proof.* Combine G1 and G2: bad means a good coprime predecessor exists (G2 gives "if"; conversely if a good coprime predecessor exists, G2 gives bad, so good means none exists, which is G1). $\square$

### 3. The seed: $k$ is good, and any two good numbers share a prime

**Lemma G3.** *$k$ is good.*

*Proof.* There is no integer $x$ with $k\le x<k$; equivalently $k$ admits no move. So Ana, to move first from $k$, has no legal move and loses immediately. Banana wins; $k$ is good. $\square$

**Lemma G4 (any two good numbers share a prime).** *If $m,n\ge k$ are both good, then $\gcd(m,n)>1$.*

*Proof.* Suppose contrariwise that $m,n$ are good and coprime; WLOG $m<n$ (if $m=n$ there is nothing to prove as $\gcd(n,n)=n>1$; if $m<n$ use the order, if $n<m$ swap). Then $m$ is a good $x$ with $k\le x<n$ and $\gcd(n,x)=1$. By Corollary G2', $n$ is bad — contradicting that $n$ is good. $\square$

### 4. The stripping lemma (Claim 4)

Call a prime **small** if $p\le k$ and **big** if $p>k$. Two integers $\ge k$ are **similar** if they are divisible by exactly the same small primes.

**Lemma G5 (stripping).** *Let $b\ge k$ have at least one small prime divisor. Then there exists an integer $x$ with $k\le x\le b$, similar to $b$, having no big prime divisor (so $P(x)$ is exactly the set of small prime divisors of $b$).*

*Proof.* If $b$ has no big prime divisor, take $x=b$. Otherwise let $p$ be a small prime divisor of $b$ and $q$ a big prime divisor of $b$ (so $q>k$). Let $a$ denote the product of all distinct small prime divisors of $b$ (the squarefree "small kernel"; $p\mid a$, so $p\le a$). Let $\alpha\ge 0$ be the least integer with $x:=p^\alpha a\ge k$ (well-defined as $p^\alpha\to\infty$). By construction $P(x)$ equals the set of small prime divisors of $b$, so $x$ is similar to $b$ and has no big prime divisor; and $x\ge k$. We verify $x\le b$:
- If $\alpha=0$, then $x=a\ge k$ (leastness of $\alpha$), and $a\mid b$ (each small prime of $b$ divides $b$), so $a\le b$.
- If $\alpha\ge 1$, leastness gives $p^{\alpha-1}a<k$, hence $x=p^\alpha a<pk$. Since $p\mid a$ we have $p\le a$, and since $q$ is a big prime we have $k<q$; therefore
$$x<pk\le ak<aq.$$
Now $a$ is a product of distinct prime divisors of $b$ (the small ones), and $q$ is a (distinct, big) prime divisor of $b$; hence $aq$ is a product of distinct prime divisors of $b$, so $aq\mid b$, giving $x<aq\le b$.

In either case $k\le x\le b$. $\square$

### 5. The descent: good numbers share a SMALL prime (Claim 5)

**Lemma G6 (crux of the game).** *Any two good numbers $\ge k$ share a small prime, i.e. a prime $\le k$.*

*Proof.* Suppose not. Take a counterexample $(b,b')$ with $b,b'$ both good, $b'\ge b\ge k$, sharing only big primes (no small prime divides both), and choose it with $b'$ **minimal**.

Since $b$ and $k$ are both good (Lemma G3), Lemma G4 gives a prime $p$ dividing both $b$ and $k$; as $p\mid k$ we have $p\le k$, i.e. $p$ is small. The pair $(b,b')$ shares no small prime, so $p\nmid b'$, whence $b'\ne b$, i.e. $b'>b$.

By Lemma G5 (applicable because $b$ has the small prime $p$), there is $x$ with $k\le x\le b$, similar to $b$, with no big prime divisor; so $P(x)$ is exactly the set of small prime divisors of $b$. Because $(b,b')$ shares no small prime, no prime of $x$ (all of which are small primes of $b$) divides $b'$; hence $\gcd(x,b')=1$. Now $b'$ is good; if $x$ were good too, then $x$ and $b'$ would be two good numbers with $\gcd(x,b')=1$, contradicting Lemma G4 (any two good numbers share a prime). Therefore $x$ is **bad**.

By Corollary G2' (the "bad $\Rightarrow$ exists good coprime predecessor" direction), there exists a move $x\to b^*$ with $b^*$ good (so $k\le b^*<x$ and $\gcd(x,b^*)=1$).

Now every small prime of $b$ divides $x$ (similarity), and $\gcd(x,b^*)=1$, so **no small prime of $b$ divides $b^*$**. Therefore any prime shared by $b^*$ and $b$ is big. By Lemma G4 (both good $\Rightarrow$ share a prime), $b^*$ and $b$ do share a prime, which by the previous sentence is big. So $(b^*,b)$ is a counterexample pair (both good, sharing only big primes). Its larger element is $b$ (since $b^*<x\le b$), and $b<b'$. This contradicts the minimality of $b'$. $\square$

### 6. The greedy characterization — P6's sequence = good numbers

**Theorem GC (greedy = good).** *For the game of numbers with parameter $k=A=a_1$, the increasing enumeration $g_0<g_1<g_2<\cdots$ of all good numbers satisfies*
$$g_0=A,\qquad g_{n+1}=\min\{m>g_n:\gcd(m,g_i)>1\ \text{for every }i\le n\}\quad(n\ge 0).$$
*In particular $a_n=g_{n-1}$ for every $n\ge 1$; P6's sequence is the increasing enumeration of the good numbers for parameter $k=A$.*

*Proof.* We argue by induction that $g_0=A$ and that the displayed recursion holds.

**Base.** $g_0=A$: $A$ is good (Lemma G3 with $k=A$), and no integer $\ge A$ is smaller than $A$, so $A$ is the smallest good number.

**Inductive step.** Assume $g_0,\ldots,g_n$ are the $n+1$ smallest good numbers (so any good number $\le g_n$ is one of them). Define
$$M:=\min\{m>g_n:\gcd(m,g_i)>1\text{ for every }i\le n\}.$$
We show $M=g_{n+1}$, the next good number, in three sub-claims.

*$M$ is good.* Suppose $M$ were bad. By Corollary G2', there is a good $x$ with $A\le x<M$ and $\gcd(M,x)=1$ (a good coprime predecessor of $M$). We split on where $x$ lies:
  - If $x\le g_n$: by the inductive hypothesis $x\in\{g_0,\ldots,g_n\}$; but $M$ satisfies $\gcd(M,g_i)>1$ for every $i\le n$ by definition, so $\gcd(M,x)>1$, contradicting $\gcd(M,x)=1$.
  - If $g_n<x<M$: $x$ is good, so by Lemma G4 it shares a prime with each of the good numbers $g_0,\ldots,g_n$; hence $\gcd(x,g_i)>1$ for every $i\le n$. Thus $x$ is admissible against $g_0,\ldots,g_n$ with $g_n<x<M$, contradicting the definition of $M$ as the *minimum* such integer.
Both cases are impossible; so $M$ is good.

*No good number lies strictly between $g_n$ and $M$.* Let $m$ satisfy $g_n<m<M$ and suppose $m$ were good. By Lemma G4, $m$ (good) shares a prime with each good $g_i$ ($i\le n$); hence $\gcd(m,g_i)>1$ for every $i\le n$, making $m$ admissible against $g_0,\ldots,g_n$ with $g_n<m<M$ — contradicting the minimality of $M$. So no good number lies in $(g_n,M)$.

*Conclusion.* $M$ is good (first sub-claim) and no good number lies in $(g_n,M)$ (second sub-claim), so $M$ is the smallest good number greater than $g_n$, i.e. $M=g_{n+1}$. This completes the induction. $\square$

**Remark.** The proof of Theorem GC uses only Lemmas G1–G4 (the game's good/bad dichotomy and "$k$ good"); it does not use the descent Lemma G6. The greedy characterization is thus established independently of the crux.

### 7. Lemma 4' (crux) — the transfer to P6

**Lemma 4'.** *For every $i<j$, the pair $(a_i,a_j)$ shares a prime $\le A=a_1$.*

*Proof.* By Theorem GC, P6's sequence $(a_n)$ equals the good numbers $(g_{n-1})$ of the game with parameter $k=A$. By Lemma G6 (crux of the game), any two good numbers share a small prime $\le k=A$. Hence any two terms $a_i,a_j$ share a prime $\le A$. $\square$

Equivalently, with $Q=\{p\le A\}$: for every $i<j$, $\tau(a_i)\cap\tau(a_j)\ne\varnothing$.

---

### 8. Periodicity machinery (conditional on Lemma 4', now proved)

We now run the round-1 finite-state machinery, instantiated with the threshold $B=A$ (any fixed threshold for which pairwise small-prime sharing holds would work; Lemma 4' supplies $B=A$). All steps below were proved in round 1 and are re-stated for completeness; the only change from round 1 is that the hypothesis "Lemma 4" is now *discharged* by Lemma 4'.

#### 8a. The transversal family and the valid-residue set

Let $F_\infty:=\{\tau(a_i):i\ge 1\}\subseteq 2^Q\setminus\{\varnothing\}$ be the set of $Q$-types ever appearing (finite, as $2^Q$ is). Let
$$H_\infty:=\{S\subseteq Q:S\cap T\ne\varnothing\ \text{for every }T\in F_\infty\}$$
be the transversal family of $F_\infty$, and
$$V:=\{r\in\{0,1,\ldots,L_0-1\}:\{p\in Q:p\mid r\}\in H_\infty\}$$
(with $0$ divisible by every $p\in Q$). Because $p\mid L_0$ for $p\in Q$, the residue $m\bmod L_0$ determines $\tau(m)$, so $V$ is the set of residues whose type is a transversal of $F_\infty$.

#### 8b. Free-rider irrelevance (uses Lemma 4')

**Claim.** *For every $n\ge 1$,*
$$a_{n+1}=\min\{m>a_n:m\bmod L_0\in V\}=:M_n.$$

*Proof.* Two directions.
- *Transversal $\Rightarrow$ admissible.* If $m\bmod L_0\in V$, then $\tau(m)\in H_\infty$, so $\tau(m)$ is a transversal of $F_\infty\supseteq F_n:=\{\tau(a_i):i\le n\}$; hence $\tau(m)\cap\tau(a_i)\ne\varnothing$ for every $i\le n$: $m$ shares a $Q$-prime with every $a_i$, so $\gcd(m,a_i)>1$. Thus $m$ is admissible. In particular $M_n$ is admissible, so $a_{n+1}\le M_n$.
- *$a_{n+1}$ has transversal type (uses Lemma 4').* The term $a_{n+1}$ is admissible against $a_1,\ldots,a_n$ (greedy). By Lemma 4' (applied to the pair $(a_{n+1},a_i)$, which is a pair of *terms*), $a_{n+1}$ shares a $Q$-prime with $a_i$ for **every** $i\ge 1$, $i\ne n+1$ — including every $i\le n$ and every future term. Hence $\tau(a_{n+1})\cap\tau(a_i)\ne\varnothing$ for every $i\ne n+1$, i.e. $\tau(a_{n+1})$ hits every type in $F_\infty\setminus\{\tau(a_{n+1})\}$. It remains to note that $\tau(a_{n+1})\ne\varnothing$ (so it also hits its own type $T=\tau(a_{n+1})\in F_\infty$): indeed, pairing $a_{n+1}$ with any other term via Lemma 4' already forces $\tau(a_{n+1})\ne\varnothing$ (e.g. with $a_1$ if $n+1\ne 1$, or with $a_2$ if $n+1=1$; both are terms, and Lemma 4' gives a shared $Q$-prime). Thus $\tau(a_{n+1})\in H_\infty$, i.e. $a_{n+1}\bmod L_0\in V$. Since $a_{n+1}>a_n$, we get $a_{n+1}\ge M_n$.

Combining, $a_{n+1}=M_n$. $\square$ (Claim)

The Claim also shows $a_1\bmod L_0\in V$ (apply Lemma 4' to $(a_1,a_j)$ for all $j$: $\tau(a_1)$ hits every type in $F_\infty$). So the residue sequence $r_n:=a_n\bmod L_0$ stays in $V$ for every $n\ge 1$.

#### 8c. The residue walk is a cyclic permutation

Define $\varphi:V\to V$ by
$$\varphi(r)=\min\{s\in V:s>r\}\text{ if such }s\text{ exists},\qquad \varphi(r)=\min V\text{ otherwise}$$
(the cyclic successor in the natural order on $\{0,\ldots,L_0-1\}$, wrapping around). By the Claim, $r_{n+1}=\varphi(r_n)$ for every $n\ge 1$. The map $\varphi$ is the cyclic successor on the finite ordered subset $V$; it is a bijection whose single orbit is $V$ (iterating $\varphi$ from any $r\in V$ visits every element of $V$ in increasing cyclic order and returns after $|V|$ steps). So $\varphi$ is a cyclic permutation of length $T:=|V|$, and
$$r_{n+T}=r_n\qquad\text{for every }n\ge 1.$$

#### 8d. Lift to translation-periodicity

Write $V=\{v_1<v_2<\cdots<v_T\}$. Over one full period of $T$ consecutive steps the residues traverse all of $V$ exactly once; the value-gaps are $a_{n+1}-a_n=\varphi(r_n)-r_n$ (no wrap) or $\varphi(r_n)+L_0-r_n$ (wrap, when $r_n=v_T$). The sum telescopes:
$$\sum_{k=0}^{T-1}(a_{n+1+k}-a_{n+k})=(v_2-v_1)+(v_3-v_2)+\cdots+(v_T-v_{T-1})+(v_1+L_0-v_T)=L_0.$$
The left side is $a_{n+T}-a_n$. Hence
$$a_{n+T}=a_n+L_0\qquad\text{for every }n\ge 1,$$
with $T=|V|$ and $L=L_0=\prod_{p\le A}p$. The walk is a bijection on $V$ from the very first term, so the periodicity holds for all positive $n$ (no transient).

---

### 9. Conclusion

Taking $T=|V|$ and $L=L_0=\prod_{p\le A=a_1}p$ — both positive integers — we have proved
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge 1,$$
as required by IMO 2026 Problem 6. $\blacksquare$

---

### Appendix: sharper supplementary bounds (round 1, retained)

The following sharper bounds were proved in round 1 and are retained as supplements; they are **not** used in the main proof line above (which uses only the cruder threshold $A$), but they record the tighter structure.

**Lemma 1 (cheap anchor).** *Every term $a_n$ is divisible by some prime divisor of $a_1$.* (Proof: for $n\ge 2$ the greedy at stage $n-1$ forces $\gcd(a_n,a_1)>1$; for $n=1$ tautological.)

**Lemma 2 (gap-bound monovariant).** *$a_{n+1}-a_n\le\operatorname{rad}(a_1)$ for every $n\ge 1$.* (Proof: the least multiple $M$ of $R=\operatorname{rad}(a_1)$ strictly above $a_n$ satisfies $M\le a_n+R$ and is admissible — $R$ is divisible by every prime of $a_1$, and every $a_i$ has a prime of $a_1$ by Lemma 1, so $M$ shares that prime with every $a_i$. Greedy minimality gives $a_{n+1}\le M$.)

**Lemma 3 (consecutive only-small).** *If $p\in P(a_n)\cap P(a_{n+1})$ then $p\le\operatorname{rad}(a_1)$.* (Proof: $p\mid(a_{n+1}-a_n)\le R$ by Lemma 2, so $p\le R$.)

These give the tighter threshold $\operatorname{rad}(a_1)\le A$ for consecutive pairs; the crux Lemma 4' above upgrades "consecutive" to "all pairs" at the (possibly coarser) threshold $A$.

## Promotable lemmas
- **Lemma G6 (small-prime sharing for good numbers).** For the game of numbers with parameter $k\ge 2$, any two good numbers share a prime $\le k$. Proved in §5 of this file (stripping descent + minimal counterexample). This is the load-bearing crux transferred to P6 via the greedy characterization. *Reusable by any approach attacking P6 via the game equivalence.*
- **Theorem GC (greedy = good).** P6's sequence (with $a_1=A$) is the increasing enumeration of the good numbers of the game of numbers with parameter $k=A$. Proved in §6. *Reusable: identifies P6's greedy sequence with the good numbers, enabling transfer of any game-theoretic fact.*
- **Lemma 4' (pairwise small-prime intersection, bound $a_1$).** For P6's sequence, every pair $a_i,a_j$ ($i<j$) shares a prime $\le a_1$. Proved in §7 (transfer of Lemma G6 via Theorem GC). *Reusable: closes the crux for the periodicity machinery at threshold $B=a_1$.*
- **Lemma 2 (gap bound).** $a_{n+1}-a_n\le\operatorname{rad}(a_1)$ for all $n\ge 1$. Proved in Appendix / round 1 §2. *Reusable: bounded-gap monovariant, foundation for windowed arguments.*
- **Lemma 3 (consecutive only-small).** Consecutive terms share only primes $\le\operatorname{rad}(a_1)$. Proved in Appendix / round 1 §3.
- **Lemma (multiple-of-$R$ satisfies Lemma 4).** If $a_j$ is a multiple of $R=\operatorname{rad}(a_1)$ then $(a_i,a_j)$ shares a prime $\le R$ for every $i<j$. Certified in `lemmas/multiple-of-r-satisfies-lemma-4.md`. (Subsumed by Lemma 4' but a clean one-paragraph standalone result.)
