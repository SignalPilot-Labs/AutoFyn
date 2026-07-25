## Status
solved

## Approach: per-prime gcd-of-exponents invariant (computes M explicitly)

Framing: decouple the board into 2026 exponent-multisets, one per prime. The move is,
per prime, exactly the subtractive Euclidean step. The gcd of each prime's exponent
multiset is an EXACT conserved quantity; this both pins the value of M (part b) and,
together with an elementary monovariant, gives part (a). This is the "compute the closed
form M = ∏_p p^{g_p}" route.

## Approaches tried
- per-prime gcd-of-exponents invariant (this round): p-adic decoupling; per-prime action
  (a,b)↦(min,max−min); exact invariant g_p = gcd of each prime's exponent multiset; lex
  monovariant (Ω_total, K) for termination; non-collapse via lcm>1. **Worked** — all gaps
  (Lemma A associativity + gcd(0,·) conventions, Lemma B Ω-identity and m=n subcase, Step 7
  gcd of {2025 zeros, one e_p}, same-slot automatic) closed; full proof of both parts below,
  concrete example {12,18,20}→M=30 verified. Status: solved.

## Current best
Complete proof of both parts, with the closed form M = ∏_p p^{g_p} where
g_p = gcd(v_p(a_1),…,v_p(a_2026)) taken over the initial board. See Full proof.

## Full proof

Throughout, the **board** is a finite multiset of positive integers, of fixed size
n = 2026. We think of the board as an ordered tuple (b_1, …, b_n) of *slots*; a slot may
hold the value 1. A **move** selects two distinct slot indices i ≠ j with b_i > 1 and
b_j > 1, sets m := b_i, n := b_j, and replaces the two entries by

    g := gcd(m, n),   ℓ := lcm(m, n) / gcd(m, n),

leaving every other slot unchanged. (Since gcd(m,n) divides lcm(m,n), ℓ is a positive
integer, so the move is well defined.) A board is **terminal** if no move is possible.

We prove:

(a) Starting from any board of n = 2026 integers each > 1, every sequence of moves
    reaches a terminal board after finitely many moves, and that terminal board has
    exactly one slot with value > 1.

(b) The value M of that single surviving entry is the same for every legal sequence of
    moves; explicitly, writing v_p(x) for the exponent of the prime p in x,

        M = ∏_p p^{g_p},   where g_p := gcd(v_p(b_1), …, v_p(b_n))

    is computed from the **initial** board and hence is independent of all choices.

We use two standard tools, both listed in `knowledge_base.md`:
- **Invariant / monovariant** (`knowledge_base.md`, "Invariants & monovariants" and
  "Invariant / monovariant"): a quantity preserved across moves (for (b)) and a quantity
  strictly monotone across moves (for termination in (a)).
- **Divisor analysis** (`knowledge_base.md`, "Divisor analysis"): the p-adic valuation
  and the gcd/lcm structure of integers.

We also use, as named number-theoretic facts, the valuation formulas for gcd and lcm and
the subtractive form of the Euclidean algorithm, each proved below where first needed.

Notation for valuations. For a prime p and a positive integer x, v_p(x) is the largest
integer k ≥ 0 with p^k ∣ x. The two facts we repeatedly use are:

  (V1)  v_p(gcd(m,n)) = min(v_p(m), v_p(n)),
  (V2)  v_p(lcm(m,n)) = max(v_p(m), v_p(n)),

for all positive integers m, n. Proof of (V1)–(V2): write a = v_p(m), b = v_p(n) and
assume WLOG a ≤ b (the two formulas are symmetric in m, n). A common divisor d of m and n
has v_p(d) ≤ v_p(m) = a and v_p(d) ≤ v_p(n) = b, so v_p(d) ≤ a; conversely p^a divides
both m and n. Applying this to every prime, the greatest common divisor has p-exponent
exactly a = min(a,b), which is (V1). For (V2), lcm(m,n) = mn/gcd(m,n), so by
multiplicativity of v_p (i.e. v_p(xy) = v_p(x)+v_p(y), immediate from unique
factorization) and (V1),
  v_p(lcm(m,n)) = v_p(m) + v_p(n) − v_p(gcd(m,n)) = a + b − min(a,b) = max(a,b),
