# Proof Review: induction-on-n (Round 4)

## Approach: `induction-on-n`

### Verdict: APPROVE
### Status: solved
### Scores:
- **Correctness:** 10/10 (every step valid, independently verified)
- **Completeness/Rigor:** 10/10 (no gaps, all cases covered)
- **Progress:** 10/10 (completes the proof, sandwich case now resolved)

---

## Review Summary

The proof is **complete and correct**. Case B (sandwich case) has been properly closed with the "create-duplicate" strategy. I adversarially verified each step.

---

## Detailed Verification

### Step B1: p_{m+1} < 2p_m

**Claim:** From sandwich conditions, p_{m+1} < 2p_m.

**Verification:** 
- Sandwich conditions: p_m > 2^{m-1} S t_m (strict) and p_{m+1} <= 2^m S t_m
- Therefore: 2p_m > 2^m S t_m >= p_{m+1}
- Thus p_{m+1} < 2p_m. VALID.

### Step B2: XY cuts p_{m+1} at position p_m

**Verification:** The cut creates pieces (p_m, p_{m+1} - p_m). Since p_{m+1} < 2p_m, we have p_{m+1} - p_m < p_m. VALID.

### Step B3: Pair (p_m, p_m) at positions 1-2

**Claim:** The two copies of p_m are the largest pieces in the final sorted order.

**Verification:**
1. p_k < p_m for k < m (original sorted order)
2. p_{m+1} - p_m < p_m (from B1)
3. All pieces created by remaining m-1 marks are splits of pieces < p_m, hence < p_m

Therefore the two copies of p_m remain the largest. VALID.

### Step B4: P(m-1) applies to sub-problem

**Verification:** Sub-problem consists of m pieces {p_1, ..., p_{m-1}, p_{m+1} - p_m}. P(m-1) requires m pieces with m-1 marks. VALID.

### Step B5: Algebraic bound (S - 2p_m) t_{m-1} <= S t_m

**Independent derivation:**

Need: (S - 2p_m) t_{m-1} <= S t_m

Rearranging: p_m >= S (t_{m-1} - t_m) / (2 t_{m-1})

Computing the RHS:
- t_{m-1} = 1/(2^m - 1), t_m = 1/(2^{m+1} - 1)
- t_{m-1} - t_m = 2^m / [(2^m - 1)(2^{m+1} - 1)]
- (t_{m-1} - t_m) / (2 t_{m-1}) = 2^{m-1} / (2^{m+1} - 1) = 2^{m-1} t_m

So the required condition is p_m >= 2^{m-1} S t_m, which is exactly (with strict inequality) the sandwich condition. VALID.

**Numerical verification:** For m = 1,2,3,4,5, confirmed algebraically that (t_{m-1} - t_m)/(2 t_{m-1}) = 2^{m-1} t_m.

### Edge Cases

**Geometric boundary (all equalities):**
- At p_k = 2^{k-1} S t_m exactly, the cut creates p_{m+1} - p_m = p_m (three copies of p_m)
- The pair at positions 1-2 still cancels; third copy handled by sub-problem
- Bound becomes equality: (S - 2p_m) t_{m-1} = S t_m. VALID.

**m=2 (smallest induction):**
- After cut: 4 pieces, pair cancels
- Sub-problem has 2 pieces, apply P(1) with 1 mark
- Verified: (S - 2p_2)/3 < S/7 when p_2 > 2S/7 (sandwich condition). VALID.

### Parity Preservation

**Verification:** The pair occupies positions 1-2. Sub-problem pieces occupy positions 3, 4, 5, ... The shift by 2 preserves parity: odd -> odd, even -> even. Alternating sum contribution of sub-problem is preserved. VALID.

---

## Overall Proof Structure

1. **Base case P(1):** Complete, verified both cases (halve vs create-duplicate).
2. **Case A (k* < m+1, halve+recurse):** Complete from Round 3, ratio > 2 prevents interleaving.
3. **Case B (k* = m+1, sandwich):** NOW COMPLETE with create-duplicate strategy.
4. **Lower bound:** Complete from Round 1, geometric marking strategy.

---

## Final Answer Verification

c(n) = 2^n / (2^{n+1} - 1)

Equivalently: c(n) = 1 / (2 - 2^{-n})

Verified correct for n = 1, 2, 3, 4, 5 by explicit computation.

---

## Promotable Lemmas

The following lemmas are **certified for promotion** to `results/imo-2026-03/lemmas/`:

1. **Greedy Optimality Lemma:** Fully proved, statement correct.
2. **Pigeonhole Existence Lemma:** Fully proved, statement correct.
3. **k*-Largest Ratio Bound:** Fully proved, statement correct.
4. **Sub-Problem Size Bound:** Fully proved, statement correct.

---

## Conclusion

The proof is **complete and rigorous**. All gaps have been closed. The answer c(n) = 2^n / (2^{n+1} - 1) is proven correct.

**Verdict: APPROVE**
**Status: solved**
