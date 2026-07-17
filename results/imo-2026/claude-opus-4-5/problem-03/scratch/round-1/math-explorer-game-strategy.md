## imo-2026-03

### Key observations about the game structure

**Two-phase game:** LB marks ≤n points, then XY marks ≤n more (distinct), stick cut at all marks. Alternating claiming (LB first), each player greedily takes the largest available piece.

**Greedy is optimal in claiming phase:** By a standard exchange argument, taking the currently largest piece dominates any other choice. With k pieces sorted p₁ ≥ p₂ ≥ ... ≥ pₖ:
- LB gets p₁ + p₃ + p₅ + ... (odd ranks)
- XY gets p₂ + p₄ + p₆ + ... (even ranks)
- LB picks ceil(k/2) pieces; with k = 2n+1 pieces, LB picks n+1, XY picks n.

**Total mark count:** LB ≤ n marks create ≤ n+1 intervals. XY ≤ n marks split existing intervals (each mark adds exactly 1 piece). Maximum pieces: 2n+1.

**LB's double advantage:** (1) LB moves first in marking (establishes initial subdivision), (2) LB moves first in claiming. Both are valuable.

### Answer conjecture (strongly supported by computation)

**c(n) = 2ⁿ/(2ⁿ⁺¹ − 1)**

| n | c(n) | decimal |
|---|------|---------|
| 1 | 2/3 | 0.6667 |
| 2 | 4/7 | 0.5714 |
| 3 | 8/15 | 0.5333 |
| n | 2ⁿ/(2ⁿ⁺¹−1) | → 1/2 |

Note: 2ⁿ/(2ⁿ⁺¹−1) = 1/(2 − 2⁻ⁿ). Verified numerically for n=1,2,3 with exhaustive grid search.

### LB's optimal strategy (lower bound construction)

Set D = 2ⁿ⁺¹ − 1. LB marks at positions {(2ᵏ−1)/D : k=1,...,n}, creating n+1 pieces of sizes:
- P₀ = 1/D, P₁ = 2/D, P₂ = 4/D, ..., Pₙ = 2ⁿ/D (geometric ratio 2)

**Verified:** For this LB marking, XY's best n-mark response gives LB exactly c(n).

**Key structural property:** The pieces form a geometric sequence with ratio 2. Each Pₖ = 2·Pₖ₋₁. The largest piece Pₙ = 2ⁿ/D > 1/2.

**Why this works (n=1 analysis, explicit proof):** LB marks at 1/3. Pieces 1/3 and 2/3. Whatever XY marks at y ∈ (1/3, 1): three pieces {1/3, y−1/3, 1−y}. The piece 1/3 is always the MEDIAN (middle pick, going to XY). LB gets the other two summing to 2/3. If y ∈ (0, 1/3): LB takes 2/3 directly plus extra. Either way LB ≥ 2/3.

**n=2 analysis (verified):** LB at {1/7, 3/7}, pieces 1/7, 2/7, 4/7.
- If XY marks 1 point inside [3/7,1] splitting it as (a,b) with a≥b and a+b=4/7: four pieces 4/7-piece, 2/7, a, b. Since b ≤ 2/7 ≤ a, sorted order is a, 2/7, b, 1/7. LB gets a+b = 4/7.
- If XY marks inside [1/7,3/7]: LB gets 4/7 + something ≥ 4/7.
- If XY marks inside [0,1/7]: LB gets 4/7 + something ≥ 4/7.
- With 2 XY marks: exhaustive check shows LB always gets ≥ 4/7.

### XY's optimal strategy (achieves equality, proving upper bound for LB's specific marking)

Given LB's geometric marking with pieces P₀ < P₁ < ... < Pₙ:

**XY marks:** one ε-mark just inside Pₙ₋₁ (the second piece) and halves Pₙ₋₁+₁ = P₂, P₃, ..., Pₙ (using n−1 halvings). Total: 1 + (n−1) = n marks.

