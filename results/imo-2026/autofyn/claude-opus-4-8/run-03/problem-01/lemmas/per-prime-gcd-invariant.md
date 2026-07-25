# Lemma: per-prime gcd of exponents is a move-invariant

**Statement.** For a board (multiset of positive integers), a move replaces two entries
m,n>1 by g=gcd(m,n) and ℓ=lcm(m,n)/gcd(m,n). For each prime p let
g_p = gcd(v_p(b_1),…,v_p(b_n)) (gcd of the p-adic valuations of all entries, with
gcd(0,x)=x, gcd(∅)=0). Then g_p is unchanged by every move, for every prime p. Hence
μ(B) = ∏_p p^{g_p} is a move-invariant.

**Proof.** By (V1)–(V2), a move sends the p-exponent pair (a,b)=(v_p(m),v_p(n)) to
(min(a,b), max(a,b)−min(a,b)) and fixes all other p-exponents. Subtractive-Euclid identity:
gcd(min(a,b),max(a,b)−min(a,b))=gcd(a,b) for all a,b≥0 (common divisors of {a,b} and
{a,b−a} coincide). Multiset-gcd associativity: for a partition E_p = R ⊔ {a,b},
gcd(E_p)=gcd(gcd(R),gcd(a,b)); after the move gcd(gcd(R),gcd(min,max−min)) equals it by the
identity. Edge cases (R empty → gcd(R)=0; zero exponents) are covered by gcd(0,x)=x. ∎

**Certified** (proof-reviewer, round 1): statement correct, no stronger than proved,
independently brute-force verified (20000 boards). Proved in approaches
per-prime-gcd-invariant (Steps 1–3) and strong-induction-descent (§1,§5).
