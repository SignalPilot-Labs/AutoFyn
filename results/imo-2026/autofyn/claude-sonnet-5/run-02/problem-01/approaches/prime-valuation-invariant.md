## Status
solved

## Approaches tried
- **Per-prime $p$-adic valuation bookkeeping (this approach).** Reduce the whole board process to
  independent one-dimensional integer sequences, one per prime, via $v_p(\gcd)=\min$,
  $v_p(\mathrm{lcm})=\max$. Track (i) a per-prime global invariant $g_p$ = gcd of the exponent
  multiset, shown constant under every move by the classical Euclidean identity
  $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$, and (ii) a lexicographic
  monovariant $(\Omega,C)$ (total prime-factor count, number of entries $>1$) forcing termination.
  **Outcome: fully successful.** Every step closes with an elementary, self-contained proof; no
  gap remains. Part (a) follows from termination + "$\ge 1$ survivor always" + "$\le 1$ survivor
  at a terminal state" $\Rightarrow$ exactly $1$. Part (b) follows by evaluating the invariant
  $g_p$ at the (now known unique-count) terminal state, which pins $v_p(M)$ to the
  move-independent quantity $g_p(\text{initial board})$ for every prime $p$, giving the closed
  form $M=\prod_p p^{\gcd_i v_p(x_i)}$.

## Current best
Complete proof below (Status: solved).

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
otherwise. This is well defined (the gcd of a nonempty finite set of positive integers is a
well-defined positive integer, by the classical existence and commutativity/associativity of the
binary $\gcd$ operation on $\mathbb Z_{>0}$, extended to $\ge 0$ by $\gcd(0,x)=x$).

**Lemma 0 (multiset-gcd well-definedness and factoring).** For $\mathbb Z_{\ge0}$ with the binary
operation $\gcd$, extended by $\gcd(0,x)=\gcd(x,0)=x$ for all $x\ge0$ (in particular
$\gcd(0,0)=0$): $\gcd$ is commutative and associative on $\mathbb Z_{\ge0}$. Consequently, for any
finite multiset $T$ partitioned as $T=T_1\sqcup T_2$, $\gcd(T)=\gcd(\gcd(T_1),\gcd(T_2))$, and this
value is independent of how $T$ is built up by repeated binary combination (any bracketing / any
order gives the same result).

*Proof.* Commutativity of ordinary $\gcd$ on $\mathbb Z_{>0}$ is standard (the set of common
divisors of $\{a,b\}$ equals that of $\{b,a\}$). For associativity, $\gcd(\gcd(a,b),c)$ and
$\gcd(a,\gcd(b,c))$ both equal, by definition, the largest positive integer dividing all three of
$a,b,c$ (a divisor argument: $d\mid \gcd(\gcd(a,b),c) \iff d\mid a,\ d\mid b,\ d\mid c$, and
symmetrically for the other bracketing; both are characterized by the same divisibility condition,
hence equal), for $a,b,c>0$. Extending to include zero entries via $\gcd(0,x)=x$ preserves
associativity and commutativity: this is a direct check of the finitely many cases where one or
more of $a,b,c$ is $0$ (e.g. $\gcd(\gcd(0,b),c)=\gcd(b,c)=\gcd(0,\gcd(b,c))$, and
$\gcd(\gcd(0,0),c)=\gcd(0,c)=c=\gcd(0,\gcd(0,c))$, etc.), so $(\mathbb Z_{\ge0},\gcd)$ is a
commutative semigroup. In a commutative semigroup, any two ways of combining a fixed finite
multiset of elements via the binary operation yield the same result (a standard consequence of
associativity + commutativity, provable by induction on the size of the multiset: for $|T|\le 2$
trivial; for $|T|\ge 3$, any full binary combination of $T$ reduces, by associativity, to combining
some element with the combination of the rest, and by the induction hypothesis the "combination of
the rest" is independent of order, and by commutativity the choice of which element is combined
last does not matter either). Hence $\gcd(T)$ (defined by that convention above as the ordinary
gcd of the nonzero elements, or $0$ if all are zero) coincides with combining all elements of $T$
pairwise in any order, which immediately gives $\gcd(T)=\gcd(\gcd(T_1),\gcd(T_2))$ for any
partition $T=T_1\sqcup T_2$. $\blacksquare$

**Lemma 0'.** If a finite multiset $T\subset\mathbb Z_{\ge0}$ contains at least one nonzero
entry, then $\gcd(T)>0$.

