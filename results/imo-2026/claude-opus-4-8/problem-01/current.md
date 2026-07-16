## Status
solved

## Approaches tried
- valuation-gcd — WORKED. Per-prime Euclidean-step framework; termination from
  T = sum Omega + count(>1), uniqueness from d_p = gcd(v_p multiset) invariant.
  APPROVED (round 1).
- omega-count-monovariant — WORKED. Integer monovariant W = sum Omega + count(>1)
  with a clean exhaustive 3-case drop analysis; (b) via d_p invariant. APPROVED
  (round 1). Cleanest self-contained route; adopted as the Full proof below.
- product-count-monovariant — WORKED. Lexicographic (P = board product, C = count>1)
  monovariant with well-foundedness by infinite descent; (b) via the same d_p
  invariant. APPROVED (round 1).

All three are complete, gap-free proofs of both parts. Certified shared lemma:
`lemmas/euclid-step-invariant.md`.

## Current best
Complete proof of both (a) and (b). Key facts, all proven below and independently
verified: v_p(gcd) = min, v_p(lcm/gcd) = |diff|; the subtractive-Euclidean invariant
gcd(min(a,b),|a-b|) = gcd(a,b); a monovariant that strictly drops at every move; and
the per-prime invariant d_p = gcd(v_p(x_1),...,v_p(x_N)), which pins the survivor to
M = prod_p p^{d_p}.

## Full proof

Throughout, N = 2026. The board is a multiset of N positive integers occupying N
labelled places, all initially > 1. A **move** picks two places holding values
m > 1 and n > 1 and replaces them by g := gcd(m,n) and h := lcm(m,n)/gcd(m,n). Since
gcd(m,n) | lcm(m,n), both g and h are positive integers and the board always has N
entries, each >= 1. Confucius moves while a move is possible.

We use the **Fundamental Theorem of Arithmetic (FTA)**: every integer >= 1 factors
uniquely into prime powers; hence for each prime p the valuation v_p(k) (exponent of
p in k) is well defined, v_p(1) = 0, and v_p(kl) = v_p(k) + v_p(l). We also use the
monovariant/invariant technique (`knowledge_base.md`, "Invariants & monovariants").

### gcd conventions

We extend gcd to non-negative integers by gcd(0,0) = 0 and gcd(0,k) = gcd(k,0) = k
for k >= 1. Then gcd is commutative and associative, so gcd(a_1,...,a_k) is well
defined independent of order and grouping; for d >= 1, d | gcd(a_1,...,a_k) iff
d | a_i for all i; and gcd(a_1,...,a_k) = 0 iff every a_i = 0, otherwise it is a
positive integer (the largest common divisor).

*(Justification.* For d >= 1: if not all a_i are 0, pick a_j > 0; by Bezout the gcd
of a list equals the least positive integer combination, so the common divisors of
the list are exactly the divisors of gcd, giving the divisibility characterization.
Associativity: d | gcd(gcd(a,b),c) iff d | a,b,c iff d | gcd(a,gcd(b,c)); two
non-negative integers with identical positive-divisor sets are equal, so the
groupings agree. If all a_i = 0 the value is 0 by convention.)*

### Lemma 0 (valuation action of a move)

For positive integers m, n and a prime p, with a = v_p(m), b = v_p(n):
1. v_p(gcd(m,n)) = min(a,b);
2. v_p(lcm(m,n)) = max(a,b);
3. v_p(h) = |a - b|, where h = lcm(m,n)/gcd(m,n).

**Proof.** By FTA, an integer d >= 1 divides both m and n iff for every prime q,
v_q(d) <= min(v_q(m), v_q(n)); the largest such d is prod_q q^{min}, so
gcd(m,n) = prod_q q^{min(v_q m, v_q n)}, giving (1). Dually the least common multiple
is prod_q q^{max}, giving (2). Since min <= max at every prime, gcd(m,n) | lcm(m,n),
so h is a positive integer with gcd(m,n) * h = lcm(m,n); applying v_p and additivity,
min(a,b) + v_p(h) = max(a,b), hence v_p(h) = max(a,b) - min(a,b) = |a - b| (the larger
minus the smaller). ∎

