# proof-builder role memory

ALWAYS: for IMO geometry "prove OM=ON"-type problems, first reduce the metric goal to a
single scalar coordinate identity (e.g. O_x = midpoint of M,N) by placing coordinates so
the key segment is axis-aligned — collapses OM=ON to one linear condition on O (round 1).

ALWAYS: when a config has a free parameter and coupled angle conditions, check if the
conditions DECOUPLE after clearing a trivial factor: an "equal-angle at vertex V" often
depends only on the DIRECTION of one ray (fixed by the parameter), so the equation depends
on only one unknown radius. Factoring E=t*poly exposed this and made sympy tractable (r1).

ALWAYS: to satisfy "sympy must be an EXACT symbolic zero", prove ideal membership by EXACT
polynomial division: reduce target T modulo the condition polys and exhibit cofactors
T=q1*G+q2*H, then assert expand(q1*G+q2*H-T)==0. This is a real proof (T vanishes on the
whole variety), unlike a numeric sweep (round 1, imo-2026-02).

ALWAYS: fix angle-equality branches by writing E=cross1*dot2-cross2*dot1 = |..|sin(δ1-δ2),
then PROVE each oriented angle lies in (0,π) via half-plane sign tests (cross(edge, point))
and the region/betweenness hypotheses. This converts unsigned-angle equalities to polynomial
equations with a genuine iff, no spurious roots (round 1).

NEVER: rely on numerics as a proof step — use them only to pick the correct branch/sign,
then prove that branch geometrically (round 1).

ALWAYS: when ideal-membership T=qG*G+qH*H uses rational cofactors (sympy sp.div over a
function field), CLEAR denominators to a polynomial identity c*T=QG*G+QH*H (QG,QH true
polynomials) BEFORE claiming G=H=0 => T=0 — else it is a 0*inf gap at c=0. The content c
is a product of the leading coeffs you divided by; prove c!=0 at the config (often c has a
clean geometric meaning like (1+s^2)*AB*AC*sin(angleA+theta)>0) (round 1, imo-2026-02 r2).