*Proof.* By definition, $\gcd(T)$ in this case is the gcd (in the classical sense) of the nonempty
set of positive integers $\{t\in T: t\ne0\}$, and the gcd of a nonempty set of positive integers is
itself a positive integer (it is, by definition/construction, the largest element of the nonempty
set of common divisors, which always contains $1$, hence is a nonempty set of positive integers
with a maximum). $\blacksquare$

### Step 1: Reduction to per-prime exponent vectors

Fix a prime $p$. For a state $S=(a_1,\dots,a_{2026})$, let
$$x_p(S) = \big(v_p(a_1),\dots,v_p(a_{2026})\big)\in\mathbb Z_{\ge0}^{2026}.$$

**Lemma 1.** For any $m,n\in\mathbb Z_{>0}$ and any prime $p$, with $\alpha=v_p(m)$, $\beta=v_p(n)$:
$$v_p\big(\gcd(m,n)\big)=\min(\alpha,\beta), \qquad v_p\Big(\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}\Big) = |\alpha-\beta|.$$

*Proof.* Write $m=p^\alpha m'$, $n=p^\beta n'$ with $p\nmid m'$, $p\nmid n'$. For any prime $q$,
$v_q(\gcd(m,n))=\min(v_q(m),v_q(n))$ and $v_q(\mathrm{lcm}(m,n))=\max(v_q(m),v_q(n))$: this is the
standard valuation formula for gcd/lcm, which follows directly from the definitions
($\gcd(m,n)$ is the largest integer dividing both, and by unique factorization a divisor's
valuation at each prime cannot exceed the minimum of the two valuations, with equality attained by
taking exactly the minimum at every prime simultaneously; symmetrically $\mathrm{lcm}$ takes the
maximum at every prime, being the smallest common multiple). Applying this at $q=p$ gives
$v_p(\gcd(m,n))=\min(\alpha,\beta)$ and $v_p(\mathrm{lcm}(m,n))=\max(\alpha,\beta)$. Since
$v_p$ is additive on ratios of integers whose valuation formula is defined multiplicatively (i.e.
$v_p(A/B)=v_p(A)-v_p(B)$ whenever $B\mid A$, immediate from $A=BC\Rightarrow v_p(A)=v_p(B)+v_p(C)$
and unique factorization), and $\gcd(m,n)\mid \mathrm{lcm}(m,n)$, we get
$$v_p\Big(\frac{\mathrm{lcm}(m,n)}{\gcd(m,n)}\Big) = \max(\alpha,\beta)-\min(\alpha,\beta) = |\alpha-\beta|. \qquad\blacksquare$$

**Consequence.** A move on positions $i,j$ (values $m,n$) transforms the pair of coordinates
$(v_p(m),v_p(n))=(\alpha,\beta)$ of $x_p(S)$ into $(\min(\alpha,\beta),\,|\alpha-\beta|)$, for
*every* prime $p$ simultaneously, and leaves every other coordinate of $x_p(S)$ (for every $p$)
unchanged, since the move only alters the two board entries at positions $i,j$.

### Step 2: The Euclidean subtraction identity

**Lemma 2.** For all integers $\alpha,\beta\ge0$: $\gcd\big(\min(\alpha,\beta),\,|\alpha-\beta|\big)=\gcd(\alpha,\beta)$, using the convention $\gcd(0,0)=0$, $\gcd(0,x)=x$.

*Proof.* We split into three exhaustive, mutually exclusive cases.

- **Case $\alpha=\beta$.** Then $\min(\alpha,\beta)=\alpha$ and $|\alpha-\beta|=0$. LHS
  $=\gcd(\alpha,0)=\alpha$. RHS $=\gcd(\alpha,\alpha)=\alpha$ (if $\alpha>0$, this is the ordinary
  gcd of equal integers, which is that integer; if $\alpha=0$, RHS $=\gcd(0,0)=0=\alpha$ by
  convention). So LHS $=$ RHS $=\alpha$ in this case.

