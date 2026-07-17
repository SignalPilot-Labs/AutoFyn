## imo-2026-01

**Lens: invariants under the transformation (m,n) → (gcd(m,n), lcm(m,n)/gcd(m,n))**

---

### The core algebra of the operation

Write m = g·a, n = g·b with g = gcd(m,n) and gcd(a,b) = 1. Then:
- gcd(m,n) = g
- lcm(m,n) = gab
- lcm(m,n)/gcd(m,n) = ab

So the pair (ga, gb) → (g, ab), with gcd(a,b) = 1 in the output.

For each prime p, the p-adic valuations transform as:
(v_p(m), v_p(n)) = (v_p(g) + v_p(a), v_p(g) + v_p(b)) → (v_p(g), v_p(a) + v_p(b))

which is NOT (min, |diff|) in general. The correct per-prime view is:
(α, β) → (min(α, β), |α − β|)

verified by: v_p(gcd) = min(v_p(m), v_p(n)), v_p(lcm/gcd) = max − min = |α − β|.

Key algebraic identity (verified numerically for all test cases):
**gcd(min(α, β), |α − β|) = gcd(α, β)**

This is the Euclidean algorithm in disguise and is the crux.

---

### INVARIANT (for part b)

**Claim:** For each prime p, the quantity d_p = gcd(v_p(a₁), v_p(a₂), ..., v_p(a_{2026})) is preserved by every move.

**Why:** A move on entries m and n changes the pair of p-adic valuations from (α, β) to (min(α,β), |α−β|). The other 2024 entries are unchanged. Since gcd(min(α,β), |α−β|) = gcd(α, β) (Euclidean identity), the gcd of all 2026 valuations is unchanged.

**Terminal state:** In the terminal state, one number M > 1 and 2025 ones. The multiset of p-adic valuations is {v_p(M), 0, ..., 0}. Since gcd(v_p(M), 0, ..., 0) = v_p(M) (convention: gcd(a,0) = a), we get v_p(M) = d_p.

**Therefore: M = ∏_p p^{d_p}**, where d_p = gcd(v_p(a₁), ..., v_p(a_{2026})) computed from the initial configuration. This is independent of move choices. (Verified numerically for all test cases including random orderings.)

**M > 1:** Since all initial aᵢ > 1, each aᵢ has at least one prime divisor p with v_p(aᵢ) ≥ 1. For that prime, d_p = gcd(..., v_p(aᵢ), ...) ≥ 1 (since gcd(a, 0) = a ≥ 1). So M ≥ p ≥ 2 > 1. (This is crucial for part a.)

---

### MONOVARIANT (for part a — termination)

Two candidate monovariants, both clean:

**Option 1 (Pair monovariant):** Let W = Σᵢ Ω(aᵢ) (total count of prime factors with multiplicity across all entries, counting 1s as contributing 0), and N = #{i : aᵢ > 1}. Order by lex: (W, N) > (W', N') if W > W' or (W = W' and N > N').

- Move with gcd(m,n) > 1: W decreases by Ω(gcd(m,n)) ≥ 1, so (W, N) decreases lexicographically regardless of N.
- Move with gcd(m,n) = 1: operation is (m,n) → (1, mn), so W stays same (Ω(1)+Ω(mn)=Ω(m)+Ω(n)), N decreases by 1. So (W,N) decreases lexicographically.

Both W ≥ 0 and N ≥ 0 are non-negative integers, so the process terminates.

**Option 2 (Product monovariant, single quantity):** Let P = ∏ aᵢ (product of all board entries) and define Q = P · 2^N where N = #{aᵢ > 1}. Then Q is a positive integer and strictly decreases by at least a factor of 2 per step:

- gcd(m,n) = g ≥ 2, both outputs > 1: P → P/g ≤ P/2, N unchanged → Q → Q/g ≤ Q/2.
- gcd(m,n) = g ≥ 2, one output = 1 (happens when m = n): P → P/g, N → N−1 → Q → Q/(2g) ≤ Q/4.
- gcd(m,n) = 1 (operation is (m,n) → (1,mn)): P unchanged, N → N−1 → Q → Q/2.

In all cases Q decreases by factor ≥ 2. Since Q is a positive integer, the process terminates in ≤ log₂(Q_initial) steps.

(Numerically verified: for [12,18], Q went 864 → 144 → 12, factors 6 and 12.)

---

### WHEN DOES THE PROCESS STOP?

