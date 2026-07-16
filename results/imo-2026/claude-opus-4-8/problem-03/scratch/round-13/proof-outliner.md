## imo-2026-03

Population health check: the three leaders bottom out on THREE DISTINCT cruxes on independent tracks
(UB = HS-A2; LB-incgap = (★); LB-dyadic = HS-D1). The old 3+ round shared gap (G-INC-1) was closed R8.
So no forced "reframe the shared gap" is due — the field is already broad (one UB route + two rival LB
routes). I advance all three leaders with a re-planned next deliverable each, and open NO new whole-problem
slug: the run is one lemma (UB) and two isolated inequalities (LB) from solved; a fresh from-scratch
approach would be strictly lower value than finishing these. I also decline a copy on ll-inclusion-gap
(its two candidate routes are not co-equal — the perturbed mutual-induction route T'(j) risks re-treading
the R10-refuted {Claim_R,T_R} class, so I route the single build through the measure/band-accounting path).

---

geometric-selfsimilar: advance
Target: c(n) = 2^n/(2^{n+1}−1); XY holds Liu Bang to ≤ c(n) for every LB configuration (the UPPER BOUND),
  matching the certified lower bound → full both-bounds proof. This round advances the ONLY open UB piece.
Technique: reduction to μ(X,b) ≤ Σ/(2^{b+1}−1); the whole UB is now the single pure hard case (Lemma MK
  closed everything else); for m=5 (T5) the multi-first-cut tree pair1_2 (δ≤2t) / pair2_3 (δ>2t), each
  reducing 5 pieces to a 4-piece min-A-at-threshold-t bound, closed by a sorted-order case split.
Skeleton:
  1. Whole UB → single pure hard case (p₁≤Σ/2, all dⱼ>t, δ>t, m≥5) — by certified Lemma MK + Case A.A
     + Lemma AB (DONE, imported; not re-proved).
  2. T5 (m=5): pair1_2 (cut p₁ at offset p₂, invisible pair) gives 4-piece Y′={d₁,p₃,p₄,p₅} at budget 3;
     T5 ⟺ min A(Y′,3) ≤ t — by certified Lemma R1 (parity-invisible pair). Airtight, DONE.
  3. Branch δ ≤ 2t: pair1_2 succeeds. Sub-A P of T4-at-t on Y′ gives A_P = δ/2 ≤ t directly. Sub-A C and
     Sub-B need the FULL merge family (invisible-pair halving + cross-match M2) to reach A ≤ t. [GAP G1]
  4. Branch δ > 2t: pair1_2's only genuine failure is Sub-A P (Opening 2: Sub-A C / Sub-B are NOT genuine
     pair1_2 failures — the full merge family handles them). Fix by pair2_3 (cut p₂ at offset p₃) →
     Y″={p₁,d₂,p₄,p₅}, p₄=δ+d₄, p₅=δ. Prove min A(Y″,3) ≤ t. [GAP G2 = HS-A2, the headline deliverable]
  5. Combine 3+4 ⇒ min over the tree ≤ t ⇒ T5 ⇒ n=4 UB rigorous. Then m≥6 (HS-A3). [GAP G3, deferred]
