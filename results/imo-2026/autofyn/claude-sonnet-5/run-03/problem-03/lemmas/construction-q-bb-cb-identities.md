# Constructions Q, BB, CB — exact closed-form value identities, and the Duplicate-Pair Contribution Fact

**Source:** `global-lp-vertex-sufficiency`, round 22 Section 13. Certified by proof-reviewer, round 22, after independent re-derivation (own `sympy`/exact-`Fraction` scripts, not reused from the builder).

Notation: $p\in B(3)$, $g_1=p_1-p_2$, $g_2=p_2-p_3$, $g_3=p_3-p_4$,
$c(3)=8/15$, $\gamma(3)=1/15$.

## Duplicate-Pair Contribution Fact (general-purpose, elementary)

In any finite multiset sorted descending, a value of even multiplicity
$2j$ contributes exactly $j$ copies of itself to $\mathrm{OddSum}$,
regardless of where the block sits in the sorted order (any $2j$
consecutive integer ranks contain exactly $j$ odd ranks).

**Independently verified**: 5000-trial exact-`Fraction` test — for random
base multisets with a random even-multiplicity duplicate block appended,
$\mathrm{OddSum}(\text{with block})-\mathrm{OddSum}(\text{without block})
=j\cdot(\text{duplicate value})$ exactly, zero mismatches.

## Construction Q

Split $p_1\to(p_1/2,p_1/2)$, $p_2\to(g_2,p_3)$ (leave $p_3,p_4$ untouched).
Whenever $4g_1+5g_2+p_4<1$, $p_4<(1+2g_1+g_2)/7$, and $p_4>g_2$ (all hold
simultaneously on an explicit sub-region of $B(3)$):
$$\mathrm{OddSum}(Q)-c(3)=\frac{p_4-g_2-\gamma(3)}2.$$

## Construction BB

Split $p_1\to(g_1,p_2)$, $p_3\to(p_3/2,p_3/2)$ (leave $p_2,p_4$ untouched).
Whenever $4g_1-g_2+p_4<1$, $7g_1+2g_2+p_4\ge1$, $g_1+2g_2+7p_4<1$:
$$\mathrm{OddSum}(BB)-c(3)=\frac{g_1-p_4-\gamma(3)}2.$$

## Construction CB

Split $p_1\to(g_1,p_2)$, $p_4\to(p_4/2,p_4/2)$ (leave $p_2,p_3$ untouched).
Order conditions: $p_2>g_1$ (i.e. $4g_1-g_2+p_4<1$) and $g_1>p_4/2$.
$$\mathrm{OddSum}(CB)-c(3)=\begin{cases}
\frac{2g_1}3+\frac{g_2}3+\frac{p_4}6-\frac15 & \text{if }4g_1+2g_2+p_4\ge1
\ (g_1\ge p_3)\\[4pt]
-\frac{2g_1}3-\frac{g_2}3-\frac{p_4}6+\frac2{15} & \text{if }4g_1+2g_2+p_4<1
\ (p_3>g_1)
\end{cases}$$
(the two branches agree exactly on the shared boundary $g_1=p_3$).

## Independent verification (this review)

All three identities re-derived from scratch symbolically (own `sympy`
script, using $p_4=(1-g_1-2g_2-3g_3)/4$ and back-substituting $p_1,p_2,p_3$
in terms of $g_1,g_2,g_3,p_4$): `sympy.simplify` confirms each identity is
exactly $0$ residual. Direct numeric check at the exact rational point
$p=(6,4,2,1)/13$ (a valid point of $B(3)$, Region II): $\mathrm{OddSum}(C)=
\mathrm{OddSum}(Q)=\mathrm{OddSum}(BB)=7/13$ exactly (all three tied,
matching the file's claimed exact counterexample), $H$ and $W$ both
illegal there ($x=(p_3-g_1)/2=0$; $p_1-p_2-p_3=0$), and $\mathrm{OddSum}
(CB)=1/2$ exactly, both $<c(3)=8/15$ — confirming CB genuinely fixes this
specific exact point.

## Scope (honest, not an overclaim)

Each identity is proved only on its own explicit order-condition domain
(not shown to be all of Region II). No case-complete (non-numeric) proof
that $\min\{H,C,Q,R,BB,W,CB\}\le c(3)$ holds everywhere on $B(3)$ or even
on Region II is given — only a broad (18-restart differential-evolution)
numeric search supports this, and is explicitly not a proof. The exact
point $p=(6,4,2,1)/13$ is a genuine, reviewer-confirmed counterexample to
the smaller 6-construction panel $\{H,C,Q,R,BB,W\}$ (without CB) and should
be used as a mandatory regression check for any future candidate panel.
