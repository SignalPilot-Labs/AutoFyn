# Approach: omega-count-monovariant

## Status
solved

## Overall route (one-line)
Prove (a) termination + "exactly one M>1" with the single integer monovariant
**W = (sum of Omega over all entries) + (count of entries > 1)** via a clean
3-case analysis of a move; prove (b) separately with the per-prime invariant
d_p = gcd of p-adic valuations. This is the likely-intended, most elementary route.

## Setup / notation
- Board = multiset of N = 2026 positive integers, all initially > 1. A move picks
  two entries m>1, n>1 from different places and replaces them by gcd(m,n) and
  lcm(m,n)/gcd(m,n).
- Omega(k) = number of prime factors of k with multiplicity, Omega(1)=0.
- v_p(k) = p-adic valuation of k (the exponent of p in k), for k a positive integer.

## Approaches tried
- Integer monovariant W = sum Omega + count for (a), per-prime gcd invariant for
  (b) — **worked**; full proof below, all six flagged gaps closed.

## Current best
Complete proof of both parts (see Full proof).

## Full proof

Throughout, "the board" is a multiset of N = 2026 positive integers occupying N
labelled places; a move replaces the contents of two places holding values m>1 and
n>1 by g := gcd(m,n) and h := lcm(m,n)/gcd(m,n). Since gcd(m,n) and lcm(m,n) are
positive integers and gcd(m,n) divides lcm(m,n), both g and h are positive
integers; hence **every entry of the board is always a positive integer ≥ 1**, and
the number of places stays N. Confucius makes moves until none is possible.

We use the technique **Invariants & monovariants** (`knowledge_base.md`,
"Invariants & monovariants": a quantity monotone across moves proves termination;
a preserved quantity constrains the outcome).

---

### 0. Number-theoretic preliminaries

We repeatedly use the **Fundamental Theorem of Arithmetic (FTA)**: every integer
≥ 1 has a unique factorization as a product of prime powers. Consequently, for
each prime p the valuation v_p(k) (exponent of p in k) is well defined, v_p(1)=0,
and v_p is additive: v_p(kl) = v_p(k) + v_p(l).

**Lemma 0.1 (valuations of gcd, lcm, and the two outputs).**
For positive integers m,n and every prime p, writing α = v_p(m), β = v_p(n):
1. v_p(gcd(m,n)) = min(α,β);
2. v_p(lcm(m,n)) = max(α,β);
3. gcd(m,n)·lcm(m,n) = mn;
4. v_p(h) = |α − β|, where h = lcm(m,n)/gcd(m,n).

*Proof.* (1) An integer d ≥ 1 divides both m and n iff, for every prime q,
v_q(d) ≤ v_q(m) and v_q(d) ≤ v_q(n) (by FTA, divisibility is per-prime:
d | m ⟺ v_q(d) ≤ v_q(m) for all q). Thus the common divisors of m,n are exactly
the d with v_q(d) ≤ min(v_q m, v_q n) for all q. The largest such d is
∏_q q^{min(v_q m, v_q n)}, so gcd(m,n) = ∏_q q^{min(v_q m, v_q n)}, giving
v_p(gcd(m,n)) = min(α,β).

(2) Dually, an integer M ≥ 1 is a common multiple of m,n iff v_q(M) ≥ max(v_q m,
v_q n) for all q; the least such M is ∏_q q^{max}, so v_p(lcm(m,n)) = max(α,β).

(3) For every prime p, v_p(gcd·lcm) = min(α,β) + max(α,β) = α + β = v_p(mn).
Since two positive integers with equal p-valuations for all p are equal (FTA), we
get gcd(m,n)·lcm(m,n) = mn.

(4) gcd(m,n) divides lcm(m,n) (by (1),(2): min ≤ max for every prime), so h is a
positive integer with gcd(m,n)·h = lcm(m,n); applying v_p and additivity,
min(α,β) + v_p(h) = max(α,β), hence v_p(h) = max(α,β) − min(α,β) = |α − β|. ∎

