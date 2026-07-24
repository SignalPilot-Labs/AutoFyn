## Statement

For any two finite multisets $X,Y$ of positive reals,
$$A(X)-A(Y)\ \le\ A(X\cup Y)\ \le\ A(X)+A(Y),$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order
functional of the certified `integral-alternating-sum-formula` lemma.

Fully general: no ladder structure, no legality/refinement structure on $X$
or $Y$ is assumed.

## Proof

By `cross-term-identity-threshold` with $F=X$, $G=Y$, threshold
$r=\mathrm{Total}(Y)$:
$$A(X\cup Y)=A(X)+A(Y)-2\int_0^r u_X(x)v_Y(x)\,dx,$$
where $u_X,v_Y\in\{0,1\}$ are the odd-parity indicators of $X,Y$. Since
$u_X,v_Y\ge0$ pointwise, $\int_0^r u_Xv_Y\ge0$, giving
$A(X\cup Y)\le A(X)+A(Y)$ immediately.

For the lower bound: since $u_X\le1$ pointwise, $\int_0^r u_Xv_Y\,dx\le
\int_0^r v_Y\,dx$. By `cross-term-identity-threshold`'s own proof, every
element of $Y$ is $\le r=\mathrm{Total}(Y)$, so $v_Y(x)=0$ for $x\ge r$,
hence $\int_0^r v_Y\,dx=\int_0^\infty v_Y\,dx=A(Y)$. So $\int_0^r u_Xv_Y\,dx
\le A(Y)$, giving $A(X\cup Y)\ge A(X)+A(Y)-2A(Y)=A(X)-A(Y)$. $\blacksquare$

## Verification

Independently verified by 20,000 exact-`Fraction` random trials over
multisets of size 1–5 with random rational entries (comparing $A(X\cup Y)$
directly, via sort-and-alternating-sum, against the two bounds): zero
violations. Script: `/tmp/round-13/test_p2pin.py` (function `A`, triangle
sublemma check), built as part of round 13's `greedy-halving-adversary`
work.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`
(Lemma 27, round 13), used to prove Proposition 28 (dominant-fragment
closure of a sub-branch of $(\dagger)$'s $p_2$-cut complement). Also
immediately gives the standard trivial bound $0\le A(Y)\le\mathrm{Total}(Y)$
as a special case-adjacent fact (take $X=\varnothing$ conceptually, or note
it follows directly from the integral formula alone).

## Certification note

**Certified by proof-reviewer, round 13.** Proof independently re-derived
line by line and re-verified with a fresh, independently-written
20,000-trial exact-`Fraction` script (`/tmp/round-13/verify.py`, function
`A`, direct sort-and-alternating-sum comparison against both bounds): zero
violations. Statement is exactly as proved (no strengthening claimed
beyond what the proof establishes). Proof is self-contained, depending only
on already-certified `cross-term-identity-threshold` and
`integral-alternating-sum-formula`.
