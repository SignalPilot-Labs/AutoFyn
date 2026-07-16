# Lemma: terms-equal-valid-set

Certification: **CERTIFIED** (round 1, proof-reviewer). All five statements (L1.1)–(L1.5) checked line by line; proofs complete and correct. (L1.5) additionally verified computationally: 0 failures on 17341 non-terms in (385, 20000] for the seed a_1 = 385.

## Setting and notation

Let a_1 < a_2 < a_3 < ... be the greedy sequence of the problem: integers > 1, and for every n ≥ 1, a_{n+1} is the smallest integer > a_n with gcd(a_{n+1}, a_i) > 1 for all i = 1, ..., n. The sequence is infinite (given) and strictly increasing (a_{n+1} > a_n by definition), hence unbounded.

For an integer m > 1 let P(m) denote the (finite, nonempty) set of primes dividing m. Write P_k := P(a_k). A "term" is a value a_k of the sequence. Define:

- **V** := { m ≥ a_1 : gcd(m, a_k) > 1 for all k ≥ 1 } (the *valid set*);
- **H\*** := { X : X a finite nonempty set of primes with X ∩ P_k ≠ ∅ for all k ≥ 1 } (the *hitting sets* of the family of term types);
- **M** := the set of inclusion-minimal elements of H\* (the *minimal types*).

## Statements

**(L1.1) Pairwise sharing.** For all i, j ≥ 1, gcd(a_i, a_j) > 1.

**(L1.2) The sequence is exactly the sorted valid set.** { a_n : n ≥ 1 } = V. Consequently, for m ≥ a_1: m is a term ⟺ m ∈ V ⟺ P(m) ∈ H\*.

**(L1.3) Realization.** H\* = { P(t) : t a term }. Moreover every X ∈ H\* is the type of infinitely many terms, of arbitrarily large size; explicitly, if X = {p_1, ..., p_r}, then every number m = p_1^j · p_2 ⋯ p_r with m ≥ a_1 is a term with P(m) = X.

**(L1.4) Self-blocking structure.**
  (a) H\* is upward closed within finite prime sets: X ∈ H\* and X ⊆ X' (X' a finite prime set) ⟹ X' ∈ H\*.
  (b) Any two members of H\* intersect; in particular M is a pairwise-intersecting antichain.
  (c) Every X ∈ H\* contains a member of M.
  (d) For a finite nonempty prime set X: X ∈ H\* ⟺ X ∩ Z ≠ ∅ for every Z ∈ M ("X is a transversal of M") ⟺ X contains a member of M. Consequently: X ∉ H\* ⟺ there exists Z ∈ M with Z ∩ X = ∅.

**(L1.5) Locality (greedy rejection is witnessed below).** If m > a_1 and m ∉ V, then there is a term t < m with gcd(t, m) = 1.

## Proofs

**(L1.1).** For i < j this is the defining condition on a_j (i is among 1, ..., j−1). For i = j, gcd(a_i, a_i) = a_i > 1. For i > j swap the roles. ∎

**(L1.2).** (⊆) Every term a_n satisfies a_n ≥ a_1 and, by (L1.1), gcd(a_n, a_k) > 1 for all k; so a_n ∈ V.

(⊇) a_1 ∈ V by (L1.1). Let m ∈ V with m > a_1. Since the sequence is strictly increasing and unbounded and a_1 < m, the index n := max{ k : a_k < m } exists. At step n+1 the number m is a candidate: m > a_n, and gcd(m, a_i) > 1 for all i ≤ n because m ∈ V. By minimality of the greedy choice, a_{n+1} ≤ m. By maximality of n, a_{n+1} ≥ m. Hence a_{n+1} = m, so m is a term.

For the consequence: for m ≥ a_1, gcd(m, a_k) > 1 ⟺ P(m) ∩ P_k ≠ ∅; ranging over k, m ∈ V ⟺ P(m) ∈ H\* (P(m) is finite and nonempty since m ≥ a_1 > 1). ∎

**(L1.3).** (⊇) If t is a term then P(t) ∩ P_k ≠ ∅ for all k by (L1.1), so P(t) ∈ H\*.

(⊆) Let X = {p_1, ..., p_r} ∈ H\* and j ≥ 1 with m := p_1^j · p_2 ⋯ p_r ≥ a_1. Then P(m) = X ∈ H\*, so m ∈ V by (L1.2), so m is a term. As j → ∞, m → ∞, giving infinitely many, arbitrarily large, terms of type exactly X. ∎

**(L1.4).** (a) X' ⊇ X ⟹ X' ∩ P_k ⊇ X ∩ P_k ≠ ∅ for all k.

(b) Let X, X' ∈ H\*. By (L1.3), X = P(t) and X' = P(t') for terms t, t'. By (L1.1), gcd(t, t') > 1, so some prime divides both, i.e., X ∩ X' ≠ ∅. M ⊆ H\* is an antichain by definition of minimality.

(c) Let X ∈ H\*. Among the (finitely many) subsets of X that lie in H\*, choose one, Y, of minimum cardinality. Then Y ∈ M: any Y' ⊊ Y with Y' ∈ H\* would be a smaller subset of X in H\*, a contradiction.

(d) First: every Z ∈ M is of the form P_k for some k. Indeed Z ∈ H\*, so by (L1.3) Z is the type of a term.
  - If X ∈ H\*: for Z ∈ M, Z = P_k for some k, and X ∩ P_k ≠ ∅ by definition of H\*. So X is a transversal of M.
  - If X is a transversal of M: every P_k ∈ H\* (by (L1.3), (⊇) direction applied to the term a_k) contains some Z ∈ M by (c); X ∩ Z ≠ ∅ gives X ∩ P_k ≠ ∅. This holds for all k, so X ∈ H\*.
  - If X contains a member of M, then X ∈ H\* by (a). Conversely X ∈ H\* contains a member by (c).
  - Negation of "transversal of M" is exactly "∃ Z ∈ M with Z ∩ X = ∅". ∎

**(L1.5).** Since m ∉ V and a_1 ∈ V, m is not a term and m > a_1, so n := max{ k : a_k < m } exists (the sequence is unbounded and a_1 < m). Then a_n < m < a_{n+1}. At step n+1 the greedy chose a_{n+1} > m although m > a_n; by minimality of a_{n+1}, m fails the compatibility condition: there is i ≤ n with gcd(m, a_i) = 1. The term t := a_i satisfies t ≤ a_n < m. ∎
