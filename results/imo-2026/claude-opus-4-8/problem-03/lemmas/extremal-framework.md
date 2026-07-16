# Lemma (Extremal framework: continuity, attainment, replica bound)

**Status:** certified (proof-reviewer, round 3). Continuity/attainment are standard; the replica bound
computation was re-derived and verified numerically (A(replica) = 1, val = 2^n for n = 1..5).

## Notation
Δ := { A = (A_1 ≥ … ≥ A_{n+1} ≥ 0) : Σ A_i = 1 } (compact, the Liu Bang spectrum simplex face).
For A ∈ Δ, V(A) := min over Xiang Yu's ≤ n cuts of val(final pieces), where val = Σ_odd = (1 + A(P))/2.
By Lemma G the claiming-game value depends only on the piece-length multiset.

## Part 1 (continuity + attainment)
val(P(A, t)) is jointly continuous in (A, t) on the compact product Δ × K, K = [0,1]^n: place Liu Bang's
pieces consecutively (cumulative marks s_j = A_1 + ⋯ + A_j), the final pieces are the sorted gaps of
{0,1} ∪ {s_j} ∪ {t_i}, each gap length is piecewise-linear hence continuous, and
val = (1 + A(P))/2 with A(P) = Σ (−1)^{i+1} p_i^↓ a symmetric 1-Lipschitz function of the piece lengths
(no jump through ties). Distinctness of Xiang Yu's marks is not a restriction: legal distinct tuples are
dense in K and val is continuous, so the infimum over legal plays equals min over the closed set K
(coincident coordinates realise "fewer than n cuts", which is legal). Hence
  V(A) = min_{t ∈ K} val(P(A, t))
is continuous on Δ (uniform continuity of a continuous function on the compact Δ × K). By the
**Extreme Value Theorem** (knowledge_base.md, "Extreme value theorem"), V attains its maximum on Δ, and
c(n) = max_{A ∈ Δ} V(A).

## Part 2 (replica bound V(G_n) ≤ c(n))
Let G_n = {1, 2, …, 2^n}/D, D = 2^{n+1} − 1. Xiang Yu halves each piece 2^i (i = 1, …, n) at its
midpoint (n distinct interior marks), leaving the piece 1 uncut. Unnormalized final multiset: value 2^j
appears twice for j = 1, …, n−1, and value 1 appears three times. For x ∈ [0,1) all D pieces exceed x,
N = D odd; for x ∈ [2^k, 2^{k+1}), 0 ≤ k ≤ n−1, exactly 2(n−1−k) pieces (values ≥ 2^{k+1}) exceed x,
even; for x ≥ 2^{n−1}, N = 0. Hence A = measure{N odd} = measure[0,1) = 1, so
val = (D + 1)/2 = 2^n, i.e. normalized val = 2^n/D = c(n). This is one admissible Xiang Yu response,
so V(G_n) ≤ c(n). ∎

## Scope note (what is NOT proved)
This framework does NOT by itself give the upper bound. The upper bound follows only via the additional
**Smoothing Lemma S1** (every non-geometric A ∈ Δ admits A' with V(A') > V(A), i.e. G_n is the unique
maximizer), which is an OPEN gap. The reduction "upper bound ⟸ S1 + this replica bound" is a valid
logical implication but is conditional on S1.
