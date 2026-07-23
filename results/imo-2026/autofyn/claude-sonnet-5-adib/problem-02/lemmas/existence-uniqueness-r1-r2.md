# Lemma: Existence and uniqueness of (r1(θ), r2(θ)) for every θ ∈ (0, min(β,γ))

**Certified round 3** (proof-reviewer independently re-derived and numerically
stress-tested every load-bearing step below from scratch, including at the
round-2 counterexample configuration (p,q)=(0.0025,5.0); no gap found).

**Source:** `approaches/coordinate-trig-bash.md`, round 3 (Lemmas 8, 8′, 9,
10, 10′, 12, 12′ and the closing Theorem).

## Setup (imported unchanged)

Frame `B=(-1,0), C=(1,0), A=(p,q)` (q>0). `φ_B=∠ABC=β`, `φ_C` s.t.
`γ=π−φ_C`, `α=π−β−γ`. For `θ∈(0,min(β,γ))`:
```
K = B + r1·(cos(φ_B−θ), sin(φ_B−θ)),  r1>0
L = C + r2·(cos(φ_C+θ), sin(φ_C+θ)),  r2>0
```
`F1(θ,r2):=∠LBK−∠LNC` (depends only on (θ,r2), Decoupling Lemma),
`F2(θ,r1):=∠LCK−∠BMK` (depends only on (θ,r1)).

## Statement

For every `θ ∈ (0, min(β,γ))`:

1. **Sign-flip points** (Lemma 8/8′): the closed forms
   `r2_signflip(θ) = 2sin(φ_B−θ)/sin(α+2θ)`,
   `r1_signflip(θ) = 2sin(φ_C+θ)/sin(α+2θ)`
   are well-defined, unique, and strictly positive.
2. **Corrected domain** (Lemma 9): on `r2 ∈ (0, r2*(θ))` where
   `r2*(θ):=min(r2max(θ), r2_signflip(θ))` (and symmetrically for r1*(θ)),
   `F1` is strictly decreasing (resp. `F2` on `(0,r1*(θ))`), with **no**
   unproven "sign convention" assumption — it follows automatically from
   monotonicity of the Sweep-Lemma polar angle plus the definition of the
   sign-flip point.
3. **Case dichotomy** (Lemma 10/10′): `r2_signflip(θ)≤r2max(θ) ⟺ θ≥δ`
   (`δ:=∠ABN`), and mirror with `δ':=∠ACM`.
4. **Unconditional endpoint sign** (Lemma 12/12′):
   `lim_{r2→r2*(θ)⁻} F1(θ,r2) < 0` and `lim_{r1→r1*(θ)⁻} F2(θ,r1) < 0`,
   in BOTH branches of the dichotomy (case (b): exact value `−θ−∠A`,
   unconditionally negative since `θ>0,∠A>0`; case (a): reduces to
   "`∠LNC>0` (resp. `∠BMK>0`) for all r2>0 (resp. r1>0)", proved by "two
   distinct lines through a common point meet only there").
5. **Theorem:** combined with the known left-endpoint values
   `F1(θ,0⁺)=β−θ>0`, `F2(θ,0⁺)=γ−θ>0`, the Intermediate Value Theorem plus
   strict monotonicity (point 2) gives a **unique** `r2(θ)∈(0,r2*(θ))` with
   `F1(θ,r2(θ))=0` and a **unique** `r1(θ)∈(0,r1*(θ))` with
   `F2(θ,r1(θ))=0`, for every `θ∈(0,min(β,γ))`.

## Reviewer verification

Independently re-derived Lemma 8's cross-product computation and
positivity argument from scratch; matched the builder's closed form exactly
via direct numerical cross-checking (own script, 5 triangle shapes ×
8 θ values). Independently verified the case-dichotomy claim (Lemma 10)
numerically in all tested cases (dichotomy predicted vs. actual r2_signflip
vs r2max ordering matched in every trial, including the shape
(-0.6,1.2) where θ<δ for the entire tested range). Independently verified,
by direct fine-grained scan of F1 on the corrected domain `(0,r2*(θ))`, that
strict monotonicity NOW holds (no sign flips), including at the exact
configuration/θ-range that broke round 2's uncorrected claim
((p,q)=(0.0025,5.0), θ up to 70°) — confirming the domain correction, not
just the restated monotonicity claim, is what fixes the round-2 error.
Independently verified Lemma 12's case-(b) closed form
`F1(θ,r2max⁻) = −θ−∠A` matches direct computation to displayed precision
in 5 configurations.

## What this does NOT establish

This lemma gives existence/uniqueness of the parameter pair `(r1(θ),r2(θ))`
satisfying the angle hypotheses for each θ. It does **not** determine
`O_x(θ)` (the circumcenter of `AKL`'s x-coordinate) or show `O_x(θ)=p/2` —
that final substitution remains open (see `current.md`).
