# imo-2026-01 — Confucius's gcd/lcm blackboard

## Status
solved

## Approaches tried
- global-lex-monovariant — SOLVED (reviewer APPROVE). Termination via well-founded lex descent of Φ=(N,P)=(#entries>1, product); value of M via the per-prime valuation-gcd invariant g_p. Both parts proven, no gaps.
- per-prime-valuation-descent — SOLVED (reviewer APPROVE). Same value invariant; termination via lex descent of (Ω,N)=(total prime-factor count, #entries>1) with an explicit move bound (Ω₀+1)·2026. Independently complete.

## Current best
Complete rigorous proof of both parts. M = ∏_p p^{g_p} where g_p = gcd(v_p(x_1),…,v_p(x_2026)) on the initial board. Verified by simulation (unique survivor, choice-independent value) over 2000 random boards.

## Full proof

### Notation and standing facts
A board is a multiset of 2026 integers ≥ 1 in fixed positions; initially all are > 1. A move selects two positions holding m > 1, n > 1 and replaces them by g = gcd(m,n) and ℓ = lcm(m,n)/gcd(m,n). Moves continue while at least two entries exceed 1. For a prime p and x ≥ 1, v_p(x) is the p-adic valuation. By the Fundamental Theorem of Arithmetic:

(F1) v_p(gcd(m,n)) = min(v_p(m),v_p(n)), v_p(lcm(m,n)) = max(v_p(m),v_p(n)).
(F2) gcd(m,n)·lcm(m,n) = m·n.
(F3) x = 1 iff v_p(x) = 0 for all primes p.

**Per-move prime-local rule.** With a = v_p(m), b = v_p(n): v_p(g) = min(a,b) and v_p(ℓ) = max(a,b) − min(a,b) = |a−b| (the difference is a valuation, so ≥ 0 and ℓ is an integer). Thus per prime the move sends (a,b) ↦ (min(a,b), |a−b|) at the two chosen positions and leaves all other 2024 valuations fixed. The position choice is shared across all primes; only the update rule is prime-local. gcd of a list of nonnegative integers uses gcd(0,e)=e, gcd(0,…,0)=0 (commutative, associative).

### Part (a): the process terminates with exactly one entry > 1

Let N = #{positions with entry > 1} and P = ∏ (all 2026 entries), a positive integer.

**Lemma 1 (product update).** A move gives P_new = P_old/gcd(m,n). Proof: unchanged positions unaffected; the two chosen contribute m·n → g·ℓ = lcm(m,n) = m·n/gcd(m,n) by (F2). So P is non-increasing, strictly decreasing iff gcd(m,n) > 1.

**Lemma 2 (count update).** N never increases. If gcd(m,n) = 1 then g = 1, ℓ = mn > 1, so the two positions go (m,n) both >1 → (1, mn) with exactly one > 1: N drops by exactly 1. If gcd(m,n) > 1, the two new values give at most 2 entries > 1, so N is unchanged or drops.

**Lemma 3 (lex descent).** Order Φ = (N,P) ∈ ℤ_{≥0}×ℤ_{≥1} lexicographically (N primary). Every move strictly decreases Φ: if gcd = 1, N drops (Lemma 2), so Φ drops; if gcd > 1 and N drops, Φ drops; if gcd > 1 and N constant, P strictly drops (Lemma 1), so Φ drops. In particular no move fixes both N and P.

**Lemma 4 (termination).** Lex order on ℤ_{≥0}×ℤ_{≥1} is well-founded: N is non-increasing and bounded below, so eventually constant = c; thereafter Φ-descent forces P strictly decreasing among positive integers, impossible infinitely. By Lemma 3 the sequence of Φ-values strictly descends, hence is finite: finitely many moves.

**Lemma 5 (terminal N ∈ {0,1}).** A move is possible iff N ≥ 2, so termination means N ∈ {0,1}.

**Lemma 5′ (N = 1).** Some initial entry x_1 > 1, so by (F3) there is a prime p with v_p(x_1) > 0; hence the initial g_p = gcd of the p-valuations contains a positive value and is ≥ 1. By the invariant of Part (b) (Lemma 6, proved without any termination claim, so no circularity), g_p stays ≥ 1. If the terminal board were all 1's (N = 0), every terminal p-valuation would be 0 and g_p = 0, a contradiction. Hence N = 1: exactly one terminal entry M > 1.

Lemmas 4, 5′ prove Part (a). ∎

### Part (b): M is independent of the choices

**Lemma 6 (per-prime valuation-gcd invariant).** For each prime p, g_p = gcd(v_p(x_1),…,v_p(x_2026)) is invariant under every move.

*(B1) Subtractive identity.* For all integers a,b ≥ 0, gcd(min(a,b),|a−b|) = gcd(a,b). By symmetry assume a ≥ b; then it reads gcd(b, a−b) = gcd(a,b), which holds since d | a,b ⟺ d | b, a−b (d | b and d | a−b ⟹ d | a; d | a,b ⟹ d | a−b): identical common-divisor sets. Boundaries a=b (gcd(a,0)=a=gcd(a,a)), b=0 (gcd(0,a)=a), a=b=0 (0=0) all covered.

*(B2) Lifting.* A move changes the p-valuation multiset only at the two chosen positions, replacing (a,b) by (min(a,b),|a−b|); call the other 2024 valuations R. By associativity, gcd(a,b,R) = gcd(gcd(a,b),R) and gcd(min,|·|,R) = gcd(gcd(min,|·|),R); by (B1) the inner gcds are equal, so g_p is unchanged. Zero exponents are handled uniformly by gcd(0,e)=e. ∎

Thus g_p equals its initial value g_p^init = gcd(v_p(x_1),…,v_p(x_2026)) throughout.

**Lemma 7 (reading off M).** By Part (a) the terminal board is (M,1,…,1). For each p its valuation multiset is (v_p(M),0,…,0), whose gcd is v_p(M). By Lemma 6 this equals g_p^init. Hence v_p(M) = g_p^init for all p, and by unique factorization
  M = ∏_p p^{ g_p^init } = ∏_p p^{ gcd(v_p(x_1),…,v_p(x_2026)) }.
Only finitely many g_p^init are nonzero (g_p^init = 0 for p dividing no initial entry), so the product is a well-defined integer > 1. The right side depends only on the initial multiset, so M is the same for every legal play. ∎

### Conclusion
Every play terminates (Lemma 4) in a state with exactly one entry M > 1 (Lemma 5′), and M = ∏_p p^{gcd(v_p(x_1),…,v_p(x_2026))} depends only on the initial board (Lemmas 6, 7), hence is independent of Confucius's choices. ∎

### Verification
Simulated over 2000 random boards × 15 random plays each: every play leaves exactly one survivor, and its value always equals ∏_p p^{gcd of initial valuations}, matching the formula and confirming choice-independence.
