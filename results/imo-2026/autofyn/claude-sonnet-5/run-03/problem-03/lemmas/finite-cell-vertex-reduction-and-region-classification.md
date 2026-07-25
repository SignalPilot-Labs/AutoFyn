# Certified (round 10): Finite-Cell Affine-Vertex Reduction Theorem (corrected),
# Small-Mass Insertion Lemma, Boundary Continuity Theorem, Region-Vertex
# Classification Theorem

Certified from `approaches/global-lp-vertex-sufficiency.md` (round 10, Section 4).
Supersedes the round-9 draft of the "Finite-Cell Affine-Vertex Reduction Theorem,"
which the reviewer rejected for a missing functional ($p_k$) in the candidate
list $L$; this round's fix (adding $p_k$ to $L$) is verified correct below, and
three genuinely new closure results (Sections 4.1–4.3 of the approach file) are
certified alongside it.

## Setting

Work in the balanced region $B(n)$: $k=n+1$ pieces, $p_1<1/2$, every consecutive
gap $p_i-p_{i+1}>\gamma(n):=1/(2^{n+1}-1)$. $V(p)$ is the inner-minimax game
value at partition $p$ (`lemmas/reduction-to-multiset-minimax.md`). By the
certified Global Vertex Lemma and Lipschitz continuity
(`lemmas/global-vertex-lemma-and-lipschitz-continuity.md`), $V$ is $1$-Lipschitz
in $\ell^1$ and equals $\min_{\sigma\in\Sigma}f_\sigma(p)$ over valid affine
branches $\sigma$ in a finite shape set $\Sigma=\Sigma(n,k)$.

## 1. Finite-Cell Affine-Vertex Reduction Theorem (corrected)

**Definition of $L$ (corrected).** $L$ is the finite list of affine functionals
on $\{p\in\mathbb R^k:\sum p_i=1\}$ consisting of: every coordinate of every
$x_\sigma(p)$ ($\sigma\in\Sigma$); every pairwise branch-comparison difference
$f_\sigma(p)-f_\tau(p)$; and the region's own defining functionals
$p_1-\tfrac12,\ p_i-p_{i+1}-\gamma(n)$ ($i=1,\dots,n$), **and** $p_k$ (the
functional omitted in the round-9 draft, whose omission the reviewer found
non-redundant — the region cut by the other functionals alone is unbounded and
admits $p_k<0$).

**Theorem.** For every $p^*\in\overline{B(n)}$ attaining $\max_{p\in
\overline{B(n)}}V(p)$, there is a cell $C$ of the (corrected) $L$-arrangement
with $p^*\in\overline C\cap\overline{B(n)}$, and $V(p^*)=V(q^*)$ for some
$q^*\in Q:=\{$solutions of some $(k-1)$-subset of $L$ set to $0\}$, a finite,
$p$-independent candidate set. No concavity of $V$ is used.

**Proof sketch (full proof in the approach file, Section 4).** (i) Cell-wise
constancy: each $\ell\in L$ has constant sign on each open connected component
("cell") of the complement of $\bigcup_{\ell\in L}\{\ell=0\}$, since $L$ is
finite and every $\ell$ is affine (hence continuous, never vanishing on a
connected component avoiding its zero set); this makes both branch-validity and
branch-ordering constant on each cell, so $V$ equals a single affine formula
$f_{\sigma(C)}$ throughout $C$. (ii) Boundary extension: $V$ (Lipschitz,
certified) and $f_{\sigma(C)}$ (affine, hence continuous) agree on the open,
dense cell $C$, hence agree on all of $\overline C$ by continuity, in particular
on $P:=\overline C\cap\overline{B(n)}$. (iii) $P$ is a closed bounded convex
polytope on which $V=f_{\sigma(C)}$ is affine, so its max over $P$ is attained
at a vertex of $P$ (elementary polytope fact, proved from scratch), and every
vertex of $P$ solves some $(k-1)$-subset of $L$ set to zero.

**Verification of the fix.** The reviewer independently confirmed: (a) $L$
without $p_k$ cuts out an unbounded region admitting $p_k<0$ (send one gap to
$+\infty$, compensate by making $p_k$ very negative while keeping $p_1\le1/2$);
adding $p_k$ restores boundedness. (b) $p_i\ge0$ for $i<k$ remains redundant
given the gap chain once $p_k\ge0$ is imposed: $p_i\ge p_k+(k-i)\gamma(n)\ge0$,
telescoped from the gap inequalities — reverified independently below (Section
3, Boundary Positivity Fact).

## 2. Small-Mass Insertion Lemma

**Statement.** For finite multisets $M,F$ of positive reals,
$|\mathrm{OddSum}(M\cup F)-\mathrm{OddSum}(M)|\le\mathrm{sum}(F)$.

**Proof.** Single-element case $F=\{t\}$: comparing $M\cup\{t\}$ and $M\cup\{0\}$
(same cardinality) rank-by-rank, the total absolute difference telescopes
exactly to $t$ regardless of where $t$ inserts in sorted order; apply the
certified 1-Lipschitz-in-$\ell^1$ fact for OddSum at fixed cardinality (Section
2 of the approach file, itself an immediate rank-matched triangle inequality).
General $F$: induct on $|F|$ via the triangle inequality. $\blacksquare$

## 3. Boundary Continuity Theorem