- **Case $\alpha<\beta$.** Then $\min(\alpha,\beta)=\alpha$, $|\alpha-\beta|=\beta-\alpha>0$. We
  must show $\gcd(\alpha,\beta-\alpha)=\gcd(\alpha,\beta)$.
  - If $\alpha=0$: LHS $=\gcd(0,\beta)=\beta$, RHS $=\gcd(0,\beta)=\beta$. Equal.
  - If $\alpha>0$: both $\alpha,\beta>0$ (since $\beta>\alpha>0$) and $\beta-\alpha>0$, so this is
    the classical fact $\gcd(a,b)=\gcd(a,b-a)$ for positive integers $a<b$. Proof of the classical
    fact: let $d$ be any common divisor of $a$ and $b$; then $d\mid b-a$ (since $b-a$ is an integer
    combination $1\cdot b + (-1)\cdot a$), so $d$ is a common divisor of $a$ and $b-a$. Conversely
    if $d$ is a common divisor of $a$ and $b-a$, then $d \mid a+(b-a)=b$, so $d$ is a common
    divisor of $a$ and $b$. Hence the set of common divisors of $\{a,b\}$ equals the set of common
    divisors of $\{a,b-a\}$; two nonempty finite sets of positive integers with identical divisor
    sets have identical maxima, so $\gcd(a,b)=\gcd(a,b-a)$. Applying with $a=\alpha$, $b=\beta$
    gives $\gcd(\alpha,\beta)=\gcd(\alpha,\beta-\alpha)$, as required.

- **Case $\alpha>\beta$.** Symmetric to the previous case with the roles of $\alpha,\beta$
  swapped: $\min(\alpha,\beta)=\beta$, $|\alpha-\beta|=\alpha-\beta$, and by the identical argument
  (with $a=\beta$, $b=\alpha$) $\gcd(\beta,\alpha-\beta)=\gcd(\beta,\alpha)=\gcd(\alpha,\beta)$
  (using commutativity of gcd for the last equality).

These three cases exhaust all possibilities for $(\alpha,\beta)\in\mathbb Z_{\ge0}^2$ (trichotomy
of $\le$), and in each the identity holds. $\blacksquare$

### Step 3: The per-prime global invariant

For a state $S$ and a prime $p$, define $g_p(S) := \gcd\big(x_p(S)\big)$, the gcd (in the
multiset sense of the Setup) of all 2026 valuations $v_p(a_1),\dots,v_p(a_{2026})$.

**Lemma 3 (Invariance).** If $S'$ is obtained from $S$ by one legal move, then $g_p(S')=g_p(S)$
for every prime $p$.

*Proof.* Fix $p$ and let the move act on positions $i,j$ with pre-move values
$(\alpha,\beta)=(v_p(a_i),v_p(a_j))$ and post-move values
$(\alpha',\beta')=(\min(\alpha,\beta),|\alpha-\beta|)$ (Step 1). Let $T=x_p(S)$ and
$T'=x_p(S')$; these are the same multiset of 2026 numbers except that the two entries at
positions $i,j$ have changed from $\{\alpha,\beta\}$ to $\{\alpha',\beta'\}$. Write
$G := \gcd\big(T\setminus\{\alpha,\beta\text{ (positions }i,j)\}\big)$, the gcd of the other 2024
(untouched) coordinates — a well-defined element of $\mathbb Z_{\ge0}$ by Lemma 0 (if this
sub-multiset is empty this cannot occur here since $2026\ge 2$ guarantees $2024\ge0$ remaining
coordinates always exist as a well-defined, possibly-empty-only-when-total-size-is-2 multiset;
since $2026>2$, it is always nonempty and well defined by Lemma 0's construction — the point being
$2026$ plays no special role beyond being $\ge 2$, see Remark below).

