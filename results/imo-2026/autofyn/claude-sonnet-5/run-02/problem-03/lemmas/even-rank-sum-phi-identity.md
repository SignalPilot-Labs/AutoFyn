## Statement

For any finite multiset $U$ of positive reals with a strict unique maximum
$m$, and $U'':=U\setminus\{m\}$, the sum of $U$'s even-sorted-rank elements
(2nd, 4th, ...) equals $\Phi(U'')$:
$$E(U) := \sum_{i\text{ even}}L_i^{(U)} = \Phi(U'') = \frac{\mathrm{Total}(U'')+A(U'')}2.$$

Fully general — no ladder-specific structure required.

## Proof

Since $m$ is the strict unique max, sorting $U$ gives $m$ at rank 1 and the
sorted list of $U''$ occupying ranks $2,3,4,\dots$ in order (rank $k+1$ of
$U$ = rank $k$ of $U''$). So $U$'s even ranks (2,4,6,...) correspond to
$U''$'s odd ranks (1,3,5,...): $E(U)=M_1+M_3+M_5+\dots$ where
$M_1\ge M_2\ge\dots$ are $U''$'s sorted elements. Writing this as
$(M_1-M_2+M_3-\dots)+\left(M_2+M_4+\dots\right)=A(U'')+E(U'')$ and using
$E(U'')=(\mathrm{Total}(U'')-A(U''))/2$ (from $A=$ odd-sum $-$ even-sum,
Total $=$ odd-sum $+$ even-sum) gives
$E(U)=A(U'')+(\mathrm{Total}(U'')-A(U''))/2=(\mathrm{Total}(U'')+A(U''))/2
=\Phi(U'')$.

## Verification (proof-reviewer, round 5)

Independently re-verified by 2000 random exact-`Fraction` trials (random
multisets with distinct elements, so the unique-max hypothesis holds):
directly computed $E(U)$ by sort-and-sum and compared against $\Phi(U'')$ —
zero mismatches.

## Origin / usage

Derived in `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` §3
(round 5), used to reduce Case II of claim (A)'s lower bound to a
one-level-smaller instance of the same shape (peeling $p_2$ off
$F'\cup T$).

## Certification note (proof-reviewer, round 5)
**CERTIFIED.** Fully general, gap-free, independently re-verified. Promoted
to `lemmas/`.
