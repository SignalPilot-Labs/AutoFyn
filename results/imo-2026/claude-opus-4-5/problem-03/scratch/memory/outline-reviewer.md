# Per-Role Rules for outline-reviewer

ALWAYS: Verify the claimed answer with small-case computation before assessing approach soundness (because this quickly catches formula errors or misunderstandings, round 1)

ALWAYS: Identify shared gaps across approaches explicitly (because these indicate either a genuine hard step or a potentially wrong direction, round 1)

ALWAYS: Register all approved approaches and update ranking in the same pass (because the ranking file must exist for future rounds, round 1)

ALWAYS: When an outline proposes a "revised" version of a dead-ended approach, check if the revision actually fixes the fundamental gap or just restates it (because Round 2 induction-on-n-revised still had the same upper-bound gap as Round 1, round 2)

NEVER: Trust Round 1 conclusions about which configuration beats another without verifying XY's response is truly optimal (because Round 1's "arithmetic beats geometric" was wrong due to suboptimal XY response, round 2)

ALWAYS: For game-theoretic upper bounds with recursive induction, verify the inductive bound f(param) <= target holds for ALL parameter values, not just the "good" case (because "always split P_1" fails when P_1 < c(n) and sub-game is geometric, round 4)

ALWAYS: When an outline claims "XY uses 0 marks" check that this actually limits LB (because with multiple pieces LB picks multiple odd-position pieces, not just the largest, round 4)

NEVER: Accept a "single recursive strategy" proof for game upper bounds without checking if different configs require different strategies (because XY's optimal response depends on the full config structure, round 4)

ALWAYS: When verifying Case B claims with "simple strategies fail", test the COMPLETE strategy family including split-to-match + halve-subset combinations (because quick heuristic tests can miss strategies that actually cover the config, round 5)

NEVER: Trust an "impossibility" claim for a sub-case without verifying the sum constraint actually forces contradiction — compute explicit bounds and check if the polytope is empty (because the "all d_j > L0 is impossible in B_small" claim was false; counterexample exists with all d_j > L0, round 10)

ALWAYS: When a gap-overlap argument (e.g., "alpha < 1 so gap = alpha-1 < 0") is claimed to extend to a new region, verify the sum constraint in THAT region bounds the relevant parameter (because the B_large constraint forces alpha < 1 but B_small does NOT, round 10)

ALWAYS: When verifying a Pigeonhole argument on weighted sums, compute the minimum weighted sum explicitly using sorted assignment (largest weight to smallest value) rather than trusting the claim (because the min is 15x+20g for n=4 vs. 21x+35g for n=5, and Pigeonhole works for n=4 but fails for n=5, round 11)

ALWAYS: When a Pairwise Strategy Lemma claims coverage for all pairs, verify that a valid XY construction exists for EACH pair, not just the pairs mentioned in existing strategies (because 10 pairs exist for n=4 but only 4 were explicitly constructed in previous rounds, round 11)

ALWAYS: When testing strategy constructions computationally, use global optimization (differential_evolution) rather than local optimization (L-BFGS-B) for cut positions — local optimizers get stuck at all-0.5 solutions and miss the true minimum (because the (2,2,1) failure case was a false alarm caused by L-BFGS-B getting stuck, round 14)

ALWAYS: When a "free-position cut" construction is proposed with a range (d_j, P_k), verify the range is non-empty by checking d_j < P_k — the range can be empty for some configs even when the pair condition holds (because (beta,gamma) construction fails when d_3 > P_2, round 14)

ALWAYS: When verifying exact rational cut positions claimed by an explorer, test the actual LB computation before trusting the claim — the explorer's specific cut values may be wrong even when the general strategy class is correct (because Round 15 explorer's wrs=35 cut positions 19/189, 23/189, 50/189 gave LB > c(5), but the correct cuts P1, P1+P2, P5 give LB = 1/2, round 16)

ALWAYS: When an outline claims "single template covers entire region" for game-theoretic coverage, verify by testing the template at ALL boundary vertex types (not just the primary vertex) — a template optimal for a Z-type vertex may fail at AP-type vertices in the same sector (because wrs=35 template covers only 7/31 Z-type vertices, round 17)

ALWAYS: When LB = sum of k largest pieces, verify that LB(x,T) is CONVEX in x (not piecewise linear non-convex) — because sum of k largest of n linear functions = max over subsets, and max of linear is convex (round 17)
