## imo-2026-01 (termination/monovariant lens)

**Problem recap.** 2026 integers > 1 on a blackboard. Move: pick m>1, n>1 (different places), replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Continue while possible. (a) Prove finitely many moves, exactly one M>1 remains. (b) Prove M is independent of choices.

---

### Key algebraic decomposition

Write m = da, n = db with d = gcd(m,n), gcd(a,b) = 1. Then:
- gcd(m,n) = d
- lcm(m,n)/gcd(m,n) = dab/d = ab

So the move replaces (da, db) with (d, ab). The results need not both be >1: if a=b=1 (i.e., m=n=d), we get (d, 1). If d=1 (coprime m,n), we get (1, mn).

**For each prime p:**  
v_p(m) = alpha, v_p(n) = beta. After move: v_p(d) = min(alpha,beta), v_p(ab) = |alpha-beta|.  
This is exactly one step of the subtractive Euclidean algorithm on exponents.

---

### Distinct openings

**Opening A — Monovariant: Omega_total + count_>1**

Let Omega_total = sum of Omega(x_i) over all board numbers (total prime factors with multiplicity). Let count_>1 = number of board entries > 1.

Under a move:
- If gcd(m,n) = 1 (coprime case): results are (1, mn). Omega unchanged. count_>1 decreases by 1 (two >1 gone, one 1 and one mn>1 added). Net: monovariant decreases by 1.
- If gcd(m,n) = d >= 2, and ab = 1 (i.e., m = n): results are (d, 1). Omega decreases by Omega(d) >= 1. count_>1 decreases by 1. Net: monovariant decreases by Omega(d)+1 >= 2.
- If gcd(m,n) = d >= 2, and ab >= 2: results are (d>1, ab>1). Omega decreases by Omega(d) >= 1. count_>1 unchanged. Net: monovariant decreases by Omega(d) >= 1.

In ALL three cases, Omega_total + count_>1 strictly decreases. Since it is a non-negative integer, the process terminates. This is a complete monovariant.

**Opening B — Product monovariant (partial)**

Total product P = prod(x_i). Under move: P -> P/d. Strictly decreases when d>=2, unchanged when d=1. Not strict in all cases, but useful: P is always a positive integer >= 1, and P > 1 throughout (see below). Not sufficient alone for termination.

**Opening C — Count monovariant alone (fails)**

count_>1 is non-increasing but NOT strictly decreasing: when gcd=d>=2 and ab>=2, both results >1 and count unchanged. Fails as monovariant alone.

---

### Terminal configuration characterization

The process terminates when count_>1 <= 1 (no two entries >1 to pick).

**Exactly one M>1 remains (not zero):**

No move can produce two 1s: if gcd(m,n) = 1 then the results are 1 and mn >= 4; if gcd(m,n) = d then results are d >= 2 and ab. The result (gcd=1 AND ab=1) would require mn=1, impossible since m,n >= 2. So every move has at least one result > 1. Hence count_>1 can decrease by at most 1 per move: from 2026 -> 2025 -> ... -> 1. It never reaches 0.

Alternatively: the product P = prod(x_i) satisfies P >= 2 at all times (P starts at >= 2^2026, only divides by integer factors, and if P=1 all numbers would be 1 meaning count_>1=0, contradiction since P > 1 from start). So at termination, product P >= 2 means at least one number > 1.

**Terminal state:** exactly one M > 1, and 2025 ones.

---

### Invariant for part (b)

For each prime p, define g_p = gcd(v_p(x_1), ..., v_p(x_2026)) (the gcd of all p-exponents across the board). Convention: gcd(0,...,0)=0 and gcd(n,0)=n.

**Claim: g_p is invariant under each move.**

Proof sketch: The move on (m,n) changes the p-exponent pair (alpha, beta) -> (min(alpha,beta), |alpha-beta|). Since gcd(beta, alpha-beta) = gcd(alpha,beta), the gcd of the whole multiset is unchanged. This uses the standard Euclidean algorithm identity.

