# Approach: geometric-selfsimilar

## Status
partial

## Approaches tried
- R2: Fully proved **Lemma G** (greedy = odd-index sum), the **measure characterization** of the
  alternating sum (Lemma M0), the **merge lemma** (Lemma M); the **answer + verification** for n=1,2;
  the **lower-bound base n=1** and **Case 1** (largest piece uncut); the **upper bound for n=1**; and the
  exact value **c(n)** attained by the replica response. Reduced the lower bound to **Lemma LL**
  (Case 2) and the upper bound to **Claim U**. Both left open.
- R2 (recorded dead sub-idea): a single merge-lemma step is **insufficient** to close Case 2 — the bound
  max(val(R)+Σ_even(Q), val(Q)+Σ_even(R)) drops strictly below 2^n on many admissible Case-2 configs
  (n=3 grid: 104/398). So LL needs more than one merge.
- **R3 (this round):**
  1. **LL sub-case t = 1 (single cut of the largest piece): NOW FULLY PROVED** — interval-overlap
     argument, B ≤ max(R) − q ≤ 2^{n−1} − q cancels A(Q) = 2^n − 2q down to A(R) ≥ 1. Written in full
     below (Lemma LL, Case t=1). Validated (0 violations on sampled Q={q,8−q} × refinements of G_2).
  2. **Upper bound Regime A (1/2 ≤ A_1 ≤ c(n)): NOW FULLY PROVED** — the **shadow strategy** carves the
     largest LB piece A_1 into copies of the other pieces plus a residual r = 2A_1 − 1; every non-A_1
     piece becomes an equal pair, so N is even except on [0, r), giving A(final) = r and hence
     **val = A_1 ≤ c(n)** exactly. Written in full below. Validated (200 random configs, val = A_1
     to the rational point, all ≤ c(n)). This **replaces the disproven "concentrate all cuts on A_1"**.
  3. **LL sub-case t ≥ 2, A(Q) > 0**: attacked with the a/b split and the two-sided merge bound
     A(Q∪R) ≥ b + |a − A(R)|; recorded which configs this misses (34/286 on the n=3 grid) and the tight
     structure (S_R ⊆ S_Q, A(Q) = A(R)+1). Genuine progress but **still an explicit open gap** — not
     papered over.
  4. Corrected the upper-bound regime analysis: the flat regime target is A(final) ≤ 1 (unnormalized),
     **not** val ≤ 1/2 (that would need A = 0, generally impossible). Regimes B (A_1 < 1/2) and C
     (A_1 > c(n)) remain explicit gaps.
  5. **n = 2 lower bound now RIGOROUS** (previously a grid assertion): the t = 2 case is closed via the
     merge identity A(Q ∪ R) = A(Q) + 1 − 2B with R = {1,2}, reduced to s_0 + s_2 ≥ s_1 for
     S_Q = [0, q_3) ∪ [q_2, q_1) and settled by explicit casework on q_1 vs 2. Hence c(2) ≥ 4/7 rigorously.
- **R5 (this round): Upper-bound Regime B (A_1 < 1/2) advanced substantially.**
  1. **General-n sub-regime B1 (A_1 ≥ 1 − c(n)): NOW FULLY PROVED** via the **partial-shadow prefix** —
     XY greedily carves A_1 into copies {A_2, …, A_k, s} (k maximal with A_2+⋯+A_k ≤ A_1, s = A_1 −
     (A_2+⋯+A_k) < A_{k+1}), doubling A_2, …, A_k (parity-invisible). This forces val ≤ 1 − A_1 for
     **every** flat config (all n, all m), via the clean bound A(R') ≤ 1 − 2A_1 proved from
     Σ_even(R') ≥ p_2 ≥ s. In B1, 1 − A_1 ≤ c(n), done. Verified (0 violations / 80000 random configs on
     each of: val ≤ 1−A_1, A(R') ≤ 1−2A_1, Σ_even(R') ≥ s). This **corrects the naive "one cut at A_2"**,
     which is special to m = 3 and fails for m > 3 ({12,9,2,2}/25 at n=3: val 14/25 > 8/15).
  2. **n = 2 Regime B fully CLOSED**: B1 (one cut, val = 1 − A_1 ≤ 4/7) and B2 (A_1 < 3/7, two exhaustive
     sub-cases B2a A_1 > A_2 → two cuts val = A_1 + A_3/2 ≤ (3A_1+1)/4 ≤ 4/7 with the ε-cut cancelling
     *exactly* via the parity-invisible A_3/2 pair; B2b A_1 = A_2 → one cut, val = 1/2). Exhaustive check
     DENOM = 84: all 820 configs ≤ 4/7, worst B1 = 4/7, worst B2 = 47/84.
  3. **General-n sub-regime B2 (A_1 < 1 − c(n)): still OPEN** — partial shadow only gives val ≤ 1 − A_1 >
     c(n); the leftover-cut recursion on the residual is not yet rigorous. Explicit gap.
- **R6 (this round): the whole upper bound UNIFIED into one sum-bound; three rigorous reduction lemmas;
  Regime C given a rigorous first step.**
  1. **Reformulation (all regimes at once).** Define μ(X, b) = min over XY's ≤ b cuts (distributed
     over the pieces of a finite multiset X, total mass Σ) of A(result). The entire upper bound is the
     single statement **μ(X, b) ≤ Σ / (2^{b+1} − 1)** (the *sum-bound*): for LB's config Σ = 1, b = n it
     reads μ ≤ 1/D, i.e. val ≤ c(n), in **every** regime A/B/C simultaneously. The sum-bound is tight
     exactly on the geometric config (Σ = 1 ⇒ 1/D). This replaces the fragmented A/B1/B2/C split by one
     target. Verified: an explicit strategy search holds μ ≤ 1/D with **0 violations** over thousands of
     LB configs for each n = 1..6 (worst μ ≤ 1/D, matched only near geometric).
  2. **Three reduction lemmas (FULLY PROVED below): R1 free-pair-removal, R2 halving (Case I),
     R3 pairing.** Each shows the sum-bound for X follows from the sum-bound for a strictly smaller
     instance, via one parity-invisible pair. Together with the base b = 0 they prove the sum-bound for
     **every LB config whose reduction tree never reaches the residual gap** — a large, precisely
     delimited class (85–100% of sampled configs; the closed fraction and the fact that no closed config
     violates the bound were both checked numerically).
  3. **Regime C now has a rigorous first move.** At the top level τ := 1·2^n/D = c(n); in Regime C
     A_1 > c(n) = τ, so **R2 (halving) applies immediately**: μ(X, n) ≤ (1 − A_1)/(2^n − 1), reducing C
     to the sum-bound for the smaller instance {A_2,…,A_m} (mass 1 − A_1) with budget n − 1. This is the
     first *justified* step for Regime C (previously its mechanism was unproven). The C-recursion bottoms
     out in the same residual gap, so C is not closed, but its opening cut is rigorous.
  4. **The residual gap is now a SINGLE, clean object** (subsuming both the old B2-general and C gaps):
     a distinct-valued multiset with **p_1 < τ and p_2 < τ/2**, τ = Σ·2^b/(2^{b+1}−1) ("spread/small
     max"). Here no single invisible pair is large enough for R2/R3. **Recorded dead-end:** the natural
     closer — the partial-shadow (greedy prefix) move — does **not** preserve the sum-bound invariant
     (the residual R' can have Σ(R')/(2^{b−j+1}−1) > Σ/(2^{b+1}−1): 18/123/315/678 violations of the
     invariant at n = 3/4/5/6 in the recursion), even though the *final* A stays ≤ 1/D. So the naive
     sum-bound induction cannot be pushed through partial-shadow; closing the gap needs a subtler
     potential than the running sum. This is the honest open frontier.
- **R7 (this round): gap-case sub-closure (Case A.A) + a rigorous SB-obstruction theorem.**
  1. **Case A.A (dominant-in-gap, p₁ > Σ/2): NOW FULLY PROVED** (no induction). The subtract-all chain
     (cut p₁ successively at p₂, …, p_m, using m−1 ≤ b cuts by the |X| ≤ b+1 budget invariant) doubles
     every non-p₁ piece (parity-invisible) and leaves the single leftover ℓ = 2p₁ − Σ, so
     A(final) = 2p₁ − Σ. Since a gap case has p₁ < τ and 2τ − Σ = Σ/D_b is an exact identity,
     A = 2p₁ − Σ < Σ/D_b **strictly**. Written in full below. Verified (0 anomalies / 3000 chains).
     Closes the p₁ ∈ (Σ/2, τ) sliver of the gap case.
  2. **SB-obstruction theorem (rigorous negative result): NOW FULLY PROVED.** The exact equivalence
     Σ'/D_{b−1} ≤ Σ/D_b ⟺ q ≥ τ/2 for a pairing step at a piece q (Σ' = Σ − 2q). In a gap case every
     piece q ≤ p₂ < τ/2, so **every** parity-invisible pairing step **strictly** breaks the SB invariant.
     Hence the proposed "gap-step-then-R3" cannot close the residual by SB-chaining — after the gap-step,
     R3's own bound Σ'/D_{b−1} already exceeds the target Σ/D_b. Any closure of the residual must track
     the *actual* A through the recursion (a potential strictly stronger than the running sum). This
     rigorously establishes the round-6 recorded dead-end and refines the outliner's mechanism. Verified
     (0 anomalies / 20000; threshold identity 2τ−Σ = Σ/D_b exact, b = 1..6).
  3. **Residual p₁ ≤ Σ/2 (the bulk of the gap case): remains OPEN**, but now with the obstruction above
     showing precisely *why* no SB-monotone reduction reaches it. Verified all n = 3 residual gap cases
     (denominator 30, budget-respecting search) have actual μ·D_b ≤ 1/2 (half the target) — (SB) is
     certainly true; only the actual-A potential is missing. Honest open frontier.
- **R8 (this round): residual gap case CLOSED for m = 3 (actual-A potential); the whole upper bound now
  RIGOROUS at n = 2; m >= 4 obstruction recorded honestly.**
  1. **Lemma R4 (gap-case m = 3 closure): NOW FULLY PROVED.** For a residual gap case with exactly
     m = 3 distinct pieces p1 > p2 > p3 and p1 <= Sigma/2, XY makes **one** R3 cut of p1 at offset p2,
     creating the parity-invisible pair {p2, p2} and effective pieces {p1 - p2, p3}. Because p1 <= Sigma/2
     gives p3 = Sigma - p1 - p2 >= p1 - p2, the larger effective piece is p3, so **A(final) = Sigma - 2p1**
     (an actual-A potential, not a sum-bound). The gap hypothesis p2 < tau/2 AND p3 < tau/2 gives
     p2 + p3 < tau, i.e. p1 > Sigma - tau = Sigma(2^b - 1)/D_b; with the **exact identity
     D_b - 2(2^b - 1) = 1** (verified b = 1..8) this yields A(final) = Sigma - 2p1 < Sigma/D_b **strictly**.
     Written in full below. Verified (0 mismatches of A = Sigma - 2p1, 0 violations of A < Sigma/D_b, over
     1351 budget-respecting m = 3 residual gap configs). Together with **Case A.A (p1 > Sigma/2, certified
     R7)** this closes the gap case for ALL m = 3, and (since m = 2 distinct is always p1 > Sigma/2 =
     Case A.A) for **all m <= 3**.
  2. **Upper bound fully RIGOROUS at n = 2** (framework route). At the top level b = 2, m <= n + 1 = 3, and
     every instance reached by the R1/R2/R3 reduction has m <= b + 1 <= 3; so every gap case that occurs
     has m <= 3 and is closed by Lemma R4 / Case A.A. This replaces the previously *by-numeric* Regime C at
     n = 2 with a rigorous closure. (Regimes A, B1 already certified; the framework now finishes n = 2.)
  3. **m >= 4 residual gap remains OPEN, and the outline's proposed cascade is REFUTED.** Bounded,
     budget-enforced numeric tests decisively refute every *simple deterministic* actual-A strategy the
     outline proposed: (i) greedy "cut largest at second-largest" cascade -- **18385/29234** gap configs
     VIOLATE A <= Sigma/D_b (worst ratio 21.2); (ii) recursive "R3 at p2 then recurse" -- **1314/2000**
     violate (worst 26.6); (iii) recursive partial-shadow (all cuts on p1, then recurse on the residual)
     -- **1268/2000** violate (worst 28.8). In particular the potential **A(final) <= Sigma - 2p1 is FALSE
     for m >= 4** (e.g. four near-equal pieces have Sigma - 2p1 ~ Sigma/2 >> Sigma/D_b). By contrast the
     **true** optimal mu (full bounded search) satisfies mu <= Sigma/D_b with **0 violations** (worst ratio
     0.88 at m = 4, b = 3), so (SB) is almost certainly true -- but the optimal strategy needs *lookahead*,
     and no monotone one-step potential closes it. This is the honest remaining upper-bound frontier
     (m >= 4, i.e. n >= 3).
- **R9 (this round): the m >= 4 gap case COLLAPSED to a single tight-budget finite inequality; the
  "abundant-budget" lemma (mu = 0 when b >= |X|) FULLY PROVED; the outline's one-cut mechanism REFUTED.**
  1. **SPEC CONCERN (outline overstated).** (i) The outline's "complement cut at p1 - pj (NOT pj)" vs
     "cut at pj" distinction is **illusory for a single cut**: cutting p1 at offset pj and cutting p1 at
     offset p1 - pj produce the *identical* fragment multiset {pj, p1 - pj}, hence the identical effective
     sub-instance and identical A. The claimed "triple pj / odd parity" from cutting at pj is false -- one
     fragment pj plus the one existing pj is a *pair*, not a triple. The R8 "cut-at-pj cascade"
     refutation was about a multi-cut deterministic cascade, not a single cut. (ii) The outline's core
     mechanism -- "one complement cut reduces m=4 to m=3, closed by R4 (one cut on the sub)" -- is
     **numerically REFUTED as insufficient**: the one-cut-on-sub value |2 max(sub) - Sigma'| violates the
     target on **141/367** budget-enforced m=4 gap configs at b=3 (worst ratio 2.5, e.g. near-equal
     {24,13,12,11}/60). The genuine strategy must use the FULL budget b-1 on the sub (recursion), not a
     single R4 cut.
  2. **Abundant-budget lemma (mu(X, b) = 0 for b >= |X|): NOW FULLY PROVED** (below, and promoted).
     XY reduces X to a single piece by |X| - 1 "pairing" cuts (cut the largest a at offset = another piece
     b, forming the invisible pair {b, b} and leaving a - b; each cut drops the piece count by 1), then
     halves the last piece into an invisible pair, giving A = 0. Uses <= |X| <= b cuts. Verified 0/3000.
  3. **CONSEQUENCE -- the m >= 4 gap case is nontrivial ONLY in the tight-budget regime b = m - 1.**
     The budget invariant |X| <= b + 1 gives b >= m - 1. If b >= m, the abundant-budget lemma gives
     mu(X,b) = 0 <= Sigma/D_b outright. So the *entire* remaining upper bound reduces to the single tight
     case **b = m - 1 (i.e. |X| = b + 1)**. (Verified: m=4 configs at b >= 4 all give mu = 0.)
  4. **Tight-case reduction to an explicit finite inequality.** With b = m - 1, XY reduces X to <= 2
     effective pieces by m - 2 pairing (merge) cuts, then spends the last cut on the residual 2 pieces
     {u, v} (u >= v), achieving A <= min(u - v, v). The reachable residuals form an explicit finite family
     (all merge-trees). Verified: min over this family <= Sigma/D_{m-1} with **0 violations over 9646
     budget-enforced exact-Fraction m=4 gap configs** (worst ratio 0.9494 at {37,21,16,5}). A cleaner
     5-strategy closed-form sub-family already covers **99.6%** (312/81866 miss). This collapses the whole
     m >= 4 upper bound to the concrete inequality "min over merge-trees of A <= Sigma/(2^m - 1) in the
     tight case." **Remaining gap: the closed-form analytic proof of that finite min-inequality** (the
     v-branch / smaller-effective-piece term is essential -- the pure balanced-partition bound delta*
     alone fails on 42822/61517 configs). Honest open frontier, now MUCH narrower than the R8 frontier.
- **R10 (this round): (T) for m = 4 PROVED analytically — the n = 3 upper bound is now RIGOROUS
  in-framework.** Absorbed the explorer's four-strategy elementary proof, re-derived every A-bound from
  scratch (the explorer's exact piece formulas had typos; only the bounds A_R≤d₂, A_S≤d₃, A_S≤|d₁−d₃|,
  A_P≤δ/2, A_C≤δ+d₃−d₁ are load-bearing and are re-derived cleanly). With d₁=p₁−p₂, d₂=p₂−p₃, d₃=p₃−p₄,
  δ=p₄, Σ=4δ+d₁+2d₂+3d₃, t=Σ/15, residual gap conditions (1) d₁≤2δ+d₃ (p₁≤Σ/2) and (2) δ+d₂+d₃<4t
  (p₂<τ/2), and derived (2′) 7d₂+3d₃<δ+4d₁. Four strategies R/S/P/C each 2 pairing cuts + ≤1 final cut
  (≤3=b, budget-legal; "min over merge-family ≤ t" is the correct existence-of-witness UB direction).
  Case split: Case 1 (d₂≤t) R; Case 2 (d₃≤t) S; Case 3 (|d₁−d₃|≤t) S; Case 4 (else) — **Sub-case B
  (d₃>d₁) IMPOSSIBLE** via the exact collision (X) 10t<δ+d₁ [from (2′)] vs (Y) δ+d₁<2t [from (2)],
  giving 8t<0; **Sub-case A (d₁>d₃)** uses P or C (complementary at d₁≷δ+d₃), both giving A<t since
  δ<2t [from (2)]. Cases exhaustive by construction. Verified: 0 violations/1528 residual gap configs,
  worst A/t=0.9375 at {25,17,13,9}; Sub-case B occurs 0 times; δ<2t always in Sub-case A. Together with
  Corollary R4.1 (m≤3) and Corollary AB.1 (b≥4⇒μ=0), this closes the whole n=3 upper bound: val≤8/15=c(3).
  **m≥5 stays OPEN** — honestly recorded as the generalized direct actual-A case-split (NOT SB-monotone,
  certified dead), with all refuted routes listed.
