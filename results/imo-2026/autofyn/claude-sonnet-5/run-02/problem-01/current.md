## Status
solved

## Approaches tried
- **Per-prime $p$-adic valuation bookkeeping** (`approaches/prime-valuation-invariant.md`). Reduces
  the board process to independent per-prime exponent sequences, tracks the invariant
  $g_p=\gcd$(exponent multiset) via the Euclidean-subtraction identity
  $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$, and a lexicographic monovariant
  $(\Omega,C)$ for termination. **Outcome: verified solved.** Complete, self-contained, rigorous;
  reviewed and computationally cross-checked (random and exhaustive simulation against the closed
  form for $M$). Adopted below as the Full proof (more direct of the two correct approaches).
- **Rewriting-system / Newman's-Lemma confluence** (`approaches/confluence-newman.md`). Models the
  board as a multiset-rewriting system, proves Newman's Lemma from scratch, and establishes local
  confluence via an "Overlap Localization Lemma" showing any two diverging moves share a footprint
  of exactly 3 or 4 occurrences. **Outcome: also verified solved** — an independent, more elaborate
  but equally rigorous route to the same result (with the closed form for $M$ obtained as a
  corollary via the same per-prime invariant). Kept as a valid alternative full proof; not used
  below only because the invariant-only approach is shorter.

## Current best
(Superseded — problem fully solved; see Full proof.)

## Full proof

### Setup and notation

Let $x_1,\dots,x_{2026}$ be the initial integers on the board, each $>1$. A **state** is a tuple
$S=(a_1,\dots,a_{2026})\in\mathbb Z_{>0}^{2026}$ (the current board values). A **move** on a state
$S$ chooses two distinct indices $i\ne j$ with $a_i=m>1$ and $a_j=n>1$, and replaces $(a_i,a_j)$
by $(\gcd(m,n),\ \mathrm{lcm}(m,n)/\gcd(m,n))$, leaving all other coordinates unchanged. Moves are
made while at least two entries of the current state exceed $1$; the process **stops** at a state
with at most one entry $>1$ (no legal move available, since a move requires two entries $>1$).

For $n\in\mathbb Z_{>0}$ and a prime $p$, write $v_p(n)\ge 0$ for the exponent of $p$ in the prime
factorization of $n$, and $\Omega(n)=\sum_p v_p(n)$ for the total number of prime factors of $n$
counted with multiplicity ($\Omega(1)=0$).

For a finite multiset $T=\{t_1,\dots,t_k\}\subset\mathbb Z_{\ge0}$ ($k\ge1$), define
$$\gcd(T) := \begin{cases} 0 & \text{if } t_1=\cdots=t_k=0,\\ \gcd\text{ of the nonzero } t_i & \text{otherwise},\end{cases}$$
matching the usual convention $\gcd(0,\dots,0)=0$ and agreeing with the ordinary pairwise gcd
otherwise.

**Lemma 0 (multiset-gcd well-definedness and factoring).** $\gcd$, extended by
$\gcd(0,x)=\gcd(x,0)=x$, is commutative and associative on $\mathbb Z_{\ge0}$. Hence for any finite
multiset $T=T_1\sqcup T_2$, $\gcd(T)=\gcd(\gcd(T_1),\gcd(T_2))$, independent of bracketing/order.