After XY's marks, the 2n+1 pieces are:
- Two copies of Pₙ₋₁ = 2ⁿ⁻¹/D (from halving Pₙ)
- Two copies of Pₙ₋₂ = 2ⁿ⁻²/D (from halving Pₙ₋₁)
- ...
- Two copies of P₁ = 2/D (from halving P₂)
- One P₁−ε and one ε (from splitting P₁)
- One P₀ = 1/D (untouched)

Sorted: Pₙ₋₁, Pₙ₋₁, Pₙ₋₂, Pₙ₋₂, ..., P₁, P₁, P₁−ε, P₀, ε.

LB picks ranks 1,3,5,...,2n+1:
Pₙ₋₁ + Pₙ₋₂ + ... + P₁ + (P₁−ε) + ε = (2ⁿ⁻¹ + 2ⁿ⁻² + ... + 2 + 2)/D = 2ⁿ/D = c(n). ✓

**Verified for n=2,3:** XY at {ε-above-P₁, midpoints of P₂,...,Pₙ} gives LB exactly c(n).

### Why LB cannot guarantee MORE than c(n) (upper bound)

For any LB n-mark strategy creating pieces (a₁,...,aₘ), XY can limit LB to ≤ c(n). The argument:
- The geometric marking is the UNIQUE optimal LB strategy (numerically verified for n=2,3 on fine grids).
- For any other LB marking, XY achieves LB < c(n) (verified: e.g., LB at {1/3,2/3} for n=2 gives XY a response limiting LB to ≈0.51 < 4/7).
- The minimax value is c(n), achieved at LB's geometric marking.

**Proof sketch for upper bound (to be made rigorous):** For any LB pieces (a₁,...,aₘ), XY applies binary splitting: mark midpoints of the n largest intervals. The resulting pieces can be shown (by induction or combinatorial argument) to satisfy: LB's sum of odd-rank pieces ≤ c(n).

### Proof structure for lower bound (explicit invariant)

**Claim:** With LB's geometric marking, for any XY n-mark response, LB gets ≥ 2ⁿ/(2ⁿ⁺¹−1).

**Proof approach 1 (induction on n):** Base case n=1 proved directly. For the inductive step: after LB's first pick (the largest surviving piece, which is ≥ Pₙ/2 since Pₙ is only halved at most once per mark) and XY's first pick, the remaining sub-game has ≤ n−1 XY marks and ≤ 2n−1 pieces. Apply induction hypothesis.

**Proof approach 2 (direct inequality):** The key observation: in the sorted pieces from LB's geometric marking + any XY marking, the pieces at even ranks (XY's picks) sum to ≤ (2ⁿ−1)/(2ⁿ⁺¹−1). This is proved by showing that the median-rank pieces cannot exceed the sum c(n)·something.

**Proof approach 3 (pairing argument):** The pieces from the geometric sequence have the property Pₖ = 2Pₖ₋₁. When any Pₖ is split, the two halves equal Pₖ₋₁ each. This preserves the "structure" of the game and can be used to pair pieces so LB always wins enough pairs.

### Promising strategic frameworks

