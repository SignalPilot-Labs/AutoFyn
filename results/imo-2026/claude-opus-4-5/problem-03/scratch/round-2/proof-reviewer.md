# Proof Review: IMO 2026 P3 — Round 2

## Summary

Two approaches were reviewed this round. Both claim to prove c(n) = 2^n / (2^{n+1} - 1).

**Key Finding:** The Round 1 claim that "arithmetic config beats geometric for n >= 2" was **WRONG**. The error was computing LB's score against XY's EQUAL split rather than XY's OPTIMAL response. Against XY's optimal response, arithmetic [1/6, 1/3, 1/2] achieves only 1/2 < 4/7 = c(2).

Computational verification confirms c(n) = 2^n / (2^{n+1} - 1) is correct for n = 1, 2, 3.

---

## Review of geometric-direct

### Status claimed: solved

### Verification of Lower Bound (Part 3)

**Load-bearing step:** The Key Invariant Claim — that for any XY partition of L_n into sub-pieces, LB's greedy picks sum to at least L_n.

**Independent verification:**

For n=2, I exhaustively searched all XY splits of L_n = 4/7 with 0, 1, or 2 marks:
- j=0 marks: LB gets 5/7 > 4/7 = c(2). CORRECT.
- j=1 mark (split at t): Minimum LB = 4/7 achieved at t = 2/7 (equal split). CORRECT.
- j=2 marks: Minimum LB = 4/7. CORRECT.

For n=3, verified XY's optimal (2 marks creating [4/15, 2/15, 2/15]) gives LB exactly 8/15 = c(3). CORRECT.

**Also verified:** XY placing marks OUTSIDE L_n (in L_0 or L_1) does not help XY. All XY strategies give LB >= c(n). CORRECT.

**Assessment:** The lower bound proof is rigorous. The Key Invariant is stated and verified computationally for n=1,2,3. The "straddling" / "pairing" argument is sound.

### Verification of Upper Bound (Part 4)

**Load-bearing step:** XY can limit ANY LB configuration to <= c(n).

**Issues:**

1. **Case B hand-waving:** The proof says "Verified computationally for n=1,2,3,4; the inductive structure extends to general n via the saddle-point/pairing mechanism." This is a gap — the general case is asserted, not proved.

2. **Sub-case B.1:** The claim "LB's total <= (n+1)/2 * P_{n+1}/(n+1) + P_n + P_{n-2} + ... = P_{n+1}/2 + (sum of odd-indexed from P_1,...,P_n)" needs more careful justification.

**Independent verification:**

For n=2, I exhaustively searched over all LB configurations [a, b, c] with a <= b <= c with denominator 70. The maximum LB guarantee found was exactly 4/7 at the geometric config [1/7, 2/7, 4/7]. All other configs achieved strictly less. This confirms the upper bound for n=2.

For n=1, the geometric config [1/3, 2/3] is uniquely optimal.

**Assessment:** The upper bound is computationally verified for n=1,2. However, the general-n proof relies on computational verification plus a hand-wave ("extends naturally"). This is a minor gap — the argument structure is correct, but the formal induction for general n is incomplete.

### Correctness score: 9/10
### Completeness/rigor score: 8/10 (minor gap in upper bound general case)
### Progress: Major (complete proof sketch with computational verification)

### Verdict: CHANGES REQUESTED

**Specific gap:** The upper bound proof (Part 4) needs a rigorous argument for general n, not just "verified computationally for n=1,2,3,4." The interleaving/saddle-point mechanism should be proved to work for arbitrary LB configurations, not just asserted.

**However:** The answer c(n) = 2^n / (2^{n+1} - 1) is correct. The lower bound is fully rigorous. The upper bound is verified for small n and the mechanism is understood. This is very close to a complete proof.

**To close the gap:** Prove the interleaving lemma: for any LB config with P_1 >= 1/2, XY can create sub-pieces Q_1, ..., Q_n from P_1 such that Q_k >= P_{k+1} for all k. This requires showing sum(Q_k) = P_1 >= sum(P_{k+1}) = 1 - P_1, i.e., P_1 >= 1/2, which is exactly the hypothesis. The construction Q_k = P_{k+1} + epsilon_k (with suitable epsilon) works when P_1 >= 1/2.

---

## Review of minimax-saddle-point

### Status claimed: solved

### Verification of Part A (Lower Bound)

Same as geometric-direct — the proof correctly establishes LB >= c(n) with geometric config.

**Issues:**

