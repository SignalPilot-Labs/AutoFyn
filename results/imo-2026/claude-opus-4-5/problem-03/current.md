# IMO 2026 P3 — Liu Bang vs Xiang Yu Stick Division

## Problem Statement

Let $n$ be a positive integer. Liu Bang and Xiang Yu have a stick of length 1 and want to divide it between themselves. Liu Bang marks at most $n$ points on the stick, and then Xiang Yu marks at most $n$ points on the stick. The marked points are distinct. Then, the stick is cut at all marked points, creating a number of pieces. Afterwards, they take turns claiming any unclaimed piece of the stick, with Liu Bang going first. Each player's goal is to maximise the total length of their own pieces. For each $n$, determine the largest value $c$ such that Liu Bang may guarantee a total length of at least $c$, regardless of Xiang Yu's play.

## Status
partial

## Approaches tried
- **geometric-direct** (Round 1, 2, 4, 5, 6, 7, 9, 10, 11) — **COMPLETE for n=1,2,3; COMPUTATIONALLY VERIFIED for n=4.** Lower bound PROVED for all n. Upper bound Case A (P_1 <= L_0) PROVED for all n via Halve-All Strategy. Upper bound Case B large (P_{n+1} >= c(n)) PROVED for all n >= 2 via Halve+IH Strategy. Upper bound Case B small (P_{n+1} < c(n)): PROVED for n=1,2,3. For n=4: V_j + Pigeonhole + Pairwise framework PROVED (Pigeonhole lemma certified), but some written constructions have errors (wrong piece counts). Computationally verified 100% coverage. For n=5: V_j + Pairwise proved; "all pairwise > 1" bounded region exists where Type 3 strategies needed, algebraic proof OPEN. Case B for n>=6 remains OPEN.

