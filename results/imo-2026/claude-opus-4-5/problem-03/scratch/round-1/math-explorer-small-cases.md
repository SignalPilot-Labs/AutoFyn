## imo-2026-03

### Problem summary

Let n be a positive integer. Liu Bang (LB) marks at most n points on a stick of length 1, then Xiang Yu (XY) marks at most n points (all marks distinct). The stick is cut at all marked points; players alternate claiming pieces, LB first, each greedily (taking the largest available). Find the largest c such that LB can guarantee total length at least c, regardless of XY's play.

**Key game model:** Both mark simultaneously (LB first, XY sees LB's marks and responds), then alternate picking pieces with LB first, both playing greedily (exchange argument shows greedy is optimal).

---

### Conjectured answer

**c(n) = 2^n / (2^{n+1} - 1)**

Values:
| n | c(n) | decimal |
|---|------|---------|
| 1 | 2/3 | 0.6667 |
| 2 | 4/7 | 0.5714 |
| 3 | 8/15 | 0.5333 |
| 4 | 16/31 | 0.5161 |

Equivalent form: c(n) = 2^n / (1 + 2 + 4 + ... + 2^n). As n → ∞, c(n) → 1/2.

---

### LB's optimal strategy

Mark at positions (2^k - 1)/(2^{n+1} - 1) for k = 1, 2, ..., n.

Let m = 2^{n+1} - 1. The n marks are at 1/m, 3/m, 7/m, ..., (2^n-1)/m.

This creates n+1 pieces of lengths:
- 1/m, 2/m, 4/m, ..., 2^n/m

**Geometric ratio 1:2:4:...:2^n.** The largest piece has length exactly c(n) = 2^n/m.

Explicit verification:
- n=1: mark at 1/3; pieces [1/3, 2/3].
- n=2: marks at [1/7, 3/7]; pieces [1/7, 2/7, 4/7].
- n=3: marks at [1/15, 3/15, 7/15]; pieces [1/15, 2/15, 4/15, 8/15].
- n=4: marks at [1/31, 3/31, 7/31, 15/31]; pieces [1/31, 2/31, 4/31, 8/31, 16/31].

---

### Small-case computations

#### n=1: c(1) = 2/3 (analytically proven)

LB marks at 1/3; pieces {1/3, 2/3}.

For any XY mark at t ≠ 1/3:
- t ∈ (0, 1/3): pieces {t, 1/3-t, 2/3}. Sorted desc: [2/3, ...]. LB takes 2/3 + min(t, 1/3-t). LB gets ≥ 2/3. ✓
- t ∈ (1/3, 2/3): pieces {1/3, t-1/3, 1-t}. Since 1-t > 1/3 > t-1/3, sorted: [1-t, 1/3, t-1/3]. LB takes (1-t) + (t-1/3) = 2/3. ✓
- t ∈ (2/3, 1): pieces {1/3, t-1/3, 1-t}. Since t-1/3 > 1/3 > 1-t, sorted: [t-1/3, 1/3, 1-t]. LB takes (t-1/3) + (1-t) = 2/3. ✓
- t ∈ (0, 1/3): LB marks inside 1/3 piece; LB gets ≥ 2/3 + something. ✓

**LB gains exactly 2/3 against any XY response in [1/3, 1], and more against XY in [0, 1/3]. Proof complete for n=1.**

#### n=2: c(2) = 4/7 (numerically verified)

LB marks at [1/7, 3/7]; pieces [1/7, 2/7, 4/7].

Without XY: LB takes 4/7+1/7 = 5/7.

XY's best response is 1 mark anywhere inside the 4/7 piece creating sub-pieces ≥ 1/7 from each end:
- XY at 4/7 (creating sub-pieces 1/7 and 3/7): pieces {1/7, 2/7, 1/7, 3/7}. Sorted: [3/7, 2/7, 1/7, 1/7]. LB takes 3/7+1/7 = 4/7. ✓
- XY at 5/7 (sub-pieces 2/7 and 2/7): pieces {1/7, 2/7, 2/7, 2/7}. Sorted: [2/7, 2/7, 2/7, 1/7]. LB takes 2/7+2/7 = 4/7. ✓
- XY at 6/7 (sub-pieces 3/7 and 1/7): same as 4/7 case. LB = 4/7. ✓

**Key observation:** XY marking inside the 2/7 or 1/7 pieces gives LB ≥ 5/7 (hurts XY). XY's only productive move is inside the 4/7 piece.

Upper bound check (exhaustive, denom 15): No LB 2-mark strategy gives a guarantee > 4/7. The geometric strategy [1/7, 3/7] achieves the maximum possible guarantee of 4/7.

XY needs only n-1=1 mark (out of the allowed 2) to achieve the limiting value.

#### n=3: c(3) = 8/15 (numerically verified)

LB marks at [1/15, 3/15, 7/15]; pieces [1/15, 2/15, 4/15, 8/15].

Without XY: LB takes 8/15 + 2/15 + (nothing left from greedy, 4 pieces total, ceil=2) = actually 8/15+2/15=10/15 = 2/3.

XY's optimal 2-mark response (n-1=2 marks):
- Mark at 4/15 (inside the 4/15 piece [3/15, 7/15], creating sub-pieces 1/15 and 3/15).
- Mark at 11/15 (inside the 8/15 piece [7/15, 1], creating sub-pieces 4/15 and 4/15).

Result: pieces {1/15, 2/15, 1/15, 3/15, 4/15, 4/15}.
Sorted: [4/15, 4/15, 3/15, 2/15, 1/15, 1/15].
LB takes positions 0, 2, 4: 4/15 + 3/15 + 1/15 = 8/15. ✓

Upper bound check (exhaustive, denom 15): No LB 3-mark strategy (with denominator ≤ 15) gives guarantee > 8/15. Confirmed.

XY uses n-1=2 marks (out of allowed 3). The 3rd XY mark doesn't improve XY's position.

#### n=4: c(4) = 16/31 (numerically verified)

LB marks at [1/31, 3/31, 7/31, 15/31]; pieces [1/31, 2/31, 4/31, 8/31, 16/31].

XY's optimal 3-mark response (n-1=3 marks):
- Marks at 19/62 and 27/62 inside the 8/31 piece [14/62, 30/62] (creating sub-pieces 5/62, 4/31, 3/62).
- Mark at 23/31 inside the 16/31 piece [15/31, 1] (equal split: 8/31 and 8/31).

Result: pieces {1/31, 2/31, 4/31, 5/62, 3/62, 8/31, 8/31}.
Sorted: [8/31, 8/31, 4/31, 4/31, 5/62, 2/31, 3/62, 1/31].
Rearranged: [16/62, 16/62, 8/62, 8/62, 5/62, 4/62, 3/62, 2/62].
LB takes positions 0, 2, 4, 6: 16/62 + 8/62 + 5/62 + 3/62 = 32/62 = 16/31. ✓

XY uses n-1=3 marks (out of allowed 4).

---

### Key structural insights

**Insight 1: XY's optimal response uses n-1 marks, not n.**
Computationally confirmed for n=1,2,3,4. Using the n-th mark does not help XY further reduce LB's gain below c(n).

**Insight 2: XY marking outside the two largest pieces is counterproductive.**
For n=2: XY marking in the 2/7 or 1/7 pieces leaves LB with 5/7 > 4/7 (verified). XY is forced to mark in the largest piece.
For n=3: XY marking in the 2/15 or 1/15 pieces creates equally-sized small pieces, which LB exploits (LB gets ≥ 3/5 > 8/15).

**Insight 3: Geometric sequences under XY splitting.**
XY's optimal strategy for the geometric LB configuration:
- n=2: 1 mark splits 4/7 piece into 1/7 + 3/7. New pieces: {1/7, 1/7, 2/7, 3/7} = {1, 1, 2, 3}/7.
- n=3: 2 marks split 4/15 into 1/15+3/15 and 8/15 into 4/15+4/15. New pieces: {1,1,2,3,4,4}/15.
- XY splits the two largest pieces, recreating a balanced configuration where LB gets exactly c(n).

**Insight 4: The largest piece equals c(n).**
The LB strategy ensures the LARGEST piece has length exactly c(n). If XY doesn't mark inside it, LB takes it and gets ≥ c(n). If XY marks inside it (j marks), the sub-pieces must sum to c(n), but the remaining intact pieces help LB recover.

**Insight 5: LB benefits more from using n marks than fewer.**
If LB places k < n marks, XY uses n marks to create even pieces (n+k+1 ≤ 2n+1 pieces), and LB gets less than c(n). For example, LB at 1/2 (1 mark for n=2) guarantees only 1/2 < 4/7 since XY can create 4 equal pieces.

---

### Lower bound proof structure (n=1 proven; general case sketched)

**For n=1:** Analytically verified above. The crucial property: wherever XY marks, LB gets exactly 2/3 or more.

**For general n — recursive structure:**
LB places the geometric marks. Consider XY's response:

Case 1 (XY marks all j points OUTSIDE the 2^n/m piece):
The 2^n/m piece is intact. LB takes it first. LB gains ≥ 2^n/m = c(n). ✓

Case 2 (XY marks inside the 2^n/m piece):
Sub-pieces sum to 2^n/m. The remaining intact pieces are {1/m,...,2^{n-1}/m}.
By induction / recursive argument (not yet formalized): LB's picks from sub-pieces plus smaller intact pieces sum to ≥ 2^n/m.

The case 2 argument is the crux of the lower bound and requires formalization. It likely involves showing that any split of the 2^n/m piece plus the smaller geometric pieces gives LB ≥ c(n) via an inductive argument.

**Key observation for lower bound:** For n=2, a clean case analysis works:
- If XY marks at position t from the start of the 4/7 piece:
  - t < 1/7: sub-pieces (t, 4/7-t). Sorted: [4/7-t, 2/7, 1/7, t]. LB takes (4/7-t) + 1/7 = 5/7-t ≥ 5/7-1/7 = 4/7. ✓
  - t ∈ [1/7, 3/7]: sub-pieces (t, 4/7-t) both ≥ 1/7. Sorted: [max, 2/7, min, 1/7] where max+min=4/7. LB takes max + min = 4/7. ✓
  - t > 3/7: symmetric to t < 1/7 case. LB ≥ 4/7. ✓

---

### Upper bound proof structure

**Claim:** For ANY LB n-mark strategy, XY can use at most n marks to limit LB to ≤ c(n).

**Status:** Confirmed numerically for n=2 (all denominators ≤ 15 exhausted) and n=3 (all denominators ≤ 15 exhausted). No LB strategy beats c(n).

**Proof direction (not yet established):** XY's strategy after seeing LB's pieces [p_{n+1} ≥ p_n ≥ ... ≥ p_1]:
XY uses n-1 marks to target the two largest pieces (p_{n+1} and p_n), splitting them to create a balanced configuration where LB gets exactly c(n).

The proof likely requires an averaging/convexity argument or a direct induction showing that for any piece configuration, XY can limit LB to ≤ c(n). This is the primary open gap.

**Key difficulty:** The upper bound requires analyzing ALL possible LB configurations, not just the geometric one. A clever XY strategy needs to handle arbitrary piece sizes.

---

### Analogous crux problems

**aimo-0117** (combinatorics, games-and-strategy):
Crux: "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others."
Analogy: LB's geometric strategy creates pieces in 1:2:4:...:2^n ratio. In our problem, the LARGEST piece (2^n/m) is c(n), and the sum of all others is (2^n-1)/m = c(n)-1/m. The key difference: in aimo-0117, the largest value EXCEEDS the sum of others; in our problem, it EQUALS the others' sum + 1/m (close but not exceeding). The technique of using a geometric sequence to "dominate" the configuration is directly analogous.

**aimo-0019** (combinatorics, games-and-strategy):
Crux: "In a covering game, respond to each opponent move by painting the cell immediately beyond the current filled frontier."
Analogy: Involves dyadic intervals on [0,1] and a coverage game. The recursive structure of dividing [0,1] into dyadic intervals parallels LB's geometric marks. Less directly analogous but the dyadic/geometric interval structure is similar.

**aimo-0262** (combinatorics, games-and-strategy):
Crux: "For an adversarial capacity game, hand the defender a self-reproducing invariant family of configurations."
Analogy: The Cinderella problem uses an invariant maintained through an adversarial game. LB's geometric configuration has a similar "self-reproducing" property: XY's marking inside the geometric pieces creates configurations that again have a geometric-like structure (as seen in n=3 and n=4 computations).

---

### Dead ends (do not retry)

- **Equal-spacing LB strategy** (marks at k/(n+1) for k=1,...,n): creates equal pieces, which XY can split symmetrically to limit LB to 1/2. Gives guarantee ≤ 1/2 < c(n). Confirmed computationally.
- **Symmetric LB strategies** [a, 1-a]: XY marks at midpoint, giving LB only 1/2 guarantee. Confirmed for various values of a.
- **Exhaustive brute-force upper bound proof for n=3 with large denominators**: The n=3 computation with denominators > 15 is feasible only by random sampling, which confirmed c(3) = 8/15 but is not a proof.

---

### Distinct openings for the outliner

1. **Lower bound via case analysis on XY's largest-piece marking** (most tractable): For the geometric LB strategy, prove by case analysis (on which LB pieces XY marks in) that LB always gets ≥ c(n). The n=2 case admits a clean 3-case analysis. Generalize by induction on n or on the number of XY marks inside the largest piece.

2. **Lower bound via exchange argument**: Show that moving any XY mark from a smaller piece to the largest piece cannot increase XY's gain; hence XY's optimal strategy involves all marks in the largest piece. Then analyze the one-piece subproblem by induction.

3. **Upper bound via greedy XY strategy**: For any LB n+1 pieces, define XY's n-1 marks to equalize the top-2 pieces. Show this brings LB's total to ≤ c(n). The key lemma: for any configuration with pieces p_{n+1} ≥ ... ≥ p_1, if XY splits p_{n+1} into p_{n+1}/2 + p_{n+1}/2, the resulting LB total decreases and the problem reduces to n-1.

4. **Recursion approach**: Verify the recursion c(n) = c(n-1)/(1+c(n-1)) or another explicit relation, and derive c(n) = 2^n/(2^{n+1}-1) from the recurrence. (Note: c(n-1)/(1+c(n-1)) = [2^{n-1}/(2^n-1)] / [1+2^{n-1}/(2^n-1)] = 2^{n-1}/(2^{n+1}-1) ≠ c(n), so this specific recursion is wrong; the correct one needs to be found.)

5. **Potential function / invariant**: Find an invariant I(pieces, LB_total) such that after LB's geometric marking, I is maintained under any XY marks and XY picking, proving LB always reaches c(n).

---

### Prior progress

None: problem is unsolved, no approaches exist yet. This is round 1.

### Small-case / intuition notes (labeled as conjecture)

**Conjecture (strongly supported):** c(n) = 2^n/(2^{n+1}-1) for all positive integers n.
Evidence: exact computation for n=1,2,3,4.

**Conjecture:** LB's unique optimal (up to reflection) strategy is the geometric marking at (2^k-1)/(2^{n+1}-1) for k=1,...,n.
Evidence: exhaustive search for n=2,3 (denom ≤ 15) shows no other LB strategy achieves the same guarantee.

**Conjecture:** XY's optimal response uses exactly n-1 marks, not n.
Evidence: numerically verified for n=1,2,3,4.

**Conjecture:** XY marking in any piece other than the two largest is suboptimal (gives LB more than c(n)).
Evidence: verified for n=2 (marking in 2/7 or 1/7 pieces) and n=3 (marking in smaller pieces gives LB ≥ 3/5 > 8/15).

### Candidate techniques

- Geometric series / geometric configuration as an optimal strategy
- Minimax game theory: Stackelberg formulation (LB is leader)
- Induction on n (the recursive case structure is clear)
- Exchange argument (showing greedy picking is optimal)
- Case analysis on XY's mark placement relative to LB's pieces

### Knowledge-base entries to use

From knowledge_base.md (to be checked by outliner):
- Minimax theorem / game theory entries
- Extremal principles (LB's strategy is extremal — geometric)
- Greedy algorithm / exchange argument (for piece-picking optimality)
- Geometric series entries
- Induction entries
