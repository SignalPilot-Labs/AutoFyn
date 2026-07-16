## imo-2026-03

geometric-direct: revise
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n (complete upper and lower bounds).
Technique: Singleton-Pair strategy framework with gap-overlap argument via sum constraint forcing alpha < 1.
Skeleton:
  1. Lower bound (PROVED for all n) -- by induction, geometric configuration achieves c(n).
  2. Upper bound Case A: P_1 <= L_0 -- by Halve-All Strategy (PROVED for all n).
  3. Upper bound Case B large P_{n+1}: P_{n+1} >= c(n) -- by Halve+IH Strategy (PROVED for all n >= 2).
  4. Upper bound Case B small P_{n+1}: P_{n+1} < c(n) with P_1 > L_0 -- NEW: sub-case structure.
     4a. If some d_j <= L_0 for j = 1,...,n-1: use S_j strategy (halve appropriate pieces, singletons {P_j, P_{j+1}}). LB = 1/2 + d_j/2 <= c(n).
     4b. **NEW** If d_{n-1} = P_{n+1} - P_n <= L_0: use S_last strategy (halve P_1,...,P_{n-1}, singletons {P_n, P_{n+1}}). LB = 1/2 + d_{n-1}/2 <= c(n).
     4c. If ALL d_j > L_0 for j = 1,...,n-1 AND d_{n-1} > L_0: show this is IMPOSSIBLE given sum = 1 and P_{n+1} < c(n).
  5. Conclude c(n) = 2^n / (2^{n+1} - 1) for all n.
Key lemmas (claim + the one-line mechanism that makes it true):
  - S_last Strategy: When d_{n-1} = P_{n+1} - P_n <= L_0, XY halves P_1,...,P_{n-1} (n-1 marks), creating pairs and singletons {P_n, P_{n+1}}. LB = 1/2 + d_{n-1}/2 <= c(n). -- because Pairing Cancellation applied (n-1) times leaves only the two largest pieces as singletons.
  - B_small "all d_j > L0" Impossibility (n=3): When P_1 > L_0, d_1 > L_0, d_2 > L_0, d_3 > L_0 AND P_4 < c(3), the sum P_1+P_2+P_3+P_4 = 1 is violated. -- because 4*L_0 + 3*L_0 + 2*L_0 + L_0 + additional = 10*L_0 + slack > 10/15 but P_1+P_2+P_3+P_4 = 1 with P_4 < 8/15 forces P_1+P_2+P_3 > 7/15, yet the "all > L_0" condition gives P_1 > 1/15, P_2 > 2/15, P_3 > 3/15, P_4 > 4/15, which sums to > 10/15 = 2/3 < 1 (more careful analysis needed).
  - For n >= 4: If B_small "all d_j > L0" exists, show the pairwise-comparison strategies (A1-A5 style) cover it, with gap-width = alpha - 1 < 0 ensuring overlap.
Open gaps:
  - Step 4c: Prove "all d_j > L0" is impossible in B_small for n=3,4,5 (or prove coverage by remaining strategies).
  - Verify S_last construction uses exactly n-1 marks and creates correct piece structure.
  - Algebraic proof that gap-overlap extends to small-P_{n+1} case.
Cases to cover:
  - n=3 B_small: S1 (d_1<=L_0), S2 (d_2<=L_0), S_last (d_3<=L_0), "all d_j > L_0" impossible.
  - n=4 B_small: S1-S3 (small d_j), S_last (d_3<=L_0), "all d_j > L_0" case.
  - n>=5 B_small: Pattern generalization.
Watch out for:
  - The sum constraint for B_small is REVERSED (P_1+...+P_n > (D-1)/D - c(n) NOT <). The S3 argument from B_large does NOT apply.
  - Confirm S_last uses n-1 marks (creating 2(n-1) + 2 = 2n pieces, which is correct for n marks total on both sides).

---

