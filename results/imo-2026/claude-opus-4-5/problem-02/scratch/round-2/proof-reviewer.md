# Proof Review: complex-identity (IMO 2026 P2)

## Verdict: CHANGES REQUESTED
## Status: partial

---

## Summary

The proof presents a sophisticated algebraic approach using complex coordinates and polynomial ideal membership. The strategy is sound and the result appears correct (OM = ON), but **the proof is not yet rigorous** because it relies on computational verification claims ("verified symbolically", "verified by polynomial division") rather than explicit mathematical derivations.

---

## Step-by-Step Analysis

### Steps 1-4: Coordinate Setup and Reformulation
**CORRECT.** The circumcenter formula, target reformulation, and encoding of angle conditions are all mathematically sound. The derivations are explicit and can be verified.

### Step 5: Parameterization from C1
**CORRECT.** The parameterization k = b(1 - mu exp(-i alpha)), l = c(1 - nu exp(i alpha)) correctly encodes the constraint C1 = 0. Verification:
- (k-b) = -b mu exp(-i alpha)
- (l-c) = -c nu exp(i alpha)
- bc / ((k-b)(l-c)) = 1/(mu nu) > 0, confirming C1 is satisfied.

### Step 6: Decoupling of C2 and C3
**CLAIMED BUT NOT RIGOROUSLY DERIVED.**

The claim is that C2 = mu |c|^2 C2_q(nu) where C2_q depends only on nu. I verified this:
- **Symbolically:** C2 factors as mu * |c|^2 * (polynomial in nu only). Confirmed.
- **Numerically:** C2/mu is constant across different mu values for fixed nu. Confirmed.

The proof states "verified by direct symbolic computation" but does **not show the explicit derivation**. The claim is TRUE but the derivation is missing. This is a gap for a rigorous proof.

**Required fix:** Show the explicit factorization derivation, not just state it was "verified."

### Step 7: The Polynomial Certificate (CRITICAL GAP)
**CLAIMED BUT NOT PROVEN.**

The proof claims T lies in the ideal <C2_q, C3_q>, meaning T = P_1 C2_q + P_2 C3_q for some polynomials P_1, P_2. This is the **core mathematical claim** of the proof.

The proof says:
- "This is verified by symbolic polynomial division"
- "Both remainder_1 and remainder_0 are identically zero"
- An "explicit form of the certificate" is given but labeled "optional verification"

This is **not a proof** but a claim of computational verification. For a rigorous mathematical proof, one must either:
1. Exhibit P_1 and P_2 explicitly and verify the identity T = P_1 C2_q + P_2 C3_q by expansion, OR
2. Perform the polynomial division explicitly with all intermediate steps shown.

I numerically verified that T = 0 on V(C2_q, C3_q) for 8 random configurations with |OM - ON| < 10^{-10}. This is strong evidence but not a proof.

**Required fix:** The polynomial certificate identity must be derived or verified explicitly, not just claimed.

### Step 8: F Nonzero for Valid Configurations
**ARGUMENT IS IMPRECISE BUT CONCLUSION APPEARS CORRECT.**

The proof claims F = 2 Im(conj(b) c exp(i alpha)) is nonzero for valid configurations. The geometric argument is hand-wavy ("the interior requirements... cannot be satisfied simultaneously").

My numerical investigation:
- When F = 0 exactly (alpha = -arg(conj(b)c) or alpha = pi - arg(conj(b)c)), I found that solutions (mu, nu) to C2_q = C3_q = 0 exist but **K and L are not in the required triangular regions**.
- No valid configuration (K in BMC, L in BNC, all angle conditions satisfied) was found with F = 0.

The claim appears correct but the proof's geometric argument is insufficient. A rigorous proof would need to show formally why the interior constraints exclude F = 0.

**Required fix:** Strengthen the geometric argument or provide an algebraic proof that the system {F=0, C2_q=0, C3_q=0, interior constraints} is inconsistent.

### Step 9: Conclusion
The logic is correct: if the certificate holds and F is nonzero, then T = 0 on the variety, hence OM = ON.

---

## Scores

| Criterion | Score | Notes |
|-----------|-------|-------|
| **Correctness** | 7/10 | No errors found, but key claims unproven |
| **Completeness/Rigor** | 5/10 | Steps 6, 7, 8 rely on "verified" claims without derivation |
| **Progress** | 8/10 | Clear strategy, good structural insights, numerical verification |

---

## Specific Gaps to Close

1. **Step 6 (Decoupling):** Provide the explicit derivation of the factorization C2 = mu |c|^2 C2_q(nu), not just "verified symbolically."

2. **Step 7 (Certificate):** This is the critical gap. Either:
   - Write out P_1 and P_2 explicitly and verify T = P_1 C2_q + P_2 C3_q by term-by-term expansion, OR
   - Show the polynomial division steps explicitly with intermediate forms.

3. **Step 8 (F nonzero):** Replace the hand-wavy geometric argument with either:
   - A rigorous geometric proof, OR
   - An algebraic proof that the variety V(F, C2_q, C3_q) intersected with the interior conditions is empty.

---

## Status Determination

The builder marked this as `solved`. This is **incorrect**. The proof has the right structure and the result is almost certainly true, but three key steps rely on computational claims without rigorous derivation. Per CLAUDE.md rigor rules:
- "No hand-waving" - Steps 7 and 8 have hand-waving
- "Name your tools" - The "polynomial division" is invoked but not performed explicitly

**True Status: partial**

The proof is 70-80% complete. The remaining work is to make Steps 6-8 rigorous, which should be straightforward given the correct structural insights already established.

---

## Promotable Lemmas

**Circumcenter formula:** The formula in the proof is correct and already in knowledge_base.md. No need to promote.

**Midpoint distance condition:** Correct but trivial. Not worth promoting.

**Decoupling Lemma:** Problem-specific and not fully proven in this approach. **Reject** until the derivation is explicit.

---

## Verdict: CHANGES REQUESTED

The approach is correct and close to complete, but the proof is not yet rigorous. The builder should:
1. Make Step 6 derivation explicit
2. Provide the explicit polynomial certificate for Step 7
3. Strengthen the F nonzero argument in Step 8

Once these gaps are closed, the proof will be complete.
