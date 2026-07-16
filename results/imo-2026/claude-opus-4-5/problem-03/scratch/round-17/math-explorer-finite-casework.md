# Math Explorer Report: Finite Casework Sufficiency (Lens: Direct Finite Casework)

## imo-2026-03 — Filling the interior coverage gap in Tier 3

---

### The gap (confirmed)

The reviewer correctly identified: the claim "max of piecewise linear function on compact polytope is at a vertex" is FALSE for f = min_T LB_T, because the min of convex functions is neither convex nor concave in general. The reviewer's counterexample f(x) = min(1, 2-x) on [0,2] has its max at the interior point x=1. This blocks the current proof.

---

### KEY STRUCTURAL DISCOVERY: LB(x,T) IS CONVEX in x

**Verified computationally (100/100 tests, no violations).**

For a fixed template T, the 10 output pieces are LINEAR functions of the 6 input pieces (P1,...,P6). LB = sum of 5 largest of those 10 linear functions = sum of the k largest of n linear functions. This equals max_{|S|=5} (sum_{i in S} piece_i(x)), which is a maximum of linear functions, hence **CONVEX in x**.

This is the key structural property the current proof is missing.

**Consequence:** For any fixed template T, the set C_T = {x in P: LB(x,T) <= c(5)} is a CONVEX POLYTOPE (sublevel set of a convex function). And the maximum of LB(x,T) over any compact convex region is attained at a **vertex** of that region.

---

### Critical realization: AP-type vertices (62) are covered by Tier 2, NOT Tier 3

**Verified exactly:** The one vertex our 360-template search "failed" on — perm=(1,2,0,3,5,4), wrs=39, v0=1/7, g=1 — is an AP-type vertex with min pairwise diff = 1. Tier 2 (pairwise strategy) covers it with LB = c(5) = 32/63 **exactly**:

```
Tier 2 strategy for (alpha, gamma) pair with diff = 1:
Cut P3 at P2, halve P4, P5, P6 (4 marks total).
LB = 1/2 + |P1 - d2|/2 = 1/2 + L0/2 = 32/63 = c(5). ✓
```

**All 62 AP-type vertices (g=1, some pairwise diff = 1) are handled by Tier 2 pairwise strategies.** They lie on the BOUNDARY of the Tier 3 region, not in its interior. The current proof incorrectly tries to verify them with (2,2,1) strategies.

The 31 Z-type vertices (v0=0, r_alpha=0) are the ONLY vertices genuinely requiring Tier 3. All pairwise diffs > 1 at Z-type vertices → Tier 2 does not apply.

---

### Discrete strategy enumeration: 360 templates, convex feasibility sets

A "(2,2,1)" discrete template specifies: one piece H to halve, one piece D for 2 cuts (creating sub-pieces matching singletons S1 and S2), one piece C for 1 cut (creating sub-piece matching singleton S3). The remaining 3 pieces are singletons. Total: 6 * 5 * C(4,2) * 2 = **360 templates**.

For each template, the 10 output pieces are determined. Within each **sorting region** (where the sorted order of the 10 pieces is fixed), LB is LINEAR. The feasibility set {x: LB(x,T) <= c(5)} within each sorting region is a **half-space**. The reviewer's formulation is exactly correct: finitely many half-spaces whose union should cover the polytope.

**Algebraic identity r=t:** For template (H=P3, D=P4, S1=P1, S2=P2, S3=P5, C=P6) applied to permutation (0,1,2,3,4,5) in the AP sub-region:

r = P4 - P1 - P2 = (1 - alpha + gamma + delta)*L0  
t = P6 - P5 = (1 + zeta)*L0  

On the WS=42 hyperplane with equal gaps (v0 = 2-5g/3): **r = t = (1 + v0 + 5g)*L0 algebraically**. This gives 5 perfect pairs and LB = 1/2 = constant throughout the entire AP sub-region of this permutation sector.

For **non-AP asymmetric interior points** (g1+g2 ≠ g4+g5), r ≠ t. LB is no longer 1/2 but remains < c(5). Test: g=(1.1, 1.2, 1.05, 1.15, 1.08), v0=0.127, LB = 901/1800 ≈ 0.5006, margin ≈ 0.0074.

---

### Single-template argument: fails, but points to the right approach

**No single template T covers all 31 Z-type vertices.** Best coverage: 14/31 (template (4,5,1,2,0,3)). However, the **convexity of LB(x,T)** gives the right framework:

