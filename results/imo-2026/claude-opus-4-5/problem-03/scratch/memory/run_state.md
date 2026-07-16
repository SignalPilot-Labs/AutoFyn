## Goal

**Problem:** IMO 2026 P3 — Liu Bang vs Xiang Yu stick division game
**Task:** compute_and_prove (find the answer c as an expression in n, prove it)
**Metric:** Status in current.md (unsolved → partial → solved)
**Eval:** Check `results/imo-2026-03/current.md` Status field and approach rankings
**Baseline:** unsolved, 0 approaches
**Target:** solved with complete rigorous proof and explicit answer

## Goal Updates

## Eval History

- Round 1 start: Status=unsolved, 0 approaches, no ranking
- Round 1 end: Status=partial. CRITICAL FINDING: The claimed answer c(n)=2^n/(2^{n+1}-1) is WRONG for n≥2. Arithmetic configuration (1:2:3:...:(n+1)) beats geometric. Verified: n=2 arithmetic gives 7/12 > 4/7 geometric. Greedy optimality lemma CERTIFIED. Two approaches built: geometric-direct (CHANGES REQUESTED), induction-on-n (RETHINK - upper bound proof fatally flawed).
- Round 2 end: Status=partial. **CRITICAL CORRECTION**: Round 1's "arithmetic beats geometric" claim was WRONG. The error: Round 1 computed XY's response as equal splits, but XY's OPTIMAL response is asymmetric. With optimal XY: arithmetic [1/6,1/3,1/2] gets only 1/2 (not 7/12). The answer c(n) = 2^n/(2^{n+1}-1) IS CORRECT. Two approaches built: geometric-direct (CHANGES REQUESTED, lower bound rigorous, upper bound needs general-n proof), minimax-saddle-point (CHANGES REQUESTED, more gaps in upper bound). ANNOTATION: BREAKTHROUGH — correction of Round 1 error.
- Round 4 end: Status=partial. **IMPROVED**: Upper bound Case A (P_1 ≤ L_0 = 1/(2^{n+1}-1)) now FULLY PROVED for all n via pairing construction. LB = 1/2 + P_1/2 ≤ c(n). Lower bound remains complete. Case B (P_1 > L_0) verified for n=2,3 but lacks closed-form proof for general n. geometric-direct verdict: CHANGES REQUESTED.
- Round 5 end: Status=partial. **IMPROVED**: n=3 Case B FULLY PROVED via three explicit strategies (S1, S2, S3). New lemmas certified: Singleton-Pair Formula, Sum-Slack Bound for n=3. Complete rigorous proof now exists for n=1,2,3. Case B for n≥4 remains OPEN (computationally verified, algebraic proof requires generalizing the sum-slack argument). geometric-direct verdict: CHANGES REQUESTED. ANNOTATION: IMPROVED — n=3 Case B closed.
- Round 6 end: Status=partial. **IMPROVED**: n=4 interval coverage framework PROVED. Five strategies (S4, S5, S6, B, PP) cover all Case B configs. Key result: gap width alpha-1 < -2/3 < 0 (S5 and B intervals overlap). S5/S6 have explicit 3-mark constructions; B/PP need 4-mark constructions (computationally verified to exist but not algebraically characterized). New lemmas: n=4 Case A Constraint (alpha < 1/3), n=4 Gap-Width Lemma. geometric-direct verdict: CHANGES REQUESTED. ANNOTATION: IMPROVED — n=4 framework established, explicit constructions partial.
- Round 7 end: Status=partial. **BREAKTHROUGH**: n=4 Case B FULLY PROVED. The "B/PP need 4 marks" claim was FALSE (parameterization mismatch). Explorer proved B and PP use the SAME 3-mark construction (unified as "BPP"): cut P_4 at P_3, cut d_3 at P_1, halve P_5. Singletons = {P_2, d_3-P_1}. Formula LB = 1/2 + |P_1+P_2-d_3|/2 <= c(4) for all BPP range configs. Complete rigorous proof now exists for n=1,2,3,4. New certified lemmas: BPP Unified Construction, BPP Range Bound. geometric-direct verdict: CHANGES REQUESTED (n>=5 still open). ANNOTATION: BREAKTHROUGH — n=4 closed with 3-mark constructions.

