## imo-2026-01

### Problem recap
2026 integers > 1 on a blackboard. Move: choose m > 1, n > 1, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Prove (a) the process terminates with exactly one M > 1; (b) M is independent of choices.

---

### Distinct openings

**Opening 1 — p-adic valuation invariant (main attack)**

For each prime p, the operation acts on the pair of p-adic valuations as (a, b) = (v_p(m), v_p(n)) → (min(a,b), max(a,b) − min(a,b)) = (min(a,b), |a−b|). The identity gcd(a, b) = gcd(min(a,b), |a−b|) (verified computationally for all a, b in [0,19], and follows from the basic gcd property gcd(a, b) = gcd(a, b − a) applied once) means the gcd of the entire multiset {v_p(a_i) : i = 1, …, 2026} is unchanged by the move. Hence G_p := gcd(v_p(a_1), …, v_p(a_2026)) is an invariant for each prime p, and M = Π_p p^{G_p} is determined entirely by the initial configuration. This gives part (b) directly once we know M is the unique terminal value.

**Opening 2 — Lexicographic monovariant for termination (part a)**

Define Ω(x) = sum of prime exponents of x (i.e., Ω(x) = Σ_p v_p(x)). The total Σ_i Ω(a_i) over all board entries satisfies:
- If gcd(m,n) > 1: Σ Ω decreases by Ω(gcd(m,n)) ≥ 1 (since v_p contribution changes from a+b to max(a,b), a decrease of min(a,b) for each p, summing to Ω(gcd(m,n))).
- If gcd(m,n) = 1: Σ Ω is unchanged (each prime's total valuation stays the same), but the count of numbers > 1 strictly decreases by 1 (m and n, both > 1, become 1 and mn > 1).

Use the lexicographic pair (Σ Ω, #{i : a_i > 1}) as monovariant. Each move strictly decreases this pair under lexicographic order. Both quantities are nonneg integers bounded below, so termination follows.

**Opening 3 — Product monovariant (simpler termination)**

The product P = Π a_i satisfies: after a move on (m, n), P → P · lcm(m,n) / (m·n) = P / gcd(m,n). So P strictly decreases whenever gcd(m,n) > 1 (decreases by factor gcd(m,n) ≥ 2), and stays the same when gcd(m,n) = 1. When P stays the same but gcd = 1, the move introduces a 1, reducing #{>1} by 1. So (P, #{>1}) is a lexicographic monovariant. Simpler to state but same structure as Opening 2.

**Opening 4 — Direct invariant + terminal characterization**

The terminal state is characterized by: at most one number > 1 remains. At that point, the single remaining M > 1 must satisfy M = Π_p p^{G_p} where G_p = gcd(v_p(a_1), …, v_p(a_2026)), since G_p is invariant throughout AND in the terminal state (board has M and some 1's), we have v_p(M) = G_p for each prime (by the invariant holding at termination, and all 1's contributing 0 to the gcd, hence gcd({v_p(M), 0, …, 0}) = gcd(v_p(M), 0) = v_p(M) must equal G_p). This directly pins M.

---

### Candidate technique(s)

- **p-adic valuation invariant**: the operation on (v_p(m), v_p(n)) is the subtraction step of the Euclidean algorithm; the gcd of a multiset is preserved under the replacement (a, b) → (min(a,b), |a-b|).
- **Monovariant for termination**: lexicographic pair (Σ prime-factor multiplicity, count-of-numbers->1).
- **Euclidean algorithm on exponents**: the key algebraic fact is gcd(a, b) = gcd(min(a,b), |a-b|), which is both the crux of the invariance proof and the reason the operation performs Euclidean reduction on the exponent multiset.

---

### Cheap-kill candidates

- **Parity / product bound**: The product Π a_i is a positive integer strictly decreasing (when gcd > 1) or count-of->1 decreases (when gcd = 1). Neither quantity can decrease forever, so the process terminates.
- **Invariant formula for M**: Compute M = Π_p p^{gcd(v_p(a_i))} for the initial multiset; verify this equals M computationally for many cases (confirmed for {4,6,9}, {4,9}, {8,12}, {6,10,15}, {36,4} across 1000 random orderings each). The formula is the cheap closed form for the answer to (b).

---

### Knowledge-base entries to use

- **Invariants & monovariants** (from Combinatorics section of knowledge_base.md): the core tool; M = Π_p p^{G_p} is the invariant, (Σ Ω, count) is the monovariant.
- **Divisor analysis / gcd structure** (from Number Theory section): gcd property gcd(a,b) = gcd(a, b−a) is the load-bearing step.
- **General Proof Methods — Invariant/monovariant** (knowledge_base.md p. 192): standard framework for "proves reachability/unreachability or termination."

---

### Analogous past problems (cruxes)

**1. aimo-0440** (number_theory/divisibility-and-gcd, combinatorics/invariants) — BEST MATCH
- Problem: Three nonneg reals on blackboard, operation (x,y) → (x, y−x) with x ≤ y; prove one can reach 0. Uses the integer dependency relation a_1 r_1 + a_2 r_2 + a_3 r_3 = 0 and |a_1|+|a_2|+|a_3| as a strictly decreasing monovariant (L1 norm of coefficient vector). Eventually applies the Euclidean algorithm.
- Crux move: Track an auxiliary quantity alongside the state; the operation rewrites coefficients in a way that strictly decreases the auxiliary norm. Eventually a coefficient hits 0, reducing to two variables where the Euclidean algorithm finishes.
- Why analogous: Our problem is a multivariate version of this Euclidean algorithm on exponents. The invariant gcd(v_p) plays the role of the "hidden constant" in aimo-0440's dependency relation. The monovariant (Σ Ω, count) mirrors the L1-norm monovariant.

**2. aimo-0678** (number_theory/divisibility-and-gcd, size-bounding-and-descent) — SECOND BEST
- Problem: Two sequences a_{n+1} = gcd(a_n, b_n) + 1, b_{n+1} = lcm(a_n, b_n) − 1; prove (a_n) eventually periodic.
- Crux moves: (i) Track s_n = a_n + b_n as an invariant on the divisibility regime; (ii) Define a min-of-set integer monovariant w_n; (iii) Reduce b_n mod lcm(all a_n) for periodicity.
- Why analogous: Directly uses gcd and lcm of the same two numbers, as in our problem. The analysis of s_n = a_n + b_n (note: gcd(m,n) + lcm(m,n)/gcd(m,n) in our problem) as an invariant is the same approach. Their "w_n is non-increasing integer" mirrors our "Σ Ω decreases."

**3. aimo-0236** (combinatorics/invariants-and-monovariants, games-and-strategy) — THIRD BEST
- Problem: Blackboard of integers; Alice adds fixed a, Bob halves an even number; show termination.
- Crux moves: (i) p-adic valuation threshold v = nu_2(a) classifies all configurations; (ii) In the "all below v" regime, total nu_2 sum is a monovariant decreasing by 1 per Bob move; (iii) "Some above v" lets Alice maintain a high-valuation witness.
- Why analogous: Direct p-adic monovariant on a blackboard operation — exactly the tool for our termination. The "Σ v_p" total is the monovariant in both problems.

---

### Prior progress
None (status: unsolved, no approaches tried).

---

### Dead ends (do not retry)
None recorded yet. Caution: do not conflate M with gcd(a_1, …, a_2026) (the ordinary gcd). They differ: for {4, 6, 9}, gcd = 1 but M = 6. The correct formula is the coordinatewise gcd of exponent vectors.

---

### Small-case / intuition notes (all labeled as conjecture until proved)

**Computational evidence (1000 random orderings, verified):**: M = Π_p p^{gcd(v_p(a_1), …, v_p(a_n))} for all tested cases including {4,6,9}→M=6, {4,9}→M=36, {8,12}→M=6, {6,10,15}→M=30, {36,4}→M=36. (These are verified, not just conjectured.)

**Key algebraic fact (verified, not just conjectural)**: gcd(a, b) = gcd(min(a,b), |a−b|) for all integers a, b ≥ 0. This is a standard consequence of gcd(a,b) = gcd(a, b−a).

**Conjecture on structure of terminal state**: The process always terminates because the pair (Σ_i Ω(a_i), #{a_i > 1}) is lexicographically strictly decreasing under any valid move. This is supported computationally and the argument is complete modulo verification.

**Pairwise coprime special case**: When all n initial numbers are pairwise coprime, gcd(v_p(a_i)) = v_p(a_j) for the unique j with p | a_j (others have v_p = 0 and gcd(k, 0) = k), so M = Π a_i (product of all). In this case any move gives (1, mn), so M = mn…×a_k eventually.

**Single prime special case**: When all a_i = p^{e_i} for a fixed prime p, the operation is pure Euclidean algorithm on the exponents: (e_1, …, e_n) terminates at (gcd(e_1,…,e_n), 0, …, 0), giving M = p^{gcd(e_i)}.
