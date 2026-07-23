# proof-builder role memory

ALWAYS: verify every algebraic identity you rely on with sympy before writing it into the proof (round 1: caught nothing wrong but confirmed the SOS factorizations (x-y-c)^2 and the (b-z)^2>=4cz cross-constraint instantly).
ALWAYS: when an outline leaves a "density/not-separated" hand-wave, check if it reduces to "both sets open + interval connected" — that is a clean, citable finish (round 1, imo-2026-05 fixed-point-vs-defect gap closed this way).

ALWAYS: when a "convex/Legendre conjugate" framing is assigned but conjugate-tightness genuinely fails off image(f), keep the support-line reading as motivation and close rigorously with the squared support inequality (off-diagonal lever) + orbit-interleaving growth comparison + openness/connectedness — this is complete and honest (imo-2026-05, round 1).
NEVER: assert "convex function tight against conjugates on both sides ⇒ affine" as a closing step without a named mechanism — for f=x+c the profile f(a²)=a²+c is quadratic not affine, so that outline claim was simply false (imo-2026-05, round 1).
ALWAYS: for IMO-2026-P5 (sqrt QM/GM sandwich FE), the constancy of g=f-id genuinely REQUIRES the inequality lever (∗); (★) f(f(y))=2f(y)-y is only equivalent to g(f(y))=g(y) and does NOT force constancy even with monotonicity+continuity. Don't try to finish a "monotone-continuity" framing on (★) alone (round 1).
ALWAYS: derive the two-sided squeeze (♦) 2√t(√x−√t) ≤ f(x)−f(t) ≤ √(2(x²+t²))−2t for t∈Im(f) by plugging (x,y0) with f(y0)=t into (L²),(R²) and using f(t)=2t−y0; it cleanly gives continuity-at-image-points and the sign law. Full global monotonicity before constancy is hard (image gaps) and unnecessary (round 1).
ALWAYS: finish g∈{0,c} via openness+connectedness — (∗) at (z∈Z,β∈P) gives (β−z)²≥4cz, which makes both Z and P open; connectedness of (0,∞) kills one (round 1).
