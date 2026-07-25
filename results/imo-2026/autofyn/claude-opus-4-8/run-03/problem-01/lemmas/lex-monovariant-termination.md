# Lemma: lexicographic monovariant (Ω_total, K) — termination

**Statement.** For a board define Ω_total = Σ_k Ω(b_k) (Ω = number of prime factors with
multiplicity) and K = #{k : b_k > 1}. Every legal move (m,n>1 ↦ gcd, lcm/gcd) strictly
decreases (Ω_total, K) in the lexicographic order; hence every sequence of moves is finite.

**Proof.** Since gℓ=lcm(m,n) and lcm·gcd=mn with Ω completely additive,
Ω(g)+Ω(ℓ)=Ω(m)+Ω(n)−Ω(gcd(m,n)), so Ω_total changes by −Ω(gcd(m,n))≤0.
- gcd(m,n)>1: Ω(gcd)≥1, first coordinate strictly drops (covers m=n>1: g=m, ℓ=1).
- gcd(m,n)=1: Ω_total unchanged, ℓ=mn>1 active while g=1 inactive, so K drops by exactly 1.
(ℤ_{≥0}×{0,…,n}, lex) is well-ordered, so no infinite strictly decreasing sequence. ∎

**Certified** (proof-reviewer, round 1): correct, coprime case verified ([2,3]→[1,6], K
drops). Proved in per-prime-gcd-invariant (Step 4) and strong-induction-descent (§2–§3).
