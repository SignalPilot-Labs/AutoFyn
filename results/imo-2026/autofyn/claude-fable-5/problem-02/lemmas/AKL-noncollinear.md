# Lemma: AKL-noncollinear (certified, round 1)

**Statement.** Under the hypotheses of imo-2026-02 (K ∈ int △BMC, L ∈ int △BNC, K inside ∠LBA, L inside ∠ACK, and the three angle equalities), the points A, K, L are not collinear; hence the circumcircle ω and circumcentre O of triangle AKL exist and are unique, and with u = ∠KAB, v = ∠LAC one has sin(A − u − v) ≠ 0.

**Proof.** If A, K, L lay on one ray ℓ from A through int △ABC, the function t ↦ ∠ABX(t) along ℓ is strictly increasing (cot∠ABX = (c/t − cosθ)/sinθ is strictly decreasing in t), and likewise t ↦ ∠ACX(t). Then ∠ABL = φ + ψ > φ = ∠ABK forces t_L > t_K, while ∠ACK = φ + χ > φ = ∠ACL forces t_K > t_L — contradiction. Full details: `approaches/complex-certificate.md`, Part 4.

**Certification.** sorry-free; argument re-checked step by step by the proof-reviewer (round 1).
