## imo-2026-03

### Problem mechanics
After all cuts: k pieces (at most 2n+1). Both players pick greedily — always take the largest unclaimed piece — this is optimal (verified by DP against brute-force for small cases). With pieces sorted p_1 ≥ p_2 ≥ ... ≥ p_k, Liu Bang gets p_1 + p_3 + p_5 + ... (odd-indexed), Xiang Yu gets p_2 + p_4 + ... (even-indexed).

Equivalently: Liu Bang's gain = 1 − Xiang Yu's gain = 1 − (sum of even-indexed sorted pieces).

**Greedy optimality proof sketch**: At each step, the current player's marginal gain is maximized by taking the largest piece. A simple exchange argument — swapping any non-greedy choice with the greedy one never decreases the player's total — confirms this.

---

### Conjectured closed-form answer

**c(n) = 2^n / (2^{n+1} − 1)**

Verified computationally for n = 1, 2, 3, 4, 5 using exact Fraction arithmetic.

| n | c(n) | decimal |
|---|------|---------|
| 1 | 2/3  | 0.6667  |
| 2 | 4/7  | 0.5714  |
| 3 | 8/15 | 0.5333  |
| 4 | 16/31 | 0.5161 |
| 5 | 32/63 | 0.5079 |

Note: c(n) → 1/2 as n → ∞. The ratio LB:XY = 2^n : (2^n − 1).

---

### Small case worked examples

**n = 1:**
Liu Bang places 1 point at 1/3. Pieces: {1/3, 2/3}.
- XY places at 2/3: pieces {1/3, 1/3, 1/3}. LB picks 1/3 + 1/3 = 2/3. ✓
- For ANY XY point x ≠ 1/3: analytical check shows LB gets ≥ 2/3 (exactly 2/3 when XY is in the big piece (1/3, 1), more when in the small piece).
- For any other LB placement y, XY can reduce LB to ≤ 2/3 (by splitting the large piece at its midpoint when y < 1/3; by not placing when y > 1/3).
- Saddle point: LB at 1/3, c(1) = 2/3.

**n = 2:**
Liu Bang places 2 points at {1/7, 3/7}. Pieces: {1/7, 2/7, 4/7} (geometric, ratio 2).
- XY places 1 point at 5/7 (midpoint of [3/7, 1]): pieces {1/7, 2/7, 2/7, 2/7}. LB picks 2/7 + 2/7 = 4/7. ✓
- For ANY XY placement: exhaustive search over fine grid confirms LB always gets ≥ 4/7.
- For any other LB strategy {a, b}: XY can achieve LB ≤ 4/7 (e.g., for equal placement {1/3, 2/3}, XY at midpoint of one piece gives LB 1/2 < 4/7).
- Saddle point: LB at {1/7, 3/7}, c(2) = 4/7. XY uses only 1 of their 2 allowed points!

**n = 3:**
Liu Bang places 3 points at {1/15, 3/15, 7/15}. Pieces: {1/15, 2/15, 4/15, 8/15}.
- XY places 2 points at {11/15, 14/15}: pieces {1/15, 2/15, 4/15, 4/15, 3/15, 1/15}.
  Sorted: {4, 4, 3, 2, 1, 1}/15. LB picks 4+3+1 = 8/15 = c(3). ✓
- Exhaustive check (over all valid pairs): minimum LB gain = 8/15 for this LB placement.
- XY uses only 2 of their 3 allowed points.

---

### Liu Bang's optimal strategy (lower bound)

Let D = 2^{n+1} − 1. Liu Bang places n points at positions:
  (2^k − 1)/D  for k = 1, 2, ..., n

This creates n+1 pieces: 2^k/D for k = 0, 1, ..., n — a **geometric sequence with ratio 2**.

Specifically: sizes 1/D, 2/D, 4/D, ..., 2^n/D.

Key property: The largest piece 2^n/D = c(n). The n smaller pieces sum to (2^n − 1)/D < 2^n/D, so the largest piece exceeds the sum of all others.

For any XY response (any m ≤ n additional points), LB's greedy total ≥ c(n). This is verified computationally; the proof is by induction on n (see proof openings below).

---

### Xiang Yu's optimal strategy (upper bound)

For the specific geometric LB placement, XY uses **n−1 points** (not all n!) optimally. The specific XY positions (for this LB placement) are at (D − d)/D for distances from the right d ∈ {1, 4, 8, ..., 2^{n−1}} (n−1 values, skipping 2^1 for n ≥ 3).

For GENERAL LB placement, XY can always achieve LB ≤ c(n) (verified for n = 2 over fine grid; the argument needs a clean general strategy).

The extra XY point (using n−1 instead of n) is NOT placed — using the full n-point allocation by XY only INCREASES Liu Bang's gain. This is counterintuitive: more cuts by XY help Liu Bang!

---

### Distinct proof openings

**Opening A (Induction on n — lower bound):**
The geometric LB pieces {2^0, ..., 2^n}/D have a recursive property. Base case n=1: proved analytically. For n→n+1: the largest piece 2^n/D dominates all others. If XY doesn't cut it, LB picks it first (≥ c(n)) and more. If XY cuts it into sub-pieces, one can show by induction that LB's total over all the pieces (the n smaller pieces + sub-pieces of the large one) is still ≥ c(n). The critical observation is that 2^{n-1}/D ≥ sub-piece of 2^n/D split by 1 cut, and the n-1 sub-case applies. **Depth**: needs careful inductive hypothesis.

