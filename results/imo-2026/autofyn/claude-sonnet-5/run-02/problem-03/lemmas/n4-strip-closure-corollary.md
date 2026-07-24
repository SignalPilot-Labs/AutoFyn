## Statement

For every 5-piece marking $p_1\ge p_2\ge\cdots\ge p_5>0$, $T=\sum p_i$
(the $n=4$ instance of the general upper-bound problem), with
$$\frac{15}{31}T\ \le\ p_1\ <\ \frac T2\qquad\text{and}\qquad p_2>\frac
T{31},$$
the feasibility condition of `half-complement-pin-theorem` (specialized
to $m=5$, untouched index $j=2$) holds automatically, and hence
$$\Phi_{\min}\ \le\ \max(p_1,T-p_1)\ =\ T-p_1\ \le\ \frac{16}{31}T\ =\ a_4T.$$

This closes the sub-strip $p_1\in[15T/31,T/2)$ of the residual
$\mathcal R=\{p_1<T/2,\ T/31<p_2<8T/31\}$ (from `rank-pigeonhole-budget`'s
—rather, `lp-duality-certificate`'s own—R29.2 definition) **unconditionally,
for arbitrary $p_3,p_4,p_5$** compatible with the sorted order and mass
conservation.

## Proof

Since $p_1\ge\frac{15}{31}T$, $T-2p_1\le T-\frac{30}{31}T=\frac1{31}T$.
Since $p_2>\frac1{31}T$ (hypothesis), $p_2>T-2p_1$, i.e. $2p_1+p_2>T$ —
feasibility holds strictly, so $\rho>0$ strictly. By
`half-complement-pin-theorem`, $\Phi=\max(p_1,T-p_1)$; since $p_1<T/2$
by hypothesis, $T-p_1>p_1$, so $\Phi=T-p_1$. Finally $p_1\ge\frac{15}{31}T
=(1-a_4)T$ gives $T-p_1\le a_4T$ directly. $\blacksquare$

The proof uses no information about $p_2$'s upper bound, nor anything
about $p_3,p_4,p_5$ individually beyond the marking being a legal sorted
5-tuple summing to $T$.

## Certification note (proof-reviewer, round 31)

**Certified.** Independently re-derived the algebra above by hand, and
separately verified by constructing the actual 8-element fragment
multiset produced by the strategy (not just the reduced 2-element
formula) and confirming, across 11,625 fresh exact-`Fraction` trials
targeted specifically at the claimed region ($p_1\in[15T/31,T/2)$,
$T/31<p_2<8T/31$, sorted, summing to $T$), that (a) feasibility always
holds, (b) the full-multiset alternating sum matches the reduced formula,
and (c) $\Phi\le a_4T$ throughout — zero violations. Also checked the
"no overlap/miscount" claim: the two previously-known hard witnesses for
$n=4$ ($p_1/T\approx0.379$ and $p_1/T\approx0.467$) both lie strictly
below $15/31\approx0.4839$ (confirmed by direct arithmetic), so this
strip is disjoint from both previously-closed points — genuinely new
territory, not a re-closure inflating the coverage count. **What this
does NOT establish** (recorded so no future round overclaims): full
coverage of the residual $\mathcal R$, or even of the smaller residual
$\mathcal R':=\{p_2\le p_1<15T/31,\ T/31<p_2<8T/31\}$ that remains after
this strip is removed — both remain open; $n=4$'s general upper bound is
not solved by this corollary alone. Certified correct and complete for
its own stated (partial) scope.

## Origin

`results/imo-2026-03/approaches/lp-duality-certificate.md`, round 31,
§R31.2.
