## imo-2026-03 (upper-bound lens: Claim U / GAP AU)

### Critical bug discovered
**Claim U as stated (geometric-selfsimilar) is WRONG.** The formulation reads: "XY, by placing all n cuts optimally inside A_1, forces val ≤ c(n)." This is FALSE for some LB configs.

Counterexample (n=2): LB config (A_1, A_2, A_3) = (0.4, 0.4, 0.2). XY concentrating both cuts on A_1 = 0.4 achieves val ≈ 0.608 > 4/7 ≈ 0.5714. Splitting cuts between A_1 and A_2 gives val = 0.6 > 4/7. But XY putting BOTH cuts on A_3 = 0.2 (the SMALLEST piece) achieves val ≈ 0.504 ≤ 4/7. So the upper bound is true, but only because XY is allowed to cut ANY piece — the "all on A_1" rule fails.

**Consequence**: Any approach that relies on "XY concentrates all cuts on A_1" for Claim U needs revision. The outliner must rewrite Claim U to allow XY to cut any piece.

### What the numerics say (all conjecture, no proof)
- **True upper bound c(n) numerically holds** for all tested n=2 LB configs. For every (A_1, A_2, A_3) with A_i ≥ 0 and Σ = 1, XY's TRUE optimal (minimizing over all possible cut placements) achieves val ≤ 4/7.
- **Geometric config is the tight case**: grid search on n=2 shows the config that maximizes min_XY(val) is (approximately) (4/7, 2/7, 1/7). All tested configs give min_XY(val) ≤ 4/7.
- **Geometric config is a strict local maximum**: ALL 6 perturbation directions from (4/7, 2/7, 1/7) give min_XY(val) strictly less than 4/7 (range 0.551–0.566 vs 0.571). This was verified with grid N=40.

### XY strategy landscape (n=2)
Three distinct regimes observed:
1. **Near-geometric, large A_1** (A_1 ≥ 1/2, A_1 ≤ c(n)): "Shadow" strategy. XY uses m-1 cuts to split A_1 into {A_2, A_3, ..., A_m, r} where r = A_1 - Σ_{i≥2} A_i = 2A_1-1 ≥ 0. Gives val = A_1 ≤ c(n). Uses only m-1 ≤ n cuts.
2. **Flat configs** (A_1 ≤ 1/2, all pieces small): "Pair-up" strategy. XY cuts ANY piece into two near-equal halves; repeated pairing cancels A, giving val → 1/2 < c(n). For (0.4, 0.4, 0.2), XY cuts A_3 into (≈0.1, ≈0.1, ≈0); the two 0.1's pair with each other, and the two 0.4's pair, giving val → 0.5. No "concentrate on A_1" needed.
3. **Dominant A_1** (A_1 > c(n)): XY creates near-equal sub-pieces of A_1 by (near-equal) halving: split A_1 into (A_1/2+ε, A_1/2-ε), then use second cut to handle residual. This achieves val ≈ 1/2 ≤ c(n).

No uniform single-rule XY strategy (e.g., "always cut A_1") works for all configs. Each regime needs its own approach.

### Four distinct openings for Claim U

**Opening 1: Shadow strategy for the core case (partial)**
When A_1 ≥ 1/2: XY uses the shadow strategy (m-1 cuts on A_1) to get val = A_1. This proves Claim U when A_1 ≤ c(n). The sub-case A_1 > c(n) requires additional argument (but val = A_1 > c(n) from shadow, so XY must use a different strategy here). This is the clean part that is already implicit in geometric-selfsimilar; the missing piece is the A_1 < 1/2 and A_1 > c(n) cases.

**Opening 2: Extremal-smoothing (most promising)**
Prove that G_n is the UNIQUE maximizer of F(A) := min_{XY, n cuts}(val) over all LB configs A. Then max_A F(A) = F(G_n) = c(n), which IS the upper bound (no explicit XY strategy for arbitrary A needed). Mechanism: the smoothing lemma (GAP S1 in extremal-smoothing approach) says every perturbation from G_n strictly decreases F. Numerics strongly confirm this: all 6 directions from G_2 give strict decrease. The compactness/USC argument (already in the extremal-smoothing approach) closes the gap between "local max" and "global max" if the smoothing lemma is proved.

This opening BYPASSES describing XY's strategy for arbitrary configs entirely.

