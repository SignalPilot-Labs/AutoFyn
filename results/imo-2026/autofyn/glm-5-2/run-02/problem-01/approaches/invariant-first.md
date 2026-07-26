# Approach: invariant-first

- **Slug:** invariant-first
- **Target:** IMO 2026 P1, full claim — (a) the process terminates with exactly one integer M>1 on the board, and (b) M is independent of Confucius's choices.
- **Route / framing:** Invariant-first. Pin the per-prime exponent invariant g_p = gcd of all v_p-exponents (preserved by a subtractive-Euclidean step), and from it derive the terminal value M = ∏ p^{g_p} (with M ≥ 2) BEFORE proving termination. Termination is then attached as the second half: a global lexicographic monovariant (W, C) = (Σ Ω, #{entries > 1}) strictly decreases every move, forcing a terminal state. The bridge to "exactly one" is: termination ⇒ ≤ 1 entry > 1; the invariant M ≥ 2 forbids 0 entries > 1; hence exactly one.

## Status
solved

## Approaches tried
- invariant-first (round 1): per-prime exponent invariant g_p pins M and M ≥ 2 first; lexicographic monovariant (W,C) attached as second half for termination; bridge termination⇒≤1 + Q≥2 forbids 0 ⇒ exactly one. All gaps from the outline-reviewer closed (broadened case partition to {g=1, m=n, g>1 & m≠n}; gcd(0,k)=k convention and (a,0) sub-case; finiteness+Q≥2; lcm/gcd integrality; full ΔW=−Ω(g) derivation; explicit contradiction chain). — COMPLETE, rigorous.

## Current best
Complete rigorous proof of parts (a) and (b). No gaps.

## Full proof

Throughout, `v_p(k)` denotes the p-adic valuation of a positive integer k (with v_p(1)=0), and `Ω(k) := Σ_p v_p(k)` is the number of prime factors of k counted with multiplicity (Ω(1)=0). Both are finitely supported: only primes dividing k contribute nonzero terms. We use the convention **gcd(0, k) = k** (and gcd(0,0)=0); equivalently 0 is the identity element for gcd. This is the standard extension of gcd to nonnegative integers, implemented recursively by gcd(x, 0)=x.

The board has 2026 entries, all initially integers greater than 1. A **move** picks two entries m > 1, n > 1 from distinct places and replaces them by gcd(m, n) and lcm(m, n)/gcd(m, n). Write N = 2026.

---

### Step 1. The move is a per-prime subtractive-Euclidean step on exponent pairs.

Fix a prime p. Let the two chosen entries have p-adic valuations (a, b) (a, b ≥ 0). By the standard p-adic valuation identities
- v_p(gcd(m, n)) = min(v_p(m), v_p(n)) = min(a, b),
- v_p(lcm(m, n)) = max(v_p(m), v_p(n)) = max(a, b),
- hence v_p(lcm(m, n)/gcd(m, n)) = max(a, b) − min(a, b) = |a − b|,

the two new entries carry p-valuations **(min(a, b), |a − b|)**. All other board positions are untouched, so at the prime p the only effect of the move is to replace the exponent pair {a, b} by {min(a, b), |a − b|}. This is exactly one step of the **subtractive Euclidean algorithm**.

(Identity source: the standard rules v_p(gcd) = min, v_p(lcm) = max, which follow directly from the unique-factorization description of gcd and lcm prime-by-prime; see knowledge_base "Invariants & monovariants" for the technique of reducing a move to its per-prime action.)

---

### Step 2. Definition of the per-prime invariant g_p.

For each prime p define

  g_p := gcd{ v_p(a_i) : i = 1, …, N },

the gcd of the multiset of all N p-valuations on the board, using the convention gcd(0, k) = k. This convention makes 0 a neutral element: entries not divisible by p contribute a 0 exponent, and gcd(0, k) = k leaves the running gcd unchanged, so such entries are simply ignored in the gcd. With this convention g_p is a well-defined nonnegative integer for every p (the gcd of a finite list of nonnegative integers is computed recursively, terminating, and gcd(0,…,0)=0). Only primes that divide at least one board entry can have g_p > 0.

(Shared lemma `exponent-euclidean-step` records this convention and the next step's preservation jointly.)

---

### Step 3. g_p is invariant under every move.

A move touches only two board positions; at prime p their exponent pair {a, b} is replaced by {min(a, b), |a − b|} (Step 1). We claim

  gcd(a, b) = gcd(min(a, b), |a − b|),

i.e. the gcd of the two touched exponents is preserved. By symmetry assume a ≤ b, so the new pair is {a, b − a}. Every common divisor of {a, b} divides a and b, hence divides b − a, hence divides both entries of the new pair; conversely every common divisor of {a, b − a} divides a and b − a, hence divides (b − a) + a = b, hence divides both entries of the old pair. The common-divisor sets coincide, so their maxima coincide: **gcd(a, b) = gcd(a, b − a)** (the subtractive Euclidean algorithm identity). Substituting back gives gcd(a, b) = gcd(min(a, b), |a − b|).

Because the two touched exponents have the same gcd before and after the move, and the other N − 2 exponents are literally unchanged, the gcd of the whole multiset of N exponents is unchanged. Hence **g_p is invariant** under every move, for every prime p.

**Zero sub-case (flagged by the outline-reviewer).** If one of the touched exponents is 0, say a = 0 (the entry is not divisible by p), then min(0, b) = 0 and |0 − b| = b, so the new pair is {0, b} — identical to the old pair {0, b}. Trivially gcd(0, b) = b = gcd(0, b) is preserved, consistent with the convention gcd(0, k) = k. The same holds if b = 0 by symmetry, and if a = b = 0 the pair {0, 0} is sent to {0, 0}. So the invariance holds in every sub-case, including when one or both touched entries are not divisible by p.

---

### Step 4. The board invariant Q := ∏_p p^{g_p}.

Define

  Q := ∏_{p prime} p^{g_p}.

This is a finite product: only primes dividing at least one initial board entry can have g_p > 0 (Step 2), and finitely many primes divide the finitely many (N) initial entries, each > 1. By Step 3 every g_p is invariant, so Q is a **board invariant**: its value depends only on the initial board, not on the sequence of moves.

---

### Step 5. Q ≥ 2.

Initially every entry is strictly greater than 1, so each entry has at least one prime divisor; pick any entry x_0 > 1 and any prime p | x_0. Then v_p(x_0) ≥ 1, so g_p = gcd{…, v_p(x_0), …} ≥ 1 (the gcd of a list containing a value ≥ 1 is at least 1, since every common divisor of a set containing a positive integer is at most that integer, and 1 is always a common divisor). Hence the factor p^{g_p} ≥ p^{1} ≥ 2 in the product Q, so **Q ≥ 2**. Combined with Step 4, Q ≥ 2 is an invariant property of every reachable board state.

---

### Step 6. Characterization of a terminal state.

A move is legal iff Confucius can pick two entries m, n > 1 from distinct places. First we confirm the move is always well-defined when it is legal: gcd(m, n) is a positive integer, and lcm(m, n)/gcd(m, n) is a positive integer because gcd(m, n) | lcm(m, n) (indeed gcd(m, n) divides both m and n, hence divides lcm(m, n)). So there is no obstruction to a legal move other than the existence of two entries > 1 in distinct places.

Therefore a state is terminal (no legal move available) iff **fewer than two entries are > 1**, i.e. iff the board has **at most one** entry greater than 1. (Entries equal to 1 cannot be chosen: the move requires m, n > 1.)

---

### Step 7. Termination: the lexicographic monovariant (W, C).

Define, for a board state,

  W := Σ_{i=1}^{N} Ω(a_i)   (total number of prime factors, with multiplicity),
  C := #{ i : a_i > 1 }     (number of entries strictly greater than 1).

Both are nonnegative integers; C ∈ {0, 1, …, N} is bounded, and W is a nonnegative integer. We show the ordered pair (W, C) **strictly decreases in the lexicographic order** with every move. Since ℕ × {0, …, N} is well-founded under lexicographic order (no infinite strictly decreasing chain: W can drop only finitely many times before hitting 0, and within a fixed W the bounded value C can drop only finitely many times), finitely many moves are possible. Hence **the process reaches a terminal state.**

Consider one move on entries m, n > 1. Set g := gcd(m, n), and write m = g·a, n = g·b with gcd(a, b) = 1 (so a, b are coprime positive integers). The two new entries are gcd(m, n) = g and lcm(m, n)/gcd(m, n) = ab (using lcm(m, n)·gcd(m, n) = m·n, so lcm/gcd = m·n/g² = (ga)(gb)/g² = ab).

**Computation of ΔW = −Ω(g).** The Ω-sum of the old pair is
  Ω(m) + Ω(n) = Ω(ga) + Ω(gb) = (Ω(g) + Ω(a)) + (Ω(g) + Ω(b)) = 2Ω(g) + Ω(a) + Ω(b),
using Ω(xy) = Ω(x) + Ω(y) (Ω counts prime factors with multiplicity). The Ω-sum of the new pair is
  Ω(g) + Ω(ab).
Because gcd(a, b) = 1, the prime factorizations of a and b are disjoint, so Ω(ab) = Ω(a) + Ω(b) (no carrying of multiplicities: each prime's exponent in ab is the sum of its exponents in a and b, and at most one of those is nonzero). Hence the new Ω-sum is Ω(g) + Ω(a) + Ω(b), and

  ΔW = (Ω(g) + Ω(a) + Ω(b)) − (2Ω(g) + Ω(a) + Ω(b)) = −Ω(g).

This derivation is valid for every move with m, n > 1, regardless of whether a or b equals 1.

**Three exhaustive, disjoint cases.** Every move with m, n > 1 falls into exactly one of:
  (i)  g = 1 (coprime move),
  (ii) m = n (equal-pair move),
  (iii) g > 1 and m ≠ n (intermediate, broadened to cover g > 1 with one of a, b equal to 1, e.g. {4,8}→{4,2}, {9,27}→{9,3}, {2,4}→{2,2}).

These are disjoint (case (i) has g = 1; cases (ii),(iii) have g > 1; case (ii) has m = n; case (iii) has m ≠ n) and exhaustive (any move has either g = 1 or g > 1; if g > 1 then either m = n or m ≠ n).

  - **Case (i): g = 1.** Then ΔW = −Ω(g) = −Ω(1) = 0. The new entries are 1 (= g) and ab = mn (since g = 1); m, n > 1 ⇒ mn > 1, so the new pair is {1, mn}. Both old entries were > 1 (count 2); among the new entries exactly one (mn) is > 1 (count 1). So ΔC = 1 − 2 = −1. The pair (W, C) goes to (W, C − 1): a strict lexicographic decrease (W unchanged, C drops).

  - **Case (ii): m = n.** Then g = m (and a = b = 1). ΔW = −Ω(g) = −Ω(m) ≤ −1 (since m > 1 ⇒ Ω(m) ≥ 1). Regardless of C's change, W strictly decreases, so (W, C) strictly decreases lexicographically. (For completeness: the new entries are g = m > 1 and ab = 1, so ΔC = 1 − 2 = −1 as well.)

  - **Case (iii): g > 1 and m ≠ n.** Because m ≠ n we have a ≠ b; together with gcd(a, b) = 1 this forces ab > 1 (if ab = 1 then a = b = 1, contradicting a ≠ b). So among the new entries {g, ab}, both are > 1 (g > 1 by hypothesis, ab > 1 just shown), giving count 2; the old pair {m, n} also had both entries > 1, count 2. Hence ΔC = 0. And ΔW = −Ω(g) ≤ −1 (since g > 1 ⇒ Ω(g) ≥ 1), so W strictly decreases and (W, C) strictly decreases lexicographically.

In all three cases (W, C) strictly decreases in lexicographic order. The computation ΔW = −Ω(g) is identical in cases (i)–(iii); what distinguishes them is whether ΔW is strictly negative (cases (ii), (iii), where g > 1) or zero (case (i), where g = 1), and in the zero-ΔW case the secondary coordinate C drops by 1. The broadening of case (iii) to "g > 1 and m ≠ n" (rather than "g > 1, a > 1, b > 1") is exactly what makes the partition exhaustive: it captures the subcase g > 1 with exactly one of a, b equal to 1 (e.g. {4,8}→{4,2} where g = 4, a = 1, b = 2), for which the ΔW = −Ω(g) ≤ −1 and ΔC = 0 conclusion is identical (both new entries g > 1 and ab = b > 1 remain > 1).

Since (W, C) strictly lexicographically decreases at every move and ℕ × {0, …, N} is well-founded under lexicographic order, only finitely many moves can occur; the process must reach a terminal state.

(This is an instance of the **Invariants & monovariants** technique — knowledge_base entry "Invariants & monovariants" / "Invariant / monovariant" in General Proof Methods — combined with integer well-foundedness, the descent principle.)

---

### Step 8. Part (a): exactly one entry > 1.

By Step 7 the process reaches a terminal state. By Step 6 a terminal state has at most one entry > 1. Suppose, for contradiction, that the terminal state has **zero** entries > 1, i.e. every entry equals 1. Then for every prime p, every v_p(a_i) = 0 (since v_p(1) = 0), so g_p = gcd{0, …, 0} = 0 (the gcd of all-zero list under our convention). Hence Q = ∏_p p^{g_p} = ∏_p p^{0} = 1 in this state. But Q is an invariant (Step 4), so Q = 1 in the initial state as well; this contradicts Step 5 (Q ≥ 2 in the initial state, hence in every reachable state). The contradiction rules out zero entries > 1.

Therefore the terminal state has exactly one entry greater than 1; call it M. This proves part (a): the process terminates, and exactly one integer M > 1 remains.

---

### Step 9. Part (b): M is independent of the choices of Confucius.

In the terminal state exactly one entry M > 1 remains; all other N − 1 entries equal 1. For each prime p the multiset of board valuations is {v_p(M), 0, 0, …, 0} (one copy of v_p(M), N − 1 copies of 0). Its gcd is, by the convention gcd(0, k) = k,
  gcd{v_p(M), 0, …, 0} = v_p(M)
(the single nonzero value, with zeros neutral). By invariance (Step 3) this equals g_p, the invariant of the initial board:
  v_p(M) = g_p  for every prime p.

Hence M = ∏_p p^{v_p(M)} = ∏_p p^{g_p} = Q, which by Step 4 depends only on the initial board, not on the sequence of moves. Therefore **M is independent of Confucius's choices.** ∎

---

### Summary of the invariant-first routing

The invariant g_p and the quantity Q = ∏ p^{g_p} (with Q ≥ 2) were established in Steps 1–5 *before* any termination argument; they pin the candidate terminal value M = Q and rule out the all-1s terminal state. The lexicographic monovariant (W, C) is then attached (Steps 6–7) purely to produce a terminal state. The bridge in Step 8 combines them: termination gives ≤ 1 entry > 1; the invariant Q ≥ 2 forbids 0 entries > 1; hence exactly one, equal to Q. Step 9 reads off M = Q.

## Promotable lemmas
- **exponent-pair Euclidean-step preservation of gcd** (lemma file `results/imo-2026-01/lemmas/exponent-euclidean-step.md`): the move sends p-valuation pair {a,b} to {min(a,b),|a−b|} and preserves gcd(a,b) = gcd(min(a,b),|a−b|) by the subtractive Euclidean identity, including the zero sub-case under gcd(0,k)=k. Proved in full in Step 1–3 of this approach and in the lemma file.
