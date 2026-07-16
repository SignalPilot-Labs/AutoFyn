## imo-2026-03

- **Distinct openings:**
  1. **Finite Rank-Permutation Algebraic Proof (MAIN FINDING):** The Tier 3 interior is fully algebraically covered by a finite case analysis. Key parametrization: any Tier 3 config is determined by a rank permutation (r_a,r_b,r_g,r_d,r_e,r_z) of {0,...,5} with WRS = 6r_a+5r_b+4r_g+3r_d+2r_e+r_z ∈ {35,...,41}. Only 63 such permutations exist. For each, the diff(g) = (s1(x,T)-s2(x,T))/L0 for the best template T is LINEAR in g, so checking |diff| ≤ 1 at endpoints g=1 and g=42/WRS covers the entire range. ALL 63 permutations pass with exact rational arithmetic.
  
  2. **Mixed Template Family (NEW):** Beyond "copy" templates, a new family of "mixed equal-split" (2,1,1) templates closes the interior gap. Structure: H-piece halved, D-piece cut at P_i (copy cut, matching uncut P_i) then equal-split of remainder (creating {P_i, (P_D-P_i)/2, (P_D-P_i)/2}), C-piece cut at P_j (copy cut). This creates 4 exact pairs + 2 near-singletons {P_C-P_j, P_k}. Coverage condition: |p_C - p_j - p_k| ≤ 1 (in L0 units). For triple (4,3,2): condition |delta-alpha-beta-1| ≤ 1 is purely algebraic. This covers 55 of 63 Tier 3 permutations.
  
  3. **LP Infeasibility Formulation (Closed):** For each template T, diff_T(x) is LINEAR in the Tier 3 parameters (after substituting the WS constraint v_0 = (42-WRS·g)/21). The system "x in Tier 3 AND LB(x,T)>c(5) for all T in F" is infeasible because for each of 63 permutations, some T in F achieves |diff_T| ≤ 1 throughout. F consists of 63 explicit templates (55 mixed + 8 copy).
  
  4. **Convexity as organizing principle:** The certified LB(x,T) Convexity Lemma (Round 17) means each coverage set C_T = {x: LB(x,T)≤c(5)} is convex. The mixed templates' coverage sets are "slabs" {|p_C-p_j-p_k| ≤ 1} (intersection of two half-spaces). The union of 63 such slabs covers K.

- **Candidate technique(s):** Finite rank-permutation case analysis + linear endpoint checking. The key is: (a) parametrize Tier 3 by 63 rank permutations, (b) for each permutation, identify a template T with linear diff_T(g), (c) check |diff_T| ≤ 1 at two rational endpoints.

- **Cheap-kill candidates:** None remaining for the interior gap — the finite case analysis directly closes it. The proof is now: (i) compute endpoint values for each of 63 permutations, (ii) invoke linearity of diff_T(g) for the intermediate value principle.

- **Knowledge-base entries to use:** 
  - "Pairing Cancellation Lemma" (CERTIFIED): used to get LB = 1/2 + |s1-s2|/2 for near-pairing templates.
  - "LB(x,T) Convexity" (CERTIFIED, Round 17): each coverage set is convex.
  - "Singleton-Pair Formula" (CERTIFIED): the 4-pair + 2-singleton structure gives LB formula.

- **Analogous past problems (cruxes):** None precisely analogous — this is a custom LP infeasibility argument for the specific parametric structure.

- **Prior progress:** Tier 1 (V_j) and Tier 2 (Pairwise) certified. Z-type vertices (31) verified with exact rational arithmetic (min margin 1/2520). Interior coverage was the only remaining gap.

- **Dead ends (do not retry):**
  - Copy templates alone do NOT cover all interior points (max |diff| ≈ 1.01 at some points).
  - "Max of piecewise linear at vertex" argument (invalid for non-convex f = min_T LB_T).
  - The triple condition |p_C-p_j-p_k| ≤ 1 alone does NOT cover the 8 "hard" permutations at g>1; those need specific copy templates.

- **Small-case / intuition notes:**
  - The Tier 3 interior has only 63 relevant rank permutations (WRS in {35,...,41}), not 720.
  - Of these 63: 55 covered by "mixed templates" with coverage condition |p_C-p_j-p_k| ≤ 1 (a TRIPLE linear condition on parameters, different from Tier 2's pairwise conditions).
  - Remaining 8 permutations covered by specific copy templates with max |diff| ≤ 4/21 ≈ 0.19 (verified with exact fractions).
  - Validity checks: (a) mixed templates always valid (j<C ensures P_j ≤ P_C; equal-split always fits in D-piece), (b) copy templates valid (u3≤C verified; P_{u1}+P_{u2}-P_D ≤ -1.81 < 0 throughout).
  - Conclusion: The interior coverage proof is COMPLETE as a finite algebraic case analysis. Combined with Z-type vertex verification (31 cases, min margin 1/2520), the full Tier 3 proof closes.

**PROOF STRUCTURE FOR BUILDER:**

The complete Tier 3 interior coverage proof:

**Claim:** For every x in the Tier 3 bounded region (all pairwise diffs > 1, g > 1, v_0 > 0), there exists a valid (2,1,1) template T with LB(x,T) ≤ c(5).

**Step 1 (Parametrization):** Any Tier 3 config is parameterized by:
- Rank permutation (r_a,...,r_z) of {0,...,5} with WRS = 6r_a+5r_b+4r_g+3r_d+2r_e+r_z
- Gap g ∈ (1, 42/WRS) (g > 1 requires WRS < 42)
- Baseline v_0 = (42-WRS·g)/21 ∈ (0, 1/3)
Only permutations with WRS ∈ {35,...,41} can be in Tier 3. There are exactly 63 such permutations.

**Step 2 (Template selection):** For each of 63 permutations, assign one template T from F (55 "mixed" + 8 "copy") such that LB(x,T) ≤ c(5) throughout.

**Step 3 (Linear diff):** For each template T, diff_T(g) = intercept + slope·g is LINEAR in g (derived by substituting v_0 = (42-WRS·g)/21 into the piece-size formulas).

**Step 4 (Endpoint verification):** Since diff_T(g) is linear, |diff_T| ≤ 1 for all g ∈ (1, 42/WRS) iff |diff_T(1)| ≤ 1 AND |diff_T(42/WRS)| ≤ 1. Both verified with exact rational arithmetic for all 63 permutations.

**Step 5 (LB formula):** For each template T (4-pair + 2-singleton structure), LB(x,T) = 1/2 + |diff_T|·L0/2 ≤ 1/2 + L0/2 = c(5). ✓

**Validity:** Copy templates: u3 ≤ C (cut fits in C-piece), P_{u1}+P_{u2} ≤ P_D (verified: max value ≤ -1.81·L0 < 0 throughout). Mixed templates: j < C and k < C (cuts fit); choose i = min remaining uncut, D = max remaining uncut, ensuring P_i ≤ P_D.