vertical-pairing: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.
Technique: "Vertical pairing" strategy family: for each j, when d_j <= L_0, halve pieces except {P_j, P_{j+1}} to create singletons with difference d_j.
Skeleton:
  1. Lower bound (PROVED) -- import from geometric-direct.
  2. Upper bound Case A (PROVED) -- import Halve-All.
  3. Upper bound Case B large (PROVED) -- import Halve+IH.
  4. Upper bound Case B small: For each j in {1,...,n-1}, define strategy V_j:
     - V_j works when d_j = P_{j+1} - P_j <= L_0.
     - Construction: XY halves all pieces except P_j and P_{j+1}. This uses n-1 marks.
     - Result: 2(n-1) pairs plus 2 singletons {P_j, P_{j+1}}.
     - By Singleton-Pair Formula: LB = 1/2 + d_j/2 <= c(n).
  5. Coverage claim: In B_small, at least one d_j <= L_0 for some j in {1,...,n-1}.
  6. Prove coverage claim: Assume all d_j > L_0. Then P_1 > L_0, P_2 > 2*L_0, ..., P_{n+1} > (n+1)*L_0.
     Sum >= L_0 * (1 + 2 + ... + (n+1)) = L_0 * (n+1)(n+2)/2 = (n+1)(n+2)/(2*(2^{n+1}-1)).
     For this to equal 1, need (n+1)(n+2)/2 = 2^{n+1}-1. Check: n=3 gives 10/2 = 5 vs 15, so sum >= 5/15 = 1/3 < 1 (no contradiction).
     Need tighter argument using P_{n+1} < c(n) AND P_1 > L_0.
Key lemmas (claim + the one-line mechanism that makes it true):
  - V_j Strategy: When d_j <= L_0, XY halves all pieces except P_j and P_{j+1}. Singletons = {P_j, P_{j+1}}, LB = 1/2 + d_j/2 <= c(n). -- because halving creates n-1 equal pairs; by Pairing Cancellation, LB gets half of paired total plus larger singleton.
  - Coverage in B_small: If all d_j > L_0 for j=1,...,n-1, then sum > (threshold) but B_small has sum < 1. Contradiction. -- because the ordering P_1 <= P_2 <= ... <= P_{n+1} with all gaps > L_0 forces minimum sum.
Open gaps:
  - Step 5-6: The minimum-sum argument is not tight enough with the naive bound. Need to use P_{n+1} < c(n) constraint.
  - Exact formula for when "all d_j > L_0" contradicts B_small constraints.
Cases to cover: n=3 (d_3 <= L_0 or impossibility), n=4 (d_3 <= L_0 or impossibility), n=5 (d_4 <= L_0 or impossibility).
Watch out for:
  - V_j for j < n-1 does NOT halve P_{n+1}, so mark count is (n+1) - 2 = n-1, correct.
  - V_{n-1} halves P_1,...,P_{n-1} (n-1 pieces), uses n-1 marks, correct.
  - Must verify piece ordering after XY's marks to confirm singleton positions.

---

pigeonhole-gaps: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.
Technique: Pigeonhole on n consecutive differences {d_1,...,d_{n-1}} plus P_1 and d_{n-1}: among these n values, at least one must be <= L_0 if their average is constrained.
Skeleton:
  1. Lower bound (PROVED) -- import.
  2. Upper bound Case A (PROVED) -- import.
  3. Upper bound Case B large (PROVED) -- import.
  4. Upper bound Case B small: Define n "gap-like" quantities:
     - G_1 = P_1 (gap from 0 to first piece)
     - G_2 = d_1 = P_2 - P_1
     - ...
     - G_n = d_{n-1} = P_{n+1} - P_n
  5. Sum relation: G_1 + G_2 + ... + G_n = P_{n+1} < c(n).
  6. Pigeonhole: If all G_j > L_0, then sum > n * L_0 = n / (2^{n+1} - 1).
     For B_small: P_{n+1} < c(n) = 2^n / (2^{n+1} - 1).
     Need n * L_0 >= c(n), i.e., n >= 2^n. FALSE for n >= 1.
     So pigeonhole alone is insufficient. Need weighted pigeonhole or case analysis.
  7. Alternative: Define weighted gaps. The sum P_1 + P_2 + ... + P_{n+1} = 1 gives a linear constraint on {G_j}. In B_small (P_{n+1} < c(n)), we have P_1 + ... + P_n > 1 - c(n). With P_1 > L_0, this constrains the other gaps.
