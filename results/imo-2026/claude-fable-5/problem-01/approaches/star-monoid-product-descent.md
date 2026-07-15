# Approach: star-monoid-product-descent

## Status
solved

## Approaches tried
- (round 1) Skeleton opened by proof-outliner; not yet built.
- (round 1, build) Filled the skeleton into a complete proof of both (a) and (b). Every gap closed: the multiset-gcd characterization and the subtractive-Euclid identity are proved from scratch (strong induction on the sum, all zero cases covered); Φ is defined order-free via common-divisor sets, so no generalized-associativity hand-wave is needed while the ⋆-monoid structure is still established; the lex (P, N) descent is written with the concrete finiteness argument (P at least halves on each gcd>1 move, N strictly drops on each gcd=1 move); "exactly one" is settled by Φ(terminal) = Φ(initial) ≥ 2 versus Φ(all-ones) = 1. The outline-reviewer's three builder notes (gcd=1 forces m ≠ n; concrete well-foundedness; multiset bookkeeping with multiplicity) are all addressed in the text. The dispatch's flagged worry — "could Φ(initial) = 1, e.g. board {2,3}?" — is resolved in Step 4: with the convention gcd(k,0) = k, zero exponents do not lower the multiset gcd, so Φ({2,3}) = 6 and in general Φ ≥ 2 as soon as one entry exceeds 1; the Φ ≥ 2 route stands as designed. — **worked**.

## Current best
Complete proof of (a) and (b) below. No open gaps.

## Route (one paragraph)
Package the invariant as a single commutative-monoid fold, and drive termination with a different engine than prime-gcd-invariant. Define the binary operation m ⋆ n = ∏_p p^{gcd(v_p(m), v_p(n))} on positive integers; it is commutative and associative with identity 1, and the fold Φ(board) = x₁ ⋆ x₂ ⋆ ⋯ ⋆ x₂₀₂₆ is well-defined on multisets (realized order-free via common-divisor sets). The single key identity m ⋆ n = gcd(m,n) ⋆ (lcm(m,n)/gcd(m,n)) (per prime: gcd(a,b) = gcd(min(a,b), |a−b|)) makes Φ invariant under every move. Part (a): termination by strict lex decrease of (P, N) with P = ∏ xᵢ and N = #{entries > 1}; "exactly one" because an all-1 terminal board would have Φ = 1, contradicting Φ = Φ(initial) ≥ 2. Part (b): M = Φ(terminal) = Φ(initial), determined by the start.

## Full proof

Throughout, ℤ≥0 denotes the non-negative integers and ℤ≥1 the positive integers. Tools used by name: the **Fundamental Theorem of Arithmetic** (unique prime factorization; classical), the **invariant / monovariant method** and **infinite descent** (knowledge_base.md, "General Proof Methods — Invariant / monovariant" and "Induction … infinite descent"), **casework / exhaustion** (same section), and elementary **divisor / gcd structure** (knowledge_base.md, "Number Theory — Divisor analysis").

### Step 0. Conventions and divisor sets

For integers d ≥ 1 and a ≥ 0, we say **d divides a** (written d | a) if a = dc for some integer c. In particular **every positive integer divides 0**. For a ∈ ℤ≥0 let

- D(a) := { d ∈ ℤ≥1 : d | a } be its set of positive divisors, so **D(0) = ℤ≥1** (all positive integers), and for a ≥ 1 the set D(a) is finite with largest element a (every divisor d of a ≥ 1 satisfies d ≤ a).

For a finite multiset A of elements of ℤ≥0 (repetitions allowed), let

- CD(A) := { d ∈ ℤ≥1 : d | a for every a ∈ A } = ⋂_{a ∈ A} D(a) be its set of **common divisors**, with the convention CD(∅) = ℤ≥1 (an empty intersection inside ℤ≥1).

Note that CD(A) depends only on the multiset A (indeed only on its underlying set), never on any ordering, and 1 ∈ CD(A) always.

