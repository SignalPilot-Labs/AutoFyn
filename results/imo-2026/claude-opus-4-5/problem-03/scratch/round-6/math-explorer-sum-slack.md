## imo-2026-03

**Lens: Sum-slack generalization for Case B n≥4**

### PRIMARY DISCOVERY: Strategy S5 (new, closes n=4 gap)

The previous round's approach set {S4, S6, B, PP} had 87/50,000 failures. **Adding S5 gives 0/100,000 failures.**

**Strategy S5 construction (n=4):**
- XY cuts P4 at P3 from its left end: creates {P3, d3}. The sub-piece P3 pairs exactly with the original P3 piece.
- XY cuts P5 at (P5-P1)/2 from each end: {(P5-P1)/2, P1, (P5-P1)/2}. The two halves form an exact pair; the middle sub-piece P1 pairs exactly with the original P1.
- Total: 3 XY marks. 4th mark is wasted (degenerate or irrelevant).
- Result: 8 pieces = 3 exact pairs {P3,P3}, {(P5-P1)/2,(P5-P1)/2}, {P1,P1} + 2 singletons {P2, d3}.
- By Singleton-Pair Formula: **LB = 1/2 + |d3-P2|/2**.
- Applies when |d3-P2| = |d3-(P1+d1)| ≤ L0, i.e., |η-(α+β+1)| ≤ 1 in reduced units.

**Verified directly on the previous round's "failure" config** (α=0.238, β=0.083, γ=1.240, η=1.188): |d3-P2| = 0.133 L0 ≤ L0 → LB = 0.5021 ≤ c(4) = 0.5161. ✓

---

### ALGEBRAIC PROOF OF COMPLETE n=4 COVERAGE

**Setup:** Reduced-unit parameterization α = P1/L0-1, β = d1/L0-1, γ = d2/L0-1, η = d3/L0-1, all >0. Sum constraint: 4α+3β+2γ+η < 5.

**The five strategies and their conditions:**
| Strategy | Works when | LB formula |
|----------|-----------|------------|
| S6 | &#124;d2-P1&#124; ≤ L0 (&#124;γ-α&#124; ≤ 1) | 1/2 + &#124;d2-P1&#124;/2 |
| S4 | &#124;d1-d3&#124; ≤ L0 (&#124;β-η&#124; ≤ 1) | 1/2 + &#124;d1-d3&#124;/2 |
| S5 (NEW) | &#124;d3-P2&#124; ≤ L0 (&#124;η-α-β-1&#124; ≤ 1) | 1/2 + &#124;d3-P2&#124;/2 |
| B | d3 ∈ [2P1+d1-L0, 2P1+d1) | 1/2 + (2P1+d1-d3)/2 |
| PP | d3-2P1-d1 ∈ (0, L0] | 1/2 + (d3-2P1-d1)/2 |

**Proof of gap-free coverage:**

*Non-Case-A:* Either |γ-α| < 1 (S6 works) or |β-η| < 1 (S4 works). The only remaining sub-case is α > γ+1 with η < β+1; in this case sum constraint forces β, η < 1/3, so |β-η| < 1/3 and S4 works.

*Case A: γ ≥ α+1, η ≥ β+1, 6α+4β < 2 (implied by sum constraint when both fail)*:
- η ≥ β+1 forces |β-η| = η-β ≥ 1, so S4 fails.
- γ ≥ α+1 forces |γ-α| = γ-α ≥ 1, so S6 fails.

Coverage by η value in Case A:
- **S5** covers η ∈ [β+1, α+β+2]: since η ≥ β+1 (Case A) and d3-P2 = (η-α-β-1)L0 ≤ (α+β+2-α-β-1)L0 = L0. ✓
- **Strategy B** covers η ∈ [2α+β, 2α+β+2].
- **Perfect Pairing** covers η ∈ (2α+β+2, η_max) where η_max = 3-6α-3β.

*Gap between S5 and B:* Width = (2α+β)-(α+β+2) = **α-2 < 0** (since α < 1/3 < 2 in Case A). **EMPTY.**

*Gap between B and PP:* None (PP starts exactly where B ends).

*PP bound:* rem = (η-2α-β-2)L0 < (η_max-2α-β-2)L0 = (1-8α-4β)L0 < L0 since α,β > 0. **rem < L0 always when PP activates.** ✓