**If one template T* achieves LB(v, T*) <= c(5) for ALL VERTICES of the compact polytope P, then by convexity, max_{x in P} LB(x, T*) = max at vertex <= c(5), so LB(x, T*) <= c(5) for ALL x in P.**

Since no single template covers all 31 Z-type vertices, this direct path fails. But the approach is still useful:

**The union of 31 convex sets C_{T_v} (one per Z-type vertex) should cover the Tier 3 interior.** Checking this union is an LP feasibility problem:

"Is there x in P with LB(x, T_v) > c(5) for all 31 Z-type templates T_v simultaneously?"

This LP is **finite** and **computationally verifiable**. Sampling confirms coverage (100% of 1000 random interior points covered with min margin 0.005).

---

### Regional coverage: permutation sectors

The Tier 3 region is naturally partitioned into **permutation sectors** (one per ordering of the 6 shifted params). Each sector's relevant vertex is its unique Z-type vertex (where v0=0).

For each permutation sector with Z-type vertex v and template T_v:
- **AP sub-region** (equal gaps): LB(x, T_v) = 1/2 = constant (algebraic identity r=t for AP configs). ✓
- **Non-AP interior**: LB(x, T_v) is piecewise convex; max within sector is at a VERTEX of the sector (by convexity). The vertices of each sector are among the 93 vertices (Z-type v and AP-type boundary). At AP-type vertices: Tier 2 handles (LB = c(5)). At Z-type vertex: LB = 1/2 < c(5). ✓

**Critical check needed:** Is the maximum of LB(x, T_v) over each permutation sector indeed <= c(5)? The convexity gives: max = max at vertex of sector. If all sector vertices (Z-type with LB = 1/2, AP-type with Tier 2 applying) satisfy LB <= c(5), coverage follows.

However, at AP-type vertices for template T_v (which is the Z-type template), LB(v_AP, T_v) might exceed c(5). But Tier 2 (not T_v) handles AP-type vertices. The question is whether T_v achieves LB <= c(5) at AP-type VERTICES of the same sector as v. If not, the interior might have LB > c(5) for T_v at AP-type corners, but Tier 2 covers those corners separately.

---

### Positive margin argument (approach 4 from task)

At all 31 Z-type vertices: LB(v, T_v) = 1/2, margin = c(5) - 1/2 = 1/126 > 0 (verified exactly for wrs=35, computationally for all 31 with min margin 0.0046).

**LB(x, T_v) is CONVEX** → the set {x: LB(x, T_v) <= c(5)} is a convex neighborhood of v (with positive "radius"). By compactness of the Tier 3 closed region and the positive margin at every Z-type vertex, the union of these convex neighborhoods covers some open set around the Z-type boundary.

**Quantitative version:** The margin at Z-type vertices is >= 1/126 ≈ 0.008. The Lipschitz constant of LB (with respect to piece sizes) is at most 1 (greedy picking picks one piece). The maximum piece size change when moving from a Z-type vertex into the interior is bounded by the polytope diameter. If the polytope diameter * 1 <= 1/126, coverage follows. (This needs the actual polytope diameter calculation.)

More practically: the positive margin means each C_{T_v} contains v plus a neighborhood, and these neighborhoods collectively cover the Tier 3 region.

---

### Bottom-line path for the proof builder

**The correct argument to replace the false "max at vertex of piecewise linear":**

1. **LB(x,T) is CONVEX in x** (standard: sum of k largest linear functions = max over subsets = convex).

2. For each template T, C_T = {x: LB(x,T) <= c(5)} is **convex** (sublevel of convex function).

3. **LP coverage check:** The interior coverage follows from showing: no x in the Tier 3 region lies outside ALL convex sets C_T (for all 360 templates). This is equivalent to the LP:
   "∃x in Tier3 region: LB(x,T) > c(5) for all T" being infeasible.

4. **Simpler (if one template suffices for each sector):** For each permutation sector, template T_sigma achieves LB(x, T_sigma) <= c(5) for all x in the sector. Since LB is convex, max over sector = max at sector vertex. Sector vertices are either Z-type (LB = 1/2 < c(5) via T_sigma) or AP-type (Tier 2 handles, max LB = c(5)). Therefore LB(x, T_sigma) <= c(5) throughout sector (but need LB(v_AP, T_sigma) <= c(5) for AP-type vertices in the same sector).

5. **Fallback (most labor-intensive but rigorous):** Provide exact algebraic proofs for all 31 Z-type vertices (one done: wrs=35). For each, the proof shows LB = 1/2 (perfect pairs, margin = 1/126). Then use the LP coverage check to handle the interior.

