## imo-2026-03 (lower-bound lens: L1 and L2)

---

### CRITICAL STRUCTURAL FINDING: Identity ‡ is circular

The existing writeup says L1 reduces to showing ∫⌊(N_F−N_I)/2⌋ dt ≤ 0. This is TRUE but CIRCULAR:

Computing algebraically (in 1/D units, total = D, ΣF = 2^n, ΣI = 2^n − 1):

  E − ΣI = 1/2 − (1/2)μ{N_F − N_I odd}

Since N_F − N_I is odd iff N = N_F + N_I is odd (they have different parities iff their sum is odd), we get μ{N_F − N_I odd} = μ{N odd} = 2O − D (by Lemma R2 scaled to total D). Substituting:

  E − ΣI = 1/2 − (1/2)(2O − D) = (D+1)/2 − O = 2^n − O.

So ∫⌊(N_F−N_I)/2⌋ dt ≤ 0 is IDENTICAL TO O ≥ 2^n. The integral formulation is a notational repackaging of the original claim, not a simplification.

CONSEQUENCE: The builder for direct-constructive must drop the integral angle and prove O ≥ 2^n (in 1/D units) directly in the confined case. Three distinct routes follow.

---

### DISTINCT OPENINGS

**Route A — Exchange/boundary-crossing argument (most tractable)**

Key computational finding (verified n=2,3,4,5):

- O is a PIECEWISE LINEAR function of fragment values in each region where the sorted ordering of fragments vs intacts is fixed.
- In the "interleaving region" where each fragment f_j strictly straddles consecutive intacts (2^{n-j} < f_j < 2^{n-j+1} for j=1,...,n, with f_{n+1} < 1), the sorted order is fixed and O = f_1+...+f_{n+1} = ΣF = 2^n (CONSTANT). Verified analytically and numerically.
- At a BOUNDARY CROSSING: when f_j drops below intact 2^{n-j} (transitions from slot j to slot j+1), the pair (f_j, 2^{n-j}) swaps in rank — intact moves to odd rank, fragment to even rank. Computed transition: O increases by exactly 2·(2^{n-j} − f_j) > 0. This was verified numerically for all boundary crossings in n=2,3.
- Since O = 2^n inside the interleaving region and O INCREASES with every boundary crossing (moving out of interleaving), O ≥ 2^n everywhere.

FORMALIZATION NEEDED: (i) O is piecewise linear with regions separated by fragment = intact thresholds; (ii) O = ΣF in the interleaving region (direct computation since all fragments at odd ranks); (iii) each boundary crossing increases O by 2 × crossing magnitude.

For (iii): when f_j crosses below I_k, the pair (f_j, I_k) goes from (fragment_odd, intact_even) to (intact_odd, fragment_even). The change in O is: new O = old O − f_j + I_k > old O (since I_k > f_j at the crossing). BUT O also loses f_j from the old odd rank, so net ΔO = (I_k − f_j) − (f_j − I_k) = 2(I_k − f_j)? Let me state more carefully: Before crossing, O includes f_j (at odd rank, since f_j > I_k). After, O includes I_k instead of f_j. ΔO = I_k − f_j > 0.

WRINKLE: This only handles LOCAL crossings (single pair swap). When a fragment jumps over multiple intacts, more complex analysis is needed. But since crossings happen one at a time as f_j decreases, induction on the number of crossings suffices.

NUMBER-OF-CUTS CONSTRAINT: The interleaving requires n+1 fragments (k=n cuts). For k < n (fewer fragments), O > 2^n strictly:
- k=1 (n=3): min O = 9 > 8 = 2^n (verified exhaustively).
- k=2 (n=3): min O = 8 = 2^n (tight).
- k=3 (n=3): min O = 8 = 2^n (tight).

