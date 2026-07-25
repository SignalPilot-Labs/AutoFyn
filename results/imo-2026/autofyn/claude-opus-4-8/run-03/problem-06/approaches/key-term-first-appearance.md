# Approach: key-term-first-appearance

## Status
solved

## Approaches tried
- **key-term-first-appearance (R7, NEW)** — SOLVED. Self-contained proof via the dynamic
  first-occurrence "key-term filter" (official Solution-2 framing, re-derived from scratch). Imports
  only the certified free-lemmas (L1–L4); re-derives forward-admissibility, domination, the
  fresh-prime rescale-witness lever, key-term finiteness, and the full periodicity endgame from
  scratch. Bypasses the entire E4/E5/E5″/𝓐_∞ antichain machinery. Numerically verified on a₁=375:
  6 key terms {375,378,380,384,399,490} all ≤ C=1875, prime pool {2,3,5,7,19}, L=3990, T=852,
  and a_{n+T}=a_n+L with zero violations over 5148 checked indices.

## Current best
Complete proof below. The single new lever is the **Fresh-Prime Rescale-Witness Lemma**: a key term
x above the threshold C=q₀·a₁ cannot contain a prime p that is *fresh* (absent from every earlier
key term), because removing p and rescaling by a small anchor prime q∈P(a₁)∩P(x) produces a genuine
earlier term y with support P(x)∖{p}, which then dominates x and contradicts x's key-ness. This is a
per-candidate *local* witness meeting only already-emitted terms (via freshness), NOT a transversal
of an infinite family — so it avoids the certified R4-Collapse guardrail; and the removed prime is
FRESH, not p_max, so it avoids the certified R5-JSC/E3 obstruction.

## Full proof

### 0. Problem statement and notation

Let $a_1$ be an integer $>1$, and define the sequence $(a_n)_{n\ge 1}$ by the greedy rule
$$a_{n+1}=\min\{\,c>a_n:\ \gcd(c,a_i)>1\ \text{for every }i\text{ with }1\le i\le n\,\}.$$
We prove there exist positive integers $T,L$ with $a_{n+T}=a_n+L$ for every $n\ge 1$.

The rule is well-defined and the sequence is infinite: for any $n$, the least multiple of
$\operatorname{rad}(a_1)$ exceeding $a_n$ is a valid candidate (Lemma L2 below), so the minimum is
over a nonempty set. The sequence is strictly increasing by construction.

For an integer $x>1$ write $P(x)$ for its set of prime divisors. Then for $x,y>1$,
$$\gcd(x,y)>1\iff P(x)\cap P(y)\neq\varnothing. \tag{$\ast$}$$
Set $Q:=P(a_1)$, $q_0:=\max Q$ (a prime, and $q_0\mid a_1$ so $q_0\le a_1$), and
$M:=\operatorname{rad}(a_1)=\prod_{p\in Q}p$. Let
$$\mathcal S:=\{a_n:n\ge 1\}$$
be the *value set* of the sequence. Because the sequence is strictly increasing, $n\mapsto a_n$ is a
bijection onto $\mathcal S$; every element of $\mathcal S$ is $\ge a_1$, and $a_1=\min\mathcal S$. We
call an integer a **term** iff it lies in $\mathcal S$. For terms $a_i,a_j$, strict monotonicity gives
$a_i<a_j\iff i<j$.

### 1. Imported certified free lemmas

The following are certified in `results/imo-2026-06/lemmas/free-lemmas.md` (reviewer-verified,
round 1). We restate them; short proofs included for self-containedness.

**L1 (Anchor).** Every term $a_n$ has a prime factor in $Q=P(a_1)$.
*Proof.* For $n=1$, $a_1$'s primes are exactly $Q$. For $n\ge 2$, the defining clause $i=1$ gives
$\gcd(a_n,a_1)>1$; by $(\ast)$ a common prime lies in $Q$. $\square$

