# Build report — geometric-selfsimilar (UB), Round 12

Status: **partial** (unchanged: n≤3 UB rigorous; n=4 / m=5 UB still OPEN). T5 not proven.

## What I did
Target was T5 (m=5 pure hard case) ⟹ n=4 UB, with HS-A2 the flagged blocking gap.

### 1. Rigorous structural reduction (solid)
For an m=5 hard case X={p₁>…>p₅}, Σ=31t, budget b=4: the single **pair1_2** cut (cut p₁ at interior
offset p₂; fresh p₂ pairs with spectator p₂ = parity-invisible, Lemma R1) is legal and reduces to the
effective 4-piece subproblem **Y′={d₁,p₃,p₄,p₅}** with 3 cuts left, Σ′=Σ−2p₂=3δ+d₁+d₃+2d₄ > 15t.
By Lemma M0, T5-via-pair1_2 ⟺ **min A(Y′,3) ≤ t**. Mechanism airtight.

### 2. CRITICAL negative finding — the integer grids are unreliable
On integer grids (Σ=31K, K∈{4,6,8,10}, ~105k configs) pair1_2's full merge-family min A(Y′,3) ≤ t with
**0 violations**. This is a **grid artifact**: an off-grid exact-Fraction search found an explicit
**counterexample where pair1_2 FAILS**:
`X = {157/5, 13, 46/5, 34/5, 23/5}` (Σ=65, t=65/31, δ=23/5 ≈ 2.19·t, i.e. δ>2t), with
`min A(Y′,3) = 1.049·t > t`. So pair1_2 is NOT universal; the multi-first-cut tree the outliner posits
is genuinely necessary. This confirms the reviewer's warning verbatim: δ>2t failures live strictly off
the denom-4/5 grids, so any "0 grid violations" claim (the R8/R10 evidence style) cannot certify the
continuous statement. **New rule: every UB numeric check must include off-grid random rationals.**

### 3. pair2_3 fallback confirmed on the witness
On the failing config, all ten single-cut pairings tested: pair1_2 = pair3_4 = pair1_5 = 1.049·t (fail),
but **pair2_3 = pair1_4 = pair2_5 = 0.382·t ≤ t** (= the true 5-piece optimum). So the outliner's
pair2_3 fallback for the δ>2t region is the correct move here. **HS-A2** ("δ>2t ⟹ pair2_3 gives A≤t")
remains the right target and the single blocking analytic gap. I could NOT close it: the explorer's
Σ-bound d₂+2d₃+3d₄+3δ ≤ 31t/2 still only yields d₂<3.5t, not the <2t a naive pair2_3-P argument needs.

### 4. T4's named strategies are insufficient at threshold t (rigorous negative)
Applying the certified T4 bounds (A_R≤e₂, A_S≤min(|e₁−e₃|,e₃), A_P≤ε/2, A_C≤ε+e₃−e₁) to sorted Y′ closes
only ≈86% (worst failing ratio 2.375, e.g. Y′={48,48,29,9}). Failures = Y′ has an **internal double
pair** (a difference of two Y′ pieces equals a third, giving invisible {w,w}, A=0 after halving the
rest). Adding cross-matching M2 and chain Pc narrows to ≈1% but the internal-double-pair configs remain.
So closing min A(Y′,3)≤t needs the full 4-piece merge family, a strictly stronger inequality than
certified T4 (whose Σ′/15 > t here). This is where the real analytic work sits.

## Remaining gaps (honest)
- **HS-A2** — UNPROVEN (the single blocker): δ>2t ⟹ some fallback (pair2_3) gives A≤t analytically.
- **The 4-piece-at-t inequality** min A(Y′,3)≤t on the pair1_2-success region — needs the full merge
  family, not T4-named. Not written.
- **Sub-B (cut_1@3) branch and general m≥6 (HS-A3)** — untouched.

## Spec concerns
1. The outliner's Step-1/Step-2 framing ("pair1_2 + T4-at-t closes 96.8%") rests on integer-grid stats
   that are unreliable off-grid — the real pair1_2-success set is smaller than the grids suggest, and the
   pair1_2 failure is not only "T4-named fails" but genuine merge-family failure (witness above). The
   qualitative tree (pair1_2 primary, pair2_3 fallback for δ>2t) is still correct.
2. All future UB verification must use off-grid rationals; I have added this as a role-memory rule.

## No new lemma files (nothing fully proved this round beyond the structural reduction, which is recorded
in the approach file, not yet certification-ready as a standalone lemma).