Consequently, a single move performs, in the multiset E_p = {v_p(x_1),...,v_p(x_N)}
of p-valuations, the substitution (a, b) -> (min(a,b), |a-b|) on the two touched
entries, leaving all others fixed — simultaneously for every prime p.

We also record the explicit output form. Let g = gcd(m,n) and write m = ga, n = gb.
Then gcd(a,b) = 1 (a common factor of a,b would enlarge g). Since
gcd(m,n)*lcm(m,n) = mn (equal p-valuation min+max = a+b at every prime, then FTA),
we get lcm(m,n) = mn/g = g*a*b, so **h = lcm/g = a*b**, with m = ga, n = gb,
gcd(a,b) = 1.

### Lemma 1 (arithmetic identity)

For all non-negative integers a, b: min(a,b) + |a-b| = max(a,b) = a + b - min(a,b).

**Proof.** If a >= b: min = b, |a-b| = a-b, sum = a = max, and a+b-b = a. If a < b,
symmetric. And a + b = min + max always (the two summands are a,b in some order). ∎

### Lemma 2 (subtractive Euclidean invariant)

For all non-negative integers a, b: gcd(min(a,b), |a-b|) = gcd(a,b).

**Proof.** By symmetry assume a >= b, so min = b and |a-b| = a-b; show
gcd(b, a-b) = gcd(a,b). If d | a and d | b then d | (a-b), so d is a common divisor
of {b, a-b}; conversely if d | b and d | (a-b) then d | (b + (a-b)) = a, so d is a
common divisor of {a, b}. The two pairs have identical common-divisor sets, hence
identical gcd. Edge cases: a = b gives gcd(a,0) = a = gcd(a,a); b = 0 gives
gcd(0,a) = a = gcd(a,0); a = b = 0 gives 0 = 0. ∎

---

## Part (a): the process terminates with exactly one entry > 1

**Terminal criterion.** A move needs two places both holding values > 1. If two or
more entries exceed 1, a move exists; if at most one does, no move exists. Hence a
state is **terminal iff at most one entry is > 1**.

### The monovariant W

For a board (x_1,...,x_N) define
  W = sum_{i=1}^N Omega(x_i) + #{ i : x_i > 1 },
where Omega(x) = sum_p v_p(x) (so Omega(x) = 0 iff x = 1). Both summands are
non-negative integers, so W is a non-negative integer.

**Claim: every legal move strictly decreases W by at least 1.**

Consider a move on m > 1, n > 1 with outputs g = gcd(m,n) and h = ab (notation
above: m = ga, n = gb, gcd(a,b) = 1, so a,b >= 1). Only the two touched places
change, so
  Delta W = [Omega(g) + Omega(h) - Omega(m) - Omega(n)] + Delta(count of entries > 1).

Compute the Omega-part exactly. For every prime p, by Lemma 0 and Lemma 1,
v_p(g) + v_p(h) = min(v_p m, v_p n) + |v_p m - v_p n| = max(v_p m, v_p n)
              = v_p(m) + v_p(n) - min(v_p m, v_p n).
Summing over all primes (finitely many nonzero terms) and using
sum_p min(v_p m, v_p n) = Omega(gcd(m,n)) = Omega(g) (Lemma 0(1)):
  Omega(g) + Omega(h) = Omega(m) + Omega(n) - Omega(g),
so
  Omega(g) + Omega(h) - Omega(m) - Omega(n) = -Omega(g).   (*)

Now the three exhaustive, pairwise-disjoint cases determined by g and by m vs n.

**Case 1: g = 1** (m, n coprime). Then a = m, b = n and the outputs are g = 1 and
h = ab = mn > 1 (since m, n > 1). By (*) the Omega-part is -Omega(1) = 0. Count:
before, both m, n > 1 (contributes 2); after, g = 1 is not > 1 while h = mn > 1
(contributes 1); so the count drops by 1. Hence Delta W = 0 + (-1) = -1.

