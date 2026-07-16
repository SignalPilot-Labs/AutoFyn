# Proof-builder memory

ALWAYS: Verify claimed formulas computationally for small cases before writing the proof (because the formula c(n) = 2^n/(2^{n+1}-1) was verified to be correct for n=1,2,3, round 1)

ALWAYS: When verifying a claimed optimal value, check BOTH that the claimed configuration achieves the value AND that no other configuration does better (because for IMO 2026 P3, the geometric configuration achieves 4/7 for n=2, but the arithmetic [1/6, 1/3, 1/2] achieves 7/12 which is better, round 1)

NEVER: Assume the claimed answer is correct just because one configuration achieves it (because arithmetic progression beats geometric progression for n>=2 in IMO 2026 P3, round 1)

ALWAYS: When proving game-theoretic bounds, prove BOTH the lower bound (player A can guarantee >= X) AND upper bound (player B can limit A to <= X) separately (because IMO 2026 P3 required showing both that LB can achieve c(n) and that XY can prevent LB from exceeding c(n), round 1)

ALWAYS: For interleaving arguments in stick-division problems, explicitly verify the sorted order inequalities Q_k > L_{n-k} > Q_{k+1} (because the interleaving construction was the crux of the proof, round 1)

NEVER: Claim an upper bound without showing the specific XY response strategy (because the upper bound direction was harder and required explicit construction, round 1)

ALWAYS: Check parity of piece count - odd count gives first player an extra pick (because parity was critical: XY prefers even piece count to avoid giving LB an extra pick, round 1)

ALWAYS: When analyzing game-theoretic responses, check ALL pieces the responder can attack - not just the "natural" largest one (because XY can split the SMALLEST piece to create favorable pairings, round 2)

NEVER: Assume XY's optimal response is to split the largest piece equally - asymmetric splits and attacks on smaller pieces can be better (because splitting [1/5, 2/5, 2/5] at the 1/5 piece gives LB only 1/2, round 2)

ALWAYS: For saddle-point proofs, verify that at the claimed equilibrium, both players are indifferent among their strategies (because geometric [1/7, 2/7, 4/7] is where XY's split of 4/7 anywhere in [1/7, 3/7] gives the same LB payoff, round 2)

ALWAYS: In comprehensive upper bound verification, test XY strategies that split MULTIPLE pieces (not just one piece) - sometimes the optimal XY response distributes marks across pieces (because for some configs in n=3, XY needed to split 2 or 3 different pieces to achieve optimal response, round 2)

ALWAYS: When a case split has boundary threshold T, verify that the boundary case (equality at T) gives the exact claimed bound - this confirms the threshold is correct (because for IMO 2026 P3, P_1 = L_0 gives LB = 1/2 + L_0/2 = c(n) exactly, round 4)

NEVER: Claim "XY uses 0 marks" for n >= 2 without checking what LB picks - greedy picks ALL odd-position pieces, not just one (because the outline-reviewer caught this fatal flaw in round 4)

ALWAYS: When exhaustive strategy enumeration fails for game-theoretic problems, consider that optimal play may require non-obvious cuts (not just at "natural" positions like opponent piece values) - grid search or numerical optimization can find these (because n=4 Case B required general cuts to achieve LB <= c(4), round 5)

ALWAYS: For sum-slack arguments, express the constraint as "total excess over minimum < slack" and derive bounds on individual terms (because the n=3 Strategy S3 proof used 3*P_1 + 2*d_1 + d_2 < 7*L_0 to show d_2 < 2*L_0, round 5)

ALWAYS: For interval coverage proofs, compute the gap width between consecutive strategy intervals - if negative, they overlap and there's no gap (because the n=4 Case A proof showed gap width = alpha - 1 < -2/3 between S5 and B intervals, round 6)

ALWAYS: Use reduced-unit parameterization (subtract 1 after dividing by L_0) to simplify sum constraints and interval bounds in Case B arguments (because alpha = P_1/L_0 - 1 made the n=4 interval coverage algebra cleaner, round 6)

NEVER: Include working notes and false starts in the final proof - clean up the proof to show only the final correct argument (because the S4 construction section had excessive trial-and-error text that obscured the key result, round 6)

ALWAYS: Verify the number of pairs created by a cutting strategy before claiming it satisfies Singleton-Pair Formula (because the Strategy B construction created only 2 pairs instead of 3, making the formula inapplicable, round 6)

NEVER: Assume n-1 marks suffice when XY has n marks available - for some configurations, all n marks may be needed (because n=4 Case B required 4-mark strategies for the B/PP ranges, not 3-mark, round 6)

ALWAYS: When a construction creates an unexpected piece structure (e.g., more singletons than expected), count the pairs and singletons explicitly before applying formulas (because several attempted constructions created 4+ singletons instead of 2, round 6)

ALWAYS: When "4 marks are needed" claims fail, check if the parameterization in the verification code matches the approach file's parameterization (because round 6's "B/PP need 4 marks" was wrong - a parameterization mismatch, round 7)

