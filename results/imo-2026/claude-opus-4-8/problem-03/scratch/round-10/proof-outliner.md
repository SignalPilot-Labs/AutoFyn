# Proof-outliner field — imo-2026-03 (Round 10)

Three fronts, three advances. All build on certified lemmas; none re-opens a recorded dead end.
The run is very close: UB = one finite inequality (T) at each m; LB = the refined-R alternating-tail
crux {Claim_R,T_R} + the non-containment G-GAP. This round attacks all three concurrently
(one builder per slug, no file collision). Two dormant slugs (alternating-sum-value,
extremal-smoothing) stay unbuilt.

---

## imo-2026-03

### geometric-selfsimilar: advance   [PLAN REVIEW REQUIRED]
Target: Full problem — c(n)=2^n/(2^{n+1}−1); this slug owns the UPPER bound (XY holds every LB config to
val ≤ c(n)), together with the already-certified LB base/tightness, i.e. the whole claim.
Technique: The certified sum-bound reframe μ(X,b) ≤ Σ/(2^{b+1}−1). Lemma AB (R9) collapses the whole
remaining UB to the finite inequality **(T)** at the tight budget b=m−1 (m=|X|, so m ↔ n+1). Spine:
a **direct 4-strategy case split** (R/S/P/C) proving (T), NOT an SB/potential induction.

Skeleton:
  1. Reduce whole UB to (T) at b=m−1 — by certified Lemma AB (μ(X,b)=0 for b≥|X|) + Cor AB.1. (done R9)
  2. **(T) for m=4 (⟺ n=3 UB):** with d₁=p₁−p₂, d₂=p₂−p₃, d₃=p₃−p₄, δ=p₄, t=Σ/15, prove
     min over merge-family {R,S,P,C} of A ≤ t. Case split:
       - Case 1 (d₂≤t): Strategy R (pair (p₁,p₄),(p₂,p₃)) gives A_R ≤ d₂ ≤ t.
       - Case 2 (d₃≤t): Strategy S (pair (p₁,p₂),(p₃,p₄)) gives A_S ≤ d₃ ≤ t.
       - Case 3 (|d₁−d₃|≤t): Strategy S gives A_S ≤ |d₁−d₃| ≤ t.
       - Case 4 (d₂>t, d₃>t, |d₁−d₃|>t): Sub-case B (d₃>d₁) is IMPOSSIBLE; Sub-case A (d₁>d₃) uses P or C.
     — by the gap-condition arithmetic + 2-term averaging (see Key lemmas).
  3. **(T) for m≥5 (general-n UB):** generalize the direct case-split — matching strategies (generalized
     R/S) cover the cases where some consecutive difference ≤ Σ/(2^m−1); a P/C chain covers the rest via
     A ≤ p_m/2 with p_m < 2Σ/(2^m−1). — **HARD/OPEN** (see below).
  4. Combine: (T) at all m ⟹ SB at all (X,b) ⟹ val ≤ c(n) all n ⟹ (with certified LB base + tightness)
     the full answer.

Key lemmas (claim + mechanism):
  - **(T) m=4, Case 4 Sub-case B impossible** — because from p₂<4Σ/15 one derives the exact identity
    `7d₂+3d₃ < δ+4d₁` (expand Σ=4δ+d₁+2d₂+3d₃; 15(δ+d₂+d₃)<4Σ). With d₂>t and d₃>d₁+t this forces
    10t < δ+d₁, while condition (2) (δ+d₂+d₃<4t) forces δ+d₁<2t ⟹ 10t<2t, contradiction.
  - **(T) m=4, Case 4 Sub-case A** — because P and C are complementary (d₁≥δ+d₃ vs d₁<δ+d₃) and in BOTH
    the two effective A-terms sum to exactly δ; condition (2) with d₂,d₃>t forces δ<4t−d₂−d₃<2t, so
    the min term ≤ δ/2 < t. (C also closes directly: δ+d₃−d₁ < 2t−t = t.)
  - **m=4 proof is purely algebraic** — holds for all positive reals, no integrality; only certified
    gap conditions (p₁≤Σ/2 residual, p₂<τ/2) + the R1/R2/R3 reductions are used.

