# Approach: prime-gcd-invariant

## Status
solved

## Approaches tried
- (round 1) Skeleton opened by proof-outliner; not yet built.
- (round 1, build) Filled the skeleton into a complete prose proof of both parts. Termination via the strict monovariant W = N + Σ Ω; "exactly one" via Lemma 3 (a move never outputs two 1s) plus the terminal condition N ≤ 1; part (b) via the per-prime invariant g_p = gcd of the exponent multiset, preserved by the subtractive-Euclid identity, read off at the terminal board. All six gaps of the skeleton closed; every case settled — worked.

## Current best
Complete proof of (a) and (b) below. The terminal value is M = ∏_p p^{g_p}, where g_p is the gcd of the 2026 exponents v_p(x_i) of the initial board. No open gaps.

## Route (one paragraph)
The consensus route. Work per prime: a move (m,n) → (gcd(m,n), lcm(m,n)/gcd(m,n)) acts on each prime's exponent pair (a,b) as the subtractive-Euclid step (a,b) → (min(a,b), |a−b|). Part (a): termination by the strict monovariant W = N + T where N = #{entries > 1} and T = Σᵢ Ω(xᵢ); "exactly one" because a move never outputs two 1s, so N (starting at 2026) drops by at most 1 per move and can never reach 0. Part (b): for each prime p the quantity g_p = gcd of the multiset of exponents {v_p(x₁),…,v_p(x₂₀₂₆)} is invariant by the Euclid identity gcd(a,b) = gcd(min(a,b), |a−b|); at the terminal board {M,1,…,1} we read off v_p(M) = g_p, so M = ∏_p p^{g_p} is determined by the initial board. (Knowledge base: "Invariant / monovariant" and "Casework / exhaustion" under General Proof Methods; "Divisor analysis: gcd structure" under Number Theory; "Infinite descent / well-ordering" under Induction in General Proof Methods.)

## Full proof

### Setup and conventions

The board is a tuple of 2026 positive integers occupying 2026 places; initially every entry is > 1. A **move** chooses two places holding entries m > 1 and n > 1 (the two places are distinct; the values m and n may be equal) and replaces those two entries by gcd(m,n) and lcm(m,n)/gcd(m,n). Every move replaces two entries by two entries, so the board always has exactly 2026 entries.

We will use throughout the **Fundamental Theorem of Arithmetic** (unique factorization): every integer x ≥ 1 factors uniquely as x = ∏_p p^{v_p(x)} over primes p, where v_p(x) ≥ 0 and v_p(x) = 0 for all but finitely many p. Consequently:

- (V1) v_p(xy) = v_p(x) + v_p(y) for all x, y ≥ 1 and all primes p.
- (V2) For x, y ≥ 1: x | y if and only if v_p(x) ≤ v_p(y) for every prime p. (If x | y, write y = xz and use (V1); conversely, z := ∏_p p^{v_p(y)−v_p(x)} is a positive integer with xz = y.)
- (V3) x = 1 if and only if v_p(x) = 0 for every prime p.
- (V4) x = y if and only if v_p(x) = v_p(y) for every prime p (uniqueness of the factorization).

Define Ω(x) := Σ_p v_p(x), the number of prime factors of x counted with multiplicity. The sum is finite by unique factorization. By (V3), Ω(x) = 0 iff x = 1, and Ω(x) ≥ 1 for x > 1. By (V1), Ω(xy) = Ω(x) + Ω(y).

**gcd conventions (stated once, used throughout).** For a finite multiset S of *nonnegative* integers, define gcd(S) as the unique integer d ≥ 0 such that

  for every integer e ≥ 1: (e | s for all s ∈ S) ⟺ e | d.  (★)

