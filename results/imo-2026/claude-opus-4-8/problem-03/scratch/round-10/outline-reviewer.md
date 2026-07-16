# Outline review — imo-2026-03 (Round 10)

Three advances, no new slug. All build on certified lemmas; none re-treads a recorded dead end.
I verified the load-bearing algebra by hand and by a 33k-config numeric sweep. Verdicts below.

---

## geometric-selfsimilar (UB) — CHANGES REQUESTED (plan sound; m=4 build approved, m≥5 open)

**Technique right.** The UB is already collapsed (certified Lemma AB + Cor AB.1) to the finite
inequality (T) at the tight budget b=m−1. Step 1 is done; the m=4 case-split is the deliverable.

**The m=4 proof is sound — I re-derived it fully.** With d₁=p₁−p₂, d₂=p₂−p₃, d₃=p₃−p₄, δ=p₄,
Σ=4δ+d₁+2d₂+3d₃, t=Σ/15:
- Cases 1/2/3 exhaust unless (d₂>t ∧ d₃>t ∧ |d₁−d₃|>t) = Case 4. Coverage is exhaustive **by
  construction** (I confirmed: 0 coverage-violations over 33 404 gap configs).
- **Sub-case B (d₃>d₁) impossible:** verified the derivation `7d₂+3d₃<δ+4d₁` from p₂<4Σ/15
  (15(δ+d₂+d₃)<16δ+4d₁+8d₂+12d₃). With d₂>t, d₃>d₁+t this forces 10t<δ+d₁; and condition (2)
  forces δ+d₁<2t ⟹ 10t<2t, contradiction. **Sub-case B never occurred in 33 404 configs.**
- **Sub-case A (d₁>d₃):** δ<4t−d₂−d₃<2t (0 failures numerically). P and C are complementary; in
  both the two effective terms sum to exactly δ (P: (Σ−2p₁)+(p₁−p₂−p₃)=p₄=δ; C: (d₁−d₃)+(δ+d₃−d₁)=δ),
  so the min ≤ δ/2 < t. C also closes directly (δ+d₃−d₁<2t−t=t). Both branches valid.

The proof is purely algebraic (no integrality), uses only certified gap conditions + R1/R2/R3 merge
mechanics. **m=4 ⟹ n=3 UB rigorous — real progress. Build it.**

**Issues for the builder to close:**
1. The explorer's *exact* A-value formulas have typos (Strategy R: `p₁−p₄=d₁+d₂+d₃`, not `+δ`;
   `A_R=min(d₁+d₃,d₂)` is loose). Only the **bounds** A_R≤d₂, A_S≤d₃, A_S≤|d₁−d₃|, A_P≤δ/2,
   A_C≤δ+d₃−d₁ are load-bearing and correct — the builder must cite the certified R1/R2/R3 merge
   mechanics for "A(2-piece {u,v}) ≤ min(u,v)" rather than restate the typo'd closed forms.
2. **Budget feasibility (outliner watch-out i) — confirm in writing:** each of R/S/P/C uses ≤ b=m−1=3
   cuts (2 pairing cuts + ≤1 final cut). And "min over merge-family ≤ t" is the correct
   existence-of-witness-strategy direction for a UB (XY only needs ONE strategy holding val ≤ c(n)).
3. **Step 3 (m≥5) is OPEN and must stay open.** The outliner correctly forbids the SB-monotone /
   Σ'≲Σ/2 pairing induction (certified DEAD, sb-obstruction R7) and requires the generalized DIRECT
   actual-A case-split. Do NOT let the builder present m≥5 as an SB reduction. Do NOT overclaim: m=4
   closes n=3 UB only; general-n UB stays partial. The m≥5 plan (generalized R/S cover small-difference
   region; P/C-chain gives A≤p_m/2 with p_m<2Σ/(2^m−1)) is a genuine direction but NOT proven — flag it.

---

## ll-inclusion-gap (LB INC) — CHANGES REQUESTED (re-opening the unifier is now legitimate)

**The R9 cut is correctly reversed.** refined-r-alt-tail was cut in R9 *only* because the anchor's
SET IDENTITY doesn't transfer. The now-certified **Gen-Decomp** (R9) supplies S_{Q_lo}⊆S_{R_lo}
DIRECTLY with no SET IDENTITY — the exact obstruction is removed by a certified lemma, and run_state's
R9 rule explicitly endorses re-opening on this basis. This is NOT a re-tread; my R9 memory rule
(cut a hedge whose descent lemma is UNKNOWN) does not apply now that the descent lemma is CERTIFIED.

