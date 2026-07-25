## Status
solved

## Approaches tried
- per-prime gcd-of-exponents invariant — **worked (APPROVE)**. p-adic decoupling; per-prime
  action (a,b)↦(min,max−min); exact invariant g_p = gcd of each prime's exponent multiset;
  lex monovariant (Ω_total, K) for termination; non-collapse via lcm>1. Complete proof of
  both parts. Reviewer-verified.
- strong-induction / well-founded descent — **worked (APPROVE)**. Same engine lemmas
  (primewise action, Ω-balance, lex monovariant, non-collapse, per-prime gcd invariant),
  packaged as one strong induction on Φ=(Ω_total,K) carrying μ(B)=∏_p p^{g_p} in the IH so
  order-independence (b) falls out of the IH. Complete and rigorous. Reviewer-verified.

## Current best
Complete proof of both parts. Closed form M = ∏_p p^{g_p} where
g_p = gcd(v_p(a_1),…,v_p(a_2026)) over the initial board — independently brute-force
verified over 20000 random boards (always exactly one survivor equal to the closed form).

## Full proof

Throughout, the **board** is a finite multiset of positive integers, of fixed size
n = 2026, viewed as an ordered tuple (b_1, …, b_n) of *slots* (a slot may hold 1). A
**move** selects two distinct slot indices i ≠ j with b_i > 1 and b_j > 1, sets m := b_i,
n := b_j, and replaces the two entries by

    g := gcd(m, n),   ℓ := lcm(m, n) / gcd(m, n),

leaving every other slot unchanged. Since gcd(m,n) divides lcm(m,n), ℓ is a positive
integer, so the move is well defined. A board is **terminal** if no move is possible.

We prove:

(a) Starting from any board of n = 2026 integers each > 1, every sequence of moves reaches
    a terminal board after finitely many moves, and that terminal board has exactly one
    slot with value > 1.

(b) The value M of that single surviving entry is the same for every legal sequence of
    moves; explicitly, M = ∏_p p^{g_p}, where g_p := gcd(v_p(b_1), …, v_p(b_n)) is computed
    from the **initial** board (v_p = p-adic valuation), hence independent of all choices.

Tools (both in `knowledge_base.md`): **invariant / monovariant** (a conserved quantity for
(b), a strictly monotone quantity for termination in (a)) and **divisor analysis** (p-adic
valuation and gcd/lcm structure).

**Valuation facts.** For a prime p and positive integer x, v_p(x) is the largest k ≥ 0
with p^k ∣ x. For all positive integers m, n:

  (V1)  v_p(gcd(m,n)) = min(v_p(m), v_p(n)),
  (V2)  v_p(lcm(m,n)) = max(v_p(m), v_p(n)).

Proof: put a=v_p(m), b=v_p(n), WLOG a ≤ b. A common divisor d of m,n has v_p(d) ≤ a, and
p^a divides both m,n; applied to every prime, gcd has p-exponent min(a,b), giving (V1).
Since lcm(m,n)=mn/gcd(m,n), additivity of v_p (v_p(xy)=v_p(x)+v_p(y), from unique
factorization) and (V1) give v_p(lcm)=a+b−min(a,b)=max(a,b), which is (V2). ∎

**gcd conventions** (slots not divisible by p contribute exponent 0):
  (G0)  gcd(0,x)=gcd(x,0)=x for x ≥ 0, gcd(0,0)=0 (every integer divides 0).
  (G1)  gcd is associative/commutative on ℤ_{≥0}; for a finite multiset S with partition
        S = A ⊔ B, gcd(S) = gcd(gcd(A), gcd(B)), and gcd(∅)=0. (An integer divides all of
        S iff it divides gcd(S); common divisors of A ⊔ B are exactly common divisors of
        gcd(A) and gcd(B).)

### Step 1 (per-prime action of a move)
Fix a prime p; a move on slots i,j with m=b_i, n=b_j, a:=v_p(m), b:=v_p(n) produces g,ℓ
with, by (V1)–(V2) and additivity,
    v_p(g) = min(a,b),   v_p(ℓ) = max(a,b) − min(a,b) ≥ 0.
All other slots' exponents are unchanged. So on the p-exponent multiset the move replaces
the pair (a,b) by (min(a,b), max(a,b)−min(a,b)) and fixes the rest. This holds for every
prime simultaneously, so the process decouples over primes: each prime p gives a multiset
E_p = (v_p(b_1),…,v_p(b_n)), and a move performs one subtractive step on two of its
entries (and (0,0)↦(0,0) for primes dividing neither m nor n). ∎

### Step 2 (Euclidean identity)
For all integers a,b ≥ 0:  gcd(min(a,b), max(a,b) − min(a,b)) = gcd(a,b).   (E)
Proof: WLOG a ≤ b. If a=0 this is gcd(0,b)=gcd(0,b) by (G0). Otherwise every common
divisor of a,b divides b−a, and every common divisor of a,b−a divides a+(b−a)=b; so
{a,b} and {a,b−a} have the same common divisors, hence the same gcd. (Subtractive Euclid.) ∎

