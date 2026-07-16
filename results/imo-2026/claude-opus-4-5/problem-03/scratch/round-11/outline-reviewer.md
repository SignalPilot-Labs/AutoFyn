# Outline Review: Round 11

## Reviewed Approaches

### 1. geometric-direct (revise)

**Summary:** Extends n=4 proof with V_j strategies for d_j <= L_0 cases, plus Pigeonhole argument for "all d_j > L_0" sub-case.

**Verification of the Pigeonhole Claim:**

The outliner claims that in B_small with all d_j > L_0 (equivalently, all 5 shifted params alpha, beta, gamma, eta, sigma > 0), if all pairwise differences > 1, then the weighted sum exceeds the constraint value.

I verified this algebraically:

1. **The constraint:** 5alpha + 4beta + 3gamma + 2eta + sigma = 16 (derived from sum of pieces = 1).

2. **Minimum weighted sum with all pairwise > 1:** If 5 values all have pairwise differences > 1, after sorting they form x, x+g, x+2g, x+3g, x+4g with g > 1 and x >= 0. The minimum weighted sum (assigning largest weight 5 to smallest value) is:
   ```
   5(x) + 4(x+g) + 3(x+2g) + 2(x+3g) + 1(x+4g) = 15x + 20g
   ```
   With g > 1 and x >= 0: **15x + 20g > 20 > 16**.

3. **Conclusion:** Since the actual weighted sum = 16 < 20, "all pairwise > 1" is IMPOSSIBLE. Therefore, some pairwise difference must be <= 1.

**Verification of 10 Pairwise Strategies:**

I verified that all C(5,2) = 10 pairs have valid 3-mark constructions. For each pair (param_i, param_j), when |param_i - param_j| <= 1, XY can create singletons with difference <= L_0. Example constructions:

- (alpha, gamma): Cut P_3 at P_2 (creates {P_2, d_2}), halve P_4, P_5. Pairs = {P_2, P_2}, {P_4/2}, {P_5/2}. Singletons = {P_1, d_2}.
- (beta, eta): Cut P_2 at P_1, cut P_4 at P_3, halve P_5. Pairs = {P_1, P_1}, {P_3, P_3}, {P_5/2}. Singletons = {d_1, d_3}.

All 10 pairs work similarly.

**V_j Strategies:** Already verified in prior rounds (explorer report confirms).

**Verdict: APPROVE**

The technique is sound:
- V_j strategies cover any d_j <= L_0 (j = 1,2,3,4).
- Pigeonhole guarantees some pairwise <= 1 when all d_j > L_0.
- Each of the 10 pairs has a valid 3-mark construction.

The n=4 proof is now COMPLETE in structure. Builder should formalize all 10 pairwise constructions explicitly.

---

### 2. n5-five-mark (new)

**Summary:** Proves c(5) = 32/63 via V_j + 15 Pairwise + 3 five-mark strategies (A, E, F) for bounded "all pairwise > 1" sub-region.

**Verification that Pigeonhole FAILS for n=5:**

For n=5, the weighted sum constraint is 6alpha + 5beta + 4gamma + 3delta + 2epsilon + zeta = 42.

Minimum weighted sum with all pairwise > 1:
```
6(x) + 5(x+g) + 4(x+2g) + 3(x+3g) + 2(x+4g) + 1(x+5g) = 21x + 35g
```

With g > 1 and x >= 0: min > 35. But **42 > 35**, so "all pairwise > 1" IS achievable.

Explicit example: g = 1.1, x = 2 - 5*1.1/3 = 0.167
- Params: alpha=0.167, beta=1.267, gamma=2.367, delta=3.467, epsilon=4.567, zeta=5.667
- Weighted sum: 42 (verified)
- Min pairwise diff: 1.1 > 1 (verified)
- Feasible region: g in (1, 1.2), a BOUNDED strip.

**Key Lemma Verification:**

The outliner correctly identifies:
- Pigeonhole fails for n=5.
- The "all pairwise > 1" sub-region is bounded (g in (1, 1.2), x in (0, 1/3)).
- Additional strategies (A, E, F) needed for this bounded region.