*Existence.* If every element of S is 0, take d = 0: every e divides 0, and every e divides every element (all are 0), so (★) holds. Otherwise let L = { Σ_{s∈S} c_s s : c_s ∈ ℤ } be the set of integer linear combinations of S; L contains a positive integer (some s > 0), so let d be the least positive element of L. Then d divides each s ∈ S: by the division algorithm s = qd + r with 0 ≤ r < d, and r = s − qd ∈ L, so by minimality of d (r is a nonnegative element of L smaller than d, and every positive element of L is ≥ d) we get r = 0. And every common divisor e of S divides every element of L, in particular d. Both directions of (★) follow. *Uniqueness.* Suppose d and d′ both satisfy (★). Case 1: some element s ∈ S is positive. Then d ≠ 0: if d = 0, every e ≥ 1 divides d = 0, so by (★) (direction ⇐) every e ≥ 1 is a common divisor of S, but e = s + 1 does not divide s > 0 — contradiction. Likewise d′ ≠ 0. Since d | d, (★) for d (direction ⇐, e = d) shows d divides every element of S; then (★) for d′ (direction ⇒, e = d) gives d | d′. Symmetrically d′ | d, and two positive integers each dividing the other are equal (d ≤ d′ ≤ d). Case 2: every element of S is 0. Then every e ≥ 1 is a common divisor of S, so by (★) (direction ⇒) every e ≥ 1 divides d; if d were positive, e = d + 1 would not divide it, so d = 0, and likewise d′ = 0. Hence d = d′ in all cases.

In particular gcd(a, 0) = a and gcd(0, 0) = 0, and:

- (G1) **(Zeros are inert.)** If S contains a positive element together with any number of zeros, gcd(S) = gcd(S \ {one 0}) — indeed every integer divides 0, so removing or adding zeros does not change the set of common divisors, hence not the gcd by (★). More specifically, gcd(a, 0, 0, …, 0) = a for a ≥ 0.
- (G2) **(Associativity/fold.)** For any finite multiset R of nonnegative integers and a, b ≥ 0: gcd(R ∪ {a, b}) = gcd(R ∪ {gcd(a,b)}). *Proof.* An integer e ≥ 1 is a common divisor of R ∪ {a,b} iff it divides every element of R and divides both a and b, which by (★) (applied to the pair {a,b}) happens iff it divides every element of R and divides gcd(a,b), i.e. iff it is a common divisor of R ∪ {gcd(a,b)}. The two multisets have the same common divisors, so by (★)-uniqueness the same gcd. ∎

### Step 1 — Move anatomy (the valuation formulas)

**Lemma 1.** Let m, n ≥ 1 and let p be a prime; write a = v_p(m), b = v_p(n). Then:

(i) v_p(gcd(m,n)) = min(a, b);
(ii) v_p(lcm(m,n)) = max(a, b);
(iii) gcd(m,n) divides lcm(m,n), the quotient lcm(m,n)/gcd(m,n) is a positive integer, and v_p(lcm(m,n)/gcd(m,n)) = max(a,b) − min(a,b) = |a − b|.

*Proof.* (i) Let g := ∏_p p^{min(v_p(m), v_p(n))}, a finite product (only primes dividing mn have a positive exponent), so g is a positive integer. By (V2), g | m and g | n, since min(v_p(m), v_p(n)) ≤ v_p(m) and ≤ v_p(n) for every p. Conversely, if d ≥ 1 divides both m and n, then by (V2) v_p(d) ≤ v_p(m) and v_p(d) ≤ v_p(n), hence v_p(d) ≤ min(v_p(m), v_p(n)) for every p, so d | g by (V2). Thus g is a common divisor divisible by every common divisor; in particular g is the greatest common divisor, and v_p(gcd(m,n)) = v_p(g) = min(a,b) by construction and (V4).

(ii) Symmetrically, let ℓ := ∏_p p^{max(v_p(m), v_p(n))} (again a finite product, hence a positive integer). By (V2), m | ℓ and n | ℓ; and every common multiple c ≥ 1 of m and n satisfies v_p(c) ≥ max(v_p(m), v_p(n)) for all p by (V2), hence ℓ | c. So ℓ = lcm(m,n) and v_p(lcm(m,n)) = max(a,b).

