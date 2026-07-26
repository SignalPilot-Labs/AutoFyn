
ALWAYS: For blackboard gcd/lcm move-process problems, write numbers as per-prime exponent vectors first — the move (a,b)→(min,|a−b|) is a Euclidean step and the gcd-of-multiset of exponents is the invariant that pins the terminal value (round 1, imo-2026-01).
NEVER: Prove termination of a coupled multi-prime move-process by "run each prime's Euclidean algorithm independently to (g,0)" — prime coupling blocks this; use a global lex monovariant (Ω, K) instead (round 1, imo-2026-01).
NEVER: Confuse "gcd of the p-exponents across positions" (the invariant, gives g_p) with "min of the p-exponents" (= v_p of the gcd of the numbers) — they differ; e.g. {2,3} has g_2=1 but min=0 (round 1).

ALWAYS: For blackboard gcd/lcm processes, compute per-prime valuation dynamics first (the move on two p-exponents is (α,β)→(min(α,β),|α−β|), the Euclidean step) — the gcd of the whole exponent multiset is invariant, and this invariant pins the terminal value and rules out degenerate termini. (round 1, imo-2026-01)
ALWAYS: For a "prove the process terminates" claim, try a lexicographic (P, C) descent (board product primary, count-of->1 entries secondary) before any per-coordinate Euclidean termination; it sidesteps cross-prime coupling. (round 1, imo-2026-01)
NEVER: rule out an "all-ones" terminus by size (product can drop arbitrarily); rule it out by an invariant (the per-prime gcd-of-exponents d_p must be 0 for all p, forcing all initial numbers 1). (round 1, imo-2026-01)
