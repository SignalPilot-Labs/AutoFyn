# proof-reviewer role memory

ALWAYS: for ideal-membership / cofactor-identity proofs (T = qG*G + qH*H over a rational
function field), check the cofactor DENOMINATORS (= leading coeffs of the divisors). The
inference "G=H=0 ⟹ T=0" is 0·∞ and FAILS where a denominator vanishes; the proof must show
those denominators are nonzero on the admissible region (or clear denominators to a
polynomial identity). This was the exact gap that made a "solved" headline actually partial
(round 1, imo-2026-02: denom factor f = (1+s²)·AB·AC·sin(∠A+θ), zero at θ=π−∠A, excluded
because θ=∠KBA<∠ABC<π−∠A).

ALWAYS: when reconstructing a coordinate config to independently check OM=ON etc., match the
builder's ray-direction SCALING exactly. Their symbolic direction `u=w·R(−θ)(A)` carries
w=1+s²; using an unscaled numeric `rot(−θ,A)` with the same root t makes a valid config look
like it violates the conditions (round 1 false alarm — my bug, not the proof's).
