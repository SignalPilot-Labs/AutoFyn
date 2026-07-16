# Lemma L1 (budget anchor bound): S_P ⊆ S_{G_{m−1}}, |P| ≤ m−1 ⟹ A(P) ≤ A(G_{m−1}) − 1

**Status:** CERTIFIED (proof-reviewer, round 9). Proposed by `ll-inclusion-gap`. Reviewer re-derived the
`m→m−2` induction and machine-verified tightness `max A(P) = A(G_{m−1}) − 1` with 0 violations for
`m = 2..6` (budget-enforced integer parts and 9806 random rational configs). The strict `−1` is forced
by the budget deficit (`|P| < m = |G_{m−1}|`), independent of `ΣP`.

## Statement
For every `m ≥ 1`: if `S_P ⊆ S_{G_{m−1}}` and `|P| ≤ m−1`, then `A(P) ≤ A(G_{m−1}) − 1`.
(`G_{m−1} = {2^0,…,2^{m−1}}`, `A(G_{m−1}) = (2^m + (−1)^{m−1})/3`.)

## Proof (strong induction on m, step m → m−2)
**Bases.** `m=1`: `P = ∅`, `A = 0 = A(G_0) − 1`. `m=2`: `|P| ≤ 1`; `P = {p}` forces `[0,p) ⊆ S_{G_1} =
[1,2)`, impossible, so `P = ∅`, `A = 0 = A(G_1) − 1`.
**Step m ≥ 3.** `S_P ⊆ S_{G_{m−1}}`, so the certified `top-band-decomposition` + `set-identity-selfsimilar`
apply at `thr = 2^{m−2}`: with `h̄ = #{parts ≥ thr}` even, `P_lo = {parts < thr}`,
`A(G_{m−1}) − A(P) = deficit_top + M`, `deficit_top = 2^{m−2} − δ_top ≥ 0`,
`M = A(G_{m−3}) − A(P_lo) ≥ 0`, with `S_{P_lo} ⊆ S_{G_{m−3}}` and `|P_lo| = |P| − h̄`. Show
`deficit_top + M ≥ 1`:
- `h̄ = 0`: `δ_top = 0`, `deficit_top = 2^{m−2} ≥ 2 ≥ 1` (`m ≥ 3`).
- `h̄ ≥ 2`: `|P_lo| = |P| − h̄ ≤ (m−1) − 2 = (m−2) − 1`, so P_lo satisfies L1 at level `m−2`
  (`S_{P_lo} ⊆ S_{G_{(m−2)−1}}`, `|P_lo| ≤ (m−2)−1`); IH gives `A(P_lo) ≤ A(G_{m−3}) − 1`, i.e. `M ≥ 1`.
Both branches give `A(G_{m−1}) − A(P) ≥ 1`. Descent lands only on levels `m−2`, grounding on m∈{1,2}. ∎

## Scope
Closes the equal-split top cut of G-INC-2 whenever the anchor bound applies (Case g=2, and g=0 with
`h̄=0` or two largest parts equal). Does NOT cover `g=0, h̄≥2, q₁>q₂` (open edge G-INC-2e), where
`ΣP_lo` leaves the certified window. Tight at `P = G_{m−1} ∖ {1}`.
