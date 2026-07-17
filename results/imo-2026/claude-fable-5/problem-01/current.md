# imo-2026-01 — tracking file (proof-reviewer owned)

## Status
solved

## Approaches tried
- per-prime-gcd-invariant — worked (round 1, APPROVED): conserved quantity g_p = gcd of the
  p-adic valuations of the board at every prime p, plus the lex monovariant (S, C)
  (S = total Omega, C = count of entries > 1) for termination. Yields both parts and the
  explicit formula M = prod_p p^{gcd(v_p(a_1),...,v_p(a_2026))}. Verified adversarially:
  key algebra re-derived from scratch, 400 random boards × 3 runs each, strict lex descent at
  every move, terminal value always matched the formula.
- newman-confluence — worked (round 1, APPROVED): independent second complete proof by abstract
  rewriting — monovariant N = 2027·P + C for termination, prime-support persistence for (a),
  explicit integer-level local-confluence joins (overlap case via gcd(m,n,k) pull-down +
  pair-collapse, with the join identity gcd(|α−β|, |min(α,β)−γ|) = gcd(|α−β|, |α−γ|)), and
  Newman's lemma proved inline by strong induction on N. Establishes uniqueness of the whole
  terminal multiset without computing M. Join identity re-verified on 5000 random triples.

## Current best
Both parts (a) and (b) fully proved (two independent complete proofs). The terminal value is
M = prod_p p^{g_p} with g_p = gcd(v_p(a_1), ..., v_p(a_2026)).

## Full proof

(Primary proof: approach `per-prime-gcd-invariant`, reviewer-verified round 1. An independent
second complete proof via local confluence and Newman's lemma is in
`approaches/newman-confluence.md`, also reviewer-verified.)

Throughout, the *board* is the multiset of 2026 integers currently written, in fixed positions
(a move replaces the two chosen entries in their places, so the board always has exactly 2026
entries). We write v_p(x) for the p-adic valuation of a positive integer x, i.e. the largest
e >= 0 with p^e | x; so v_p(1) = 0 for every prime p, and for each fixed x we have v_p(x) = 0 for
all but finitely many primes p. We use throughout the **Fundamental Theorem of Arithmetic**
(unique prime factorization; knowledge_base.md, Number Theory): every positive integer x
satisfies x = prod_p p^{v_p(x)}, the product taken over all primes, with all but finitely many
exponents zero; consequently, for positive integers x, y:

- x | y if and only if v_p(x) <= v_p(y) for every prime p, and
- x = y if and only if v_p(x) = v_p(y) for every prime p.

The overall strategy is the standard **invariant/monovariant method** (knowledge_base.md:
"Invariants & monovariants", Combinatorics; "Invariant / monovariant", General Proof Methods):
a strictly decreasing quantity forces termination, and an exactly conserved quantity pins down
the terminal state.

### Step 0. The moves are well defined and the board consists of positive integers.

Initially all entries are integers greater than 1, in particular positive. Suppose all entries
are positive integers before a move on entries m > 1, n > 1. The outputs are g := gcd(m,n) and
L/g where L := lcm(m,n). We have g >= 1. Moreover g | m and m | L (by definition of lcm, L is a
common multiple of m and n), so g | L and L/g is a positive integer. Hence after the move all
entries are again positive integers. By induction on the number of moves, every board arising in
the process consists of 2026 positive integers. (Entries equal to 1 can and do appear; the rules
only forbid *choosing* an entry equal to 1.)

### Lemma 1 (valuations of gcd and lcm, and of a move).

*For positive integers m, n and any prime p, with a := v_p(m), b := v_p(n):*

1. *v_p(gcd(m,n)) = min(a, b);*
2. *v_p(lcm(m,n)) = max(a, b);*
3. *v_p(lcm(m,n)/gcd(m,n)) = max(a,b) - min(a,b) = |a - b|.*

