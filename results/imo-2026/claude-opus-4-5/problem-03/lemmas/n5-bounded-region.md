# Bounded "All Pairwise > 1" Region for n=5

## Statement

For n=5 with shifted parameters alpha, beta, gamma, delta, epsilon, zeta (where alpha = P_1/L_0 - 1, beta = d_1/L_0 - 1, etc.) satisfying:

1. Weighted sum: 6*alpha + 5*beta + 4*gamma + 3*delta + 2*epsilon + zeta = 42
2. All params > 0 (i.e., P_1 > L_0 and all d_j > L_0)
3. All 15 pairwise differences > 1

Then the configuration lies in a bounded region with:
- Common gap g in (1, 6/5) where g is the minimum spacing between consecutive sorted params
- Minimum parameter v_0 in (0, 1/3) where v_0 is the smallest sorted param value

## Proof

Let v_0 < v_1 < ... < v_5 be the 6 shifted params sorted in increasing order. Since all pairwise differences exceed 1, consecutive differences exceed 1: v_k >= v_0 + k*g for some gap g > 1.

**Minimum weighted sum bound (Rearrangement Inequality):**

The weighted sum 6*x_alpha + 5*x_beta + 4*x_gamma + 3*x_delta + 2*x_epsilon + x_zeta depends on how the sorted values v_0,...,v_5 are assigned to the parameters.

By the Rearrangement Inequality, the minimum weighted sum (over all assignment permutations) is achieved when the largest weight (6) is assigned to the smallest value (v_0), the second-largest weight (5) to the second-smallest value (v_0 + g), etc.

Min WS = 6*v_0 + 5*(v_0+g) + 4*(v_0+2g) + 3*(v_0+3g) + 2*(v_0+4g) + 1*(v_0+5g)
       = (6+5+4+3+2+1)*v_0 + (5*1 + 4*2 + 3*3 + 2*4 + 1*5)*g
       = 21*v_0 + (5 + 8 + 9 + 8 + 5)*g
       = 21*v_0 + 35*g

**Deriving the bounds:**

Since the actual weighted sum equals 42:

21*v_0 + 35*g <= 42

With g > 1: 21*v_0 < 42 - 35 = 7, so v_0 < 7/21 = 1/3.

With v_0 > 0 (from condition 2): 35*g < 42, so g < 42/35 = 6/5 = 1.2.

Therefore: g in (1, 1.2) and v_0 in (0, 1/3). QED.

## Computational Verification

At the g=1 boundary, there are exactly 63 permutation vertices (configurations where v_k = v_0 + k for all k). These correspond to weighted rank sums (wrs) in {35, 36, ..., 41}:

- wrs=35: 1 vertex, v_0 = 7/21 = 1/3
- wrs=36: 5 vertices, v_0 = 6/21 = 2/7
- wrs=37: 6 vertices, v_0 = 5/21
- wrs=38: 9 vertices, v_0 = 4/21
- wrs=39: 16 vertices, v_0 = 3/21 = 1/7
- wrs=40: 12 vertices, v_0 = 2/21
- wrs=41: 14 vertices, v_0 = 1/21

Total: 1+5+6+9+16+12+14 = 63 vertices.

## Certified

Round 12, proof-reviewer.
