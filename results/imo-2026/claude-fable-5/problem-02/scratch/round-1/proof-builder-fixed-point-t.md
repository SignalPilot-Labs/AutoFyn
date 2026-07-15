# Build report — round 1 — fixed-point-t (imo-2026-02)

## Status claimed: solved

Complete rigorous proof written to `results/imo-2026-02/approaches/fixed-point-t.md`. Every step of the outline is closed; no gaps remain in the file.

## What I closed (all five open gaps from the outline, plus reviewer issues 1–5)

1. **Step 1 interiority/orientation (reviewer issue 2).** Closed via two small tools proved from scratch: an **Angle Fact** (angle between unit vectors e^{iθ₁}, e^{iθ₂} is |θ₁−θ₂| when ≤ π) and a **Sector Lemma** (Lemma 0, half-plane/cross-product proof of the polar description of an open convex angle). Interiority int(BMC), int(BNC) ⊆ int(ABC) is a two-line barycentric computation (M = (A+B)/2 substitution). All direction angles, positivity of α, β, γ, and the bounds α+β < B, α+γ < C (hence sin(A+α) > 0, the domain of the cot-substitution) are derived, with the hypotheses "K inside angle LBA" / "L inside angle ACK" cited exactly where the angle additions happen.

2. **Step 3 constraint quadratics.** Full prose derivation, done ONCE with free variables (θ, φ) (Lemma 3b: trig-to-quadratic conversion) and instantiated at (C, γ) and (B, β) — no "by symmetry". Cot-substitution derived from scratch (sin²h = 1/(t²+1)).

3. **Step 4 coefficient computations (reviewer issue 4).** Abstract Lemma 5a (perpendicular-bisector criterion + the three coefficients of F(x;t)), then all three coefficient matches displayed line by line on BOTH sides. The constant-coefficient simplification is isolated as **Identity (⋆)** in a free variable θ, proved in three lines, instantiated at θ = C and θ = B.

4. **Step 6 Claims A and B (reviewer issue 1, the rigor bottleneck) — dissolved by restructuring.** Instead of defining T by two linear equations and proving the CAS-certified Claims A/B afterwards, I define T by its closed form
   T = ( (c cos B)/2 + a/4 , (c sin B)/2 + c sin A cos(A+α)/(4 sin C sin(A+α)) )
   and verify four dot-product identities (Lemma 4): (i) T·u₁ = d₁ and (ii) T·u₂ = d₂ collapse to the **sine addition formula** (one line each); (iii), (iv) reduce to two product-to-sum identities (I₃), (I₄), each proved by a short hand expansion (~10 lines). Claim A becomes a remark (T_x = (2A_x+B_x+C_x)/4 via the projection formula, itself proved in coordinates); Claim B and the whole mirror/reflection step (reviewer issue 3) disappear — the L-side is verified directly in the same coordinates, no orientation-reversing map is ever used.

5. **Step 7 nondegeneracy.** K ≠ L via distinct ray directions from B (β > 0); ℓ_AK ≠ ℓ_AL via the reflection-across-a-common-bisector argument; O = T via "two distinct points determine a unique line".

## Verification performed (reviewer issue 5)

- Fresh numeric harness (own code, `/tmp/verify.py`): 5 triangles × α, root-solved configurations; checked every displayed formula: hypothesis angles reproduced, T closed form vs 2×2 solve, all four dot products, TA=TK=TL, O=T (≤ 5e-15), OM=ON, plus a spurious-root configuration (identity (♣) still holds — no root selection, as the outline-reviewer's report predicted).
- Second harness (`/tmp/recheck.py`): the identities exactly as displayed in the file — (I₃), (I₄), (⋆) with free θ, Lemma 3a, and every intermediate link of the Lemma 3b chain — over 200 random (B, C, α, θ, φ): max residual 7e-15.
- All numeric checks are evidence only; the written proof derives every identity from the addition formulas (PS1–PS3, SP1–SP2 stated and derived in §0).

## Lemma proposals (for reviewer certification into lemmas/)

- `results/imo-2026-02/lemmas/setup-bookkeeping.md` (= §0–§1, Lemmas 0–1)
- `results/imo-2026-02/lemmas/parametrization.md` (= §2, Lemma 2)
- `results/imo-2026-02/lemmas/constraint-quadratics.md` (= §3, Lemmas 3a/3b/3)
These are the shared Steps 1–3 the quadratic-ideal-certificate builder can import; the full proofs live in my approach file (§ references in each lemma file).

## Spec concerns

None. The statement's "circumcentre of triangle AKL" is used only through OA = OK = OL; the proof independently establishes that the two bisectors are distinct lines, so O is forced to equal the explicit point T.

## For the proof-reviewer

The load-bearing chain is: Lemma 1 (direction angles) → Lemma 2 (sine rule ×2) → Lemma 3 (sine rule ×2 + Lemma 3b) → Lemma 4 (four dot products; (I₃)/(I₄) are the only nontrivial expansions) → Lemma 5 (coefficient matching, Identity (⋆)) → O = T → OM = ON. Suggested spot-checks: the sign conventions in Lemma 1.2 (e.g. ray CK at π−C+α+γ), the (I₃)/(I₄) expansions term by term, and the constant-coefficient match in Lemma 5.