**Open Gap:** The three-strategy sub-claim ("at least one of A, E, F works") is stated but NOT proved. The mechanism is "by case analysis or LP verification" which is underspecified.

**Verdict: CHANGES REQUESTED**

The technique is right but there's a fixable gap:
1. **Missing:** Algebraic proof or explicit case analysis showing that in the bounded region, at least one of {A, E, F} has condition <= 1.
2. **Requested:** The builder should either:
   - Provide an explicit algebraic argument (e.g., sum of condition bounds contradicts constraint), OR
   - Verify via LP that the polytope {all 3 conditions > 1} intersected with the bounded region is empty.

The 0.55% computational failure rate mentioned in the explorer report is from n=4, not n=5. For n=5, the explorer claims 100% coverage with V_j + Pairwise + A/E/F, but this needs rigorous proof.

---

### 3. geometric-direct-advance (advance)

**Summary:** Extends V_j + Pigeonhole to general n.

**Analysis:**

The approach conjectures that Pigeonhole extends to all n. This is FALSE for n >= 5, as I verified above:
- n=4: Weighted sum = 16, min with all pairwise > 1 is > 20. Pigeonhole works.
- n=5: Weighted sum = 42, min with all pairwise > 1 is > 35. Since 42 > 35, Pigeonhole FAILS.

For general n, the weighted sum is n(n+1)(n+2)/6 (need to verify this formula). The minimum with all pairwise > 1 for (n+1) params is (n+1)*(n+2)/2 * x + (sum of weights * gaps) which grows differently.

**Verdict: RETHINK**

The approach is based on extending Pigeonhole to n >= 5, but Pigeonhole provably fails for n >= 5. The outliner should either:
- Accept that n=5+ requires explicit strategy enumeration (not just Pigeonhole), OR
- Find a different technique that generalizes.

---

### 4. direct-counting (new)

**Summary:** Proves c(n) via LP feasibility / polytope emptiness argument.

**Analysis:**

This is actually a more general framing of the Pigeonhole idea. The approach proposes proving that the polytope {all > 0, weighted = W, all pairwise > 1, unweighted < U} is infeasible.

For n=4 (W=16), this is correct. For n=5 (W=42), I showed the polytope is NON-empty (bounded but non-empty).

The "Diameter Bound" lemma is essentially the Pigeonhole argument restated. The LP infeasibility claim is correct for n=4 but FALSE for n=5.

**Verdict: RETHINK**

The LP approach is correct for n <= 4 but does not extend to n >= 5 as stated. The polytope is non-empty for n=5. The approach needs to be reformulated: for n >= 5, show that additional strategy conditions (A, E, F) cover the non-empty polytope.

---

## Ranking Update

Current population:
- geometric-direct (Elo 1700, partial, selected 1, last round 10)
- induction-on-n (Elo 1403, dead-end)
- minimax-saddle-point (Elo 1513, never built)
- minimax-value (Elo 1455, never built)
- piece-count-parity (Elo 1413, never built)
- vertical-pairing (Elo 1505, never built, merged into geometric-direct)

New approaches this round:
- n5-five-mark: new, distinct from geometric-direct (different technique for n=5)
- geometric-direct-advance: RETHINK (not registering)
- direct-counting: RETHINK (not registering)

**Comparisons:**

1. geometric-direct (revised) vs geometric-direct (round 10): Winner geometric-direct (revised) - the n=4 Pigeonhole argument is now verified to close the gap.

2. n5-five-mark vs geometric-direct: Draw - different targets (n5-five-mark focuses on n=5, geometric-direct covers n<=4 rigorously). Both are viable paths forward.

3. geometric-direct vs minimax-saddle-point: Winner geometric-direct - has proven results for n<=4, while minimax-saddle-point has only framework and was never built.

---

## Registration

**Register:** n5-five-mark (new approach with distinct technique for n=5)

---

## Build Set

Given the verdicts:
- **geometric-direct (revise):** APPROVE - Build to formalize the n=4 Pigeonhole proof with all 10 pairwise constructions.
- **n5-five-mark (new):** CHANGES REQUESTED - Build to close the three-strategy sub-claim gap.

Both should be built in parallel.

---

**build set: geometric-direct, n5-five-mark**
