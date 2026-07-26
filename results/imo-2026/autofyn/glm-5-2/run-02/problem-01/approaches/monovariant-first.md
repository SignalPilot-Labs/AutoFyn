# Approach: monovariant-first

- **Slug:** monovariant-first
- **Target:** IMO 2026 P1, full claim — (a) the process terminates with exactly one integer M>1 on the board, and (b) M is independent of Confucius's choices.
- **Route / framing:** Lead with termination. Exhibit a global lexicographic monovariant (W,C) that strictly decreases every move, proving the process reaches a terminal state and characterizing that state as having at most one entry >1. Only then bring in the per-prime exponent invariant g_p to (i) rule out the all-1s terminal state (upgrading "at most one" to "exactly one") and (ii) pin M = ∏_p p^{g_p}, giving choice-independence. The monovariant carries part (a)'s "finitely many moves" and the upper bound; the invariant carries the upgrade and all of part (b).

## Status
solved

## Approaches tried
- round 1: monovariant-first skeleton filled into a complete rigorous proof of (a)+(b), with the third move case broadened to "g>1 and m≠n" (covering g>1 with one exponent equal to 1, e.g. {4,8},{9,27},{2,4}) — outcome: complete, no gaps.

## Current best
Complete rigorous proof of both parts (a) and (b), below.

## Full proof

### Setup and notation

Let the 2026 entries on the board be a_1, …, a_2026 (each initially >1). For a
positive integer n write Ω(n) for the total number of prime factors of n counted
with multiplicity (so Ω(1) = 0, Ω(p) = 1, Ω(p^k) = k, and Ω(xy) = Ω(x)+Ω(y)
whenever gcd(x,y)=1, since the multisets of prime factors of two coprime integers
are disjoint). Write v_p(n) for the p-adic valuation (v_p(1)=0).

Define two integer quantities attached to the board:

  W := Ω(a_1) + Ω(a_2) + … + Ω(a_2026),     C := #{ i : a_i > 1 }.

Both are non-negative integers; W ≤ W_0 := W at the initial position throughout the
process (we will show W never increases) and C ≤ 2026.

### Reduction of a move to the (g, ab) form

A move picks two entries m > 1 and n > 1 from distinct places and replaces them by
gcd(m,n) and lcm(m,n)/gcd(m,n). Put

  g := gcd(m,n),    m = g·a,    n = g·b,    so gcd(a,b) = 1.

Then, using the identity lcm(m,n)·gcd(m,n) = m·n (the standard gcd–lcm identity,
`knowledge_base.md` "Divisor analysis"),

  lcm(m,n)/gcd(m,n) = (m·n / gcd(m,n)) / gcd(m,n) = m·n / g² = (g·a)(g·b)/g² = ab.

Also g | lcm(m,n) (since lcm(m,n) is a multiple of m and g | m), so lcm(m,n)/g is
a positive integer, and the move always produces two valid positive-integer entries.
The new pair of entries is therefore **(g, ab)**.

### Casework on a move: ΔW and ΔC

We split all moves into three disjoint, exhaustive cases. Because m, n > 1 we have
g ≥ 1; the cases are

  (i) **g = 1** ("coprime");
  (ii) **g > 1 and m = n** ("equal");
  (iii) **g > 1 and m ≠ n** ("intermediate", broadened per the outline-reviewer).

These are disjoint by construction and exhaustive: either g = 1, or g > 1; and
when g > 1, either m = n or m ≠ n. (Case (iii) covers, in particular, the
subcase g > 1 with exactly one of a, b equal to 1, e.g. {4,8}→{4,2}, {9,27}→{9,3},
{2,4}→{2,2}; this is why the case is stated as "g>1 and m≠n", not "a,b>1".)

---

**(i) g = 1.** Then a = m and b = n, and the new pair is (1, mn).
- *ΔW.* The two removed entries contribute Ω(m)+Ω(n). The two new entries contribute
  Ω(1)+Ω(mn) = 0 + Ω(mn). Since gcd(m,n)=1, Ω(mn)=Ω(m)+Ω(n) (additivity of Ω on
  coprime factors). Hence ΔW = 0.
- *ΔC.* Both removed entries (m, n) are >1; of the new entries, 1 is not >1 and
  mn > 1. So the count of entries >1 changes by (−2)+(+1) = −1. ΔC = −1.

**(ii) g > 1 and m = n.** Then m = n = g, so a = b = 1, and the new pair is (g, 1) = (m, 1).
- *ΔW.* Removed: 2·Ω(m). New: Ω(m)+Ω(1) = Ω(m). ΔW = −Ω(m). Since m > 1, Ω(m) ≥ 1,
  so ΔW ≤ −1.