Key lemmas (claim + mechanism):
  - HS-A2 (G2): in the Sub-A P branch with δ>2t, pair2_3 gives A(Y″,3) ≤ t — via the Σ-P bound
    [*] 2d₂ ≤ 2(p₂−p₃) ≤ 31t − 7δ − 6d₄ − 4d₃ (from the Sub-A-P-fires condition D1_{Y′} ≥ δ+d₄ and
    Σ=31t), then a 6-case split on the sorted order of Y″. Each case closes by a NAMED T4 strategy:
      • Case A (d₂>p₄): E2 ≤ (31−9δ−8d₄−4d₃)/2 < t/2 since 9δ+8d₄+4d₃ > 18+8+4 = 30 (δ>2,d₄>1,d₃>1). R closes.
      • Case B1 (δ≤d₂≤p₄, d₂<δ+t): E3 = d₂−δ < t. S(E3) closes.
      • Case B2 (δ≤d₂≤p₄, d₂≥δ+t): [*] forces 9δ+6d₄+4d₃ ≤ 29 ⇒ d₄ < 7/6·t; E2 = p₄−d₂ ≤ d₄−t < t/6. R closes.
      • Case C1 (δ−t ≤ d₂ < δ): E3 = δ−d₂ ≤ t. S(E3) closes. (This is the R12 off-grid witness, E3=0.382t.)
      • Case C2 (d₂ < δ−t, δ≤3t): Sub-A P fires on Y″ (D1_{Y″}=p₁−p₄ ≥ δ from [*]); A_P = d₂/2 < (δ−t)/2 ≤ t. P closes.
      • Case C3 (d₂ < δ−t, δ>3t): VACUOUS — Sub-A P on Y′ forces p₂ ≤ 5t but p₂=δ+d₄+d₃+d₂ > 5t (δ>3,d₄>1,d₃>1). Contradiction.
  - Merge-family closure (G1): for Y′ in Sub-A C (A_C = δ+d₄−D1 > t) or Sub-B (D1 < E3), pair1_2's full
    merge family (not just R/S/P/C) achieves A ≤ t — because the invisible-pair halving of the largest
    fragment plus the M2 cross-match drives the residual alternating quantity to ≤ t (numerically 0/149
    Sub-A-C configs and 0/1555 δ≤2t configs; needs the analytic write-up of the halving recursion, akin to MK).
Open gaps:
  - G2 (HS-A2, PRIMARY): VERIFY the Σ-P bound [*] from scratch (re-derive p₃=δ+d₄+d₃, p₂=p₃+d₂, and the
    Sub-A-P condition) and write the 6-case split rigorously with every constant in units of t. This closes
    the δ>2t branch and is the round's target.
  - G1 (merge-family, SECONDARY): analytic proof that pair1_2's full merge family gives A ≤ t for Sub-A C /
    Sub-B. Without it, the δ≤2t branch (and hence T5) is not fully written even after G2.
  - G3 (m≥6 / HS-A3): state EXPLICITLY as open — the tree is NOT yet proven uniform in m (Σ=63t, b=5, the
    δ-threshold may shift; Case-C3-type impossibility unverified for m=6). Do not claim m≥6.
Cases to cover: the 6 sorted-order cases of HS-A2 (A, B1, B2, C1, C2, C3) — all six, none skippable; plus
  Sub-A C and Sub-B of Y′ for G1.
Watch out for:
  - The strict arithmetic in Cases A / B2 / C3 relies on all dⱼ>t AND δ>2t (hard-case + branch). Verify each
    inequality is STRICT and that "all dⱼ>t" is exactly the pure-hard-case hypothesis, not assumed extra.
  - T4-tight-m4 is a bound at threshold Σ(Y′)/15, NOT at threshold t; only the NAMED strategies R/S/P/C
    transfer, applied case-by-case at threshold t. Do not invoke T4-tight-m4 as a black box here.
  - FORBIDDEN (do not revive): SB-monotone, R3-cascade actual-A, complement-cut m=4→3→R4, p₁@p₂
    threshold-invariant induction, integer-grid UB numerics (grid artifact — use OFF-GRID exact Fractions only).
  - Do not claim a global d₂<2t bound (FALSE — d₂ reaches 3.5t in Case A); the proof MUST be case-by-case.

---

ll-inclusion-gap: advance
Target: c(n) = 2^n/(2^{n+1}−1); Liu Bang guarantees ≥ c(n) (the LOWER BOUND) — via the inclusion route
  reducing LL (Case 2, A(Q)>0) to A(R)−A(Q) ≥ 1 for the refined-R top-cut branch.
