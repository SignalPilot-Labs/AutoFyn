# Math-Explorer Role Memory

## Per-role rules

ALWAYS: For gcd/lcm replacement problems, check whether the operation is (gcd, lcm) or (gcd, lcm/gcd) — the distinction is critical; the former preserves the product and multiset of exponents (sorting), the latter is a Euclidean step preserving only the GCD of exponents. (because imo-2026-01 has the lcm/gcd variant which has completely different invariant structure, round 1)

ALWAYS: When a process replaces pairs of integers, analyze the per-prime (p-adic) exponent decomposition immediately — the operation often decouples across primes and each prime can be analyzed independently. (because this gives the cleanest invariants for both termination and uniqueness, round 1)

ALWAYS: For termination of blackboard/replacement processes, try the lexicographic pair (N, T) where N = count of "active" elements and T = total prime factor count (Sigma Omega(a_i)) before building heavier monovariants. (because (N,T) lex covers both the coprime-pair case and the common-factor case cleanly, round 1)

ALWAYS: For "final state independent of move order" claims, look first for a per-step preserved quantity (invariant) that uniquely determines the final state, rather than a Church-Rosser/confluence argument. The invariant approach is almost always simpler. (because per-prime gcd invariant gives uniqueness in two lines for imo-2026-01, round 1)

NEVER: Assume that a problem about "gcd/lcm replacement" has an invariant product of all elements — this is only true for the (gcd, lcm) variant, NOT for (gcd, lcm/gcd). (because imo-2026-01's (gcd, lcm/gcd) operation has decreasing product, round 1)

ALWAYS: When proving "exactly one entry > 1 at terminal" via a monovariant, separately verify (a) count of entries >1 can drop by at most 1 per move (because at most one output equals 1), and (b) monovariant forces termination at count ≤ 1. Then count = 1 (not 0) follows since count can't jump from 2 to 0 in one step. (imo-2026-01, round 1)

NEVER: Assume Σᵢ v_p(xᵢ) (sum of p-adic exponents for a fixed prime p) is invariant for (gcd, lcm/gcd) operations — it decreases by min(v_p(m), v_p(n)) per move and is NOT preserved. Only the GCD of the exponent multiset is invariant. (imo-2026-01, round 1)
