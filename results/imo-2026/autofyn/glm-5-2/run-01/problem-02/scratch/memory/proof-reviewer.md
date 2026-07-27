# proof-reviewer rules (learned)

ALWAYS: when checking a "linear in trig variable" claim from an outline-review, verify the degree by direct sympy expansion — outline-reviews can be wrong (conK was claimed linear in (sin γ, cos γ) but is actually degree 2; round 1, imo-2026-02).

ALWAYS: for trig-divisibility gaps (H ≡ 0 mod C, verified only numerically), recommend univariate pseudodivision in one tan-half-angle variable over the rational-function field in the rest — it terminates where unconstrained multivariate Groebner does not (round 1, imo-2026-02).

NEVER: accept numerical verification (~1e-12) as a rigorous proof for a proof_only olympiad problem, even across 40+ random configs — it is a gap, downgrade to partial (round 1, imo-2026-02).

ALWAYS: when verifying an "equal-and-opposite directed angles ⟹ isosceles ⟹ on perpendicular bisector" conclusion, use the coordinate check (place B=(0,0), C=(d,0); lines through B at angle +θ and through C at angle −θ meet at x=d/2) rather than trusting "∠=|∡|" — the interior angle equals |directed angle| only in the right positioning, though the isosceles conclusion is robust either way (round 3, imo-2026-02).

ALWAYS: when a proof uses a B↔C relabeling "symmetry" to derive a signed directed angle for the C-side from the B-side, independently verify the NUMERICAL value of the intermediate angle (e.g. ∡(CB, CA')) — the relabeling reverses triangle orientation (CCW→CW), so the signed angle picks up a negative, and "converting" ∡(CB,·) to ∡(BC,·) does NOT flip sign (same line mod π). Two compensating sign errors can hide in such arguments (round 2, imo-2026-02).