**Opening 3: Direct inductive Claim U with adaptive XY**
Prove by induction on n: for any LB config (A_1,...,A_m) with m ≤ n+1, XY can achieve val ≤ c(n). Inductive step: use 1 cut to reduce to an (n-1)-round sub-problem. The adaptive part: XY's first cut depends on the config:
  - If A_1 ≥ 2A_2 (A_1 "dominant"): halve A_1 into (A_1/2, A_1/2). The two halves are ≥ A_2 so they form the top-two pieces. By the sorted structure, one goes to each player; remaining sub-problem is on pieces {A_2,...,A_m} with A_1/2 "donated" to each player — reducing to the (n-1)-game on m pieces, where IH applies.
  - If A_1 < 2A_2 (pieces close to each other): use the "pair-up" argument to show A(final) ≤ 1/D with appropriate cuts.
The IH must be strengthened: "for m ≤ n+1 pieces summing to T, XY with n cuts forces val ≤ c(n)·T" (scale-invariant form). The inductive step for the A_1 ≥ 2A_2 case: after halving A_1, the sub-config has m+1 ≤ n+2 pieces with n-1 XY cuts. Key: the two halves (A_1/2, A_1/2) form a "committed pair" (they interleave but the pair contributes exactly A_1/2 to val = one half to each player), reducing the effective problem size.
**CAUTION**: The halve-A_1 strategy does NOT work for (0.4, 0.4, 0.2) (checked: gives val=0.6 > 4/7). So the A_1 < 2A_2 case needs its own sub-argument.

**Opening 4: Potential-function (A-decrease per cut)**
Use the measure representation A = ∫ 1[N(x) odd] dx. XY's goal: make N(x) even as much as possible. A single cut of piece ℓ into (s, ℓ-s) flips parity on [0,s) and [ℓ-s,ℓ) (certified in alt-sum-integral.md). XY's greedy rule: always cut the piece and position that maximizes ΔA = (measure of "newly made even") - (measure of "newly made odd"). Claim: this greedy strategy achieves A(final) ≤ 1/D after n cuts. The challenge: proving the greedy achieves exactly 1/D on G_n (tight) and ≤ 1/D everywhere else. The tight case works: against G_n, the replica cuts halve each piece, flipping parity intervals optimally. Against other configs, A starts smaller (or XY can reduce A faster) so the bound holds more easily.

### Key computational evidence (conjecture)
- Shadow strategy gives val = A_1; this proves Claim U when 1/2 ≤ A_1 ≤ c(n). (Clean, no case needed — shadow uses m-1 ≤ n cuts.)
- For A_1 ≤ 1/2 (flat case): pair-up strategy achieves val ≤ 1/2 < c(n). No proof written; should be elementary (equal-pairing argument + A-bounds).
- For A_1 > c(n): XY can cut A_1 into (near-equal halves), achieving val ≤ c(n) via n=1 upper bound applied recursively. Numerically confirmed for n=2 with A_1 up to 0.9.
- The hardest case (tightest): A_1 = c(n), A_2 = c(n-1)·(1-c(n)), ... exactly geometric. ONLY at G_n does val = c(n) under XY's optimal play. All other configs give strict inequality.

### Dead ends / cautions
- **"Concentrate all cuts on A_1"**: wrong as stated (counterexample above). Do not attempt to prove Claim U with this strategy restriction.
- **Shadow strategy for A_1 > c(n)**: shadow gives val = A_1 > c(n). Shadow alone cannot close Claim U.
- **Halve A_1 strategy**: fails for (0.4, 0.4, 0.2) (gives val=0.6 > c(2)) and (0.45, 0.35, 0.2) (gives val=0.575 > c(2)). Not a valid universal first step.
- **Top/bottom decomposition for upper bound** (by analogy with the failed GAP AL attempt in alternating-sum-value): A(Q∪R) ≠ A_top + A_bot - 2B in a useful way for proving ≤ 1/D. Numerics show A_top - 2B can be strongly negative, so this decomposition does not give a term-by-term bound.

### Candidate technique(s)
- **Extremal smoothing** (most promising): exchange/perturbation argument to locate the LB maximizer.
- **Piecewise linear / USC minimax**: F(A) = min_XY(val) is USC in A, attains max on compact set; show max = G_n by smoothing.
- **Induction with adaptive XY strategy**: direct but requires careful case analysis on the regime.
- **Measure-form potential function**: A = ∫ 1[N odd] dx; greedy XY maximizes parity-flip coverage per cut.

### Knowledge-base entries to use
- **Invariants & monovariants**: the potential function A as a monovariant under XY's cuts.
- **Induction (general proof methods)**: inductive step with adaptive strategy.
- **Piecewise-concavity smoothing**: LB's problem is a maximin; the LB config space is compact; F is piecewise linear (min of finitely many linear functions of LB's config) — apply exchange argument.
- **Extreme value theorem / Lagrange multipliers on compact manifold**: F attains its max on the simplex (compact).
- **Constructive vs. existence**: the upper bound is existential (XY HAS a strategy), not constructive for arbitrary configs; extremal approach avoids needing the construction explicitly.