By Lemma 0, splitting $T$ into "the pair at $i,j$" and "the rest":
$$g_p(S) = \gcd(T) = \gcd\big(G,\ \gcd(\alpha,\beta)\big), \qquad g_p(S') = \gcd(T') = \gcd\big(G,\ \gcd(\alpha',\beta')\big).$$
By Lemma 2, $\gcd(\alpha',\beta') = \gcd(\min(\alpha,\beta),|\alpha-\beta|) = \gcd(\alpha,\beta)$.
Substituting, $g_p(S') = \gcd(G,\gcd(\alpha,\beta)) = g_p(S)$. $\blacksquare$

**Remark (no special role for 2026).** The only place the number of board entries enters this
argument is "$2026\ge2$," used solely to ensure at least two positions exist for a move to act on
and to make sense of "the other coordinates." Nothing above (Lemma 0, 1, 2, 3) uses any property of
2026 beyond this; the same proof works verbatim for any board size $n\ge2$.

By induction on the number of moves performed (base case: $0$ moves, trivial; inductive step:
Lemma 3 applied to the last move), $g_p(S)=g_p(S_0)$ for **every** state $S$ reachable from the
initial state $S_0=(x_1,\dots,x_{2026})$ by any finite sequence of legal moves, and every prime
$p$.

### Step 4: Termination

For a state $S=(a_1,\dots,a_{2026})$ define
$$\Omega(S) = \sum_{i=1}^{2026}\Omega(a_i) \in \mathbb Z_{\ge0}, \qquad C(S) = \#\{i: a_i>1\}\in\mathbb Z_{\ge0},$$
and order pairs $(\Omega,C)\in\mathbb Z_{\ge0}\times\mathbb Z_{\ge0}$ lexicographically:
$(\Omega_1,C_1)\prec(\Omega_2,C_2)$ iff $\Omega_1<\Omega_2$, or $\Omega_1=\Omega_2$ and $C_1<C_2$.

**Lemma 4.** Every legal move strictly decreases $(\Omega,C)$ in this lexicographic order.

*Proof.* Consider a move on values $m,n>1$ producing $g=\gcd(m,n)$, $r=\mathrm{lcm}(m,n)/\gcd(m,n)$.
By Lemma 1, for every prime $p$ (with $\alpha=v_p(m)$, $\beta=v_p(n)$):
$$v_p(g)+v_p(r) = \min(\alpha,\beta) + |\alpha-\beta| = \max(\alpha,\beta) \le \alpha+\beta = v_p(m)+v_p(n),$$
with equality iff $\min(\alpha,\beta)=0$, i.e. iff $p$ does not divide both $m$ and $n$. Summing
over all primes $p$:
$$\Omega(g)+\Omega(r) = \sum_p \max(v_p(m),v_p(n)) \le \sum_p \big(v_p(m)+v_p(n)\big) = \Omega(m)+\Omega(n),$$
with equality iff $\min(v_p(m),v_p(n))=0$ for **every** prime $p$, i.e. iff $\gcd(m,n)=1$. This
gives two exhaustive, mutually exclusive cases, according to $\gcd(m,n)=1$ or $\gcd(m,n)>1$:

- **Case $\gcd(m,n)=1$.** Then $\Omega(g)+\Omega(r)=\Omega(m)+\Omega(n)$, so all other entries of
  the board being unchanged, $\Omega(S')=\Omega(S)$ (equal total). Also $g=\gcd(m,n)=1$ and
  $r = \mathrm{lcm}(m,n)/1 = mn$. Before the move, both touched positions held values $m,n>1$,
  contributing $2$ to $C(S)$. After the move they hold $g=1$ (not counted) and $r=mn>1$ (since
  $m,n>1\Rightarrow mn>1$; counted), contributing $1$ to $C(S')$. All untouched positions
  contribute identically to $C(S)$ and $C(S')$. Hence $C(S')=C(S)-1<C(S)$, while
  $\Omega(S')=\Omega(S)$. So $(\Omega(S'),C(S')) \prec (\Omega(S),C(S))$ lexicographically (equal
  first coordinate, strictly smaller second).
- **Case $\gcd(m,n)>1$.** Then some prime $p_0$ divides both $m,n$, i.e.
  $\min(v_{p_0}(m),v_{p_0}(n))>0$, so for that prime the inequality
  $v_{p_0}(g)+v_{p_0}(r)\le v_{p_0}(m)+v_{p_0}(n)$ above is strict. Since all other primes
  contribute a $\le$ inequality (possibly equality) to the same sum, the total sum inequality
  $\Omega(g)+\Omega(r) < \Omega(m)+\Omega(n)$ is strict. Hence $\Omega(S') = \Omega(S) -
  \big[(\Omega(m)+\Omega(n))-(\Omega(g)+\Omega(r))\big] < \Omega(S)$ strictly (all other board
  entries unchanged so contribute identically to both sums). Thus $\Omega(S')<\Omega(S)$, which by
  itself gives $(\Omega(S'),C(S'))\prec(\Omega(S),C(S))$ lexicographically, regardless of how
  $C$ changes.

These two cases are exhaustive ($\gcd(m,n)=1$ or $\gcd(m,n)>1$ partitions all possibilities, since
$m,n\ge1$ always have $\gcd(m,n)\ge1$) and disjoint, and in both, $(\Omega,C)$ strictly decreases
lexicographically. $\blacksquare$

**Corollary (finiteness).** Since $(\Omega(S),C(S))\in\mathbb Z_{\ge0}\times\mathbb Z_{\ge0}$ for
every reachable state $S$, and this pair strictly decreases (in the well-order on
$\mathbb Z_{\ge0}\times\mathbb Z_{\ge0}$ given by the lexicographic order, which is a well-order
since it is a lexicographic product of two well-orders) with every move, there can be no infinite
strictly decreasing sequence of such pairs (a well-ordered set admits no infinite strictly
descending chain, by definition of well-order). Hence any sequence of legal moves starting from
$S_0$ must terminate after finitely many moves, i.e. reach a state $S^*$ from which no legal move
is possible (equivalently, $C(S^*)\le1$).

### Step 5: At least one survivor at the terminal state

**Lemma 5.** Let $S^*$ be any terminal state reached from $S_0=(x_1,\dots,x_{2026})$ by a finite
legal move sequence (existing by Step 4). Then $C(S^*)\ge1$.

*Proof.* Since $x_1>1$, it has at least one prime factor; fix a prime $p_0\mid x_1$, so
$v_{p_0}(x_1)>0$. The multiset $x_{p_0}(S_0)$ then contains the nonzero entry $v_{p_0}(x_1)$, so
by Lemma 0', $g_{p_0}(S_0)=\gcd(x_{p_0}(S_0))>0$.

By Step 3 (invariance, applied along the specific move sequence from $S_0$ to $S^*$),
$g_{p_0}(S^*)=g_{p_0}(S_0)>0$. If every board entry of $S^*$ were $\le1$ (equivalently $=1$, since
all board entries are always positive integers arising from gcd/lcm of positive integers, hence
$\ge1$), then $v_{p_0}(a)=0$ for every entry $a$ of $S^*$, making $x_{p_0}(S^*)$ the all-zero
multiset, forcing $g_{p_0}(S^*)=0$ by the definition of the multiset-gcd convention — contradicting
$g_{p_0}(S^*)>0$. Hence some entry of $S^*$ is $>1$, i.e. $C(S^*)\ge1$. $\blacksquare$

### Step 6: At most one survivor at a terminal state

By definition, $S^*$ is terminal precisely when no legal move is available, i.e. it is *not* the
case that at least two entries exceed $1$ (a move requires selecting two such entries). Hence
$C(S^*)\le1$.

### Step 7: Proof of part (a)

Let $S_0=(x_1,\dots,x_{2026})$ with all $x_i>1$, and consider any sequence of legal moves. By Step
4, the process must terminate after finitely many moves, reaching some state $S^*$ with no legal
move available. By Step 6, $C(S^*)\le1$; by Step 5, $C(S^*)\ge1$. Hence $C(S^*)=1$ exactly: **at
termination, exactly one board entry exceeds $1$**, regardless of the sequence of moves chosen.
This proves part (a). $\blacksquare$

### Step 8: Proof of part (b) and the closed form for $M$

Fix any legal move sequence starting from $S_0$; by part (a) it terminates at a state $S^*$ with a
unique index $k$ such that the entry at position $k$, call it $M>1$, and all other entries equal
$1$.

For every prime $p$: the multiset $x_p(S^*)$ consists of $v_p(M)$ in the slot corresponding to
position $k$, and $v_p(1)=0$ in every other slot (since $v_p(1)=0$ for all $p$). Hence, by
definition of the multiset-gcd convention (Setup): if $v_p(M)=0$, $x_p(S^*)$ is all-zero so
$g_p(S^*)=0=v_p(M)$; if $v_p(M)>0$, $x_p(S^*)$ has exactly one nonzero entry $v_p(M)$, so
$g_p(S^*) = \gcd(\{v_p(M)\}) = v_p(M)$ (the gcd of a singleton positive integer, in the classical
sense, is that integer itself). In both cases,
$$g_p(S^*) = v_p(M) \quad\text{for every prime } p. \tag{$\ast$}$$

By Step 3, $g_p(S^*) = g_p(S_0) = \gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big)$ for every prime $p$,
where the right-hand side depends **only on the initial board** $S_0$, not on which moves were
made to reach $S^*$. Combining with $(\ast)$:
$$v_p(M) = \gcd\big(v_p(x_1),\dots,v_p(x_{2026})\big) \qquad \text{for every prime } p. \tag{$\ast\ast$}$$

The right-hand side of $(\ast\ast)$ is a fixed nonnegative integer depending only on $x_1,\dots,x_{2026}$
and $p$, independent of any choice made during the process. A positive integer is uniquely
determined by the collection of all its prime valuations (the fundamental theorem of arithmetic:
$M = \prod_p p^{v_p(M)}$, the product taken over the finitely many primes with $v_p(M)>0$). Hence
$(\ast\ast)$ determines $M$ completely and uniquely as
$$\boxed{M = \prod_{p} p^{\gcd\left(v_p(x_1),\,\dots,\,v_p(x_{2026})\right)}}$$
where the product ranges over primes $p$ dividing at least one $x_i$ (primes $p$ dividing none of
the $x_i$ have $v_p(x_i)=0$ for all $i$, so by the multiset-gcd convention
$\gcd(v_p(x_1),\dots,v_p(x_{2026}))=0$ and contribute the factor $p^0=1$, i.e. do not affect the
product — so the product may equivalently, and more precisely, be written over that restricted
set of primes without changing the value).

Since this value depends only on $x_1,\dots,x_{2026}$ (the fixed initial data) — and not on the
particular legal move sequence used, nor on which state $S^*$ or index $k$ arose from it — every
legal play of the process yields the **same** value $M$. This proves part (b), together with the
explicit closed-form formula for $M$.

### Verification (sanity check of the closed form)

As a direct consistency check: taking the initial board with all $x_i$ equal to a fixed prime
power $p^{e}$ (a degenerate/no-move-needed board is not required by the problem, but consider two
values $x_1=p^{e_1}$, $x_2=p^{e_2}$, $e_1\le e_2$, with all other $x_i=p^{e_1}$ say — or more
simply, the two-value case $n=2$, $x_1=p^{e_1}$, $x_2=p^{e_2}$): a single move replaces
$(p^{e_1},p^{e_2})$ with $(\gcd,\mathrm{lcm}/\gcd) = (p^{\min(e_1,e_2)}, p^{|e_1-e_2|})$; iterating
this is precisely the subtractive Euclidean algorithm on exponents $(e_1,e_2)$, which is classically
known to terminate at $(\gcd(e_1,e_2),0)$, i.e. surviving value $p^{\gcd(e_1,e_2)}$ — matching the
formula $M=p^{\gcd(v_p(x_1),v_p(x_2))}$ exactly, confirming the general argument on this concrete
family (the general multi-prime, multi-board-entry case is handled in full by Steps 1–8 above,
this is only an illustrative special-case check, not part of the proof itself). $\blacksquare$

## Promotable lemmas

- **Lemma 0 / 0' (multiset-gcd on $\mathbb Z_{\ge0}$: well-definedness, associativity/commutativity
  via semigroup structure, and positivity when a nonzero entry is present).** Proved in full above
  (Setup + Step 3 prelude). Reusable by any approach needing "gcd of a multiset" as a rigorous
  primitive (e.g. relevant to `confluence-newman`'s 3-variable identity, which is the $n=3$
  specialization of this same lemma).
- **Lemma 1 (valuation formula for $\gcd$/$\mathrm{lcm}$ of two integers: $v_p(\gcd(m,n))=\min$,
  $v_p(\mathrm{lcm}(m,n))=\max$, hence $v_p(\mathrm{lcm}(m,n)/\gcd(m,n))=|v_p(m)-v_p(n)|$).** Proved
  in full in Step 1. Standard but fully derived here; reusable anywhere the problem's move
  operation needs to be translated into per-prime exponent arithmetic.
- **Lemma 2 (Euclidean subtraction identity $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$
  for $\alpha,\beta\ge0$, including the $\alpha=\beta=0$ boundary).** Proved in full in Step 2 by
  exhaustive case split. This is the core arithmetic engine also needed (as the $n=3$-variable
  case) by `confluence-newman`'s local-confluence step; can be cited/imported directly rather than
  re-derived.
- **Lemma 3 (per-prime multiset-gcd invariance under the board move).** Proved in full in Step 3,
  using Lemma 0 + Lemma 2. This is the paper's main invariant and could be certified as a
  standalone reusable lemma for this problem.
- **Lemma 4 + Corollary (lexicographic $(\Omega,C)$ strict descent $\Rightarrow$ termination).**
  Proved in full in Step 4. Directly reusable by `confluence-newman`, which imports this same
  termination monovariant per the outline review.
