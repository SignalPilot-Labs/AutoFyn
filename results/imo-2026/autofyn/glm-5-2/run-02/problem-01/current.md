## Status
solved

## Approaches tried
- invariant-first — APPROVE. Complete rigorous proof of (a) and (b). Per-prime exponent invariant g_p = gcd of all v_p-exponents (preserved by subtractive-Euclidean action of the move, including the zero sub-case under gcd(0,k)=k) pins Q = ∏_p p^{g_p} ≥ 2; lexicographic monovariant (W, C) = (Σ Ω, #{>1}) strictly decreases every move over three disjoint cases {g=1}, {m=n}, {g>1 & m≠n}, the last covering g>1 with one exponent =1 (e.g. {4,8},{9,27},{2,4}); termination ⇒ ≤1 entry >1; invariant Q ≥ 2 forbids 0 entries >1; hence exactly one M = Q, choice-independent.
- monovariant-first — APPROVE. Same core argument, led with the (W, C) monovariant and three-case casework (ΔW = −Ω(gcd(m,n)) verified), then the g_p invariant for the all-1s contradiction and M = Q for part (b). Equally rigorous; the two proofs are essentially equivalent in strength.

## Current best
A complete rigorous proof of both parts (a) and (b) of IMO 2026 P1. The terminal value is M = ∏_p p^{g_p}, where g_p = gcd(v_p(a_1), …, v_p(a_2026)) (with gcd(0,k)=k), computed from the initial board. Termination is forced by the lexicographic monovariant (W, C) = (Σ Ω(a_i), #{a_i > 1}), which strictly decreases every move (ΔW = −Ω(gcd(m,n)) ≤ 0, with ΔC = −1 exactly when ΔW = 0, i.e. the coprime case g = 1). The "exactly one" bridge: termination gives ≤ 1 entry > 1; the invariant Q ≥ 2 rules out the all-1s state; hence exactly one, equal to Q.

## Full proof

Let N = 2026, entries a_1, …, a_N initially all > 1. Write Ω(k) for the number of prime factors with multiplicity (Ω(1) = 0, Ω(xy) = Ω(x) + Ω(y) always), and v_p(k) for the p-adic valuation. Use the convention gcd(0, k) = k (so 0 is the identity for gcd, and gcd of a finite nonnegative list is the fold of pairwise gcds, well-defined and terminating).

### Move reduction
A move picks m, n > 1 from distinct places and replaces them with gcd(m, n) and lcm(m, n)/gcd(m, n). Put g := gcd(m, n), m = g·a, n = g·b with gcd(a, b) = 1. By lcm·gcd = m·n (standard identity), lcm/g = m·n/g² = ab. So the new pair is **(g, ab)**, both positive integers (g | lcm since g | m and m | lcm).

### Per-prime exponent action
For each prime p, the touched valuation pair (α, β) = (v_p(m), v_p(n)) becomes (min(α, β), |α − β|), since v_p(gcd) = min, v_p(lcm) = max. This is one subtractive-Euclidean step.

### The invariant g_p and Q
Define g_p := gcd(v_p(a_1), …, v_p(a_N)) (gcd(0, k) = k convention). Under a move the touched pair (α, β) is replaced by (α', β') = (min(α, β), |α − β|) with gcd(α, β) = gcd(α', β') (verified: assume α ≤ β; new pair (α, β − α); common divisors of {α, β} = common divisors of {α, β − α} since each divides b − a iff it divides a and conversely; zero sub-case: (0, β) → (0, β) is identical). Folding over the other unchanged N − 2 valuations, the whole-board g_p is invariant. Hence **Q := ∏_p p^{g_p}** (finite product: only finitely many primes divide the initial entries) is a board invariant. Initially every a_i > 1; pick a_1 and a prime p | a_1, so v_p(a_1) ≥ 1 and g_p ≥ 1, giving a factor p^{g_p} ≥ 2. So **Q ≥ 2** invariantly.

### Monovariant (W, C) and termination
Define W := Σ Ω(a_i), C := #{i : a_i > 1}. For a move with g = gcd(m, n), m = ga, n = gb, gcd(a, b) = 1:
- Old Ω-sum of the pair: 2Ω(g) + Ω(a) + Ω(b).
- New Ω-sum: Ω(g) + Ω(ab) = Ω(g) + Ω(a) + Ω(b) (Ω(ab) = Ω(a) + Ω(b) since a, b coprime).
- So **ΔW = −Ω(g)**.

Three disjoint exhaustive cases:
- (i) g = 1: ΔW = 0; new pair (1, mn), mn > 1; ΔC = −1.
- (ii) m = n (so g = m, a = b = 1): ΔW = −Ω(m) ≤ −1; ΔC = −1.
- (iii) g > 1 and m ≠ n: a ≠ b; with gcd(a, b) = 1 and a ≠ b, not both a, b = 1, so ab > 1; both new entries (g, ab) > 1; ΔC = 0; ΔW = −Ω(g) ≤ −1.

In cases (ii), (iii), W strictly drops; in case (i), W is fixed and C drops by 1. So the lexicographic pair (W, C) strictly decreases in ℕ × {0, …, N} every move. This order is well-founded (W can drop at most W_0 times; C is non-increasing, bounded below by 0, so drops at most N times), so only finitely many moves occur. The process reaches a terminal state.

### Part (a): exactly one entry > 1
A state is terminal iff fewer than two entries are > 1 (entries = 1 cannot be chosen, and the move is otherwise always executable since (g, ab) are valid positive integers). So a terminal state has ≤ 1 entry > 1. If it had 0 entries > 1 (all 1s), then every v_p(a_i) = 0, so g_p = 0 for all p and Q = 1, contradicting Q ≥ 2. Hence the terminal state has exactly one entry > 1; call it M.

### Part (b): M is independent of choices
In the terminal state, the valuations at prime p are {v_p(M), 0, …, 0} (one copy of v_p(M), N − 1 zeros), whose gcd is v_p(M) by gcd(0, k) = k. By invariance, v_p(M) = g_p for every prime p. Hence M = ∏_p p^{v_p(M)} = ∏_p p^{g_p} = Q, which depends only on the initial board. ∎

### Promotable lemmas (reviewer-certified)
- `exponent-euclidean-step` — certified, statement correct and proved sorry-free.
- `exponent-pair-euclidean-invariant` — certified, statement correct and proved sorry-free.
