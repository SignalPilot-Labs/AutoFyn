# IMO 2026 Problem 1 — Confucius's GCD/LCM Blackboard Problem

*A polished write-up of the solution recorded (in contract form) in
`results/imo-2026-01.md`, Status: **solved**. No mathematical content is
changed here; this is a presentation companion with a plain-language summary
and commentary.*

## Problem Statement

There are $2026$ integers greater than $1$ written on a blackboard, not
necessarily different. In a move, Confucius chooses two integers $m>1$ and
$n>1$ from different places on the blackboard and replaces these two integers
with $\gcd(m,n)$ and $\dfrac{\operatorname{lcm}(m,n)}{\gcd(m,n)}$. He continues
to make moves while it is possible to do so.

**(a)** Prove that, regardless of the choices of Confucius, after finitely
many moves, exactly one integer $M$ on the blackboard is greater than $1$.

**(b)** Prove that the value of $M$ does not depend on the choices of
Confucius.

(Source: IMO 2026, Problem 1; `problem_id = imo-2026-01` in this repository's
benchmark, `problems.jsonl`.)

## Key Idea

Three ideas, in this order, drive the whole solution.

1. **Translate the move into exponents (a change of coordinates).** Writing
   each number via its prime factorization and tracking, for each prime $p$
   separately, the exponent (the **$p$-adic valuation** $v_p$) of every entry,
   the identities $v_p(\gcd(m,n))=\min(v_p(m),v_p(n))$ and
   $v_p(\operatorname{lcm}(m,n))=\max(v_p(m),v_p(n))$ turn the board's
   multiplicative move
   $$(m,n)\ \longmapsto\ \Bigl(\gcd(m,n),\ \operatorname{lcm}(m,n)/\gcd(m,n)\Bigr)$$
   into, independently at every prime $p$, the purely additive move on
   exponents
   $$(x,y)\ \longmapsto\ \bigl(\min(x,y),\ |x-y|\bigr).$$
   This is the single reformulation that makes everything else tractable: a
   messy multiplicative process on $2026$ integers becomes infinitely many
   independent (but structurally identical) processes on pairs of
   non-negative integers, one per prime.

2. **A monovariant to force the process to stop.** There is no a priori bound
   on how many moves Confucius could make, so termination needs proof. Neither
   "the product of all board entries" nor "the count of entries $>1$" shrinks
   on *every* move (each has moves on which it stalls) — but their combination
   $\Psi = \bigl(\prod_i x_i\bigr)\cdot 2^{\#\{i:\,x_i>1\}}$ strictly
   decreases, and at least halves, on *every* legal move. Since $\Psi$ is
   always a positive integer, it cannot decrease forever, so the process must
   halt.

3. **An invariant to pin down the halting state.** At each prime independently,
   the exponent move $(x,y)\mapsto(\min(x,y),|x-y|)$ is exactly one step of
   the subtractive Euclidean algorithm, which is well known to preserve
   $\gcd(x,y)$. Extending this from a single pair to all $2026$ entries at
   once produces a genuine process invariant,
   $$\Gamma(x_1,\dots,x_{2026}) \;=\; \prod_{p}\ p^{\,\gcd\left(v_p(x_1),\dots,v_p(x_{2026})\right)},$$
   which is *exactly preserved* by every move, from the very first board to
   the very last. Reading $\Gamma$ off the terminal board (where it collapses
   to $M$ itself) and off the initial board (where it is a fixed function of
   the given numbers) simultaneously (i) rules out total collapse to all
   $1$'s, closing part (a), and (ii) gives the closed form of $M$, closing
   part (b).

The rest of this document gives the complete, rigorous argument built on
these three ideas, followed by a commentary section.

---

## Setup, Model, and Notation

Throughout, let $N = 2026$. Model the blackboard as an ordered $N$-tuple
$(x_1,\dots,x_N)$ of positive integers, where position $i$ holds the value
$x_i$. Initially every $x_i > 1$. A **move** chooses two *distinct* positions
$i \ne j$ whose current values $m := x_i$ and $n := x_j$ both satisfy $m>1$ and
$n>1$, and replaces the pair $(m,n)$ occupying those two positions by
$$
g := \gcd(m,n), \qquad h := \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)},
$$
leaving all other $N-2$ positions unchanged. (Lemma B below shows $g \mid
\operatorname{lcm}(m,n)$, so $h$ is a positive integer, and the move is
well-defined.) Which of $g,h$ is written at position $i$ and which at $j$ will
never matter, because every quantity we track is symmetric in the two touched
positions. A move is **legal** exactly while it is possible to make one, i.e.
while at least two positions hold values $> 1$. The board is **terminal** when
no legal move remains, i.e. when at most one position holds a value $> 1$.

**Notation and conventions.**

