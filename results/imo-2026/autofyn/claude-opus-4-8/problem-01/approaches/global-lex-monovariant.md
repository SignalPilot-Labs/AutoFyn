# Approach: global-lex-monovariant

## Status
solved

## Approaches tried
- (round 1, new) Global lexicographic monovariant Φ=(N,P) = (#entries >1, product of all entries) for termination (part a), plus the per-prime exponent-gcd invariant g_p for the value of M (part b). **Built and completed in full this round — solved.**

## Current best
Complete proof of both parts, below. Part (a) is proved by the well-founded lexicographic descent of Φ=(N,P); part (b) by the invariance of g_p = gcd of the p-adic valuations across the board. The N=0 terminal case is excluded by importing the g_p invariant (positivity of some initial g_p). No residual gaps.

## Notation and standing facts

A **board** is a multiset of 2026 integers, each ≥ 1. Initially all 2026 entries are > 1. A **move** selects two entries m > 1 and n > 1 occupying different positions and replaces them by
  gcd(m, n)  and  lcm(m, n) / gcd(m, n).
Confucius makes moves as long as at least two entries exceed 1.

For a prime p and an integer x ≥ 1, let v_p(x) denote the p-adic valuation (the exponent of p in the unique prime factorization of x). We use the following standard facts, all consequences of the **Fundamental Theorem of Arithmetic** (unique factorization; see `knowledge_base.md`, "Fundamental Theorem of Arithmetic / Unique Factorization"):

(F1) For every prime p, v_p(gcd(m, n)) = min(v_p(m), v_p(n)) and v_p(lcm(m, n)) = max(v_p(m), v_p(n)).

(F2) gcd(m, n) · lcm(m, n) = m · n. (Because for each p, min(a,b) + max(a,b) = a + b.)

(F3) A positive integer x equals 1 iff v_p(x) = 0 for every prime p.

**The per-move prime-local update rule.** Fix a move that replaces entries m, n by g := gcd(m,n) and ℓ := lcm(m,n)/gcd(m,n). Fix a prime p and write a := v_p(m), b := v_p(n). Then by (F1),
  v_p(g) = min(a, b),   v_p(ℓ) = v_p(lcm(m,n)) − v_p(gcd(m,n)) = max(a, b) − min(a, b) = |a − b|.
(The subtraction is valid because lcm(m,n) is an integer multiple of gcd(m,n), so max ≥ min and the difference of valuations is the valuation of the quotient.) Thus, at the level of p-adic valuations, the move replaces the pair (a, b) at the two chosen positions by (min(a, b), |a − b|), and leaves the p-valuations of all other 2024 positions unchanged. The *choice of which two positions* is a single choice shared by all primes; only the update *rule* is prime-local. We do **not** claim distinct primes evolve independently.

Throughout, gcd of a finite list of nonnegative integers uses the conventions gcd(0, e) = gcd(e, 0) = e and gcd(0, 0) = 0; this is the usual gcd (greatest common divisor, with gcd(0,e)=e since every integer divides 0). gcd is commutative and associative on the nonnegative integers, so gcd of a multiset is well-defined independent of the order of combination.

## Full proof

### Part (a): the process terminates with exactly one entry > 1

Define two quantities of the current board:
- N := #{ positions whose entry is > 1 } (the *count*),
- P := ∏ (all 2026 entries) (the *product*).

Since every entry is ≥ 1 and the board is finite, P is a positive integer, so P ≥ 1.

**Lemma 1 (product update).** A move that chooses m, n multiplies the board product by 1/gcd(m,n). Precisely, P_new = P_old / gcd(m, n). Hence P is non-increasing at every move, and strictly decreases iff gcd(m, n) > 1; it is unchanged iff gcd(m, n) = 1.

*Proof.* All entries except the two chosen ones are unchanged, so their contribution to the product is unaffected. The two chosen entries contribute m·n before the move and g·ℓ = gcd(m,n) · (lcm(m,n)/gcd(m,n)) = lcm(m,n) after it. By (F2), lcm(m,n) = m·n / gcd(m,n). Therefore
  P_new = P_old · (lcm(m,n)) / (m·n) = P_old · (m·n / gcd(m,n)) / (m·n) = P_old / gcd(m,n).
Since gcd(m,n) ≥ 1, P_new ≤ P_old, with equality iff gcd(m,n) = 1 and strict inequality iff gcd(m,n) ≥ 2. As P is a positive integer, P_new = P_old / gcd(m,n) is again a positive integer (indeed the product of the new board of positive integers). ∎

**Lemma 2 (count update).** A move never increases N. Moreover:
- if gcd(m, n) = 1, then N strictly decreases by exactly 1;
- if gcd(m, n) > 1, then N is unchanged or decreases.

*Proof.* Before the move the two chosen positions both hold values > 1, so they contribute 2 to N. After the move they hold g = gcd(m,n) and ℓ = lcm(m,n)/gcd(m,n); all other positions and their contribution to N are unchanged. So the change in N equals (number of the two new values that are > 1) − 2.

Case gcd(m,n) = 1: then g = 1 and ℓ = lcm(m,n)/1 = lcm(m,n) = m·n (by (F2), gcd=1). Since m > 1 and n > 1, ℓ = m·n > 1. So exactly one of the two new values (namely ℓ) exceeds 1. The two positions now contribute 1 to N instead of 2, and all else is unchanged, so N decreases by exactly 1.

Case gcd(m,n) > 1: the number of new values > 1 is at most 2, so N changes by (≤ 2) − 2 ≤ 0; that is, N is unchanged or decreases. ∎

(Remark, per the outline-reviewer: a non-coprime move *can* also drop N — e.g. entries p, p become gcd = p and lcm/gcd = 1, so N drops by 1. This is harmless: any drop in N is a lexicographic decrease of Φ regardless of P, as shown next.)

**Lemma 3 (lexicographic strict descent).** Consider Φ := (N, P) ∈ ℤ_{≥0} × ℤ_{≥1}, ordered lexicographically (compare N first; if equal, compare P). Every move strictly decreases Φ in this order.

*Proof.* Consider any move, with chosen entries m, n.

- If gcd(m, n) = 1: by Lemma 2, N strictly decreases. In the lexicographic order a strict decrease in the first coordinate makes Φ strictly smaller, whatever happens to P (in fact P is unchanged here by Lemma 1). So Φ strictly decreases.
- If gcd(m, n) > 1: by Lemma 2, N is unchanged or decreases. If N decreases, Φ strictly decreases as above. If N is unchanged, then by Lemma 1 (since gcd > 1) P strictly decreases; with N equal and P strictly smaller, Φ strictly decreases in lexicographic order.

In every case Φ strictly decreases. In particular, there is no move that leaves both N and P unchanged: an N-preserving move must have gcd(m,n) > 1 (else Lemma 2 forces N down), and then P strictly drops. ∎

**Lemma 4 (termination).** The process makes only finitely many moves.

*Proof.* The set ℤ_{≥0} × ℤ_{≥1} with the lexicographic order is well-founded, i.e. it has no infinite strictly-decreasing sequence. Indeed, suppose (N_0, P_0) > (N_1, P_1) > … were an infinite strictly-decreasing lex chain. The first coordinates form a non-increasing sequence of nonnegative integers N_0 ≥ N_1 ≥ …, which is bounded below by 0, hence eventually constant, say N_k = N_{k+1} = … = c for all k ≥ K. For indices k ≥ K, since the first coordinates are equal, lexicographic strict descent forces P_k > P_{k+1} for all k ≥ K. Thus P_K > P_{K+1} > … is an infinite strictly-decreasing sequence of positive integers, which is impossible (a strictly decreasing sequence of positive integers has length at most P_K). Contradiction. Hence the lex order is well-founded.

By Lemma 3, the sequence Φ_0 > Φ_1 > Φ_2 > … of values taken by Φ before successive moves is strictly decreasing in this well-founded order, so it cannot be infinite. Therefore only finitely many moves occur.

(Explicit bound, for concreteness: N can drop at most N_0 ≤ 2026 times; between two consecutive N-drops every move keeps N fixed and hence strictly decreases the positive integer P, which can happen at most P_0 − 1 times before another N-drop or termination. So the total number of moves is finite, bounded by roughly (2027)·P_0. We only need finiteness.) ∎

**Lemma 5 (terminal count is 0 or 1).** When the process stops, N ∈ {0, 1}.

*Proof.* By definition, Confucius makes a move whenever at least two entries exceed 1, i.e. whenever N ≥ 2. The process stops exactly when no move is available, i.e. when N < 2, i.e. N ∈ {0, 1}. By Lemma 4 this terminal state is reached after finitely many moves. ∎

It remains to exclude N = 0 (all entries equal to 1). For this we use the invariant established in Part (b) below; there is no circularity, because that invariant (Lemma 6) is proven independently of any termination claim.

**Lemma 5′ (the survivor exceeds 1; N = 1).** The terminal board has exactly one entry > 1.

*Proof.* Since the initial board has all 2026 entries > 1, in particular the first entry x_1 > 1, so by (F3) there is a prime p with e := v_p(x_1) > 0. Consider the invariant g_p := gcd of the p-adic valuations over all 2026 positions of the board (Part (b), Lemma 6, proves g_p is unchanged by every move). Initially the multiset of p-valuations includes the value e > 0, so
  g_p^{initial} = gcd(v_p(x_1), …, v_p(x_{2026})) = gcd(e, other nonnegative values) > 0,
because gcd of a finite list of nonnegative integers is > 0 as soon as the list contains a positive value: any common divisor d of the list divides e, and if the gcd were 0 then (by the convention that gcd = 0 only for the all-zero list, since gcd(0,…,0)=0 and gcd is positive whenever some entry is positive — the gcd of a set containing a positive integer e is a positive divisor of e) we would need every entry to be 0, contradicting e > 0. Hence g_p^{initial} ≥ 1.

By Lemma 6, g_p is invariant, so at the terminal state g_p = g_p^{initial} ≥ 1. If the terminal board were all 1's (N = 0), then every terminal p-valuation would be 0 and g_p would be gcd(0,…,0) = 0, contradicting g_p ≥ 1. Therefore N ≠ 0. Combined with Lemma 5 (N ∈ {0,1}), we get N = 1: exactly one terminal entry exceeds 1. ∎

Lemmas 4, 5, 5′ together prove Part (a): after finitely many moves the process stops (Lemma 4), and the terminal board has exactly one entry M > 1 (Lemma 5′), regardless of Confucius's choices. ∎ (Part a)

### Part (b): the value of M is independent of the choices

**Lemma 6 (per-prime valuation-gcd is invariant).** Fix a prime p. For a board with p-adic valuations (e_1, …, e_{2026}) at its 2026 positions, define
  g_p := gcd(e_1, e_2, …, e_{2026})
(with conventions gcd(0, e) = e, gcd(0, …, 0) = 0). Then g_p is unchanged by every move.

*Proof.* We first prove the two-variable subtractive identity, then lift it to the whole multiset.

*(B1) Subtractive gcd identity.* For all integers a, b ≥ 0,
  gcd( min(a, b), |a − b| ) = gcd(a, b).
We check all cases:
- If a = b: then min(a,b) = a and |a − b| = 0, so the left side is gcd(a, 0) = a, and the right side is gcd(a, a) = a. Equal.
- If a = 0 (and b arbitrary ≥ 0): min(0, b) = 0 and |0 − b| = b, so the left side is gcd(0, b) = b, and the right side is gcd(0, b) = b. Equal. Symmetrically for b = 0.
- If a > b ≥ 0 (WLOG by symmetry of both sides in a, b — note min(a,b), |a−b|, and gcd(a,b) are all symmetric): then min(a,b) = b and |a − b| = a − b, so the left side is gcd(b, a − b). By the standard Euclidean subtraction identity gcd(b, a − b) = gcd(b, a) = gcd(a, b) (since a common divisor of b and a−b divides their sum a, and a common divisor of a and b divides a−b; so the two pairs have identical common-divisor sets, hence equal gcd). Equal. The case b > a follows by symmetry.
This exhausts all a, b ≥ 0 (either a = b, or one is 0, or a > b > 0, or b > a > 0), proving (B1).

*(B2) Lifting to the multiset.* A move changes the board's p-valuation multiset only at the two chosen positions, replacing the pair (a, b) there by (min(a,b), |a−b|), and leaves the remaining 2024 valuations, call their multiset R, untouched. By associativity and commutativity of gcd over the nonnegative integers, for any nonnegative integers a, b and any finite list R,
  gcd(a, b, R) = gcd( gcd(a, b), R ).
(Here gcd(a, b, R) means the gcd of the combined list; associativity lets us group the first two terms.) Therefore the board's total valuation-gcd before the move is
  g_p^{before} = gcd( gcd(a, b), R ),
and after the move it is
  g_p^{after} = gcd( gcd(min(a,b), |a−b|), R ).
By (B1), gcd(min(a,b), |a−b|) = gcd(a, b), so g_p^{before} = g_p^{after}. Thus g_p is unchanged by every move.

(The zero-exponent boundary is handled uniformly by the conventions: R may contain zeros, and (B1) already covers a = 0, b = 0, a = b. The identity gcd(0, e) = e is exactly the statement that a position holding an entry with p-valuation 0 contributes nothing to the gcd, consistent with such entries possibly being 1.) ∎

Being unchanged by every move, g_p is constant throughout the process and equals its initial value g_p^{initial} = gcd(v_p(x_1), …, v_p(x_{2026})), which depends only on the starting board.

**Lemma 7 (reading off M).** Let M be the unique terminal entry > 1 guaranteed by Part (a). Then, for every prime p,
  v_p(M) = g_p^{initial} = gcd(v_p(x_1), …, v_p(x_{2026})),
and hence
  M = ∏_p p^{ g_p^{initial} }.

*Proof.* By Part (a), the terminal board is (M, 1, 1, …, 1) up to reordering: one entry equals M and the other 2025 entries equal 1. Fix a prime p. The terminal p-valuation multiset is (v_p(M), v_p(1), …, v_p(1)) = (v_p(M), 0, 0, …, 0). Its gcd is
  gcd(v_p(M), 0, …, 0) = v_p(M),
by the convention gcd(e, 0) = e applied 2025 times. By Lemma 6 this terminal gcd equals the invariant value g_p, which equals g_p^{initial}. Hence v_p(M) = g_p^{initial}.

Only finitely many primes p have g_p^{initial} > 0 (indeed g_p^{initial} = 0 for every prime p not dividing any initial entry, since then all v_p(x_i) = 0). So the product ∏_p p^{g_p^{initial}} is a well-defined positive integer, and by (F3)/unique factorization an integer is determined by its valuations at all primes. Since v_p(M) = g_p^{initial} for every p, we conclude M = ∏_p p^{g_p^{initial}}. ∎

The right-hand side ∏_p p^{g_p^{initial}} = ∏_p p^{gcd(v_p(x_1),…,v_p(x_{2026}))} depends only on the initial multiset {x_1, …, x_{2026}}, not on the sequence of moves Confucius performs. Therefore M is the same for every valid play. This proves Part (b). ∎ (Part b)

### Conclusion
Part (a): every play terminates (Lemma 4) in a state with exactly one entry M > 1 (Lemmas 5, 5′). Part (b): that entry is M = ∏_p p^{ gcd(v_p(x_1), …, v_p(x_{2026})) }, a function of the initial board alone (Lemmas 6, 7), so it is independent of Confucius's choices. ∎

## Promotable lemmas
- **Lemma 6 (per-prime valuation-gcd invariant):** For the gcd/lcm move (m,n) ↦ (gcd(m,n), lcm(m,n)/gcd(m,n)), the quantity g_p = gcd of the p-adic valuations across the whole board is invariant, for every prime p. Proved in full above via the subtractive identity gcd(min(a,b),|a−b|) = gcd(a,b) (all boundary cases a=0,b=0,a=b covered) plus associativity of gcd over a zero-containing multiset.
- **Lemma 1 (product update P_new = P_old/gcd(m,n)) and Lemma 3 (lexicographic descent of Φ=(N,P)):** the termination engine; reusable for any argument needing a well-founded monovariant for this move.
- **Subtractive identity (B1):** gcd(min(a,b), |a−b|) = gcd(a,b) for all a,b ≥ 0. Fully case-checked.
