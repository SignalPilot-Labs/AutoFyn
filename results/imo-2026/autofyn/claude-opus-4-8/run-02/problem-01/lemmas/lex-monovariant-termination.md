# Lemma (lexicographic monovariant / termination) — CERTIFIED round 1

For a board with values b_1,…,b_N set Ω_tot = Σ_i Ω(b_i) (prime factors with multiplicity) and
C = #{i : b_i>1}. Order pairs (Ω_tot, C) lexicographically on ℕ×ℕ.

Every legal move strictly decreases (Ω_tot, C):
- ΔΩ_tot = −Ω(gcd(m,n)) ≤ 0 (from the per-prime move step, Σ_p min = Ω(gcd)).
- If gcd(m,n)>1: Ω_tot drops (first coordinate). 
- If gcd(m,n)=1: Ω_tot unchanged, {m,n}→{1,mn} with mn>1, so C drops by exactly 1.

Lex order on ℕ×ℕ is a well-order (type ω²), so no infinite descending chain: every maximal move
sequence is finite and halts with C≤1 (at most one value >1). Combined with the nonvanishing g_p
invariant (some g_p≥1), the halt has exactly one value >1.

Certified by proof-reviewer, round 1.
Source: perprime-valuation §2 / descent-induction §2.