### Step 3 (Lemma A: g_p is an exact invariant)
For each prime p, g_p := gcd(E_p) is unchanged by every move. Proof: a move touches only
positions i,j of E_p, replacing (a,b) by (min(a,b),max(a,b)−min(a,b)) and fixing the
multiset R of the other n−2 exponents. By (G1), gcd(E_p)=gcd(gcd(R),gcd(a,b)); after the
move it is gcd(gcd(R), gcd(min(a,b),max(a,b)−min(a,b))), equal by (E). The n=2 boundary
(R empty, gcd(R)=0, gcd(0,gcd(a,b))=gcd(a,b)) and 0-exponent cases are covered by (G0).
So g_p is invariant for every prime. ∎

### Step 4 (Lemma B: lex monovariant — termination)
Statistics of a board: Ω_total := Σ_k Ω(b_k) with Ω(x)=Σ_p v_p(x) (Ω(1)=0), and
K := #{k : b_k > 1}. Order (Ω_total,K) lexicographically. Every move strictly decreases it.
Proof: only slots i,j change, and since gℓ=lcm(m,n),
    Ω(g)+Ω(ℓ) = Ω(lcm(m,n)) = Ω(m)+Ω(n) − Ω(gcd(m,n))
(using lcm·gcd=mn and complete additivity of Ω), so
    Ω_total,new − Ω_total,old = −Ω(gcd(m,n)) ≤ 0.   (†)
- Case gcd(m,n) > 1: Ω(gcd) ≥ 1, so Ω_total strictly drops; (Ω_total,K) drops
  lexicographically. (Includes m=n>1: g=m>1, ℓ=1, Ω(gcd)=Ω(m)≥1.)
- Case gcd(m,n) = 1: g=1, ℓ=lcm(m,n)=mn>1 (m,n>1). By (†) Ω_total is unchanged; slot i
  becomes 1 (inactive), slot j holds mn>1 (active), so K drops by exactly 1. (Ω_total,K)
  drops lexicographically.
The values lie in ℤ_{≥0}×{0,…,n}, well-ordered by lex (embed via (Ω_total,K) ↦
(n+1)·Ω_total+K into ℕ). A strictly decreasing sequence there is finite, so no infinite
sequence of moves exists: a terminal board is reached after finitely many moves. ∎

### Step 5 (at most one survivor)
A move is possible iff two distinct slots have value > 1, i.e. iff K ≥ 2. So a terminal
board has K ≤ 1: at most one slot exceeds 1. (Pure move-legality.) ∎

### Step 6 (Lemma C: at least one survivor)
For a single move, g·ℓ = lcm(m,n) ≥ max(m,n) > 1 (m,n > 1), so g,ℓ are not both 1; at
least one of slots i,j stays active, so every move keeps K ≥ 1. Initially K=n ≥ 1, hence
every reachable board, in particular the terminal one, has K ≥ 1. The board can never
become all 1s. ∎

### Step 7 (Part (a))
By Step 4 any sequence halts at a terminal board. By Step 5 it has K ≤ 1, by Step 6 K ≥ 1,
so K = 1: exactly one slot exceeds 1, for every sequence of choices. ∎(a)
(Only "n ≥ 2 finite, all initial entries > 1" is used, not n = 2026 specifically.)

### Step 8 (Value of the survivor — Part (b))
Fix a legal play with terminal board B* = (b*_1,…,b*_n); by (a) exactly one slot s has
b*_s = M > 1, all others = 1. Fix a prime p: E*_p is v_p(M) =: e_p at slot s and 0
elsewhere, so gcd(E*_p) = e_p by (G0). By Lemma A (Step 3), g_p is invariant, so
    e_p = gcd(E*_p) = g_p = gcd(v_p(b_1),…,v_p(b_n))  (initial board).
Hence v_p(M) = g_p for every p, and by unique factorization M = ∏_p p^{g_p}. Only finitely
many p have g_p > 0 (each such p divides every initial entry), so the product is a
well-defined integer. Its value is computed entirely from the initial board and does not
reference the moves, so M is the same for every legal sequence of choices. ∎(b)

### Verification
Board {12,18,20}: 12=2²·3, 18=2·3², 20=2²·5, so g_2=gcd(2,1,2)=1, g_3=gcd(1,2,0)=1,
g_5=gcd(0,0,1)=1, predicting M=2·3·5=30. A play [12,18,20]→[6,6,20]→[6,1,20]→[2,1,30]
→[2,1,15]→[1,1,30] gives survivor 30. (Note M ≠ gcd in general: {4,8} gives g_2=gcd(2,3)=1,
M=2, not 4.) An independent brute-force over 20000 random boards, each played to
termination several times, returned exactly one survivor equal to ∏_p p^{g_p} in every
case. ∎
