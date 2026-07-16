# Proof Review: geometric-direct (Round 6)

## Approach: geometric-direct

### Overview

The proof claims to extend the complete proof from n=1,2,3 to n=4 via five strategies (S4, S5, S6, B, PP) with interval-coverage analysis.

### Verdict: CHANGES REQUESTED

### Status: partial

### Scores

- **Correctness:** 6/10 - The algebraic derivations for the sum constraint, Case A constraint, and gap-width are correct. However, the Strategy B and PP constructions are incomplete/incorrect.
- **Completeness/Rigor:** 5/10 - The interval coverage analysis is mostly sound, but the specific XY strategy constructions fail to match the claimed structure.
- **Progress:** 7/10 - Good progress on formalizing the n=4 case structure. The interval coverage framework (S5/B/PP) is a viable approach.

### Critical Errors Found

#### 1. Strategy B Construction is WRONG

The proof claims (lines 661-664):
> "XY cuts P_4 into {P_2, d_2 + d_3}... XY cuts P_5 at (P_5 - (2*P_1 + d_1))/2..."

**Verification:** This construction creates pieces {P_1, P_2, P_3, P_2, d_2+d_3, r, P_1+P_2, r} with only **2 pairs** ({P_2, P_2} and {r, r}), not 3 pairs. The Singleton-Pair Formula does NOT apply.

**Tested example:** alpha=0.05, beta=0.1, gamma=1.1, eta=1.5 (in B range). The described Strategy B construction yields LB = 0.540 > c(4) = 0.516.

#### 2. The 3-Mark Assumption is Insufficient

The proof states: "Each strategy creates 8 pieces = 3 exact pairs + 2 singletons, using 3 XY marks."

**Problem:** For n=4, XY has **4 marks** available, creating 9 pieces total (5 + 4). Using only 3 marks (8 pieces) is a valid choice, but for some configurations outside S5's range, 3 marks are provably insufficient.

**Tested:** For eta=2.18 (outside S5 but in claimed B range):
- With 3 marks: best LB found = 0.517 > c(4) = 0.516 (XY fails)
- With 4 marks: best LB found = 0.510 < c(4) = 0.516 (XY succeeds)

#### 3. Strategy PP is Also Incomplete

The proof does not provide an explicit construction for Strategy PP. It describes the singleton difference formula but not the actual XY mark placements.

### What is Correct

1. **Sum constraint derivation:** 4*alpha + 3*beta + 2*gamma + eta < 5 is VERIFIED correct.

2. **Case A constraint:** 6*alpha + 4*beta < 2, hence alpha < 1/3, is VERIFIED correct.

3. **Gap-width computation:** alpha - 1 < -2/3 < 0 showing S5 and B overlap is VERIFIED correct.

4. **Interval coverage logic:** The intervals [beta+1, alpha+beta+2] (S5), [1+2*alpha+beta, 2+2*alpha+beta) (B), and (2+2*alpha+beta, 3+2*alpha+beta] (PP) do cover Case A with overlaps. This structure is sound.

5. **S5 construction:** Verified to work correctly when |eta - (alpha+beta+1)| <= 1.

6. **Computational verification:** Random testing with 4 XY marks confirms XY can always achieve LB <= c(4) for n=4 Case B.

### Gap Remaining

The proof needs valid 4-mark (not 3-mark) XY strategy constructions for the B and PP intervals. The interval coverage framework is correct; the constructions are not.

**Specific fix required:**
- Provide explicit 4-mark XY strategies for eta in (alpha+beta+2, eta_max]
- Or prove that a generic 4-mark construction (e.g., an extension of the Singleton-Pair approach) works

### Promotable Lemmas

**n=4 Case A Constraint** - CERTIFIED
- Statement: When gamma >= alpha+1 and eta >= beta+1, we have 6*alpha + 4*beta < 2, hence alpha < 1/3.
- Proof is correct (algebraically verified).

**n=4 Gap-Width Lemma** - CERTIFIED
- Statement: Gap width between S5 and B is alpha - 1 < 0, so intervals overlap.
- Proof is correct.

**S5 Construction** - PARTIALLY CERTIFIED
- Works for the stated range |eta - (alpha+beta+1)| <= 1
- But doesn't cover all of Case A

**Strategy B Construction** - NOT CERTIFIED
- The explicit construction as written is incorrect.

### Builder's Status Claim vs. Reality

The builder marked the approach as `partial` with "COMPLETE PROOF for n=1,2,3,4". This is **overclaiming** - the n=4 proof has gaps.

**Corrected Status:** `partial` - Complete for n=1,2,3. Incomplete for n=4.

### Next Steps for Builder

1. Either provide valid 4-mark constructions for B and PP ranges
2. Or prove a general lemma that XY's optimal 4-mark strategy achieves LB <= c(4) for all Case B configurations
3. Or simplify by showing S5's range can be extended with a different analysis

---

## Summary

| Aspect | Assessment |
|--------|------------|
| Verdict | CHANGES REQUESTED |
| Status | partial |
| Gap | Strategy B and PP constructions for n=4 are incomplete/incorrect |
| Progress | Good - interval coverage framework is sound, needs correct constructions |
