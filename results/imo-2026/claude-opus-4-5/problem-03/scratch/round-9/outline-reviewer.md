# Outline Review — Round 9

## Approach reviewed: geometric-direct (advance)

### Change 1: "Case B Trivial" claim removed

**VERIFIED.**

The claim "If P_{n+1} <= c(n), XY uses 0 marks and LB picks P_{n+1}" was correctly identified as WRONG for n >= 2. With 0 XY marks and n+1 pieces, LB picks ceil((n+1)/2) pieces, not just the largest.

Counterexample verified: n=2 with P = {1/3, 1/3, 1/3}. LB picks 2 pieces totaling 2/3 > 4/7 = c(2), even though P_3 = 1/3 < c(2).

The approach file has properly marked this with strikethrough: `~~Case B Trivial: P_{n+1} <= c(n)~~ [REMOVED]` and replaced it with a note explaining the error.

**ISSUE FOUND in current.md:** The file `results/imo-2026-03/current.md` still contains the erroneous claim at line 53:
> 3. **Upper Bound Case B Trivial (PROVED for all n):** If P_{n+1} <= c(n), XY uses 0 marks and LB picks P_{n+1} <= c(n).

This is inconsistent with the corrected approach file. The builder should fix current.md to remove this claim.

---

### Change 2: Halve + IH Strategy (Part 2.5)

**VERIFIED.**

The new lemma claims: For n >= 2 with P_{n+1} >= c(n), XY halves P_{n+1} (1 mark) and applies the (n-1)-game upper bound (n-1 marks), giving:
  LB <= P_{n+1}/2 + c(n-1)*(1 - P_{n+1})

**Algebraic identity verified:**
```
c(n-1)*(1 - c(n)) = c(n)/2

Proof:
  c(n-1) = 2^{n-1}/(2^n - 1)
  1 - c(n) = (2^n - 1)/(2^{n+1} - 1)
  Product = 2^{n-1}/(2^{n+1} - 1) = c(n)/2
```

Computationally verified for n = 1 through 9.

**Decreasing function verified:**
f(x) = x/2 + c(n-1)*(1-x) has derivative f'(x) = 1/2 - c(n-1) < 0 for all n >= 1 (since c(n-1) > 1/2).

**Conclusion:** f(P_{n+1}) <= f(c(n)) = c(n) when P_{n+1} >= c(n). The proof is rigorous.

**Mark count verified:** 1 mark to halve P_{n+1}, plus (n-1) marks for the (n-1)-game strategy on {P_1, ..., P_n}. Total = n marks, within budget.

---

### Change 3: n=5 strategies (Part 2.6)

**VERIFIED as OPEN.**

The approach correctly marks n=5 as "IDENTIFIED, COMPUTATIONALLY VERIFIED" with "algebraic proof OPEN". The 11 strategies are listed with their working conditions, and the gap (proving the sum constraint prevents all 11 conditions from failing simultaneously) is explicitly stated.

No overclaiming detected.

---

### Change 4: Promotable lemmas updated

**VERIFIED.**

Two new lemmas correctly added:
- Halve + IH Strategy (with proof in Part 2.5)
- c(n-1)*(1-c(n)) = c(n)/2 Identity (with algebraic proof)

---

## Verdict: CHANGES REQUESTED

The technique is sound and the mathematical changes are correct. One fixable issue:

1. **current.md inconsistency:** Line 53 still claims "Case B Trivial (PROVED for all n)" which contradicts the corrected approach file. The builder should remove this claim and replace it with a reference to the Halve + IH Strategy.

---

## Ranking update

The only live approach is geometric-direct. No comparisons needed (fewer than 2 comparable approaches are active).

**Approaches in population:**
- geometric-direct: Elo 1702, last_outcome=advanced, status=advancing
- induction-on-n: Elo 1420, dead-end
- minimax-saddle-point: Elo 1521, not built
- minimax-value: Elo 1460, not built
- piece-count-parity: Elo 1418, not built

No ranking update required.

---

## Build set

build set: geometric-direct

Tasks for builder:
1. Fix the inconsistency in current.md (remove the erroneous "Case B Trivial" claim).
2. Verify the Halve + IH Strategy proof (Part 2.5) for any edge cases.
3. Optionally: Attempt the n=5 algebraic casework.
