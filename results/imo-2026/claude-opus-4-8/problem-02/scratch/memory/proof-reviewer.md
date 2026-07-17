# proof-reviewer role memory

ALWAYS: for geometry problems with unsigned-angle hypotheses, build a from-scratch
PHYSICAL config to test the theorem — magnitude-only angle solvers land on spurious
reflected branches where the target FAILS, so a "numerically verified" claim can be true
only on the physical branch. Use the containment constraints (e.g. "K inside angle LBA")
to select it. (imo-2026-02 round 1: a naive fsolve on the three angle equalities gave
OM≠ON on below-BC branches; only the trig parametrization on 0<γ<C−θ gave OM=ON.)

NEVER: certify a lemma whose sign/orientation is fixed by "what the numeric solver
returns" — the mod-π reality of an angle condition is provable, but the product-vs-quotient
handedness is load-bearing and must be derived from the hypotheses, not numerics
(imo-2026-02 round 1, complex approach L2 rejected).

ALWAYS: for a CAS pseudo-division / ideal-membership "certificate", REBUILD the polynomials
(P,Q,TN here) from the geometric definitions yourself and re-run pdiv + Groebner-reduce the
final remainder to 0 — don't trust the builder's scripts. An explicit certificate identity
lc(P)lc(Q)TN=fP+gQ mod Pythagorean is a valid proof (not "numeric only") once you reproduce
it exactly; it also dissolves branch-selection worries because it's a literal identity valid
on all branches (imo-2026-02 round 2, trig-lawofsines APPROVED).
ALWAYS: verify a "reduced to identity (T)" claim as an EXACT relation for arbitrary points
(here OM²−ON²=(T-diff)/(4D)), not just that both vanish on the solution — proves genuine
equivalence, and sign conventions in a stated circumcentre formula become immaterial
(imo-2026-02 round 2).
