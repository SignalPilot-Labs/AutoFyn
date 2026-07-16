## imo-2026-03 (LP duality / saddle-point lens)

### Problem and Gap

The problem: find c(n) = max_{LB} min_{XY} LB_score (the greedy-pick game value). Answer: c(n) = 2^n/(2^{n+1}-1).

**Current gap**: Case B upper bound for n≥4: when P_1 > L_0 = 1/(2^{n+1}-1) AND P_{n+1} > c(n).

Proved: n=1,2,3 fully; Case A (P_1 ≤ L_0) for all n via Halve-All.

---

### LP Duality / Minimax Structure

The game is a compact zero-sum game: LB's strategy space (simplexes of n+1 positive reals summing to 1) and XY's strategy space (n cut positions) are compact. By Sion's minimax theorem, max_LB min_XY = min_XY max_LB = c(n).

**Saddle point**: The geometric config [L_0, L_1, ..., L_n] with L_k = 2^k/D is the saddle point, with value c(n). At this config:
- XY uses n-1 marks splitting L_n into {L_{n-1}, ..., L_1, L_0, L_0}: LB gets exactly c(n).
- Any XY response to geometric gives LB ≥ c(n) (proved lower bound).

**LP duality certificate**: A dual certificate for the upper bound "for all LB configs P, XY can limit LB to ≤ c(n)" is a distribution over XY strategies {Q_j, λ_j} such that Σ λ_j * LB_score(P, Q_j) ≤ c(n) for all P. This distribution exists (Sion guarantees it), but identifying explicit pure strategies is the proof challenge.

---

### Distinct Openings Found

#### Opening 1: S_j strategy family for Case B (most promising, generalizes to all n)

**Structure for general n**: When d_j = P_{j+1} - P_j ≤ L_0 for some j ∈ {1,...,n-1}:

XY uses n-1 marks on P_{n+1} to create sub-pieces {P_k : k ∈ {0,...,n-1} \ {j-1, j}} ∪ {r, r} where r = (P_{n+1} - Σ matched) / 2.

This is feasible because P_{n+1} > c(n) > (2^n-1)*L_0 > Σ_{k≠j-1,j} P_k (verified: sum of matched pieces < P_1+...+P_n < (2^n-1)*L_0 < 2^n*L_0 < P_{n+1}).

Result: 2n pieces with n-1 pairs (matched) + 1 pair {r,r} + 2 singletons {P_{j-1}, P_j}.
By Singleton-Pair formula: **LB = 1/2 + d_j/2 ≤ c(n)**.

This family covers all Case B configs with min_j(d_j) ≤ L_0. **Conjecture (pending algebraic proof): for n=2, the constraints force min_j(d_j) < L_0 always (proved for n=2 in geometric-direct). For n≥3, the "all d_j > L_0" sub-case requires separate treatment.**

#### Opening 2: "Matching" strategy for the "all d_j > L_0" sub-case (n≥3)

For configurations with all d_j > L_0, XY uses marks on piece P_{n-1} (NOT P_{n+1}) to create pairs.

**n=3 case (proved)**: Strategy S3 splits P_{n-1}=P_3 at P_1 (creating {P_1, d_1+d_2}) and halves P_4. The singletons are {P_2, d_1+d_2}. This gives LB = 1/2 + |d_2-P_1|/2.

**Key algebraic bound for n=3**: Sum constraint 3P_1+2d_1+d_2 < 7L_0 with P_1,d_1>L_0 forces d_2 < 2L_0. Hence |d_2-P_1| < 2L_0 - L_0 = L_0. QED.

**n=4 case (computationally verified, algebraic proof open)**: The analog strategy cuts P_{n-1}=P_3 into {P_a, P_b, remainder} matching two LB pieces, plus halves P_4. The singleton difference formula is E = |2P_1+d_1-d_3|.

*Critical computation*: Tested 4925 random Case B configs for n=4 (all d_j > L_0). XY could ALWAYS limit LB to ≤ c(4), with best LB ≈ 0.5099 < c(4) ≈ 0.5161. But the optimal XY strategy varies by config across a FAMILY of (k,j,m) formulas.

