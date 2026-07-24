# Approach: descent-induction

## Status
solved

## Target (whole problem)
(a) exactly one $M>1$ remains after finitely many moves; (b) $M$ is independent of the choices.

## Technique (the spine)
**Well-founded (minimal-counterexample) induction on the terminating lex order** $(\Omega_{\text{tot}},C)$.
Part (a) is the standard monovariant termination plus a nonvanishing invariant. Part (b) is packaged as
*confluence proved by descent*: I prove by strong induction on the terminating order that **every** maximal
sequence of moves from a board ends at the **same** board. The only nontrivial critical pair — two first
moves sharing one entry (the "3-cell" pair) — is joined by an **explicit common reduct** whose existence and
value are certified by the per-prime gcd-of-valuations invariant. The framing difference from the
closed-form route is that uniqueness of $M$ is obtained from the descent, not by computing the terminal
valuations of the whole board; the closed form $M=\prod_p p^{g_p}$ falls out only as a closing corollary.

## Approaches tried
- Round 1: full descent/minimal-counterexample write-up. The 3-cell joinability crux (G1) closed by an
  explicit common reduct built from the per-prime gcd invariant (Lemma 3), not by "normal forms are unique"
  (which would be circular). Well-foundedness (G2) and termination (G3) closed via the lex monovariant
  (Lemma 2). Verified on $\{4,6,9\}$ and on random boards. **Outcome: complete — Status solved.**

## Current best
Complete proof of (a) and (b) below.

---

## Full proof

### 0. Setup, notation, conventions

Model the blackboard as a **multiset $B$ of $2026$ positive integers**, i.e. a collection of $2026$
*occurrences*, each carrying a positive-integer value; occurrences are distinguishable (there are $2026$
board places), so a multiset with repeated values is handled without ambiguity. Initially every value is
$>1$.

A **move** chooses two occurrences with values $m>1$ and $n>1$, deletes them, and inserts two occurrences
with values $\gcd(m,n)$ and $\dfrac{\operatorname{lcm}(m,n)}{\gcd(m,n)}$. (Since $\gcd(m,n)\mid
\operatorname{lcm}(m,n)$, the second value is a positive integer.) The board size stays $2026$. A move is
**legal** iff two occurrences with value $>1$ exist. The process stops exactly when **at most one**
occurrence has value $>1$ (if two did, they would furnish a legal move; if at most one does, no two values
$>1$ exist, so no move is possible). Call such a board **terminal**.

For a positive integer $k$ and a prime $p$, write $v_p(k)$ for the $p$-adic valuation (exponent of $p$ in
$k$), and $\Omega(k)=\sum_p v_p(k)$ for the number of prime factors of $k$ counted with multiplicity, so
$\Omega(1)=0$. Integer $\gcd$ is used with the standard conventions $\gcd(a,0)=a$ for $a\ge 0$ and
$\gcd(0,0)=0$; it is associative and commutative on $\mathbb{N}$, so $\gcd$ of a finite list is
well-defined regardless of order.

For a board $B$ with values $b_1,\dots,b_{2026}$ define
$$
\Omega_{\text{tot}}(B)=\sum_{i=1}^{2026}\Omega(b_i),\qquad C(B)=\#\{i: b_i>1\},\qquad
\mu(B)=\bigl(\Omega_{\text{tot}}(B),\,C(B)\bigr)\in\mathbb{N}\times\mathbb{N},
$$
and order the pairs $\mu(B)$ by the **lexicographic order** $<_{\mathrm{lex}}$ on $\mathbb{N}\times\mathbb{N}$.

We repeatedly use one elementary fact.

> **Fact (KB: Divisor analysis / unique factorization).** For positive integers $m,n$ and every prime $p$,
> with $a=v_p(m),\ b=v_p(n)$:
> $$v_p(\gcd(m,n))=\min(a,b),\qquad v_p(\operatorname{lcm}(m,n))=\max(a,b).$$

### 1. Lemma 1 (per-prime description of a move)

