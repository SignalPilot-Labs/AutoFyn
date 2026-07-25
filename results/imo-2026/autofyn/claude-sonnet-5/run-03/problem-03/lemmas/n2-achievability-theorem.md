## Source
`approaches/global-lp-vertex-sufficiency.md`, round 20, Section 10.6
(rewritten in full) and Section 11.1. Certified by the round-20
proof-reviewer after full independent re-derivation (own exact-`Fraction`
fine-grid search over every one of the ten finite response shapes at
$p^*$, built directly from the shapes' definitions, not the builder's
script).

## Theorem ($n=2$ Achievability, completing the $n=2$ Existence Theorem)

At $p^*=(4/7,2/7,1/7)$ (the "geometric" witness partition, $k=3$, all $\le
2$-cut responses), every one of the ten finite response shapes
$(m_1,m_2,m_3)$ with $m_1+m_2+m_3\le2$ (guaranteed exhaustive by the
already-certified Global Vertex Lemma) satisfies $\mathrm{OddSum}(M)\ge
c(2)=4/7$, with equality attained (e.g. shapes $(2,0,0)$ and $(1,1,0)$).
Combined with the already-certified $n=2$ Existence Theorem upper-bound
witness ($V(p^*)\le c(2)$,
`n2-existence-theorem-upper-bound.md`-adjacent result), this gives
$$V(p^*)=c(2)=\tfrac47\ \text{exactly, both directions fully proved.}$$

*Proof (casework, source Section 10.6).* Write $t=1/7$ so $p_1=4t,p_2=2t,
p_3=t$. Three shapes ($(0,0,0),(0,1,0),(0,0,1)$) reduce trivially: the
untouched $p_1=4t$ remains the unconditional rank-1 element and all other
terms are $\ge0$, giving $\mathrm{OddSum}\ge4t$ immediately (values $5t,
5t,4.5t$ respectively — wait, exact values $5/7,5/7,9/14$). Shape $(1,0,0)$
gives $\mathrm{OddSum}=4t=c(2)$ exactly by a 4-sub-case order analysis.
The remaining six two-cut shapes ($(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),
(0,1,1)$) are closed by an exhaustive order/rank analysis on the induced
5-element multiset in each case (three via trivial nonnegativity since
$p_1=4t$ dominates; three — $(2,0,0),(1,1,0),(1,0,1)$ — via an
$M_1+m_1\ge4t$ identity proved by a 2–3-sub-case order split). Full
details in the source file.

## Independent verification (round-20 proof-reviewer)

Own exact-`Fraction` fine-grid search (not random sampling), built
directly from each shape's definition:
- $(0,0,0),(1,0,0),(0,1,0),(0,0,1)$: dense 1-parameter grid (400 steps).
- $(2,0,0),(0,2,0),(0,0,2)$: dense 2-simplex grid (80 subdivisions per
  axis).
- $(1,1,0),(1,0,1),(0,1,1)$: dense 2-parameter grid ($120\times120$).

**Result: the observed global minimum matches the file's claimed exact
value digit-for-digit in every one of the ten shapes** — $5/7$ ($000$),
$4/7$ ($100$), $5/7$ ($010$), $9/14$ ($001$), $4/7$ ($200$), $5/7$ ($020$),
$9/14$ ($002$), $4/7$ ($110$), $4/7$ ($101$), $9/14$ ($011$) — zero
violations of $\ge c(2)=4/7$ anywhere. Since each shape's $\mathrm{OddSum}$
is piecewise-linear in its free parameters, a sufficiently fine rational
grid (matching the claimed rational optimum exactly, as observed here)
reliably locates the true minimum; the exact match across all ten
independently-computed shapes is strong corroboration of the casework
proof, not merely consistency.

## Status
**Certified.** This completes the full $n=2$ Existence Theorem
($V(p)\le c(2)$ for all $p\in B(2)$, from the round-19 certified upper
bound, plus $V(p^*)=c(2)$ exactly from this theorem) — a genuine, complete
milestone for $n=2$. $n\ge3$ remains open and is **not** addressed by this
lemma.
