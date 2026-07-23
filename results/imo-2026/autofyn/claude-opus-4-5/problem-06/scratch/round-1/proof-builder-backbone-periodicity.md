# Build Report: backbone-periodicity

## Status
solved

## Summary

Built a complete, rigorous proof of IMO 2026 P6 using the backbone periodicity approach.

## Key steps proven

1. **Backbone constraint (Lemma 1):** Every term a_n is divisible by some prime in B = primes(a_1), since gcd(a_n, a_1) > 1.

2. **Self-blocking family (Lemmas 3-5):** The minimal backbone types form a self-blocking family H after at most 2^|B| - 1 steps. This uses the antichain bound on subsets of B.

3. **Constraint stabilization (Lemma 6):** After the startup phase, every new backbone type contains an element of H, so constraints are subsumed. The valid set V_N stabilizes.

4. **Periodicity of valid set (Lemma 7):** V_N is L-periodic where L = lcm(B) = product of primes in B.

5. **Residue cycling (Lemmas 9-12):** The greedy picks residues in R (valid residues mod L) in cyclic order. After T steps, the residue returns and the value increases by L.

6. **Full shift-periodicity:** The key insight is that even during startup, the greedy picks residues in R (because every term's backbone type contains an element of H, so its residue satisfies all eventual constraints). Thus a_{n+T} = a_n + L holds for all n >= 1.

## Gaps closed

- **Gap 1 (Minimal transversal characterization):** Rephrased as self-blocking property. Proved that H becomes self-blocking, which suffices.

- **Gap 2 (K bounded):** K <= 2^|B| - 1 since minimal types form an antichain in the power set of B.

- **Gap 3 (Extra primes outside B):** Backbone intersection is sufficient for gcd > 1, so primes outside B don't create new constraint structure.

## Remaining gaps
None.

## Result
Proof written to results/imo-2026-06/approaches/backbone-periodicity.md (Status: solved)
