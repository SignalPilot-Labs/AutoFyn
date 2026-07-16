# Lemma: dodging-and-witness

Certification: **CERTIFIED** (round 1, proof-reviewer). Statements (L2.1)–(L2.4) checked line by line; proofs complete and correct (the singleton case of (L2.3) is handled explicitly).

## Setting

Notation and prerequisites as in `terms-equal-valid-set.md` (which is used throughout): the greedy sequence a_1 < a_2 < ..., terms, types P_k = P(a_k), the valid set V, the hitting family H\*, the minimal antichain M, and facts (L1.1)–(L1.5).

Fix once and for all a member **A ∈ M of minimum cardinality**, and set

- **g** := ∏_{p ∈ A} p,
- **E₀** := { primes q : q ≤ g }.

Note A ⊆ E₀ (every p ∈ A divides g, so p ≤ g) and E₀ is finite.

## Statements

**(L2.1) Bounded gaps.** Every multiple of g that is ≥ a_1 is a term. Consequently every interval (x, x+g] with x ≥ a_1 contains a term.

**(L2.2) Dodging.** For every finite set B of primes, all > g, there exist infinitely many terms t with P(t) ∩ B = ∅; moreover such a term can be found in an interval (x, x+g] for suitable arbitrarily large x.

**(L2.3) Witness lemma.** For every Y ∈ M and every ρ ∈ Y there exists W ∈ M with W ∩ Y = {ρ}.

**(L2.4) Nonempty small trace.** Every Z ∈ M satisfies Z ∩ A ≠ ∅; in particular Z ∩ E₀ ≠ ∅.

## Proofs

**(L2.1).** Let m = gk ≥ a_1. Then P(m) ⊇ A ∈ H\*, so P(m) ∈ H\* by upward closure (L1.4a), so m ∈ V by (L1.2), so m is a term by (L1.2). Any interval (x, x+g] of g consecutive integers contains a multiple of g; if x ≥ a_1 that multiple is ≥ a_1, hence a term. ∎

**(L2.2).** Let B = {q_1, ..., q_s}, all q_i > g, and let N := q_1 ⋯ q_s. Choose any x ≥ a_1 with x ≡ 0 (mod N). For each i and each j with 1 ≤ j ≤ g: q_i | x + j would force q_i | j (as q_i | x), impossible since 0 < j ≤ g < q_i. So the interval (x, x+g] contains no multiple of any q_i. By (L2.1) it contains a term t, and P(t) ∩ B = ∅. There are infinitely many such x (all multiples of N above a_1), giving infinitely many such terms. ∎

**(L2.3).** By minimality of Y, the proper subset Y ∖ {ρ} is not in H\* (if Y ∖ {ρ} were empty, i.e., Y = {ρ}: then take W := Y itself, W ∩ Y = {ρ}, done; so assume Y ∖ {ρ} ≠ ∅). By (L1.4d) there is F ∈ M — indeed, directly: Y ∖ {ρ} ∉ H\* means Y ∖ {ρ} misses some P_k; set F := P_k, so F ∈ H\* and F ∩ (Y ∖ {ρ}) = ∅. Since Y, F ∈ H\* intersect (L1.4b), F ∩ Y = {ρ}. By (L1.4c) take W ∈ M with W ⊆ F. Then W ∩ Y ⊆ F ∩ Y = {ρ}, and W ∩ Y ≠ ∅ since W, Y ∈ M ⊆ H\* intersect (L1.4b). So W ∩ Y = {ρ}. ∎

**(L2.4).** Z, A ∈ M ⊆ H\* intersect by (L1.4b), so Z ∩ A ≠ ∅, and A ⊆ E₀. ∎