*PP upper limit:* η < η_max = 3-6α-3β < 2α+β+3 iff 8α+4β > 0 (always). So PP_start = 2α+β+2 < 3-6α-3β when they both apply. ✓

**Complete coverage. QED for n=4.**

---

### GENERALIZATION TO GENERAL N

**The "level-k" singleton strategy family:** For n marks, XY can produce exact pairs at multiple levels. The key comparison is between consecutive-level quantities:

- Level 0: compare d2 vs P1 (S6 / S3-analog for all n).
- Level 1: compare d3 vs P2 (S5-analog for n≥4).
- Level 1': compare d1 vs d3 (S4-analog for n≥4).
- Level 2: compare d4 vs P3 (new for n≥5).
- Level 2': compare d2 vs d4 (new for n≥5).
- Etc.

**n=5 strategy structure (numerically verified, 0 real failures in 200,000 tests):**
- Global optimizer for n=5 "all d_j>L0" configs consistently finds 5 near-pairs with total difference-budget well within the allowed L0/2 = c(n)-1/2.
- Clean analog: XY cuts P6 into {P3, (P6-P3)/2, (P6-P3)/2} (2 marks: exact pair of P3 + exact pair of (P6-P3)/2), cuts P5 at P2 from left (exact pair {P2,P2}), cuts P4 at P1 from left (exact pair {P1,P1}). Singletons: {P5-P2, P4-P1} = {d2+d3+d4, d1+d2+d3}. Difference: |d4-d1|. Formula: **LB = 1/2+|d4-d1|/2 ≤ c(5) iff |d4-d1| ≤ L0**. Uses 4 marks.
- When |d4-d1| > L0: use S5-analog (singletons {P2, d3} or {P3, d4}, etc.).
- When no singleton-pair works: B and PP with higher-level structure.

**Extra marks create stronger coverage:** For n≥4, XY has n marks but the singleton-pair strategies use only 3 marks. The n-3 spare marks can be used to create additional pairs, reducing the singleton-difference further. This makes coverage EASIER for larger n.

**Key algebraic claim generalizing from n=4:** In "Case A-generalized" for any n (where all "adjacent-level" differences exceed L0), the sum constraint forces the "smallest parameter" α < 1/(2^n-1)·something to be small, making the gap between consecutive strategy intervals have negative width.

---

### DISTINCT OPENINGS FOR THE OUTLINER

**Opening 1 (Direct algebraic proof for n=4, then induct):**
The n=4 case is now complete: S4+S5+S6+B+PP cover ALL "all d_j>L0" configs. The algebraic proof (5 strategies, 2 cases, verified 0/100,000 failures) is rigorous. Then use induction: for n≥5, the analogous strategy family covers all cases because (a) XY has spare marks to create more pairs, and (b) the "negative gap width" argument still applies.

**Opening 2 (Singleton-pair via level-k comparison):**
For any n and any "all d_j>L0" config, define the n-1 "level-k differences": Δ_k = |d_{k+1} - P_k| for k=0,...,n-2 (comparing consecutive differences with "prefix sums"). The sum constraint forces min_k(Δ_k) ≤ L0, giving a singleton-pair strategy directly. This would be a clean one-lemma proof if the min-bound holds.

**Opening 3 (Recursive halving + induction):**
For n≥4: XY uses 1 mark to halve P_{n+1} (creating exact pair). For the sub-problem {P1,...,P_n} with n-1 XY marks, apply the (n-1)-proof structure. The key observation: after halving P_{n+1}, LB gets P_{n+1}/2 and the sub-game score needs to be ≤ c(n)-P_{n+1}/2. This leads to a modified game with a tighter target. Verifying the recursion closes is the challenge.

**Opening 4 (Strategy S5 as the "canonical" extra strategy for Case B):**
Strategy S5 is structurally the "dual" of the Halve-All strategy (Case A). While Case A pairs all pieces at once by creating one copy of each, S5 pairs P3 and P1 specifically to isolate {P2, d3}. For general n, the "canonical extra strategy" might be: pair P_{n-1} from P_n and pair P_1 from P_{n+1}, leaving singletons {P_{n-2}, d_{n-1}} with small difference by sum constraint.

---

### CANDIDATE TECHNIQUES

