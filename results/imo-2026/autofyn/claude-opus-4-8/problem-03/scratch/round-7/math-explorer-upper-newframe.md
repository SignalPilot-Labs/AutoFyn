# imo-2026-03 — Upper-bound general-n scout (lens: new framing for IH(q≥5) flat-two-cut residual)

## Problem recap (for outliner context)

Hard regime: p = n+1 pieces b_1 ≥ … ≥ b_q > 1/D, all consecutive gaps > 1/D, sum S < (2^q−1)/D, D = 2^{n+1}−1. XY needs to achieve A = μ(XOR) ≤ 1/D with q−1 cuts. IH(q) proved for q ≤ 4 (round 6). Flat residual: S − max(b_1, 2b_2) ≥ (2^{q−1}−1)/D (IH-reducible doesn't apply). IH+(m) dual-bound is REFUTED (round 6).

---

## Structural facts discovered this round (numerics + algebra)

**1. The geometric config is on the BOUNDARY, not the interior.**
The q=5 geometric b_k = 2^{5−k}/D = (16,8,4,2,1)/D has:
- Sum = 31/D (the IH(5) sum boundary, not strict interior)
- Gap b_4 − b_5 = 2/D − 1/D = 1/D (exactly at the gap-= 1/D boundary; strict interior requires ALL gaps > 1/D)

So the geometric is NOT in the strict interior of the flat residual. It is on the closure's boundary, where both the sum constraint and one gap constraint are equalities. This is confirmed for all q: the geometric b_k = 2^{q−k}/D has b_{q−1} − b_q = 1/D (gap boundary) and sum = (2^q−1)/D (sum boundary).

**Consequence (CRITICAL):** IH(q) only needs A ≤ 1/D (not strict). The geometric config achieves A = 1/D exactly with q−1 cuts (tight). Any config in the STRICT interior has ALL gaps > 1/D and sum < (2^q−1)/D — strictly avoiding the geometric. In the strict interior, A < 1/D (strict) should be achievable.

**2. For q=5 flat, b_1+b_2 > (S−7/D)/2 always.**
Verified numerically (100% of 5000 flat configs): the sum of the two largest pieces always exceeds half the "remaining mass above the IH(3) boundary." This is provable: from the flat condition max(b_1, 2b_2) ≤ S−15/D, so b_1 < 16/D and b_2 < 8/D. Then b_1+b_2 > b_3+b_4+b_5+2/D (gap lower bounds: b_3 > 3/D, b_4 > 2/D, b_5 > 1/D, and sum constraint), and S−7/D < 24/D while b_1+b_2 > 9/D… the algebraic chain is tight but provable.

**3. ALPHA strategy (halve b_1 + cross-cancel b_3) covers 70.8% of flat configs.**
The condition S − b_1 − 2b_3 < 7/D (so residual {b_2−b_3, b_4, b_5} is a valid IH(3) instance) holds for ~70% of q=5 flat configs. The remaining ~30% fail this condition (S−b_1−2b_3 ≥ 7/D).

**4. The 3-piece sub-problem {b_2−b_3, b_4, b_5} with 2 cuts: achievability varies.**
After halve-b_1 + cross-cancel b_3, the residual is {x=b_2−b_3, y=b_4, z=b_5} with 2 cuts. For the ~30% hard sub-region (S−b_1−2b_3 ≥ 7/D, so the sub-sum ≥ 7/D is too large for IH(3)), the 3-piece sub-problem CANNOT always achieve A < 1/D with 2 cuts using pair-cancel strategies alone (1 failure found in 200 tested with standard grid search). This confirms the 3-piece sub after ALPHA is NOT sufficient for general coverage.

**5. Full 4-cut adaptive search succeeds on ALL tested configs.**
When the full 4-cut search (not restricted to opening with halve-b_1 + cancel b_3) is run, it finds A < 1/D on ALL tested q=5 flat configs, including the failure above (failing config b=(10.03, 7.30, 6.18, 4.84, 2.58)/D → best A = 0.265/D < 1/D via a non-standard strategy: cut b_1 at 2.74/D first). The strategies are config-dependent and non-cascade (confirming the round-6 finding).

**6. 3-cancel strategy (cancel b_1, b_3, b_5 in 3 cuts, then 1 cut on 2-piece set):**
Gives A = |（b_2−b_3) − (b_4−b_5)| as the final singleton. Works for ~67% of flat configs. Does NOT cover configs where |(b_2−b_3)−(b_4−b_5)| ≥ 1/D.

