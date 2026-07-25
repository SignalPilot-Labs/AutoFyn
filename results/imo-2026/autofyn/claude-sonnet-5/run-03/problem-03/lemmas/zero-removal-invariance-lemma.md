# Zero-Removal Invariance Lemma

Certified round 15 (proof-reviewer), from `global-lp-vertex-sufficiency.md`
Section 6.1.

## Statement

Let $M$ be a finite multiset of nonnegative reals, and let $M_0$ denote $M$
with every zero-valued element removed. Then
$\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$.

## Proof

Sort $M$ descending: $m_1\ge m_2\ge\cdots\ge m_N\ge0$. Let $z\ge0$ be the
number of zero elements. Since the list is sorted descending and every
element is $\ge0$, the zero elements occupy exactly the last $z$ positions
$m_{N-z+1},\ldots,m_N$ (a zero element cannot precede a nonzero one in a
descending sort, as $0$ is the minimum possible value), and
$m_1,\ldots,m_{N-z}$ — the nonzero elements, in the same relative order —
is exactly $M_0$ sorted descending. Hence
$$\mathrm{OddSum}(M)=\sum_{j\text{ odd},\,1\le j\le N}m_j
=\sum_{j\text{ odd},\,1\le j\le N-z}m_j+\sum_{j\text{ odd},\,N-z+1\le
j\le N}m_j.$$
The second sum is $0$ (every term is one of the zero elements, contributing
$0$ regardless of whether its own rank is odd or even). The first sum is,
by definition, exactly $\mathrm{OddSum}(M_0)$. $\blacksquare$

## Reviewer independent verification

Own exact-`Fraction` script (not the builder's), 20,000 random multisets
(size 0–10, random positive rationals padded with 0–10 zero elements):
zero violations of $\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$.

## Reusable by

Any future approach needing to relate the value of a degenerate response
(some fragment exactly $0$) to the value of a strictly-fewer-move response
on the same instance. Used in `global-lp-vertex-sufficiency.md` Section
6.2 to show that branch-validity-boundary candidates in the Finite-Cell
Theorem's candidate set $Q$ always encode an $(n-1)$-or-fewer-cut shape,
not a genuinely new $n$-cut obstruction (that downstream application does
not, by itself, close the Existence Theorem's remaining gap — see
`global-lp-vertex-sufficiency.md` Section 6.3 for what remains open).
