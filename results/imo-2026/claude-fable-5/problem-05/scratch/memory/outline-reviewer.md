# outline-reviewer per-role rules

ALWAYS: re-verify each claimed algebraic identity independently with sympy (simplify(LHS-RHS-claimed_form)==0) instead of trusting "verified by sympy" claims in the outline — the check takes seconds and anchors the verdict in evidence (round 1, imo-2026-05: all identities held, but this is the cheapest fatal-flaw detector for algebra FEs).
ALWAYS: for asymptotic-slack arguments, check the sign/coefficient of the leading term symbolically AND confirm the "bounded" residual terms are actually bounded over the parameter choice (round 1: marching-orbits' S in [0,p) made the residual bounded — legit, but this is where such arguments usually break).
