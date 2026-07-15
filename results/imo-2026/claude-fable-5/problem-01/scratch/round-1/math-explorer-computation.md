## imo-2026-01 (Computation & Small Cases Lens)

### Problem Restatement

2026 integers > 1 on a blackboard. A move picks m > 1, n > 1 and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n). Prove: (a) terminates with exactly one entry M > 1; (b) M is path-independent.

---

### Computational Findings

#### The key structural decomposition (verified computationally)

For a move (m, n) → (gcd(m,n), lcm(m,n)/gcd(m,n)), the effect on p-adic valuations is:

  v_p(m) = a, v_p(n) = b  →  v_p(gcd) = min(a,b), v_p(lcm/gcd) = |a−b|

This is **exactly one step of the subtractive Euclidean algorithm** on the pair (a, b), applied **independently for each prime p**.

#### Conjectured (and computationally confirmed) formula for M

**M = ∏_p  p^{gcd(v_p(a₁), v_p(a₂), …, v_p(a_n))}**

where the product ranges over all primes p, and the gcd uses the convention gcd(0, k) = k.

**Verification:**
- BFS exhaustion on all boards of size 2–4 (with entries up to 35): unique terminal state always confirmed, formula always correct.
- 100 random plays each on 10 random 5-element boards: formula correct in every case.
- 50 random plays each on 5 random 20-element boards: formula correct in every case.

Selected spot-checks:
| Start | Formula M | BFS/random M | Match |
|---|---|---|---|
| (4, 6, 9, 15) | 30 | {30} | ✓ |
| (12, 18, 8, 6) | 6 | {6} | ✓ |
| (6, 10, 15, 35) | 210 | {210} | ✓ |
| (4, 4, 4, 4) | 4 | {4} | ✓ |
| (2, 3, 5, 7) | 210 | {210} | ✓ |
| (30, 42, 70, 105) | 210 | {210} | ✓ |

---

#### The invariant (empirically exact)

For each prime p, define g_p = gcd({v_p(a_i) : i = 1, …, n}).

**Claim (empirically verified across all tests): g_p is preserved by every move.**

Proof of this one-step invariance: the move sends (a, b) → (min(a,b), |a−b|) for prime p. The key identity:
  gcd(min(a,b), |a−b|) = gcd(a, b)

(standard Euclidean property: gcd(a, b) = gcd(a, b−a) when b ≥ a). Therefore:
  gcd(a, b, rest) = gcd(min(a,b), |a−b|, rest)

This was verified numerically for all pairs (a, b) ∈ {0,…,9}²: gcd(a,b) = gcd(min(a,b), |a−b|) in every case.

Note: gcd(0, k) = k (standard convention), so even when some entries are NOT divisible by p, the invariant still encodes the right information.

---

#### Termination monovariant (empirically verified)

Let P = ∏ a_i (product of all board entries) and k = #{i : a_i > 1}.

**Move types:**
- **Type A** (gcd(m,n) > 1, m ≠ n): Both outputs > 1. P decreases by factor gcd(m,n). k unchanged.
- **Type B** (gcd(m,n) = 1): One output becomes 1, the other becomes mn. P unchanged (since 1·mn = mn = m·n). k decreases by 1.
- **Type C** (m = n, so gcd = m): One output becomes m, other becomes 1. P decreases by m. k decreases by 1.

Empirically verified: P decreases by exactly gcd(m,n) at every type-A/C move. The pair (P, k) strictly decreases in lex order at every move. (Verified across all moves in multiple runs.)

Since P is a positive integer (bounded below by 1) and k is a non-negative integer, the game terminates in finitely many moves. The bound on total moves is at most P_initial steps (since P + k can increase by at most 1 per type-B move before P drops again).

---

#### Exactly one entry > 1 at termination (empirically: always exactly 1)

Across all BFS runs (boards of size 2–5, many start states): **every terminal state has exactly 1 entry > 1.** (The flag `exactly_1>1` was True in 100% of tests.)

Reasoning: At termination, k ≤ 1 (either 0 or 1 entries > 1).
- k = 0 impossible: If all entries were 1, then for every prime p dividing some initial a_i, the invariant g_p ≥ 1 (since gcd(k₁, k₂, …) ≥ 1 when at least one k_j ≥ 1). But all-1s gives g_p = 0. Contradiction.
- So k = 1. ✓

---

#### Edge cases

