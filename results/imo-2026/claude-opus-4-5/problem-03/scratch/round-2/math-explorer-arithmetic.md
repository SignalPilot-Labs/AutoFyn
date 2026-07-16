# imo-2026-03: Arithmetic Configuration Analysis

## CRITICAL CORRECTION OF ROUND 1 ERROR

**Round 1 claimed: arithmetic pieces (1:2:...:n+1) beat geometric for n≥2.**
**This is WRONG. The round 1 XY response was suboptimal.**

### The Error Explained (n=2 case)

Round 1 claimed: LB uses [1/6, 1/3, 1/2], XY responds with [1/4, 1/4] (splitting 1/2 into halves), giving LB = 7/12.

**But XY has a BETTER response**: split 1/2 into (1/6, 1/3) — matching the two smaller LB pieces exactly.

After XY's optimal response:
- Pieces: [1/3, 1/3, 1/6, 1/6] (sorted desc)
- LB picks positions 1 and 3: 1/3 + 1/6 = **1/2** (not 7/12!)

So LB gets only 1/2 < 4/7 (geometric) from the arithmetic configuration!

### The Structural Reason Arithmetic Fails

For arithmetic pieces (1/T, 2/T, ..., (n+1)/T) with T = (n+1)(n+2)/2:
- For n=2: pieces (1/6, 1/3, 1/2). Sum of two smaller = 1/6 + 1/3 = **1/2 = largest piece**.
- XY splits 1/2 into its "components" (1/6, 1/3): creates twins of the smaller pieces.
- Result: [1/3, 1/3, 1/6, 1/6]. LB picks 1/3 + 1/6 = 1/2.

For arithmetic configuration: sum of n smaller pieces = n(n+1)/2 / T = n/(n+2).
Largest piece = (n+1)/T = 2/(n+2).
For n=2: sum of smaller = 1/2 = largest piece (EQUAL! XY can perfectly clone it).
For n≥3: sum of smaller > largest piece (XY can do even better — the smaller pieces EXCEED the large one).

### Corrected Values (Arithmetic vs Geometric)

| n | Geometric c(n) | Arithmetic guarantee | Better |
|---|---------------|---------------------|--------|
| 1 | 2/3 | 2/3 | Equal |
| 2 | 4/7 ≈ 0.5714 | 1/2 = 0.5000 | **Geometric** |
| 3 | 8/15 ≈ 0.5333 | 1/2 = 0.5000 | **Geometric** |
| 4 | 16/31 ≈ 0.5161 | 1/2 = 0.5000 | **Geometric** |

Arithmetic is uniformly worse than geometric for n≥2.

---

## TRUE ANSWER: c(n) = 2^n / (2^{n+1} - 1)

**Confirmed by minimax computation for n=1,2,3:**

- n=1: Minimax gives optimal LB = [1/3, 2/3] (geometric). Guarantee = 2/3. ✓
- n=2: Minimax gives optimal LB = [1/7, 2/7, 4/7] (geometric). Guarantee = 4/7. ✓
- n=3: Minimax confirms geometric = [1/15, 2/15, 4/15, 8/15]. Guarantee = 8/15. ✓

The geometric answer c(n) = 2^n/(2^{n+1}-1) is CORRECT.

---

## Key Structural Analysis

### Why Geometric is Optimal for LB

**Geometric dominance property**: For pieces {1/D, 2/D, 4/D, ..., 2^n/D} with D = 2^{n+1}-1:
- The largest piece 2^n/D > sum of all smaller pieces (2^n-1)/D.
- Ratio: largest/(sum of others) = 2^n/(2^n-1) > 1.

**Contrast with arithmetic**: For arithmetic, the ratio = (n+1)/[n(n+1)/2] = 2/n. For n=2: ratio = 1 (largest EQUALS sum of others, making cloning trivial for XY).

### XY's Optimal Response to Geometric

For geometric LB, XY's optimal uses n-1 marks (out of n available):
- XY splits 2^n/D into sub-pieces {2^{n-1}/D, 2^{n-2}/D, ..., 2^1/D, 2^0/D}.
- This uses exactly n-1 marks, creating n sub-pieces.
- Result: sorted pieces = {2^{n-1}/D, 2^{n-1}/D, 2^{n-2}/D, 2^{n-2}/D, ..., 2^1/D, 2^1/D, 2^0/D, ...} where each geometric level appears twice (one from LB, one from XY).

**Example n=3**: Geometric [1/15, 2/15, 4/15, 8/15]. XY splits 8/15 into {4/15, 2/15, 2/15}:
- All pieces: {1/15, 2/15, 4/15, 4/15, 2/15, 2/15} = {4, 4, 2, 2, 2, 1}/15 (sorted desc).
- LB picks positions 1, 3, 5: 4/15 + 2/15 + 2/15 = 8/15 = c(3). ✓

### Geometric Lower Bound: Invariant Property

