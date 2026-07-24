## Statement

Let $S$ be a finite multiset of positive reals with total $T$ and maximum
element $M_1$ (if $M_1$ has multiplicity $>1$, remove exactly one copy). If
$M_1 > T-M_1$ (i.e. $M_1$ exceeds half the total), and $R:=S\setminus\{M_1\}$
(total $\rho:=T-M_1$), then
$$A(S) = M_1 - A(R),$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order functional
of the certified `integral-alternating-sum-formula` lemma.

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 7
(round 2): split the integral-alternating-sum formula's defining integral at
$x=\rho$, using that every element of $R$ is $\le\rho$ (they sum to $\rho$
and are positive) while $M_1>\rho$.

## Certification note (proof-reviewer, round 2)

Independently re-verified by an exact-`Fraction` brute-force script: 3000
random multisets of size 1–6, checked the dominance condition $M_1>T-M_1$,
and compared $A(S)$ (direct sort-and-alternate-sum) against $M_1-A(R)$ — zero
mismatches. The written proof (splitting the integral of Lemma 2 at
$x=\rho$) is algebraically sound on independent re-derivation. Strictly
generalizes the previously-certified `untouched-top-piece-lower-bound` (that
lemma is the special case $S=\{p_1\}\cup G'$ with the ladder's specific
dominance $p_1 > 1 - p_1$). Certified correct, fully general (no ladder- or
game-specific structure required).
