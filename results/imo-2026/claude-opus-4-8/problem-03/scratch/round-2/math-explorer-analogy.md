## imo-2026-03

### ANSWER CONJECTURE (strongly supported by computation for n=1,2,3,4)

**c(n) = 2^n / (2^{n+1} - 1)**

Values:
- c(1) = 2/3
- c(2) = 4/7
- c(3) = 8/15
- c(4) = 16/31
- c(n) → 1/2 as n → ∞

---

### Small-case / intuition notes (labeled as computation, not proof)

**Claiming phase is greedy**: Both players maximize their own total, so the optimal strategy for each is to always claim the LARGEST remaining piece. Thus the claiming phase is deterministic: sort pieces in decreasing order p_1 ≥ p_2 ≥ ... ≥ p_k; Liu Bang takes p_1, p_3, p_5, ...; Xiang Yu takes p_2, p_4, .... Liu Bang's share = 1 - (p_2 + p_4 + ...). Verified by exchange argument.

**n=1 exact computation (proved)**:
- LB marks at x=1/3. Creates pieces {1/3, 2/3}.
- XY adds any point y ∈ (1/3, 1): pieces {1/3, t, 2/3-t} for t=y-1/3. The piece 1/3 is ALWAYS the median of the 3 pieces (since t < 1/3 makes 1/3 the middle, and t > 1/3 makes 1/3 the middle). LB gets 1 - 1/3 = 2/3. If XY places in the (1/3) piece: LB gets even more. Guarantee = 2/3 exactly.
- For x ≠ 1/3: XY can limit LB to < 2/3 (verified computationally and analytically). For x > 1/3, XY marks in small piece near 0, limiting LB to ≈ (1+x)/2 or less.

**n=2 key finding (computational)**:
- LB at {1/7, 3/7} achieves guarantee 4/7 = 0.5714.
- Pieces: {1/7, 2/7, 4/7} — geometric ratio 1:2:4.
- XY's tightest response: split 4/7 into two 2/7 pieces (1 mark), split 2/7 into two 1/7 pieces (1 mark). Result: {2/7, 2/7, 1/7, 1/7, 1/7}. LB takes 2/7+1/7+1/7 = 4/7.
- Every other XY configuration gives LB ≥ 4/7.
- No symmetric strategy {a, 1-a} achieves guarantee > ~1/2 for n=2.
- Exhaustive grid search over all 2-mark LB strategies: maximum guarantee = 4/7, achieved uniquely by {1/7, 3/7} (and its reflection {4/7, 6/7}).

**n=3, n=4 computationally verified**: c(3) = 8/15, c(4) = 16/31, both matching 2^n/(2^{n+1}-1) exactly.

**XY's tight strategy (inductive structure)**:
- Start with LB's n+1 geometric pieces {1/D, 2/D, ..., 2^n/D} where D = 2^{n+1}-1.
- XY mark 1: split the biggest piece 2^n/D into {2^{n-1}/D, 2^{n-1}/D}.
- XY mark 2: split the second biggest (either the original 2^{n-1}/D or one of the new 2^{n-1}/D) into {2^{n-2}/D, 2^{n-2}/D}.
- ...
- After n XY marks: 2n+1 pieces with specific sorted order. LB gets exactly 2^n/D.

---

### LB's optimal strategy (geometric pieces)

LB marks at positions **(2^k - 1) / (2^{n+1} - 1)** for k = 1, 2, ..., n.

This creates n+1 pieces:
- Piece k has size **2^{k-1} / (2^{n+1}-1)** for k = 1, ..., n+1.
- Sizes: 1/D, 2/D, 4/D, ..., 2^n/D (geometric progression, ratio 2).

Key structural property:
- The largest piece 2^n/D exceeds the sum of all other pieces: 2^n/D > (2^n-1)/D.
- When XY halves the largest piece, LB's total is preserved at 2^n/D.
- When XY places a mark outside the largest piece, LB claims the intact 2^n/D immediately.

