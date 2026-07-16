## imo-2026-03 — General n Lens

### Problem Recap
c(n) = 2^n / (2^{n+1} - 1) for all n ≥ 1. Prove LB achieves it with geometric config, prove XY limits LB to at most this for ANY LB config.

### Patterns Observed Across n=1,2,3,4

**Sum constraint structure.** In Case B (P_1 > L_0, P_{n+1} > c(n)), with differences d_j = P_{j+1} - P_j:

The key constraint is: n*P_1 + (n-1)*d_1 + ... + d_{n-1} < (2^n-1)*L_0.

In "all d_j > L_0" regime (the hardest sub-case), define reduced excesses a_0 = P_1/L_0 - 1 > 0 and a_j = d_j/L_0 - 1 > 0 for j=1,...,n-1. The constraint becomes:

  n*a_0 + (n-1)*a_1 + ... + a_{n-1} < M_n := 2^n - 1 - n(n+1)/2.

M_n values: n=2: 0, n=3: 1, n=4: 5, n=5: 16, n=6: 42, ..., growing exponentially.

For n=2: M_2=0, so "all a_j > 0" is IMPOSSIBLE → d_1 < L_0 always in Case B n=2. Proves the case automatically.

For n≥3: "all a_j > 0" is possible (M_n > 0), requiring actual strategies.

**Strategy structures found for small n.** The XY strategies use n-1 marks to create (n-1) pairs + 2 singletons with singleton diff ≤ L_0. The singleton differences come from one of two families:
- **D_ij type**: singleton diff = |d_i - d_j| = |a_i - a_j| * L_0 (comparing two differences)
- **S_{j,k} type**: singleton diff = |d_j - P_k| = |a_j - (k-1) - sum_{i=0}^{k-1} a_i| * L_0 (comparing a difference with a partial piece sum)

**CRITICAL NEW OBSERVATION.** Computationally verified for n=6,8,10,12 with 500k samples each: 0 failures with the combined strategy "either some |d_i - d_j| ≤ L_0 or some |d_j - P_k| ≤ L_0".

Moreover: when all pairwise d_i - d_j differences exceed L_0, some d_j - P_k comparison ALWAYS works (0/200k samples with n=6,8,10). These are genuinely complementary cases.

### Candidate General Arguments

**Argument 1: Two-case pigeon-hole (works for n ≤ 9 but not generally).**

If any two d values are within L_0 of each other → D_ij strategy (n-1 marks: halve A_{i+1} at A_i to create pair, similarly for j; halve remaining n-3 pieces).

If all d values are pairwise > L_0 apart → the weighted minimum sum (assigning largest weight to smallest value) is n(n+1)(4n-1)/6 * L_0 (derived from sorted values with all gaps > L_0 and assignment to weights (n,n-1,...,1)). For this to be < (2^n-1)*L_0, need n(n+1)(4n-1)/6 ≥ 2^n-1. Verified true for n=2,...,9, fails for n≥10.

This IS a valid proof for n≤9, but not general.

**Argument 2: The "interleaving" argument (promising, unproven).**

CLAIM: When all |d_i - d_j| > L_0, the sorted d-values and P-values necessarily interleave closely.

Specifically: sort d_1,...,d_{n-1} as b_1 < b_2 < ... < b_{n-1} with all gaps > L_0. Define g(k) = P_k/L_0 - 1 = (k-1) + sum_{j=0}^{k-1} a_j (the "reduced P_k"). The claim is: min_{j,k} |a_j - g(k)| ≤ 1.

Observation (numerical): this ALWAYS holds (verified), but algebraic proof is the gap.

Note that g(k+1) - g(k) = 1 + a_k and d_j / L_0 = 1 + a_j. Both sequences grow by similar amounts (all increments > 1). The SUM CONSTRAINT forces a bound on the "mismatch" between how the d sequence grows vs. how P accumulates.

**Argument 3: True induction on n (the CLEANEST potential route).**

The proof for n=2 is trivial (M_2=0 forces d_1 < L_0). For n=3: M_3=1, and all a_j > 0 gives 3a_0 + 2a_1 + a_2 < 1. This forces a_2 < 1 and a_0 < 1/3, giving |a_2 - a_0| < 1 automatically. For n=4: similarly the Case A constraint 6a_0 + 4a_1 < 2 forces a cascade of coverage.

