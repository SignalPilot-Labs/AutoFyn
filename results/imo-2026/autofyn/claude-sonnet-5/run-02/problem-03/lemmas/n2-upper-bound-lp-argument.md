## Statement

For $n=2$: for every Liu Bang configuration (0, 1, or 2 marked points), Xiang
Yu has an explicit response (using $\le2$ points) with $\Phi\le4/7$. Hence
$c(2)\le4/7$.

## Proof

See `results/imo-2026-03/approaches/smoothing-compactness-certificate.md`,
the "n=2: a complete, rigorous mechanism for the upper bound" section: six
explicit template strategies (bisect-largest, bisect-two-largest,
bisect-smallest, bisect-two-smallest, and two "capture" strategies) with
closed-form $\Phi$ values, combined via a two-region (split on $p\ge1/2$
vs. $p\le1/2$) linear-arithmetic contradiction argument, plus separate
handling of the 0- and 1-point degenerate configurations.

## Certification note (proof-reviewer, round 1)

Independently re-derived: (a) numerically searched 200,000 random points of
the simplex $\{p\ge q\ge r>0,\ p+q+r=1\}$, computing $\min$ over the six
strategies at each point — the maximum of this min over the whole simplex
came out to exactly $4/7\approx0.57143$, attained at the ladder
$(4/7,2/7,1/7)$, matching the claim precisely, with no point found where the
min exceeds $4/7$; (b) independently re-derived the region-1 and region-2
contradiction algebra by hand and it matches the written argument exactly
(region 1: $p<4/7$ contradicts $p>4/7$; region 2: $p>10/21$ contradicts
$p<3/7$, and $10/21>3/7$ checked); (c) spot-checked the "capture" strategies'
extremal boundary case (e.g. Strategy B with $z=0$) directly against the
resulting finite piece multiset and confirmed $\Phi=p$ exactly, and
confirmed it only requires $\le2$ Xiang Yu points (in fact 1, well within
budget) so no legality issue. No numerics remain in the final logical
argument itself — numerics were only used by the reviewer as an independent
cross-check, not as a proof step. Certified correct and complete for
$n=2$'s upper-bound direction only (this lemma does NOT cover the lower
bound or any $n\ge3$).
