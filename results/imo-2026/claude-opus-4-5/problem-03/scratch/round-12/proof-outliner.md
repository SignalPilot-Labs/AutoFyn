## imo-2026-03

n5-five-mark: revise
Target: Prove c(5) = 32/63 for n=5 — complete upper bound for Case B small (P_6 < c(5) with P_1 > L_0)
Technique: Three-tier strategy cascade: V_j (covers any d_j <= L_0) -> Pairwise (covers any shifted-param pair diff <= 1) -> (2,2,1) strategies (covers the bounded "all pairwise > 1" region)
Skeleton:
  1. Import V_j strategies for n=5 — by direct construction (halve 4 pieces, singletons {P_j, P_{j+1}}, already PROVED)
  2. Import Pairwise strategies for n=5 — by construction (15 pairs, already PROVED)
  3. Characterize "all pairwise > 1" bounded region: g in (1, 1.2), v_0 in (0, 1/3), entirely in B_small — by Rearrangement Inequality (PROVED in explorer)
  4. Identify that Type 3 strategies (2 cuts + 3 halves on 5 different pieces) are INSUFFICIENT — ~95% coverage, counterexamples near alpha -> 0 (explorer verified)
  5. Define (2,2,1) strategy class: 2 marks on P_a creating 3 sub-pieces, 2 marks on P_b creating 3 sub-pieces, 1 mark (halve) on P_c, 3 singletons — by definition
  6. The canonical (2,2,1) strategy "Split P_3, P_5; Halve P_6; Singletons P_1, P_2, P_4" creates: Halve P_6 (1 mark) + Split P_3 at (t1, t2) into 3 pieces (2 marks) + Split P_5 at (s1, s2) into 3 pieces (2 marks) — by construction
  7. The pieces after (2,2,1) are: {P_6/2, P_6/2} (pair), {t1, t2-t1, P_3-t2} (3 from P_3), {s1, s2-s1, P_5-s2} (3 from P_5), {P_1, P_2, P_4} (3 singletons) = 11 pieces total — by counting
  8. LB picks ceil(11/2) = 6 pieces. Apply Pairing Cancellation to P_6 pair: LB = P_6/2 + lb_score(remaining 9 pieces) — by Pairing Cancellation Lemma
  9. XY's optimal cuts: set s1 = P_1, s2 = P_1 + P_2 = d_1 + 2*P_1, making P_5-s2 = P_5 - d_1 - 2*P_1 = d_4 + d_3 + d_2 - P_1 — by algebra
  10. This creates near-pairs: {s1, P_1} ~ {P_1, P_1}, {s2-s1, P_2} ~ {P_2, P_2}, {P_5-s2, P_4} — by construction
  11. The third "near-pair" {P_5-s2, P_4} has difference |P_5-s2-P_4| = |d_4-2*P_1-d_1| = |epsilon-2*alpha-beta-1|*L_0 — by algebra
  12. For P_3 cuts, XY creates similar near-pairs with P_1 and/or d_2 — by analogous construction
  13. Apply "4-near-pair Pairing Cancellation": LB <= P_6/2 + P_1 + P_2 + P_4 + sum(near-pair-errors)/2 + small_terms — by Singleton-Pair generalization
  14. The combined LB formula satisfies LB <= c(5) when the weighted sum = 42 holds in the bounded region — by algebraic verification (computational proof, optionally rigorous via LP breakpoint enumeration)
Key lemmas (claim + the one-line mechanism that makes it true):
  - V_j Strategy for n=5: If d_j <= L_0, LB <= c(5) — because halving 4 pieces creates 4 pairs + 2 singletons, and LB = 1/2 + d_j/2 <= c(5)
  - Pairwise Strategy for n=5: If |x_i - x_j| <= 1 for shifted params, LB <= c(5) — because XY creates 4 pairs + 2 singletons with difference <= L_0
  - Bounded Region Characterization: The "all pairwise > 1" region has g in (1, 1.2), v_0 in (0, 1/3), and is entirely in B_small — because min weighted sum = 21*v_0 + 35*g implies these bounds from wsum <= 42
  - (2,2,1) Strategy Coverage: "Split P_3, P_5; Halve P_6" achieves LB <= c(5) for all configs in bounded region — because the 4 near-pairs created by optimal (s1, s2, t1, t2) satisfy combined error bound in the bounded region (verified by scipy with exact constraint wsum=42)
  - Type 3 Insufficiency: 2 cuts + 3 halves on 5 different pieces is NOT sufficient — because counterexamples exist with alpha ~ 0.007 and best Type 3 LB > c(5)
