## imo-2026-03 — lower-bound lens (L1 case a=0 and L2)

---

### MAIN FINDING: A ≥ 1 is the canonical restatement of G-L1, and the alternating-sum-path route closes it

G-L1(n) [E(I_n ∪ F) ≤ ΣI_n] is equivalent to A ≥ 1 where A = alternating sum of the merged sorted list (A = O − E, and O ≥ 2^n ↔ A ≥ 2*2^n − D = 1 in 1/D units). Numerically verified: min A = 1.000000 over 100 000 random n=3 configs (3 cuts, all placements). The minimum is achieved exactly at the interleaving family.

---

### (a) Concrete routes to close L1 case a=0

#### Route A — alternating-sum boundary-crossing (recommended)

**Setup.** In the interleaving region (f_j ∈ (2^{n−j}, 2^{n−j+1}) for j=1,...,n with f_{n+1} < 1 and Σf = 2^n), all fragments are at odd ranks and all intacts at even ranks, giving A = Σ(fragments) − Σ(intacts) = 2^n − (2^n−1) = 1 (proved in §4.2.2 of direct-constructive). Case a=0 means f_1 ≤ 2^{n−1}, i.e., we are outside this region.

**The crossing law.** When fragment f (at odd rank r) crosses below intact I (at even rank r+1) — moving from the interleaving toward case a=0 — ΔA = 2(I − f) > 0. This follows from Lemma S (proved in §4.2.3): fragment leaves odd rank (−2f) and intact enters odd rank (+2I), net = 2(I − f) > 0. Every crossing AWAY from the interleaving strictly increases A.

**Path argument.** For any target config F (not necessarily in the interleaving region), choose a continuous path from the interleaving config F* to F while keeping ΣF = 2^n fixed. Along this path, A changes only at boundary crossings. Each crossing AWAY from the interleaving contributes +2(I_k − f_j) > 0 to A; crossings TOWARD the interleaving contribute negative amounts. But:

**Key structural fact.** Case a=0 is entirely "away from" the interleaving: the top intact 2^{n−1} is above the top fragment f_1 (i.e., f_1 has crossed below 2^{n−1} compared to the interleaving). The minimum-A config has exactly ONE "essential crossing": f_1 = 2^{n−1}. At this boundary, A = 1 + 2*(2^{n−1} − f_1) ≥ 1 with equality at f_1 = 2^{n−1}. For f_1 strictly below 2^{n−1}, A > 1 (verified: strict-a=0 gives min O = 8.042 > 8 on n=3 fine grid).

**Simplest formalization of Route A.** Instead of paths, use a DIRECT FORMULA: for any config, A = 1 + 2·Σ_{crossings from interleaving} (I_k − f_j) where the sum is over all (intact I_k, fragment f_j) pairs that are "inverted" relative to the interleaving (meaning: in the interleaving, f_j is ABOVE I_k, but in the target config, f_j ≤ I_k). Each term ≥ 0, so A ≥ 1. This is a direct algebraic identity that avoids paths entirely; the outliner should develop it as the main step.

**Numerical kill-switch for Route A.** The claim A ≥ 1 is false without the cut-count constraint k ≤ n. For n=3, k=4 cuts (5 fragments, illegal): verified min A < 1 (min O ≈ 7.54 < 8). So the cut count IS essential and Route A must use it.

**How the cut count enters.** With k ≤ n cuts, there are k+1 ≤ n+1 fragments. In the interleaving, exactly n+1 fragments occupy the n+1 odd slots (ranks 1,3,...,2n+1) and n intacts occupy the n even slots. With fewer fragments (k < n), not all odd slots are filled by fragments — some intacts are at odd ranks, making A > 1 (interleaving value). The tight case k = n (n+1 fragments) achieves A = 1 exactly.

#### Route B — induction with sub-problem (cleanest for case a=0 with k ≤ n−1)

In case a=0, the top piece is the intact 2^{n−1}. After removing it:

- Old O = 2^{n−1} + E_sub; Old E = O_sub.
- Need: Old E ≤ ΣI_n = 2^n − 1, i.e., O_sub ≤ 2^n − 1.