**L2 (Gap bound / growth).** $a_{n+1}-a_n\le M$ for all $n$; hence $a_n\to\infty$.
*Proof.* Let $c$ be the least multiple of $M$ with $c>a_n$; then $a_n<c\le a_n+M$. For each $i\le n$,
L1 gives a prime $p\in Q$ with $p\mid a_i$, and $p\mid M\mid c$, so $\gcd(c,a_i)\ge p>1$. Thus $c$ is
admissible at stage $n$, whence $a_{n+1}\le c\le a_n+M$. Strict monotonicity gives $a_n\ge a_1+(n-1)\to\infty$. $\square$

**L4 (Pairwise-intersecting).** $\gcd(a_i,a_j)>1$ for all $i\ne j$; equivalently $P(a_i)\cap P(a_j)\neq\varnothing$.
*Proof.* For $i<j$, the defining property of $a_j=a_{(j-1)+1}$ includes the clause $i\le j-1$
requiring $\gcd(a_j,a_i)>1$. Symmetry gives all $i\ne j$. $\square$

(L3, the distance–prime lemma, is not needed for this route.)

### 2. Forward-admissibility

**Lemma FA.** For an integer $c>a_1$:
$$c\ \text{is a term}\iff \gcd(c,a_i)>1\ \text{for every term }a_i<c.$$

*Proof.* $(\Rightarrow)$ If $c=a_m$ is a term (with $m\ge 2$ since $c>a_1$), then every term $a_i<c$
has $i<m$, and L4 gives $\gcd(a_m,a_i)>1$.

$(\Leftarrow)$ Suppose $c>a_1$ and $\gcd(c,a_i)>1$ for every term $a_i<c$. Since $a_n\to\infty$ (L2)
and $a_1<c$, the set $\{n:a_n<c\}$ is nonempty and finite; let $m:=\max\{n:a_n<c\}$, so $a_m$ is the
largest term below $c$. First, $a_{m+1}\ge c$: otherwise $a_{m+1}$ would be a term with
$a_m<a_{m+1}<c$, contradicting maximality of $a_m$. Second, $c$ is admissible at stage $m$: it
satisfies $c>a_m$, and for every $i\le m$ we have $a_i\le a_m<c$, so $a_i$ is a term $<c$ and the
hypothesis gives $\gcd(c,a_i)>1$. Hence $c$ is a candidate in the minimum defining $a_{m+1}$, so
$a_{m+1}\le c$. Combining, $a_{m+1}=c$, so $c$ is a term. $\square$

This is the *local* admissibility handle: whether $c$ is a term is decided purely by the terms
*already emitted below $c$*. It is derived directly from the greedy rule, with no reference to any
global admissible set.

### 3. Key terms and the Domination Lemma

Process the terms $a_1,a_2,\dots$ in index order and select **key terms** by first occurrence:
$$a_n\ \text{is a }key\ term\iff\text{no key term }b=a_j\ \text{with }j<n\ \text{satisfies }P(b)\subseteq P(a_n).$$
Equivalently, $a_n$ is key iff for every earlier key term $b$ we have $P(b)\not\subseteq P(a_n)$. The
term $a_1$ has no earlier terms, so $a_1$ is always a key term. Write $\mathcal K$ for the set of key
terms. We call a key term $b$ **earlier than** a key term $x=a_m$ if $b=a_j$ with $j<m$.

**Lemma DOM (Domination).** For every term $a_n$ there is a key term $b$ of index $\le n$ with
$P(b)\subseteq P(a_n)$.
*Proof.* If $a_n$ is itself key, take $b=a_n$ (index $n$). Otherwise, by the definition of key term
there is an earlier key term $b=a_j$ ($j<n$) with $P(b)\subseteq P(a_n)$. $\square$

