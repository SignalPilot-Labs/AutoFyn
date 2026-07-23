## imo-2026-03

### Problem recap
Liu Bang (LB) marks ≤ n points on a unit stick, then Xiang Yu (XY) marks ≤ n more (all distinct). The stick is cut at all marked points. They alternate claiming pieces, LB first, each always claiming the largest unclaimed piece (greedy = optimal since picking is from an independent set). Find c(n) = largest LB can guarantee.

---

### Distinct openings (attack routes)

**Route A — Geometric-ratio LB strategy + invariant analysis.**
LB places n marks to create n+1 pieces in descending geometric ratio 2^n : 2^{n-1} : ... : 2 : 1 (normalized to sum 1 by dividing by 2^{n+1}−1). The conjectured answer c(n) = 2^n/(2^{n+1}−1) is precisely the LARGEST of these pieces. Lower bound: prove this LB strategy is immune to any XY n-mark response. Upper bound: prove XY can force LB ≤ 2^n/(2^{n+1}−1) against ANY LB strategy.

**Route B — Alternating-pick induction.**
With k pieces (sorted s_1 ≥ s_2 ≥ ... ≥ s_k), LB's alternating picks give s_1+s_3+s_5+... ≥ 1/2 (proved by pairing s_{2i-1} ≥ s_{2i}). The question is how far above 1/2 LB can guarantee. Route: use induction on n; the n-mark game reduces to an (n−1)-mark sub-game inside the interval claimed by LB.

**Route C — Recursion / Stackelberg minimax.**
View as two-stage game: LB commits first, XY responds. By minimax, c(n) = max_{LB strategy} min_{XY strategy} LB's share. Route: find the Nash equilibrium by solving the saddle-point conditions; the geometric-ratio placement is LB's saddle-point strategy.

**Route D — Binary invariant: "each piece is ≤ half the remaining unallocated."**
Alternative framing: after LB marks, the pieces form a partition. XY's optimal play is to insert marks that pair up pieces, reducing LB's "excess over 1/2." The c(n) formula emerges from how many times XY can halve LB's advantage.

---

### Answer (conjectured, with strong numerical support)

**c(n) = 2^n / (2^{n+1} − 1)**

Verified:
- n=1: c(1) = 2/3 (proved analytically; LB places at 1/3)
- n=2: c(2) = 4/7 (verified: min over all XY 2-point placements for LB at (1/7, 5/7) equals exactly 4/7 via 300-point grid; equality at XY = (3/7, 6/7))
- n=3: c(3) = 8/15 (verified numerically with 80-point grid; equality at XY splitting each non-largest piece)

As n→∞: c(n) → 1/2.

---

### Optimal LB strategy (lower bound construction)

For general n: LB places n marks creating n+1 pieces of sizes  
2^n/(2^{n+1}−1),  2^{n-1}/(2^{n+1}−1),  ...,  2/(2^{n+1}−1),  1/(2^{n+1}−1)  
in LEFT-TO-RIGHT order. Concretely, mark positions are the partial sums:
- Position 1: 1/(2^{n+1}−1)  
- Position 2: (1 + 2^n)/(2^{n+1}−1)  
- Position 3: (1 + 2^n + 2^{n-1})/(2^{n+1}−1)  
- etc.

For n=1: mark at 1/3. Pieces: (2/3, 1/3).  
For n=2: marks at 1/7 and 5/7. Pieces (left to right): (1/7, 4/7, 2/7).  
For n=3: marks at 1/15, 9/15, 13/15. Pieces: (1/15, 8/15, 4/15, 2/15).

**Key structural insight:** The largest initial piece P_n = 2^n/(2^{n+1}−1) is strictly larger than the sum of ALL other pieces (sum of P_0+...+P_{n-1} = (2^n−1)/(2^{n+1}−1) < P_n).

---

### Lower bound argument sketch (LB guarantees c(n))

For n=2 with LB at (1/7, 5/7) (pieces 1/7, 4/7, 2/7):

