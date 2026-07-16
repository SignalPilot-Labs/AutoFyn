## imo-2026-03 — Convex Covering Geometry Lens

### Lens
Investigate whether a finite collection of convex coverage sets C_T can cover the entire Tier 3 polytope, using the certified LB(x,T) convexity lemma.

---

### Key structural finding: 63 non-empty sector simplices, each with 6 vertices

The Tier 3 closure decomposes into exactly **63 non-empty permutation sectors** (the permutations sigma with WRS = 6*r_alpha + 5*r_beta + ... + r_zeta in {35,...,41}). This confirms the LP feasibility explorer's count.

Each sector sigma gives a **5-simplex** (6-vertex convex polytope) in the 5D Tier 3 space. Verified computationally: all 63 sectors give exactly 6 simplex vertices (378 total).

**Vertex structure per sector:**
- 1 **AP-type vertex**: g=1 (all consecutive sorted gaps exactly 1), v_0 > 0. Located on the Tier 2 (pairwise) boundary.
- 5 **Z-type simplex vertices**: v_0 = 0 (smallest sorted param = 0), one large gap > 1, four gaps = 1. Located on the Tier 1 boundary.

**ALL 378 simplex vertices are at Tier 1/2 boundaries** (proved):
- 63 AP-type vertices: at the g=1 pairwise boundary (all 5 adjacent sorted pairs have diff = 1), covered by Tier 2 pairwise strategies (LB = c(5) exactly).
- 315 Z-type simplex vertices: at the v_0=0 boundary (smallest sorted param = 0):
  - If smallest sorted param is alpha (P_1 = L_0): Halve-All covers (LB = c(5) exactly). **155 such vertices.**
  - If smallest sorted param is beta, gamma, etc. (some d_j = L_0): V_j strategy covers (LB = c(5) exactly). **160 such vertices.**
  - All 315 covered, 0 uncovered.

**Computational verification:** for each of 315 Z-type vertices across all 63 sectors, either Halve-All or some V_j gives LB = c(5) exactly. No failures.

---

### Key finding: the "31 Z-type all-equal-gap vertices" are interior-of-face points, NOT sector simplex vertices

The 31 Z-type all-equal-gap vertices cited in n5-lp-direct.md (v_0=0, all sorted gaps equal to 42/WRS > 1) are NOT simplex vertices of any sector. They are INTERIOR-OF-FACE points at the intersection of the v_0=0 face with the Tier 3 interior (all sorted consecutive gaps > 1, specifically all equal). These points DO have positive margin (min 1/2520 in n5-lp-direct), but:

1. Since they're NOT true Tier 3 polytope vertices, the max-at-vertex argument cannot use them to close the interior gap.
2. They ARE covered by Halve-All (LB = c(5) exactly at v_0=0 boundary), as Case A lemma already handles P_1 = L_0.

**Correction for current.md:** The relevant simplex vertices for the convex covering argument are the 63 AP-type + 315 Z-type simplex vertices (378 total), NOT the 93 cited in Round 16/17 (62 AP + 31 Z-type all-equal-gap). The 93 set is a different (partial) enumeration.

---

### Convex covering argument: when it works

For each non-empty sector sigma, if there exists a (2,1,1) template T_sigma (with cut positions linear in piece sizes) such that:
- LB(v, T_sigma) ≤ c(5) for all 6 simplex vertices v of Sector_sigma

Then by the certified LB Convexity Lemma (Round 17): C_{T_sigma} = {x: LB(x,T_sigma) ≤ c(5)} is convex, and since it contains all 6 vertices of a simplex, it contains the entire simplex. Union over all 63 sectors covers all of Tier 3.

**This is a FINITE algebraic proof: 63 sectors × 6 vertices per sector = 378 vertex checks.**

---

### Status of copy template coverage per sector

Exhaustive search over all (2,1,1) copy templates (cut positions equal to specific piece sizes):

- **32 of 63 sectors**: single copy template covers all 6 simplex vertices (min margin ≥ 0). Proof for these sectors is complete.
- **31 of 63 sectors**: NO single copy template covers all 6 vertices (best margin negative, ranging from -0.0185 to -0.0026).

