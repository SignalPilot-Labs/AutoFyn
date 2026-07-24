## Statement (DEAD-END RECORD, not a positive reusable lemma)

The round-5 outline's "band-invariance formula" conjecture — that
$A(F\cup T)$ (for $F$ subject to the $\le n+1$-part cardinality bound)
depends only on $F$'s per-band occupancy pair $(m_j,\mu_j)$ (count and total
mass of $F$-parts landing in each of $T$'s dyadic bands), not on the exact
within-band positions — is **FALSE**.

**Counterexample.** $n=4$ ($D=31$): $T=\{8/31,4/31,2/31,1/31\}$, band
$(2/31,4/31)$. Two partitions $F$ with identical per-band occupancy data
($(m_0,\mu_0)=(1,x_0)$, $(m_2,\mu_2)=(2,p_1-x_0)$, all else empty) but
different within-band placements give $A(F\cup T)=3781/38750$ versus
$15031/155000$ — these differ (difference $93/155000\ne0$).

## Verification (proof-reviewer, round 5)

Independently re-verified by exact `Fraction` computation: both partitions
checked to sum exactly to $p_1$ and to place both fragments strictly inside
the same band; $A$ values recomputed directly by sort-and-alternate-sum and
match the builder's claimed values exactly; the two values are confirmed
unequal. Genuine and correct refutation.

## Why this matters

Shows the coarse "count + mass per band" invariant genuinely loses
information needed to determine $A(F\cup T)$ — any correct closed form must
retain finer within-band shape information (at least as detailed as
`rank-pigeonhole-budget`'s per-band partition-shape decomposition, itself
still open). Do not re-attempt a pure count/mass-only band-occupancy
formula for this problem.

## Recorded as

`results/imo-2026-03/approaches/dyadic-band-occupancy.md`, Proposition 3
(round 5, new slug).
