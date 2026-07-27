# proof-outliner per-role rules

ALWAYS: compute the combined SOS of both inequalities before assuming a direct kill — for imo-2026-05 the two gap squares satisfy U+L=(x-f(y))^2/2 and U-L=-(g(x)-g(y))(g(x)+g(y)+2x+2y)/2, reducing BOTH inequalities to a single master squeeze |g(x)-g(y)|(g(x)+g(y)+2x+2y)≤(x-f(y))^2 (verified symbolically with sympy, round 2). This is the clean squeeze engine; flag any "one-move kill" as conjectural until a substitution actually forces equality.

NEVER: claim the large-image limit pins small-x values — (x-f(y))^2/(2x+2f(y)) ~ f(y)/2 → ∞ grows, so taking f(y)→∞ does NOT pin g(x); it is a wrong-direction trap (flagged in extremal-infimum, round 2).

NEVER: pursue "g additive/Cauchy" or "f(x)/x constant" — g≡c is constant not additive (recovers only c=0), and f(x)/x=1+c/x is not constant for c>0; both ruled out in round 1 dead ends.

NEVER: use orbit amplification along the master inequality to force constancy — the forward orbit makes the RHS ~n^2 (grows), so the bound is useless; the squeeze only helps near image points (round 2).

ALWAYS: keep the gap region (0,M], M=inf image(f), explicit in every approach — it is the shared hard wall; ensure each approach has a DIFFERENT mechanism to cross it (monotonicity trap / density landing / small-y descent / fixed-point collapse) so the field does not collapse to one wall (round 2).
