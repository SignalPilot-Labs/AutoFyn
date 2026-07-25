# Lemma L13 — Measure of a super-level set equals an order statistic

**Status:** CERTIFIED (proof-reviewer, round 5). Elementary; source: induction-peel §3.4 (R3).

**Statement.** For any finite multiset X with parts sorted descending x_(1) ≥ x_(2) ≥ … and
N_X(t) := #{ parts of X that exceed t }, one has for every integer k ≥ 1
  meas{ t > 0 : N_X(t) ≥ k } = x_(k)   (with the convention x_(k) := 0 for k > |X|).

**Proof.** N_X(t) ≥ k ⟺ at least k parts exceed t ⟺ the k-th largest part exceeds t ⟺ t < x_(k).
Thus { t > 0 : N_X(t) ≥ k } = (0, x_(k)), of Lebesgue measure x_(k). ∎

**Corollary (single-block sum bound).** If Q_low is a capped ≤c-cut refinement of the single
block {2^n} (so it has c+1 shards s_1 ≥ … ≥ s_{c+1}, all ≤ H = 2^{n-1}, summing to 2^n − e), then
  meas{ N_{Q_low} ≥ k } = s_k   and   Σ_k s_k = sum(Q_low) = 2^n − e ≤ 2^n.
This is the measure-theoretic form of the single-block part budget. (Summing meas{N_X ≥ k} over
all k recovers ∫ N_X = sum(X), consistent with L3.)
