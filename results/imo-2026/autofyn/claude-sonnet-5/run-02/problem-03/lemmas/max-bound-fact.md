## Statement (CERTIFIED — round 32, proof-reviewer)

**Max Bound.** For any finite multiset $S$ of nonnegative reals,
$$A(S)\ \le\ \max(S)$$
(with $A(\varnothing):=0\le0$ by convention).

## Proof

Write $S$ sorted descending $s_1\ge s_2\ge\cdots\ge s_n\ge0$ ($s_1=\max(S)$).
$$A(S)=s_1-s_2+s_3-s_4+\cdots = s_1-\big[(s_2-s_3)+(s_4-s_5)+\cdots\big].$$
Each bracketed term is $\ge0$ since the sequence is sorted descending (a
possible unpaired trailing term is itself $\ge0$). Hence $A(S)\le s_1=
\max(S)$. $\blacksquare$

(Equivalently: an immediate corollary of `sharp-dominant-removal-identity`
plus $A\ge0$: $A(S)=s_1-A(S\setminus\{s_1\})\le s_1$.)

## Verification

Independently re-derived and verified by the proof-reviewer (round 32):
50,000 random exact-`Fraction` trials (multiset sizes 0–7), zero violations.

## Origin / usage

Proved in `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` §7.19.2,
round 32. Used as a building block for the Insertion Sandwich Lemma and the
Master Theorem (both this round).