which is (V2). ∎ (V1)–(V2)

Two elementary conventions/facts about gcd that we make explicit, because slots where p
does not divide the entry contribute exponent 0:
  (G0)  gcd(0, x) = x and gcd(x, 0) = x for every integer x ≥ 0, and gcd(0,0) = 0.
        (Here gcd(u,v) for nonnegative integers is the largest integer dividing both,
        with the convention that every integer divides 0, so gcd(0,x)=x.)
  (G1)  gcd is associative and commutative on nonnegative integers, so for a finite
        multiset S of nonnegative integers the value gcd(S) := gcd of all members is well
        defined independently of the order of combination, and for any partition
        S = A ⊔ B into submultisets,
            gcd(S) = gcd( gcd(A), gcd(B) ).
        (This is the standard fact that the set of common divisors of S equals the set of
        divisors of gcd(S), and common divisors of A ⊔ B are exactly the common divisors
        of gcd(A) and gcd(B).)

---

### Step 1 (per-prime action of a move)

Fix a prime p. Suppose a move acts on slots i, j with old values m = b_i, n = b_j, and
put a := v_p(m), b := v_p(n). The new entries are g = gcd(m,n) and ℓ = lcm(m,n)/gcd(m,n).
Then by (V1),
    v_p(g) = v_p(gcd(m,n)) = min(a, b),
and by (V2) and multiplicativity of v_p,
    v_p(ℓ) = v_p(lcm(m,n)) − v_p(gcd(m,n)) = max(a,b) − min(a,b).
Every slot other than i, j is unchanged, hence its p-exponent is unchanged. Therefore, in
the multiset of p-exponents of the board, the effect of the move is precisely: replace
the pair (a, b) at positions i, j by

    (a, b) ↦ ( min(a,b),  max(a,b) − min(a,b) ),

and leave all other exponents fixed. Note max(a,b) − min(a,b) ≥ 0 is a legitimate
exponent, so this is a valid operation on the exponent multiset. This holds for every
prime p simultaneously. ∎ (Step 1)

Thus the whole process decouples over primes: for each prime p the board induces a
multiset E_p = (v_p(b_1), …, v_p(b_n)) of n nonnegative integers, and a single physical
move performs on E_p exactly one "subtractive step" on two of its entries (and does
nothing to E_q for primes q not dividing either m or n, since then both a and b, or the
relevant exponents, may be 0 and (0,0)↦(0,0)).

---

### Step 2 (the Euclidean identity)

For all integers a, b ≥ 0,
    gcd( min(a,b), max(a,b) − min(a,b) ) = gcd(a, b).                              (E)

Proof. By symmetry assume a ≤ b, so min = a, max − min = b − a. We must show
gcd(a, b − a) = gcd(a, b). If a = 0 this reads gcd(0, b) = gcd(0, b), true by (G0). For
a ≥ 0 in general: every common divisor d of a and b divides b − a, hence divides the pair
(a, b−a); conversely every common divisor d of a and b−a divides a + (b−a) = b, hence
divides the pair (a, b). So the two pairs have exactly the same set of common divisors,
and therefore the same greatest common divisor. This is the subtractive step of the
**Euclidean algorithm**. ∎ (E)

---

### Step 3 (Lemma A: g_p is an exact invariant)

**Lemma A.** For each prime p, the quantity g_p := gcd(E_p) = gcd(v_p(b_1),…,v_p(b_n)) is
unchanged by every move.

Proof. A move touches only two positions i, j of E_p, replacing the pair (a, b) =
(v_p(b_i), v_p(b_j)) by (min(a,b), max(a,b)−min(a,b)) (Step 1), and leaves the remaining
n−2 exponents fixed. Let R denote the multiset of those n−2 untouched exponents. Using
associativity (G1) with the partition E_p = R ⊔ {a, b}:
    gcd(E_p) = gcd( gcd(R), gcd(a, b) ).
After the move the two touched entries become min(a,b), max(a,b)−min(a,b), while R is
unchanged, so the new value is
    gcd( gcd(R), gcd( min(a,b), max(a,b)−min(a,b) ) ).