We also record the explicit form of the outputs. Let g = gcd(m,n) and write
m = g·a, n = g·b. Then gcd(a,b) = 1 (a common factor of a,b would enlarge g), and
by Lemma 0.1(3), lcm(m,n) = mn/g = g·a·b, so h = lcm/g = a·b. Thus **the two
outputs are g = gcd(m,n) and h = ab**, where m = ga, n = gb, gcd(a,b) = 1.

**Lemma 0.2 (gcd of non-negative integers).** Define, for non-negative integers,
gcd as the largest positive integer dividing all arguments, with the conventions
gcd(0,0) = 0 and gcd(k,0) = gcd(0,k) = k for k ≥ 1. Then:
1. (Universal property) For non-negative integers a,b and any integer d ≥ 1:
   d | gcd(a,b) ⟺ (d | a and d | b).
2. (Associativity) gcd(gcd(a,b),c) = gcd(a,gcd(b,c)); consequently the gcd of a
   finite list is independent of the order and grouping of its members, so we may
   write gcd(a_1,…,a_k) unambiguously.
3. (List universal property) For d ≥ 1: d | gcd(a_1,…,a_k) ⟺ d | a_i for all i.
4. gcd(a_1,…,a_k) = 0 ⟺ a_i = 0 for all i; otherwise gcd(a_1,…,a_k) ≥ 1.

*Proof.* (1) If d | gcd(a,b) then, since gcd(a,b) | a and gcd(a,b) | b, we get
d | a and d | b. Conversely suppose d | a and d | b. If a = b = 0 then
gcd(a,b) = 0 and d | 0 trivially. Otherwise, by **Bézout's identity** (a
consequence of the Euclidean algorithm) there are integers x,y with
ax + by = gcd(a,b); then d | ax + by = gcd(a,b).

(2) By (1), an integer d ≥ 1 divides gcd(gcd(a,b),c) iff d | gcd(a,b) and d | c,
iff d | a, d | b, d | c. The same characterization holds for gcd(a,gcd(b,c)). Two
non-negative integers with exactly the same set of positive divisors are equal
(each divides the other, hence they are equal; if the divisor set is that of 0,
both are 0). Hence the two groupings are equal, and by induction the gcd of a list
is independent of order and grouping.

(3) Immediate from (1) by induction on k using (2).

(4) If all a_i = 0 the gcd is 0 by convention. If some a_j ≥ 1, then 1 is a common
divisor and every common divisor divides a_j, so it lies in {1,…,a_j}; the largest
common divisor is therefore a positive integer, i.e. ≥ 1. ∎

**Lemma 0.3 (Euclidean step).** For all non-negative integers a,b,
gcd(min(a,b), |a−b|) = gcd(a,b).

*Proof.* Both sides are symmetric in a,b (gcd, min, and |·| are), so assume
a ≥ b ≥ 0. Then min(a,b) = b and |a−b| = a − b, and we must show
gcd(b, a−b) = gcd(a,b). By Lemma 0.2(1) it suffices to show that (a,b) and
(b, a−b) have the same common divisors. If d | a and d | b, then d | (a − b), so d
is a common divisor of (b, a−b). Conversely, if d | b and d | (a−b), then
d | ((a−b) + b) = a, so d is a common divisor of (a,b). Thus the common-divisor
sets coincide; as in Lemma 0.2(2), equal common-divisor sets force
gcd(b, a−b) = gcd(a,b). (Edge cases are included: if a = b then
gcd(a,0) = a = gcd(a,a); if b = 0 then gcd(0,a) = a = gcd(a,0).) ∎

---

### Part (a): termination and exactly one survivor

**A move is possible iff at least two entries exceed 1.** A move requires two
places holding values > 1. If two or more entries are > 1, pick two such places
(they are different places): a move is available. If at most one entry is > 1,
there is no pair of places both holding values > 1, so no move is possible. Hence
**a state is terminal (no move possible) iff at most one entry is > 1.**

#### The monovariant W

Define, for a board (x_1,…,x_N),
```
    W = Σ_{i=1}^{N} Omega(x_i)  +  #{ i : x_i > 1 }.
```
Both summands are non-negative integers (Omega ≥ 0, a count ≥ 0), so **W is a
non-negative integer**.

**Claim.** Every legal move strictly decreases W (by at least 1).