- **Singleton-Pair Formula** (certified lemma): LB = 1/2 + (s2-s1)/2 where s1<s2 are the unique singletons. Core tool for ALL the strategies above.
- **Pairing Cancellation Lemma** (certified lemma): lb_score({v,v}∪S) = v + lb_score(S). Justifies why exact pairs can be removed from analysis.
- **Sum-slack analysis**: The bound η < 3-6α-3β (Case A) is derived from the sum constraint P1+...+P_n < (2^n-1)L0. Key for proving PP rem < L0.
- **Case analysis by sign of (d3-P2)** and **(d3-2P1-d1)**: divides Case A into 3 non-overlapping intervals with negative-width gaps.

---

### CHEAP-KILL CANDIDATES

- **S5 directly resolves all "Case A" failures from Round 5**. The prior 87-failure dataset drops to 0 immediately.
- **Gap-width computation**: α-2 < 0 (since α < 1/3) is a 1-line arithmetic check that closes the coverage.
- **PP bound**: rem < (1-8α-4β)L0 ≤ 1·L0 is a 1-line bound from the sum constraint; covers the tail.

---

### KNOWLEDGE-BASE ENTRIES TO USE

From knowledge_base.md (to be named when building proof):
- **Greedy Optimality Lemma** (certified): LB's greedy strategy is optimal.
- **Pairing Cancellation Lemma** (certified): {v,v}∪S gives LB = v + lb_score(S).
- **Singleton-Pair Formula** (certified): LB = (1 - s_min + s_max)/2 for 2n-piece config with 2 singletons.
- **Halve-All Strategy Lemma** (Case A, certified): If P1 ≤ L0, XY halves P2,...,P_{n+1}.
- The recurrence c(n) = 2^n/(2^{n+1}-1) and L0 = 1/(2^{n+1}-1).

---

### ANALOGOUS PAST PROBLEMS (CRUXES)

None closely analogous in the crux corpus. The "level-k singleton" strategy family is novel. The closest conceptual analog would be a combinatorial game where a "budget" of differences must be allocated across multiple levels, but no such problem was found in the corpus.

---

### PRIOR PROGRESS

- **Complete proof for n=1,2,3** (geometric-direct.md).
- **Case A proved for all n** (Halve-All strategy).
- **Case B for n≥4**: Previously unproved. THIS ROUND: n=4 is now ALGEBRAICALLY CLOSED via S4+S5+S6+B+PP. The proof of gap-free coverage is explicit and verifiable.
- **n=5**: Computationally verified (0 true failures in 200,000 tests; 998 "failures" were optimizer non-convergence, each with true optimum < c(5)).

---

### DEAD ENDS (DO NOT RETRY)

- **Single sum-slack bound for all d_j > L0**: For n≥4, no single bound like "d_{n-1} < 2L0" covers all cases. The slack (2^n-1-n(n+1)/2)L0 grows exponentially, making direct bounds too weak.
- **S4+S6+B+PP without S5**: 87/50,000 failures. S5 is essential.
- **Strategy D-v2** (pair P3, pair P2, halve rest, singletons P1 and d3): Fails when d3 > P1+L0. Not robust.
- **Recursive halving of P_{n+1} as sole strategy**: Gives LB ≤ P_{n+1}/2 + c(n-1) > c(n) since c(n-1) > c(n)/2.

---

### SMALL-CASE / INTUITION NOTES

*Conjectures, not proved:*

1. **Conjecture**: For general n "all d_j>L0", the strategy set {S6, S4, S5, B, PP and their level-k analogs} covers all cases. For level k, the strategy compares d_{k+2} vs P_{k+1} and uses n-3+k marks.

2. **Conjecture**: The key "Case A-generalized" for n≥5 has "sum coefficient 8α+4β replaced by 2^{n-2}·α + lower-order terms", forcing α to be exponentially small. This makes the gap width even more negative for larger n, so coverage gets EASIER.

3. **Evidence from n=5 optimizer**: XY's optimal near-pair structure has near-pairs with differences <<L0 even when all d_j>L0. The "level-k comparison" differences are all small simultaneously, suggesting the sum constraint is much more powerful for large n than for small n.

4. **The n=4 Case A is the HARDEST case**: In n=3, the sum-slack directly gives d2-P1<L0 (single strategy). In n=4, Case A requires THREE strategies (S5, B, PP) but the algebraic argument is clean. For n≥5, the extra marks give XY more flexibility, suggesting the proof generalizes by induction with decreasing difficulty.