---

### Distinct openings for the proof

**Opening 1 (direct case analysis + induction)**:
Lower bound: Induction on n. For n=1, the fixed piece 1/3 is always the median regardless of where XY places the mark — proved by exhaustive case split on which side XY places. For n: LB's n+1 pieces have the "halving" property. After XY's n marks, prove by strong induction that LB's greedy share ≥ 2^n/D. Key: the largest LB piece is ≥ all other initial pieces combined. When XY inserts all marks into the largest piece, use a sub-case on whether any sub-piece exceeds 2^{n-1}/D.

Upper bound: Given any LB strategy (any n marks creating n+1 pieces), XY constructs a response limiting LB to ≤ 2^n/D. XY's strategy: find the "imbalanced split" in LB's piece set and exploit it. For any LB pieces P_1 ≤ ... ≤ P_{n+1}: XY uses n marks to halve P_{n+1}, then halve the largest remaining, etc.

**Opening 2 (potential / weight function)**:
Assign weight w(p) to each piece of size p in the sorted order. LB's share = Σ w over odd positions = Σ_{j odd} q_j. Show this is invariant or lower-bounded under XY's insertions using a potential. The geometric structure ensures a "balanced" potential.

**Opening 3 (pairing / averaging argument)**:
Pair pieces: (q_1, q_2), (q_3, q_4), ..., with q_{2n+1} unpaired. LB gets q_1 + q_3 + ... + q_{2n+1}. Note q_{2i-1} ≥ q_{2i} for all i, so LB gets ≥ XY's share. Then show LB's share ≥ 2^n/D by bounding XY's share ≤ sum of the n smaller original LB pieces = (2^n-1)/D. If XY can never "exceed" the smaller LB pieces in total... need careful argument.

**Opening 4 (self-similar / recursive structure)**:
The key insight: with geometric pieces {P, 2P, 4P, ..., 2^n P}, when XY halves the biggest piece, the resulting pieces still have the "each piece ≤ half the next" structure. This self-similarity means the game recurses on a smaller instance. Specifically:

After XY halves 2^n/D into {2^{n-1}/D, 2^{n-1}/D}:
New 5-piece set (for n=2): {1/7, 2/7, 2/7, 2/7, ...}... actually for n=2 XY uses both marks, and the resulting 5 pieces = {2/7, 2/7, 1/7, 1/7, 1/7}. LB takes 3 pieces summing to 4/7.

The recursion: LB gets P_n + LB's share in the residual game on n pieces with n-1 marks... perhaps? This needs formalizing.

