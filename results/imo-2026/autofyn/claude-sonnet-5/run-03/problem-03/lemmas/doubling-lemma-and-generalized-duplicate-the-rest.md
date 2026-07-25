## Lemmas: Doubling Lemma, and Generalized Duplicate-the-Rest (arbitrary LB partition)

### Theorem 1 (Doubling Lemma)

**Statement.** For any finite multiset $R$ of positive reals with sum $S$,
$\mathrm{OddSum}(R\cup R)=S$ (duplicating every element and playing the
alternating-claim game on the doubled multiset gives the first mover
exactly the *undoubled* sum, regardless of ties/multiplicities within $R$
itself).

**Proof.** Group $R\cup R$ by distinct value $v_1>\cdots>v_t$ with
multiplicities $c_1,\dots,c_t$ in $R$ ($S=\sum c_jv_j$); each value has
even multiplicity $2c_j$ in $R\cup R$ and forms a block of consecutive
ranks in the descending sort. Any block of even length $2c$, starting at
any rank $e$, splits exactly $c$ odd-ranked and $c$ even-ranked positions
(pairing $e,e+1$ then $e+2,e+3$, etc. — true for any starting parity).
Since the first mover gets exactly the odd-ranked elements
(Greedy-Optimality Lemma), it gets exactly $c_j$ of each block, total
$\sum c_jv_j=S$. $\blacksquare$

**Independent verification.** Brute-force checked by the proof-reviewer
over 2000 random integer multisets $R$ (sizes 1–6): exact match in every
case.

### Theorem 2 (Generalized duplicate-the-rest)

**Statement.** Let $p_1\ge p_2\ge\cdots\ge p_{n+1}>0$ sum to $1$ with
$p_1\ge S:=p_2+\cdots+p_{n+1}$. Let $R=(p_2,\dots,p_{n+1})$,
$\ell:=p_1-S\ge0$. XY's move: replace $p_1$ by $R\cup\{\ell\}$ (a valid
$\le n$-cut split of $p_1$). The resulting multiset
$M=(R\cup R)\cup\{\ell\}$ ($\ell=0$: $M=R\cup R$) has
$\mathrm{OddSum}(M)=p_1$ **exactly**.

**Proof.** $\ell=0$ case is immediate from Theorem 1. For $\ell>0$: exhaustive
two-case split according to whether $\ell$ coincides with a value already
occurring in $R$ (Case (a): no; Case (b): yes, $\ell=v_w$). In both cases,
every $v_j$-block ($j\ne w$ if applicable) retains even length and splits
evenly by Theorem 1's Claim (parity-independence of even-length block
splits), and $\ell$ itself (Case (a): a singleton at an odd rank since the
number of elements above it is even; Case (b): merged into an odd-length
block of length $2c_w+1$ starting at an odd rank, giving the first mover
$c_w+1$ of the $2c_w+1$ copies) contributes exactly $\ell$ extra to the
first mover beyond the even blocks' $S$. Total: $S+\ell=p_1$. Both cases
verified algebraically by the reviewer to be exhaustive and correct
(a value is either present in $R$ or not — no third case).

**Independent verification.** Brute-force checked by the proof-reviewer
over 5000 random partitions with $p_1\ge S$, $n=1,\dots,5$: max error
$1.1\times10^{-16}$ (floating-point noise only).

### Corollary (regime $1/2\le p_1\le c(n)$ closed, general LB partition)

If $1/2\le p_1\le c(n)$, Theorem 2 gives an explicit $\le n$-cut XY
response achieving $\mathrm{OddSum}=p_1\le c(n)$ — closing this whole
regime of the general upper bound, for every $n$ and every LB partition
with $p_1$ in this range (not just the geometric one).

**Source.** Both theorems proved in
`approaches/universal-halving-adversary.md` (round 2, Theorem 1, Theorem
2). Certified by the proof-reviewer, round 2.

**Reuse.** The Doubling Lemma is a general-purpose reusable fact about
self-duplicated multisets (useful for any construction that duplicates a
part of a multiset, e.g. self-similar recursive constructions). Theorem 2
strictly generalizes the previously-certified geometric-only identity
(`duplicate-the-rest-exact-response.md`) and is directly reusable by any
future approach attacking the general upper bound: it fully disposes of
the regime $p_1\in[1/2,c(n)]$, leaving only $p_1>c(n)$ and $p_1<1/2$ open.
