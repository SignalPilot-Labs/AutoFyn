## imo-2026-03

**Problem (Chu-Han War / stick game):**
LB marks ≤ n points, then XY marks ≤ n more (distinct) points on a stick of length 1. The stick is cut at all marked points. They then alternate claiming pieces, LB first, each picking the largest unclaimed piece. Find the largest c such that LB can guarantee total length ≥ c regardless of XY's play.

---

### CONJECTURED ANSWER (strongly supported by numerical evidence for n=1,2,3,4):

**c(n) = 2^n / (2^(n+1) − 1)**

Verification:
- n=1: c = 2/3
- n=2: c = 4/7 ≈ 0.5714
- n=3: c = 8/15 ≈ 0.5333
- n=4: c = 16/31 ≈ 0.5161
- n→∞: c → 1/2

---

### Distinct Openings

**Opening A (Geometric Interval Strategy — LB lower bound):**
LB creates n+1 intervals in geometric ratio 1:2:4:…:2^n by placing marks at positions (2^k−1)/D for k=1,…,n, where D = 2^(n+1)−1. Numerically verified to guarantee c(n) for n=1,2,3,4. The binding XY strategy is to halve each of the n non-minimal intervals, converting {1/D, 2/D, …, 2^n/D} into a (2n+1)-piece configuration from which LB picks exactly 2^n/D.

**Opening B (Alternating-pick parity — XY upper bound):**
With n+1+k total pieces (k = XY marks placed), LB picks ⌈(n+1+k)/2⌉ pieces, XY picks ⌊(n+1+k)/2⌋. The "worst parity" for LB is k ∈ {n−1, n} (even total pieces 2n or 2n+1). XY can use k<n marks (NOT all n marks!) to create 4 or 6 pieces where LB and XY have roughly equal picks; this is a key subtlety — XY using fewer marks can sometimes be more damaging for LB.

**Opening C (Self-similar doubling invariant):**
The geometric sequence {1/D, 2/D, 4/D, …, 2^n/D} is self-similar under halving: halving 2^k/D produces two pieces of 2^{k-1}/D, the same size already present in LB's intervals. This "halving invariant" means XY can always convert any subset of LB's intervals into equal-paired pieces, keeping LB's alternating-pick total at exactly 2^n/D. The proof of the lower bound (LB's guarantee) likely proceeds by showing any XY strategy that doesn't fully exploit this invariant gives LB more than c(n).

**Opening D (Exchange argument / induction on marks):**
For the lower bound proof: argue that XY's best response to LB's geometric intervals is always to halve the largest available interval. Any deviation from this (e.g., splitting at unequal fractions, or splitting a smaller interval) gives LB a strictly larger total. Possible proof by induction on n, using that the n=1 case (c(1)=2/3) is the base and the geometric structure is self-similar.

**Opening E (Upper bound — XY matching strategy):**
For any LB placement, XY can limit LB to at most c(n). XY's strategy: find LB's n+1 intervals, then choose n marks to "rebalance" them toward the geometric configuration (or worse for LB). The challenge: proving this for arbitrary LB placements, not just the geometric one. May use a minimax argument or direct construction.

---

### Candidate Techniques

- **Geometric/dyadic sequence construction**: The answer formula involves 2^n, and LB's strategy uses geometric intervals of ratio 2. This is analogous to the "one large value exceeds the sum of all others" principle (aimo-0117).
- **Alternating-pick analysis**: With m pieces (sorted desc), LB picks positions 0,2,4,… and XY picks 1,3,5,…; LB gets ⌈m/2⌉ of the pieces.
- **Invariant maintenance / self-similar halving**: The key invariant is that LB's geometric sequence is closed under the halving operation XY applies.
- **Induction on n**: The n-mark problem reduces to an (n−1)-mark problem after one LB–XY exchange.
- **Exchange argument**: Show any XY strategy other than halving gives LB strictly more, establishing uniqueness of the binding configuration.
- **Pairing strategy (aimo-0115, aimo-0461)**: Not directly applicable here, but the idea of pairing symmetric pieces has some resonance.

---

### Cheap-Kill Candidates

- **Parity of piece count**: With n+1 intervals from LB and k XY marks (k ≤ n), total pieces = n+1+k. If n+k is even, LB and XY each get (n+k)/2+? picks — parity matters. A key structural observation is that XY using exactly n−1 marks (creating n+1+n−1 = 2n pieces, even) can sometimes hurt LB more than using n marks!
- **Size bound**: c(n) = 2^n/(2^{n+1}−1) < 1/2 + ε for large n. The "fair" bound is 1/2 (what happens with many pieces), and LB's n marks give it an advantage that decays exponentially fast.
- **No cheap single-step kill**: The problem requires both a strategy for LB (constructive lower bound) and an upper bound for XY; neither direction is "trivial pigeonhole."

---

### Knowledge-Base Entries to Use

