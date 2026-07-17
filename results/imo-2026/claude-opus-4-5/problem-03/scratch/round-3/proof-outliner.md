## imo-2026-03

induction-on-n: revise
Target: Prove c(n) = 2^n/(2^{n+1}-1) is the exact guaranteed value for Liu Bang
Technique: Strong induction with scale-invariant hypothesis + LARGEST-index pigeonhole choice
Skeleton:
  1. Scale-invariant claim P(m): For m+1 pieces summing to S, XY with m marks achieves A <= S*t_m — by induction
  2. Base m=1: ratio-based case split (r>2: halve; r<=2: clone) — by direct calculation (already proven)
  3. Pigeonhole existence: For m+1 pieces summing to S, exists k with p_k <= 2^{k-1}*S*t_m — by sum constraint
  4. Choose k* = LARGEST such k. Then for all j>k*: p_j > 2^{j-1}*S*t_m (strict) — by definition of largest
  5. (A) No interleaving: p_{k*+1}/p_{k*} > 2, so all halved pieces stay above p_{k*} — by ratio bound
  6. (B) Sub-problem bound: S_{k*} = p_1+...+p_{k*} < (2^{k*}-1)*S*t_m — by summing strict inequalities for j>k*
  7. Case k*=m+1 (sandwich): XY marks m points inside p_{m+1} creating interleaved sub-pieces; LB takes p_{m+1} <= S*c(m); A <= S*t_m — by sandwich analysis
  8. Case k*<m+1: XY halves p_{k*+1},...,p_{m+1} using m+1-k* marks (pairs cancel), uses k*-1 marks on sub-problem — by construction
  9. Apply IH to sub-problem: A_sub <= S_{k*}*t_{k*-1} = S_{k*}/(2^{k*}-1) < S*t_m — by the algebraic miracle (2^{k*}-1 cancels)
  10. Combine: total A = A_sub (pairs contribute 0) < S*t_m — by pair-cancellation lemma
Key lemmas (claim + the one-line mechanism that makes it true):
  - Pigeonhole for largest satisfying index: exists k* = max{k : p_k <= 2^{k-1}*S*t_m} — because sum p_1+...+p_{m+1}=S forces at least one such k (if none, sum > S)
  - No interleaving guarantee: p_{k*+1} > 2*p_{k*} — because k*+1 violates the condition and k* satisfies it, ratio > 2
  - Sub-problem size bound: S_{k*} < (2^{k*}-1)*S*t_m — because summing p_j > 2^{j-1}*S*t_m for j=k*+1,...,m+1 gives 1-S_{k*} > S*t_m*(2^{m+1}-2^{k*})
  - Algebraic miracle: S_{k*}*t_{k*-1} < (2^{k*}-1)*S*t_m / (2^{k*}-1) = S*t_m — because t_{k*-1} = 1/(2^{k*}-1) and the factors cancel exactly
Open gaps: Sandwich strategy for equal pieces (step 7); formal proof that the pair-cancellation applies when halved pieces don't interleave (step 5)
Cases to cover: k*=1 (trivial halve-all), k*=2,...,m (the general halve+recurse), k*=m+1 (sandwich)
Watch out for: Equal pieces in sandwich (need sum-based argument, not strict interleaving); pairs may require k*+1 distinct from all p_1,...,p_{k*} for clean separation

n2-explicit-casework: new
Target: Prove c(n) = 2^n/(2^{n+1}-1) with complete n=2 base case
Technique: Direct 4-case exhaustive analysis for n=2, then induction
Skeleton:
  1. n=1 base: ratio-based (proved) — by existing proof
  2. n=2 base: 4 exhaustive cases covering all (a_1,a_2,a_3) configurations — by case analysis
     - Case A: a_1 <= 1/7 -> halve a_2, a_3; A = a_1 <= 1/7
     - Case B: a_1 > 1/7, a_3 in [3/7, 4/7] -> clone a_1 in a_1 and a_3; A = |2a_3-1| <= 1/7
     - Case C: a_1 > 1/7, a_3 < 3/7 -> halve a_1, split a_3; A = a_3-a_2 < 1/7
     - Case D: a_3 > 4/7 -> halve a_3, apply n=1; A <= (1-a_3)/3 <= 1/7
  3. Inductive step n>=3: follows k*-largest structure (revise approach handles this)
Key lemmas (claim + the one-line mechanism that makes it true):
  - Case B bound: a_3 in [3/7, 4/7] implies |2a_3-1| <= 1/7 — because 2*(3/7)-1 = -1/7 and 2*(4/7)-1 = 1/7
  - Case C bound: a_3 < 3/7, a_1 > 1/7 implies a_2 > 2/7 — because a_1+a_2 > 4/7 and a_1 <= a_2
  - Case C final: a_3-a_2 < 3/7-2/7 = 1/7 — by combining the bounds
Open gaps: Verify Case B sorted order for both sub-cases (a_3 <= 1/2 vs a_3 > 1/2); extend to general n via k*-largest
Cases to cover: All 4 cases for n=2 plus inductive step
Watch out for: Case B has two sorted-order sub-cases; verify each

ratio-based-induction: advance
Target: Same as above
Technique: Ratio threshold 2 organizing principle
Skeleton: Existing skeleton with gaps identified
Open gaps: Sorted order after XY's first move; verify IH applies to residual
Cases to cover: r>2 (halve), r<=2 (clone)
Watch out for: Interleaving of halved/cloned pieces with residual pieces

exchange-argument: advance
Target: Prove geometric marking uniquely maximizes V(L) = min_X G(L,X)
Technique: Variational/exchange argument showing deviations from geometric decrease LB's guarantee
Skeleton:
  1. Define V(L) = min_X G(L,X) for any LB marking L
  2. Show geometric marking has V(geom) = c(n) — by lower bound proof
  3. Show any perturbation of geometric strictly decreases V — by showing XY has a strictly better response
  4. Conclude geometric is unique maximum, hence c(n) is the value
Key lemmas (claim + the one-line mechanism that makes it true):
  - First-order optimality: dV/dp_k = 0 at geometric — because perturbing piece sizes changes sorted order, and the unique equilibrium is the geometric ratio
Open gaps: The variational derivative analysis; showing XY's response to perturbation exploits the deviation
Cases to cover: none (continuous analysis)
Watch out for: Tied pieces create discontinuities in V; may need regularization
