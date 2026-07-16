# Approach: valuation-gcd (unified per-prime framework)

## Status
solved

## Overall route (one-line)
Reduce the ENTIRE problem to one per-prime picture and derive both parts inside
it: for each prime p the board's p-valuation multiset evolves by the subtractive
Euclidean step (a,b) -> (min(a,b),|a-b|). From this single framework, (a)
termination comes from the global monovariant T = sum Omega(x_i) + #{x_i>1}, and
(b) comes from d_p = gcd(v_p multiset) being invariant.

## Setup / notation
- Board of N = 2026 entries, each an integer > 1, written with multiplicity as a
  multiset X = {x_1, ..., x_N}.
- A **move** picks two entries m > 1 and n > 1 from different positions and
  replaces them by gcd(m,n) and lcm(m,n)/gcd(m,n).
- For a positive integer x and a prime p, v_p(x) is the p-adic valuation: the
  exponent of p in the prime factorization of x (Fundamental Theorem of
  Arithmetic). Omega(x) = sum_p v_p(x) is the number of prime factors of x counted
  with multiplicity; Omega(x) = 0 iff x = 1, and Omega(x) >= 1 iff x > 1.
- For each prime p, the board induces the multiset E_p = { v_p(x_i) : i = 1..N }
  of non-negative integers.

## Approaches tried
- Per-prime Euclidean-step framework: monovariant T = sum Omega + count for (a),
  per-prime gcd invariant d_p for (b) — WORKED, full proof below.

## Current best
Complete proof of both (a) and (b); see Full proof.

## Full proof

Throughout, N = 2026 and the board is the multiset X = {x_1, ..., x_N}. We use the
**Fundamental Theorem of Arithmetic** (every integer > 1 factors uniquely into
primes), which underlies the valuation function v_p and the identities below. For
the monovariant/invariant technique see `knowledge_base.md`, entry
"Invariants & monovariants".

### Conventions for gcd

We extend gcd to all non-negative integers by the standard conventions
gcd(0,0) = 0 and gcd(0,k) = k for k >= 1. With these, gcd(a,b) is well-defined for
all a,b >= 0, gcd is **commutative** and **associative**, and for any a,
gcd(a,0) = a. The gcd of a finite multiset {a_1, ..., a_N} of non-negative
integers is gcd(a_1, ..., a_N), independent of the order by commutativity and
associativity; it equals 0 iff every a_i = 0.

### Lemma 0 (valuation of gcd and of lcm/gcd)

For positive integers m, n and any prime p, write a = v_p(m), b = v_p(n). Then
1. v_p(gcd(m,n)) = min(a,b);
2. v_p(lcm(m,n)) = max(a,b);
3. v_p(lcm(m,n)/gcd(m,n)) = max(a,b) - min(a,b) = |a - b|.

**Proof.** By the Fundamental Theorem of Arithmetic, m = prod_p p^{v_p(m)} and
n = prod_p p^{v_p(n)}, the products over all primes with all but finitely many
exponents zero. The gcd is the largest integer dividing both; a prime power p^k
divides m iff k <= v_p(m) and divides n iff k <= v_p(n), so the largest power of p
dividing both is p^{min(a,b)}. Since distinct primes contribute independently,
gcd(m,n) = prod_p p^{min(v_p(m),v_p(n))}, giving (1). Dually, lcm(m,n) is the
smallest positive integer that both m and n divide; m | p^k-part requires
k >= v_p(m) and similarly for n, so the exponent of p in lcm is max(a,b), giving
(2). For (3): since gcd(m,n) | lcm(m,n) (as min(a,b) <= max(a,b) at every prime),
lcm(m,n)/gcd(m,n) is a positive integer, and taking v_p is additive/subtractive
under multiplication/division (v_p(uv) = v_p(u) + v_p(v)), so
v_p(lcm/gcd) = max(a,b) - min(a,b). Finally max(a,b) - min(a,b) = |a - b|: if
a >= b this is a - b = |a-b|, and if a < b it is b - a = |a-b|. This proves (3).
∎ (Lemma 0)