**Well-foundedness is genuinely named.** Descent measure = n, dropping by 2 each Gen-Decomp step,
grounding at n∈{1,2} or the n=4 direct base. For lower-band and non-equal-a≥1 top cuts, h_{R_lo}=2
stays EVEN so Gen-Decomp re-applies at every level, and the class {max(R)≤2^{n−1}, h_R even, A(R)≥1}
is closed under R→R_lo — so Claim_{R_lo}/T_{R_lo} are genuine in-hypothesis calls. Mirrors the
certified t-ell-mutual-induction exactly.

**No hidden circularity / no ε<0.** ε'=a−b∈(−1,1); the anchor's 2a/2b-i/2b-ii split routes ε'<0 to
**T_{R_lo}(n−2)**, never to Claim with negative ε (the run_state FALSE case). Outliner watch-out (i)
states this explicitly. Good.

**Issues for the builder:**
1. **a<1 sub-unit flip is honestly HARD/OPEN** and correctly handled as a direct n=4 base (R_lo=
   G_{n−3}△[0,a) is not a standard refinement; A(R_lo)=A(G_{n−3})−a can dip below 1 for n even). Keep
   flagged; do NOT sweep into "clean descent." Numeric 0-violation n=4 is not a proof — mark it.
2. G-INC-2e: both explorers confirm vacuous for m≤5 (sum bound q₁+q₂>2^{m−2}(9−m) exceeds max 2^m)
   and margin≥3 at m≥6. The m≥6 "L1 extended by one budget step" is small but genuinely unwritten —
   list it as an open sub-item, not "done."
3. **G-GAP (non-containment) is NOT covered here** — the outliner states this explicitly. Good; it is
   the ll-dyadic-symdiff residual. Enforce the joint budget c_Q+c_R≤n in every numeric check.

---

## ll-dyadic-symdiff (LB GAP) — CHANGES REQUESTED (exploratory; Opening D is a wish with a direction)

**Legitimate distinct whole-attempt.** This route bounds measure(S_Q△S_R)≥1 for ALL admissible Q,R
and thus OWNS the non-containment G-GAP cases the containment route cannot reach — the one remaining
LB piece with NO certified mechanism. Keeping a scout on it is warranted.

**Honest about the gap.** The REFL-telescope base reduction is certified (R9); the INC sub-instances
import {Claim_R,T_R} (conditional on ll-inclusion-gap certifying it — outliner correctly says state as
conditional if that build stalls). The genuinely new content this round is **Opening D** (dyadic-level
pairing for the GAP part), which the outliner flags as "the load-bearing OPEN gap… least-developed…
treat as exploratory… do not overclaim," and notes ∫(N_Q−N_R)=1 alone is provably INSUFFICIENT.

**Issue:** Opening D is currently a *direction*, not a mechanism — "pair each S_Q-only interval against
a nearest S_R-only interval, cost accumulating to ≥1" has no proof the accumulation reaches 1. Accept
as an exploratory build; a partial (GAP sub-instances with ≤2 mismatched levels, or an all-mass-below
constraint) is honest progress. Do NOT let the builder claim bucket(iii) closed on the strength of the
import + an unproven Opening D. Do NOT re-import the decertified "max(Q)<2^{n−1}⟹A≥2" (FALSE, B3 tight).

---

## Ranking (Elo after this round, stale cleared)

geometric-selfsimilar 1709.1 > ll-inclusion-gap 1625.9 > ll-dyadic-symdiff 1508.0 >
alternating-sum-value 1391.9 > extremal-smoothing 1265.1

Head-to-heads recorded: geometric > ll-inclusion (UB collapsed to one finite ineq, m=4 closes n=3
this round vs ll-inclusion still has a<1+G-GAP open); ll-inclusion > ll-dyadic (certified Gen-Decomp +
named well-founded induction vs an unproven Opening D wish); geometric/ll-inclusion/ll-dyadic all >
alternating-sum-value (dead-ended greedy, unbuilt since R3) > extremal-smoothing (S1 stuck 4+ rounds).
No new slug (unifier folded into ll-inclusion-gap); no copy.

build set: geometric-selfsimilar, ll-inclusion-gap, ll-dyadic-symdiff