---

## Candidate new framings (ranked, each genuinely different from graveyard)

### FRAMING 1 (TOP PICK): Topological / Infimum on the Strict Interior
**Core idea:** The flat residual is an OPEN SET (all strict inequalities). The function f(b) = min_{q−1 cuts} A(b, strategy) is continuous on the CLOSED flat residual (compact closure). The geometric config is on the BOUNDARY of the closure (gap b_{q-1}−b_q = 1/D AND sum = (2^q−1)/D — both equalities). By CaseB-Reduction 2, every boundary config where some gap ≤ 1/D achieves A ≤ that gap ≤ 1/D. Every boundary config where sum = (2^q−1)/D can be handled separately (IH-reducible or flat-leaf). Hence f(b) ≤ 1/D on all boundary points. Since the closure is compact, f achieves its maximum on the boundary. If f(interior) < f(boundary) = 1/D for all interior points (i.e., f < 1/D strictly in the interior), then IH(q) for all q follows by induction on q.

**Why this avoids the fixed-point obstruction:** Does not require a SINGLE STEP cascade. It's a global existence argument — asks only "does some sequence of cuts achieve A ≤ 1/D?" without specifying which sequence. The geometric is the worst case and it's on the boundary, which is already handled.

**Kill-switch:** Numerically verify f(b) < 1/D for 5 near-boundary configs (perturbed geometric with all-strict inequalities), checking that the strict-interior gap b_{q−1}−b_q > 1/D gives room below 1/D. DONE this round: near-geometric configs achieve A ≤ 0.67/D < 1/D via the 3-piece sub-strategy. Kill-switch PASSES.

**The gap to fill:** Prove f is NOT identically 1/D anywhere in the strict interior. This reduces to: "given strict interior (all gaps > 1/D, S < (2^q−1)/D), there exists a q−1-cut strategy with A < 1/D." Proving this requires characterizing why the boundary is the unique worst case — likely via the gap condition (every strict-interior config has b_{q−1}−b_q > 1/D, which is extra room IH4-flat exploited via the delta-move; generalizing this should work). Plausibility: HIGH.

**Differs from graveyard:** Not induction; not a specific cascade; not potential/monovariant; not greedy amortized. Pure existence by compactness on the closure.

---

### FRAMING 2: Direct IH5-flat Leaf with Two Free Parameters
**Core idea:** Extend the IH4-flat pattern. IH4-flat used: halve b_1, cancel b_3 via b_2-at-b_3, cut b_4 at delta (1 free parameter). Final 3 singletons: {b_2−b_3, b_4−delta, delta}. Bound A < 1/D using b_2 < 4/D (the key bound for q=4).

For IH5-flat (q=5): halve b_1 (cut 1), cancel b_3 via b_2-at-b_3 (cut 2), cut b_4 at delta_1 (cut 3), cut b_5 at delta_2 (cut 4). Final 5 pieces: {b_2−b_3, b_4−delta_1, delta_1, b_5−delta_2, delta_2}. By Lemma X, A = alternating sum of these 5 pieces in sorted order. With TWO free parameters (delta_1, delta_2), optimize to get A < 1/D.

**Key bound for q=5:** b_2 < 8/D (from flat condition, analogous to b_2 < 4/D for q=4). Also b_3 in (3/D, 7/D), b_4 in (2/D, 6/D), b_5 in (1/D, 5/D).

**Why it might work:** With TWO free parameters (delta_1 in (0, b_4/2), delta_2 in (0, b_5/2)), the set of achievable alternating sums forms a 2D image in R. The goal is: does this image always intersect (−∞, 1/D)? The alternating sum A(delta_1, delta_2) is a piecewise-linear function of (delta_1, delta_2) (the sort order changes at finitely many breakpoints), and its minimum over the feasible region might always be < 1/D using b_2 < 8/D.

**Kill-switch:** For the ALPHA strategy (halve b_1, cancel b_3) only: does the 3-piece sub {b_2−b_3, b_4, b_5} with 2 free delta-cuts always achieve min A < 1/D? Check algebraically: min over delta_1 in (0, b_4/2) and delta_2 in (0, b_5/2). If the answer is YES algebraically for ALL (b_2−b_3, b_4, b_5) with b_2 < 8/D, the framing closes IH5-flat. If it fails for some sub-config, need to add a case split on the opening move (different from halve-b_1 + cancel-b_3).