*Proof.* Commutativity/associativity of ordinary gcd on $\mathbb Z_{>0}$ is standard (a common
divisor characterization: $\gcd(\gcd(a,b),c)$ and $\gcd(a,\gcd(b,c))$ both equal the largest
integer dividing all of $a,b,c$). Extending to zero via $\gcd(0,x)=x$ preserves both properties (a
direct finite case check). In a commutative semigroup, any two full binary combinations of a fixed
finite multiset agree (induction on multiset size, using associativity to reduce to "combine one
element with the combination of the rest," and commutativity for which element is last). $\blacksquare$

**Lemma 0'.** If a finite multiset $T\subset\mathbb Z_{\ge0}$ has a nonzero entry, $\gcd(T)>0$.

*Proof.* $\gcd(T)$ is then the classical gcd of the nonempty set of positive integers
$\{t\in T:t\ne0\}$, which is itself a positive integer (the maximum of the nonempty set of common
divisors, which contains $1$). $\blacksquare$

### Step 1: Reduction to per-prime exponent vectors

**Lemma 1.** For $m,n\in\mathbb Z_{>0}$, prime $p$, $\alpha=v_p(m)$, $\beta=v_p(n)$:
$$v_p(\gcd(m,n))=\min(\alpha,\beta), \qquad v_p(\mathrm{lcm}(m,n)/\gcd(m,n)) = |\alpha-\beta|.$$

*Proof.* The standard valuation formulas $v_q(\gcd(m,n))=\min(v_q(m),v_q(n))$,
$v_q(\mathrm{lcm}(m,n))=\max(v_q(m),v_q(n))$ for every prime $q$ follow from unique factorization
(the gcd's valuation at each prime cannot exceed the min of the two, with equality attained by
taking the min at every prime simultaneously; symmetrically for lcm and max). Apply at $q=p$; then
$v_p(\mathrm{lcm}(m,n)/\gcd(m,n))=v_p(\mathrm{lcm})-v_p(\gcd) = \max(\alpha,\beta)-\min(\alpha,\beta)=|\alpha-\beta|$
(using $v_p(A/B)=v_p(A)-v_p(B)$ when $B\mid A$). $\blacksquare$

**Consequence.** A move on positions $i,j$ transforms $(v_p(a_i),v_p(a_j))=(\alpha,\beta)$ into
$(\min(\alpha,\beta),|\alpha-\beta|)$, for every prime $p$ simultaneously, leaving all other
coordinates (of every prime's exponent vector) unchanged.

### Step 2: The Euclidean subtraction identity

**Lemma 2.** For all $\alpha,\beta\ge0$: $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$.

*Proof.* If $\alpha=\beta$: LHS $=\gcd(\alpha,0)=\alpha=\gcd(\alpha,\alpha)=$RHS. If $\alpha<\beta$
(the case $\alpha>\beta$ is symmetric): LHS $=\gcd(\alpha,\beta-\alpha)$. If $\alpha=0$ both sides
are $\beta$. If $\alpha>0$: for $d\ge1$, $d\mid\alpha,d\mid\beta-\alpha \iff d\mid\alpha,d\mid\beta$
(add/subtract $\alpha$), so the common-divisor sets of $\{\alpha,\beta-\alpha\}$ and $\{\alpha,\beta\}$
coincide, hence so do their maxima. $\blacksquare$

### Step 3: The per-prime global invariant

For a state $S$ and prime $p$, $g_p(S) := \gcd(x_p(S))$ where $x_p(S)=(v_p(a_1),\dots,v_p(a_{2026}))$.

**Lemma 3 (Invariance).** If $S'$ is obtained from $S$ by one legal move, $g_p(S')=g_p(S)$ for
every prime $p$.

*Proof.* Fix $p$; the move acts on positions $i,j$, sending $(\alpha,\beta)\mapsto(\min,|{\rm diff}|)$
(Step 1). Let $G$ be the gcd of the other $2024$ coordinates (well defined, Lemma 0, since $2026>2$
leaves a nonempty rest). By Lemma 0, $g_p(S)=\gcd(G,\gcd(\alpha,\beta))$,
$g_p(S')=\gcd(G,\gcd(\min(\alpha,\beta),|\alpha-\beta|))$; by Lemma 2 these agree. $\blacksquare$

By induction on the number of moves, $g_p(S)=g_p(S_0)$ for every state $S$ reachable from the
initial state $S_0$, for every prime $p$.

### Step 4: Termination

$\Omega(S)=\sum_i\Omega(a_i)$, $C(S)=\#\{i:a_i>1\}$, ordered lexicographically as $(\Omega,C)$.

**Lemma 4.** Every legal move strictly decreases $(\Omega,C)$ lexicographically.

*Proof.* For a move on $m,n>1$ producing $g=\gcd(m,n)$, $r=\mathrm{lcm}(m,n)/g$: for every prime
$p$, $v_p(g)+v_p(r)=\max(\alpha,\beta)\le\alpha+\beta$ with equality iff $\min(\alpha,\beta)=0$.
Summing, $\Omega(g)+\Omega(r)\le\Omega(m)+\Omega(n)$ with equality iff $\gcd(m,n)=1$.
- If $\gcd(m,n)=1$: $\Omega$ unchanged; $(g,r)=(1,mn)$, so $C$ strictly drops by $1$ (two entries
  $>1$ become one entry $1$ and one entry $mn>1$). $(\Omega,C)$ strictly decreases.
- If $\gcd(m,n)>1$: some prime $p_0\mid m,n$ makes the inequality strict at $p_0$, so
  $\Omega(g)+\Omega(r)<\Omega(m)+\Omega(n)$ strictly, so $\Omega(S')<\Omega(S)$ strictly, forcing
  strict lexicographic decrease regardless of $C$.

These two cases are exhaustive. $\blacksquare$

**Corollary (finiteness).** $(\Omega,C)\in\mathbb Z_{\ge0}\times\mathbb Z_{\ge0}$ strictly decreases
(a well-ordered set) with every move, so no infinite move sequence exists: every play terminates.

### Step 5: At least one survivor

**Lemma 5.** At a terminal state $S^*$ reached from $S_0$, $C(S^*)\ge1$.

*Proof.* Pick a prime $p_0\mid x_1$ (exists, $x_1>1$); then $v_{p_0}(x_1)>0$, so
$g_{p_0}(S_0)=\gcd(x_{p_0}(S_0))>0$ (Lemma 0'). By Step 3, $g_{p_0}(S^*)=g_{p_0}(S_0)>0$. If every
entry of $S^*$ were $=1$, $x_{p_0}(S^*)$ would be all-zero, forcing $g_{p_0}(S^*)=0$, contradiction.
So some entry of $S^*$ exceeds $1$. $\blacksquare$

### Step 6: At most one survivor

By definition, $S^*$ terminal means not $C(S^*)\ge2$, i.e. $C(S^*)\le1$.

### Step 7: Part (a)

By Step 4, any play terminates at some $S^*$; by Steps 5,6, $C(S^*)=1$ exactly. Regardless of the
sequence of moves, exactly one board entry exceeds $1$ at termination. $\blacksquare$

### Step 8: Part (b) and the closed form for $M$

At termination, let $M>1$ be the unique surviving entry (position $k$), all others $=1$. For every
prime $p$: $x_p(S^*)$ has $v_p(M)$ at slot $k$ and $0$ elsewhere, so $g_p(S^*)=v_p(M)$ (directly
from the multiset-gcd convention, whether $v_p(M)=0$ or $>0$). By Step 3,
$g_p(S^*)=g_p(S_0)=\gcd(v_p(x_1),\dots,v_p(x_{2026}))$, a quantity depending only on the initial
board. Hence
$$v_p(M) = \gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big) \quad\text{for every prime } p,$$
which (by unique factorization, $M=\prod_p p^{v_p(M)}$) determines $M$ uniquely:
$$\boxed{M = \prod_{p} p^{\gcd\left(v_p(x_1),\,\dots,\,v_p(x_{2026})\right)}}$$
(product over primes dividing some $x_i$; other primes contribute exponent $0$). Since this depends
only on $x_1,\dots,x_{2026}$ and not on the move sequence, every legal play yields the same $M$.
This proves part (b) together with the explicit closed form. $\blacksquare$

**Verification.** For $n=2$, $x_1=p^{e_1}$, $x_2=p^{e_2}$: a move replaces $(p^{e_1},p^{e_2})$ by
$(p^{\min(e_1,e_2)},p^{|e_1-e_2|})$ — the subtractive Euclidean algorithm on exponents — which
terminates at $p^{\gcd(e_1,e_2)}$, matching $M=p^{\gcd(v_p(x_1),v_p(x_2))}$. Independently verified
computationally (Monte Carlo simulation over random boards of size $2$–$6$ with all-order
enumeration for small sizes) that the unique surviving value always equals
$\prod_p p^{\gcd_i v_p(x_i)}$, for every order of moves tried.

$\blacksquare$ (Both parts (a) and (b) proved in full.)
