## imo-2026-03 (lens: refined-R branches and lower-bound unification)

### Summary of lens

This round I investigated: (1) whether T(ℓ)/GAP-A for anchor R=G_{n−1} automatically gives refined-R cases; (2) how T(ℓ) can be closed; (3) the structure of G-INC-2 and GAP-B refined R; (4) the cleanest proof ordering.

---

### MAIN FINDING: T(ℓ) closes by the SAME mutual induction as Claim(n,ε)

**T(ℓ) statement:** For `S_P ⊆ S_{G_{ℓ−1}}`, `|P| ≤ ℓ+1`, `ΣP ∈ (2^ℓ−1, 2^ℓ)`, prove `O_P ≤ O_{G_{ℓ−1}}`.

**Key arithmetic:** Write `τ = 2^ℓ − ΣP ∈ (0,1)`. Then T(ℓ) ⟺ `deficit_top + M ≥ 1−τ` via the certified top-band decomposition. This is strictly WEAKER than Claim(n,0)'s target `≥ 1`.

**Case h ≥ 4 is IMPOSSIBLE for T(ℓ):** Four parts each ≥ 2^{ℓ−2} would sum to ≥ 4·2^{ℓ−2} = 2^ℓ > ΣP. Strict impossibility, verified for ℓ = 2,3,4,5. (For Claim(n,ε), h≥4 gives M ≥ A(G_{n−3})−ε ≥ 1−ε; for T(ℓ) this case simply cannot arise.)

**Case h = 0 (NEW, not in Step 12 of the current approach):** All parts < 2^{ℓ−2}, so δ_top = 0, deficit_top = 2^{ℓ−2} ≥ 1 ≥ 1−τ. Trivially done. (This also resolves the reviewer-flagged unwritten h=0 gap in Step 12 for Claim(n,ε), where the same argument gives deficit_top = 2^{n−2} ≥ 1 ≥ 1−ε.)

**Case h = 2 (same structure as Claim):** Let q₁ ≥ q₂ be the two parts ≥ 2^{ℓ−2}. Put a = 2^{ℓ−1}−q₁ ≥ 0, b = q₂−2^{ℓ−2} ≥ 0, ε' = a−b−τ. Then ΣP_lo = 2^{ℓ−2}+ε'. deficit_top = a+b.

