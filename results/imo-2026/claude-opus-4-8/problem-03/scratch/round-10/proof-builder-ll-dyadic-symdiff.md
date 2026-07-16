# Build report — ll-dyadic-symdiff (imo-2026-03, Round 10)

**Status: partial** (advanced; not solved). Approach file:
`results/imo-2026-03/approaches/ll-dyadic-symdiff.md`.

## What I built (general-`n` bucket (iii): the base inequality `A(Q∪R) ≥ 1`)
- **Direct containment split** of bucket (iii) (`max(Q), max(R) < 2^{n−1}`) into INC (`S_Q ⊆ S_R`) and GAP
  (`S_Q ⊄ S_R`), on the original `Q,R` — no telescope needed (the certified REFL-telescope is restated as
  an alternative reduction but does not close the residual). Rigorous.
- **INC ⟸ refined-`R` crux (conditional import).** Certified INC-reduction gives `A(Q∪R) = A(R) − A(Q)`,
  so INC ⟺ `A(R) ≥ A(Q)+1` = `Claim_R(n,0)` (h_R even) / `|Q|`-parity (h_R odd). Stated as a clean
  conditional import of `{Claim_R, T_R}` (being built in ll-inclusion-gap this round). NOT claimed closed.
- **NEW promotable Lemma D1 (small-discrepancy kill), all `n`, fully rigorous.** If `|N_Q − N_R| ≤ 1`
  pointwise then `A(Q∪R) ≥ |ΣQ − ΣR|` (= 1 in bucket (iii)). Proof: `{g odd} = {g≠0}` when `|g|≤1`, and
  `measure{g≠0} = ∫|g| ≥ |∫g| = |ΣQ−ΣR|`. This is the first rigorous general-`n` GAP tool that beats the
  recorded "`∫g=1` alone insufficient" obstruction.
- **GAP cheap-kill package K1/K2/D1** closes the overwhelming majority of GAP for every `n`
  (numeric, joint budget enforced): n=3 166/168, n=4 1449/1488; the n=4 residual is 39 configs, ALL with
  `A(Q∪R) ≥ 2` (non-tight, `max|g| ≤ 3`).
- **Opening D framework** made rigorous as a level-charge reduction `A(Q∪R) = Σ_k δ_k`, target
  `Σ_k δ_k ≥ 1`, with (G1) parity, (G2) `∫g=1`, (G3) bounded complexity (`≤ 2n+1` breakpoints over `n`
  levels). Two provable slices (Sub-3a, D1). The general accumulation over even-`|g|` excursions is the
  honest OPEN gap.

## Honest open gaps
- INC sub-instances: conditional on ll-inclusion-gap's `{Claim_R, T_R}` certification.
- GAP residual (small, non-tight, `A ≥ 2` empirically) and the general Opening-D accumulation: OPEN. No
  proof that the dyadic-pairing cost reaches 1.

## Numeric checks (bounded, joint budget `c_Q+c_R ≤ n` enforced)
- n=3 bucket (iii): 168 configs (all GAP), 0 violations; K1/K2/D1 close 166, R9 `n=3` closure the other 2.
- n=4 bucket (iii): 1617 configs (129 INC / 1488 GAP), 0 violations; K1/K2/D1 close 1449 GAP; residual 39,
  all `A ≥ 2`.

## Promotable lemmas (for reviewer certification)
- **Lemma D1 (small-discrepancy kill), all `n`** — new this round, proof in full in the approach file
  (§Opening D). Reusable across both LB routes.

## Spec concerns:
None. (Slug stayed in lane; no `current.md` edit; Status honestly `partial`; INC import flagged
conditional per outline/reviewer; Opening D marked OPEN, not overclaimed; did not re-import the false
`max(Q)<2^{n−1}⟹A≥2`.)