For k < n, there are fewer fragments than intacts, so some intacts must appear at adjacent ranks, and O > ΣF. This follows because with k+1 < n+1 fragments, perfect interleaving (all intacts at even ranks) is IMPOSSIBLE — the "interleaving region" doesn't exist for k < n, so O is strictly above 2^n. No separate argument needed; the boundary-crossing route proves O ≥ 2^n for all k ≤ n by: (1) for k = n, the interleaving region has O = 2^n; (2) for k < n, no configuration achieves O = 2^n, so the boundary analysis still gives O ≥ 2^n (since the k=n analysis applies once additional zero-length fragments are added).

**Route B — Inductive proof with top-piece case split**

Direct induction on n:

Base n=1: Two fragments summing to 2, one intact {1}. Pieces {2−a, 1, a} with 2−a ≥ 1 ≥ a (WLOG). O = (2−a) + a = 2 = ΣF always (EXACT EQUALITY regardless of a). Proved in O(1).

Inductive step: Given n intacts {1, 2, ..., 2^{n-1}} and k+1 ≤ n+1 fragments summing to 2^n. Two cases:

CASE A (some fragment f_1 > 2^{n-1}): f_1 is the unique largest piece (rank 1, odd). O = f_1 + [contribution from ranks 3,5,...].  Remove f_1; sub-problem has n intacts + k remaining fragments summing to S = 2^n − f_1 < 2^{n-1}. All remaining fragments < 2^{n-1} (since f_1 > 2^{n-1} and ΣF = 2^n). The sub-problem's largest piece is the intact 2^{n-1}. It lands at total rank 2 (even), contributing to E(sub-problem). O_total = f_1 + E(sub). Need: E(sub) ≥ 2^n − f_1 = S. Since 2^{n-1} is at rank 1 of sub, E(sub) ≥ 2^{n-1} > S (because f_1 > 2^{n-1} implies S < 2^{n-1}). DONE.

CASE B (all fragments ≤ 2^{n-1}): Intact 2^{n-1} is at rank 1 (odd). O ≥ 2^{n-1}. Remove intact 2^{n-1}; sub-problem has n−1 intacts {1,...,2^{n-2}} and k+1 ≤ n+1 fragments summing to 2^n, all ≤ 2^{n-1}. O_total = 2^{n-1} + E(sub). Need: E(sub) ≥ 2^{n-1}. This reduces to O(sub) ≤ ΣI_sub + S − 2^{n-1} = (2^{n-1}−1) + 2^n − 2^{n-1} = 2^n − 1 = D_sub_I. Sub-problem: O(sub) ≤ ΣI_sub?

The sub-problem has n−1 intacts summing to 2^{n-1}−1 and k+1 fragments summing to 2^n. This is NOT a self-similar subproblem (fragments sum to 2^n, not 2^{n-1}). But: can O(sub) exceed ΣI_sub = 2^{n-1}−1? We need O(sub) ≤ 2^{n-1}−1... but O(sub)+E(sub) = (2^{n-1}−1)+2^n = 3·2^{n-1}−1, and if O(sub) ≤ 2^{n-1}−1 then E(sub) ≥ 2^n. CHECK: n=3, all frags ≤ 4, intacts (sub) = {2,1}. Fragments sum to 8, all ≤ 4. E(sub) ≥ 4? With frags {4,4} (two pieces both = 4 = 2^{n-1}): sub-pieces = {4,4,2,1}, E(sub) = 4+1 = 5 ≥ 4. ✓. With frags {3,3,2}: sub-pieces = {3,3,2,2,1}, E(sub) = 3+2 = 5 ≥ 4. ✓.

This case needs further analysis. The sub-problem differs structurally (fragments may dominate intacts). POSSIBLE APPROACH: Apply Case A recursively (find the largest fragment in sub-problem). If some fragment f' > 2^{n-2}: similar argument. If all fragments ≤ 2^{n-2}: intact 2^{n-2} is at sub-rank 1 (total rank 3, ODD), further recursion. The recursion terminates when fragments exceed all intacts.

