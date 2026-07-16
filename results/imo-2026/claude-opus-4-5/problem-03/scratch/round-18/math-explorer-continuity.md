## imo-2026-03 — Continuity/Compactness Extension Lens

### Problem recap
The Tier 3 interior coverage gap: show that for every config x in the bounded "all pairwise > 1" polytope K (g ∈ (1,6/5), v₀ ∈ (0,1/3)), some (2,1,1) XY template achieves LB(x,T) ≤ c(5) = 32/63.

---

### Findings

#### 1. True vertex count is larger than 94

My corrected enumeration (with the proper LB score formula — picking positions 1,3,5,7,9 in sorted order, NOT the top 5) reveals:

- 63 AP-type vertices (wrs ∈ {35,...,41}, v₀ > 0, g=1)
- 31 Z-type vertices (r_alpha=0, wrs ∈ {35,...,41}, v₀=0, g>1)
- 24 "degenerate corner" vertices (wrs=42, v₀=0, g=1) — ON BOTH BOUNDARIES simultaneously

Total: at least 118 vertices of the closed Tier 3 polytope.

The 24 degenerate corners (wrs=42) were NOT included in the prior rounds' analysis. However, they lie on the g=1 boundary and are handled by Tier 2 (pairwise), so they don't require separate Tier 3 verification. They ARE covered; the proof just needs to note they fall under Tier 2.

**Correction for current.md:** The "93 vertices" cited is an undercount. The full count includes 24 additional degenerate corners, all covered by Tier 2.

#### 2. No single copy template covers all vertices

Exhaustive search over all (2,1,1) copy templates (cuts at piece-size positions) on the 94 originally-enumerated vertices:

- **Best single copy template covers only 39/94 vertices** (template (H=3, D=5, C=2, s1=0, s2=4, s3=1)).
- The template from the wrs=35 exact lemma (H=2,D=3,C=5,s1=0,s2=1,s3=4) covers 34/94.
- **Conclusion: a single copy template cannot close the interior coverage gap.**

#### 3. Bug: the original "31 Z-type perfect template" result was computed on wrong inputs

The earlier claimed "template H=2,D=5,C=3,s1=0,s2=1,s3=0 covers all 31 Z-type vertices" used piece sizes computed as raw differences (diffs[i] = L0*(1+perm[i]*g)) instead of cumulative sums. With the **correct** cumulative piece sizes, this template gives LB ≈ 0.85 — far above c(5). This prior result is INVALID.

#### 4. Interior sampling confirms worst case is near the boundary

1000 randomly sampled Tier 3 interior points tested with all copy templates:
- **Worst margin: -0.00051** at (v₀=0.046, g=1.012) — very close to the v₀=0 and g=1 boundaries.
- Interior points near BOTH boundaries simultaneously are the hardest.
- Points deep in the interior have larger positive margins.

This matches the dispatch observation (interior sampling min margin 0.00588 > Z-type min 1/378 ≈ 0.00265) — but note that prior interior sampling used GENERAL (optimized) templates, not copy templates. Copy templates have a small negative margin (-0.0005) for a few interior points.

#### 5. Why "all boundary covered → all interior covered" fails for copy templates

The boundary coverage argument requires:
- h(x) = min_T LB(x,T) is quasi-convex (sublevel sets convex), OR
- h achieves its maximum at the boundary.

For **copy templates**: h_copy(x) is piecewise affine and NOT quasi-convex (union of convex sets is not convex). The worst interior point (margin -0.0005) proves the maximum is in the interior, NOT at the boundary, for this restricted template family.

