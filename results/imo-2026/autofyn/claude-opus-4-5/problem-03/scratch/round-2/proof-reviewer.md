# Proof Review: induction-on-n (IMO 2026 P3)

## Approach Summary
The approach proves c(n) = 2^n / (2^{n+1} - 1) using:
1. **Lower bound:** LB's geometric marking guarantees at least c(n) against any XY response
2. **Upper bound:** Saddle-point argument via minimax theorem

## Assessment

### Correctness of Answer
The formula c(n) = 2^n / (2^{n+1} - 1) is **correct**. Verified computationally for n=1,2,3,4 by exhaustive search over LB markings and XY responses.

### Part 1: Lower Bound (LB guarantees >= c(n))

**Verdict: CORRECT**

- **Base case n=1:** Fully verified. LB marks at 1/3, gets exactly 2/3 in all cases.
- **Lemma 1 (Greedy Optimality):** Correct, standard backward induction.
- **Geometric marking strategy:** Correct. Pieces P_k = 2^k * t_n sum to 1.
- **Lemma 2 (Copy Optimality):** The argument that symmetric halving is XY-optimal against geometric marking is correct in conclusion, though Case (ii) is hand-wavy ("may jump to an earlier odd position"). Computationally verified.

### Part 2: Upper Bound (XY limits LB to <= c(n))

**Verdict: CORRECT CONCLUSION, BUT FLAWED PROOF**

**Critical Gap: Lemma 5 is FALSE**

The proof claims: "For any n+1 positive pieces summing to 1, either p_1 <= t_n OR p_{n+1} <= c(n)."

**Counterexample for n=2:**
- Pieces: [107/700, 93/350, 407/700] (sum = 1)
- p_1 = 107/700 > t_2 = 1/7 = 100/700
- p_3 = 407/700 > c(2) = 4/7 = 400/700
- Both conditions fail simultaneously.

The "Alternative Pigeonhole" argument in the proof is incomplete. It shows pieces can't grow geometrically from a base > t_n, but this doesn't establish the claimed dichotomy.

**However:** Despite Lemma 5 being false, the upper bound c(n) **still holds**. Computationally verified that for ALL tested LB markings (including the counterexamples to Lemma 5), XY can limit LB to at most c(n).

**Case (b) is underspecified:** When p_{n+1} > c(n), the proof says "XY uses the capping strategy," but this case is not fully analyzed. The proof leaves gaps about exactly how XY achieves the bound when Lemma 5 fails.

### Other Issues

1. **Lemma 4 (Pair-Cancellation):** Correct when pairs are actually consecutive in sorted order. The proof assumes pairs from halving remain consecutive, which holds when original pieces have geometric ratios but may not hold in general.

2. **Case B in Lemma 3:** Claims "XY can use asymmetric splitting to cap LB's take at c(n)" but the precise mechanism is not rigorously justified beyond the capping strategy sketch.

3. **Saddle Point Conclusion:** The logic is valid IF Condition 2 (G(L, copy) <= c(n) for all L) holds. The proof doesn't rigorously establish this for all L.

## Computational Verification

Exhaustive search confirms:
- For n=1,2,3, the maximum LB guarantee over all markings equals c(n)
- The maximum is achieved uniquely by geometric marking
- For all tested non-geometric markings, XY can limit LB to strictly less than c(n)

This provides strong evidence the answer is correct, but the proof has logical gaps.

## Verdict: CHANGES REQUESTED

**Status: partial**

The answer c(n) = 2^n / (2^{n+1} - 1) is correct. The lower bound is rigorous. The upper bound conclusion is correct but the proof has a critical gap:

**Gap to close:**
Lemma 5 is false as stated. The upper bound proof needs a different argument. Options:
1. Prove directly that for ANY LB marking, XY's optimal response (which may involve asymmetric splits) limits LB to at most c(n)
2. Find a correct pigeonhole-style lemma that captures why the upper bound holds
3. Use a potential function or direct case analysis instead of the flawed Lemma 5

The proof currently overclaims: it marks itself as "solved" but contains a false lemma in the load-bearing path.

## Scores
- **Correctness:** 7/10 (answer correct, lower bound correct, upper bound has false lemma)
- **Completeness/Rigor:** 5/10 (Lemma 5 is false, Case (b) underspecified)
- **Progress:** 8/10 (very close to complete; just need to fix the upper bound argument)

## Promotable Lemmas

**Certified:**
- **Greedy Optimality Lemma (Lemma 1):** Correct and rigorous.
- **Key Identity:** (1 + t_n)/2 = c(n) is verified algebraically.

**Rejected:**
- **Lemma 5 (Pigeonhole Bound):** FALSE. Counterexamples exist.
- **Lemma 4 (Pair-Cancellation):** Needs conditions on when pairs remain consecutive.
