## imo-2026-01

### Lens: computational (small cases, prime-factorization analysis)

---

## Distinct openings

**Opening 1 — Lexicographic monovariant (k, P) for termination.**
Let k = count of numbers > 1 on the board, P = product of all board numbers. Case analysis:
- (A) m = n (equal pair): move gives (m, 1). k decreases by 1, P decreases.
- (B) m ≠ n, gcd(m,n) = 1 (coprime pair): move gives (1, mn). k decreases by 1, P unchanged.
- (C) m ≠ n, gcd(m,n) > 1: move gives (gcd, m*n/gcd^2). k unchanged, P → P/gcd < P.
The pair (k, P) strictly decreases lexicographically with every move. Bounded below by (1, 2) while game continues (since k ≥ 2 is required for a move, the game stops at k = 1). Since k decreases by at most 1 per step (verified computationally for all m,n in 2..14), exactly k = 1 remains at termination.

**Opening 2 — p-adic gcd invariant for uniqueness.**
For each prime p, define G_p = gcd(v_p(a_1), ..., v_p(a_2026)) where v_p(n) is the p-adic valuation of n.
Key algebraic fact (Euclidean property): gcd(min(a,b), |a-b|) = gcd(a, b).
The move changes v_p(m), v_p(n) from (α, β) to (min(α,β), |α−β|), which has the same gcd.
So G_p is unchanged by every move. In the terminal state {M, 1, 1, ..., 1}, gcd of v_p values = gcd(v_p(M), 0, ..., 0) = v_p(M). Therefore v_p(M) = G_p (initial), for all p. This pins M uniquely.

**Opening 3 — Explicit formula for M.**
M = prod_p p^{gcd(v_p(a_1), ..., v_p(a_2026))}, computed prime by prime. Confirmed by simulation on many examples. This is the outliner's hook for part (b): M is determined by the initial config via a prime-by-prime gcd of exponents.

**Opening 4 — Why coprime moves don't block termination.**
A coprime move (B) does NOT change P but DOES decrease k. So even when all pairs of numbers > 1 are pairwise coprime, moves can still be made (they reduce k). This avoids a potential confusion about whether P being stuck means the game stalls. The lexicographic structure handles it cleanly.

---

## Candidate technique(s)

- **Invariants and monovariants** (knowledge_base.md: "Invariants & monovariants"): both parts need one — (k, P) for termination, G_p = gcd of v_p values for uniqueness.
- **p-adic valuation analysis** (knowledge_base.md: Number Theory — p-adic valuation, Modular arithmetic/CRT): the operation is transparently described by v_p exponents.
- **Euclidean algorithm property**: the identity gcd(min(a,b), |a-b|) = gcd(a,b) is the algebraic heart of part (b). This is the gcd operation on exponents.

---

## Cheap-kill candidates

- **Exact case analysis on k**: each move changes k by 0 or −1 (three mutually exclusive cases). Coprimality-or-equality → k drops by 1; else → k stays, P strictly drops. Both are bounded, termination is immediate.
- **gcd(k, 0) = k** (critical for the final-state invariant calculation): in the terminal state, v_p(1) = 0, and gcd(v_p(M), 0, ..., 0) = v_p(M). Without this, one can't conclude the invariant pins M.

---

## Knowledge-base entries to use

- "Invariants & monovariants" (Combinatorics section): main technique for both parts.
- "Direct proof" + "Casework / exhaustion" (General Proof Methods): the three-case analysis for termination.
- "Divisor analysis" (Number Theory section): v_p structure.
- "General Proof Methods — Induction" (for the invariant's preservation under all n-1 moves starting from 2026 numbers down to 1).

---

## Analogous past problems (cruxes)

1. **aimo-0900** — Blackboard problem with arithmetic and harmonic means. Crux: "Find a residue class modulo a well-chosen prime closed under every allowed operation, making it a conserved invariant." Analogy: we also find a conserved invariant (G_p = gcd of v_p values) that pins the terminal value. Not identical (they use a mod-p invariant to prove impossibility; we use a gcd-of-exponents invariant to prove uniqueness), but the structure "conserved invariant determines terminal value on a blackboard" is exactly the same.

2. **aimo-0324** — Blackboard game, squarefree part as monovariant (product of primes with odd exponent). Crux: "Assign each board position the squarefree part and use as monovariant." Analogy: similarly assigns a prime-factorization-based quantity (squarefree part) as a monovariant; our problem uses the gcd of exponents across all board numbers instead. Both analyze the operation in terms of how prime factors transform.

3. **aimo-0003** (combinatorics) — "Reduce invariant under all orderings to invariance under a single adjacent transposition." Mild analogy for structure: if we can show G_p is invariant under a single arbitrary move, it's invariant under all sequences of moves. Not a direct crux match.

---

## Prior progress

None — workspace empty (Status: unsolved, no approaches yet).

---

## Dead ends (do not retry)

None — first round, no prior attempts.

---

## Small-case / intuition notes (labeled as conjecture)

**Confirmed by computation** (not proven here, but strongly supported):
- [4, 6, 9]: M = 6 regardless of move order (20 seeds tested).
- [12, 18, 30]: M = 30 regardless of order (10 seeds).
- [8, 12, 18, 27]: M = 6 regardless of order.
- [2, 3, 5, 7]: M = 210 = 2·3·5·7 (all pairwise coprime → M = product of all).
- 5 random boards of size 7–12 with random seed=0..4: formula always correct.

**Conjecture (supported by all examples)**: M = prod_p p^{gcd_i(v_p(a_i))}. This is the value that the gcd-of-exponents invariant forces.

**Key observation — operation in exponent space**: For each prime p independently, the move (m,n) → (gcd(m,n), lcm(m,n)/gcd(m,n)) acts on p-adic exponents as (a,b) → (min(a,b), |a-b|). This is one step of the binary GCD/Euclidean algorithm applied to the exponent pair. The gcd of any two-element multiset is preserved (gcd(min,|diff|) = gcd(a,b)), and by induction the gcd of the whole multiset is preserved.

**Stopping condition observed**: The game stops when only 1 number > 1 remains. This always happens (never saw 0 or 2+ remaining in any example). The three-case analysis explains why: k decreases by 0 or 1 per step, starts at 2026, terminates at k = 1.

**An edge case**: If all initial numbers are equal (e.g., [6, 6, 6]), then each move gives (6, 1), and k decreases by 1 each time. M = 6. Formula: gcd(v_p) = v_p(6) for each p. ✓