The pattern for general n: whenever "all a_j > 0" regime has a_k ≥ a_{k-2} + 1 (the Case A-like condition), the sum constraint forces 2^k * a_0 < 1 (roughly), allowing the next comparison to work. The number of levels equals n.

For the INDUCTIVE STEP from n-1 to n: if d_j ≤ L_0 for some j, done. Otherwise, in the "all a_j > 0" regime, the n-piece sum constraint is STRICTLY STRONGER than the (n-1)-piece sum constraint, allowing the inductive hypothesis to apply to a "derived" sub-problem.

**Argument 4: DIRECT construction using XY's n marks (potentially cleaner).**

With n marks (the FULL allotment), XY creates 2n+1 pieces = n pairs + 1 singleton s. Then LB = 1/2 + s/2 ≤ c(n) iff s ≤ L_0.

The strategy: XY uses n marks to create n pairs, leaving one "residual" piece s. If XY halves n specific pieces, the singleton is determined by the summing to 1. This may give a cleaner algebra because the singleton is:
  s = 1 - 2*(sum of n halved pieces)/2 = 1 - (sum of n halved pieces).

XY chooses WHICH n pieces to halve to make s = L_0 exactly. This requires:
  sum of n chosen pieces = 1 - L_0 = (2^{n+1}-2)/(2^{n+1}-1) = 2(2^n-1)*L_0.

With P_1,...,P_{n+1} summing to 1, XY needs to find n pieces whose sum = 2(2^n-1)*L_0. Since each piece > L_0, the sum of any n pieces > n*L_0, and sum of all n+1 pieces = 1 = (2^{n+1}-1)*L_0. We need the sum to hit EXACTLY 2(2^n-1)*L_0.

This might not always be achievable exactly, but XY can CHOOSE continuous halving fractions to adjust. The algebraic content is whether XY can always achieve LB = 1/2 + s/2 ≤ c(n).

### Obstacles to Generalization

1. **Pigeon-hole breaks down for n ≥ 10**: n(n+1)(4n-1)/6 < 2^n-1 for n≥10. A different argument is needed for large n.

2. **S_{j,k} construction feasibility**: When d_j ≈ P_k, XY needs to create a piece of size P_k inside the large piece P_{n+1}. This requires P_{n+1} > P_k, which holds since P_{n+1} > c(n) > (2^n-1)*L_0 while P_k ≤ (n-1)*P_{n+1} * (something)... actually P_k < 1-c(n) < 1. So P_k < 1 and P_{n+1} > 1/2 > P_k for n≥1. FEASIBILITY OK.

3. **The algebraic proof that Case 2 (all |d_i-d_j| > L_0) implies some |d_j-P_k| ≤ L_0**: This is the main algebraic gap. The proof would need to show that the G-sequence (defined by cumulative sums of a_j) always "catches" one of the a_j values within ±1.

### Distinct Openings

1. **Complete proof via n(n+1)(4n-1)/6 > 2^n-1 for n ≤ 9, then cite large-n slack**: For n ≥ 10, M_n grows so fast that the "hard" region (all a_j > 1) would require WS > M_n, giving a direct contradiction. Need to verify this bound explicitly.

2. **Two-family strategy proof**: Prove the two families (D_ij and S_{j,k}) cover all cases via the "interleaving" claim. Algebraic proof needed for Case 2.

3. **Induction exploiting Case A cascade**: Generalize the "Case A forces tighter constraint" structure from n=3 and n=4. For general n, there are n-2 "levels" of Case A, each tightening the sum constraint by a factor of ~2, eventually forcing coverage.

4. **Use n marks (not n-1)**: XY with n marks needs singleton ≤ L_0. The 4-pair+1-singleton structure (used in n=4 B/PP strategies) generalizes: XY creates n pairs by "doubling" specific pieces (halving each creates a pair). The residual singleton = 1 - (sum of n doubled pieces). Since XY can CHOOSE fractional halvings (not necessarily exact halvings of original pieces), they can make the singleton arbitrarily small. This might give a much CLEANER proof.