- Round 9 end: Status=partial. **IMPROVED**: New rigorous result — Halve+IH Strategy PROVED for all n≥2. When P_{n+1} ≥ c(n), XY halves P_{n+1} and applies (n-1)-game IH, giving LB ≤ c(n) via identity c(n-1)·(1-c(n)) = c(n)/2. **ERROR FIXED**: "Case B Trivial" claim (0 XY marks) was WRONG for n≥2 — removed and replaced with Halve+IH. Proof structure updated: each n=2,3,4 proof now explicitly handles P_{n+1} ≥ c(n) via Halve+IH, and P_{n+1} < c(n) via sum-constraint forcing d_j < L_0. n=5: 11 strategies identified, computationally verified (max slack 0.9575 < 1), algebraic proof OPEN. geometric-direct verdict: CHANGES REQUESTED (structural fixes applied this round). ANNOTATION: IMPROVED — new inductive lemma proved.

- Round 10 end: Status=partial. **CRITICAL FINDING**: The B_small sub-case (P_{n+1} < c(n) with P_1 > L_0) has REVERSED sum constraint compared to B_large. The 11 n=5 strategies were tested on the WRONG region (B_large, which Halve+IH already handles). New n=5 strategies identified: S_vertical_last, Cut-P6-at-P3, Cut-P6-at-P5, Cut-P4-at-P1. With 15 strategies, ~99.5% computational coverage achieved. **GAP FOUND IN N=4 PROOF**: The stated S6/S4/S5/BPP strategies miss configs where d_j < L_0 (e.g., beta < 0). Need to add V1/V2/V3/V4 strategies (halve all except {P_j, P_{j+1}} when d_j <= L_0). Fix is straightforward but current proof is incomplete. ANNOTATION: IMPROVED — found B_small structure, identified new strategies; REGRESSION — discovered n=4 gap.

- Round 11 end: Status=partial. **BREAKTHROUGH**: n=4 Pigeonhole Lemma CERTIFIED. The V_j + Pigeonhole + Pairwise framework CLOSES n=4: (1) V_j strategies handle any d_j ≤ L_0, (2) Pigeonhole guarantees some pairwise ≤ 1 when all d_j > L_0 (min weighted sum > 20 > 16, contradiction), (3) 10 Pairwise strategies cover all pairs. Written constructions have minor errors (wrong piece counts in some cases) but coverage computationally verified 100%. **n=5**: New approach n5-five-mark created. V_j + Pairwise strategies PROVED. Key finding: Pigeonhole FAILS for n=5 (min weighted sum > 35 but constraint = 42, so "all pairwise > 1" region is NON-EMPTY but bounded: g ∈ (1, 1.2)). Counterexample found for proposed A/E/F strategies. Type 3 strategies (2 cuts + 3 halves) computationally cover 100% but algebraic proof OPEN. ANNOTATION: BREAKTHROUGH — n=4 closed via Pigeonhole; IMPROVED — n=5 structure clarified.

- Round 12 end: Status=partial. **BREAKTHROUGH**: n=5 (2,2,1) strategy discovered. Key findings: (1) Type 3 strategies (2 cuts + 3 halves on 5 different pieces) are INSUFFICIENT (~95% coverage, failures near α→0). (2) The (2,2,1) strategy family (2 marks on each of 2 pieces + 1 halve) achieves 100% coverage on bounded region. (3) All 63 boundary vertices at g=1 verified (worst margin 0.0057). (4) Boundary reduction: at g=1 exactly, Pairwise strategies apply (adjacent ranks give |diff|=1). **Certified lemmas:** V_j Strategy (n=5), Bounded Region characterization. **Gap found:** Pairwise example (beta,gamma) construction is incorrect. Algebraic (2,2,1) proof OPEN (63-vertex finite check needed for rigor). ANNOTATION: BREAKTHROUGH — identified (2,2,1) as solution; IMPROVED — bounded region fully characterized.

