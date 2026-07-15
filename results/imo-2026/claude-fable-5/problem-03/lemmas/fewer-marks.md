# Lemma: fewer-marks (certified, round 1)

**Statement.** If Liu Bang's marks produce at most n positive pieces (fewer than n marks, or marks wasted at endpoints/duplicating cut points), Xiang Yu can hold Liu Bang's optimal-play take to exactly 1/2 < 2^n/(2^{n+1}−1).

**Proof.** Let the positive pieces be q_1, …, q_r with r ≤ n. Xiang Yu marks the midpoint of each (r ≤ n marks, strictly interior to distinct pieces, hence distinct from each other and from all existing marks — legal). The final multiset is r equal pairs {q_i/2, q_i/2}; by defect-identity Corollary D2 with L = ∅, defect = 0, and by claiming-value Liu Bang gets exactly (1 + 0)/2 = 1/2. Conversely Liu Bang always gets ≥ ΣP/2 = 1/2 by nonnegativity of the defect (Lemma D). Finally 2^n/(2^{n+1}−1) = 1/2 + 1/(2(2^{n+1}−1)) > 1/2. ∎

**Use.** Reduces the upper bound to the case of exactly n interior marks, i.e. n+1 positive pieces.
