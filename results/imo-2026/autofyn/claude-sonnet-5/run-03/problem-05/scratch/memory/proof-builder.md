ALWAYS: when a verified algebraic tool is stated "for all x,y>0" (not just for orbit-linked
pairs), check whether plugging in a literal real perturbation (x=y+ε, ε→0) yields continuity
"for free" — this can be far stronger than the outline's proposed limiting/sup-inf mechanism and
can collapse the whole remaining gap (round 1, imo-2026-05, extremal-sup-inf: turned a stuck
sup/inf argument into continuity ⟹ monotonicity ⟹ full global-constancy proof).
NEVER: trust an outline's proposed finishing mechanism (e.g. "pass to the limit along a
minimizing sequence") as the only route — if it only yields a local/one-sided bound, look for a
strictly stronger use of the same already-verified lemma before spending budget patching the
weak mechanism (round 1, imo-2026-05).
ALWAYS: when proving a derived quantity g is constant via monotonicity + an orbit-AP structure
(g(f(y))=g(y), f^n(y)=y+n·g(y)), the "zero value coexists with positive value" edge case needs
its own dedicated argument (downward-closed zero-set + sup + continuity at the boundary) — don't
assume the "both positive" crossing argument automatically covers it (round 1, imo-2026-05).
ALWAYS: verify sufficiency of a proposed answer family against the ORIGINAL un-squared/un-reduced
inequality (not just the collapsed algebraic identity), and check nonnegativity of all quantities
before squaring/unsquaring — a quick sympy check of the SOS identity is a good sanity pass but
the written proof must still state the equivalence argument explicitly.
ALWAYS: check /tmp/memory/proof-builder.md itself mid-task for hints written by parallel builders
in the SAME round working on a sibling approach with shared lemmas — one sibling's "ALWAYS" note
about a stronger finishing mechanism (e.g. continuity-for-free from a cross inequality) can
directly upgrade your own approach from partial to solved with the same base lemmas (round 1,
imo-2026-05, cross-substitution-fixed-point: upgraded via a memory hint from extremal-sup-inf's
round-1 finding without needing to rediscover it independently).
ALWAYS: when you have a two-sided pointwise bound like |g(x)-g(y)| <= (x-y)^2/(4*min(f(x),f(y)))
holding for ALL x,y (not just orbit-linked pairs), try a finite N-point telescoping/triangle-
inequality chain along the segment [min(x,y),max(x,y)] before reaching for orbit machinery or
density arguments — it gives an exact equality (not just a limit) via elementary "bounded by a
null sequence" reasoning, no continuity assumed, and is far simpler than orbit/pigeonhole routes
(round 1, imo-2026-05).
ALWAYS: when a "mixed case" (a derived quantity taking two values 0/c, needing to rule out both
occurring) resists finite/discrete point-comparison tricks, try inf/sup of one value-class near
the other's witness point + a convergent-pair limit into an already-proven pointwise inequality
tool — this closed the exact gap the whole imo-2026-05 population was stuck on (round 1,
monotonicity-order: turned `partial` into `solved` in one extra pass after the discrete crossing
argument only handled one ordering sub-case).
ALWAYS: for orbit-comparison ("telescoping") arguments comparing two arithmetic-progression
orbits X_n=x0+np, Y_m=y0+mq, never match indices n=m (leading order cancels uselessly) — instead
fix one orbit's index growing and choose the OTHER index via nearest-integer rounding
(n(m)=round((Y_m-x0)/p)) to keep the two orbit points at BOUNDED distance while a genuinely
growing coefficient elsewhere in the inequality blows up; this "nearest lattice point" mismatched
pairing is what makes orbit-telescoping non-vacuous (round 1, imo-2026-05,
orbit-telescoping-aimo0710: fixed the diagonal dead end this way, solved the problem).
