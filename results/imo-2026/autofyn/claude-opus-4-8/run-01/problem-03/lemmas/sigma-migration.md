# Lemma σ-migration — max of f migrates onto the σ-face (certified round 8)

**Setup.** D = 2^{n+1}−1, q ≥ 2, S := (2^q−1)/D. The hard-regime polytope
K_q = {b : b_1 ≥ … ≥ b_q, b_i − b_{i+1} ≥ 1/D, b_q ≥ 1/D, Σ b_i ≤ S}. f(b) = min over ≤ q−1 XY cuts of
A (Lemma X). f is continuous on the compact K_q with min attained (Lemma f-continuous-attained), and
1-homogeneous on the positive cone (Lemma f-homogeneous). The σ-face is Φ := {b ∈ K_q : Σ b_i = S}.

**Statement.** **max_{K_q} f = max_Φ f.** Consequently IH(q) ⟺ (f ≤ 1/D on K_q) ⟺ (f ≤ 1/D on Φ).

**Proof.** Φ ⊆ K_q gives max_Φ f ≤ max_{K_q} f. Conversely take b ∈ K_q with s := Σ b_i ≤ S. If s = S,
b ∈ Φ. If s < S set c := S/s > 1 and b' := c·b. Then:
- ordering preserved (c > 0);
- gaps: b'_i − b'_{i+1} = c(b_i − b_{i+1}) ≥ c/D > 1/D ✓;
- floor: b'_q = c·b_q ≥ c/D > 1/D ✓;
- sum: Σ b'_i = c·s = S ✓.
So b' ∈ Φ. Since b_q ≥ 1/D > 0, b is in the positive cone; by f-homogeneous f(b') = c·f(b). As
A = μ(·) ≥ 0 gives f ≥ 0 and c > 1, f(b') = c f(b) ≥ f(b). Every K_q point is thus weakly f-dominated
by a Φ point; taking suprema (attained, §f-continuous-attained), max_{K_q} f ≤ max_Φ f. ∎

**Consequence.** Replaces the round-7 open statement (V): reduces IH(q) to bounding f on the σ-face,
using NO vertex-attainment, NO piecewise-linearity, NO convexity — only 1-homogeneity + monotone
rescaling. Derived from f-homogeneous + f-continuous-attained (both certified).
