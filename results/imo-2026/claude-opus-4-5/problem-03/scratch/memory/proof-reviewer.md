# Proof Reviewer Memory

## Rules

ALWAYS: Independently verify computational claims by running Python code, not trusting the builder's assertions (because the induction-on-n claim of "verified computationally" was wrong, round 1)

ALWAYS: When two approaches contradict each other on the answer, resolve the contradiction computationally before rendering verdicts (because geometric-direct vs induction-on-n had opposite claims about correctness, round 1)

NEVER: Accept "interleaving" or "pairing" arguments without verifying the exact sorted order for the specific configuration (because induction-on-n's interleaving argument failed for non-geometric configs, round 1)

ALWAYS: For game theory problems, check that upper bound proofs actually apply to ALL player strategies, not just the claimed-optimal one (because induction-on-n only verified XY's response to geometric LB, not arithmetic LB, round 1)

ALWAYS: When a previous round claims "config A beats config B", verify against the OPPONENT'S OPTIMAL response, not a specific response (round 1 claimed arithmetic beats geometric, but round 2 found this was wrong - arithmetic loses to XY's optimal split, round 2)

NEVER: Accept "extends naturally to general n" as a proof for all n. Demand the formal induction or a rigorous argument (both approaches had this gap in upper bound, round 2)

ALWAYS: When verifying pairing constructions, check boundary cases (e.g., when r = P_1 exactly) and verify the claimed strict inequalities hold (round 4)

ALWAYS: Use comprehensive XY strategy search when verifying upper bounds computationally - simple strategies (halving, 0 marks) may miss the optimal XY response (round 4)

ALWAYS: When verifying a Singleton-Pair Formula or similar structural claim, test edge cases where singletons equal pair values - the formula may or may not hold depending on how ties are handled (round 5)

ALWAYS: For contradiction proofs involving multiple constraints (P_1 > L_0, d_1 > L_0, etc.), verify the algebra by substituting the constraint boundary values and checking that the claimed contradiction arises (round 5)

ALWAYS: When a proof claims a strategy creates "k pairs + m singletons", verify the actual piece count and structure by enumerating the pieces (round 6 - B strategy claimed 3 pairs but only had 2)

ALWAYS: Check that the proof uses ALL available resources (marks, moves, etc.) when needed - using fewer than available is fine IF sufficient, but verify sufficiency (round 6 - 3 marks insufficient for some n=4 configs, needed 4)

ALWAYS: When testing "does strategy X cover configuration Y", ensure the configuration is actually in strategy X's stated range - my Round 7 test falsely showed a failure because I applied BPP formula to an S5-range config (round 7)

ALWAYS: Verify algebraic coefficients by re-deriving from scratch - the Round 7 approach file had 5*beta where 4*beta was correct, though this didn't affect validity (round 7)

ALWAYS: Check proof STRUCTURE, not just the math - a proof that says "If X, trivial case. So assume not-X" must actually have a valid "trivial case" handling, or the whole structure is broken even if the "not-X" case is proved correctly (round 9)

ALWAYS: When a case is "removed" or "replaced", verify the ENTIRE proof structure still covers all configs - removing one case without adding a replacement creates a gap (round 9)

ALWAYS: When a proof uses shifted parameters (like d_j/L_0 - 1), verify the case structure covers NEGATIVE values, not just positive - a proof that only handles "all shifted >= 0" may miss valid configs where some d_j < L_0 (round 10)

ALWAYS: Verify sum constraint DIRECTION - if P_{n+1} < c(n) gives constraint A > B, don't accept a proof that claims A < B without re-checking the derivation (round 10)

ALWAYS: When a proof claims "X pieces = Y pairs + Z singletons", verify the arithmetic: with k marks on n pieces you get n+k pieces total, and 2*Y + Z must equal n+k (round 11)

ALWAYS: When Pigeonhole argument claims "all pairwise > threshold implies weighted sum > constraint", verify the minimum weighted sum formula by assigning largest weights to smallest values (round 11)

ALWAYS: For greedy picking games, the lb_score is NOT "sum of ceil(n/2) largest pieces" but rather "sum of pieces at odd positions (1,3,5,...) in sorted descending order" due to alternating turns (round 12)

ALWAYS: When an example construction is given for a general claim (e.g., "15 Pairwise strategies are valid"), verify the example matches the claimed condition - the (beta,gamma) example had wrong singletons (round 12)

NEVER: Accept computational verification as full proof for a mathematical claim - it's strong evidence but algebraic proof is required for rigor (round 12, (2,2,1) strategies)

ALWAYS: When a proof claims "at boundary X, strategy Y applies", verify that Y actually works at boundary configs, not just that Y's CONDITIONS are satisfied (round 14 - at g=1 boundary, Pairwise conditions are met but LB > c(5) for some vertices; (2,2,1) covers those cases)

ALWAYS: When verifying finite-case computational claims, independently enumerate and count the cases (round 14 - verified 63 vertices by computing all 720 permutations and filtering by v_0 constraint)

NEVER: Accept "max of piecewise linear on polytope is at vertex" without verifying the function is CONVEX (max of linear). For f = min_strategy LB, this is FALSE because min of convex is convex but the overall f is the lower envelope of continuous functions, not necessarily convex piecewise linear. (round 16)

ALWAYS: When a proof claims interior coverage from vertex verification, check if the function is convex (max of linears) or if alternative coverage argument (LP half-space union, explicit mapping) is provided. (round 16)

ALWAYS: When testing constrained interior points, ensure the generation satisfies ALL constraints (e.g., sum=1, weighted sum=42) - generating invalid points gives misleading "failure" results (round 17 - my initial test generated invalid configs with sum != 1)

ALWAYS: Independently verify minimum margin claims by exhaustive enumeration - claimed 1/2520 was wrong, actual minimum was 1/378 (round 17)
