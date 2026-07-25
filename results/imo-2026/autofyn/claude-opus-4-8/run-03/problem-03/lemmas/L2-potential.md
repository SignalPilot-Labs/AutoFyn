# Lemma L2 — Alternating-sum (potential) identity

**Status:** CERTIFIED (proof-reviewer, round 2).

**Statement.** For a multiset B with Σ b_i = 1, sorted b_(1) ≥ b_(2) ≥ …, define the potential
S(B) := Σ_i (−1)^{i+1} b_(i). Then Σ_odd(B) = (1 + S(B))/2 and Σ_even(B) = (1 − S(B))/2.

**Proof.** Σ_odd + Σ_even = Σ B = 1 and Σ_odd − Σ_even = S(B). Add/subtract and halve. ∎

**Consequence.** c(n) = (1 + max_A min_B S(B))/2. Since 2·(2^n/D_n) − 1 = 1/D_n with
D_n = 2^{n+1} − 1, the target c(n) = 2^n/D_n is equivalent to max_A min_B S(B) = 1/D_n.

Depends on: L1 (for the game reformulation).
