## Result (Bounded index-gap density mechanism — refuted)

The proposed mechanism "for each prime $p\in R(a_1)$, consecutive elements
of $I_p:=\{n:p\mid a_n\}$ differ in index by at most $p$" is **false in
general**.

### Refutation (hand-verified counterexample, $a_1=385=5\cdot7\cdot11$)
Direct computation from the recursive definition (independently
re-simulated by the proof-reviewer, exact match):
$$a_1,\dots,a_8 = 385,\ 390,\ 392,\ 396,\ 399,\ 406,\ 418,\ 420.$$
Restricting to $I_5$: $5\mid385,390,420$ and $5\nmid392,396,399,406,418$.
So consecutive elements of $I_5$ include indices $2$ and $8$, an index gap
of $8-2=6>5=p$. This directly refutes the proposed bound.

Not an isolated artifact: a computational sweep (evidence only) over
$a_1=3,\dots,1999$ found further violations, e.g. $a_1=315,p=7$ (index gap
$11>7$); $a_1=429,p=11$ (gap $14>11$); $a_1=1425,p=19$ (gap $25>19$).

### Status
No closed-form bound of this shape (index gap $\le p$) holds in general. A
value-gap variant (consecutive $I_p$-values, not indices, differing by
$\le\mathrm{rad}(a_1)$) is numerically consistent with all tests performed
but has **no proof** and is not claimed here — flagged as an open,
untested-by-proof observation for a future round.

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md`, §12.4, round 5.
Independently re-simulated by the proof-reviewer for $a_1=385$: exact match
of $a_1,\dots,a_8$ and the stated $I_5$ membership.