**Statement.** If a move combines values $m,n$ into $g=\gcd(m,n)$ and $\ell=\operatorname{lcm}(m,n)/\gcd(m,n)$,
then for every prime $p$, writing $a=v_p(m),\,b=v_p(n)$,
$$
v_p(g)=\min(a,b),\qquad v_p(\ell)=|a-b|.
$$

**Proof.** $v_p(g)=\min(a,b)$ is the Fact. For $\ell$: since $\gcd\mid\operatorname{lcm}$, the quotient is a
positive integer and $v_p(\ell)=v_p(\operatorname{lcm}(m,n))-v_p(\gcd(m,n))=\max(a,b)-\min(a,b)=|a-b|$,
using the Fact for both terms. $\qquad\blacksquare$

Thus, at the two combined occurrences, the valuation pair transforms, **simultaneously for every prime $p$**,
by the map
$$
(a,b)\longmapsto(\min(a,b),\,|a-b|),
$$
one subtractive-Euclid step. All other occurrences are unchanged.

### 2. Lemma 2 (lexicographic monovariant; termination and terminal shape)

**Statement.** Every legal move strictly decreases $\mu$ in $<_{\mathrm{lex}}$. Consequently every sequence
of moves is finite, and it ends at a terminal board (at most one value $>1$).

**Proof.** Let a move combine $m,n>1$ into $g=\gcd(m,n)$ and $\ell=\operatorname{lcm}(m,n)/\gcd(m,n)$; all
other occurrences are unchanged, so $\Delta\Omega_{\text{tot}}=\Omega(g)+\Omega(\ell)-\Omega(m)-\Omega(n)$.
By Lemma 1, summing over primes,
$$
\Omega(g)+\Omega(\ell)=\sum_p\bigl(\min(a_p,b_p)+|a_p-b_p|\bigr)=\sum_p\max(a_p,b_p),\qquad
\Omega(m)+\Omega(n)=\sum_p(a_p+b_p),
$$
where $a_p=v_p(m),\,b_p=v_p(n)$. Hence
$$
\Delta\Omega_{\text{tot}}=\sum_p\bigl(\max(a_p,b_p)-a_p-b_p\bigr)=-\sum_p\min(a_p,b_p)=-\Omega(\gcd(m,n))\le 0 .
$$

*Case $\gcd(m,n)>1$.* Then $\Omega(\gcd(m,n))\ge 1$, so $\Omega_{\text{tot}}$ strictly decreases; hence $\mu$
decreases in $<_{\mathrm{lex}}$ (first coordinate drops).

*Case $\gcd(m,n)=1$.* Then $\ell=\operatorname{lcm}(m,n)/1=mn$, and the move replaces the two occurrences of
values $m,n$ by values $1$ and $mn$. Here $\Delta\Omega_{\text{tot}}=0$. Now consider $C$: since $m,n>1$ we
have $mn>1$, so among the two new values exactly one ($=1$) is not $>1$; two values that were $>1$ become one
value $>1$ and one value $=1$, while all other occurrences are unchanged. Thus $C$ strictly decreases (by
$1$). Since $\Omega_{\text{tot}}$ is unchanged and $C$ drops, $\mu$ decreases in $<_{\mathrm{lex}}$.

In every case $\mu$ strictly decreases. The lexicographic order on $\mathbb{N}\times\mathbb{N}$ is
**well-founded** (it admits no infinite strictly descending chain; it is a well-order of order type
$\omega^2$). Therefore no infinite sequence of moves exists: every sequence is finite and, being unable to
continue, ends at a terminal board. $\qquad\blacksquare$