**Proof.** (1) Let d := prod_p p^{min(v_p(m), v_p(n))} (a finite product, since all but finitely
many exponents vanish). By the divisibility criterion above, d | m and d | n, so d is a common
divisor. Conversely, if e | m and e | n, then for every prime p we have v_p(e) <= v_p(m) and
v_p(e) <= v_p(n), hence v_p(e) <= min(v_p(m), v_p(n)) = v_p(d), so e | d. Thus d is the greatest
common divisor: gcd(m,n) = d, and v_p(gcd(m,n)) = min(a,b).

(2) Symmetrically, let l := prod_p p^{max(v_p(m), v_p(n))}. Then m | l and n | l, so l is a
common multiple; and if m | f and n | f then v_p(f) >= max(v_p(m), v_p(n)) = v_p(l) for all p,
so l | f. Thus lcm(m,n) = l and v_p(lcm(m,n)) = max(a,b).

(3) Since gcd(m,n) | lcm(m,n) (Step 0), the quotient is a positive integer and valuations
subtract: v_p(lcm(m,n)/gcd(m,n)) = v_p(lcm(m,n)) - v_p(gcd(m,n)) = max(a,b) - min(a,b). Finally
max(a,b) - min(a,b) = |a - b|: if a >= b this is a - b = |a-b|, and if a < b it is
b - a = |a-b|. ∎

So in exponent language: a move on entries with p-valuations (a, b) replaces them, at every
prime p simultaneously, by (min(a,b), |a - b|).

### Part (a): termination, and the shape of the terminal board.

Define, for the current board (x_1, ..., x_2026):

- S := sum_{i=1}^{2026} Omega(x_i), where Omega(x) := sum_p v_p(x) is the number of prime
  factors of x counted with multiplicity (a finite sum; Omega(1) = 0, and Omega(x) >= 1 for
  x > 1 since x > 1 has at least one prime factor by the Fundamental Theorem of Arithmetic);
- C := #{ i : x_i > 1 }.

Both S and C are nonnegative integers, and C <= 2026.

**Lemma 2 (strict lex descent).** *Every move strictly decreases the pair (S, C) in the
lexicographic order on N x N: either S strictly decreases, or S stays equal and C strictly
decreases.*

**Proof.** Consider a move on entries m > 1, n > 1, with outputs g = gcd(m,n) and
q = lcm(m,n)/gcd(m,n). All other entries are untouched, so the changes in S and C come only
from replacing the pair (m, n) by (g, q).

*Change in S.* Fix a prime p and set a := v_p(m), b := v_p(n). By Lemma 1 the p-part of the
touched pair's contribution to S changes from a + b to min(a,b) + |a - b|. Writing
a + b = min(a,b) + max(a,b) and |a - b| = max(a,b) - min(a,b), the new contribution is
min(a,b) + max(a,b) - min(a,b) = max(a,b), so the change at p is
max(a,b) - (min(a,b) + max(a,b)) = -min(a,b). Summing over all primes (a finite sum),

  Delta S = - sum_p min(v_p(m), v_p(n)) = - Omega(gcd(m,n))  (using Lemma 1(1)).

Hence Delta S <= 0 always, and Delta S < 0 if and only if gcd(m,n) > 1 (since Omega(x) >= 1 for
x > 1 and Omega(1) = 0).

*Change in C.* The move removes two entries that are > 1 (m and n) and inserts two entries
(g and q), of which at most two are > 1. Hence C cannot increase at any move: C_new <= C_old.

Now split into two exhaustive, disjoint cases according to gcd(m,n).

**Case 1: gcd(m,n) > 1** (this includes the case m = n, where gcd(m,m) = m > 1, with outputs
(m, 1)). Then Delta S = -Omega(gcd(m,n)) <= -1, so S strictly decreases; since S is the first
lex coordinate, (S, C) strictly lex-decreases regardless of how C moves (and C does not
increase in any case, as shown).

**Case 2: gcd(m,n) = 1.** Then Delta S = -Omega(1) = 0, so S is unchanged. The outputs are
g = 1 and q = lcm(m,n)/1 = mn > 1 (as m, n > 1). So the two removed entries were both > 1 and
exactly one inserted entry is > 1: C decreases by exactly 1. Hence S is equal and C strictly
decreases, again a strict lex decrease.