---

### Distinct openings

- **Opening A (Single-template+Convexity):** Find T that achieves LB <= c(5) at all 31 Z-type vertices AND all AP-type vertices have Tier 2 covering them. Then convexity closes the interior. Computation shows no T* achieves all 31 Z-type, but might be achievable with a slightly broader template family (e.g., allowing cut positions that are not just "match singleton exactly").

- **Opening B (Permutation-sector partition):** Show each of the 360 permutation sectors has a template T_sigma with LB <= c(5) throughout that sector. The sector's max is at its Z-type vertex (LB = 1/2) and AP-type vertices (Tier 2 = c(5)). Need: LB(v_AP, T_sigma) <= c(5) for AP vertices in the sector. Algebraic check per sector.

- **Opening C (LP coverage):** Run the LP feasibility check: union of 360 convex sets C_T covers Tier 3 region. Each C_T is defined by linear constraints (within each sorting region). The LP has ~36,000 constraints and is computationally verifiable.

- **Opening D (Full algebraic Z-type):** Prove all 31 Z-type vertices with exact rational arithmetic (wrs=35 done, 30 remain). Then use convexity + LP coverage for interior.

- **Opening E (Continuity from boundary):** The Tier 3 closed region is compact. f = min_T LB is continuous. f = c(5) on AP-type boundary (Tier 2). f = 1/2 on Z-type boundary (31 vertices). By intermediate value theorem / connectedness, f < c(5) throughout the interior... but this argument has gaps (f is not monotone along paths).

---

### Candidate techniques

- **Convexity of LB(x,T)** (sum of k largest of n linear functions): KEY technique, enables the single-template argument and LP coverage.
- **LP feasibility** (check union of convex sets covers polytope): reviewer's suggested approach.
- **Algebraic identity r=t** (for perfect-pair strategies): gives LB = 1/2 = constant on AP sub-regions of each permutation sector.

### Knowledge-base entries

- **Casework / exhaustion**: "split into finitely many cases and settle each" — for the 31 Z-type vertices (not 93).
- **Extreme value theorem** (Linear algebra section): continuous function on compact set attains min/max — applies to f.
- **Direct proof**: chain from convexity of LB → sublevel sets convex → LP coverage.

### Analogous past problems

None found in the crux corpus that directly match this convexity-of-greedy-LB structure.

### Prior progress

- Tier 1 (V_j): PROVED.
- Tier 2 (Pairwise non-adjacent, 10 pairs): PROVED.
- Bounded region characterization (g in (1,6/5), v0 in (0,1/3)): PROVED.
- Z-type vertex wrs=35 exact proof: LB = 1/2, margin = 1/126. PROVED.
- 93 vertices computationally verified. AP-type: margin >= 0.0026 (but now understood to be covered by Tier 2, not needing (2,2,1)). Z-type: margin >= 0.0046 (wrs=35 exact, others computational).
- Interior sampling: 100% coverage with margin >= 0.005.

### Dead ends (do not retry)

- **"Max of piecewise linear at vertex" for f = min_T LB**: FALSE. Reviewer confirmed. Do not retry.
- **Berge's Maximum Theorem for continuity**: VALID for continuity of f, but continuity alone does not give "max at vertex".
- **Single (2,2,1) template covering all 93 vertices**: FAILS. wrs35 template covers only 33/93. No single template covers all 31 Z-type vertices (best: 14/31).
- **Type 3 strategies (2 cuts + 3 halves)**: Previously shown insufficient (~95% coverage).

### Small-case / intuition notes

- **LB = 1/2 is achievable** (algebraically) for Z-type vertices via perfect pairs (r=t identity). This is the "natural" bound below c(5) = 32/63.
- **AP-type vertices hit LB = c(5) exactly** via Tier 2 (pairwise diff = 1 is the tight case). This boundary is where Tier 2 "hands off" to Tier 3.
- **Interior points** have LB strictly between 1/2 and c(5) for the appropriate templates. The min margin in sampling is 0.005 > 0 (conjecture: interior margin > Z-type margin > AP-type margin = 0 for Tier 3 strategies).
- The **convexity of LB(x,T) for each T** is the structural fact that should replace the false "max at vertex" claim. VERIFIED empirically (no violations in 100 random tests).
- **360 discrete templates, each giving a convex feasibility set C_T** — the union should cover the Tier 3 region. LP verification is the rigorous check.
