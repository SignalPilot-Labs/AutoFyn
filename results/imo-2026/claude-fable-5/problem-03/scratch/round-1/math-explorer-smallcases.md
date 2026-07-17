## imo-2026-03

### Conjectured answer
**c(n) = 2^n / (2^(n+1) − 1)**

Verified numerically for n = 1 (2/3), n = 2 (4/7), n = 3 (8/15) using exhaustive minimax search.

---

- **Distinct openings:**

  1. **Geometric-ratio construction + halving counter (direct equilibrium analysis).** LB places n marks creating n+1 pieces in geometric ratio 1:2:4:…:2^n (pieces 2^k/D for k=0,…,n where D=2^(n+1)−1). XY's best response: halve the n largest pieces. This creates 2n+1 pieces; sorted in decreasing order they are 2^(n−1)/D, 2^(n−1)/D, 2^(n−2)/D, 2^(n−2)/D, …, 1/D, 1/D, 1/D (three copies of 1/D, two of each larger value). LB picks positions 1,3,5,…,2n+1 = (2^(n−1)+2^(n−2)+…+1+1)/D = 2^n/D. The saddle-point structure is verified: no XY 2-mark (n=2) or 3-mark (n=3) strategy beats this, confirmed by dense numerical search.

  2. **Inductive/recursive argument.** The formula c(n) = 1/(2 − 1/2^n) suggests a self-similar structure: c(n) satisfies c(n) = 1/(1 + 1/c(n−1)) or some recurrence. Note 1/c(n) = 1 + 1/2^n = (2^n+1)/2^n. The recursion 1/c(n) = 1 + 1/2^n links to 1/c(n−1): 1/c(n) = 1 + 1/2^n = 1 + (1/2)(1/2^(n−1)) = 1 + (1/(2·c(n−1))) · (2^(n−1)/2^(n−1))… May not simplify cleanly, but induction on n is a viable approach.

  3. **Saddle-point / mixed strategy minimax.** Treat as a minimax over continuous choices. The saddle point is the geometric configuration. Approach: prove LB ≤ c(n) for any LB strategy (upper bound) by showing XY can always achieve this, and LB ≥ c(n) for the geometric strategy (lower bound) by showing any XY counter gives ≥ c(n). Separate two-direction proof.

  4. **Exchange argument / smoothing.** For the lower bound: given LB's geometric pieces and any XY n-mark response, show the XY cuts can only "rearrange" pieces in a way that keeps LB's greedy gain ≥ 2^n/(2^(n+1)−1). The key is that for geometric pieces, halving the n largest is XY's unique optimal strategy, and it gives exactly c(n).

---

- **Candidate technique(s):**
  - Minimax / saddle point analysis for combinatorial games on the interval.
  - Greedy algorithm analysis: when both players pick greedily (largest first), LB's gain = sum of odd-indexed pieces in sorted order.
  - Induction on n via the self-similar geometric structure.
  - Direct computation: show that for the geometric LB strategy, any XY n-mark response gives LB ≥ c(n), and for any LB strategy, some XY n-mark response gives LB ≤ c(n).

---

- **Cheap-kill candidates:**
  - **Parity check:** With 2n+1 pieces (maximum), LB picks ⌈(2n+1)/2⌉ = n+1 pieces. Even pieces: LB gets at best 1/2. XY always prefers creating 4 pieces (not 5) to limit LB when pieces can be made equal.
  - **XY strategy of 0 marks:** If LB creates pieces (a_0 ≤ … ≤ a_n), XY can use 0 marks and LB gets a_n + a_{n-2} + … (depending on n). For n≥2 this is large (LB gets all odd positions of n+1 pieces), so XY should always use marks.
  - **LB uses fewer than n marks:** If LB uses k < n marks, XY has n ≥ k+1 marks and can "overcome" LB more easily. LB should always use all n marks.

---

- **Knowledge-base entries to use:**
  - **Invariants & monovariants** (Combinatorics section): The invariant is the ratio structure 1:2:4:…:2^n at the saddle point.
  - **Extremal principle** (Combinatorics section): Taking a minimax over LB/XY strategies; the extremum is the geometric ratio.
  - **Standard inequalities: AM-GM** (Algebra section): Possibly needed to show XY can achieve LB ≤ c(n) for any LB strategy.
  - **Constructive / incremental** (Combinatorics section): The proof that LB's geometric strategy works requires showing any XY response gives LB ≥ c(n) — this is a construction argument.

---

- **Analogous past problems (cruxes):**
  1. **aimo-0117** (combinatorics, games-and-strategy): "Assign the played values as a two-sided geometric (dyadic) sequence so that the single largest value strictly exceeds the sum of all the others." Crux: dyadic/geometric ratio in a game-theory context. The geometric 1:2:4:…:2^n ratio for LB's pieces is directly analogous to this dyadic valuation structure.
  2. **aimo-0019** (combinatorics, games-and-strategy): "Bound a family of dyadic-length pieces of pairwise distinct sizes by twice the largest, via the geometric sum of distinct negative powers of two." Crux: dyadic intervals on the real line, geometric sums. Analogous because the formula 2^n/(2^(n+1)−1) = 1/(1 + 1/2 + 1/4 + … + 1/2^n) (inverted geometric series) mirrors the dyadic-piece potential bound.
  3. **aimo-0225** (combinatorics, games-and-strategy): "Determine the game value by recursing on the 2-adic valuation of a difference that exactly halves at each relevant step." Crux: 2-adic (dyadic) recursion determining game outcome. The formula c(n) = 2^n/(2^(n+1)−1) has a dyadic recursion structure: c(n) = 1/(2 − c(n−1)) or similar.

