# Approach: perprime-valuation

## Status
solved

## Target (whole problem)
(a) From any start of 2026 integers >1, after finitely many moves exactly one entry M>1 remains.
(b) M is independent of the choices, with explicit value **M = ∏_p p^{g_p}** where
`g_p = gcd(v_p(x_1),…,v_p(x_2026))` (gcd of the p-adic valuations of the 2026 initial entries,
convention gcd(x,0)=x, gcd(0,…,0)=0).

## Approaches tried
- Round 1: prime-by-prime valuation decomposition. One per-prime gcd invariant `g_p` for (b) plus one
  lexicographic monovariant `(Ω_total, C)` for (a). All gaps G1–G5 closed; conventions fixed;
  example {4,8,3}→6 verified (and a 300-board / 20-order random stress test confirms the closed form).
  Outcome: **complete rigorous proof of both (a) and (b)**.

## Current best
Complete proof (below). Key facts, all proved from scratch: the move acts on each prime's valuation
pair by `(a,b) ↦ (min(a,b), |a-b|)` (Lemma 1); `gcd(min(a,b),|a-b|) = gcd(a,b)` gives the invariant
`g_p` (Lemma 3); the lexicographic pair `(Ω_total, C)` strictly decreases (Lemma 2), forcing
termination with ≤1 entry >1; the invariant forces ≥1 entry >1, hence exactly one, of value
`M = ∏_p p^{g_p}`.

## Full proof

### 0. Setup, notation, and conventions

The blackboard holds an (unordered) multiset of `N = 2026` positive integers. We track it as a tuple
`(x_1, …, x_N)` with `x_i ≥ 1`; the labelling of positions is only a bookkeeping device and plays no
role. Initially every `x_i > 1`.

**The move.** A *move* is legal only when at least two entries exceed `1`. It selects two positions
`i ≠ j` with `x_i = m > 1` and `x_j = n > 1`, and replaces them by
`gcd(m,n)` and `lcm(m,n)/gcd(m,n)`, leaving all other positions unchanged. (Which of the two new
numbers is written in position `i` versus `j` is immaterial, since the board is a multiset; the proof
below never uses this choice.) Confucius performs moves as long as a legal move exists.

We must show: (a) every such maximal sequence of moves is finite and ends with exactly one entry `>1`;
(b) that surviving entry `M` is the same no matter which legal moves are chosen.

**`lcm(m,n)/gcd(m,n)` is a positive integer.** We have `lcm(m,n) = mn/gcd(m,n)`, so
`lcm(m,n)/gcd(m,n) = mn/gcd(m,n)^2`, and `gcd(m,n)^2 ∣ mn` because `gcd(m,n) ∣ m` and `gcd(m,n) ∣ n`.
Thus `lcm(m,n)/gcd(m,n)` is a positive integer. Hence a move keeps all entries positive integers and
keeps `N = 2026` entries; only the two chosen entries change.

**`p`-adic valuation.** For a prime `p` and a positive integer `x`, let `v_p(x)` denote the exponent of
`p` in the prime factorization of `x` (so `x = ∏_p p^{v_p(x)}`, a finite product). We use throughout
the standard **valuation identities** (consequences of unique factorization; KB "Divisor analysis"):
for positive integers `m, n` and every prime `p`,
```
v_p(mn) = v_p(m) + v_p(n),        v_p(m/n) = v_p(m) − v_p(n)  when n ∣ m,
v_p(gcd(m,n)) = min(v_p(m), v_p(n)),   v_p(lcm(m,n)) = max(v_p(m), v_p(n)).
```
The last two hold because `gcd(m,n) = ∏_p p^{min(v_p(m),v_p(n))}` and
`lcm(m,n) = ∏_p p^{max(v_p(m),v_p(n))}` are exactly the standard product formulas for gcd and lcm
under unique factorization. Note `x = 1 ⟺ v_p(x) = 0` for all `p`, and `x > 1 ⟺ v_p(x) ≥ 1` for at
least one prime `p`.