**Observation 0.1.** CD(A) = ℤ≥1 if and only if every element of A is 0.
*Proof.* If every element is 0, every d ≥ 1 divides every element, so CD(A) = ℤ≥1. Conversely, if some a ∈ A satisfies a ≥ 1, then every d ∈ CD(A) divides a, hence d ≤ a; so a + 1 ∉ CD(A) and CD(A) ≠ ℤ≥1. ∎

For a prime p and an integer m ≥ 1, let v_p(m) denote the exponent of p in the prime factorization of m, i.e. the largest k ∈ ℤ≥0 with p^k | m. By the Fundamental Theorem of Arithmetic:

- (FTA-1) m = ∏_p p^{v_p(m)}, a finite product: v_p(m) = 0 for every prime p > m, since p | m and m ≥ 1 would force p ≤ m.
- (FTA-2) Two positive integers are equal if and only if v_p takes the same value on both for every prime p.
- (FTA-3) Conversely, any assignment p ↦ e_p ∈ ℤ≥0 with e_p = 0 for all but finitely many p is the exponent vector of the (unique) positive integer ∏_p p^{e_p}.
- (FTA-4) m = 1 if and only if v_p(m) = 0 for every prime p; equivalently, m > 1 if and only if some prime divides m.

### Step 1. Exponent laws for products, gcd and lcm

**Lemma 1.** Let m, n ∈ ℤ≥1 and let p range over primes. Write a = v_p(m), b = v_p(n).

1. v_p(mn) = a + b.
2. m | n if and only if v_p(m) ≤ v_p(n) for every prime p.
3. gcd(m,n) (the greatest common divisor) and lcm(m,n) (the least common multiple) exist and satisfy v_p(gcd(m,n)) = min(a,b) and v_p(lcm(m,n)) = max(a,b). Moreover, for d ∈ ℤ≥1: d | m and d | n ⟺ d | gcd(m,n); and lcm(m,n) divides every common multiple of m and n.
4. gcd(m,n) · lcm(m,n) = m · n.
5. gcd(m,n) | lcm(m,n), and v_p( lcm(m,n)/gcd(m,n) ) = max(a,b) − min(a,b) = |a − b|.

*Proof.*

(1) Multiplying the factorizations of m and n (FTA-1) gives a factorization of mn with exponent a + b at p; by uniqueness (FTA-2/3) this is v_p(mn).

(2) If m | n, write n = mc with c ∈ ℤ≥1; by (1), v_p(n) = v_p(m) + v_p(c) ≥ v_p(m) for every p. Conversely, if v_p(m) ≤ v_p(n) for all p, set c := ∏_p p^{v_p(n) − v_p(m)}; all exponents are in ℤ≥0 and all but finitely many are 0, so c ∈ ℤ≥1 by (FTA-3), and mc has exponent v_p(n) at every p by (1), hence mc = n by (FTA-2). So m | n.

(3) Let g := ∏_p p^{min(a,b)} and ℓ := ∏_p p^{max(a,b)} (both are positive integers by (FTA-3): the exponents vanish whenever p ∤ mn, hence for all but finitely many p). By (2), g | m and g | n, so g is a common divisor; and if d ∈ ℤ≥1 divides both m and n, then v_p(d) ≤ a and v_p(d) ≤ b for all p by (2), i.e. v_p(d) ≤ min(a,b), so d | g by (2) — in particular d ≤ g. Hence g is the greatest common divisor, gcd(m,n) = g, and the common divisors of m, n are exactly the divisors of g. Dually, by (2), m | ℓ and n | ℓ, so ℓ is a common multiple; and any common multiple L ∈ ℤ≥1 has v_p(L) ≥ max(a,b) for all p by (2), so ℓ | L and in particular ℓ ≤ L. Hence ℓ is the least common multiple, lcm(m,n) = ℓ.

(4) For every p, v_p(gcd·lcm) = min(a,b) + max(a,b) = a + b = v_p(mn), using (1) and (3); the first equality holds because {min(a,b), max(a,b)} = {a, b} as multisets. By (FTA-2), gcd·lcm = mn.

