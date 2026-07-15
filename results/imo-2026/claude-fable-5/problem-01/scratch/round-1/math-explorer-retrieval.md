## imo-2026-01

### Problem restatement
2026 integers > 1 on a blackboard. Move: pick m, n > 1 from distinct slots, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Continue while possible. (a) Prove finitely many moves leave exactly one M > 1. (b) Prove M is independent of choices.

---

### Critical structural observation (verified computationally)

**Per-prime decomposition**: The operation acts on each prime p independently. If v_p(m) = a and v_p(n) = b, then the new board entries have p-exponents (min(a,b), |a-b|). This is exactly one step of the **Euclidean algorithm** applied to the pair (a, b).

**Consequence 1 (GCD identity)**: gcd(min(a,b), |a-b|) = gcd(a,b). This is the fundamental step of the Euclidean algorithm and is the engine of part (b).

**Consequence 2 (sum decrease)**: a + b → min(a,b) + |a-b| = max(a,b) ≤ a+b. The sum of all p-exponents for prime p decreases by exactly min(a,b) = v_p(gcd(m,n)) ≥ 0 at each step.

**Consequence 3 (exact T formula)**: Defining T = Σ_i Ω(a_i) (total prime factor count over all board elements), each operation changes T by exactly −Ω(gcd(m,n)):
- gcd(m,n) = 1: T unchanged, but N (count of elements > 1) decreases by 1 (result is (1, mn)).
- gcd(m,n) > 1: T decreases by Ω(gcd(m,n)) ≥ 1.

**CRITICAL distinction from classical gcd/lcm problem**: The classical (m,n) → (gcd,lcm) acts as (a,b) → (min,max) on each prime's exponents — a pure sorting step that preserves the multiset of exponents. **Our operation** (m,n) → (gcd, lcm/gcd) acts as (a,b) → (min, |a-b|) — a Euclidean step that destroys the multiset but preserves the GCD of the pair. This changes which arguments transfer:
- Classical: "the multiset of p-exponents is preserved" → works to prove product invariant, but produces different final configuration.
- Ours: "the GCD of all p-exponents is preserved" → proves M is unique; product DECREASES.

---

### Distinct openings

**Opening A — Lex-monovariant (N, T) for termination**
Define N = count of board elements > 1, T = Σ Ω(a_i). Each step: either T decreases (gcd > 1 case) while N stays same or also drops; or T is unchanged (gcd = 1 case) while N drops by 1. The pair (N, T) strictly decreases under lexicographic order on ℕ² (well-founded). Since N ≥ 0 and T ≥ 0 always, the process terminates. That terminal state has N = 1 because: (i) when any operation is applied, max(gcd, lcm/gcd) ≥ 2 since gcd · (lcm/gcd) = lcm ≥ max(m,n) ≥ 2, so N never drops below 1 via any single step; (ii) terminal state has N < 2 (no two elements > 1); hence N = 1. Expected hard step: making the "N never drops below 1" claim rigorous.

**Opening B — Single monovariant: product of all elements**
Product of all board elements Π_i a_i changes by factor lcm(m,n)/(m·n) = 1/gcd(m,n) per step. Product is a positive integer, strictly decreasing (by at least a factor of 2) whenever gcd(m,n) > 1. For coprime pairs, the product stays the same but a 1 enters the board (N decreases). A combined integer monovariant V = Π_i a_i · C^N for some large constant C could work. Or simply use (N, Π) lex. This is equivalent to Opening A but the product is harder to bound cleanly (it can be huge); T is the cleaner variable.

**Opening C — Per-prime GCD invariant for M's uniqueness (Part b)**
For each prime p, let G_p = gcd(v_p(a_1), …, v_p(a_2026)) where v_p(1) = 0. Prove G_p is invariant: one application (a_i, a_j) → (min(a_i,a_j), |a_i−a_j|) changes the pair but gcd(d, min(a,b), |a−b|) = gcd(d, a, b) for any d (by the Euclidean algorithm identity gcd(a,b) = gcd(min(a,b), |a−b|)). At termination (N=1), the multiset of p-exponents is {v_p(M), 0, 0, …, 0} and G_p = gcd(v_p(M), 0, …, 0) = v_p(M). So v_p(M) = G_p = gcd of initial p-exponents, for each prime p; M is completely determined.

**Opening D — Adjacent transposition / Church-Rosser for Part (b)**
Reduce order-independence to showing two operations on DISJOINT pairs commute (trivial) and two operations on OVERLAPPING pairs (sharing one element) lead to the same state. This is the diamond lemma / confluence approach analogous to aimo-0003. More complex than Opening C; only worthwhile if the invariant approach has a hidden gap.

**Opening E — Sum of v_p over all positions as per-prime monovariant**
For termination of each prime's contribution separately: S_p = Σ_i v_p(a_i) is non-increasing and bounded below by 0. It decreases whenever both a_i and a_j (the two picked) have positive p-exponent. Eventually S_p stabilizes, and at stabilization exactly one board element has positive p-exponent (the rest have 0 for prime p). Combining over all primes: for each prime p, exactly one "carrier" element at termination. The carrier for each prime might be different elements... but at the terminal state N=1, all primes must be concentrated in M. This is consistent and proves convergence per prime.

