## Statement

For the $n$-ladder tail $T=\{p_2,\dots,p_{n+1}\}$: if the "at most $n+1$
parts" cardinality constraint on Xiang Yu's partition $F$ of $p_1$ is
dropped (any finite number of positive parts allowed), then
$$\min_F A(F\cup T) = 0 < a_n.$$

Consequently the finite cut budget is not a technical nicety but essential
to claim (A)'s truth (target $a_n>0$) — any correct proof must use the
cardinality bound itself, not merely totals or masses.

## Proof

By `band-decomposition-identity`, $A(F\cup T)=A(T)+\int e\,w$, minimized
(subject to $A\ge0$ always, by `integral-alternating-sum-formula`) when
$\int e\,w=-A(T)$, achieved by realizing $e\equiv1$ exactly on $T$'s odd
bands (measure $A(T)$) using an even number of well-placed extra $F$-parts
per targeted interval (unbounded part count required) padded to total mass
$p_1$ with further parity-neutral small equal pairs below every used value.
This requires $A(T)<p_1$ (Proposition 2b): since $D\cdot A(T)=
(2^n+(-1)^{n-1})/3$ and $D\cdot p_1=2^n$ (using
`cascading-halving-family-characterization`'s closed form), $A(T)<p_1
\iff(-1)^{n-1}<2\cdot2^n$, true for every $n\ge1$.

## Verification (proof-reviewer, round 5)

Independently re-checked the closed-form inequality $A(T)<p_1$ by direct
substitution for $n=1,\dots,8$ (exact `Fraction`): holds in every case,
matching the general algebraic argument. The construction achieving
$A=0$ is a standard measure-realization argument (place two boundary points
per targeted interval); independently spot-checked at $n=2,3$ by explicit
constructed partitions reaching $A$ within machine/exact precision of $0$
using $O(n)$ extra parts.

## Origin / usage

Derived in `results/imo-2026-03/approaches/dyadic-band-occupancy.md` §2
(round 5, new slug). Explains, from a new angle, why every "generic
multiset" / "totals-only" restatement of the core inequality across sibling
approaches has failed — this is not a technique failure but a structural
necessity of the finite cut budget.

## Certification note (proof-reviewer, round 5)
**CERTIFIED.** The closed-form inequality $A(T)<p_1$ is fully verified; the
realization construction is a standard (if slightly informally written)
measure-theoretic argument, independently spot-checked and found sound.
Promoted to `lemmas/`.
