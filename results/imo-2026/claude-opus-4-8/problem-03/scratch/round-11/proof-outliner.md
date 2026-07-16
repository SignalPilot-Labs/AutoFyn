## imo-2026-03

Field this round: advance the three leaders, each with the concrete new opening its explorer
found. UB (geometric-selfsimilar) and the two rival LB routes (ll-inclusion-gap,
ll-dyadic-symdiff) together cover the whole remaining frontier. No reframe needed: the shared
LB residual is NOT stuck on one unchanged step — both explorers found genuinely NEW
NON-inductive traction this round (D1-based INC base, parametric-family descent), so the
direction is sound and freshly moving.

**Anti-stuck rules for every builder (hard):** any python must run < 20 s, print incrementally
(never a long silent computation), cap search denominators (denom ≤ 6, |X| ≤ m), and abort +
report if a check exceeds budget. Do NOT re-open the refuted abstract {Claim_R, T_R} mutual
induction, the SB-monotone chaining, the R3-cascade actual-A for m≥4, or the complement-cut
m=4→3→R4 (all certified dead). Verify, don't trust: re-derive every "0 violations" claim.

---

geometric-selfsimilar: advance
Target: the WHOLE upper bound val(P) ≤ c(n) = 2^n/(2^{n+1}−1) for every Liu-Bang config, all n
  (LB imported from the LL routes). Concretely: the residual gap-case inequality (T) for all m.
Technique: reduction to (T) (certified R1/R2/R3 + AB.1 + Case A.A) + Lemma MK as the uniform
  easy-case tool + a THRESHOLD-INVARIANT induction T_m-at-t → T_{m−1}-at-t for the hard case.
Skeleton:
  1. Import: whole UB ⟸ (T) [μ(X,m−1) ≤ t := Σ/(2^m−1) for the m-piece distinct gap case,
     p₁<τ=2^{m−1}t, p₂<τ/2=2^{m−2}t]. Certified for m≤4 (T4-tight-m4 + R4 + Case A.A + AB.1).
  2. Lemma MK: μ(k pieces, k−1 cuts) ≤ min(pieces). Establish as a standalone certifiable tool.
  3. Easy cases (some d_j := p_j−p_{j+1} ≤ t, or δ := p_m ≤ t): do (m−j) pairings to expose d_j
     (resp. δ) as the minimum piece → j effective pieces with j−1 cuts → Lemma MK ⇒ A ≤ min
     ≤ d_j ≤ t. Uniform over all m. (m=5 Cases 0/1/2/3 verified 0-viol.)
  4. Hard case (all d_j > t AND δ > t): universal first move — R3-cut p₁@p₂ →
     (m−1)-piece subproblem {d₁, p₃, …, p_m} with budget m−2. Claim it satisfies T_{m−1}-at-t
     (SAME threshold t), then recurse to step 2 on the subproblem.
Key lemmas (claim + mechanism):
  - Lemma MK (μ(k,k−1) ≤ min) — because halving the top piece p₁ makes an equal pair {p₁/2,p₁/2}
    that is A-invisible (cancels), dropping to k−1 pieces with k−2 cuts; min is preserved down the
    induction; bases k=1 (μ=p₁=min), k=2 (μ=min(v,u−v)≤v=min). This is the general-m easy-case key
    that T4's ad-hoc argument never needed.
  - **CORRECTION to the flagged UB obstruction (arithmetic slip in both explorer + dispatch):**
    the Σ'-bound DOES hold for every m. Σ'=Σ−2p₂>(2^{m−1}−1)t ⟺ p₂<2^{m−2}t, and condition (2)
    is exactly p₂<τ/2=2^{m−2}t (NOT 2^{m−1}t). Verified match for m=3..8. So after p₁@p₂ the
    subproblem sum Σ'>(2^{m−1}−1)t strictly, always. The induction is NOT blocked here.
  - Threshold-invariant descent T_m-at-t → T_{m−1}-at-t — because Lemma MK gives the easy cases at
    the ORIGINAL t (threshold-free: A≤d_j≤t), and the hard case's p₁@p₂ leaves a genuine
    (m−1)-piece gap-case whose OWN threshold Σ'/(2^{m−1}−1) exceeds t (so the self-similar
    certified T_{m−1} is too weak) — we must prove the stronger at-t version internally.