**Key invariant**: For geometric LB and ANY XY cut of the largest piece 2^n/D into (x, 2^n/D - x):
- If x ∈ [2^{n-1}/D, 2^n/D - 2^{n-1}/D]: LB picks BOTH sub-pieces (x and 2^n/D-x), getting exactly 2^n/D.
  - The sub-pieces "straddle" the 2^{n-1}/D piece in sorted order. LB picks 1st sub-piece and 2nd sub-piece = 2^n/D.
- If x < 2^{n-1}/D: LB picks the large sub-piece PLUS the original 2^{n-1}/D piece, getting MORE than 2^n/D.

**Verified for n=2**: For any cut of 4/7 into (x, 4/7-x):
- x ∈ [1/7, 3/7]: LB gets exactly 4/7. ✓
- x < 1/7 or x > 3/7: LB gets strictly more than 4/7. ✓
- XY's extra 2nd mark does not reduce LB below 4/7. ✓

---

## Proof Components Needed

### Part A: Lower Bound (LB achieves c(n)) — EASIER DIRECTION

**Claim**: Geometric LB configuration achieves guarantee exactly c(n) = 2^n/(2^{n+1}-1).

**Proof by induction on n:**

n=1: LB = [1/3, 2/3]. Any XY cut of 2/3 at position x:
- Pieces: {1/3, x, 2/3-x}. LB picks 1st+3rd = x + (2/3-x) = 2/3. (LB always picks BOTH sub-pieces of 2/3, giving sum = 2/3.) ✓

For general n: Key subcase is XY uses j marks inside 2^n/D and n-j outside. 
- j=0: 2^n/D intact and largest. LB picks it: gain ≥ 2^n/D. ✓
- j≥1: sub-pieces sum to 2^n/D; careful analysis of sorted order gives LB ≥ 2^n/D.
  The key: in sorted order, sub-pieces of 2^n/D "pair" with original pieces, and LB always picks a sum ≥ 2^n/D.

**The n-j marks outside 2^n/D can only help LB** (they create extra small pieces that push XY's picks down, freeing LB to pick more).

### Part B: Upper Bound (XY limits any LB to ≤ c(n)) — HARDER DIRECTION

**Claim**: For any LB n+1 pieces (a_1 ≤ ... ≤ a_{n+1}) summing to 1, XY can limit LB to ≤ c(n).

**Key XY strategies (verified computationally):**
- Against arithmetic [1/T, ..., (n+1)/T]: XY splits largest piece into the other pieces → LB gets 1/2 ≤ c(n).
- Against equal pieces [1/(n+1), ..., 1/(n+1)]: XY splits one piece to create a near-pair → LB gets 1/2 ≤ c(n).
- Against large-dominated pieces [ε, ε, ..., 1-nε]: XY splits large piece into n equal parts → LB gets ≤ 1/(n+1) + something.

**Candidate proof approach (by induction on n)**:
- XY uses 1 mark to "reduce" the n+1-piece problem.
- After cutting the largest LB piece a_{n+1} at an appropriate position, the n+2-piece problem can be bounded by applying the n-1 case inductively.
- The exact reduction needs careful analysis of how cutting a_{n+1} changes the sorted order.

**This direction remains the key gap** in the proof.

---

## Computational Summary

| n | True c(n) | Geometric | Arithmetic | Equal | Formula |
|---|-----------|-----------|------------|-------|---------|
| 1 | 2/3 | 2/3 | 2/3 | 2/3 | 2^1/3 |
| 2 | 4/7 | 4/7 | 1/2 | 1/2 | 2^2/7 |
| 3 | 8/15 | 8/15 | 1/2 | 1/2 | 2^3/15 |
| 4 | 16/31 | 16/31 | 1/2 | 1/2 | 2^4/31 |

The answer is **c(n) = 2^n / (2^{n+1} - 1)**.

---

## What Still Needs Proving

1. **Lower bound (Part A)** — The geometric configuration proves LB can guarantee c(n). The key inductive step (XY's marks inside the largest piece give LB exactly c(n)) needs to be formalized as a rigorous induction. The invariant "sum of LB's odd-indexed picks = 2^n/D" needs proof for all XY strategies.

2. **Upper bound (Part B)** — The hard direction. XY's strategy to limit ANY LB configuration to ≤ c(n). The proof should construct an explicit XY strategy and verify it works for all LB configurations. The "pairing" intuition is clear but the formal proof is nontrivial.

3. **Optimality of geometric**: Show that c(n) is tight, i.e., NO LB strategy achieves guarantee > 2^n/(2^{n+1}-1). This follows from the upper bound (Part B).

---

## Status of Previous Approaches

- **geometric-direct**: PARTIALLY CORRECT. The lower bound (geometric achieves c(n)) is essentially correct, but needs the formal invariant proof. The upper bound gap remains. Target should be c(n) = 2^n/(2^{n+1}-1) (the geometric formula), NOT a new answer.
- **induction-on-n**: DEAD. Had the wrong answer and a fatally flawed upper bound.

The correct target is c(n) = 2^n/(2^{n+1}-1) and the main task is proving BOTH bounds rigorously.
