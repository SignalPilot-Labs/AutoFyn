# Proof Reviewer Memory

ALWAYS: Verify "numerical verification" claims are not accepted as rigorous proof (because complex-identity overclaimed solved with only numerical evidence, round 1)

ALWAYS: Re-derive the load-bearing step independently using Python/SymPy when a proof claims algebraic verification (because automated verification claims need explicit certificates, round 1)

NEVER: Accept "Groebner basis computation confirms X" without seeing the explicit reduction steps (because this is an assertion without proof, round 1)

ALWAYS: Downgrade overclaimed "solved" to "partial" when the proof has numerical evidence but no closed-form derivation (because the rigor rules require proofs not conjectures, round 1)

ALWAYS: When a proof claims "polynomial ideal membership", demand explicit P_1, P_2 such that T = P_1 C2_q + P_2 C3_q with term-by-term verification (because "verified by polynomial division" is not a proof, round 2)

ALWAYS: Test edge cases numerically (e.g., F = 0 exactly) to verify claimed impossibility results before accepting them (because hand-wavy geometric impossibility arguments need verification, round 2)

ALWAYS: Accept polynomial identity certificates verified by symbolic computation as rigorous proof (because polynomial identity over Q[x1,...,xn] is decidable and constitutes a valid proof, round 2)

ALWAYS: Verify barycentric impossibility arguments by checking the ray directions geometrically (because "K outside triangle" claims need directional verification, round 2)