- *ΔC.* Both removed entries (m, m) are >1; of the new entries, m > 1 and 1 is not.
  ΔC = (−2)+(+1) = −1.

**(iii) g > 1 and m ≠ n.** We claim both new entries g and ab are >1.
  g > 1 by hypothesis. For ab: since m ≠ n and m = ga, n = gb, we have a ≠ b. With
  gcd(a,b)=1 and a ≠ b, they cannot both equal 1 (else m = n = g); hence at least
  one of a, b exceeds 1, so ab > 1. Thus both new entries stay >1.
- *ΔW.* Removed: Ω(m)+Ω(n) = Ω(ga)+Ω(gb) = Ω(g)+Ω(a) + Ω(g)+Ω(b) = 2Ω(g)+Ω(a)+Ω(b)
  (using Ω(xy)=Ω(x)+Ω(y) for any positive integers — true because prime-factor
  multisets add under multiplication; no coprimality needed for the factors g, a
  separately). New: Ω(g)+Ω(ab). Because gcd(a,b)=1, Ω(ab)=Ω(a)+Ω(b). Hence new =
  Ω(g)+Ω(a)+Ω(b), and ΔW = −Ω(g). Since g > 1, Ω(g) ≥ 1, so ΔW ≤ −1.
- *ΔC.* Both removed entries >1; both new entries >1 (shown above). ΔC = 0.

In particular **ΔW = −Ω(gcd(m,n)) ≤ 0** in every case, with equality (ΔW = 0) exactly
in the coprime case (i); and in the coprime case C strictly drops. Summary table:

| case | ΔW | ΔC |
|------|------|------|
| (i) g = 1 | 0 | −1 |
| (ii) g>1, m = n | −Ω(m) ≤ −1 | −1 |
| (iii) g>1, m ≠ n | −Ω(g) ≤ −1 | 0 |

### Termination: the lexicographic pair (W, C) strictly decreases

Order pairs in ℕ² lexicographically: (W,C) < (W',C') iff W < W', or W = W' and C < C'.
From the table, every move sends (W, C) to a strictly smaller lexicographic pair:
in cases (ii) and (iii) the first component W drops by at least 1 (so the pair
decreases regardless of C); in case (i) W is unchanged but C drops by 1, so the pair
decreases in the second component. Both W and C are non-negative integers bounded
below by 0, and throughout the process W ≤ W_0 and C ≤ 2026.

A strictly decreasing sequence in ℕ² under lexicographic order cannot be infinite:
each move either drops W by ≥1 (which can happen at most W_0 times before W reaches
0) or keeps W fixed and drops C by 1 (which can happen at most 2026 times at fixed
W). Hence the total number of moves is at most W_0 + 2026·(W_0+1) in the crudest
bound — in any case finite. This is the standard **integer-descent / monovariant**
argument (`knowledge_base.md`, "Invariants & monovariants", line 117, and the
"Infinite descent" sibling, line 184–185: a non-negative integer quantity that
strictly decreases each step admits no infinite chain, by the well-foundedness of ℕ).

Therefore, **regardless of Confucius's choices, the process reaches a terminal
state after finitely many moves.** This establishes the "finitely many moves" half
of part (a).

### The terminal state has at most one entry >1

A move is legal exactly when there exist two entries >1 in distinct places: that is
the only hypothesis required of (m, n), and we showed above that the replacement
(g, ab) always consists of two positive integers, so the move is always executable
whenever two entries >1 are available — no other obstruction exists. Hence the
process stops ("no move is possible") precisely when fewer than two entries are >1,
i.e. when the board has **at most one entry >1**.

Termination alone therefore gives "at most one entry >1". We must still rule out the
case "zero entries >1" (an all-1s board) to obtain "exactly one".

### The per-prime exponent invariant g_p

For each prime p define

  g_p := gcd( v_p(a_1), v_p(a_2), …, v_p(a_2026) ),

with the conventions gcd(0, k) = k and gcd(0, 0) = 0 (so that zeros are neutral and
gcd of a list is obtained by folding pairwise gcd, which is associative and
commutative).

**Lemma (exponent-pair Euclidean preservation).** *Every move leaves g_p unchanged.*

*Proof.* Under a move on (m, n) with p-valuations (α, β) = (v_p(m), v_p(n)), the two
new valuations are

  v_p(gcd(m,n)) = min(α, β),    v_p(lcm(m,n)/gcd(m,n)) = max(α,β) − min(α,β) = |α − β|,