XY adds ≤ 2 marks to create at most 5 pieces. In ALL cases:
- XY places both marks inside [1/7, 5/7] (the big segment): 5 pieces total. In the sorted order, LB always picks sum ≥ 4/7. Analytically: pieces (1/7, a, b, 2/7) or (1/7, a, b, c, 2/7) with a+b(+c)=4/7; one can verify LB's picks = 4/7 or higher in all cases.
- XY places marks across multiple pieces: also ≥ 4/7 by case analysis.
- Equality: XY at (3/7, 6/7) → pieces (1/7, 2/7, 2/7, 1/7, 1/7), sorted (2/7, 2/7, 1/7, 1/7, 1/7), LB = 2/7+1/7+1/7 = 4/7.

For general n, the argument is by induction: each XY mark can only split one existing piece, and the geometric structure ensures that even after n splittings, the sorted-pick sum stays ≥ 2^n/(2^{n+1}−1).

---

### Upper bound argument sketch (XY forces LB ≤ c(n))

XY's strategy for arbitrary LB placement creating pieces p_1 ≥ p_2 ≥ ... ≥ p_{n+1}:

Case: p_1 ≥ 2^n/(2^{n+1}−1). XY places marks to split the smaller pieces and create pairs of equal pieces (reducing LB's "excess picks"). Specifically, XY can often create paired configurations where LB's sum equals exactly 4/7 (n=2) or 8/15 (n=3).

Verified for n=2: for LB at (1/7, 5/7), minimum = 4/7. For any other LB placement, XY finds a 1- or 2-point response achieving ≤ 4/7. 

Note: LB at "near-endpoint" positions (like (1/7, 2/7) creating pieces 1/7, 1/7, 5/7) can be reduced to approach 1/2 by XY using only 1 mark near the endpoint of the big piece. The minimax optimum for XY is 4/7 (not 1/2), achieved by the specific LB strategy above.

---

### Picking phase analysis

Key facts about alternating greedy pick from sorted pieces:
1. LB ALWAYS gets ≥ 1/2 (from sorted list: s_1 ≥ s_2, s_3 ≥ s_4, etc. so LB ≥ XY)
2. With m pieces, LB picks ceil(m/2) of them.
3. With equal pieces: LB gets ceil(m/2)/m → 1/2 as m → ∞.
4. The formula c(n) = 2^n/(2^{n+1}−1) > 1/2 for all finite n.

XY cannot create pieces with 0 length (all marks must be interior, distinct), so LB always gets strictly > 1/2, but c(n) = 2^n/(2^{n+1}−1) is the infimum of LB's guarantee over all XY responses.

---

### XY interaction with LB's marks

For n=1: XY cannot go below 2/3 against LB at 1/3, because:
- XY inside [0, 1/3]: LB still takes 2/3 + something.  
- XY inside [1/3, 1]: LB takes max(y−1/3, 1−y) + 1/3. Both sub-pieces of [1/3, 1] sum to 2/3, and LB picks BOTH (1st and 3rd from the 3-piece sorted list). Always exactly 2/3.

For n=2: XY tries to create "pairs" of pieces of equal size. When XY creates two pairs (a,a,b,b), LB gets a+b=1/2 (if all from XY's 2-point placement). The optimal XY response to LB at (1/7, 5/7) is to split the big 4/7 piece into two 2/7 pieces, creating (2/7, 2/7, 2/7, 1/7, 1/7) → LB = 4/7 (not 1/2!).

Key asymmetry: the two outer pieces (1/7 and 2/7) are UNEQUAL, which prevents XY from creating a fully balanced configuration.

---

### Candidate techniques

- **Geometric series / binary sequences**: the answer 2^n/(2^{n+1}−1) is the sum of a geometric series and the "largest piece in a geometric partition."
- **Greedy alternating pick analysis**: sorted-list alternating sum, pairing argument.
- **Minimax / Stackelberg equilibrium**: two-stage commit-then-respond game.
- **Induction on n**: reducing n-mark game to (n−1)-mark sub-game.
- **Invariant under XY's moves**: the key invariant is that LB's picks always include contributions from each "generation" of the geometric partition.

---

### Cheap-kill candidates

- **Parity argument**: with 2n+1 pieces (odd), LB picks n+1, XY picks n. LB gets > 1/2 always (sorted-list argument). This kills c(n) = 1/2 as possible answer.
- **Equal-piece lower bound**: n+1 equal pieces give LB (n+1)/(2n+1) ≥ c(n). Confirmed: (n+1)/(2n+1) > 2^n/(2^{n+1}−1) for n≥2 (e.g., 3/5 > 4/7). So the EQUAL partition is NOT optimal — XY disrupts it.
- **Size argument**: c(n) must be between (n+1)/(2n+1) (equal piece optimum) and the XY-disrupted optimum 2^n/(2^{n+1}−1). Wait, actually (n+1)/(2n+1) > 2^n/(2^{n+1}−1) for n≥2 since: 3/5=0.6 > 4/7≈0.571. So the equal partition OVER-promises what LB can guarantee.

---

### Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics section): the key invariant is LB's minimum pick sum under geometric placement.
- **Extremal principle** (Combinatorics): take the optimal LB placement as the extremal configuration; prove it's the minimax solution.
- **Constructive vs. existence** (General Proof Methods): need upper bound AND matching construction (both for competition).
- **Direct proof / casework** (General Proof Methods): the lower bound for n=2 relies on casework over where XY's marks fall (inside big piece / outside).
- **Induction** (General Proof Methods): likely the proof for general n uses induction, building the n-mark strategy from the (n−1)-mark one.

---

### Analogous past problems (cruxes)

**aimo-0012** (combinatorics/processes-and-algorithms): Greedy fill forcing each closed part past a capacity threshold, then charging against per-part surplus. The crux move "greedy pick with a capacity argument" is analogous to how LB's greedy claim of the largest piece always guarantees at least a threshold. Somewhat analogous.

**aimo-0115** (combinatorics/games-and-strategy): Pairing strategy — "pair the cells into dominoes and answer in the partner cell." The pairing idea (XY pairs pieces to reduce LB's advantage) appears here. Somewhat analogous.

No perfect match in corpus — the specific "alternating pick from a partition with adversarial marking" structure doesn't appear directly.

---

### Prior progress

None — first round, no prior approaches.

---

### Dead ends (do not retry)

- **LB at (1/3, 2/3) for n=2**: Shown to give only 1/2 guarantee (XY at 1/6 reduces to exactly 1/2). Dead.
- **LB at equal spacing for any n**: XY can always split ONE piece to create two pairs, reducing LB to ~1/2. Not optimal.
- **c(n) = (n+1)/(2n+1)**: LB cannot achieve this. Equal partition is disrupted by XY using just 1 mark. Dead.
- **c(n) = 1/2 for n≥2**: False. LB can always guarantee > 1/2; and specifically c(n) = 2^n/(2^{n+1}−1) > 1/2. Dead.

---

### Small-case / intuition notes (all labeled as evidence, not proof)

**Evidence for c(n) = 2^n/(2^{n+1}−1):**
- n=1: c(1) = 2/3 = 2/(4−1). Analytically proved.
- n=2: c(2) = 4/7 = 4/(8−1). Numerically verified (300-point grid, minimum = 4/7 exactly for LB at (1/7, 5/7)).
- n=3: c(3) = 8/15 = 8/(16−1). Numerically verified (80-point grid, minimum = 8/15 for LB at (1/15, 9/15, 13/15)).

**Key structural conjecture** (not proved):
The optimal LB strategy creates pieces in geometric ratio 2^n : 2^{n-1} : ... : 1, with the largest piece being c(n). XY's worst-case response achieves exactly c(n) = LB's share.

**Likely proof structure:**
- Lower bound: LB at specific geometric placement, prove by induction or direct case analysis that XY's n marks cannot reduce LB below c(n).
- Upper bound: For any LB placement, XY's n marks can achieve LB = c(n). Key: if pieces are NOT in geometric ratio, XY can "pair up" pieces to reduce LB's picks to ≤ c(n).

**Note on n=1 proof transferring to n=2:**
For n=1, LB at 1/3: any XY mark in [1/3,1] creates two sub-pieces of [1/3,1] that BOTH go to LB (as 1st and 3rd picks in 3-piece game). For n=2, LB at (1/7, 5/7): the two "outer" pieces (1/7 and 2/7) serve as "anchors" that LB always picks, while the large piece 4/7 acts like the n=1 "large piece" — XY can split it but LB claims a guaranteed amount.
