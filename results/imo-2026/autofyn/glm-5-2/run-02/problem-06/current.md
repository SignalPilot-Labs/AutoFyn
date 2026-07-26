# IMO 2026 Problem 6

## Status
solved

## Approaches tried
- `essential-monovariant` (round 2) — **SOLVED.** Game-of-numbers equivalence (Theorem GC, proved from scratch via G1–G4) identifies P6's greedy sequence with the good numbers of the game with parameter $k=a_1$; stripping descent (Lemma G6, re-proved from scratch, adapting aimo-0030's Claim 5) shows any two good numbers share a small prime $\le k$; transferring via GC gives Lemma 4' (every pair of terms shares a prime $\le a_1$); round-1 periodicity machinery at threshold $B=a_1$ yields $a_{n+T}=a_n+L_0$ for all $n\ge 1$ with $T=|V|$, $L=L_0=\prod_{p\le a_1}p$, no transient. Verified empirically for $a_1\in\{2,3,5,6,7,10,15\}$. APPROVED.
- `crude-reduced-type` (round 2) — partial. Second conditional-on-crux bridge at threshold $Q=\{p\le a_1\}$. Steps 1–6, 8–10 rigorous; crux Lemma 4 [GAP] imported from `essential-monovariant` (not independently closed). Honest partial; now fillable from the APPROVED Lemma 4' (same threshold). Redundant once `essential-monovariant` is solved.
- `propagation-bezout` (round 2) — unsolved / dead-end. Propagation route is circular as filed (Sub-step 4b: shift algebra $\varphi$ defined via $V$, whose relevance uses Lemma 4). Non-transitivity of "shares-a-small-prime" verified; growing bound only ($\le kR$); no promotable lemma; extractable partial subsumed by Lemma 1. Route cannot prove Lemma 4 as set up.
- `grid-counting-shared-primes` (round 2) — partial. Certified large-prime-span lemma (correct, in `lemmas/`); growing-window ceiling $\le(N-1)R$ honestly [GAP] (obstructions G1 growing window, G2 aggregate-vs-per-cell). Lemma 5 ($\sum_p1/p^2<1/2$) proof has an arithmetic error (subtracts $1/25$ for $n=5\in\{n\ge5\}$; stated bound $389/900$ is false, true $\approx0.4522$); conclusion survives via corrected bound $17/36<1/2$. Not load-bearing (only feeds the [GAP] ceiling characterization). Fix: $389/900\to17/36$.

## Current best
The complete proof (see Full proof below). The crux Lemma 4' (every pair of terms shares a prime $\le a_1$) is proved via the game-of-numbers equivalence: P6's greedy sequence is the increasing enumeration of the good numbers of the game with parameter $k=a_1$ (Theorem GC), and any two good numbers share a small prime $\le k$ (Lemma G6, stripping descent). The round-1 periodicity machinery at threshold $B=a_1$ then gives $a_{n+T}=a_n+L_0$ for every $n\ge 1$, with $T=|V|$ and $L=L_0=\prod_{p\le a_1}p$. No gaps remain.

## Full proof

### 0. Definitions and notation

Let $a_1,a_2,a_3,\ldots$ be the sequence of the problem: integers $>1$ with $a_{n+1}$ the smallest integer greater than $a_n$ such that $\gcd(a_{n+1},a_i)>1$ for every $i=1,\ldots,n$. Set
$$A:=a_1\;(\ge 2),\qquad Q:=\{p\text{ prime}:p\le A\},\qquad L_0:=\prod_{p\in Q}p.$$
$Q$ is a finite set (primes up to the fixed integer $A$) and $L_0$ is a fixed positive integer. For an integer $m>1$ write $P(m)$ for its set of prime divisors, and define the **$Q$-type** $\tau(m):=P(m)\cap Q$. Because $p\mid L_0$ for every $p\in Q$, the type $\tau(m)$ depends only on $m\bmod L_0$ (with the convention $0\bmod L_0$ divisible by every $p\in Q$).

