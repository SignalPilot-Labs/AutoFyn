## imo-2026-03

Answer (fixed): c(n) = 2^n/D_n, D_n = 2^{n+1}−1. Certified imports available to every approach:
L0 claim=odd-rank-sum, L1 reduction to multiset-refinement game, L2 S↔odd-sum, L3 layer-cake
+ XOR (S(Q⊔C)=S(Q)+S(C)−2W), L4 min-pairing S=sum−2β, L5 peel-max, L6 truncation
(S(B)=e+S(B_low), ≤1 shard above H), L7 unconditional h≥1⟹S≥1, L8 φ-telescoping Case-1.

Field-wide state: the LB residual is ONE inequality in three guises — **S(Q)+S(C)−2W ≥ 1**
(equiv W ≤ (S(Q)+S(C)−1)/2, equiv β(B_low) ≤ 2^n−1) in the h<1 / e<1 sub-case; PLATEAUED 3
rounds. NEW facts driving this round: (a) the "cuts-on-C cap W" mechanism is NUMERICALLY REFUTED
(true n=3 extremal spends ZERO cuts on C, W large) — every approach below MUST drop it; (b) the
LB extremal witness = the UB dyadic cascade B_min, exactly; (c) a free mini-lemma exists
(Q self-pairing ⟹ W=0). The four approaches below attack the shared inequality with FOUR
DISTINCT mechanisms (profile-IH / β-matching / frontier-sweep / convex-average) so they do NOT
die together, per the single-gap trap.

---

induction-peel: advance (LB residual via STRENGTHENED POINTWISE IH; drop cut-on-C cap)
Target: max_A min_B S(B) = 1/D_n, hence c(n)=2^n/D_n (whole problem, both bounds).
Technique: strong induction on n peeling the top dyadic scale; layer-cake/XOR (L3) + truncation
  (L6). The advance replaces the refuted scalar-budget cap with a *profile* induction hypothesis.
Skeleton:
  1. Import reduction + truncation: S(B)=e+S(B_low); e≥1 done (L6/L7). Residual: e<1 ⟹
     S(B_low) ≥ 1−e, i.e. S(Q_low)+S(C)−2W ≥ 1−e with C a ≤(n−1)-cut refinement of R={2^0..2^{n−1}}.
  2. WARM-UP mini-lemma (free, certify as L9): if Q_low's parts pair into equal consecutive
     values (N_Q(t) even ∀ t<H) then W=0 and S(B_low)=S(C) ≥ 1 by IH alone. Covers the pure-
     bisect boundary h=0; template for "self-cancelling Q bypasses overlap." — by L3 (N_Q even
     ⟹ integrand of W is 0) + IH.
  3. STRENGTHEN the IH from scalar "S(C) ≥ 1" to a pointwise profile P*(n−1) on the layer-cake
     function N_C(t): a lower bound on the *odd-measure profile* m_C(t):=meas{s<t : N_C(s) odd}
     that the induction carries, chosen so that it directly upper-bounds the achievable overlap
     W against ANY Q_low, not via a scalar. Prove P*(n) by the same peel induction.
  4. Close the residual: combine P*(n−1) with the high-band term and the extra-unit accounting
     (at the extremal Q_low→copy(C)+one unit; the surviving +1 is exactly S(Q_low)−S(C)).
Key lemmas (claim + mechanism):
  - L9 self-pairing ⟹ W=0 — because N_Q even at every height kills the XOR overlap integrand
    pointwise; then S(B_low)=S(Q_low)+S(C) ≥ S(C) ≥ 1 (IH). RIGOROUS NOW, bank it.
  - P*(n): profile IH — because the scalar S(C)≥1 is provably too weak (explorer finding (a):
    C uncut yet W large), only the *shape* m_C(t) of C's odd-region controls its alignment
    overlap with Q; a profile bound is the honest missing content, and it inducts because R is
    itself a scaled P_{n−1}.
Open gaps: step 3 (formulate + prove the correct profile statement P*) and step 4 (the extremal
  +1 accounting) — the builder's real work.
Cases to cover: e≥1 (done, L6/L7); e<1 with Q self-pairing (step 2, free); e<1 general (steps 3–4).
Watch out for: do NOT write "cut count on C caps W" (REFUTED this round — flag if it reappears);
  P* must bound W's alignment, not C's cut count. Keep S(Q_low)≥0 (P1) — Q_low may itself be cut.