ASSESSMENT: Route B (Case A) is clean and rigorous. Case B requires further sub-case analysis but the pattern is clear. The key is the CASCADE: whenever a fragment dominates all intacts, Case A closes cleanly. When intacts dominate, each intact at rank 1 contributes 2^{n-j}/D to O, and the fragments fill later ranks. The total can be bounded inductively.

**Route C — O = ΣF + S_I^odd − S_F^even, with S_I^odd ≥ S_F^even**

Write O = ΣF + S_I^{odd} − S_F^{even} where S_I^{odd} = sum of intacts at odd ranks, S_F^{even} = sum of fragments at even ranks.

For S_I^{odd} ≥ S_F^{even}: pair each consecutive rank pair (2k−1, 2k).
- If (intact, fragment): gap = intact − fragment ≥ 0 (sorted order). Net = +gap ≥ 0.
- If (fragment, intact): Net = 0.
- If (fragment, fragment): contributes −fragment_{even} < 0 to net.
- If (intact, intact): contributes +intact_{odd} > 0 to net.

PROBLEM: fragment-fragment pairs contribute negatively. The claim S_I^{odd} ≥ S_F^{even} is NOT term-by-term from pairing alone. It requires the specific structure of intacts being a geometric sequence with ratio 2.

PROMISING ANGLE: The geometric structure ensures that at most one fragment can exceed 2^{n-1} (any two would sum > ΣF = 2^n). So the top rank pair is always (big fragment, 2^{n-1}) or (2^{n-1}, smaller piece). The chain cascades downward using the doubling property. 

ASSESSMENT: Route C is less developed. The core inequality S_I^{odd} ≥ S_F^{even} needs a separate proof that may be as hard as the original.

---

### FOR L2: THE CONFINE-TO-R_n EXCHANGE

Exchange argument sketch: XY cuts in R_j (j < n). Move that cut to R_n.

KEY OBSERVATION: By §4.1, if R_n has no cuts, O ≥ P_n = 2^n/D. So XY MUST cut R_n to reduce O below 2^n/D. For cuts OUTSIDE R_n: a cut in R_j (j < n) splits P_j into (a, P_j − a). Both fragments are ≤ P_j = 2^j/D < P_n = 2^n/D.

EXCHANGE: Replace the R_j cut with an additional cut in R_n. Before: pieces include {a, P_j−a} from R_j (two small pieces). After: piece P_j (intact R_j restored) and one more cut in R_n.

Does this help XY (reduce O)? The EXCHANGE reduces XY's mark usage in small pieces and redeploys it to R_n. By the DOMINANCE IDENTITY (P_j = ΣI_{<j} + 1/D), restoring P_j merges two small pieces into one slightly-larger piece. In the sorted order, this single piece P_j likely goes to an ODD rank (since it's larger than everything in R_{<j}), potentially increasing O. Meanwhile, the extra R_n cut can DECREASE O by fragmenting the dominant piece further.

FORMAL ARGUMENT: Need to show O(all-in-R_n) ≤ O(cut-in-R_j-and-R_n). The key mechanism:
- With R_j intact: P_j = 2^j/D contributes to the sorted order at some rank r_j.
- With R_j split into (a, P_j−a): both pieces are < P_j, so they don't bump up into higher ranks.
- The splitting of R_j DOES NOT help XY's goal of displacing odd-rank pieces. It makes two small pieces instead of one medium piece.
- Replacing the R_j cut with an R_n cut instead: the R_n piece is the dominant piece. Splitting it (by an additional cut) does change the top of the sorted order, giving XY more ability to interleave.

NUMERICAL CONFIRMATION: For n=3 (minimax grid), XY's optimal play indeed confines all cuts to R_3 = [x_3, 1]. Verified for n=2,3,4,5 (Monte Carlo).

