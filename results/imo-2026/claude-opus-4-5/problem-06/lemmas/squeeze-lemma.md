# Squeeze Lemma

## Statement

For all n >= 1 in a greedy gcd-linked sequence, a_{n+1} = min{m in V_stable : m > a_n}, where V_stable is the set of integers whose prime set transverses the stable antichain H_stable.

## Proof

By definition, a_{n+1} = min{m in V_n : m > a_n}.

From the Pairwise Intersection Lemma, a_{n+1} in V_stable.

Since H_stable refines H_n (each element of H_n contains some element of H_stable), we have V_stable subset V_n.

Therefore:
- min{m in V_stable : m > a_n} >= min{m in V_n : m > a_n} = a_{n+1}
- a_{n+1} in V_stable and a_{n+1} > a_n, so a_{n+1} >= min{m in V_stable : m > a_n}

Combining: a_{n+1} = min{m in V_stable : m > a_n}. QED

## Status
certified (round 2)