(iii) Since min(v_p(m), v_p(n)) ≤ max(v_p(m), v_p(n)) for every p, (V2) with (i) and (ii) gives gcd(m,n) | lcm(m,n), so q := lcm(m,n)/gcd(m,n) is a positive integer. From gcd(m,n) · q = lcm(m,n) and (V1), v_p(q) = v_p(lcm) − v_p(gcd) = max(a,b) − min(a,b). Finally max(a,b) − min(a,b) = |a − b|: if a ≥ b this reads a − b = |a − b|, and if a < b it reads b − a = |a − b|. ∎

**Consequence (one global move, all primes at once).** A single move replaces the pair of entries (m, n) by (gcd(m,n), lcm(m,n)/gcd(m,n)); by Lemma 1, for *every* prime p simultaneously, the pair of p-exponents (a, b) = (v_p(m), v_p(n)) at the two chosen places becomes (min(a,b), |a − b|), and the exponents at all other places are unchanged. We emphasize: the move is a single global operation whose only legality condition is m > 1 and n > 1; we never perform a "move for one prime" — the per-prime statements below are identities satisfied by every prime under each one global move.

We also record the elementary identity, used repeatedly:

- (E) min(a,b) + |a − b| = max(a,b) for all integers a, b ≥ 0. (If a ≥ b: b + (a − b) = a = max. If a < b: a + (b − a) = b = max.)

### Step 2 — Two output lemmas

**Lemma 2 (when the second output is 1).** For m, n ≥ 1: lcm(m,n)/gcd(m,n) = 1 if and only if m = n.

*Proof.* By (V3), lcm(m,n)/gcd(m,n) = 1 iff v_p(lcm/gcd) = 0 for every prime p, iff (Lemma 1(iii)) |v_p(m) − v_p(n)| = 0 for every p, iff v_p(m) = v_p(n) for every p, iff m = n by (V4). ∎

**Lemma 3 (a move never outputs two 1s).** Let m, n > 1 and let the outputs be u = gcd(m,n) and w = lcm(m,n)/gcd(m,n). Then at most one of u, w equals 1. Precisely, exactly one of the following disjoint, exhaustive cases holds:

- **Case A (m = n):** then u = gcd(m,m) = m > 1 and w = 1 (Lemma 2). Outputs: (m, 1) — exactly one output is 1.
- **Case B (gcd(m,n) = 1, which forces m ≠ n):** if m = n then gcd(m,n) = m > 1, a contradiction, so indeed m ≠ n. Here u = 1, and lcm(m,n) = mn/gcd(m,n) = mn (the identity gcd(m,n)·lcm(m,n) = mn holds by Lemma 1(i),(ii), (V1), (V4) and min(a,b) + max(a,b) = a + b for every prime), so w = mn/1 = mn ≥ 2·2 = 4 > 1. Outputs: (1, mn) — exactly one output is 1.
- **Case C (gcd(m,n) > 1 and m ≠ n):** then u = gcd(m,n) > 1 by hypothesis, and w > 1 by Lemma 2 (w = 1 would force m = n). Outputs: both > 1 — no output is 1.

*Exhaustiveness and disjointness.* If m = n we are in Case A (and gcd = m > 1, so not in Case B; the condition m ≠ n excludes A from B and C). If m ≠ n, exactly one of gcd(m,n) = 1 (Case B) and gcd(m,n) > 1 (Case C) holds, since gcd(m,n) ≥ 1 always. In every case at most one output equals 1, and both outputs are positive integers (Lemma 1(iii)). ∎

### Step 3 — Termination (part (a), first half)

For a board B = (x₁, …, x₂₀₂₆) define

  N(B) := #{ i : xᵢ > 1 },  T(B) := Σᵢ Ω(xᵢ),  W(B) := N(B) + T(B).

All three are nonnegative integers (each xᵢ ≥ 1 always: initially all entries exceed 1, and both outputs of a move are positive integers by Lemma 1(iii); so Ω(xᵢ) ≥ 0 is defined).

**Legality.** A move is possible if and only if N(B) ≥ 2: a move needs two distinct places holding entries > 1, and conversely any two such places admit the move. (The board always has 2026 places, so "two different places" is never obstructed by board size.)