- For a prime $p$ and a positive integer $k$, $v_p(k)$ is the exponent of $p$
  in the prime factorization of $k$ (the **$p$-adic valuation**); thus
  $v_p(1)=0$, and $v_p(k) \ge 1$ for at least one prime $p$ whenever $k>1$.
- For a finite list of non-negative integers $a_1,\dots,a_r$,
  $\gcd(a_1,\dots,a_r)$ denotes their greatest common divisor under the
  standard conventions $\gcd(a,0)=a$ and $\gcd(0,\dots,0)=0$. Because every
  integer divides $0$, the gcd is characterized by the universal property
  $$
  (\ast)\qquad d \mid \gcd(a_1,\dots,a_r)\iff d\mid a_i\text{ for every }i,
  \qquad\text{for every integer } d\ge 1 .
  $$
  (When some $a_i>0$, the common divisors of the list form a finite nonempty
  set of positive integers with maximum $\gcd$; when all $a_i=0$, both sides
  of $(\ast)$ hold for every $d\ge1$ and $\gcd=0$. In particular, if some
  $a_i \ge 1$ then $\gcd(a_1,\dots,a_r) \ge 1$.)

We first assemble a prime-valuation toolkit (Lemmas A–F), then build the two
process invariants (Lemmas G, H), then prove parts (a) and (b).

---

## Part 1: A Prime-Valuation Toolkit

### Lemma A (Unique factorization / valuation basics)

*Every positive integer $k$ has $k = \prod_p p^{v_p(k)}$ (a finite product,
all but finitely many exponents zero). For positive integers $a,b$:
$v_p(ab)=v_p(a)+ v_p(b)$; if $b\mid a$ then $v_p(a/b)=v_p(a)-v_p(b)$; and $b
\mid a \iff v_p(b)\le v_p(a)$ for every prime $p$. Consequently two positive
integers are equal iff they have the same $p$-adic valuation at every prime.*

