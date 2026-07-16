## imo-2026-01

### Problem recap
2026 integers > 1 on a blackboard. Move: choose m > 1, n > 1, replace with gcd(m,n) and lcm(m,n)/gcd(m,n). Prove (a) game terminates with exactly one M > 1; (b) M is independent of choices.

---

### The core algebraic structure

Write m = g·a, n = g·b with g = gcd(m,n) and gcd(a,b) = 1. The operation produces (g, ab):
- gcd(m,n) = g
- lcm(m,n)/gcd(m,n) = gab/g = ab

**At each prime p**, the valuation vector (v_p(m), v_p(n)) maps to (min(v_p(m), v_p(n)), |v_p(m) - v_p(n)|). This is EXACTLY the subtraction step of the Euclidean algorithm on the pair of valuations.

**Euclidean identity**: gcd(min(α,β), |α−β|) = gcd(α, β) — this is the key algebraic fact that underlies the proof of part (b).

---

### Distinct structural openings

**Opening A — p-adic gcd invariant (direct route to part b):**
For each prime p, define D_p = gcd(v_p(a_1), ..., v_p(a_{2026})). In any move on (a_i, a_j):
- v_p changes: (α, β) → (min(α,β), |α−β|)
- gcd(min(α,β), |α−β|) = gcd(α,β) by the Euclidean algorithm
- So D_p = gcd({v_p(a_k) for all k}) is unchanged — it is an invariant

At termination (exactly one M > 1, rest are 1): D_p = gcd(v_p(M), 0, 0, ..., 0) = v_p(M) [using gcd(k,0) = k].
Therefore v_p(M) = D_p for all p, determining M = Π_p p^{D_p} from initial data alone. Part (b) proved.

**Opening B — lexicographic monovariant for termination (part a):**
Three cases in any move on (m, n):
1. gcd(m,n) = 1 (coprime, m≠n): output (1, mn). N_gt1 decreases by 1. Product P = Π(all a_i) unchanged (gcd=1).
2. m = n: output (m, 1). N_gt1 decreases by 1. Product P decreases by factor m ≥ 2.
3. gcd(m,n) > 1, m≠n: output (gcd, ab) with both > 1. N_gt1 unchanged. Product P decreases by factor gcd(m,n) ≥ 2.

In ALL cases, the pair (P, N_gt1) with lexicographic order strictly decreases: cases 2 and 3 decrease P; case 1 keeps P constant but decreases N_gt1. Since P is a positive integer and N_gt1 ≥ 0, the pair is well-founded. Termination follows.

Equivalent monovariant: (Σ_i Ω(a_i), N_gt1) where Ω(n) = number of prime factors with multiplicity. Total Ω decreases by Ω(gcd(m,n)) ≥ 0 in each move; when decrease is 0 (gcd=1), N_gt1 decreases by 1.

**Opening C — N_gt1 = 0 is impossible (completing part a):**
The invariant D_p ≥ 1 for any prime p dividing some initial a_i [since gcd(k, 0) = k ≥ 1 for k ≥ 1]. If N_gt1 = 0 at termination (all values are 1), then D_p = gcd(0,0,...,0) = 0 for all p. But since all a_i > 1, at least one a_i has a prime divisor p with v_p(a_i) ≥ 1, hence D_p ≥ 1. Contradiction. So N_gt1 = 1 at termination.

**Combined proof sketch:**
- Termination: (P, N_gt1) monovariant.
- Exactly one M > 1: N_gt1 ≤ 1 at termination (game-stop condition), N_gt1 ≥ 1 (from D_p invariant), so N_gt1 = 1.
- M = Π_p p^{D_p}: from invariant + terminal-state analysis.
- Independence of M: D_p preserved, so M formula uses only initial data.

---

### What quantities are NOT invariant / NOT useful alone