The proof has two stages. **Stage I** proves the crux Lemma 4' by introducing an auxiliary *game of numbers* (parameter $k=A$), proving the relevant game-theoretic facts from scratch (most importantly the stripping descent showing any two good numbers share a small prime $\le k$), and transferring to P6's sequence via the greedy characterization (the good numbers are exactly P6's terms). **Stage II** runs the periodicity machinery on Lemma 4' to conclude. Every step is proved from scratch; the game-of-numbers scaffold is an auxiliary construction, not a citation.

---

### Stage I: the crux

#### 1. The game of numbers (auxiliary construction)

Fix $k\ge 2$ (later $k=A=a_1$). Two players, Ana and Banana, play: initially some integer $n\ge k$ is written; they alternate, Ana first; a *move* replaces the current number $m$ by an integer $m'$ with $k\le m'<m$ and $\gcd(m,m')=1$; the first player unable to move loses. Call $n\ge k$ **good** if Banana (the second player) wins from $n$, **bad** otherwise. The written number strictly decreases each move, so the game terminates, and exactly one player wins: every $n\ge k$ is good or bad. Write $n\to x$ for a move ($k\le x<n$, $\gcd(n,x)=1$).

#### 2. Good/bad characterization

**Lemma G1 (good-via-only-bad-moves).** *If every move $n\to x$ lands at a bad $x$, then $n$ is good.* Whatever Ana plays, $n\to x$ lands at a bad $x$; the player to move from $x$ (now Banana) wins. $\square$

**Lemma G2 (bad-via-good-move).** *If a good $x$ with $k\le x<n$ and $\gcd(n,x)=1$ exists, then $n$ is bad.* Ana plays $n\to x$; $x$ good means the second player from $x$ wins; Ana is now the second player. $\square$

**Corollary G2'.** *$n$ is good iff no good $x$ with $k\le x<n$, $\gcd(n,x)=1$ exists; bad iff such $x$ exists.* (Combine G1, G2.) $\square$

#### 3. Seed and pairwise sharing

**Lemma G3.** *$k$ is good.* No move from $k$ exists (no $x\in[k,k)$); Ana loses first move. $\square$

**Lemma G4 (any two good numbers share a prime).** *If $m,n\ge k$ are good, then $\gcd(m,n)>1$.* If $m<n$ good and coprime, $m$ is a good coprime predecessor of $n$, so $n$ is bad by G2' — contradiction. $\square$

#### 4. The stripping lemma

Call a prime **small** if $p\le k$ and **big** if $p>k$. Two integers $\ge k$ are **similar** if divisible by the same small primes.

**Lemma G5 (stripping).** *Let $b\ge k$ have a small prime divisor. Then $x$ exists with $k\le x\le b$, similar to $b$, with no big prime divisor.* If $b$ has no big prime, take $x=b$. Else let $p$ be a small and $q$ a big prime divisor of $b$; let $a$ be the product of all distinct small prime divisors of $b$ (so $p\mid a$, $p\le a$); let $\alpha\ge0$ be least with $x:=p^\alpha a\ge k$. Then $P(x)$ is exactly the small prime divisors of $b$ (so $x$ similar to $b$, no big prime). For $x\le b$: if $\alpha=0$, $x=a\ge k$ (leastness) and $a\mid b$ so $a\le b$. If $\alpha\ge1$, leastness gives $p^{\alpha-1}a<k$, so $x=p^\alpha a<pk$; with $p\le a$ and $k<q$, $x<pk\le ak<aq$; and $aq$ is a product of distinct prime divisors of $b$, so $aq\mid b$, giving $x<aq\le b$. $\square$

#### 5. The descent: good numbers share a SMALL prime

**Lemma G6 (crux of the game).** *Any two good numbers $\ge k$ share a small prime $\le k$.* Suppose not; take a counterexample $(b,b')$ with $b,b'$ good, $b'\ge b\ge k$, sharing only big primes, $b'$ minimal. By G3 and G4, $b$ and $k$ (both good) share a prime $p$; $p\mid k$ so $p$ is small. The pair shares no small prime, so $p\nmid b'$, hence $b'>b$. Apply G5 to $b$ (has small prime $p$): $x$ with $k\le x\le b$, similar to $b$, no big prime. Then $P(x)$ = small primes of $b$, none of which divides $b'$ (pair shares no small prime), so $\gcd(x,b')=1$. Since $b'$ is good and $\gcd(x,b')=1$, $x$ cannot be good (else $x,b'$ good and coprime, contradicting G4), so $x$ is bad. By G2' (bad $\Rightarrow$ good coprime predecessor), a move $x\to b^*$ with $b^*$ good exists ($k\le b^*<x$, $\gcd(x,b^*)=1$). All small primes of $b$ divide $x$ (similarity) and $\gcd(x,b^*)=1$, so no small prime of $b$ divides $b^*$; hence any prime shared by $b^*$ and $b$ is big. By G4 (both good), $b^*$ and $b$ share a prime, which is big; so $(b^*,b)$ is a counterexample (both good, sharing only big primes) with larger element $b$ (since $b^*<x\le b$), and $b<b'$, contradicting minimality of $b'$. $\square$

#### 6. The greedy characterization — P6's sequence = good numbers

**Theorem GC.** *For the game with parameter $k=A=a_1$, the increasing enumeration $g_0<g_1<\cdots$ of all good numbers satisfies $g_0=A$ and $g_{n+1}=\min\{m>g_n:\gcd(m,g_i)>1\ \forall i\le n\}$. In particular $a_n=g_{n-1}$ for every $n\ge 1$.*

*Proof.* Induction. **Base:** $g_0=A$ (G3: $A$ good; nothing $\ge A$ is smaller). **Step:** Assume $g_0,\ldots,g_n$ are the $n+1$ smallest good numbers. The set $\{m>g_n:\gcd(m,g_i)>1\ \forall i\le n\}$ is nonempty: any sufficiently large multiple of $k=A$ is admissible, since by G4 each $g_i$ and $k$ (both good) share a prime $p_i\mid k$, and a multiple of $k$ is divisible by $p_i\mid g_i$. Define
$$M:=\min\{m>g_n:\gcd(m,g_i)>1\ \text{for every }i\le n\}.$$
*$M$ is good:* if $M$ were bad, by G2' a good $x$ with $A\le x<M$, $\gcd(M,x)=1$ exists. If $x\le g_n$, then $x\in\{g_0,\ldots,g_n\}$ (IH) but $\gcd(M,x)>1$ (definition of $M$) — contradiction. If $g_n<x<M$, then $x$ good $\Rightarrow$ by G4 $x$ shares a prime with each $g_i$ ($i\le n$) $\Rightarrow$ $x$ admissible with $g_n<x<M$ — contradicting minimality of $M$. So $M$ is good.
*No good number in $(g_n,M)$:* if $m\in(g_n,M)$ good, G4 makes $m$ admissible against $g_0,\ldots,g_n$, contradicting minimality of $M$.
So $M$ is the smallest good number $>g_n$, i.e. $M=g_{n+1}$. $\square$

(The proof uses only G1–G4; G6 is not invoked. The construction matches aimo-0030 Comment 2, but is here proved, not asserted.)

#### 7. Lemma 4' (crux) — transfer to P6

**Lemma 4'.** *For every $i<j$, the pair $(a_i,a_j)$ shares a prime $\le A=a_1$.* By Theorem GC, $(a_n)=(g_{n-1})$ for the game with $k=A$. By Lemma G6, any two good numbers share a small prime $\le k=A$. Hence any two terms $a_i,a_j$ share a prime $\le A$. $\square$

Equivalently, with $Q=\{p\le A\}$: for every $i<j$, $\tau(a_i)\cap\tau(a_j)\ne\varnothing$.

---

### Stage II: periodicity machinery (conditional on Lemma 4', now proved)

#### 8a. The transversal family and the valid-residue set

Let $F_\infty:=\{\tau(a_i):i\ge 1\}\subseteq 2^Q\setminus\{\varnothing\}$ (finite). Let
$$H_\infty:=\{S\subseteq Q:S\cap T\ne\varnothing\ \forall T\in F_\infty\}$$
be the transversal family, and
$$V:=\{r\in\{0,\ldots,L_0-1\}:\{p\in Q:p\mid r\}\in H_\infty\}$$
($0$ divisible by every $p\in Q$). Since $p\mid L_0$ for $p\in Q$, the residue $m\bmod L_0$ determines $\tau(m)$; $V$ is the set of residues whose type is a transversal of $F_\infty$.

#### 8b. Free-rider irrelevance (uses Lemma 4')

**Claim.** *For every $n\ge 1$, $a_{n+1}=\min\{m>a_n:m\bmod L_0\in V\}=:M_n$.*

*Proof.* (Transversal $\Rightarrow$ admissible.) If $m\bmod L_0\in V$, $\tau(m)\in H_\infty$, so $\tau(m)$ is a transversal of $F_\infty\supseteq F_n$; hence $\tau(m)\cap\tau(a_i)\ne\varnothing$ for every $i\le n$: $m$ shares a $Q$-prime with every $a_i$, so $\gcd(m,a_i)>1$. Thus $M_n$ is admissible, so $a_{n+1}\le M_n$.
($a_{n+1}$ has transversal type.) By Lemma 4' applied to the pair $(a_{n+1},a_i)$ (a pair of terms), $a_{n+1}$ shares a $Q$-prime with $a_i$ for **every** $i\ge 1$, $i\ne n+1$: $\tau(a_{n+1})\cap\tau(a_i)\ne\varnothing$ for every $i\ne n+1$, i.e. $\tau(a_{n+1})$ hits every type in $F_\infty\setminus\{\tau(a_{n+1})\}$. Also $\tau(a_{n+1})\ne\varnothing$: pair $a_{n+1}$ with any other term via Lemma 4' (e.g. $a_1$ if $n+1\ne1$, else $a_2$). So $\tau(a_{n+1})\in H_\infty$, i.e. $a_{n+1}\bmod L_0\in V$. Since $a_{n+1}>a_n$, $a_{n+1}\ge M_n$. Combining, $a_{n+1}=M_n$. $\square$

The Claim also gives $a_1\bmod L_0\in V$ (apply Lemma 4' to $(a_1,a_j)$ for all $j$). So $r_n:=a_n\bmod L_0\in V$ for every $n\ge 1$.

#### 8c. The residue walk is a cyclic permutation

Define $\varphi:V\to V$ by $\varphi(r)=\min\{s\in V:s>r\}$ if such $s$ exists, $\varphi(r)=\min V$ otherwise (cyclic successor). By the Claim, $r_{n+1}=\varphi(r_n)$ for every $n\ge 1$. $\varphi$ is the cyclic successor on the finite ordered subset $V$; it is a bijection whose single orbit is $V$, returning after $T:=|V|$ steps. So
$$r_{n+T}=r_n\qquad\text{for every }n\ge 1.$$

#### 8d. Lift to translation-periodicity

Write $V=\{v_1<v_2<\cdots<v_T\}$. Over one full period, the residues traverse all of $V$ exactly once; exactly one transition wraps. The value-gaps are $a_{k+1}-a_k=\varphi(r_k)-r_k$ (no wrap) or $\varphi(r_k)+L_0-r_k$ (wrap, at $r_k=v_T$). The sum telescopes:
$$\sum_{k=0}^{T-1}(a_{n+1+k}-a_{n+k})=(v_2-v_1)+\cdots+(v_T-v_{T-1})+(v_1+L_0-v_T)=L_0.$$
The left side is $a_{n+T}-a_n$. Hence
$$a_{n+T}=a_n+L_0\qquad\text{for every }n\ge 1,$$
with $T=|V|$ and $L=L_0=\prod_{p\le A}p$. The walk is a bijection on $V$ from the first term, so the periodicity holds for all positive $n$ (no transient).

---

### 9. Conclusion

Taking $T=|V|$ and $L=L_0=\prod_{p\le A=a_1}p$ — both positive integers — we have proved
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge 1,$$
as required by IMO 2026 Problem 6. $\blacksquare$

---

## Problem statement

Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than $1$. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i)>1$ for every $i=1,2,\ldots,n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$ for every positive integer $n$.

## Notes
- Domain: number_theory. Task: proof_only (no numeric answer). Difficulty: 9/10.
- Solved in round 2 by `essential-monovariant` via the game-of-numbers equivalence (corpus crux `aimo-0030`, IMO-SL 2013 N5, adapted and re-proved from scratch).
- Supplementary (non-load-bearing) bounds retained in `approaches/essential-monovariant.md` Appendix: Lemma 1 (every term has a prime divisor of $a_1$), Lemma 2 (gap bound $\le\operatorname{rad}(a_1)$), Lemma 3 (consecutive terms share only primes $\le\operatorname{rad}(a_1)$).