**Statement.** For $p^0=(p_1,\dots,p_n,0)\in\overline{B(n)}$ (so $p_1,\dots,p_n$
sum to $1$ and satisfy the region's other closed inequalities): (Boundary
Positivity) $p_i\ge(n+1-i)\gamma(n)>0$ for each $i\le n$ — telescoped directly
from the closed gap inequalities down from $p_{n+1}=0$. (Boundary value) the
continuous (Lipschitz) extension $\bar V$ of the $(n+1)$-piece value function
satisfies $\bar V(p^0)=V_n(p_1,\dots,p_n)$, the $n$-piece value function at the
surviving coordinates. Consequently $\bar V(p^0)\le c(n)$ (since $V_n(\tilde
p)\le1/2<c(n)$ by the certified Perfect-Pairing Corollary,
`lemmas/perfect-pairing-subadditivity-and-general-insertion.md`).

**Proof.** Via the path $p^{(t)}=(p_1-t/n,\dots,p_n-t/n,t)\to p^0$, a two-sided
$O(t)$ sandwich using the proportional-transport construction (certified
Lipschitz proof) combined with the Small-Mass Insertion Lemma above, then
$t\to0^+$. Full detail in the approach file, Section 4.2.

## 4. Region-Vertex Classification Theorem

**Statement.** Reparametrizing $\overline{B(n)}$ (region-only, dropping the
$\Sigma$-shape functionals of $L$) as an $n$-simplex $\Delta$ (in slack
coordinates $a=\tfrac12-p_1\ge0$, $g_i=p_i-p_{i+1}-\gamma(n)\ge0$) sliced by
$z:=p_k\ge0$: $\overline{B(n)}$ has exactly $3$ vertices for $n=2$ ($e_0,e_1,e_2$,
all with $z>0$), $5$ for $n=3$ ($e_0,e_1$ with $z>0$; $e_2$ with $z=0$ exactly;
two further $z=0$ crossing points on edges $e_0$–$e_3$, $e_1$–$e_3$), and
$2+2(n-1)$ for $n\ge4$ (two genuine, $z>0$: $e_0,e_1$; the rest, $z=0$ crossing
points on the $2(n-1)$ edges from $\{e_0,e_1\}$ to $\{e_2,\dots,e_n\}$).

**Proof.** Via the exact sign computation $N(n,j)=j(2n+1-2^{n+1})+(2^{n+2}-n^2-
n-2)$ for $z(e_j)$'s numerator (denominator always positive), and three closed
sign claims: (A) $z(e_0)>0$ for all $n\ge2$; (B) $N(n,1)=2^{n+1}+n-n^2-1>0$ for
all $n\ge2$ (induction, recursion $h(n+1)=2h(n)+(n^2-3n+1)$, base cases
$h(2)=5,h(3)=9$); (C) $N(n,\cdot)$ strictly decreasing in $j$ (coefficient
$2n+1-2^{n+1}<0$), with $N(n,2)=n(3-n)$ exactly (so $>0$ at $n=2$, $=0$ at
$n=3$, $<0$ for $n\ge4$), giving the vertex count and sign pattern for every
$n\ge2$.

**Independent verification (reviewer).** Re-derived $N(n,j)$ from scratch and
computed it directly (not via the closed form) for $n=2,\dots,9$, $j=1,\dots,n$:
matches the closed form exactly in all cases, confirming the sign pattern
(positive at $j=1$ for all tested $n$; $N(n,2)=n(3-n)$ exactly; strictly
decreasing in $j$).

## 5. Exact closure of the region-only genuine vertices ($e_0,e_1$, and $e_2$ at $n=2$)

**Statement.** At $e_0$ (all $n+1$ pieces form one AP run, common difference
$\gamma(n)$) and $e_1$ ($p_1=1/2$ unpaired, pieces $2,\dots,n+1$ form an AP run),
pairing consecutive AP terms and bisecting any unpaired piece(s) via the
certified General $k$-Anchor-Merge Lemma (Theorem 10,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`) gives, exactly,
$\mathrm{OddSum}=\tfrac12$ (if the number of pairs $k$ is even) or $c(n)$ (if
$k$ is odd) — in both cases $\le c(n)$. The $n=2$ third vertex $e_2$ is closed
directly, $V(e_2)\le c(2)=4/7$ exactly.

**Independent verification (reviewer, exact `Fraction` script, $n=2,\dots,8$,
both $e_0$ and $e_1$).** Reconstructed each vertex's coordinates from the
closed-form slack formulas, applied the stated $k$-Anchor-Merge construction
literally (including the untouched copies at multiplicity $2$), and computed
$\mathrm{OddSum}$ by direct sort-and-sum: in every one of the 14 instances
tested, the result matches the predicted parity rule exactly ($=1/2$ when $k$
even, $=c(n)$ when $k$ odd), confirming both the vertex coordinate formulas and
the closed-form evaluation.

## Scope / what remains open

This certifies the full closure of the region-only candidate sub-list
$Q_{\mathrm{region}}\subset Q$ (every $q\in Q$ arising from a $(k-1)$-subset of
$L$ drawn entirely from the region functionals, no $\Sigma$-shape functional):
$V(q)\le c(n)$ for every such $q$, every $n\ge2$. The $\Sigma$-shape part of
$Q$ (candidates involving a branch-validity or branch-comparison boundary) is
**not** addressed by this certification; nothing here shows the true maximizer
$p^*$ of $V$ over $\overline{B(n)}$ avoids that part of $Q$, so the Existence
Theorem itself (the approach's ultimate target) remains open.