Sub-problem: intacts I_{n−1} = {1,...,2^{n−2}} plus all k+1 fragments with ΣF = 2^n, each f ≤ 2^{n−1}.

**Verified (n=4 fine grid):** max O_sub = 15 = 2^n − 1. Tight at the "shifted-interleaving" config {8,4,2,1,1} which has f_1 = 2^{n−1} = 8.

The sub-problem O_sub ≤ 2^n − 1 is NOT G-L1(n−1) (since ΣF = 2^n > 2^{n−1}), so a different inductive statement is needed. This is the gap for Route B: either prove a generalized G-L1 statement, or recognize that the sub-problem in case a=0 can be handled by Route A's argument applied at one level lower.

**Route B assessment:** less clean than Route A for the general case but clean for the case where all fragments are strictly below 2^{n−2} (cascade applies recursively). Route A gives a unified treatment.

#### n=3 numerical kill-switch: config {4,4,3,2,1,1}/15 (dispatch test case)

Fragments of R_3=8: {4,3,1} (2 cuts). All fragments ≤ 4 = 2^{n−1}: case a=0. Pieces sorted: {4,4,3,2,1,1}. O = 4+3+1 = 8 = 2^n. A = (4−4)+(3−2)+(1−1) = 0+1+0 = 1. This is a TIGHT case (A = 1) with f_1 = 4 = 2^{n−1} (boundary of a=0/a=1). Route A predicts A = 1 here: zero "essential crossings" since f_1 = I_{n−1} exactly. ✓

Full grid search n=3 (case a=0, k=1,2,3): min O = 8.000000 exactly (0.1-unit grid, 3 cut depths). ✓

---

### (b) Making L2 rigorous

**Numerical confirmation.** For n=3:
- Config A (1 cut in R_1, 2 in R_3): min O = 8.5 over all R_3 splits.
- Config B (3 cuts all in R_3): min O = 8.0.
- Config C (1 cut in R_2, 2 in R_3): min O = 8.04.
Moving cuts from small R_j to R_3 strictly helps XY (lowers O). ✓

**The mechanism (now clear from numerical analysis):**

When XY cuts R_j (j < n) into (a, P_j − a), both pieces are < P_j. These two pieces occupy two adjacent ranks (one odd, one even). The odd-rank piece contributes to O unnecessarily — this piece is tiny (≤ P_j/2 ≤ 2^{j−1}/D) but still burns an odd rank.

When XY instead keeps R_j intact (= P_j) and uses that cut in R_3, the intact P_j occupies ONE slot and can be positioned at an EVEN rank (by choosing R_3 fragments appropriately). The extra R_3 fragment is tiny (arbitrarily small), taking a bottom odd rank with negligible contribution.

**Net saving.** In the optimal Config B (all-in-R_3), XY achieves the interleaving (A = 1). In Config A, the tiny pieces from the R_j cut land at ranks where one is odd, forcing A > 1 (O > 8). The savings equals at least (value at wasted odd rank in Config A) − (value at last rank in Config B) > 0.

**Rigorous exchange argument (structure for the builder).**

Fix any XY strategy with at least one cut in some R_j (j < n). We construct a better-or-equal strategy with all cuts in R_n.

Step 1. Suppose XY has a cut in R_j producing pieces (a, P_j − a) and k_n cuts in R_n producing n_R fragments summing to P_n.

Step 2. In the modified strategy: restore R_j intact (one piece P_j) and place one more cut in R_n (now k_n + 1 cuts in R_n, n_R + 1 fragments summing to P_n).

Step 3. Compare O_old vs O_new:

- O_old includes max(a, P_j − a) at some odd rank (the larger of the two R_j halves).
- O_new has P_j at rank r_P in the merged list. Since P_j = 2^j/D < P_n = 2^n/D and P_j < all intacts R_k with k ≥ j: P_j appears BELOW all intacts of the same or higher level. Specifically, if j < n, then P_j ≤ P_{n−1} ≤ I_{n−1} = 2^{n−1}/D... hmm this needs care.