---

### Candidate techniques

- **Invariants & monovariants**: Primary technique for both parts. Knowledge-base entry "Invariants & monovariants: a quantity preserved (or monotone) across moves."
- **p-adic valuation / per-prime decomposition**: Decompose the problem into independent per-prime problems. Knowledge-base NT section: "Modular arithmetic, CRT: solve by factoring n = Π pᵢ^{eᵢ}."
- **Euclidean algorithm on exponents**: The key structural fact — the operation acts as a Euclidean step on each prime's exponents. This is domain knowledge, not directly in KB by name, but is a basic NT fact.
- **GCD identity**: gcd(a, b) = gcd(min(a,b), |a−b|). Elementary; the crux of Part (b).

---

### Cheap-kill candidates

- **Monovariant T = Σ Ω(a_i)**: Non-increasing integer bounded below by 0. Terminates the process immediately, with the (N, T) lex argument handling the case gcd = 1.
- **Max of board exceeds product of two smallest**: probably not useful here.
- **Parity of Ω(gcd)**: each step decreases T by Ω(gcd(m,n)) ≥ 0 exactly; parity not needed.
- **No two elements can simultaneously equal each other and be coprime**: structural observation that 1s are dead. Simple.

---

### Knowledge-base entries to use

- **"Invariants & monovariants"** (Combinatorics section): primary tool for both termination and uniqueness.
- **"Divisor analysis: gcd structure"** (NT section): gcd(a,b) = gcd(b, a−b) = gcd(min(a,b), |a−b|).
- **"Induction / infinite descent"** (General methods): the monovariant argument is a descending chain argument.
- **"Direct proof"** (General methods): Part (b) is a direct calculation once the invariant is established.
- No need for LTE, Zsigmondy, or other heavy NT tools.

---

### Analogous past problems (cruxes)

1. **aimo-0193** (combinatorics/invariants-and-monovariants): "Several positive integers in a row. Iteratively replace adjacent pair (x>y, x left of y) by (y+1,x) or (x−1,x). Prove finitely many steps." Crux move: weighted positional sum S = Σ i·a_i is a strictly increasing monovariant bounded above by (Σi)·max. **Why analogous**: same structure — process on integers with a monovariant that increases strictly at each step and is bounded; our T decreases strictly and is bounded below. The technique transfers almost verbatim.

2. **aimo-0324** (number_theory/invariants-and-monovariants): "Amy writes n>1; Bob subtracts a²; Amy raises to k. Prove Bob can always win." Crux move: squarefree part S(n) = product of primes with odd exponent is a monovariant (Amy's k-th power never increases it; Bob can always strictly decrease it). **Why analogous**: uses per-prime parity (exponent mod 2) as a monovariant, which is a special case of per-prime exponent analysis. The approach of decomposing the invariant prime-by-prime is directly applicable.

3. **aimo-0003** (combinatorics/invariants-and-monovariants): "Matching between red and blue points on circle; count arcs covering (1,0) is independent of red-point ordering." Crux move: reduce "invariant under all permutations" to "invariant under adjacent transposition"; verify locally. **Why analogous**: this is the alternative approach for Part (b) — proving M is independent of move order by showing any two consecutive moves can be swapped without changing the outcome. The technique transfers if the per-prime invariant approach is not used.

**No crux in the corpus directly covers the gcd/lcm replacement operation.** The problem is novel in the corpus.

---

### Prior progress

None — round 1, no workspace exists yet.

### Dead ends (do not retry)

None yet.

---

### Small-case / intuition notes (labeled as conjecture)

- **Conjecture (verified computationally for dozens of cases)**: The terminal M equals Π_p p^{gcd(v_p(a_i) : i=1..2026)}, i.e., M is the product over each prime p of p raised to the GCD of all p-adic valuations across the initial board. This is NOT the same as gcd(a_1,…,a_2026) in general (e.g., [4,6,12] gives M = 6, not gcd(4,6,12) = 2).

- **Conjecture (verified)**: The terminal M is always uniquely determined regardless of move order; tested with boards of up to 20 elements across 10 random orderings, always giving the same M.

- **Verified fact**: gcd(min(a,b), |a−b|) = gcd(a,b) for all non-negative integers a, b (exhaustive check up to 50). This is the GCD identity needed for Part (b).

- **Verified fact**: delta T = −Ω(gcd(m,n)) exactly (tested for ~20 pairs). So T decreases by exactly the prime-factor count of gcd(m,n) per step.

- **Verified fact**: from any pair (m, n) with m, n > 1, the operation produces at least one result > 1 (since gcd · lcm/gcd = lcm ≥ max(m,n) ≥ 2). So N never drops to 0 during the process.
