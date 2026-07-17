# Lemma: termination of the gcd/lcm-split process (CERTIFIED, round 1)

**Statement.** The gcd/lcm board process (replace m>1,n>1 by gcd(m,n) and lcm(m,n)/gcd(m,n), continue while ≥2 entries exceed 1) makes only finitely many moves and terminates with exactly one entry > 1.

**Proof (two independent monovariants, either suffices).**
- Φ = (N, P), N = #{entries>1} primary, P = product secondary, lex order on ℤ_{≥0}×ℤ_{≥1}. Coprime move: N drops by exactly 1 (one entry → 1, other → mn>1). Non-coprime move: P = P/gcd strictly drops, N non-increasing. So Φ strictly decreases every move; lex order well-founded ⇒ finite.
- Ψ = (Ω, N), Ω = Σ_i Ω(x_i) total prime-factor count primary. Non-coprime move: Ω drops by Ω(gcd(m,n))>0. Coprime move: Ω fixed, N drops by 1. Explicit bound ≤ (Ω₀+1)·2026 moves.

Terminal N ∈ {0,1}; N=0 excluded by the valuation-gcd invariant (some g_p ≥ 1 initially, preserved), so N=1.

**Certification.** Both monovariants verified against the move rule; termination and unique survivor confirmed by simulation over 2000 random boards. Admitted.