Technique: Gen-Decomp descent A(R)−A(Q)=deficit_top+(A(R_lo)−A(Q_lo)) with S_{Q_lo}⊆S_{R_lo}; Floor Lemma
  A({a}∪G_j) ≥ A(G_{j−1}) ≥ 1; the remaining crux is the DFB / (★) at general size, a≥1.
Skeleton:
  1. LL Case 2 → refined-R top-cut → single odd-position inequality (★) O_{Q_lo} ≤ O_{R_lo}+a_v for h=2, a≥1
     — by certified Floor Lemma + Gen-Decomp + A=2O−Σ (DONE R12; h≥4, h=0, fully-tight n∈{4,5}, a<1 closed).
  2. Size-2 Q_lo (all j, all a∈[1,2^j)): CLOSE via the EQUAL-PAIR FORCING theorem — no non-equal pair can
     satisfy S_{Q_lo}⊆S_{R_lo} AND ΣQ_lo>2^{j+1}; so A(Q_lo)=0 and A(R)−A(Q)=deficit_top+A(R_lo) ≥ A(G_{j−1}) ≥ 1.
     This also closes ALL even j (parity forces |Q_lo|∈{0,2}). [was conjecture, now proven this round — WRITE it]
  3. Sizes ≥ 3 (only reachable at odd j, and size-4 at even j≥5): CLOSE via the measure/band-accounting form
     of (★). [GAP: this is the remaining crux, PRIMARY target]
Key lemmas (claim + mechanism):
  - Equal-pair forcing (proven this round — write rigorously): for R_lo={a}∪G_j (a∈[1,2^j)), any size-2
    S_{Q_lo}⊆S_{R_lo} with ΣQ_lo>ΣR_lo=a+2^{j+1}−1 ≥ 2^{j+1} FORCES p1=p2 — because (Case A) p1>2^j puts
    [2^j,p1)⊄S_{R_lo} (that band is R-even), and (Case B) p1≤2^j forces p2>2^j≥p1, contradicting p2≤p1.
    Then A(Q_lo)=0, so DFB ≥ deficit_top + A(R_lo) ≥ 1 by Floor Lemma. [CLOSES size-2 all j, all a; and all even j]
  - Band-accounting (★) for sizes ≥ 3 (PRIMARY GAP): rewrite (★) via A(P)=2O_P−ΣP as
    A(Q_lo) ≤ A(R_lo) + deficit_top − 1. Use S_{Q_lo}⊆S_{R_lo} ⇒ A(Q_lo)=measure(S_{Q_lo}) ≤ measure(S_{R_lo})=A(R_lo),
    the top-pair forcing p1 ≤ 2^j, and the sum constraint ΣQ_lo = ΣR_lo+σ_lo (σ_lo∈(0,2)) to bound the
    UNCOVERED measure A(R_lo)−A(Q_lo) ≥ 1−deficit_top band by band. Concretely:
      • size-3 (odd j): A(Q_lo)=(p1−p2)+p3 with p1≤2^j and p2+p3 > 2^j; bound p3 by the width of the
        lowest allowed S_{R_lo} band; min DFB=3/2 (slack) — write the band bound.
      • size-4 equal-top-pair (even j≥4): A(Q_lo)=p3−p4; top pair p1=p2≤2^j ⇒ p3+p4 = ΣQ_lo−2p1 < σ_lo+a−1 < 3;
        A(R_lo) ≥ A(G_{j−1}) ≥ 5 for j≥4 ⇒ DFB ≥ 5−3−1 = 1. (Opening D — near-complete, write it.)
Open gaps:
  - Band-accounting (★) for sizes ≥ 3 (PRIMARY): write the general band-by-band bound of A(R_lo)−A(Q_lo) ≥ 1−deficit_top.
    The measure-monotonicity A(Q_lo)≤A(R_lo) plus the sum constraint (σ_lo<2) and top-pair forcing (p1≤2^j)
    are the three ingredients; the slack is large (min DFB 3/2 for size-3, 4 for size-4) so this should close.
  - Size-4 general (even j≥5, non-top-band placement of the equal pair): Opening D closes X≥2^{j−1}; the
    X<2^{j−1} placement needs the same band bound. Cover it.