**gcd conventions with zero.** For nonnegative integers we use `gcd(a, 0) = gcd(0, a) = a` and
`gcd(0,0) = 0`; `gcd` of a finite list is taken by iterating the binary gcd, and this is well defined
because the binary gcd on `ℤ_{≥0}` is commutative and associative (both sides equal the largest
nonnegative integer dividing every argument, with the convention that every integer divides `0` and
`gcd` of all zeros is `0`). These are the standard conventions and are used consistently below.

Since only finitely many primes divide any of the (finitely many) board entries at any time, all sums
and products "over all primes `p`" below have only finitely many nontrivial terms and are genuine
finite expressions.

---

### 1. Lemma 1 (the move is one subtractive-Euclid step on each prime's valuations)

**Lemma 1.** Fix a move on entries `m > 1`, `n > 1`. Write the two new entries as `d = gcd(m,n)` and
`e = lcm(m,n)/gcd(m,n)`. Then for **every** prime `p`, setting `a = v_p(m)` and `b = v_p(n)`,
```
v_p(d) = min(a, b),        v_p(e) = |a − b|.
```
Consequently, for every prime `p` the unordered pair of valuations at the two touched positions
transforms as
```
{a, b}  ↦  {min(a, b), |a − b|},
```
while the `p`-valuation of every untouched position is unchanged.

*Proof.* By the valuation identities of §0, `v_p(d) = v_p(gcd(m,n)) = min(a,b)`. Next,
`e = lcm(m,n)/gcd(m,n)`, and `gcd(m,n) ∣ lcm(m,n)` (indeed `lcm(m,n) = mn/gcd(m,n)` and
`gcd(m,n) ∣ m`, so `gcd(m,n) ∣ mn/gcd(m,n) = lcm(m,n)`), so the quotient rule for valuations applies:
```
v_p(e) = v_p(lcm(m,n)) − v_p(gcd(m,n)) = max(a,b) − min(a,b).
```
For any two real numbers, `max(a,b) − min(a,b) = |a − b|` (if `a ≥ b` both sides equal `a − b`; if
`a < b` both equal `b − a`). Hence `v_p(e) = |a − b|`.

Because `min(a,b)` and `|a−b|` are exactly `v_p(d)` and `v_p(e)`, the multiset of `p`-valuations at the
two touched positions changes from `{a, b}` to `{min(a,b), |a − b|}`. All other positions are literally
unchanged by the move, so their valuations at every prime are unchanged. This holds simultaneously for
every prime `p`, since the two displayed identities were derived for an arbitrary prime. ∎

Two remarks used later. First, if `p` divides neither `m` nor `n` then `a = b = 0` and
`{min, |a−b|} = {0,0}`: consistent (the prime is untouched). Second,
`min(a,b) + |a − b| = max(a,b)`, recorded here for §2.

---

### 2. Lemma 2 (termination monovariant) and proof of finiteness

Define two nonnegative-integer quantities of a board `(x_1,…,x_N)`:
```
Ω(x) = Σ_p v_p(x)   (the number of prime factors of x counted with multiplicity; Ω(1)=0),
Ω_total = Σ_{i=1}^{N} Ω(x_i) = Σ_p Σ_{i=1}^{N} v_p(x_i),
C = #{ i : x_i > 1 }.
```
Order pairs `(Ω_total, C) ∈ ℕ × ℕ` **lexicographically**: `(A,B) < (A',B')` iff `A < A'`, or `A = A'`
and `B < B'`.

**Lemma 2.** Every legal move strictly decreases `(Ω_total, C)` in the lexicographic order.

*Proof.* Consider a move on `m > 1`, `n > 1`, producing `d = gcd(m,n)`, `e = lcm(m,n)/gcd(m,n)`. Only
these two positions change, so we compare their contributions before and after.