(5) min(a,b) ≤ max(a,b) for every p, so gcd | lcm by (2) and (3). Write lcm = gcd · q with q ∈ ℤ≥1; by (1), v_p(q) = v_p(lcm) − v_p(gcd) = max(a,b) − min(a,b). Finally max(a,b) − min(a,b) = |a − b|: if a ≥ b this is a − b = |a − b|, and if a < b it is b − a = |a − b|. ∎

### Step 2. The gcd of a finite multiset of non-negative integers

**Lemma 2 (multiset gcd).** For every finite multiset A of elements of ℤ≥0 there is a **unique** g ∈ ℤ≥0 with CD(A) = D(g). We write g = G(A). Moreover:

1. G(∅) = 0 and G({a}) = a.
2. G(A) = 0 if and only if every element of A is 0 (in particular G(A) ≥ 1 as soon as A contains a non-zero element).
3. G depends only on the multiset A; and if CD(A) = CD(B) for two finite multisets, then G(A) = G(B).
4. For m, n ∈ ℤ≥1, G({v_p(m), v_p(n)}) is defined for each prime p, and the **pair conventions** hold: G({a, 0}) = a, G({0,0}) = 0, and for a, b ≥ 1, G({a,b}) is the ordinary greatest common divisor gcd(a,b). (We freely write gcd(a,b) := G({a,b}) for a, b ∈ ℤ≥0; this is the convention "gcd(k,0) = k, gcd(0,0) = 0".)

*Proof.*

**Uniqueness.** Suppose D(g) = D(g′) with g, g′ ∈ ℤ≥0. If g = 0 then D(g) = ℤ≥1 is infinite; if g ≥ 1 then D(g) is finite. So g = 0 forces g′ = 0. If g, g′ ≥ 1, then g ∈ D(g) = D(g′) gives g | g′, and symmetrically g′ | g, so g = g′ (both positive).

**Existence for pairs.** Claim: for all x, y ∈ ℤ≥0 there is g ∈ ℤ≥0 with D(x) ∩ D(y) = D(g). We prove this by strong induction on x + y.
- If y = 0: D(x) ∩ D(0) = D(x) ∩ ℤ≥1 = D(x); take g = x. Symmetrically if x = 0, take g = y. (This covers the base x + y = 0 and every case where one entry vanishes.)
- If x, y ≥ 1, assume without loss of generality x ≥ y (the statement is symmetric in x, y). Then
  D(x) ∩ D(y) = D(x − y) ∩ D(y):
  indeed if d | x and d | y then d | x − y (x − y = d·(x/d − y/d) with integer cofactors); and if d | x − y and d | y then d | (x − y) + y = x. Since (x − y) + y = x < x + y (because y ≥ 1), the strong induction hypothesis applies to the pair (x − y, y) and yields g with D(x − y) ∩ D(y) = D(g). ∎(claim)

**Existence in general**, by induction on the size |A|. If |A| = 0: CD(∅) = ℤ≥1 = D(0). If |A| = 1, say A = {a}: CD(A) = D(a). For the step, write A = A₀ ⊎ {a} (multiset union; |A₀| = |A| − 1). Then CD(A) = CD(A₀) ∩ D(a) = D(g₀) ∩ D(a) for g₀ := G(A₀) by the induction hypothesis, and D(g₀) ∩ D(a) = D(g) for some g by the pair claim. So CD(A) = D(g) and G(A) := g exists.

**Properties.** (1) was shown in the base cases. (2): By Observation 0.1, every element of A is 0 iff CD(A) = ℤ≥1 iff D(G(A)) = ℤ≥1 iff G(A) = 0 (using D(g) finite for g ≥ 1). (3): CD(A) depends only on the multiset, and G(A) is determined by CD(A) via uniqueness. (4): the pair values are the base cases above; for a, b ≥ 1, D(a) ∩ D(b) = D(G({a,b})) says exactly that the common divisors of a and b are the divisors of G({a,b}), and since G({a,b}) divides itself it is a common divisor, while every common divisor d satisfies d | G({a,b}), hence d ≤ G({a,b}); so G({a,b}) is the greatest common divisor. ∎

