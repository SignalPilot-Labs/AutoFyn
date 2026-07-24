## Statement

For any finite multiset $S$ of positive reals and any $\lambda>0$,
$A(\lambda S) = \lambda A(S)$, where $\lambda S := \{\lambda s : s\in S\}$
and $A(\cdot)$ is the functional of `integral-alternating-sum-formula`.

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 9
(round 2) — equivalently `self-similar-potential-certificate.md`'s use of
the same fact (homogeneity of degree 1, immediate from $A(S)=\sum
(-1)^{i+1}L_i$: scaling every $L_i$ by $\lambda$ preserves sorted order and
scales every term). Change of variables $y=x/\lambda$ in the integral
formula gives the same conclusion.

## Certification note (proof-reviewer, round 2)

Trivial and immediate from the definition of $A$ (direct algebraic identity,
no case analysis needed); independently re-derived by hand, both via the
direct sum definition and via the integral-formula substitution. Certified
correct.