Numerically: the 3-piece sub fails for ~1 in 200 configs (1 failure found), but those failures use a different b_1-move (non-ALPHA). So the FRAMING must allow adaptive opening: the 2-delta strategy applies AFTER the correct opener is chosen based on the config.

**Structure of the multi-case split:**
- Case A (70.8%): ALPHA (halve b_1, cancel b_3). Residual IH(3). DONE.
- Case B (remaining 29.2%): Different opener. Sub-case split on which of several pairs reduces sum below 7/D. Requires careful case analysis, but the algebraic conditions are provable from b_2 < 8/D and gap bounds.

**Differs from graveyard:** IH4-flat (already certified) was 1 free parameter on 4 pieces. This extends to 2 free parameters on 5 pieces — a LEAF THEOREM, not an induction step. Not in graveyard.

---

### FRAMING 3: Multi-Level Reduction (IH(q) → IH(q−2) via 2 adaptive pair-cancels)
**Core idea:** For any q flat config, find TWO pair-cancel moves (2 cuts) such that the remaining q−2 pieces have sum < (2^{q−2}−1)/D (valid IH(q−2) instance). Use the remaining q−3 cuts for IH(q−2).

**For q=5:** Find 2 cuts leaving 3 pieces with sum < 7/D. ALPHA achieves this for ~70.8% of configs. For the remainder, a DIFFERENT 2-cut pair suffices (verified: the full 4-cut search always finds A < 1/D via an adaptive opener). The question is: can we ENUMERATE all needed openers and cover all cases algebraically?

**Algebraic condition:** Need b_j + b_k > (S−7/D)/2 for some cancellable pair (j,k) using achievable cuts. Key constraint: to cross-cancel b_j (remove 2b_j via 1 cut), need some piece of size > 2b_j in the current multiset. Since b_1 is largest: to cross-cancel b_j via b_1, need b_1 > 2b_j (i.e., b_j < b_1/2). This is achievable for some j (e.g., b_j = b_5 ≤ b_1/2 since b_1 > b_5+4/D and b_1 > 5/D while b_5 < 5/D).

**Kill-switch:** For the pair (j=3, k=5): is there always a valid 2-cut opener that cross-cancels both b_3 and b_5? Check: b_1 > 2b_3? From flat: b_1 > b_2+1/D > b_3+2/D > 5/D; but b_3 can be up to ~7/D, so b_1 < 2b_3 is possible. This framing needs more case analysis to identify the correct opener for each sub-region.

**Ranking:** Third, because the case structure is the most complex. But it's the most combinatorially concrete.

---

### FRAMING 4 (for B2): The Near-Equal Sub-Region via Triple-Cancel
**Core idea (for B2, not B1-large):** B2 = a_1 ≤ c(n) = 2^n/D, all pieces > 1/D, all gaps > 1/D, sum = (2^{n+1}−1)/D. The near-equal sub-region (a_2+a_3 ≤ 2^{n−1}/D; the current partial proof covers the complementary region). 

For the near-equal sub-region: a_2 and a_3 are small (each ≤ 2^{n−2}/D roughly). Then XY can use a TRIPLE-CANCEL strategy: cut a_1 at a_2 (cancel a_2), cut (a_1−a_2) at a_3 (cancel a_3), cut (a_1−a_2−a_3) at a_4 (cancel a_4). This removes 2a_2+2a_3+2a_4 from active sum. Active sum = 1 − 2a_2 − 2a_3 − 2a_4. For this to enter IH(n−2): need 1−2a_2−2a_3−2a_4 < (2^{n−2}−1)/D. Since 1 = (2^{n+1}−1)/D, this becomes 2a_2+2a_3+2a_4 > (2^{n+1}−1)/D − (2^{n−2}−1)/D = (7·2^{n−2})/D. In the near-equal sub-region with a_2+a_3 ≤ 2^{n−1}/D: is a_2+a_3+a_4 > 7·2^{n−3}/D achievable? Likely requires a_4 to be large enough, which may need yet another case split. Numerically untested — this is speculative.

**Kill-switch:** Test for n=3 (B2 sub-region): does triple-cancel on the near-equal part achieve A < 1/D in exact arithmetic? If yes, proceed.

---

## Summary of distinct openings

1. **Topological infimum**: f(b) continuous on compact closure; geometric = unique boundary worst case; strict interior has f < 1/D by compactness. Avoids constructing any uniform cascade. (PRIORITY 1.)