Open gaps:
  - THE hard step (relocated, now precise): does the subproblem {d₁,p₃,…,p_m} inherit gap
    conditions (1') q₁≤Σ'/2 and (2') q₂<2^{m−3}t at threshold t? The Σ' size is fine; condition
    INHERITANCE is the open content. Where a subproblem condition fails, it must instead fall into
    an easy case (some subproblem-difference ≤ t) closed by Lemma MK — this dichotomy is the thing
    to prove.
  - Certify Lemma MK.
Cases to cover: Case 0 (δ≤t); Cases 1..m (d_j≤t easy, via (m−j) pairings); the true hard case
  (all d_j>t, δ>t) split into Sub-A (d_m ≤ d₁) and Sub-B (d_m > d₁) — BOTH via p₁@p₂; Sub-B is
  NOT vacuous for m≥5 (do not mimic the m=4 vacuousness argument).
Watch out for: (i) do NOT apply certified T_{m−1} at Σ'/(2^{m−1}−1) (>t, too weak — refuted);
  (ii) Sub-B genuinely non-vacuous m≥5; (iii) after p₁@p₂ the effective pieces may need a P/C
  bound (Opening 3: find explicit (u,v) with A=min(v,u−v)≤t in terms of δ,d_j) as the
  base-of-recursion when the subproblem is itself the hard 2-effective-piece case — keep this as a
  fallback if condition-inheritance stalls; (iv) budget b=m−1 tight (AB kills b≥m).

---

ll-inclusion-gap: revise
Target: the WHOLE lower bound c(n) ≥ 2^n/(2^{n+1}−1), i.e. Lemma LL (t≥2, A(Q)>0): A(Q∪R)≥1 for
  every refinement R and every Q; open residual = G-INC-2 (refined-R, INC branch S_Q⊆S_R).
  (Revise: the abstract {Claim_R,T_R} descent is refuted (O1); keep the INC route but re-plan the
  refined-R gap by a DIRECT per-cut / per-FAMILY descent that IS closure-stable.)
Technique: Gen-Decomp (certified) top-band descent, applied per cut-location and per parametric
  family — never to the abstract structure-free class.
Skeleton:
  1. Import: anchor R=G_{n−1} INC done all n (t-ell-mutual-induction). Refined-R INC = G-INC-2.
     Split by cut location of R: (I) lower-band cut of piece 2^{k₀}, k₀≤n−3; (II) top-cut of
     2^{n−1} into {a, 2^{n−1}−a}.
  2. (I) G-INC-2lb — CLEAN self-similar descent: Gen-Decomp at threshold 2^{n−2} keeps
     R_hi={2^{n−1},2^{n−2}} UNCUT ⇒ h_R=2 (even) at every level; R_lo = G_{n−3} carrying the SAME
     lower-band cut = G-INC-2lb one level down. Induct n→n−2. Base n=4 (verified 0-viol, 123
     configs, min margin 1).
  3. (II-e) equal split a=2^{n−3} (G-INC-2e): closed n≤6 (vacuousness 2^{m−2}(9−m)≥2^m ⟺ m≤5);
     push to general n.
  4. (II-nt, a<1) — PER-FAMILY mutual induction on R_k := {a}∪G_{k−1} (a fixed <1). Claim_a(k):
     A(R_k)−A(Q)≥1 for S_Q⊆S_{R_k}, |Q|≤k, ΣQ=2^k; T_a(k): the ε-relaxed companion. Step k→k−2
     mirroring the certified t-ell arithmetic (deficit_top=a_val'+b, ε'=ε+a_val'−b, h∈{0,2}).
  5. (II-nt, a≥1) — piecewise-linear A(R) in a; case split via Opening C (S_R-measure bound:
     A(Q)≤measure(S_R)=A(R), budget forces the one-short gap) OR early-termination when h_{R_lo}
     first goes odd.
Key lemmas (claim + mechanism):
  - G-INC-2lb clean descent — because a lower-band cut leaves the top two pieces uncut, so
    h_R=2 (even) at EVERY descent level; O1 (the parity break that killed the abstract class) can
    never fire, and R_lo is literally G-INC-2lb at n−2. Self-similar, no companion T needed.
  - Parametric-family closure for a<1 — because for fixed a<1, R_lo={a}∪G_{k−3} is the SAME family
    two levels down and h_{R_lo}=#{2^{k−3},2^{k−4}}=2 (even, since a<1≤2^{k−4} for k≥6; k=4,5
    direct), so THIS family is descent-closed even though the abstract class is not. Sidesteps O3.
  - h=0 cheap kill — because with no Q-part ≥ threshold 2^{n−2}, deficit_top =
    measure(S_R∩I_{n−1}) = 2^{n−2}−a ≥ 2^{n−2}−1 ≥ 1 for a<1. Immediate.
  - h≥4 impossible — four Q-parts ≥2^{n−2} sum to ≥2^n=ΣQ ⇒ Q_lo=∅, M=A(R_lo)≥1.
Open gaps: G-INC-2e general n (>6); the a≥1 sub-branch (h_{R_lo} can go odd — the genuine hard
  residual here); a<1 bases k=4,5; G-GAP (non-containment refined R, alignment cost).
Cases to cover: {lower-band cut}, {top-cut a<1}, {top-cut a=2^{n−3}}, {top-cut 1≤a<2^{n−2}}.
Watch out for: do NOT reopen the abstract {Claim_R,T_R} (refuted, O1 witness {1,2,2,2,8,16,32});
  Claim_R is FALSE for non-refinement R (R={1,3,3}), so the family MUST stay parametric; L1 needs
  anchor structure (fails 2880-viol on arbitrary R). The a≥1 branch is where closure can still
  break — treat it as the honest open gap, not as covered.

---

ll-dyadic-symdiff: advance
Target: the WHOLE lower bound via Lemma LL; open residual = refined-R bucket(iii)
  (max(Q),max(R)<2^{n−1}), attacked WITHOUT mutual induction — INC (containment) base + GAP
  (non-containment) residual.
Technique: double-REFL cancellation + certified D1 (small-discrepancy kill) + Sub-3a
  (dyadic-level parity), plus Opening-D charge/budget accumulation for GAP.
Skeleton (INC containment base, general n, NON-inductive):
  1. INC forces max(Q)≤max(R): if max(Q)>max(R), a point x between them has N_Q(x)=1 (odd),
     N_R(x)=0 (even) ⇒ INC (N_Q odd ⟹ N_R odd) fails. Set r=max(R), q=max(Q), Q'=Q\{q}, R'=R\{r}.
  2. Double-REFL: A(Q∪R) = (r−q) + A(Q'∪R'). [REFL-gen removing r (top of Q∪R since r≥q), then
     removing q.]
  3. If r−q ≥ 1: A(Q∪R) ≥ r−q ≥ 1. Trivial.
  4. If r−q ∈ [0,1) and max|g_{Q',R'}| ≤ 1: D1 ⇒ A(Q'∪R') ≥ |ΣQ'−ΣR'| = 1+(r−q); total
     A(Q∪R) ≥ 1+2(r−q) ≥ 1. ✓
  5. If r−q ∈ [0,1) and max|g_{Q',R'}| ≥ 2 (n=4: 7 configs, all r=q=μ): Sub-3a on Q'∪R' — μ is the
     only piece >2^{n−2}, so N=1 (odd) throughout [2^{n−2},μ), measure μ−2^{n−2}≥1 ⇒ Sub-3a fires.
Skeleton (GAP non-containment residual, after K1/K2/Sub-3a/D1):
  6. Charge accumulation (Opening D-2/D-3): ∫g=1 splits as (A₊−A₋)+2(B₊−B₋)=1 (A± = measure{g=±1},
     B± = measure{g=±2}); A = A₊+A₋. Show A₊+A₋ ≥ 1 via the budget-breakpoint count: ≤2n+1
     breakpoints across n dyadic levels, Sub-3a-failure ⇒ ≥1 breakpoint per level, max|g|=2 ⇒ one
     bounded bad region ⇒ compensating odd-g measure ≥ 1.
Key lemmas (claim + mechanism):
  - max(Q)≤max(R) under INC — because a point between them makes N_Q odd while N_R even, breaking
    the INC implication. Clean, no induction.
  - Double-REFL cancellation A(Q∪R)=(r−q)+A(Q'∪R') — two applications of certified REFL-gen (reflect
    off top of R, then off top of Q). NOTE the second step needs q≥max(R'); verify this holds
    (it may fail if R's second piece exceeds q — the builder must check and branch).
  - INC base closes with NO mutual induction — because the three sub-cases (r−q≥1 trivial;
    max|g|≤1 by certified D1 giving ≥1+(r−q); max|g|≥2 dominant-piece by Sub-3a) are exhaustive.
    This is the corrected reduction: the earlier "ΣQ'−ΣR''≥1 alone ⟹ A≥1" was WRONG; the true
    relation is A=(r−q)+A(Q'∪R') and D1 supplies the +1+(r−q) slack.
Open gaps:
  - General-n Sub-3a-firing: prove that in the INC base, max|g_{Q',R'}|≥2 ⟹ max(Q)=max(R)=μ ∈
    (2^{n−2}+1, 2^{n−1}) (so I_{n−1} has exactly one piece μ, Sub-3a fires, measure μ−2^{n−2}≥1).
    Verified n=4 (7 configs); conjecture for n≥5.
  - GAP residual A≥1 (Opening-D charge/budget): formal proof open (empirically A≥2, big margin).
Cases to cover: INC base {r−q≥1 | r−q∈[0,1) with max|g|≤1 | r−q∈[0,1) with max|g|≥2};
  GAP residual {max|g|=2 with Sub-3a failing}.
Watch out for: do NOT claim "∫g=1 alone ⟹ A≥1" (FALSE: g≡2 on [0,1/2) gives ∫g=1, A=0); K2 for
  INC is CIRCULAR (fires iff A(R)−A(Q)≥1, which is the claim); do NOT reimport "max(Q)<2^{n−1} ⟹
  A≥2" (FALSE, tight witness Q={3,3,2},R={2,2,2,1} gives A=1). Verify the q≥max(R') precondition
  of double-REFL before using step 2.

---

Field handed to the outline-reviewer (rank + emit build set):
  - geometric-selfsimilar (advance) — UB m≥5 via Lemma MK + threshold-invariant descent; Σ'-bound
    slip corrected (holds all m), hard step = subproblem condition-inheritance.
  - ll-inclusion-gap (revise) — refined-R INC via clean lower-band descent + parametric-family
    (a<1) induction + h=0 kill; genuine open = a≥1 closure + G-INC-2e general n.
  - ll-dyadic-symdiff (advance) — INC containment base closed non-inductively (double-REFL + D1 +
    Sub-3a); open = general-n Sub-3a firing + GAP residual charge bound.