- **R11 (this round): Lemma MK PROVED + certified-ready; the whole UB reduced (all m) to the PURE hard
  case; Case A.A re-proved at arbitrary threshold t; the naive threshold-invariant condition-inheritance
  REFUTED.**
  1. **Lemma MK (μ(k pieces, k−1 cuts) ≤ min(pieces)): NOW FULLY PROVED** (induction on k: halve the
     largest piece into a parity-invisible equal pair, recurse on the other k−1 pieces with k−2 cuts;
     bases k=1,2). Written to `lemmas/MK.md`. Verified: MK-strategy A ≤ min, 0/4000 random rational
     multisets (k≤6). This is the **uniform easy-case tool for all m** that T4's ad-hoc R/S strategies
     never had.
  2. **All easy sub-cases closed for ALL m (Corollary MK.1).** If δ=p_m ≤ t: MK on X directly gives
     A ≤ δ ≤ t. If any adjacent difference d_j = p_j−p_{j+1} ≤ t: one pairing cut p_j@p_{j+1} (invisible
     pair {p_{j+1},p_{j+1}}) leaves m−1 effective pieces including d_j, then MK gives A ≤ min ≤ d_j ≤ t.
     Budget 1+(m−2)=m−1 exactly. Verified 0/4000. This replaces T4's Cases 1/2/3 uniformly.
  3. **Case A.A re-proved at ARBITRARY threshold t (all m).** For a gap instance with q₁>Σ/2, the
     subtract-all chain gives A = 2q₁−Σ; under (I) q₁<2^{m−1}t and (III) Σ≥(2^m−1)t,
     A = 2q₁−Σ < 2·2^{m−1}t − (2^m−1)t = t. So q₁>Σ/2 is closed at threshold t for every m. Verified
     0 violations (m=3,4,5 gap configs). This is the "threshold-invariant" form of certified Case A.A.
  4. **CONSEQUENCE — the whole upper bound (all m) reduces to the PURE HARD CASE:** the residual gap case
     (distinct X, p₁<τ=2^{m−1}t, p₂<τ/2=2^{m−2}t, Σ=(2^m−1)t, tight budget b=m−1) splits exhaustively:
     (a) p₁>Σ/2 → Case A.A at t [CLOSED, all m]; (b) p₁≤Σ/2 and (δ≤t or some d_j≤t) → MK [CLOSED, all m];
     (c) **p₁≤Σ/2, all d_j>t, δ>t → HARD case [m≤3 R4/Cor R4.1, m=4 T4, m≥5 OPEN].**
  5. **The naive threshold-invariant condition-inheritance is REFUTED (honest negative result).** The
     outliner's proposed hard-case step "p₁@p₂ → subproblem Y'={d₁,p₃,…,p_m} inherits gap conditions
     (1′)q₁'≤Σ'/2, (2′)q₂'<2^{m−3}t at threshold t, else easy MK case" does **not** hold: over m=5 (MAX=20:
     898 hard configs) and m=6 (MAX=14: 2120 hard configs), condition (2′) — the *halved* threshold
     2^{m−3}t on the subproblem's second piece — FAILS on the large majority (only 88/898 m=5, 236/2120
     m=6 satisfy (1′)&(2′)&(3′)), AND the "easy-MK escape" (some Y'-difference ≤ t) also fails on many
     (356/898 m=5, 1290/2120 m=6 satisfy NEITHER). So the {(I′),(II′),(III′)} induction cannot be the
     right invariant. **Yet μ(Y', m−2) ≤ t still holds** for these configs (e.g. Y'={4,3,2,1} at
     t=18/31≈0.581 has μ=0 via {4,3,2,1}→{2,2,2,2,1,1} all-pairs, NOT via any single gap-condition
     inheritance): the subproblem closes through the *full richer strategy space*, not through
     self-similar gap conditions. The honest open content: an invariant strictly weaker than the gap
     conditions but strong enough to recurse, OR a direct hard-case strategy for general m. The
     Σ′-arithmetic (Σ′=Σ−2p₂>(2^{m−1}−1)t, condition (III′)) IS correct and inherited — that was never
     the blocker; condition (II′)/(2′) inheritance is, and it is now shown FALSE.

- **R12 (this round): T5 hard-case structure mapped rigorously; the "0 grid violations" evidence
  EXPOSED as an artifact; HS-A2 remains the explicit blocking gap (honest partial). NO overclaim.**
  1. **T5 reduces to a 4-piece-at-threshold-t inequality (structural, rigorous).** For an m=5 pure hard
     case X={p₁>p₂>p₃>p₄>p₅}, Σ=31t, budget b=4, the single **pair1_2** cut (cut p₁ at interior offset
     p₂; the fresh p₂ pairs with the spectator p₂ into a parity-invisible pair, Lemma R1) is legal and
     leaves the **effective 4-piece subproblem Y′={d₁,p₃,p₄,p₅}** (d₁=p₁−p₂) with 3 cuts remaining,
     Σ′=Σ−2p₂=3δ+d₁+d₃+2d₄>(2⁴−1)t=15t (from cond (2) p₂<8t). By Lemma M0 A(final)=A(play on Y′), so
     **T5 via pair1_2 ⟺ min A(Y′,3) ≤ t.** This is a genuine one-cut reduction (mechanism airtight).
  2. **CRITICAL NEGATIVE FINDING — the integer grids LIE; pair1_2 is NOT universal.** On integer grids
     (Σ=31K, K∈{4,6,8,10}, ~105k configs) pair1_2's full 4-piece merge-family min A(Y′,3) ≤ t with
     **0 violations** (worst ratio exactly 1.0). BUT this is a **grid artifact**: an off-grid rational
     search (6000 exact-Fraction hard configs) found an explicit **witness where pair1_2 FAILS**:
     X={157/5, 13, 46/5, 34/5, 23/5} (Σ=65, t=65/31, δ=23/5≈2.19·t, so δ>2t), for which
     **min A(Y′,3)=1.049·t > t**. So pair1_2 alone does NOT close the hard case; the multi-first-cut tree
     the outliner posits IS genuinely necessary. This vindicates the reviewer's warning that "0 grid
     violations" (the R8/R10 evidence style) cannot certify a continuous claim — the δ>2t failures live
     strictly off the denom-4/5 grids. **Rule for future rounds: every UB numeric check MUST include
     off-grid random rationals, not just Σ=31K integer grids.**
  3. **The outliner's pair2_3 fallback is confirmed on the witness.** For the failing config above,
     testing all ten single-cut pairings: pair1_2=pair3_4=pair1_5 give 1.049·t (fail), but
     **pair2_3=pair1_4=pair2_5 give 0.382·t ≤ t** (and the true 5-piece optimum is 0.382·t). So the
     outliner's Step-3/Step-5 fallback (pair2_3 for the δ>2t Sub-A-P-fail region) is the right move on
     this witness. HS-A2 — "δ>2t ⟹ pair2_3 gives A≤t" — is therefore the correct target and remains the
     single blocking analytic gap. I could NOT close HS-A2 analytically this round (the Σ-bound
     d₂+2d₃+3d₄+3δ≤31t/2 still only yields d₂<3.5t, not the <2t a naive pair2_3-P argument needs).
  4. **T4's named strategies R/S/P/C are insufficient at threshold t (rigorous negative).** Applying the
     certified T4 bounds A_R≤e₂, A_S≤min(|e₁−e₃|,e₃), A_P≤ε/2, A_C≤ε+e₃−e₁ to the sorted Y′ (differences
     e_i, min ε) closes only ≈86% of hard configs (worst failing ratio 2.375, e.g. Y′={48,48,29,9}).
     The failures are exactly configs where Y′ has an **internal double pair**: a difference of two Y′
     pieces equals a third Y′ piece (e.g. w₁−w₂=w₄, giving a parity-invisible {w₄,w₄} and A=0 after
     halving the remaining piece). Adding the cross-matchings M2={w₁−w₃,w₂−w₄} and the chain Pc narrows
     the gap to ≈1% but still leaves the internal-double-pair configs. So closing min A(Y′,3)≤t needs the
     full 4-piece merge family (matchings + chains + internal-double-pair), not the T4-named quartet —
     this is a strictly stronger inequality than certified T4 (whose target Σ′/15 > t here). Honest gap.
  5. **Consequence / honest status.** T5 is NOT proven. Its structure is now sharply delimited: (i) the
     primary route min A(Y′,3)≤t closes all integer grids but has an explicit off-grid failure region
     (δ>2t); (ii) on that region the pair2_3 fallback numerically closes every tested config but the
     analytic bound (HS-A2) is unproven; (iii) the general Sub-B (cut_1@3) branch and general m≥6 (HS-A3)
     are untouched. n=4 UB stays OPEN. The n≤3 UB (R10, certified T4) is unaffected and remains rigorous.
- **R13 (this round): HS-A2 PROVED in full — the Sub-A-P branch of T5 with δ>2t is closed by pair2_3.**
  Verified from scratch (off-grid exact Fractions, 0 violations / 12422 genuine Sub-A-P δ>2t configs) and
  written rigorously below (section "R13"). The Σ-P bound `2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃` [*] is re-derived
  from `D1_{Y'} = 31t − 6δ − 5d₄ − 4d₃ − 2d₂` and the Sub-A-P condition `D1_{Y'} ≥ δ + d₄`. The 6-case
  sorted-order split on Y″={p₁,d₂,p₄,δ} (A / B1 / B2 / C1 / C2 / C3) is exhaustive and disjoint (split on
  d₂ vs p₄, δ, δ±t, 3t), and each case closes by a NAMED ≤3-cut strategy re-derived from Lemma R1:
  Case A (R, A≤(31t−9δ−8d₄−4d₃)/2<t/2), B1 (S, A≤d₂−δ<t), B2 (R, forces d₄<7t/6, A≤d₄−t<t/6),
  C1 (S, A≤δ−d₂≤t), C2 (**custom**: halve p₁, cut p₄@δ, finish {d₄,d₂} → A≤|d₄−d₂|<t, both d₄,d₂∈(t,2t)),
  C3 (VACUOUS: [*] forces 2d₂<0). **CORRECTION to the outliner:** the outliner's Case-C2 justification
  "P fires, A_P≤d₂/2" is WRONG — the P construction gives effective {p₁−p₄−δ, d₂} with p₁−p₄−δ>d₂ always in
  C2 (I proved p₁−p₄−δ≤d₂ ⟺ δ+2d₄+2d₃≤0, impossible), so A_P is NOT ≤ d₂/2; the true optimum (≈0.1–0.34t)
  is reached by the custom halve-p₁ strategy, whose bound |d₄−d₂|<t I derived and verified. The R12 witness
  X={157/5,13,46/5,34/5,23/5} falls in Case C1 (δ=2.194t, d₂=1.812t, E3=δ−d₂=0.382t), S closes — confirmed.
  **HONEST SCOPE: HS-A2 ≠ T5.** HS-A2 closes ONLY the Sub-A-P sub-branch of δ>2t. Gap G1 (the pair1_2
  full-merge-family write-up for Sub-A C / Sub-B, ~40k of ~50k failure configs, and the whole δ≤2t region)
  is STILL OPEN — numerics only, no analytic proof. So **T5 is NOT proven and the n=4 UB is NOT rigorous
  this round.** The Step tree closes only m=5's Sub-A-P branch; it is NOT uniform in m: m≥6 (HS-A3) is
  UNTOUCHED (Σ=63t, b=5, the δ-threshold and Case-C3 impossibility are unverified for m≥6). Also stated
  open. No forbidden route (SB-monotone, R3-cascade, complement-cut, p₁@p₂ induction, integer-grid) used.

## Current best
- **Answer:** c(n) = 2^n / (2^{n+1} − 1), verified for n = 1 (2/3) and n = 2 (4/7) directly.
- **Reduction complete** (Lemma G, certified): LB gets val(P) = Σ_odd = (T + A(P))/2 with A the
  alternating sum; in unnormalized units (×D, D = 2^{n+1} − 1, pieces = integers G_n = {1, …, 2^n}) the
  target is **A(final) ≥ 1** (lower) and **A(final) ≤ 1** (upper).
- **Lower bound**: base n=1, Case 1 (largest uncut), LL sub-case A(Q)=0, and **LL sub-case t=1** are all
  complete. Open: **LL sub-case t ≥ 2 with A(Q) > 0** (the load-bearing shared gap).
- **Upper bound (unified sum-bound (SB) framing, R6/R7)**: μ(X, b) ≤ Σ/D_b is proved for every (X, b)
  whose R1/R2/R3 reduction tree avoids the gap case (distinct X, p₁ < τ, p₂ < τ/2), **and (R7) for every
  gap case with p₁ > Σ/2 (Case A.A: subtract-all chain ⇒ A = 2p₁ − Σ < Σ/D_b, strict)**. This covers
  Regimes A, B1, the whole n = 2 case, the R2/R3 boundaries, and Regime C's opening cut. **(R7)** every
  gap case with p₁ > Σ/2 (Case A.A). **(R8)** the residual gap case with **m = 3** (Lemma R4, actual-A
  potential A = Σ − 2p₁ < Σ/D_b), hence — with Case A.A covering m = 2 — the **gap case for all m ≤ 3**,
  which makes the **whole upper bound rigorous at n = 2** via the framework. **(R9)** the remaining m ≥ 4
  residual gap case is now reduced to a single tight-budget finite inequality: (a) **[PROVED]** μ(X,b) = 0
  whenever b ≥ |X| (abundant-budget lemma), so with the budget invariant |X| ≤ b+1 the only nontrivial
  case is **b = m − 1** exactly; (b) in that tight case XY reduces X to ≤ 2 effective pieces by m−2 pairing
  cuts and finishes with one cut, achieving A ≤ Σ/D_{m−1}. **(R10) [PROVED] (T) at m = 4**: the four-strategy
  direct actual-A case split (R/S/P/C, gap conditions (1)/(2)/(2′), Sub-case-B impossibility, δ<2t P/C
  averaging) gives μ(X,3) ≤ Σ/15 for every m=4 residual gap case — so, with Cor R4.1 (m≤3) and Cor AB.1
  (b≥4⇒μ=0), **the entire n = 3 upper bound is rigorous: val ≤ 8/15 = c(3)**. The **SB-obstruction theorem
  (R7)** shows why no SB-monotone reduction reaches the residual (Σ'/D_{b−1} > Σ/D_b ⟺ q < τ/2, exact);
  (T) bypasses it with an *actual-A* reduction (not a sum-bound of a sub-instance).
- **Upper bound status by n:** n = 1 ✓, n = 2 ✓, **n = 3 ✓ (R10)**. **n ≥ 4 (m ≥ 5) OPEN**, but the
  frontier is now sharply isolated. **(R11)** Lemma MK (μ(k,k−1) ≤ min, `lemmas/MK.md`) + Case A.A at
  arbitrary threshold t reduce the ENTIRE UB (all m) to the **pure hard case** (c): p₁≤Σ/2, ALL d_j>t,
  δ>t, at t=Σ/(2^m−1). Cases (a) p₁>Σ/2 [Case A.A: A=2q₁−Σ<t] and (b) some d_j≤t or δ≤t [MK: A≤min≤t]
  are CLOSED for all m. The hard case (c) is m≤3 (R4), m=4 (T4), m≥5 OPEN. **The naive threshold-invariant
  induction is REFUTED:** the subproblem after p₁@p₂ does NOT inherit gap condition (2′) q₂′<2^{m−3}t
  (fails on the majority of hard configs, m=5,6 verified) and often has no easy-MK difference either, yet
  μ(Y′,m−2)≤t still holds through the full strategy space (Y′ can even reach μ=0). So the {(I′),(II′),(III′)}
  self-similar induction is the WRONG invariant; the Σ′-size (III′) is fine, condition (II′) inheritance is
  the false step. Closing m≥5 needs a weaker-but-recursable invariant or a direct hard-case strategy.
  0-violation at m=5 (true μ) confirms (T) is TRUE, not proven.
  **(R12)** T5's hard case reduces (via the legal single cut pair1_2) to the 4-piece inequality
  min A({d₁,p₃,p₄,p₅}, 3) ≤ t. This closes ALL integer grids but has an EXPLICIT off-grid failure
  (witness X={157/5,13,46/5,34/5,23/5}, δ>2t, ratio 1.049) — so pair1_2 is not universal and the
  multi-first-cut tree is genuinely needed; pair2_3 closes the witness (0.382·t). **HS-A2** ("δ>2t ⟹
  pair2_3 gives A≤t") is the single blocking analytic gap and is UNPROVEN. Also proven negative: T4's
  named R/S/P/C strategies are insufficient at threshold t (fail ≈14%, worst 2.375) — the full 4-piece
  merge family (incl. internal double pairs) is required. m=5 UB (hence n=4) remains OPEN; n≤3 rigorous.
  **(R13)** **HS-A2 is now PROVEN** (section R13, promotable lemma): in the m=5 pure hard case with δ>2t,
  IF the T4-P condition D1_{Y'}=d₁−p₃ ≥ δ+d₄ holds on Y'={d₁,p₃,p₄,δ} (the "Sub-A-P" sub-branch, the sole
  genuine pair1_2 failure mode per Opening 2), THEN the pair2_3 cut (p₂@p₃, Lemma R1) gives the 4-piece
  Y″={p₁,d₂,p₄,δ} with min A(Y″,3) ≤ t. Proved by the Σ-P bound [*] `2d₂ ≤ 31t−7δ−6d₄−4d₃` plus a 6-case
  exhaustive/disjoint split; each case closes by a named ≤3-cut strategy (R/S + one custom halve-p₁ move
  for C2, C3 vacuous). 0 violations / 12422 off-grid genuine configs. **This closes the δ>2t/Sub-A-P
  branch of T5, NOT T5.** The residual open gaps are G1 (pair1_2 merge family for Sub-A-C/Sub-B and the
  whole δ≤2t region — ~40k configs, numerics only) and G3 (m≥6/HS-A3, untouched). n=4 UB stays OPEN.
- **Overall Status:** the **upper bound is complete for n ≤ 3**; the **lower bound** is complete for n ≤ 2
  with the single open gap **LL sub-case t ≥ 2, A(Q) > 0** (load-bearing, shared with the LL slugs). So the
  full answer c(n) = 2^n/(2^{n+1}−1) is rigorously established for **n ≤ 2**, and the n = 3 upper bound is
  now rigorous; both bounds remain partial for larger n.

---

# Setup and reduction

After both players mark and the stick is cut, we have a finite multiset of piece lengths. The claiming
phase is a finite perfect-information game; the two players' totals sum to the constant total length T,
so maximizing one's own total equals minimizing the opponent's — the claiming phase is a **zero-sum
game** with a well-defined value by backward induction (knowledge_base.md: *Zero-sum games / backward
induction*).

## Lemma G (greedy optimality; odd-index sum) — CERTIFIED (imported)

**Statement.** For a multiset sorted p_1 ≥ … ≥ p_k, in the alternating claiming game taking a largest
remaining element is optimal on every turn; the first mover (Liu Bang) obtains exactly
**val(P) := Σ_{i odd} p_i** and the second mover Σ_{i even} p_i.

Proved and certified in `results/imo-2026-03/lemmas/greedy-odd-index.md`. **Consequence (reduction):**
after all cuts, sort the final pieces; Liu Bang gets val(P) = Σ_odd, so

  c = max_{LB marks} min_{XY marks} val(final pieces).

## Measure characterization and A-bounds — CERTIFIED (imported)

For P sorted p_1 ≥ … ≥ p_k, set A(P) := Σ_odd − Σ_even = p_1 − p_2 + p_3 − ⋯ (the **alternating sum**).
Since Σ_odd + Σ_even = T,

  **val(P) = (T + A(P)) / 2,   Σ_even(P) = (T − A(P)) / 2.**                     (†)

**Lemma M0 (measure form).** With N_P(x) := #{i : p_i > x},

  A(P) = measure{ x ≥ 0 : N_P(x) is odd } = ∫_0^∞ 𝟙[N_P(x) odd] dx,   and   0 ≤ A(P) ≤ p_1.

Proved and certified in `results/imo-2026-03/lemmas/alt-sum-integral.md`.

## Lemma M (merge lemma) — CERTIFIED (imported)

For finite multisets X, Y, since N_{X∪Y}(x) = N_X(x) + N_Y(x),

  **A(X ∪ Y) = A(X) + A(Y) − 2B,   B := measure{ x : N_X(x) odd AND N_Y(x) odd } ≥ 0,**

and consequently val(X∪Y) ≥ val(X) + Σ_even(Y) (certified in `lemmas/alt-sum-integral.md`). Since B ≥ 0,
B ≤ A(X), and B ≤ A(Y), the merge identity gives the two-sided bound

  A(X ∪ Y) ≥ A(X) + A(Y) − 2·min(A(X), A(Y)) = |A(X) − A(Y)|.                    (M±)

## Single-cut parity flip — CERTIFIED (imported)

Cutting a length-ℓ piece into (a, ℓ−a) with smaller part s = min(a, ℓ−a) flips the parity of N (the
count of all pieces > x) **exactly** on [0, s) ∪ [ℓ−s, ℓ) (measure 2s) and nowhere else; hence
|ΔA| ≤ 2s (certified in `lemmas/alt-sum-integral.md`).

---

# The answer and its verification

Let D = 2^{n+1} − 1. **Claim: c(n) = 2^n / D.** In unnormalized units (multiply every length by D) LB
marks produce the integer pieces G_n = {2^0, …, 2^n}, total T = D, and the target is **val ≥ 2^n**
(lower) resp. **val ≤ 2^n** (upper); dividing by D gives c(n). By (†) with T = D these read
**A(final) ≥ 1** and **A(final) ≤ 1** respectively.

*n = 1:* D = 3, c(1) = 2/3. Lower bound: LB marks at 1/3, pieces {1/3, 2/3}. Any XY cut of the 2/3-piece
into {u, 2/3 − u} leaves three pieces with median exactly 1/3 (one of u, 2/3 − u is ≥ 1/3, the other
≤ 1/3, as they sum to 2/3), so by Lemma G val = 1 − 1/3 = 2/3; a cut of the 1/3-piece keeps 2/3 the
unique max and val ≥ 2/3. Upper bound: proved in full below (n = 1). Hence c(1) = 2/3. ✓

*n = 2:* D = 7, c(2) = 4/7. Lower bound from the geometric construction (base + Case 1 + Case 2 with
t ∈ {1, 2}, all covered below: t = 1 is the general LL t=1 proof, t = 2 leaves R = {1, 2} uncut and is a
finite check). Upper bound: LB's best config {1, 2, 4}/7 is held to 4/7 by XY's replica (computation
below). The n = 2 upper bound is now proven for **Regime A** (1/2 ≤ A_1 ≤ 4/7, shadow) and **Regime B**
(A_1 < 1/2, R5 below, full two-case proof); only **Regime C** (A_1 > 4/7) is still by-numeric. Verified
numerically that no LB config beats 4/7. ✓ (Regime C at n = 2 pending a written strategy.)

---

# Liu Bang's construction (lower-bound side)

Liu Bang marks the n points (2^k − 1)/D, k = 1, …, n, creating n + 1 pieces of lengths g_i = 2^i / D,
i = 0, …, n — a geometric sequence of ratio 2, largest g_n = 2^n/D = c(n). **Dominance:**
g_i = 2^i/D > (2^i − 1)/D = g_0 + ⋯ + g_{i−1}, so each piece exceeds the sum of all smaller ones.

We work unnormalized: pieces are the integers G_n = {2^0, …, 2^n}, T = D, target **val ≥ 2^n**, i.e.
**A(final) ≥ 1**. Xiang Yu adds ≤ n cut points; a piece receiving t of them splits into t + 1 positive
subpieces summing to its length.

## Lower bound: A(P) ≥ 1 for every refinement P of G_n by ≤ n cuts

We induct on n. Write G_n = {2^n} ∪ G_{n−1}, G_{n−1} = {2^0, …, 2^{n−1}}. Let t = number of XY cuts
inside the largest piece 2^n; the remaining ≤ n − t cuts fall on G_{n−1}.

**Base n = 1.** Pieces {1, 2}, ≤ 1 cut. 0 cuts: A = 2 − 1 = 1. Cut on 2 → {a, 2−a, 1}, median 1, val =
3 − 1 = 2, A = 2·2 − 3 = 1. Cut on 1 → {2, b, 1−b}, 2 unique max, val = 2 + min(b, 1−b) ≥ 2, A ≥ 1. ✓

**Case 1 (t = 0): the largest piece is uncut.** 2^n survives. Every other original piece is ≤ 2^{n−1},
and cutting only shrinks pieces, so every other subpiece is ≤ 2^{n−1} < 2^n. Hence 2^n is the unique
maximum (sorted position 1) and val(P) = 2^n + (p_3 + p_5 + ⋯) ≥ 2^n, i.e. A ≥ 1. ✓

**Case 2 (t ≥ 1): the largest piece is cut.** 2^n splits into Q = {q_1, …, q_{t+1}} (Σ Q = 2^n,
t ≥ 1). The pieces of G_{n−1} receive ≤ n − t ≤ n − 1 cuts, producing a refinement R of G_{n−1}; by the
**induction hypothesis** applied to G_{n−1} with ≤ n − 1 cuts,

  **A(R) ≥ 1,   equivalently val(R) ≥ 2^{n−1}.**                                 (IH)

The final multiset is P = Q ∪ R, and by the merge identity we must show

> **Lemma LL.** With Q a partition of 2^n into t + 1 ≥ 2 positive parts (A(Q) ≥ 0 by Lemma M0), R a
> refinement of G_{n−1} with A(R) ≥ 1, and M := max(R) ≤ 2^{n−1} (all G_{n−1} pieces are ≤ 2^{n−1} and
> cutting only shrinks), one has A(Q ∪ R) = A(Q) + A(R) − 2B ≥ 1, where B = measure{x : N_Q(x) odd and
> N_R(x) odd}.

Two facts are used repeatedly. First, **A(R) ≥ 1** by (IH). Second, since every R-piece is ≤ M, the
R-odd region **S_R := {x : N_R(x) odd} ⊆ [0, M) ⊆ [0, 2^{n−1})** (for x ≥ M, N_R(x) = 0).

### Sub-case A(Q) = 0 (Q balanced). LL holds.

By the merge lemma, A(Q ∪ R) ≥ A(R) − A(Q) = A(R) ≥ 1. ✓ (This is (M±) with A(Q) = 0.)

### Sub-case t = 1 (single cut of 2^n). LL holds. **[Proved this round.]**

Here Q = {q, 2^n − q} with q ≤ 2^n − q, i.e. q ≤ 2^{n−1}. Then N_Q(x) counts how many of the two parts
exceed x: N_Q(x) = 2 for x < q, N_Q(x) = 1 for q ≤ x < 2^n − q, N_Q(x) = 0 for x ≥ 2^n − q. Thus the
**Q-odd region is the single interval S_Q = [q, 2^n − q)**, of length A(Q) = 2^n − 2q ≥ 0. Now

  B = measure(S_Q ∩ S_R) = measure{x ∈ [q, 2^n − q) : N_R(x) odd}.

Because S_R ⊆ [0, M) and S_Q = [q, 2^n − q), the intersection lies in [q, M) (empty if M ≤ q). Hence

  **B ≤ measure([q, M)) = max(0, M − q).**                                       (★)

We split on the position of M relative to q.

- **If M ≤ q:** by (★), B = 0. By the merge identity,
  A(Q ∪ R) = A(Q) + A(R) − 0 = (2^n − 2q) + A(R) ≥ 0 + A(R) ≥ 1. ✓

- **If M > q:** by (★), B ≤ M − q, so
  A(Q ∪ R) ≥ (2^n − 2q) + A(R) − 2(M − q) = 2^n − 2M + A(R).
  Since M ≤ 2^{n−1}, we have 2^n − 2M ≥ 2^n − 2·2^{n−1} = 0, so A(Q ∪ R) ≥ A(R) ≥ 1. ✓

In both cases A(Q ∪ R) ≥ 1, so LL holds when t = 1. ∎ (LL, t = 1)

The single load-bearing input is **M = max(R) ≤ 2^{n−1}**, which holds because R refines G_{n−1} whose
pieces are all ≤ 2^{n−1} and cutting only shrinks pieces. Note the argument does **not** need any
bound on max(Q): the two-piece structure of Q makes S_Q a single interval, and the only overlap with
S_R that can occur sits inside [q, M), of length ≤ 2^{n−1} − q, which exactly cancels
A(Q) = 2^n − 2q ≥ 2^{n−1} − q down to A(R).

### Sub-case t ≥ 2, A(Q) > 0. **OPEN GAP** (partial progress recorded).

*Partial bound (rigorous).* Let M = max(R) ≤ 2^{n−1}. Since Σ Q = 2^n, at most one part of Q exceeds
2^{n−1} (two parts each > 2^{n−1} would sum > 2^n), so for x ≥ 2^{n−1} we have N_Q(x) ∈ {0, 1}, equal to
𝟙[max(Q) > x]. Hence, writing

  b := measure(S_Q ∩ [2^{n−1}, ∞)) = (max(Q) − 2^{n−1})^+,   a := A(Q) − b = measure(S_Q ∩ [0, 2^{n−1})),

we have a, b ≥ 0 and A(Q) = a + b. Because S_R ⊆ [0, M) ⊆ [0, 2^{n−1}), the overlap obeys
B ≤ measure(S_Q ∩ [0, 2^{n−1})) = a; also B ≤ A(R). Feeding B ≤ min(a, A(R)) into the merge identity,

  **A(Q ∪ R) ≥ A(Q) + A(R) − 2·min(a, A(R)) = b + |a − A(R)|.**                  (LL-partial)

This is a genuine, correct lower bound sharper than (M±). It **closes** the following two chunks:
- **B = 0 disjoint-region chunk:** if S_Q ∩ [0, M) = ∅ (the Q-odd region lies entirely above M), then
  B = 0 and A(Q ∪ R) = A(Q) + A(R) ≥ A(R) ≥ 1. ✓
- **S_R ⊆ S_Q chunk:** if S_R ⊆ S_Q then B = A(R), so A(Q ∪ R) = A(Q) − A(R); this is ≥ 1 exactly when
  A(Q) ≥ A(R) + 1. (This is the *tight* configuration, e.g. n = 3: Q = {3, 3, 2} gives S_Q = [0, 2),
  R = {2, 2, 2, 1} gives S_R = [1, 2) ⊆ S_Q, B = A(R) = 1, A(Q) = 2 = A(R) + 1, A(Q ∪ R) = 1 exactly.)

*Why (LL-partial) does not close the residual.* The bound b + |a − A(R)| can drop below 1 while the true
A(Q ∪ R) ≥ 1. A bounded n = 3 grid check (Q = partitions of 8 into 3–4 parts, R = refinements of
{1,2,4} by ≤ 1 cut, step 1/2; 286 configs) found **0** configs with true A(Q ∪ R) < 1 but **34** configs
with b + |a − A(R)| < 1 (as low as 0). So the two-sided merge bound is provably too weak; a genuine
joint bound on B = measure(S_Q ∩ S_R) using the *dyadic refinement structure of R* is required. This is
the **load-bearing open gap**; it is left explicit and is **not** claimed closed. The natural handle
(unexplored to completion) is a strengthened induction hypothesis on R that controls
measure(S_R ∩ I) for the intervals I on which S_Q is odd, exploiting that S_R is a union of dyadic-type
intervals inherited from G_{n−1}.

*Recorded dead sub-ideas for the residual (do not retry):*
- Merge lemma alone / (M±): insufficient (A(Q ∪ R) ≥ |A(Q) − A(R)| can be < 1).
- Two-sided bound (LL-partial): insufficient (34/286 configs above).
- "A(Q) ≥ A(R) + 1 always": FALSE (e.g. Q = {5, 3}, R with A(R) = 3/2 gives A(Q) − A(R) = 1/2).
- Top/bottom split A = A_top + A_bot − 2B with A_top ≥ 2B: FALSE (reviewer, round 2).
- Monotonicity "more Q-cuts help LB": FALSE (the minimum val over refinements is at t = 2, not t = 1),
  so an induction that peels one Q-cut cannot go through in the naive direction.

**n = 2 fully closed (rigorous).** Case 2 forces t ∈ {1, 2}. t = 1 is the LL t = 1 proof above. For
t = 2, both cuts are inside 4, so R = {1, 2} is uncut, A(R) = A({1, 2}) = 1, and Q = {q_1, q_2, q_3}
with q_1 ≥ q_2 ≥ q_3 > 0, Σ Q = 4 (so q_1 ≥ 4/3). Here S_R = {x : N_R(x) odd} = [1, 2) (N_R = 2 on
[0,1), 1 on [1,2), 0 on [2,∞)), and N_Q is the step function 3 on [0, q_3), 2 on [q_3, q_2), 1 on
[q_2, q_1), 0 on [q_1, ∞), so the **Q-odd region S_Q = [0, q_3) ∪ [q_2, q_1)**. By the merge identity,
with B = measure(S_Q ∩ [1, 2)),

  A(Q ∪ R) = A(Q) + A(R) − 2B = A(Q) + 1 − 2B,   so A(Q ∪ R) ≥ 1 ⟺ B ≤ A(Q)/2.

Write s_0 = measure(S_Q ∩ [0,1)), s_1 = B = measure(S_Q ∩ [1,2)), s_2 = measure(S_Q ∩ [2,∞)); then
A(Q) = s_0 + s_1 + s_2, and B ≤ A(Q)/2 ⟺ **s_0 + s_2 ≥ s_1**. We prove s_0 + s_2 ≥ s_1 by cases on
q_1 vs 2 (using S_Q = [0, q_3) ∪ [q_2, q_1) throughout, and q_2 + q_3 = 4 − q_1).

- **q_1 ≤ 2** (so s_2 = 0; also q_2 + q_3 ≥ 2, and q_2 < 1 would force q_1 = 4 − q_2 − q_3 > 2, so
  q_2 ≥ 1). Then s_1 = (q_3 − 1)^+ + (q_1 − max(q_2,1))^+ and s_0 = min(q_3, 1) (the interval [q_2, q_1)
  contributes nothing to [0,1) since q_2 ≥ 1). With max(q_2, 1) = q_2:
  · if q_3 ≥ 1: s_0 = 1, s_1 = (q_3 − 1) + (q_1 − q_2); using q_1 = 4 − q_2 − q_3, s_1 = 3 − 2q_2, and
    3 − 2q_2 ≤ 1 ⟺ q_2 ≥ 1 ✓, so s_0 = 1 ≥ s_1.
  · if q_3 < 1: s_0 = q_3, s_1 = 0 + (q_1 − q_2) = 4 − 2q_2 − q_3, and q_3 ≥ 4 − 2q_2 − q_3 ⟺
    q_2 + q_3 ≥ 2 ✓ (equivalent to q_1 ≤ 2). So s_0 ≥ s_1.
- **q_1 > 2** (so q_2 + q_3 = 4 − q_1 < 2, hence q_2 < 2 and s_2 = q_1 − 2). Then
  s_1 = (q_3 − 1)^+ + (2 − max(q_2, 1)) and s_0 = min(q_3, 1) + (1 − q_2)^+. Using q_1 − 2 = 2 − q_2 − q_3,
  the inequality s_0 + s_2 ≥ s_1 becomes s_0 ≥ q_2 + q_3 + (q_3 − 1)^+ − max(q_2, 1):
  · if q_2 ≥ 1: max(q_2,1) = q_2, (1 − q_2)^+ = 0, and q_3 ≤ q_2 with q_2 + q_3 < 2 force q_3 < 1, so
    (q_3 − 1)^+ = 0, s_0 = q_3; need q_3 ≥ q_3, ✓ (equality).
  · if q_2 < 1: q_3 ≤ q_2 < 1, so s_0 = q_3 + (1 − q_2), and need q_3 + 1 − q_2 ≥ q_2 + q_3 − 1 ⟺
    q_2 ≤ 1 ✓.

In every case s_0 + s_2 ≥ s_1, so B ≤ A(Q)/2 and A(Q ∪ R) ≥ 1. Together with t = 1, Case 1, and the
base, this gives A(final) ≥ 1 for all ≤ 2-cut refinements of G_2, i.e. **c(2) ≥ 4/7**. ∎ (n = 2)
(The minimum A = 1 is attained, e.g. Q = {31/15, 22/15, 7/15}: A(Q ∪ {1,2}) = 1.)

**Summary of the lower bound.** Complete except **LL, sub-case t ≥ 2 with A(Q) > 0**, which is the single
remaining lower-bound gap.

---

# Upper bound: Xiang Yu holds Liu Bang to ≤ c(n)

Let Liu Bang's pieces be A_1 ≥ A_2 ≥ … ≥ A_m (m ≤ n + 1, Σ A_i = 1). The target is: XY, using ≤ n cuts,
forces val(final) ≤ c(n). By (†) with T = 1 this reads **A(final) ≤ 2c(n) − 1 = 1/D** (normalized), i.e.
A(final) ≤ 1 in unnormalized units. We do **not** aim for val ≤ 1/2 (that would need A = 0, generally
impossible when the piece count is odd); the correct target is A(final) ≤ 1/D.

The old "concentrate all n cuts on the largest piece A_1" strategy is **disproven** and abandoned: for
(0.4, 0.4, 0.2) at n = 2, forcing XY to cut only A_1 gives min val = 0.625 > 4/7, whereas XY's true
2-cut minimum is ≈ 0.508 ≤ 4/7. XY must be allowed to cut any pieces.

## The value c(n) is attained (tightness against the geometric config)

Unnormalized G_n = {1, …, 2^n}. XY places all n cuts inside 2^n, splitting it into
{2^{n−1}, 2^{n−2}, …, 2, 1, 1} (sum (2^n − 2) + 2 = 2^n ✓). Merged with the untouched {1, …, 2^{n−1}}
the sorted multiset is [2^{n−1}, 2^{n−1}, …, 2, 2, 1, 1, 1] (2n + 1 pieces, each value 2^i for
1 ≤ i ≤ n−1 doubled, and three 1's). By Lemma G, LB takes odd positions:
val = (2^{n−1} + ⋯ + 2) + 1 + 1 = (2^n − 2) + 2 = 2^n. Dividing by D, LB gets exactly c(n). So XY holds
the geometric config to exactly c(n); with the lower bound this pins the value **for the geometric
config**. (Equivalently: each doubled pair 2^i cancels in A, and the three 1's give A(final) = 1.)

## Upper bound for n = 1 (complete)

LB marks ≤ 1 point; pieces {1 − a, a} with a ≤ 1/2 (0 marks → single {1}; XY cuts into {x, 1−x},
val = 1 − max ≤ 1/2 ≤ 2/3). XY cuts the larger piece 1 − a into {y, 1 − a − y}; by Lemma G,
val = 1 − median, and XY maximizes the median.
- a ≤ 1/3: equal split y = (1−a)/2 gives pieces {a, (1−a)/2, (1−a)/2} with a ≤ (1−a)/2, median (1−a)/2,
  val = (1 + a)/2 ≤ 2/3. The median cannot exceed (1−a)/2 (the two split parts sum to 1 − a so one is
  ≤ (1−a)/2, and a ≤ (1−a)/2), so this is optimal.
- 1/3 < a ≤ 1/2: pick 0 < y < a, so y < a < 1 − a − y, median = a, val = 1 − a ≤ 2/3. The median cannot
  exceed a (the two split parts sum to 1 − a < 2a, cannot both exceed a).

So val ≤ 2/3 always, equality at a = 1/3. Hence c(1) ≤ 2/3, and with the lower bound c(1) = 2/3. ∎ (n=1)

## Regime A: 1/2 ≤ A_1 ≤ c(n) — the shadow strategy. **[Proved this round; COMPLETE.]**

Assume 1/2 ≤ A_1 ≤ c(n). XY uses the **shadow strategy**: cut the largest piece A_1 into the m parts

  {A_2, A_3, …, A_m, r},   where   r := A_1 − (A_2 + ⋯ + A_m) = A_1 − (1 − A_1) = 2A_1 − 1 ≥ 0,

using m − 1 cut points inside A_1 (the partial sums A_2, A_2 + A_3, …). Since m ≤ n + 1, this is
m − 1 ≤ n cuts — within budget. (If r = 0, i.e. A_1 = 1/2, XY uses only m − 2 cuts to carve
{A_2, …, A_m}, still ≤ n; the argument below is unchanged with the r-interval empty.) The cut points sit
strictly inside A_1, hence are distinct from LB's marks (piece boundaries) and from each other (all
sublengths are positive), so this is a legal set of distinct marks.

The final multiset is the LB pieces A_2, …, A_m together with the subpieces A_2, …, A_m, r of A_1:

  M_final = {r} ∪ {A_2, A_2, A_3, A_3, …, A_m, A_m}   —   r together with each A_i (i ≥ 2) **doubled**.

**Claim: A(M_final) = r, hence val = (1 + r)/2 = A_1.** Indeed, for every x,

  N_{M_final}(x) = 𝟙[r > x] + 2·#{ i ≥ 2 : A_i > x }.

The second term is even for every x, so N_{M_final}(x) is **odd iff 𝟙[r > x] = 1**, i.e. iff x < r. Thus
S_{M_final} = [0, r) and, by Lemma M0, A(M_final) = measure[0, r) = r. By (†) with T = 1,

  **val = (1 + r)/2 = (1 + 2A_1 − 1)/2 = A_1 ≤ c(n).**

So in Regime A, Xiang Yu forces val = A_1 ≤ c(n). ∎ (Regime A)

*Mechanism.* Carving A_1 into exact copies of the other pieces makes every non-A_1 length appear an even
number of times; equal values contribute an even count to N everywhere, so they are invisible to the
parity of N and cancel in the alternating sum. Only the residual r = 2A_1 − 1 survives, giving
A = r and val = A_1 exactly. (Validated: 200 random configs with 1/2 ≤ A_1 ≤ c(n), val = A_1 to the
rational point, all ≤ c(n).)

## Regime B: A_1 < 1/2 ("flat"). **[R5: n = 2 COMPLETE; general-n sub-regime B1 COMPLETE; B2 open.]**

Here the shadow residual r = 2A_1 − 1 < 0 is infeasible, so the Regime-A shadow does not apply. Split
Regime B at the threshold **1 − c(n)** (recall 1 − c(n) = (2^n − 1)/(2^{n+1} − 1) < 1/2):

  **B1:** A_1 ≥ 1 − c(n)   (so 1 − A_1 ≤ c(n)),      **B2:** A_1 < 1 − c(n)   (so 1 − A_1 > c(n)).

### The partial-shadow prefix (a general-n construction, used in B1)

Since A_1 < 1/2, we have A_2 + ⋯ + A_m = 1 − A_1 > A_1. Let **k** be the **largest** index with
2 ≤ k ≤ m and A_2 + A_3 + ⋯ + A_k ≤ A_1. Then:
- **k ≥ 2**, since A_2 ≤ A_1 (so the singleton sum A_2 already qualifies);
- **k < m**, since A_2 + ⋯ + A_m = 1 − A_1 > A_1, so the *full* tail exceeds A_1 and the greedy prefix
  stops strictly before index m. In particular **A_{k+1} exists**.

Set **s := A_1 − (A_2 + ⋯ + A_k) ≥ 0**. By maximality of k, A_2 + ⋯ + A_{k+1} > A_1, hence **s < A_{k+1}**.

Xiang Yu cuts the piece A_1 at the interior partial-sum points A_2, A_2 + A_3, …, A_2 + ⋯ + A_k,
carving A_1 into the k subpieces **{A_2, A_3, …, A_k, s}** (only the k − 1 pieces {A_2, …, A_k} if s = 0).
The number of cut points is at most **k − 1 ≤ m − 1 ≤ n** (using m ≤ n + 1), within budget. All cut
points are strictly interior to A_1, hence distinct from Liu Bang's marks (piece boundaries) and from
each other (all sublengths are positive) — a legal set of marks.

The final multiset is the carved subpieces {A_2, …, A_k, s} together with the untouched original pieces
A_2, …, A_m:

  **F = { A_2, …, A_k each doubled } ∪ R',   where   R' := {s} ∪ {A_{k+1}, …, A_m}** (drop s if s = 0).

Each value A_i (2 ≤ i ≤ k) occurs an **even** number of times (twice) in F, so it contributes an even
amount to N_F(x) for every x and does **not** affect the parity of N_F. Hence N_F(x) ≡ N_{R'}(x) (mod 2)
for all x, and by Lemma M0

  **A(F) = A(R'),   so   val(F) = (1 + A(R'))/2.**                                  (PS)

**Key bound: A(R') ≤ 1 − 2A_1.** Compute the total of R':

  Σ R' = s + (A_{k+1} + ⋯ + A_m) = s + (1 − A_1 − (A_2 + ⋯ + A_k)) = s + 1 − A_1 − (A_1 − s)
       = **1 − 2A_1 + 2s.**

Sort R' descending as p_1 ≥ p_2 ≥ …. The multiset R' contains at least **two** elements that are ≥ s:
namely A_{k+1} (since s < A_{k+1}) and s itself (an element of R'). Therefore the second-largest element
satisfies **p_2 ≥ s**, and since all parts are nonnegative,

  **Σ_even(R') = p_2 + p_4 + ⋯ ≥ p_2 ≥ s.**

(When s = 0 this reads Σ_even ≥ 0, still valid.) By (†), A(R') = Σ_odd − Σ_even = Σ R' − 2·Σ_even(R'),
hence

  **A(R') = (1 − 2A_1 + 2s) − 2·Σ_even(R') ≤ (1 − 2A_1 + 2s) − 2s = 1 − 2A_1.**

Substituting into (PS):

  **val(F) = (1 + A(R'))/2 ≤ (1 + 1 − 2A_1)/2 = 1 − A_1.**                          (PS-VAL)

So the partial-shadow prefix forces **val ≤ 1 − A_1** for *every* Regime-B configuration (any n, any m).

### Sub-regime B1 (A_1 ≥ 1 − c(n)) — COMPLETE (general n).

By (PS-VAL), val ≤ 1 − A_1. Since A_1 ≥ 1 − c(n), we get 1 − A_1 ≤ c(n). Hence **val ≤ c(n)**. ∎ (B1)

*(Consistency at n = 2, m = 3.* Here k = 2 forced: A_2 ≤ A_1 but A_2 + A_3 = 1 − A_1 > A_1, so the prefix
is just {A_2}; s = A_1 − A_2, R' = {A_1 − A_2, A_3} with A_1 − A_2 < A_3 (⟺ A_1 < A_2 + A_3 = 1 − A_1 ⟺
A_1 < 1/2). Then A(R') = A_3 − (A_1 − A_2) = 1 − 2A_1 and val = 1 − A_1 — the "one cut of A_1 at A_2" move.
For A_1 ≥ 3/7 = 1 − c(2) this gives val = 1 − A_1 ≤ 4/7.)* Note the naive "one cut at A_2" move is
**special to m = 3**: for m > 3 it can give val > c(n) (e.g. {12, 9, 2, 2}/25 at n = 3 gives 14/25 >
8/15); the greedy *prefix* of length k − 1 is what makes B1 go through for all m.

### Sub-regime B2 (A_1 < 1 − c(n)) at n = 2 (m = 3) — COMPLETE.

At n = 2, Regime B forces m = 3 (m = 2 gives A_1 ≥ 1/2, excluded), and A_1 ≥ 1/3 (max of three parts
summing to 1). B2 is 1/3 ≤ A_1 < 3/7. Recall A_2 ≥ A_3, A_2 + A_3 = 1 − A_1, so **A_3 ≤ (1 − A_1)/2**.

**Case B2a: A_1 > A_2.** Set ε := (A_1 − A_2)/2 > 0. XY makes two cuts: A_1 → (ε, A_1 − ε) and
A_3 → (A_3/2, A_3/2). Final F = {ε, A_1 − ε, A_2, A_3/2, A_3/2}. The pair {A_3/2, A_3/2} contributes
2·𝟙[x < A_3/2] to N_F — even for all x — so N_F(x) ≡ N_G(x) (mod 2) where G = {ε, A_1 − ε, A_2}; hence
A(F) = A(G). We locate the three values of G:
  · A_1 − ε = (A_1 + A_2)/2 > A_2 (⟺ A_1 > A_2, i.e. B2a);
  · ε = (A_1 − A_2)/2 < A_2, because ε < A_2 ⟺ A_1 < 3A_2, and A_2 ≥ (1 − A_1)/2 gives 3A_2 ≥
    3(1 − A_1)/2 > A_1 ⟺ A_1 < 3/5 (true, as A_1 < 3/7).
So the descending order is A_1 − ε > A_2 > ε, giving N_G = 3 on [0, ε), 2 on [ε, A_2), 1 on
[A_2, A_1 − ε), 0 above; the odd region is [0, ε) ∪ [A_2, A_1 − ε), of measure ε + (A_1 − ε − A_2) =
A_1 − A_2. Thus A(F) = A_1 − A_2 and, by (†) with T = 1,

  **val = (1 + A_1 − A_2)/2 = (A_1 + A_2 + A_3 + A_1 − A_2)/2 = A_1 + A_3/2.**

The ε cancels **exactly** (the identity above is independent of the value of ε in the legal range
0 < ε ≤ A_1 − A_2). Bounding with A_3 ≤ (1 − A_1)/2:

  val = A_1 + A_3/2 ≤ A_1 + (1 − A_1)/4 = (3A_1 + 1)/4 < (3·(3/7) + 1)/4 = 4/7 = c(2)   (since A_1 < 3/7). ✓

**Case B2b: A_1 = A_2** (so A_3 = 1 − 2A_1). XY makes one cut: A_3 → (A_3/2, A_3/2). Final
F = {A_1, A_1, A_3/2, A_3/2} — two doubled pairs, so N_F(x) is even for every x, A(F) = 0, and
**val = 1/2 ≤ 4/7 = c(2)**. ✓ (Consistently, A_1 + A_3/2 = A_1 + (1 − 2A_1)/2 = 1/2 here.)

Cases B2a, B2b are exhaustive (A_1 > A_2 or A_1 = A_2) and each gives val ≤ c(2). Together with B1, this
proves **the entire Regime B (A_1 < 1/2) at n = 2**: XY holds every flat config to ≤ 4/7. ∎ (Regime B,
n = 2)

*(Exhaustive rational check, DENOM = 84: all 820 flat m = 3 configs give val ≤ 4/7; worst B1 val = 4/7
attained at A_1 = 3/7, worst B2 val = 47/84 < 4/7; the identities val = 1 − A_1 (B1) and val = A_1 + A_3/2
(B2) hold exactly on 2000 random configs.)*

### Sub-regime B2, general n — **OPEN GAP.**

For A_1 < 1 − c(n), (PS-VAL) only yields val ≤ 1 − A_1 > c(n), which is **not** enough; XY must spend the
leftover n − (k − 1) cuts to further reduce A(R') on the residual R' = {s, A_{k+1}, …, A_m}. The n = 2
case is closed by the explicit two-cut move above (val = A_1 + A_3/2 ≤ (3A_1 + 1)/4 ≤ c(2)), but the
general-n recursion on the residual (a sub-instance of total Σ R' = 1 − 2A_1 + 2s, not normalized to 1)
is **not yet made rigorous**. Recorded as an explicit gap. (Numerically, for n = 2, 3 XY holds every flat
config to ≤ c(n).)

## Regime C: A_1 > c(n) ("dominant") — **OPEN GAP.**

The non-A_1 pieces sum to 1 − A_1 < 1 − c(n) = (2^n − 1)/D. The shadow overshoots (it would give
val = A_1 > c(n)); an equal n-split of A_1 only reaches A_1 ≤ (n + 1)/D < c(n) in special cases and is
insufficient in general. The proposed mechanism (a **recursive reduction**: XY's first cut splits A_1
into (1 − A_1, 2A_1 − 1); the part 1 − A_1 = A_2 + ⋯ + A_m caps the sorted top, and the remaining n − 1
cuts recurse on a scaled sub-instance via the (n − 1) upper bound) is only a mechanism, **not** a proof:
the scaling and the induction hypothesis are not made rigorous. Recorded as an explicit gap.
(Numerically, for n = 2 XY holds every dominant config to ≤ 4/7; worst observed LB share ≈ 0.501.)

---

# Unified sum-bound framework (R6) — three rigorous reduction lemmas

Throughout, X is a finite multiset of positive real lengths, Σ = Σ(X) its total mass, and b ≥ 0 an
integer cut budget. Write D_b := 2^{b+1} − 1 and

  **μ(X, b) := min over all placements of ≤ b cut points (distributed arbitrarily among the pieces of X)
  of A(resulting multiset),   A(P) = measure{x ≥ 0 : N_P(x) odd}** (Lemma M0).

Cutting only subdivides pieces, so it never changes Σ. All cuts below are strictly interior to a piece,
hence legal (distinct from LB's marks and, being at distinct positive offsets, from one another).

**Target (sum-bound).** For every (X, b):   **μ(X, b) ≤ Σ / D_b = Σ/(2^{b+1} − 1).**   (SB)

For LB's config (Σ = 1, b = n) this is μ ≤ 1/D, i.e. val = (1 + A)/2 ≤ (1 + 1/D)/2 = c(n) — the full
upper bound in one line, uniform over Regimes A, B, C. (SB) is tight exactly at the geometric config:
G_n = {1,…,2^n}/D has Σ = 1 and μ = 1/D (the certified replica bound `extremal-framework.md`).

We prove (SB) by strong induction on the pair (b, |X|) ordered lexicographically. The base and the three
reduction lemmas below are each unconditional as *reductions* (they bound μ(X, b) by μ of a
lexicographically smaller instance); granting (SB) for that smaller instance — the induction hypothesis
— each yields (SB) for X. A branch that reaches the **gap case** (defined after R3) is where the
induction is not yet closed; every other branch terminates at the base case, proving (SB) there.

## Base case b = 0

No cuts: μ(X, 0) = A(X) ≤ p_1 (largest piece) by the A-bound of Lemma M0, and p_1 ≤ Σ = Σ/D_0
(D_0 = 2^1 − 1 = 1). ∎

## Lemma R1 (free pair removal)

**Statement.** If X contains two equal pieces of common value w, then
μ(X, b) ≤ μ(X ∖ {w, w}, b).

**Proof.** Xiang Yu leaves those two pieces uncut and plays an optimal ≤ b-cut response to
X′ := X ∖ {w, w}. For every x, the two spectator pieces contribute exactly 2·𝟙[w > x] — an even
amount — to N, so N_{final}(x) ≡ N_{X′-response}(x) (mod 2) for all x; by Lemma M0 the two multisets have
equal A. Hence the value XY achieves on X equals the one it achieves on X′, giving
μ(X, b) ≤ μ(X′, b). ∎

Since |X′| = |X| − 2 < |X| with the same b, this is a lex-smaller instance; granting (SB) for X′,
μ(X, b) ≤ (Σ − 2w)/D_b < Σ/D_b, so (SB) holds for X.

## Lemma R2 (halving; the "Case I" move)

**Statement.** Let b ≥ 1 and let p_1 be the largest piece of X, with

  **p_1 ≥ Σ · 2^b / D_b.**                                                    (R2-cond)

Then μ(X, b) ≤ μ(X ∖ {p_1}, b − 1), and granting (SB) for X ∖ {p_1} at budget b − 1, (SB) holds for X.

**Proof.** Xiang Yu cuts p_1 at its midpoint into (p_1/2, p_1/2) — one interior cut — then plays an
optimal ≤ (b−1)-cut response to X ∖ {p_1}. The two halves are equal, so (exactly as in R1) they are
parity-invisible and contribute 0 to A; thus μ(X, b) ≤ μ(X ∖ {p_1}, b − 1). Granting (SB) at (b−1),
μ(X ∖ {p_1}, b − 1) ≤ (Σ − p_1)/D_{b−1} = (Σ − p_1)/(2^b − 1). Finally

  (Σ − p_1)/(2^b − 1) ≤ Σ/(2^{b+1} − 1)
  ⟺ (Σ − p_1)(2^{b+1} − 1) ≤ Σ(2^b − 1)
  ⟺ Σ[(2^{b+1} − 1) − (2^b − 1)] ≤ p_1(2^{b+1} − 1)
  ⟺ Σ · 2^b ≤ p_1 · D_b,

which is exactly (R2-cond). Hence μ(X, b) ≤ Σ/D_b. ∎ (X ∖ {p_1} has b − 1 < b, so it is lex-smaller.)

## Lemma R3 (pairing)

**Statement.** Let b ≥ 1, let p_1 be the largest piece, and suppose some *other* piece q of X (so
0 < q ≤ p_1) satisfies

  **q ≥ Σ · 2^{b−1} / D_b.**                                                  (R3-cond)

Then μ(X, b) ≤ μ((X ∖ {p_1, q}) ∪ {p_1 − q}, b − 1), and granting (SB) for that instance at budget
b − 1, (SB) holds for X.

**Proof.** If q = p_1 then X has an equal pair {p_1, q}; use R1 instead. So assume q < p_1. Xiang Yu
cuts p_1 at offset q into (q, p_1 − q) — one interior cut, p_1 − q > 0 — then plays optimally on the
rest with b − 1 cuts. The freshly-cut piece of length q is equal to the spectator piece q, so this pair
is parity-invisible and contributes 0 to A; the remaining pieces are X ∖ {p_1, q} together with the
leftover p_1 − q. Hence μ(X, b) ≤ μ((X ∖ {p_1, q}) ∪ {p_1 − q}, b − 1). Granting (SB) at (b−1) for this
instance, whose mass is Σ − 2q,

  μ(X, b) ≤ (Σ − 2q)/(2^b − 1) ≤ Σ/(2^{b+1} − 1)
  ⟺ (Σ − 2q)(2^{b+1} − 1) ≤ Σ(2^b − 1)
  ⟺ Σ · 2^b ≤ 2q · D_b
  ⟺ q ≥ Σ · 2^{b−1}/D_b,

which is (R3-cond). ∎ (The reduced instance has budget b − 1, hence is lex-smaller.)

## The induction, and the single residual gap

Set τ := Σ · 2^b / D_b (so R2 needs p_1 ≥ τ and R3 needs some q ≥ τ/2). Given (X, b) with b ≥ 1:

1. If two pieces of X are equal, apply **R1** (lex-smaller: |X| drops). 
2. Else X has distinct values p_1 > p_2 > …. If p_1 ≥ τ, apply **R2** (b drops).
3. Else if p_2 ≥ τ/2, apply **R3** with q = p_2 (b drops).
4. Else (**gap case**: X distinct, p_1 < τ and p_2 < τ/2) the three moves do not certify (SB).

Every non-gap branch strictly decreases (b, |X|) and terminates at b = 0, where (SB) holds. Hence:

  **(SB) is proved for every (X, b) whose reduction tree never enters the gap case.**

Numerically, running steps 1–3 as a deterministic reducer on random LB configs closes **100%** at
n = 1, and 99.3 / 96.7 / 93.8 / 89.9 / 85.6 % at n = 2 / 3 / 4 / 5 / 6, with **zero** closed configs
violating μ ≤ 1/D. The uncovered fraction is exactly the gap case.

## Consequences for the classical regimes

- **Regime C (A_1 > c(n)).** At the top level Σ = 1, b = n, so τ = 2^n/D = c(n). Since A_1 > c(n) = τ,
  **R2 fires immediately**: μ(X, n) ≤ (1 − A_1)/(2^n − 1), which is ≤ 1/D precisely because A_1 ≥ c(n)
  (the R2 arithmetic). Thus Regime C's opening cut — halve A_1 — is rigorous, and C reduces to (SB) for
  the smaller multiset {A_2, …, A_m} (mass 1 − A_1) with budget n − 1. This supersedes the previous
  unproven "dominant-chop" mechanism; only the smaller-instance (SB) remains, i.e. C funnels into the
  same residual gap.
- **A slice of Regime B2** (A_1 < 1 − c(n)) with A_2 ≥ 2^{n−1}/D is closed at the top by **R3**
  (q = A_2 ≥ τ/2 = 2^{n−1}/D), reducing to a smaller instance.
- Regime A and B1 remain independently closed by the certified shadow / partial-shadow lemmas; the R6
  framework is a complementary, unifying route, not a replacement.

## The gap and the recorded dead-end (do not retry the naive induction)

The gap case (distinct X, p_1 < τ, p_2 < τ/2) is the "spread/small-max" configuration; the natural move
is the **partial-shadow** cut of p_1 into a greedy prefix of copies {p_2, p_3, …, p_{j+1}, s}
(s = p_1 − (p_2 + ⋯ + p_{j+1}) < p_{j+2}), removing j parity-invisible pairs with j cuts and leaving the
residual R′ = {s, p_{j+2}, …} of mass Σ(R′) = Σ − 2(p_1 − s), budget b − j. **This move does NOT
preserve the sum-bound invariant:** the inequality Σ(R′)/D_{b−j} ≤ Σ/D_b that a clean induction would
need fails on many instances (18 / 123 / 315 / 678 instances at n = 3 / 4 / 5 / 6 in the deterministic
recursion), because partial-shadow can leave *too much residual mass* for the reduced budget while the
final A still comes out ≤ 1/D via slack accrued elsewhere. Hence closing the gap requires a potential
strictly stronger than the running sum Σ — the honest open problem. (A brute strategy search *does*
reach μ ≤ 1/D on every sampled gap config, so (SB) is almost certainly true; only a *proof* through the
gap is missing.)

---

# R7: gap-case sub-closure (Case A.A) and the SB-obstruction theorem

Throughout, (X, b) is a **gap-case** instance of the sum-bound induction: X = {p₁ > p₂ > ⋯ > p_m}
distinct, b ≥ 1, τ := Σ·2^b/D_b, with **p₁ < τ** and **p₂ < τ/2** (hence p_j < τ/2 for all j ≥ 2). Two
structural facts feed the arguments below.

**Budget invariant.** Every instance reached by the R1/R2/R3 reductions from an LB config (base
|X| = m ≤ n + 1 at b = n) satisfies **|X| ≤ b + 1**. Indeed R1 sends (|X|, b) ↦ (|X| − 2, b), R2 sends
(|X|, b) ↦ (|X| − 1, b − 1), and R3 sends (|X|, b) ↦ (|X| − 1, b − 1); each preserves |X| ≤ b + 1
(check: |X| ≤ b + 1 ⟹ |X| − 1 ≤ b = (b − 1) + 1, and |X| − 2 ≤ b − 1 ≤ b + 1). In particular in any
gap case **m ≤ b + 1**, so **m − 1 ≤ b**.

**Threshold identity (exact).** **2τ − Σ = Σ/D_b.** Proof:
2·Σ·2^b/D_b − Σ = Σ(2^{b+1} − D_b)/D_b = Σ(2^{b+1} − (2^{b+1} − 1))/D_b = Σ/D_b. (Confirmed by the
outline-reviewer; verified exact for b = 1..6.)

## Case A.A (dominant-in-gap): p₁ > Σ/2. **[Proved this round; CLOSED.]**

Because p₁ > Σ/2 = ½(p₁ + p₂ + ⋯ + p_m) we have **p₁ > p₂ + ⋯ + p_m**, hence a fortiori
p₁ > p₂ + ⋯ + p_j for every j ≤ m. Xiang Yu performs the **subtract-all chain**: for j = 2, 3, …, m in
turn, cut the current leftover

  L_{j−1} := p₁ − (p₂ + ⋯ + p_{j−1})   (with L_1 = p₁)

at interior offset p_j, into the two subpieces (p_j, L_{j−1} − p_j). The cut at step j is legal exactly
when L_{j−1} > p_j, i.e. p₁ > p₂ + ⋯ + p_j — which holds by the display above. The chain uses **m − 1
cuts**, and m − 1 ≤ b by the budget invariant, so it is within budget; all cut points are strictly
interior to descendants of p₁, hence distinct from LB's marks and from one another (all sublengths
positive), a legal placement.

The resulting multiset consists of:
- the m − 1 spectator pieces {p₂, p₃, …, p_m} (never cut), and
- the m carved subpieces of p₁, namely {p₂, p₃, …, p_m, L_m}, where
  L_m = p₁ − (p₂ + ⋯ + p_m) = p₁ − (Σ − p₁) = **2p₁ − Σ > 0** (positive since p₁ > Σ/2).

Thus each value p_j (2 ≤ j ≤ m) occurs an **even** number of times (exactly twice), and the only piece
of odd multiplicity contribution is L_m. By the parity-invisibility mechanism of Lemma R1 (each equal
pair adds an even amount to N(x) for every x), N_final(x) ≡ 𝟙[L_m > x] (mod 2); hence by Lemma M0,

  **A(final) = measure[0, L_m) = L_m = 2p₁ − Σ.**

Applying p₁ < τ (gap case) and the threshold identity 2τ − Σ = Σ/D_b,

  **μ(X, b) ≤ A(final) = 2p₁ − Σ < 2τ − Σ = Σ/D_b   (strict).**

So (SB) holds — strictly — for every gap-case instance with p₁ > Σ/2. ∎ (Case A.A)

*Scope.* Case A.A closes exactly the window **p₁ ∈ (Σ/2, τ)**, of width τ − Σ/2 = Σ(2^b/D_b − 1/2) =
Σ/(2D_b): a genuine but **thin** sliver of the gap case (for Σ = 1, b = 3 it is p₁ ∈ (1/2, 8/15), width
1/30). The bulk of the gap case, p₁ ≤ Σ/2, is not covered — see the obstruction below.
*(Verified: the subtract-all chain is feasible and gives A = 2p₁ − Σ on 3000 random p₁ > Σ/2 configs,
0 anomalies.)*

## The SB-obstruction theorem (why the residual p₁ ≤ Σ/2 is genuinely hard). **[Proved this round.]**

For the residual gap case p₁ ≤ Σ/2 the subtract-all chain is infeasible (L_m = 2p₁ − Σ ≤ 0). The natural
next move is a **single parity-invisible pairing step**: choose a piece q of X, cut p₁ at interior
offset q into (q, p₁ − q), delete the invisible pair {q, q}, and pass to

  X' := (X ∖ {p₁, q}) ∪ {p₁ − q},   Σ' = Σ − 2q,   budget b − 1.

Exactly as in Lemma R3, this reduction is **unconditional**: the pair {q, q} is parity-invisible, so
μ(X, b) ≤ μ(X', b − 1). What R3 *additionally* requires — and the gap case denies — is the arithmetic
Σ'/D_{b−1} ≤ Σ/D_b that would let the sum-bound for X' imply it for X.

**Theorem (SB-obstruction).** For the pairing step at a piece q,

  **Σ'/D_{b−1} ≤ Σ/D_b   ⟺   q ≥ τ/2 = Σ·2^{b−1}/D_b.**

*Proof.* Σ' = Σ − 2q and D_b − D_{b−1} = (2^{b+1} − 1) − (2^b − 1) = 2^b. Hence
  (Σ − 2q)/D_{b−1} ≤ Σ/D_b
  ⟺ (Σ − 2q)·D_b ≤ Σ·D_{b−1}
  ⟺ Σ(D_b − D_{b−1}) ≤ 2q·D_b
  ⟺ Σ·2^b ≤ 2q·D_b
  ⟺ q ≥ Σ·2^{b−1}/D_b = τ/2. ∎ (verified: 0 anomalies / 20000 random (b, Σ, q))

**Corollary (the gap case blocks every SB-monotone step).** In a gap case every piece satisfies
q ≤ p₂ < τ/2; therefore for **every** choice of pairing piece q,

  **Σ'/D_{b−1} > Σ/D_b   (strict).**

Consequently the proposed *gap-step-then-R3* route cannot close the residual by **chaining the
sum-bound**: after the gap-step, R3 (or R2, or the base case) can only certify μ(X', b − 1) ≤
Σ'/D_{b−1}, and Σ'/D_{b−1} already **exceeds** the target Σ/D_b. The same holds for R2's own bound and
for the base bound Σ_leaf/D_0. Hence *any* proof of the residual must track the **actual** alternating
sum A through the multi-step recursion — a potential strictly stronger than the running sum Σ — rather
than any SB-monotone reduction. This is a rigorous proof of the round-6 recorded dead-end (partial-shadow
does not preserve the invariant) and sharpens it: it is not partial-shadow specifically, but **every**
invisible-pair step in a gap case that breaks SB. It also refines the outliner's gap-step-then-R3
mechanism: the "then-R3" cannot be an SB-chaining.

*(Numerically the residual bound itself is comfortably true: under a budget-respecting exact search, all
n = 3 residual gap cases at denominator 30 achieve actual μ·D_b ≤ 1/2 — half the target 1/D_b — so (SB)
certainly holds throughout the residual; only its *proof*, via the missing actual-A potential, is
absent.)*

## Status of the gap case after R7

- **p₁ > Σ/2 (Case A.A): CLOSED** (strict), no induction.
- **p₁ ≤ Σ/2 (residual, the bulk): OPEN.** The SB-obstruction theorem shows no SB-monotone reduction can
  reach it; closing it needs an actual-A potential. This is the single remaining upper-bound gap in this
  approach.

---

# R8: residual gap case closed for m = 3 (actual-A potential), and the m ≥ 4 obstruction

Throughout, (X, b) is a **residual gap-case** instance of the sum-bound induction: X = {p₁ > p₂ > ⋯ > p_m}
distinct positive pieces, |X| = m ≤ b + 1 (budget invariant), Σ = Σ(X), D_b = 2^{b+1} − 1,
τ := Σ·2^b/D_b, with **p₁ < τ**, **p₂ < τ/2** (hence every piece p_j < τ/2 for j ≥ 2), and
**p₁ ≤ Σ/2** (the residual not covered by Case A.A). The goal is (SB): μ(X, b) ≤ Σ/D_b.

## Lemma R4 (gap-case m = 3 closure). **[Proved this round; CLOSED.]**

**Statement.** Let X = {p₁ > p₂ > p₃} be three distinct positive pieces with |X| = 3 ≤ b + 1 (so b ≥ 2),
Σ = p₁ + p₂ + p₃, τ = Σ·2^b/D_b, satisfying the residual gap hypotheses **p₂ < τ/2, p₃ < τ/2, and
p₁ ≤ Σ/2**. Then

  **μ(X, b) ≤ A(final) = Σ − 2p₁ < Σ/D_b   (strict).**

**Proof.** *The strategy (one R3 cut).* Since p₁ > p₂ > 0, Xiang Yu cuts p₁ at the interior offset p₂
into the two subpieces (p₂, p₁ − p₂), with p₁ − p₂ > 0. This is one cut, and 1 ≤ b (as b ≥ 2), so it is
within budget; the cut point is strictly interior to p₁, hence distinct from Liu Bang's marks and legal.
The freshly-cut subpiece of length p₂ equals the untouched spectator piece p₂, so the final multiset is

  F = {p₂, p₂} ∪ {p₁ − p₂, p₃}.

*The value of A(F).* The pair {p₂, p₂} contributes 2·𝟙[p₂ > x] — an even amount — to N_F(x) for every x,
so by the parity-invisibility mechanism (Lemma R1, imported/certified `sum-bound-reductions.md`)
N_F(x) ≡ N_{{p₁−p₂, p₃}}(x) (mod 2) for all x, and by Lemma M0 (certified `alt-sum-integral.md`)
A(F) = A({p₁ − p₂, p₃}) = |p₃ − (p₁ − p₂)| (the alternating sum of a two-element multiset is the absolute
difference). We determine the sign. From p₁ ≤ Σ/2 = ½(p₁ + p₂ + p₃) we get p₁ ≤ p₂ + p₃, i.e.

  **p₃ ≥ p₁ − p₂ ≥ 0.**

Hence p₃ is the larger of the two effective pieces, and

  **A(F) = p₃ − (p₁ − p₂) = (p₂ + p₃) − p₁ = (Σ − p₁) − p₁ = Σ − 2p₁ ≥ 0.**                    (R4-A)

*The bound.* The gap hypotheses give p₂ < τ/2 and p₃ < τ/2, hence

  **p₂ + p₃ < τ,   equivalently   p₁ = Σ − (p₂ + p₃) > Σ − τ = Σ(D_b − 2^b)/D_b = Σ(2^b − 1)/D_b,**

using D_b − 2^b = (2^{b+1} − 1) − 2^b = 2^b − 1. Substituting into (R4-A) and invoking the **exact
identity**

  **D_b − 2(2^b − 1) = (2^{b+1} − 1) − (2^{b+1} − 2) = 1   (for every b ≥ 1),**                (ID)

we obtain

  A(F) = Σ − 2p₁ < Σ − 2·Σ(2^b − 1)/D_b = Σ·[D_b − 2(2^b − 1)]/D_b = Σ·1/D_b = Σ/D_b   (strict).

Therefore μ(X, b) ≤ A(F) < Σ/D_b, which is (SB) — strictly. ∎ (Lemma R4)

*(Verified: A(F) = Σ − 2p₁ exactly and A(F) < Σ/D_b with 0 mismatches / 0 violations over 1351 exact
budget-respecting m = 3 residual gap configs; identity (ID) exact for b = 1..8.)*

## Corollary R4.1 (gap case closed for all m ≤ 3; the upper bound is rigorous at n = 2).

For a gap-case instance (distinct X, p₁ < τ, p₂ < τ/2):

- **m = 2.** X = {p₁ > p₂}. Then p₁ > p₂ ⟺ p₁ > Σ/2, so p₁ > Σ/2 and **Case A.A** (certified
  `gap-caseAA-subtract-chain.md`) gives μ(X, b) = A(final) = 2p₁ − Σ < Σ/D_b (using p₁ < τ and 2τ − Σ =
  Σ/D_b). CLOSED.
- **m = 3.** If p₁ > Σ/2, **Case A.A** closes it (A = 2p₁ − Σ < Σ/D_b). If p₁ ≤ Σ/2, **Lemma R4** closes
  it (A = Σ − 2p₁ < Σ/D_b). These two sub-cases are exhaustive and disjoint. CLOSED.

Hence the gap case is fully closed for every m ≤ 3.

**Consequence at n = 2.** The LB config has Σ = 1, m ≤ n + 1 = 3, budget b = n = 2. Every instance reached
by the R1/R2/R3 reductions from it obeys the budget invariant |X| ≤ b + 1, and every reduction strictly
decreases (b, |X|); each branch either terminates at the base b = 0 (where (SB) holds, μ = A(X) ≤ p₁ ≤ Σ)
or enters a gap case. Every gap case that arises has m ≤ b + 1 ≤ 3 and is closed by Corollary R4.1. Since
the deterministic reducer plus these closures covers **all** branches, (SB) holds for every n = 2 LB
config, i.e. **XY holds every LB config to val ≤ c(2) = 4/7**. This finishes the n = 2 upper bound
rigorously inside the framework (previously Regime C at n = 2 was only by-numeric). ∎ (n = 2 upper bound)

## The m ≥ 4 residual gap: the outline's cascade is refuted; honest open frontier.

For m ≥ 4 the actual-A potential of Lemma R4 does **not** extend: the value Σ − 2p₁ is generally **far
above** the target Σ/D_b. Indeed A = Σ − 2p₁ < Σ/D_b would require p₁ > Σ(2^b − 1)/D_b, whereas in a
residual gap the m pieces are each < τ/2, so p₁ can be as small as ≈ Σ/m; for four near-equal distinct
pieces p₁ ≈ Σ/4 gives Σ − 2p₁ ≈ Σ/2 ≫ Σ/D_b. Consequently the single-shot bound A(final) ≤ Σ − 2p₁ is
useless for m ≥ 4, and one must spend the *whole* remaining budget (up to b cuts) to drive A down.

I tested — with bounded, budget-enforced exact-Fraction computation — every simple deterministic strategy
the round-8 outline proposed for m ≥ 4, and **each fails decisively**:

| Deterministic strategy | gap configs | violate A ≤ Σ/D_b | worst ratio |
|---|---|---|---|
| greedy "cut largest at second-largest" cascade | 29234 | **18385** | 21.2 |
| recursive "R3 at p₂, then recurse" | 2000 | **1314** | 26.6 |
| recursive partial-shadow (all cuts on p₁, recurse on residual) | 2000 | **1268** | 28.8 |

By contrast, the **true optimal** μ, computed by a full bounded search over invisible-pair / halving cuts
(≤ b cuts, budget-enforced), satisfies μ ≤ Σ/D_b with **0 violations** (worst ratio 0.88, at m = 4,
b = 3; e.g. X = {8,4,3,2}, Σ = 17, μ = 1 < 17/15). So (SB) is almost certainly true throughout the m ≥ 4
residual gap, but the optimal strategy genuinely requires **lookahead** (its first cut is not determined
by any of the greedy/recursive rules above), so no monotone one-step potential — in particular not the
outline's A ≤ Σ − 2p₁ cascade — closes it. This matches the R7 **SB-obstruction theorem** (every
invisible-pair step in a gap case strictly breaks the running-sum invariant) and extends its message to
the *actual-A* side: even tracking A, no myopic rule suffices. **The m ≥ 4 residual gap (which only bites
at n ≥ 3) is the honest, still-open upper-bound frontier.**

---

## Verification log (bounded computations, this round)
- **R8 — gap-case m = 3 closure + m ≥ 4 obstruction** (exact Fractions, budget-enforced):
  (a) Identity (ID) D_b − 2(2^b − 1) = 1: exact for b = 1..8.
  (b) Lemma R4: over 1351 m = 3 residual gap configs (distinct integer pieces, p₁ ≤ Σ/2, budget b with
  m ≤ b + 1), the one-cut value equals Σ − 2p₁ with **0** mismatches, and Σ − 2p₁ < Σ/D_b with **0**
  violations.
  (c) m ≥ 4 refutations (budget invariant m ≤ b + 1 enforced in every config): greedy-largest-pair
  cascade **18385/29234** violations; recursive R3-at-p₂ **1314/2000**; recursive partial-shadow
  **1268/2000**. True optimal μ (bounded DFS over invisible-pair + halving cuts) — **0/60** violations at
  m = 4, b = 3 (worst ratio 0.88), and 0 in a 300-config sample; μ ∈ {0, 1} on integer configs, always
  below the target Σ/D_b > 1.
- **R6 — sum-bound framework** (exact Fractions throughout):
  (a) Strategy search (halve / pair-any / shadow-all / free-remove, branch-limited) achieves μ ≤ 1/D on
  **every** sampled LB config (Σ = 1, m ≤ n + 1), n = 1..5: 0 configs beat 1/D; worst μ matches the
  geometric 1/D only near the geometric config.
  (b) Deterministic reducer using only R1/R2/R3 (rigorous moves): closed 100 / 99.3 / 96.7 / 93.8 / 89.9
  / 85.6 % of configs at n = 1..6, with **0** bound violations among closed configs (confirming R1–R3
  are correct). Uncovered fraction = the gap case.
  (c) Adding the partial-shadow move closes the recursion to μ ≤ 1/D (0 fails, n = 1..6) but the
  sum-bound invariant Σ(R′)/D_{b−j} ≤ Σ/D_b is **violated** 18 / 123 / 315 / 678 times at n = 3/4/5/6 —
  proving partial-shadow cannot be the inductive step for (SB).
- **R5 — Regime B**: (a) partial-shadow key facts over 80000 random flat configs (m ≤ 9, exact
  Fractions): val ≤ 1 − A_1, A(R') ≤ 1 − 2A_1, Σ_even(R') ≥ s — **0 violations each**; identities
  Σ R' = 1 − 2A_1 + 2s and A = Σ − 2Σ_even confirmed exact. (b) B1 partial-shadow within the regime
  A_1 ≥ 1 − c(n): 0/5482 fail val ≤ c(n). (c) Naive "one cut at A_2" FAILS for m > 3 in-regime
  (289/3891), confirming the prefix is needed. (d) n = 2 Regime B exhaustive DENOM = 84: 820 configs,
  0 fail, worst B1 = 4/7, worst B2 = 47/84; identities val = 1 − A_1 and val = A_1 + A_3/2 exact.
- **Regime A shadow**: 200 random configs with 1/2 ≤ A_1 ≤ c(n) (n ≤ 4): val = A_1 exactly (Fractions),
  all ≤ c(n). 0 mismatches.
- **LL two-sided bound (LL-partial)**: n = 3 grid, 286 (Q, R) configs. True A(Q ∪ R) < 1: **0** configs
  (LL is true). Bound b + |a − A(R)| < 1: **34** configs (bound insufficient). Confirms LL t ≥ 2 needs
  a joint B-bound beyond merge.
- Prior rounds: Lemma G = brute-force minimax (0 mismatches, 2000 trials); merge lemma (0 violations,
  20000 trials); lower-bound worst-case val = 2^n for n = 1, 2, 3; replica value = 2^n for n = 1, 2, 3.
- **R7 — gap-case Case A.A + SB-obstruction** (exact Fractions, budget-respecting):
  (a) Subtract-all chain feasible and A(final) = 2p₁ − Σ on 3000 random configs with p₁ > Σ/2: 0
  anomalies. (b) Threshold identity 2τ − Σ = Σ/D_b exact for b = 1..6. (c) SB-obstruction equivalence
  Σ'/D_{b−1} ≤ Σ/D_b ⟺ q ≥ τ/2: 0 anomalies / 20000 random (b, Σ, q). (d) n = 3 gap-case census at
  denominator 30 (budget-respecting μ search, cut menu = pair-at-value + halve, ≤ b cuts): 7 gap cases,
  all residual (p₁ ≤ Σ/2), all with actual μ·D_b ≤ 1/2 (worst = 1/2, well inside target 1); SB invariant
  fails on the gap-step at p₂ in 7/7 (consistent with the obstruction corollary).

# Open gaps (precise)
- **LL, sub-case t ≥ 2 with A(Q) > 0** (lower bound): A(Q ∪ R) ≥ 1 where Q partitions 2^n into ≥ 3 parts
  with A(Q) > 0 and R refines G_{n−1} with A(R) ≥ 1, max(R) ≤ 2^{n−1}. The two-sided merge bound
  b + |a − A(R)| is provably too weak (34/286). Needs a joint bound on B = measure(S_Q ∩ S_R) from R's
  dyadic refinement structure (strengthened IH). Load-bearing shared gap.
- **Upper bound — the unified sum-bound gap (R6/R7)**: (SB) μ(X, b) ≤ Σ/(2^{b+1}−1) is proved for every
  (X, b) whose R1/R2/R3 reduction tree avoids the **gap case** (distinct X, p_1 < τ, p_2 < τ/2,
  τ = Σ·2^b/D_b), **(R7) for every gap case with p₁ > Σ/2 (Case A.A, strict)**, and **(R8) for every gap
  case with m ≤ 3 (Lemma R4 handles m = 3, p₁ ≤ Σ/2; Case A.A handles m = 2 and p₁ > Σ/2)**. In
  particular the whole upper bound is now **rigorous at n = 2** via the framework (Corollary R4.1). This
  single gap subsumes the old B2-general and Regime-C gaps. **Remaining gap: the residual gap case with
  p₁ ≤ Σ/2 AND m ≥ 4** (only occurs at n ≥ 3, since m ≤ b + 1). The R8 numeric study **refutes** the
  outline's proposed m ≥ 4 potential: the bound A(final) ≤ Σ − 2p₁ is FALSE for m ≥ 4, and all three
  candidate deterministic strategies (greedy-largest-pair cascade, recursive R3-at-p₂, recursive
  partial-shadow) violate μ ≤ Σ/D_b on a majority of configs; yet the true optimal μ obeys the bound
  (0 violations), so the truth is (SB) but the strategy needs *lookahead*. Combined with the R7
  **SB-obstruction theorem** (no SB-monotone reduction reaches the residual; Σ'/D_{b−1} > Σ/D_b ⟺
  q < τ/2, exact), the m ≥ 4 residual gap is the honest, still-open upper-bound frontier. *(Regime A, B1
  remain independently CLOSED; Regime B and the whole upper bound closed at n = 2.)*

## Promotable lemmas
- **Lemma HS-A2 (pair2_3 closes the Sub-A-P branch of T5, δ>2t) — NEW this round (R13).** *Statement:*
  let `X = {p₁>p₂>p₃>p₄>p₅}` be an m=5 pure hard case (Σ=31t, t=Σ/31, `p₁≤Σ/2`, all `d_j>t`, `δ:=p₅>t`,
  (I) `p₁<16t`, (II) `p₂<8t`) with **δ>2t** and the Sub-A-P firing condition `D1_{Y'}:=d₁−p₃ ≥ δ+d₄`.
  Then the pair2_3 cut (cut `p₂` at offset `p₃`, invisible pair by Lemma R1) yields the effective 4-piece
  instance `Y″={p₁,d₂,p₄,δ}` at budget 3 with `min A(Y″,3) ≤ t`; hence `μ(X,4) ≤ t`. *Proof (full above,
  section R13):* the Σ-P bound `2d₂ ≤ 31t−7δ−6d₄−4d₃` [*] (from `D1_{Y'}=31t−6δ−5d₄−4d₃−2d₂` and the
  firing condition) plus a 6-case exhaustive/disjoint split on the sorted position of `d₂` in `Y″`; each
  case closes by a named ≤3-cut strategy re-derived from Lemma R1: A (R, `A≤(31t−9δ−8d₄−4d₃)/2<t/2`),
  B1 (S, `A≤d₂−δ<t`), B2 (R, `[*]⇒d₄<7t/6`, `A≤d₄−t<t/6`), C1 (S, `A≤δ−d₂≤t`), C2 (halve `p₁`, cut
  `p₄@δ`, finish `{d₄,d₂}` ⟹ `A≤|d₄−d₂|<t`, both `d₄,d₂∈(t,2t)`), C3 (VACUOUS: `[*]⇒2d₂<0`). Verified
  0 violations / 12422 off-grid exact-Fraction genuine configs; R12 witness is Case C1. *Scope:* closes
  ONLY the Sub-A-P/δ>2t branch — NOT all of T5 (gap G1: pair1_2 merge family for Sub-A-C/Sub-B and δ≤2t)
  and NOT m≥6 (gap G3). Proposed at `results/imo-2026-03/lemmas/HS-A2.md`.
- **Lemma MK (μ(k pieces, k−1 cuts) ≤ min(pieces)) — NEW this round (R11).** *Statement:* for any finite
  multiset X of k ≥ 1 positive lengths and budget b = k − 1, `μ(X, k−1) ≤ min(X)`. *Proof (full in
  `lemmas/MK.md`):* induction on k; halve the largest piece into an equal (parity-invisible) pair (Lemma
  R1) and recurse on the remaining k − 1 pieces with k − 2 cuts; bases k = 1 (`A = p₁ = min`), k = 2
  (halve `p₁` → effective `{p₂}`, `A = p₂ = min`); total cuts `1 + (k−2) = k−1`. *Consequence (Corollary
  MK.1):* the residual gap-case easy sub-cases close **uniformly for all m** — if `δ = p_m ≤ t` apply MK
  to X directly; if `d_j = p_j−p_{j+1} ≤ t` do one pairing cut `p_j@p_{j+1}` then MK on the m−1 effective
  pieces, `A ≤ min ≤ d_j ≤ t`. Verified 0 violations / 4000 random configs (MK-strategy A ≤ min) and
  0/4000 (easy-case A ≤ d_j). Written to `results/imo-2026-03/lemmas/MK.md` for certification.
- **Case A.A at arbitrary threshold t (all m) — REFINEMENT this round (R11).** *Statement:* for m distinct
  pieces with `q₁ > Σ/2`, `q₁ < 2^{m−1}t`, and `Σ ≥ (2^m−1)t`, the subtract-all chain (`m−1` cuts) yields
  `A = 2q₁ − Σ < t`, so `μ(X, m−1) < t`. *Proof:* `2q₁ − Σ < 2·2^{m−1}t − (2^m−1)t = t`. This is the
  certified Case A.A stated with a free threshold (needs only `Σ ≥ (2^m−1)t`, not equality), so it applies
  to subproblems too. Verified 0 violations (m = 3,4,5). (Absorb into `gap-caseAA-subtract-chain.md` as the
  threshold-invariant corollary.)
- **Lemma T4 ((T) at m = 4; the n = 3 upper-bound crux) — NEW this round.** *Statement:* let
  `X = {p₁ > p₂ > p₃ > p₄}` be four distinct positive reals with `Σ = Σpᵢ`, `t = Σ/15`, satisfying the
  residual gap conditions `p₁ ≤ Σ/2` and `p₂ < 4Σ/15`. Then Xiang Yu has a legal `≤ 3`-cut strategy with
  `A(final) ≤ t`, i.e. `μ(X, 3) ≤ Σ/15`. *Proof (full above, "R10"):* with `d₁=p₁−p₂, d₂=p₂−p₃, d₃=p₃−p₄,
  δ=p₄`, the gap conditions read (1) `d₁ ≤ 2δ+d₃`, (2) `δ+d₂+d₃ < 4t`, and (2′) `7d₂+3d₃ < δ+4d₁`. Four
  two-pairing-cut strategies give `A_R ≤ d₂`, `A_S ≤ min(|d₁−d₃|, d₃)`, `A_P ≤ δ/2` (if `d₁ ≥ δ+d₃`),
  `A_C ≤ δ+d₃−d₁` (if `d₁ ≤ δ+d₃`), each via the "two effective pieces `{u,v}` + one final cut ⟹
  `A ≤ min(u−v, v)`" reduction. Case split `d₂≤t` (R) / `d₃≤t` (S) / `|d₁−d₃|≤t` (S) is exhaustive with
  Case 4 (`d₂,d₃>t, |d₁−d₃|>t`): Sub-case `d₃>d₁` is impossible ((2′)⇒`10t<δ+d₁`, (2)⇒`δ+d₁<2t`, so
  `8t<0`); Sub-case `d₁>d₃` gives `δ<2t` (from (2)), and P or C (complementary) yields `A < t`. Purely
  algebraic, no integrality. *Consequence:* with Cor R4.1 (m≤3) and Cor AB.1 (b≥4⇒μ=0), the **n = 3
  upper bound `val ≤ c(3) = 8/15` is rigorous**. Verified 0 violations / 1528 budget-enforced residual
  gap configs (worst A/t = 0.9375). Propose to `results/imo-2026-03/lemmas/tight-m4-inequality.md`.
- **Lemma AB (abundant budget) — NEW this round.** *Statement:* for every finite multiset X of positive
  lengths and every integer budget b ≥ |X|, `μ(X, b) = 0`. *Proof (full above, "Lemma AB"):* the pairing
  reduction cuts the current largest piece `a` at offset = another piece `b'` (forming the invisible pair
  `{b', b'}`, leaving `a − b'`), dropping the piece count by 1 per cut; after `≤ |X| − 1` cuts one piece
  `w` remains, and one further cut halves it into an invisible pair, so `A = 0` with `≤ |X| ≤ b` cuts.
  *Consequence (Corollary AB.1):* under the budget invariant `|X| ≤ b + 1`, the residual gap case is
  nontrivial only at the **tight budget `b = |X| − 1`**; all looser budgets give `μ = 0 ≤ Σ/D_b`. This
  reusably closes any instance with slack budget. Verified 0/3000. Proposed to
  `results/imo-2026-03/lemmas/abundant-budget.md`.
- **Sum-bound reduction lemmas R1/R2/R3 (upper bound, all regimes).** *Statement:* with
  μ(X, b) = min over ≤ b cuts of A(result), Σ = Σ(X), D_b = 2^{b+1}−1: **(R1)** an equal pair {w, w}
  gives μ(X, b) ≤ μ(X∖{w,w}, b); **(R2, halving)** if max piece p_1 ≥ Σ·2^b/D_b then μ(X, b) ≤
  μ(X∖{p_1}, b−1) and this is ≤ Σ/D_b whenever the reduced instance obeys the sum-bound; **(R3, pairing)**
  if some piece q ≥ Σ·2^{b−1}/D_b then μ(X, b) ≤ μ((X∖{p_1,q})∪{p_1−q}, b−1), likewise ≤ Σ/D_b. Each is
  proved in full above via one parity-invisible pair plus the stated D_b arithmetic (both equivalences
  derived line-by-line). *Consequence:* the sum-bound μ ≤ Σ/D_b — hence the full upper bound val ≤ c(n)
  for LB configs (Σ = 1, b = n) — holds for every config whose reduction tree avoids the gap case, and
  **Regime C's opening cut (halve A_1 when A_1 > c(n)) is rigorous** (R2 at the top level). Proposed to
  `results/imo-2026-03/lemmas/sum-bound-reductions.md`.
- **Lemma LL, sub-case t = 1 (single cut of the largest geometric piece).** *Statement:* if Q = {q, 2^n − q}
  (q ≤ 2^{n−1}) partitions 2^n and R refines G_{n−1} with A(R) ≥ 1 and max(R) ≤ 2^{n−1}, then
  A(Q ∪ R) ≥ 1. *Proof:* the Q-odd region is the single interval [q, 2^n − q); B ≤ (max(R) − q)^+ ≤
  2^{n−1} − q cancels A(Q) = 2^n − 2q down to A(R) ≥ 1. Proved in full above ("LL, t = 1"). Proposed to
  `results/imo-2026-03/lemmas/ll-t1-single-cut.md`.
- **Shadow strategy (upper bound, Regime A).** *Statement:* if LB's pieces have A_1 ∈ [1/2, c(n)], XY can
  cut A_1 (≤ n cuts) so that val(final) = A_1 ≤ c(n). *Proof:* carving A_1 into {A_2, …, A_m, r},
  r = 2A_1 − 1, doubles every non-A_1 piece, so N is even except on [0, r); A(final) = r, val = A_1.
  Proved in full above ("Regime A"). Proposed to `results/imo-2026-03/lemmas/shadow-regime-A.md`.
- **Partial-shadow prefix (upper bound, Regime B / any A_1 < 1/2).** *Statement:* for LB pieces
  A_1 ≥ ⋯ ≥ A_m (m ≤ n + 1, Σ = 1) with A_1 < 1/2, XY using ≤ k − 1 ≤ n cuts (k = max index with
  A_2 + ⋯ + A_k ≤ A_1) forces **val ≤ 1 − A_1**. Consequently, if A_1 ≥ 1 − c(n) then val ≤ c(n)
  (sub-regime B1, all n). *Proof:* carve A_1 into {A_2, …, A_k, s}, s = A_1 − (A_2 + ⋯ + A_k) < A_{k+1};
  the doubled A_2, …, A_k are parity-invisible, so A(final) = A(R'), R' = {s, A_{k+1}, …, A_m}. Then
  Σ R' = 1 − 2A_1 + 2s and Σ_even(R') ≥ p_2 ≥ s (two elements of R' are ≥ s), so A(R') = Σ R' −
  2Σ_even ≤ 1 − 2A_1, giving val = (1 + A(R'))/2 ≤ 1 − A_1. Proved in full above ("Regime B / partial-
  shadow prefix / B1"). Proposed to `results/imo-2026-03/lemmas/partial-shadow-B1.md`.
- **Regime B at n = 2 (m = 3), full.** *Statement:* if A_1 < 1/2 with three LB pieces, XY forces
  val ≤ c(2) = 4/7 using ≤ 2 cuts. *Proof:* B1 (A_1 ≥ 3/7) one cut, val = 1 − A_1; B2 (A_1 < 3/7)
  sub-cases A_1 > A_2 (two cuts, val = A_1 + A_3/2, ε cancels via the parity-invisible A_3/2 pair) and
  A_1 = A_2 (one cut, val = 1/2); all ≤ 4/7. Proved in full above. Could be folded into
  `results/imo-2026-03/lemmas/partial-shadow-B1.md` or its own file.
- **Gap-case Case A.A closure (upper bound, subtract-all chain).** *Statement:* let X = {p₁ > ⋯ > p_m}
  be distinct with |X| ≤ b + 1, Σ = Σ(X), τ = Σ·2^b/D_b, and suppose **p₁ > Σ/2** and **p₁ < τ**. Then
  μ(X, b) ≤ 2p₁ − Σ < Σ/D_b (strict). *Proof:* the subtract-all chain (cut p₁ successively at p₂, …, p_m,
  m − 1 ≤ b cuts) doubles every non-p₁ piece (parity-invisible) and leaves the single leftover
  L_m = 2p₁ − Σ > 0, so A(final) = L_m; the exact threshold identity 2τ − Σ = Σ/D_b and p₁ < τ give the
  strict bound. Proved in full above ("Case A.A"). Closes the gap-case sub-window p₁ ∈ (Σ/2, τ). Proposed
  to `results/imo-2026-03/lemmas/gap-caseAA-subtract-chain.md`.
- **SB-obstruction theorem (upper bound, negative result).** *Statement:* for a parity-invisible pairing
  step at a piece q (Σ' = Σ − 2q, budget b − 1), **Σ'/D_{b−1} ≤ Σ/D_b ⟺ q ≥ τ/2 = Σ·2^{b−1}/D_b**.
  *Consequence:* in a gap case (every piece q ≤ p₂ < τ/2) every such step strictly increases the
  sum-bound ratio, so no SB-monotone reduction (partial-shadow, or gap-step-then-R3 as an SB-chaining)
  can close the residual p₁ ≤ Σ/2; an actual-A potential is required. *Proof:* one-line arithmetic from
  D_b − D_{b−1} = 2^b. Proved in full above ("SB-obstruction theorem"). Proposed to
  `results/imo-2026-03/lemmas/sb-obstruction.md`.
- **Gap-case m = 3 closure (Lemma R4, upper bound, actual-A potential).** *Statement:* let
  X = {p₁ > p₂ > p₃} be three distinct positive pieces with 3 ≤ b + 1, Σ = Σ(X), τ = Σ·2^b/D_b, and
  suppose the residual gap hypotheses **p₂ < τ/2, p₃ < τ/2, p₁ ≤ Σ/2**. Then μ(X, b) ≤ A(final) =
  Σ − 2p₁ < Σ/D_b (strict). *Proof:* XY makes one R3 cut of p₁ at offset p₂ → parity-invisible pair
  {p₂, p₂} and effective pieces {p₁ − p₂, p₃}; p₁ ≤ Σ/2 ⟹ p₃ ≥ p₁ − p₂, so A(final) =
  p₃ − (p₁ − p₂) = Σ − 2p₁; the gap gives p₂ + p₃ < τ ⟹ p₁ > Σ(2^b − 1)/D_b, and the exact identity
  D_b − 2(2^b − 1) = 1 yields Σ − 2p₁ < Σ/D_b. Proved in full above ("Lemma R4"). *Consequence
  (Corollary R4.1):* with Case A.A (m = 2 and p₁ > Σ/2), the gap case is CLOSED for all m ≤ 3, and the
  whole upper bound is rigorous at n = 2. Proposed to
  `results/imo-2026-03/lemmas/gap-case-m3-closure.md`.

---

# R9: the m ≥ 4 gap case — abundant-budget lemma + tight-case collapse

Throughout, `X = {p₁ > p₂ > ⋯ > p_m}` is a **residual gap-case** instance of the sum-bound induction:
distinct pieces, `|X| = m ≥ 4`, budget `b`, the **budget invariant** `|X| ≤ b + 1` (so `b ≥ m − 1`),
`Σ = Σ(X)`, `D_b = 2^{b+1} − 1`, `τ = Σ·2^b/D_b`, with the gap hypotheses `p₁ < τ`, `p₂ < τ/2` (hence
`p_j < τ/2` for all `j ≥ 2`) and the residual restriction `p₁ ≤ Σ/2` (the complementary window
`p₁ > Σ/2` is Case A.A, certified for all `m` in `lemmas/gap-caseAA-subtract-chain.md`). Target:
`μ(X, b) ≤ Σ/D_b`.

Recall `μ(X, b) := min over placements of ≤ b interior cut points of A(result)`, `A(P) = measure{x ≥ 0 :
N_P(x) odd}` (Lemma M0). Adding an **equal pair `{w, w}`** to any multiset changes `N` by an even amount
everywhere, hence leaves `A` unchanged — equal pairs are *parity-invisible spectators* (Lemma R1
mechanism, `lemmas/sum-bound-reductions.md`).

## Spec correction: the "complement cut" is not distinct from the "cut-at-pⱼ" for a single cut

The round-9 outline proposes to distinguish "cut `p₁` at offset `pⱼ`" from "cut `p₁` at offset
`p₁ − pⱼ`," asserting the former makes *three* copies of `pⱼ` (odd, uncancelled) and only the latter makes
a pair. **This is incorrect.** Cutting `p₁` at either offset yields the *same unordered fragment pair*
`{pⱼ, p₁ − pⱼ}`; the single fragment of length `pⱼ` together with the one pre-existing piece `pⱼ` is a
**pair `{pⱼ, pⱼ}`** (two copies, not three). So both offsets produce the identical effective sub-instance
`sub = (X ∖ {p₁, pⱼ}) ∪ {p₁ − pⱼ}` and the identical `A`. (This is exactly Lemma R3, whose leftover is
`p₁ − q`.) The R8 "cut-at-pⱼ cascade" refutation concerned a *multi-cut deterministic cascade*, not a
single cut; there is no one-cut parity distinction to exploit.

Moreover the outline's headline reduction — "one such cut reduces `m = 4` to `m = 3`, then apply Lemma R4
(one cut) to the sub" — **does not reach the target.** Lemma R4's one-cut value on the 3-piece sub is
`|2·max(sub) − Σ'|` with `Σ' = Σ − 2pⱼ`; a budget-enforced exact-Fraction scan of the `m = 4` gap region
at `b = 3` finds this value **exceeds `Σ/D_b` on 141 of 367 configs** (worst ratio 2.5, all near-equal,
e.g. `{24, 13, 12, 11}/60`). The sub must be solved with its *full* budget `b − 1`, not one cut.

## Lemma AB (abundant budget). For every finite multiset X of positive lengths and every b ≥ |X|,
`μ(X, b) = 0`.

**Proof.** Write `k = |X|`. Xiang Yu performs the following **pairing reduction**. While at least two
pieces remain, pick any two distinct pieces `a ≥ b'` of the current multiset:
- if `a = b'`, they already form an equal pair; delete both (no cut, parity-invisible), reducing the
  count by 2;
- if `a > b'`, cut the piece `a` at interior offset `b'` (legal: `0 < b' < a`) into `(b', a − b')`. The
  fresh fragment `b'` together with the piece `b'` is an equal pair `{b', b'}` (parity-invisible); the
  surviving new piece is `a − b' > 0`. This removes `a` and `b'` and adds `a − b'`, reducing the count
  by 1 at the cost of **one** cut.

Each step strictly decreases the number of pieces, so after at most `k − 1` cuts the process reaches a
multiset with `≤ 1` piece. If it reaches `0` pieces (all cancelled in equal pairs), then `N ≡ 0` and
`A = 0`. If it reaches a single piece `{w}`, `w > 0`, at most `k − 1 ≤ b − 1` cuts have been used, so at
least one cut remains: cut `w` at its midpoint into `(w/2, w/2)` — an equal pair, parity-invisible — after
which `N` is even everywhere and `A = 0`.

In every case the number of cuts used is `≤ k ≤ b`, and the final multiset has `A = 0`, so
`μ(X, b) ≤ 0`, i.e. `μ(X, b) = 0` (as `A ≥ 0` always). All cut points are strictly interior to distinct
current pieces, hence occupy distinct stick-positions and are disjoint from Liu Bang's marks (the piece
boundaries) — a legal placement. ∎

*(Verified: the deterministic "pair the two largest, then halve" instance of this reduction gives `A = 0`
on 0/3000 failures for random multisets with `b = |X|`.)*

## Corollary AB.1 (the gap case is nontrivial only at tight budget). In the residual gap case, if
`b ≥ m` then `μ(X, b) = 0 ≤ Σ/D_b`. Hence the only case requiring further argument is the **tight budget
`b = m − 1`** (equivalently `|X| = b + 1`).

**Proof.** `b ≥ m = |X|` triggers Lemma AB. The budget invariant forces `b ≥ m − 1`, so the sole
remaining possibility is `b = m − 1`. ∎

*(This is a genuine reduction of the frontier: the R8 statement "m ≥ 4 open for all b ≥ 3" is now sharpened
to "only `b = m − 1` open." Verified: every `m = 4` gap config at `b ∈ {4, 5}` has optimal `μ = 0`.)*

## The tight case b = m − 1: reduction to a finite merge-family inequality

With `b = m − 1` cuts on `m` pieces, Xiang Yu applies the pairing reduction of Lemma AB for `m − 2`
steps, reaching **exactly two effective pieces** `{u, v}` (`u ≥ v > 0`) using `m − 2` cuts, then spends
the last cut on `{u, v}`:
- cut `u` at offset `v` (pair `{v, v}`, single leftover `u − v`) gives `A = u − v`;
- cut `u` at its midpoint (pair `{u/2, u/2}`, spectator `v`) gives `A = v`;

so `A ≤ min(u − v, v)`. (Alternatively XY may run the pairing reduction one further step to a single piece
`w` with `A = w`, using all `m − 1` cuts.) The reachable pairs `{u, v}` — equivalently the reachable
single values `w` — form the **finite merge-family**: all outcomes of `m − 2` (resp. `m − 1`) successive
"replace two pieces `a ≥ b'` by `a − b'`" operations. Each such outcome is an explicit signed combination
of the `p_i` with parity-invisible pairs removed.

**Tight-case inequality (T).** For every residual gap-case `X` with `b = m − 1`,
```
min over the merge-family of A  ≤  Σ / D_{m−1} = Σ / (2^m − 1).
```
Granting (T), `μ(X, m−1) ≤ Σ/D_{m−1}`, and with Corollary AB.1 the entire `m ≥ 4` residual gap case is
closed, completing the upper bound.

---

# R10: (T) for m = 4 — PROVED analytically (closes the n = 3 upper bound in-framework)

We now prove the tight-case inequality **(T) at m = 4** by a direct, purely algebraic four-strategy case
split on the *actual* alternating sum A (no sum-bound, no potential induction). This closes the m = 4
residual gap case, hence — with Corollary AB.1 (b ≥ 4 gives μ = 0) and Corollary R4.1 (m ≤ 3) — the
**entire upper bound at n = 3**.

## Setup and gap conditions (m = 4)

Let `X = {p₁ > p₂ > p₃ > p₄}` be four **distinct** positive pieces, `Σ = p₁+p₂+p₃+p₄`, budget `b = 3`,
`D₃ = 2⁴ − 1 = 15`, `τ = Σ·2³/D₃ = 8Σ/15`, target `t := Σ/D₃ = Σ/15`. The residual gap hypotheses
(inherited from the R1/R2/R3 reducer, Lemma R4 scope, and the p₁ > Σ/2 split of Case A.A) are

- (residual)  **p₁ ≤ Σ/2**   — the complementary `p₁ > Σ/2` is closed for all m by **Case A.A**
  (`gap-caseAA-subtract-chain.md`, certified R7: `A = 2p₁ − Σ < Σ/D_b`), so we may assume `p₁ ≤ Σ/2`;
  note `p₁ ≤ Σ/2 < 8Σ/15 = τ` recovers `p₁ < τ` automatically.
- (gap)  **p₂ < τ/2 = 4Σ/15**.

Introduce the consecutive differences and the base
```
  d₁ = p₁ − p₂ > 0,   d₂ = p₂ − p₃ > 0,   d₃ = p₃ − p₄ > 0,   δ = p₄ > 0,
```
so `p₄ = δ, p₃ = δ+d₃, p₂ = δ+d₂+d₃, p₁ = δ+d₁+d₂+d₃`, and
```
  Σ = 4δ + d₁ + 2d₂ + 3d₃.                                                         (Σ)
```
The two gap hypotheses translate exactly (all reversible):

- **(1)** `p₁ ≤ Σ/2 ⟺ 2p₁ ≤ Σ ⟺ 2(δ+d₁+d₂+d₃) ≤ 4δ+d₁+2d₂+3d₃ ⟺ d₁ ≤ 2δ + d₃.`
- **(2)** `p₂ = δ + d₂ + d₃ < 4t = 4Σ/15.`

From (2) we also derive an equivalent linear form used once below. Multiplying (2) by 15 and using (Σ):
```
  15(δ+d₂+d₃) < 4Σ = 16δ + 4d₁ + 8d₂ + 12d₃
  ⟹  15δ + 15d₂ + 15d₃ − 16δ − 8d₂ − 12d₃ < 4d₁
  ⟹  7d₂ + 3d₃ < δ + 4d₁.                                                         (2′)
```

## The four strategies and their A-bounds

Each strategy performs two **pairing cuts** (cut the larger of two pieces `a > b'` at interior offset
`b'`; the fresh copy of `b'` pairs with an existing `b'` into a parity-invisible pair, by Lemma R1
`sum-bound-reductions.md`; one cut, one fewer effective piece) reaching **two effective pieces** `{u, v}`,
`u ≥ v > 0`. By the tight-case reduction above, the third cut yields
```
  A ≤ min(u − v, v)                                                                (2P)
```
(no third cut ⟹ A = u − v by Lemma M0; halve the larger `u` ⟹ its two halves are an invisible pair and
`A = v`). **Budget:** two pairing cuts + at most one final cut = `≤ 3 = b`; every offset is strictly
interior to a positive current piece, hence a legal mark distinct from LB's boundary marks. For a UB we
need only exhibit **one** legal strategy per configuration achieving `A ≤ t` (existence of a witness), so
"min over the merge-family ≤ t" is the correct direction.

**Strategy R** (matching `{p₁,p₄},{p₂,p₃}`). Cut `p₁` at offset `p₄ = δ` (leftover `p₁−δ = d₁+d₂+d₃`, the
fresh `δ` pairs with the spectator `p₄`); cut `p₂` at offset `p₃` (leftover `p₂−p₃ = d₂`, fresh `p₃` pairs
with spectator `p₃`). Effective `{u,v} = {d₁+d₂+d₃, d₂}` with `u = d₁+d₂+d₃ > d₂ = v`. By (2P), halving `u`:
```
  A_R ≤ v = d₂.                                                                    (R-bound)
```

**Strategy S** (matching `{p₁,p₂},{p₃,p₄}`). Cut `p₁` at `p₂` (leftover `d₁`); cut `p₃` at `p₄ = δ`
(leftover `d₃`). Effective `{d₁, d₃}`. By (2P) (either no final cut, or halve the larger):
```
  A_S ≤ |d₁ − d₃|   and   A_S ≤ min(d₁, d₃) ≤ d₃.                                  (S-bound)
```

**Strategy P** (applicable when `d₁ ≥ δ + d₃`, i.e. `p₁ ≥ p₂ + p₃`). Cut `p₁` at `p₂` (fresh `p₂` pairs
with spectator `p₂`, leftover `d₁ = p₁ − p₂`); then cut that leftover `d₁` at offset `p₃ = δ + d₃` — legal
since `d₁ ≥ p₃` (if `d₁ = p₃`, the leftover is `0` and only the piece `δ` remains, giving `A ≤ δ/2` after
one final halving cut; so assume `d₁ > p₃`) — leaving `d₁ − p₃ = d₁ − δ − d₃`, the fresh `p₃` pairing with
spectator `p₃`. Effective `{u,v} = {δ, d₁ − δ − d₃}`. By gap (1), `d₁ ≤ 2δ + d₃ ⟹ d₁ − δ − d₃ ≤ δ`, so
`u = δ ≥ v = d₁ − δ − d₃ ≥ 0`. By (2P): `A_P ≤ min(u − v, v) = min(2δ + d₃ − d₁,\; d₁ − δ − d₃)`. The two
terms are both `≥ 0` (the first by (1), the second by P's hypothesis) and **sum to δ**, so
```
  A_P ≤ min(2δ + d₃ − d₁,\; d₁ − δ − d₃) ≤ δ/2.                                    (P-bound)
```

**Strategy C** (applicable when `d₁ ≤ δ + d₃`, i.e. `p₁ ≤ p₂ + p₃`). Cut `p₁` at `p₂` (leftover
`d₁ = p₁ − p₂`, fresh `p₂` pairs with spectator `p₂`); then cut `p₃` at offset `d₁` — legal since
`d₁ ≤ p₃ = δ + d₃` — leaving `p₃ − d₁ = δ + d₃ − d₁ ≥ 0`, the fresh `d₁` pairing with the leftover `d₁`.
Effective `{δ, δ + d₃ − d₁}`. When `d₁ ≥ d₃` (the regime where C is invoked below) the larger effective
piece is `δ`; halving it via (2P) leaves the smaller piece, giving
```
  A_C ≤ δ + d₃ − d₁.                                                              (C-bound)
```
P and C are **complementary**: their hypotheses `d₁ ≥ δ+d₃` and `d₁ ≤ δ+d₃` cover all X (both hold, with
`A = 0`, at equality `d₁ = δ+d₃`).

## The case split (target A ≤ t = Σ/15)

**Case 1** (`d₂ ≤ t`). Strategy R: `A_R ≤ d₂ ≤ t`. ✓

**Case 2** (`d₃ ≤ t`). Strategy S: `A_S ≤ d₃ ≤ t`. ✓

**Case 3** (`|d₁ − d₃| ≤ t`). Strategy S: `A_S ≤ |d₁ − d₃| ≤ t`. ✓

**Case 4** (`d₂ > t` **and** `d₃ > t` **and** `|d₁ − d₃| > t`). This is exactly the complement of
Cases 1–3, so Cases 1–4 are **exhaustive**. We split on the sign of `d₁ − d₃`.

**Sub-case B (`d₃ > d₁`) is impossible.** Then `d₃ − d₁ = |d₁ − d₃| > t`, i.e. `d₃ > d₁ + t`, and `d₂ > t`.
Two inequalities collide:
- From (2′), `7d₂ + 3d₃ < δ + 4d₁`. Using `d₂ > t` and `d₃ > d₁ + t`:
  `7t + 3(d₁ + t) < 7d₂ + 3d₃ < δ + 4d₁`, i.e. `10t + 3d₁ < δ + 4d₁`, hence `10t < δ + d₁`.  (X)
- From (2) directly, `δ + d₂ + d₃ < 4t`. Using `d₂ > t` and `d₃ > d₁ + t`:
  `δ + t + (d₁ + t) < δ + d₂ + d₃ < 4t`, i.e. `δ + d₁ + 2t < 4t`, hence `δ + d₁ < 2t`.  (Y)

Chaining (X) and (Y): `10t < δ + d₁ < 2t`, so `8t < 0`, contradicting `t = Σ/15 > 0`. Thus in Case 4,
necessarily `d₁ ≥ d₃`; and since `|d₁ − d₃| > t > 0`, in fact **`d₁ > d₃`** with `d₁ − d₃ > t`.

**Sub-case A (`d₁ > d₃`, `d₁ − d₃ > t`).** First, from (2) with `d₂ > t` and `d₃ > t`,
```
  δ = (δ + d₂ + d₃) − d₂ − d₃ < 4t − t − t = 2t,   i.e.  δ < 2t.                    (Z)
```
Exactly one of P, C applies:
- **P applies** (`d₁ ≥ δ + d₃`). By (P-bound) and (Z): `A_P ≤ δ/2 < t`. ✓
- **C applies** (`d₁ ≤ δ + d₃`, and here `d₁ > d₃`, so C's halving branch is valid). By (C-bound), (Z),
  and `d₁ − d₃ > t`: `A_C ≤ δ + d₃ − d₁ = δ − (d₁ − d₃) < 2t − t = t`. ✓ (Also `δ + d₃ − d₁ ≥ 0` by C's
  hypothesis, so this is a genuine nonnegative bound.)

In every case Xiang Yu has a legal `≤ 3`-cut strategy with `A ≤ t = Σ/15`. Hence
```
  μ(X, 3) ≤ Σ/D₃ = Σ/15   for every residual gap-case X with m = 4.               (T, m=4)
```

## Consequence: the n = 3 upper bound is rigorous

By the R1/R2/R3 induction (`sum-bound-reductions.md`) every instance reached from an LB config with
`n = 3` (so `m ≤ n+1 = 4`, `b = 3`) either terminates at the base `b = 0` (where `μ = A ≤ p₁ ≤ Σ = Σ/D₀`)
or reaches a gap case with `m ≤ b + 1 ≤ 4`. Gap cases with `m ≤ 3` are closed by **Corollary R4.1**
(`gap-case-m3-closure.md`); gap cases with `m = 4` and `b ≥ 4` give `μ = 0` by **Corollary AB.1**
(`abundant-budget.md`); and the one remaining possibility, `m = 4` at the tight budget `b = 3`, is closed
by **(T, m=4)** just proved. Therefore `μ(X, 3) ≤ Σ/D₃ = Σ/15` for every LB config, i.e. (with `Σ = 1`)
`A(final) ≤ 1/15` and `val ≤ (1 + 1/15)/2 = 8/15 = c(3)`. Combined with Liu Bang's geometric construction
attaining `c(3)` (tightness section above), **the n = 3 upper bound `c(3) = 8/15` is rigorous.** ∎ (n = 3 UB)

*(Verification, bounded/exact `Fraction`, budget-enforced `#cuts ≤ 3`: over all 1528 residual gap configs
with `p₄ ≤ 11, Σ` small the four-strategy minimum satisfies `A ≤ t` with **0 violations**, worst ratio
`A/t = 0.9375` at `{25,17,13,9}`; the designated per-case strategy passes every assertion; Sub-case B
occurs **0** times and `δ < 2t` holds in every Sub-case-A config. Runtime < 5 s.)*

## m ≥ 5 (general-n upper bound): OPEN — direct actual-A case-split required

For `m ≥ 5` the tight case is `b = m − 1` and (T) reads `min over merge-family of A ≤ Σ/(2^m − 1)`. The
m = 4 proof is **purely algebraic** (no integrality) and suggests a generalization, but it is **NOT proven
here** and is recorded as the honest open frontier:

- The correct route is the **generalized direct actual-A case-split** (matching strategies covering the
  region where some consecutive difference `d_i ≤ Σ/(2^m − 1)`, plus a P/C-type chain giving
  `A ≤ p_m/2` with the tight gap condition forcing `p_m < 2Σ/(2^m − 1)`). Numerically 0-violation at
  `m = 5` in bounded budget-enforced search, but the generalized Sub-case-B impossibility and the P/C-chain
  bound are **not** yet established in closed form.
- **This is NOT an SB-monotone / pairing-sum induction.** The step `Σ′/(2^{m−1}−1) ≤ Σ/(2^m−1)` needed for
  an SB reduction is **certified DEAD** in the gap case (SB-obstruction theorem, `sb-obstruction.md`,
  R7: it holds iff `q ≥ τ/2`, and every gap-case piece `q ≤ p₂ < τ/2`). Any m ≥ 5 closure must track the
  *actual* A, exactly as the m = 4 proof does.
- The refuted routes (do **not** retry): the R3-cascade potential `A ≤ Σ − 2p₁` (FALSE for m ≥ 4:
  near-equal pieces give `Σ − 2p₁ ≈ Σ/2 ≫ Σ/D_b`); the complement-cut `m=4 → m=3 → R4` one-cut-on-sub
  mechanism (numerically insufficient, 141/367 configs, R9); the partial-shadow SB induction (R6/R7).

**Scope claim (honest).** This round proves the upper bound for **n ≤ 3** in full (n = 1, 2 previously;
n = 3 now via (T, m=4)). The general-n upper bound (m ≥ 5) remains **partial**: reduced to the concrete
finite inequality (T) at each m, with m = 4 discharged and m ≥ 5 an explicit open gap.

---

# R11: reduction of the general-m upper bound to the PURE HARD CASE

This section proves — for **every** m — that the residual gap-case inequality (T) reduces to a single
"hard" sub-case, discharging all other sub-cases uniformly via the new **Lemma MK** and via **Case A.A at
threshold t**. For `m ≤ 4` the hard case is already closed (Cor R4.1 / T4), so this *re-derives* the
n ≤ 3 upper bound through a cleaner uniform mechanism and pins the m ≥ 5 gap to one precise statement.

## Setup and the three carried conditions

Recall (certified `sum-bound-reductions.md` + `abundant-budget.md`) that the whole upper bound reduces to
the **residual gap case at tight budget**: `X = {p₁ > p₂ > … > p_m}` distinct, `Σ = Σpᵢ`, budget
`b = m − 1`, `t := Σ/(2^m − 1) = Σ/D_{m−1}`, `τ := 2^{m−1}t`, with
- **(I)** `p₁ < τ = 2^{m−1}t`   (else Lemma R2 fires — `p₁` too big),
- **(II)** `p₂ < τ/2 = 2^{m−2}t`  (else Lemma R3 fires — `p₂` too big),
- **(III)** `Σ = (2^m − 1)t`  (the definition of `t`; equality at top level, `≥` in subproblems).

Write `d_j := p_j − p_{j+1}` (`1 ≤ j ≤ m−1`) and `δ := p_m`. Target: `μ(X, m−1) ≤ t`.

## Lemma MK and Corollary MK.1 (uniform easy cases) — PROVED, `lemmas/MK.md`

**Lemma MK.** For any `k` positive pieces and budget `k − 1`, `μ ≤ min(pieces)`. *Proof:* induction on
`k`; halve the largest piece into an equal (parity-invisible) pair and recurse on the remaining `k − 1`
pieces with `k − 2` cuts; bases `k = 1` (`A = p₁ = min`), `k = 2` (halve `p₁` → `A = p₂ = min`). Full
proof in `lemmas/MK.md`. ∎

**Corollary MK.1 (easy cases, all m).** In the gap case with `p₁ ≤ Σ/2`:
- **Case 0 (`δ ≤ t`).** Apply Lemma MK to `X` (`m` pieces, `m−1` cuts): `μ(X,m−1) ≤ min(X) = δ ≤ t`. ✓
- **Case j (`d_j ≤ t`, some `1 ≤ j ≤ m−1`).** One pairing cut of `p_j` at interior offset `p_{j+1}`
  (legal, `0 < p_{j+1} < p_j`) makes the fresh `p_{j+1}` pair with the existing `p_{j+1}`
  (parity-invisible, Lemma R1), leaving `m − 1` effective pieces `Y = {p₁,…,p_{j−1}, d_j, p_{j+2},…,p_m}`.
  Lemma MK on `Y` (`m−1` pieces, `m−2` remaining cuts) gives `A ≤ min(Y) ≤ d_j ≤ t` (as `d_j ∈ Y`). Total
  cuts `1 + (m−2) = m−1 = b`. ✓

(Verified: MK-strategy `A ≤ min` and easy-case `A ≤ d_j`, 0 violations / 4000 random rational configs each.)

## Case A.A at threshold t (the p₁ > Σ/2 case, all m) — PROVED

Suppose `p₁ > Σ/2`. Xiang Yu runs the **subtract-all chain** (certified Case A.A mechanism,
`gap-caseAA-subtract-chain.md`): cut `p₁` successively at the interior offsets `p₂, p₂+p₃, …,
p₂+⋯+p_{m}` — legal because `p₁ > Σ/2` gives `p₂+⋯+p_m = Σ − p₁ < p₁`, so every partial sum is `< p₁`,
a genuine interior offset. This uses `m − 1 = b` cuts and produces the fragments `p₂, p₃, …, p_m` (each
now doubled: one fresh copy plus the original) together with the single leftover
`ℓ = p₁ − (p₂+⋯+p_m) = 2p₁ − Σ ≥ 0`. Every doubled value is parity-invisible, so
```
  A(final) = A({ℓ}) = ℓ = 2p₁ − Σ.
```
Now bound using **(I)** and **(III)**:
```
  A = 2p₁ − Σ  <  2·(2^{m−1}t) − (2^m − 1)t  =  2^m t − 2^m t + t  =  t.
```
Hence `μ(X, m−1) ≤ 2p₁ − Σ < t`. ✓ (Verified 0 violations, m = 3,4,5 gap configs.) This is the exact
**threshold-invariant** form of the certified Case A.A: it needs only `q₁ < 2^{m−1}t` and
`Σ ≥ (2^m−1)t`, not `Σ = (2^m−1)t`, so it applies verbatim to any subproblem satisfying (I),(III).

## The exhaustive split — reduction to the pure hard case

Given a residual gap-case `X`, exactly one of the following holds, and each but the last is now closed:
- **(a)** `p₁ > Σ/2`  →  Case A.A at threshold t: `A = 2p₁ − Σ < t`. **CLOSED, all m.**
- **(b)** `p₁ ≤ Σ/2` and (`δ ≤ t` or some `d_j ≤ t`)  →  Corollary MK.1: `A ≤ min ≤ t`. **CLOSED, all m.**
- **(c)** `p₁ ≤ Σ/2`, all `d_j > t` (`1 ≤ j ≤ m−1`), and `δ > t`  →  **the PURE HARD CASE.**

For `m ≤ 3` the hard case (c) is closed by Corollary R4.1 (`gap-case-m3-closure.md`); for `m = 4` by
(T, m=4) above (indeed the T4 Cases 1/2/3 are precisely instances of Corollary MK.1, and Case 4 is the
hard case (c)). **For `m ≥ 5`, case (c) is OPEN.** Thus the entire remaining upper bound is *exactly* the
pure hard case (c) at tight budget, for `m ≥ 5`.

## The hard case (c): the naive threshold-invariant induction is REFUTED (honest gap)

The outliner's proposed closure of (c): apply the universal first move `p₁@p₂` (Lemma R3 pairing),
producing the `(m−1)`-piece subproblem `Y' = {d₁, p₃, p₄, …, p_m}` at budget `m − 2`, with
`Σ' = Σ − 2p₂`; then claim `Y'` is a valid `T_{m−1}`-instance **at the same threshold t**, i.e. it
inherits `(I') max(Y') < 2^{m−2}t`, `(II') 2nd(Y') < 2^{m−3}t`, `(III') Σ' ≥ (2^{m−1}−1)t`, or else falls
into an easy MK case.

**(III') is correct and always inherited:** `Σ' = Σ − 2p₂ > (2^m−1)t − 2·2^{m−2}t = (2^{m−1}−1)t`, using
(II) `p₂ < 2^{m−2}t` and the exact identity `2^m − 2^{m−1} − 1 = 2^{m−1} − 1`. So the subproblem always
has "enough sum" — this was never the obstruction.

**(II') is NOT inherited — the induction fails here.** Direct enumeration (exact `Fraction`,
budget-respecting) of the hard case (c):

| m | source | hard configs | satisfy (I')&(II')&(III') | fall into easy MK | satisfy NEITHER |
|---|--------|--------------|---------------------------|-------------------|-----------------|
| 5 | MAX=20 | 898          | 88                        | 454               | **356**         |
| 6 | MAX=14 | 2120         | 236                       | 594               | **1290**        |

On the majority of hard configs the subproblem `Y'` satisfies **neither** the self-similar gap conditions
(condition (II'), the *halved* threshold `2^{m−3}t` on `Y'`'s second piece, fails) **nor** has any adjacent
difference `≤ t` (its differences are the original `d_3, …, d_{m−1} > t` plus the one new difference
`|d₁ − p₃|`, and its minimum `p_m > t`). So the `{(I'),(II'),(III')}` self-similar induction is the
**wrong invariant**; it cannot carry the recursion.

**Yet `μ(Y', m−2) ≤ t` genuinely holds.** For instance `X = {8,4,3,2,1}` (t = 18/31 ≈ 0.581) gives
`Y' = {4,3,2,1}`; this satisfies neither escape, but `μ({4,3,2,1}, 3) = 0` — via
`{4,3,2,1} → 4=(2,2), 3=(2,1) → {2,2,2,2,1,1}`, all equal pairs, `A = 0` — well below `t`. (Computed by
direct optimal search.) The subproblem closes through the **full richer strategy space** (equal-pair
saturation, Case A.A at a *later* level, etc.), not through inherited self-similar gap conditions.

**Honest open gap (m ≥ 5).** Closing case (c) needs one of:
1. a potential/invariant strictly weaker than the gap conditions `(I'),(II')` but strong enough to
   recurse under `p₁@p₂` (the `Σ'`-size (III') is available; the missing ingredient controls the
   *second* piece without the lossy factor-2 threshold drop); or
2. a *direct* hard-case strategy for general m (the m = 4 T4 proof's P/C construction, generalized —
   giving `A ≤ p_m/2` or `A ≤ δ + d_{m−1} − d₁`-type bounds `< t` from the gap conditions, with a
   generalized Sub-case-B impossibility). Sub-case B (`d_{m−1} > d₁`) is **non-vacuous for m ≥ 5**, so the
   m = 4 collision argument does not transfer.

Numerically (true optimal `μ`, bounded budget-enforced search) `μ(X, m−1) ≤ t` holds with **0 violations**
at `m = 5` (2722 gap configs, worst ratio 0.795), so (T) is **true**; only its analytic proof for `m ≥ 5`
is open. This round's contribution: Lemma MK (uniform easy-case tool, certifiable), Case A.A at threshold
t (all m), the clean reduction (a)/(b)/(c), and the **rigorous refutation** of the naive
condition-inheritance — narrowing the frontier to the pure hard case (c) with a precise account of why the
self-similar induction does not close it.

---

# R13: HS-A2 — the Sub-A-P branch of T5 (δ > 2t) is closed by pair2_3

This section proves **HS-A2**, the designated blocking sub-lemma of the m = 5 pure hard case (T5). It is
one sub-branch of T5; the remaining sub-branches (gap **G1**) and m ≥ 6 (gap **G3**) stay open — see the
honest scope statement at the end.

## Setup and notation (the m = 5 pure hard case)

Let `X = {p₁ > p₂ > p₃ > p₄ > p₅ > 0}` be five distinct pieces in the pure hard case at tight budget
`b = 4`: writing `Σ = p₁+p₂+p₃+p₄+p₅`, `t := Σ/(2⁵−1) = Σ/31`, so **Σ = 31t**, and
- (I) `p₁ < 2⁴t = 16t`, (II) `p₂ < 8t`, (hard-case reduction R11, section above);
- `p₁ ≤ Σ/2`, and **all differences exceed t**: with

  `d₁ := p₁−p₂,  d₂ := p₂−p₃,  d₃ := p₃−p₄,  d₄ := p₄−p₅,  δ := p₅`,

  we have `d₁,d₂,d₃,d₄ > t` and `δ > t`.

From the telescoping `p₅ = δ`, `p₄ = δ+d₄`, `p₃ = δ+d₄+d₃`, `p₂ = δ+d₄+d₃+d₂`, `p₁ = δ+d₄+d₃+d₂+d₁`,

  **Σ = 5δ + 4d₄ + 3d₃ + 2d₂ + d₁ = 31t,   hence   d₁ = 31t − 5δ − 4d₄ − 3d₃ − 2d₂.**   (Σ-id)

Throughout, all quantities are homogeneous of degree 1 in length, so we may (and do) keep `t` as an
explicit unit; every inequality below is scale-invariant.

## The strategy toolkit (re-derived from Lemma R1, not cited from T4)

We use only two elementary facts, both from the certified **Lemma R1** (`sum-bound-reductions.md`,
parity-invisible pairs) and **Lemma M0** (`alt-sum-integral.md`, `A = measure{x : N(x) odd}`):

- **(Invisible pairing cut.)** Cutting a piece `a` at an interior offset `w` with `0 < w < a` produces a
  fragment `w`; if the current multiset already contains a piece of value `w`, the two equal copies form a
  parity-invisible pair (they change `N(·)` by an even amount everywhere), so they may be deleted without
  changing `A`. The net effect of this one cut is to replace `{a, w}` by the single effective piece `a−w`.
- **(Finishing a 2-piece instance.)** Given two effective pieces `{u, v}` with `u ≥ v > 0` and one cut
  left: cutting `u` at offset `v` makes an invisible pair `{v,v}` and leaves `u−v`, so `A ≤ u−v`;
  alternatively halving `u` leaves the single piece `v`, so `A ≤ v`. Hence **`A ≤ min(u−v, v)`**. (If
  `u = v` the pair is already invisible and `A = 0`.)

For a **sorted 4-piece** effective instance `{q₁ > q₂ > q₃ > q₄}` at budget 3, two named strategies (each
= two invisible pairing cuts reaching two effective pieces, then one finishing cut) will be used:

- **Strategy S** (pair `{q₁,q₂}` and `{q₃,q₄}`): cut `q₁@q₂` and `q₃@q₄`, effective `{q₁−q₂, q₃−q₄}`;
  by the finishing bound `A_S ≤ min(q₁−q₂, q₃−q₄) ≤ q₃−q₄` (and `A_S ≤ |(q₁−q₂)−(q₃−q₄)|`).
- **Strategy R** (pair `{q₁,q₄}` and `{q₂,q₃}`): cut `q₁@q₄` and `q₂@q₃`, effective `{q₁−q₄, q₂−q₃}`.
  Since `q₁ ≥ q₂` and `q₄ ≤ q₃` give `q₁−q₄ ≥ q₂−q₃`, the finishing bound yields `A_R ≤ q₂−q₃`.

Each uses `2+1 = 3` interior cuts on distinct current pieces, hence is a legal budget-3 placement.

## The pair2_3 reduction (Lemma R1)

Cut `p₂` at interior offset `p₃` (legal: `0 < p₃ < p₂`). The fragment `p₃` pairs with the spectator piece
`p₃` into a parity-invisible pair (Lemma R1); the other fragment is `p₂ − p₃ = d₂`. By Lemma M0 the final
alternating sum over all physical pieces equals the alternating sum of the play on the **effective
4-piece instance**

  **Y″ := {p₁, d₂, p₄, p₅} = {p₁, d₂, δ+d₄, δ},  at remaining budget 3.**

Thus `T5 via pair2_3 ⟺ min A(Y″, 3) ≤ t`, which is what we now prove **in the Sub-A-P sub-branch**.

## The Sub-A-P hypothesis and the Σ-P bound [*]

We work in the sub-branch where the T4 P-strategy fires on the pair1_2 subproblem
`Y' = {d₁, p₃, p₄, p₅}` (this is the unique genuine pair1_2 failure mode with δ>2t; the Sub-A-C and Sub-B
modes are gap G1, handled elsewhere). The top gap of `Y'` is

  `D1_{Y'} := d₁ − p₃`  (this is ≥ 0, i.e. `d₁ > p₃`, precisely in this branch, so `Y'` is sorted
  `d₁ > p₃ > p₄ > p₅` — the ordering the whole analysis presumes is thus **forced**, not assumed).

Using (Σ-id) and `p₃ = δ+d₄+d₃`,

  `D1_{Y'} = d₁ − p₃ = (31t − 5δ − 4d₄ − 3d₃ − 2d₂) − (δ + d₄ + d₃) = 31t − 6δ − 5d₄ − 4d₃ − 2d₂.`

The **Sub-A-P firing condition** is `D1_{Y'} ≥ δ + d₄` (in T4-notation on `Y'`: `e₁ ≥ ε + e₃` with
`e₁ = D1_{Y'}`, `ε = p₅ = δ`, `e₃ = p₄−p₅ = d₄`). Substituting,

  `31t − 6δ − 5d₄ − 4d₃ − 2d₂ ≥ δ + d₄`  ⟺  **`2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃`.**   [*]

## Branch hypothesis and the ordering of Y″

We are in the branch **δ > 2t**. In `Y″ = {p₁, d₂, p₄=δ+d₄, δ}`:
- `p₁` is the maximum: `p₁ > p₄` and `p₁ > δ` (both from `X` sorted), and `p₁ > d₂` since
  `d₂ = p₂ − p₃ < p₂ < p₁`.
- `p₄ = δ + d₄ > δ` (as `d₄ > 0`).

So the only freedom in the sorted order of `Y″` is the position of `d₂` relative to `p₄` and `δ`. We split
on `d₂`; the split is on the single real parameter `d₂`, hence **exhaustive and pairwise disjoint** by
construction. (We use closed/half-open boundaries as written; each closing bound below holds weakly up to
its boundary.)

## The six cases

**Case A: `d₂ ≥ p₄`.** Sorted `Y″ = {p₁, d₂, p₄, δ}`; apply **R** (`q₂ = d₂`, `q₃ = p₄`):

  `A ≤ A_R ≤ q₂ − q₃ = d₂ − p₄ = d₂ − δ − d₄ =: E2 ≥ 0.`

By [*], `d₂ ≤ (31t − 7δ − 6d₄ − 4d₃)/2`, so

  `E2 ≤ (31t − 7δ − 6d₄ − 4d₃)/2 − (δ + d₄) = (31t − 9δ − 8d₄ − 4d₃)/2.`

Since `δ > 2t`, `d₄ > t`, `d₃ > t`, we have `9δ + 8d₄ + 4d₃ > 18t + 8t + 4t = 30t`, hence
`E2 < (31t − 30t)/2 = t/2 < t.` **R closes.** ∎(A)

**Case B (`δ ≤ d₂ < p₄`).** Sorted `Y″ = {p₁, p₄, d₂, δ}`.
- **B1 (`δ ≤ d₂ < p₄` and `d₂ < δ + t`):** apply **S** (`q₃ = d₂`, `q₄ = δ`):
  `A ≤ A_S ≤ q₃ − q₄ = d₂ − δ =: E3`, and `E3 = d₂ − δ < t.` **S closes.** ∎(B1)
- **B2 (`δ ≤ d₂ < p₄` and `d₂ ≥ δ + t`):** apply **R** (`q₂ = p₄`, `q₃ = d₂`):
  `A ≤ A_R ≤ q₂ − q₃ = p₄ − d₂ =: E2 ≥ 0` (as `d₂ < p₄`). From `d₂ ≥ δ + t` and [*],
  `2(δ + t) ≤ 2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃`, i.e. `9δ + 6d₄ + 4d₃ ≤ 29t`, whence (using `δ > 2t`, `d₃ > t`)
  `6d₄ ≤ 29t − 9δ − 4d₃ < 29t − 18t − 4t = 7t`, so `d₄ < 7t/6`. Then
  `E2 = (δ + d₄) − d₂ ≤ (δ + d₄) − (δ + t) = d₄ − t < 7t/6 − t = t/6 < t.` **R closes.** ∎(B2)

**Case C (`d₂ < δ`).** Sorted `Y″ = {p₁, p₄, δ, d₂}`.
- **C1 (`δ − t ≤ d₂ < δ`):** apply **S** (`q₃ = δ`, `q₄ = d₂`):
  `A ≤ A_S ≤ q₃ − q₄ = δ − d₂ =: E3`, and `E3 = δ − d₂ ≤ t` (as `d₂ ≥ δ − t`). **S closes.** ∎(C1)
  *(This is the R12 witness `X = {157/5, 13, 46/5, 34/5, 23/5}`: `Σ=65`, `t=65/31`, `δ=2.194t`,
  `d₂=1.812t`, so `δ−t = 1.194t ≤ d₂ < δ`, giving `E3 = δ−d₂ = 0.382t`.)*
- **C2 (`d₂ < δ − t` and `δ ≤ 3t`):** here `d₂ ∈ (t, 2t)` since `d₂ > t` (hard) and `d₂ < δ − t ≤ 2t`.
  Also `d₄ ∈ (t, 2t)`: `d₄ > t` (hard), and from `d₂ > t` and [*], `2t < 2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃`, so
  `6d₄ < 31t − 7δ − 4d₃ − 2t = 29t − 7δ − 4d₃ < 29t − 14t − 4t = 11t`, i.e. `d₄ < 11t/6 < 2t`. Hence
  `|d₄ − d₂| < t`. Xiang Yu plays the **custom 3-cut strategy**:
  (i) halve `p₁` into `{p₁/2, p₁/2}` (1 cut) — an invisible pair; effective `{p₄, δ, d₂}`, budget 2;
  (ii) cut `p₄ = δ + d₄` at interior offset `δ` (1 cut, legal as `0 < δ < p₄`) — the fragment `δ` pairs
  with the spectator `δ` (invisible), leaving effective `{d₄, d₂}`, budget 1;
  (iii) finish the 2-piece instance `{d₄, d₂}` (1 cut): `A ≤ |d₄ − d₂|`.
  Total 3 cuts, all interior; `A ≤ |d₄ − d₂| < t.` **Custom strategy closes.** ∎(C2)
- **C3 (`d₂ < δ − t` and `δ > 3t`):** **vacuous.** By [*] with `δ > 3t`, `d₄ > t`, `d₃ > t`,
  `2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃ < 31t − 21t − 6t − 4t = 0`, so `d₂ < 0`, contradicting `d₂ > t > 0`. Hence
  no configuration lies in Case C3. ∎(C3)

## Conclusion of HS-A2

Every configuration of the Sub-A-P sub-branch (m = 5 pure hard case, `δ > 2t`, `D1_{Y'} ≥ δ + d₄`) lands
in exactly one of Cases A, B1, B2, C1, C2 (C3 being empty), and in each Xiang Yu has a legal ≤ 3-cut
strategy on `Y″` with `A ≤ t`. Therefore `min A(Y″, 3) ≤ t`, and via the pair2_3 reduction

  **min A(X, 4) ≤ t   for every m = 5 pure hard configuration with δ > 2t and D1_{Y'} ≥ δ + d₄.**   ∎(HS-A2)

*Numerical validation (off-grid exact Fractions, Σ = 31, t = 1).* Over 12422 genuine Sub-A-P δ>2t
configurations, the per-case bounds above hold with **0 violations**: Case A (8 configs, R,
`E2 < t/2`), B1 (1429, S, `E3 < t`), B2 (4, R, `d₄ < 7t/6`, `E2 < t/6`), C1 (8123, S, `E3 ≤ t`),
C2 (2858, `d₂,d₄ ∈ (t,2t)`, `|d₄−d₂| < t`), C3 (0, empty). The R12 witness is Case C1 (`E3 = 0.382t`),
as claimed. A full continuous-optimum search independently confirms `min A(Y″,3) ≤ 0.34t` on the C2
configs, consistent with the `|d₄−d₂|` bound.

*Correction to the outline (recorded so it is not retried).* The outliner closed Case C2 by "the T4
P-strategy fires (`p₁ − p₄ ≥ δ`) and gives `A_P ≤ d₂/2 < t`". This is **false**: the P construction on
`Y″` yields effective pieces `{p₁ − p₄ − δ, d₂}`, and `A_P ≤ d₂/2` would require `p₁ − p₄ − δ ≤ d₂`, i.e.
`d₁ + d₃ ≤ δ`; but combining with [*] this forces `δ + 2d₄ + 2d₃ ≤ 0`, impossible. So `p₁ − p₄ − δ > d₂`
always in C2 and `A_P` is not `≤ d₂/2`. The correct closure is the custom halve-`p₁` strategy above with
bound `|d₄ − d₂| < t`.

## Honest scope — what HS-A2 does and does NOT prove

- **Proved:** the Sub-A-P sub-branch of T5 in the region δ > 2t (via pair2_3). This is one leaf of the
  first-cut tree for m = 5.
- **NOT proved (gap G1, OPEN):** the pair1_2 SUCCESS region — the full merge-family write-up for `Y'` in
  Sub-A-C (`A_C = δ+d₄−D1_{Y'} > t`) or Sub-B (`D1_{Y'} < e₃`), and the entire δ ≤ 2t region. These are
  ~40k of ~50k genuine pair1_2 failure configurations; only numerics (0 violations) support them, with no
  analytic proof. **Consequently T5 is NOT complete and the n = 4 upper bound is NOT rigorous.**
- **NOT proved (gap G3, OPEN):** m ≥ 6 (HS-A3). The Step tree is **not uniform in m** — it closes only
  m = 5's Sub-A-P branch. For m ≥ 6, Σ = 63t (resp. `(2^m−1)t`), b = 5, the δ-threshold `2t` and the
  Case-C3 impossibility are unverified. Untouched this round.

No forbidden route is used: SB-monotone, R3-cascade, complement-cut m4→3, and the p₁@p₂
threshold-invariant induction are all avoided; all numerics are off-grid exact Fractions.
