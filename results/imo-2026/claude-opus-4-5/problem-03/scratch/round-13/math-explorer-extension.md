## imo-2026-03 — Extension to n≥6 and Induction Structure

### 1. n=6 Pigeonhole Analysis

**Parameters for n=6:** 7 pieces, 7 shifted params (alpha, d1,...,d6), weights (7,6,5,4,3,2,1).

- **Weighted sum constraint:** 7*alpha + 6*beta + 5*gamma + 4*delta + 3*epsilon + 2*zeta + xi = 99  
  (where D = 2^7 - 1 = 127, and 99 = 127 - (7*8)/2 = 127 - 28)
- **Minimum weighted sum when all pairwise > 1:** Sort params as v_0 < v_1 < ... < v_6 with gaps > 1. By Rearrangement Inequality (assign largest weight to smallest value): Min WS = 28*v_0 + 56*g (where sum_k = C(8,2) = 28, sum_kg = 6*7*8/6 = 56).
- **Pigeonhole for n=6 FAILS:** Min WS at g=1, v_0=0 is 56 < 99. So the 'all pairwise > 1' region is non-empty. Pigeonhole works only if Min WS > WS_constraint, i.e., n(n+1)(n+2)/6 > D - (n+1)(n+2)/2. Equivalently: C(n+3,3) = (n+1)(n+2)(n+3)/6 > 2^{n+1}-1.

### 2. Pigeonhole Threshold — n* = 4

The Pigeonhole strategy (used for n=4) works exactly for n ≤ 4:

| n | C(n+3,3) | 2^{n+1}-1 | Pigeonhole works? |
|---|----------|-----------|-------------------|
| 1 | 4        | 3         | YES               |
| 2 | 10       | 7         | YES               |
| 3 | 20       | 15        | YES               |
| 4 | 35       | 31        | YES               |
| 5 | 56       | 63        | NO (56 < 63)      |
| 6 | 84       | 127       | NO                |
| 7 | 120      | 255       | NO                |

The threshold is n* = 4: for n ≥ 5, a bounded non-empty 'all pairwise > 1' region exists.

### 3. Bounded Region Growth (n ≥ 5)

For the 'all pairwise > 1' sub-region with WS constraint = D - (n+1)(n+2)/2:

| n | WS_constraint | g_max | v0_max |
|---|--------------|-------|--------|
| 5 | 42           | 1.20  | 0.33   |
| 6 | 99           | 1.77  | 1.54   |
| 7 | 219          | 2.61  | 3.75   |
| 8 | 466          | 3.88  | 7.69   |
| 9 | 968          | 5.87  | 14.60  |

**The bounded region grows EXPONENTIALLY with n.** For large n: g_max ~ 12·2^{n+1}/n^3 → ∞. For n=5, the region is compact (g < 1.2). For n ≥ 6, it is much larger. This exponential growth means n=5 is genuinely special in its compactness.

### 4. Higher-Tier Strategy for n=6 — No Simple Family

For the n=6 bounded region, computational search finds XY strategies that work, but no simple clean family analogous to n=5's (2,2,1):

| g    | v0     | Best LB   | Best distribution (marks on P1,...,P7) |
|------|--------|-----------|---------------------------------------|
| 1.05 | 1.496  | 0.501821  | (1,0,0,2,1,1,1)                       |
| 1.20 | 1.136  | 0.501040  | (1,0,0,2,1,1,1)                       |
| 1.35 | 0.796  | 0.501809  | (1,1,0,1,1,0,2)                       |
| 1.47 | 0.596  | 0.501176  | (1,1,0,1,0,2,1)                       |
| 1.50 | 0.536  | 0.500656  | (1,1,0,1,0,2,1)                       |
| 1.65 | 0.196  | 0.502517  | (0,0,1,0,2,2,1)                       |
| 1.74 | 0.016  | 0.501580  | (1,1,0,0,2,1,1)                       |

All verified ≤ c(6) = 64/127 ≈ 0.5039. But the distributions vary widely — different g values need different XY strategy structures. (These tests use monotone param assignment; the full argument needs all permutations too.)