Key lemmas (claim + the one-line mechanism that makes it true):
  - (WEAK) If all consecutive gaps > L_0, then P_{n+1} > n * L_0. -- because P_{n+1} = sum of first n gaps starting from P_1.
  - (NEEDED) In B_small with P_1 > L_0 and P_{n+1} < c(n), at least one d_j <= L_0. -- requires refined sum argument.
Open gaps:
  - The pigeonhole bound n * L_0 vs c(n) does not give contradiction for n >= 1.
  - Need a tighter argument combining P_1 + P_2 + ... + P_n = 1 - P_{n+1} > 1 - c(n) with the gap conditions.
Cases to cover: All n >= 3 (n=1,2 already proved via direct computation).
Watch out for:
  - The "weighted sum" approach may require linear algebra (LP) rather than pure pigeonhole.
  - This approach may reduce to the sum-slack LP from the explorer, which showed 11 strategies insufficient for n=5 B_large (wrong region). Need to apply to B_small.

---

geometric-direct: advance
Target: Same as original.
Technique: Same as original.
Skeleton: (as already written in approach file)
Key lemmas: (as already certified)
Open gaps: n >= 5 Case B small pieces sub-case needs algebraic proof.
Cases to cover: n=5 B_small, then pattern for n >= 6.
Watch out for:
  - The 11 strategies were tested on WRONG sub-case (B_large not B_small).
  - Need to add S_last (vertical pairing for d_{n-1}) and verify coverage.

---