**Effect of a move on the valuation multisets.** Fix a move that replaces entries
m (at position i) and n (at position j) by g := gcd(m,n) and h := lcm(m,n)/g. For
every prime p, set a = v_p(m) = v_p(x_i) and b = v_p(n) = v_p(x_j). By Lemma 0 the
new entries at positions i, j have p-valuations v_p(g) = min(a,b) and
v_p(h) = |a - b|. All other positions are unchanged. Hence in E_p the pair of
values {a, b} at positions i, j is replaced by {min(a,b), |a-b|}, and every other
value of E_p is unchanged. **This holds simultaneously for all primes p**: a
single board move performs the substitution (a,b) -> (min(a,b),|a-b|) in E_p for
every p at once. In particular, for a prime p dividing neither m nor n we have
a = b = 0, so (min,|diff|) = (0,0): the two valuations are unaffected, as expected
(such p divides neither g nor h either).

### Lemma 1 (arithmetic of the Euclidean step)

For all non-negative integers a, b:
(i) min(a,b) + |a - b| = max(a,b);
(ii) min(a,b) <= max(a,b) <= a + b, with equality max = a + b iff min(a,b) = 0.

**Proof.** (i): If a >= b then min = b, |a-b| = a - b, and b + (a-b) = a = max. If
a < b, min = a, |a-b| = b - a, and a + (b-a) = b = max. (ii): min(a,b) <= max(a,b)
is immediate; and a + b = min(a,b) + max(a,b) always (the two summands are a and b
in some order), so max(a,b) = a + b - min(a,b) <= a + b, with equality iff
min(a,b) = 0. ∎ (Lemma 1)

### Lemma 2 (key gcd identity — the subtractive Euclidean invariant)

For all non-negative integers a, b (with the conventions above),
gcd(min(a,b), |a - b|) = gcd(a, b).

**Proof.** By symmetry assume a >= b, so min(a,b) = b and |a-b| = a - b; we must
show gcd(b, a - b) = gcd(a, b). This is the **subtractive form of the Euclidean
algorithm**. We prove it by showing the two pairs (b, a-b) and (a, b) have exactly
the same set of common divisors.

Let D be a non-negative integer. If D | a and D | b, then D | (a - b) (a divisor
of two integers divides their difference), so D | b and D | (a - b). Conversely if
D | b and D | (a - b), then D | (b + (a - b)) = a, so D | a and D | b. Hence the
common divisors of {a, b} are exactly the common divisors of {b, a - b}. Two pairs
with identical common-divisor sets have identical greatest common divisors (the
gcd is the maximum of the common-divisor set; when both a = b = 0 all of Z divides
both and gcd = 0 by convention, and then also b = 0, a - b = 0, gcd = 0, so the
identity holds there too). Therefore gcd(b, a - b) = gcd(a, b).

Edge cases are covered by the same argument but we record them explicitly:
- a = b: LHS = gcd(a, 0) = a = gcd(a, a) = RHS.
- b = 0 (a >= 0): min = 0, |a-b| = a, LHS = gcd(0, a) = a = gcd(a, 0) = RHS.
- a = b = 0: LHS = gcd(0,0) = 0 = RHS.
∎ (Lemma 2)

---

## Part (a): the process terminates with exactly one entry > 1

### The monovariant T

Define, for a board X,
  T(X) = sum_{i=1}^{N} Omega(x_i) + C(X),   where C(X) = #{ i : x_i > 1 }.
Since each Omega(x_i) >= 0 and C(X) >= 0, T(X) is a **non-negative integer**.

We show every legal move strictly decreases T by at least 1. Consider a move
replacing m and n (both > 1) by g = gcd(m,n) and h = lcm(m,n)/g. Only the two
touched entries change, so the change in T is
  Delta T = [Omega(g) + Omega(h) - Omega(m) - Omega(n)]
            + [ (1_{g>1} + 1_{h>1}) - (1_{m>1} + 1_{n>1}) ],
where 1_{condition} is 1 if the condition holds and 0 otherwise. Since m > 1 and
n > 1, the last bracket equals (1_{g>1} + 1_{h>1}) - 2.

First compute the Omega-change. Omega(x) = sum_p v_p(x), and by Lemma 0 for every
prime p, v_p(g) = min(a_p, b_p) and v_p(h) = |a_p - b_p| where a_p = v_p(m),
b_p = v_p(n). By Lemma 1(i), for each p:
  v_p(g) + v_p(h) = min(a_p,b_p) + |a_p - b_p| = max(a_p,b_p)
                  = a_p + b_p - min(a_p,b_p) = v_p(m) + v_p(n) - min(a_p,b_p).