**Lemma 3 (subtractive Euclid identity, with zero cases).** For all a, b ∈ ℤ≥0:
G({a, b}) = G({min(a,b), |a − b|}).

*Proof.* Both sides are symmetric in a and b — the inputs {a,b} and {min(a,b), |a−b|} are unchanged when a and b are swapped — so assume without loss of generality a ≥ b. Then min(a,b) = b and |a − b| = a − b, and the claim reads G({a, b}) = G({b, a − b}). By Lemma 2(3) it suffices to prove CD({a,b}) = CD({b, a−b}), i.e. D(a) ∩ D(b) = D(b) ∩ D(a − b). This is exactly the two-way divisibility argument from the proof of Lemma 2 when a ≥ b ≥ 1 (d | a, d | b ⟹ d | a − b; d | b, d | a − b ⟹ d | a), and it also holds when b = 0: then both sides equal D(a) ∩ ℤ≥1 = D(a) (note a − 0 = a). The case a = b is included: then {b, a − b} = {a, 0} and D(a) ∩ D(a) = D(a) = D(a) ∩ D(0). ∎

**Lemma 4 (splitting off a pair).** Let T be a finite multiset of elements of ℤ≥0 (possibly empty) and a, b ∈ ℤ≥0. Then
G( {a, b} ⊎ T ) = G( {G({a,b})} ⊎ T ),
where ⊎ is multiset union (multiplicities add).

*Proof.* CD({a,b} ⊎ T) = D(a) ∩ D(b) ∩ CD(T) = D(G({a,b})) ∩ CD(T) = CD({G({a,b})} ⊎ T), using Lemma 2 for the middle equality. Equal common-divisor sets give equal G by Lemma 2(3). ∎

### Step 3. The ⋆-monoid and the fold Φ

**Definition.** For m, n ∈ ℤ≥1 define
m ⋆ n := ∏_p p^{ G({v_p(m), v_p(n)}) } ,
the product over all primes p. This is a well-defined positive integer: if p divides neither m nor n then v_p(m) = v_p(n) = 0 and the exponent is G({0,0}) = 0 (Lemma 2(4)); so only the finitely many primes dividing mn contribute, and (FTA-3) applies. By (FTA-2/3),
v_p(m ⋆ n) = G({v_p(m), v_p(n)}) for every prime p.  (⋆-exp)

**Lemma 5 ((ℤ≥1, ⋆, 1) is a commutative monoid).**
1. (Commutativity) m ⋆ n = n ⋆ m for all m, n ∈ ℤ≥1.
2. (Associativity) (m ⋆ n) ⋆ k = m ⋆ (n ⋆ k) for all m, n, k ∈ ℤ≥1.
3. (Identity) 1 ⋆ n = n ⋆ 1 = n for all n ∈ ℤ≥1.

*Proof.* Fix a prime p and write a = v_p(m), b = v_p(n), c = v_p(k).

(1) v_p(m ⋆ n) = G({a,b}) = G({b,a}) = v_p(n ⋆ m) by (⋆-exp) and Lemma 2(3) (the multiset {a,b} is unordered). By (FTA-2) the integers are equal.

(2) By (⋆-exp) twice, v_p((m ⋆ n) ⋆ k) = G({G({a,b}), c}) = G({G({a,b})} ⊎ {c}) = G({a, b, c}) by Lemma 4 with T = {c}. Symmetrically, v_p(m ⋆ (n ⋆ k)) = G({a, G({b,c})}) = G({a} ⊎ {G({b,c})}) = G({a, b, c}) by Lemma 4 with T = {a} (and commutativity of ⊎). The exponent vectors agree at every p, so the integers are equal by (FTA-2).