- **Product Π a_i**: non-increasing (decreases by gcd(m,n) each step). NOT invariant. Useful as monovariant component.
- **Sum of v_p values at prime p** (= Σ_i v_p(a_i)): non-increasing (decreases by min(v_p(m), v_p(n)) = v_p(gcd)). NOT invariant. Not strong enough alone for termination.
- **N_gt1 (count of numbers > 1)**: non-increasing but can stay constant (case 3). NOT invariant alone.
- **gcd(a_1, ..., a_{2026}) (ordinary gcd)**: NOT the invariant! Example: [2,3] has gcd=1 but M=6. The correct invariant is coordinatewise gcd of exponent vectors, which differs from ordinary gcd.
- **Product alone**: product can stay constant (when gcd(m,n)=1) so doesn't alone prove termination.

---

### Terminal condition

The game stops when N_gt1 ≤ 1 (no two numbers > 1 to choose). Since N_gt1 = 1 at termination (proved above), the terminal state is exactly one M > 1 and 2025 ones.

---

### Key subtlety: gcd(k, 0) = k

The crucial convention for the invariant argument: gcd(k, 0) = k for any k ≥ 1 (since 0 is divisible by every integer). This ensures D_p ≥ v_p(a_i) ≥ 1 whenever a_i has prime factor p, even if all other a_j are coprime to p. Without this, the argument that N_gt1 ≥ 1 at termination would break.

---

### Candidate technique(s)

- **p-adic valuation + Euclidean algorithm on valuations**: the central technique. The operation is a Euclidean step on each prime's valuation coordinate; the gcd of the coordinate multiset is invariant.
- **Lexicographic monovariant**: (product, N_gt1) or (total Ω-count, N_gt1) for termination.
- **Invariants & monovariants** (KB entry directly applicable).

---

### Cheap-kill candidates

- **Parity alone**: does not work (the operation is not a parity-type operation).
- **Ordinary gcd of the board**: NOT preserved (as shown by [2,3] → [1,6]).
- **Product as sole monovariant**: insufficient (stays constant for gcd=1 moves). Must pair with N_gt1.
- **Sum of all a_i**: not monotone — can increase (e.g., (2,3) → (1,6), sum goes from 5 to 7).

---

### Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics section): the core proof method.
- **p-adic valuation** (Number Theory section): v_p notation, gcd on valuations.
- **Divisor analysis** (Number Theory section): gcd(k,0)=k, gcd structure.
- **General Proof Methods: Invariant/monovariant**: template for part (b).
- **Problem-Solving Heuristics: Solve simpler case first**: check small boards ([2,3], [4,6,10]) to build confidence.

---

### Analogous past problems (cruxes)

1. **aimo-0324** (NT, invariants-and-monovariants): Board game where the squarefree part is a monovariant. Crux: assign a number-theoretic function (squarefree part) to board positions and show it's one-sided monotone. Analogous because it uses a multiplicative number-theoretic quantity as a game invariant. Less analogous because it's a 2-player game with a single number, not a multiset of numbers with a gcd/lcm operation.

2. **aimo-0236** (combinatorics, invariants-and-monovariants): Board game where 2-adic valuations of board entries are key. Crux: the total sum of 2-adic valuations is a monovariant when the additive constant has higher valuation. Analogous in using p-adic valuations as the "state" of a board game. The phase structure (valuation-based classification) is similar in spirit to our D_p invariant.

3. No problem in the corpus directly uses the "gcd of valuation multiset is preserved by Euclidean subtraction step" idea — this specific crux move appears not to be in the database. The closest analogies are the two above.

---

### Prior progress
None — workspace empty (round 1, no approaches tried yet).

### Dead ends (do not retry)
None tried yet.

### Small-case / intuition notes (conjectures verified computationally)

- Conjecture (verified): D_p = gcd(v_p(a_1),...,v_p(a_n)) is invariant for all primes p, all initial boards. Confirmed on boards [2,3], [4,6,10], [12,18,30,45,60] across all random game plays.
- Conjecture (verified): All game plays on the same board reach the SAME terminal state {M, 1, 1, ..., 1} where M = Π_p p^{D_p}. Verified for multiple boards.
- Conjecture (verified): M ≠ ordinary gcd of the board in general (e.g., [2,3]: M=6, gcd=1; [4,6]: M=6, gcd=2).
- The game length varies by choices (10–13 moves for [12,18,30,45,60]) even though terminal M is fixed.
