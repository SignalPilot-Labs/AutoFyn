## imo-2026-02 (Spiral Similarity / Homothety lens)

- **Distinct openings:**

  **Opening A — Direct complex algebraic manipulation (most promising).**
  The three conditions translate into clean complex-form constraints:
  - C1: arg(s) = -φ, arg(t) = +φ (with K = sA, L = 1 + t(A-1)), so s·t = r_s·r_t ∈ ℝ+ trivially.
  - C2: K·(N−L)/(L·(A−1)) ∈ ℝ. Equivalently K·(1/2−t)/L ∈ ℝ (value ≈ 0.168 for test case).
  - C3: A·(C−K)/((C−L)·(K−M)) ∈ ℝ (value ≈ −5.28 for test case).
  The Key Lemma (A, K, L, A' concyclic) is equivalent to p(q−d)/(q(p−d)) ∈ ℝ where p = A−K, q = A−L, d = Re(A)−1/2 ∈ ℝ. With p = (1−s)·A, q = (A−1)·(1−t), p−d = A'−K, q−d = A'−L. The outliner should build an approach that derives this real-valuedness by DIRECTLY COMBINING C2 and C3 algebraically. The "product" C2·C3 = −0.888 (real, verified). The gap is showing how the two real-valued constraints force a third specific ratio to also be real.

  **Opening B — New cyclic trapezoid geometry.**
  A, A', M, N are ALWAYS concyclic (numerically verified: CR imaginary part < 3·10⁻¹⁷). They form a cyclic isosceles trapezoid: AA' ∥ MN (both horizontal), |AM| = |A'N| = |AB|/2. This fixed circle γ = circ(A, A', M, N) satisfies angle(MAN) = angle(MA'N) exactly. The Key Lemma says circumcircle(AKL) also passes through A'. Both circles pass through A; for both to pass through A', their radical axis must be line AA' (horizontal). This forces the circumcenter O to lie on the perpendicular bisector of AA' = perpendicular bisector of MN — but this is circular restating. Instead: the cyclic trapezoid is a KNOWN, FIXED circle on which A and A' both lie. The outliner could try to show that the circumcircle of AKL intersects γ precisely in A and A' using the angle conditions and the known geometry of γ.

  **Opening C — Inversion centered at K (or L).**
  Invert in a circle centered at K. The circumcircle of AKL becomes the line through images A*, L* of A and L. The condition A' ∈ circumcircle(AKL) becomes A' on line A*L*, i.e., A, A', L map collinearly under this inversion. The angle conditions C2, C3 might transform to circle-through-specified-points conditions under this inversion. This approach bypasses the cross-ratio algebra.

  **Opening D — Trigonometric elimination (computational).**
  BK = (AB/2)·sin(ν)/sin(φ+ν) and CL = (AC/2)·sin(μ)/sin(φ+μ) are already proven. The Key Algebraic Identity (★) is:
  |A−L|²·Im(A−K) − |A−K|²·Im(A−L) = (Re(A)−1/2)·Im((A−K)·conj(A−L)).
  Substituting explicit coordinates for K and L (from the Law of Sines and angle conditions) should make (★) a verifiable trigonometric identity. No spiral needed; brute-force trig suffices. This is unappealing but closes the gap.

- **Candidate technique(s):** Direct complex number algebra (combining two "real-imaginary-part-zero" conditions to produce a third). Possibly the cyclic isosceles trapezoid A,A',M,N as an intermediate structure. No spiral similarity is viable.

- **Cheap-kill candidates:** None that apply here; the problem requires a non-trivial argument. However: the observation that s·t ∈ ℝ+ is "free" from C1 and should be used explicitly in any algebraic proof.

- **Knowledge-base entries to use:** Inscribed angle theorem (for A, K, L, A' concyclic ↔ angle equality at A and A'), spiral similarity (knowledge_base.md mentions it but it's not viable here), Law of Sines (already proven in existing approaches), cross-ratio / Ptolemy for concyclicity.

- **Analogous past problems (cruxes):** None — geometry is not in the crux corpus.

- **Prior progress:**
  - Key Reduction proven: A' on circumcircle(AKL) ⟹ OM = ON.
  - Key Lemma numerically verified to < 10⁻¹⁴: the angle conditions force A' onto circumcircle(AKL).
  - All three existing approaches (directed-angle-concyclic, power-of-point, complex-coords) stall at the same gap: proving the Key Lemma analytically.
  - Key Algebraic Identity (new, equivalent to Key Lemma): |A−L|²·Im(A−K) − |A−K|²·Im(A−L) = (Re(A)−1/2)·Im((A−K)·conj(A−L)), verified to 2·10⁻¹² across all configs.

- **Dead ends (do not retry):**
  - **Naive spiral similarity σ_L (B→N, K→C)**: Confirmed geometrically false. |σ_L(K) − C| ≈ 0.703 in the test case. The Round 1 rejection stands.
  - **rho(K) on circumcircle claim**: The earlier session claim that "rho(K) and rho(L) lie on circumcircle(AKL)" is WRONG. Numerically: |O − rho(K)| = 2.317 while R = 0.780. Do not pursue this.
  - **Homothety h_A (ratio 1/2) for the Key Lemma**: Maps B→M, C→N. Since C2 involves (B,N) and C3 involves (C,M), the CROSS-pairing means h_A does not send the C2 picture to the C3 picture. Does not directly help the Key Lemma.
  - **B,K,L,N concyclic interpretation of C2**: WRONG. CR(B,K;L,N) ≈ 1.024 + 0.641i (not real). C2 is NOT the concyclicity of B,K,L,N. Similarly C3 is NOT concyclicity of C,K,L,M.

- **Small-case / intuition notes (all labeled as conjecture):**
  - **FACT (proved):** A, A', M, N are always concyclic: they form a cyclic isosceles trapezoid. |AM| = |A'N| = |AB|/2 exactly. AA' ∥ MN (both horizontal). The circumcircle of this trapezoid is centered at x = (2a+1)/4 (the axis of symmetry = perp bisector of MN = perp bisector of AA'). The angles subtended at A and A' by chord MN are equal: angle(MAN) = angle(MA'N) ≈ 27.82° in the test case.
  - **FACT (verified numerically):** s·t ∈ ℝ+ for every valid configuration. This follows from C1 alone: s = r_s·e^{−iφ}, t = r_t·e^{+iφ}, so s·t = r_s·r_t > 0. No mystery here — this is automatic.
  - **CONJECTURE (numerically verified, not proved):** The conditions C2 and C3 in complex form are: C2: K·(N−L)/(L·(A−1)) ∈ ℝ and C3: A·(C−K)/((C−L)·(K−M)) ∈ ℝ. Their product is real (≈ −0.888). BOTH are needed: C2 alone does not imply OM = ON (numerically: there is a second root for r_t satisfying the complex C2 condition that gives |r_t ≈ 0.965| but places L outside triangle BNC and makes angle(LBK) ≠ angle(LNC) geometrically; so C2 alone does not determine K, L uniquely up to the valid constraint).
  - **CONJECTURE:** The Key Lemma should be provable by the following route: express p = A−K = (1−s)A and q = A−L = (A−1)(1−t), write p−d = A'−K and q−d = A'−L (where d = Re(A)−1/2), and show the cross-ratio p(q−d)/(q(p−d)) is real using C2 and C3. The two "real" conditions from C2 and C3 each kill one degree of freedom in Im[...], and together they should force the Key Lemma's Im[...] = 0. The algebraic path is not yet clear.