In both cases (S, C) strictly decreases lexicographically. ∎

**Lemma 3 (well-foundedness of lex order on N x N).** *There is no infinite strictly
lex-decreasing sequence (S_0, C_0) > (S_1, C_1) > ... in N x N.*

**Proof.** Suppose such an infinite sequence existed. The first coordinates satisfy
S_0 >= S_1 >= ... (in a lex decrease the first coordinate never increases), a non-increasing
sequence of nonnegative integers, so it is eventually constant: there is K with S_k = S_K for
all k >= K. For k >= K, the lex decreases (S_k, C_k) > (S_{k+1}, C_{k+1}) with equal first
coordinates force C_K > C_{K+1} > C_{K+2} > ..., an infinite strictly decreasing sequence of
nonnegative integers — impossible. ∎

**Termination.** By Lemma 2, the boards after 0, 1, 2, ... moves give a strictly lex-decreasing
sequence of pairs in N x N; by Lemma 3 this sequence cannot be infinite. Hence, regardless of
choices, only finitely many moves occur: the process reaches a board on which no move is
possible.

**Terminal shape (at most one entry > 1).** A move is possible exactly when the board contains
two entries, in different places, each greater than 1 — the rules impose no other restriction
on the choice. ("He continues while possible": the process stops precisely at a board admitting
no move.) Hence the terminal board has at most one entry greater than 1, i.e. C <= 1; by Step 0
all its entries are positive integers, so all entries except possibly one are equal to 1.

It remains to rule out the all-ones terminal board (C = 0); we do this with the exact invariant
below, which also proves part (b).

### The exact invariant.

**Conventions on gcd of a multiset of nonnegative integers.** Recall that every integer divides
0. For a finite multiset T of nonnegative integers, if T contains a positive element, the set of
common divisors of T is a nonempty finite set of positive-or-negative integers bounded by that
positive element, and we define gcd(T) as its largest element (so gcd(T) >= 1, since 1 is always
a common divisor). If all elements of T are 0, every positive integer is a common divisor and we
set gcd(T) := 0. With these conventions, gcd(T) = 0 if and only if all elements of T are 0; and
in all cases the set of common divisors of T is exactly the set of divisors of gcd(T) — for the
all-zero multiset because every integer divides 0 = gcd(T), and otherwise by the classical
characterization proved as follows: if d = gcd(T) > 0 and e is a common divisor of T, then so is
lcm(d, e) — indeed each t in T is a common multiple of d and e, hence a multiple of lcm(d, e)
(by the defining minimality of lcm as established in Lemma 1(2), every common multiple of d and
e is divisible by lcm(d, e)) — so lcm(d, e) <= d by maximality of d, while d | lcm(d, e) forces
lcm(d, e) = d, i.e. e | d. Conversely any divisor of d divides every element of T.

**Definition.** For a prime p and a board B = (x_1, ..., x_2026), let

  g_p(B) := gcd{ v_p(x_1), ..., v_p(x_2026) }  (multiset gcd with the conventions above).

**Lemma 4 (Euclidean subtraction identity, all cases).** *For nonnegative integers a, b, the
pairs {a, b} and {min(a,b), |a - b|} have the same set of common divisors; in particular
gcd(a, b) = gcd(min(a,b), |a - b|).*

**Proof.** By symmetry assume a >= b, so min(a,b) = b and |a - b| = a - b. If d | a and d | b,
then d | (a - b) (a difference of multiples of d) and d | b. Conversely, if d | b and
d | (a - b), then d | (b + (a - b)) = a and d | b. So the common-divisor sets coincide. This
argument uses nothing about positivity and is valid in all four exponent cases: a = b > 0
(then the second pair is (a, 0), and d | a, d | 0 iff d | a, d | a); a != b both positive;
exactly one of a, b zero (say b = 0: the second pair is (0, a), same divisor conditions); and
a = b = 0 (both pairs are (0,0)). Equal common-divisor sets give equal gcds under our
conventions (both the all-zero case, where both gcds are 0, and the case of a positive element,
where both gcds are the largest common divisor). ∎