Open gaps:
  - Step 14: Rigorous algebraic proof that (2,2,1) strategy always succeeds in bounded region. Current evidence is computational (scipy optimization). Two paths: (a) LP breakpoint enumeration (finite case analysis), (b) explicit formula for LB as function of params and verify LB <= c(5) analytically.
Cases to cover:
  - The (2,2,1) strategy must work for all 63 permutation vertices at g=1 boundary AND the interior. Interior follows from boundary by continuity/compactness.
Watch out for:
  - The cut positions (s1, s2, t1, t2) are NOT always exactly P_1 and P_1+P_2 — they depend on the config. The "exact near-pair" claim may need case analysis by which param is smallest.
  - Some configs may need a DIFFERENT (2,2,1) variant (e.g., "Split P_2, P_5" instead of "Split P_3, P_5"). Verify the single "Split P_3, P_5; Halve P_6" strategy is universal OR enumerate variants.

---

geometric-direct: advance
Target: Complete proof of c(n) = 2^n/(2^{n+1}-1) for all n >= 1
Technique: Singleton-Pair strategies with V_j + Pigeonhole + Pairwise + (2,2,1) cascade for each n
Skeleton:
  1. Lower bound (PROVED for all n)
  2. Upper bound Case A (P_1 <= L_0): PROVED for all n via Halve-All Strategy
  3. Upper bound Case B large (P_{n+1} >= c(n)): PROVED for all n >= 2 via Halve+IH Strategy
  4. Upper bound Case B small for n=1,2,3,4: PROVED
  5. Upper bound Case B small for n=5: Import n5-five-mark result when complete
  6. Upper bound Case B small for n >= 6: OPEN (likely requires generalizing (2,2,1) or new techniques)
Key lemmas (claim + the one-line mechanism that makes it true):
  - All lemmas already certified (see current.md)
Open gaps:
  - Step 5: Depends on n5-five-mark completion
  - Step 6: n >= 6 remains open (no immediate plan)
Cases to cover: None new (depends on n5-five-mark)
Watch out for: The n=4 written pairwise constructions have minor errors (e.g., (gamma,eta) piece count). Coverage is verified but text corrections needed.

---

