## imo-2026-03

**Lens: The claiming phase as a combinatorial game**

---

### The Answer (strong conjecture, verified numerically for n=1,2,3)

**c(n) = 2^n / (2^(n+1) - 1)**

| n | c(n) | decimal |
|---|------|---------|
| 1 | 2/3  | 0.6667  |
| 2 | 4/7  | 0.5714  |
| 3 | 8/15 | 0.5333  |
| n | 2^n/(2^(n+1)-1) | → 1/2 as n→∞ |

---

### Distinct Openings

**Opening A: Greedy reduction + geometric marking**
Phase 1 (Claiming): Once pieces are fixed, both players should take the largest available piece each turn. This is optimal (exchange argument). Result: LB gets pieces at odd ranks (1st, 3rd, 5th, ...) of the sorted-descending piece list.
Phase 2 (Marking): This reduces the whole problem to: choose n marks to maximize (against adversarial XY marks) the sum of odd-ranked pieces.

**Opening B: Geometric strategy as Nash equilibrium**
LB marks at positions (2^k − 1)/(2^(n+1)−1) for k=1,...,n, creating n+1 pieces 1/D, 2/D, 4/D, ..., 2^n/D where D = 2^(n+1)−1. The ratio-2 geometric structure is the minimax equilibrium. Key property: the largest piece (2^n/D) strictly exceeds the sum of all other pieces (which sum to (2^n−1)/D). This means LB can "protect" the large piece.

**Opening C: XY's interleaving counter-strategy (explains upper bound)**
Against any LB strategy with pieces p_1 ≥ p_2 ≥ ... ≥ p_{n+1}, XY puts all n marks inside p_1, creating n+1 sub-pieces that interleave between the n smaller LB pieces. Specifically, sub-piece j is made slightly larger than p_{j+1}. Then the sorted order alternates: sub-piece_1, p_2, sub-piece_2, p_3, ..., with LB claiming all sub-pieces (sum = p_1) and XY claiming p_2,...,p_{n+1}. This gives LB exactly p_1. So LB's total = p_1 (its own largest piece). This gives the upper bound: LB gets at most p_1.

**Opening D: Upper bound via XY's halving + interleaving**
If p_1 > 2^n/D, XY halves p_1 (uses 1 mark), creating p_1/2, p_1/2. Now the "effective largest piece" is p_1/2 (plus the remaining XY marks to deal with the new constellation). This reduces to a smaller problem. Combined with the interleaving argument, XY can force LB ≤ 2^n/D.

**Opening E: Self-similar structure of the geometric pieces**
The n=1 lower bound has a beautiful self-containment proof:
- LB marks at 1/3. Pieces: 1/3, 2/3.
- If XY marks in [1/3, 1] at z: pieces 1/3, z−1/3, 1−z. The piece 1/3 is ALWAYS the middle piece (since (z−1/3)+(1−z) = 2/3, one of these is ≤ 1/3 and the other ≥ 1/3). LB gets exactly 2/3.
- If XY marks in [0, 1/3]: LB gets ≥ 2/3.

For general n, the geometric structure ensures every XY mark in ANY piece produces sub-pieces that "bracket" the adjacent LB pieces in value, preserving LB's odd-ranked total.

---

### Candidate Technique(s)

- **Greedy algorithm optimality in alternating selection**: exchange argument shows greedy-largest is optimal for both players. This is the key to Phase 1.
- **Minimax / game-tree analysis**: the marking phase is a two-player zero-sum game on intervals.
- **Geometric sequence as equilibrium**: the ratio-2 condition is the minimax balance point (not equal pieces, not a single big piece).
- **Interleaving argument**: the key to the upper bound — XY can always arrange sub-pieces to bracket the smaller LB pieces in sorted order.

---

### Cheap-Kill Candidates

