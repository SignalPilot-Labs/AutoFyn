## imo-2026-01

### Algebraic / Prime-Valuation / Invariant Lens

---

**The per-prime operation (exact description)**

Write v_p(x) for the p-adic valuation of board entry x. If a move picks entries m, n with gcd(m,n) = d, m = da, n = db, gcd(a,b) = 1, the replacements are gcd(m,n) = d and lcm(m,n)/gcd(m,n) = ab.

For a fixed prime p, let alpha = v_p(m), beta = v_p(n). Then:
- v_p(gcd(m,n)) = min(alpha, beta)
- v_p(lcm(m,n)/gcd(m,n)) = v_p(ab) = alpha + beta - 2*min(alpha,beta) = |alpha - beta|

So the operation on the pair (alpha, beta) of p-adic valuations is:
  (alpha, beta) --> (min(alpha, beta), |alpha - beta|)

This is precisely one step of the **subtractive Euclidean algorithm**. This is the core algebraic structure of the problem.

---

**Invariant: gcd of the entire valuation multiset**

For a multiset {a_1, a_2, ..., a_n} of p-adic valuations across all board entries, define G_p = gcd(a_1, ..., a_n).

Key identity (verified numerically for all a, b in [0, 19]):
  gcd(min(a,b), |a-b|) = gcd(a,b)

This is the classical Euclidean identity (subtractive form). Therefore, when the operation (a_i, a_j) --> (min(a_i, a_j), |a_i - a_j|) is applied to any pair from the multiset, the gcd of the full multiset is preserved:
  gcd(min(a_i, a_j), |a_i - a_j|, a_1, ..., rest) = gcd(a_i, a_j, a_1, ..., rest) = G_p.

**G_p is a true invariant** under all moves (for each prime p).

---

**What is NOT preserved / monovariants**

- **Sum** of the multiset {a_1, ..., a_n}: decreases by min(a_i, a_j) >= 0 per move (not preserved; decreases when both valuation entries are nonzero for prime p).
- **Max** of the multiset: non-increasing (weakly monovariant).
- **Number of nonzero entries in the p-multiset**: non-increasing (once an entry reaches 0 it stays 0 for that prime).

---

**Monovariant for termination (part (a))**

Define:
  k = number of board entries that are > 1 (the "active" count).
  T = sum_{active i} Omega(x_i), where Omega(n) = total number of prime factors of n with multiplicity.

(Equivalently, T = sum_p S_p where S_p = sum of v_p values over all active entries.)

After a move on (m, n):
- If gcd(m,n) = 1: result is (1, mn). One entry becomes 1 (inactive). k decreases by 1. T is unchanged (Omega(1) + Omega(mn) = 0 + Omega(m) + Omega(n) = Omega(m) + Omega(n)). So T+k decreases by 1.
- If gcd(m,n) = d > 1 and m != n: result is (d, ab) both > 1. k unchanged. T decreases by Omega(d) >= 1 (since d >= 2). So T+k decreases by >= 1.
- If gcd(m,n) = d > 1 and m = n = d: result is (d, 1). k decreases by 1. T decreases by Omega(d) >= 1. So T+k decreases by >= 2.

**T + k is a strict monovariant** (decreases by at least 1 at each step). Since T >= 0 and k >= 0 and both are non-negative integers, the process terminates in at most T_0 + 2026 steps.

**Verified numerically**: T+k decreases by 1 or more at every step in all tested configurations (see simulation output above).

---

**Why exactly one M > 1 remains (not zero)**

A move on (m, n) with m, n > 1 produces (gcd, lcm/gcd). Both results can be 1 only if gcd = 1 AND lcm/gcd = 1, i.e., mn = 1, impossible since m, n > 1. So each move reduces k by **at most 1**.

Consequence: k decreases from 2026 by at most 1 per step. The process stops when no move is possible, i.e., k <= 1. But k cannot jump from 1 to 0 (that would require a move starting from k=1, which is impossible since a move needs two active entries). So the process always terminates at **k = 1**: exactly one M > 1 remains. This is the entirety of part (a).

Alternative cleaner monovariant for (a): the product P = x_1 * x_2 * ... * x_2026 (all board entries, including 1s). P -> P / gcd(m,n) at each step, so P never increases. P >= 2^{2026} initially and P is a positive integer. But this alone doesn't easily give k=1 terminal; the T+k argument is cleaner.

---

**Precise conjecture for M (part (b))**

**Conjecture (proved by the invariant):**
  v_p(M) = G_p = gcd{ v_p(x_i) : i = 1, ..., 2026 }

and therefore:
  M = product over primes p of p^{gcd(v_p(x_1), ..., v_p(x_2026))}.

**Proof sketch for (b):**

At the terminal state (k=1), the multiset of v_p values is {v_p(M), 0, 0, ..., 0} (one entry M > 1, all others are 1 so have v_p = 0).

The gcd of this terminal multiset is gcd(v_p(M), 0, 0, ..., 0) = v_p(M) (since gcd(n, 0) = n for any n >= 0).

But G_p is invariant throughout the entire process (proved above). Therefore:
  v_p(M) = G_p = gcd{ v_p(x_i) : i = 1, ..., 2026 } (initial values).