---

alternating-sum-potential: advance (LB residual reforged as a DIRECT β-MATCHING bound via L4)
Target: max_A min_B S(B) = 1/D_n (whole problem).
Technique: min-pairing identity L4 (S = sum − 2β, β = max matched-smaller-mass) used for the
  LOWER bound — a genuinely different language from the measure-theoretic overlap W. Reduces the
  residual to a clean combinatorial matching cap on shard ranks.
Skeleton:
  1. Import truncation: residual is S(B_low) ≥ 1−e, B_low all parts ≤ H, sum = D_n − e.
  2. By L4, S(B_low) = sum − 2β = (D_n − e) − 2β(B_low). So S(B_low) ≥ 1−e  ⟺
     **β(B_low) ≤ (D_n − 1)/2 = 2^n − 1.**  (the entire residual, as a matching cap)
  3. Prove β(B_low) ≤ 2^n − 1: the max matched weight of B_low cannot reach half its mass;
     at least ~1 unit of mass is forced unmatchable by the superincreasing scale gaps.
  4. Combine with the certified generalized Case-1 (L8) and e≥1 (L6/L7) to assemble the full LB.
Key lemmas (claim + mechanism):
  - Residual ⟺ β(B_low) ≤ 2^n−1 — because S = sum − 2β exactly (L4) and sum(B_low)=D_n−e; the
    algebra collapses the e-dependence cleanly (target is e-free).
  - β-cap β(B_low) ≤ 2^n−1 — mechanism to build: any pairing pairs a part only with one ≤ it;
    B_low is a ≤n-cut refinement of the superincreasing {1,2,…,2^{n−1}} with 2^n shredded into
    parts ≤2^{n−1}. Match-weight ≤ sum/2 = (2^{n+1}−1−e)/2; the superincreasing "odd count at the
    finest scale" (extremal: three 1's, one unmatched) forces the deficit ≥ (1−e)/2·2. At the
    cascade B_min one unit is the lone unmatched singleton, so β=2^n−1 is exactly attained.
Open gaps: step 3 (the β ≤ 2^n−1 combinatorial cap) — the real crux, but now a matching/rank
  counting statement, not a measure overlap; may yield to a scale-bucket / Hall-deficit argument
  on the dyadic ranks.
Cases to cover: top-uncut (L8, done); e≥1 (L6/L7, done); e<1 (step 3).
Watch out for: L4's matched twin does NOT delete the original (both survive); β is a MAX over
  pairings, so the cap must hold for EVERY pairing — a single good pairing does not suffice here
  (opposite direction from the UB witness use of L4).

---

global-max-peel: revise (LB residual via an AMORTIZED FRONTIER-POTENTIAL sweep — new framing)
Target: max_A min_B S(B) = 1/D_n (whole problem, LB first).
Technique: aimo-0019-style amortized/banker's charging over a dynamic height sweep — REPLACES
  the static Q/C split (self-admittedly cosmetic in the current file) with a process framing far
  from the rest of the field, per the plateau rule.
Skeleton:
  1. Import G(n) ⟺ S(B) ≥ 1 for ≤n-cut refinements of P_n; import Lemma H (L7) to kill h≥1.
  2. Sweep the height variable t from 0 upward through the layer-cake N_B(t). Maintain a
     running potential Φ(t) = (odd-measure accumulated up to t) − λ(t), where λ(t) is a linear/
     dyadic-scale "credit line" tuned so Φ stays ≥ some floor.
  3. Each time t crosses a part-boundary of B (a jump of N_B), charge the crossing against the
     part being crossed; show the invariant Φ(t) ≥ deficit-floor(t) is preserved across every
     crossing by the superincreasing gap between consecutive dyadic scales.
  4. At t = H the accumulated odd-measure is ≥ 1 (the total deficit caps at exactly the
     superincreasing "+1"), giving S(B) ≥ 1.
