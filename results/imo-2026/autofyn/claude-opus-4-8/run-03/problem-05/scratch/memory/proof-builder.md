# proof-builder role memory

ALWAYS: when a monotonicity/surjectivity GAP is the wall, pivot to ordering the LEVEL SETS of the invariant (F={d=0},G={d=b}) and prove both are OPEN via one raw inequality, then use connectedness of (0,inf) to force one empty — this closes IMO-2026-05-style problems without ever proving f monotone (round 1).
NEVER: rely on "f = sup of increasing envelope" for monotonicity — it needs surjectivity/range-density that functional-equation solutions do not give; f >= increasing sup does NOT make f increasing (round 1).
ALWAYS: verify every completing-the-square / defect identity with sympy before writing it as a proof step (round 1).
ALWAYS: cleanest version of the two-valued-invariant kill — prove BOTH value-sets open (each from a cross-pair inequality whose failure-band open interval is centered around the point, verified interior via a b^2<b(...) center-check). Two nonempty disjoint open sets covering a connected interval is an immediate contradiction; no sequence/boundary-point needed. Used in imo-2026-05 shift-family-sos §5. (round 1)