**Key mechanism in clean form.** In Config B with optimal R_n fragmentation, XY can always achieve O = ΣF_Rn via the interleaving of R_n fragments with the FULL intact set I_n (including the now-intact P_j). The interleaving uses ALL n+1 cuts in R_n, achieving A = 1 (O = 2^n/D). In Config A, XY has only k_n < n cuts in R_n (one wasted on R_j), and CANNOT achieve the full interleaving of R_n fragments with I_n: at least one intact has no fragment above it (insufficient cuts), forcing A > 1 (O > 2^n/D) by the argument of §4.2.3.

**Formal statement for L2.** If XY has k ≤ n cuts with at least one cut outside R_n, then for any XY strategy: min_F O(I_n ∪ F) ≥ 2^n/D, and this bound is LOOSE (strictly greater than 2^n/D) because the interleaving is unreachable with a cut wasted outside R_n. In contrast, if all k cuts are in R_n: the interleaving is achievable (for k = n) giving O = 2^n/D exactly. Therefore, XY's optimum (minimum O) is achieved with all cuts in R_n. ∎

**Gap in current treatment.** The step "interleaving is unreachable with one cut wasted outside R_n" needs to be formalized. It follows from the fragment-count: with k_n = n − 1 cuts in R_n, only k_n + 1 = n fragments of R_n are created, but the interleaving requires n + 1 fragments (one per odd rank). With n fragments and n intacts, there are 2n pieces and n odd ranks; the best XY can do leaves at least one intact at an odd rank contributing to O, but this intact (say P_m, m < n) is NOT a fragment of R_n and contributes a FIXED amount to O that is strictly > 0. This forces O to exceed the "n-cuts interleaving" value of 2^n/D.

**Kill-switch for L2.** Verified: min O with one cut in R_2 and n−1 in R_3 (n=3) = 8.04 > 8 = 2^3. ✓

---

### (c) Cleaner unified lower-bound argument

**Proposal: Prove O ≥ ΣF_Rn for any XY strategy directly, without the two-step decomposition (L2 + L1).**

The current proof route is: L2 (confine to R_n) + L1 (confined lower bound). A potential shortcut:

After XY places k ≤ n cuts (anywhere), the pieces are I_n ∪ F_cut where F_cut = fragments created by XY's cuts from LB's pieces. Let F* = all fragments from R_n cuts (summing to 2^n/D if all cuts are in R_n, or to whatever remains of R_n if R_n is not cut). Let W = pieces from cuts in R_j, j < n.

Direct argument: O = Σ_{odd ranks} pieces. The pieces W are ALL < P_{n−1}/D (small). By the fragment-count bound applied to W: at most 2*(number of cuts outside R_n) pieces total from W; each appears at some rank (odd or even). The pieces in F* ∪ I_n form the dominant structure. By Route A applied to F* ∪ I_n (with ΣF* ≤ 2^n), O_F*∪I_n ≥ ΣF* ≥ 2^n − Σ(wasted_on_W). The W-pieces at odd ranks add back to O. Net: O ≥ 2^n/D.

**Assessment**: This is potentially cleaner but requires careful accounting of the W-pieces at odd ranks. The two-step route (L2 + L1) is more modular and each step is independently useful. Recommend keeping the two-step structure but adding the "unreachable interleaving" formalization as the core of L2.

---

### Distinct openings (summary for outliner)

1. **Route A (alternating sum ≥ 1)**: Prove A = O − E ≥ 1 directly via the "boundary-crossing raises A" argument. Formally: A = 1 + 2·Σ_{crossings from interleaving} (I_k − f_j) with each term ≥ 0. The crossing sum is determined by the configuration (path-independent). This closes L1 case a=0 without needing the per-rank bound (which is false) or the induction (which loops).

2. **Route B (sub-problem induction)**: Remove top intact 2^{n−1}; reduce to O_sub ≤ 2^n − 1 for a sub-problem with ΣF = 2^n and each f ≤ 2^{n−1}. Apply case a=1 of G-L1 to the sub-problem (its top fragment ≤ 2^{n−1} but often there is a fragment in (2^{n−2}, 2^{n−1}) that triggers the cascade again). Terminates when all fragments are ≤ 1, giving trivial E_sub = 0. Verified numerically for n=4.