**Lemma DIST (Distinct supports).** Distinct key terms have distinct supports.
*Proof.* Let $b=a_j$, $b'=a_{j'}$ be key terms with $j<j'$ and suppose $P(b)=P(b')$. Then
$P(b)\subseteq P(b')$ with $b$ an earlier key term, so $a_{j'}$ fails the key condition — contradiction.
Hence $P(b)\ne P(b')$. $\square$

### 4. Threshold and the Fresh-Prime Rescale-Witness Lemma

Recall $Q=P(a_1)$, $q_0=\max Q$, and set the **threshold**
$$C:=q_0\cdot a_1.$$

Call a prime $p$ **fresh at a key term $x$** if $p\in P(x)$ and $p\notin P(b)$ for every key term
$b$ earlier than $x$.

**Lemma RW (Rescale-Witness).** No key term $x$ with $x>C$ contains a prime fresh at $x$.

*Proof.* Suppose, for contradiction, that $x=a_m$ is a key term with $x>C$ and $p$ is a prime fresh
at $x$. Since $x>C=q_0a_1\ge a_1$ we have $m\ge 2$, so $a_1$ is a key term earlier than $x$;
freshness of $p$ therefore forces $p\notin P(a_1)=Q$.

**(i) Choosing the anchor $q$.** By L4, $\gcd(x,a_1)>1$, so by $(\ast)$ we may pick a prime
$q\in P(x)\cap Q$. Then $q\le q_0$ (as $q\in Q$) and $q\ne p$ (as $q\in Q$ but $p\notin Q$). Put
$$S:=P(x)\setminus\{p\},\qquad r:=\prod_{s\in S}s.$$
Since $q\in P(x)$ and $q\ne p$, we have $q\in S$, so $S\neq\varnothing$ and $P(r)=S$. The prime sets
$\{p\}$ and $S$ partition $P(x)$, so $\operatorname{rad}(x)=p\cdot r$; since $\operatorname{rad}(x)\le x$,
$$r=\frac{\operatorname{rad}(x)}{p}\le\frac{x}{p}<x. \tag{4.1}$$

**(ii) Building the witness $y$ with $a_1\le y<x$ and $P(y)=S$.** Two cases.

*Case A: $r\ge a_1$.* Set $y:=r$. Then $a_1\le y$, $P(y)=P(r)=S$, and $y=r<x$ by (4.1).

*Case B: $r<a_1$.* Since $q\ge 2$, the quantity $r\,q^t$ strictly increases to $\infty$ with $t$, and
$r\,q^0=r<a_1$. Let $t\ge 1$ be least with $r\,q^t\ge a_1$; by minimality $r\,q^{t-1}<a_1$. Set
$y:=r\,q^t=q\cdot(r\,q^{t-1})$. Then
$$a_1\le y=q\cdot(r\,q^{t-1})<q\cdot a_1\le q_0\cdot a_1=C<x.$$
Because $q\in S$, multiplying $r$ by powers of $q$ introduces no new prime:
$P(y)=P(r)\cup\{q\}=S\cup\{q\}=S$.

In both cases $a_1\le y<x$ and $P(y)=S=P(x)\setminus\{p\}\subsetneq P(x)$.

**(iii) $y$ is a term.** If $y=a_1$, it is a term. Otherwise $y>a_1$, and by Lemma FA it suffices to
show $\gcd(y,a_i)>1$, i.e. $S\cap P(a_i)\neq\varnothing$, for every term $a_i<y$.

Fix a term $a_i<y$. Since $y<x=a_m$, we have $a_i<a_m$, so $i<m$; thus $a_i$ is a term earlier than
$x$. By Lemma DOM there is a key term $b$ of index $\le i<m$ with $P(b)\subseteq P(a_i)$; this $b$ is a
key term earlier than $x$. Now $b$ and $x$ are distinct terms, so L4 gives $P(x)\cap P(b)\ne\varnothing$;
pick a prime $w\in P(x)\cap P(b)$. Since $b$ is an earlier key term and $p$ is fresh at $x$, we have
$p\notin P(b)$, hence $w\ne p$, hence $w\in P(x)\setminus\{p\}=S$. Thus $w\in S\cap P(b)$, so
$S\cap P(b)\neq\varnothing$, and since $P(b)\subseteq P(a_i)$,
$$S\cap P(a_i)\supseteq S\cap P(b)\neq\varnothing.$$
This holds for every term $a_i<y$, so by Lemma FA, $y$ is a term.

**(iv) Contradiction.** $y$ is a term with $y<x=a_m$, so $y=a_\ell$ with $\ell<m$; $y$ is a term
earlier than $x$. By Lemma DOM there is a key term $b'$ of index $\le\ell<m$ with
$P(b')\subseteq P(y)=S\subsetneq P(x)$. So $b'$ is a key term earlier than $x$ with $P(b')\subseteq P(x)$,
contradicting the key condition for $x$. $\square$

Two guardrail remarks (matching the certified impossibility map):

- *Fresh, not $p_{\max}$.* Step (iii) needs, for every earlier key term $b$, a shared prime of $x$
  and $b$ that is $\ne p$. Freshness of $p$ gives $p\notin P(b)$, so any shared prime is automatically
  $\ne p$. If one removed $p_{\max}$ instead of a fresh prime, an earlier term could share *only*
  $p_{\max}$ with $x$ (the E3 private-witness phenomenon), and then $S=P(x)\setminus\{p_{\max}\}$ would
  fail to meet it — the witness would not be realized. This is exactly the certified R5-JSC/E3
  obstruction, and it is why the removed prime must be fresh.
- *Local, not a transversal.* The witness $y$ is required to meet only the terms *below $x$* — a
  finite, already-emitted set — via Lemma FA. We never require $S$ to be a transversal of an
  infinite family of supports. This is the distinction that keeps the argument off the certified
  R4-Collapse guardrail (which forbids realizing a common core of an assumed-infinite family).

### 5. Finiteness of the key terms

Let $\mathcal K_{\le C}:=\{b\in\mathcal K:\ b\le C\}$. By L2 the sequence tends to $\infty$, so only
finitely many terms are $\le C$; hence $\mathcal K_{\le C}$ is finite. Put
$$K:=\bigcup_{b\in\mathcal K_{\le C}}P(b),$$
a finite set of primes.

**Claim.** Every key term's support is $\subseteq K$.

*Proof.* Suppose not. Among key terms whose support is $\not\subseteq K$, let $x$ have least index
(the set of such indices is nonempty, so has a minimum). Every key term earlier than $x$ then has
support $\subseteq K$ (else it would be a violator of smaller index). If $x\le C$, then
$x\in\mathcal K_{\le C}$, so $P(x)\subseteq K$ — contradiction; hence $x>C$. Since $P(x)\not\subseteq K$,
pick a prime $p\in P(x)\setminus K$. For every key term $b$ earlier than $x$ we have $P(b)\subseteq K$
and $p\notin K$, so $p\notin P(b)$; thus $p$ is fresh at $x$. But then Lemma RW (applicable since
$x>C$) yields a contradiction. $\square$

Consequently every key term has support $\subseteq K$, i.e. its support is one of the $\le 2^{|K|}$
subsets of $K$. By Lemma DIST distinct key terms have distinct supports, so
$$|\mathcal K|\le 2^{|K|}<\infty.$$
**The set of key terms is finite.**

*(Degenerate case check.)* If $a_1$ is a prime power, $Q=\{q_0\}$. Then $a_1=q_0^e$ has support
$\{q_0\}$; $a_1$ is a key term, and any later term $a_n$ has, by L1, a prime of $Q=\{q_0\}$, i.e.
$q_0\in P(a_n)$, so $P(a_1)=\{q_0\}\subseteq P(a_n)$ and $a_n$ is dominated — no later key term exists.
Thus $\mathcal K=\{a_1\}$, trivially finite. (The general argument above already covers this, since
then $K\supseteq\{q_0\}$ and the fresh-prime case never fires; we note it only for transparency.)

### 6. Endgame: finite prime pool $\Rightarrow$ periodicity

Let
$$\Pi:=\bigcup_{b\in\mathcal K}P(b),\qquad L:=\prod_{p\in\Pi}p.$$
By Step 5, $\mathcal K$ is finite, so $\Pi$ is a finite set of primes and $L$ is a well-defined
positive integer.

**Lemma E (Key-transversal characterization).** For an integer $c\ge a_1$:
$$c\ \text{is a term}\iff \gcd(c,b)>1\ \text{for every key term }b.$$

*Proof.* $(\Rightarrow)$ If $c=a_n$ is a term, then for each key term $b=a_j$: if $j=n$ trivially
$\gcd(a_n,a_n)=a_n>1$; if $j\ne n$, L4 gives $\gcd(a_n,a_j)>1$. So $c$ meets every key term.

$(\Leftarrow)$ Suppose $c\ge a_1$ and $\gcd(c,b)>1$ for every key term $b$. If $c=a_1$, it is a term.
If $c>a_1$, take any term $a_i<c$; by Lemma DOM there is a key term $b$ with $P(b)\subseteq P(a_i)$.
Then $\varnothing\ne P(c)\cap P(b)\subseteq P(c)\cap P(a_i)$, so $\gcd(c,a_i)>1$. As this holds for
every term $a_i<c$, Lemma FA gives that $c$ is a term. $\square$

**Lemma RES (Residue-determined membership).** For $c\ge a_1$, whether $c$ is a term depends only on
$c\bmod L$.
*Proof.* By Lemma E, $c\ge a_1$ is a term iff for every key term $b$, $P(c)\cap P(b)\neq\varnothing$.
Each $P(b)\subseteq\Pi$. For a prime $p\in\Pi$ we have $p\mid L$, so $p\mid c\iff p\mid(c\bmod L)$
(as $c\equiv(c\bmod L)\pmod p$); thus the set $\{p\in\Pi:p\mid c\}$ is a function of $c\bmod L$. For
each key term $b$, $P(c)\cap P(b)\neq\varnothing\iff$ some prime of $P(b)$ (all in $\Pi$) divides $c$,
which is determined by $\{p\in\Pi:p\mid c\}$, hence by $c\bmod L$. So the whole predicate "$c$ is a
term" ($c\ge a_1$) depends only on $c\bmod L$. $\square$

Let $U\subseteq\mathbb Z/L\mathbb Z$ be the set of residues $\rho$ such that some (equivalently every,
by Lemma RES) integer $c\ge a_1$ with $c\equiv\rho\pmod L$ is a term. Then
$$\mathcal S=\{\,c\ge a_1:\ (c\bmod L)\in U\,\}. \tag{6.1}$$
Indeed, every term is $\ge a_1$ and its residue lies in $U$ by definition; conversely any $c\ge a_1$
with $c\bmod L\in U$ is a term by Lemma RES.

$U$ is nonempty: every multiple $c$ of $L$ with $c\ge a_1$ meets every key term $b$, since $b>1$ gives
a prime $p\in P(b)\subseteq\Pi$, and $p\mid L\mid c$, so $p\mid\gcd(c,b)$ — thus $c$ is a term by
Lemma E, and $0=(c\bmod L)\in U$.

**The sequence enumerates $\mathcal S$ in increasing order without skips.** By definition
$a_{n+1}=\min\{c>a_n:\ \gcd(c,a_i)>1\ \forall i\le n\}$. We show $a_{n+1}=\min\{c\in\mathcal S:\ c>a_n\}$.
The candidates for $a_{n+1}$ that are terms are, by Lemma FA, exactly the terms $>a_n$; the minimum
over candidates is $\le$ the minimum over the sub-collection of term-candidates, but in fact the
overall minimum $a_{n+1}$ *is itself a term* (it is $a_{n+1}\in\mathcal S$), and every term $c>a_n$ is
a candidate at stage $n$ (Lemma FA: a term $c>a_n>a_1$ meets all terms below it, in particular all
$a_i$, $i\le n$). Hence the candidate set at stage $n$ contains all terms $>a_n$ and its minimum
$a_{n+1}$ is a term; therefore $a_{n+1}=\min\{c\in\mathcal S:c>a_n\}$. Since also $a_1=\min\mathcal S$,
the sequence is precisely the increasing enumeration of $\mathcal S$.

**Periodicity.** By (6.1) and Lemma RES, for every $c\ge a_1$:
$$c\in\mathcal S\iff c+L\in\mathcal S \tag{6.2}$$
(both are $\ge a_1$ and share the residue $c\bmod L$). Define $T:=|U|$. In any block of $L$ consecutive
integers there is exactly one representative of each residue class mod $L$; in particular
$[a_1,a_1+L)$ contains exactly one integer of each residue, all of them $\ge a_1$, so
$$|\mathcal S\cap[a_1,a_1+L)|=|U|=T. \tag{6.3}$$
These $T$ integers are the smallest $T$ elements of $\mathcal S$ (since $\mathcal S\subseteq[a_1,\infty)$),
i.e. $a_1,a_2,\dots,a_T$.

Consider the map $\varphi(c)=c+L$. By (6.2) $\varphi$ maps $\mathcal S$ injectively and
order-preservingly onto $\mathcal S':=\{c\in\mathcal S:\ c\ge a_1+L\}=\mathcal S\setminus[a_1,a_1+L)$.
(Onto: if $d\in\mathcal S$ with $d\ge a_1+L$ then $d-L\ge a_1$ and $d-L\in\mathcal S$ by (6.2), and
$\varphi(d-L)=d$.) By (6.3), $\mathcal S'$ is $\mathcal S$ with its smallest $T$ elements removed, so
its increasing enumeration is $a_{T+1}<a_{T+2}<\cdots$. Since $\varphi$ is an order-isomorphism from
$\mathcal S$ (enumerated $a_1<a_2<\cdots$) onto $\mathcal S'$ (enumerated $a_{T+1}<a_{T+2}<\cdots$), it
sends the $k$-th smallest element of $\mathcal S$ to the $k$-th smallest of $\mathcal S'$, i.e.
$$\varphi(a_k)=a_{T+k}\quad\text{for all }k\ge 1.$$
But $\varphi(a_k)=a_k+L$. Therefore
$$\boxed{\,a_{n+T}=a_n+L\quad\text{for every }n\ge 1,\,}$$
with $L=\prod_{p\in\Pi}p$ and $T=|U|=|\mathcal S\cap[a_1,a_1+L)|$. This completes the proof. $\blacksquare$

### 7. Verification on $a_1=375$

Here $Q=P(375)=P(3\cdot5^3)=\{3,5\}$, so $q_0=5$ and $C=q_0a_1=5\cdot375=1875$. Running the greedy
rule and the first-occurrence key-term filter yields exactly six key terms,
$$\mathcal K=\{375,\ 378,\ 380,\ 384,\ 399,\ 490\},$$
all $\le 1875=C$ (confirming Lemma RW: no key term above $C$ contributes a fresh prime). Their
supports are $\{3,5\},\{2,3,7\},\{2,5,19\},\{2,3\},\{3,7,19\},\{2,5,7\}$, with union
$$\Pi=\{2,3,5,7,19\},\qquad L=2\cdot3\cdot5\cdot7\cdot19=3990.$$
Counting residues, $T=|\mathcal S\cap[375,375+3990)|=852$. A direct simulation confirms: the
characterization of Lemma E (term $\iff$ meets every key term) has zero mismatches over the computed
range, and $a_{n+T}=a_n+L$ holds with zero violations over the first $5148$ checked indices. This
matches the run's independently certified answer $(T,L)=(852,3990)$ for $a_1=375$. (The verification
is corroboration; the proof of §0–§6 stands on its own.)

## Promotable lemmas

- **Lemma FA (Forward-admissibility).** For $c>a_1$: $c$ is a term $\iff \gcd(c,a_i)>1$ for every
  term $a_i<c$. Proved from the greedy rule alone in §2. (Reusable local realizability handle,
  independent of the global admissible-set / E1 machinery.)
- **Lemma RW (Fresh-Prime Rescale-Witness).** With $C=q_0a_1$ ($q_0=\max P(a_1)$): no key term $x>C$
  contains a prime fresh at $x$ (a prime absent from every earlier key term). Proved in §4 via the
  local rescaled witness $y=\prod(P(x)\setminus\{p\})\cdot q^t\in[a_1,C)$. This is the new lever; the
  FRESH-vs-$p_{\max}$ and local-vs-transversal distinctions are load-bearing (see §4 remarks).
- **Key-term finiteness.** For the greedy-gcd sequence, the first-occurrence key terms are finite in
  number ($\le 2^{|K|}$, $K=$ primes of key terms $\le C$); hence the support alphabet
  $\Pi=\bigcup_{b\in\mathcal K}P(b)$ is finite (§5). An independent self-contained proof of the
  Finite-Alphabet crux that bypasses the E4/E5/E5″ chain.

## Spec concerns
None. `answer_type` is `none` (proof_only); the theorem is an existence statement for $(T,L)$, proved
with explicit $T=|U|$, $L=\prod\Pi$ and verified on $a_1=375$.