using v_p(gcd) = min and v_p(lcm) = max. So the pair (α, β) is replaced by
(α', β') = (min(α,β), |α−β|).

- If α = 0 (symmetrically β = 0): the new pair is (0, β) — the same multiset as
  {0, β}, so the gcd is unchanged (the convention gcd(0, β) = β, including gcd(0,0)=0,
  handles this).
- If α, β > 0: assume α ≤ β (both gcd and the replacement are symmetric in the two
  entries). Then (α', β') = (α, β − α), and the **subtractive Euclidean step**
  gcd(x, y) = gcd(x, y − x) for y ≥ x > 0 (one-step form of the Euclidean algorithm)
  gives gcd(α, β) = gcd(α, β − α) = gcd(α', β').

So in every case the pairwise gcd of the touched pair is preserved. The whole-board
gcd g_p is the fold of pairwise gcds over all 2026 valuations; replacing two
elements of the multiset by a pair with the same pairwise gcd leaves the fold
unchanged. Hence g_p is invariant. ∎

(This lemma is recorded in `results/imo-2026-01/lemmas/exponent-pair-euclidean-invariant.md`
for reuse by the sibling approach.)

### The board invariant Q := ∏_p p^{g_p} and the bound Q ≥ 2

Define

  Q := ∏_p p^{g_p},

the product ranging over all primes. Because each entry a_i is a fixed positive
integer with only finitely many prime divisors, and there are 2026 entries, only
finitely many primes divide some entry; for every other prime p, every
v_p(a_i) = 0, so g_p = 0 and p^{g_p} = 1. Thus **Q is a finite product** and is
well-defined. Since every g_p is invariant (Lemma), **Q is a board invariant.**

**Q ≥ 2 at all times.** Initially every a_i > 1. Pick any entry, say a_1 > 1; it has
at least one prime divisor p, so v_p(a_1) ≥ 1. The gcd of a multiset containing a
positive integer is itself a positive integer, hence g_p ≥ 1. Therefore the factor
p^{g_p} ≥ p ≥ 2 appears in Q, giving Q ≥ 2. By invariance, Q ≥ 2 throughout.

### Ruling out the all-1s terminal state (completing part (a))

Suppose, for contradiction, that the terminal state were all 1s. Then every entry
equals 1, so v_p(a_i) = 0 for every i and every prime p. Hence

  g_p = gcd(0, 0, …, 0) = 0     for every prime p,

and so Q = ∏_p p^0 = 1. This contradicts the invariant lower bound Q ≥ 2.

Therefore the terminal state is not all 1s. Combined with "at most one entry >1"
from the terminal characterization, the terminal state has **exactly one entry >1**.
Call that entry M. This completes part (a): after finitely many moves, regardless of
choices, exactly one integer M > 1 remains on the board.

### Pinning M for part (b)

In the terminal state exactly one entry M > 1 remains; the other 2025 entries are
1. For each prime p, the multiset of p-valuations on the board is

  { v_p(M), 0, 0, …, 0 }    (one v_p(M) and 2025 zeros).

Its gcd is gcd(v_p(M), 0, …, 0) = v_p(M), using gcd(k, 0) = k and folding. By the
invariance of g_p (Lemma), this equals g_p:

  v_p(M) = g_p     for every prime p.

Therefore

  M = ∏_p p^{v_p(M)} = ∏_p p^{g_p} = Q.

The right-hand side Q is completely determined by the initial board (it is built
only from the initial valuations v_p(a_i) and is invariant under moves). Hence the
terminal value M is the same for every sequence of choices Confucius makes. This
proves part (b). ∎

## Promotable lemmas
- **exponent-pair Euclidean preservation** — for each prime p, the whole-board gcd
  g_p = gcd(v_p(a_1),…,v_p(a_2026)) (with gcd(0,k)=k) is invariant under the move
  (m,n)→(gcd(m,n), lcm(m,n)/gcd(m,n)), because the touched valuation pair
  (α,β)=(v_p(m),v_p(n)) is sent to (min(α,β),|α−β|), a subtractive-Euclidean step
  preserving the pairwise gcd (Euclidean identity gcd(α,β)=gcd(min,|α−β|)), and the
  whole-board gcd is a fold of pairwise gcds. Proved in full in this file (step
  "The per-prime exponent invariant g_p") and recorded in
  `results/imo-2026-01/lemmas/exponent-pair-euclidean-invariant.md`.