| Configuration | v_p gcd pattern | M | Result |
|---|---|---|---|
| All entries equal (a,a,…,a) | All exponents equal c; gcd = c | a | M = a ✓ |
| Pairwise coprime (2,3,5,7) | Each prime has gcd(1,0,0,0) = 1 | 2·3·5·7 = 210 | ✓ |
| Powers of one prime (4,4,16,64) | v_2 = [2,2,4,6], gcd = 2 | 4 | ✓ |
| Powers of one prime (2,4,8,16) | v_2 = [1,2,3,4], gcd = 1 | 2 | ✓ |
| Two coprime entries (2,9) | v_2=[1,0]→gcd=1, v_3=[0,2]→gcd=2 | 2·9=18 | ✓ |

---

### Distinct Openings

1. **Invariant-first (prime-by-prime) route**: The central object is the multiset of p-adic valuations for each prime. The invariant g_p = gcd({v_p(a_i)}) is preserved by each move (one identity: gcd(a,b) = gcd(min(a,b), |a−b|)). At termination the unique entry M satisfies v_p(M) = g_p. This simultaneously proves (b) and the form of M.

2. **Product monovariant route for (a)**: P = ∏ a_i is non-increasing. It decreases by exactly gcd(m,n) with each type-A/C move. Between decreases, only type-B moves happen, and each type-B move decreases k. The lex pair (P, k) is strictly decreasing — elementary termination argument.

3. **Alternative termination — total Ω sum**: Σ Ω(a_i) = Σ_i Σ_p v_p(a_i) is also non-increasing (decreases by Ω(gcd(m,n)) at each type-A/C move). This is equivalent to log P (same moves change both). Less clean since it's the same phenomenon.

4. **Reachability / "can always complete"**: Any starting board can reach exactly one terminal (confirmed by BFS). The game cannot get stuck (at any board with k ≥ 2, there are always valid moves). Combining with invariant gives uniqueness.

---

### Candidate techniques

- **Invariants & monovariants** (knowledge_base.md: "Invariants & monovariants: a quantity preserved (or monotone) across moves").
- The **subtractive Euclidean algorithm** identity: gcd(a, b) = gcd(min(a,b), |a−b|). This is the engine of the invariant.
- **p-adic valuation analysis**: the problem reduces per-prime; valuations evolve independently.

---

### Candidate knowledge-base entries

- "Invariants & monovariants" (Combinatorics section): directly applicable — g_p is the invariant.
- "Number Theory — Divisor analysis / gcd structure": the gcd convention gcd(0, k) = k matters.
- "General Proof Methods — Invariant / monovariant": product P as monovariant for termination.
- "Problem-Solving Heuristics — Solve a simpler / special case first": the 2-element case is just the Euclidean algorithm on (v_p(m), v_p(n)); all conclusions generalize.

---

### Analogous past problems (cruxes)

- **aimo-0028** (NT, divisibility-and-gcd): Uses the Euclidean step gcd(n²+n+1, n²−n+1) = gcd(2n, …) to prove a gcd = 1 conclusion. The crux move (stripping via Euclidean step) is analogous to the identity gcd(a,b) = gcd(min(a,b), |a−b|) used here. Not a close structural match but uses the same Euclidean gcd identity.
- No crux in the corpus is a genuinely close match: this problem's crux (gcd of p-adic valuation multiset as invariant of an iterative operation) doesn't appear to be in the database. The problem is elementary for NT but the specific invariant is clean.

---

### Empirical invariants (hold exactly)

1. **g_p = gcd({v_p(a_i)})** is preserved exactly by every move. (Proved one-step; verified exhaustively.)
2. **Product P = ∏ a_i is non-increasing**, decreasing by exactly gcd(m,n) at type-A/C moves. (Verified exactly.)
3. **At termination: exactly one entry M > 1.** (Verified in 100% of all BFS/random runs.)
4. **M = ∏_p p^{g_p}** with g_p as above. (Correct in 100% of all tests.)

---

### Prior progress

None (round 1, fresh workspace).

### Dead ends

None explored (first round). Candidate false directions to avoid:
- Do NOT try to prove g_p = max(v_p) or g_p = sum(v_p); both are wrong.
- Do NOT use Σ a_i (sum of entries) as a monovariant — it is NOT monotone (type-B moves can increase it).

### Small-case / intuition notes (labeled as conjecture)

- **Conjecture (strongly supported)**: The invariant g_p = gcd({v_p(a_i)}) characterizes M completely and is the *only* game-theoretically relevant quantity.
- **Observation**: The move is a prime-by-prime subtractive Euclidean step; the game is n simultaneous copies of the subtractive Euclidean algorithm (one per prime), coupled only by the constraint that moves pick actual board entries (not individual primes).
- **Observation**: Termination is faster when gcds are large (more product decrease per move). Slowest case is pairwise coprime entries (all type-B moves, each reducing k by 1).