Cases to cover: size-2 (closed, write it); size-3 odd j; size-4 even j (equal-top-pair X≥2^{j−1} closed;
  other placements open); higher sizes only via the general band bound.
Watch out for:
  - Do NOT use "perturbed L1 without sum constraint" A(Q)≤A(R_lo)−1 for S_Q⊆S_{R_lo}: FALSE (j=1,a=1,Q={2}).
    The sum constraint ΣQ_lo=ΣR_lo+σ_lo (σ_lo∈(0,2)) is ESSENTIAL and must appear in the band bound.
  - Do NOT re-open the perturbed mutual induction T'(j) (Opening B): its descent {a}∪G_{j−2} is NOT closed
    for a≥2^{j−2}, echoing the R10-refuted {Claim_R,T_R} class. Route via band-accounting instead.
  - FORBIDDEN: "INC forces max(Q)≤max(R)" (FALSE R11 — even-mult counterexample); use the equal-pair
    forcing / measure-monotonicity + sum constraint. a<1 Family descent is unavailable for a≥1 (O1).

---

ll-dyadic-symdiff: advance (gap re-planned around the NEW R-cut pairing mechanism)
Target: c(n) = 2^n/(2^{n+1}−1); Liu Bang guarantees ≥ c(n) (the LOWER BOUND) — via the direct
  measure(S_Q△S_R) ≥ 1 route, an INDEPENDENT rival to ll-inclusion-gap. This round attacks the residual
  HS-D1 by a mechanism that BYPASSES the shared alternating-tail crux (per the CLAUDE.md plateau rule).
Technique: A(Q∪R) = measure{x : g(x) odd}, g = N_Q − N_R. Residual = {Sub-3a fails ∧ max g ≥ 2}. NEW:
  R-cut pairing — each R-cut of a G_{n−1} piece 2^k that crosses the level boundary places fragments in
  two consecutive dyadic levels whose odd-g measures SUM to exactly the crossed level's measure (≥1),
  independent of the cut point; Q-pieces contribute additional positive odd-g. This gives A ≥ 1 WITHOUT
  the alternating-tail bound and is max|g|-agnostic (no Sub-3a, no max|g|≤2 assumption).
Skeleton:
  1. LL Case 2 (A(Q)>0) → bucket (iii) (all pieces < 2^{n−1}) → measure(S_Q△S_R) ≥ 1, i.e. A(Q∪R) ≥ 1
     — imported (certified core: Case 1, Case 2 odd-count, Sub-3a, G1, F-neg). Residual = HS-D1.
  2. max g ≤ 1 slice: A ≥ ΣQ−ΣR = 1 — by certified Lemma G1. DONE.
  3. HS-D1 residual {Sub-3a fails ∧ max g ≥ 2}: prove A ≥ 1 by R-cut pairing. [GAP HS-D1, PRIMARY]