Summing over all primes p (finitely many nonzero terms):
  Omega(g) + Omega(h) = Omega(m) + Omega(n) - sum_p min(v_p(m), v_p(n)).
By Lemma 0(1), sum_p min(v_p(m),v_p(n)) = sum_p v_p(g) = Omega(g). Hence
  Omega(g) + Omega(h) - Omega(m) - Omega(n) = - Omega(g).   (*)

So Delta T = -Omega(g) + (1_{g>1} + 1_{h>1}) - 2. We now split into the exhaustive
and disjoint cases determined by g = gcd(m,n).

**Case 1: g = 1 (m, n coprime).** Then Omega(g) = 0 and 1_{g>1} = 0. Also
h = lcm(m,n)/1 = lcm(m,n) = mn (as gcd = 1), and since m,n > 1 we have h = mn > 1,
so 1_{h>1} = 1. Thus
  Delta T = -0 + (0 + 1) - 2 = -1.
T strictly decreases by 1. (Here the Omega-sum is flat, Omega(g)=0 by (*), and the
count drops by 1 because one of the two outputs, g = 1, is no longer > 1.)

**Case 2: g > 1.** Then Omega(g) >= 1 (as g > 1) and 1_{g>1} = 1. The term
1_{h>1} is 0 or 1, so 1_{g>1} + 1_{h>1} - 2 = 1 + 1_{h>1} - 2 = 1_{h>1} - 1 <= 0.
Therefore
  Delta T = -Omega(g) + (1_{h>1} - 1) <= -Omega(g) <= -1.
T strictly decreases by at least 1.

(These two cases are exhaustive since g = gcd(m,n) is either 1 or > 1, and
disjoint. We did not even need to sub-split g > 1 by whether m = n; the bound
Delta T <= -1 holds throughout. For completeness: if m = n then g = m = n and
h = 1, so 1_{h>1} = 0 and Delta T = -Omega(g) <= -1; if m != n with g > 1 then
h may be > 1 or = 1, and in all sub-cases Delta T <= -Omega(g) <= -1.)

**Termination.** T is a non-negative integer that strictly decreases by at least 1
at every move. A strictly decreasing sequence of non-negative integers has length
at most T(X_0) + 1, where X_0 is the initial board. Hence Confucius can make only
finitely many moves; the process reaches a board on which **no move is possible**.
(This is the monovariant/termination technique, `knowledge_base.md` entry
"Invariants & monovariants".)

### The terminal board has exactly one entry > 1

Let X* be a terminal board (no move possible) and C* = C(X*) its count of entries
> 1.

**At most one:** a move only requires two entries that are both > 1. If C* >= 2,
there would be two positions with entries > 1, and a move on them would be legal,
contradicting terminality. Hence C* <= 1.

**Not zero:** we must rule out C* = 0, i.e. all entries equal 1. This is proved in
Part (b) below (via the invariant d_{p_1} >= 1 for a prime p_1 dividing x_1,
combined with the terminal read-off), and the argument there is not circular: the
value M > 1 is forced by an invariant computed from the *initial* board, not from
assuming the terminal count. Concretely, Part (b) establishes that the terminal
board contains an entry equal to M = prod_p p^{d_p} > 1, hence C* >= 1.

Combining C* <= 1 and C* >= 1 gives C* = 1: **exactly one** entry of the terminal
board exceeds 1. Call it M. This proves (a) (modulo the C* >= 1 fact proved next,
which is logically independent of the terminal count). ∎ (part a)

---

## Part (b): M does not depend on the choices

### The invariant d_p

For a board X and prime p, define
  d_p(X) = gcd of the multiset E_p = gcd( v_p(x_1), ..., v_p(x_N) ),
with the gcd conventions above (so d_p(X) = 0 iff p divides none of the x_i).

**Claim: d_p is invariant under every move, for every prime p.**

