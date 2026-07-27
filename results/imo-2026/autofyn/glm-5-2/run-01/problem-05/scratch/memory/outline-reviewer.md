# outline-reviewer per-role rules

ALWAYS: verify the shared load-bearing algebraic identity (SOS / master squeeze) symbolically with sympy before approving any field that depends on it — it is the engine for the whole population, and a sign error there would doom every approach at once (round 2, imo-2026-05).

ALWAYS: numerically sanity-check the chosen mechanism's core claim with a small python script (Kronecker landing for density approaches; perturbation failures for rigidity claims; large-image limit growth for squeeze-at-infinity arguments) — a "conjectural" step that contradicts a concrete instance must be RETHINK, not APPROVE (round 2, imo-2026-05).

NEVER: accept "the squeeze gives an open g=0 set" from a quadratic-neighborhood bound — a squeeze |g(x)|≤(x-y*)²/(2x+2y*) yields a positive bound, not zero; getting exact zero needs a separate argument. Treat "open zero-set + connectedness" as a mis-identified gap, demand the real mechanism (round 2, imo-2026-05 extremal-infimum).

NEVER: accept "g(y_ε)→m as y_ε→0" when m=inf g is a global infimum — the minimizing sequence need not approach 0; this conflates infimum with a boundary limit and is a genuine mis-identification (round 2, imo-2026-05 extremal-infimum).

ALWAYS: confirm forward-iterate density (n≥0) suffices for Kronecker-type arguments, since backward orbits leave R₊ when g>0 — one-sided density holds because nβ→∞ supplies the matching nonnegative lattice index (round 2, imo-2026-05 density-contradiction).

ALWAYS: anchor the ranking of a "lemma-provider" approach (conjectural direct kill, certain certifiable lemma) BELOW the primary full-solution bets but ABOVE approaches with mis-identified gaps — its certain value is the shared lemma, not the kill (round 2, imo-2026-05 master-sos-identity).