Key lemmas (claim + mechanism):
  - R-cut pairing (n=3 sub-case Q⊆I₂, R cuts piece 2, RIGOROUS this round — write it): with R={b,2−b,1,4}
    (b∈(0,1)) and Q={q1≤q2≤q3}⊂(2,4), the explicit g-profile gives
    A = b + (1−b) + (q2−q1) + (4−q3) = 1 + (q2−q1) + (4−q3) > 1. The first two terms (from the R-cut of
    piece 2: odd-g on (0,b) of measure b and on (1,2−b) of measure 1−b) sum to EXACTLY 1 regardless of b;
    the Q-terms are strictly positive. This is the mechanism template.
  - R-cut pairing (GENERALIZATION, PRIMARY GAP): every R-cut of a G_{n−1} piece 2^k into f∈I_{k−1} and
    2^k−f∈I_k creates odd-g regions whose measures sum to ≥ measure(I_{k−1}) = 2^{k−2} ≥ 1 (for k≥1;
    I₀ has measure 1). Since the residual has max g ≥ 2 (so g is genuinely non-monotone), at least one
    such level-crossing R-cut exists, and its paired contribution alone gives A ≥ 1; other R-cuts and the
    Q-pieces add non-negative odd-g measure. The load-bearing steps to make rigorous:
      (i) at least one R-cut crosses a level boundary in the residual (else all R-fragments stay within
          levels ⇒ N_R has the staircase parity of G_{n−1} ⇒ handle via Sub-3a/G1, contradiction with residual);
      (ii) the two paired odd-g regions do not get CANCELLED by overlapping Q-breakpoints — i.e. the paired
          measures are a genuine lower bound on the total odd-g measure, not double-counted;
      (iii) sum over all R-cuts + Q-contributions ≥ 1 (a level-decomposition A = Σ_k A_k with A_k ≥ 0 and
          the pairing lower-bounding two adjacent A_k's).
Open gaps:
  - HS-D1 generalization (PRIMARY): steps (i)–(iii). The n=3 R-cuts-piece-2 case is rigorous; extend to
    (a) n=3 R cuts piece 4 (fragments in I₁,I₂ — the report claims the same pairing, min A=9/8; write it),
    (b) Q not confined to the top level, (c) all n with multiple R-cuts. The cancellation-avoidance (ii)
    and the multi-cut accounting (iii) are the genuinely hard parts — the pairing per-cut is clean, but
    proving the contributions don't cancel across cuts/Q needs the level-decomposition A=Σ_k A_k ≥ 0.
Cases to cover: n=3 R-cut positions {piece 2 (DONE), piece 4, piece 1 (Sub-3a fires — outside residual)};
  Q inside vs crossing top level; general n multiple R-cuts.
Watch out for:
  - N_R(x) counts VALUES > x, not positions (the explorer corrected its own draft mid-report). Recompute
    every g-profile from N_R(x)=#{r∈R : r>x}; the sorted order of R-values (e.g. b<1<2−b<4 for b<1) drives
    the level structure.
  - The budget-forcing argument (Opening 3) is NOT rigorous (a cut can change odd-mult count by −3, R12).
    Do not rely on it — use the direct pairing/level-decomposition instead.
  - This is a BYPASS: it must NOT route through the alternating-tail crux A(Q′∪R″)≥1 shared with
    ll-inclusion-gap, nor through the R11 target B₊≤A₋+B₋ (CIRCULAR, R12). Keep it max|g|-agnostic.
  - The residual has min A strictly > 1 (5/4 at n=3, ≥ n−2 pattern) — do NOT aim to prove tightness A=1;
    the target is only A ≥ 1.

---

Field for the reviewer:
  - geometric-selfsimilar (advance) — PRIMARY: verify + write HS-A2 (6-case Sub-A P, δ>2t); this closes
    T5's δ>2t branch. SECONDARY: merge-family write-up (G1). Honest: m≥6 (G3) deferred. Highest value: the
    only step to a solved UPPER BOUND for n=4.
  - ll-inclusion-gap (advance) — write the proven size-2 equal-pair-forcing closure; PRIMARY: band-accounting
    (★) A(Q_lo)≤A(R_lo)+deficit_top−1 for sizes ≥ 3 (large slack). LOWER-BOUND route 1.
  - ll-dyadic-symdiff (advance, gap re-planned) — PRIMARY: generalize the NEW R-cut pairing (bypasses the
    alternating-tail crux) from the rigorous n=3 sub-case to all R-cut positions and all n; the
    cancellation-avoidance + multi-cut level-decomposition are the hard steps. LOWER-BOUND route 2 (rival).
  No new slug and no copy this round: the three cruxes are distinct and each is one step from closing its
  track; opening a fresh whole-problem attempt would be strictly lower value than finishing these.
  Retire candidates if slots scarce: alternating-sum-value, extremal-smoothing (unbuilt since R3, last two).