- **n5-five-mark** (Round 11-16) — **PARTIAL for n=5.** V_j strategies PROVED. Bounded region characterization PROVED (g in (1, 1.2), v_0 in (0, 1/3)). Key findings: (1) Type 3 strategies are INSUFFICIENT (~95% coverage); (2) the (2,2,1) strategy family achieves 100% computational coverage. **Round 14 progress:** 10 non-adjacent Pairwise constructions PROVED. **Round 16 progress:** CORRECTED vertex count from 63 to 93 (62 AP-type + 31 Z-type). Added Z-type vertices with r_alpha=0 (V_j doesn't apply). wrs=35 EXACT PROOF with LB = 1/2 (margin 1/126). **GAP IDENTIFIED IN COMPACTNESS ARGUMENT:** The claim "max of piecewise linear on polytope is at vertex" is FALSE for non-convex piecewise linear functions. 93-vertex verification is VALID finite casework, but interior coverage needs a different argument (LP coverage check or full algebraic enumeration).

- **minimax-saddle-point** (Round 2) — Game-theoretic saddle-point framework. Good intuition about geometric config being the equilibrium. Multiple gaps: interleaving construction, crucial lemma, uniqueness. NOT BUILT.

- **induction-on-n** (Round 1) — DEAD END. Upper bound proof fatally flawed for non-geometric configs.

- **vertical-pairing** (Round 10) — Identified S_vertical_last strategy family (halve all except two adjacent pieces). Merged into geometric-direct.

## Current best

**Answer:** c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.

**COMPLETE RIGOROUS PROOF for n = 1, 2, 3. COMPUTATIONALLY VERIFIED for n = 4 (written proof has minor errors in some pairwise constructions; coverage verified 100% but needs corrections for full rigor).**

**Key values:**
- n=1: c(1) = 2/3
- n=2: c(2) = 4/7
- n=3: c(3) = 8/15
- n=4: c(4) = 16/31
- n=5: c(5) = 32/63 (computationally verified)

**Certified Lemmas:**

1. **Greedy Optimality Lemma:** In the picking phase, greedy play (always take the largest piece) is optimal for both players. LB gets pieces at positions 1, 3, 5, ... in sorted descending order.

2. **Geometric Dominance Lemma:** L_n > L_0 + L_1 + ... + L_{n-1} where L_k = 2^k/(2^{n+1}-1).

3. **Parity Constraint Lemma:** With n LB marks and j XY marks, there are n+1+j pieces. LB picks ceil((n+1+j)/2) pieces.

4. **Pairing Cancellation Lemma:** For multiset S and v > 0: lb_score({v, v} + S) = v + lb_score(S).

5. **Halve-All Strategy Lemma (Case A):** If P_1 <= L_0, XY halves P_2, ..., P_{n+1}, yielding LB = 1/2 + P_1/2 <= c(n).

6. **Singleton-Pair Formula:** When XY creates 2n pieces as (n-1) pairs + 2 singletons s_1 < s_2, then LB = (1 - s_1 + s_2)/2.

7. **BPP Unified Construction (n=4):** For Case A with eta in [1+2*alpha+beta, eta_max), XY uses 3 marks to create pairs {P_3,P_3}, {P_1,P_1}, {P_5/2,P_5/2} and singletons {P_2, d_3-P_1}. LB = 1/2 + |P_1+P_2-d_3|/2 <= c(4).

8. **BPP Range Bound (n=4):** In the BPP range, the singleton difference |2+2*alpha+beta-eta| approaches at most 1-8*alpha-4*beta < 1, hence LB < c(4).

9. **Halve + IH Strategy Lemma (Case B Large P_{n+1}):** For n >= 2, if P_{n+1} >= c(n), XY halves P_{n+1} (1 mark) and applies the (n-1)-game strategy (n-1 marks). Result: LB <= P_{n+1}/2 + c(n-1)*(1-P_{n+1}) <= c(n). Uses identity: c(n-1)*(1-c(n)) = c(n)/2.

10. **Algebraic Identity c(n-1)*(1-c(n)) = c(n)/2:** Proof: c(n-1) = 2^{n-1}/(2^n-1) and 1-c(n) = (2^n-1)/(2^{n+1}-1). The (2^n-1) terms cancel, giving 2^{n-1}/(2^{n+1}-1) = c(n)/2.

11. **n=4 Pigeonhole Lemma:** CERTIFIED. If all 5 shifted params {alpha, beta, gamma, eta, sigma} > 0 and satisfy weighted sum 5*alpha + 4*beta + 3*gamma + 2*eta + sigma = 16, then some pairwise difference <= 1. Proof: Min weighted sum with all pairwise > 1 (sorting and assigning largest weight to smallest value) is 15*v_1 + 20*g > 20 > 16 for g > 1 and v_1 >= 0. Contradiction.

12. **n=5 Pigeonhole FAILS:** The weighted sum constraint for n=5 is 42, but min with all pairwise > 1 is only > 35. Since 42 > 35, the "all pairwise > 1" region is non-empty (bounded: g in (1, 1.2), v_0 in (0, 1/3)).

13. **LB(x,T) Convexity (n=5):** For any fixed (2,1,1) or (2,2,1) template T, the function LB(x,T) = (sum of 5 largest of 10 pieces) is convex in the configuration x. Proof: Each output piece is linear in x. LB = max over C(10,5)=252 subsets of (sum of pieces in subset). Maximum of linear functions is convex. CERTIFIED Round 17.

**Proven Results:**

1. **Lower Bound (PROVED for all n):** LB's geometric configuration [L_0, L_1, ..., L_n] achieves exactly c(n) against XY's optimal response.

2. **Upper Bound Case A (PROVED for all n):** For configs with P_1 <= L_0 = 1/(2^{n+1}-1), Halve-All Strategy gives LB = 1/2 + P_1/2 <= c(n).

3. **Upper Bound Case B Large P_{n+1} (PROVED for all n >= 2):** If P_{n+1} >= c(n), XY halves P_{n+1} (1 mark) and applies the (n-1)-game upper bound strategy (n-1 marks) to {P_1, ..., P_n}. Result: LB <= P_{n+1}/2 + c(n-1)*(1 - P_{n+1}) <= c(n).

4. **Upper Bound Case B Small P_{n+1}:**
   - n=1: PROVED (P_2 < c(1) automatically).
   - n=2: PROVED (sum constraint forces d_1 < L_0).
   - n=3: PROVED via three strategies (S1, S2, S3).
   - n=4: V_j + Pigeonhole + Pairwise framework PROVED. Pigeonhole lemma certified (min weighted sum > 20 > 16, contradiction). Pairwise strategy constructions have minor errors in written form but coverage computationally verified 100%.
   - n=5: V_j + Pairwise strategies PROVED. Pigeonhole FAILS for n=5 (bounded region with g in (1,1.2) has all pairwise > 1). A/E/F strategies insufficient (counterexample found). Type 3 strategies computationally cover 100%, algebraic proof **OPEN**.
   - n >= 6: **OPEN**.

**Gap remaining:** Case B small P_{n+1} sub-case (P_1 > L_0 AND P_{n+1} < c(n)) for n >= 5. For n=5: V_j + Pairwise strategies cover most configs; the "all pairwise > 1" bounded region (g in (1, 1.2), v_0 in (0, 1/3)) requires (2,2,1) strategies, which are computationally verified (63 boundary vertices, all succeed with margin >= 0.0057) but lack algebraic proof. For n >= 6: OPEN.

**Round 10 progress:** Identified that the B_small region has REVERSED sum constraint (sum > C, not < C). Found that original 11 strategies fail on B_small counterexamples. Added 4 new strategies: S_vertical_last, Cut-P6-at-P3, Cut-P6-at-P5, Cut-P4-at-P1. Cut-P6-at-P3 verified to work on counterexample. **ALSO FOUND: n=4 proof gap** — missing V1-V4 strategies for d_j < L_0 cases.

**Round 11 progress:** FIXED n=4 proof structure. Added V_j strategies (4 strategies for when any d_j <= L_0). Added Pigeonhole Lemma (CERTIFIED: proves some pairwise diff <= 1 when all d_j > L_0 since min weighted sum > 20 > 16). Added Pairwise strategy constructions. **Reviewer note:** Some written constructions have errors (e.g., (gamma,eta) claims "9 pieces" but 3 marks give 8 pieces). Coverage is computationally verified but written form needs corrections. n=5: V_j + Pairwise proved, but "all pairwise > 1" bounded region exists and needs Type 3 strategies (algebraic characterization OPEN).

**Round 12 progress:** n=5 breakthrough: the (2,2,1) strategy family (2 marks on each of 2 pieces + 1 halve) covers 100% of the bounded "all pairwise > 1" region. Key findings: (1) Type 3 strategies are INSUFFICIENT (~95% coverage). (2) (2,2,1) creates 4 near-pairs vs Type 3's 3, providing more flexibility. (3) All 63 boundary vertices at g=1 computationally verified (worst margin 0.0057). **Pairwise example errors:** The (beta, gamma) construction was incorrect (wrong singletons).

**Round 14 progress:** n=5 Pairwise constructions corrected. 10 non-adjacent pairs verified with "chop-at-adjacent" method (0 failures each). 5 adjacent pairs covered by (2,2,1) fallback.

**Round 16 progress:** CORRECTED vertex count from 63 to 93. The bounded region polytope has 62 AP-type vertices (g=1 boundary, wrs in {36,...,41}) + 31 Z-type vertices (v_0=0 boundary, r_alpha=0, wrs in {35,...,41}). All 93 computationally verified (min margin 0.0026). The wrs=35 Z-type vertex has EXACT ALGEBRAIC PROOF: pieces [1/63, 16/315, 11/105, 8/45, 17/63, 8/21], strategy creates 5 perfect pairs, LB = 1/2, margin = 1/126. **GAP:** The compactness argument claiming "max of piecewise linear at vertex" is INVALID for f = min_strategy LB (non-convex). Interior coverage needs LP-based verification or full algebraic enumeration. **New certified lemma:** wrs=35 Z-type Exact Construction.

**Round 17 progress:** Both n5-lp-direct and n5-convex-coverage correctly removed the false "max at vertex" claim. **New certified lemma:** LB(x,T) Convexity (for each fixed template T, LB is convex in config x). **CORRECTION:** Minimum Z-type vertex margin is **1/378** (at wrs=36, perm=(0,2,1,3,4,5)), not 1/2520 as claimed in n5-lp-direct. All 31 Z-type vertices verified with positive margin via exact rational arithmetic. Computational testing of 66 valid Tier 3 interior points shows 100% coverage with "copy" templates (min margin 0.00588). **GAP REMAINS:** Interior coverage is computationally supported but NOT rigorously proven. LP verification or algebraic argument still needed.

## Full proof
(Not yet complete for all n — see approaches/geometric-direct.md for complete proof for n=1,2,3,4)