---

- **Prior progress:** None (status: unsolved, first round).

---

- **Dead ends (do not retry):**
  - **Pieces in ratio 1:2:3:…:(n+1) (arithmetic ratio):** Numerical search confirms this gives only c ≈ 0.50 for n=2 and n=3 (XY at 2/3 achieves LB=1/2). Dead end.
  - **Pieces in ratio 1:3:9:…:3^n (powers of 3):** Gives only 0.517 for n=3. Dominated by geometric 1:2:4:…:2^n.
  - **Equal pieces (1/(n+1) each):** XY at 2/(n+1) etc. achieves LB=1/2. Dead end.
  - **Formula c(n) = 2n/(4n−1):** Matches for n=1,2 but gives 6/11≈0.545 for n=3, which is larger than the actual 8/15≈0.533. Wrong formula.
  - **Formula c(n) = (n+1)/(2n+1):** Gives 3/5=0.6 for n=2, contradicted by numerical c(2)=4/7. Wrong.
  - **LB at (1/6, 1/2) (pieces 1/6:1/3:1/2 = 1:2:3):** XY at 2/3 achieves LB=1/2. This strategy only guarantees 1/2, not 7/12 as I initially believed (error due to missing XY strategy q=2/3).

---

- **Small-case / intuition notes (labeled as conjecture):**

  **n=1 (proved):** LB at 1/3. Pieces (1/3, 2/3). XY at 2/3: 3 pieces (1/3, 1/3, 1/3), LB=2/3. For any other XY mark q, LB ≥ 2/3. So c(1) = 2/3 = 2/(2²−1). ✓

  **n=2 (strongly conjectured, dense numerical verification):** LB at (1/7, 3/7). Pieces (1/7, 2/7, 4/7) = ratio 1:2:4. XY's best response: halve 4/7 at 3/7+2/7=5/7 (creating pieces 2/7, 2/7), or more generally any of the equivalent XY strategies all give LB=4/7. Dense search with 5000 q-points confirms: min LB over all XY 2-mark strategies = 4/7. c(2) = 4/7 = 4/(2³−1). (Conjecture, not proved.)

  **n=3 (strongly conjectured, grid+dense numerical verification):** LB at (1/15, 3/15, 7/15). Pieces (1/15, 2/15, 4/15, 8/15) = ratio 1:2:4:8. XY halves the 3 largest: 7 pieces (1/15, 1/15, 1/15, 2/15, 2/15, 4/15, 4/15). LB picks 4/15+2/15+1/15+1/15=8/15. Dense numerical grid search for LB finds max guarantee = 8/15. c(3) = 8/15 = 8/(2⁴−1). (Conjecture.)

  **General structural observation (conjecture):** c(n) = 2^n/(2^(n+1)−1). As n→∞, c(n)→1/2. The formula can be written c(n) = 1/(1 + 1/2 + 1/4 + … + 1/2^n)^{−1}… equivalently 1/(2 − 2^(1−n))... Actually c(n) = 2^n/(2^(n+1)−1). 

  **Saddle-point verification (key equilibrium structure):** At LB's geometric strategy, multiple XY strategies all achieve exactly c(n):
  - XY halves the n largest pieces → achieves c(n).
  - XY splits the largest piece at exactly 1 unit from the bottom (creating the second-largest piece twice) → same value.
  This multiplicity of XY optima confirms the saddle-point structure.

  **Why XY can't do better against geometric LB (conjecture):** For pieces in ratio 1:2:4:…:2^n, LB's gain under any XY n-mark strategy is ≥ 2^n/(2^(n+1)−1). This likely follows from an inequality on geometric sequences: for pieces p_0 ≤ p_1 ≤ … ≤ p_n = (1, 2, 4, …, 2^n)/D and any 2n+1 sub-pieces (n pieces each split into 2), the odd-indexed LB gain ≥ 2^n/D.

  **Why LB can't do better than geometric ratio (conjecture):** For any LB piece configuration other than geometric ratio, XY can achieve LB < c(n). This is the upper bound direction.

---

### Key computation details

For n=2, LB at (1/7, 3/7), XY at q=5/7 (dense search confirms this as XY optimum):
- Cuts: 1/7, 3/7, 5/7. Pieces: [0,1/7]=1/7, [1/7,3/7]=2/7, [3/7,5/7]=2/7, [5/7,1]=2/7. Sorted: 2/7, 2/7, 2/7, 1/7. LB=2/7+2/7=4/7. ✓
- XY also at q=5/7 AND q=2/7 (2-mark): 5 pieces (1/7,1/7,1/7,2/7,2/7). LB=2/7+1/7+1/7=4/7. ✓

For n=3, XY halves the 3 largest of (1/15, 2/15, 4/15, 8/15):
- 7 pieces: 4/15, 4/15, 2/15, 2/15, 1/15, 1/15, 1/15. LB picks 4/15+2/15+1/15+1/15=8/15. ✓

The LB cut positions for the geometric strategy: cut_j = (2^(j+1)−1)/(2^(n+1)−1) for j=0,1,…,n−1.
- n=1: cut_0 = 1/3.
- n=2: cut_0 = 1/7, cut_1 = 3/7.
- n=3: cut_0 = 1/15, cut_1 = 3/15=1/5, cut_2 = 7/15.