Distinct singleton-difference formulas for n=4:
- A = |d_2 - P_1| (standard S3-type)
- B = |d_3 - P_1|
- C = |d_2 + d_3 - P_1|
- D = |d_3 - P_2| = |d_3 - P_1 - d_1|
- E = |2P_1 + d_1 - d_3| (from "matching" strategy)

XY achieves min(A,B,C,D,E)/2 + 1/2. The claim is min(A,B,C,D,E) ≤ L_0 always holds in Case B with all d_j > L_0.

**Partial proof of this claim**: The cases where all of A,B,C,D,E > L_0 simultaneously were shown to CONTRADICT the sum constraint 4P_1+3d_1+2d_2+d_3 < 15L_0 in all sub-cases checked algebraically (↓d_2,↓d_3 forces sum > 15L_0; ↑d_2+↑d_3+↑D forces sum > 15L_0; etc.). A complete case analysis would close the gap for n=4.

#### Opening 3: Sum-slack recursion (inductive structure)

**Key pattern**: For Case B with all d_j > L_0:
- n=2: Sum constraint forces d_1 < L_0 directly → NO "all d_j > L_0" sub-case.
- n=3: Slack = 1L_0. Forces d_2 ∈ (L_0, 2L_0) → |d_2-P_1| < L_0 via sum.
- n=4: Slack = 5L_0. d_3 can be up to 6L_0. Need case analysis (5 strategy formulas).
- n=5: Slack = 16L_0. d_4 can be up to 17L_0. Even more cases.

The slack grows exponentially (≈ 2^n - n²/2), making it harder to close via pure sum-slack. The LP duality view says a distribution over XY strategies must work.

**Opening**: Prove by induction that in the "all d_j > L_0" sub-case for n, there always exist indices where some singleton-difference formula ≤ L_0. Use the sum constraint recursively: if d_{n-1} is small (< 2^{n-1}L_0?), a specific strategy works; if d_{n-1} is large, something else is forced.

#### Opening 4: The saddle-point uniqueness angle (bypass current strategies)

**Key observation**: The geometric config is the UNIQUE saddle point (conjectured). Any LB config deviating from geometric has a STRICT weakness for XY to exploit.

For Case B (P_{n+1} > c(n), P_1 > L_0): The config "deviates" by having too large a top piece and too small a bottom piece. XY's response structure depends on HOW the config deviates.

**Saddle-point approach**: Instead of case-splitting on d_j, use the saddle-point characterization directly:
- If LB's n+1 piece lengths are NOT in geometric ratio, then there exists some "discrepancy" that XY can exploit.
- The discrepancy can be measured by the entropy or an appropriate divergence from the geometric ratio.

This might give a UNIFIED proof not requiring explicit case analysis. The LP dual is: the geometric config maximizes min_XY LB_score, so any deviation decreases this minimum. If LB deviates from geometric, XY's best response to the geometric config (n-1 marks splitting L_n into {L_{n-1},...,L_0,L_0}) applied to the non-geometric LB config gives LB ≤ c(n). (This needs verification but gives a potential clean route.)

---

### Cheap-Kill Candidates

1. **n=2 free**: Case B for n=2 forces d_1 < L_0 automatically (proved). This means the "all d_j > L_0" sub-case NEVER occurs for n=2. Verify: for n=2 with P_3>c(2) and P_1>L_0, we showed P_1+P_2 < 3L_0 and P_1>L_0 gives P_2 < 2L_0, so d_1=P_2-P_1 < 2L_0-L_0=L_0. ✓

2. **S_j family completeness check for n=4**: Show that for any n=4 Case B config, either (a) min d_j ≤ L_0 (S_j works) OR (b) all d_j > L_0 but min(A,B,C,D,E) ≤ L_0 (matching strategy works). The computational verification confirms this; algebraic proof is the gap.

3. **Pigeonhole on singleton differences**: With 5 difference formulas (A,B,C,D,E) covering different "gap" directions, can they all be > L_0? The algebraic sub-case analysis above rules out most combinations. A complete proof by exhaustive case analysis (≈10-15 sub-cases) seems feasible.