Key lemmas (claim + mechanism):
  - Frontier invariant Φ(t) ≥ floor(t) — because each part of B lives below its origin scale 2^j,
    so a crossing at height t can only absorb credit proportional to the scale reached; the
    superincreasing 2^n = 1+Σ_{j<n}2^j means the cumulative absorbable credit is short of the
    total by exactly 1 unit (aimo-0019: cumulative resource ≤ const·progress, cap 3<4 units).
  - Deficit caps at 1 — because the "+1" is the top scale's excess over the sum of all lower
    scales; the sweep spends it exactly once (matches the cascade extremal's lone unit).
Open gaps: the exact credit function λ(t) / floor(t) and the per-crossing charge bound (step 3).
  This is the genuinely-different bet; it may or may not beat the wall, but it is FAR from the
  profile-IH and β routes so it fails independently.
Cases to cover: h≥1 (L7, done); h<1 handled by the sweep uniformly (no c_n case split — that is
  the point of the reframing).
Watch out for: do not silently re-import the static W-overlap bound (that is the wall). The
  charge must be against the part crossed, not against C's cut count (REFUTED). Read aimo-0019
  in full before building (crux corpus).

---

averaging-upper-bound: new (UPPER bound via CONVEX-COMBINATION of MATCH/BISECT — min ≤ average)
Target: max_A min_B S(B) ≤ 1/D_n for every A, i.e. Lemma B: U_k(A) ≤ sum(A)/D_k (whole UB).
Technique: probabilistic/averaging bound (crux aimo-0198: min(X,Y) ≤ weighted avg), sidestepping
  the exhausted case-split "which of MATCH/BISECT wins." FAR from the branch-inequality DP and
  the min-pairing/amortized-charging witness (both exhausted per dispatch).
Skeleton:
  1. Import the certified recursion (R) U_k(A)=min(S(A), min_{split} U_{k−1}(split)), the base
     case U_0(A)=S(A) ≤ sum(A) (P2, any part count), and the EXACT S-effect of MATCH/BISECT
     (induction-peel §4 — the FORMULAS are certified; only the case-split reasoning is off-limits).
  2. For A with ≥2 parts, top a_1, ρ=sum−a_1, r=a_1/ρ: by (R),
     U_k(A) ≤ min(U_{k−1}(MATCH A), U_{k−1}(BISECT A)) ≤ p·U_{k−1}(MATCH A)+(1−p)·U_{k−1}(BISECT A)
     for ANY p=p(r)∈[0,1]. (single-part A: BISECT to {s/2,s/2}, S=0 ≤ s/D_k, done.)
  3. KEY inequality: choose p(r) and a strengthened profile IH so that the p-average ≤ sum/D_k.
     Since D_k = 2D_{k−1}+1, the factor-2 must come from BISECT capping a_1 at a_1/2 and MATCH's
     carry a_1−a_2 dropping into a strictly smaller subgame; the weight p(r) balances the two so
     their average telescopes to 1/D_k.
Key lemmas (claim + mechanism):
  - min ≤ weighted average — trivial (min(X,Y) ≤ pX+(1−p)Y for p∈[0,1]); the point is it AVOIDS
    ever deciding which branch wins (the source of the F1 no-closed-form obstruction).
  - The averaged bound closes — mechanism: aimo-0198 pattern; the two moves have complementary
    strengths (BISECT good when r large, MATCH good when r small), so a well-chosen convex mix is
    uniformly ≤ target even though NEITHER branch's scalar sum-IH (s/D_{k−1}) is enough alone.
Open gaps: step 3 — finding p(r) and the profile IH that makes the convex combination telescope
  to s/D_k. THE crux of this approach; honestly hard, but a structurally new lever.
Cases to cover: |A|=1 (trivial bisect); |A|≥2 (the average). No "which branch" split — by design.
Watch out for: the scalar sum-IH (U_{k−1}(A')≤s/D_{k−1}) on BOTH branches is provably TOO WEAK
  (average of two things each ≤ s/D_{k−1} is still ≤ s/D_{k−1} > s/D_k) — the averaging MUST use
  the exact S-effect and a profile-sensitive IH, not the scalar sum bound. Confirm MATCH needs
  a_2 to exist (≥2 parts). This is NOT a one-pass greedy rule (it mixes two analyzed global moves
  by a fixed-in-r weight), so it escapes the KNOWN-FALSE one-pass ban — verify this distinction.

---

Retire/leave: smoothing-extremal (RETHINK, Lemma G refuted — do not resurrect), explicit-
certificate (stub; its "concentrate cuts on a_1" is KNOWN-FALSE). Not nominated.

Build set (recommended): induction-peel, alternating-sum-potential, global-max-peel,
averaging-upper-bound — four distinct mechanisms on the two shared walls; they fail independently.