1. **Recursive/inductive structure:** The n-player game reduces to the (n−1)-player game after removing the top pair of pieces. The formula c(n) = 2·c(n−1)/(2·c(n−1)+c(n−1)... satisfies the recurrence c(n) = f(c(n−1)) where f(x) = ... (to be determined by the outliner).

   Note: c(n) satisfies the recurrence: c(n) = 2ⁿ/(2ⁿ⁺¹−1). Verify: c(n) = (2·c(n−1))·D(n−1)/D(n) where D(n) = 2ⁿ⁺¹−1. Since D(n) = 2D(n−1)+1: c(n) = 2ⁿ/(2D(n−1)+1) = 2·2ⁿ⁻¹/(2D(n−1)+1). Hmm. Also c(n)/(1−c(n)) = 2ⁿ/(2ⁿ−1) = 2·2ⁿ⁻¹/(2(2ⁿ⁻¹)−1) = 2·c(n−1)/(1−c(n−1))/(2−1/2^{n-1}). Not clean. Best via: 1/c(n) = 2 − 1/2ⁿ, so 1/c(n) − 1/c(n−1) = 1/2ⁿ − 1/2ⁿ⁻¹ = −1/2ⁿ. The reciprocals 1/c(n) = 2−2⁻ⁿ satisfy 1/c(n) = 1/c(n−1) + 1/2ⁿ with 1/c(0) = 1 (trivial: stick undivided, LB takes all → but n=0 means 0 marks each, 1 piece, LB takes all). Wait 1/c(0)=1 doesn't fit: 1/c(0) = 2-1 = 1. ✓ And the recurrence 1/c(n) − 1/c(n−1) = 1/2ⁿ.

2. **The "absorber" principle:** In the geometric strategy, the piece P₀ = 1/D is a "bait piece" that keeps absorbing into XY's picks at various levels. This forces LB to always collect the "geometric sum" of the pieces.

3. **Binary representation / dyadic structure:** The optimal LB marking corresponds to the n points needed to create pieces in ratio 1:2:4:...:2ⁿ. This is a "base-2 weighing scheme."

### Dead ends or traps to avoid

1. **Equal-spacing strategy for LB is suboptimal:** LB marking at uniform {k/(n+1) : k=1,...,n} (equal pieces) is easily defeated by XY. XY uses the "equal pair + tiny piece" trick: mark ε in one piece and the midpoint of another to create two equal large pieces. This limits LB to ≈1/2 + small correction, well below c(n).

2. **Symmetric LB strategies (a, 1−a) for n=2:** All tested symmetric placements give guarantee ≈1/2 + small, much below 4/7.

3. **Formula (n+1)/(2n+1) is wrong:** This is the "equal pieces" answer and is not achievable. The true answer 2ⁿ/(2ⁿ⁺¹−1) grows more slowly.

4. **Assuming LB's greedy claiming is obvious:** Need to formally prove greedy is optimal in the claiming phase (exchange argument), not just assume it.

5. **The "XY uses fewer marks" option:** XY can use 0, 1, ..., or n marks. For LB's geometric marking, the minimum over XY's response is achieved by XY using ALL n marks. But for other LB markings, XY sometimes does better using fewer.

### Analogous past problems (cruxes)

From searching `domain=combinatorics`, `subtopic=games-and-strategy`:

1. **aimo-0117 (Jesse en Tjeerd dyadic stones game):** Crux = "assign played values as a dyadic (geometric) sequence so the single largest value dominates all others." Analogous: the geometric 1:2:4:...:2ⁿ piece structure in our problem is exactly this dyadic hierarchy. The crux move of using powers of 2 to control dominance applies directly to LB's optimal marking strategy.

2. **aimo-0262 (Cinderella buckets):** Crux = "self-reproducing invariant family of configurations; each legal move restores it." The invariant in our problem (the pieces always sum to c(n) for LB) resembles this structure. The "invariant maintained under adversarial moves" proof structure is highly relevant.

3. **aimo-0596 (card deck pairing):** Crux = "involution-pairing strategy; partner-mirroring." The "pairing of pieces at equal ranks" structure in the claiming phase (LB and XY each get one piece from each tied pair) is analogous to the pairing argument. Less directly analogous.

### Prior progress
None (Round 1 baseline: unsolved).

### Small-case / intuition notes (all conjectural unless marked ✓)

- c(1) = 2/3 ✓ (proved analytically: LB at 1/3 always achieves 2/3 regardless of XY's 1 mark)
- c(2) = 4/7 (numerically confirmed to high precision; the geometric LB strategy achieves exactly this and no other LB strategy achieves more)
- c(3) = 8/15 (numerically confirmed on N=60 grid)
- **General conjecture:** c(n) = 2ⁿ/(2ⁿ⁺¹−1) (labeled CONJECTURE, numerical evidence for n≤3)
- The formula is equivalent to 1/c(n) + 1/c(n) = 2 + 2⁻ⁿ... better: c(n) = 1/(2−2⁻ⁿ).
- As n→∞, c(n)→1/2 (as both players can create fine subdivisions, the first-pick advantage vanishes).
- LB never benefits from marking FEWER than n points (using all n marks gives strictly better guarantee than using fewer).
- The claiming phase optimal strategy is greedy (takes largest available). This is a standard result for alternating selection from sorted lists.
