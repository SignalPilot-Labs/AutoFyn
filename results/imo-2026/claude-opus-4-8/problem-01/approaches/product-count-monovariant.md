# Approach: product-count-monovariant

## Status
solved

## Overall route (one-line)
Prove (a) termination with a **lexicographic** monovariant (P, C) where
P = product of ALL board entries and C = count of entries > 1: every move either
strictly shrinks P (when gcd>1) or keeps P fixed and strictly shrinks C (when
gcd=1). Prove (b) with the per-prime gcd invariant d_p = gcd(v_p(x_1),...,v_p(x_N)).

## Approaches tried
- Lexicographic (P, C) monovariant for (a) + per-prime gcd invariant for (b) —
  worked; complete proof below. Well-foundedness of lex order argued from scratch
  by infinite descent (no infinite strictly-decreasing chain), the product
  identity P_after = P_before/gcd(m,n) and the Euclidean-step valuation identity
  proven in full.

## Current best
Complete proof of both (a) and (b); see Full proof.

## Full proof

### 0. Setup, notation, and conventions

There are $N = 2026$ integers, each $> 1$, written on the blackboard. We model the
board as a *multiset* $B = \{x_1, x_2, \dots, x_N\}$ of positive integers (order
and position are irrelevant to every quantity we track). Initially every $x_i > 1$.
As the process runs, some entries may become $1$; the board always has exactly $N$
entries (a move removes two entries and writes two new ones).

**The move.** A move selects two entries $m > 1$ and $n > 1$ (from different
positions) and replaces them by
$$g := \gcd(m,n) \qquad\text{and}\qquad h := \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.$$
Confucius keeps moving while a move is possible, i.e. while at least two entries
exceed $1$.

**Prime valuations.** For a prime $p$ and a positive integer $x$, let $v_p(x)$
denote the exponent of $p$ in the prime factorization of $x$ (so $v_p(x) \ge 0$,
and $v_p(1) = 0$). We use the standard facts
$$v_p(\gcd(m,n)) = \min(v_p(m), v_p(n)), \qquad
  v_p(\operatorname{lcm}(m,n)) = \max(v_p(m), v_p(n)), \tag{V}$$
