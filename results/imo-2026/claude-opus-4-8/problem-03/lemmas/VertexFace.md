# Lemma VertexFace — vertices of K_q lie on a gap/bottom face (certified round 7)

**Setup.** Case-B hard regime, q = n+1 pieces, D = 2^{n+1}−1. Define the compact polytope
    K_q = { b ∈ ℝ^q : b_i − b_{i+1} ≥ 1/D (1 ≤ i ≤ q−1), b_q ≥ 1/D, Σ_i b_i ≤ (2^q−1)/D }.
For b ∈ K_q let f(b) = min over all XY strategies using ≤ q−1 cuts of A(final multiset)
(A via Lemma X). IH(q) ⟺ f ≤ 1/D on K_q.

**Statement.** Every vertex v (0-dimensional face) of K_q satisfies either b_q(v) = 1/D, or
b_i(v) − b_{i+1}(v) = 1/D for some i. Consequently **f(v) ≤ 1/D at every vertex v of K_q.**

**Proof.** K_q ⊂ ℝ^q is cut out by q+1 affine constraints: the q−1 gap constraints (g_i), the
bottom constraint (β): b_q ≥ 1/D, and the sum constraint (σ): Σ b_i ≤ (2^q−1)/D. K_q is
q-dimensional (nonempty relative interior: gaps slightly above 1/D, sum below the bound). A vertex
in ℝ^q has ≥ q linearly independent active constraints, hence at most one of the q+1 constraints is
inactive at v. If neither any (g_i) nor (β) were active, the only possible active constraint would
be (σ) — at most 1 active, but 1 < q for q ≥ 2, contradicting ≥ q active. So some (g_i) is active
(a gap = 1/D) or (β) is active (b_q = 1/D).

At such a vertex all pieces are positive and strictly decreasing (b_q ≥ 1/D > 0, gaps ≥ 1/D > 0),
a valid p = n+1 config for XY's q−1 = n cuts.

- **Gap-face** (some gap = 1/D): the minimum consecutive gap d* ≤ 1/D. By **Reduction 2**
  (certified, `CaseB-reductions.md`): XY cuts the larger piece of the minimal-gap pair at the
  smaller (XOR-cancelling the intact smaller piece) and halves the other q−2 pieces, using q−1 cuts;
  the surviving XOR is [0, d*], so A = d* ≤ 1/D. Hence f(v) ≤ 1/D.
- **Bottom-face** (b_q = 1/D): the smallest piece a_p = b_q = 1/D. By **Lemma H** (certified,
  `H-halve-largest.md`): XY halves the q−1 largest pieces and spares a_p, giving O = 1/2 + a_p/2 and
  A = a_p = 1/D. Hence f(v) ≤ 1/D.

In both cases f(v) ≤ 1/D. ∎

**Machine check (reviewer, round 7).** Exact-rational vertex enumeration of K_q for q = 2,3,4,5:
every feasible vertex (3,4,5,6 respectively) lies on a gap-face or bottom-face; 0 off-face.

**Certification.** Reviewer-verified round 7. Pure polytope combinatorics + two certified imports
(Reduction 2, Lemma H); no PL assumption, no numerics in the load-bearing steps. Statement is a
closed conditional-free fact. Admitted to shared cache.

**Scope / caveat.** This bounds f only at the VERTICES of K_q. Concluding max_{K_q} f ≤ 1/D (i.e.
IH(q)) requires the SEPARATE statement (V): f attains its max on K_q at a vertex — equivalently f
piecewise-linear. (V) is NOT part of this lemma and remains OPEN: the marginal-PL principle fails
without joint convexity, and A = min-over-strategies is non-convex. Do not read IH(q) out of this
lemma.