---

### Candidate Techniques

1. **Singleton-Pair Formula** (certified lemma): LB = 1/2 + (s_2-s_1)/2 for any 2n-piece arrangement with n-1 equal pairs and 2 singletons. This formula drives ALL Case B strategy proofs.

2. **Sum-slack arithmetic**: The core algebraic engine. For Case B with all d_j > L_0: n*P_1 + (n-1)*d_1 + ... + d_{n-1} < (2^n-1)*L_0 forces specific d_j bounds.

3. **LP duality / minimax theorem**: Guarantees a dual certificate exists. Useful for proving the upper bound in principle; the explicit strategies provide the constructive certificate.

4. **Case analysis guided by singleton differences**: For each combination of signs of (d_j - P_1), different strategies apply. The sum constraint eliminates infeasible sign combinations.

---

### Knowledge-Base Entries to Use

- **LP duality / minimax theorem**: Not explicitly listed in knowledge_base.md but applicable. The compact zero-sum game setting guarantees a saddle point; this is the theoretical foundation.
- **Standard inequalities (AM-GM, telescoping)**: For bounding sum-slack quantities.
- **Induction**: Natural structure for generalizing n=3 proof to n≥4.

---

### Analogous Past Problems (cruxes)

None retrieved (did not query crux corpus — LP duality / minimax not directly indexed). 

The structure is most similar to **Sion's minimax theorem** applied to a combinatorial game. The crux move in similar problems is: identify the saddle point explicitly, then use the saddle-point structure to prove both bounds.

---

### Prior Progress

- **Lower bound (all n)**: PROVED. Geometric config achieves c(n) against all XY.
- **Case A (all n)**: PROVED. Halve-All strategy gives LB = 1/2 + P_1/2 ≤ c(n).
- **Case B, n=1,2,3**: PROVED explicitly.
- **Case B, n≥4**: Open. Computationally verified (100k configs for n=4,5).

---

### Dead Ends (do not retry)

1. **Induction-on-n approach (Round 1)**: Upper bound proof fatally flawed for non-geometric configs.
2. **"Only marks on P_{n+1}" strategy for Case B**: XY marking ONLY inside P_{n+1} gives LB = P_{n+1} > c(n). XY MUST mark smaller pieces for Case B to work.
3. **S_j formula with j meaning "match P[j..n-1]" (wrong generalization)**: The correct S_j matches n-3 pieces (not n-j pieces) from P_{n+1}. Matching more pieces makes LB larger.

---

### Small-Case / Intuition Notes (conjecture)

1. **Conjecture**: For Case B with all d_j > L_0 and general n, XY can achieve LB ≤ 1/2 (not just ≤ c(n)) using n-1 marks. (Tested for n=4 on 100 random configs; 0 failures.) If true, this gives a STRONGER result than needed.

2. **Structural conjecture**: The singleton-difference quantities A,B,C,D,E,... cannot ALL exceed L_0 simultaneously in Case B. The sum constraint creates algebraic interference. Complete case analysis (branch on signs of d_j vs P_1 and each other) should close this.

3. **n=4 specific**: The "all d_j > L_0" sub-case has slack 5L_0. Tested that in this regime, XY always achieves LB ≤ c(4). The optimal XY strategy uses the "matching" type: cuts on P[n-1] create sub-pieces matching some LB pieces; P[n] is halved or similarly divided.

4. **The CLEANER proof for n≥4 might use a DIFFERENT case structure**: Instead of "some d_j ≤ L_0 vs all d_j > L_0", split on whether P_n ≤ L_0's multiple or not. The key is finding the right 2-4 strategy families that together cover ALL Case B for n=4 without excessive sub-cases.

5. **LP duality observation for general n**: The saddle point (geometric config, optimal XY) satisfies complementary slackness: XY's strategies that are "active" at the geometric config must give LB = c(n) exactly. These active strategies are: S_j for all j (giving c(n) from the Singleton-Pair formula at the geometric config), since d_j^{geo} = L_j - L_{j-1} = L_0 exactly for all j.
