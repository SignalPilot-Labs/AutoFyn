## Statement

If Liu Bang marks $j\le n-1$ points, Xiang Yu has a strategy (bisecting each
of the resulting $\le n$ pieces once) forcing $\Phi=1/2$ exactly, regardless
of where Liu Bang's points are. Since $2^n/(2^{n+1}-1)>1/2$ for all $n\ge0$,
this is strictly worse for Liu Bang than the ladder construction, so in
analyzing the optimum Liu Bang may assume WLOG he uses exactly $n$ points.

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 4.
Immediate from the degenerate case of the leftover-formula lemma: bisecting
every piece produces an all-paired multiset with $A=0$, hence $\Phi=1/2$.

## Certification note (proof-reviewer, round 1)

Correct and immediate given the certified leftover-formula lemma. Note this
only reduces Liu Bang's optimal choice to "exactly $n$ points" — it does not
by itself say anything about which $n$-point configuration is optimal.
Certified correct.
