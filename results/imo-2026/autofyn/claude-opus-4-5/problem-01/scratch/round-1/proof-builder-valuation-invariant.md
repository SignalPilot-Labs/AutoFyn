# Proof Builder Report: valuation-invariant (IMO 2026-01)

## Status
solved

## Summary

Built a complete, rigorous proof for both parts (a) and (b) of IMO 2026-01 using the p-adic valuation invariant approach.

## Key components proved

1. **Valuation decomposition (Lemma 1):** Showed the operation acts on valuations as (alpha, beta) -> (min(alpha, beta), |alpha - beta|).

2. **Euclidean identity (Lemma 2):** Proved gcd(min(alpha, beta), |alpha - beta|) = gcd(alpha, beta) using the standard Euclidean algorithm step gcd(a, b-a) = gcd(a, b).

3. **Invariance of d_p (Lemma 3):** Established that d_p = gcd of all p-adic valuations is preserved under each move, since replacing two elements with a pair having the same gcd preserves the overall gcd.

4. **Monovariant (Lemma 4):** Proved (T, N) = (total Omega, count > 1) strictly decreases lexicographically. All three cases explicitly verified:
   - gcd = 1: T unchanged, N decreases by 1
   - gcd >= 2, lcm/gcd >= 2: T decreases by Omega(gcd) >= 1
   - gcd >= 2, lcm/gcd = 1 (m = n): T decreases by Omega(m) >= 1

5. **Terminal condition (Lemmas 5-6):** Proved termination occurs when N <= 1, and N = 1 (not 0) because some d_p >= 1.

## Final answer

M = prod_p p^{d_p} where d_p = gcd(v_p(x_1), ..., v_p(x_{2026})) from the initial configuration.

## Gaps closed

None remained from the outline - the outline was complete. Builder expanded all case analysis with full justification.

## Output

Written to: `/home/agentuser/repo/results/imo-2026-01/approaches/valuation-invariant.md`