Open gaps (builder fills):
  - **Step 3 (m≥5) is the load-bearing OPEN gap.** The explorer's induction m→m−1 via one pairing step
    goes through SB-monotone (Σ'/(2^{m−1}−1) ≤ Σ/(2^m−1) needs Σ'≲Σ/2) which is **certified DEAD**
    (sb-obstruction, R7) — so the m≥5 route MUST be the generalized DIRECT case-split (actual-A, like
    m=4), not an SB pairing induction. Concretely the builder must (a) prove the generalized matching
    strategies cover the "some small consecutive difference" region, and (b) prove the P/C-chain bound
    A ≤ p_m/2 together with the general Sub-case-B-impossibility forcing p_m < 2Σ/(2^m−1) from the tight
    gap condition. Numerically 0-violation at m=5, NOT proven. Mark honestly.
Cases to cover: m=2 (Case A.A, done), m=3 (Lemma R4, done), m=4 (Step 2, this round), m≥5 (Step 3, open).
Watch out for: (i) **budget feasibility** — verify R/S/P/C each use ≤ b=m−1 cuts (2 pairing cuts + at
most one final cut at m=4); the outline-reviewer should confirm the 4 strategies are budget-legal and
that "min over merge-family" is the right (existence-of-witness-strategy) direction for a UB.
(ii) Do NOT let the builder present the m≥5 induction as SB-monotone (dead); it must be actual-A.
(iii) Do NOT overclaim m≥5 — m=4 closes n=3 UB, the general-n UB stays partial.

---

### ll-inclusion-gap: advance   [PLAN REVIEW REQUIRED — re-opens the R9-cut unifier mechanism]
Target: Full problem — the LOWER bound (Liu Bang guarantees val ≥ c(n)) via Lemma LL: A(Q∪R) ≥ 1 for
every admissible XY-cut pattern, plus the certified UB tightness → the whole answer. This slug owns the
INC (S_Q ⊆ S_R) branch and now the refined-R closure.
Technique: **Mutual strong induction {Claim_R(n,ε), T_R(n)} descending n→n−2**, the exact analogue of the
certified `t-ell-mutual-induction`, using the certified **Gen-Decomp** as the descent engine in place of
the anchor-only SET IDENTITY. This is the refined-r-alt-tail unifier cut in R9 — now revived because the
lb-unifier report supplies the concrete descent (Gen-Decomp gives S_{Q_lo}⊆S_{R_lo} directly).