**Mechanism insight for n=6:** The common pattern observed is: halve LARGE pieces (P6, P7) + apply 2 marks to an INTERMEDIATE piece + halve some SMALL pieces. This is reminiscent of n=5's (2,2,1) but with more halves and without a single universal family. The key algebraic observation at g=1.5: P1+P2+P3 ≈ P4 (numerically), so cutting P4 into {P1,P2,P3,epsilon} creates 3 near-pairs, and halving P5,P6,P7 creates 3 exact pairs. LB ≈ (P5+P6+P7)/2 + P1+P2+P3 ≈ 1/2.

### 5. Bounded Region Containment in B_small (Verified for n=6)

The B_small condition requires sum of shifted params < 2^n - (n+1) = 57 for n=6. In the all-pairwise > 1 region: sum params ≥ 7*v_0 + 21, and the WS constraint gives 28*v_0 ≤ 43, so v_0 ≤ 43/28. Maximum sum ≈ 7*(43/28) + 21 = 31.75 << 57. So the bounded region is entirely contained in B_small for n=6, same as n=5.

### 6. Induction Possibility

**Can the n=5 proof (V_j → Pairwise → (2,2,1)) generalize to all n via induction?**

- V_j strategies generalize trivially for all n (halve all except {Pj, Pj+1}).
- Pairwise strategies generalize for all n (check all C(n+1,2) pairs).
- Tier 3 strategies CANNOT be captured by a single algebraic family as n grows.

The n=5 proof relies crucially on the COMPACTNESS of the bounded region (g < 1.2, v_0 < 1/3 = 0.33). This allowed the 63-vertex finite check. For n=6, the bounded region is 5× larger in each dimension, and for n=7+, it grows without bound. A direct induction from n=5 would need to handle exponentially growing bounded regions.

**Alternative induction structure:** No clean inductive hypothesis is visible from this analysis. The current Case B_small proof for n=4 used Pigeonhole (an argument that breaks at n=5). The n=5 (2,2,1) proof uses finite enumeration at the boundary. For n≥6, neither approach scales.

### 7. Is n=5 the Representative Hard Case?

**No — n=5 is uniquely tractable.** 

- n=4: Pigeonhole closes the problem cleanly.
- n=5: Bounded region is compact (g < 1.2), admitting a finite vertex check.
- n=6+: Bounded region grows exponentially, no finite vertex check feasible.

n=5 is NOT representative of the general pattern; it is the LAST n where the current approach is feasible. For n ≥ 6, the proof requires fundamentally different techniques:
- LP duality or minimax theorem for implicit strategy characterization
- A stronger inductive hypothesis that sidesteps the bounded region analysis
- Or a different parameterization that makes the high-n case tractable

### Key Candidates for the Proof of n≥5 (General n)

1. **LP/Minimax approach:** XY's optimal response can be characterized as a solution to a linear program parameterized by the piece sizes. The optimal value 1/2 + LB_error is continuous in the pieces and equals c(n) at equality. This bypasses the need for explicit strategy families.

2. **Stronger inductive hypothesis:** Instead of "XY can limit LB to c(n)", prove a stronger statement about the structure of the optimal strategy that makes the induction work. Candidate: prove that XY's optimal strategy always involves a specific "hierarchical halving" structure.

3. **Convexity argument:** The LB function (after XY's optimal play) is concave in the pieces. The maximum of a concave function over a convex set is attained at the boundary. Show the boundary reduces to simpler cases. (Speculative — not yet verified.)

### Priority for Current Proof

The immediate gap is the n=5 (2,2,1) algebraic proof. The 63-vertex finite check is the most tractable path. The n≥6 case is a separate major open question that likely requires a different technique, NOT an extension of the n=5 strategy. The builder should focus on n=5; n≥6 is deferred.

### Dead Ends to Avoid

- Trying to extend (2,2,1) directly to n=6: no single strategy family works.
- Using Pigeonhole for n≥5: provably fails.
- Using Type 3 (2 cuts + 3 halves) for n=5: insufficient (~95% coverage, counterexample found).
- Trying to generalize the 63-vertex check to n≥6: bounded region grows exponentially.
