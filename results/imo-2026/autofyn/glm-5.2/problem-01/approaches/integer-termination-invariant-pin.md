# imo-2026-01 — approach `integer-termination-invariant-pin`

Approach: valuation-free termination for part (a) via the pure-integer
lexicographic potential (P, c) (no Ω, no p-adic valuations); the "exactly one
> 1" clause via the radical-support invariant (prime *divisibility* only, still
no valuations); part (b) via the per-prime invariant D_p = gcd of positionwise
p-valuations (valuations invoked only here). The differentiator from
`per-prime-euclidean-invariant` is the part-(a) potential: the plain integer
product P instead of the valuation-sum W = Σ Ω.

## Status
solved

## Approaches tried
- Round 1 build: wrote the complete proof below. Part (a) termination uses the
  pure-integer lex potential (P, c); the "exactly one" clause uses the
  radical-support invariant (no p-adic valuations anywhere in part (a)). Part
  (b) uses the per-prime D_p invariant with the Euclidean identity
  gcd(min(α,β),|α−β|)=gcd(α,β). All lemmas proved from scratch; all cases
  settled; sympy/random sanity-checks pass. Outcome: complete, no gaps.

## Current best
The whole problem (both parts) is proved below.

## Full proof

### Setup and notation

The blackboard holds a multiset of 2026 integers, all initially greater than 1.
A **move** picks two entries m > 1 and n > 1 in *different positions* and
replaces them (in those two positions) by

  g = gcd(m, n)   and   L/g,   where L = lcm(m, n).

Write m = g·x and n = g·y with gcd(x, y) = 1 (the canonical gcd decomposition).
Then

  L = lcm(m, n) = m·n / gcd(m, n) = (g x)(g y)/g = g x y,

so L/g = x y. Hence a move sends the ordered pair of values (m, n) = (g x, g y)
to the pair (g, x y), where gcd(x, y) = 1. This is the form we use throughout.

Let P denote the product of *all* board entries, and let

  c = #{ board entries strictly greater than 1 }.

Both P and c are positive integers (P ≥ 1, c ≥ 0). We order the pair (P, c) in
**lexicographic order** with P primary: (P′, c′) < (P, c) iff P′ < P, or
P′ = P and c′ < c.

---

### Part (a): termination and "exactly one integer M > 1"

#### Lemma 1 (product change).

Under a move on the pair (m, n) = (g x, g y), the product of the two chosen
entries changes from m·n = g² x y to g·(x y) = g x y. The other 2024 entries
are untouched. Therefore the total product changes by

  P_new = P_old / g = P_old / gcd(m, n).

*Proof.* Direct: m·n = (g x)(g y) = g² x y, while the new pair product is
g·(x y) = g x y = (g² x y)/g = (m·n)/g. Dividing the old total product P_old by
m·n and multiplying by g x y gives P_old · (g x y)/(g² x y) = P_old / g. ∎

Consequences:
- If g = gcd(m, n) ≥ 2 (a **non-coprime** move), then P strictly decreases,
  being divided by the integer g ≥ 2. In particular P_new ≤ P_old / 2 < P_old.
- If g = 1 (a **coprime** move, i.e. gcd(m, n) = 1), then P is unchanged.

#### Lemma 2 (count change, coprime case).

If the move is coprime (g = 1), then the new pair is (1, m n), and c drops by
exactly 1.

*Proof.* With g = 1 we have x = m, y = n, and x y = m n. Both m, n > 1
(hypothesis of a move), so m n > 1. The new pair is therefore (1, m n): one
entry equals 1 (contributes 0 to c), the other equals m n > 1 (contributes 1).
Before the move both chosen entries were > 1 (contributing 2 to c); after, they
contribute 1. The other 2024 entries are unchanged. Hence c_new = c_old − 1. ∎

#### Lemma 3 (strict lex decrease of (P, c) every move).

Every move strictly decreases (P, c) in lexicographic order.

*Proof.* Split on g = gcd(m, n).

- **Case g ≥ 2 (non-coprime).** By Lemma 1, P strictly decreases. Hence
  (P_new, c_new) < (P_old, c_old) in lex order regardless of how c changes.
  (The value of c in this case is immaterial for the lex decrease; we record
  for later use that c does not increase: the new pair is (g, x y) with g ≥ 2
  hence g > 1 always, and x y ≥ 1; x y = 1 iff x = y = 1 iff m = n, in which
  case the new pair is (m, 1) and c drops by 1, otherwise x y > 1 and c is
  unchanged. In all sub-cases c is non-increasing, though we do not need this
  for the lex argument.)

- **Case g = 1 (coprime).** By Lemma 1, P is unchanged; by Lemma 2, c drops
  by 1. Hence (P_new, c_new) = (P_old, c_old − 1) < (P_old, c_old) in lex
  order.

