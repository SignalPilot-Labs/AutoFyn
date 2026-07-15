# Build report — quadratic-ideal-certificate — round 1

## Status claimed: solved

File: `results/imo-2026-02/approaches/quadratic-ideal-certificate.md` (complete rewrite; Full proof section present).

## What was closed (all outline gaps)

1. **Steps 1–3 (shared foundations)** — written in full, self-contained:
   - Lemma 1 (position bookkeeping): rigorous interiority arguments via half-plane/cross-product tests with direction angles; all positivity facts (α, β, γ > 0, α+β < B, α+γ < C) and all four ray directions derived, including the two angle additions licensed by "K inside ∠LBA" / "L inside ∠ACK".
   - Lemma 2 (parametrization): sine rule in BMK / CNL, K(τ), L(σ) closed forms.
   - Lemma 3 (constraints): stated as a FORMAL one-variable lemma (product-to-sum + half-angle substitution, full computation displayed) applied twice — no "by a similar argument"; Corollaries 3.1/3.2 give q_K(τ) = 0, q_L(σ) = 0.
2. **Step 4 (reduction)** — simplified: instead of the 3×3 determinant, OM = ON ⟺ F(X) = 0 where F(x) = E_K(x)(A−L)_y − E_L(x)(A−K)_y is affine with gradient (D, 0), D = (A−K)×(A−L) ≠ 0 (non-collinearity granted by the problem's "triangle AKL"). A one-line Remark shows F((x₀,h)) equals the outlined determinant Δ, so this IS the promised certificate target.
3. **Step 5 (the certificate — the main gap)** — fully closed in human-checkable form. Key discovery while building: the certificate point is simply **X = M + (a/4)(1, cot(A+α))**, and then the whole certificate reduces to ONE formal identity (Lemma 5: Ê(X̂; K̂(t)) ≡ m₀q₀(t)), proved by three displayed coefficient computations, each 2–5 lines of angle-addition/product-to-sum. The L-side is obtained by applying the formal lemma with B↔C swapped and pulling back through the reflection isometry ψ(x,y) = (a−x, y) (all three point-matching checks displayed; uses only the projection formula a = b cos C + c cos B and b sin C = c sin B, both derived in one line from the law of sines).
   Final displayed cofactors: **G(t,s) = m_K·(A−L(s))_y** (degree 1 in s), **H(t,s) = −m_L·(A−K(t))_y** (degree 1 in t) — cofactor notation fixed per the outline-reviewer's condition (H depends on τ; no σ-only slip).
4. **Step 6** — conclusion assembled; no cases needed (uniform algebra; τ = 0 / σ = 0 harmless since everything is polynomial identities).

## Verification performed (per the "re-verify each displayed formula" warning)
- 40-digit mpmath check of EVERY displayed formula on 4 triangles (generic, C > B, isosceles, obtuse A), at a root pair for which all six original hypothesis conditions + both interiorities were confirmed (< 1e-40): q_K(τ) = q_L(σ) = 0, X·u₁ = d₁, X·u₂ = d₂, both certificate identities at random t, s, F(x) = D(x_x − O_x), O_x = x₀, OM = ON.
- Exact sympy check: all six polynomial coefficients of E(X;K(t)) − m_K q_K(t) and E(X;L(s)) − m_L q_L(s) are identically 0 in (α, B, C, d). The prose proof stands independently of both checks (noted in the file).

## Notes for the proof-reviewer / other builders
- **Importable by fixed-point-t:** the point X = M + (a/4)(1, cot(A+α)) is exactly their T in closed form; Lemma 5 hand-proves their Step 4, Claim A becomes true by construction (X_x = x₀), Claim B is the manifest B↔C symmetry of X_y via c sin B = b sin C. Listed under Promotable lemmas (items 1–4) in my file.
- I did NOT write files into `lemmas/` to avoid a collision with the fixed-point-t builder running in parallel; all four promotable lemmas are fully proved inside my approach file with exact locations given, ready for reviewer certification.
- Spec concern: none. `answer_type` is none (proof_only) — no final answer to state.