By the Euclidean identity (E), gcd(min(a,b), max(a,b)−min(a,b)) = gcd(a,b). Hence the two
expressions are equal:
    gcd(E_p)_new = gcd( gcd(R), gcd(a,b) ) = gcd(E_p)_old.
(The n = 2 boundary and cases where an exponent is 0 are covered by the conventions (G0):
if R is empty, gcd(R) is the empty gcd = 0 and gcd(0, gcd(a,b)) = gcd(a,b) by (G0), and
the argument is unchanged.) Thus g_p is invariant under every move, for every prime p. ∎
(Lemma A)

---

### Step 4 (Lemma B: a strictly decreasing lexicographic monovariant — termination)

Define two nonnegative-integer statistics of a board:
- Ω_total := Σ_{k=1}^{n} Ω(b_k), where Ω(x) = Σ_p v_p(x) is the number of prime factors of
  x counted with multiplicity (Ω(1) = 0). Since each b_k ≥ 1, Ω_total ≥ 0.
- K := #{ k : b_k > 1 }, the number of active slots, with 0 ≤ K ≤ n.

Order pairs lexicographically: (Ω_total, K) < (Ω_total', K') iff Ω_total < Ω_total', or
Ω_total = Ω_total' and K < K'.

**Lemma B.** Every move strictly decreases (Ω_total, K) in this lexicographic order.

Proof. A move replaces m = b_i, n = b_j (both > 1) by g = gcd(m,n),
ℓ = lcm(m,n)/gcd(m,n), leaving other slots untouched. Only slots i, j change, so
    Ω_total,new − Ω_total,old = [ Ω(g) + Ω(ℓ) ] − [ Ω(m) + Ω(n) ].
Now Ω is completely additive: Ω(xy) = Ω(x) + Ω(y) (immediate from Ω(x) = Σ_p v_p(x) and
multiplicativity of each v_p). Since gℓ = gcd(m,n)·lcm(m,n)/gcd(m,n) = lcm(m,n),
    Ω(g) + Ω(ℓ) = Ω(gℓ) = Ω(lcm(m,n)).
And from lcm(m,n)·gcd(m,n) = mn we get, again by additivity,
    Ω(lcm(m,n)) + Ω(gcd(m,n)) = Ω(m) + Ω(n),  so  Ω(lcm(m,n)) = Ω(m)+Ω(n) − Ω(gcd(m,n)).
Therefore
    Ω_total,new − Ω_total,old = Ω(m)+Ω(n) − Ω(gcd(m,n)) − Ω(m) − Ω(n) = − Ω(gcd(m,n)).  (†)
Since Ω(gcd(m,n)) ≥ 0 always, Ω_total is non-increasing. Two cases:

Case 1: gcd(m,n) > 1. Then Ω(gcd(m,n)) ≥ 1, so by (†) Ω_total strictly decreases (by at
least 1). The pair (Ω_total, K) then strictly decreases lexicographically regardless of
how K changes.

Case 2: gcd(m,n) = 1. Then g = 1 and ℓ = lcm(m,n)/1 = lcm(m,n) = mn > 1 (as m,n > 1). By
(†), Ω_total is unchanged. We show K strictly decreases. Before the move, slots i and j
were both active (m, n > 1), contributing 2 to K. After the move slot i holds g = 1
(inactive) and slot j holds ℓ = mn > 1 (active), contributing 1. No other slot changed.
Hence K decreases by exactly 1. So (Ω_total, K) strictly decreases lexicographically
(same first coordinate, smaller second).

The special subcase m = n (allowed: two different slots may hold equal values) falls under
Case 1 when m = n > 1: then g = gcd(m,m) = m > 1 and ℓ = lcm(m,m)/m = m/m = 1, so
Ω(gcd) = Ω(m) ≥ 1 and Ω_total strictly drops by Ω(m); K also drops (slot becomes 1) but
the strict drop in the first coordinate already suffices. So m = n needs no separate
treatment.

In all cases (Ω_total, K) strictly decreases. ∎ (Lemma B)