**Lemma 4 (ΔT = −Ω(gcd(m,n))).** A move on entries (m, n) changes T by exactly −Ω(gcd(m,n)).

*Proof.* Only the two chosen entries change, so ΔT = Ω(u) + Ω(w) − Ω(m) − Ω(n) with u = gcd(m,n), w = lcm(m,n)/gcd(m,n). For each prime p, with a = v_p(m), b = v_p(n), Lemma 1 gives v_p(u) + v_p(w) = min(a,b) + |a − b| = max(a,b) by (E), while v_p(m) + v_p(n) = a + b = min(a,b) + max(a,b). Hence per prime the exponent sum drops by exactly min(a,b) = v_p(gcd(m,n)) (Lemma 1(i)). Summing over all primes (a finite sum: only primes dividing mn contribute a nonzero term to any of these valuations):

  ΔT = Σ_p [max(a,b) − (a+b)] = −Σ_p min(a,b) = −Ω(gcd(m,n)). ∎

**Lemma 5 (W strictly decreases on every move).** Every legal move decreases W by at least 1.

*Proof.* By the case split of Lemma 3 (disjoint and exhaustive for any legal move, since legality requires m, n > 1):

- **Case A (m = n):** outputs (m, 1). The two chosen places held two entries > 1 and now hold one entry > 1 (namely m) and one entry 1; other places unchanged; so ΔN = −1. By Lemma 4, ΔT = −Ω(gcd(m,m)) = −Ω(m) ≤ −1 since m > 1. Hence ΔW ≤ −2.
- **Case B (gcd(m,n) = 1, m ≠ n):** outputs (1, mn) with mn > 1. Again two entries > 1 became one entry > 1 and one entry 1, so ΔN = −1. By Lemma 4, ΔT = −Ω(1) = 0. Hence ΔW = −1.
- **Case C (gcd(m,n) > 1, m ≠ n):** both outputs are > 1 (Lemma 3, Case C), so the count of entries > 1 among the two chosen places stays 2 and ΔN = 0. By Lemma 4, ΔT = −Ω(gcd(m,n)) ≤ −1 since gcd(m,n) > 1. Hence ΔW ≤ −1.

In every case ΔW ≤ −1. ∎

**Termination.** Along any play, the values of W form a strictly decreasing sequence of nonnegative integers (Lemma 5). By the well-ordering of the nonnegative integers, no infinite strictly decreasing sequence of nonnegative integers exists (knowledge base: "Infinite descent" under Induction, General Proof Methods). Hence every play makes at most W(B₀) moves and stops after finitely many moves, where B₀ is the initial board. ∎(termination)

### Step 4 — Exactly one entry > 1 at the end (part (a), second half)

**N never reaches 0.** Initially N(B₀) = 2026 ≥ 1. Consider any move, performed from a board with N ≥ 2 (legality). The two chosen entries are > 1; by Lemma 3, at most one of the two outputs equals 1, so at least one output is > 1; entries at the other 2024 places are unchanged. Hence among the two chosen places, the count of entries > 1 goes from 2 to at least 1, so N_after ≥ N_before − 1 ≥ 1. By induction along the play, N ≥ 1 at every board ever reached.

**Stopping means N ≤ 1.** Confucius moves while a move is possible, and a move is possible iff N ≥ 2. So the play stops exactly at a board with N ≤ 1 — and by Step 3 it does stop, after finitely many moves.

**Conclusion of part (a).** At the terminal board, N ≤ 1 (stopping condition) and N ≥ 1 (never reaches 0), so N = 1: exactly one entry, call it M, is greater than 1, and the other 2025 entries — being positive integers not exceeding 1 — all equal 1. This holds regardless of the choices made. ∎(a)

### Step 5 — The invariant (engine of part (b))

For each prime p and each board B = (x₁, …, x₂₀₂₆), let E_p(B) := { v_p(x₁), …, v_p(x₂₀₂₆) } (a multiset of 2026 nonnegative integers) and

  g_p(B) := gcd(E_p(B)),

