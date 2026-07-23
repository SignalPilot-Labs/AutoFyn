# Lemma: pair-collapse

**Statement.** Iterating the (formal) move {x, y} ↦ {gcd(x,y), lcm(x,y)/gcd(x,y)} on a fixed
pair of places (values x, y ≥ 1) terminates in finitely many steps at the fixed pair
{1, E(x,y)}, where E(x,y) = ∏_p p^{gcd(v_p x, v_p y)}; pairs containing 1 are fixed points.

**Proof.** Proved in full as Lemma 4 (§4) of `approaches/newman-confluence.md`: per-prime gcd of
the valuation pair is a step invariant (Euclidean subtraction), termination by strong induction
on the product xy, endpoint identified valuation-by-valuation.

**Certified** by proof-reviewer, round 1. sorry-free; statement exactly as proved.
