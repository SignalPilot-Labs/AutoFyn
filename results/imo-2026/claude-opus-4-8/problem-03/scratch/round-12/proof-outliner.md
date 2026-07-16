## imo-2026-03

Field: advance all 3 leaders, each toward its single residual, with the outline of the open
gap RE-PLANNED per this round's explorer findings. No new slug and no forced copy — the
explorers surfaced better *sub-routes inside* the three live approaches, not a fourth rival
route to the whole claim. One contingency copy flagged at the end (reviewer's discretion).

The whole-problem claim (target of every slug): **c(n) = 2^n/(2^{n+1}−1)** for all n, both
bounds. Each slug is a complete attempt; the residual below is the only open gap in that attempt.

---

geometric-selfsimilar: advance (open UB gap re-planned)
Target: c(n)=2^n/(2^{n+1}−1) for all n (this approach owns the UPPER bound; LB imported/shared).
Technique: direct actual-A multi-strategy case split at threshold t (the certified-T4 template,
extended), keyed by which first cut is available. NOT SB-monotone / R3-cascade / complement-cut /
threshold-invariant induction (all four rigorously refuted — R7/R8/R9/R11).
Immediate deliverable: **T5 (m=5 hard case)** ⟹ n=4 UB flips to rigorous (exactly as certified
T4 flipped n=3). General-m T_m flagged as the harder residual beyond T5.
Skeleton (pure hard case (c): distinct p₁>…>p_m, Σ=(2^m−1)t, budget b=m−1, p₁≤Σ/2, all dⱼ>t, δ>t):
  1. Double-invisible-pair pre-check — if ∃ triple (i,j,k) with p_i−p_j=p_k, ONE cut p_i@p_j makes
     fragment p_i−p_j=p_k, so {p_k,p_k} is a parity-invisible pair ⟹ effective (m−2)-piece instance,
     budget m−2 ⟹ certified Lemma AB (μ=0) or MK closes. (Explorer: covers 67.4% of m=5 hard configs.)
  2. Generic (no double-pair) — cut p₁@p₂ (pair1_2): invisible pair {p₂,p₂}, leaves 4-piece
     Y'={d₁,p₃,p₄,p₅} with Σ'=Σ−2p₂>(2^{m−1}−1)t (certified from cond (2)). Apply certified T4's
     R/S/P/C strategies AT THE ORIGINAL threshold t (not Σ'/15) — the load-bearing non-obvious move.
     Easy sub-cases R, S_e3, S_sym close via MK. (Explorer: 96.8% of no-double-pair configs.)
  3. T4-at-t residual failure modes (only two, per explorer): (i) Sub-A P with δ>2t (A_P=δ/2>t);
     (ii) Sub-B C with d₁≈p₃ (A_C=δ+d₄−|d₁−p₃|>t). Fallbacks: pair2_3 (cut p₂@p₃, P gives A=d₂/2)
     for (i); cut_1@3 (fragment d₁+d₂, S_sym via |d₁−p₃|<t) for (ii). (Explorer: 0 failures / 1551
     m=5 hard configs after these; also 0 / 70722 fractional.)
  4. Exhaustive first-cut case split (Opening D): Step1 double-pair, Step2 pair1_2→easy-T4,
     Step3 pair1_2→Sub-A (P if δ≤2t, C if d₁−p₃≥δ+d₄−t), Step4 pair1_2→Sub-B via cut_1@3→S_sym,
     Step5 both-fail → pair2_3 with A=d₂/2≤t. Covers all cases ⟹ μ(X,m−1)≤t ⟹ T5.
Key lemmas (claim + mechanism):
  - Double-pair reduction — because p_i−p_j=p_k makes one physical cut cancel THREE pieces (p_i,p_j
    absorbed into {p_j,p_j}-type pairs and p_k paired), dropping to m−2 with a spare cut ⟹ AB.
  - T4-at-t transfer — because R/S/P/C bound actual A by a gap/δ term (A_R≤d₂, A_S≤d₃, A_S≤|d₁−d₃|,
    A_P≤δ/2, A_C≤δ+d₄−|d₁−p₃|) that is compared to the ORIGINAL t; certified for m=4, re-used verbatim.
  - Sub-A δ≤2t escape — because cond (2) gives p₂<2^{m−2}t hence (via Σ arithmetic) δ<2t in the
    T4-branch, so A_P=δ/2<t. (True for m=4; the m=5 analogue is the HARD STEP below.)
Open gaps (the builder fills these — flagged HARD):
  - **HS-A2 [the crux analytic sub-lemma]:** when pair1_2's Sub-A P fires with δ>2t (a REAL
    continuous config, off the integer grid — e.g. d₁=8.6t, d₂=d₃=d₄=1.1t, δ=2.5t), prove pair2_3
    gives A≤t, i.e. δ>2t forces the pair2_3 min-piece ≤2t. Explorer's bound from (*)
    d₂+2d₃+3d₄+3δ≤31t/2 gives only d₂<3.5t, NOT <2t — so this needs either a sharper Σ-bound OR a
    non-P pair2_3 sub-case covering d₂∈(2t,3.5t). UNPROVEN. This is the single blocking lemma for T5.
  - **HS-A3 [general m ≥ 6]:** the explorer maps m=5 only. For m≥6 Sub-B is non-vacuous with MORE
    sub-cases and double-pair coverage is untested. State explicitly whether the Step1–5 case tree is
    UNIFORM in m or only closes m=5. A full T5 alone (leaving T_m, m≥6 open) is still real progress
    (flips n=4 UB), so the builder should target T5 first and mark general-m honestly open.
Cases to cover: Step1 (double-pair) / Step2 (easy-T4) / Step3 (Sub-A: δ≤2t P, δ>2t→pair2_3) /
  Step4 (Sub-B → cut_1@3) / Step5 (both-fail → pair2_3). All at threshold t, budget m−1.
Watch out: continuous vs grid — the Sub-A P δ>2t failure is exactly a config the denom-4/5 grids
  MISS, so "0 grid violations" does NOT close it; HS-A2 must be an analytic inequality. Do NOT invoke
  any of the four forbidden UB routes. "min over strategy-family ≤ t" is the correct existence-of-
  witness UB direction (XY only needs ONE good cut set).

---

ll-inclusion-gap: advance (open LB gap re-planned — Opening C direct, NOT mutual induction)
Target: c(n) for all n (this approach owns the LB via the inclusion split S_Q⊆S_R).
Technique: single Gen-Decomp step + DIRECT analytic evaluation of A(R_lo) with tight-case forcing —
deliberately AVOIDS the {Claim_R,T_R} mutual induction (refuted R10) and the F_a family descent
(scope-limited to a<1, certified). Closes the last INC branch: **G-INC-2nt a≥1**.
Skeleton (R = top-cut refinement of G_{n−1} with cut value a∈[1,2^{n−2}); a<1 already certified F_a):
  1. Gen-Decomp at the top level (always valid: h_R=2 for any a∈(0,2^{n−2})): certified identity
     A(R)−A(Q)=deficit_top+(A(R_lo)−A(Q_lo)), with clean descent S_{Q_lo}⊆S_{R_lo} and R_lo={a}∪G_{n−3}.
  2. Analytic floor (Opening C): A({a}∪G_j) ≥ A(G_{j−1}) for all a∈(0,2^{j+1}), equality iff a=2^j
     — so A(R_lo)=A({a}∪G_{n−3})≥A(G_{n−4})≥1.
  3. Tight-case forcing: A(R_lo)=1 only at a=2^{n−3} and only n∈{4,5}; there S_{R_lo}=[1,2) (single
     band), and ΣQ_lo=2^{n−2}+a=3·2^{n−3}≫2 with S_{Q_lo}⊆[1,2) forces Q_lo into equal pairs ⟹
     A(Q_lo)=0. So A(R_lo)−A(Q_lo)≥1.
  4. Non-tight (a≠2^{n−3}, or n≥6 where A(R_lo)≥3): the slack A(R_lo)−1>0 absorbs A(Q_lo) via
     S_{Q_lo}⊆S_{R_lo}+budget (an L1-type bound A(Q_lo)≤A(R_lo)−1).
  5. Combine: A(R)−A(Q)=deficit_top+(A(R_lo)−A(Q_lo))≥0+1=1 ⟹ INC closed, all n. With a<1 (F_a)
     and the anchor (t-ell-mutual-induction) this finishes G-INC.
Key lemmas (claim + mechanism):
  - A({a}∪G_j)≥A(G_{j−1}), min at a=2^j — because A({2^j}∪G_j)=A(G_{j−1}) (the pair {2^j,2^j}
    cancels the top term), and A viewed as a function of a (measure form A=measure{N odd}) is
    piecewise-linear with its unique minimum at that cancellation point.
  - Tight forcing A(Q_lo)=0 — because parts summing to 3·2^{n−3} with odd-count region confined to
    [1,2) admit only equal-pair structures (any unpaired part shifts the odd-region out of [1,2)).
Open gaps (HARD-flagged):
  - **HS-B1 [piecewise-linear min claim]:** prove A({a}∪G_j)≥A(G_{j−1}) with equality iff a=2^j, for
    ALL j (explorer confirmed j=1..6 numerically only). Needs the exact piecewise-linear profile of
    A({a}∪G_j) in a via the measure form and the dyadic staircase of G_j.
  - **HS-B2 [tight-case forcing A(Q_lo)=0]:** the load-bearing step. From ΣQ_lo=3·2^{n−3},
    |Q_lo|≤budget, and S_{Q_lo}⊆[1,2), rigorously force Q_lo = equal pairs (A=0). Explorer verified the
    unique witness (n=5: Q_lo={6,6}) but a general argument is unwritten — mind the parity subtlety
    (S_{Q_lo}⊆[1,2) constrains the ODD-count region, not the parts' magnitudes directly).
  - **HS-B3 [non-tight slack absorption]:** A(Q_lo)≤A(R_lo)−1 for the REFINED R_lo={a}∪G_{n−3}. Confirm
    the certified L1 (proved for S_P⊆S_{G_{m−1}}) transfers to containment in the refined S_{R_lo}; if
    not, supply the −1 budget deficit directly. (n≥6 has A(R_lo)≥3, ample slack — the pinch is n∈{4,5}.)
Cases to cover: a=2^{n−3} tight (n∈{4,5}) / a≠2^{n−3} non-tight / n≥6 (auto-slack). Descent for
  a∈[1,2^{n−4}) via repeated Gen-Decomp bottoming at k∈{2,3} base cases (explorer Opening B: 0
  violations, n=4 496 configs, n=5 662 configs) is the fallback if the direct top-level floor stalls.
Watch out: do NOT re-open the {Claim_R,T_R} mutual induction (NOT descent-closed, O1 fires, R10) nor
  the false "INC forces max(Q)≤max(R)" (R11). Opening C is designed to bypass both by using the
  ANALYTIC A(R_lo)≥1 floor + a static forcing argument, no induction on R's structure.

---

ll-dyadic-symdiff: advance (open LB gap RE-PLANNED — the "reduction" was circular)
Target: c(n) for all n (rival LB via measure(S_Q△S_R), independent of the INC route).
CRITICAL RE-FRAME (explorer): the level-charge "reduction" B₊≤A₋+B₋ is ALGEBRAICALLY EQUIVALENT to
the goal A(Q∪R)≥1 (for max|g|≤2), NOT a genuine reduction — so the R11 outline target must be
dropped. Re-plan the gap around a route that actually descends: the **Sub-3a dichotomy**.
Technique: parity case split on whether the certified Sub-3a fires; when it fails, prove A>1
STRICTLY via the g(0+)≤−1 foundation + budget-parity + a level-by-level odd-g accumulation.
Skeleton (bucket (iii): max(Q),max(R)<2^{n−1}, ΣQ=2^n, joint budget; g:=N_Q−N_R, ∫g=1, A=measure{g odd}):
  1. Structural foundation (PROVED by explorer): g(0+)=|Q|−|R|=c_Q−c_R−(n−1)≤−1 always in bucket(iii).
     So g starts strictly negative and, since ∫g=1>0, must cross to positive — the crossing is the
     source of odd-g mass.
  2. Budget-parity (PROVED by explorer, Opening C): R cannot have all-even multiplicities with c_R<n
     cuts (the odd-mult count P starts at n and each cut changes it by an odd amount, so ≥n cuts needed
     to zero it, but c_R≤n−1). Hence R has ≥1 odd-multiplicity piece ⟹ N_R has ≥1 unit parity
     transition ⟹ an odd-g interval exists (A>0 — a prerequisite, not yet the +1).
  3. Dichotomy on Sub-3a: Sub-3a fires (some dyadic level fully odd) ⟹ A≥1 (CERTIFIED). Else prove
     A>1 (Opening A/B).
  4. Sub-3a-fails ⟹ A>1: split on g(0+) parity.
     - g(0+) odd (≤−1): I₀=(0,1) starts odd-N; if no interior odd-mult piece in (0,1), Sub-3a fires
       on I₀ (contradiction) — so the odd-mult piece there itself contributes ≥1 measure of odd-g.
     - g(0+) even (≤−2, the "doubly-negative" hard sub-case, e.g. n=4,c_R=1,|Q|=3): g must descend
       through odd values to reach positive; each ±1 crossing (forced by step 2's odd-mult piece)
       deposits A₋/A₊ mass; accumulate over the n dyadic levels to reach total ≥1.
Key lemmas (claim + mechanism):
  - g(0+)≤−1 — because |Q|−|R|=c_Q−c_R−(n−1) and c_Q+c_R≤n, c_R≥1 (budget). PROVED, 1548/1548.
  - R has an odd-mult piece — because the parity of #odd-mult-values changes by an odd amount per cut,
    starting at n; killing all n needs n cuts, exceeding the c_R≤n−1 budget. PROVED.
  - Sub-3a fires ⟹ A≥1 — certified `dyadic-level-parity.md`.
Open gaps (HARD-flagged):
  - **HS-D1 [Sub-3a-fails ⟹ A>1, the new crux]:** the load-bearing claim. Explorer numerics:
    min A after Sub-3a exclusion = 9/8 (n=3), 2 (n=4), 3 (n=5) — all >1, growing ~⌈n/2⌉. NO proof
    mechanism yet: "each failing level has an internal parity switch creating paired odd-g
    sub-intervals" is a sketch. The builder must turn the per-level parity switch into ≥ a fixed
    positive measure and sum over levels to exceed 1.
  - **HS-D2 [g(0+) even, doubly-negative]:** when g(0+)=−2 Sub-3a cannot fire on I₀; must show the
    forced ±1 crossings (from HS budget-parity) deposit ≥1 total odd-g measure — getting exactly ≥1,
    not merely >0, is the gap.
  - **HS-D3 [max|g|≥3 agnosticism]:** the Sub-3a-fails/parity route must be verified NOT to secretly
    assume max|g|≤2 (unlike the discarded level-charge algebra). For general n, max|g|≤n+1; the
    argument should act on the parity structure directly, so confirm it is max|g|-agnostic.
Cases to cover: Sub-3a fires (certified) / Sub-3a fails ∧ g(0+) odd / Sub-3a fails ∧ g(0+) even.
Watch out: do NOT present B₊≤A₋+B₋ as a reduction (it IS the goal, explorer-confirmed circular). Do
  NOT use "INC forces max(Q)≤max(R)" (false, R11) — this route is INC-free (D1-direct is ordering-free).
  REFL-telescope "alone only recomputes A" (dead-end) — usable ONLY as an induction on max(P) with
  non-circular base cases, which is the contingency copy below.

---

Contingency copy (reviewer's discretion, NOT a forced 4th build):
copy-of ll-dyadic-symdiff: only if the reviewer judges HS-D1 too speculative to be the sole dyadic
  line. The twin would fill the SAME bucket-(iii) gap by the DISTINCT mechanism of Opening 3:
  induction on max(P) via the double-REFL cancellation A(Q∪R)=max(Q)−max(R)+A(Q'∪R'') (ΣQ'−ΣR''=1,
  max strictly decreases), base cases closed by K1/K2/D1/Sub-3a on the reduced object. This is a
  genuinely different fill (structural recursion vs parity accumulation) and both are worth running if
  a slot is free; otherwise advance the three leaders and revisit next round.

Build set recommendation to the outline-reviewer: geometric-selfsimilar, ll-inclusion-gap,
ll-dyadic-symdiff (all advance with the re-planned gaps above). Optionally add copy-of
ll-dyadic-symdiff if a fourth slot is available.
