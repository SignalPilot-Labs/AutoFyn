# Build report — ll-dyadic-symdiff (LB), Round 12

**Status: partial** (advanced; residual precisely isolated, no overclaim).

## Target (per outline-reviewer CHANGES REQUESTED)
Sub-3a dichotomy: `Sub-3a fires ⟹ A ≥ 1` (certified); new crux `HS-D1: Sub-3a fails ⟹ A ≥ 1`.
Also HS-D2 (g(0+)-even doubly-negative) and HS-D3 (max|g|≥3 agnosticism). Turn the per-level parity
switch into a fixed positive measure — rigorously.

## What I did (all in `results/imo-2026-03/approaches/ll-dyadic-symdiff.md`, R12 section)

1. **Dropped the R11 target `B₊ ≤ A₋ + B₋`** as a reduction — confirmed algebraically `⟺ A ≥ 1` (circular).
   Recorded dead-end.

2. **Re-framed the crux as the Sub-3a dichotomy** and showed the tight `A=1` witness `Q={3,3,2},R={2,2,2,1}`
   has **Sub-3a firing** (g(0+)=−1 odd, I₀ fully odd), so it is NOT in the `Sub-3a fails` residual; the
   residual is numerically `min A = 9/8, 2, 3` for n=3,4,5.

3. **Foundation F-neg (full rigorous proof, PROMOTABLE):** `g(0⁺) = |Q|−|R| = c_Q − c_R − (n−1) ≤ −1`.

4. **NEW rigorous cheap-kill Lemma G1 (full proof, PROMOTABLE):** `max g ≤ 1 ⟹ A(Q∪R) ≥ ΣQ−ΣR = 1`.
   One-line via `∫g = M₁ − Σ_{k≤−1}|k|M_k ≤ M₁` and `A ≥ M₁`. **Strictly generalizes certified Lemma D1**
   on the upper side (D1 needs `|g|≤1`; G1 needs only `g≤1`, g arbitrarily negative). Closes the ENTIRE
   `max g ≤ 1` slice of the residual, all n. Verified 0 viol (n=3, 168 configs).

5. **HS-D3 RESOLVED (rigorous):** the whole route (`A=measure{g odd}`, F-neg, Sub-3a, G1) is
   `max|g|`-agnostic — no `max|g|≤2` hypothesis anywhere (only D1 uses `|g|≤1`). Also corrected the record:
   `max|g|≤2` is NOT easier (level-charge reduction is circular there too).

6. **RIGOROUS OBSTRUCTION pinning HS-D1/HS-D2:** the residual is exactly `{Sub-3a fails ∧ max g ≥ 2}`. I gave
   an abstract g-profile `g=(−1 on [0,ε), +2 on [ε,ε+s), 0)` with `∫g=1` that satisfies F-neg (g(0+)=−1 odd)
   AND makes Sub-3a fail on every level, YET has `A = ε < 1`. So **F-neg + budget-parity are provably
   insufficient** — any proof of HS-D1 MUST use the `ΣQ=2^n` / `N_{G_{n−1}}` staircase geometry, not parity
   alone. This refutes a parity-only "per-level fixed measure" mechanism and precisely delimits the open gap.

## Correction I flagged (spec concern)
The explorer's **budget-parity** proof ("each cut lowers the odd-mult count P by ≤ 1, so need ≥ n cuts") is
**not rigorous**: a cut can change P by −3 (both fragments land on pre-existing odd-mult values). The claim
(R has an odd-mult piece) is verified n=3 (min cuts to all-even = n) but its general-n proof is OPEN. It is
NOT load-bearing for my results (only yields A>0), so I present it with the caveat, not as established. The
sum-parity shortcut (ΣR odd) does NOT work here because R's values are arbitrary reals.

## Honest residual (OPEN, not overclaimed)
`HS-D1`/`HS-D2` = `{Sub-3a fails ∧ max g ≥ 2}`. Numerically true with margin (A ≥ 9/8, 2, 3) but the
mechanism needs the dyadic-staircase geometry — the obstruction shows parity foundations cannot supply it.

## Promotable lemmas for certification
- **Lemma G1** (one-sided small-discrepancy kill): `max g ≤ 1 ⟹ A(Q∪R) ≥ ΣQ−ΣR`. Full proof §4.
- **Foundation F-neg**: `g(0⁺) = c_Q − c_R − (n−1) ≤ −1` in bucket (iii). Full proof §2.

## Numerics (all bounded <30s, exact Fraction)
- F-neg: 1548/1548 (n=3,4,5). Target A≥1: 0 viol (n=3,168 / n=4 / n=5). G1: 0 viol. Budget-parity n=3:
  min cuts to all-even = 3 = n, 0 all-even R with c_R ≤ 2.

Verdict expectation: CHANGES REQUESTED (real new rigorous progress — Lemma G1 + F-neg + agnosticism +
obstruction — but the core HS-D1 residual remains open).
