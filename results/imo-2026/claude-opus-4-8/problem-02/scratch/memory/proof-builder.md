NEVER: use plain Groebner ideal-membership to certify a trig identity holds on a
geometric configuration when the defining relation is a linear function of a
DOUBLE angle (e.g. F(cos2γ,sin2γ)=0). The unit-circle intersection has a spurious
second root (γ vs γ+π) and membership returns a false negative even when the
identity is true on the physical branch. Substitute the explicit branch instead.
(imo-2026-02, round 1)
ALWAYS: set the Bash tool `timeout` PARAMETER (max 600000ms=10min) for long
sympy/Groebner runs; the shell `timeout N` inside the command does not override
the tool's 2-min default. (imo-2026-02, round 1)
ALWAYS: for OM=ON-type circumcentre problems, reduce via pow(X)=|X-O|^2-R^2 and
the circumcentre formula O_x=A_x+(|u|^2 v2-|v|^2 u2)/(2D) to a SINGLE scalar
identity; you only need O.(C-B), gettable from the 2x2 perp-bisector system, not
full O. (imo-2026-02, round 1)
ALWAYS: for "inversion at a vertex A on a circle through A" reformulations, remember the
image line is the POLAR of A (equation 2O.Y=1 with A=origin), so its intercepts encode O
directly — such a reformulation is EXACT but often TAUTOLOGICAL (collapses back to the
target) unless you compute the intercepts from the OTHER points' images (here K*,L*)
independently of O. Check for this collapse before claiming injection. (imo-2026-02, round 2)
ALWAYS: for imo-2026-02, derive closing relations E2'/E3' by computing the cevian
BK (resp CL) TWO ways -- via triangle BMK (gives (c/2)sinγ/sin(θ+γ)) and via
triangle BKC (using the SECOND ray CK at angle θ+γ to CA, from "L inside angle
ACK") -- and equate. This proves E3' rigorously (was only numeric). Uses
θ+γ<C and a=c sinA/sinC. (round 2)
NEVER: expect the SAS-chain final identity (G3) to hold for free β,γ; verified
numerically it is FALSE off the E2'/E3' locus (perturb γ -> LHS -0.288 vs target
-0.200). G3 genuinely needs E2',E3' + transcendental closure = the shared trig
wall. (imo-2026-02, round 2)

ALWAYS: when a doubled-angle (cos2γ,sin2γ) Groebner membership gives a false negative,
retry with the SINGLE-angle Weierstrass t=tan(γ/2) on the UN-doubled relation. The
target identity may vanish on ALL roots (T invariant under γ→γ+π ⟺ t→−1/t), making it a
genuine ideal membership with NO branch selection needed. Certify via exact prem/div:
lc(P)^k lc(Q)^j·TN = f·P+g·Q mod Pythagorean, then check leading coeffs nonzero on the
physical config from the strict angle inequalities. (imo-2026-02 P2, round 2 — closed the gap)
