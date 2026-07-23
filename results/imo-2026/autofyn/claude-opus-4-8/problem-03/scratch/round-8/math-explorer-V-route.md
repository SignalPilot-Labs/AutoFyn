## imo-2026-03 — Route to Statement (V)

**Context.** Statement (V): the function f(b) = min_{≤q-1 cuts} A(b) attains its maximum over the compact polytope K_q at a VERTEX of K_q. If (V) holds, then VertexFace gives f ≤ 1/D everywhere on K_q, closing IH(q). (V) is the sole open gap in the upper-vertex-reduction approach.

---

- Distinct openings:

  1. **1-homogeneity route (NEW, VIABLE — primary recommendation).** f is 1-homogeneous: f(λb) = λ·f(b) for λ > 0. Proof: scaling all pieces by λ scales every cut position by λ, scales A by λ, so min_strategy A(λb) = λ·min_strategy A(b). Consequence: for any interior point b with Σb_i < (2^q-1)/D, the σ-face rescaling b' = b·S/Σb_i has f(b') = (S/Σb_i)·f(b) > f(b). So the max of f over K_q is strictly on the σ-face {Σb_i = (2^q-1)/D}. This reduces (V) to: "max_{σ-face ∩ K_q} f ≤ 1/D," which avoids needing (V) proper (no vertex claim needed). On the σ-face:
     - B1-large (b_1 > 2^{q-1}/D): IH-reducible (halving branch) applies → IH(q-1) on σ-face of K_{q-1}. ✓ certified
     - b_2 > 2^{q-2}/D: IH-reducible (cut-at-b_2 branch) applies → 1-2b_2 < (2^{q-1}-1)/D. ✓ certified
     - Flat residual on σ-face (b_1 ≤ 2^{q-1}/D AND b_2 ≤ 2^{q-2}/D): q=4 closed by IH4-flat (certified); q≥5 open.
     
     The 1-homogeneity observation completely avoids the "PL marginal" trap and vertex-claim — it converts (V) into a direct bound on the σ-face. No continuity or convexity assumption needed.

  2. **Generalized IH-flat strategy for q≥5 flat residual.** The certified IH4-flat lemma uses: halve b_1 (pair cancel), cut b_2 at b_3 (pair cancel), cut b_4 into (b_4-δ, δ) — three singletons remain. Bounds: b_2 < 4/D and b_3+b_4 > 3/D give A < 1/D. For q=5 (D=31), flat residual on σ-face: b_1 ≤ 16/31, b_2 ≤ 8/31, Σ = 1. Attempt: halve b_1, cut b_2 at b_3, then cut b_3 at b_4 (another pair cancel), leaving singletons b_4 (one remaining), b_5. This uses 4 cuts out of 4 allowed (q-1=4). Key bound: b_2 < 8/31, b_3+b_4+b_5 > (31-16-8)/31 = 7/31 > ... need to check if the surviving singleton sum < 1/31. This is the OPEN subproblem. Worth attempting: the IH4-flat proof technique (cascade of pair-cancels leaving singletons, then sum bound) may generalize directly for q=5.

  3. **Direct attack via σ-face extreme-point theorem (alternative to 1-homogeneity).** The σ-face ∩ K_q is itself a compact polytope. Its extreme points (vertices of σ-face ∩ K_q) are either (a) vertices of K_q that happen to lie on σ-face, or (b) edge intersections with σ. Any vertex of σ-face ∩ K_q is a vertex of K_q OR has one MORE active constraint beyond σ (i.e., lies on a gap-face or bottom-face of K_q). The VertexFace-style argument then applies directly to extreme points of σ-face ∩ K_q — no need to prove max at vertex of K_q, just at extreme point of σ-face. This is equivalent to 1-homogeneity but has a different proof flavor.

  4. **Induction on q via σ-face.** (V) holds for q=2 trivially (K_2 is 1D segment, max at endpoints = vertices). Assuming IH(q-1): on σ-face, IH-reducible reduces non-flat-residual to IH(q-1), done. Flat residual needs separate treatment (IH4-flat, IH5-flat,...). This is the natural IH structure; the key gap is proving IH-flat for general q.

- Candidate technique(s): 1-homogeneity (scaling argument) + reduction to σ-face + IH-flat cascade construction. The IH-flat cascade generalizes the IH4-flat proof — alternating pair-cancel cuts on (b_1 halved at b_2, b_2 cut at b_3, b_3 cut at b_4, ...) leaving singletons whose sum is bounded by the flat-residual constraints.

- Cheap-kill candidates: 1-homogeneity is nearly free (one line argument) and converts (V) to a direct σ-face bound — try this first. If accepted, the only remaining gap is the q≥5 flat residual on σ-face.

- Knowledge-base entries to use: Berge Maximum Theorem (already used in f-continuous-attained); Extreme-point theorem (linear function on convex polytope attains max at vertex — but f is not linear, so this doesn't apply directly to f); standard convex-polytope vertex characterization (used in VertexFace proof structure).

- Analogous past problems (cruxes): Not consulted this round (1-homogeneity is the key new structural fact; crux corpus less relevant here).

- Prior progress: §A (setup), §B (IH-reducible certified), §C (VertexFace certified), §D (f-continuous-attained certified), IH4-flat certified. Upper bound approach is 90%+ complete; only q≥5 flat residual on σ-face remains.

- Dead ends (do not retry):
  - Interior-descent route: f is NOT monotone along the path from interior to geometric vertex; went down then up. Ruled out numerically (q=4 tested).
  - Quasi-convexity of f on σ-face: violated; found 47/100 pairs with f(midpoint) > max(f(endpoints)) in q=4 numerical test.
  - Concavity of f on σ-face: violated (27/100 violations in q=4 numerical test, some real).
  - Marginal-PL principle: forbidden per run_state.md; f demonstrably non-affine on interior segments (values 0.10→0.27→0.12 in q=5 test from approach file).
  - IH+(m) dual-bound (carry sum AND max): refuted by fixed-point obstruction, forbidden per run_state.md.

- Small-case / intuition notes (conjecture, not proved):
  - For q=3,4,5: numerical tests show all interior points of K_q have f << 1/D = 1/(2^{q+1}-1), while the geometric vertex b_k = 2^{q-k}/D achieves f = 1/D exactly. No interior point found with f > f(geometric vertex). Supports (V) being TRUE.
  - 1-homogeneity is proved (one-line argument — not a conjecture). The σ-face reduction is clean and correct.
  - The flat residual on σ-face for q=5 has the structure: b_1 ≤ 16/31, b_2 ≤ 8/31, gaps ≥ 1/31, Σ=1. Three pair-cancel cuts + one singleton cut might suffice for 4 total (q-1=4 allowed). This requires a direct check analogous to IH4-flat.
  - Conjecture: the IH4-flat proof technique (cascade pair-cancels leaving small singletons, then sum bound) generalizes to all q via induction on the flat-residual structure.