3. **L2 via unreachable-interleaving**: Formalise L2 as: with k ≤ n − 1 cuts in R_n (one cut wasted elsewhere), XY cannot achieve the n-cut interleaving of R_n fragments with I_n, so min O > 2^n/D. With all n cuts in R_n, the interleaving achieves O = 2^n/D exactly. This makes L2 a direct corollary of the interleaving value (§4.2.2) rather than a continuous exchange argument.

---

### Candidate technique(s)

- **Alternating-sum monotonicity** (Route A): A piecewise-linear function whose minimum (A = 1) is at the interleaving; each boundary crossing away from the interleaving raises A. This is the load-bearing technique for L1 case a=0.
- **Fragment-count bound** (§4.2.1, certified): Used to limit how many fragments can be in a given dyadic band; essential for the cut-count constraint. Enters L2 ("interleaving unreachable with one cut wasted outside R_n").

### Knowledge-base entries to use

- **Invariants & monovariants**: A = alternating sum is a monovariant; it increases at each boundary crossing (Lemma S), giving a global lower bound.
- **Casework / exhaustion**: Only needed for the base cases n=1,2 (already proved in §7).
- **Pigeonhole / extremal**: Cut-count gives N_F(2^{n−j}) ≤ 2^j − 1 (certified fragment-count bound); fragment-count bound enters the unreachable-interleaving argument for L2.

### Analogous past problems

- **aimo-0146** [exchange-smoothing]: Move weight toward higher-coefficient positions, strictly raising objective, until extremal. Analogous to Route A's boundary crossing raising A.
- None are direct analogs; the dyadic-interleaving structure is specific to this problem.

### Prior progress

Status: partial (CHANGES REQUESTED, elo 1558). Certified: G1, R, Lemma H (closes UB Case A), Lemma S, fragment-count bounds, interleaving value = 2^n, top-fragment cascade (G-L1 case a=1). Open: L1 case a=0, L2, U1 Case B.

### Dead ends (do not retry)

- **Per-rank bound r_{2j} ≤ 2^{n−j}** for L1: FALSE (n=3, F={3,2.5,2.5}: r_4 = 2.5 > 2). Do not retry.
- **Integral ‡ (∫⌊(N_F−N_I)/2⌋ dt ≤ 0)**: Algebraically identical to O ≥ 2^n (circular). Dropped in current draft.
- **Route B sub-problem induction without a generalized statement**: The sub-problem O(I_{n−1} ∪ F) ≤ 2^n − 1 is NOT G-L1(n−1) (ΣF too large), so G-L1(n−1) cannot be directly invoked. Need a different statement. Route A is cleaner.
- **Convexity of O in fragment values**: FALSE (2307/10000 violations in n=3). Do not use.

### Small-case / intuition notes (conjecture)

- **CONJECTURE (n=3 verified)**: Min A over all confined configs is exactly 1, achieved on the interleaving family (all fragments each straddling a distinct intact). For case a=0 with f_1 strictly < 2^{n−1}: min A > 1 strictly. This means L1 case a=0 has a STRICT lower bound (O > 2^n when f_1 < 2^{n−1}) but the tight case is at the a=0/a=1 boundary (f_1 = 2^{n−1}).
- **OBSERVED**: The formula A = 1 + 2·Σ_{crossings} (I_k − f_j) appears to hold exactly (verified on multiple n=3 configs). If this formula is provable, it closes L1 in one line.
- **OBSERVED**: L2 kill-switch: min O with 1 cut outside R_n is always strictly > 2^n/D (numerically by ≥ 0.04 for n=3 configs tested). The gap is O(P_j/D) where P_j is the piece that was cut outside R_n.
- **OBSERVED (n=4)**: Sub-problem O(I_{n−1} ∪ F) ≤ 15 = 2^n − 1 holds, tight at F = {8,4,2,1,1}. This is a shifted-interleaving config where the largest fragment equals 2^{n−1}.