Consider a move on places holding m > 1 and n > 1, with outputs g = gcd(m,n) and
h = ab (notation of §0: m = ga, n = gb, gcd(a,b) = 1). Only these two places
change, so
```
  ΔW = [Omega(g) + Omega(h) − Omega(m) − Omega(n)]  +  [Δ(count of entries > 1)].
```

First we compute the Omega-part exactly. For every prime p, with α = v_p(m),
β = v_p(n), Lemma 0.1 gives v_p(g) = min(α,β) and v_p(h) = |α−β|, so
```
  v_p(g) + v_p(h) = min(α,β) + |α−β| = max(α,β).
```
Summing over all primes (Omega(k) = Σ_p v_p(k)):
```
  Omega(g) + Omega(h) = Σ_p max(α,β)
                      = Σ_p (α + β) − Σ_p min(α,β)
                      = [Omega(m) + Omega(n)] − Omega(g),
```
because Σ_p min(v_p m, v_p n) = Omega(gcd(m,n)) = Omega(g) by Lemma 0.1(1). Hence
```
  Omega(g) + Omega(h) − Omega(m) − Omega(n) = −Omega(g).            (★)
```
So the Omega-part of ΔW equals −Omega(g) ≤ 0. Now the three exhaustive, disjoint
cases on the move; recall a,b ≥ 1 are positive integers with gcd(a,b) = 1.

- **Case 1: g = 1** (m,n coprime). Then a = m, b = n, and the outputs are g = 1 and
  h = ab = mn. By (★) the Omega-part is −Omega(1) = 0. Count: before the move both
  m,n > 1 (contributing 2); after, g = 1 is not > 1, while h = mn > 1 (as m,n > 1),
  contributing 1. So the count drops by exactly 1. Therefore ΔW = 0 + (−1) = −1.

- **Case 2: g > 1 and m = n.** From m = ga, n = gb and m = n we get a = b; with
  gcd(a,b) = 1 this forces a = b = 1, so m = n = g and h = ab = 1. By (★) the
  Omega-part is −Omega(g) ≤ −1 (since g > 1 implies Omega(g) ≥ 1). Count: before,
  both m,n > 1 (2); after, g > 1 (1) and h = 1 is not > 1 (0), so the count drops by
  1. Therefore ΔW = −Omega(g) − 1 ≤ −2.

- **Case 3: g > 1 and m ≠ n.** From m = ga, n = gb and m ≠ n we get a ≠ b. Since
  a,b ≥ 1 with a ≠ b, not both can equal 1, so max(a,b) ≥ 2, whence h = ab ≥ 2 > 1.
  Thus both outputs g > 1 and h > 1. Count: before 2 (both > 1), after 2 (both
  g,h > 1), so the count is unchanged. By (★), ΔW = −Omega(g) ≤ −1 (g > 1).

In every case ΔW ≤ −1, proving the Claim.

#### Termination and "at most one"

W is a non-negative integer that strictly decreases at each move, so it can
decrease at most W_initial times. Hence **Confucius makes only finitely many
moves**, and the process reaches a terminal state (no move possible). By the
criterion above, a terminal state has **at most one entry > 1**.

#### The per-prime invariant, and "not zero"

Fix a prime p. For a board (x_1,…,x_N) define
```
  d_p := gcd( v_p(x_1), …, v_p(x_N) ),
```
the gcd of the N non-negative integer valuations (Lemma 0.2). We show **d_p is
invariant under every move.**

A move changes only the two touched places, whose valuations go from (α,β) to
(v_p(g), v_p(h)) = (min(α,β), |α−β|) by Lemma 0.1. Let G be the gcd of the
valuations of the N−2 untouched entries. By associativity (Lemma 0.2(2)),
```
  d_p (before) = gcd( gcd(α, β), G ),
  d_p (after)  = gcd( gcd(min(α,β), |α−β|), G ).
```
By the Euclidean-step Lemma 0.3, gcd(min(α,β),|α−β|) = gcd(α,β). Hence the two
expressions are identical, so d_p is unchanged. This holds for every prime p and
every move; therefore **d_p equals its initial value D_p := gcd(v_p(x_1^{(0)}),…,
v_p(x_N^{(0)}))** (computed on the initial board) at every stage of the process.