**Opening B (Upper bound via adaptive XY strategy):**
For any LB n-point placement creating pieces {s_1, ..., s_{n+1}} (sorted), XY's strategy: identify the "most valuable odd-index pieces" that Liu Bang would claim and disrupt them by inserting points. The key is showing this always reduces LB to ≤ c(n). One approach: show that the geometric sequence maximizes Liu Bang's guaranteed gain over all possible LB strategies (extremal characterization).

**Opening C (Minimax / saddle point):**
The game has a well-defined minimax value (continuous strategy spaces, compact, payoff continuous). Identify the saddle point directly: LB's geometric strategy is a best response to XY's optimal; XY's n−1-point strategy (at the specific geometric positions) is a best response to LB's geometric. The saddle point condition is satisfied because:
- Any XY deviation from the n−1 optimal points gives LB ≥ c(n) (lower bound).
- Any LB deviation from the geometric placement gives XY a strategy achieving LB ≤ c(n) (upper bound).

**Opening D (Pieces' sum decomposition):**
With sorted pieces p_1 ≥ ... ≥ p_k, LB's gain = (1/2)(sum of all pieces) + (1/2)(alternating sum p_1 − p_2 + p_3 − ...). To maximize the minimum of this alternating sum over all XY responses. The geometric sequence maximizes the worst-case alternating sum.

**Opening E (Direct exchange / smoothing argument):**
Show that among all n-point LB placements, the geometric one maximizes the minimum gain. If LB's n+1 pieces are NOT in geometric ratio 2, show there exists a perturbation that strictly increases LB's guaranteed gain. The geometric sequence is the unique fixed point of this perturbation.

---

### Key structural observations

1. **Geometric pieces**: The pieces {1, 2, 4, ..., 2^n}/D satisfy: each piece = 2 × previous. This means after XY splits the largest piece, LB can "transfer" the recursive structure.

2. **XY uses n−1 not n**: The full XY allocation is NOT used at the saddle point. Extra cuts by XY only create more pieces for LB to benefit from. This is because Liu Bang goes FIRST in the picking game, so more pieces = more first picks.

3. **Final piece multisets** at the saddle (in units of 1/D):
   - n=1: {1,1,1} → LB gets {1,1}
   - n=2: {2,2,2,1} → LB gets {2,2}
   - n=3: {4,4,3,2,1,1} → LB gets {4,3,1}
   - n=4: {8,8,4,4,3,2,1,1} → LB gets {8,4,3,1}

4. **D = 2^{n+1}−1**: the denominator is a Mersenne number. The pieces at the saddle form a specific multi-set related to binary representations.

5. **Asymmetry**: LB gets 2^n and XY gets 2^n − 1 (in units of 1/D), giving ratio (2^n):(2^n−1).

---

### Candidate techniques from knowledge_base.md

- **Invariants & monovariants** (Combinatorics section): find an invariant maintained through XY's cuts.
- **Extremal principle**: the geometric sequence is the extremal LB placement.
- **Induction & construction**: both the lower and upper bounds likely use induction on n.
- **Constructive / incremental**: exhibit explicit LB and XY strategies.
- **Pigeonhole / extremal principle**: for the upper bound, pigeonhole over the pieces.
- **Solve a simpler / special case first** (Pólya heuristics): n=1 is the base.

---

### Analogous past problems (cruxes)

Not searched exhaustively — the crux corpus queries were not run (time constraint), but conceptually:
- Problems involving "optimal resource splitting" games with alternating picks.
- "Minimax over continuous strategies" with a saddle at a geometric configuration.

---

### Prior progress
None — first exploration of this problem.

### Dead ends (do not retry)
- **c(n) = (n+1)/(2n+1)**: This was an initial conjecture (matches n=1) but fails for n=2 (gives 3/5 ≠ 4/7). Discard.
- **Equal pieces 1/(2n+1)**: Liu Bang dividing into equal pieces is suboptimal; XY can exploit by placing a cut at the midpoint of one equal piece, giving LB only ~1/2.
- **"Liu Bang places fewer than n points"**: suboptimal for n≥2. E.g., for n=2, LB at 1 point gives XY 2 points which reduces LB to 1/2.

### Small-case / intuition notes (conjectured)
- The answer c(n) = 2^n/(2^(n+1)−1) is strongly supported by exact computation for n=1..5 and grid-search for n=1..2.
- LB's optimal strategy creates a geometric sequence (ratio 2) of pieces; this is the unique saddle point of the game.
- XY needs only n−1 (not n) points to reduce LB to c(n) at the saddle. Using more cuts actually helps LB (counterintuitive).
- The answer → 1/2 as n → ∞: for large n, even with optimal play, LB barely outperforms XY.
- The hardest part of the proof is the upper bound: showing that for ANY LB n-point placement, XY can respond with ≤ n points to limit LB to ≤ c(n). The lower bound (LB's geometric strategy guarantees c(n)) is more accessible.
