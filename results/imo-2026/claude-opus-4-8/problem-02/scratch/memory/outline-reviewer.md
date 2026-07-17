# outline-reviewer role memory — imo-2026-02

ALWAYS: sanity-check any "degree ≤ N" claim on a trig identity by actually running the
Weierstrass substitution in sympy — products of two single-angle sines generate double-angle
terms, so the polynomial degree is higher than the naive "only single angles appear" count
(E3' claimed ≤2, was actually degree 4, round 2).
ALWAYS: when an explorer justifies an inscribed-angle equality with "same arc", verify the
point's position first — if the auxiliary point (A') is BETWEEN the two chord endpoints, the
correct chain is two supplement flips that cancel (opposite arc + opposite rays), NOT "same
arc"; the numeric result can be right while the stated justification is geometrically false
(power-of-point-BC Step B, round 2).
NEVER: treat two approaches as diverse just because their techniques differ — check whether
their FINAL gap is the same scalar identity. power-of-point-BC G3 == trig-lawofsines (T);
they share the wall despite synthetic vs trig routing (round 2).
