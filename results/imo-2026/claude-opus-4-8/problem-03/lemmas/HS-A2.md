# Lemma HS-A2 — pair2_3 closes the Sub-A-P branch of T5 (m = 5, δ > 2t)

**Status:** CERTIFIED by proof-reviewer, round 13. Reviewer independently re-derived [*] and all 6 case
bounds by hand, and independently confirmed the CONCLUSION `min A(Y″,3) ≤ t` by an achievable-strategy
search (matching/halving cuts, an upper bound on the true minimum) over targeted off-grid Fraction configs
hitting all live cases (A=27, B1, B2=21, C1, C2=556; worst achievable value = 1.0·t, 0 violations); C3
confirmed vacuous. Scope (one branch of T5) is correctly stated. The C2 correction (custom halve-p₁ giving
`A ≤ |d₄−d₂| < t`, replacing the false "P/A_P≤d₂/2") is verified.
Verified from scratch off-grid (exact `Fraction`, Σ=31, t=1): the per-case bounds below hold with
**0 violations over 12422 genuine Sub-A-P δ>2t configurations**; the case split is exhaustive and
disjoint; the R12 witness `X={157/5,13,46/5,34/5,23/5}` falls in Case C1.

## Scope (IMPORTANT — this is ONE branch, not all of T5)
Closes only the **Sub-A-P sub-branch** of the m=5 pure hard case in the region **δ > 2t**. It does NOT
prove T5 (m=5 upper bound): the pair1_2 success region — Sub-A-C, Sub-B, and the whole δ ≤ 2t region
(gap G1, ~40k configs, numerics only) — is OPEN, and m ≥ 6 (gap G3, HS-A3) is untouched. The Step tree
is NOT uniform in m.

## Setup
`X = {p₁ > p₂ > p₃ > p₄ > p₅ > 0}` distinct, budget `b = 4`, `Σ = Σpᵢ = 31t`, `t = Σ/31`. Pure hard
case: `p₁ ≤ Σ/2`, `d₁,d₂,d₃,d₄ > t`, `δ := p₅ > t`, where `d₁=p₁−p₂, d₂=p₂−p₃, d₃=p₃−p₄, d₄=p₄−p₅`;
also (I) `p₁ < 16t`, (II) `p₂ < 8t`. Telescoping gives
`Σ = 5δ+4d₄+3d₃+2d₂+d₁ = 31t`, so `d₁ = 31t − 5δ − 4d₄ − 3d₃ − 2d₂`.

**Branch hypotheses:** `δ > 2t`, and the Sub-A-P firing condition on `Y' = {d₁,p₃,p₄,p₅}`:
`D1_{Y'} := d₁ − p₃ ≥ δ + d₄` (equivalently `31t − 6δ − 5d₄ − 4d₃ − 2d₂ ≥ δ + d₄`). This forces `d₁ > p₃`,
so `Y'` is sorted `d₁ > p₃ > p₄ > p₅`.

## Statement
Under the setup, the **pair2_3** cut (cut `p₂` at interior offset `p₃`; the fragment `p₃` pairs with the
spectator `p₃` into a parity-invisible pair, Lemma R1 `sum-bound-reductions.md`) leaves the effective
4-piece instance `Y″ = {p₁, d₂, p₄, δ}` at budget 3, and
```
        min A(Y″, 3) ≤ t,     hence     μ(X, 4) ≤ t.
```

## Toolkit (from Lemma R1 + Lemma M0)
- *Invisible pairing cut:* cutting piece `a` at offset `w` (`0<w<a`) with a spectator `w` present replaces
  `{a,w}` by effective `a−w` and leaves `A` unchanged.
- *2-piece finish:* effective `{u ≥ v > 0}`, one cut ⟹ `A ≤ min(u−v, v)`.
- On sorted `{q₁>q₂>q₃>q₄}`, budget 3: **S** (pair `{q₁,q₂},{q₃,q₄}`) gives `A_S ≤ q₃−q₄`; **R** (pair
  `{q₁,q₄},{q₂,q₃}`) gives `A_R ≤ q₂−q₃`.

## The Σ-P bound [*]
`D1_{Y'} = d₁ − p₃ = 31t − 6δ − 5d₄ − 4d₃ − 2d₂`. The firing condition `D1_{Y'} ≥ δ + d₄` rearranges to
```
        2d₂ ≤ 31t − 7δ − 6d₄ − 4d₃.                              [*]
```

## Ordering of Y″
`p₁ = max(Y″)` (`p₁ > p₄, δ` and `p₁ > d₂` since `d₂ < p₂ < p₁`); `p₄ = δ+d₄ > δ`. The sorted order of
`Y″` depends only on `d₂`. Split on `d₂` (exhaustive and disjoint):

- **Case A (`d₂ ≥ p₄`):** sorted `{p₁,d₂,p₄,δ}`; R gives `A ≤ d₂−p₄`. By [*],
  `d₂−p₄ ≤ (31t−9δ−8d₄−4d₃)/2 < (31t−30t)/2 = t/2` (since `9δ+8d₄+4d₃ > 18t+8t+4t = 30t`). ✓
- **Case B1 (`δ ≤ d₂ < p₄`, `d₂ < δ+t`):** sorted `{p₁,p₄,d₂,δ}`; S gives `A ≤ d₂−δ < t`. ✓
- **Case B2 (`δ ≤ d₂ < p₄`, `d₂ ≥ δ+t`):** sorted `{p₁,p₄,d₂,δ}`; R gives `A ≤ p₄−d₂`. From `d₂ ≥ δ+t`
  and [*], `9δ+6d₄+4d₃ ≤ 29t`, so `6d₄ < 29t−18t−4t = 7t`, `d₄ < 7t/6`; hence
  `p₄−d₂ ≤ d₄−t < t/6 < t`. ✓
- **Case C1 (`δ−t ≤ d₂ < δ`):** sorted `{p₁,p₄,δ,d₂}`; S gives `A ≤ δ−d₂ ≤ t`. ✓ *(R12 witness.)*
- **Case C2 (`d₂ < δ−t`, `δ ≤ 3t`):** `d₂ ∈ (t,2t)` (as `d₂ > t`, `d₂ < δ−t ≤ 2t`); `d₄ ∈ (t,2t)`
  (as `d₄ > t`, and from `d₂ > t` with [*], `6d₄ < 29t−7δ−4d₃ < 11t`). So `|d₄−d₂| < t`. Custom 3-cut:
  halve `p₁` (invisible pair), cut `p₄@δ` (invisible `δ`, leaving effective `{d₄,d₂}`), finish
  ⟹ `A ≤ |d₄−d₂| < t`. ✓
- **Case C3 (`d₂ < δ−t`, `δ > 3t`):** VACUOUS: [*] gives `2d₂ ≤ 31t−7δ−6d₄−4d₃ < 31t−21t−6t−4t = 0`,
  contradicting `d₂ > t`. ✓

Every genuine configuration lands in exactly one nonempty case (A/B1/B2/C1/C2), each closing with
`A ≤ t`. ∎

## Note (recorded correction)
The outliner's Case-C2 closure "P fires, `A_P ≤ d₂/2`" is FALSE: the P construction on `Y″` gives
effective `{p₁−p₄−δ, d₂}` with `p₁−p₄−δ > d₂` always in C2 (`p₁−p₄−δ ≤ d₂ ⟺ δ+2d₄+2d₃ ≤ 0`, impossible),
so `A_P ≰ d₂/2`. The correct closure is the custom halve-`p₁` strategy with bound `|d₄−d₂| < t`.