**Opening 5 (upper bound via XY's response to any LB configuration)**:
For any LB piece configuration A_1 ≤ ... ≤ A_{n+1} with ΣA_i = 1:
XY uses n marks to create 2n+1 pieces s.t. LB gets ≤ max(A_i) ≤ 1. But this is too weak. Need: LB gets ≤ 2^n/(2^{n+1}-1). This requires showing that if LB deviates from the geometric strategy, XY can punish. The punishment: if A_n > 2A_{n-1} (too imbalanced), XY halves A_n to force LB below 2^n/D. If A_n ≤ 2A_{n-1}, LB can't "concentrate" enough in A_n to guarantee 2^n/D... this argument needs precision.

---

### Candidate techniques

- **Geometric doubling**: The "halving" structure of LB's strategy is the key invariant. The proof likely uses binary representations or the sum-of-geometric-series identity.
- **Greedy invariant**: Both the lower bound (LB's guarantee) and upper bound (XY's limit) can be phrased as greedy invariants.
- **Induction on n**: Both bounds have a natural inductive structure (from n-1 to n, using n/n-1 marks).
- **Extremal principle**: LB's optimal strategy is found by extremizing the minimax objective.

---

### Cheap-kill candidates

- **Parity / alternating claim**: LB takes positions 1, 3, 5, ... in sorted order — LB always gets > 1/2 (since they take more pieces). But this only gives > 1/2, not the tight bound. (LB always gets > 1/2 by this simple argument.)
- **Large piece dominance**: If LB creates any piece of size s > (2^n-1)/(2^{n+1}-1) = 1/2, XY cannot prevent LB from claiming it (it's strictly more than the sum of n other pieces). But the tight case has the big piece just barely more than the rest. For the LB lower bound, just noting "LB claims the big piece" gives LB ≥ 2^n/D immediately in the case XY doesn't split the big piece.

---

### Knowledge-base entries to use

- **Constructive vs. existence**: Must prove BOTH upper bound (XY strategy limiting LB) AND lower bound (LB strategy achieving 2^n/D). "For find all / largest n: prove an upper bound AND construct an example."
- **Invariants & monovariants**: The geometric piece structure is a monovariant/invariant under XY's optimal splitting.
- **Induction**: Both bounds should follow by induction on n, with the n=1 case as a clean base.
- **Pigeonhole / extremal principle**: Among XY's n marks, at most n-1 can go into pieces other than the big one; pigeonholing the marks into pieces.
- **Greedy exchange**: Optimality of greedy claiming is the key structural fact about the claiming phase.

---

### Analogous past problems (cruxes)

**Best match: aimo-0369** (card game where first player picks odd or even cards)
- Statement: 2n cards in a row; players alternately take from ends; first player maximizes sum. Crux: the first player can guarantee to take either all odd-indexed or all even-indexed cards (induction).
- Analogy to IMO 2026 P3: Both problems involve two phases (setup then claiming) where a player guarantees to claim a specific "slot pattern." The crux in 0369 (the first player can choose the parity class) is analogous to LB always taking the "odd" pieces in the sorted claiming phase. However, 0369 has a specific structure (take from ends) while our problem has free selection — less directly analogous.

**Second match: aimo-0019** (painting game on the real line, dyadic intervals)
- Statement: Player A controls ink supply, player B paints dyadic intervals; B wins by covering [0,1] before ink runs out. Crux: B responds to each A-move by jumping "just beyond the frontier," maintaining an invariant that ink spent ≤ 3× progress.
- Analogy: Involves real interval, adversarial game, and a dyadic/geometric invariant. The dyadic structure (intervals of length 1/2^m) parallels the geometric pieces in our problem. However, the game type is different (one player sets size, other sets location), so the crux move doesn't transfer directly.

**Third match: aimo-0596** (card game with XOR pairing)
- Statement: Card mirroring strategy in a combinatorial card game. Crux: respond to opponent's pick with involution-partner.
- Analogy: The "pairing" argument (pair each piece with another and let LB claim one from each pair) is a structural parallel, but the combinatorial context is quite different.

**Conclusion on crux corpus**: No past problem is directly analogous to the two-phase mark-then-claim game. The closest structural parallel is that "greedy first-mover advantage" problems have been solved via induction + explicit strategy construction (as in aimo-0369, aimo-0019). The specific geometric-piece construction for this problem appears novel.

---

### Prior progress

None — Round 1 had no approaches registered.

---

### Dead ends (do not retry)

- **Symmetric LB strategies {a, 1-a}**: For n=2, these give guarantee ≈ 1/2, far below c(2) = 4/7. XY marks one tiny piece and one at the midpoint of one large region to reduce to 4 pieces with LB getting ~1/2.
- **Equal-piece LB strategies**: LB marking at {1/3, 2/3} (equal thirds) gives only ~1/2 guarantee for n=2, because XY can place two marks near 1/2 to split the middle third into tiny pieces and reduce LB to 1/2.
- **Single-mark LB for n=2**: LB using just 1 mark (even the optimal x=1/3) is limited to ~1/2 guarantee when XY has 2 marks (XY uses {1/6, 2/3} to give LB = 1/2). Always use all n marks.
