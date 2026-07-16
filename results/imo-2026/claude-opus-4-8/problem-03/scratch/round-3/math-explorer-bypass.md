## imo-2026-03

**Lens: BYPASS** — Scout attacks on the two shared open gaps (Lemma LL / Case-2 lower bound and Claim U / universal upper bound) that do NOT route through the geometric-induction Case-2 split or the per-config inductive upper bound.

---

### Distinct openings

**(A) Parity-of-piece-count argument for Lemma LL (most promising new route)**

Key structural fact: G_n has n+1 pieces; each XY cut adds exactly 1 piece; so the total piece count k ≤ n+1+n = 2n+1. Crucially, **when XY uses all n cuts and does NOT cut the smallest piece "1" (= 2^0/D)**, k = 2n+1 is ODD and "1" is the strict minimum of P. Then the sorted list is {p_1, …, p_{2n}, 1} with all p_i ≥ 1 (since G_n's pieces are all ≥ 1 and cuts of larger pieces stay ≥ their "half", so may drop below 1 only if a piece ≥ 2 is cut past midpoint — but XY is cutting pieces of G_{n-1} = {1,2,4,...}, not necessarily ≥ 1).

For the pure sub-case where every final piece ≥ 1 (e.g., XY cuts only pieces of size ≥ 2 and cuts symmetrically enough):

A(P) = [p_1 − p_2 + p_3 − ⋯ − p_{2n}] + 1 = [n pairs each ≥ 0] + 1 ≥ 1.

This is a clean 1-line argument when the sub-case conditions hold. The **crux gap for this route**: handle the remaining sub-cases: (i) XY cuts the piece "1" (creating pieces < 1); (ii) k is even (XY uses < n cuts or uses one cut twice on an already-cut piece — the last case is impossible since cuts must be on distinct original pieces, so k = n+1 + t with t ≤ n, and k can be odd or even). The sub-case analysis seems more structured than the current merge-lemma route.

Numerical verification confirms: for all tested Case-2 configurations with n=2,3 (>1000 grid points), A(Q∪R) ≥ 1 is tight (min = 1 exactly attained at specific rational configurations, e.g. Q={2,1,1}, R={1,2}: sorted P={2,2,1,1,1}, A=1). The equality case has the pair-cancelation pattern: P = {a,a,b,b,...,1} → A=1.

**(B) Extremal-smoothing route: bypasses Claim U but still needs Lemma LL**

The extremal-smoothing approach proves that the geometric config is the LB maximizer of V(A) = min_XY val, by showing any non-geometric LB config can be perturbed to a strictly higher V. This gives the upper bound c(n) ≤ V(geometric) for free (the geometric config is the max, so LB can't do better). The lower bound V(geometric) ≥ c(n) is still Lemma LL. **Conclusion**: the smoothing route is a genuine bypass of Claim U (no explicit XY strategy for arbitrary LB needed), but STILL needs Lemma LL. The crux gap for GAP S1 (smoothing lemma): for any non-geometric LB config, the directional derivative of V along a "toward-geometric" perturbation is ≥ 0. V is piecewise linear (min of a finite family), so only one-sided derivatives are needed. Numerically: n=2 maximin = 4/7 is unique at the geometric config; a few explicit perturbations all decrease the guaranteed value (confirmed computationally for non-geometric LB).

**(C) Direct LP-duality / Sion minimax: no genuine bypass**

Sion's minimax theorem (max_x min_y f = min_y max_x f for compact convex X, Y, quasiconcave-quasiconvex f) applies formally IF the payoff A(LB, XY) is quasiconcave in LB marks and quasiconvex in XY marks. The result would give: max_LB min_XY val = min_XY max_LB val. This is mathematically clean, but computing min_XY max_LB val (the "dual side") still requires knowing XY's optimal strategy against the best LB response — the same structure as Claim U. Verified: for equal LB pieces {1/3,1/3,1/3} (n=2), XY's optimal response is NOT "halve 2 of 3 pieces" but a skewed split giving val ≈ 0.513 < 4/7 = c(2). So any LP argument must capture XY's nontrivial optimal strategy. **Conclusion**: Sion/minimax does not bypass; it relocates the same gap to the dual side.

**(D) Averaging / random XY argument: insufficient alone**

If XY uses a random mark strategy, E[A] = 0 (by symmetry of the game when both players' marks are exchangeable). So min_XY A ≤ E_random[A] = 0 ≤ 1/D, giving Claim U trivially from the averaging bound. **But**: this proves the upper bound via the trivially correct "min ≤ average = 0 < 1/D", which means XY can achieve val ≤ 1/2. This is WEAKER than what XY actually achieves at the saddle (c(n) > 1/2). So the averaging argument proves the upper bound Claim U (XY can hold LB to ≤ c(n) ≤ 1/2)! But it proves a STRONGER statement (val ≤ 1/2 < c(n)) — which would mean LB's geometric config (which achieves exactly c(n) > 1/2) contradicts this. **Error**: the averaging argument proves min_XY val ≤ 1/2 is achievable by XY, but XY needs distinct marks from LB, and the averaging over RANDOM XY marks gives val = 1/2 only on average; the min could be much less. This is NOT a proof of Claim U. The averaging gives A(LB, XY_random) has expectation = 0, not a deterministic bound. So this route does not bypass Claim U rigorously.

**(E) B=0 cancellation argument (specific but illuminating)**

For Q with ALL pieces > 2^{n-1} (e.g., Q = {4+ε, 4−ε} in n=3 context), the "odd region" of N_Q is entirely above threshold 2^{n-1}, while the "odd region" of N_R (for the replica R) is entirely below 1. These are disjoint, so B = 0 and A(Q∪R) = A(Q) + A(R) ≥ A(R) ≥ 1. This handles a large family of Case-2 configurations without the merge lemma. **Crux gap**: when Q has pieces ≤ 2^{n-1} (A_Q^{high} = 0), the B=0 argument fails and the interaction is entirely "low", requiring either the parity argument (A) or a new structural bound.

---

### Candidate technique(s)

- **Parity of piece count + alternating-sum identity**: when k = 2n+1 and piece "1" is uncut, A(P) = (sum of n non-negative pairs) + 1 ≥ 1. One clean line; needs sub-case analysis for k < 2n+1 or piece "1" cut.
- **Disjoint odd-regions (B=0)**: when all Q pieces > max(R), the Q and R odd regions are disjoint, so A(P) = A(Q) + A(R) ≥ 1. Handles roughly the "q* > 2^{n-1}" case.
- **Extremal/smoothing**: the geometric config is the unique LB maximizer (argmax of V); compactness + one-sided perturbation argument. Bypasses Claim U.

---

### Cheap-kill candidates

- **Parity of k (piece count)**: When XY uses exactly n cuts (k = 2n+1 odd) and the smallest G_n piece (= 1) is NOT cut, A(P) ≥ 1 follows from the sorted-pair identity in ONE step — no merge lemma needed. This might kill the A(Q)>0 sub-case of Lemma LL for "generic" XY responses.
- **Disjoint support for B=0**: when max(Q) > max(R), the two odd-parity regions live in disjoint ranges (above and below 2^{n-1}), so B = 0 and A(Q∪R) = A(Q) + A(R) ≥ A(R) ≥ 1. Cheap for the sub-case max(Q) > 2^{n-1}.

---

### Knowledge-base entries to use

- **Invariants & monovariants** (KB): the piece count parity k mod 2 as an invariant tracking whether the alternating sum terminates with +1 or −1.
- **Casework / exhaustion** (KB: "split into finitely many cases, settle each"): the parity argument splits into (k odd, piece-1 uncut) vs (k even) vs (piece-1 cut). Each sub-case is handleable by slightly different means.
- **Induction** (KB: "ordinary, strong, or structural"): for the remaining sub-cases (piece "1" cut or k even), induction on the number of pieces below 1 might close the gap.
- **Piecewise-concavity smoothing** (KB): for the extremal-smoothing GAP S1, the value function V is piecewise linear; perturbing LB marks is a finite smoothing problem, and the knowledge-base entry on "piecewise-concavity smoothing" (finding the min at a breakpoint) is directly relevant.

---

### Analogous past problems (cruxes)

- **aimo-0287** (algebra/extremal-principle): "When a distinguished subset is optimal, test a single boundary exchange (drop one element, check if it increases the objective)." This is precisely the smoothing-lemma structure for GAP S1: if the LB config is not geometric, a boundary exchange (moving one mark) strictly increases V(A). Crux move: the optimality condition forces a specific local structure. Genuinely analogous to GAP S1.
- **aimo-0019** (combinatorics/games-and-strategy): covering-game on dyadic intervals. The response strategy "paint the next dyadic interval beyond the frontier" uses the geometric/dyadic structure of the reply. Analogous in that the equilibrium uses a self-similar (dyadic) structure, and the proof tracks invariants of a covering process. Not a direct match but gives intuition for why the GEOMETRIC config is optimal.
- **aimo-0117** (combinatorics/games-and-strategy): "Assign the played values as a two-sided geometric (dyadic) sequence so the single largest value strictly exceeds the sum of all others." The crux is the same dominance property we rely on (each G_n piece = 2^k/D strictly exceeds the sum of smaller pieces). Genuinely analogous: the proof there uses this "dyadic domination" to show the game value equals the top piece, which is the mechanism behind Case 1 of our lower bound.

---

### Prior progress

Status: **partial**. Certified: Lemma G (greedy = Σ_odd), integral rep of A, merge lemma. Proven: lower bound Case 1, tightness (replica gives exactly c(n)), full n=1 upper bound. Open: **Lemma LL** (lower bound Case 2, sub-case A(Q)>0) and **Claim U** (general upper bound for arbitrary LB config). Both are numerically confirmed true; equality is attained at specific configurations (e.g., sorted P = {2,2,1,1,1}, A = 1).

---

### Dead ends (do not retry)

- **Single merge-lemma step for Lemma LL (A(Q)>0)**: proven insufficient by reviewer (104/398 n=3 grid configs have merge-max < 2^n while true val ≥ 2^n).
- **Top/bottom decomposition A = A_top + A_bot − 2B for Lemma LL**: the bound A_top ≥ 2B is FALSE (A_top − 2B can be ≈ −10.5 numerically).
- **"Halve n of n+1 LB pieces" as XY's universal strategy**: gives val = (1 + p_{n+1})/2 which exceeds c(n) when LB uses equal pieces (p_{n+1} = 1/(n+1) > 1/D for large n).
- **Three-gap / Steinhaus theorem**: LB's optimal marks are NOT a Kronecker sequence; the theorem applies to irrational rotations, not to this rational combinatorial structure. Not applicable.
- **LP / Sion's theorem as a bypass of both gaps simultaneously**: relocates the same gap to the dual side of the minimax; no net simplification.

---

### Small-case / intuition notes

**(All labeled as conjecture unless tagged "proved")**

- [Proved] For n=1 unnormalized: A(P) = 1 EXACTLY and CONSTANTLY for any XY cut of the piece "2" — the value is the same regardless of where XY cuts. This is because the sorted-triple alternating sum always telescopes to 1.
- [Conjecture, numerically confirmed n=2,3] For A(Q) > 0, the minimum of A(Q∪R) over all valid R is > 1 (strict), while the infimum 1 is only approached as A(Q) → 0 (the balanced/closed sub-case). This suggests a proof by continuity: A(P) ≥ 1 with equality ONLY at the A(Q)=0 boundary.
- [Key identity, proved] When k = 2n+1 (all n cuts used) and smallest piece = 1 is uncut: A(P) = (sum of n pairs p_{2i-1}−p_{2i}) + 1 ≥ 1. (The n pairs are non-negative by sorting.)
- [Parity observation] When XY uses fewer than n cuts (k < 2n+1): k could be even, making the last term of A negative. In practice: the "lost" cut means some G_n piece is left LARGER, and the dominant-piece argument (Case 1) or the merge lemma handles those configs. This sub-case may not even fall in Case 2 (since if a large piece is uncut, it's Case 1).
- [Bypass feasibility] The extremal-smoothing route genuinely bypasses Claim U: it replaces "for every LB config, XY has a strategy to hold val ≤ c(n)" with "geometric is the unique LB maximizer", which only requires perturbation monotonicity of V near geometric — a one-sided derivative condition, not a universal strategy.
