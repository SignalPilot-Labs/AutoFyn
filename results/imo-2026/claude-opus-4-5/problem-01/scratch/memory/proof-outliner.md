# Proof-Outliner Role Memory

## Round 1 observations

ALWAYS: State the mechanism behind each key lemma, not just the claim -- e.g., "gcd(min(a,b), |a-b|) = gcd(a,b) because gcd(a,b) = gcd(a, b-a) is the subtraction step of Euclid" rather than just "Euclidean identity". (because the dispatch asks for claim + mechanism, round 1)

ALWAYS: For gcd/lcm blackboard problems, check the convention gcd(k,0) = k -- it's essential for terminal-state invariant calculations. (because the explorers flagged this as a key subtlety, round 1)

NEVER: Confuse the coordinatewise gcd of exponent vectors G_p = gcd(v_p(a_i)) with the ordinary gcd(a_1,...,a_n) -- they differ. Example: {2,3} has M=6 but gcd=1. (because the explorers explicitly warned against this, round 1)