with the conventions of the Setup (in particular gcd(a,0) = a, gcd(0,…,0) = 0).

**Lemma 6 (subtractive Euclid identity, with zero cases).** For all integers a, b ≥ 0: gcd(a, b) = gcd(min(a,b), |a − b|).

*Proof.* Both sides are symmetric in a and b (gcd is symmetric by (★); min and |a − b| are symmetric), so assume WLOG a ≥ b. Then min(a,b) = b and |a − b| = a − b, and the claim reads gcd(a, b) = gcd(b, a − b). By (★)-uniqueness it suffices to show the pairs {a, b} and {b, a − b} have the same common divisors. Let e ≥ 1. If e | a and e | b, then e | (a − b) (difference of multiples of e), so e is a common divisor of {b, a − b}. Conversely, if e | b and e | (a − b), then e | (a − b) + b = a, so e is a common divisor of {a, b}. The divisor argument above did not assume a > b > 0, so the zero cases are already covered; for concreteness: if b = 0 (so a ≥ b automatically), the claim reads gcd(a, 0) = gcd(0, a − 0) = gcd(0, a), true since gcd is symmetric and both sides equal a; if a = b, the claim reads gcd(a, a) = gcd(a, 0), and both sides equal a (every e divides 0, so the common divisors of {a, a} and of {a, 0} are exactly the divisors of a). ∎

**Lemma 7 (g_p is invariant under every move).** For every prime p, every legal move leaves g_p unchanged.

*Proof.* Fix a prime p. The move replaces entries m, n (at two places) by gcd(m,n) and lcm(m,n)/gcd(m,n), and leaves the other 2024 entries untouched. Write a = v_p(m), b = v_p(n), and let R be the multiset of p-exponents of the 2024 untouched entries. Before the move, E_p = R ∪ {a, b}; after the move, by Lemma 1, E_p = R ∪ {min(a,b), |a − b|}. Then

  gcd(R ∪ {a, b})
  = gcd(R ∪ {gcd(a, b)})            (fold, (G2))
  = gcd(R ∪ {gcd(min(a,b), |a − b|)})   (Lemma 6)
  = gcd(R ∪ {min(a,b), |a − b|})       (fold, (G2), read backwards).