- **Sub-case 2a (a+b ≥ 1−τ):** deficit_top ≥ 1−τ. Done.
- **Sub-case 2b-i (ε' ≥ 0):** ε' = a−b−τ < 1 (since a+b < 1−τ forces a < 1). Apply Claim(ℓ−2, ε'): M ≥ 1−ε'. Total ≥ (a+b)+(1−ε') = 1+2b+τ ≥ 1−τ. ✓
- **Sub-case 2b-ii (ε' < 0):** ε' > −1 (since b < 1−τ, τ < 1 ⟹ ε' > −b−τ > −1). ΣP_lo ∈ (2^{ℓ−2}−1, 2^{ℓ−2}). Apply T(ℓ−2): O_{P_lo} ≤ O_{G_{ℓ−3}}, equivalently A(P_lo) ≤ A(G_{ℓ−3})−1−ε'. So M ≥ 1+ε'. Total ≥ (a+b)+(1+ε') = 1+2a−τ ≥ 1−τ. ✓

**CONCLUSION:** The inductive step for T(ℓ) invokes exactly Claim(ℓ−2, ε') and T(ℓ−2), mirroring the step for Claim(n,ε). The base cases T(1), T(2) are already proved in Step 11. Therefore, **Claim(n,ε) and T(n) are simultaneously proved by one mutual strong induction on n, with base n=1,2.** This CLOSES G-INC-1 = Claim(n,0) unconditionally for ALL n ≥ 1 (not just n ≤ 4).

Verified numerically: T(ℓ) holds with 0 violations at ℓ=2,3,4 (corrected O_G function, grid=4, budget enforced); min_margin = 0 in each case (tight).

---

### Refined-R is GENUINELY separate (not automatic from anchor)

**G-INC-2 (INC + refined R):** At n=4, the tight case is R = {4,4,4,2,1} (G₃ with 8→4+4 cut), Q = {5,5,4,2}:
- S_R = [0,1) ∪ [2,4). A(R) = 3.
- S_Q = [2,4). A(Q) = 2. S_Q ⊆ S_R. ✓
- A(Q ∪ R) = A(R)−A(Q) = 1. Exactly tight.
- KEY: S_Q = [2,4) is NOT a subset of S_{G₃} = [1,2) ∪ [4,8). So this Q is **NOT** in INC branch for anchor G₃. It only arises for the refined R.

**This disproves automatic inheritance:** G-INC-1 for anchor R=G_{n−1} does not cover G-INC-2. The proof must handle S_R's new band structure (which differs from S_{G_{n−1}}).

Numerically: G-INC-2 holds with 0 violations at n=4, joint budget enforced (377 configs spanning c_R=1,2,3). Min margin = 0 (tight at the case above).

**Why the anchor proof fails for refined R:** The top-band decomposition used `S_{G_{n−1}} ∩ [0,2^{n−2}) = [0,2^{n−2}) \ S_{G_{n−2}}` (anti-complementation identity, specific to G_{n−1}). For refined R, S_R ∩ [0,2^{n−2}) has a different shape (depends on which pieces were cut).

---

### Distinct openings

**Opening 1 (STRONGEST — closes G-INC-1 for all n):** Extend the two-step strong induction in ll-inclusion-gap Step 12 to simultaneously prove Claim(n,ε) AND T(n). T(n)'s inductive step is identical to Claim(n,ε)'s, with ε→τ and h∈{0,2} only. Write:

> **Step 12 extension (T(n) by mutual induction):** Add after Case h≥4 a new Case h=0 (trivial, deficit_top = 2^{n−2} ≥ 1−τ), then run the Case h=2 sub-cases (2a, 2b-i via Claim(n−2,ε'), 2b-ii via T(n−2)) with target 1−τ. Arithmetic is word-for-word the same as Claim(n,ε)'s inductive step. Base cases T(1) and T(2) are already Step 11. By mutual strong induction, T(n) holds for all n ≥ 1, closing G-INC-1 for all n.

**Opening 2 (G-INC-2, induction on c_R):** Prove G-INC-2 by induction on the number of extra cuts c_R in R. Base case c_R=0 is G-INC-1 (now closed by Opening 1). For the inductive step: cutting piece p of R_0 into {p₁, p₂} gives R with S_R = S_{R₀} △ ([0,p₂) ∪ [p₁,p)). Split into:
- **Case A (S_Q ∩ flipped region = ∅):** Then S_Q ⊆ S_{R₀} (since S_Q ⊆ S_R and S_Q avoids the flip). Apply IH (G-INC-2 for R_0). Also check A(R) vs A(R₀) to get A(Q) ≤ A(R)−1.
- **Case B (S_Q meets flipped region):** Q has mass in [0,p₂) or [p₁,p). The budget forces |Q| ≤ n, and the flipped region contributes extra symmetric-difference mass. Likely gives a direct bound.

This requires careful casework but the structure is clear. The budget c_R ≥ 1 ⟹ c_Q ≤ n−1 ⟹ |Q| ≤ n (not n+1), which may simplify Case B.

**Opening 3 (G-INC-2 via direct structural argument for refined R at n=4,5):** The n=4 case has |R| ∈ {5,6,7} and |Q| ∈ {2,3,4}. With few Q parts and the band structure of S_R more constrained, a direct top-band argument for each refinement type may work. The parity condition still holds: h = #{Q parts ≥ 2^{n−2}} is even (general parity lemma applies to any R). The top-band decomposition A(Q) = A(Q_lo) + δ_top also holds (general). The missing piece is bounding A(Q_lo) in terms of A(R_lo). For specific refinement types (e.g., cutting 2^{n−1} vs cutting a smaller piece), the S_R band structure splits into cases that each inherit a clean inequality.

**Opening 4 (GAP-B refined R via Cases 1/2/Sub-3a):** In the ll-dyadic-symdiff framework, Cases 1 (max(Q) ≥ 2^{n−1}+1), Case 2 (odd count), and Sub-3a (full dyadic level in S_Q △ S_R) ALL work for ANY R with max(R) ≤ 2^{n−1} — they don't use G_{n−1}'s specific structure. Only Sub-3b (double-REFL, GAP-B) is anchor-specific. So for GAP-B refined R: if S_Q ⊄ S_R (non-containment), first check if Cases 1/2/Sub-3a apply. The residual is a genuinely harder sub-3b with refined R. Key observation: the budget reduction (c_R ≥ 1 ⟹ |Q| ≤ n) may push more configs into Sub-3a.

**Opening 5 (unifying lemma across both routes and all R):** The cleanest unifying statement is: for any R refining G_{n−1} with A(R) ≥ 1, max(R) ≤ 2^{n−1}, and any Q partitioning 2^n with joint budget, A(Q ∪ R) = measure(S_Q △ S_R) ≥ 1. The anchor proofs (G-INC-1, GAP-B closed at n=3) establish this for R=G_{n−1}. The natural proof strategy is: EITHER (a) handle the non-containment case by Cases 1/2/Sub-3a (general) + Sub-3b anchor + Sub-3b refined-R argument OR (b) handle the containment case by G-INC-1 (anchor) + G-INC-2 (refined). These two routes are the same at the level of (S_Q ⊆ S_R) vs (S_Q ⊄ S_R), just with different R.

---

### Is a single unifying lemma possible across all R?

**Partial yes:** The INC reduction (A(Q∪R) = A(R)−A(Q) when S_Q ⊆ S_R) and the GAP branch (direct measure bound) both work for any R. The specific sub-tools (top-band decomp, SET IDENTITY, double-REFL) are anchor-specific but might generalize as follows:

- **Top-band decomp for general R:** A(Q) = A(Q_lo) + δ_top and A(R)−A(Q) = (δ_R_top − δ_top) + (A(R_lo) − A(Q_lo)), both terms ≥ 0 when S_Q ⊆ S_R. This is a general identity; the difficulty is bounding the sum ≥ 1 without the G_{n−1} structure.

- **SET IDENTITY for general R:** S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}} was the key engine. For a refinement R_0 obtained from G_{n−1} by cuts, S_{R_0} ∩ [0,2^{n−2}) changes. No clean analogue is known.

**Assessment:** Genuine separate work for G-INC-2 and GAP-B refined R. No single reduction that gives them for free from the anchor.

---

### Two-step induction IH strength check

**The two-step induction IH Claim(n,ε) is strong enough** to carry T(ℓ) without any strengthening:
- T(ℓ)'s 2b-i sub-case invokes Claim(ℓ−2, ε') with ε' ∈ [0,1) — exactly the existing Claim statement.
- T(ℓ)'s 2b-ii sub-case invokes T(ℓ−2) — the other half of the mutual induction, which is available by the strong induction hypothesis.
- The FALSE ε<0 extension of Claim was never used: T(ℓ)'s own target uses τ = 2^ℓ−ΣP (a sum BELOW 2^ℓ), but the invocations of sub-claims are at POSITIVE ε (for Claim) or genuinely sub-threshold (for T at the lower level). The rule "NEVER strengthen IH to Claim(n,ε) with ε<0" is respected throughout.

---

### Small-case / intuition notes (conjectural)

- T(3) at grid=4: 0 violations / 172 configs, min_margin=0 (tight). Tight instances have ΣP close to 8 (i.e., τ→0) and O_P close to 5 = O_{G₂}. E.g., P with two parts near 4 and ΣP = 7+δ.
- T(4) at grid=4: 0 violations / 452 configs, min_margin=0. Consistent with the induction working.
- G-INC-2 at n=4: 0 violations / 377 configs, min_margin=0. The unique tight case (found via sampling) is R={4,4,4,2,1}, Q={5,5,4,2}, A(R)−A(Q)=1. This structure (S_Q = [2,4) ⊆ S_R = [0,1)∪[2,4)) suggests the tight cases arise when S_Q aligns with one "allowed band" of S_R, which is not in S_{G_{n−1}}.
- (CONJECTURE) G-INC-2 might be provable by induction on c_R with a 2-case split (S_Q meets flipped region or not), since the budget reduction is significant.

---

### Candidate technique(s)

- **Mutual strong induction** (Claim(n,ε) and T(n) simultaneously): strongest and most direct; uses only existing certified machinery (top-band decomp, SET IDENTITY, parity condition).
- **Induction on refinement depth c_R** for G-INC-2: pairs with the above; inherits the anchor result as the base case.
- Knowledge-base: **"Generalize / induction loading / strengthening the hypothesis"** — the mutual induction IS exactly this: T(n) is a companion to Claim(n,ε) that was needed to close the 2b-ii sub-case.

### Cheap-kill candidates

- **h=0 write-up:** Both Claim(n,ε) and T(n) miss h=0 in Step 12. For both: deficit_top = 2^{n−2} ≥ 1 ≥ 1−ε or 1−τ. One line.
- **T(ℓ) base case T(2):** Already proved (O_P = p₁ ≤ 2 = O_{G₁} since |P|=2 and Forcing gives p₁ ≤ 2). No extra work.

### Knowledge-base entries to use

- **"Generalize: a stronger, cleaner statement is sometimes easier to prove by induction (induction loading / strengthening the hypothesis)"** — directly applicable to the Claim(n,ε)/T(n) mutual induction.

### Analogous past problems (cruxes)

Not consulted this round (time constraint); the mutual induction structure is internal to the problem's certified machinery.

### Prior progress

- G-INC-1 proven for n≤4; general n reduced to T(ℓ) (R7).
- T(ℓ) verified 0 violations at ℓ=2,3,4.
- GAP-B closed at n=3 for anchor; B3a, B3b for all n (anchor).
- G-INC-2 vacuous at n=3; first nontrivial n=4, 0 violations.

### Dead ends (do not retry)

- **Claim(n,ε) with ε<0:** FALSE, counterexample Q_lo={1.9,1.5}. Do not extend T by this route.
- **h≥4 sub-case for T(ℓ):** Impossible (4·2^{ℓ−2} = 2^ℓ > ΣP). Do not case-split on h≥4 in T(ℓ)'s proof.
- **Monotonicity of A(Q∪R) in R (naive):** Cutting a piece of R can increase or decrease A(Q∪R). No simple monotone reduction G-INC-1 → G-INC-2.
- **SET IDENTITY for refined R:** S_{G_{n−1}} ∩ [0,2^{n−2}) = S_{G_{n−3}} is specific to G_{n−1}. No analogue for general R. Do not try to generalize the SET IDENTITY directly.

### Ordering for remaining lower-bound pieces

1. **T(ℓ) (all n):** Extend Step 12 of ll-inclusion-gap to prove T(n) by mutual induction with Claim(n,ε). Write the h=0 case (trivial) and h=2 cases (same arithmetic with τ). This closes G-INC-1 for all n via the Step 13 logical accounting.
2. **h=0 write-up for Claim(n,ε):** The unwritten h=0 sub-case in Step 12 (reachable n≥5, trivially true: deficit_top = 2^{n−2} ≥ 1 ≥ 1−ε).
3. **G-INC-2 (refined R):** New proof required. Recommended approach: induction on c_R with split on whether S_Q meets the flipped region under the extra cut.
4. **GAP-B refined R:** Cases 1/2/Sub-3a from ll-dyadic-symdiff apply for any R. Residual is Sub-3b with refined R; investigate whether budget reduction (|Q| ≤ n for c_R ≥ 1) gives easier sub-cases.