Now suppose, for contradiction, that the terminal board were **all 1's** (count of
entries > 1 equal to 0). Then v_p(x_i) = 0 for every i and every prime p, so
d_p = gcd(0,…,0) = 0 for all p, by Lemma 0.2(4). By invariance, D_p = 0 for all p.
But the initial board contains some entry x_1^{(0)} > 1, which by FTA has a prime
factor p_1, i.e. v_{p_1}(x_1^{(0)}) ≥ 1. Then not all valuations feeding D_{p_1}
are zero, so by Lemma 0.2(4), D_{p_1} ≥ 1 > 0 — contradicting D_{p_1} = 0.

Therefore the terminal board is **not** all 1's: at least one entry is ≠ 1, i.e.
(being a positive integer) > 1. Combined with "at most one entry > 1," the
terminal board has **exactly one entry M > 1**, and all others equal 1. This
proves part (a). ∎ (a)

---

### Part (b): the surviving value is forced

By part (a) the process ends with exactly one entry M > 1 and N−1 entries equal to
1. For each prime p, the valuation multiset of the terminal board is
(v_p(M), 0, 0, …, 0), since v_p(1) = 0. Hence, using gcd(k,0)=k and Lemma 0.2,
```
  d_p (terminal) = gcd( v_p(M), 0, …, 0 ) = v_p(M)
```
(the trailing zeros do not change a gcd: gcd(v_p(M),0,…,0) = v_p(M) both when
v_p(M) ≥ 1 and when v_p(M) = 0, giving 0). But d_p is invariant, so it equals the
initial value D_p. Therefore
```
  v_p(M) = D_p   for every prime p.
```
By FTA, M is determined by its valuations:
```
  M = ∏_p p^{D_p},
```
a finite product, since D_p = gcd(v_p(x_1^{(0)}),…,v_p(x_N^{(0)})) > 0 only for
primes p dividing some initial entry, of which there are finitely many (each
D_p = 0 for the rest, contributing a factor p^0 = 1).

The right-hand side ∏_p p^{D_p} depends **only on the initial board** — the D_p are
computed from the starting valuations alone, before any choice is made. Since every
sequence of moves (whatever choices Confucius makes) leaves each d_p invariant and
ends, by part (a), in a state with a single entry M satisfying v_p(M) = D_p for all
p, **every such terminal M equals ∏_p p^{D_p}**. Hence M does not depend on the
choices. Moreover M > 1: as shown in part (a), D_{p_1} ≥ 1 for a prime p_1
dividing some initial entry, so p_1 | M and M ≥ p_1 > 1, consistent with (a). ∎ (b)

---

### Verification of the closed form (consistency check)

The formula M = ∏_p p^{D_p} with D_p = gcd of the initial p-valuations is exactly
what a numerical simulation over thousands of random boards and random legal
play-outs produces: every play-out terminates with a single entry > 1, equal
across all play-outs of a given board, and equal to ∏_p p^{D_p}. (This is a check,
not part of the proof; the proof above is self-contained.)

∎

## Promotable lemmas

- **euclid-step-invariant.** For all non-negative integers a,b,
  gcd(min(a,b),|a−b|) = gcd(a,b) (conventions gcd(0,0)=0, gcd(k,0)=k). Proved in
  full as Lemma 0.3 above via the common-divisor-set argument. Together with the
  valuation action v_p(gcd(m,n)) = min(v_p m, v_p n),
  v_p(lcm(m,n)/gcd(m,n)) = |v_p m − v_p n| (Lemma 0.1), this yields invariance of
  d_p = gcd of the p-valuation multiset under a move. Reusable by valuation-gcd and
  product-count-monovariant for part (b). Candidate cache file:
  `results/imo-2026-01/lemmas/euclid-step-invariant.md`.
- **omega-gcd-lcm identity.** Omega(gcd(m,n)) + Omega(lcm(m,n)/gcd(m,n))
  = Omega(m) + Omega(n) − Omega(gcd(m,n)) (Lemma 0.1 + identity (★)). This is the
  engine of the monovariant drop; reusable by valuation-gcd.