**Termination.** The values (Ω_total, K) lie in ℤ_{≥0} × {0,1,…,n}, a set well-ordered by
the lexicographic order (it is order-isomorphic to a subset of ℕ, e.g. via
(Ω_total,K) ↦ (n+1)·Ω_total + K, which is a strictly increasing map into ℕ). A strictly
decreasing sequence in a well-ordered set is finite. Since every move strictly decreases
(Ω_total, K), no infinite sequence of moves is possible: after finitely many moves a
terminal board is reached. This is the **monovariant / infinite-descent** principle
(`knowledge_base.md`, "Invariant / monovariant"; "Infinite descent"). ∎ (Termination)

---

### Step 5 (at most one survivor)

By the definition of a move, a move is possible if and only if there exist two distinct
slots i ≠ j with b_i > 1 and b_j > 1, i.e. if and only if K ≥ 2. Contrapositively, a
terminal board (no move possible) has K ≤ 1, that is, at most one slot holds a value > 1.
This is purely the move-legality rule and needs nothing else. ∎ (Step 5)

---

### Step 6 (Lemma C: at least one survivor — non-collapse)

**Lemma C.** Every move leaves at least one active slot among the whole board; more
precisely, the board never becomes all-1s. Consequently a terminal board reached from a
starting board with K ≥ 1 has K ≥ 1.

Proof. Consider a single move on m, n (both > 1) producing g, ℓ. Their product is
    g · ℓ = gcd(m,n) · lcm(m,n)/gcd(m,n) = lcm(m,n) ≥ max(m,n) > 1,
using lcm(m,n) ≥ max(m,n) (each of m, n divides lcm(m,n), so lcm(m,n) is a positive
multiple of each, hence ≥ each). Since g·ℓ > 1, the two outputs g, ℓ are not both equal to
1 (if both were 1 their product would be 1). Hence after the move at least one of slots i,
j is active. Therefore each move keeps K ≥ 1: indeed K counts active slots over the whole
board, and immediately after a move at least one of the two touched slots is active, so
K ≥ 1.

Initial board: all n = 2026 entries exceed 1, so K = n ≥ 1 initially. As shown, every move
keeps K ≥ 1, so at every board reached — in particular the terminal one — we have K ≥ 1.
(Equivalently: the board can never be all 1s, because that would require a last move
producing two 1-outputs, impossible since g·ℓ > 1.) ∎ (Lemma C)

---

### Step 7 (Part (a))

By Termination (Step 4) any sequence of moves halts at a terminal board after finitely
many moves. By Step 5 a terminal board has K ≤ 1, and by Lemma C (Step 6) it has K ≥ 1.
Hence K = 1: exactly one slot holds a value > 1. This proves part (a), for every sequence
of Confucius's choices. ∎ (a)

Remark. Nothing above used n = 2026 beyond "n ≥ 2 finite and all initial entries > 1"; the
statement holds for any starting board of ≥ 2 integers each greater than 1.

---

### Step 8 (Value of the survivor and Part (b))

Fix any legal sequence of moves and let the terminal board be B* = (b*_1,…,b*_n). By part
(a) exactly one slot, say slot s, has b*_s = M > 1, and every other slot holds 1.

Fix a prime p. The terminal p-exponent multiset E*_p = (v_p(b*_1),…,v_p(b*_n)) has
v_p(b*_k) = v_p(1) = 0 for all k ≠ s, and v_p(b*_s) = v_p(M) =: e_p at the single active
slot. Thus E*_p consists of one value e_p together with n−1 = 2025 zeros. Its gcd is
    gcd(E*_p) = gcd( e_p, 0, 0, …, 0 ) = e_p,
by repeated application of (G0) (gcd(0,x) = x): combining the 2025 zeros first gives
gcd of zeros = 0, and gcd(e_p, 0) = e_p. (Note this holds uniformly whether e_p > 0 or
e_p = 0.)

Crucially, all nonzero p-exponents of the terminal board live in this **same** slot s for
every prime p: there is only one slot with value > 1 (part (a)), and any slot holding 1 has
v_p = 0 for all p. So we do not need to prove separately that different primes concentrate
on the same slot — it is forced by K = 1.

By Lemma A (Step 3), g_p = gcd(E_p) is invariant under every move, so its terminal value
equals its initial value:
    e_p = gcd(E*_p) = g_p = gcd( v_p(b_1),…,v_p(b_n) )   (initial board).
