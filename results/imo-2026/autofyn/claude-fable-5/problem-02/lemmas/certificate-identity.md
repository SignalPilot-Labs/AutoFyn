# Lemma: certificate-identity (certified, round 1)

**Statement (unconditional trig identity in six free real variables u, v, φ, A, b, c).**
With P_u = cos A − cos(φ+u)cos(A+φ−u), Q_u = sin²(φ+u), P_v, Q_v analogous,
ℓ_K = bQ_u − cP_u, ℓ_L = cQ_v − bP_v, and

G = c sinφ sin(φ+v)[c sin(A−v) + b sin v] − b sinφ sin(φ+u)[c sin u + b sin(A−u)]
    − ½(c²−b²) sin(A−u−v) sin(φ+u) sin(φ+v),

one has identically
2 sin A · G = α ℓ_K + β ℓ_L, where
α = −[b(sin²φ + sin²v) + c sin(φ+v) sin(A−φ−v)],
β =  c(sin²φ + sin²u) + b sin(φ+u) sin(A−φ−u).

**Companion identity (KI, four free real variables s, t, φ, μ).** With
N(w) = sin w sin(μ−w) − 2 sin(w−φ) sin(μ−φ−w),
U = sin t[sin(μ−s−t) sin t − 2 sinφ sin(μ−φ−s)],
V = sin s[2 sinφ sin(μ−φ−t) − sin(μ−s−t) sin s],
W = 2 sinφ[sin t sin(t−φ) − sin s sin(s−φ)] sin s sin t:

N(s)U + N(t)V + W = sin(s−t)[N(s)N(t) − sin²s sin²t].

**Proof.** Certificate: coefficient match in b², bc, c², each a product-to-sum Fourier-table cancellation (`approaches/complex-certificate.md`, Part 6). KI: frequency analysis (odd frequencies ≤ 3 in s) + evaluation at s ∈ {t, 0, φ, μ−φ} + Factor Theorem + density/continuity (`approaches/secant-trig-identity.md`, Step 6).

**Certification.** Both identities verified fully symbolically by the proof-reviewer (sympy exp-rewrite, `/tmp/round-1/review/check_identities.py`, `check_cert_sym.py`), and every displayed Fourier-table row verified individually (`check_tables.py`), round 1.
