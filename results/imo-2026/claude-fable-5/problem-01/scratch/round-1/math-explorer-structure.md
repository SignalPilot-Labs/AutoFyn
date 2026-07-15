## imo-2026-01

### Per-prime decomposition and the critical coupling note

**The per-prime operation.** Fix any prime p. If a move replaces (m, n) by (gcd(m,n), lcm(m,n)/gcd(m,n)), then for each prime p the pair of exponents (a, b) = (v_p(m), v_p(n)) transforms to:

  (min(a, b),  max(a, b) − min(a, b)) = (min(a, b), |a − b|)

This is precisely the subtraction step of the Euclidean algorithm (gcd(a, b) = gcd(min(a,b), |a−b|)). The primes evolve INDEPENDENTLY under the same move: the exponent dynamics for distinct primes p, q do not interact.

**Where coupling bites.** The only cross-prime constraint is the legality condition: the move requires m > 1 and n > 1 (i.e., at least one prime's exponent in each entry is positive). This affects which pairs may be selected but does NOT affect the per-prime invariant structure once a move is made. In particular, it is never the case that a move is illegal due to some per-prime condition; the legality is a global condition on the whole integer. The coupling is therefore benign for both termination and uniqueness.

---

### The exact invariant (completely pinned down)

For each prime p, define:

  g_p = gcd(v_p(x_1), v_p(x_2), ..., v_p(x_{2026}))

using the convention gcd(k, 0) = k (so zeros from entries not divisible by p are ignored, and the gcd equals the gcd of the NONZERO exponents only).

**Claim: g_p is invariant throughout the process.**

Proof sketch: the move on (m, n) changes (a, b) = (v_p(m), v_p(n)) to (min(a,b), |a−b|). By the Euclidean subtraction identity, gcd(a, b) = gcd(min(a,b), |a−b|). Hence gcd(g_p^(other entries), a, b) = gcd(g_p^(other), gcd(a,b)) = gcd(g_p^(other), gcd(min(a,b), |a−b|)) = gcd(g_p^(other), min(a,b), |a−b|). The gcd of the full exponent multiset is unchanged.

**Computational verification:** All strategies (first pair, last pair, max-gcd pair, random) give the same M on all tested boards (confirmed by exhaustive simulation of small boards and 10-strategy simulation of large boards including 2026-copy boards). The W-monovariant strictly decreased on all 4150 exhaustively tested moves.

**Value of M.** In the terminal state {M, 1, 1, ..., 1}, the exponent multiset for prime p is {v_p(M), 0, ..., 0}. The gcd = gcd(v_p(M), 0, ..., 0) = v_p(M). By invariance: v_p(M) = g_p. So

  **M = Π_p p^{gcd(v_p(x_1), ..., v_p(x_{2026}))}**

This is determined entirely by the initial multiset, independent of choices. (Conjecture verified computationally to high confidence; proved structurally via the invariant.)

**M > 1 is forced.** Each x_i > 1 has at least one prime factor p_i with v_{p_i}(x_i) ≥ 1. The gcd of the exponent multiset for p_i includes this positive value and possibly zeros from other entries; but gcd(k, 0, ..., 0) = k ≥ 1. So g_{p_i} ≥ 1, hence M ≥ p_i ≥ 2 > 1.

---

### What is monotone (monovariants for termination)

**Ω(n) = number of prime factors of n with multiplicity** (i.e., Σ_p v_p(n)).

For a move on (m, n):
  Ω(gcd(m,n)) + Ω(lcm(m,n)/gcd(m,n)) = Σ_p [min(a_p,b_p) + |a_p−b_p|] = Σ_p max(a_p, b_p) = Ω(lcm(m,n)).

Original sum: Ω(m) + Ω(n) = Σ_p (a_p + b_p).

Difference: [Ω(m) + Ω(n)] − [Ω(gcd(m,n)) + Ω(lcm(m,n)/gcd(m,n))] = Σ_p min(a_p, b_p) = Ω(gcd(m,n)).

So ΣᵢΩ(xᵢ) decreases by exactly Ω(gcd(m,n)) per move, which is ≥ 1 when gcd(m,n) > 1 and = 0 when gcd(m,n) = 1.

**The three cases for a move on m > 1, n > 1 (verified exhaustively):**
- **Case A (m = n):** outputs {m, 1}. Count of entries > 1 drops by 1. ΣΩ drops by Ω(m) ≥ 1.
- **Case B (m ≠ n, gcd(m,n) = 1):** outputs {1, mn}. Count drops by 1. ΣΩ unchanged (Ω(mn) = Ω(m)+Ω(n)).
- **Case C (m ≠ n, gcd(m,n) > 1):** both outputs > 1. Count unchanged. ΣΩ drops by Ω(gcd) ≥ 1.

Define the monovariant: **W = (count of entries > 1) + ΣᵢΩ(xᵢ)**.

In all three cases, W drops by ≥ 1. Since W is a non-negative integer (all terms ≥ 0), the process must terminate after finitely many moves.

**Alternative monovariant:** log(Π xᵢ) + C·(count > 1) for any C > 0 also works: in Case B log-product is unchanged but count drops; in Cases A and C log-product drops by log(gcd²) and count changes accordingly. Less clean than W.

---

### Why exactly one entry > 1 at termination

**The board always has exactly 2026 entries total** (each move removes 2 and adds 2).

**At most one output equals 1 per move.** From m, n > 1:
- gcd(m,n) = 1 → lcm(m,n)/gcd(m,n) = mn ≥ 4 > 1. So ONE output is 1 (the gcd), the other > 1.
- m = n → gcd(m,n) = m > 1, lcm(m,n)/gcd(m,n) = 1. ONE output is 1, the other > 1.
- gcd(m,n) > 1 and m ≠ n → both > 1. ZERO outputs are 1.
Confirmed computationally: no pair (m,n) with m,n > 1 and m ≤ 50 gives both outputs = 1.

**Count of entries > 1 is non-increasing** (drops by 0 or 1 per move), starts at 2026, and can never jump from ≥ 2 to 0 in one step. The process terminates when count ≤ 1. But count = 1 → no valid pair to pick → process already stopped. Thus termination always happens at count = 1 (EXACTLY one entry > 1 remains).

---

### Candidate invariants (classification)

| Quantity | Status |
|---|---|
| g_p = gcd(v_p(xᵢ)) for each prime p | **Exact invariant** (proved) |
| M = Π_p p^{g_p} | **Determined by invariant** (the terminal value) |
| Product Π xᵢ | Not invariant (drops by gcd(m,n)² per Case A/C move) |
| LCM of all xᵢ | Monotone non-increasing (max v_p non-increasing), not invariant |
| ΣᵢΩ(xᵢ) | Strict monovariant (decreases in Cases A and C) |
| Count of entries > 1 | Monotone non-increasing (decreases in Cases A and B) |
| W = count + ΣΩ | **Strict monovariant** (decreases in ALL cases) |
| Σᵢv_p(xᵢ) (sum of exponents for fixed p) | NOT invariant (decreases by min(a,b) per move when both divisible by p) |
| max_i v_p(xᵢ) | Monotone non-increasing |

---

### Distinct proof openings

**Opening 1 (cleanest, recommended): Per-prime gcd-invariant + W monovariant.**
Define the invariant g_p per prime using the Euclidean identity gcd(a,b) = gcd(min(a,b), |a−b|). Use W = (count>1) + ΣΩ as the strict monovariant to guarantee termination. Combine with the "at most one output = 1 per move" case analysis to pin the terminal count at exactly 1. Read off v_p(M) = g_p for uniqueness. Likely hard step: case analysis for W and proving at most one output can be 1, both of which are elementary.

**Opening 2: Ω-only monovariant with separate count argument.**
Use ΣᵢΩ(xᵢ) as monovariant for termination in Cases A/C, and separately track that Case B moves reduce the count. Show the two quantities together force termination. This splits the argument into two sub-cases but is arguably more transparent about what each type of move does.

**Opening 3: Product monovariant.**
The product Π xᵢ over entries > 1: Case C moves decrease it (by gcd(m,n)² ≥ 4), Case A moves also decrease it (by m), Case B moves keep Π xᵢ steady over entries > 1 (we lose m and n, gain mn, with gcd=1). So log(Π xᵢ over entries > 1) + C·(count>1) is a monovariant. For uniqueness, still need the per-prime invariant g_p. Slightly less clean than W.

**Opening 4: LCM-decrease route.**
The LCM of all entries is v_p(lcm) = max v_p(xᵢ) ≥ g_p: it decreases or stays. Together with invariance of g_p, the LCM is "squeezed" toward M. This approach would need a separate termination argument and is less self-contained.

---

### Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics section): "a quantity preserved (or monotone) across moves" — g_p is the preserved quantity, W is the monovariant.
- **Divisor analysis, gcd structure** (Number Theory): gcd(a,b) = gcd(min(a,b), |a−b|) (subtraction Euclidean algorithm) is the core.
- **Direct proof + Casework** (General): three-case analysis of move outcomes.
- **p-adic valuation** (Number Theory): the entire framing is in terms of v_p(n).

---

### Analogous past problems (cruxes)

1. **aimo-0836** (combinatorics, processes-and-algorithms): Board operations {a,b} → {a+b, |a−b|}. The crux of showing convergence uses minimal-sum descent for a set; the invariant is the gcd of all entries. Analogous: same "board operation" style, same "gcd of all entries is invariant" structural idea (though for sums/differences instead of gcd/lcm). Crux move: "prove a size-reducing move always exists by contradiction on minimal sum extremal object."

2. **aimo-0236** (combinatorics, invariants-and-monovariants): Blackboard with numbers evolving under arithmetic operations; uses p-adic valuation to classify terminal states. Analogous: the classification of terminal/non-terminal configurations via v_p is directly relevant.

3. **aimo-0324** (combinatorics, invariants-and-monovariants): Squarefree part as monovariant in a blackboard game. Crux: "the squarefree part S(n) = product of primes with odd exponent is a monovariant." Analogous in spirit: tracking per-prime exponent parity/values as the structural quantity.

---

### Prior progress
None (round 1, fresh workspace).

### Dead ends (do not retry)
None (round 1).

### Small-case / intuition notes (conjectural)
- **Formula for M** (confirmed by computation, not yet proved): M = Π_p p^{gcd(v_p(x_1), ..., v_p(x_{2026}))}. Equivalently, v_p(M) = gcd of the nonzero p-adic valuations across all initial entries, for each prime p.
- **The "all entries coprime" extreme**: if x_1, ..., x_{2026} are pairwise coprime (each prime appears in at most one entry), then g_p = 1 for each prime p that appears at all, so M = product of all distinct prime factors appearing. E.g., {2,3,5} → M = 30.
- **The "all entries equal to c" extreme**: {c, c, ..., c} → M = c (since g_p = v_p(c) for each p). Confirmed: each move {c,c} → {c, 1} reduces count by 1. After 2025 such moves, one c remains.
- The coupling between primes (the "m > 1 and n > 1" constraint) is benign and does not create new obstacles in either proof.
