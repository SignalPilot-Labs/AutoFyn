# Approach: pairing-interleave

## Core idea
The geometric marking creates pieces whose sizes form a "dyadic hierarchy" - each piece is exactly twice the previous. XY's optimal response creates interleaved pairs: splitting piece P_k yields two copies of size P_{k-1}. In sorted order, copies and originals alternate, and LB claims one from each "tier" getting exactly c(n). The upper bound follows because ANY LB marking can be countered by XY creating similar interleaved structure.

## Target
Prove c(n) = 2^n / (2^{n+1} - 1) for all positive integers n.

## Outline

### Lower bound (LB's strategy achieves c(n))

1. **LB's geometric marking**: Pieces P_0 = t, P_1 = 2t, ..., P_n = 2^n t where t = 1/(2^{n+1} - 1).

2. **XY's optimal response (copy strategy)**: 
   - Mark midpoints of P_n, P_{n-1}, ..., P_2 (n-1 marks), creating two copies of P_{k-1} from each P_k.
   - Use 1 mark to create a near-copy of P_1 (epsilon above P_0).

3. **Resulting pieces**: Sorted as approximately {P_{n-1}, P_{n-1}, P_{n-2}, P_{n-2}, ..., P_1, P_1, P_1-eps, P_0, eps}.

4. **LB's take (odd positions)**: One P_{n-1} + one P_{n-2} + ... + one P_1 + (P_1-eps) + eps.
   Sum = P_{n-1} + P_{n-2} + ... + P_1 + P_1 = sum_{k=1}^{n-1} P_k + P_1.
   
5. **Gap: Verify this sum equals c(n)** - Check that sum_{k=1}^{n} 2^{k-1} t = (2^n - 1)t... wait, this seems wrong. Need to recompute.

6. **Claim: LB's sum >= c(n) for any XY response** - Need to prove that no XY strategy gives LB less than c(n).

### Upper bound (XY limits LB to c(n))

1. **For geometric LB marking**: XY's copy strategy achieves exactly c(n) (computed above).

2. **For arbitrary LB marking**: 
   - Let LB's pieces be a_1 <= a_2 <= ... <= a_{n+1}.
   - XY's strategy: Place all n marks inside the largest piece a_{n+1} to create "copies" of a_1, ..., a_n plus a remainder.

3. **Key insight**: The resulting 2n+1 pieces interleave so that XY captures the "originals" while LB captures the "copies" plus remainder. If copies approximate originals, LB gets approximately a_{n+1} (the piece XY split).

4. **Gap: General upper bound** - For any LB marking, show XY can limit LB to <= c(n). The geometric marking maximizes the "forced" value a_{n+1} = c(n).

### The dyadic hierarchy principle (from crux aimo-0117)

1. **Analogous crux move**: In dyadic/geometric sequences, the largest element strictly exceeds all others combined. This "dominance" ensures the first player captures at least half of the total minus a controlled remainder.

2. **Application**: LB's geometric marking maximizes P_n / (total) = 2^n / (2^{n+1} - 1) = c(n), which is exactly the guaranteed share.

## Gaps
- [ ] Gap 1: Verify LB's sum calculation in the copy strategy response
- [ ] Gap 2: Prove LB >= c(n) for ALL XY responses to geometric marking
- [ ] Gap 3: Upper bound for arbitrary LB marking

## Status
unsolved