*Change in `Ω_total`.* For each prime `p`, with `a = v_p(m)`, `b = v_p(n)`, the two touched positions
contribute `a + b` before and, by Lemma 1, `min(a,b) + |a − b| = max(a,b)` after. Hence the change at
prime `p` is `max(a,b) − (a + b) = −min(a,b) ≤ 0`. Summing over all primes (finitely many nonzero
terms),
```
Ω_total(after) − Ω_total(before) = − Σ_p min(v_p(m), v_p(n)) = − Σ_p v_p(gcd(m,n)) = − Ω(gcd(m,n)) ≤ 0,
```
where we used `v_p(gcd(m,n)) = min(a,b)` (Lemma 1 / §0). So `Ω_total` never increases, and it strictly
decreases **iff** `Ω(gcd(m,n)) > 0`, i.e. iff `gcd(m,n) > 1`.

We now split into the two exhaustive cases according to `gcd(m,n)`.

**Case A: `gcd(m,n) > 1`.** Then `Ω(gcd(m,n)) ≥ 1`, so `Ω_total` strictly decreases by at least `1`.
Since the first lexicographic coordinate drops, `(Ω_total, C)` strictly decreases (regardless of what
`C` does). Done.

**Case B: `gcd(m,n) = 1`.** Then `Ω(gcd(m,n)) = 0`, so `Ω_total` is unchanged; we must show `C`
strictly decreases. Here `d = gcd(m,n) = 1` and `e = lcm(m,n)/gcd(m,n) = lcm(m,n) = mn` (as
`gcd = 1`), and `mn > 1` because `m, n > 1`. So the two touched positions held `{m, n}` with **both**
`> 1` (contributing `2` to `C`) and now hold `{1, mn}` with **exactly one** entry `> 1` (contributing
`1` to `C`). No other position changes. Therefore `C` decreases by exactly `1`, while `Ω_total` is
unchanged, so `(Ω_total, C)` strictly decreases in lex order. Done.

In both cases `(Ω_total, C)` strictly decreases. ∎

**Finiteness (first half of (a)).** `Ω_total ≥ 0` and `C ≥ 0` are integers, so `(Ω_total, C)` ranges in
`ℕ × ℕ`. The lexicographic order on `ℕ × ℕ` is a **well-order**: it has no infinite strictly
decreasing sequence. (Proof: given a strictly decreasing sequence, its first coordinates form a
non-increasing sequence of nonnegative integers, hence are eventually constant, say from index `k`
onward; from index `k` the second coordinates must strictly decrease, an infinite strictly decreasing
sequence of nonnegative integers, which is impossible. So no infinite strictly decreasing sequence
exists.) By Lemma 2 each move produces a strict decrease, so **only finitely many moves can occur**:
every maximal sequence of moves is finite. (KB: "Invariants & monovariants".)

**Terminal shape.** A move is legal exactly when at least two entries exceed `1`. The process stops
precisely when **no** legal move exists, i.e. when at most one entry exceeds `1`. Thus at the halt,
`C ≤ 1`. This gives "at most one survivor"; §4 upgrades it to exactly one.

---

### 3. Lemma 3 (the per-prime gcd invariant) and proof of invariance

For each prime `p` and a board `(x_1, …, x_N)`, define
```
g_p := gcd( v_p(x_1), v_p(x_2), …, v_p(x_N) )
```
using the zero conventions of §0.

**Lemma 3 (one-step gcd identity).** For all nonnegative integers `a, b`,
```
gcd( min(a,b), |a − b| ) = gcd(a, b).
```

*Proof.* By symmetry of both sides in `a, b`, assume WLOG `a ≤ b`, so `min(a,b) = a` and
`|a − b| = b − a`. We must show `gcd(a, b − a) = gcd(a, b)`. This is the **subtractive Euclidean
identity**: a nonnegative integer `k` divides both `a` and `b` iff it divides both `a` and `b − a`
(if `k ∣ a` and `k ∣ b` then `k ∣ b − a`; conversely if `k ∣ a` and `k ∣ (b − a)` then
`k ∣ a + (b − a) = b`). Hence the pairs `(a, b)` and `(a, b − a)` have identical sets of common
divisors, so identical greatest common divisor. The edge cases are covered by the same statement:
if `a = b`, LHS `= gcd(a, 0) = a = gcd(a, a)` = RHS; if `a = 0 ≤ b`, LHS `= gcd(0, b) = b = gcd(0, b)`
= RHS. ∎

