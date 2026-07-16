# Proof Reviewer Report: Round 9

## Approach: geometric-direct

### Verification of Key Claims

#### 1. ERROR FIX: "Case B Trivial" Claim Removed

**VERIFIED.** The erroneous claim "If P_{n+1} <= c(n), XY uses 0 marks and LB picks P_{n+1} <= c(n)" has been removed from `current.md`. The approach file now has a strikethrough note explaining why it was wrong:

> "This claim was WRONG for n >= 2. With 0 XY marks and n+1 pieces, LB picks ceil((n+1)/2) pieces (not just the largest)."

This is correct. Counterexample verified: n=2 with P={1/3, 1/3, 1/3}, LB picks 2 pieces totaling 2/3 > c(2) = 4/7.

#### 2. HALVE + IH STRATEGY (Part 2.5)

**VERIFIED ALGEBRAICALLY.** I independently re-derived the key identity.

**Mark count:** 1 + (n-1) = n. CORRECT.

**Pairing Cancellation application:** CORRECT. Halving P_{n+1} contributes exactly P_{n+1}/2 to LB's score.

**Key identity: c(n-1)*(1-c(n)) = c(n)/2**

Independent derivation:
```
c(n-1) = 2^{n-1}/(2^n - 1)
1 - c(n) = (2^n - 1)/(2^{n+1} - 1)

c(n-1)*(1-c(n)) = [2^{n-1}/(2^n - 1)] * [(2^n - 1)/(2^{n+1} - 1)]
                = 2^{n-1}/(2^{n+1} - 1)    [The (2^n - 1) terms CANCEL]
                = c(n)/2                    [Since c(n) = 2^n/(2^{n+1} - 1)]
```

Numerically verified for n=1,...,10. **IDENTITY CORRECT.**

**Decreasing function:** f(x) = x/2 + c(n-1)*(1-x) has f'(x) = 1/2 - c(n-1) < 0 since c(n-1) > 1/2 for all n >= 1. CORRECT.

**Conclusion:** f(P_{n+1}) <= f(c(n)) = c(n) when P_{n+1} >= c(n). **PROVED.**

---

### CRITICAL GAP FOUND

**The proof has a structural gap in Case B for n >= 2.**

The proof structure says:
- "If P_{n+1} <= c(n), the trivial case applies. So assume P_{n+1} > c(n)."
- Then proceeds to prove only for P_{n+1} > c(n).

**The "trivial case" (0 marks) was WRONG and has been removed.** But it was NOT replaced with a correct strategy for P_{n+1} < c(n)!

**The Halve+IH Strategy handles P_{n+1} >= c(n), NOT P_{n+1} < c(n).**

**Gap region:** Configs with P_1 > L_0 AND P_{n+1} < c(n).

**Verification that gap region is non-empty (n=2 example):**
- P = [0.18, 0.35, 0.47]
- P_1 = 0.18 > L_0 = 1/7 (Case B)
- P_3 = 0.47 < c(2) = 4/7 (gap sub-case)
- d_1 = 0.17 > L_0 (halving strategy fails)

**Halving P_3 gives LB = 0.585 > c(2) = 0.571. FAILS.**

**However, the B2b strategy (split P_3 at P_2) gives LB = 0.53 <= c(2). WORKS.**

The math is correct for all configs (verified computationally: XY can always limit LB to <= c(n) using at most n marks), but the PROOF doesn't cover the case P_{n+1} < c(n). The proof assumes P_{n+1} > c(n) throughout.

---

### Goal Progress

**Proved:**
- Lower bound for all n: COMPLETE
- Upper bound Case A (P_1 <= L_0) for all n: COMPLETE
- Upper bound Case B when P_{n+1} >= c(n) for all n >= 2: COMPLETE (Halve+IH)
- Upper bound Case B for n=1: COMPLETE

**GAP:**
- Upper bound Case B when P_1 > L_0 AND P_{n+1} < c(n) for n >= 2

The explicit n=2,3,4 Case B proofs DO cover this case when P_{n+1} > c(n) (via the d_j < L_0 argument). But the structural claim "If P_{n+1} <= c(n), trivial case applies" is WRONG and uncorrected.

The fix is simple: The proof's strategies (B2b for n=2, S1/S2/S3 for n=3, etc.) actually work for ALL P_1 > L_0 configs, not just P_{n+1} > c(n). The d_j < L_0 bounds come from either:
1. P_{n+1} > c(n) (as currently proved), OR
2. Other constraints that force small differences even when P_{n+1} < c(n)

But this is NOT currently proved in the approach file.

---

### Scores

- **Correctness:** 7/10 — The math that IS proved is correct. The Halve+IH Strategy and identity are verified. But the proof structure has a gap.
- **Completeness/Rigor:** 5/10 — Significant gap: Case B for P_{n+1} < c(n) is NOT proved for n >= 2.
- **Progress:** +1 — Halve+IH Strategy proved and identity verified. This closes part of Case B but not the "small pieces" sub-case.

---

### True Status

**partial**

The proof is correct for:
- n = 1 (complete)
- n >= 2: Case A and Case B when P_{n+1} >= c(n)

The proof is INCOMPLETE for:
- n >= 2: Case B when P_{n+1} < c(n) (the "small pieces" sub-case)

The builder marked this as partial, which is correct. But the specific gap description was wrong — it said the gap is for n >= 5, when in fact the gap exists for n >= 2.

---

### Promotable Lemmas

**Halve + IH Strategy Lemma:** CERTIFIED. The proof is complete and the identity c(n-1)*(1-c(n)) = c(n)/2 is verified.

**Algebraic Identity c(n-1)*(1-c(n)) = c(n)/2:** CERTIFIED. Independently verified.

---

## Verdict: CHANGES REQUESTED

**Status: partial**

**Specific gap to close:**

The proof structure claims "If P_{n+1} <= c(n), trivial case applies" for n >= 2, but this is WRONG. The "trivial case" (0 marks) was correctly identified as wrong and removed, but it was NOT replaced with a correct proof for the case P_{n+1} < c(n).

**To fix:** Either:
1. Extend the explicit proofs (S1/S2/S3, B2a/B2b, etc.) to cover P_{n+1} < c(n) directly, showing the same strategies work, OR
2. Prove that in Case B (P_1 > L_0), the constraint P_1 + ... + P_n + P_{n+1} = 1 with P_1 > L_0 forces P_{n+1} > c(n) or some d_j < L_0. This would close the gap.

The Halve+IH Strategy is a real advance (closing the P_{n+1} >= c(n) sub-case), but it does NOT close the P_{n+1} < c(n) sub-case.