The process stops when no two entries > 1 exist (N ≤ 1). By the invariant, M = ∏_p p^{d_p} > 1 must remain on the board, so N ≥ 1. Hence the process stops with N = 1: exactly one entry M > 1 on the board.

---

### Distinct openings

1. **Pure invariant approach (cleanest for both parts):** Use the gcd-of-p-adic-valuations invariant to identify M; use Q = P·2^N as a single strictly-decreasing monovariant for termination. These two ideas together close both parts.

2. **Lex-monovariant approach:** Use the pair (W, N) = (Σ Ω(aᵢ), count of entries > 1) with lexicographic order. Cleaner case analysis distinguishing gcd > 1 vs gcd = 1.

3. **Valuation-sequence convergence approach:** For each prime p, view the multiset of p-adic valuations as a sequence converging (via the operation (α,β) → (min,|diff|)) to a terminal state with all valuations equal to 0 except one equal to d_p. This is the Euclidean algorithm running on the exponent vectors, and it terminates because the sum of p-adic valuations for each prime is non-increasing (strictly decreasing unless one of the operated values has v_p = 0).

4. **Prime-by-prime tracking approach:** For each prime p independently, track the multiset of v_p values. The operation on v_p is (α,β) → (min(α,β), |α−β|). The sum Σ v_p(aᵢ) is non-increasing for each p. Termination: the sum across all primes strictly decreases when gcd > 1, and N decreases when gcd = 1. Final state: multiset of v_p values is {d_p, 0, 0, ..., 0} for each p.

---

### Candidate techniques

- **Invariants & monovariants** (knowledge_base.md: "Invariant / monovariant" section; "Divisor analysis" for the gcd-of-valuations fact)
- **p-adic valuations** (knowledge_base.md: Number Theory section)
- **Euclidean algorithm identity:** gcd(min(a,b), |a-b|) = gcd(a,b) is the key lemma
- **Ω(gcd) trick:** total Ω decreases by exactly Ω(gcd(m,n)) per step when gcd > 1

---

### Cheap-kill candidates

- **Product monovariant Q = P·2^N:** decreases by factor ≥ 2 each step — this is the cleanest single monovariant for part (a), requiring no case split into sub-cases.
- **M = ∏_p p^{d_p}:** once the invariant is found, part (b) is immediate by inspection of the terminal state.

---

### Knowledge-base entries to use

- "Invariants & monovariants" (Combinatorics section of knowledge_base.md)
- "Divisor analysis: gcd structure" (Number Theory section)
- "p-adic valuation" (Number Theory section — d_p = gcd of valuations)

---

### Analogous past problems (cruxes)

1. **aimo-0324** (number_theory | invariants-and-monovariants): "Assign each board position the squarefree part of its number and use it as a monovariant." — Crux: tracking a valuation-derived quantity (squarefree part = ∏_p p^{v_p mod 2}) as a board invariant/monovariant. Analogous because it uses the prime-exponent parity as an invariant of a blackboard operation, just as we use gcd of p-adic valuations here. Less directly analogous (squarefree vs. gcd of exponents) but closest match.

2. **aimo-0236** (combinatorics | invariants-and-monovariants): "Reduce a two-player termination question to a single p-adic threshold." — Uses p-adic valuation to partition regimes for termination. The technique of using v_p to track progress is analogous to tracking d_p = gcd of v_p values here.

3. None closely analogous: no crux problem found with the exact (m,n) → (gcd,lcm/gcd) operation. The problem is self-contained with the Euclidean identity as its crux.

---

### Prior progress

None (first round, Status: unsolved, no approaches).

---

### Dead ends (do not retry)

None yet.

---

### Small-case / intuition notes (labeled conjecture)

- **Verified numerically:** M = ∏_p p^{gcd(v_p(a₁),...,v_p(a_{2026}))} matches simulated terminal value for all test cases: [2,3]→6, [4,6]→6, [4,8]→2, [4,4,4]→4, [12,18,45,60,30]→30 (10 random orderings all agree).
- **Conjecture:** The upper bound on steps is O(log(∏ aᵢ)) since Q decreases by factor ≥ 2 each step.
- **Note:** The number 2026 plays no role in the proof — the result holds for any number of initial entries ≥ 2.
- The operation (m,n) → (gcd,lcm/gcd) is "spreading" prime factors: when m and n share prime factors, some are peeled off from both and one factor gets them concentrated. This is a "prime factor redistribution" that always moves toward the terminal state where each prime's exponents are concentrated in one number.
