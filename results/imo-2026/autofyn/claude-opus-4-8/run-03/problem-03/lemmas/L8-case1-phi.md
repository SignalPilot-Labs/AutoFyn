# Lemma L8 — Generalized Case-1 lower bound (φ-telescoping, top part uncut)

**Status:** CERTIFIED (proof-reviewer, round 3). Numerically verified: 0 violations over 40000
random ratio-≥2 sets with top part uncut (n = 1..4). Source: alternating-sum-potential §3 Case 1.

A finite set a_0 < a_1 < … < a_n is **ratio-≥2** if a_j ≥ 2a_{j−1} for all j; then it is
superincreasing (Σ_{i<j} a_i < a_j). Put φ_k := a_k − Σ_{i<k} a_i (φ_0 = a_0).

**Lemma φ-monotone.** a_0 ≤ φ_1 ≤ φ_2 ≤ … ≤ φ_n.
**Proof.** φ_1 = a_1 − a_0 ≥ 2a_0 − a_0 = a_0. For k ≥ 2, a_k ≥ 2a_{k−1} = a_{k−1} + a_{k−1}, so
φ_k = a_k − a_{k−1} − Σ_{i<k−1} a_i ≥ a_{k−1} − Σ_{i<k−1} a_i = φ_{k−1}. ∎

**Lemma L8 (generalized Case 1).** Let B be any refinement of a ratio-≥2 set {a_0,…,a_n} in which
the top part a_n is left uncut (any number of cuts elsewhere). Then S(B) ≥ φ_n ≥ a_0.
**Proof.** All parts of B other than a_n partition Σ_{i<n} a_i, whose total is < a_n; hence a_n
exceeds the sum of all other parts and is the strict global maximum of B. By the peel-max identity
(L5), S(B) = a_n − S(B ∖ {a_n}) = a_n − S(C), where C := B ∖ {a_n}. By the sum bound (L5),
S(C) ≤ Σ C = Σ_{i<n} a_i, so S(B) ≥ a_n − Σ_{i<n} a_i = φ_n ≥ a_0 (last step by φ-monotone). ∎

**Specialisation.** For the dyadic set a_i = 2^i, a_0 = 1 and φ_n = 2^n − (2^n − 1) = 1, so the
bound S(B) ≥ 1 is exactly tight — this is the problem's lower-bound Case 1, sharp. (Equivalent to
L7's Corollary for the dyadic set; L8 is the version valid for all ratio-≥2 sets.)