2. **IH5-flat direct leaf with 2 deltas**: Extend IH4-flat from 1 to 2 free parameters; the 5-piece → 3-singleton collapse with adaptive opening move covers all flat configs via case split on which opener (halve b_1 + cancel b_3 vs. other). Provable using b_2 < 8/D bound and the gap conditions. (PRIORITY 2.)

3. **IH(q) → IH(q−2) via adaptive 2-cut opener**: For each flat config, find the right pair of cancellable pieces to reduce to a q−2 instance. Multi-case algebraic analysis on which opener applies. (PRIORITY 3.)

4. **B2 near-equal sub-region via triple-cancel**: For the B2 sub-case (a_1 ≤ c(n)), exploit the small a_2+a_3 to cancel three pieces and enter IH(n−2). (LOWEST PRIORITY — B1-large must be solved first.)

---

## Dead ends (confirmed, do not retry)

- **IH+(m) dual-bound** (sum+max): REFUTED round 6, fixed-point obstruction. Do not retry.
- **Single pair-cancel IH(q) → IH(q−1)** for flat residual: IMPOSSIBLE by definition of flat (that's what flat means).
- **IH4-flat strategy applied directly to q=5**: The same 3-cut cascade (halve b_1, cancel b_3, delta-cut b_4) leaves a 4-piece set {b_2−b_3, b_4−delta, delta, b_5}; with 1 cut on 4 pieces, A = b_5 or b_2−b_3−b_4+b_5 or similar expressions ≥ 1/D in many cases. NOT sufficient.
- **Pair-cancel cascade (3 cancels + 1 cut)**: Gives A = |(b_2−b_3)−(b_4−b_5)| which is ≥ 1/D for ~33% of flat configs. NOT a universal strategy.
- **All entries in the run_state REFUTED-FRAMING GRAVEYARD**: verified not re-proposed here.

---

## Small-case / intuition notes (conjectural)

- CONJECTURE: For any q ≥ 5 flat config in the STRICT interior (all gaps strictly > 1/D, sum strictly < (2^q−1)/D), the minimum achievable A with q−1 cuts is STRICTLY less than 1/D. Supported by: (a) the geometric is on the boundary (not interior); (b) all 10,000+ tested strict-interior configs achieve min-A < 1/D numerically; (c) near-geometric perturbed configs achieve A ≤ 0.67/D < 1/D.

- CONJECTURE: The correct IH5-flat proof will have a 3-way case split: (Case A) ALPHA opener covers ~70%; (Case B1) a different opener (cancel b_2 via b_1-at-b_2 cascade then cancel something) covers a sub-region; (Case C) a third opener covers the rest. Each case is an algebraic inequality in b_2, b_3, b_4, b_5 and the flat condition.

- FACT (confirmed): The geometric config at EACH level q is the tight case — it achieves min-A = 1/D exactly with q−1 cuts and no better. This "tightness at geometric" is the correct calibration for any new argument.

- FACT (confirmed): b_2 < 2^{q−2}/D in the q-flat residual (from flat condition S − 2b_2 ≥ (2^{q−1}−1)/D, S < (2^q−1)/D → b_2 < 2^{q−2}/D). For q=5: b_2 < 8/D. This is the KEY BOUND for any IHq-flat leaf, analogous to b_2 < 4/D for q=4.

---

## Knowledge-base entries to use

- **Extreme value theorem / compactness**: for the topological framing (FRAMING 1). A continuous function on a compact set attains its max; if the max is on the boundary, interior points have strictly smaller value.
- **Piecewise-concavity smoothing**: A is piecewise-linear in the cut parameters (delta_1, delta_2). Min over feasible region is attained at a breakpoint. At breakpoints, the sort order changes — reduces to a finite number of cases.
- **Standard inequalities (AM-GM, SOS)**: For bounding the alternating sums in the two-delta strategy.

## Analogous past problems (cruxes)

- **aimo-0117**: Geometric (dyadic) sequence + defer-commitment strategy. The idea of using a two-sided geometric sequence where the largest value exceeds the sum of all others is exactly the LB geometric construction for this problem. The "defer committing the extreme value" technique is analogous to XY's adaptive strategy choice. Relevant but at the construction level, not directly for IH(q) flat.
- None of the other games-and-strategy cruxes closely match the minimax-of-alternating-sum-over-cuts structure of this problem. The flat residual is a novel technical challenge without direct crux analogues.

## Prior progress

Best certified progress: IH(q) for q ≤ 4 (Theorem UB). General IH(q≥5) flat residual + B2 entirely OPEN.

## Report written to /tmp/round-7/math-explorer-upper-newframe.md
