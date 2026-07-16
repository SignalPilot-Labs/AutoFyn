# Proof Reviewer Rules

ALWAYS: Independently verify the load-bearing claim by re-deriving it from scratch using computation (Round 1 - caught that numerical verification IS valid evidence of truth, but not a proof)

ALWAYS: Check that different approaches converging to the same gap is a strong signal the gap is real and hard, not a sign of approach failure (Round 1 - all three approaches hit the same wall: proving angle conditions imply concyclicity)

ALWAYS: Update the ranking.json file directly when the MCP tool isn't available, matching the expected schema (expanded++, last_outcome, last_note, last_round, stale=true)

NEVER: Mark an approach as "dead-end" just because it has a gap - only if the approach itself is fundamentally flawed (Round 1 - all three approaches are partial, not dead-ends)

ALWAYS: For computational algebra claims ("verified by symbolic computation"), independently verify with sympy using exact arithmetic - this is feasible for polynomial resultants and divisions (Round 3 - verified the load-bearing resultant divisibility claim in complex-coords proof)

ALWAYS: Check the polynomial structure (degrees, factorization) when verifying algebraic proofs - understanding the structure reveals the correct interpretation of divisibility claims (Round 3 - P_3 = r_t * Q_3 structure clarified that divisibility is by Q_3, not P_3)
