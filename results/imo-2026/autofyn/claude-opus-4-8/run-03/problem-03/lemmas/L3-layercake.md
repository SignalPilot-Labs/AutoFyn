# Lemma L3 — Layer-cake identity for the potential

**Status:** CERTIFIED (proof-reviewer, round 2). Numerically verified: 0/400 mismatches.

**Statement.** For any finite multiset B of positive reals,
S(B) := Σ_i (−1)^{i+1} b_(i) = meas{ t > 0 : N(t) is odd },
where N(t) := #{ parts of B of length > t } (equivalently ≥ t; they differ on a null set), and
meas is Lebesgue measure on (0,∞). Also Σ B = ∫_0^∞ N(t) dt.

**Proof.** Layer-cake: b_(i) = ∫_0^∞ 1[t < b_(i)] dt. Then
S(B) = Σ_i (−1)^{i+1} ∫ 1[t < b_(i)] dt = ∫_0^∞ ( Σ_i (−1)^{i+1} 1[t < b_(i)] ) dt.
For fixed t the parts exceeding t are exactly the N(t) largest, so the inner sum is
Σ_{i=1}^{N(t)} (−1)^{i+1} = 1 if N(t) odd, 0 if N(t) even. Integrate. ∎

**Corollary (XOR decomposition).** If B = Q ⊔ C then N_B = N_Q + N_C, so N_B(t) is odd iff
exactly one of N_Q(t), N_C(t) is odd; hence
S(B) = S(Q) + S(C) − 2·meas{ t : N_Q(t) and N_C(t) both odd },
and in particular S(B) ≥ |S(Q) − S(C)|.

Reusable by every approach; the primary tool for the lower bound.
