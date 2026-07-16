# Proof-Outliner Role Memory

## Patterns and lessons learned

ALWAYS: For game-theory problems with alternating selection, first establish that greedy picking is optimal (exchange argument) -- this simplifies the analysis to computing alternating sums of sorted pieces (round 1)

ALWAYS: Check the crux corpus for analogous problems; the aimo-0117 "geometric dominance" crux (largest value > sum of all others) was directly applicable to the stick-division problem (round 1)

ALWAYS: For "find c(n)" problems, separate the proof into lower bound (LB guarantees >= c(n)) and upper bound (XY limits LB to <= c(n)) -- both directions need explicit construction + proof (round 1)

ALWAYS: When the answer involves powers of 2, look for geometric/dyadic structures; the ratio 1:2:4:...:2^n appears frequently in game-theoretic optimality (round 1)

NEVER: Assume piece count alone determines the value -- the exact piece sizes and sorted order matter for the alternating sum (round 1)

ALWAYS: When verifying XY's best response to an LB configuration, consider ASYMMETRIC splits, not just equal splits -- equal splits may be far from optimal (round 2, the arithmetic-beats-geometric error)

ALWAYS: When the explorers find an error in a prior round's computation, verify the correction independently before accepting it -- the correction is itself a claim that needs evidence (round 2)

NEVER: Mark an approach "solved" when the upper bound proof has unexplained gaps like "careful XY play" or "interleaving gives LB exactly P_1" without rigorous justification -- these are the hard parts and need explicit proofs (round 2)

ALWAYS: When explorers find a clean inductive mechanism (like Pairing Cancellation), consolidate it into the lead approach rather than opening many new parallel approaches -- one well-built proof beats three half-built ones (round 4)

ALWAYS: For game-theoretic upper bounds, look for "cancellation" lemmas where opponent's move creates symmetric elements that split evenly between players -- this often enables clean induction (round 4)

ALWAYS: When an outline proposes "use 0 marks" as a strategy, verify that the resulting piece count and greedy selection actually achieves the claimed bound -- LB picks ceil(m/2) pieces from m pieces, not just the largest (round 4)

ALWAYS: When exhaustive computational search says a strategy fails, try MORE strategies including multi-split approaches -- XY can split MULTIPLE original pieces, not just one (round 4)

NEVER: Assume the case structure from an explorer is complete without testing all sub-cases -- explorers may focus on "big P_{n+1}" cases and miss the "small P_{n+1}" regime (round 4)

ALWAYS: When multiple explorers converge on the same sub-case structure (e.g., three strategies for n=3), that's a strong signal to adopt it rather than invent a new decomposition (round 5)

ALWAYS: For game-theoretic upper bounds with pairing structures, count marks carefully -- using n-1 marks (not n) can give even-parity piece counts that enable cleaner pair-based analysis (round 5)

ALWAYS: When two explorers use different parameterizations (e.g., x=P1/L0 vs alpha=P1/L0-1), map between them carefully -- the strategies may be identical under different names (round 6, S5 = S_D discovery)

ALWAYS: For interval coverage proofs, compute the gap width algebraically (end of interval 1 minus start of interval 2) -- a negative gap width means the intervals overlap and coverage is complete (round 6, alpha-2<0 closes the S5-to-B gap)

ALWAYS: When a reviewer claims "k marks are insufficient, need k+1 marks", verify the parameterization matches the approach file -- different variable conventions (e.g., eta = d_3/L_0 - 1 vs eta = d_4/L_0 - 1) can give wildly different results and lead to false gaps (round 7, the B/PP "4-mark requirement" was a parameterization mismatch)

ALWAYS: When strategies are "tested on 500k configs with 0 failures", verify the test region matches the open gap -- strategies may cover B_large (P_{n+1} >= c(n)) perfectly while failing on B_small (P_{n+1} < c(n)), or vice versa. The sum constraint REVERSES between these regions (round 10, 11 n=5 strategies tested on wrong sub-case)

ALWAYS: For n=4 B_small "all d_j > L_0", use the Pigeonhole lemma: 5 shifted params with weighted sum = 16 and all > 0 cannot all have pairwise > 1 (min weighted with all pairwise > 1 is > 20 > 16). This closes n=4 without enumerating individual strategies. (round 11, n=4 Pigeonhole discovery)

ALWAYS: For n=5, Pigeonhole does NOT close (min weighted = 35 < 42). The "all pairwise > 1" sub-region is bounded (gap g in (1, 1.2), x_min in (0, 1/3)) and requires 5-mark strategies (A, E, F). (round 11, n=5 structure clarified)

ALWAYS: For Singleton-Pair coverage proofs, include "vertical pairing" strategies (halve P_1,...,P_{n-1}, singletons {P_n, P_{n+1}}) that cover d_{n-1} <= L_0 -- this completes the strategy family and enables gap-overlap arguments (round 10, missing S_last strategy)

ALWAYS: When Type 3 strategies (2 cuts + 3 halves on 5 different pieces) fail to cover a bounded region, consider (2,2,1) strategies: split 2 pieces into 3 sub-pieces each + halve 1 piece. The extra marks on the same piece create MORE near-pairs than Type 3 can achieve (4 vs 3). (round 12, n=5 bounded region breakthrough)

ALWAYS: When claiming "max of piecewise linear on polytope at vertex", verify the function is CONVEX (supremum of linear functions). For f = min_T LB_T (minimum of convex functions), this claim is FALSE — the max can be at an interior point. Instead use: (a) LB(x,T) is convex for each fixed T (sum of k largest = max over subsets), (b) each feasibility set C_T is convex, (c) LP coverage check for union of convex sets. (round 17, n5-five-mark compactness gap)

ALWAYS: When the "all constraints tight" boundary (like g=1 for "all pairwise > 1") is exactly where a simpler tier applies (like Tier 2 pairwise), those boundary vertices are NOT interior to the harder tier — they are the handoff boundary. Don't waste effort proving Tier 3 strategies cover Tier 2 boundary points. (round 17, 62 AP-type vertices are Tier 2, not Tier 3)

NEVER: Trust "100% coverage with N x N grid" claims without finer verification — at N=50 the Type 3 coverage appeared complete, but N=40+ per dimension revealed 5-6% failures. Always test at multiple grid resolutions before claiming complete coverage. (round 12, Type 3 insufficiency discovery)

ALWAYS: When a pairwise strategy example is wrong (like (beta,gamma) "halve P1,P4,P5,P6"), look for two distinct construction types: (1) "chop-at-adjacent" works for NON-adjacent param pairs (cut P_{k+1} at P_k creates singleton d_k), (2) "free-position cut" is needed for ADJACENT param pairs (cutting at a variable position t because chop-at-adjacent consumes the needed singleton into a pair). (round 14, Pairwise construction types)

ALWAYS: For adjacent param pairs like (beta,gamma), the correct construction cuts a bridging piece P_{k+2} at free position t and uses a different LB formula: LB = 1/2 + (P_k + P_{k+1} - P_{k+2})/2 instead of Singleton-Pair. The condition becomes an inequality on the params (e.g., alpha+beta <= delta) which must be verified to hold under the exclusivity assumption ("ONLY this pair has diff <= 1"). (round 14, adjacent pair mechanism)

ALWAYS: When counting vertices of a "all constraints > threshold" polytope, check for TWO types of extreme points: (1) the threshold constraint going tight (e.g., g=1 for "all pairwise > 1"), and (2) a parameter hitting its boundary (e.g., v_0=0 for "all params > 0"). Missing either type gives an incomplete finite case enumeration. (round 16, 63-vertex miscounting fixed to 93)
