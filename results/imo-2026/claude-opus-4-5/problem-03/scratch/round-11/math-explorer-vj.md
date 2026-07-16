## imo-2026-03: V_j Strategy Verification and n=4 Case B Small Analysis

### Task
Verify V_j strategy family for n=4 and characterize the n=4 Case B small (P_1 > L_0 AND P_5 < c(4)) gap.

---

### 1. V_j Strategy Family — VERIFIED

For n=4, L_0 = 1/31, c(4) = 16/31.

**V_j construction:** XY halves all 3 pieces NOT in {P_j, P_{j+1}}, using 3 marks.

| Strategy | XY marks | Singletons | LB formula | Condition |
|----------|----------|------------|------------|-----------|
| V_1 | halve P_3, P_4, P_5 | {P_1, P_2} | 1/2 + d_1/2 | d_1 ≤ L_0 (beta ≤ 0) |
| V_2 | halve P_1, P_4, P_5 | {P_2, P_3} | 1/2 + d_2/2 | d_2 ≤ L_0 (gamma ≤ 0) |
| V_3 | halve P_1, P_2, P_5 | {P_3, P_4} | 1/2 + d_3/2 | d_3 ≤ L_0 (eta ≤ 0) |
| V_4 | halve P_1, P_2, P_3 | {P_4, P_5} | 1/2 + d_4/2 | d_4 ≤ L_0 (sigma ≤ 0) |

**Mark count:** Each V_j uses exactly 3 marks ≤ n = 4. ✓

**Piece count:** 3 halved pieces → 3 pairs + 2 singletons = 2 + 3*2 = 8 pieces. LB picks ceil(8/2) = 4. ✓

**Algebraic proof of V_1 (representative):** After halving P_3, P_4, P_5:
- 3 exact pairs {P_3/2, P_3/2}, {P_4/2, P_4/2}, {P_5/2, P_5/2}.
- 2 singletons {P_1, P_2}.
- By Pairing Cancellation (3 applications): LB = (P_3+P_4+P_5)/2 + lb_score({P_1,P_2}).
- lb_score({P_1,P_2}) = P_2 (LB picks the larger singleton).
- LB = (1-P_1-P_2)/2 + P_2 = 1/2 + (P_2-P_1)/2 = 1/2 + d_1/2 ≤ c(4) iff d_1 ≤ L_0. ✓
- Note: Pairing Cancellation applies regardless of the relative ordering of pairs vs singletons.

**Dispatch counterexample verification:** alpha=1.63, beta=-0.5 → d_1/L_0 = 0.5 < 1.
- V_1 applies: LB = 1/2 + 0.5*L_0/2 = 0.5 + 0.008065 = 0.508065 < c(4) = 0.516129. ✓ (Computed directly.)

---

### 2. CRITICAL FINDING: Sum Constraint Direction is WRONG in Current Proof

**The current n=4 Case B proof states:** "Sum constraint: 4*alpha + 3*beta + 2*gamma + eta < 5."

**This is the B_LARGE constraint.** The correct derivation:

From the parameterization (P_k = LB piece sizes, alpha=P_1/L_0-1, beta=d_1/L_0-1, etc.):
- P_5/L_0 = 21 - 4*alpha - 3*beta - 2*gamma - eta (derived from sum = 1).
- B_SMALL (P_5 < c(4) = 16*L_0) requires: P_5/L_0 < 16, i.e., **4*alpha + 3*beta + 2*gamma + eta > 5**.
- B_LARGE (P_5 ≥ c(4)) requires: 4*alpha + 3*beta + 2*gamma + eta ≤ 5.

The current proof's "Sum constraint < 5" corresponds to B_LARGE. The strategies S6/S4/S5/BPP were PROVED to cover B_LARGE using this constraint, but the section is LABELED as "Sub-case P_5 < c(4)" (B_SMALL). This is an internal contradiction.

**Consequence:** The n=4 Case B large is handled TWICE (Halve+IH and S6/S4/S5/BPP), and B_SMALL is NOT handled at all in the current proof.

---

### 3. Coverage Test: V_j + S6/S4/S5/BPP on B_SMALL

