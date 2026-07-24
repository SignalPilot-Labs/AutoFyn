## Statement

For any finite multiset $S$ of reals, writing $E(S)$ for the sum of its
even-sorted-rank elements (2nd, 4th, ...) and $\mathrm{Total}(S)$ for its
sum,
$$E(S)\ \le\ \frac{\mathrm{Total}(S)}2,$$
equivalently (via $A(S)=\mathrm{Total}(S)-2E(S)$) $A(S)\ge0$ for every
finite multiset of reals.

## Proof

Sort $S$ descending. Pair consecutive ranks $(2i-1,2i)$: since the sort is
descending, $L_{2i}\le L_{2i-1}$ for every complete pair. Summing over all
complete pairs, (sum of even-rank elements in complete pairs) $\le$ (sum of
odd-rank elements in complete pairs); if $|S|$ is odd there is one leftover
unpaired element at the final (odd) rank, contributing only to the
odd-sum. Hence $E(S)\le O(S)$ (sum of odd-rank elements), so
$2E(S)\le O(S)+E(S)=\mathrm{Total}(S)$. $\blacksquare$

## Remark

This is the same fact as "$A(S)\ge0$, immediate from
`integral-alternating-sum-formula`'s nonnegative-integrand
representation," restated as an $E$-bound for reuse by approaches working
directly in the even-rank-sum ($E$) language rather than the integral
language.

## Verification (proof-reviewer, round 7)

Elementary and re-derived by hand, no gap — a direct pairwise-domination
argument with no game-specific content. Used in
`rank-pigeonhole-budget.md` §4.8 (the $k=m+1$ boundary closure of Branch A
of the peel-the-minimum mechanism); the chain of inequalities there
($E(F\cup\tau')\le\mathrm{Total}(F\cup\tau')/2\le(2\tau_1+R(\tau'))/2=
R(\tau)$, using $R(\tau)+\tau_m=2\tau_1$) was independently re-checked by
hand, algebra correct.

## Origin

`results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §4.7 (round 7).

## Certification note (proof-reviewer, round 7)

**CERTIFIED.** Fully general, elementary, no gap.
