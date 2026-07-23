ALWAYS: Verify the proposed invariant/monovariant with concrete small-case simulations before claiming it works (because formulas can have edge-case errors, round 1)
ALWAYS: For board operation problems, decompose the operation prime-by-prime and check if each prime's exponent multiset has a gcd-type invariant (because this pattern arose cleanly in imo-2026-01, round 1)
NEVER: Claim count_>1 alone is a strict monovariant for GCD/LCM operations without checking the case where both results are >1 (because when gcd>=2 and quotient>=2, count is unchanged, round 1)