valid for all primes $p$ and all positive integers $m,n$. These are the defining
valuation formulas for gcd and lcm (see **knowledge_base.md**, "Divisor analysis:
gcd structure").

**gcd conventions.** We use $\gcd$ on any finite tuple of non-negative integers,
with the standard conventions
$$\gcd(0,k) = \gcd(k,0) = k \ (k \ge 0), \qquad \gcd(0,0) = 0, \tag{C}$$
and $\gcd$ associative and commutative: $\gcd(a,b,c) = \gcd(\gcd(a,b), c)$, etc.
(With convention (C), $\gcd(a_1,\dots,a_r)$ is the largest integer dividing every
$a_i$ when some $a_i > 0$, and is $0$ when all $a_i = 0$; associativity and
commutativity hold throughout, since $\gcd$ of a tuple equals the generator of the
ideal $a_1\mathbb Z + \cdots + a_r\mathbb Z$, which is symmetric and computable in
any grouping.)

Define the two tracked quantities on any board state $B = \{x_1,\dots,x_N\}$:
$$P(B) := \prod_{i=1}^{N} x_i \quad (\text{product of the whole board, including any } 1\text{'s}),
\qquad C(B) := \#\{\, i : x_i > 1 \,\}.$$
Since every entry is $\ge 1$, $P(B) \ge 1$ is a positive integer, and
$0 \le C(B) \le N$ is a non-negative integer.

---

### 1. Key lemma: the move product identity

**Lemma 1 (Product identity).** For a move on entries $m>1,\, n>1$ producing
$g = \gcd(m,n)$ and $h = \operatorname{lcm}(m,n)/\gcd(m,n)$, we have
$$g \cdot h = \operatorname{lcm}(m,n) = \frac{mn}{\gcd(m,n)}, \qquad\text{hence}\qquad
  g \cdot h = \frac{mn}{g}.$$

*Proof.* By definition $h = \operatorname{lcm}(m,n)/g$, so
$g \cdot h = g \cdot \operatorname{lcm}(m,n)/g = \operatorname{lcm}(m,n)$. It remains
to prove the classical identity $\operatorname{lcm}(m,n)\cdot\gcd(m,n) = mn$. Fix a
prime $p$ and write $\alpha = v_p(m),\ \beta = v_p(n)$. By (V),
$$v_p(\operatorname{lcm}(m,n)) + v_p(\gcd(m,n)) = \max(\alpha,\beta) + \min(\alpha,\beta)
  = \alpha + \beta = v_p(m) + v_p(n) = v_p(mn),$$
where $\max(\alpha,\beta)+\min(\alpha,\beta)=\alpha+\beta$ holds because one of the
two summands is $\alpha$ and the other is $\beta$. Thus $\operatorname{lcm}(m,n)\cdot
\gcd(m,n)$ and $mn$ have equal $p$-valuation for every prime $p$; two positive
integers with the same valuation at every prime are equal (uniqueness of prime
factorization). Hence $\operatorname{lcm}(m,n)\cdot g = mn$, i.e.
$\operatorname{lcm}(m,n) = mn/g$, and combining gives $g\cdot h = mn/g$. $\quad\blacksquare$

**Corollary 2 (Effect of a move on $P$).** A move on $m,n$ changes the board
product from $P$ to $P' = P / \gcd(m,n)$.

*Proof.* $P$ is the product of all entries. The move deletes the two factors $m,n$
and inserts $g, h$, leaving all other factors unchanged. Hence
$$P' = \frac{P}{mn}\cdot (g\cdot h) = \frac{P}{mn}\cdot \frac{mn}{g} = \frac{P}{g},$$
using Lemma 1 for $g\cdot h = mn/g$. Since $g = \gcd(m,n) \ge 1$ is a positive
integer dividing $mn$, indeed $g \mid P$ (as $mn \mid P$), so $P' = P/g$ is a
positive integer. $\quad\blacksquare$

---

### 2. Part (a): termination via the lexicographic monovariant (P, C)

We track the pair $(P(B), C(B)) \in \mathbb{Z}_{\ge 1}\times\mathbb{Z}_{\ge 0}$ and
order such pairs **lexicographically**: $(p,c) \prec (p',c')$ iff $p < p'$, or
($p = p'$ and $c < c'$).

**Lemma 3 (Each move strictly decreases $(P,C)$ in $\prec$).** Let a move act on
entries $m>1, n>1$, and let $(P,C) \to (P',C')$ be the resulting change. Set
$g = \gcd(m,n)$. Then exactly one of the following holds, and in both cases
$(P',C') \prec (P,C)$:

- **(i) $g > 1$:** $P' = P/g < P$. Then $(P',C') \prec (P,C)$ regardless of $C'$,
  because the first coordinate already strictly drops.
- **(ii) $g = 1$:** $P' = P$ (unchanged), and $C' = C - 1$. Then $P' = P$ and
  $C' < C$, so $(P',C') \prec (P,C)$.

*Proof.* By Corollary 2, $P' = P/g$ in all cases.

Case (i): if $g > 1$ then $P' = P/g \le P/2 < P$ (as $P \ge 1$), so the first
coordinate strictly drops and $(P',C')\prec (P,C)$ by definition of lex order, no
matter what $C'$ is.

Case (ii): if $g = \gcd(m,n) = 1$, then $P' = P/1 = P$, so the first coordinate is
tied. We must compute $C'$. The two outputs are
$$g = \gcd(m,n) = 1, \qquad h = \frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}
  = \frac{mn/g}{g} = \frac{mn}{g^2} = mn \quad(\text{since } g=1),$$
using Lemma 1's $\operatorname{lcm}(m,n)=mn/g$. Since $m > 1$ and $n > 1$, we have
$h = mn > 1$. Thus the move removes the two entries $m,n$ (both $> 1$, contributing
$2$ to $C$) and inserts $g = 1$ (contributing $0$) and $h = mn > 1$ (contributing
$1$). Every untouched entry keeps its status. Therefore
$$C' = C - 2 + 1 = C - 1,$$
so the second coordinate strictly drops while the first is tied, giving
$(P',C') \prec (P,C)$. $\quad\blacksquare$

The two cases are exhaustive ($g \ge 1$ always, since $\gcd$ of positive integers
is $\ge 1$) and disjoint ($g=1$ versus $g>1$).

**Lemma 4 (No infinite strictly $\prec$-decreasing chain — well-foundedness).**
There is no infinite sequence $(p_0,c_0) \succ (p_1,c_1) \succ (p_2,c_2) \succ
\cdots$ of pairs with $p_k \in \mathbb{Z}_{\ge 1}$ and $c_k \in \mathbb{Z}_{\ge 0}$.

*Proof.* Suppose, for contradiction, such an infinite strictly decreasing chain
exists. Consider the first-coordinate sequence $p_0, p_1, p_2, \dots$. By the
definition of $\prec$, for each $k$ either $p_{k+1} < p_k$, or ($p_{k+1} = p_k$ and
$c_{k+1} < c_k$). In particular $p_{k+1} \le p_k$ for all $k$, so $(p_k)_{k\ge 0}$
is a **non-increasing** sequence of positive integers.

A non-increasing sequence of positive integers takes only finitely many distinct
values and stabilizes: indeed $p_0 \ge p_1 \ge \cdots \ge 1$, and each strict
decrease $p_{k+1} < p_k$ lowers the value by at least $1$ while the value never goes
below $1$; hence at most $p_0 - 1$ strict decreases can occur. So there is an index
$K$ beyond which the first coordinate is constant: $p_k = p_K =: q$ for all
$k \ge K$.

For all $k \ge K$ we then have $p_{k+1} = p_k = q$, so the strict inequality
$(p_{k+1},c_{k+1}) \prec (p_k,c_k)$ can hold only via the second clause, i.e.
$c_{k+1} < c_k$. Thus $c_K > c_{K+1} > c_{K+2} > \cdots$ is an infinite **strictly
decreasing** sequence of non-negative integers. But a strictly decreasing sequence
of non-negative integers must terminate: $c_{K+j} \le c_K - j$ by an immediate
induction ($c_{K}\le c_K$, and each step drops by at least $1$), so $c_{K+j} < 0$
once $j > c_K$, contradicting $c_{K+j} \ge 0$.

This contradiction shows no such infinite chain exists; equivalently, $\prec$ is
well-founded on $\mathbb{Z}_{\ge 1}\times\mathbb{Z}_{\ge 0}$. $\quad\blacksquare$

(This is the standard well-ordering of a finite lexicographic product of
well-ordered coordinates; here we have proven it from first principles by infinite
descent — the dual of induction, **knowledge_base.md** "Infinite descent / no
minimal counterexample".)

**Termination.** Consider any sequence of moves Confucius performs, producing board
states $B_0, B_1, B_2, \dots$ where $B_0$ is the initial board and $B_{k+1}$ is
obtained from $B_k$ by one move. By Lemma 3, $(P(B_{k+1}), C(B_{k+1})) \prec
(P(B_k), C(B_k))$ for every $k$. If the process never stopped it would produce an
infinite such sequence of pairs, i.e. an infinite strictly $\prec$-decreasing chain,
contradicting Lemma 4. Hence **the process stops after finitely many moves**,
independently of Confucius's choices.

**Terminal count is at most one.** The process stops precisely when no move is
possible, i.e. when there is *no* pair of entries both $> 1$. This means at most one
entry exceeds $1$: $C(B_{\mathrm{final}}) \le 1$. (If two or more entries were $>1$,
Confucius could still move — contradicting that the process stopped.)

It remains to rule out $C(B_{\mathrm{final}}) = 0$ and to identify the surviving
value; both come from the invariant of Part (b), to which we now turn.

---

### 3. Part (b): the per-prime gcd invariant

**Lemma 5 (Euclidean-step identity).** For all integers $a,b \ge 0$,
$$\gcd\big(\min(a,b),\ |a-b|\big) = \gcd(a,b),$$
using the conventions (C).

*Proof.* By symmetry of both sides in $a,b$, assume without loss of generality
$a \le b$, so $\min(a,b) = a$ and $|a-b| = b-a \ge 0$. We must show
$\gcd(a,\, b-a) = \gcd(a,b)$.

This is the subtractive Euclidean step. We prove it via the common-divisor
characterization. An integer $d \ge 1$ divides both $a$ and $b$ iff $d$ divides both
$a$ and $b-a$: indeed if $d \mid a$ and $d \mid b$ then $d \mid (b - a)$; conversely
if $d \mid a$ and $d \mid (b-a)$ then $d \mid \big(a + (b-a)\big) = b$. Hence the set
of common divisors of $\{a,b\}$ equals the set of common divisors of $\{a, b-a\}$.

If $a = b = 0$: both sides are $\gcd(0,0) = 0$ by (C). Otherwise at least one of
$a, b$ is positive; then $\{a,b\}$ has a *largest* common divisor (a positive
integer), and since the two sets of common divisors coincide, $\{a,b-a\}$ has the
same largest common divisor. By convention (C) this largest common divisor is
exactly $\gcd(a,b) = \gcd(a,b-a)$. (When $a = 0 < b$: $\gcd(0,b) = b$ and
$\gcd(0, b-0) = \gcd(0,b) = b$; consistent.) This establishes
$\gcd(a, b-a) = \gcd(a,b)$, i.e. $\gcd(\min(a,b), |a-b|) = \gcd(a,b)$.
$\quad\blacksquare$

**Lemma 6 (Move acts as a Euclidean step on each valuation).** Fix a prime $p$. In a
move on entries $m,n$ producing $g = \gcd(m,n)$ and $h = \operatorname{lcm}(m,n)/g$,
write $\alpha = v_p(m),\ \beta = v_p(n)$. Then
$$v_p(g) = \min(\alpha,\beta), \qquad v_p(h) = |\alpha - \beta|.$$

*Proof.* From (V), $v_p(g) = v_p(\gcd(m,n)) = \min(\alpha,\beta)$. For $h$, using
$h = \operatorname{lcm}(m,n)/\gcd(m,n)$ and additivity of $v_p$ under
multiplication/division of positive integers,
$$v_p(h) = v_p(\operatorname{lcm}(m,n)) - v_p(\gcd(m,n))
        = \max(\alpha,\beta) - \min(\alpha,\beta) = |\alpha-\beta|,$$
where the last equality holds because $\max(\alpha,\beta) - \min(\alpha,\beta)$ is
the larger minus the smaller of $\alpha,\beta$, i.e. $|\alpha - \beta|$. (The
division is exact — $\gcd(m,n) \mid \operatorname{lcm}(m,n)$ — so $v_p(h) \ge 0$ is a
genuine valuation.) $\quad\blacksquare$

**Definition.** For a prime $p$ and a board state $B = \{x_1,\dots,x_N\}$, define
$$d_p(B) := \gcd\big(v_p(x_1),\, v_p(x_2),\, \dots,\, v_p(x_N)\big),$$
the gcd of the $p$-valuations of all $N$ entries (using convention (C); this is $0$
iff $p$ divides no entry).

**Lemma 7 ($d_p$ is invariant under every move).** For every prime $p$, a move does
not change $d_p$: if $B \to B'$ is a single move, then $d_p(B') = d_p(B)$.

*Proof.* Fix $p$. A move touches exactly two entries $m, n$, replacing them by
$g, h$, and leaves the other $N-2$ entries unchanged; call the multiset of the
other entries' valuations $R = \{v_p(x) : x \text{ untouched}\}$ (a tuple of
$N-2$ non-negative integers). Write $\alpha = v_p(m), \beta = v_p(n)$. Then, using
commutativity/associativity of $\gcd$ to group the touched pair together,
$$d_p(B) = \gcd\big(\alpha,\ \beta,\ R\big) = \gcd\Big(\gcd(\alpha,\beta),\ R\Big),$$
$$d_p(B') = \gcd\big(v_p(g),\ v_p(h),\ R\big)
          = \gcd\Big(\gcd\big(v_p(g), v_p(h)\big),\ R\Big).$$
By Lemma 6, $v_p(g) = \min(\alpha,\beta)$ and $v_p(h) = |\alpha-\beta|$, so by
Lemma 5,
$$\gcd\big(v_p(g), v_p(h)\big) = \gcd\big(\min(\alpha,\beta), |\alpha-\beta|\big)
   = \gcd(\alpha,\beta).$$
Substituting this equal inner value into the two displayed expressions gives
$d_p(B') = \gcd(\gcd(\alpha,\beta), R) = d_p(B)$. $\quad\blacksquare$

Since $d_p$ is unchanged by each individual move, it is unchanged along the whole
process: for every prime $p$ and every reachable state $B_k$,
$$d_p(B_k) = d_p(B_0), \tag{INV}$$
where $B_0$ is the initial board. We write $d_p := d_p(B_0)$.

**Finitely many primes matter.** Every $d_p$ with $p$ not dividing any initial entry
$x_i$ is $0$ (all $v_p(x_i)=0$, and $\gcd(0,\dots,0)=0$ by (C)). Only the finitely
many primes dividing $\prod_i x_i$ can have $d_p > 0$. Hence the product
$\prod_p p^{d_p}$ below is a finite product and is a well-defined positive integer.

---

### 4. Finishing Part (a): exactly one entry $> 1$

We have shown (Section 2) that the process terminates in a state $B_{\mathrm{final}}$
with $C(B_{\mathrm{final}}) \le 1$. We now rule out $C(B_{\mathrm{final}}) = 0$.

Because every initial entry is $> 1$, pick any initial entry $x_1 > 1$ and any prime
$p_1$ dividing it; then $v_{p_1}(x_1) \ge 1$. Consequently
$$d_{p_1} = \gcd\big(v_{p_1}(x_1), v_{p_1}(x_2), \dots, v_{p_1}(x_N)\big) \ge 1,$$
because $d_{p_1}$ is (by convention (C), since $v_{p_1}(x_1) > 0$) the largest
positive integer dividing all the $v_{p_1}(x_i)$, and every positive common divisor
of a set containing the positive integer $v_{p_1}(x_1)$ is at least $1$. So
$d_{p_1} \ge 1$.

Suppose, for contradiction, $C(B_{\mathrm{final}}) = 0$, i.e. every entry of
$B_{\mathrm{final}}$ equals $1$. Then $v_p(x) = 0$ for every entry $x$ and every
prime $p$, so $d_p(B_{\mathrm{final}}) = \gcd(0,\dots,0) = 0$ for all $p$. In
particular $d_{p_1}(B_{\mathrm{final}}) = 0$. But by (INV),
$d_{p_1}(B_{\mathrm{final}}) = d_{p_1} \ge 1$, a contradiction.

Therefore $C(B_{\mathrm{final}}) = 1$: **exactly one** entry $M$ on the final board
is greater than $1$ (all other $N-1 = 2025$ entries equal $1$). This proves Part (a).
$\quad\blacksquare$ *(Part a)*

---

### 5. Finishing Part (b): $M$ is determined by the initial board

By Part (a) the terminal board $B_{\mathrm{final}}$ consists of one entry $M > 1$ and
$N-1$ entries equal to $1$. For each prime $p$, the valuations of the terminal
entries are $v_p(M)$ (from $M$) and $0$ (from each $1$). Hence, by convention (C)
and $\gcd(k,0,\dots,0)=k$,
$$d_p(B_{\mathrm{final}}) = \gcd\big(v_p(M),\, 0,\, \dots,\, 0\big) = v_p(M).$$
By the invariance (INV), $d_p(B_{\mathrm{final}}) = d_p$, so
$$v_p(M) = d_p \qquad\text{for every prime } p.$$
A positive integer is determined by its valuations at all primes (unique
factorization), so
$$M = \prod_{p} p^{\,d_p}, \tag{$\star$}$$
a finite product (Section 3, "finitely many primes matter"). The right-hand side of
$(\star)$ depends **only on the initial board** $B_0$ — the numbers $d_p =
\gcd(v_p(x_1),\dots,v_p(x_N))$ are computed from the initial entries alone and, by
Lemma 7, are unaffected by any moves. Since Confucius's choices never enter $(\star)$,
the surviving value $M$ is the same regardless of the choices he makes. This proves
Part (b). $\quad\blacksquare$ *(Part b)*

---

### 6. Verification of the closed form (sanity check)

$(\star)$ says the survivor is the integer $M = \prod_p p^{\,\gcd_i v_p(x_i)}$
whose $p$-exponent is $\gcd_i v_p(x_i)$ for each prime. We record a direct check on
a concrete board. Take the two-entry board $\{4, 8\}$ ($N=2$):
$v_2 = (2,3)$, $d_2 = \gcd(2,3) = 1$, all other $d_p = 0$, so $(\star)$ predicts
$M = 2^1 = 2$. Direct move: $\gcd(4,8)=4$, $\operatorname{lcm}=8$, so outputs
$4$ and $8/4 = 2$; board becomes $\{4,2\}$. Move again: $\gcd(4,2)=2$,
$\operatorname{lcm}=4$, outputs $2$ and $4/2=2$; board $\{2,2\}$. Again:
$\gcd(2,2)=2$, $\operatorname{lcm}=2$, outputs $2$ and $2/2=1$; board $\{2,1\}$.
Terminal survivor $M = 2$, matching $(\star)$. This concrete run also illustrates
termination (Part a) and choice-independence (any move order on this board yields
survivor $2$). $\quad\blacksquare$

---

**Summary.** Part (a): the pair $(P,C)$ strictly decreases in the well-founded
lexicographic order at every move (Lemmas 3, 4), forcing termination with
$C \le 1$; the invariant $d_{p_1}\ge 1$ (Lemma 7) rules out $C = 0$, giving exactly
one survivor $M > 1$. Part (b): $v_p(M) = d_p$ for all $p$, so $M = \prod_p p^{d_p}$
is fixed by the initial board (Lemmas 5–7). $\qquad\blacksquare$

## Promotable lemmas

- **euclid-step-invariant** (Lemmas 5 & 6 & 7 combined): For integers $a,b\ge 0$,
  $\gcd(\min(a,b),|a-b|)=\gcd(a,b)$ (conventions $\gcd(0,k)=k$, $\gcd(0,0)=0$);
  consequently a move on $m,n$ sends each prime valuation pair
  $(v_p m, v_p n) \mapsto (\min, |{\rm diff}|)$, and therefore
  $d_p=\gcd(v_p(x_1),\dots,v_p(x_N))$ is invariant under every move (proof by
  gcd associativity, grouping the touched pair). Proved in full in Section 3 of
  this file. Reusable by omega-count-monovariant and valuation-gcd.
- **move-product-identity** (Lemma 1 / Corollary 2): $g\cdot h=\operatorname{lcm}(m,n)
  =mn/\gcd(m,n)$, hence a move divides the board product $P$ by $\gcd(m,n)$.
  Proved in full in Section 1.
- **lex-well-foundedness** (Lemma 4): the lexicographic order on
  $\mathbb Z_{\ge1}\times\mathbb Z_{\ge0}$ admits no infinite strictly decreasing
  chain (proof by infinite descent on each coordinate). Proved in Section 2.