- Round 14 end: Status=partial. **IMPROVED**: n=5 Pairwise constructions corrected. 10 non-adjacent pairs PROVED with "chop-at-adjacent" method (0 failures each). 5 adjacent pairs covered by (2,2,1) fallback. 63-vertex algebraic framework established: wrs in {35-41}, v_0 = (42-wrs)/21, 63 total vertices. Three worked algebraic examples provided (wrs=35, 41, hardest vertex). Continuity/compactness argument for interior stated. **New certified lemma:** Pairwise Strategy - 10 Non-Adjacent Pairs (n=5). **Remaining gap:** algebraic enumeration of remaining 60 vertices (or formal justification that computational verification of 63 finite cases constitutes proof). ANNOTATION: IMPROVED — Pairwise fixed, 63-vertex framework complete, algebraic examples provided.

- Round 16 end: Status=partial. **IMPROVED**: CORRECTED vertex count from 63 to 93. The bounded region has 62 AP-type vertices (g=1 boundary, wrs∈{36,...,41}) + 31 Z-type vertices (v₀=0 boundary, r_alpha=0). All 93 computationally verified (min margin 0.0026). **New certified lemma:** wrs=35 Z-type Exact Construction — pieces [1/63, 16/315, 11/105, 8/45, 17/63, 8/21], 4-mark (2,1,1) strategy creates 5 perfect pairs, LB = 1/2 exactly, margin = 1/126. **GAP IDENTIFIED**: The compactness argument claiming "max of piecewise linear at vertex" is INVALID for f = min_strategy LB (non-convex piecewise linear). Interior coverage needs LP-based verification or full algebraic enumeration. n5-five-mark verdict: CHANGES REQUESTED. ANNOTATION: IMPROVED — 93-vertex framework complete, wrs=35 exact proof certified; gap found in compactness argument.

- Round 17 end: Status=partial. **IMPROVED**: Fixed the false "max at vertex" claim. Two approaches built: n5-lp-direct (LP coverage) and n5-convex-coverage (revised n5-five-mark). **New certified lemma:** LB(x,T) Convexity — for each fixed (2,1,1) template T, LB(x,T) = sum of 5 largest of 10 linear pieces is convex in x (max over 252 linear functions = convex). **Key structural clarification:** 62 AP-type vertices (g=1) are handled by Tier 2 pairwise strategies with LB = c(5) exactly; only 31 Z-type vertices (v₀=0, r_alpha=0) genuinely need Tier 3 verification. **Correction:** Min Z-type margin is 1/378 (not 1/2520). All 31 Z-type vertices verified with exact rational arithmetic. Interior sampling: 66/66 valid points covered (min margin 0.00588). **GAP REMAINS:** Interior coverage is computationally supported (100% coverage in sampling) but NOT rigorously proven. Need LP verification or algebraic argument. Both approaches CHANGES REQUESTED. ANNOTATION: IMPROVED — LB convexity lemma certified, structural corrections complete; gap narrowed but not closed.

## Rules

