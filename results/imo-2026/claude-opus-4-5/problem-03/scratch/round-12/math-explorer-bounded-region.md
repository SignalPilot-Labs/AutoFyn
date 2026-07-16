## imo-2026-03 (n=5 All-Pairwise>1 Bounded Region)

### Tightest Algebraic Bounds (PROVED)

By rearrangement inequality: min WS over all permutations = 21*v0 + 35*g (assign largest weight to smallest value). Since this <= actual WS = 42:

- **g < 42/35 = 6/5 = 1.2** (tight: achieved as g->1 with v0->1/3)
- **v0 < 7/21 = 1/3** (tight: achieved as g->1 with monotone ordering)

### Crucial Structural Finding: All-Pairwise Implies B_small

**ALGEBRAICALLY PROVED**: The 5 params excl. zeta (weighted by 5,4,3,2,1) satisfy 5a+4b+3c+2d+e >= 15*v0 + 20*g > 20. So Sum of all 6 params = 42 - (5a+4b+3c+2d+e) < 22 < 26. Since B_small requires Sum < 26 (equivalent to P_6 < 28/63 < c(5)), the all-pairwise>1 region is ENTIRELY CONTAINED in B_small. No separate B_large/B_small split needed here.

### Ordering Constraints on Parameters (PROVED)

From impossibility of having v0 > 0 with certain rank assignments (min WS > 42):
- **zeta (weight 1) has rank >= 2**: Min WS with rank 0 is 50 > 42, with rank 1 is 45 > 42. So d_5 is NOT one of the 2 smallest among {P_1, d_1, d_2, d_3, d_4, d_5}.
- **epsilon (weight 2) has rank >= 1**: Min WS with rank 0 is 44 > 42. So d_4 is NOT the smallest.
- **alpha (weight 6) has rank <= 3**: If rank 4 or 5, min WS >= 45 > 42.
- **Smallest param is one of alpha, beta, gamma, delta** (= P_1, d_1, d_2, or d_3). This gives a 4-case decomposition.

### Extreme Vertices (at g=1 boundary)

63 of 720 permutations give valid all-pairwise=1 boundary configs (WS_const in {35,...,41}):
- **Vertex A** (WS_const=35, max v0=1/3): params = (1/3, 4/3, 7/3, 10/3, 13/3, 16/3), monotone increasing. Sum=17.
- **Vertex B** (WS_const=41, min v0=1/21): params = (1/21, 22/21, 64/21, 85/21, 106/21, 43/21). Sum≈15.3.
- v0 ranges from 1/21 to 1/3 across these 63 vertices.

### Key Reduction Opportunities

1. **4-case split by smallest param**: Since smallest is alpha/beta/gamma/delta, each sub-case has a specific XY strategy targeting the smallest piece or gap.
2. **Type 3 strategies (2 cuts + 3 halves)**: Computationally verified 100% coverage. The 63 extreme vertices define the "hard cases" any proof must handle.
3. **Forbidden orderings**: zeta and epsilon cannot be the smallest, which constrains XY strategy choices (e.g., strategies that pair based on zeta being large are always valid).

### Dead End

Halve+IH (n=4 IH on {P_1,...,P_5} + halve P_6): gives LB <= c(4)*(1-P_6) + P_6/2 which is INCREASING as P_6 decreases, so exceeds c(5) in B_small. Does NOT work.

### Candidate Techniques

- Rearrangement inequality to prove g and v0 bounds
- 4-case split on which of {alpha, beta, gamma, delta} is smallest; explicit Type 3 construction per case
- The 63 boundary vertices as a finite check set: prove each vertex has a Type 3 strategy, then use compactness/continuity
