# Lemma: move-anatomy

**Status: certified (proof-reviewer, round 1).** Proved in full in `approaches/prime-gcd-invariant.md`, Steps 1–2 (Lemmas 1–3 there). Statement checked against the proof — no overclaim; all three parts re-derived independently and numerically spot-checked (25,000 random moves, no violation of part 3).

## Statement

Let m, n be positive integers and write, for each prime p, a = v_p(m), b = v_p(n) (p-adic valuations from unique factorization).

1. **(Valuation formulas.)** v_p(gcd(m,n)) = min(a,b) and v_p(lcm(m,n)) = max(a,b) for every prime p; gcd(m,n) divides lcm(m,n), and v_p(lcm(m,n)/gcd(m,n)) = max(a,b) − min(a,b) = |a − b|. Consequently the blackboard move (m, n) → (gcd(m,n), lcm(m,n)/gcd(m,n)) acts, for every prime p simultaneously, as the subtractive-Euclid step (a, b) → (min(a,b), |a − b|) on the exponent pair, and both outputs are positive integers.
2. **(Second output = 1 criterion.)** lcm(m,n)/gcd(m,n) = 1 if and only if m = n.
3. **(No two 1s.)** If m > 1 and n > 1, then at most one of the two outputs gcd(m,n), lcm(m,n)/gcd(m,n) equals 1. Precisely, in the disjoint exhaustive cases:
   - m = n: outputs (m, 1), exactly one output is 1;
   - gcd(m,n) = 1 (which forces m ≠ n): outputs (1, mn) with mn ≥ 4, exactly one output is 1;
   - gcd(m,n) > 1 and m ≠ n: both outputs are > 1.

## Where proved

`results/imo-2026-01/approaches/prime-gcd-invariant.md`: Lemma 1 (part 1), Lemma 2 (part 2), Lemma 3 (part 3), together with the valuation facts (V1)–(V4) in the Setup there.