**Reading off M from the invariant:**

In the terminal state {M, 1, 1, ..., 1}: g_p = gcd(v_p(M), 0, ..., 0) = v_p(M).

So v_p(M) = g_p(initial) for all primes p, giving:

**M = prod_p p^{gcd(v_p(x_1), ..., v_p(x_2026))}**

This is completely determined by the initial configuration. M is invariant of choices. Confirmed by simulation on many examples.

Note: M > 1 because the initial numbers are all > 1, so for each x_i there exists some prime p with v_p(x_i) >= 1. The product defining M is therefore > 1 (there exists some prime p where gcd >= 1 because some x_i has v_p >= 1 while others may be 0 but gcd(n,0)=n).

---

### Candidate technique(s)

- **Invariants & monovariants** (knowledge_base.md: "Invariants & monovariants" under Combinatorics and General Proof Methods).
- **Divisor analysis / gcd structure** (knowledge_base.md: NT section).
- The key algebraic fact: the Euclidean algorithm step gcd(min(a,b), |a-b|) = gcd(a,b).

---

### Cheap-kill candidates

None for the main proof. But cheap to verify:
- No move can make both results 1 (since m*n >= 4 but we'd need gcd=1 and mn/1=1).
- Product is always >= 1 and never drops to 1 from > 1 while count_>1 >= 2 (since at termination count=1, product = M >= 2).

---

### Knowledge-base entries to use

1. **Invariants & monovariants** (Combinatorics section) — exactly the technique.
2. **Divisor analysis** (NT section: "gcd structure, consecutive-integer coprimality") — for the gcd decomposition.
3. **General Proof Methods > Invariant/monovariant** — for both parts.
4. **Problem-Solving Heuristics > Solve simpler cases** — small N=2,3 cases confirm the formula.

---

### Analogous past problems (cruxes)

1. **aimo-0236** (combinatorics, invariants-and-monovariants): Uses p-adic valuation sum as a strict monovariant for a token-halving process. The crux: "when adding a fixed constant whose valuation strictly exceeds each token's valuation, the addition preserves every valuation, so the total-valuation sum is a strict monovariant under the halving move." Analogous in that p-adic exponents are tracked as a monovariant/invariant for a process on integers. Not a perfect match (different operation) but the closest in style.

2. **aimo-0264** (combinatorics, invariants-and-monovariants): "To prove a string-rewriting/branching process terminates, assign each string an ordinal-valued rank via a tower of exponentials nested by a monotone parameter." Analogous in that termination of a combinatorial rewriting process is proved by a carefully designed (multi-level) monovariant. Our case is simpler — Omega + count works.

3. **aimo-0028** (number_theory, divisibility-and-gcd): "Strip an even factor from a gcd of two near-equal quadratics via the Euclidean step." Uses the identity gcd(a, b-a) = gcd(a,b) in a number theory argument. The Euclidean step identity is the key algebraic fact underlying the invariance of g_p.

No problem in the corpus is a direct analog of this exact board operation.

---

### Prior progress

None — first round, no approaches yet.

### Dead ends (do not retry)

None established yet.

### Small-case / intuition notes (conjectured)

- Simulation with N=2,3,4 and various initial values: M = prod_p p^{gcd(v_p(x_i))} confirmed every time.
- When all initial numbers are equal (all = k): g_p = v_p(k) for all p, so M = k. The process eventually yields (k, 1, 1, ..., 1).
- When all initial numbers are pairwise coprime: for each prime p, at most one x_i has v_p > 0, so gcd(v_p(x_1),...) = that v_p. Hence M = prod x_i (= product of all, since the gcd captures each prime fully). In this case the moves just collect all prime factors into one number.
- The monovariant Omega_total + count_>1 starts at (Sigma Omega(x_i)) + 2026 and ends at Omega(M) + 1. The total number of steps is at most (Sigma Omega(x_i)) + 2025.
