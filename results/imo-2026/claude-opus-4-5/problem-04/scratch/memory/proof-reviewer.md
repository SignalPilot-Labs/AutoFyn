# Proof-Reviewer Per-Role Memory

## Rules

ALWAYS: Re-derive the load-bearing step independently with python3/sympy before approving (because computational verification catches algebraic errors, round 2)

ALWAYS: Check geometric constraints (like t in (0, alpha)) are satisfied for ALL cases in a casework proof, not just the "main" case (because edge cases often break, round 2)

ALWAYS: For game theory problems, verify the opponent's response to each claimed forcing move (because forgetting the adversary's options is a common gap, round 2)

NEVER: Accept "relabel so X" without verifying the relabeling always exists (because relabeling can fail in edge cases, round 2)