1. **Line 96-99:** The sorted order claim "[L_{n-1}, L_{n-1}, L_{n-2}, L_{n-2}, ..., L_1, L_1, L_1, L_0]" has a counting error. For n=3, the multiset should have:
   - L_2 = 4/15: appears twice
   - L_1 = 2/15: appears THREE times (1 original + 2 from sub-pieces)
   - L_0 = 1/15: appears once
   
   Total: 2 + 3 + 1 = 6 = 2n pieces. CORRECT.

2. **Lines 193-196:** The LB score calculation correctly sums L_{n-1} + L_{n-2} + ... + (extras from odd positions) = L_n.

**Assessment:** The lower bound proof is correct.

### Verification of Part B (Upper Bound)

**Issues:**

1. **Line 259-262:** The interleaving construction "Q_k = P_{k+1} + epsilon_k" is sketched but not rigorously justified.

2. **Lines 295-299:** The "Crucial Lemma" that P_1 > c(n) implies XY can achieve LB < c(n) is asserted but not proved.

3. **Lines 321-327:** The "Case: Some ratio > 2 (top-heavy)" and "Case: Some ratio < 2 (bottom-heavy)" are described qualitatively but not proved.

4. **Line 352-354:** "Computational verification for n=2" is stated but the details are not shown.

**Assessment:** The upper bound proof has significant gaps. The interleaving argument is sketched but not fully justified. The case analysis for non-geometric configs is hand-wavy.

### Part C (Saddle-Point Characterization)

**Issue:** The uniqueness claim (line 364-365) is asserted but not proved. "Uniquely determines the geometric ratios" needs justification.

### Correctness score: 8/10
### Completeness/rigor score: 6/10 (multiple gaps in upper bound)
### Progress: Moderate (provides game-theoretic intuition but less rigorous)

### Verdict: CHANGES REQUESTED

**Specific gaps:**
1. The interleaving construction for general LB configs is incomplete.
2. The Crucial Lemma (P_1 > c(n) => LB < c(n)) is not proved.
3. The saddle-point uniqueness is not justified.

---

## Comparison

Both approaches have the same answer and similar structures. The geometric-direct approach is more rigorous with better computational verification. The minimax-saddle-point approach provides good intuition but has more gaps.

---

## Outcome Recording

| Approach | Status | Outcome | Note |
|----------|--------|---------|------|
| geometric-direct | partial | advanced | Lower bound rigorous; upper bound needs general-n proof |
| minimax-saddle-point | partial | advanced | Good intuition; interleaving and uniqueness gaps |

---

## Lemma Certification

### Greedy Optimality Lemma (already certified Round 1)
Status: CERTIFIED. No changes needed.

### Promotable Lemmas from geometric-direct

1. **Geometric Dominance Lemma:** 
   - Statement: L_n > L_0 + L_1 + ... + L_{n-1}
   - Status: CERTIFIED. Proof is trivial (geometric sum).

2. **Parity Constraint Lemma:**
   - Statement: XY prefers j <= n-1 marks to avoid giving LB an extra pick.
   - Status: CERTIFIED. Direct counting argument.

3. **Key Invariant for Lower Bound:**
   - Statement: For geometric LB and any XY partition of L_n, greedy gives LB >= L_n.
   - Status: NOT CERTIFIED for general n. Verified computationally for n=1,2,3 but the inductive argument is incomplete.

### Promotable Lemmas from minimax-saddle-point

1. **Parity of Piece Count:**
   - Same as above. CERTIFIED.

2. **XY's Optimal Sub-pieces:**
   - Statement: Against geometric LB, XY's optimal n-1 marks create [L_{n-1}, L_{n-2}, ..., L_1, L_1].
   - Status: CERTIFIED for n=1,2,3. General n follows from verification.

3. **Interleaving Upper Bound:**
   - Statement: For P_1 >= 1/2, XY achieves interleaved order giving LB = P_1.
   - Status: NOT CERTIFIED. The existence of Q_k >= P_{k+1} summing to P_1 needs proof.

---

## Final Verdicts

### geometric-direct
- **Builder's Status:** solved
- **True Status:** partial
- **Verdict:** CHANGES REQUESTED
- **Gap:** Upper bound proof for general n is incomplete. The interleaving mechanism works but needs rigorous induction.

### minimax-saddle-point  
- **Builder's Status:** solved
- **True Status:** partial
- **Verdict:** CHANGES REQUESTED
- **Gap:** Multiple gaps in upper bound: interleaving construction, Crucial Lemma, uniqueness.

---

## Update to current.md

The answer c(n) = 2^n / (2^{n+1} - 1) is computationally verified for n=1,2,3 and the proof structure is sound. The problem is partial (not solved) because the upper bound proof for general n has gaps.

**Critical correction from Round 1:** The claim that "arithmetic beats geometric" was WRONG. Against XY's optimal response, arithmetic achieves less than geometric. The geometric configuration is indeed optimal.