ALWAYS: Verify computational claims independently before accepting an answer as correct.
ALWAYS: When two builders disagree on the answer, the reviewer must resolve the contradiction.
NEVER: Assume the "claimed answer" from problem folklore is correct without verification.
ALWAYS: Test XY's response with ASYMMETRIC splits, not just equal splits.
ALWAYS: For game-theoretic problems, verify the minimax by searching over ALL opponent responses.
NEVER: Claim "XY uses 0 marks" limits LB to a single piece for n≥2 (LB picks multiple pieces).
NEVER: Claim "always split P_1" works universally — fails when P_1 < c(n) with geometric sub-game.
ALWAYS: The correct upper bound case structure is based on P_1 vs L_0, not P_1 vs c(n).
ALWAYS: In Case B, XY typically uses n-1 marks (creating 2n pieces) not n marks (creating 2n+1 pieces).
NEVER: Use "Case B Trivial (0 marks)" claim for n≥2 — LB picks ceil((n+1)/2) pieces with 0 XY marks, not just 1. (Round 9)
ALWAYS: For P_{n+1} ≥ c(n), use Halve+IH Strategy (1 + (n-1) = n marks). For P_{n+1} < c(n), use Singleton-Pair strategies. (Round 9)
ALWAYS: B_small (P_{n+1} < c(n)) has REVERSED sum constraint direction from B_large (P_{n+1} >= c(n)). Do not apply B_large arguments to B_small. (Round 10)
ALWAYS: When any d_j <= L_0, use V_j strategy (halve all except {P_j, P_{j+1}}) BEFORE checking the "all d_j > L_0" case. (Round 10)
ALWAYS: For n=4, use Pigeonhole Lemma: min weighted sum with all pairwise > 1 is > 20 > 16, so some pairwise must be ≤ 1. (Round 11)
ALWAYS: For n=5, Pigeonhole FAILS (min > 35 but constraint = 42). The "all pairwise > 1" region exists but is bounded (g ∈ (1, 1.2)). (Round 11)
ALWAYS: For n=5 bounded region, use (2,2,1) strategy (2 marks on each of 2 pieces + 1 halve), NOT Type 3 (2 cuts + 3 halves on 5 different pieces). Type 3 is insufficient (~95%). (Round 12)
ALWAYS: At g=1 boundary, Pairwise strategies already apply (adjacent sorted ranks give |diff|=1). (2,2,1) only needed for strict interior g > 1. (Round 12)
NEVER: Trust the (beta, gamma) Pairwise example in n5-five-mark — it's incorrect (wrong singletons). (Round 12)
ALWAYS: For n=5 bounded region, correct vertex count is 93 (62 AP-type + 31 Z-type), NOT 63. The wrs=35 AP-type is a BOUNDARY point handled by Tier 2. (Round 16)
NEVER: Claim "max of piecewise linear on polytope is at vertex" for f = min_strategy LB — this is FALSE for non-convex piecewise linear functions. Use LP coverage verification or full algebraic enumeration instead. (Round 16)
ALWAYS: For each fixed (2,1,1) template T, LB(x,T) is CONVEX in x (sum of 5 largest = max over 252 linear functions). Use this for coverage arguments. (Round 17)
ALWAYS: AP-type vertices (62, g=1 boundary) are handled by Tier 2 pairwise strategies with LB = c(5) exactly. Only 31 Z-type vertices (v₀=0, r_alpha=0) need Tier 3 verification. (Round 17)

## State

**Done:**
- Round 1-16: See above.
- Round 17: Removed false "max at vertex" claim. Proved LB(x,T) Convexity lemma (CERTIFIED). Clarified AP-type vs Z-type vertex structure. Built n5-lp-direct and n5-convex-coverage approaches. Verified all 31 Z-type vertices with exact rational arithmetic (min margin 1/378). Computational sampling supports interior coverage (66/66 points, min margin 0.00588).

**Broken:**
- N=4 written proof: Some pairwise constructions have wrong piece counts (low priority, coverage verified).
- N=5 interior coverage: LP verification or algebraic argument still needed (computational evidence is strong but not rigorous proof).

**Next:**
- Round 18: Execute the LP coverage verification rigorously. Show that for every point x in Tier 3, some (2,1,1) template achieves LB(x,T) ≤ c(5). Options: (a) formulate LP and prove infeasibility of "uncovered" system, (b) identify finite set of templates whose convex coverage sets provably cover Tier 3, (c) full algebraic proof for all 31 Z-type vertices + convexity extension argument.
