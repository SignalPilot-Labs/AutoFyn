# proof-reviewer — per-role rules

ALWAYS: verify trig identities with sympy via `expand(expr.rewrite(exp))` then `simplify`; plain `simplify(expand_trig(...))` can return False on true identities (certificate (10) and Id-bc failed that way but are true, round 1)
ALWAYS: back a symbolic-check failure with a high-precision numeric probe (mpmath, dps=30) before declaring an identity false — distinguishes CAS weakness from a real error (round 1)
ALWAYS: for geometry claims, build the configuration from scratch yourself (root-find on the decoupled hypothesis conditions, then re-verify ALL hypotheses including interiority numerically) rather than trusting builder scripts — this validates the hypothesis→constraint encoding, not just the algebra (round 1)
ALWAYS: when a proof rests on displayed Fourier/product-to-sum tables, verify every table row individually, not just the final identity — a true identity with a wrong displayed row would still violate the "proof stands on its prose" rule (round 1, all rows happened to be correct)
