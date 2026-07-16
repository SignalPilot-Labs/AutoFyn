## imo-2026-03 (Structure / Game Theory Lens)

### Answer (Conjecture, strongly supported numerically)

**c(n) = 2^n / (2^{n+1} - 1)**

Equivalently: c(n) = 1/(2 - 2^{-n}). As n → ∞, c(n) → 1/2.

Verified: c(1) = 2/3 (analytic), c(2) = 4/7 (numerical to 6 dp), c(3) = 8/15 (numerical, 2 and 3 XY-cut worst cases both hit 8/15 exactly).

---

### Small-case evidence

**n=1**: LB cuts at 1/3; any XY cut on the 2/3 piece gives pieces [alpha, 2/3-alpha, 1/3]; greedy LB always gets (alpha) + (2/3-alpha) = 2/3. XY cutting the small 1/3 piece gives LB even more. LB guarantee = 2/3 = c(1). (Label: proved by exhaustive case analysis on where XY cuts.)

**n=2**: LB cuts at 1/7 and 3/7, creating pieces [4/7, 2/7, 1/7]. Exhaustive numerical check (1000-point grid for 1 XY cut; 200×200 grid for 2 XY cuts): worst LB = 4/7 exactly. Every other LB placement (e.g. [0.1, 0.5] or [1/4, 1/2]) allows XY to reduce LB to ~0.5. Label: strong numerical conjecture that c(2) = 4/7.

**n=3**: LB cuts at 1/15, 3/15, 7/15, pieces [8/15, 4/15, 2/15, 1/15]. Worst-case over 3 XY cuts (grid search): LB = 8/15 = c(3).

---

### LB's optimal strategy (Geometric Piece Strategy)

LB uses all n cuts to create n+1 pieces in geometric ratio 1 : 2 : 4 : ... : 2^n.

Specifically, LB places cuts at positions (2^k - 1)/(2^{n+1} - 1) for k = 1, ..., n, creating pieces:
  P_k = 2^{k-1}/(2^{n+1} - 1), k = 1, ..., n+1.

The largest piece P_{n+1} = 2^n/(2^{n+1}-1) = c(n).
The sum of all other pieces = (2^n - 1)/(2^{n+1} - 1) = c(n) - 1/(2^{n+1}-1) < c(n).

**Key algebraic identity**: P_{n+1} = P_1 + P_2 + ... + P_n + P_1 (largest = sum of rest + smallest).
Equivalently: P_{n+1} > sum of rest. This means LB's largest piece ALWAYS beats any surviving piece when XY cannot create anything larger.

---

### XY's optimal response to the Geometric Strategy

XY uses all n cuts on the largest LB piece (P_{n+1} = c(n)), splitting it into:
  Q_i = 2^{n-i}/(2^{n+1}-1), i = 1, ..., n, and Q_{n+1} = 1/(2^{n+1}-1).

This creates a REPLICA of LB's smaller pieces {P_1,...,P_n} plus one extra copy of P_1.

Total 2n+1 pieces, sorted descending: [P_n, P_n, P_{n-1}, P_{n-1}, ..., P_1, P_1, P_1].

LB picks odd-indexed (1st, 3rd, ..., 2n+1-th):
P_n + P_{n-1} + ... + P_1 + P_1 = (2^{n-1} + 2^{n-2} + ... + 1 + 1)/(2^{n+1}-1) = 2^n/(2^{n+1}-1) = c(n).

**XY achieves exactly c(n): this is XY's best response (anything else gives LB more).**

---

### Why LB's Geometric Strategy is robust (Lower Bound argument sketch)

Given geometric pieces and ANY XY placement of m ≤ n cuts, LB gets ≥ c(n). Two cases:

**Case 1: XY does not cut the largest piece P_{n+1} at all.**
Then P_{n+1} remains intact. Since P_{n+1} > sum of all other pieces (before or after XY's cuts, because XY can only shrink existing pieces, not create new large pieces), P_{n+1} is the unique largest piece in the final multiset. LB takes it first, getting at least c(n) = P_{n+1}. Done.

**Case 2: XY uses k ≤ n cuts on the largest piece (and n-k cuts elsewhere).**
The largest piece is split into k+1 sub-pieces summing to c(n). The remaining n-k cuts hit smaller pieces (P_1,...,P_n), only shrinking them.

Sub-claim: LB gets at least sum of sub-pieces of P_{n+1} = c(n).
Reason: In the sorted order of all pieces, the n smaller LB pieces (or their sub-pieces) compete for even positions. When a small LB piece "displaces" a sub-piece of P_{n+1} to a lower odd position, LB compensates: if the small piece p occupies position j (odd) and sub-piece q is pushed to position j+1 (even), then LB trades q for p + (next piece). The net effect on LB is ≥ 0 due to the dominance property.

Analytic check for n=2 (XY cuts both in I_3 = largest interval, all sub-pieces < 2/7): 
- 5 pieces {q1,q2,q3,2/7,1/7}, q1+q2+q3=4/7, all q_i < 2/7.
- 2/7 lands at position 1 (it's the max). LB gets 2/7 + q_mid + q_min = 2/7 + (4/7 - q_max) ≥ 2/7 + (4/7 - 2/7) = 4/7. (Since q_max < 2/7.)
- Verified computationally: minimum is exactly 4/7.

The general induction uses the SELF-SIMILAR structure: removing the largest piece and rescaling gives the same problem for n-1.

---

### Upper Bound argument sketch (XY's strategy against arbitrary LB)

For any LB placement creating k ≤ n+1 pieces with sizes P_1 ≥ ... ≥ P_k:

**XY's strategy**: Use all n cuts on the largest piece P_1.

After XY's n cuts on P_1, total 2n+1 pieces. In the greedy game, LB picks odd-indexed.

Claim: LB's total ≤ c(n) when XY optimally splits P_1.

XY splits P_1 into n+1 pieces Q_1 ≥ ... ≥ Q_{n+1}. XY wants to minimize LB's gain.

Sub-claim: XY can always achieve LB ≤ c(n) by choosing the split of P_1 to mimic the geometric sub-structure. Key: XY creates Q_i = P_i·(P_1/sum(P)) scaled to sum to P_1, which puts all of P_2,...,P_k at even positions.

**Numerical confirmation**: For n=2, no LB placement outperforms geometric:
- LB at [0.1, 0.5]: XY holds to 0.501 < 4/7.
- LB at [0.25, 0.75]: XY holds to 0.503 < 4/7.
- LB at [1/7, 3/7] (geometric): XY holds to exactly 4/7 (best LB can do).

The geometric strategy is the unique LB optimum.

---

### Distinct strategic openings for the Outliner

**Opening 1 (Geometric Lower Bound)**: Prove that with geometric pieces [1,2,...,2^n]/(2^{n+1}-1), LB guarantees exactly c(n). Key step: induction on n using the self-similar structure. Base n=1 by direct case analysis. Inductive step: "Case 1 vs Case 2" dichotomy (XY cuts largest vs doesn't).

**Opening 2 (Upper Bound via XY's Concentration Strategy)**: For any LB placement, XY concentrates all n marks on LB's largest piece and creates a "replica" sub-structure, capping LB at c(n). Key: show this is well-defined regardless of LB's choice.

**Opening 3 (Invariant / Potential approach)**: Define a potential Φ on piece multisets. Show Φ ≥ c(n) is preserved under any XY cut when LB uses the geometric strategy. Likely candidate: Φ = LB's greedy gain from the multiset. Show Φ is non-decreasing in some ordering of XY cuts.

**Opening 4 (Minimax / LP duality)**: Frame as a zero-sum game. LB's optimal strategy and XY's optimal strategy form a saddle point at value c(n). The dual formulation: XY's minimax and LB's maximin coincide (von Neumann minimax).

**Opening 5 (Exchange argument for upper bound)**: Show that for any LB placement NOT equal to geometric, there exists a nearby placement with strictly higher guarantee. This pins geometric as the unique optimum. Likely proves upper bound without needing to construct XY's full strategy.

---

### Key structural properties (for the proof)

1. **Self-similarity**: Pieces [1,2,...,2^n]/(2^{n+1}-1) restricted to the n smallest form a rescaled copy of the n=n-1 problem. The induction telescopes.

2. **Dominance**: P_{n+1} = c(n) > sum(P_1,...,P_n) = 1-c(n). So P_{n+1} > 1/2; it's the unique "majority piece." No XY cut creates a piece larger than P_{n+1}.

3. **Replica property**: XY's optimal split of P_{n+1} using n cuts creates exactly a rescaled copy of {P_1,...,P_n} plus an extra P_1. The 2n+1 sorted pieces form n pairs plus one extra, and LB gets the "odd half" = sum of one element from each pair = c(n).

4. **"Parity trap"**: XY's n cuts on P_{n+1} create n+1 sub-pieces. Total pieces = 2n+1 (odd). LB makes n+1 picks; XY makes n. LB has one extra pick - but it's the smallest piece (P_1 = 1/(2^{n+1}-1)), keeping LB's advantage at minimum = P_1 = 1/(2^{n+1}-1) = 2c(n)-1.

5. **LB-XY gap**: LB_total - XY_total = 2c(n)-1 = 1/(2^{n+1}-1) at the optimum. This equals P_1 (the smallest piece). The smallest piece is the "margin."

---

### Cheap-kill candidates

- **Parity check**: Total pieces with both using all marks = 2n+1 (odd). LB picks n+1, XY picks n. If all pieces equal: LB gets (n+1)/(2n+1) > 1/2. But XY can make pieces unequal to reduce LB. The parity analysis shows LB's "one-extra-pick" advantage is the minimal piece.
- **Size bound**: c(n) > 1/2 for all finite n (approaches 1/2 from above). LB always gets more than half. XY cannot flip to < 1/2 with any strategy.
- **Monotonicity**: c(n) is strictly decreasing in n (each additional mark helps XY cut more). As n→∞, c(n)→1/2.

---

### Candidate techniques (Knowledge base)

- **Invariants & monovariants** (Combinatorics section): Need an invariant showing LB's greedy gain ≥ c(n) under any XY cut.
- **Constructive / incremental** (Combinatorics): LB's geometric construction is explicit and verifiable.
- **Pigeonhole / extremal** (Combinatorics): Key step in upper bound — XY concentrates on largest piece.
- **Direct proof + induction** (General Proof Methods): Induction on n using self-similar structure.

---

### Analogous past problems (cruxes)

Not yet checked in the crux corpus. The problem resembles:
- Fair division / cake-cutting literature with strategic cuts.
- "Maker-Breaker" games where one player sets up structure, the other disrupts.
- Binary / geometric halving problems (Sprague-Grundy type).

The geometric halving structure (ratio 2) and the minimax at c(n) = 2^n/(2^{n+1}-1) resemble binary search trees / Fibonacci/geometric series competition problems. Check crux corpus for combinatorics/game subtopics.

---

### Prior progress

None (round 1 produced nothing). No approaches, no lemmas registered.

### Dead ends (do not retry)

- Equal-pieces LB strategy (1/3, 1/3, 1/3 for n=2): XY uses both cuts on one piece, creating 5 pieces with LB getting only 1/2. Verified bad.
- LB using fewer than n marks: wastes strategic advantage; XY can hold to ~1/2.
- Halving/bisection-equal LB strategy (1/4, 1/2, 3/4 type): XY holds LB to ~1/2.

### Small-case / intuition notes (labeled conjectures)

**Conjecture A**: c(n) = 2^n/(2^{n+1}-1) for all positive integers n.
**Conjecture B**: LB's unique optimal strategy is the geometric piece strategy (up to reflection of the stick).
**Conjecture C**: XY's unique optimal response to geometric pieces is to concentrate all n cuts on the largest piece, replicating the sub-structure.
**Conjecture D**: The key invariant is: with the geometric strategy, XY cutting any non-largest piece strictly INCREASES LB's gain (so XY's only rational choice is to cut the largest).
