# Lemma: finite-core-implies-periodicity

Certification: **CERTIFIED** (round 1, proof-reviewer). Checked line by line; the order-isomorphism argument in (c) correctly yields the claim for ALL n ≥ 1 (not just eventually). Verified computationally on 8 seeds (6, 15, 20, 21, 35, 45, 77, 105, 385): a_{n+T} = a_n + L holds from n = 1 in every case.

## Setting

Notation and prerequisites as in `terms-equal-valid-set.md`: the greedy sequence a_1 < a_2 < ..., the valid set V, the family H\*, the minimal antichain M, and facts (L1.1)–(L1.4).

## Statement

**If M is finite, then there exist positive integers T and L with a_{n+T} = a_n + L for every positive integer n.** (This is the full claim of IMO 2026 Problem 6.)

Explicitly one may take E := ∪_{Z ∈ M} Z, L := ∏_{p ∈ E} p, and T := |V ∩ [a_1, a_1 + L)|.

## Proof

Assume M is finite. Then E := ∪_{Z ∈ M} Z is a finite set of primes, and E ≠ ∅ (M ≠ ∅ since P(a_1) ∈ H\* contains a member by (L1.4c), and members are nonempty). Set L := ∏_{p ∈ E} p, a positive integer.

**(a) Any two terms share a prime of E.** Let t, t' be terms. By (L1.4c), P(t) contains some Z ∈ M. By (L1.3), Z = P(t_Z) for some term t_Z. By (L1.1), gcd(t', t_Z) > 1, so P(t') ∩ Z ≠ ∅. Any prime p ∈ P(t') ∩ Z satisfies p ∈ P(t) (as Z ⊆ P(t)), p ∈ P(t'), and p ∈ E (as Z ⊆ E).

**(b) For every m ≥ a_1: m ∈ V ⟺ m + L ∈ V.**

(⟹) Let m ∈ V; by (L1.2), m is a term. For each k ≥ 1, by (a) applied to the terms m and a_k, there is a prime p ∈ E with p | m and p | a_k. Since p ∈ E, p | L, so p | m + L, hence gcd(m + L, a_k) > 1. As this holds for all k and m + L ≥ a_1, we get m + L ∈ V.

(⟸) Let m + L ∈ V; since m + L ≥ a_1, m + L is a term (L1.2). For each k ≥ 1, by (a) there is a prime p ∈ E dividing both m + L and a_k. Then p | L, so p | (m + L) − L = m, hence gcd(m, a_k) > 1. As this holds for all k and m ≥ a_1, we get m ∈ V.

**(c) Conclusion.** Write V = { v_1 < v_2 < v_3 < ... }; by (L1.2), a_n = v_n for all n ≥ 1. By (b), the map x ↦ x + L is a bijection from V onto V ∩ [a_1 + L, ∞), and it preserves order. Set T := |V ∩ [a_1, a_1 + L)|. This count is finite (a subset of an interval of length L) and positive (a_1 ∈ V by (L1.2)), so T is a positive integer, and V ∩ [a_1 + L, ∞) = { v_{T+1}, v_{T+2}, ... } (exactly T elements of V precede a_1 + L). Since x ↦ x + L is an order isomorphism from { v_1 < v_2 < ... } onto { v_{T+1} < v_{T+2} < ... }, it maps the n-th element to the n-th element: v_n + L = v_{n+T} for all n ≥ 1. That is, a_{n+T} = a_n + L for **all** n ≥ 1, with T, L positive integers. ∎
