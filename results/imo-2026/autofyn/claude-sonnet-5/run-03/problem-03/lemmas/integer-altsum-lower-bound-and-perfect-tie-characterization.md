# Integer-Alternating-Sum Lower Bound Lemma, and the Perfect-Tie-Family Exact Characterization at $e_0$

Certified round 12, from `approaches/lp-duality-split-polytope.md`
Section "Round 12: the Perfect-Tie-Family Exact Characterization at
$e_0$". Independently re-verified by the proof-reviewer (exact `Fraction`,
brute force over all active-set choices, $n=2,\dots,12$, 0 mismatches).

## Integer-Alternating-Sum Lower Bound Lemma (general-purpose)

**Statement.** Let $v_1>v_2>\cdots>v_m\ge0$ be $m$ distinct nonnegative
integers. Then $\mathrm{AltSum}(\{v_1,\dots,v_m\}):=v_1-v_2+v_3-\cdots\pm
v_m\ge\lfloor m/2\rfloor$.

**Proof.** Pair consecutively from the top: $(v_1,v_2),(v_3,v_4),\dots$,
giving $\lfloor m/2\rfloor$ pairs (plus a leftover $v_m\ge0$ if $m$ is
odd). Each pair difference $v_{2j-1}-v_{2j}\ge1$ (distinct integers,
strictly decreasing). Summing gives $\mathrm{AltSum}\ge\lfloor m/2
\rfloor$; the odd leftover only adds a non-negative amount. $\blacksquare$
Equality iff consecutive kept pairs are adjacent integers (and, if $m$
odd, the smallest kept value is $0$).

## Perfect-Tie construction family at $e_0$

At the region vertex $e_0$ (AP partition
$p_i=p_{n+1}(e_0)+(n+1-i)\gamma(n)$, $\gamma(n)=1/(2^{n+1}-1)$, certified
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`), a
**Perfect-Tie construction** chooses an active set $S\subseteq\{1,\dots,
n+1\}$, $|S|=s\le n$, splits every $p_i$ ($i\in S$) into fragments, and
ties every fragment into an even-multiplicity equal-value block using
only fragments of $S$ (self-tie or genuine cross-piece fragment-vs-
fragment tying — this excludes only the already-refuted
tie-to-whole-untouched-piece family), with zero residual. Every $j\notin
S$ is left untouched.

**Lemma (exact value, via the certified Singleton-Interleaving Lemma,
Theorem 9).** For any Perfect-Tie construction with active set $S$,
$\mathrm{OddSum}(M)=\tfrac12+\tfrac12\mathrm{AltSum}(U)$, $U:=\{p_i(e_0):
i\notin S\}$ — depends only on which pieces are untouched, not on the
internal tying pattern. (Reviewer independently confirmed this identity
against a literal bisection construction, $n=4,6,8$, 30 random active
sets each, exact match.)

## Theorem (Perfect-Tie-Family Exact Characterization at $e_0$)

Write $m:=n+1-s=|U|$. For every $n\ge2$:
$$\min_{|S|=s}\mathrm{OddSum}(M)=\begin{cases}
\tfrac12+\tfrac{\gamma(n)m}4, & m\text{ even},\\[4pt]
\tfrac12+\tfrac{p_{n+1}(e_0)}2+\tfrac{\gamma(n)(m-1)}4, & m\text{ odd}.
\end{cases}$$
Consequently: (1) every odd-parity $s$ fails (exceeds $c(n)$) for every
$n\ge2$, since $p_{n+1}(e_0)>\gamma(n)$ for every $n\ge2$ (proved by
induction from the certified bound $n(n+1)\gamma(n)<1$); (2) among
even-parity $s$, the achieved value is $\le c(n)$ iff $m\le2$, and since
$s\le n$ forces $m\ge1$, the **only** legal value is $m=2$, i.e.
$s=n-1$; (3) at $s=n-1$ the value is **exactly** $c(n)$ (never below).

**Corollary (Bounded-$s_0$ impossibility, Perfect-Tie family).** For any
fixed $s_0$, once $n>s_0+1$, no Perfect-Tie construction with $\le s_0$
active pieces achieves $\mathrm{OddSum}(M)\le c(n)$.

**Reviewer verification.** Independent brute-force exact-`Fraction`
script: for $n=2,\dots,12$, every active-set size $s=0,\dots,n$
(exhaustive over all $\binom{n+1}{s}$ choices, not just the closed-form
prediction), the true minimum $\mathrm{OddSum}(M)$ over all active-set
choices of that size matches the closed form exactly in every one of the
tested $(n,s)$ pairs; the theorem's three consequences (odd fails, only
$m=2$ works among even, $s=n-1$ hits $c(n)$ exactly) hold with zero
exceptions across all tested $n$.

## Scope (honest, as reported by the builder, unchanged by certification)

This is a complete, proved characterization of the Perfect-Tie
(zero-residual) sub-family specifically. It is **structurally disjoint**
from the round-11 Mass-Constraint Theorem (`lemmas/rank-pinning-lemma-
and-mass-constraint-theorem.md`, which covers tie-to-whole-untouched-piece
constructions) — no untouched piece's mass is ever consumed as a tie
target here — proved by a different technique (integer combinatorics vs.
mass summation), giving independent convergent evidence that no bounded
named-tool family suffices at $e_0$. It does **not** resolve the fully
general fragment-vs-fragment family (nonzero residual permitted), which
remains open (a numerical spot-check at $n=6,s=3$ found a nonzero-residual
construction beating the Perfect-Tie optimum, though still short of
$c(6)$).