halve-ih-plus-slast: new
Target: Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.
Technique: Two-strategy sufficiency: Halve+IH for large P_{n+1}, S_last for small P_{n+1} with d_{n-1} <= L_0, plus impossibility of "all d_j > L_0 in B_small".
Skeleton:
  1. Lower bound (PROVED) -- import.
  2. Upper bound Case A (PROVED) -- import Halve-All.
  3. Upper bound Case B: Split by P_{n+1} vs c(n).
     3a. P_{n+1} >= c(n): Halve+IH Strategy (PROVED for all n >= 2).
     3b. P_{n+1} < c(n) with some d_j <= L_0: S_j or S_last strategy.
     3c. P_{n+1} < c(n) with all d_j > L_0: IMPOSSIBLE (to be proved).
  4. Prove 3c (impossibility): In B_small, all pieces in (L_0, c(n)).
     - P_1 > L_0, P_{n+1} < c(n).
     - If all d_j > L_0 for j = 1,...,n-1, then P_2 > P_1 + L_0 > 2*L_0, ..., P_{n+1} > n*L_0 + P_1 > (n+1)*L_0.
     - But P_{n+1} < c(n) = 2^n * L_0. So (n+1)*L_0 < 2^n * L_0, i.e., n+1 < 2^n. TRUE for n >= 2.
     - Need stronger: P_1 + P_2 + ... + P_{n+1} = 1. With P_j > j * L_0 (from cumulative gaps), sum > L_0 * (1+2+...+(n+1)) = L_0 * (n+1)(n+2)/2.
     - For n=3: sum > 10/15 = 2/3. But sum = 1 > 2/3, no contradiction yet.
     - Add constraint P_{n+1} < c(n): In B_small, P_1 + ... + P_n > 1 - c(n) = (D - 2^n)/D = (2^n - 1)/D.
     - For n=3: P_1 + P_2 + P_3 > 7/15. With P_1 > 1/15, P_2 > 2/15, P_3 > 3/15 (from all d > L_0): sum > 6/15. Need 6/15 >= 7/15? NO, 6/15 < 7/15.
     - So the "all d_j > L_0" bound gives P_1+P_2+P_3 > 6/15, but B_small requires P_1+P_2+P_3 > 7/15. The gap 7/15 - 6/15 = 1/15 = L_0.
     - Refined: P_3 >= P_1 + d_1 + d_2 > P_1 + 2*L_0. P_2 >= P_1 + d_1 > P_1 + L_0.
     - Sum = P_1 + (P_1+L_0+eps) + (P_1+2*L_0+eps') + P_4 = 3*P_1 + 3*L_0 + small + P_4.
     - With P_4 < c(3) = 8/15 and P_1 > L_0 = 1/15: sum > 3/15 + 3/15 + 0 + 0 = 6/15 vs 1. Still no contradiction.
     - The bound is not tight enough. Need exact analysis or numerical LP.
Key lemmas (claim + the one-line mechanism that makes it true):
  - S_last Strategy (CERTIFIABLE): When d_{n-1} <= L_0, XY halves P_1,...,P_{n-1}, leaving {P_n, P_{n+1}} as singletons. LB = 1/2 + d_{n-1}/2 <= c(n).
  - B_small All-d-Large Impossibility (CONJECTURED): For each n >= 3, if P_1 > L_0 and P_{n+1} < c(n), then at least one d_j <= L_0.
Open gaps:
  - Step 4: The impossibility argument is not complete. The sum bounds are not tight enough.
  - May need LP or explicit enumeration to show no "all d_j > L_0" config exists in B_small.
Cases to cover: n=3 (verify or prove impossibility), n=4, n=5, general n.
Watch out for:
  - The explorers found that "all d_j > L_0 in B_small" DOES exist numerically for n >= 4 (e.g., the counterexample with delta < 0 for n=5). But wait, delta < 0 means d_3 < L_0, so that's NOT all d_j > L_0. Need to re-examine.
  - The induction explorer's counterexample (alpha=2.641, beta=2.594, gamma=0.206, delta=0.253, epsilon=4.913) has delta = 0.253 > 0, so d_3 = (1+delta)*L_0 > L_0. And epsilon = 4.913 > 0, so d_4 = (1+epsilon)*L_0 > L_0. So "all d_j > L_0" CAN exist in the n=5 small-pieces region! The impossibility argument must be WRONG.
  - BUT: gamma = 0.206 means d_2 = 1.206*L_0 > L_0 but barely. And alpha = 2.641 means P_1 = 3.641*L_0. The strategy |gamma - alpha| = |0.206 - 2.641| = 2.435 >> 1. So the pairwise strategies all fail here. This confirms the explorers' finding that 11 strategies are insufficient.
  - THE CORRECT FIX: Add more strategies, not prove impossibility. The "vertical pairing" S_last covers d_{n-1} <= L_0 but NOT all d_j > L_0. Need ADDITIONAL strategies for the corner case.

---

BUILD SET RECOMMENDATION:

1. **geometric-direct (revise)**: Add S_last strategy (vertical pairing for d_{n-1} <= L_0) and correct the Case B sub-case structure. This is the highest-priority fix.

2. **vertical-pairing (new)**: Articulate the full family of V_j strategies clearly, then attempt the coverage proof. This provides an alternative framing.

3. **halve-ih-plus-slast (new)**: If the impossibility argument can be completed, this gives a cleaner two-strategy sufficiency proof.

Note: The explorers confirmed that "all d_j > L_0 in B_small" CAN exist for n >= 5, so the impossibility argument is FALSE. The correct approach is to enumerate MORE strategies (the 11 + S_last + ...) and prove their union covers all B_small configs via sum-slack LP or gap-overlap analysis.

CRITICAL CORRECTION: The geometry explorer found that for the B_small region, the sum constraint forces alpha < 1 in the deepest Case A, so gap = alpha - 1 < 0 still holds. This means the strategy intervals OVERLAP even in B_small. The fix is to:
1. Add S_last (vertical pairing d_{n-1} <= L_0).
2. Apply the gap-overlap argument (alpha - 1 < 0) to show strategies cover "all d_j > L_0" sub-case.

