# Lemma: side-relations (certified, round 1)

**Statement.** Under the hypotheses of imo-2026-02, set φ = ∠KBA = ∠ACL, u = ∠KAB, v = ∠LAC, and A = ∠BAC, b = CA, c = AB. Then

- (K-side) ℓ_K := b sin²(φ+u) − c[cos A − cos(φ+u)cos(A+φ−u)] = 0,
- (L-side) ℓ_L := c sin²(φ+v) − b[cos A − cos(φ+v)cos(A+φ−v)] = 0.

Equivalent form (used by `secant-trig-identity`, with s = φ+u, t = φ+v, μ = 2φ+A and
N(w) := sin w sin(μ−w) − 2 sin(w−φ) sin(μ−φ−w)):
c·N(s) = b sin²s and b·N(t) = c sin²t. (The two forms agree identically:
sin(φ+u)sin(φ+A−u) − 2 sin u sin(A−u) = cos A − cos(φ+u)cos(A+φ−u), verified symbolically.)

This pair is the complete trig-resolved encoding of all five hypothesis conditions
(interiority + the three angle equalities), after eliminating χ = ∠LCK = ∠BMK and
ψ = ∠LBK = ∠LNC.

**Proof.** Law of Sines in the six nondegenerate triangles ABK, MBK, ACK, ACL, NCL, ABL (all sines positive by interiority), angle additivity ∠ACK = φ+χ, ∠ABL = φ+ψ from the two "inside the angle" hypotheses, and elimination of χ, ψ (branch-pinned parametrization or 2×2 homogeneous determinant). Full details: `approaches/complex-certificate.md`, Parts 0–3; `approaches/secant-trig-identity.md`, Steps 0 and 3.

**Certification.** sorry-free; elimination re-derived by hand by the proof-reviewer, bracket identity verified symbolically, and both relations confirmed to ~1e-15 on five independently constructed valid configurations (`/tmp/round-1/review/endtoend.py`), round 1.
