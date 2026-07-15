# Outline review — round 1 — imo-2026-02

Field of 4 new approaches reviewed. All four target the full claim (OM = ON) end to end — no fragment slugs. I independently re-implemented the displayed formulas (not the outliner's scripts) and re-verified the load-bearing claims; results below.

## Independent verification performed (this review, own code)

1. **Parametrization + quadratics + fixed point:** From ONLY the formulas as displayed in `fixed-point-t.md` (coefficients P, Q, R of q_K; mirror P', Q', R'; K, L parametrizations; d₁, d₂ and the explicit T), I reconstructed the configuration for 4 triangles × several α. Results: OM − ON, O_x − x₀, |T − O|, and Claim A (T_x = (3c cos B + b cos C)/4) all vanish to ≤ 2e-15 at **all four root pairs** of (q_K, q_L).
2. **Forward direction (the one the proof actually needs):** at exactly one root pair per (triangle, α) — the pair with both τ, σ at the larger root — the constructed (K, L) satisfies ALL original hypotheses to 3e-15: ∠KBA = ∠ACL = α, ∠LBK = ∠LNC, ∠LCK = ∠BMK, K in triangle BMC, L in triangle BNC, K inside ∠LBA, L inside ∠ACK. The other three pairs violate interiority (spurious), yet T = O still holds there — confirming fixed-point-t **needs no root-selection argument**, a decisive robustness advantage over concyclic-with-w.
3. **Claim B (T = T'):** verified |T − T'| ≤ 8e-16 with T' = (a − T*_x, T*_y), T* the B↔C-swapped formula, across 4 triangles.

Shared-line risk (outliner's own flag): Steps 1–3 are common to all four slugs, but they are elementary sine-rule derivations that I re-verified independently, and power-point-trig's Steps 1–2 do not even use them. Not a single-line trap; the finishing mechanisms are genuinely disjoint (fixed point / ideal certificate / concyclicity / trig identity).

---

## fixed-point-t — verdict: APPROVE

The skeleton is logically sound: hypotheses ⟹ parametrization (Step 2, sine rule in BMK/CNL) ⟹ q_K(τ) = 0, q_L(σ) = 0 (Step 3, equate the two sine-rule expressions for BK, resp. CL) ⟹ E(T; τ) ≡ m·q_K(τ) puts T on the perp bisector of AK (Step 4) ⟹ mirror for AL (Step 5) ⟹ O = T (Step 7, two distinct lines) ⟹ OM = ON via Claim A. T is defined independently of τ, σ — no circularity. m := e₂/(P−R) is well-defined since P − R = sin C sin α sin(A+α) ≠ 0 (needs α > 0 and A + α < π, both available). Nondegeneracy in Step 7 (K ≠ L from β > 0; distinct bisectors via reflection argument) is correct.

Issues for the builder (fixable while building — none fatal):
1. **Step 6 is the rigor bottleneck.** CAS-certified is NOT acceptable under the rigor rules — Claims A and B must be expanded by hand (product-to-sum) in the prose. Budget real effort here; if the raw expansion is ugly, factor through intermediate identities (e.g. first prove T·u₂-form of Claim A in the (α, B, C) variables).
2. **Step 1 must pin down the domain of the cot-substitution:** justify 0 < α + γ < π (K inside triangle ABC puts ray CK strictly inside ∠ACB, so α + γ = ∠ACK < C < π) and α > 0 (K strictly inside BMC is off line AB, so ∠KBA > 0), β > 0, γ > 0 similarly. These feed P − R ≠ 0 and the τ = cot(α+γ) validity.
3. **Step 5 mirror:** write the reflection x ↦ a − x argument explicitly — it is orientation-reversing, so state precisely how each angle hypothesis maps to its mirror; do not just say "by symmetry".
4. **Step 4:** the two coefficient computations (e₁(T) = 2Qm ⟺ T·u₁ = d₁; e₀(T) = −(P+R)m ⟺ T·u₂ = d₂) must be displayed line by line; the two sub-simplifications quoted in the file are correct (I checked them symbolically-by-hand feasible) but must appear in the prose.
5. Numerically re-verify every displayed formula while writing (the file's own warning about e^{i(B−α)} sign conventions is apt).

## quadratic-ideal-certificate — verdict: APPROVE (with changes noted)

Technique sound: Δ = 0 ⟺ consistency of the 3-equation linear system given A, K, L non-collinear (granted by "circumcentre of triangle AKL" in the statement) is a correct reduction, and ideal membership Δ ∈ (q_K, q_L) is forced by vanishing at all four root pairs plus bidegree (2,2) (generic argument — but the final proof must display the certificate, not the genericity argument).

Issues:
1. **Notational slip in Step 5 / the skeleton:** the cofactor H cannot be a function of σ only. Division of Δ by q_K in τ leaves remainder r₁(σ)τ + r₀(σ); each rᵢ must then be divisible by q_L(σ), giving Δ = G(τ,σ)·q_K(τ) + (h₁(σ)τ + h₀(σ))·q_L(σ) — so H = H(τ, σ) of τ-degree ≤ 1. Fix the display accordingly.
2. The rigor rules bar "CAS says remainder is 0". The certificate must be displayed in human-verifiable form. Strongly prefer the exponential variables (z = e^{iB}, w = e^{iC}, ζ = e^{iα}) so the division is exact Laurent-polynomial arithmetic, then organize the write-up by factored sub-identities. If the cofactors do not compress to something a reviewer can check by expansion, this approach stalls at CHANGES REQUESTED forever — that is its known risk.
3. Coordinate with the fixed-point-t builder on the shared Steps 1–3: whoever finishes first files them under `lemmas/` (Parametrization Lemma, Constraint Lemma) with full proofs; the other imports.

## concyclic-with-w — verdict: CHANGES REQUESTED (hold — live, not in build set)

The Reformulation Lemma (Step 1) is correct and complete modulo prose — worth certifying in `lemmas/` at low cost, since it gives every approach the clean target "A, K, L, W concyclic". But the finish has two genuinely unproven pieces: (a) the B↔C symmetry of the eliminant Φ (mechanical but unchecked), and (b) root selection (Step 4), whose continuity mechanism needs discriminant-nonvanishing on the whole α-interval — currently pure conjecture. My verification above shows fixed-point-t proves the SAME reformulated statement with NO root selection, so this slug's only value is a shorter synthetic proof. Do not build it this round; it stays live. If a future round builds it, Step 4(b) (spurious root violates a sign/range constraint) looks more promising than 4(a).

## power-point-trig — verdict: CHANGES REQUESTED (hold — live, not in build set)

Steps 1–4 are correct (midpoint power formula is the standard median-length identity; the product-to-sum reduction to (♦) is exact) and the reduction target (♦) is clean and mirror-symmetric. But Step 5 has **no verified mechanism** — the file itself says so — and the file's own warning (λ = γ, μ = β are false) shows the naive closing fails. Not buildable yet; not a dead end either (the (♦) target is a genuine intermediate an explorer could attack). Also note the outstanding Step 2/3 configuration facts (position of X, arc sides) — if built later, prefer directed lengths/angles throughout.

---

## Selection

Registered all four (all survive; none is junk): fixed-point-t, quadratic-ideal-certificate, concyclic-with-w, power-point-trig. No copies (no approach has two viable fills of one gap yet — concyclic-with-w's Step 4(a)/(b) fork is not worth branching while the whole slug is on hold).

Ranking applied (update_ranking, 6 comparisons, full round-robin — all approaches are round-1 cold starts, ordered by evidence: verified-mechanism coverage of the remaining gaps):
- fixed-point-t 1545.8 — every step has a verified mechanism; no root selection needed (verified at all four root pairs); only prose gaps.
- quadratic-ideal-certificate 1515.4 — certificate existence verified at 40 digits; gap is exact human-checkable display (heavy, mechanical).
- concyclic-with-w 1484.8 — elegant reformulation proven; resultant symmetry + root selection unproven.
- power-point-trig 1454.0 — correct reduction to (♦), but the closing step has no mechanism at all.

Build priorities: the two builders should treat certification of the shared Parametrization + Constraint Lemmas into `lemmas/` as the round's first deliverable (outliner is right that these are the only shared failure point), then diverge on their finishes.

build set: fixed-point-t, quadratic-ideal-certificate
