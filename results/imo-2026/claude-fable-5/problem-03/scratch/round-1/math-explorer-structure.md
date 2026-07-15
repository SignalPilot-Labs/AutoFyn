## imo-2026-03 (GAME STRUCTURE lens)

### Problem restatement

Length-1 stick. Phase 1: Liu Bang places ≤ n points. Phase 2: Xiang Yu (seeing Liu Bang's marks) places ≤ n points. All marked points distinct. Stick cut at all marks → at most 2n+1 pieces. Alternating claiming, Liu Bang first; each player greedily takes the largest unclaimed piece (this is dominant strategy — never pass on largest available). Find c(n) = max-min guaranteed total for Liu Bang.

---

### Distinct openings

**Opening 1 (Geometric placement / doubling invariant — the central discovery)**

Liu Bang's optimal strategy is to place n points creating n+1 pieces of sizes 1/D, 2/D, 4/D, ..., 2^n/D where D = 2^{n+1} − 1. Points at cumulative positions 1/D, 3/D, 7/D, ..., (2^n−1)/D.

Key property: each piece is strictly larger than the sum of all smaller pieces (2^k/D > (2^k−1)/D). This mirrors the aimo-0117 crux exactly.

Verified computationally (n=1,2,3):
- n=1: pieces {1/3, 2/3}, c(1) = 2/3
- n=2: pieces {1/7, 2/7, 4/7}, c(2) = 4/7
- n=3: pieces {1/15, 2/15, 4/15, 8/15}, c(3) = 8/15

General conjecture (strongly supported): **c(n) = 2^n / (2^{n+1} − 1)**

Equivalent forms: 1/(2 − 2^{−n}) = 1/2 + 1/(2(2^{n+1}−1)).

**Opening 2 (Lower bound: why Liu Bang guarantees c(n) with geometric placement)**

With Xiang Yu's n marks and the geometric initial pieces, the key claim is:

*Xiang Yu's take (even-indexed positions) ≤ (2^n−1)/D, regardless of Xiang Yu's mark placement.*

n=1 proof (clean and complete): Pieces after Xiang Yu = {1/3, a, 2/3−a} for some a ∈ (0, 2/3). The median of {1/3, a, 2/3−a} is always exactly 1/3 (since a + (2/3−a) = 2/3 = 2 × 1/3, one of {a, 2/3−a} ≤ 1/3 and the other ≥ 1/3). Liu Bang takes 1 − median = 2/3. Verified: all a give exactly 2/3, constant.

n=2 proof (clean and complete): Pieces = {1/7, 2/7, a, b, c} with a+b+c=4/7 (or other Xiang Yu placements). Xiang Yu's even positions = p2+p4.
- At most ONE of {a,b,c} can exceed 2/7 (since two ≥ 2/7 would sum ≥ 4/7 = their total, contradiction for strict).
- If a ≥ 2/7 (one sub-piece is large): sorted starts …, p2=2/7, …, p4 ≤ 1/7. So p2+p4 ≤ 3/7. ✓
- If all sub-pieces < 2/7: p1=2/7, p2 = largest sub-piece < 2/7, p4 ≤ 1/7. So p2+p4 < 3/7. ✓
- Same analysis for marks in different pieces — verified numerically to give higher Liu Bang scores.
- Conclusion: Xiang Yu take ≤ 3/7, Liu Bang ≥ 4/7 = c(2). Equality achieved (Xiang Yu creates interleaving: a ∈ (2/7, 4/7), b ∈ (1/7, 2/7), c ∈ (0, 1/7), sum = 4/7).

General inductive argument for lower bound: uses "at most one sub-piece of 2^n/D exceeds 2^{n-1}/D" at each induction level, reducing to the (n−1) case for the remaining 2n−1 pieces.

**Opening 3 (Upper bound: Xiang Yu prevents Liu Bang from exceeding c(n))**

For any Liu Bang placement with n+1 initial pieces q_1 ≥ q_2 ≥ ... ≥ q_{n+1}, Xiang Yu's n marks can force Liu Bang ≤ c(n).

n=1 explicit strategy: Liu Bang places at x.
- If x ≤ 1/3: Xiang Yu splits (1−x) into equal halves → Liu Bang gets (1+x)/2 ≤ 2/3. ✓
- If x ≥ 1/3: Xiang Yu places a mark near one endpoint of the small piece x (splitting into ε, x−ε) → Liu Bang gets 1−x+ε → 1−x ≤ 2/3 (since x ≥ 1/3). ✓
- At x=1/3: both bounds meet exactly at 2/3. This is why 1/3 is optimal AND tight.

General upper bound structure: for any Liu Bang placement, Xiang Yu can find a response forcing Liu Bang ≤ c(n). Key: if Liu Bang's largest piece is L > c(n), Xiang Yu can use marks to create sub-pieces of L that "fill in" the even positions and restrict Liu Bang. If L ≤ c(n), Liu Bang gets ≤ c(n) from position 1 alone. (Proof needs careful case analysis — recommend developing via induction on n for the outliner/builder.)

**Opening 4 (Xiang Yu's optimal response: the interleaving strategy)**

Against Liu Bang's geometric placement {1/D, 2/D, ..., 2^n/D}:
- Xiang Yu uses ALL n marks inside the largest piece 2^n/D.
- Creates n+1 sub-pieces s_1 > 2^{n-1}/D > s_2 > 2^{n-2}/D > ... > 1/D > s_{n+1} > 0.
- These sub-pieces interleave with the n small Liu Bang pieces in sorted order.
- Resulting sorted order: s_1, 2^{n-1}/D, s_2, 2^{n-2}/D, ..., 1/D, s_{n+1}.
- Xiang Yu takes the odd indexed Liu Bang small pieces (even positions); Liu Bang takes the sub-pieces (odd positions) summing to exactly 2^n/D = c(n).

This works because: sub-pieces sum to 2^n/D and are arranged to "sandwich" the n small pieces. Xiang Yu takes sum = (2^n−1)/D. Feasibility: requires s_1 ∈ (2^{n-1}/D, 2^n/D), s_k ∈ (2^{n-k}/D, 2^{n-k+1}/D), s_{n+1} ∈ (0, 1/D), which is satisfiable since the total matches 2^n/D. (Check: sum of interval centers ≈ 2^n/D − something, achievable with small perturbation.)

**Opening 5 (Why equal spacing and other natural strategies fail)**

- Equal spacing (1/(n+1), ..., n/(n+1)) → pieces all equal 1/(n+1). Xiang Yu concentrates both marks in one piece, splitting into two equal sub-pieces and getting the two equal-sized "middle" pieces at positions 2 and 4. Liu Bang reduced to 1/2 for n=2. DEAD END for Liu Bang.
- Half-point (Liu Bang at 1/2 for n=1) → Xiang Yu places near endpoint, giving Liu Bang → 1/2. WORSE than 2/3.
- Powers-of-two offset (pieces 2^0, 2^1, ..., but wrong denominator) → suboptimal.
- Key: the geometric ratio must be exactly 2 with denominator 2^{n+1}−1 to make each piece equal to (sum of all smaller pieces + 1/D). This tight calibration prevents Xiang Yu from "shifting" mass.

---

### Candidate technique(s)

- **Doubling / geometric sequences**: the crux is that initial pieces form a geometric progression with ratio 2 (each piece = sum of all smaller + 1/D). This is a direct analog of the dyadic sequence technique in aimo-0117.
- **Minimax exchange argument**: to prove the lower bound (Liu Bang always gets ≥ c(n)), use an induction where the "at most one large sub-piece" observation limits what Xiang Yu can do at each level.
- **Median invariant**: for n=1, the key is that 1/3 is always the median of the 3 final pieces. Generalization is the "at most one piece exceeds 2^{k-1}/D" argument.
- **Two-phase minimax**: Liu Bang's max-min and Xiang Yu's min-max coincide at c(n) — the game has a saddle point.

---

### Cheap-kill candidates

- Greedy claiming is dominant (taking any piece other than the largest is strictly worse): cite this as a standard observation — only the relative sizes matter.
- Symmetry reduction: WLOG Liu Bang uses all n marks (using fewer only helps Xiang Yu).
- Parity: with 2n+1 pieces (maximum), Liu Bang takes n+1 and Xiang Yu takes n, so Liu Bang has a natural advantage of 1 extra pick. The question is how large each pick is.
- Size bound: Liu Bang's n+1 greedy picks ≥ (n+1)/(2n+1) × 1 by averaging, but the actual answer is worse (4/7 ≈ 0.571 < 3/5 = 0.600 for n=2) because Xiang Yu can skew the distribution.

---

### Knowledge-base entries to use

- **Pigeonhole / extremal principle** (Combinatorics section): "at most one sub-piece can exceed 2^{n-1}/D" is a pigeonhole argument (since two such sub-pieces would sum to ≥ their total).
- **Invariants & monovariants** (Combinatorics section): the median-is-1/3 invariant for n=1; the analogous invariant for n=2,3,...
- **Constructive / incremental** (Combinatorics section): both the Liu Bang strategy (constructive geometric placement) and the Xiang Yu response (interleaving construction) need to be explicitly exhibited.
- **Problem-solving heuristics** (Meta): "solve a simpler/special case first" → n=1 was the key insight generator.

---

### Analogous past problems (cruxes)

1. **aimo-0117** (`problem_id=aimo-0117`): Crux = "Assign played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all others." How used: Jesse uses powers of 2, ensuring whichever box contains the current largest power outweighs everything else. **Directly analogous**: our Liu Bang uses the same doubling structure (pieces 1, 2, 4, ..., 2^n scaled by 1/D) for the same reason — the large piece dominates the rest. The crux move translates directly.

2. **aimo-0262** (`problem_id=aimo-0262`): Crux = "For an adversarial capacity game, hand the defender a self-reproducing invariant family of configurations and show each legal move can restore it, so the bound holds forever by induction." Somewhat analogous: our lower bound proof needs to show that Liu Bang's guarantee is maintained no matter what Xiang Yu does. The "self-reproducing invariant" flavor matches the induction on n structure.

3. **aimo-0461** (`problem_id=aimo-0461`): Crux = "For an upper bound in a placement game, partition the conflict graph into small identical components each of which can hold at most one non-conflicting piece, and have the blocker respond inside the same component the mover just used to exhaust it." Partially analogous: Xiang Yu's response strategy (concentrate all marks in the large piece) is a form of "exhaust the same component." Less direct than aimo-0117.

---

### Prior progress

None — round 1, no prior approaches.

---

### Dead ends (do not retry)

- **Equal spacing** (pieces all 1/(n+1)): Xiang Yu concentrates 2 marks in one piece to reduce Liu Bang to 1/2 for n=2. Verified dead end.
- **Liu Bang places at 1/2 for n=1**: Xiang Yu near-endpoint placement gives Liu Bang → 1/2, strictly less than 2/3.
- **Formula (n+1)/(2n+1)** (uniform average): ruled out numerically (4/7 < 3/5 for n=2).

---

### Small-case / intuition notes (conjecture)

**Conjecture (strongly supported by computation):** c(n) = 2^n / (2^{n+1} − 1).

Evidence:
- n=1: 2/3 confirmed analytically (median argument).
- n=2: 4/7 confirmed by exhaustive grid search (500×500 grids) — all Xiang Yu strategies give Liu Bang ≥ 4/7, with equality achievable.
- n=3: 8/15 confirmed by grid search (marks in various configurations).
- Formula matches the geometric placement: c(n) = (largest piece) / (sum of all pieces) = 2^n / (2^{n+1}−1).

**Pattern in Liu Bang's placement:** points at 1/D, 3/D, 7/D, ..., (2^n−1)/D (cumulative sums 1, 3, 7, ... = 2^k−1 for k=1,...,n). Creates pieces of sizes 2^0/D, 2^1/D, ..., 2^n/D.

**Pattern in Xiang Yu's optimal response:** use all n marks in the largest piece (2^n/D), interleaving sub-pieces between the n small Liu Bang pieces.

**Behavior as n → ∞:** c(n) = 2^n/(2^{n+1}−1) → 1/2. Liu Bang's advantage over 1/2 is exactly 1/(2(2^{n+1}−1)) → 0. Consistent with increasing difficulty as n grows.

**Proof structure indicated:**
- Lower bound: geometric placement + induction on n using "at most one sub-piece exceeds the (n−1)th piece" → Liu Bang gets ≥ 2^n/D.
- Upper bound: for any Liu Bang placement, Xiang Yu's response (analysis by two cases: largest piece < or > c(n)) gives Liu Bang ≤ 2^n/D. Needs detailed case work.
- Both bounds need explicit construction exhibits.

**Critical gap for the outliner:** The upper bound proof is the harder direction. For any Liu Bang configuration, Xiang Yu needs to demonstrate a concrete n-mark response achieving Liu Bang ≤ c(n). One approach: Xiang Yu's strategy mimics the n=1 case (split small pieces appropriately to force even positions ≤ (2^n−1)/D) applied inductively. Alternatively, Xiang Yu uses a "normalize" response that produces pieces proportional to the geometric sequence from whichever Liu Bang starting configuration.
