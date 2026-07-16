# Proof Reviewer Report: Round 7

## Approach: geometric-direct

### Verdict: CHANGES REQUESTED
### Status: partial (n=1,2,3,4 PROVED; n>=5 OPEN)

---

## Summary

The n=4 Case B proof is **CORRECT** with one minor algebraic typo. The BPP unified construction is valid, and all four strategies (S6, S4, S5, BPP) together cover all Case B configurations for n=4. The proof is now complete for n=1,2,3,4.

However, the status remains **partial** because n>=5 is not proved (only computationally verified).

---

## Detailed Verification

### 1. BPP Construction Validity (d_3 > P_1)

**VERIFIED CORRECT.**

In BPP range: eta >= 1 + 2*alpha + beta.

Since alpha < 1/3 (from Case A constraint 6*alpha + 4*beta < 2) and beta > 0:
- eta_min = 1 + 2*alpha + beta > 1 > 1/3 > alpha

Therefore d_3 = (1 + eta)*L_0 > (1 + alpha)*L_0 = P_1 always holds in BPP range.

The cut inside d_3 at position P_1 is always valid.

### 2. Singleton-Pair Formula Application

**VERIFIED CORRECT.**

The BPP construction creates:
- Pairs: {P_3, P_3} (one from LB, one from cutting P_4), {P_1, P_1} (one from LB, one from cutting d_3), {P_5/2, P_5/2} (from halving P_5)
- Singletons: {P_2, d_3 - P_1}

By the certified Singleton-Pair Formula:
LB = 1/2 + |s_2 - s_1|/2 = 1/2 + |P_2 - (d_3 - P_1)|/2 = 1/2 + |P_1 + P_2 - d_3|/2

This formula handles both B range (d_3 < P_1 + P_2) and PP range (d_3 > P_1 + P_2) via the absolute value.

### 3. Algebraic Bound for PP Range

**VERIFIED CORRECT with minor typo.**

In PP range: eta > 2 + 2*alpha + beta
Singleton difference = (eta - 2 - 2*alpha - beta)*L_0

From sum constraint + Case A (gamma >= alpha + 1):
eta < eta_max = 5 - 4*alpha - 3*beta - 2*gamma <= 3 - 6*alpha - 3*beta (with gamma = alpha + 1)

Maximum singleton diff = eta_max - (2 + 2*alpha + beta)
                       = (3 - 6*alpha - 3*beta) - (2 + 2*alpha + beta)
                       = **1 - 8*alpha - 4*beta** (NOT 5*beta as stated in approach file)

This is still strictly < 1 for all alpha, beta > 0, so the proof is valid.

**TYPO:** Line 701 says "1 - 8*alpha - 5*beta" but should be "1 - 8*alpha - 4*beta".

### 4. Numerical Verification

**VERIFIED CORRECT.**

I independently tested:
- 5000 random Case A configurations: 0 failures
- All explorer's test cases (eta = 1.20, 1.50, 2.18, 2.20, 2.25, 2.29): all pass
- Edge cases (B/PP boundary, S5 upper bound, BPP lower bound): all pass

The Singleton-Pair Formula gives correct LB values matching explicit greedy computation.

### 5. Interval Coverage

**VERIFIED CORRECT.**

- S6 covers |gamma - alpha| <= 1 (explicit 3-mark construction)
- S4 covers |eta - beta| <= 1 (explicit 3-mark construction)  
- S5 covers |eta - (alpha + beta + 1)| <= 1, i.e., eta in [alpha+beta, alpha+beta+2] (explicit 3-mark construction)
- BPP covers eta in [1 + 2*alpha + beta, eta_max) (explicit 3-mark construction)

Gap between S5 and BPP: (1 + 2*alpha + beta) - (alpha + beta + 2) = alpha - 1 < -2/3 < 0

**Negative gap width = OVERLAP.** No uncovered configurations exist.

In Case A (gamma >= alpha+1, eta >= beta+1):
- S5's effective range: [beta+1, alpha+beta+2]
- BPP's range: [1+2*alpha+beta, eta_max)
- Union covers [beta+1, eta_max) = all valid eta in Case A

---

## Errors Found

1. **Minor typo:** Line 701 states "1 - 8*alpha - 5*beta" but the correct formula is "1 - 8*alpha - 4*beta". This does not affect correctness since both are < 1 for alpha, beta > 0.

---

## Remaining Gap

**n >= 5 is NOT PROVED.** The proof is complete for n = 1, 2, 3, 4 only.

The approach correctly notes this: "n >= 5: OPEN. Computationally verified (0/200k failures)."

To achieve Status = solved, a general proof for all n is required.

---

## Promotable Lemmas Review

### 1. BPP Unified Construction
**CERTIFIED.**

*Statement:* For n=4 Case A with eta in [1+2*alpha+beta, eta_max), XY uses 3 marks: (1) cut P_4 at P_3 from left, (2) cut d_3 at P_1 from left, (3) halve P_5. This creates pairs {P_3,P_3}, {P_1,P_1}, {P_5/2,P_5/2} and singletons {P_2, d_3-P_1}. LB = 1/2 + |P_1+P_2-d_3|/2 <= c(4).

*Verification:* Construction validity (d_3 > P_1) proved. Formula verified against explicit computation. All test cases pass.

### 2. BPP Range Bound
**CERTIFIED with correction.**

*Statement:* In the BPP range eta in [1+2*alpha+beta, eta_max), the singleton difference |2+2*alpha+beta-eta| is at most 1 (in reduced units), hence LB <= c(4). In particular, for eta approaching eta_max = 3-6*alpha-4*beta (using gamma = alpha+1), the difference approaches 1 - 8*alpha - 4*beta < 1.

*Note:* Approach file says "5*beta" but correct is "4*beta".

---

## Scores

- **Correctness:** 9/10 (minor typo in coefficient)
- **Completeness/Rigor:** 9/10 (n=1,2,3,4 complete; n>=5 gap acknowledged)
- **Progress:** Major (closed the B/PP gap for n=4 with explicit 3-mark constructions)

---

## Action Items

1. Fix the typo on line 701: change "5*beta" to "4*beta"
2. For Status = solved: prove n >= 5 (either by generalizing the level-k strategy family or by a different approach)

---

## Record Outcome

Calling `record_outcome` with:
- outcome: advanced (closed n=4 B/PP gap)
- note: n=4 Case B PROVED via unified BPP 3-mark construction; typo 5beta->4beta; n>=5 open
