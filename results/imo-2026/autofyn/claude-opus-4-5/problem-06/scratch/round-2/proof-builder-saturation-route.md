# Proof Builder Report: saturation-route

## Summary

Created the saturation-route approach for IMO 2026 P6. The approach establishes a framework where:

1. **Saturation concept**: An antichain H is saturated iff every transversal P contains some Q in H. Proved that saturation implies H is frozen (no future changes).

2. **Dichotomy lemma**: Proved that H_stable (the antichain of all prime sets from the sequence) is either finite OR all terms share a common prime. In the "common prime" case, we're in Sub-case 2a (already solved).

3. **Periodicity from finite H**: Once H_stable is finite, L = product of support(H_stable), V_stable is L-periodic, and greedy enumeration gives a_{n+T} = a_n + L.

4. **Key auxiliary results**:
   - All terms a_n lie in V_stable (via pairwise GCD)
   - The sequence is the greedy enumeration of V_stable from n=1
   - V_stable subset of V_n for all n (antichain refinement)

## Status: partial

## Gap

The proof has one remaining gap:

**Stabilization gap**: The dichotomy shows H_stable is finite, but we need to show H_n actually stabilizes to H_stable after finitely many steps. 

The dynamics of H_n involve:
- Additions (new incomparable elements)
- Replacements (element replaced by strict subset)

Both operations are bounded in principle (since H_stable is finite), but the formal proof of termination is missing.

The outline suggested proving saturation via "all essential pairs enter H" but this has a hard sub-gap: proving greedy eventually picks terms with exactly 2 prime factors.

## Approach vs. two-of-k-structure

Both approaches share:
- The V_stable enumeration framework
- The CRT periodicity argument
- Pairwise GCD and backbone constraint lemmas

Saturation-route adds:
- The saturation framework (cleaner conceptual handle on when H freezes)
- Dichotomy argument for finiteness

The stabilization gap is the same fundamental difficulty as proving H_stable is finite without the dichotomy.

## Promotable Lemmas

1. **All Terms in V_stable**: For all n >= 1, a_n in V_stable.
2. **Greedy on V_stable**: The sequence is exactly the greedy enumeration of V_stable.
3. **Saturated Implies Frozen**: If H_n is saturated, then H_m = H_n for all m >= n.

## File Written

`/home/agentuser/repo/results/imo-2026-06/approaches/saturation-route.md`