**Mixed template test** (LP feasibility explorer's "mixed equal-split" family: cut D at pieces[i] then equal-split remainder, cut C at pieces[j]):
- Combined copy + mixed: **52 of 63 sectors** covered.
- **11 sectors remain** where neither copy nor mixed template covers all 6 vertices simultaneously.

The worst-case sector: sigma=(0,1,2,3,4,5) (identity permutation, WRS=35), best copy margin = -0.0185.

---

### Why no single copy template covers the identity sector

The identity sector's AP-type vertex (alpha=1/3, all params equally spaced by 4/3) needs LB ≤ c(5). The (2,1,1) copy template creates two singletons {s1, s2} from the AP-type config. The coverage condition |s1-s2| ≤ L_0 is tight (with P_1 large relative to L_0 at this vertex).

Meanwhile, the 5 Z-type simplex vertices (alpha=0) are extremely easy to cover. But the optimal template for the AP-type vertex (minimizing LB there) is NOT optimal for Z-type vertices, and vice versa. The gap is structural: the AP-type vertex has P_1 = 4L_0/3 >> L_0, while Z-type have P_1 = L_0.

---

### Correct proof strategy: sub-cell decomposition (from continuity explorer)

The continuity explorer's finding is the correct geometric insight: use **permutation CELLS** (720 total, 63 non-degenerate in Tier 3), NOT the 63 sector simplices.

Each permutation cell C_perm has 6 vertices:
- 1 AP-type vertex (g=1, all consecutive sorted gaps = 1)
- 5 partial-AP vertices (v_0=0, exactly 4 consecutive sorted gaps = 1, 1 gap free)

**Critical difference**: In a permutation CELL C_perm, the partial-AP vertices (my "Z-type simplex vertices") have NOT JUST v_0=0 but ALSO some consecutive sorted gap = 1, meaning the PAIRWISE STRATEGY for that specific adjacent sorted pair covers them with LB = c(5) exactly. All 6 vertices of each C_perm are at PAIRWISE boundaries (both AP-type and partial-AP), all covered by Tier 2.

The AP-type vertex of C_perm: all 5 consecutive sorted gaps = 1 → ANY adjacent pair's pairwise strategy covers it.
The partial-AP vertex (gap m = 1): sorted gaps are 1,1,1,1,g_free,1 or similar → the adjacent pair at the "equal" gap gives diff = 1 → pairwise covers.

**Key: within a single permutation cell C_perm, the LP feasibility explorer can find a SINGLE (2,1,1) template that covers all 6 vertices** (all at pairwise boundaries), and the LP explorer claims this for all 63 non-empty cells.

---

### Distinct openings for outliner

1. **Sector simplex / convex covering (32/63 immediate + 31 need richer templates):** For 32 sectors, single copy template covers all 6 simplex vertices → convexity → done. For remaining 31, need either (a) richer linear-cut template family, or (b) finer sub-cell decomposition.

2. **Sub-cell decomposition (from continuity explorer):** Decompose each sector into sub-cells (permutation cells where all 6 vertices are at pairwise boundaries). For each sub-cell, find a (2,1,1) template covering all 6 vertices. This is the LP feasibility explorer's approach.

3. **Halve-All handles the Z-face completely, Pairwise handles the AP-face**: The Tier 3 interior is enclosed between the v_0=0 face (covered by Halve-All = Case A) and the g=1 face (covered by Pairwise = Tier 2). An interpolation argument: any path from a Z-type simplex vertex to the AP-type vertex within a sector passes through the interior. If a single template T_path covers BOTH endpoints (LB ≤ c(5) at both endpoints), then by convexity of LB(·, T_path), it covers the entire path. For the 32 sectors with a good copy template, this is proved. The remaining 31 sectors need this interpolation.

4. **Fix for the 11 hard sectors**: Use a general LP to find affine-cut template covering all 6 vertices of the hard sector simplices. The LP has 3 continuous variables (c1/P_D, c2/P_D, c3/P_C fractions) and is separately solvable per sector vertex. The question is feasibility (whether a simultaneous cover exists).

---

- **Candidate technique(s):** Finite sector simplex decomposition (63 sectors) + LB convexity lemma + per-sector single template verification. For 32 sectors, copy templates suffice. For 31 more, need richer affine-cut template family (LP optimizer).

- **Cheap-kill candidates:** The 32 sectors with copy template coverage are immediately closed by convexity. For the 11 hardest sectors (where even mixed templates fail), check if the sub-cell decomposition (LP explorer's approach) applies — the sub-cells have all vertices at pairwise boundaries, which might admit a better single template.

- **Knowledge-base entries to use:**
  - "LB(x,T) Convexity (n=5)" (CERTIFIED Round 17): sublevel sets C_T are convex.
  - "Halve-All Strategy Lemma" (Case A, CERTIFIED): covers v_0=0 face (LB = c(5) exactly).
  - "n=5 Pigeonhole FAILS" (from run_state.md): confirms Tier 3 bounded region exists with 63 non-empty sectors.
  - "Singleton-Pair Formula" (CERTIFIED): LB = (1 + |s1-s2|) / 2 for 4-pair + 2-singleton structures.

- **Analogous past problems (cruxes):** None identified — this is a custom geometric coverage argument for a specific parametric polytope.

- **Prior progress:** Tier 1 (Halve-All, V_j) and Tier 2 (Pairwise, 10 non-adjacent pairs) certified. LB Convexity certified (Round 17). 31 Z-type all-equal-gap vertex checks complete (min margin 1/2520). Interior computationally verified (66/66). Now have: 63 non-empty sectors, 378 simplex vertices ALL at Tier 1/2 boundaries, 32/63 sectors with single copy template proof.

- **Dead ends (do not retry):**
  - "Single copy template for all 94 boundary points": best covers 39/94. Infeasible.
  - "Halve-All alone covers all Z-type simplex vertices": FALSE for 160/315 (those have alpha > 0, covered by V_j instead).
  - "31 Z-type all-equal-gap verifications give max-at-vertex proof": they are interior-of-face points, NOT K-vertices. Max-at-vertex fails.
  - "Single copy template per sector covers all 6 simplex vertices": fails for 31/63 sectors (best margin -0.0185).
  - "Mixed equal-split templates fix all remaining sectors": fails for 11/63 sectors.
  - Lipschitz ball argument (safety radius 0.00115 << diameter 0.084, from continuity explorer).

- **Small-case / intuition notes:**
  - CONJECTURE: For the 11 hard sectors (including identity sector WRS=35), there exists a (2,1,1) template with affine (but non-copy, non-mixed) cut positions that covers all 6 simplex vertices. Evidence: the AP-type vertex needs |s1-s2| ≤ L_0 (tight constraint), and Z-type vertices need the same but have much more slack. A CONTINUOUS template family interpolating between the Tier 2 construction (at AP vertex) and the Z-face construction should exist.
  - CONJECTURE: The LP feasibility explorer's claimed 63-template coverage is correct but uses a richer template family than "copy" + "mixed equal-split." Their computation should be independently verified with the correct `get_pieces` formula.
  - The sector simplex approach gives a GEOMETRIC PICTURE cleaner than the "63 permutation cells" approach: 63 sectors, 6 vertices each, all vertices at Tier 1/2 boundaries. A single template per sector closes the entire interior via convexity.
