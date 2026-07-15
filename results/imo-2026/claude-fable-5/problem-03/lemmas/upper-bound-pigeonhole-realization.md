# Lemma: upper-bound-pigeonhole-realization (certified, round 1)

Two components which together give the full upper bound c(n) ≤ 2^n/D, D = 2^{n+1}−1.

**Lemma P (subset-sum pigeonhole).** Let q_1, …, q_k ≥ 0 with Σq_i = S. Then there is a nonzero x ∈ {−1,0,+1}^k with |Σ x_i q_i| ≤ S/(2^k − 1).

*Proof.* The 2^k subset sums lie in [0,S]; partition [0,S] into 2^k − 1 intervals of length S/(2^k−1) (last one closed). Pigeonhole gives distinct subsets T ≠ T′ with |σ(T) − σ(T′)| ≤ S/(2^k−1); take x = 1_T − 1_{T′} ≠ 0. ∎

**Lemma R (realization).** Let q_1, …, q_k > 0 be the pieces after the first marker's cuts and x ∈ {−1,0,+1}^k nonzero. The second marker can place at most k − 1 marks, all distinct from each other and from existing cut points, so that the final multiset is a disjoint union of equal pairs plus leftovers of total exactly |x·q|. Hence (defect-identity, D2) defect ≤ |x·q|.

*Proof.* WLOG Σ_A := Σ_{x_i=+1} q_i ≥ Σ_B := Σ_{x_i=−1} q_i (replace x by −x); then A ≠ ∅. Halve each piece with x_i = 0 (|Z| marks, equal pairs). If B = ∅, stop: the A-pieces are leftovers of total Σ_A = |x·q|, marks = |Z| ≤ k−1. Otherwise lay the A-pieces end to end on a tape [0, Σ_A] with boundaries α_0 = 0 < α_1 < ⋯ < α_r = Σ_A, and the B-pieces on [0, Σ_B] with boundaries β_0 = 0 < ⋯ < β_s = Σ_B. Cut each A-piece at the tape positions β_1, …, β_s strictly interior to it (≤ s marks) and each B-piece at the α_1, …, α_{r−1} strictly interior to it (≤ r−1 marks); positions coinciding with existing boundaries get no cut. Then the A-fragments in (0, Σ_B] and the B-fragments realize the same partition of (0, Σ_B) by T = {α_1,…,α_{r−1}} ∪ {β_1,…,β_s} — match them into equal pairs; the remaining A-fragments cover (Σ_B, Σ_A), total Σ_A − Σ_B = |x·q|. All marks are strictly interior to their pieces (distinct, legal); total ≤ |Z| + r + s − 1 = k − 1. ∎

**Theorem UB.** For every Liu Bang marking, Xiang Yu has an ≤ n-mark reply holding Liu Bang to ≤ 2^n/D. *Proof.* If < n+1 positive pieces, use fewer-marks (value 1/2). Else k = n+1, S = 1: Lemma P gives nonzero x with |x·q| ≤ 1/D; Lemma R realizes it with ≤ n marks; defect ≤ 1/D and by claiming-value Liu Bang gets (1 + defect)/2 ≤ (1 + 1/D)/2 = 2^n/D. ∎

**Reviewer verification.** Independent re-implementation in exact rationals: 400 random configurations for each n = 1..4 — the construction always used ≤ n marks, produced exactly equal-pairs-plus-leftovers with leftover total |x·q|, and achieved defect ≤ 1/D. (An equivalent iterative merge process, per pairing-defect-strategy-family Theorem UB Steps 2–3, was verified the same way.)