**Lemma 5 (one-move invariance of g_p).** *For every prime p, a single move does not change
g_p of the board.*

**Proof.** Fix p. The move touches two positions, changing their valuations from (a, b) to
(min(a,b), |a - b|) by Lemma 1; the other 2024 positions are untouched. Let R be the multiset of
valuations of the untouched positions. An integer d is a common divisor of the multiset
R ∪ {a, b} if and only if d divides every element of R and d is a common divisor of {a, b};
by Lemma 4 the latter is equivalent to d being a common divisor of {min(a,b), |a-b|}. Hence
R ∪ {a, b} and R ∪ {min(a,b), |a-b|} have the same set of common divisors, and therefore the
same gcd (same reasoning as at the end of Lemma 4: in the all-zero case both gcds are 0 — note
the two multisets are all-zero simultaneously, since a = b = 0 iff min(a,b) = |a-b| = 0 — and
otherwise both gcds are the largest element of the common set of common divisors). So
g_p(board) is unchanged. ∎

**Corollary (invariance along the whole process).** *Let B_0 be the initial board and B_k the
board after k moves (any choices). Then for every prime p and every k >= 0,
g_p(B_k) = g_p(B_0).*

**Proof.** Induction on k. Base k = 0: trivial. Step: assume g_p(B_k) = g_p(B_0); the (k+1)-st
move turns B_k into B_{k+1}, and Lemma 5 gives g_p(B_{k+1}) = g_p(B_k) = g_p(B_0). ∎

### Part (a), completed: exactly one entry > 1 remains.

We showed the process terminates after finitely many moves at a board B* with at most one entry
greater than 1. Suppose, for contradiction, that all entries of B* equal 1. The initial board
contains a_1 > 1, which by the Fundamental Theorem of Arithmetic has a prime factor p, so
v_p(a_1) >= 1. Thus the initial valuation multiset at p contains a positive element, so
g_p(B_0) >= 1 by our conventions. But if B* is all ones, every valuation on B* is v_p(1) = 0,
so g_p(B*) = gcd(0, ..., 0) = 0. This contradicts the Corollary, which gives
g_p(B*) = g_p(B_0) >= 1. Hence B* is not all ones, so it has exactly one entry M > 1, and the
other 2025 entries equal 1. This proves part (a). ∎

### Part (b): M is independent of the choices.

Let B_0 = (a_1, ..., a_2026) be the initial board, and let B* be any terminal board reached by
any sequence of choices; by part (a), B* consists of one entry M > 1 and 2025 entries equal
to 1. Fix a prime p. The valuation multiset of B* at p is {v_p(M), 0, 0, ..., 0} (2025 zeros).
Its gcd is v_p(M): if v_p(M) = 0 this is the all-zero multiset with gcd 0 = v_p(M); if
v_p(M) > 0, the common divisors of {v_p(M), 0, ..., 0} are exactly the divisors of v_p(M)
(every integer divides 0), the largest of which is v_p(M). Hence g_p(B*) = v_p(M), and by the
Corollary,

  v_p(M) = g_p(B*) = g_p(B_0) = gcd( v_p(a_1), ..., v_p(a_2026) )   for every prime p.

Only finitely many primes divide a_1 · ... · a_2026, and for any other prime p all v_p(a_i) = 0,
so g_p(B_0) = 0; thus all but finitely many exponents below vanish and the product is finite.
By the Fundamental Theorem of Arithmetic, a positive integer is determined by its valuations:

  M = prod_p p^{v_p(M)} = prod_p p^{ gcd(v_p(a_1), ..., v_p(a_2026)) }.

The right-hand side depends only on the initial board B_0, not on any of the choices made.
Therefore every sequence of choices terminates with the same integer M. This proves part (b). ∎
