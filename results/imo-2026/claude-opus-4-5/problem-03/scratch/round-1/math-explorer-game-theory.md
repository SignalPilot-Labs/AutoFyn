## imo-2026-03 (game theory / strategy lens)

### Answer conjecture

**c(n) = 2^n / (2^(n+1) - 1)**

Verified computationally for n = 1, 2, 3, 4 via exhaustive rational-arithmetic search (fractions with denominator up to 200, XY trying all combinations of up to n marks):

| n | c(n) | decimal |
|---|------|---------|
| 1 | 2/3 | 0.6667 |
| 2 | 4/7 | 0.5714 |
| 3 | 8/15 | 0.5333 |
| 4 | 16/31 | 0.5161 |

Note: c(n) = 2^n / (1 + 2 + 4 + ... + 2^n) = (largest piece)/(sum of all pieces in LB's geometric marking). As n → ∞, c(n) → 1/2 from above.

---

### Picking-phase structure

Both players pick greedily (always take the largest unclaimed piece). This is optimal for both and was verified computationally: `game_value(pieces) == greedy_value(pieces)` for every tested configuration. So the picking phase reduces to: sort pieces descending as p_1 ≥ p_2 ≥ ... ≥ p_N; LB gets p_1 + p_3 + p_5 + ... (odd-indexed, 1-based).

With at most 2n marks total → at most 2n+1 pieces → LB picks at most n+1 pieces.

---

### LB's optimal marking strategy (lower bound)

**Geometric progression:** Mark at positions (2^k - 1)/D for k = 1, ..., n, where D = 2^(n+1) - 1.

This creates n+1 pieces of lengths 1/D, 2/D, 4/D, ..., 2^n/D.

Key structural property: the largest piece (2^n/D) is strictly greater than the sum of all others:
2^n/D > (1 + 2 + ... + 2^(n-1))/D = (2^n - 1)/D.

**Claim (verified for n=1,2,3,4):** For this LB marking, any XY response with at most n marks gives LB ≥ 2^n/D.

**Why XY can only reach the floor 2^n/D:**

XY's optimal response is to cut the big piece (2^n/D) into sub-pieces: 2^(n-1)/D, 2^(n-2)/D, ..., 2/D, 1/D, 1/D (using n-1 marks, not even all n marks). This gives:

All pieces (units of 1/D):
- From LB: 1, 2, 4, ..., 2^(n-1)
- From XY cutting big piece: 2^(n-1), 2^(n-2), ..., 2, 1, 1

Sorted (for n=3): 4, 4, 2, 2, 2, 1 (in 1/15 units). LB picks positions 0,2,4: 4+2+2 = 8 = 2^3.
Sorted (for n=4): 8, 8, 4, 4, 2, 2, 2, 1 (in 1/31 units). LB picks positions 0,2,4,6: 8+4+2+2 = 16 = 2^4.

The general pattern: the sorted configuration is (2^(n-1), 2^(n-1), 2^(n-2), 2^(n-2), ..., 2, 2, 2, 1) and LB picks every other one, getting exactly 2^n/D.

**Why XY's third (extra) mark can't reduce LB further:** Tested for n=3: cutting any piece beyond the (n-1)-mark XY strategy only helps LB (creates more small pieces that happen to go to LB at positions 0, 2, 4, 6 of the new sorted list). Verified computationally.

---

### Upper bound (XY can limit LB to ≤ c(n))

For any LB marking creating pieces B_1 ≥ B_2 ≥ ... ≥ B_m (m ≤ n+1):

**XY strategy:** Cut B_1 (the largest LB piece) into sub-pieces that "mirror" the geometric structure.

Concretely: if B_1 > B_2 ≥ B_3 ≥ ..., XY cuts B_1 into sub-pieces ≤ B_2. Once the maximum piece size drops, the alternating sum is controlled.

The upper bound is confirmed by the exhaustive search (n=2 with denominators 7,14,21,28,35): the best LB can guarantee is exactly 4/7, achieved at marks [4/35, 2/5] and also at [1/7, 3/7]. No LB strategy beats c(n).

**Key insight for upper bound proof:** Whatever m ≤ n+1 pieces LB creates, XY has n marks with which to limit LB. The difficult case is m = n+1 (LB uses all marks). For m < n+1, XY has "surplus" marks to equalize aggressively, limiting LB to less than c(n).

The formal upper bound argument for m = n+1 likely goes by induction on n, using the observation: if LB's top piece is A_1 ≤ c(n), then XY cuts the next piece down, and inductively the alternating sum stays ≤ c(n). If A_1 > c(n), XY cuts A_1 down to create copies of A_2, which by induction keeps LB bounded.

---

### Distinct openings (rival approaches for the outliner)

1. **Direct geometric strategy:** Prove both bounds directly using the specific LB marking (2^k-1)/D and the explicit XY counter. Lower bound: case analysis on where XY's n marks land (in which original pieces). Upper bound: show XY's "geometric mirror" cutting dominates any LB configuration.

2. **Induction on n:** Base n=1 (LB marks at 1/3, proved analytically). Inductive step: given LB's optimal strategy for n, extend to n+1 by understanding how one extra mark changes the equilibrium. The answer 2^n/(2^(n+1)-1) satisfies c(n+1) = c(n)/(2-c(n)) or equivalently the "doubling reduction" 1/c(n+1) = 2/c(n) - 1 (not verified; needs checking).

3. **Linear programming / minimax formulation:** Frame as a zero-sum game and compute the value using LP. The answer c(n) is the minimax value of LB's total under optimal play by both. The extremal LB strategy and XY response are saddle points.

4. **Greedy selection analysis:** Focus first on the picking phase. Since greedy is optimal, LB's value = alternating sum of sorted pieces. The marking phase becomes: LB places n marks to maximize the adversarial minimum of this alternating sum. XY places n marks to minimize it. This is a minimax problem on piece distributions.

---

### Candidate techniques (from knowledge base)

- **Invariants & monovariants** (knowledge_base.md — General Proof Methods): the "geometric dominance" property (each piece > sum of all smaller) is the key invariant.
- **Constructive + upper bound duality** (knowledge_base.md — General Proof Methods): "For 'find all / largest n': prove an upper bound AND construct an example that attains it."
- **Pigeonhole** (knowledge_base.md — Combinatorics): used implicitly in showing XY's marks can't reduce LB below c(n) in certain configurations.
- **Casework / exhaustion** (knowledge_base.md — General Proof Methods): proof of lower bound proceeds by cases on where XY places marks relative to LB's geometric pieces.

---

### Analogous past problems (cruxes)

1. **aimo-0117** (combinatorics, `games-and-strategy`): "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." This is exactly the key LB technique in our problem — geometric pieces where the largest dominates. The problem involves two players placing values into boxes; LB uses powers of 2 for their marks. Crux: `geometric/dyadic dominance`.

2. **aimo-0262** (combinatorics, `games-and-strategy`): "For an adversarial capacity game, hand the defender a self-reproducing invariant family of configurations and show each legal move can restore it, so the bound holds forever by induction." The self-reproducing invariant structure is analogous to how the geometric pieces preserve LB's guarantee regardless of XY's response.

3. **aimo-0596** (combinatorics, `games-and-strategy`): Pairing/mirroring strategy where one player uses a "floating" unpaired element to maintain control. The XY response of cutting the big piece into geometric sub-pieces has a similar "mirror" flavour.

---

### Prior progress

None (first round, problem unsolved with no approaches).

---

### Dead ends (do not retry)

- **LB marking equal-spaced n points:** For example (1/3, 2/3) for n=2 gives LB only 1/2 (XY marks at 1/2 → pieces 1/3, 1/6, 1/6, 1/3, LB gets 1/2). Equal spacing is provably suboptimal.
- **LB marking 0 points:** For n ≥ 1, XY marks n points to split the stick into n+1 or more pieces, forcing LB to only 1/(n+1) or less. Much worse than c(n).
- **c(n) = (n+1)/(2n+1):** Computationally falsified for n=2 (3/5 ≠ 4/7). Equal-piece formula is wrong.
- **c(n) = 2n/(4n-1):** Matches n=1,2 but fails for n=3 (6/11 ≈ 0.545 ≠ 8/15 ≈ 0.533).

---

### Small-case / intuition notes (labeled as conjecture)

**n=1:** LB marks at 1/3. For any XY mark y ≠ 1/3: if y ∈ (1/3, 1), pieces are 1/3, y-1/3, 1-y. LB picks (1-y) and (y-1/3) → total 2/3. If y < 1/3, LB gets ≥ 2/3. So LB guarantees EXACTLY 2/3. This is fully proved analytically.

**n=2:** LB marks at 1/7, 3/7. For any XY marks y_1, y_2: CONJECTURE LB always gets ≥ 4/7. Supported by exhaustive rational search. XY's best response: mark at 5/7, creating pieces 1/7, 2/7, 2/7, 2/7; LB gets 4/7 exactly.

**n=3:** CONJECTURE c(3) = 8/15. LB marks at 1/15, 3/15, 7/15. XY marks at 11/15, 13/15 (in the 8/15 piece), creating pieces 4, 4, 2, 2, 2, 1 (in 15ths). LB gets 4+2+2 = 8/15.

**Structural insight (key conjecture):** The proof reduces to showing that the geometric LB marking creates pieces with the "dominance" property that forces LB ≥ c(n) regardless of XY's response. The upper bound (LB can't do better) is supported computationally but the general argument is the main proof gap.

**Note on XY's optimal marks:** XY only needs n-1 marks (not all n) to achieve the minimum LB value of c(n) against the geometric strategy. The n-th mark does not help XY further.
