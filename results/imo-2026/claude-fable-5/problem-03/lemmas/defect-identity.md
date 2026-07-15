# Lemma: defect-identity (certified, round 1)

For a finite multiset P of nonnegative reals sorted decreasingly, defect(P) = Odd(P) − Even(P), N_P(x) = #{i : p_i > x}, E_P = {x > 0 : N_P(x) odd}.

**Lemma D (layer-cake identity).** defect(P) = |E_P| (Lebesgue measure); in particular defect(P) ≥ 0.

*Proof.* By p_i = ∫_0^∞ 1[p_i > x] dx and linearity, defect(P) = ∫_0^∞ Σ_i (−1)^{i−1} 1[p_i > x] dx; for fixed x the pieces exceeding x are exactly p_1, …, p_{N_P(x)}, so the integrand is 1[N_P(x) odd]. ∎

**Corollary D0 (Δ-additivity).** N_{P⊎Q} = N_P + N_Q, hence E_{P⊎Q} = E_P Δ E_Q and defect(P ⊎ Q) ≤ defect(P) + defect(Q).

**Corollary D1 (strip pairs).** Removing an exactly equal pair {a, a} leaves the defect unchanged.

**Corollary D2 (pairs + leftovers).** If P is a disjoint union of equal pairs and a leftover sub-multiset L, then defect(P) = defect(L) ≤ ΣL; if L = {ρ} or ∅ then defect(P) = ρ or 0.

**Corollary D4 (zero-append).** defect(P ∪ {0}) = defect(P), Odd(P ∪ {0}) = Odd(P).

**Lemma P (pairing duality).** A *pairing* of P partitions the multiset into unordered pairs {a, b} and singleton leftovers ℓ; its *cost* is Σ|a − b| + Σℓ. Then defect(P) = min over pairings of the cost.

*Proof.* (≤) By D0 applied blockwise: defect(P) ≤ Σ defect({a,b}) + Σ defect({ℓ}) = Σ|a−b| + Σℓ. (≥) The consecutive sorted pairing {p_1,p_2}, {p_3,p_4}, … (last element a leftover if |P| odd) costs exactly defect(P). ∎