Computational test (200,000 random B_small configs):
- **Without V_j:** 1714 failures (0.86%) when S6/S4/S5/BPP all fail.
- **With V_j (all four):** 1105 failures remain in "all d_j > L_0" sub-case (0.55%).
- **With V_j + 3 more strategies (S_ae, S_sa, S_p2d4):** 270 failures (0.014%).
- **With V_j + 7 extra strategies:** ~24 failures per 2M configs (0.0012%).

The 7 additional singleton-pair strategies identified:
- **S_ae:** singletons {P_1, d_3}, condition |eta - alpha| ≤ 1. XY: cut P_4@P_3, cut P_5@P_2, halve (P_5-P_2). 3 marks.
- **S_sa:** singletons {P_1, d_4}, condition |sigma - alpha| ≤ 1. XY: halve P_2, halve P_3, cut P_5@P_4. 3 marks.
- **S_p2d4:** singletons {P_2, d_4}, condition |sigma-(1+alpha+beta)| ≤ 1. XY: halve P_1, halve P_3, cut P_5@P_4. 3 marks.
- **S_d3d4:** singletons {d_3, d_4}, condition |eta - sigma| ≤ 1. (Construction needs verification.)
- **S_d2d4:** singletons {d_2, d_4}, condition |gamma - sigma| ≤ 1.
- **S_d1d4:** singletons {d_1, d_4}, condition |beta - sigma| ≤ 1.
- **S_p3d4:** singletons {P_3, d_4}, condition |sigma-(2+alpha+beta+gamma)| ≤ 1.

Even with all these, ~24/2M failures remain. The remaining failures have large sigma (d_4 >> L_0) and large eta (d_3 >> L_0) with small alpha, beta. The optimizer confirms XY CAN achieve LB ≤ c(4) for these (e.g., optimal LB = 0.502 for config: a=1.0015, b=1.018, c=2.367, d=4.276, e=6.268 in L_0 units). But the strategy is a 4-near-pair structure with tiny singleton that resists algebraic characterization.

---

### 4. Structure of Remaining Hard Cases

For "all d_j > L_0" B_small cases the optimizer cannot be matched with known strategies, the structure found is:

**4-pair + tiny-singleton:** XY creates 4 approximate equal pairs from all 9 pieces (5 LB + 4 XY cuts), leaving one tiny singleton s. LB = (1+s)/2 ≤ c(4) iff s ≤ L_0.

Specific structure: In each hard case, XY uses 3 cuts to shadow P_4, P_3, P_2 in P_5 (approximately), and 1 cut in P_4 (leaving a tiny residual). The pairing is:
- {P_4(LB) ≈ P_5-cut1}: near-pair
- {P_3(LB) ≈ P_5-cut2}: near-pair
- {P_2(LB) ≈ P_5-cut3}: near-pair
- {P_1/2, P_1/2}: exact pair (halve P_1)
- Singleton: P_4 - (P_5-cut1-value) ≈ tiny

This works when |P_5 - (P_4+P_3+P_2)| is small, i.e., d_4 ≈ d_1+d_2+d_3 approximately. No clean algebraic formulation found.

---

### 5. Corrected n=4 Case B Small Proof Structure

The CORRECT structure for n=4 Case B small (P_1 > L_0 AND P_5 < c(4)) is:

**Step 1 (Halve+IH):** Handles P_5 ≥ c(4). PROVED.

**Step 2 (V_j strategies, NEWLY NEEDED):** Handles P_5 < c(4) with any d_j ≤ L_0:
- For j=1,2,3,4: if d_j ≤ L_0, use V_j → LB = 1/2 + d_j/2 ≤ c(4). 3 marks.

**Step 3 (All d_j > L_0 sub-case):** P_5 < c(4) AND all d_1,d_2,d_3,d_4 > L_0. This is NOT proved.
- Existing strategies S6/S4/S5/BPP are NOT proved to cover this region (they were proved for B_LARGE).
- Many additional strategies cover MOST cases but not all.
- The algebraic proof of complete coverage is OPEN.