So g_p(before) = g_p(after). This is an identity holding for *every* prime p under the *one* global move; no per-prime legality is used (the move's only condition, m, n > 1, is global). ∎

### Step 6 — Reading off M (part (b))

Let B₀ = (x₁, …, x₂₀₂₆) be the initial board and consider any complete play, ending (by part (a)) at a terminal board B* whose entries are M > 1 together with 2025 copies of 1.

**Terminal exponents.** For each prime p, the exponent multiset of B* is E_p(B*) = { v_p(M), 0, 0, …, 0 } (2025 zeros, since v_p(1) = 0 by (V3)). By (G1) (zeros are inert), g_p(B*) = gcd(v_p(M), 0, …, 0) = v_p(M). (This is correct also when v_p(M) = 0: then all entries are 0 and the gcd is 0 by convention.)

**Applying the invariant.** By Lemma 7 applied to each move of the play in turn (a finite induction along the play), g_p(B*) = g_p(B₀) for every prime p. Hence

  v_p(M) = g_p(B₀)  for every prime p.  (†)

**Only finitely many primes matter.** If a prime p divides none of x₁, …, x₂₀₂₆, then v_p(xᵢ) = 0 for all i, so g_p(B₀) = gcd(0, …, 0) = 0 and, by (†), v_p(M) = 0. The initial entries have finitely many prime divisors in total (each xᵢ has finitely many, and there are 2026 of them), so g_p(B₀) > 0 for only finitely many primes p.

**The value of M.** By unique factorization and (†),

  M = ∏_p p^{v_p(M)} = ∏_p p^{g_p(B₀)},

a finite product depending only on the initial board B₀ — not on the sequence of choices. Since every complete play ends with its unique entry > 1 equal to this same number, the value of M does not depend on the choices. ∎(b)

**Consistency check (no circularity).** Part (a) was proved in Steps 3–4 without using Steps 5–6; part (b) uses part (a) only for the *shape* of the terminal board. As a sanity check, the formula independently confirms M > 1: pick any prime q dividing x₁ (x₁ > 1 has a prime divisor). Then v_q(x₁) ≥ 1, so the multiset E_q(B₀) contains the positive element s := v_q(x₁). Its gcd g_q(B₀) is then a positive integer: g_q(B₀) = 0 would mean, by (★), that every e ≥ 1 (all of which divide 0) is a common divisor of E_q(B₀), but e = s + 1 does not divide s > 0. So g_q(B₀) ≥ 1 and M ≥ q^{g_q(B₀)} ≥ q ≥ 2 > 1, consistent with part (a).

**Worked verification (small instance of the formula).** For a 3-entry analogue with initial board (12, 18, 10): the exponents of 2 are (2, 1, 1), gcd = 1; of 3: (1, 2, 0), gcd = 1; of 5: (0, 0, 1), gcd = 1; so the formula predicts M = 2·3·5 = 30 for every play. One concrete full play: (12, 18, 10) → move on (12, 18) [gcd 6, lcm/gcd 36/6 = 6] → (6, 6, 10) → move on (6, 10) [gcd 2, lcm/gcd 30/2 = 15] → (6, 2, 15) → move on (6, 2) [gcd 2, lcm/gcd 6/2 = 3] → (2, 3, 15) → move on (2, 3) [gcd 1, lcm/gcd 6] → (1, 6, 15) → move on (6, 15) [gcd 3, lcm/gcd 30/3 = 10] → (1, 3, 10) → move on (3, 10) [gcd 1, lcm/gcd 30] → (1, 1, 30): terminal with M = 30 ✓. The invariant is visible along the way, e.g. at (6, 2, 15): p = 2 exponents (1, 1, 0), gcd 1; p = 3: (1, 0, 1), gcd 1; p = 5: (0, 0, 1), gcd 1. This numeric check illustrates the mechanism; the proof above does not rely on it.

∎

## Promotable lemmas

- **move-anatomy** (proposed at `results/imo-2026-01/lemmas/move-anatomy.md`, uncertified): for m, n > 1 and every prime p, the move (m,n) → (gcd(m,n), lcm(m,n)/gcd(m,n)) sends the exponent pair (a,b) = (v_p(m), v_p(n)) to (min(a,b), |a−b|); lcm/gcd = 1 ⇔ m = n; a move never outputs two 1s (three-case analysis A/B/C). Proved in full in Steps 1–2 above.
- **multiset-gcd-invariance** (proposed at `results/imo-2026-01/lemmas/multiset-gcd-invariance.md`, uncertified): the gcd of a finite multiset of nonnegative integers (with gcd(0,…,0)=0) is characterized by its common-divisor set, satisfies the fold rule gcd(R ∪ {a,b}) = gcd(R ∪ {gcd(a,b)}), and gcd(a,b) = gcd(min(a,b), |a−b|) for all a, b ≥ 0; hence the per-prime exponent-multiset gcd is invariant under the move. Proved in full in Setup + Step 5 above.

## Open gaps (builder's list)
None. All six gaps of the round-1 skeleton are closed in the Full proof.

## Cases to cover
Move cases A (m = n), B (coprime, m ≠ n), C (gcd > 1, m ≠ n) — settled in Lemmas 3 and 5, shown disjoint and exhaustive; exponent cases a = b, b = 0, a,b > 0 — settled inside Lemma 6 (the divisor argument covers them uniformly, and the zero cases are spelled out).

## Watch out for
- The m,n > 1 legality couples primes: moves are global; the per-prime statements (Lemmas 1, 7) are identities under each global move. Stated explicitly after Lemma 1 and inside Lemma 7.
- "Exactly one", not "at most one": Step 4 proves both N ≤ 1 (stopping) and N ≥ 1 (Lemma 3 walk).
- gcd conventions with 0: stated once in the Setup via the characterization (★); (G1)/(G2) proved from it.
