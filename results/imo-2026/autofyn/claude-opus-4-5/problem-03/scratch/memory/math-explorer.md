ALWAYS: For stick-division / allocation games with alternating claiming, simulate greedy claiming (sort pieces, LB takes odd ranks) to compute guarantees numerically. (because direct simulation is fast and exact with Fraction arithmetic, round 1)
ALWAYS: Try geometric piece sequences (ratio 2) for "marks then claim" problems — they often yield optimal strategies with clean fractional answers. (because c(n) = 2^n/(2^{n+1}-1) was found via the 1/7, 3/7 geometric structure, round 1)
NEVER: Assume equal-spacing LB strategy is optimal in marking-then-claiming games — XY's "equal pair + epsilon" trick defeats it easily. (because LB at {1/3, 2/3} gives only ~0.51 guarantee vs optimal 4/7, round 1)
# Math Explorer Role Notes

ALWAYS: Verify small cases n=1,2,3 numerically before conjecturing a formula — the pattern from n=1 alone is often misleading (round 1)
ALWAYS: For game-theory problems with marking + claiming, check both the lower bound (LB's marking strategy) and upper bound (XY's adversarial response) separately (round 1)
NEVER: Assume equal-spacing marks are optimal for Liu Bang — XY's sliver strategy defeats equal spacing, giving LB only ~1/2 (round 1)
ALWAYS: For the copy/clone adversarial strategy, check that the big piece alone exceeds the sum of all smaller pieces — this is the key structural property (round 1)
ALWAYS: For "XY halves the n largest pieces" strategy — prove A = smallest piece using pair-cancellation: equal halves (p/2, p/2) always occupy consecutive positions in sorted order and cancel in the alternating sum, so only the unhaved singleton contributes. (round 2)
ALWAYS: For upper bound in marking+claiming games, check a pigeonhole/sum argument — the optimal marking's piece sizes sum to 1 AND are the thresholds for individual conditions; if all conditions fail their thresholds, the sum exceeds 1, contradiction. (round 2)
NEVER: Assume the "halve the n largest pieces" strategy universally proves the upper bound — it only works when the smallest piece p_1 ≤ t_n. For p_1 > t_n, XY needs a case-specific strategy. (round 2)
NEVER: Assume "halve the n largest pieces" is XY's universally optimal strategy — it fails for non-geometric LB markings (e.g., {1/4,1/4,1/2} gives LB 5/8 > c(2)). (round 2)
ALWAYS: For upper bound in marking games, prove A = alternating_sum ≤ t_n = 1/(2^{n+1}-1) rather than proving LB ≤ c(n) directly — the alternating sum formulation is cleaner and admits induction. (round 2)
ALWAYS: The n=1 upper bound has a complete proof via case-split on a_1 vs 1/3: if a_1 < 1/3 halve a_2 (A=a_1); if a_1 ≥ 1/3 clone a_1 in a_2 (A=1-2a_1). Both ≤ 1/3. (round 2)
ALWAYS: For the two-case induction (halve vs clone), the identity t_n/t_{n-1} = (2^n-1)/(2^{n+1}-1) is the key: Case A (p_{n+1}>=c(n)): 1-p_{n+1} ≤ (2^n-1)/(2^{n+1}-1); Case B (k=n+1): 1-2p_n < (2^n-1)/(2^{n+1}-1). Both are tight at the geometric marking boundary. (round 3)
ALWAYS: For intermediate Pigeonhole cases k=2,...,n-1, the clone p_{k-1} in p_k strategy is ALWAYS FEASIBLE (since p_k < 2p_{k-1} by Pigeonhole), but the IH bound (1-2p_{k-1})*t_{n-1} ≤ t_n requires p_{k-1} ≥ c(n)/2 which only holds when k=n+1. Need a different argument for smaller k. (round 3)
ALWAYS: Case k=2 of the Pigeonhole has a simple direct proof: XY halves p_3,...,p_{n+1} (n-1 marks), leaving singletons p_1, p_2. A = p_2 - p_1 < 2t_n - t_n = t_n. No spare marks needed. (round 3)
ALWAYS: The interleaving strategy for case k gives A = p_k - S_{k-1} where S_{k-1}=p_1+...+p_{k-1}. Since p_k ≤ 2^{k-1}t_n and S_{k-1} > (2^{k-1}-1)t_n, we get A < t_n. This works when p_k > S_{k-1} (feasible interleaving). When p_k ≤ S_{k-1}: A < 0 trivially but XY must find a valid placement. (round 3)
ALWAYS: For the upper bound in pigeonhole-based casework, take k* = the LARGEST index satisfying p_{k*} ≤ 2^{k*-1} t_n — this guarantees p_{k*+1} > 2p_{k*} (no interleaving) AND S_{k*} < (2^{k*}-1)t_n (sub-problem small enough). The factor (2^{k*}-1) cancels exactly in the bound A ≤ S_{k*}·t_{k*-1} < t_n. (round 3)
NEVER: Take any satisfying pigeonhole index for the halving strategy — taking the SMALLEST k gives interleaving problems; only the LARGEST k* guarantees p_{k*+1} > 2p_{k*}. (round 3)

ALWAYS: Check whether "pair-cancellation gives A = singleton" holds when pairs may not be at the bottom of sorted order — it does hold regardless of pair position (proved rigorously round 3).
ALWAYS: When Lemma 5 is false, look for multi-strategy case analysis (as in n=2: 4 cases) rather than a single universal bound.
NEVER: Use the "consecutive differences all > t_n → sum contradiction" argument for n ≥ 2 — the threshold (n+1)(n+2)/2 · t_n < 1 for n≥2, so no contradiction (verified round 3).
ALWAYS: Verify case analysis with random numerical testing before claiming completeness.
ALWAYS: In sandwich case P(m) (all p_k exceed geometric thresholds, p_{m+1} ≤ S·c(m)), XY's strategy is: cut p_{m+1} → (p_m, p_{m+1}-p_m) to create a paired duplicate of p_m that cancels at top, then apply P(m-1) to {p_1,...,p_{m-1},p_{m+1}-p_m}. Key: p_{m+1}<2p_m (from sandwich condition), so duplicate sits at top. Bound: (S-2p_m)·t_{m-1} < S·t_m iff p_m > 2^{m-1}·S·t_m (exactly the sandwich condition for k=m). (round 4)
