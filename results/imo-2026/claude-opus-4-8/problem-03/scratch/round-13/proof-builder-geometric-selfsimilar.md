# Build report — geometric-selfsimilar (imo-2026-03), round 13

## Verdict: HS-A2 PROVED (Sub-A-P branch of T5, δ>2t). Status stays `partial` (T5 NOT complete).

## What I proved (rigorous, written into approaches/geometric-selfsimilar.md §R13 + lemmas/HS-A2.md)
- **HS-A2:** in the m=5 pure hard case with δ>2t, IF the Sub-A-P condition `D1_{Y'}=d₁−p₃ ≥ δ+d₄` holds
  on `Y'={d₁,p₃,p₄,δ}`, THEN pair2_3 (cut p₂@p₃, Lemma R1) gives `Y″={p₁,d₂,p₄,δ}` with `min A(Y″,3) ≤ t`.
- Re-derived the Σ-P bound [*] `2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃` from scratch (`D1_{Y'}=31t−6δ−5d₄−4d₃−2d₂`,
  firing condition `≥ δ+d₄`).
- 6-case exhaustive/disjoint split on d₂'s sorted position in Y″, each closed by a NAMED ≤3-cut strategy
  re-derived from Lemma R1 (not cited as a T4 black box):
  - A (d₂≥p₄): R, `A ≤ (31t−9δ−8d₄−4d₃)/2 < t/2` (uses δ>2t,d₄>t,d₃>t ⇒ 9δ+8d₄+4d₃>30t).
  - B1 (δ≤d₂<p₄, d₂<δ+t): S, `A ≤ d₂−δ < t`.
  - B2 (δ≤d₂<p₄, d₂≥δ+t): [*] forces `d₄<7t/6`; R, `A ≤ d₄−t < t/6`.
  - C1 (δ−t≤d₂<δ): S, `A ≤ δ−d₂ ≤ t`. (R12 witness lives here, E3=0.382t.)
  - C2 (d₂<δ−t, δ≤3t): custom — halve p₁, cut p₄@δ, finish {d₄,d₂}; `A ≤ |d₄−d₂| < t` since d₂,d₄∈(t,2t).
  - C3 (d₂<δ−t, δ>3t): VACUOUS — [*] forces 2d₂<0.

## KEY CORRECTION to the outliner/explorer (do not retry the broken version)
Case C2 does NOT close via "T4-P fires, A_P ≤ d₂/2". I disproved this: the P construction on Y″ gives
effective {p₁−p₄−δ, d₂} and `p₁−p₄−δ ≤ d₂ ⟺ δ+2d₄+2d₃ ≤ 0`, impossible, so p₁−p₄−δ > d₂ always in C2 and
A_P is NOT ≤ d₂/2. My numerics confirmed: the simple pair2_3 menu (R/S/M2/Pa/Pb/Pc/pair+MK) FAILS on ALL
~5.7k C2 configs (worst ratio 1.20). The TRUE optimum (~0.1–0.34t) is reached by the custom halve-p₁
strategy, whose clean bound |d₄−d₂|<t I derived (both d₄,d₂ ∈ (t,2t) from hard-case + [*]) and verified.

## Numerically verified (off-grid exact Fractions, Σ=31, t=1)
- All 6 per-case exact bounds: **0 violations / 12422 genuine Sub-A-P δ>2t configs.**
  Case counts A=8, B1=1429, B2=4, C1=8123, C2=2858, C3=0 (empty as claimed).
- Split exhaustive & disjoint (every config lands in exactly one case).
- R12 witness X={157/5,13,46/5,34/5,23/5}: Case C1, δ=2.194t, d₂=1.812t, E3=0.382t — confirmed.
- Continuous-optimum search confirms min A(Y″,3) ≤ 0.34t on C2 (consistent with |d₄−d₂|).

## Gaps that REMAIN OPEN (honest — T5 and n=4 UB are NOT proven)
- **G1 (blocks T5):** the pair1_2 success region — Sub-A-C (`A_C=δ+d₄−D1_{Y'}>t`), Sub-B (`D1_{Y'}<e₃`),
  and the whole δ≤2t region — needs the full merge-family analytic write-up (~40k of ~50k failure configs).
  Numerics 0-violation only; no proof. Without G1, HS-A2 alone does NOT close T5.
- **G3 (m≥6, HS-A3):** untouched. Step tree is NOT uniform in m — HS-A2 closes only m=5's Sub-A-P branch.
  For m≥6 the δ-threshold and Case-C3 impossibility are unverified.

## Spec concerns for the outliner
1. The Case-C2 "P/A_P≤d₂/2" mechanism in the outline is wrong (see correction). The certified fix is the
   custom halve-p₁ strategy. Update any downstream plan that reuses "A_P≤ε/2 for the min piece" — it needs
   the effective smaller piece ≤ ε, which does not hold here.
2. G1 is the true next blocker for a solved n=4 UB. The custom halve-p₁ strategy that saved C2 (invisible
   halving of the huge top piece, then solve the 3-piece residual) may be the right template for the G1
   merge family too — worth scouting as a uniform "halve-p₁-then-3-piece" reduction on the pair1_2 side.