(3) v_p(1 ⋆ n) = G({0, b}) = b = v_p(n) by Lemma 2(4); apply (FTA-2), and use (1) for n ⋆ 1. ∎

**Definition (the fold Φ).** For a finite non-empty multiset S = {x₁, …, x_k} of positive integers, define for each prime p the exponent multiset A_p(S) := {v_p(x) : x ∈ S} (a multiset of k non-negative integers, with multiplicity), and set
Φ(S) := ∏_p p^{ G(A_p(S)) } .
This is a well-defined positive integer: if p divides no x ∈ S, then A_p(S) is all-zero and G(A_p(S)) = 0 by Lemma 2(2); so only the finitely many primes dividing x₁⋯x_k contribute, and (FTA-3) applies. Moreover
v_p(Φ(S)) = G(A_p(S)) for every prime p.  (Φ-exp)

Φ is manifestly well-defined on **multisets** — A_p(S) and hence G(A_p(S)) (Lemma 2(3)) depend only on the multiset S, with multiplicities, and on no ordering. Φ is exactly the ⋆-fold of S: Φ({m}) = m, since G({v_p(m)}) = v_p(m) (Lemma 2(1)) and (FTA-1) applies; and Φ(S ⊎ {y}) = Φ(S) ⋆ y, because for each prime p, v_p(Φ(S) ⋆ y) = G({G(A_p(S)), v_p(y)}) by (⋆-exp) and (Φ-exp), and CD({G(A_p(S)), v_p(y)}) = D(G(A_p(S))) ∩ D(v_p(y)) = CD(A_p(S)) ∩ D(v_p(y)) = CD(A_p(S) ⊎ {v_p(y)}) = CD(A_p(S ⊎ {y})) (the second equality by Lemma 2's characterization CD(A_p(S)) = D(G(A_p(S)))), so G({G(A_p(S)), v_p(y)}) = G(A_p(S ⊎ {y})) = v_p(Φ(S ⊎ {y})) by Lemma 2(3) and (Φ-exp); conclude Φ(S ⊎ {y}) = Φ(S) ⋆ y by (FTA-2). By Lemma 5 the fold order is immaterial, consistently with the order-free definition. (Only the order-free definition and Lemma 4 are used below; the monoid structure is what makes the definition natural.)

### Step 4. Φ is invariant under moves, and its extreme values

A **board** is a multiset of 2026 positive integers (we track the 2026 positions; the moves below replace exactly two entries and leave the other 2024 untouched, so the board size stays 2026). A **move** on a board S: choose two entries m > 1 and n > 1 at different positions, and replace them by gcd(m,n) and lcm(m,n)/gcd(m,n). By Lemma 1(3) and 1(5) both replacements are positive integers, so the result S′ is again a board. As multisets,
S′ = ( S ∖ {m, n} ) ⊎ { gcd(m,n), lcm(m,n)/gcd(m,n) },
where S ∖ {m,n} removes one copy of m and one copy of n (the two chosen positions).

**Lemma 6 (invariance).** For every move, Φ(S′) = Φ(S).

*Proof.* Fix a prime p; write a = v_p(m), b = v_p(n), and let T := A_p(S ∖ {m,n}) be the multiset of p-exponents of the 2024 untouched entries. Then
A_p(S) = {a, b} ⊎ T, and A_p(S′) = {min(a,b), |a−b|} ⊎ T,
because v_p(gcd(m,n)) = min(a,b) and v_p(lcm(m,n)/gcd(m,n)) = |a − b| by Lemma 1(3) and 1(5), and the other entries are unchanged. Now
G(A_p(S)) = G({a,b} ⊎ T) = G({G({a,b})} ⊎ T)   (Lemma 4)
        = G({G({min(a,b), |a−b|})} ⊎ T)   (Lemma 3)
        = G({min(a,b), |a−b|} ⊎ T) = G(A_p(S′))   (Lemma 4 again).
So v_p(Φ(S)) = v_p(Φ(S′)) for every prime p by (Φ-exp), and Φ(S) = Φ(S′) by (FTA-2). ∎

**Lemma 7 (extreme values of Φ).** Let S be a board.
1. If some entry x ∈ S satisfies x > 1, then Φ(S) ≥ 2.
2. If every entry of S equals 1, then Φ(S) = 1.
3. If S = {M, 1, 1, …, 1} with M ≥ 1 (one entry M and 2025 entries 1), then Φ(S) = M.

*Proof.*
1. By (FTA-4) some prime p divides x, i.e. v_p(x) ≥ 1. Then A_p(S) contains the non-zero element v_p(x), so G(A_p(S)) ≥ 1 by Lemma 2(2). Hence p | Φ(S) by (Φ-exp) and Lemma 1(2), so Φ(S) ≥ p ≥ 2.
2. All exponent multisets are all-zero, so G(A_p(S)) = 0 for every p (Lemma 2(2)) and Φ(S) = ∏_p p⁰ = 1.
3. For each prime p, A_p(S) = {v_p(M), 0, 0, …, 0} (2025 zeros). Its common divisors: CD(A_p(S)) = D(v_p(M)) ∩ ℤ≥1 ∩ ⋯ ∩ ℤ≥1 = D(v_p(M)), since D(0) = ℤ≥1. By uniqueness in Lemma 2, G(A_p(S)) = v_p(M). Hence Φ(S) = ∏_p p^{v_p(M)} = M by (FTA-1). (Equivalently: Φ(S) = M ⋆ 1 ⋆ ⋯ ⋆ 1 = M by Lemma 5(3).) ∎

### Step 5. Termination: the lex pair (P, N)

For a board S define
P(S) := ∏_{x ∈ S} x ∈ ℤ≥1  (the product of all 2026 entries) and N(S) := #{ positions of S whose entry is > 1 } ∈ {0, 1, …, 2026}.

**Lemma 8 (effect of a move).** Suppose a move replaces the entries m, n (both > 1) of S by d := gcd(m,n) and q := lcm(m,n)/d, producing S′. Then exactly one of the following two cases occurs, and they are exhaustive and disjoint:

- **Case d ≥ 2.** P(S′) = P(S)/d ≤ P(S)/2 < P(S), and P(S′) is again a positive integer. (This case includes m = n: then d = m ≥ 2 and q = 1.)
- **Case d = 1.** Then m ≠ n, q = mn > 1, P(S′) = P(S), and N(S′) = N(S) − 1.

*Proof.* The cases d ≥ 2 and d = 1 are disjoint and exhaustive since d = gcd(m,n) ∈ ℤ≥1 (Lemma 1(3)).

First, in both cases: the product of the two replaced entries is d · q = d · (lcm/d) = lcm(m,n) = mn/d by Lemma 1(4). All other 2024 entries are unchanged, so
P(S′) = P(S) · (dq)/(mn) = P(S) · (mn/d)/(mn) = P(S)/d.

**Case d ≥ 2.** P(S′) = P(S)/d ≤ P(S)/2 < P(S) (as P(S) ≥ 1 > 0). P(S′) is an integer: d | m by Lemma 1(3), and m | P(S) because P(S) is the product of all entries, one factor of which is m and the rest are positive integers; hence d | P(S), and P(S′) = P(S)/d ∈ ℤ≥1 (positive as a quotient of positive numbers). If moreover m = n, then d = gcd(m,m) = m ≥ 2 (so m = n indeed lands in this case), and q = lcm(m,m)/m = m/m = 1.

**Case d = 1.** If m = n then d = gcd(m,m) = m > 1, a contradiction; so m ≠ n. Here q = lcm(m,n)/1 = mn/d = mn by Lemma 1(4), and mn ≥ 2·2 = 4 > 1 since m, n ≥ 2. P(S′) = P(S)/1 = P(S). For N: among the two replaced positions, S had two entries > 1 (namely m, n), while S′ has exactly one entry > 1 there (q = mn > 1) and one entry equal to 1 (d = 1); every other position is unchanged, so its contribution to N is unchanged. Hence N(S′) = N(S) − 2 + 1 = N(S) − 1. ∎

**Lemma 9 (finiteness).** Every play — every sequence of boards S₀, S₁, S₂, … in which each S_{t+1} is obtained from S_t by a legal move — is finite. Hence, since a move is available whenever one is legal, the process stops after finitely many moves.

*Proof.* Suppose, for contradiction, that an infinite play S₀, S₁, S₂, … exists. By Lemma 8, P(S_{t+1}) ≤ P(S_t) for every t, so the sequence P(S₀) ≥ P(S₁) ≥ ⋯ ≥ 1 is non-increasing and bounded below by 1. Let D := { t : the move S_t → S_{t+1} has gcd ≥ 2 }.

*D is finite.* If t₁ < t₂ < ⋯ < t_k are elements of D, then, chaining the inequalities P(S_{t+1}) ≤ P(S_t) (all t) and P(S_{tᵢ+1}) ≤ P(S_{tᵢ})/2 (Lemma 8, Case d ≥ 2), we get P(S_{t_k+1}) ≤ P(S₀)/2^k. Since P ≥ 1 always, 2^k ≤ P(S₀), i.e. k ≤ log₂ P(S₀). So |D| ≤ log₂ P(S₀) < ∞.

Let T := (max D) + 1 if D ≠ ∅, and T := 0 otherwise. For every t ≥ T the move S_t → S_{t+1} has gcd = 1, so by Lemma 8 (Case d = 1), N(S_{t+1}) = N(S_t) − 1. Then N(S_{T + j}) = N(S_T) − j for every j ≥ 0; taking j = N(S_T) + 1 gives N(S_{T + N(S_T) + 1}) = −1 < 0, contradicting N ≥ 0. (This is infinite descent on the lexicographically ordered pair (P, N) ∈ ℤ≥1 × {0, …, 2026}: the pair strictly decreases at every move — first coordinate strictly in Case d ≥ 2, first coordinate tied and second strictly in Case d = 1 — and the argument just given shows no infinite strictly decreasing sequence exists. Knowledge base: "Invariant / monovariant", "infinite descent".)

Hence no infinite play exists: every play is finite. Since Confucius continues to move while a move is possible, the sequence of boards he produces is a play; being finite, it ends at a board from which he makes no further move, i.e. at a board admitting no legal move (otherwise he would move again). This holds regardless of his choices. ∎

**Lemma 10 (terminal shape).** A board S admits a legal move if and only if N(S) ≥ 2. Consequently a terminal board (one where no move is possible) satisfies N ≤ 1.

*Proof.* If N(S) ≥ 2, there are two different positions with entries m > 1 and n > 1; choosing them is a legal move. If N(S) ≤ 1, then among any two entries at different positions at least one equals 1, so no legal choice of a pair m, n > 1 at different positions exists. ∎

### Step 6. Part (a)

Let S₀ be the initial board: 2026 integers, every entry > 1. By Lemma 9, after finitely many moves — regardless of the choices — the process reaches a terminal board S_f, and by Lemma 10, N(S_f) ≤ 1.

By Lemma 6 applied to each move of the play, Φ(S_f) = Φ(S₀). Since S₀ has an entry > 1 (indeed all 2026 of them), Lemma 7(1) gives Φ(S₀) ≥ 2.

Suppose N(S_f) = 0. Then every entry of S_f equals 1 (all entries are positive integers ≥ 1, and none exceeds 1), so Φ(S_f) = 1 by Lemma 7(2). But Φ(S_f) = Φ(S₀) ≥ 2 — a contradiction. Hence N(S_f) = 1: after finitely many moves, **exactly one** integer M on the blackboard is greater than 1. ∎ (a)

### Step 7. Part (b)

By part (a), the terminal board is S_f = {M, 1, 1, …, 1} with exactly one entry M > 1 and 2025 entries equal to 1. By Lemma 7(3), Φ(S_f) = M. By Lemma 6 (invariance along the whole play),
M = Φ(S_f) = Φ(S₀) = ∏_p p^{ G( { v_p(x) : x ∈ S₀ } ) } ,
the product over the finitely many primes p dividing some initial entry, where the exponent is the gcd (in the multiset sense of Lemma 2, i.e. with gcd(k, 0) = k) of the p-adic valuations of the 2026 initial entries.

The right-hand side depends only on the initial board S₀ and not on any of Confucius's choices. Hence M is the same for every play: **the value of M does not depend on the choices**. Consistently with part (a), this value satisfies M = Φ(S₀) ≥ 2 by Lemma 7(1). ∎ (b)

*(Part (b) uses part (a) only through the shape of the terminal board — that exactly one entry exceeds 1 — which was proved in Step 6 without reference to part (b); there is no circularity.)*

### Remark (sanity check)

For the board {4, 6} (a 2-entry illustration of the invariant; the proof above is stated for 2026 entries but Lemmas 1–8 never use the count): Φ({4,6}) = 2^{gcd(2,1)} · 3^{gcd(0,1)} = 2·3 = 6. The play: {4,6} → {gcd, lcm/gcd} = {2, 6} (Φ = 2^{gcd(1,1)}·3^{gcd(0,1)} = 6) → {2, 3} (gcd(2,6) = 2, lcm/gcd = 6/2 = 3; Φ = 2^{gcd(1,0)}·3^{gcd(0,1)} = 6) → {1, 6} (gcd(2,3) = 1, lcm/gcd = 6). Terminal, M = 6 = Φ, as predicted. The intermediate board {2, 3} also illustrates why Lemma 7(1) holds: zero exponents do not pull the multiset gcd down (gcd(k,0) = k), so Φ({2,3}) = 6 ≥ 2, not 1.

## Promotable lemmas
- **multiset-gcd-characterization** (Lemma 2 above): for every finite multiset A ⊂ ℤ≥0 there is a unique G(A) ∈ ℤ≥0 whose divisor set equals the common-divisor set of A; G(A) = 0 iff A is all-zero; equal common-divisor sets force equal G; pair conventions gcd(k,0) = k, gcd(0,0) = 0. Proved in full in Step 2 (strong induction on the pair sum + induction on |A|). Reusable by prime-gcd-invariant for its 2026-entry multiset gcd bookkeeping. Proposed at `results/imo-2026-01/lemmas/multiset-gcd-characterization.md` (uncertified).
- **euclid-identity-with-zeros** (Lemma 3 above): gcd(a,b) = gcd(min(a,b), |a−b|) on ℤ≥0, all zero cases covered. Proved in Step 2. Proposed at `results/imo-2026-01/lemmas/euclid-identity-with-zeros.md` (uncertified).

## Cases covered (audit trail)
- Move cases: d = gcd(m,n) ≥ 2 (including m = n, where q = 1) vs d = 1 (where m ≠ n is forced and q = mn > 1) — disjoint, exhaustive (Lemma 8).
- Exponent cases in the Euclid identity: a ≥ b vs a < b (by symmetry), b = 0, a = b (Lemma 3).
- Zero cases of the multiset gcd: empty multiset, all-zero multiset, singleton (Lemma 2).
- Terminal N: N = 0 excluded by Φ ≥ 2 vs Φ = 1; N = 1 is the conclusion; N ≥ 2 is non-terminal (Lemmas 7, 10, Step 6).

## Watch out for (kept from skeleton, all handled)
- P alone is not a strict monovariant (coprime moves fix it) — the lex pair (P, N) is load-bearing (Lemmas 8–9).
- Σxᵢ is not monotone — never used.
- Legality is global (m, n > 1); Φ-invariance uses only the global move via per-prime identities, never a "per-prime move" (Lemma 6).
- Shares the subtractive-Euclid identity with prime-gcd-invariant — proved from scratch here (Lemmas 2–3).
