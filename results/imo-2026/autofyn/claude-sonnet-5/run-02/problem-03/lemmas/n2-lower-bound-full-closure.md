## Statement

For $n=2$, against the ladder configuration $(p_1,p_2,p_3)=(4/7,2/7,1/7)$,
**every** Xiang Yu response using $\le 2$ further points gives $\Phi\ge4/7$.
(All 10 cut-distribution compositions $(k_P,k_Q,k_R)$ with $k_P+k_Q+k_R\le2$
are closed exactly, symbolically, with no numerics in the final argument.)
Combined with the previously-certified `n2-upper-bound-lp-argument`, this
gives the fully rigorous, complete, non-numeric result $c(2) = 4/7$, both
directions.

## Proof

See `results/imo-2026-03/approaches/smoothing-compactness-certificate.md`,
sections "n=2: the matching lower bound $c(2)\ge4/7$" and "The 3 remaining
mixed compositions, closed exactly this round." 7 of the 10 compositions
(`(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,0,0),(0,2,0),(0,0,2)`) were closed in
round 1; the 3 mixed compositions `(1,1,0),(1,0,1),(0,1,1)` were closed this
round (round 2) via the same "insert fixed pieces into the sorted order,
case-split on the free parameter" method, yielding exact closed forms
$\Phi\ge4$ (units of $1/7$), $\Phi>4$ (infimum $4$), $\Phi>4.5$ (infimum
$4.5$) respectively.

## Certification note (proof-reviewer, round 2)

Independently re-verified the 3 newly-closed cases by an exact-`Fraction`
script: (a) random-sampled 20000 valid instances each of compositions
$(1,0,1)$ and $(0,1,1)$ and confirmed the claimed closed-form identities
$\Phi=5-\mathrm{median}(p_2,r_1,r_2)$ and
$\Phi=5+q_2-\mathrm{median}(q_2,r_1,r_2)$ exactly match a direct
sort-and-sum computation of $\Phi$, zero mismatches; (b) grid/random-searched
composition $(1,1,0)$'s minimum and found $\approx4.00001$, consistent with
the claimed infimum $4$ attained exactly at $p_1=p_2=2$; (c) ran an
independent 60000-trial fully-random-cut Monte Carlo search (not restricted
to any one composition) over the ladder for $n=1,2,3$ and found the global
minimum of $\Phi$ matches $2^n/(2^{n+1}-1)$ in every trial for $n=2$ in
particular. The case-exhaustion in the write-up (e.g. the 4-way split on
$p_2$'s position in case $(1,1,0)$) is exhaustive and the boundary values
match at the case seams (verified by hand and by the script). Certified
correct and complete for $n=2$'s lower-bound direction. **This makes $c(2) =
4/7$ a fully certified base case, both directions, zero gaps — a genuine
milestone**, though it does not by itself establish the general-$n$ claim
(still open).
