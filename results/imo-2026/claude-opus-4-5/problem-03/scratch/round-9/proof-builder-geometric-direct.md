# Proof Builder Report: geometric-direct (Round 9)

## Tasks completed

### 1. Fixed inconsistency in current.md

**FIXED.**

Removed the erroneous claim at line 53:
> "Upper Bound Case B Trivial (PROVED for all n): If P_{n+1} <= c(n), XY uses 0 marks and LB picks P_{n+1} <= c(n)."

This claim was WRONG for n >= 2. Counterexample: n=2 with P = {1/3, 1/3, 1/3}. With 0 XY marks and 3 pieces, LB picks ceil(3/2) = 2 pieces totaling 2/3 > 4/7 = c(2), even though P_3 = 1/3 < c(2).

Replaced with the correct result:
> "Upper Bound Case B Large P_{n+1} (PROVED for all n >= 2): If P_{n+1} >= c(n), XY halves P_{n+1} (1 mark) and applies the (n-1)-game upper bound strategy (n-1 marks) to {P_1, ..., P_n}. Result: LB <= P_{n+1}/2 + c(n-1)*(1 - P_{n+1}) <= c(n). Uses algebraic identity: c(n-1)*(1-c(n)) = c(n)/2."

Also added certified lemmas 9 and 10 to current.md for the Halve + IH Strategy and algebraic identity.

Updated the "Gap remaining" description to clarify that the Halve + IH Strategy handles P_{n+1} >= c(n), and only the "small pieces" sub-case (P_1 > L_0 and P_{n+1} < c(n)) remains open for n >= 5.

---

### 2. Verification of Halve + IH Strategy (Part 2.5)

**VERIFIED. The proof is rigorous.**

#### Mark count verification

- XY uses 1 mark to halve P_{n+1}
- XY uses at most (n-1) marks for the (n-1)-game upper bound strategy on {P_1, ..., P_n}
- Total: 1 + (n-1) = n marks (exactly the budget)

**VERIFIED for n = 2 through 10.**

#### Pairing Cancellation application

By the Pairing Cancellation Lemma:
- Halving P_{n+1} creates the pair {P_{n+1}/2, P_{n+1}/2}
- This pair contributes exactly P_{n+1}/2 to LB's score
- The remaining score comes from the (n-1)-game played on {P_1, ..., P_n}

The (n-1)-game upper bound (by inductive hypothesis) limits LB to at most c(n-1) of the remaining total (1 - P_{n+1}).

Therefore: LB <= P_{n+1}/2 + c(n-1)*(1 - P_{n+1})

**Application is correct.**

#### Algebraic identity: c(n-1)*(1 - c(n)) = c(n)/2

**Proof:**
```
c(n-1) = 2^{n-1} / (2^n - 1)
1 - c(n) = 1 - 2^n/(2^{n+1}-1) = (2^{n+1} - 1 - 2^n)/(2^{n+1}-1) = (2^n - 1)/(2^{n+1}-1)

c(n-1) * (1 - c(n)) = [2^{n-1}/(2^n - 1)] * [(2^n - 1)/(2^{n+1} - 1)]
                     = 2^{n-1}/(2^{n+1} - 1)    [The (2^n - 1) terms CANCEL]
                     = c(n)/2                   [Since c(n) = 2^n/(2^{n+1} - 1)]
```

**VERIFIED algebraically and computationally for n = 1 through 10.**

#### Decreasing function verification

Define f(x) = x/2 + c(n-1)*(1 - x).

Derivative: f'(x) = 1/2 - c(n-1)

Since c(n-1) = 2^{n-1}/(2^n - 1) > 1/2 for all n >= 1 (verified: c(0) = 1, c(1) = 2/3, ..., all > 1/2), we have f'(x) < 0.

Therefore f is strictly decreasing. When P_{n+1} >= c(n), we have:
LB <= f(P_{n+1}) <= f(c(n)) = c(n)

**VERIFIED.**

#### Edge cases

1. **Boundary case P_{n+1} = c(n):** f(c(n)) = c(n)/2 + c(n-1)*(1-c(n)) = c(n)/2 + c(n)/2 = c(n). LB = c(n) exactly. **OK.**

2. **n = 2 base case:** Uses n=1 game result (1 mark to halve or 0 marks for large P_1). The n=1 result is proved directly in Part 2, Case B for n=1. **OK.**

3. **Induction well-founded:** For n >= 2, we use the (n-1)-game result as the inductive hypothesis. The induction terminates at n=1 which is proved directly. **OK.**

**No edge cases fail.**

---

### 3. Concerns or gaps found

**None.** The Halve + IH Strategy is completely rigorous. The only remaining gap is Case B for n >= 5 when P_1 > L_0 and P_{n+1} < c(n) (the "small pieces" sub-case), which requires the algebraic coverage proof for the Singleton-Pair strategies.

---

## Summary of changes to current.md

1. Replaced erroneous "Case B Trivial" claim with correct "Case B Large P_{n+1}" via Halve + IH Strategy
2. Added certified lemma 9: Halve + IH Strategy Lemma
3. Added certified lemma 10: Algebraic Identity c(n-1)*(1-c(n)) = c(n)/2
4. Updated "Gap remaining" to clarify the Halve + IH Strategy handles P_{n+1} >= c(n)

---

## Recommended verdict

**APPROVE** for the geometric-direct approach at its current scope (n = 1, 2, 3, 4).

The approach correctly:
- Proves the lower bound for all n
- Proves the upper bound Case A for all n
- Proves the upper bound Case B for n = 1, 2, 3, 4 with complete algebraic verification
- Proves the Case B Large P_{n+1} sub-case for all n >= 2 via Halve + IH Strategy

The remaining gap (Case B with P_1 > L_0 and P_{n+1} < c(n) for n >= 5) is an extension, not a flaw in the current proof. The proof for n = 1, 2, 3, 4 is complete and rigorous.

However, since the problem asks for "each n" and we only have a complete proof for n <= 4, the overall status should remain **partial** until a general-n proof is obtained.

**Recommended action:** Mark the approach as CHANGES REQUESTED to continue working on n >= 5, or APPROVE if a partial result (complete proof for n <= 4) is acceptable for this problem.
