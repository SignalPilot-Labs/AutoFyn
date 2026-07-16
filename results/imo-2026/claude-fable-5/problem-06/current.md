# imo-2026-06 — tracking file (proof-reviewer owned)

## Status
solved

Solved in round 1 by approach `crt-window-small-prime-lockin` (verdict APPROVE). The full proof below was verified step by step by the proof-reviewer, with the load-bearing descent (Step 6) re-derived independently and the key claims checked computationally (Exclusion Principle: 0 failures on 17341 non-terms; exact periodicity from n = 1 confirmed on 9 seeds including the edge seed a_1 = 385 with T = 5088, L = 43890).

**Round-2 independent re-verification (fresh reviewer, adversarial pass): APPROVE confirmed.** Every step re-audited from scratch; the descent in Step 6 re-derived independently (both cases exhaustive; the case-(b) boost m = s_i^j·c_i strictly bounded by g·a_1 ≤ ρ, contradicting QW's ρ < m; case-(a) termination by strict decrease of c_i). Fresh code (independent of round-1 scripts, sieve-based simulator): Exclusion Principle 0 failures on all non-terms in (385, 30000); minimal members for a_1 = 385 recomputed on a 15278-term prefix ({2,7}, {2,3,5}, {2,3,11}, {2,11,19}, {3,7,11}, {3,7,19}, {5,7,11}), E = {2,3,5,7,11,19} with every prime < a_1·g = 5390; exact periodicity a_{n+T} = a_n + L from n = 1 re-confirmed on 9 seeds (6, 10, 15, 21, 22, 35, 45, 77, 385), with the proof's own definitions L = ∏E and T = |V ∩ [a_1, a_1+L)|. No gap found.

## Approaches tried
- **crt-window-small-prime-lockin** — **worked (solved)**. Reduction to the valid set V, then the Exclusion Principle (static form of greedy minimality) + Quantitative Witness Lemma + multiplicative descent prove every essential prime is < a_1·g, so the core E = ∪M is finite and L = ∏E gives exact periodicity from n = 1. The originally planned CRT dodging windows turned out to be unnecessary.
- **valid-set-sunflower-core** — partial (correct foundation, sunflower kill of the bounded-size case, and the König transversal-tree Theorem K, all verified; its GAP 1 "M finite" was closed globally by the rival's descent, not within this route).
- **self-blocking-clutter-induction** — dead end as scoped, but produced a **certified no-go theorem**: the pure clutter statement "identically self-blocking ⟹ finite" is FALSE (ladder counterexample, verified), so finiteness of M genuinely requires the number-theoretic realization — which the winning proof uses (the size bound rad(t) ≤ t < m in the witness).

## Current best
Complete proof (below).

## Full proof

**Problem.** Let a_1, a_2, ... be an infinite sequence of integers greater than 1 such that for every positive integer n, a_{n+1} is the smallest integer greater than a_n with gcd(a_{n+1}, a_i) > 1 for every i = 1, ..., n. Prove that there exist positive integers T and L with a_{n+T} = a_n + L for every positive integer n.

**Notation and standing facts.** For an integer m > 1 let P(m) denote the set of primes dividing m; by the Fundamental Theorem of Arithmetic, P(m) is a finite nonempty set and ∏_{p ∈ P(m)} p divides m, so ∏_{p∈P(m)} p ≤ m. A "term" is a value a_n of the sequence. The sequence is strictly increasing (a_{n+1} > a_n by hypothesis), hence injective and unbounded; in particular, for every real x the set of terms less than x is finite, and every term is ≥ a_1 > 1. (For completeness, the greedy step is always well-defined: 2a_n > a_n and gcd(2a_n, a_i) ≥ gcd(a_n, a_i) > 1 for i < n, and gcd(2a_n, a_n) = a_n > 1, so a candidate exists at every step and a smallest one exists by the well-ordering principle.)

### Step 1 (Pairwise sharing)

**Claim.** gcd(a_i, a_j) > 1 for all i, j ≥ 1.

*Proof.* For i < j this is the defining condition on a_j (i ranges over 1, ..., j−1). For i = j, gcd(a_i, a_i) = a_i > 1. Equivalently, P(a_i) ∩ P(a_j) ≠ ∅ for all i, j. ∎

### Step 2 (The sequence is exactly the sorted valid set)

Define V := {m ≥ a_1 : gcd(m, a_k) > 1 for every k ≥ 1}.

**Claim.** {a_n : n ≥ 1} = V.

*Proof.* (⊆) Every term is ≥ a_1 and shares a factor with every term by Step 1.

(⊇) Let m ∈ V. If m = a_1 we are done, so let m > a_1. The set of terms < m is nonempty (it contains a_1) and finite; since the sequence is strictly increasing, this set is {a_1, ..., a_n} where n is the largest index with a_n < m. At step n+1, m is a candidate: m > a_n and gcd(m, a_i) > 1 for all i ≤ n (since m ∈ V). By the greedy minimality of a_{n+1}, a_{n+1} ≤ m. On the other hand a_{n+1} is a term greater than a_n, and every term < m is at most a_n; hence a_{n+1} ≥ m. So a_{n+1} = m and m is a term. ∎

### Step 3 (Types: the family H* and its minimal members M)

Define H* := {X : X is a finite nonempty set of primes with X ∩ P(a_k) ≠ ∅ for every k ≥ 1}.

**Claim.** H* = {P(t) : t a term}; moreover every X ∈ H* is the type P(t) of infinitely many terms t.

*Proof.* (⊇) For any term t, P(t) is finite, nonempty, and meets every P(a_k) by Step 1.

(⊆) Let X = {p_1, ..., p_r} ∈ H* and for j ≥ 1 put m_j := p_1^j · p_2 ⋯ p_r. Then P(m_j) = X. For every k there is a prime p ∈ X ∩ P(a_k); then p | gcd(m_j, a_k), so gcd(m_j, a_k) > 1. Since m_j → ∞ as j → ∞, we have m_j ≥ a_1 for all large j, and then m_j ∈ V, hence m_j is a term by Step 2. This gives infinitely many terms of type exactly X. ∎

**Corollary 3.1 (intersecting).** Any two members of H* intersect. *Proof.* Let X, X' ∈ H*. By the Claim, X = P(t) for some term t = a_k; by definition of H*, X' ∩ P(a_k) ≠ ∅. ∎

Let M := {Y ∈ H* : no proper subset of Y lies in H*} (the inclusion-minimal members).

**Corollary 3.2 (descent to a minimal member).** Every X ∈ H* contains some U ∈ M. *Proof.* Among the (finitely many) subsets of X that lie in H*, choose U of minimum cardinality (X itself qualifies). If a proper subset U' ⊊ U were in H*, then U' ⊆ X would lie in H* with smaller cardinality — contradiction. So U ∈ M. ∎

In particular M ≠ ∅, since P(a_1) ∈ H* (Step 1). **Fix A ∈ M** and set g := ∏_{p ∈ A} p. Every p ∈ A divides g, so every element of A is ≤ g. By Corollary 3.1, **every Y ∈ M meets A** (both lie in H*).

### Step 4 (Exclusion Principle — the static form of greedy minimality)

**Lemma EP.** If m > a_1 is an integer that is not a term, then there exists a term t < m with gcd(t, m) = 1.

*Proof.* Suppose instead that gcd(t, m) > 1 for every term t < m. The set of terms < m is nonempty (a_1 < m) and finite; as in Step 2 it equals {a_1, ..., a_n} with n the largest index satisfying a_n < m. Then m is a candidate at step n+1: m > a_n and gcd(m, a_i) > 1 for i = 1, ..., n. By greedy minimality a_{n+1} ≤ m; and a_{n+1} is a term exceeding a_n, so a_{n+1} ≥ m by maximality of n. Hence a_{n+1} = m, i.e., m is a term — contradiction. ∎

### Step 5 (Quantitative Witness Lemma)

**Lemma QW.** Let Y ∈ M with |Y| ≥ 2, let ρ ∈ Y, and put X := Y ∖ {ρ} (a nonempty proper subset of Y). Let m be **any** integer with m ≥ a_1 and P(m) = X. Then there exists U ∈ M with

  ρ ∈ U,  U ∩ Y = {ρ},  and  ∏_{p ∈ U} p ≤ t < m for some term t;

in particular ρ < m and ∏_{p∈U} p < m.

*Proof.* Since Y ∈ M, its proper nonempty subset X is not in H*. Since P(a_1) ∈ H* and P(m) = X ∉ H*, we have m ≠ a_1, so m > a_1. Also m is not a term: terms have types in H* (Step 3), but P(m) = X ∉ H*.

By Lemma EP there is a term t < m with gcd(t, m) = 1, i.e., P(t) ∩ X = ∅. Now P(t) ∈ H* (Step 3), so P(t) ∩ Y ≠ ∅ by Corollary 3.1 (Y ∈ H*). But P(t) ∩ Y ⊆ Y ∖ X = {ρ}, hence P(t) ∩ Y = {ρ}; in particular ρ ∈ P(t).

By Corollary 3.2 choose U ∈ M with U ⊆ P(t). By Corollary 3.1, U ∩ Y ≠ ∅; and U ∩ Y ⊆ P(t) ∩ Y = {ρ}, so U ∩ Y = {ρ} and ρ ∈ U. Finally ∏_{p∈U} p ≤ ∏_{p∈P(t)} p ≤ t < m (the product of the distinct primes of t divides t). Since ρ ∈ U, also ρ ≤ ∏_{p∈U} p < m. ∎

### Step 6 (Essential prime bound: every prime in ∪M is < a_1·g)

**Theorem.** No member of M contains a prime ρ ≥ a_1·g. Hence ∪M ⊆ {primes < a_1·g}.

*Proof.* Suppose, for contradiction, that ρ ≥ a_1·g is a prime lying in some Y_1 ∈ M. Since a_1 ≥ 2 we have ρ ≥ 2g > g, so ρ exceeds every element of A (all ≤ g, Step 3); in particular **ρ ∉ A**.

First note: **every Z ∈ M containing ρ has |Z| ≥ 2.** Indeed Z ∩ A ≠ ∅ (Step 3), and ρ ∉ A, so Z contains an element of A distinct from ρ.

We construct recursively a sequence Y_1, Y_2, ... of members of M, each containing ρ. Write X_i := Y_i ∖ {ρ} (nonempty, by the note) and c_i := ∏_{p ∈ X_i} p, an integer ≥ 2. Note that P(c_i) = X_i and, more generally, P(s^j · c_i) = X_i for every s ∈ X_i and j ≥ 0. Also pick s_i ∈ Y_i ∩ A; then s_i ≠ ρ (as ρ ∉ A), so s_i ∈ X_i, and s_i ≤ g.

Given Y_i, exactly one of the following two cases holds.

**Case (a): c_i ≥ a_1.** Apply Lemma QW to (Y_i, ρ) with m := c_i (indeed m ≥ a_1 and P(m) = X_i). We obtain Y_{i+1} := U ∈ M with ρ ∈ Y_{i+1} and

  ρ · c_{i+1} = ∏_{p ∈ Y_{i+1}} p < c_i,

using that Y_{i+1} is the disjoint union {ρ} ∪ X_{i+1}. Hence c_{i+1} < c_i / ρ ≤ c_i / 2 < c_i. The recursion continues from Y_{i+1}.

**Case (b): c_i < a_1.** Let j ≥ 1 be minimal with s_i^j · c_i ≥ a_1 (it exists since s_i ≥ 2 and s_i^j c_i → ∞; and j ≥ 1 because c_i < a_1). Put m := s_i^j · c_i. Then P(m) = X_i, m ≥ a_1, and by minimality of j, s_i^{j−1} c_i < a_1, so

  m = s_i · (s_i^{j−1} c_i) < s_i · a_1 ≤ g · a_1 ≤ ρ.

Apply Lemma QW to (Y_i, ρ) with this m: it yields ρ < m ≤ ρ — a contradiction. So if the recursion ever reaches a Y_i with c_i < a_1, we have our contradiction and are done.

It remains to rule out the recursion staying in Case (a) forever. In Case (a) the integers c_i satisfy c_{i+1} < c_i, so an infinite run of Case (a) would produce an infinite strictly decreasing sequence of positive integers, impossible by the well-ordering principle. Hence after finitely many steps some c_i < a_1, and Case (b) delivers the contradiction.

In all cases we have contradicted the existence of ρ ≥ a_1 g in a member of M. ∎

*(Remark: the strict lock-in ∪M ⊆ {p ≤ g} is FALSE in general — for a_1 = 385 = 5·7·11 one finds A = {2,7}, g = 14, yet {2, 11, 19} ∈ M contains 19 > g — so the weakened bound ρ < a_1·g is what is true, and it suffices.)*

### Step 7 (The finite core E)

Set E := ∪M. By Step 6, E ⊆ {primes < a_1·g}, a finite set; and E ⊇ A ≠ ∅. Every member of M is a nonempty subset of E, so M is finite (|M| ≤ 2^{|E|}), though only the finiteness of E is used below.

**Claim 7.1.** Any two terms t, t' (not necessarily distinct) share a prime of E: P(t) ∩ P(t') ∩ E ≠ ∅.

*Proof.* P(t) ∈ H* (Step 3), so by Corollary 3.2 there is U ∈ M with U ⊆ P(t). Now P(t') ∈ H* and U ∈ H*, so P(t') ∩ U ≠ ∅ by Corollary 3.1. Any p ∈ P(t') ∩ U satisfies p ∈ P(t) (as U ⊆ P(t)), p ∈ P(t'), and p ∈ E (as U ⊆ ∪M = E). ∎

### Step 8 (Finale: periodicity from n = 1)

Set **L := ∏_{p ∈ E} p**, a positive integer (indeed L ≥ 2 since E ≠ ∅).

**Claim 8.1.** For every integer m ≥ a_1: m ∈ V ⟺ m + L ∈ V.

*Proof.* (⇒) Let m ∈ V; by Step 2, m is a term. Fix k ≥ 1. By Claim 7.1 the terms m and a_k share a prime p ∈ E. Then p | L, and p | m, so p | m + L; hence gcd(m + L, a_k) ≥ p > 1. As k was arbitrary and m + L > m ≥ a_1, we get m + L ∈ V.

(⇐) Let m + L ∈ V; by Step 2, m + L is a term. Fix k ≥ 1. By Claim 7.1, m + L and a_k share a prime p ∈ E. Then p | L and p | m + L, so p | m; hence gcd(m, a_k) ≥ p > 1. As k was arbitrary and m ≥ a_1, we get m ∈ V. ∎

**Conclusion.** By Step 2, V is exactly the set of terms; write V = {v_1 < v_2 < v_3 < ...}, so a_n = v_n for all n ≥ 1 (the sequence is strictly increasing and enumerates V, so its n-th term is the n-th smallest element of V). Define

  **T := |V ∩ [a_1, a_1 + L)|.**

T is finite (a set of integers in an interval of length L) and T ≥ 1 (a_1 ∈ V). So T is a positive integer.

Consider the map φ(x) = x + L on V. By Claim 8.1 (⇒), φ maps V into V, and clearly into [a_1 + L, ∞). Conversely, if v ∈ V with v ≥ a_1 + L, then m := v − L ≥ a_1 and m + L = v ∈ V, so by Claim 8.1 (⇐), m ∈ V and φ(m) = v. Hence **φ is a bijection from V onto V ∩ [a_1 + L, ∞)**, and it is strictly increasing.

Since min V = v_1 = a_1, the elements of V smaller than a_1 + L are exactly v_1, ..., v_T (they are T in number by the definition of T, and they are the T smallest elements of V), so

  V ∩ [a_1 + L, ∞) = {v_{T+1} < v_{T+2} < v_{T+3} < ...}.

A strictly increasing bijection between two sets of integers enumerated in increasing order matches n-th smallest to n-th smallest: by induction on n, φ(v_1) = min image = v_{T+1} (φ preserves order and v_1 = min V); and if φ(v_i) = v_{T+i} for i ≤ n, then φ(v_{n+1}) is the least element of the image exceeding v_{T+n}, which is v_{T+n+1}. Hence

  v_n + L = φ(v_n) = v_{n+T} for every n ≥ 1,

that is, **a_{n+T} = a_n + L for every positive integer n**, with T and L positive integers. ∎

### Tools used (named)

- Fundamental Theorem of Arithmetic (prime factorization; the product of the distinct prime divisors of t divides t, hence is ≤ t).
- Well-ordering principle / infinite descent [knowledge_base.md: extremal principle, infinite descent] — existence of the greedy minimum, choice of minimal members (Cor. 3.2), termination of the descent in Step 6.
- Elementary gcd/divisibility facts.

### Reviewer verification notes (round 1)

- Every step re-derived independently; the descent in Step 6 checked case by case (both cases exhaustive by trichotomy; singleton members handled by the |Z| ≥ 2 note; the degenerate input m = a_1 excluded inside QW).
- Computational checks: exact periodicity a_{n+T} = a_n + L from n = 1 verified for seeds 6, 15, 20, 21, 35, 45, 77, 105, 385 (for 385: T = 5088, L = 43890 = 2·3·5·7·11·19, over 16185 terms). Exclusion Principle: 0 failures on all 17341 non-terms in (385, 20000]. Minimality of {2,11,19} and A = {2,7} for a_1 = 385 confirmed on a 5394-type prefix.
- Consistency with the certified no-go lemma (`lemmas/no-go-infinite-self-blocking-clutter.md`): the proof's essential number-theoretic input beyond the clutter axioms is the size bound ∏_{p∈P(t)} p ≤ t < m in Lemma QW, exactly the kind of input the no-go shows is necessary.