Skeleton:
  1. State **Claim_R(n,ε)**: for Q,R with max(R)≤2^{n−1}, h_R:=#{R-parts≥2^{n−2}} EVEN, A(R)≥1,
     S_Q⊆S_R, |Q|≤n+1, ΣQ=2^n+ε (ε∈[0,1)) ⟹ A(R)−A(Q) ≥ 1−ε. **T_R(n)**: same with ΣP∈(2^n−1,2^n),
     τ=2^n−ΣP ⟹ A(R)−A(P) ≥ 1−τ.
  2. Base cases n∈{1,2} (= anchor bases, R=G_0/G_1, certified); first nontrivial refined-R base n=4
     verified (lb-unifier §c: lower-band R_lo={1,1,1}, non-equal-top R_lo={3,2,1}, both 0-violation).
  3. Inductive step (h_R even): Gen-Decomp ⟹ A(R)−A(Q)=deficit_top+(A(R_lo)−A(Q_lo)), S_{Q_lo}⊆S_{R_lo}.
       - h=0: deficit_top ≥ 2^{n−2} ≥ 1 ≥ 1−ε. Done.
       - h=2: deficit_top=a+b, ΣQ_lo=2^{n−2}+ε', ε'=a−b (or a−b−τ) — the SAME 2a/2b-i/2b-ii split and
         arithmetic as the certified anchor; invoke Claim_{R_lo}(n−2,ε') or T_{R_lo}(n−2).
  4. **G-INC-2lb (lower-band cut, cut at 2^{k0}, k0≤n−3):** h_R=2, R_lo=G_{n−3} with the same cut →
     descends within the induction; well-founded on H=n−k0 (drops by 2), grounding on G-INC-2nt(n−2)
     or base n≤4.
  5. **G-INC-2nt, a≥1 (non-equal top cut 2^{n−1}→{a,2^{n−1}−a}):** h_R=2, R_lo=G_{n−3}∪{a}, a≥1 →
     R_lo a valid refinement, h_{R_lo}=2, descent clean.
  6. **G-INC-2e (equal-split, g=0, h̄≥2, q1>q2):** close by the |Q|-parity argument (|R|=n+1;
     Forcing ⟹ max(Q)≤2^{n−2}; |Q| even ⟹ [0,1)∉S_Q ⟹ A(Q)≤A(R)−1) PLUS the sum-vacuousness bound
     (feasibility needs q1+q2 > 2^{m−2}(9−m); for m≤5 exceeds max q1+q2 ≤ 2^m ⟹ vacuous).
  7. Conclude: G-INC-2 closed for lower-band + non-equal-top(a≥1) + equal-split, all n.

Key lemmas (claim + mechanism):
  - **Descent well-founded** — because Gen-Decomp applies at EVERY level (h_{R_lo}=2 stays even for
    lower-band and non-equal-a≥1 top cuts), n drops by 2, ΣQ_lo=2^{n−2}+ε' with ε'∈(−1,1) stays inside
    the certified {Claim,T} window (lb-unifier §a, verified identical to anchor).
  - **Induction carries R as a parameter** — R_lo is variable (not fixed G_{n−3}); the class {max(R)≤2^{n−1},
    h_R even, A(R)≥1} is closed under the R→R_lo descent, so Claim_{R_lo}/T_{R_lo} are in-hypothesis.
  - **G-INC-2e vacuous/parity** — because equal-split gives |R|=n+1 and Forcing caps max(Q)≤2^{n−2}; the
    unequal-top feasible region is empty for m≤5 (sum bound) and parity-killed for |Q| even.

Open gaps (builder fills):
  - **G-INC-2nt with a<1 (sub-unit flip): HARD.** R_lo=G_{n−3}△[0,a) is NOT a standard refinement; for n
    even A(R_lo)=A(G_{n−3})−a can dip below 1. Handle as a DIRECT n=4 base case (first occurrence in the
    descent), budget forces A(Q_lo)=0 (equal pairs). Mark; verified 0-violation n=4 but not proven general.
  - **G-INC-2e for m≥6:** needs L1 extended by one budget step (|Q_lo|≤m−1 vs L1's m−3). Small.
  - **G-GAP (non-containment S_Q⊄S_R): NOT closed here — separate residual** (handled by ll-dyadic-symdiff
    below). State explicitly that this advance does not cover it.
Cases to cover: h∈{0,2}; lower-band / non-equal-top-a≥1 / equal-split; a<1 sub-case; m≤5 vs m≥6 for 2e.
Watch out for: (i) do NOT strengthen the IH to ε<0 (FALSE, Q_lo={1.9,1.5}); ε'∈[0,1) only in 2b-i.
(ii) The a<1 exotic-R_lo must be flagged, not swept into "clean descent." (iii) Fallback if {Claim_R,T_R}
stalls on a<1: the lb-edges "direct A(R) bound" for R=G_{n−2}∪{a,2^{n−1}−a} (compute A(R) exactly).
(iii) enforce joint budget c_Q+c_R≤n in every numeric check.

---

### ll-dyadic-symdiff: advance   [PLAN REVIEW REQUIRED — introduces Opening D for the GAP part]
Target: Full problem — the LOWER bound via measure(S_Q△S_R) ≥ 1 for all admissible Q,R (this route does
NOT assume containment, so it owns the non-containment G-GAP cases), plus certified UB tightness.
Technique: certified REFL-telescope (double-REFL A(Q∪R)=max(Q)−max(R)+A(Q'∪R''), well-founded
piece-count descent) reducing general-n bucket (iii) to the base object A(Q'∪R'')≥1, then splitting that
base into INC + GAP sub-instances.

Skeleton:
  1. General-n bucket (iii) (max(Q),max(R)<2^{n−1} top-cut regime): REFL-telescope (certified) ⟹
     reduce to base A(Q'∪R'') ≥ 1. (n=3 fully closed R9.)
  2. Split the base by containment:
       - **INC sub-instances (S_{Q'}⊆S_{R''}):** ⟸ Claim_{R''}/T_{R''} — IMPORT {Claim_R,T_R} once
         certified in ll-inclusion-gap this round (state as a clean reduction; do not re-derive).
       - **GAP sub-instances (S_{Q'}⊄S_{R''}):** attack via **Opening D** — dyadic-level pairing of
         mismatched intervals: at each dyadic level pair each S_Q-only interval against a nearest
         S_R-only interval, the alignment cost accumulating to ≥1. — **HARD/OPEN**.
  3. Conclude bucket (iii) ≥1 ⟹ LL for the top-cut regime ⟹ (with the certified Cases 1/2/3a covering the
     other regimes) LL for all admissible Q,R ⟹ LB val ≥ c(n).

Key lemmas (claim + mechanism):
  - **Base reduction is legitimate** — because the double-REFL cancellation A(Q∪R)=max(Q)−max(R)+A(Q'∪R'')
    is certified and its telescope terminates by well-founded piece-count/Σ descent (certified R9).
  - **INC part of the base ⟸ {Claim_R,T_R}** — the INC sub-instance is exactly Claim_{R''} at the reduced
    level; no new work beyond the import (dependency on ll-inclusion-gap's build this round).

Open gaps (builder fills):
  - **Opening D (GAP sub-instances): the load-bearing OPEN gap.** ∫(N_Q−N_R)=1 alone is provably
    INSUFFICIENT (recorded); the builder must supply the dyadic-level pairing that upgrades the signed
    integral to measure(S_Q△S_R)≥1. Least-developed of the three fronts — treat as exploratory; a partial
    (e.g. closing GAP sub-instances with ≤2 mismatched levels, or all-mass-below constraint) is honest
    progress. Do not overclaim.
Cases to cover: bucket (iii) INC vs GAP; general n (n=3 done).
Watch out for: (i) the INC import is only valid once ll-inclusion-gap certifies {Claim_R,T_R} — if that
build stalls, state bucket (iii) INC as "conditional on the crux," not closed. (ii) enforce joint budget.
(iii) do NOT re-import the decertified "max(Q)<2^{n−1}⟹A≥2" (FALSE, B3 tight at A=1).

---

## Nominations (build set)
- **geometric-selfsimilar** — advance (UB): write (T) for m=4 (closes n=3 UB), attempt m≥5 direct
  case-split. PLAN REVIEW.
- **ll-inclusion-gap** — advance (LB INC): build {Claim_R,T_R} mutual induction (Gen-Decomp descent)
  closing G-INC-2nt(a≥1)+G-INC-2lb+G-INC-2e; a<1 as direct n=4 base. PLAN REVIEW (re-opens R9-cut unifier).
- **ll-dyadic-symdiff** — advance (LB GAP): general-n bucket (iii) base — import {Claim_R,T_R} for INC,
  Opening D dyadic-level pairing for GAP (non-containment). PLAN REVIEW.

No new slug opened: the R9-cut refined-r-alt-tail unifier is folded into ll-inclusion-gap's advance
(same INC route, same Gen-Decomp engine) rather than duplicated — its certified {Claim_R,T_R} lemma then
feeds ll-dyadic-symdiff. Dormant: alternating-sum-value, extremal-smoothing (retire if slots scarce).
Remaining LB frontier after this round: **G-GAP non-containment** (Opening D), the only piece with no
certified mechanism.