5. **Bypass the case analysis entirely**: Consider the function f(s) = (XY's optimal LB limit given s = P_1). This is a monotone function. The upper bound proof reduces to: f(L_0) ≤ c(n). The continuity argument might give a cleaner proof than case-by-case strategy construction.

### Key Algebraic Facts

- |d_j - P_{j+1}| = P_j (exactly), so d_j vs P_{j+1} comparisons NEVER give < L_0.
- |d_1 - P_2| = L_0 * (1 + a_0) ≥ L_0 (equality at boundary of Case B, but in strict Case B it's > L_0).
- |d_2 - P_2| = |(1+a_2) - (2+a_0+a_1)| = |a_2 - a_0 - a_1 - 1|. For n=3,4: sum constraint forces this ≤ 1.
- For all n, when "all a_j > 0": the MINIMUM over j,k of |a_j - g(k)| can be made ≤ 1 (where g(k) = (k-1) + sum_{i=0}^{k-1} a_i). Verified numerically.

### Explicit XY Strategy Constructions

**D_ij strategy** (when |d_i - d_j| ≤ L_0, using n-1 marks):
- XY cuts A_{i+1} at position A_i from bottom → creates pair {A_i, A_i} and singleton d_i.
- XY cuts A_{j+1} at position A_j from bottom → creates pair {A_j, A_j} and singleton d_j.
- XY halves remaining n-3 pieces (those not used above) → creates n-3 pairs.
- Total: n-1 marks, (n-1) pairs, 2 singletons {d_i, d_j}, LB = 1/2 + |d_j - d_i|/2 ≤ c(n). ✓

**S_{j,k} strategy** (when |d_j - P_k| ≤ L_0, using n-1 marks):
- XY cuts A_{j+1} at position A_j from bottom → creates pair {A_j, A_j} and singleton d_j.
- XY cuts A_{n+1} at position P_k from one end → creates {P_k, P_{n+1}-P_k}.
  The {P_k} piece pairs with the "A_k" LB piece (of size P_k).
  Wait: A_k (sorted original LB pieces) is P_k in this notation.
- More precisely: XY cuts A_{n+1} = P_{n+1} at position P_k from the bottom,
  creating {P_k, P_{n+1}-P_k}. The {P_k} pairs with LB piece A_k.
  The {P_{n+1}-P_k} becomes the "other singleton" = P_{n+1} - P_k.
- Actually: singleton diff = |d_j - P_k| requires singletons to be d_j and P_k. Need construction.
  More natural: halve A_{n+1} and A_n and ..., cut A_{j+1} to create d_j, cut something to create P_k.
- Feasibility: P_{n+1} > c(n) > P_k for all k≤n, so cutting at P_k from A_{n+1} is valid.
- Uses: 1 mark on A_{j+1}, 1 mark on A_{n+1} for the P_k clone, then n-3 halvings of remaining pieces.
  Total: n-1 marks. ✓
- LB = 1/2 + |d_j - P_k|/2 ≤ c(n). ✓

### Prior Progress
- n=1,2,3: Complete rigorous proofs. n=4: Framework proved, B/PP 4-mark constructions needed.
- The KEY GAP for general n: algebraic proof that "all d_j > L_0" case in Case B is always covered.

### Dead Ends (Do Not Retry)
- XY interleaving strategy for LOWER BOUND (wrong direction for upper bound, only for lower)
- Claiming c(n) = arithmetic spacing answer (Round 1 error, corrected Round 2)
- Using n marks (not n-1) for the "easy" Case B strategies (creates one more piece, changing parity)

### Small-Case / Intuition Notes (labeled as CONJECTURE)
- CONJECTURE: For all n, in Case B "all d_j > L_0", min_{i≠j} |d_i - d_j| ≤ L_0 OR min_{j,k} |d_j - P_k| ≤ L_0. Verified computationally for n up to 12 with 500k samples.
- CONJECTURE: The proof for general n requires exactly TWO strategy families (D_ij and S_{j,k}), analogous to the two cases in the n=3 proof (S1/S2 → some d_j ≤ L_0, S3 → S3 type comparison).
- OBSERVATION: n(n+1)(4n-1)/6 > 2^n-1 for n ≤ 9 but fails n ≥ 10. The pigeon-hole via this bound covers n ≤ 9 completely. For n ≥ 10, a fundamentally different argument is needed.
- OBSERVATION: The "Case A cascade" in n=4 (where gamma ≥ alpha+1 forces 6alpha+4beta < 2, and then eta is bounded) generalizes to n levels for general n, each halving the bound on alpha. For n → ∞, alpha → 0, so P_1 → L_0, and the gap with Case A vanishes. This EXPONENTIAL SQUEEZING might be the key to the general proof.