n5-compactness: new
Target: Prove c(5) = 32/63 via compactness argument on the bounded region
Technique: Continuous minimum over compact set + boundary reduction
Skeleton:
  1. Define f(config) = min over all 5-mark XY strategies of LB(config) — by definition
  2. Prove f is continuous on the bounded region K (Berge's Maximum Theorem) — by continuity of LB in all arguments
  3. Prove K is compact (closed and bounded subset of R^6 intersected with affine constraint wsum=42) — by characterization
  4. On boundary of K (some param -> 0 or some pairwise -> 1), V_j or Pairwise strategies achieve f <= c(5) — by V_j and Pairwise lemmas
  5. In interior, computational verification shows f < c(5) with margin >= 0.007 — by scipy/numpy (NOT algebraic)
  6. By extreme value theorem on compact K with continuous f, if f <= c(5) on boundary and f < c(5) strictly in interior, then f <= c(5) on all of K — by compactness
Key lemmas (claim + the one-line mechanism that makes it true):
  - Berge continuity: f(config) = min_T LB(T, config) is continuous when LB is continuous and feasible T varies continuously — by Berge's Maximum Theorem
  - Boundary triviality: On boundary of K, V_j or Pairwise applies — because boundary is exactly where some d_j -> L_0 or some pairwise -> 1
Open gaps:
  - Step 5: The interior computation is NOT a proof; it's numerical evidence. This approach requires either interval arithmetic certification OR the 63-permutation algebraic enumeration to be rigorous.
Cases to cover:
  - 63 permutation-ordered vertices at g=1 boundary (the extreme points of K at the pairwise=1 boundary)
Watch out for:
  - This is NOT a complete proof without rigorous certification of the interior bound. The compactness argument establishes the STRUCTURE (continuous + compact => attains sup), but the bound sup < c(5) still needs algebraic/computational certification.

---

n5-lp-breakpoint: new
Target: Prove c(5) = 32/63 via LP breakpoint enumeration (finite algebraic certificate)
Technique: LP duality + finite casework over piece orderings
Skeleton:
  1. Fix a strategy type T (which pieces XY splits, how many marks per piece) — by enumeration
  2. For fixed T and fixed ordering of the 11 result-pieces, LB is a LINEAR function of (config, cut positions) — by sorted-sum formula
  3. Optimal cut positions (a*, b*) lie at a breakpoint where piece ordering changes — by LP theory (optimal at vertex)
  4. Enumerate all possible piece orderings (finite number for each T) — by casework
  5. For each ordering, LB <= c(5) is a LINEAR inequality in config — by algebra
  6. Union of these linear regions covers the bounded region K — by completeness
  7. Therefore LB <= c(5) for all configs in K — by union coverage
Key lemmas (claim + the one-line mechanism that makes it true):
  - LP optimality at vertex: For LP minimization over a polytope, the optimum is at a vertex (breakpoint where constraints change) — by LP duality
  - Finite ordering enumeration: 11 pieces have at most 11! orderings, but symmetry and monotonicity reduce this drastically — by combinatorial bound
Open gaps:
  - Step 4-6: The enumeration is large but finite. Need explicit computation of the orderings and verification of each inequality.
Cases to cover:
  - All piece orderings for each (2,2,1) strategy variant
Watch out for:
  - The number of orderings could be large (even with reduction). This is a "brute force" algebraic proof, less elegant but rigorous.

---

n5-equal-position-cut: new
Target: Prove c(5) = 32/63 via "equal-position double-cut" strategy (cut two pieces at the same position t)
Technique: Create pair {t, t} by cutting P_i and P_j both at position t
Skeleton:
  1. XY cuts P_3 at position t (creating {t, P_3-t}) and P_5 at position t (creating {t, P_5-t}) — by construction
  2. This creates pair {t, t} (exact) plus singletons {P_3-t, P_5-t, P_1, P_2, P_4, P_6} — by counting
  3. XY also halves 2 of the singletons (e.g., halve P_2 and P_6) using 2 more marks — by construction
  4. Total: 5 marks = 2 (double-cut at t) + 2 (halves on P_2, P_6) + 1 (cut on another piece, say tiny cut on P_1)
  5. Resulting pieces: {t, t} (pair), {P_3-t, P_5-t, P_1, P_4} (singletons), {P_2/2, P_2/2}, {P_6/2, P_6/2} (pairs) = 10 pieces
  6. LB picks ceil(10/2) = 5 pieces. Apply Pairing Cancellation to 3 pairs: LB = t + P_2/2 + P_6/2 + lb_score({P_3-t, P_5-t, P_1, P_4})
  7. Optimize t to minimize LB. The optimal t equates certain singleton sizes — by calculus/LP
  8. Verify LB <= c(5) for all configs in bounded region — by algebraic analysis
Key lemmas (claim + the one-line mechanism that makes it true):
  - Equal-position cut creates {t,t}: Cutting two pieces at the same position t creates a pair that contributes t to LB via Pairing Cancellation — by direct application
  - Optimal t formula: t* = some function of P_1, P_3, P_4, P_5 that minimizes lb_score — by LP optimality
Open gaps:
  - Step 7-8: Need explicit formula for t* and verification of LB <= c(5)
Cases to cover:
  - All configs in bounded region
Watch out for:
  - The "equal-position" strategy may not work for ALL configs. It may need to be combined with other strategies (case split by which param is smallest).