Consider a move replacing entries at positions i, j (values m, n) by g, h. Fix a
prime p and write a = v_p(m), b = v_p(n). As established after Lemma 0, in E_p only
the two entries at positions i, j change: from {a, b} to {min(a,b), |a-b|}; call
the remaining N-2 valuations (unchanged) the multiset R with r := gcd(R) (r = 0 if
N = 2, i.e. R empty, using gcd of the empty multiset = 0). By associativity and
commutativity of gcd,
  d_p(before) = gcd( R, a, b ) = gcd( r, gcd(a, b) ),
  d_p(after)  = gcd( R, min(a,b), |a-b| ) = gcd( r, gcd(min(a,b), |a-b|) ).
By Lemma 2, gcd(min(a,b), |a-b|) = gcd(a,b). Substituting,
  d_p(after) = gcd( r, gcd(a,b) ) = d_p(before).
Thus d_p is unchanged by the move. Since p was arbitrary, every d_p is invariant.
∎ (Claim)

Because each move preserves every d_p, the value d_p is the **same on the initial
board and on every subsequent board**, including the terminal board. Write d_p for
this common value (a function of the initial board only).

### M > 1 and finiteness of the product

Since x_1 > 1, by the Fundamental Theorem of Arithmetic there is a prime p_1 with
v_{p_1}(x_1) >= 1. Recall d_p = 0 iff every member of E_p is 0 (a gcd of
non-negative integers is 0 exactly when all of them are 0, by our convention).
Since v_{p_1}(x_1) >= 1, not all members of E_{p_1} are zero, so d_{p_1} != 0;
being a non-negative integer, d_{p_1} >= 1. Thus at least one prime has d_p >= 1.

Only finitely many primes have d_p > 0: d_p > 0 forces some v_p(x_i) > 0, i.e. p
divides some initial entry x_i; the finitely many integers x_1, ..., x_N together
have only finitely many prime divisors. Hence
  M := prod_p p^{d_p}
is a product over a finite set of primes, so it is a well-defined positive integer,
and M > 1 because the exponent d_{p_1} >= 1 contributes a factor p_1^{d_{p_1}} >= 2.

This already supplies the missing fact in Part (a): the terminal board cannot be
all 1's. Indeed we now show the single surviving entry equals M.

### Terminal read-off: the survivor is M

By Part (a) the terminal board X* has exactly one entry > 1 — call it M' — and all
other N - 1 entries equal 1. (We may invoke "exactly one" now: Part (a) gave
C* <= 1, and C* >= 1 follows because if C* = 0 then every terminal entry is 1, so
every terminal E_p = {0, ..., 0} and terminal d_p = 0 for all p; but terminal
d_p = initial d_p, contradicting d_{p_1} >= 1. Hence C* = 1.)

For a prime p, the terminal multiset E_p^* consists of v_p(M') together with N - 1
copies of v_p(1) = 0. Therefore
  d_p = d_p(X*) = gcd( v_p(M'), 0, ..., 0 ) = v_p(M'),
using gcd(k, 0) = k repeatedly (and gcd(0,...,0) = 0 = v_p(1) when v_p(M') = 0).
Hence v_p(M') = d_p for every prime p. By the Fundamental Theorem of Arithmetic an
integer is determined by its valuations at all primes, so
  M' = prod_p p^{v_p(M')} = prod_p p^{d_p} = M.

Since each d_p depends only on the initial board (the d_p are invariants), M
depends only on the initial board, not on Confucius's choices. This is precisely
statement (b). ∎

### Summary of the answer
The surviving integer is
  M = prod_p p^{d_p},   d_p = gcd( v_p(x_1), ..., v_p(x_N) ),
the product over all primes p, which is a finite product > 1 determined by the
initial board alone. Both (a) (exactly one survivor) and (b) (its value is
choice-independent) are established. ∎

## Promotable lemmas
- **euclid-step-invariant** (written to `results/imo-2026-01/lemmas/euclid-step-invariant.md`):
  the valuation action v_p(gcd) = min, v_p(lcm/gcd) = |diff| (Lemma 0), the
  arithmetic identity min + |diff| = max (Lemma 1), and the invariant identity
  gcd(min(a,b), |a-b|) = gcd(a,b) (Lemma 2), plus the whole-multiset invariance of
  d_p = gcd(E_p). Reusable by omega-count-monovariant and
  product-count-monovariant.
