## Double-Sandwich-Below and Double-Sandwich-Above chambers (n=3, m=4)

**Source:** `lp-duality-certificate`, round 24, §R24.1.

**Construction (Below).** Split p1 into v1,v2 (v1+v2=p1, one cut);
bisect p4 into p4/2,p4/2 (one cut); p2,p3 untouched. 2 cuts total.
Order p2>v1>p3>v2>p4/2.
Φ_Below(p) = p2 + p3 + p4/2.
Feasible iff p3 + p4/2 < p1 < p2 + p3.

**Construction (Above).** Same cut shape, order v1>p2>v2>p3>p4/2.
Φ_Above(p) = p1 + p4/2.
Feasible iff p1 > p2 + p3.

**Proof method (both).** The two p4/2 fragments (same original piece)
cancel by `odd-run-reduction-lemma` regardless of sort position, leaving
a 4-element multiset drawn from {p2,p3,v1,v2}; each surviving/untouched
piece occupies a single rank so `cross-piece-sign-assignment-identity`'s
monochromaticity hypothesis holds trivially; the exact feasibility
interval for v1 is derived by solving the assumed strict order as a
system of 4 linear inequalities in v1 (shown non-empty iff the stated
two-sided condition holds).

**Proof-reviewer independent re-verification.** Wrote an independent
exact-`Fraction` script (not the builder's own): for 20,000 random
p1>=p2>=p3>=p4>0, whenever the feasibility condition holds, constructed
the midpoint v1 of the derived interval and directly recomputed Φ from
the full 6-element multiset via sort-and-alternate-sum — exact match to
the closed form in every trial, zero mismatches, for both Below and
Above.

**Complementarity note (correctly reported by the builder, not an
overclaim):** Below's region {p3+p4/2 < p1 < p2+p3} and Above's region
{p1 > p2+p3} together cover {p1 > p3+p4/2}, leaving a genuine residual
strip {p1 <= p3+p4/2} uncovered by this pair alone (covered elsewhere in
the round-24 20-member family, not claimed here).

**Certification.** CERTIFIED — both closed forms and both exact
feasibility regions, unconditional, n=3 (m=4) specific construction
(uses p3,p4 explicitly; not yet stated/verified for general n).