These two cases are exhaustive (g is a positive integer, so g ≥ 2 or g = 1).
In both, (P, c) strictly decreases in lex order. ∎

*Edge case m = n.* When m = n, we have g = m ≥ 2 (since m > 1), x = y = 1,
and the move sends (m, m) to (m, 1); this falls under Case g ≥ 2 above (P is
divided by g = m ≥ 2), and additionally c drops by 1. No separate termination
argument is required, but the behavior of c is recorded as stated.

#### Lemma 4 (well-foundedness of ℕ² lex; finite termination).

There is no infinite strictly decreasing chain in ℕ² under lexicographic
order. Consequently the process terminates after finitely many moves.

*Proof.* Suppose (P_1, c_1) > (P_2, c_2) > ··· is a strictly decreasing chain
in ℕ² lex. The P_k are non-negative integers and non-increasing, so they
stabilize: there exists N with P_k = P_N for all k ≥ N. For k ≥ N the strict
lex decrease forces c_k > c_{k+1} strictly (P is now constant, so the
decrease must come from c). But (c_k)_{k ≥ N} is then a strictly decreasing
sequence of non-negative integers, which must be finite — a strictly
decreasing sequence of elements of ℕ has length at most c_N + 1. This
contradicts the assumed infinitude. Hence no infinite strictly decreasing
chain exists.

By Lemma 3 every move strictly decreases (P, c) ∈ ℕ² in lex order; by the
well-foundedness just proved, only finitely many moves can occur. Hence
Confucius must stop after finitely many moves. ∎

#### Lemma 5 (radical-support invariant; no p-adic valuations used).

The set S of prime divisors of the total product P is invariant under every
move.

*Proof.* It suffices to check the two chosen entries, since the other 2024 are
unchanged. Before the move the pair product is m·n = g² x y; after the move
the pair product is g·x y. A prime divides g² x y iff it divides g or x y, and
it divides g·x y iff it divides g or x y; the prime *support* is the same
(squaring g does not change which primes divide it). Hence

  { primes dividing m·n } = { primes dividing g² x y }
                         = { primes dividing g } ∪ { primes dividing x y }
                         = { primes dividing g·x y }
                         = { primes dividing (new pair product) }.

The radical support of P is therefore unchanged. ∎

(Equivalently: lcm(m, n) has the same prime divisors as m·n, and the move
replaces the pair (m, n) by entries whose product is lcm(m, n) = m·n/g; dividing
by g cannot *introduce* a new prime, and the primes of lcm(m, n) are exactly
those of m·n, so the support is preserved.)

#### Lemma 6 (P > 1 forever, hence c ≥ 1 forever).

At every moment (including the terminal state), the total product P exceeds 1,
and therefore at least one board entry exceeds 1, i.e. c ≥ 1.

*Proof.* Initially all 2026 entries exceed 1, so P ≥ 2^{2026} > 1, and S (the
set of prime divisors of P) is nonempty. By Lemma 5, S is invariant, so S is
nonempty at every subsequent moment. A positive integer with a prime divisor is
at least 2, so P > 1 at every moment. If at some moment c = 0 then every entry
is 1 and P = 1, contradicting P > 1. Hence c ≥ 1 at every moment. ∎

#### Lemma 7 (terminal state has c ≤ 1).

When the process stops, at most one entry exceeds 1.

*Proof.* The process stops precisely when no move is possible, i.e. when there
do not exist two entries > 1 in different positions. That is exactly c ≤ 1. ∎

#### Conclusion of part (a).

By Lemma 4 the process terminates. At the terminal state, Lemma 7 gives c ≤ 1
and Lemma 6 gives c ≥ 1, so **c = 1**: exactly one board entry M exceeds 1
(and all others equal 1). This holds regardless of Confucius's choices. ∎

---

### Part (b): M is independent of the choices

For part (b) we now introduce p-adic valuations. For a prime p and a positive
integer a, let v_p(a) be the exponent of p in the prime factorization of a
(so v_p(1) = 0). For the current board (a_1, …, a_{2026}) define, for each
prime p,

  D_p = gcd( v_p(a_1), v_p(a_2), …, v_p(a_{2026}) ),

where we use the convention gcd(x, 0) = x (so gcd of a list containing zeros is
the gcd of the nonzero entries; positions where p does not divide the entry are
invisible). Note gcd(0, 0) = 0 is consistent with this convention, but this
value will never be the one we use.

#### Lemma 8 (the move on p-valuations).

Fix a prime p, and let the two chosen entries have p-valuations α = v_p(m),
β = v_p(n). After the move the two new entries have p-valuations

  v_p(g) = min(α, β),   and   v_p(x y) = v_p(L/g) = |α − β|.

