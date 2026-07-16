# Lemma (T(ℓ) for all ℓ, and G-INC-1 = Claim(n,0) for all n — mutual strong induction)

**Status:** CERTIFIED (proof-reviewer, round 8). Proposed by `ll-inclusion-gap`. Reviewer independently
re-derived the h=2 arithmetic (`deficit_top = a+b`, `ΣP_lo = 2^{n−2} + ε'`, the A-form conversions, and
the two target inequalities `1+2b+τ ≥ 1−τ`, `1+2a−τ ≥ 1−τ`), verified the four base cases by hand, and
confirmed there is no same-level circularity (each of `Claim(n)`, `T(n)` uses only level-`(n−2)`
statements). Statements verified 0-violation, joint cut budget enforced: `Claim(n,ε)` and `T(n)` for
n = 3 (grid 1/8, 1490 + 2135 configs), n = 4 (grid 1/2, 545 + 452), n = 5 (grid 1/2, 2907 + 1369).

## Definitions
For a finite multiset `P` sorted `p₁ ≥ p₂ ≥ …`, `O_P := p₁ + p₃ + …` (odd-position sum),
`A(P) = 2O_P − ΣP = measure(S_P)`. `G_k = {2^0,…,2^k}`. Depends on the certified lemmas
`forcing-inc-reduction.md`, `parity-condition-inc.md`, `top-band-decomposition.md`,
`set-identity-selfsimilar.md`, `alt-sum-integral.md`.

- **Claim(n,ε)** (`ε ∈ [0,1)`): if `S_Q ⊆ S_{G_{n−1}}`, `|Q| ≤ n+1`, `ΣQ = 2^n + ε`, then
  `O_Q ≤ O_{G_{n−1}} + ε` (equivalently `A(Q) ≤ A(G_{n−1}) − 1 + ε`, i.e. `deficit_top + M ≥ 1 − ε`).
- **T(ℓ)** (`ℓ ≥ 1`): if `S_P ⊆ S_{G_{ℓ−1}}`, `|P| ≤ ℓ+1`, `ΣP ∈ (2^ℓ − 1, 2^ℓ)`, then
  `O_P ≤ O_{G_{ℓ−1}}` (equivalently, with `τ = 2^ℓ − ΣP ∈ (0,1)`, `deficit_top + M ≥ 1 − τ`).

## Result
`Claim(n,ε)` (all `ε ∈ [0,1)`) and `T(n)` hold for all `n ≥ 1`. In particular `G-INC-1 = Claim(n,0)`
holds for all `n`, so in the INC branch with anchor `R = G_{n−1}`,
`A(Q ∪ G_{n−1}) = A(G_{n−1}) − A(Q) ≥ 1`.

## Proof (mutual strong induction on `P(n) := Claim(n,·) ∧ T(n)`, descending `n → n−2`)
**Bases `P(1), P(2)`** (Step 11): `Claim(1,·)`, `Claim(2,·)`, `T(1)`, `T(2)` proved outright — in each,
`S_P ⊆ S_{G_{ℓ−1}}` plus the budget forces an equal pair / a bounded top part, giving the odd-index bound.

**Step `n ≥ 3`.** Apply the ΣP-free top-band decomposition: `h := #{parts ≥ 2^{n−2}}` even,
`A(G_{n−1}) − A(P) = deficit_top + M`, `deficit_top ≥ 0`, `M = A(G_{n−3}) − A(P_lo) ≥ 0`,
`S_{P_lo} ⊆ S_{G_{n−3}}`, `|P_lo| = |P| − h`.
- `Claim(n,ε)`: `h ∈ {0,2,≥4}`. `h=0`: `deficit_top = 2^{n−2} ≥ 1 ≥ 1−ε`. `h≥4`: `ΣP_lo ≤ ε ⟹ A(P_lo)
  ≤ ε ⟹ M ≥ 1−ε`. `h=2`: `deficit_top = a+b`, `ε' = ε+a−b`; 2a (`a+b ≥ 1−ε`) direct; 2b-i (`ε'∈[0,1)`)
  invokes `Claim(n−2,ε')` ⟹ `≥ 1−ε+2b`; 2b-ii (`ε'∈(−1,0)`) invokes `T(n−2)` ⟹ `≥ 1−ε+2a`.
- `T(n)`: `h ≥ 4` IMPOSSIBLE (`ΣP < 2^n`); `h ∈ {0,2}`. `h=0`: `deficit_top = 2^{n−2} ≥ 1 > 1−τ`.
  `h=2`: `deficit_top = a+b`, `ε' = a−b−τ ∈ (−1,1)` (from `a ≥ 0`, `b < 1−τ`); 2a direct; 2b-i
  (`ε'∈[0,1)`) invokes `Claim(n−2,ε')` ⟹ `deficit_top+M ≥ 1+2b+τ ≥ 1−τ`; 2b-ii (`ε'∈(−1,0)`,
  `ΣP_lo ∈ (2^{n−2}−1, 2^{n−2})`) invokes `T(n−2)` ⟹ `≥ 1+2a−τ ≥ 1−τ`.

Both steps reach only level `n−2`; the two residues `n−2 ∈ {1,2}` are the bases. Negative-ε `Claim` is
never invoked (2b-ii always calls `T`). Hence `P(n)` for all `n`. ∎

## Scope (what this does NOT close)
Closes the INC branch of Lemma LL **only for the anchor `R = G_{n−1}`** (`c_R = 0`). The full lower
bound additionally needs: **G-INC-2** (INC with refined `R`, `c_R ≥ 1`; no `G_{n−1}`-band structure) and
**G-GAP** (non-containment `S_Q ⊄ S_R` with `0 < b < 1`). Both remain open.