ALWAYS: When two strategy ranges (B and PP) differ only in which side of a boundary the difference falls, try unifying them with absolute value |...| (because B and PP were unified into BPP via |P_1+P_2-d_3|, round 7)

ALWAYS: When a sub-case has "sum constraint < C", verify whether the sub-case being analyzed actually has sum < C or sum > C (because the B_small sub-case has REVERSED sum constraint from B_large, which invalidated the original n=5 verification, round 10)

ALWAYS: When computational verification claims "0 failures", check if the test samples are from the CORRECT sub-region of the parameter space (because the original n=5 "0/500k failures" was on B_large where Halve+IH already works, not B_small which is the actual gap, round 10)

ALWAYS: When Pigeonhole guarantees "some pair has diff <= 1", verify that EACH of the C(n,2) pairs has a valid XY construction - don't assume all constructions are symmetric (because pair (alpha, beta) required 4 marks while other pairs used 3 marks, round 11)

ALWAYS: When simple Singleton-Pair constructions fail for a pairwise condition, try "near-pair" constructions where XY cuts pieces to create approximately equal lengths (because (alpha, beta) pair needed XY to cut P_5 at strategic positions to create near-pairs with P_1 and other pieces, round 11)

ALWAYS: Use numerical optimization (scipy differential_evolution or random search) to verify XY can achieve the bound even when algebraic construction is unclear (because random search found LB = 0.500 < c(4) = 0.516 for counterexample config where all standard constructions failed, round 11)

ALWAYS: When a single strategy variant fails for some configs, enumerate ALL possible variants of the strategy class (because (2,2,1) with Split P_3,P_5 + Halve P_6 fails some configs, but other variants like Split P_4,P_6 + Halve P_3 succeed, round 12)

ALWAYS: For bounded regions with extreme vertices, test ALL vertices computationally before claiming coverage (because the 63 permutation vertices at g=1 boundary are the hardest cases for (2,2,1) strategies, round 12)

ALWAYS: When enumerating vertices by weighted rank sum (wrs), verify that the permutation you write actually gives the claimed wrs before computing piece sizes (because initial attempt at wrs=41 used invalid permutation with wrs=70, round 14)

ALWAYS: For adjacent pairs in Pairwise strategies, explain WHY they cannot use the standard construction (the mechanism: creating d_k consumes P_k into a pair) rather than just stating they need a different approach (because the proof structure is clearer when the obstruction is explicit, round 14)

ALWAYS: When a polytope has multiple boundary types (e.g., g=1 vs v_0=0), count vertices from EACH boundary separately and verify no double-counting (because the n=5 proof required both 62 AP-type and 31 Z-type vertices, for 93 total, round 16)

ALWAYS: When claiming "V_j handles all cases with r_alpha != 0", explain the mechanism explicitly: if r_alpha != 0, then some d_j gets rank 0, meaning d_j = L_0 exactly (because this is the key insight that reduces the Z-type vertex count from 32 to 31 needing verification, round 16)

ALWAYS: For "perfect pairing" constructions where two intended singletons turn out equal, recognize this creates an additional pair and LB = 1/2 exactly (because the wrs=35 construction has P4-P1-P2 = P6-P5 = 1/9, making 5 pairs instead of 4 pairs + 2 singletons, round 16)

ALWAYS: When computing LB in alternating-pick games, use actual alternating picks (LB gets positions 1,3,5,...), NOT "sum of top k pieces" (because greedy LB doesn't get both copies of a pair - the players alternate, so each gets one from each pair, round 17)

ALWAYS: When "copy" templates (cut positions = existing piece sizes) fail to cover some interior points, try GENERAL templates with optimized cut positions (because the 31 Z-type templates with "copy" cuts achieved coverage at vertices but missed ~6% of interior points; general optimization achieved coverage everywhere, round 17)

ALWAYS: When proving LB(x,T) is convex for a fixed template T, use the "sum of k largest = max over subsets" structure: LB = max_{|S|=k} sum_{i in S} piece_i(x), and max of linear functions is convex (because this is the correct structural basis for n=5 coverage arguments, round 17)

NEVER: Claim "max of piecewise linear on polytope is at vertex" for f = min_T LB(x,T) - this function is the minimum of convex functions, which is NOT convex. Interior max can exist (because the 1D counterexample min(|x|, |x-1|) has max 0.5 at interior point x=0.5, round 17)

ALWAYS: When verifying coverage of a region by convex slabs, use LP feasibility: "exists x in region with x outside ALL slabs?" If infeasible, coverage is proved. Do not rely on vertex-only verification for functions that are min of convex (because the false compactness argument was the key gap in n5-five-mark, round 17)