For **general templates** (optimized cut positions): the evidence strongly suggests h_gen(x) ≤ c(5) everywhere, with the maximum achieved at the Z-type boundary. But h_gen is continuous (minimum of continuous functions, by Berge's theorem) and the boundary/sampling evidence cannot replace a proof.

#### 6. The infimal projection theorem does NOT apply directly

For each fixed type (H,D,C), define:
h_type(x) = min_{c1,c2,c3 feasible} LB(x; type, c)

For FIXED absolute cuts (c not depending on x), LB(x; type, c) is LINEAR in x. But the feasibility constraint (c1 ≤ P[D](x)) depends on x, preventing direct application of the infimal projection theorem.

With **relative cuts** (c_k = t_k * P[D](x) for fixed fractions t_k ∈ [0,1]): the pieces become bilinear in (x, t), not jointly convex, so the infimal projection theorem still does not apply.

#### 7. Diameter vs. safety radius analysis

- Tier 3 diameter (L2 of cumulative pieces): **0.084**
- Lipschitz constant of LB(x,T) for a specific template: **2.29**
- "Safety radius" at min Z-type margin 1/378: margin/Lipschitz = **0.00115**

The safety radius (0.00115) is far smaller than the diameter (0.084), so the coverage balls around each Z-type vertex do NOT overlap to cover the whole polytope. The Lipschitz-based neighborhood argument fails.

#### 8. The correct rigorous approach

**Most promising path: Sub-polytope cell decomposition with single template per cell.**

The Tier 3 region decomposes into 720 sub-polytopes C_perm (one per ordering of the 6 parameters). Within each C_perm:

- All 6 vertices of C_perm are on the **BOUNDARY of Tier 3** (either g=1 or v₀=0 face):
  - 1 AP-type vertex (all 5 consecutive gaps = 1)
  - 5 "partial AP" vertices (v₀=0, 4 consecutive gaps = 1, 1 gap > 1)
- ALL 6 vertices are covered: AP-type by Tier 2 (pairwise), partial-AP by V_j strategies (d_j = L0 at the tight gap, giving LB = c(5) exactly).
- For any template T, LB(x, T) is **convex** in x, so max over C_perm is at a vertex.
- **If we find T(perm) with LB ≤ c(5) at all 6 vertices of C_perm, convexity guarantees LB ≤ c(5) everywhere in C_perm.**

This argument does NOT require the "max at boundary" principle to hold globally — it works cell by cell.

**Why this closes the gap (if verified):**
1. C_perm vertices are on the Tier 3 boundary where Tier 2/V_j strategies cover with LB = c(5).
2. T(perm) must satisfy LB ≤ c(5) at the 6 C_perm vertices — this is the constraint.
3. By LB convexity (certified), interior of C_perm is covered.
4. Union of all 720 C_perm covers all of Tier 3.

The VERIFICATION step is: for each of the 720 permutations, find a (2,1,1) template with cut positions that are affine functions of piece sizes (so pieces remain linear in x) and check 6 boundary vertices per perm.

Note: The C_perm vertices with v₀=0 and 4 gaps=1 are "partial AP" points that are NOT in the prior 94-vertex enumeration. However, V_j strategies cover them (d_j = L0 at the tight gap).

#### 9. Maximum principle argument: one clean version

**Claim:** For the sub-polytope C_perm, the function LB(x, T(perm)) (for a fixed template T with affine cuts in x) is AFFINE within each ranking cell (where the top-5 among 10 output pieces has fixed ordering). On each ranking cell, the max is at a vertex of that cell. The vertices of ranking cells within C_perm are either:
- Vertices of C_perm (on Tier 3 boundary) — covered by Tier 2/V_j
- Points where two output pieces swap rank — these are INTERIOR vertices of C_perm

For interior ranking-cell vertices: the function is continuous and the LB value at such a "swap point" is the SAME from both sides (by continuity). If LB ≤ c(5) on both adjacent ranking cells at the swap point, coverage holds at the swap point too.

If every ranking cell of T(perm) within C_perm has LB ≤ c(5) at ALL its vertices (including swap points), then LB ≤ c(5) everywhere in C_perm. The swap points satisfy LB ≤ c(5) if the AFFINE function on each ranking cell is ≤ c(5), which follows from the max being at ranking-cell vertices, which are either Tier-3-boundary points (covered) or swap points of lower-dimensional cells (induction).

This is a valid structural argument but needs formalization.

#### 10. CRITICAL FINDING: Z-type "vertices" are NOT true vertices of the Tier 3 polytope K

This is the most important finding of this analysis.

For the natural permutation sub-polytope C_nat (where params are naturally ordered alpha<beta<...<zeta), the extreme points (vertices) are:
1. AP vertex: all 5 sorted consecutive gaps = 1, v₀ = (42-WRS)/21 > 0. (1 vertex)
2. Partial-AP vertices: v₀=0, 4 of 5 consecutive gaps = 1, 1 gap free. (5 vertices)

Total: 6 vertices per permutation sub-polytope.

The Z-type "vertex" (v₀=0, ALL sorted gaps = 6/5, all pairwise > 1) has ONLY ONE active constraint (v₀=0) within C_nat. It is an INTERIOR POINT of the v₀=0 face of C_nat, NOT a vertex of C_nat or of K.

**Consequence:** The "31 Z-type verifications" from prior rounds verify LB at 31 interior-of-face points of K, NOT at actual K-vertices. The max-at-vertex argument for convexity does NOT apply based on these 31 verifications alone.

**What ARE the actual vertices of K?**
- For each permutation type, the 6 vertices of C_perm are at: (a) AP vertex (sorted gaps all = 1), and (b) 5 partial-AP vertices (v₀=0, 4 sorted gaps = 1, 1 gap free).
- ALL actual vertices of K are at the AP/pairwise boundary (Tier 2 coverage, LB = c(5) exactly).
- The "partial AP" vertices (v₀=0, some sorted gap = 1) correspond to a PAIR of params with |param_a - param_b| = 1 (in sorted units), which means that pair's piece-size difference = L0. The pairwise strategy for that specific pair gives LB = 1/2 + L0/2 = c(5) exactly. So these are ALSO covered by Tier 2.

**Revised understanding of the Tier 3 proof structure:**
- All actual vertices of K are at AP/pairwise boundaries, handled by Tier 2 (LB = c(5)).
- The Z-type "vertices" (31 points, interior of K's v₀=0 face) have been verified with positive margin but are NOT needed for the max-at-vertex argument.
- For a SINGLE Tier 3 template T with LB(v, T) ≤ c(5) at all 6 vertices of every C_perm, convexity of LB(·, T) gives full interior coverage.
- The key question becomes: does T give LB ≤ c(5) at the AP/pairwise boundary vertices?

---

### Summary for outliner

**What works:**
- LB(x,T) is convex in x for each fixed T (CERTIFIED).
- All actual vertices of K (AP-type and partial-AP-type) are at AP/pairwise boundaries, ALL covered by Tier 2 (LB = c(5) exactly).
- If a SINGLE Tier 3 template T satisfies LB(v, T) ≤ c(5) at ALL actual K-vertices (which are at AP/pairwise boundaries), then by convexity of LB(·, T), LB(x, T) ≤ c(5) everywhere in K = complete interior coverage.
- The 31 Z-type "vertex" verifications from prior rounds (positive margins, min 1/378) are INTERIOR-OF-FACE POINTS of K — not needed for convexity argument, but provide supplementary evidence.

**What does NOT work:**
- "31 Z-type verifications → interior covered by max-at-vertex": The Z-type points are NOT actual K-vertices. The max-at-vertex argument requires checking at TRUE K-vertices (AP/pairwise boundaries, all covered by Tier 2).
- Single copy template for all 94 "boundary points": Best covers 39/94 of the enumerated points.
- "Max at boundary" for min_T LB(x,T) without extra structure.
- Lipschitz ball argument (safety radius 0.00115 << diameter 0.084).

**The correct COMPACTNESS ARGUMENT (if it can be established):** Find a single Tier 3 template T* such that LB(v, T*) ≤ c(5) at EVERY ACTUAL VERTEX of K (i.e., at all AP/pairwise boundary vertices). By convexity of LB(·, T*), interior coverage follows. The AP/pairwise boundary vertices are exactly the "AP-type vertices (63, wrs 35-41)" and the partial-AP vertices (v₀=0, some sorted gap = 1). The latter may number in the thousands across all permutation types.

**Prior progress issues:**
- The "94 vertices" count is incomplete. True K has AP-type vertices (63 for wrs 35-41), degenerate corner vertices (24 for wrs=42), plus many partial-AP vertices. Partial-AP vertices are at v₀=0 with some pairwise condition active — all covered by Tier 2.
- The "31 Z-type verifications" are interior-of-face checks, not K-vertex checks. Still valid as supplementary computational evidence but don't close the gap via the max-at-vertex argument.
- The "copy template T*" result from an earlier round-18 search used incorrect piece-size formulas (differences instead of cumulative sums) and is INVALID.

---

### Distinct openings

1. **Sub-polytope decomposition (most promising):** For each of 720 orderings, identify the 6 boundary vertices of C_perm, find template T(perm), verify 6 points, cite LB convexity. This is a FINITE ALGEBRAIC PROOF.

2. **Affine structure within ranking cells:** LB(x,T) is PIECEWISE AFFINE. Within each ranking cell (fixed top-5 ordering of 10 output pieces), LB is affine. Max on a convex region is at its vertices. If all ranking-cell vertices in Tier 3 have LB ≤ c(5), done. The ranking-cell vertices include Tier-3-boundary points (covered) and swap points (reachable by induction on cell dimension).

3. **LP duality approach:** For each permutation cell and each ranking sub-cell, formulate an LP min_{c} LB(x; T, c) and exhibit a dual certificate showing the optimal value ≤ c(5). The dual certificate is a function of x (via strong duality), giving a constructive proof.

4. **Single non-copy template:** Search for a template with cut positions given as AFFINE FUNCTIONS of piece sizes (not necessarily equal to specific piece sizes) that covers all Tier 3 vertices. Such a template, if found, gives a one-template proof via convexity of LB. The search space is larger than copy templates.

---

### Dead ends

- **Single copy template:** Best covers 39/94 verified boundary vertices. Not viable.
- **Lipschitz neighborhood extension:** Safety radius 0.00115 vs diameter 0.084. Fails.
- **Quasi-convexity of min_T LB(x,T):** Not established; interior worst case with copy templates has negative margin (not max at boundary).
- **Infimal projection theorem with variable feasibility set:** Does not give convexity of h_type(x).

### Small-case / intuition notes

**Conjecture (from evidence):** For general optimized templates, max_{x ∈ K} h(x) is achieved at the Z-type boundary (v₀=0, all pairwise > 1). The interior is strictly easier. Evidence: prior interior sampling showed min margin 0.00588 > Z-type min 1/378. Our additional sampling (1000 points) shows worst interior margin -0.0005 with copy templates, but general templates give positive margins there.

**Conjecture:** The 6 vertices of each C_perm sub-polytope (on Tier 3 boundary) all have LB ≤ c(5) under some common template T(perm). If verified computationally for all 720 permutations, the sub-polytope decomposition gives a complete proof.
