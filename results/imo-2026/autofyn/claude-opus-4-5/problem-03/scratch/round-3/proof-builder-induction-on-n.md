# Proof Builder Report: induction-on-n (Round 3)

## Summary

Attempted to complete the induction-on-n proof using the k*-largest pigeonhole approach from the outliner.

## What was done

1. **Verified the k*-largest pigeonhole approach** computationally on the R2 counterexample [107/700, 93/350, 407/700]:
   - k* = 2 (the largest satisfying index)
   - Ratio p_3/p_2 = 2.19 > 2 confirms no interleaving
   - Sub-problem size bound holds: S_2 = 0.419 < 0.429
   - Algebraic miracle works: S_2*t_1 = 0.139 < 0.143 = t_2

2. **Structured the proof** with scale-invariant claim P(m):
   - Base case m=1: Complete and rigorous (two cases: ratio > 2 vs ratio <= 2)
   - Inductive step Case A (k* < m+1): Complete with halve+recurse

3. **Investigated the sandwich case (k* = m+1)**:
   - Found configurations where halving alone does NOT achieve the target
   - Example: pieces [0.08, 0.17, 0.30, 0.45] for m=3 with only k=4 satisfying
   - Best halving strategy gives A = 0.08 > t_3 = 0.0667 (FAILS)
   - Asymmetric splits CAN achieve A = 0.02 < 0.0667 (numerical search)

## Gap identified

The **sandwich case (k* = m+1)** remains as a genuine gap:

- When only k = m+1 satisfies the pigeonhole condition, there's nothing "above k*" to halve
- The halve+recurse strategy doesn't directly apply
- Asymmetric splitting can achieve the target (verified numerically), but proving this in full generality requires additional machinery
- Attempted recursion via P(m-1) on p_1,...,p_m, but the remaining piece p_{m+1} may interleave with the sub-problem after splitting

## Outcome

**Status: partial**

The proof covers:
1. Lower bound: Complete (geometric marking guarantees c(n))
2. Upper bound Case A (k* < m+1): Complete (halve+recurse works)
3. Upper bound Case B (k* = m+1): Gap (sandwich case)

The claimed answer c(n) = 2^n/(2^{n+1}-1) is strongly supported by numerical evidence for the sandwich case, but a rigorous proof is incomplete.

## Recommendations for next round

1. Consider an alternative approach that avoids the case split on k* (e.g., direct minimax analysis, LP duality)
2. The sandwich case might be provable via a "balancing" lemma showing XY can always create near-equal pairs
3. The exchange-argument approach (variational) might bypass this difficulty if the non-differentiability issues can be resolved
