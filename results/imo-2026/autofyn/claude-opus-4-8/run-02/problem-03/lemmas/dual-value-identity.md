# Lemma DUAL (dual value identity) — CERTIFIED round 6

Source: `dual-integer-certificate` §1. Basic linear algebra; reviewer verified.

## Statement
Let `U ∈ ℤ^{(n+1)×p}` have full column rank (`ker U = {0}`), let `w ∈ ℝ^p` satisfy `Uw = b`, and
let `s ∈ ℝ^p`. Then:
1. `Uᵀλ = s` is solvable over `ℚ`;
2. for **every** solution `λ`, `λᵀb` is the same number, equal to `sᵀw`;
3. hence any block-formula functional `f = sᵀw` with `Uw=b` equals `Σ_k λ_k b_k`.

## Proof
(1) `ker U={0}` ⇒ `rank Uᵀ = p` ⇒ `Uᵀ:ℝ^{n+1}→ℝ^p` surjective ⇒ `Uᵀλ=s` solvable for every `s`
(rationally when `U,s` integer/rational).
(2) `λᵀb = λᵀ(Uw) = (Uᵀλ)ᵀw = sᵀw`, independent of `λ` (two solutions differ by `δ∈ker Uᵀ`, and
`δᵀb=δᵀUw=(Uᵀδ)ᵀw=0`; equivalently `b=Uw∈col U=(ker Uᵀ)^⊥`).
(3) Write out `λᵀb=Σ_k λ_k b_k`. ∎

## Verification (reviewer, independent)
- On the Gap-D config `{2,4/3,4/3,4/3,1}` (`U=[[0,0,1],[1,0,0],[0,3,0]]`, `b=(1,2,4)`, `s=(1,-1,1)`,
  `w=(2,4/3,1)`): `λ=(1,1,-1/3)`, `λᵀb = 5/3 = sᵀw = f`. Identity holds.
- Random full-column-rank integer `U` (`5×3`), two distinct solutions `λ0,λ1` (differ by `ker Uᵀ`):
  `λ0ᵀb = λ1ᵀb = sᵀw` in all trials. Value-independence confirmed.

## Use
Reads the alternating sum `f` off the incidence system `(U,s,b)`. Unconditional (no minimizer
hypothesis needed). Does NOT by itself give integrality — that needs an INTEGER `λ`, which requires
`s ∈ Uᵀℤ^{n+1}` (Gap D), a separate lattice condition.