*Proof.* The standard valuation identities (see knowledge base, "Divisor
analysis: gcd structure") give v_p(gcd(m, n)) = min(v_p(m), v_p(n)) = min(α, β)
and v_p(lcm(m, n)) = max(α, β). Since L/g = lcm(m, n)/gcd(m, n), its valuation
is max(α, β) − min(α, β) = |α − β|. ∎

So in p-valuations the move replaces the pair (α, β) by (min(α, β), |α − β|).

#### Lemma 9 (Euclidean identity).

For all non-negative integers α, β,

  gcd( min(α, β), |α − β| ) = gcd(α, β).

*Proof.* The subtractive form of the Euclidean algorithm states that for
non-negative integers a, b one has gcd(a, b) = gcd(a − b, b) whenever a ≥ b
(every common divisor of a and b divides a − b, and every common divisor of
a − b and b divides (a − b) + b = a; the two gcds therefore have the same
divisors, hence are equal). Let u = min(α, β) and v = max(α, β); then
|α − β| = v − u. By the subtractive identity (with a = v, b = u, so a ≥ b),

  gcd(u, v − u) = gcd(u, v) = gcd(α, β),

using gcd(u, v) = gcd(min(α, β), max(α, β)) = gcd(α, β). Hence
gcd(min(α, β), |α − β|) = gcd(α, β). ∎

#### Lemma 10 (D_p is invariant).

For every prime p, the quantity D_p is unchanged by every move.

*Proof.* D_p is the gcd of a list of 2026 non-negative integers. The move
changes only two entries of this list, replacing the pair (α, β) (the
p-valuations of the two chosen board entries) by the pair
(min(α, β), |α − β|) (Lemma 8). By Lemma 9 these two pairs have the same gcd:
gcd(min(α, β), |α − β|) = gcd(α, β). Replacing two entries of a list by two new
entries with the same pairwise gcd does not change the gcd of the whole list:
indeed gcd(a_1, …, α, β, …, a_n) = gcd(gcd(α, β), gcd of the rest) = gcd(gcd
of the new pair, gcd of the rest) = gcd(a_1, …, min(α, β), |α − β|, …, a_n).
Hence D_p is preserved. ∎

#### Lemma 11 (terminal valuation list).

At the terminal board, exactly one entry M > 1 and the rest are 1 (part (a)).
Therefore for each prime p the list of p-valuations is

  ( v_p(M), 0, 0, …, 0 ),

and its gcd is gcd(v_p(M), 0, …, 0) = v_p(M) (by gcd(x, 0) = x).

#### Conclusion of part (b).

Fix a prime p. By Lemma 10 the value D_p is invariant, so the terminal value
of D_p equals the initial value D_p^{(init)} (a function of the initial board
only). By Lemma 11 the terminal D_p equals v_p(M). Hence

  v_p(M) = D_p^{(init)}     for every prime p.

Only finitely many primes divide the initial product P (2026 finite integers),
so only finitely many D_p^{(init)} are positive, and the product below is
finite. By unique prime factorization,

  M = ∏_p p^{v_p(M)} = ∏_p p^{D_p^{(init)}}.

The right-hand side depends only on the initial board, not on any choice
Confucius made. Therefore the terminal value M is independent of Confucius's
choices. ∎

### Summary

- (a) Termination: the lexicographic potential (P, c) ∈ ℕ² strictly decreases
  at every move (Lemma 3), and ℕ² is well-founded under lex order (Lemma 4),
  so the process stops. "Exactly one > 1": the radical-support invariant
  (Lemma 5) keeps P > 1 (Lemma 6, so c ≥ 1), and the terminal condition gives
  c ≤ 1 (Lemma 7); hence c = 1.
- (b) The per-prime invariant D_p = gcd of positionwise p-valuations is
  preserved (Lemmas 8–10); at the terminal board D_p = v_p(M) (Lemma 11), so
  M = ∏_p p^{D_p^{(init)}}, a function of the initial board alone. ∎

## Promotable lemmas

- **Lemma 9 (Euclidean identity).** Statement: for non-negative integers
  α, β, gcd(min(α, β), |α − β|) = gcd(α, β). Proved in full above (subtractive
  Euclidean step). Location: this file, Lemma 9. (Already a standard identity
  but spelled out from scratch; reusable by any approach needing the D_p
  invariance engine.)
- **Lemma 5 (radical-support invariant).** Statement: the set of prime
  divisors of the total board product P is preserved by every move; hence
  P > 1 forever when initially P > 1. Proved in full above, valuation-free
  (uses prime *divisibility* only, no p-adic valuations). Location: this file,
  Lemma 5. Reusable for any valuation-free lower-bound on c.
- **Lemma 10 (D_p invariant).** Statement: for each prime p, the gcd of the
  positionwise p-valuations (gcd(x, 0) = x) is preserved by every move.
  Proved in full above via Lemmas 8–9. Location: this file, Lemma 10. Reusable
  by any approach pinning the terminal value M.