Therefore, for every prime p, v_p(M) = e_p = g_p, and since M is determined by its prime
exponents (unique factorization),
    M = ∏_p p^{v_p(M)} = ∏_p p^{g_p}.
Primes p with g_p = 0 (those dividing no initial entry, or with min-structure making the
exponent gcd 0) contribute a factor p^0 = 1 and are harmless; only finitely many primes
have g_p > 0 (each such p divides every initial entry, and there are finitely many primes
below max_k b_k), so the product is a finite well-defined integer.

The right-hand side ∏_p p^{g_p} is computed entirely from the **initial** board and does
not reference the sequence of moves at all. Hence M is the same for every legal sequence
of Confucius's choices. This proves part (b). ∎ (b)

---

### Concrete verification of the closed form

Take the board {12, 18, 20} (n = 3; the mechanism is identical to n = 2026). Valuations:
    12 = 2^2·3,  18 = 2·3^2,  20 = 2^2·5.
Exponent multisets: E_2 = (2,1,2), E_3 = (1,2,0), E_5 = (0,0,1), all other primes give
all-zero multisets. Their gcds:
    g_2 = gcd(2,1,2) = 1,  g_3 = gcd(1,2,0) = 1,  g_5 = gcd(0,0,1) = 1,
so the predicted survivor is M = 2^1·3^1·5^1 = 30.

Check by one explicit play:
    [12, 18, 20] → (act on 12,18: g=6, ℓ=6) → [6, 6, 20]
                 → (act on 6,6:  g=6, ℓ=1) → [6, 1, 20]
                 → (act on 6,20: g=2, ℓ=30) → [2, 1, 30]
                 → (act on 2,30: g=2, ℓ=15) → [2, 1, 15]
                 → (act on 2,15: g=1, ℓ=30) → [1, 1, 30].
Terminal survivor = 30, matching M = ∏_p p^{g_p} = 30. (A brute-force check over 2000
random play orders on this board every time returned exactly the single survivor 30,
consistent with part (b); the proof above establishes this for all boards and all plays.)

Note also the caution that M ≠ gcd(a_1,…,a_n) in general: for the board {4, 8},
gcd(4,8) = 4, but E_2 = (2,3) gives g_2 = gcd(2,3) = 1, so the invariant predicts
M = 2^1 = 2, not 4. A play confirms this:
    [4, 8] → (act on 4,8: g = gcd = 4, ℓ = lcm/gcd = 8/4 = 2) → [4, 2]
           → (act on 4,2: g = 2, ℓ = 4/2 = 2) → [2, 2]
           → (act on 2,2: g = 2, ℓ = 1) → [2, 1].
Here Ω_total starts at Ω(4)+Ω(8) = 2+3 = 5 and drops by Ω(gcd) at each move: the three
gcds are 4, 2, 2 with Ω = 2, 1, 1, so Ω_total goes 5 → 3 → 2 → 1, forcing termination by
Lemma B; the survivor is 2 = ∏_p p^{g_p} ≠ 4 = gcd, as predicted. ∎

∎

## Promotable lemmas

- **Lemma A (per-prime gcd invariant).** For each prime p, g_p = gcd of the p-adic
  valuations of all board entries is unchanged by every move (a,b)↦(min(a,b),
  max(a,b)−min(a,b)). Proved in full in Step 3 via the Euclidean identity (E, Step 2) and
  gcd-associativity gcd(A⊔B)=gcd(gcd A, gcd B) with the convention gcd(0,x)=x.
- **Lemma B (lexicographic monovariant / termination).** (Ω_total, K) strictly decreases
  lexicographically under every move (Ω_total drops by Ω(gcd(m,n)) when gcd>1, else K drops
  by 1), so the process terminates. Proved in full in Step 4, key identity
  Ω(g)+Ω(ℓ)=Ω(m)+Ω(n)−Ω(gcd(m,n)).
- **Lemma C (non-collapse).** g·ℓ = lcm(m,n) > 1, so a move's two outputs are never both 1;
  the board never becomes all-1s. Proved in full in Step 6.
- **Closed form.** M = ∏_p p^{g_p} with g_p = gcd(v_p(a_1),…,v_p(a_n)) over the initial
  board. Proved in Step 8; verified on {12,18,20}→30.