So M is **completely determined** by the initial configuration and does not depend on the choices made.

**Numerically verified** for 5-element boards with 200 random-choice runs each: M is always the same value and always equals the product formula above.

---

**Distinct openings**

1. **Prime-valuation invariant (cleanest for (b))**: For each prime p, G_p = gcd of initial p-adic valuations is a true invariant. At terminal, v_p(M) = G_p. This directly gives part (b). Load-bearing step: gcd(min(a,b), |a-b|) = gcd(a,b).

2. **T+k monovariant (cleanest for (a))**: Strict decrease of T+k at each step, combined with the impossibility of reducing k from 1 to 0 in one step, gives exactly k=1 at termination.

3. **Product monovariant (alternative for (a))**: P = product of all board entries is non-increasing (divides by gcd(m,n) at each step). P >= 2^{2026} initially. But note gcd=1 moves don't decrease P; however gcd=1 moves do decrease k by 1. So P together with k give termination.

4. **Interpretation as subtractive Euclidean algorithm on multisets**: The per-prime process is the "n-pile" generalization of the Euclidean subtractive algorithm. The termination (convergence to gcd) for two elements is the standard Euclidean algorithm; for a multiset of n elements the same gcd invariant propagates because each step preserves gcd of the whole multiset.

---

**Candidate techniques**

- **Invariants & monovariants** (knowledge base: "Invariants & monovariants" entry under Combinatorics and General Proof Methods).
- **Divisor analysis / gcd structure** (knowledge base: "Divisor analysis: gcd structure, consecutive-integer coprimality" under Number Theory).
- The classical identity gcd(a,b) = gcd(min(a,b), |a-b|) — this is the **subtractive Euclidean algorithm identity**, not explicitly listed in knowledge_base.md but is elementary.
- **p-adic valuation** (knowledge base: "Lifting the Exponent (LTE)" and related entries; more directly, working prime by prime and the Omega function).

---

**Cheap-kill candidates**

- The identity gcd(min(a,b), |a-b|) = gcd(a,b) is the single structural fact that immediately gives the entire invariance for (b). No computation needed beyond this one-liner.
- For (a): note that k can decrease by at most 1 per move, so the process must stop at k=1 (not k=0) since reaching k=0 from k=1 is impossible (no valid move). This is a cheap parity/monotonicity kill.

---

**Knowledge-base entries to use**

- "Invariants & monovariants: a quantity preserved (or monotone) across moves." (under Combinatorics and General Proof Methods sections)
- "Divisor analysis: gcd structure" (under Number Theory)
- "Direct proof: chain definitions and known results from hypothesis to conclusion." (under General Proof Methods)

---

**Analogous past problems (cruxes)**

1. **aimo-0440** (most analogous): "Three nonneg reals r1,r2,r3 on blackboard with integer relation. Permitted operation: (x,y) -> (x, y-x). Prove we can end with at least one 0." Crux: L1 norm of coefficient vector as strict monovariant; the operation is exactly the subtractive Euclidean step. Why analogous: the Euclidean-style operation on a multiset with an L1-norm monovariant for termination and gcd as the preserved quantity is the direct analog of our per-prime analysis.

2. **aimo-0324** (moderately analogous): Board game where squarefree part of the board number is a monovariant. Uses the prime-exponent parity structure (analogous to our per-prime valuation analysis). Less directly analogous because the problem structure differs.

3. No closer match found in the corpus for "gcd/lcm board with both gcd-of-valuations invariant and T+k termination."

---

**Prior progress**

None (empty approach population, first round).

---

**Dead ends (do not retry)**

None yet. The approach space is open.

---

**Small-case / intuition notes (labeled as conjecture verified numerically)**

Conjecture (confirmed by simulation across many cases): M = product_p p^{gcd(v_p(x_i) : i=1..2026)}. Equivalently, M is the "gcd in the exponent-vector sense" of the 2026 initial numbers, where gcd is taken coordinate-wise in the prime factorization.

Examples verified:
- [6, 4]: v_2 gcds are gcd(1,2)=1, v_3 gcds are gcd(1,0)=1 -> M = 2^1 * 3^1 = 6. Confirmed.
- [12, 18]: gcd(2,1)=1 for p=2, gcd(1,2)=1 for p=3 -> M = 6. Confirmed.
- [4, 6, 15, 10, 9]: M = 30. Confirmed across 200 random runs.
- [100, 200, 300, 400, 500]: M = 30. Confirmed across 200 random runs.

Note: M is NOT the gcd(x_1,...,x_2026) in the usual sense. For [100, 200, 300, 400, 500], gcd = 100 but M = 30. This is because the operation acts on valuations, not directly on values.

---

**Load-bearing facts for (a) vs (b)**

- **(a) termination**: The monovariant T+k (or equivalently: k is non-increasing with T strictly decreasing whenever k stays constant; and k cannot reach 0 from k=1). The T+k argument is sufficient and clean.
- **(b) uniqueness of M**: The invariant G_p = gcd of all v_p values is preserved under each move (by the Euclidean gcd identity). At the terminal state, v_p(M) = G_p. These two facts together give the result.

The two parts are logically independent but use the same per-prime framework: (a) uses T+k, (b) uses G_p invariance.