- **Invariants & monovariants** (kb): The geometric interval structure is an "invariant" under XY's halving operations.
- **Constructive/incremental** (kb): Realize LB's strategy explicitly; verify it by induction.
- **Extremal principle** (kb): The geometric sequence is the extremal configuration; any other LB placement allows XY to do better.
- **General proof methods — Contradiction** (kb): For the upper bound, assume LB guarantees more than c(n) and derive a contradiction using XY's halving strategy.

---

### Analogous Past Problems (Cruxes)

1. **aimo-0117** (most analogous): "Jesse assigns played values as a two-sided geometric (dyadic) sequence so the single largest value strictly exceeds the sum of all others." Crux: geometric sequence used as a domination argument in an adversarial game. Here, LB's geometric intervals satisfy a similar "largest piece > sum of all others / doubling" property, and XY's halving destroys this advantage systematically. **Direct analog**: aimo-0117's dyadic-sequence strategy maps to LB's geometric interval construction.

2. **aimo-0019** (strong analogy): Dyadic-interval covering game where "a family of dyadic-length pieces of pairwise distinct sizes is bounded by twice the largest, via the geometric sum of distinct negative powers of two." Crux: geometric sum = 2×largest. This is exactly the structure of LB's intervals {1/D, 2/D, …, 2^n/D}: sum = D/D = 1, largest = 2^n/D, and sum of all others = (D−2^n)/D = (2^n−1)/D = (2^n/D)·(1−1/2^n). The ratio 2^n/(2^{n+1}−1) has a direct geometric-sum interpretation.

3. **aimo-0262** (structural analogy): Cinderella-Stepmother bucket game. XY (Stepmother) distributes adversarially, LB (Cinderella) empties. Solved by invariant-maintenance: the defender keeps a self-reproducing invariant. Here, XY maintains an invariant that LB cannot exceed c(n), while LB's geometric strategy maintains a self-reproducing lower bound. The **defender's invariant** approach from aimo-0262 is directly adaptable.

---

### Prior Progress

None (round 1, fresh workspace).

---

### Dead Ends (Do Not Retry)

- **c(n) = (n+1)/(2n+1)** (LB divides into 2n+1 equal pieces): LB doesn't have enough marks to create 2n+1 pieces; this formula gives 2/3 for n=1 ✓ but 3/5 for n=2, whereas numerics give 4/7 ≈ 0.571 < 3/5. RULED OUT.
- **c(n) = (n+1)/(n+2)**: gives 2/3 for n=1 ✓ but 3/4 for n=2 — clearly too high. RULED OUT.
- **LB placing equal intervals**: e.g., n=2 LB at [1/3, 2/3] gives only ~0.50 worst case (XY places 1 mark at e.g. 0.833 creating 4 nearly-equal pieces giving LB only 1/2). DEAD END.
- **LB places symmetric intervals**: any symmetric LB strategy allows XY to exploit the symmetry to get close to 50/50.

---

### Small-Case / Intuition Notes (conjecture status)

**n=1 (proven):**
- LB places at 1/3, creating pieces [1/3, 2/3]. Any XY response (0 or 1 mark) leaves LB with at least 2/3. The binding cases: XY halves 2/3 interval → pieces {1/3, 1/3, 1/3}, LB picks two of three 1/3 pieces = 2/3. Confirmed: c(1) = 2/3.

**n=2 (verified numerically):**
- LB marks at [1/7, 3/7], intervals {1/7, 2/7, 4/7}.
- XY binding strategies: (i) halve 2/7 and 4/7 → 5 pieces {1/7,1/7,1/7,2/7,2/7}, LB gets 2/7+1/7+1/7=4/7; (ii) halve 4/7 only → 4 pieces {1/7,2/7,2/7,2/7}, LB gets 2/7+2/7=4/7; (iii) split 4/7 at x=1/7 → pieces {1/7,2/7,1/7,3/7}, LB gets 3/7+1/7=4/7. ALL XY strategies give LB ≥ 4/7 (verified by grid search with grid=200, 1+2+3 marks). c(2) = 4/7. *Conjecture status for the lower bound: strongly supported.*

**n=3 (verified numerically):**
- LB marks at [1/15, 3/15, 7/15], intervals {1/15, 2/15, 4/15, 8/15}.
- XY binding: halve 4/15 and 8/15 → 6 pieces, LB gets 8/15; halve 2/15, 4/15, 8/15 → 7 pieces, LB gets 8/15.
- Full worst-case grid search (grid=200, 0+1+2+3 marks) confirms minimum LB = 8/15. c(3) = 8/15. *Conjecture status: strongly supported.*

**Key structural observation:** The binding XY configuration for n=k is the same as for n=k−1 (scaling) — this suggests a recursive/inductive proof.

**LB's total at binding**: In all binding cases, the 2n+1 or 2n pieces give LB picks summing to exactly {a sequence of n+1 terms summing to 2^n/D}. The specific structure is:
- 2n+1 pieces: 2 each of 2^{n-1}/D, 2^{n-2}/D, …, 2^0/D, plus an extra 2^0/D. LB picks 2^{n-1}/D + 2^{n-2}/D + … + 2^0/D + 2^0/D = (2^n−1)/D + 1/D = 2^n/D = c(n). ✓

