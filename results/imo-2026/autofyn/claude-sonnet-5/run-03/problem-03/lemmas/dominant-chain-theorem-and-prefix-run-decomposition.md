# Certified (round 3): Companion Peeling Lemma, Dominant-Chain Theorem, Prefix-Run Peeling Decomposition Lemma

Certified from `approaches/greedy-reduction-geometric.md` (round 3, Section
7). Notation: $\Gamma_{m-1}:=\{2^{m-1},\dots,2^0\}$ ($m\ge0$ elements,
$\Gamma_{-1}:=\varnothing$), sum $2^m-1$.

## Lemma 5 (Companion Peeling Lemma)

**Statement.** For any finite multiset $N$ of positive reals with
$g:=\max(N)$ (any copy, if tied), $\mathrm{EvenSum}(N)=\mathrm{OddSum}(N\setminus\{g\})$.

**Proof.** By the certified Global-max Peeling Lemma,
$\mathrm{OddSum}(N)=g+\mathrm{EvenSum}(N\setminus\{g\})$; also
$\mathrm{OddSum}(N)+\mathrm{EvenSum}(N)=\mathrm{sum}(N)=g+\mathrm{sum}(N\setminus\{g\})
=g+\mathrm{OddSum}(N\setminus\{g\})+\mathrm{EvenSum}(N\setminus\{g\})$.
Subtracting gives the claim. $\blacksquare$

## Theorem 5 (Dominant-Chain Theorem)

**Definition (Dominance-Chain property at level $m$).** A finite descending
sequence $a_1\ge\cdots\ge a_k>0$ has the property if $k=0$, or if $k\ge1$,
$m\ge0$, $a_1\ge2^{m-1}$ (with $2^{-1}:=0$), and $(a_2,\dots,a_k)$ has the
property at level $m-1$.

**Statement.** For $m\ge0$ and $a_1\ge\cdots\ge a_k>0$ with $\sum a_i\le2^m$
having the Dominance-Chain property at level $m$:
$$\mathrm{OddSum}\bigl(\{a_1,\dots,a_k\}\cup\Gamma_{m-1}\bigr)\ \ge\ \sum_i a_i.$$

**Proof.** Strong induction on $k$. Base $k=0$: LHS $=\mathrm{OddSum}(\Gamma_{m-1})\ge0$.
Inductive step ($k\ge1$, so $a_1\ge2^{m-1}$, $m\ge1$): let
$S=\sum a_i\le2^m$, $S'=S-a_1\le2^{m-1}$ (from $a_1\ge2^{m-1}$). Every
$a_i$ ($i\ge2$) and every element of $\Gamma_{m-1}$ is $\le2^{m-1}\le a_1$,
so $a_1=\max(A\cup\Gamma_{m-1})$. By the Global-max Peeling Lemma,
$\mathrm{OddSum}(A\cup\Gamma_{m-1})=a_1+\mathrm{EvenSum}(A'\cup\Gamma_{m-1})$
where $A'=\{a_2,\dots,a_k\}$. Since every element of $A'\cup\Gamma_{m-1}$
is $\le2^{m-1}$ (attained by $\Gamma_{m-1}$'s own top element),
$2^{m-1}=\max(A'\cup\Gamma_{m-1})$, so by the Companion Peeling Lemma
(with $N\setminus\{g\}=A'\cup\Gamma_{m-2}$):
$\mathrm{EvenSum}(A'\cup\Gamma_{m-1})=\mathrm{OddSum}(A'\cup\Gamma_{m-2})$.
By the inductive hypothesis (applicable: $(a_2,\dots,a_k)$ has the property
at level $m-1$, $k-1<k$ elements, sum $S'\le2^{m-1}$),
$\mathrm{OddSum}(A'\cup\Gamma_{m-2})\ge S'$. Chaining:
$\mathrm{OddSum}(A\cup\Gamma_{m-1})=a_1+\mathrm{OddSum}(A'\cup\Gamma_{m-2})\ge a_1+S'=S$.
$\blacksquare$

**Corollary.** Strictly generalizes the original Lower-bound Case 1
($j=0$: chain trivially satisfied). Also covers LB's equality-attaining
self-similar construction at every level (verified: the ratio
$a_i/2^{n-i}$ is constant across levels for that construction).

## Lemma 6 (Prefix-Run Peeling Decomposition Lemma)

**Statement.** Let $m\ge1$, $a_1\ge\cdots\ge a_k>0$ ($k\ge0$), $1\le d\le m$
with $a_1<2^{m-d}$ (vacuous if $k=0$). Write
$\Gamma_{[m-d,m-1]}=\{2^{m-1},\dots,2^{m-d}\}$ (top $d$ of $\Gamma_{m-1}$),
$\Gamma_{m-d-1}$ the remaining $m-d$ elements. Then
$$\mathrm{OddSum}(\{a_1,\dots,a_k\}\cup\Gamma_{m-1})=\mathrm{OddSum}(\Gamma_{[m-d,m-1]})+\begin{cases}\mathrm{OddSum}(\{a_i\}\cup\Gamma_{m-d-1}),&d\text{ even}\\\mathrm{EvenSum}(\{a_i\}\cup\Gamma_{m-d-1}),&d\text{ odd}.\end{cases}$$

**Proof.** Since $a_1<2^{m-d}\le\cdots\le2^{m-1}$, every element of $A$ is
strictly below every element of $\Gamma_{[m-d,m-1]}$, which is in turn
strictly above every element of $\Gamma_{m-d-1}$ ($\le2^{m-d-1}<2^{m-d}$).
So the top $d$ global ranks are exactly $\Gamma_{[m-d,m-1]}$'s own sorted
values, and the remaining ranks $d+1,d+2,\dots$ carry $R:=A\cup\Gamma_{m-d-1}$
in its own sorted order at local rank $i=(\text{global rank})-d$. Global
rank $p=d+i$ is odd iff $i$ has parity opposite to $d$ (when $d$ odd) or
same as $i$ (when $d$ even), giving $\mathrm{OddSum}(R)$ (d even) or
$\mathrm{EvenSum}(R)$ (d odd) for the tail contribution. $\blacksquare$

## Verification (proof-reviewer, round 3)
- Dominant-Chain Theorem: verified numerically, 8808 random Dominance-Chain-
  satisfying instances ($m\le5$), zero violations.
- Prefix-Run Decomposition: verified numerically, 20000 random instances
  ($m\le6$), zero mismatches (exact match to $10^{-9}$).
- Companion Peeling Lemma: elementary consequence of already-certified
  facts, re-derived directly.

## Reuse notes
Directly reusable by any approach needing a lower bound on
$\mathrm{OddSum}(A\cup\Gamma_{m-1})$ for a top-piece split $A$ whose
fragments dominate the tail level-by-level (Dominant-Chain regime), or a
structural decomposition for the complementary (non-dominant) regime
(Lemma 6). Documented as *not* sufficient by itself for the complementary
regime (see `approaches/greedy-reduction-geometric.md` Section 7.3 for the
precise diagnosis of why — a genuine open gap, not resolved by this lemma
alone).
