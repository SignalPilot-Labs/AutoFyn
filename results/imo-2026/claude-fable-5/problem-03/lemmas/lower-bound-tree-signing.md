# Lemma: lower-bound-tree-signing (certified, round 1)

**Lemma T (tree lower bound).** Let q_1, …, q_k > 0 be the pieces after the first marker's cuts and let P be the multiset after the second marker adds at most k − 1 further interior, distinct marks. Then defect(P) ≥ δ(q) := min{ |Σ x_i q_i| : x ∈ {−1,0,+1}^k, x ≠ 0 }.

*Proof.* P has t ≤ k + (k−1) = 2k−1 pieces; the consecutive sorted pairing has ⌊t/2⌋ ≤ k−1 pairs and costs exactly defect(P) (defect-identity, Lemma P duality). Build the multigraph H on the k "home" vertices (one per original piece) with one edge per pair joining the homes of its two fragments. Σ_components e ≤ k−1 < k = Σ_components v, so some component C has e(C) < v(C); connected forces e(C) = v(C) − 1, and C is a tree (a loop or parallel edge would put a cycle in C). Properly 2-color C: x_i ∈ {±1} on V(C), x_i = 0 off C; x ≠ 0. Every pair touching a home in C has both homes in C (edges stay in their component), and joins oppositely signed homes, contributing ±(a − b); leftover fragments contribute 0 or ±ℓ. Summing q_i = Σ_{fragments with home i} over i with weights x_i and applying the triangle inequality: |Σ x_i q_i| ≤ Σ_{pairs} |a − b| + Σ_{leftovers} ℓ = defect(P). Hence defect(P) ≥ δ(q). ∎

**Lemma G (dyadic dissociation).** For g = (u, 2u, 4u, …, 2^n u), u = 1/(2^{n+1}−1): δ(g) = u. *Proof.* Σ x_j 2^j is a nonzero integer for nonzero x ∈ {−1,0,1}^{n+1}: reduce mod 2^{j_0+1} at the least index j_0 with x_{j_0} ≠ 0. So |Σ x_j g_j| ≥ u; x = (1,0,…,0) attains u. ∎

**Theorem LB.** Liu Bang marks (2^j − 1)/D for j = 1..n (distinct, interior), creating pieces g. For every Xiang Yu reply (≤ n marks, distinct, so ≤ n = k−1 interior cuts; endpoint marks create nothing), defect(P) ≥ δ(g) = 1/D by Lemmas T and G, so by claiming-value Liu Bang gets ≥ (1 + 1/D)/2 = 2^n/D. Tightness: Xiang Yu halving g_1, …, g_n leaves n equal pairs plus leftover g_0 = u, defect exactly u. ∎

**Reviewer verification.** Numerical minimization (all cut assignments, multistart Nelder–Mead) of the defect over ≤ n-cut refinements of the geometric configuration returns exactly 1/D at n = 1, 2, 3.
