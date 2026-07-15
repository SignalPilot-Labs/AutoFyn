# Proof review — round 1 — imo-2026-02

Problem: triangle ABC, M, N midpoints of AB, AC; K inside triangle BMC, L inside triangle BNC, K inside ∠LBA, L inside ∠ACK, ∠KBA = ∠ACL, ∠LBK = ∠LNC, ∠LCK = ∠BMK; O circumcentre of AKL; prove OM = ON. `task: proof_only`, `answer_type: none` — both candidates target exactly this claim; no final answer is required.

## How I verified (independent, adversarial)

1. **End-to-end reconstruction from the hypotheses alone** (`/tmp/review/e2e.py`): for 18 triangles (6 chosen incl. obtuse at A, at B, at C; 12 random), I constructed K on the ray forced by ∠KBA = α by root-solving the coupled condition ∠BMK = ∠ACK − ∠ACL directly from coordinates (no use of the builders' parametrization), then L likewise from ∠LNC = ∠LBK. All six angle hypotheses + both triangle interiorities + both angle-interiority conditions confirmed from raw coordinates. Then O computed as the actual circumcentre: **|OM − ON| ≤ 2.3e-15 and |O − T| ≤ 2.4e-15 in all 18 cases**, and the two closed forms of T (fixed-point-t's and quadratic-ideal's X = M + (a/4)(1, cot(A+α))) agree exactly. The theorem is true and the claimed fixed point is the circumcentre.
2. **Exact symbolic re-derivation of every displayed identity** (`/tmp/review/symbolic.py`, sympy, all results identically 0):
   - Lemma 3b chain: both product-to-sum links, the (E) ⟺ (E′) rearrangement, and the cot-substitution identity (P−R)t² + 2Qt − (P+R) = (t²+1)(P cos u + Q sin u − R) at t = cot(u/2).
   - Lemma 3a closed forms of P ± R.
   - fixed-point-t: all four dot products of Lemma 4 (d₁, d₂, d₁′, d₂′), Identity (⋆), (I₃), (I₄), and — the load-bearing step — the **full polynomial identities F(T;t) − m·q_K(t) ≡ 0 and F(T;t) − m′·q_L(t) ≡ 0**, computed from the raw definitions, not from the proof's intermediate steps.
   - quadratic-ideal-certificate: the free-parameter certificate identity Ê(X̂; K̂(t)) − m₀q₀(t) ≡ 0 (symbolic B₀, C₀, α₀, d₀), and the three reflection facts ψ(A) = Â*, ψ(L(s)) = K̂*(s), ψ(X) = X̂*.
   - Parametrization and quadratics validated against the independently constructed configurations: K, L rebuilt from the closed forms reproduce all six hypothesis angles (≤ 2e-15); q_K(τ) = q_L(σ) = 0 (≤ 4e-15).
3. **Line-by-line logical audit** of the non-algebraic steps: Sector Lemma (half-plane cross-product argument — sound, including the normalization case split), Lemma 1 interiority (int(BMC), int(BNC) ⊆ int(ABC) via the barycentric substitution M = (A+B)/2 — checked), the use of "K inside ∠LBA" / "L inside ∠ACK" precisely to fix the orderings θ_L < θ_K < B and π−C < θ′_L < θ′_K (without these the signs of β, γ could flip — both proofs invoke them at exactly the right spot), Law-of-Sines nondegeneracy conditions (all cited from Lemma 1.1/(e)), Lemma 5a / E_K algebra (|x−Z|² − |x−Y|² = −2F, checked by hand), the K ≠ L and ℓ_AK ≠ ℓ_AL arguments, O = T via uniqueness of the line through two distinct points, and quadratic-ideal's Step 4 (∇F = (D, 0), F(x) = D(x_x − O_x), OM = ON ⟺ O_x = x₀ — all checked by hand).

No circularity: both proofs run hypotheses → constraints → identity → conclusion; neither selects roots of the quadratics (the identities are polynomial in t, s, so only q_K(τ) = 0, q_L(σ) = 0 — necessary conditions — are used). Both note explicitly that noncollinearity of A, K, L is granted by the problem's "circumcentre of triangle AKL"; fixed-point-t needs only the existence of O (uses OA = OK = OL) and proves K ≠ L itself; quadratic-ideal uses D ≠ 0 from the same grant. Acceptable — the statement posits the triangle AKL.

---

## Verdict per approach

### fixed-point-t — Verdict: APPROVE — Status: solved
- **Correctness: 10/10.** Every displayed identity re-derived exactly; end-to-end numeric confirmation; all logical steps audited and sound.
- **Completeness / rigor: 10/10.** Fully self-contained: Angle Fact and Sector Lemma proved from scratch; interiority, direction angles, positivity, and the bounds α+β < B, α+γ < C all derived with the hypotheses cited where used; nondegeneracies (K ≠ L, distinct bisectors) proved, not asserted; no "by symmetry" — the L-side coefficient checks are displayed.
- **Progress: full solve** (prior best: outline only).
- Builder's recorded Status `solved` is **correct**. Full proof written into `results/imo-2026-02/current.md`.

### quadratic-ideal-certificate — Verdict: APPROVE — Status: solved
- **Correctness: 10/10.** The load-bearing certificate identity verified symbolically with free parameters; reflection bookkeeping exact; Step 4 reduction algebra checked by hand; shares the (verified) Lemmas 1–3 foundation.
- **Completeness / rigor: 9.5/10.** Complete. Two minor stylistic notes, neither a gap: (a) in Lemma 1(b) the L-side sector test is compressed to "cross-product test as before" — the computation is genuinely one line and displayed in full on the K-side (and in fixed-point-t); (b) D ≠ 0 leans on the problem's grant of triangle AKL, which is legitimate and is flagged honestly in the text.
- **Progress: full solve**, by a genuinely different closing mechanism (affine-functional ideal-membership certificate vs perpendicular-bisector fixed point).
- Builder's recorded Status `solved` is **correct**.

## Lemma certifications
- `lemmas/setup-bookkeeping.md` — **CERTIFIED** (statement matches what is proved; audited + numerically confirmed).
- `lemmas/parametrization.md` — **CERTIFIED** (closed forms reproduce all six hypothesis angles on independent configs).
- `lemmas/constraint-quadratics.md` — **CERTIFIED** (whole Lemma 3b chain re-derived exactly in sympy).
- `lemmas/circumcentre-closed-form.md` — **CREATED + CERTIFIED** (quadratic-ideal's Promotable lemma 4: X = M + (a/4)(1, cot(A+α)) is the circumcentre; certificate identity verified with free parameters).

## Records
- `record_outcome(imo-2026-02, fixed-point-t, round 1, verified-milestone)` — gap closed: none remain; proof complete and verified.
- `record_outcome(imo-2026-02, quadratic-ideal-certificate, round 1, verified-milestone)` — gap closed: certificate exhibited in human-checkable form; proof complete and verified.
- `results/imo-2026-02/current.md` created: **Status = solved**, Full proof recorded (fixed-point-t's text; quadratic-ideal-certificate noted as an independent second proof).

## Goal Progress
**Status: solved** (round 1). Both built approaches APPROVED; `current.md` carries the full proof. Ranking snapshot (Elo pre-update, outcomes recorded this round, stale=true pending outline-reviewer fold): fixed-point-t 1545.8 (verified-milestone), quadratic-ideal-certificate 1515.4 (verified-milestone), concyclic-with-w 1484.8 (not built), power-point-trig 1454.0 (not built). The run's goal is met — no further building is required on this problem.