- **Parity**: LB gets ⌈k/2⌉ pieces from k total. Since LB goes first and gets more pieces, LB always has at least 1/2. But the exact value is above 1/2.
- **Pigeonhole on piece sizes**: With n+1 pieces summing to 1, the largest piece is at least 1/(n+1). But c(n) = 2^n/(2^(n+1)−1) > 1/(n+1) for all n, so LB can do better.
- **No cheap kill on the main bound** — the geometric structure needs a real proof.

---

### Knowledge-Base Entries to Use

- **Invariants & monovariants** (Combinatorics section): the self-similar structure of the geometric pieces is essentially an invariant argument.
- **Constructive / incremental** (Combinatorics): exhibit LB's explicit strategy (geometric marking) and XY's explicit response (interleaving).
- **Extremal principle** (Combinatorics): the answer is the minimax; exhibit strategies for both sides.
- **Direct proof** and **Contradiction** (General): the claiming phase optimality uses exchange argument (assume deviation; show contradiction with optimality).
- **Constructive vs. existence** (General): need both lower bound (LB construction) and upper bound (XY construction).

---

### Analogous Past Problems (Cruxes)

**aimo-0596** (combinatorics, games-and-strategy): "In a pairing/misère take-turns game, have the responder answer each opponent pick with its fixed involution-partner." Analogous in that the key is identifying an invariant (LB's total from the sub-pieces of the large piece is constant regardless of XY's action in that piece). The interleaving argument is structurally similar: one player's picks are "paired" with the other's.

**aimo-0117** (combinatorics, games-and-strategy): "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." This is DIRECTLY analogous to LB's geometric marking strategy: the key property is that the largest piece exceeds the sum of all others, which is exactly the ratio-2 geometric series property used here.

**aimo-0262** (combinatorics, games-and-strategy): "Hand the defender a self-reproducing invariant family of configurations and show each legal move can restore it." The self-similar structure of the geometric pieces (ratio-2 preserved under XY's optimal interleaving response) is the same type of invariant.

---

### Prior Progress

None (first round, no prior approaches).

---

### Dead Ends (Do Not Retry)

None yet.

---

### Small-Case / Intuition Notes (labeled as conjecture)

**Verified numerically (not proved)**:
- n=1: c(1) = 2/3 with LB at 1/3. Verified exhaustively.
- n=2: c(2) = 4/7 with LB at (1/7, 3/7). Verified with grid N=300.
- n=3: c(3) = 8/15 with LB at (1/15, 3/15, 7/15). Verified with grid N=150.

**Conjecture**: c(n) = 2^n / (2^(n+1) − 1) for all n ≥ 1.

**Observation (proved for n=1)**: When LB marks at 1/3, LB gets EXACTLY 2/3 regardless of XY's response. The piece 1/3 always ends up as the MIDDLE piece when XY splits the large piece.

**Observation (numerical)**: XY's worst-case strategy for n=2 is to put BOTH marks inside the 4/7 piece, creating 3 sub-pieces that interleave between 2/7 and 1/7. LB claims all 3 sub-pieces = 4/7. XY claims the untouched 2/7 and 1/7 = 3/7.

**Key structural insight**: LB's pieces 1/D, 2/D, ..., 2^n/D have the property:
- 2^n/D = (2^n-1)/D + 1/D > sum of all other pieces.
- Each piece = 2 × previous piece.
- When XY splits piece 2^j/D into (a, b) with a ≥ b: a ≥ 2^(j-1)/D = next smaller LB piece.

**Upper bound mechanism**: For the n=1 upper bound, XY's strategy depends on x (LB's mark position):
- If x ≤ 1/3: XY splits the large piece (1−x) at the midpoint → LB gets (1+x)/2 ≤ 2/3.
- If x > 1/3: XY marks near x in the large piece → LB gets ≈ 1−x < 2/3.
The crossover at x = 1/3 yields exactly 2/3 = c(1). This is the minimax equilibrium.

**Note on LB using fewer than n marks**: If LB uses fewer than n marks, XY has more power to cut LB down. E.g., for n=2, if LB uses only 1 mark, XY can limit LB to ≈ 1/2 < 4/7. So LB should use all n marks.