**Case 2: g > 1 and m = n.** Then a = b, and gcd(a,b) = 1 forces a = b = 1, so
m = n = g and h = ab = 1. By (*) the Omega-part is -Omega(g) <= -1 (g > 1 gives
Omega(g) >= 1). Count: before 2; after g > 1 (1) and h = 1 (0), so the count drops
by 1. Hence Delta W = -Omega(g) - 1 <= -2.

**Case 3: g > 1 and m != n.** Then a != b; with a, b >= 1 this gives max(a,b) >= 2,
so h = ab >= 2 > 1, and also g > 1. Both outputs exceed 1. Count: before 2, after 2,
unchanged. By (*), Delta W = -Omega(g) + 0 = -Omega(g) <= -1.

These cases are exhaustive (g = 1, or g > 1 with m = n, or g > 1 with m != n) and
disjoint, and in every case Delta W <= -1. This proves the Claim.

**Termination and "at most one".** W is a non-negative integer strictly decreasing
at every move, so at most W(initial) moves occur. The process reaches a terminal
state, which by the criterion has **at most one** entry > 1.

### The per-prime invariant d_p, and "not zero"

For a prime p and board B define d_p(B) = gcd(v_p(x_1), ..., v_p(x_N)) (gcd
conventions above; d_p = 0 iff p divides no entry).

**d_p is invariant under every move.** A move sends the two touched valuations
(a, b) = (v_p m, v_p n) to (min(a,b), |a-b|) (Lemma 0) and fixes the other N-2. Let
G be the gcd of the untouched valuations. By associativity,
  d_p(before) = gcd(gcd(a,b), G),   d_p(after) = gcd(gcd(min(a,b),|a-b|), G).
By Lemma 2 the inner gcds are equal, so d_p(after) = d_p(before). This holds for
every prime p and every move; hence for every reachable board B_k and the initial
board B_0, d_p(B_k) = d_p(B_0) =: d_p.

**Not zero.** Pick an initial entry x_1 > 1 and a prime p_1 | x_1, so
v_{p_1}(x_1) >= 1. Then d_{p_1} = gcd of a list containing the positive integer
v_{p_1}(x_1) is a positive integer, i.e. d_{p_1} >= 1. Suppose for contradiction the
terminal board were all 1's. Then every terminal valuation is 0, so terminal
d_p = gcd(0,...,0) = 0 for all p, in particular terminal d_{p_1} = 0. But by
invariance terminal d_{p_1} = d_{p_1} >= 1, a contradiction. This crucial fact is
derived from the *initial* board via the invariant, not from assuming the terminal
count, so the argument is not circular.

Therefore the terminal board has at least one entry > 1. Combined with "at most one",
it has **exactly one** entry M > 1, all others equal to 1. This proves Part (a). ∎

---

## Part (b): the surviving value M is determined by the initial board

By Part (a) the terminal board has one entry M > 1 and N-1 entries equal to 1. For
each prime p the terminal valuation multiset is (v_p(M), 0, ..., 0), so, using
gcd(k, 0, ..., 0) = k (valid whether v_p(M) >= 1 or v_p(M) = 0),
  d_p(terminal) = gcd(v_p(M), 0, ..., 0) = v_p(M).
By invariance d_p(terminal) = d_p, hence
  v_p(M) = d_p   for every prime p.
By FTA an integer is determined by its valuations at all primes, so
  M = prod_p p^{d_p},   where d_p = gcd(v_p(x_1),...,v_p(x_N)).
Only finitely many primes have d_p > 0 (namely those dividing some initial entry),
so this is a well-defined positive integer, and M > 1 because d_{p_1} >= 1 gives a
factor p_1^{d_{p_1}} >= 2.

The right-hand side prod_p p^{d_p} is computed from the initial valuations alone and,
by the invariance of every d_p, is unaffected by any move. Confucius's choices never
enter it. Hence every play-out terminates in a single survivor equal to
M = prod_p p^{d_p}, the same value regardless of the choices. This proves Part (b). ∎

### Answer
The surviving integer is M = prod_p p^{d_p} with d_p = gcd(v_p(x_1),...,v_p(x_N)),
a finite product > 1 determined by the initial board alone. Verified numerically:
across thousands of random boards and random play-outs, every run terminates with
exactly one entry > 1, equal to this M across all play-outs of a given board.