Note: sigma = d_4/L_0 - 1 (derived from 5alpha+4beta+3gamma+2eta+sigma = 16). If sigma ≤ 0, then d_4 ≤ L_0 and V_4 applies. Otherwise all 5 shifted parameters are positive.

---

### 6. Dead End: S6/S4/S5/BPP Coverage for B_SMALL

**Do NOT attempt to prove B_SMALL using S6/S4/S5/BPP with the "sum < 5" constraint.** 
- The constraint 4alpha+3beta+2gamma+eta < 5 is the B_LARGE condition. It CANNOT hold in B_SMALL.
- Any coverage argument using this constraint is vacuously false for B_SMALL configs.
- These strategies INDIVIDUALLY can work for some B_SMALL configs (when their conditions happen to hold), but the existing coverage PROOF doesn't apply.

---

### 7. Key Algebraic Identities Verified

**V_j LB formula (general):** For V_j (halve all pieces except {P_j, P_{j+1}}):
- 3 exact pairs {P_k/2, P_k/2} for k ≠ j, j+1.
- 2 singletons {P_j, P_{j+1}}.
- LB = (1 - P_j - P_{j+1})/2 + P_{j+1} = 1/2 + (P_{j+1}-P_j)/2 = 1/2 + d_j/2.
- Works when d_j ≤ L_0. Proven for all j=1,2,3,4.

**4-pair + 1 singleton (general):** For any strategy creating 4 exact pairs and 1 singleton s from 9 pieces:
- LB = (1+s)/2 by symmetric argument.
- LB ≤ c(4) = 1/2 + L_0/2 iff s ≤ L_0.

---

### 8. Distinct Openings for Outliner

1. **V_j + pigeon-hole:** In the "all d_j > L_0" sub-case, apply a pigeon-hole among {alpha, beta, gamma, eta, sigma} (weighted sum = 16, all > 0) to guarantee some pairwise difference ≤ 1 (in L_0 units). Rule 43 suggests this works for n ≤ 9. The constraint is 5alpha+4beta+3gamma+2eta+sigma = 16 with B_small (alpha+beta+gamma+eta+sigma < 11). Need to find which pair is ≤ 1.

2. **V_j + min-diff lemma:** Among ALL pairwise differences of {P_1/L_0, d_1/L_0, d_2/L_0, d_3/L_0, d_4/L_0}, if all are > 1, derive a contradiction from the sum constraint. This would complete the B_SMALL proof.

3. **V_j + 4-pair singleton bound:** For "all d_j > L_0," show that XY can always construct 4 pairs with singleton s ≤ L_0 using the SPECIFIC bound: XY cuts P_4 at (P_4 - P_3) or similar to match sub-pieces. The algebraic condition reduces to a linear inequality in {alpha, beta, gamma, eta, sigma}.

4. **Different case split:** Instead of splitting on "some d_j ≤ L_0 vs all > L_0," split on the MINIMUM of {beta, gamma, eta, sigma} (smallest shifted param) and show the corresponding strategy gives LB ≤ c(4) via the sum constraint.

---

### Summary for Outliner

- **V_j strategies:** VERIFIED. Each uses 3 marks. Condition: d_j ≤ L_0. Covers "some d_j ≤ L_0" sub-case of B_SMALL completely.
- **Sum constraint direction:** The current n=4 "Case B small" proof has the WRONG sum constraint direction. The strategies S6/S4/S5/BPP were proved for B_LARGE (sum < 5), not B_SMALL (sum > 5). The "Case B for n=4" section after "Sub-case P_5 < c(4)" must be rewritten.
- **Remaining gap:** B_SMALL "all d_j > L_0" is UNPROVED. Computationally, XY always achieves LB ≤ c(4), but the algebraic proof is open.
- **Candidate technique:** Pigeon-hole on the 5-dimensional sum constraint 5alpha+4beta+3gamma+2eta+sigma = 16 to force some pairwise difference ≤ 1 (L_0 units).
- **Knowledge-base entries:** Singleton-Pair Formula (certified), Pairing Cancellation Lemma (certified), pigeon-hole (n(n+1)(4n-1)/6 > 2^n-1 for n ≤ 9).