**Proof.** These are the standard consequences of the **Fundamental Theorem of
Arithmetic** (unique factorization into primes), the "$v_p$ count" tool in
`knowledge_base.md` (Number Theory; Meta-Strategy "a multiplicity or $v_p$
count"). Existence and uniqueness of the factorization give the product
formula and the additivity $v_p(ab)=v_p(a)+v_p(b)$ directly by collecting
powers of each prime. If $b\mid a$, write $a=bc$ with $c$ a positive integer;
then $v_p(a)=v_p(b)+v_p(c)$, so $v_p(c)=v_p(a)-v_p(b)\ge 0$ for all $p$, giving
$v_p(a/b)=v_p(a)-v_p(b)$. For divisibility: if $b\mid a$ then $v_p(b)\le
v_p(a)$ for all $p$ by the previous line; conversely if $v_p(b)\le v_p(a)$ for
all $p$, then $a/b := \prod_p p^{\,v_p(a)-v_p(b)}$ is a positive integer with
$b\cdot(a/b)=a$, so $b\mid a$. Finally, if $v_p(a)=v_p(b)$ for all $p$ then
$a=\prod_p p^{v_p(a)}=\prod_p p^{v_p(b)}=b$. $\blacksquare$

### Lemma B (Valuations of gcd and lcm; the valuation transform)

*For all positive integers $m,n$ and every prime $p$,*
$$
v_p(\gcd(m,n)) = \min\bigl(v_p(m),v_p(n)\bigr), \qquad
v_p(\operatorname{lcm}(m,n)) = \max\bigl(v_p(m),v_p(n)\bigr).
$$
*In particular $\gcd(m,n) \mid \operatorname{lcm}(m,n)$, so
$h=\operatorname{lcm}(m,n)/\gcd(m,n)$ is a positive integer, and writing
$x=v_p(m),\ y=v_p(n)$,*
$$
v_p(g)=\min(x,y),\qquad v_p(h)=v_p\!\left(\tfrac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)=\max(x,y)-\min(x,y)=|x-y|.
$$

**Proof.** Put $D := \prod_p p^{\min(v_p(m),v_p(n))}$ (a finite product, hence
a positive integer). For every prime $p$, $v_p(D)=\min(v_p(m),v_p(n))\le
v_p(m)$ and $\le v_p(n)$, so by Lemma A $D\mid m$ and $D\mid n$; thus $D$ is a
common divisor of $m,n$. Conversely, if $d\mid m$ and $d\mid n$ then
$v_p(d)\le v_p(m)$ and $v_p(d)\le v_p(n)$ for all $p$ (Lemma A), hence
$v_p(d)\le \min(v_p(m),v_p(n))=v_p(D)$, so $d\mid D$. Therefore $D$ is the
greatest common divisor: $\gcd(m,n)=D$ and
$v_p(\gcd(m,n))=\min(v_p(m),v_p(n))$. The identical argument with $\max$ in
place of $\min$, "multiple" in place of "divisor", and $\mid$ reversed, shows
$\operatorname{lcm}(m,n)=\prod_p p^{\max(v_p(m),v_p(n))}$, so
$v_p(\operatorname{lcm}(m,n))=\max(v_p(m),v_p(n))$. Since $\min\le\max$ at
every prime, $v_p(\gcd)\le v_p(\operatorname{lcm})$ for all $p$, so
$\gcd(m,n)\mid\operatorname{lcm}(m,n)$ by Lemma A, and $h$ is a positive
integer. Finally, using $v_p(h)=v_p(\operatorname{lcm})-v_p(\gcd)$ (Lemma A,
since $\gcd\mid\operatorname{lcm}$), $v_p(h)=\max(x,y)-\min(x,y)=|x-y|$.
$\blacksquare$

This valuation transform — reading the multiplicative gcd/lcm move as, at
each prime $p$ independently, the map $(x,y)\mapsto(\min(x,y),\,|x-y|)$ on the
exponents — is the central reformulation ("Reformulate: translate to another
domain", `knowledge_base.md` Problem-Solving Heuristics). It decouples the
whole problem into one additive problem per prime.

### Lemma C (gcd·lcm product identity)

*For all positive integers $m,n$: $\gcd(m,n)\cdot\operatorname{lcm}(m,n)=mn$.
Equivalently $g\cdot h=\operatorname{lcm}(m,n)=mn/g$.*

**Proof.** For every prime $p$, by Lemma B,
$$
v_p(\gcd(m,n))+v_p(\operatorname{lcm}(m,n))
=\min(v_p(m),v_p(n))+\max(v_p(m),v_p(n))
=v_p(m)+v_p(n)=v_p(mn),
$$
using that $\min(x,y)+\max(x,y)=x+y$ for any reals, and $v_p(mn)=v_p(m)+v_p(n)$
(Lemma A). Two positive integers with equal valuation at every prime are equal
(Lemma A), so $\gcd(m,n)\cdot\operatorname{lcm}(m,n)=mn$. Rearranging,
$g\cdot h=\gcd(m,n)\cdot\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}
=\operatorname{lcm}(m,n)=\frac{mn}{\gcd(m,n)}=\frac{mn}{g}$. $\blacksquare$

### Lemma D (Squeeze Lemma)

*For positive integers $m,n$, $\gcd(m,n)\le\operatorname{lcm}(m,n)$, with
equality iff $m=n$. Consequently, if $m\ne n$ then
$\gcd(m,n)<\operatorname{lcm}(m,n)$, and
$h=\operatorname{lcm}(m,n)/\gcd(m,n)\ge 2$.*

**Proof.** Since $\gcd(m,n)$ divides $m$ and $m$ divides
$\operatorname{lcm}(m,n)$ (gcd is a common divisor, lcm is a common multiple),
we have $\gcd(m,n)\mid \operatorname{lcm}(m,n)$, hence
$\gcd(m,n)\le\operatorname{lcm}(m,n)$ (both positive). If $m=n$ then
$\gcd(m,m)=m=\operatorname{lcm}(m,m)$, giving equality. Conversely, suppose
$\gcd(m,n)=\operatorname{lcm}(m,n)$. From the divisibility chain
$\gcd(m,n)\mid m\mid\operatorname{lcm}(m,n)=\gcd(m,n)$ we get $m\mid
\gcd(m,n)$ and $\gcd(m,n)\mid m$, so $m=\gcd(m,n)$ (mutual divisibility of
positive integers). Symmetrically $\gcd(m,n)\mid n\mid\operatorname{lcm}(m,n)=
\gcd(m,n)$ gives $n=\gcd(m,n)$. Hence $m=\gcd(m,n)=n$, i.e. $m=n$. This proves
the equivalence. If $m\ne n$, equality fails, so $\gcd(m,n)<\operatorname{lcm}
(m,n)$; and since $h=\operatorname{lcm}(m,n)/\gcd(m,n)$ is a positive integer
(Lemma B) strictly greater than $1$, we have $h\ge 2$. $\blacksquare$

### Lemma E (Subtraction / Euclid-step Lemma)

*For all integers $x,y\ge 0$, $\ \gcd\bigl(\min(x,y),\,|x-y|\bigr)=\gcd(x,y)$.*

**Proof.** Both sides are symmetric in $x,y$ (swapping $x,y$ fixes $\min(x,y)$
and $|x-y|$, and $\gcd$ is symmetric), so we may assume $x\ge y\ge 0$; then
$\min(x,y)=y$ and $|x-y|=x-y\ge 0$. We show the pairs $\{x,y\}$ and $\{y,\,
x-y\}$ have exactly the same positive common divisors. For any integer $d\ge
1$: if $d\mid x$ and $d\mid y$, then $d\mid(x-y)$ (a $\mathbb Z$-linear
combination of $x,y$), so $d$ divides both $y$ and $x-y$; conversely, if
$d\mid y$ and $d\mid(x-y)$, then $d\mid\bigl((x-y)+y\bigr)=x$, so $d$ divides
both $x$ and $y$. Hence the two pairs share identical sets of positive common
divisors. If $(x,y)\ne(0,0)$, at least one entry of each pair is positive, so
each gcd equals the maximum of this common set, and the two maxima agree; if
$x=y=0$, both sides equal $\gcd(0,0)=0$. In every case
$\gcd(\min(x,y),|x-y|)=\gcd(x,y)$. (This is one step of the subtractive
Euclidean algorithm.) $\blacksquare$

### Lemma F (Grouping Lemma)

*Let $a_1,\dots,a_N$ be nonnegative integers and $i\ne j$ two indices. Form
the $(N-1)$-element list obtained by deleting $a_i,a_j$ and appending the
single value $\gcd(a_i,a_j)$. Then this list has the same gcd as the
original:*
$$
\gcd(a_1,\dots,a_N)=\gcd\Bigl(\gcd(a_i,a_j),\ \{a_k\}_{k\ne i,j}\Bigr).
$$

**Proof.** For any integer $d\ge 1$, the universal property $(\ast)$ of gcd
gives $d\mid a_i$ and $d\mid a_j\iff d\mid\gcd(a_i,a_j)$. Hence
$$
d\mid a_k\ \text{for all }k
\iff \bigl(d\mid a_i\text{ and }d\mid a_j\text{ and }d\mid a_k\ \forall k\ne i,j\bigr)
\iff \bigl(d\mid\gcd(a_i,a_j)\text{ and }d\mid a_k\ \forall k\ne i,j\bigr),
$$
i.e. $d$ divides every entry of the original list iff $d$ divides every entry
of the regrouped list. Thus the two lists have the same positive common
divisors, and (arguing as in Lemma E: their common gcd is the maximum of that
common set when not all entries vanish, and is $0$ when all entries vanish)
the same gcd. $\blacksquare$

---

## Part 2: The Invariant $\Gamma$ and the Monovariant $\Psi$

We now define the two quantities tracked through the process.

**Definition of $\Gamma$.** For a board $y=(y_1,\dots,y_N)$ of positive
integers and a prime $p$, set
$$
\gamma_p(y):=\gcd\bigl(v_p(y_1),\dots,v_p(y_N)\bigr)\ \ (\ge 0),
\qquad
\Gamma(y):=\prod_{p\ \text{prime}} p^{\,\gamma_p(y)} .
$$
*$\Gamma(y)$ is a well-defined positive integer.* Only finitely many primes
divide any single $y_i$, so only finitely many primes divide some $y_i$; for
every other prime $p$ we have $v_p(y_i)=0$ for all $i$, hence
$\gamma_p(y)=\gcd(0,\dots,0)=0$ and the factor $p^{0}=1$. Thus the product is
really a finite product of positive integers, so $\Gamma(y)$ is a positive
integer (and $\ge 1$).

**Definition of $\Psi$.** For a board $y=(y_1,\dots,y_N)$, set
$$
\Phi(y):=\prod_{i=1}^N y_i,\qquad
c(y):=\#\{\,i: y_i>1\,\},\qquad
\Psi(y):=\Phi(y)\cdot 2^{\,c(y)} .
$$
Each $y_i$ is a positive integer, so $\Phi(y)\ge 1$; and $2^{c(y)}\ge 1$;
hence $\Psi(y)$ is a positive integer, $\Psi(y)\ge 1$.

### Lemma G ($\Gamma$-invariance)

*A single legal move leaves $\Gamma$ unchanged. Consequently, along any finite
sequence of legal moves, $\Gamma$ of the board never changes; in particular
$\Gamma(\text{final board})=\Gamma(\text{initial board})$ for any play that
reaches a terminal board.*

**Proof.** Consider one legal move at positions $i\ne j$, with old values
$m=y_i,\ n=y_j$ replaced by $g=\gcd(m,n)$ and $h=\operatorname{lcm}(m,n)/
\gcd(m,n)$ (in either order at the two positions); all other positions are
unchanged. Fix a prime $p$ and write $x=v_p(m),\ y=v_p(n)$. By Lemma B, after
the move the valuations at positions $i,j$ are $\min(x,y)$ and $|x-y|$ (in the
corresponding order). Apply the Grouping Lemma (Lemma F) to the two touched
positions, both before and after the move:
$$
\gamma_p(\text{before})=\gcd\Bigl(\gcd(x,y),\ \{v_p(y_k)\}_{k\ne i,j}\Bigr),
\qquad
\gamma_p(\text{after})=\gcd\Bigl(\gcd(\min(x,y),|x-y|),\ \{v_p(y_k)\}_{k\ne i,j}\Bigr).
$$
The untouched entries $\{v_p(y_k)\}_{k\ne i,j}$ are literally identical on
both sides, and by the Subtraction Lemma (Lemma E, valid since $x,y\ge 0$)
$\gcd(\min(x,y),|x-y|)=\gcd(x,y)$. Hence $\gamma_p(\text{after})=
\gamma_p(\text{before})$. This holds for every prime $p$ (note the symmetry
in $i,j$ makes the placement of $g,h$ irrelevant), so
$\Gamma(\text{after})=\prod_p p^{\gamma_p(\text{after})}=\prod_p
p^{\gamma_p(\text{before})}=\Gamma(\text{before})$.

For a finite sequence of moves we induct on the number of moves $t$. For
$t=0$ there is nothing to prove. If $\Gamma$ is unchanged after $t$ moves and
one more legal move is made, the single-move statement just proved gives that
$\Gamma$ is unchanged after $t+1$ moves. Hence $\Gamma$ is constant along any
finite play. This argument uses nothing about whether or when the process
terminates, so it is valid as stated. $\blacksquare$

### Lemma H ($\Psi$-descent)

*On every legal move, $\Phi_{\mathrm{new}}=\Phi_{\mathrm{old}}/g$, and*
$$
\Psi_{\mathrm{new}}\le\tfrac12\,\Psi_{\mathrm{old}} .
$$
*Moreover, whenever a move is legal, $\Psi_{\mathrm{old}}\ge 4$, so this is a
strict decrease $\Psi_{\mathrm{new}}<\Psi_{\mathrm{old}}$ of positive
integers.*

**Proof.** A move replaces $m,n$ (with $m,n>1$) at positions $i,j$ by $g,h$,
and leaves the other $N-2$ entries fixed. By Lemma C, $g\cdot h=
\operatorname{lcm}(m,n)=mn/g$, so
$$
\Phi_{\mathrm{new}}=\Phi_{\mathrm{old}}\cdot\frac{g\cdot h}{m\cdot n}
=\Phi_{\mathrm{old}}\cdot\frac{mn/g}{mn}
=\frac{\Phi_{\mathrm{old}}}{g}.
$$
Only the two touched positions can change the count $c$; the change $\Delta
c:= c_{\mathrm{new}}-c_{\mathrm{old}}$ is determined by how many of $g,h$
exceed $1$, minus $2$ (both $m,n$ exceeded $1$). We split into three cases
according to the *exact boolean conditions* on $(m,n)$ (both $>1$):

- **Case (i): $g=1$.** Then $h=\operatorname{lcm}(m,n)/1=\operatorname{lcm}
  (m,n)$, and by Lemma C, $g\cdot h = mn$, so $h=mn>1$ (as $m,n>1$). The new
  pair is $\{g,h\}=\{1,\ mn\}$: exactly one entry $>1$, so $\Delta c=1-2=-1$.
  Here $\Phi_{\mathrm{new}}=\Phi_{\mathrm{old}}/g=\Phi_{\mathrm{old}}$, so
  $$
  \Psi_{\mathrm{new}}=\Phi_{\mathrm{old}}\cdot 2^{\,c_{\mathrm{old}}-1}
  =\tfrac12\,\Psi_{\mathrm{old}}.
  $$

- **Case (ii): $g>1$ and $m=n$.** (Consistent: $m=n>1\Rightarrow
  g=\gcd(m,m)=m>1$; this case is exactly "$m=n$".) By Lemma D, $m=n$ gives
  $\operatorname{lcm}(m,n)=\gcd(m,n)=g$, so $h=\operatorname{lcm}(m,n)/g=1$.
  The new pair is $\{g,h\}=\{m,\ 1\}$ with $m=g>1$: exactly one entry $>1$,
  so $\Delta c=-1$. Since $\Phi_{\mathrm{new}}=\Phi_{\mathrm{old}}/g$ with
  $g=m\ge 2$,
  $$
  \Psi_{\mathrm{new}}=\frac{\Phi_{\mathrm{old}}}{g}\cdot 2^{\,c_{\mathrm{old}}-1}
  =\frac{\Psi_{\mathrm{old}}}{2g}\le\tfrac14\,\Psi_{\mathrm{old}}
  \le\tfrac12\,\Psi_{\mathrm{old}}.
  $$

- **Case (iii): $g>1$ and $m\ne n$.** By Lemma D (Squeeze), $m\ne n$ gives
  $h=\operatorname{lcm}(m,n)/\gcd(m,n)\ge 2>1$; and $g>1$. So both new entries
  exceed $1$: $\Delta c=2-2=0$. Since $\Phi_{\mathrm{new}}=\Phi_{\mathrm{old}}/g$
  with $g\ge 2$,
  $$
  \Psi_{\mathrm{new}}=\frac{\Phi_{\mathrm{old}}}{g}\cdot 2^{\,c_{\mathrm{old}}}
  =\frac{\Psi_{\mathrm{old}}}{g}\le\tfrac12\,\Psi_{\mathrm{old}}.
  $$

*These three cases are exhaustive and pairwise disjoint.* Any pair $(m,n)$
with $m,n>1$ has either $g=1$ (case i) or $g>1$; if $g>1$, then either $m=n$
(case ii) or $m\ne n$ (case iii). The combination "$g=1$ and $m=n$" cannot
occur, since $m=n>1\Rightarrow g=m>1\ne 1$; so the three conditions
$\{g=1\},\{g>1,m=n\},\{g>1,m\ne n\}$ partition all legal pairs. In every case
$\Psi_{\mathrm{new}}\le\frac12\Psi_{\mathrm{old}}$.

(The reason $\Psi=\Phi\cdot 2^c$ works while neither factor alone does: case
(i) is precisely when $\Phi$ fails to shrink — but then $c$ drops; case (iii)
is precisely when $c$ fails to shrink — but then $\Phi$ drops by a factor
$\ge2$. The two stalls are complementary, so the product always at least
halves.)

Finally, a legal move requires two distinct positions with values $>1$, so
$c_{\mathrm{old}}\ge 2$, whence
$\Psi_{\mathrm{old}}=\Phi_{\mathrm{old}}\cdot 2^{c_{\mathrm{old}}}\ge
1\cdot 2^2=4>0$. Combined with $\Psi_{\mathrm{new}}\le
\frac12\Psi_{\mathrm{old}}$ and $\Psi_{\mathrm{old}}>0$, this yields the
strict inequality $\Psi_{\mathrm{new}}<\Psi_{\mathrm{old}}$ between positive
integers. $\blacksquare$

---

## Part 3: Proof of Part (a) — Termination with Exactly One Survivor

**Step 1 — the process terminates after finitely many moves.** Consider any
sequence of legal moves. By Lemma H, each move strictly decreases the
positive integer $\Psi$: $\Psi(\text{after move})<\Psi(\text{before move})$.
A strictly decreasing sequence of positive integers must be finite — this is
the **well-ordering principle** on $\mathbb N$ (equivalently **infinite
descent**; `knowledge_base.md`, General Proof Methods, "Induction / Infinite
descent", and "Invariant / monovariant"): if the sequence of $\Psi$-values
could continue forever, its infinitely many distinct terms would form a
subset of the positive integers with no least element, which is impossible.
Concretely, since each move at least halves $\Psi$ and $\Psi\ge 1$ always,
after $t$ moves $1\le\Psi\le \Psi_0/2^{t}$, forcing $2^{t}\le\Psi_0$, i.e.
$t\le\log_2\Psi_0$, where $\Psi_0=\Psi(\text{initial board})$ is a fixed
positive integer. Hence at most $\lfloor\log_2\Psi_0\rfloor$ moves are
possible: the process halts after finitely many moves, regardless of the
choices made.

**Step 2 — at termination, $c\le 1$.** The process stops precisely when no
legal move remains. A legal move needs two distinct positions holding values
$>1$; this is possible iff $c\ge 2$. Hence at termination $c\le 1$, i.e. the
terminal board has $c\in\{0,1\}$.

**Step 3 — the terminal board cannot be all $1$'s ($c\ne 0$).** Suppose, for
contradiction, that the terminal board is $(1,1,\dots,1)$ (i.e. $c=0$). Then
$v_p(y_i)=0$ for every $i$ and every prime $p$, so $\gamma_p(\text{terminal})=
\gcd(0,\dots,0)=0$ for every prime $p$, and therefore
$$
\Gamma(\text{terminal})=\prod_p p^{0}=\prod_p 1=1 .
$$
(Here $p^0=1$ is definitional; the all-zero-exponent product is $1$, not $0$.)
On the other hand, consider the initial board $(x_1,\dots,x_N)$, all entries
$>1$. In particular $x_1>1$, so $x_1$ has some prime factor $p_0$ with
$v_{p_0}(x_1)\ge 1$. Then
$$
\gamma_{p_0}(\text{initial})=\gcd\bigl(v_{p_0}(x_1),\dots,v_{p_0}(x_N)\bigr)\ge 1,
$$
because this is a gcd of nonnegative integers whose first entry is $\ge 1$,
and a gcd of a list containing a positive term is $\ge 1$ (property $(\ast)$:
$1$ is a common divisor, so the gcd, being the greatest common divisor of a
not-all-zero list, is at least $1$). Every prime's exponent
$\gamma_p(\text{initial})\ge 0$ contributes a factor
$p^{\gamma_p(\text{initial})}\ge 1$, so dropping all factors except the one at
$p_0$ can only decrease the product:
$$
\Gamma(\text{initial})=\prod_p p^{\gamma_p(\text{initial})}
\ \ge\ p_0^{\,\gamma_{p_0}(\text{initial})}\ \ge\ p_0^{\,1}\ \ge\ 2\ >\ 1 .
$$
But the terminal board is reached from the initial board by the finite
sequence of moves of this play (Step 1), so by Lemma G ($\Gamma$-invariance)
$\Gamma(\text{terminal})=\Gamma(\text{initial})$. This gives
$$
1=\Gamma(\text{terminal})=\Gamma(\text{initial})\ge 2,
$$
a contradiction. Hence $c\ne 0$ at termination.

**Conclusion of (a).** By Steps 1–3, every play halts after finitely many
moves (Step 1) at a terminal board with $c\le 1$ (Step 2) and $c\ne 0$ (Step
3), hence $c=1$: exactly one entry $M$ on the blackboard is $>1$. This holds
regardless of Confucius's choices. $\square$

## Part 4: Proof of Part (b) — $M$ Is Independent of the Choices

Fix any complete play; by part (a) it terminates at a board with exactly one
entry $>1$, namely $M$, and the other $N-1$ entries equal to $1$. Compute
$\Gamma$ of this terminal board. For each prime $p$, the list of valuations is
$v_p(M)$ at the position holding $M$ and $0$ at the other $N-1$ positions, so
$$
\gamma_p(\text{terminal})=\gcd\bigl(v_p(M),0,\dots,0\bigr)=v_p(M),
$$
using $\gcd(a,0,\dots,0)=a$ for $a\ge 0$ (property $(\ast)$: the common
divisors of $\{v_p(M),0,\dots,0\}$ are exactly the divisors of $v_p(M)$, whose
greatest is $v_p(M)$; and if $v_p(M)=0$ both sides are $0$). Therefore, by
Lemma A,
$$
\Gamma(\text{terminal})=\prod_p p^{\,v_p(M)}=M .
$$
By Lemma G, $\Gamma$ is preserved by the whole play, so
$$
M=\Gamma(\text{terminal})=\Gamma(\text{initial})
=\prod_p p^{\ \gcd\bigl(v_p(x_1),\dots,v_p(x_N)\bigr)} .
$$
The right-hand side depends only on the initial numbers $x_1,\dots,x_N$ and
not on any choice made during the process. Since the play was arbitrary,
every legal sequence of moves ends with the **same** value
$$
\boxed{\,M=\Gamma(x_1,\dots,x_N)=\prod_p p^{\ \gcd\left(v_p(x_1),\dots,v_p(x_N)\right)}\, }.
$$
Thus $M$ does not depend on the choices of Confucius. $\square$

### Self-check of the closed form

The formula $M=\prod_p p^{\gcd_i v_p(x_i)}$ can be sanity-checked on a small
board. Take $(x_1,x_2)=(4,8)$ (the mechanism is identical for any $N$; here
$N=2$). Only the prime $p=2$ occurs, with $v_2(4)=2,\ v_2(8)=3$ and
$\gcd(2,3)=1$; every other prime contributes exponent $\gcd(0,0)=0$. So the
formula predicts $M=2^{1}=2$. Running the process directly: $(4,8)\to(\gcd=4,\
\operatorname{lcm}/\gcd=8/4=2)=(4,2)\to(\gcd=2,\ 4/2=2)=(2,2)\to(\gcd=2,\
2/2=1)=(2,1)$, which is terminal with the single value $M=2>1$. The two
agree. (For a pairwise-coprime board such as $(2,3,5,7)$, every $\gcd_i
v_p(x_i)$ equals the lone nonzero exponent $1$, so $M=2\cdot3\cdot5\cdot7=210$,
the ordinary product — consistent with the general fact that on
pairwise-coprime input nothing can be shared and the numbers merge into their
product.)

$\blacksquare$

---

## Commentary

### Why this is naturally an invariant/monovariant problem, not "standard" number theory

The problem is filed under `number_theory` in the benchmark, and it does
visibly involve $\gcd$ and $\operatorname{lcm}$ — but the proof technique
above is not multiplicative number theory in the usual sense (there is no
modular arithmetic, no prime-counting estimate, no Diophantine equation to
solve). It belongs instead to the **process / invariant–monovariant** genre:
a discrete dynamical system evolves by a local rule on a finite state (here,
an ordered tuple of $2026$ positive integers), and one is asked (i) to show
it must halt, and (ii) to show the value at which it halts is determined
already by the start. That two-part shape is exactly what such problems
always require: a **monovariant** — a quantity moving strictly in one
direction on every legal move, and bounded — certifies halting (this is
$\Psi$, Lemma H); an **invariant** — a quantity fixed by every legal move —
certifies that the halting state's key data was already fixed at the start
(this is $\Gamma$, Lemma G). Number theory enters only as the *coordinate
system* in which these two quantities become visible: the $p$-adic valuation
transform of Lemma B turns the multiplicative gcd/lcm move into, at each
prime, the additive move $(x,y)\mapsto(\min(x,y),|x-y|)$, which is
transparently one step of the Euclidean algorithm (Lemma E) — and it is only
after this translation that the invariant ($\gcd$ of exponents) and the
monovariant (the halving of $\Psi$) become simple to write down and to prove.
So the problem is number-theoretic in its *encoding* and combinatorial/
dynamical in its *proof architecture*.

### How the two parts connect

The two parts are not logically independent, and the proof structure above
makes this explicit rather than incidental. Termination via $\Psi$-descent
(Lemma H) only forces the process to stop with $c \le 1$ survivors (Step 2 of
part (a)); it does not by itself rule out $c=0$, i.e. total collapse to all
$1$'s. Ruling out $c=0$ is Step 3 of part (a), and it is proved using the
*same* invariant $\Gamma$ that part (b) needs to identify the closed form of
$M$: a collapse to all $1$'s would force $\Gamma(\text{terminal})=1$
(Lemma G, terminal case), while the hypothesis that every starting number
exceeds $1$ forces $\Gamma(\text{initial})\ge 2$ — and $\Gamma$-invariance
(Lemma G) equates the two, a contradiction. In other words, a fully rigorous
solution to part (a) already requires discovering the invariant that part (b)
is built around; the two parts share their single hardest idea, and the
write-up above accordingly proves $\Gamma$-invariance (Lemma G) once and
draws on it twice — negatively, to exclude a case in part (a), and
constructively, to compute $M$ in part (b) — rather than presenting two
unrelated arguments.

### What the closed form for $M$ concretely means

By Lemma B, the multiplicative move $(m,n)\mapsto(\gcd(m,n),
\operatorname{lcm}(m,n)/\gcd(m,n))$ becomes, prime by prime, the additive move
$(x,y)\mapsto(\min(x,y),|x-y|)$ on $p$-adic exponents, and Lemma E identifies
this exponent move as exactly one step of the subtractive Euclidean algorithm
for $\gcd(x,y)$. So, at every prime independently, repeatedly applying the
board's moves is repeatedly running the Euclidean algorithm on that prime's
exponents across all $2026$ numbers at once (via the Grouping Lemma, Lemma F,
which lets the algorithm act on two entries of an $N$-term list while leaving
the list's overall gcd unchanged); the quantity this repeated process
preserves — and hence the value it must reduce to — is the gcd of *all*
$2026$ exponents at that prime, not merely of two of them at a time.
Reassembling over all primes, $M=\prod_p p^{\gcd_i v_p(x_i)}$: the surviving
number is obtained by applying $\gcd$ "one level up," to whole vectors of
exponents rather than to the numbers themselves. This is also why $M$ is
generally *neither* $\gcd(x_1,\dots,x_{2026})$ nor
$\operatorname{lcm}(x_1,\dots,x_{2026})$: both are refuted by the explicit
example $(4,8)\mapsto M=2$ worked out in the Self-check above, since
$\gcd(4,8)=4$ and $\operatorname{lcm}(4,8)=8$, neither equal to $2$. The
closed form coincides with the ordinary product only in special cases, such
as when the $x_i$ are pairwise coprime (illustrated above with $(2,3,5,7)$,
where $M=210$): there, no two entries can ever share a prime factor, so at
each prime that divides some $x_i$, exactly one entry contributes a nonzero
valuation and the multi-argument gcd of the exponents at that prime
degenerates to that single valuation, reproducing ordinary multiplication.

### Relative difficulty

In this benchmark's own classification (`problems.jsonl`), the problem
carries `difficulty_level: medium` and `difficulty_rating: 5`, distinctly
below the `difficulty_rating: 8–10` reserved for the benchmark's "hard"
(IMO P3/P6-caliber) tier. This matches its role as an IMO **Problem 1**
(traditionally the most accessible problem on an IMO paper): once the
valuation transform (Lemma B) and the pairing of one monovariant with one
invariant ($\Psi$ and $\Gamma$) are found, every remaining step above is a
short, largely mechanical verification. No case split runs deep — the
case analysis in Lemma H has exactly three cases, each closed in a few
lines — no construction is delicate, and no auxiliary combinatorial gadget
beyond $\Psi$ and $\Gamma$ is required anywhere. The one genuine subtlety the
proof has to get right (and which an earlier drafting pass of this solution
did get wrong before correction — see `results/imo-2026-01.md`, outline-review
history) is the arithmetic of the boundary case in part (a): a terminal board
of all $1$'s has $\Gamma=1$, not $\Gamma=0$, because $p^0=1$ is definitional;
getting this the wrong way around would silently break the contradiction that
closes Step 3. Apart from that one bookkeeping trap, the main creative
content is recognizing that neither $\Phi=\prod x_i$ nor $c=\#\{x_i>1\}$
alone is monotonic (Lemma H's closing remark makes precise how each stalls
exactly when the other strictly improves, which is why their product
$\Psi=\Phi\cdot2^c$ is the right composite monovariant) — a natural, but not
deep, design step once the valuation transform is in hand.