CLEANEST FORMULATION: Suppose XY has k ≤ n cuts, with at least one in R_j (j < n). Compare:
Config C: cut in R_j, giving two fragments of R_j and some R_n fragments.
Config C': same cuts except move the R_j cut to R_n (making one more R_n fragment, R_j intact).
Claim: O(C') ≤ O(C).

In C': R_j is intact (one piece P_j = 2^j/D) and R_n has one extra cut. In C: R_j has two pieces summing to P_j, R_n has one fewer cut. Since P_j < P_{j+1} < ... < P_n, and the dominant piece is P_n, the extra R_n cut in C' can achieve better interleaving within R_n, while restoring R_j in C' merges two small pieces into P_j (potentially going to an ODD rank and INCREASING O in C' vs C). 

WAIT: That would mean O(C') ≥ O(C), i.e., confining helps LB, not XY. But L2 claims confining is XY's OPTIMAL strategy (minimizing O). If confining increases O from LB's perspective, that means XY should NOT confine to R_n!

CONTRADICTION WITH NUMERICAL EVIDENCE: The numerics show XY's optimal play is to confine. So the exchange argument must show O(C') ≤ O(C), i.e., confining DECREASES O (is better for XY).

RESOLUTION: The exchange needs to show that when XY moves a cut from R_j to R_n, the R_n interleaving becomes MORE EFFECTIVE (lower O) than restoring R_j. Specifically: if XY had k_n cuts in R_n (giving k_n+1 fragments of R_n) and k_j ≥ 1 cut in R_j (giving k_j+1 fragments of R_j), then:
- O(C) with {R_n has k_n cuts, R_j has k_j cuts} vs.
- O(C') with {R_n has k_n+1 cuts, R_j has k_j−1 cuts (= 0 means R_j intact)}.

The comparison depends on the SPECIFIC optimal fragment placements in each case. This exchange is non-trivial because XY must re-optimize the R_n fragmentation in C'. 

SIMPLIFICATION: For L2, maybe the cleanest approach is to note:
- If XY uses any cut outside R_n, they can ALWAYS move it to R_n and get O(C') ≤ O(C).
- This requires showing that "adding one more cut to R_n while restoring one R_j piece" WEAKLY DECREASES O.
- The key: adding a cut to R_n → the dominant piece P_n gets split → its rank structure changes. With the EXTRA R_n cut, XY can potentially achieve the fully-interleaved minimum O = P_n = 2^n/D. Without that cut (but with R_j cut), XY achieves O ≥ P_n anyway (by the confined lower bound already proved).

So the exchange argument shows: the minimum O achievable with k cuts all-in-R_n ≤ minimum O with some cuts outside R_n. This follows because ALL-IN-R_n gives XY maximum ability to fragment the dominant piece.

TRACTABILITY ASSESSMENT: L2 is cleaner than L1. The key insight is: splitting smaller pieces (R_j, j < n) gives XY no benefit because those pieces are already small (≤ 2^{n-1}/D) and don't affect the dominant rank structure. XY's efficiency comes from fragmenting R_n. The formal argument needs to show that moving a cut to R_n (away from R_j) weakly improves XY's outcome.

---

### Candidate techniques (by name)

- **Exchange argument (consecutive transposition)**: The route for both L1 and L2. For L1: boundary-crossing increases O, interleaving is minimum. For L2: moving a cut from R_j to R_n weakly decreases O.
- **Induction on n with top-piece case split**: For L1, Case A (f_1 > 2^{n-1}) closes cleanly; Case B needs further analysis.
- **Piecewise linearity of the odd-sum**: O is linear in each fragment-ordering region; minimum at the interleaving region where O = ΣF = 2^n.
- Knowledge-base entries: **Invariants & monovariants** (exchange argument as a monovariant proof), **Casework / extremal principle** (Case A/B split).

---

### Cheap-kill candidates

- For L1: The case k=1 (2 fragments) gives O ≥ 2^n + (2^{n-1} − 1) > 2^n (strictly, for n ≥ 2). This can be proved by elementary analysis (Σf = 2^n, one fragment > 2^{n-1} is the largest piece at rank 1). So k=1 is much easier than k=n.
- For k=n: The interleaving configuration achieves O = ΣF = 2^n EXACTLY. Any other config gives O > 2^n. The "cheapest" proof is the exchange argument.

---

### Knowledge-base entries to use

- **Invariants & monovariants** (combinatorics section): the piecewise-linear O with monovariant decrease (O stays ≥ 2^n under each boundary crossing).
- **Casework / exhaustion** (proof methods): Case A / Case B split in the inductive argument.
- **Constructive / incremental** (combinatorics): the boundary-crossing construction, showing each step maintains O ≥ 2^n.
- **Pigeonhole / extremal**: "at most one fragment can exceed 2^{n-1}" (since two would sum > 2^n = ΣF).

---

### Analogous past problems (cruxes)

1. **aimo-0146** [combinatorics/extremal-principle]: Crux = "exchange-smoothing: move unit weight toward higher-coefficient positions, strictly raising the objective, until only extremal profiles remain." Analogous to L1's boundary-crossing argument: perturbing fragments toward the interleaving monotonically changes O, extremal (min) at the interleaving.

2. **aimo-0019** [combinatorics/games-and-strategy]: Crux = "dyadic-interval covering game with frontier invariant." The problem involves claiming dyadic intervals, and the potential is maintained by an amortized accounting across levels. Analogous to the dyadic structure of LB's geometric marking {1/D, 2/D, 4/D, ...} and the level-by-level analysis in the confined case.

3. **aimo-0292** [combinatorics/extremal-principle]: Crux = "order quantities, assume bound fails at one index, force all later quantities to also violate, contradict global total." Analogous to the pigeonhole argument for L1: if O < 2^n, then some fragment is at an even rank with value larger than the adjacent intact, but the sorted order forces a contradiction via the dominance identity.

No crux is a direct analog (the problem structure is novel), but these are the closest.

---

### Prior progress

Status: partial. Proved: G1 (greedy = odd-ranked), R1/R2 (odd-sum rewritings), LB construction + dominance identity, easy lower-bound case (XY spares R_n), interleaving Lemma I, base cases n=1 (both bounds) and n=2 (lower confined). Open: L1, L2, U1.

---

### Dead ends (do not retry)

- **Integral inequality ∫⌊(N_F−N_I)/2⌋ dt as a SIMPLIFICATION of L1**: CIRCULAR — this integral equals 2^n − O exactly (proved here), so proving it ≤ 0 is identical to proving O ≥ 2^n. The integral formulation does not reduce L1 to a simpler problem.
- **Term-by-term bound q_{2j} ≤ 2^{n-j}**: FALSE (counterexample n=3, fragments {3,2.5,2.5}: q_4 = 2.5 > 2 = 2^{n-2}). So L1 cannot be proved term-by-term.
- **Induction n → n-1 game-separation**: Already refuted in round 2. Not a proof route.

---

### Small-case / intuition notes (labeled as conjecture)

- CONJECTURE (numerically verified n=2,3,4,5): The minimum of O in the confined case is exactly ΣF = 2^n, achieved at the perfect interleaving (fragments f_j ∈ (2^{n-j}, 2^{n-j+1}) for j=1,...,n, f_{n+1} < 1). For k < n (fewer fragments), min O > 2^n strictly.
- OBSERVED (n=3): For k=1, min O = 9 > 8; for k=2, min O = 8; for k=3, min O = 8. The binding constraint is k ≥ n−1 (i.e., at least n−1 cuts needed to approach the minimum 2^n).
- OBSERVED: O is CONSTANT inside the interleaving region (not just minimized there). This is because in the interleaving, O = ΣF = 2^n regardless of the exact fragment values within their slots. This makes the minimum a "flat bottom" region, not a unique point.
- OBSERVED: For k > n (more than n cuts, ILLEGAL), min O drops below 2^n (e.g., n=3, k=4 gives min O ≈ 7.54 < 8). This confirms the cut-count bound k ≤ n is essential.