We record the immediate corollary used throughout: **if $B'$ is obtained from $B$ by one or more moves, then
$\mu(B')<_{\mathrm{lex}}\mu(B)$.**

### 3. Lemma 3 (per-prime gcd-of-valuations invariant)

For a board $B$ with values $b_1,\dots,b_{2026}$ and a prime $p$ set
$$
g_p(B)=\gcd\bigl(v_p(b_1),\dots,v_p(b_{2026})\bigr).
$$
More generally, for a subset $S$ of occurrences let $g_p^{S}(B)=\gcd_{\,i\in S} v_p(b_i)$.

**Statement.** Let a move combine two occurrences whose set is $\{u,w\}$. Then for **every** prime $p$:
1. $\gcd\bigl(v_p(\text{new value at }u),\,v_p(\text{new value at }w)\bigr)=\gcd\bigl(v_p(b_u),v_p(b_w)\bigr)$;
2. $g_p^{S}$ is unchanged for every occurrence-set $S$ containing both $u$ and $w$; in particular
   $g_p(B)$ is invariant under every move.

**Proof.** (1) By Lemma 1 the pair $(a,b)=(v_p(b_u),v_p(b_w))$ becomes $(\min(a,b),|a-b|)$. We show
$\gcd(\min(a,b),|a-b|)=\gcd(a,b)$, treating all cases with the conventions of §0. WLOG $a\le b$ (the map's
output is symmetric in $a,b$, and so is $\gcd$).
- If $0<a\le b$: output $(a,\,b-a)$. Every common divisor of $a,b$ divides $b-a$, and every common divisor
  of $a$ and $b-a$ divides $b=(b-a)+a$; hence $\{$common divisors of $a,b\}=\{$common divisors of
  $a,b-a\}$, so $\gcd(a,b-a)=\gcd(a,b)$.
- If $a=b>0$: output $(a,0)$, and $\gcd(a,0)=a=\gcd(a,a)$.
- If $a=0\le b$: output $(0,b)$, and $\gcd(0,b)=b=\gcd(0,b)$ trivially.

These cases are exhaustive (given $a\le b$), so (1) holds in all cases.

(2) Let $S\supseteq\{u,w\}$ and let $R=S\setminus\{u,w\}$ (values on $R$ are unchanged by the move). Using
associativity/commutativity of $\gcd$ and part (1),
$$
g_p^{S}(\text{after})=\gcd\Bigl(\gcd_{i\in R}v_p(b_i),\ \gcd\bigl(v_p(\text{new }u),v_p(\text{new }w)\bigr)\Bigr)
=\gcd\Bigl(\gcd_{i\in R}v_p(b_i),\ \gcd(v_p(b_u),v_p(b_w))\Bigr)=g_p^{S}(\text{before}).
$$
Taking $S=$ all $2026$ occurrences gives the invariance of $g_p(B)$. $\qquad\blacksquare$

### 4. Part (a): exactly one surviving value $>1$

By Lemma 2 the process terminates at a board with **at most one** value $>1$. It remains to rule out zero.

Because every initial value is $>1$, some initial value has a prime factor; fix a prime $p$ dividing some
initial value, so at least one initial valuation $v_p(b_i)>0$. Then
$g_p(B_0)=\gcd_i v_p(b_i)$ is the $\gcd$ of a list of nonnegative integers not all zero, i.e. the $\gcd$ of
its positive members (zeros are neutral by convention $\gcd(x,0)=x$), hence $g_p(B_0)\ge 1$.

By Lemma 3, $g_p$ is invariant, so the **terminal** board $B_\infty$ satisfies $g_p(B_\infty)=g_p(B_0)\ge 1$.
If $B_\infty$ had *no* value $>1$, all its values would be $1$, every valuation would be $0$, and
$g_p(B_\infty)=0$ — contradiction. Hence $B_\infty$ has at least one value $>1$; combined with "at most one,"
**exactly one** value $M>1$ survives. This proves (a). $\qquad\blacksquare$

### 5. Lemma 4 (disjoint moves commute)

**Statement.** Let $\mu$ act on occurrence-set $\{i,j\}$ and $\nu$ on occurrence-set $\{k,l\}$ with
$\{i,j\}\cap\{k,l\}=\varnothing$, both legal on board $B$. Then $\nu$ is legal on $\mu(B)$, $\mu$ is legal on
$\nu(B)$, and $\nu(\mu(B))=\mu(\nu(B))$.

**Proof.** A move changes only the values of the occurrences it acts on, and computes the two new values from
the two old values of those occurrences alone. Since $\{i,j\}$ and $\{k,l\}$ are disjoint, $\mu$ leaves the
values at $k,l$ untouched (still $>1$, so $\nu$ remains legal), and $\nu$ leaves the values at $i,j$
untouched (so $\mu$ remains legal). In $\nu(\mu(B))$ the pair $\{i,j\}$ holds the outputs of $\mu$ and
$\{k,l\}$ holds the outputs of $\nu$; the same holds in $\mu(\nu(B))$, and all other occurrences are
unchanged in both. Hence the two boards are identical. $\qquad\blacksquare$

### 6. Lemma 5 (3-cell joinability — the critical pair)

**Statement.** Let $x,y,z>1$ be the values at three distinct occurrences $X,Y,Z$ of a board $B$ (all other
occurrences arbitrary). Let $B'=\mu(B)$ combine $\{X,Y\}$ and $B''=\nu(B)$ combine $\{Y,Z\}$. Then there is
a board $W$ reachable **from $B'$** and **from $B''$**, using only moves among $\{X,Y,Z\}$, such that
$W$ has value $\prod_p p^{g_p^{\{X,Y,Z\}}(B)}$ at one of $X,Y,Z$, value $1$ at the other two, and all other
occurrences equal to those of $B$. In particular $W$ is a **common reduct** of $B'$ and $B''$, and
$\mu(W)<_{\mathrm{lex}}\mu(B')$ (possibly with equality only when $W=B'$), and likewise for $B''$.

**Proof.** Write $g_p:=g_p^{\{X,Y,Z\}}(B)=\gcd(v_p(x),v_p(y),v_p(z))$ and $s:=\prod_p p^{g_p}$ (a finite
product: $g_p=0$ for all but finitely many $p$). Both $\mu$ and $\nu$ are moves among $\{X,Y,Z\}$, so by
Lemma 3(2) with $S=\{X,Y,Z\}$ we have $g_p^{\{X,Y,Z\}}(B')=g_p^{\{X,Y,Z\}}(B'')=g_p$ for all $p$.

Now run, starting from $B'$, **any maximal sequence of moves that uses only occurrences in $\{X,Y,Z\}$**
(leaving the other $2023$ occurrences fixed). Lemma 2 applies verbatim to these moves (they strictly
decrease $\mu$), so such a sequence is finite and stops when at most one of $X,Y,Z$ still has value $>1$;
call the resulting board $W_1$. During the whole run $S=\{X,Y,Z\}$ contains every combined pair, so by Lemma
3(2) $g_p^{\{X,Y,Z\}}$ stays equal to $g_p$. At $W_1$ two of $X,Y,Z$ have value $1$ (valuation $0$) and the
third has some value $t$, so for every prime $p$
$$
g_p=g_p^{\{X,Y,Z\}}(W_1)=\gcd\bigl(v_p(t),0,0\bigr)=v_p(t).
$$
Hence $v_p(t)=g_p$ for all $p$, i.e. $t=\prod_p p^{g_p}=s$. Thus $W_1$ has values $\{s,1,1\}$ on
$\{X,Y,Z\}$ and the original values elsewhere. (If $s=1$ this reads $\{1,1,1\}$.)

Repeat starting from $B''$ to obtain $W_2$ with values $\{s,1,1\}$ on $\{X,Y,Z\}$ and original values
elsewhere. As multisets of $2026$ occurrences, $W_1$ and $W_2$ are the *same* board $W$: they agree on the
$2023$ untouched occurrences and both carry the multiset $\{s,1,1\}$ on $\{X,Y,Z\}$.

Finally $W$ is reached from $B'$ (resp. $B''$) by a finite sequence of moves, so by the corollary to Lemma 2,
$\mu(W)\le_{\mathrm{lex}}\mu(B')$ with $\mu(W)<_{\mathrm{lex}}\mu(B')$ unless $W=B'$ (no moves needed); the
same for $B''$. $\qquad\blacksquare$

*Concrete check.* Take $x,y,z=4,6,9$ (rest irrelevant). Here $v_2=(2,1,0)$ so $g_2=\gcd(2,1,0)=1$, and
$v_3=(0,1,2)$ so $g_3=\gcd(0,1,2)=1$; thus $s=2^1 3^1=6$. The move on $(4,6)$ gives $\gcd=2,
\operatorname{lcm}/\gcd=6$, so $B'=\{2,6,9\}$; the move on $(6,9)$ gives $\gcd=3,\operatorname{lcm}/\gcd=6$,
so $B''=\{3,4,6\}$. From $B'$ the move on $(6,9)$ gives $\{2,3,6\}$; from $B''$ the move on $(4,6)$ gives
$\{2,3,6\}$ — a **common** board, and reducing it further ($\{2,3,6\}\to\{1,6,6\}\to\{1,1,6\}$) reaches
$W=\{6,1,1\}=\{s,1,1\}$ from both branches, as Lemma 5 predicts.

### 7. Part (b): $M$ is choice-independent, via descent

For a board $B$ let $\mathcal{M}(B)$ be the set of terminal boards reachable from $B$ by maximal move
sequences (nonempty by Lemma 2; a terminal board's only maximal sequence is the empty one).

> **Claim.** For every board $B$, $\mathcal{M}(B)$ is a singleton; write $T(B)$ for its unique element.

We prove the Claim by **well-founded induction on $\mu(B)$** in $<_{\mathrm{lex}}$ (valid since
$<_{\mathrm{lex}}$ on $\mathbb{N}\times\mathbb{N}$ is well-founded, Lemma 2). *Induction hypothesis:* the
Claim holds for every board $B^\ast$ with $\mu(B^\ast)<_{\mathrm{lex}}\mu(B)$.

If $B$ is terminal, its only maximal sequence is empty and $\mathcal{M}(B)=\{B\}$; the Claim holds. Assume
$B$ is not terminal and let $P,Q$ be two maximal sequences from $B$, with respective first moves $\mu$
(to $B'$) and $\nu$ (to $B''$). Since $\mu(B'),\mu(B'')<_{\mathrm{lex}}\mu(B)$ (corollary to Lemma 2), the
Claim holds for $B'$ and $B''$: the tail of $P$ is a maximal sequence from $B'$, so $P$ ends at $T(B')$;
likewise $Q$ ends at $T(B'')$. Thus it suffices to prove
$$
T(B')=T(B'').\tag{$\ast$}
$$
We use the following one-line principle, valid whenever $\mu(V)<_{\mathrm{lex}}\mu(B)$:

> **(R)** *If $V'$ is reachable from $V$ by finitely many moves (so $\mu(V')\le_{\mathrm{lex}}\mu(V)
> <_{\mathrm{lex}}\mu(B)$), then $T(V)=T(V')$.* Indeed, prepend the moves $V\to V'$ to any maximal sequence
> from $V'$: the result is a maximal sequence from $V$, so by the Claim at $V$ (I.H.) it ends at $T(V)$; but
> as a sequence from $V'$ it ends at $T(V')$ (Claim at $V'$, I.H.). Hence $T(V)=T(V')$.

The two first moves $\mu$ (on $\{i,j\}$) and $\nu$ (on $\{k,l\}$) fall into exactly three disjoint,
exhaustive cases according to $|\{i,j\}\cap\{k,l\}|\in\{2,1,0\}$.

**Case $|\{i,j\}\cap\{k,l\}|=2$ (identical move).** Then $\{i,j\}=\{k,l\}$ and $\mu,\nu$ act on the same two
occurrences, producing the same two values $\gcd,\operatorname{lcm}/\gcd$; so $B'=B''$ and $(\ast)$ is
immediate.

**Case $|\{i,j\}\cap\{k,l\}|=0$ (disjoint).** By Lemma 4, $\nu$ is legal on $B'$, $\mu$ is legal on $B''$,
and $\nu(B')=\mu(B'')=:B'''$. Both $B'$ and $B''$ reach $B'''$ by one move, and $\mu(B'),\mu(B'')
<_{\mathrm{lex}}\mu(B)$. Apply (R) with $V=B',V'=B'''$ and with $V=B'',V'=B'''$:
$T(B')=T(B''')=T(B'')$, giving $(\ast)$.

**Case $|\{i,j\}\cap\{k,l\}|=1$ (share one occurrence).** Write the shared occurrence as $Y$ and the others
as $X$ (from $\mu$) and $Z$ (from $\nu$); their values $x,y,z$ are all $>1$ (legality of $\mu,\nu$ on $B$).
By Lemma 5 there is a board $W$ reachable **from both $B'$ and $B''$** by finitely many moves. Since
$\mu(B'),\mu(B'')<_{\mathrm{lex}}\mu(B)$, apply (R) with $V=B',V'=W$ and $V=B'',V'=W$:
$T(B')=T(W)=T(B'')$, giving $(\ast)$.

In all three cases $(\ast)$ holds, so $P$ and $Q$ end at the same terminal board. As $P,Q$ were arbitrary
maximal sequences from $B$, $\mathcal{M}(B)$ is a singleton. This completes the induction and proves the
Claim. $\qquad\blacksquare$

**Conclusion of (b).** Applying the Claim to the initial board $B_0$: every maximal sequence of Confucius's
moves ends at the *same* terminal board $T(B_0)$, hence at the same surviving value $M$. Thus $M$ is
independent of the choices. $\qquad\blacksquare$

### 8. Corollary (the value, as a by-product)

By §4 the terminal board $T(B_0)$ has exactly one value $M>1$, with the other $2025$ values equal to $1$.
For each prime $p$ its valuations are $(v_p(M),0,\dots,0)$, so $g_p(T(B_0))=v_p(M)$. By invariance
(Lemma 3), $v_p(M)=g_p(B_0)=\gcd_i v_p(b_i)$ for every $p$, whence
$$
\boxed{\,M=\prod_p p^{\,\gcd_i v_p(b_i)}\,}.
$$
This is not needed for (a) or (b) — both were established above by termination, the nonvanishing invariant,
and the descent — but it identifies $M$ explicitly. (For $\{4,6\}$: $g_2=\gcd(2,1)=1,\ g_3=\gcd(0,1)=1$, so
$M=6$; a direct move sends $\{4,6\}\to\{2,6\}$, terminal survivor $6$, matching.) $\qquad\blacksquare$

---

## Promotable lemmas

- **Lemma 3 (per-prime gcd-of-valuations invariant).** For the gcd/lc-quotient move, for every prime $p$ the
  quantity $g_p=\gcd_i v_p(b_i)$ (and, more generally, $g_p^S$ over any occurrence-set $S$ containing both
  combined cells) is invariant. Proved in full in §3 (mechanism: $\gcd(\min(a,b),|a-b|)=\gcd(a,b)$ with the
  $0$-edge cases, lifted by associativity of $\gcd$). Reusable by every approach.
- **Lemma 2 (lexicographic monovariant / termination).** Every move strictly decreases
  $(\Omega_{\text{tot}},C)$ in lex order; the process terminates at a board with $\le 1$ value $>1$. Proved
  in full in §2, both branches ($\gcd>1$ and $\gcd=1$). Reusable.
- **Lemma 5 (3-cell joinability).** Two first moves sharing one occurrence have an explicit common reduct
  $\{s,1,1\}$ on the three cells with $s=\prod_p p^{\gcd(v_p(x),v_p(y),v_p(z))}$. Proved in full in §6 via
  Lemma 3; certifies the critical pair non-circularly. Reusable by the confluence-newman approach as its
  WCR/local-confluence witness.