### Analogous past problems (cruxes)
1. **aimo-0117** (combinatorics, games-and-strategy): Jesse assigns values as a two-sided geometric (dyadic) sequence so the largest exceeds the sum of all others. Crux move: "single largest value strictly exceeds the sum of all the others." Direct analogy: this is exactly LB's construction (G_n has 2^n > 2^{n-1}+...+1 = 2^n-1). The UPPER BOUND analogy would be Tjeerd's counter-strategy — but in aimo-0117 the problem is about which box holds the maximum, not about minimizing a share. Partial analogy; useful for the lower bound not the upper bound.
2. **aimo-0262** (Cinderella/Stepmother buckets, combinatorics, games-and-strategy): Cinderella (the "defender") maintains an invariant family of configurations by responding to the Stepmother's moves. Crux: "self-reproducing invariant family" where each legal move restores the invariant. Analogy: XY's upper-bound strategy can be viewed as maintaining an invariant (A ≤ 1/D is preserved or decreasing after each XY cut). Mechanism candidate: XY's cuts maintain the invariant "A(current config) ≤ c(k) where k = remaining XY cuts." The Cinderella proof structure (exhibit invariant, show it's restorable) is directly applicable if such an invariant can be found.
3. **aimo-0988** (algebra, inequalities-SOS-and-convexity): "Reduce a mean-of-n inequality to iterated two-variable smoothing by adjoining the target mean itself as an extra variable." Crux: iterated pairwise smoothing telescopes to the desired bound. Analogy: for Claim U, the smoothing lemma is a pairwise exchange (adjacent pair perturbation) that shows G_n is optimal. The "iterated two-variable smoothing" technique from aimo-0988 maps onto GAP S1 in the extremal-smoothing approach.

### Prior progress
Status: partial. Both top approaches (geometric-selfsimilar, alternating-sum-value) share GAP AU as an open gap. Lower bound Case 1 proven, Case 2 open. n=1 upper bound proven fully. Tightness computed. The claim U currently written in geometric-selfsimilar is incorrectly formulated (see critical bug above) — this must be corrected before the approach can close.

### Dead ends (do not retry)
- "XY concentrates all n cuts on A_1" as a universal strategy — FALSE for some configs.
- Shadow strategy alone — fails for A_1 > c(n) and for A_1 < 1/2.
- Halve-A_1 first step — fails for near-equal, near-flat configs (A_1/A_2 < 2 cases).
- Top/bottom decomposition of A (as in alternating-sum-value dead-end) — numerics show A_top - 2B can be << 0, making term-by-term bounds impossible.

### Small-case / intuition notes (all conjecture unless noted)
- The "shadow strategy" + "pair-up" combination covers ALL n=2 configs (verified by grid): shadow covers A_1 ≤ c(2); pair-up covers the rest. This two-case case analysis might be the cleanest direct proof for n=2.
- For general n: the inductive argument needs "after XY's first shadow cut, the resulting config falls under the (n-1)-IH." This requires A_1/2 ≤ c(n-1)·T_{rest} where T_{rest} = 1-A_1 (so the residual r = 2A_1-1 is small enough for (n-1) more cuts). This is exactly the condition A_1 ≤ c(n) (proved by direct algebra: 2A_1-1 ≤ 1/D_{n-1} iff A_1 ≤ c(n)). So shadow + induction closes A_1 ≤ c(n) case cleanly for all n. Only the A_1 > c(n) sub-case is open.
- For A_1 > c(n): since A_2+...+A_m = 1-A_1 < 1-c(n) = (2^n-1)/D < 2^{n-1}/D, all non-A_1 pieces are very small. XY making n equal cuts in A_1 → (n+1) pieces of A_1/(n+1) each. The (n+1) equal pieces have A = A_1/(n+1) (odd count of equal pieces), so val = (1+A_1/(n+1))/2. This is ≤ c(n) iff A_1 ≤ (2c(n)-1)·(n+1) = (n+1)/D. For n=1: A_1 ≤ 2/3 (= c(1)), so equal split closes n=1 for A_1 ≤ c(1). For n=2: need A_1 ≤ 3/7 < c(2) = 4/7. So the equal split of A_1 only closes a sub-range. Need a better strategy for large A_1. — CONJECTURE.
- For A_1 → 1 (single dominant piece), XY makes n equal cuts in A_1: A(final) = A_1/(n+1) → 0, val → 1/2 < c(n). So the extreme case is easy. The hardest case is A_1 = c(n) (geometric config).