**Lemma 4 (multiset lift / associativity).** For nonnegative integers `r_1,…,r_{N-2}, a, b`,
```
gcd(r_1,…,r_{N-2}, a, b) = gcd( r_1,…,r_{N-2}, gcd(a,b) ).
```

*Proof.* Both sides equal the largest nonnegative integer dividing every one of the listed arguments
(with the zero conventions of §0). Replacing the last two arguments `a, b` by `gcd(a,b)` leaves the set
of common divisors of the whole list unchanged, because an integer divides both `a` and `b` iff it
divides `gcd(a,b)`. Hence the overall gcd is unchanged. (This is exactly the associativity/commutativity
of the binary gcd folded over the list.) ∎

**Invariance of `g_p`.** Consider any single move; by Lemma 1 it changes, at each prime `p`, only the
two touched coordinates, from `{a, b}` to `{min(a,b), |a−b|}`, leaving the remaining `N − 2`
coordinates `r_1,…,r_{N-2}` (the `p`-valuations of the untouched entries) fixed. Then, using Lemma 4
twice and Lemma 3 in the middle,
```
g_p(before) = gcd(r_1,…,r_{N-2}, a, b)
            = gcd(r_1,…,r_{N-2}, gcd(a,b))                     [Lemma 4]
            = gcd(r_1,…,r_{N-2}, gcd(min(a,b), |a−b|))         [Lemma 3]
            = gcd(r_1,…,r_{N-2}, min(a,b), |a−b|)              [Lemma 4]
            = g_p(after).
```
This holds for every prime `p` and every move. Therefore, for each prime `p`, the number `g_p` takes
the same value throughout the entire process — it is an **invariant** (KB: "Invariants &
monovariants"). In particular, at every stage `g_p` equals its value on the initial board,
`g_p = gcd(v_p(x_1^{init}),…,v_p(x_N^{init}))`, which depends only on the initial multiset. ∎

---

### 4. Exactly one survivor (completes (a)) and its value (completes (b))

By §2 the process halts after finitely many moves at a board with at most one entry `> 1` (`C ≤ 1`).
It remains to rule out `C = 0` and to identify the surviving entry.

**At least one prime has `g_p ≥ 1`.** Every initial entry is `> 1`, hence divisible by some prime; so
there is a prime `p` and an index `i` with `v_p(x_i^{init}) ≥ 1`. Fix such a `p`. Consider `g_p =
gcd(v_p(x_1),…,v_p(x_N))` on the initial board. This is a gcd of nonnegative integers that are **not
all zero** (the `i`-th is ≥ 1). A gcd of nonnegative integers not all zero is a positive integer: it is
the largest positive integer dividing all of them, and `1` always divides all of them, so it is `≥ 1`.
Hence `g_p ≥ 1` for this prime. By §3 (invariance), `g_p ≥ 1` **at the halt** as well.

**`C ≥ 1`, hence `C = 1`.** Suppose, for contradiction, that at the halt every entry equals `1`. Then
`v_p(x_i) = 0` for all `i` and all primes, so `g_p = gcd(0,…,0) = 0` at the halt for every prime — in
particular for the prime `p` above, contradicting `g_p ≥ 1`. Therefore at least one entry at the halt
is `> 1`, i.e. `C ≥ 1`. Combined with `C ≤ 1` from §2, we get exactly `C = 1`: **exactly one entry
`M > 1` remains**, and the rest are `1`. This proves **part (a)** in full (finiteness from §2, exactly
one survivor here).

**Value of `M` and choice-independence.** At the halt the board is (as a multiset) `{M, 1, 1, …, 1}`
with `M > 1`. Fix any prime `p`. The `p`-valuations of the entries are `v_p(M)` for the surviving slot
and `0` for the other `N − 1` slots. Hence, at the halt,
```
g_p = gcd( v_p(M), 0, 0, …, 0 ) = v_p(M)
```
by the convention `gcd(k, 0, …, 0) = k` (§0). But by §3, `g_p` at the halt equals its value on the
**initial** board, `g_p = gcd(v_p(x_1^{init}), …, v_p(x_N^{init}))`, which is determined solely by the
starting multiset — not by any of Confucius's choices. Therefore, for every prime `p`,
```
v_p(M) = g_p = gcd( v_p(x_1^{init}), …, v_p(x_N^{init}) ),
```
and by unique factorization
```
M = ∏_p p^{ g_p }.
```
Only finitely many `g_p` are nonzero (only primes dividing some initial entry can have `g_p ≥ 1`), so
this is a finite product and a genuine positive integer, with `M > 1` since at least one `g_p ≥ 1`. The
right-hand side depends only on the initial board. Hence `M` is the same for **every** valid sequence
of moves: **part (b)** is proved, with the explicit value `M = ∏_p p^{g_p}`. ∎

---

### 5. Verification on a concrete example

Take a board `{4, 8, 3}` (illustrative; the argument is size-independent, and `N = 2026` plays no
special role beyond `N ≥ 2`). Prime valuations:
`v_2 = (2, 3, 0)`, `v_3 = (0, 0, 1)`, and `v_p = (0,0,0)` for all other primes.
```
g_2 = gcd(2, 3, 0) = gcd(gcd(2,3), 0) = gcd(1, 0) = 1,
g_3 = gcd(0, 0, 1) = 1,
g_p = 0   (p ≠ 2, 3).
```
Predicted survivor: `M = 2^1 · 3^1 = 6`.

Check one play: `gcd(4,8)=4`, `lcm(4,8)=8`, `8/4 = 2`, so `{4,8,3} → {4, 2, 3}`. Then `gcd(4,2)=2`,
`lcm(4,2)=4`, `4/2 = 2`, giving `{2, 2, 3}`. Then `gcd(2,2)=2`, `lcm(2,2)=2`, `2/2 = 1`, giving
`{2, 1, 3}`. Then `gcd(2,3)=1`, `lcm(2,3)=6`, `6/1 = 6`, giving `{1, 1, 6}`. Exactly one survivor
`M = 6`, matching `∏_p p^{g_p} = 6`. A different order, e.g. `gcd(8,3)=1, lcm=24 → {4, 24, 1}`, then
`gcd(4,24)=4, lcm=24, 24/4=6 → {4, 6, 1}`, then `gcd(4,6)=2, lcm=12, 12/2=6 → {2, 6, 1}`, then
`gcd(2,6)=2, lcm=6, 6/2=3 → {2,3,1}`, then `gcd(2,3)=1, lcm=6 → {1,6,1}`: again `M = 6`. Consistent
with (b).

(A computational stress test over 300 random boards, each played to completion in 20 random move
orders, confirmed the survivor is unique per board and equals `∏_p p^{g_p}` in every case. This is a
sanity check only; the proof above is self-contained.)

∎

## Promotable lemmas
- **Lemma 1 (per-prime move step).** A move `{m,n} → {gcd(m,n), lcm(m,n)/gcd(m,n)}` acts on each
  prime's touched valuation pair by `{a,b} ↦ {min(a,b), |a−b|}`, all other valuations fixed. Proved in
  §1 from the valuation identities for gcd/lcm and the quotient rule.
- **Lemma 3 (subtractive-Euclid gcd identity).** For nonnegative integers `a,b`,
  `gcd(min(a,b), |a−b|) = gcd(a,b)` (with `gcd(x,0)=x`). Proved in §3. Together with the associativity
  lift (Lemma 4) this yields the invariance of `g_p = gcd_i v_p(x_i)` under a move — the central
  invariant of part (b), reusable by the descent-induction and confluence-newman approaches.