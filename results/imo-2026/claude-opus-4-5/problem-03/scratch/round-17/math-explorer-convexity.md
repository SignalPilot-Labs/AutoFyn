## imo-2026-03

### Lens: Convexity structure of the strategy space

---

### Root cause of the gap (confirmed)

The proof claims: "A piecewise linear function on a compact convex polytope attains its maximum at a vertex."

This is **FALSE** for `f(config) = min_strategy LB(config, strategy)`.

Here is why precisely:

For each fixed (2,1,1) template T with cut targets expressed as piece sizes, `LB_T(config)` = 1/2 + |P_a - P_b - P_c - (P_e - P_f)| / 2. This equals 1/2 + |linear form in config| / 2, which is **convex** in config (absolute value of a linear function is convex).

Therefore `f = min_T LB_T` is the **minimum of convex functions** — which is neither convex nor concave in general. The classic counterexample: `min(|x|, |x-1|)` on `[0,2]` attains its maximum 0.5 at the **interior** point x=0.5, not at the vertices x=0 or x=2.

**Consequence:** Verifying that `f(v) <= c(5)` at all 93 vertices does NOT imply `f(x) <= c(5)` for interior points.

---

### Key structural finding: coverage sets are CONVEX SLABS

For a (2,1,1) template T = "cut P_a at {P_b, P_b+P_c}, halve P_d, cut P_e at P_f" (leaving P_b, P_c, P_f uncut):

XY creates 10 pieces = 4 exact pairs {P_b, P_b}, {P_c, P_c}, {P_d/2, P_d/2}, {P_f, P_f} plus 2 singletons {R_a, R_e} where:
- R_a = P_a - P_b - P_c
- R_e = P_e - P_f

By the Singleton-Pair Formula: `LB_T = 1/2 + |R_a - R_e| / 2`.

The coverage set `R_T = {config : LB_T <= c(5)} = {config : |R_a - R_e| <= L_0}` is the intersection of two half-spaces:
- R_a - R_e <= L_0
- R_e - R_a <= L_0

This is a **CONVEX SLAB** — always.

In terms of shifted params x = [alpha, beta, gamma, delta, epsilon, zeta]:
`|P_a - P_b - P_c - (P_e - P_f)| / L_0 = |A_T · x + c_T|`

where A_T is a specific integer coefficient vector and c_T is an integer constant, both computable from the template indices.

**Example (the wrs=35 template):** a=4, b=1, c=2, d=3, e=6, f=5 gives:
- R_a/L_0 = 1 + gamma + delta - alpha
- R_e/L_0 = 1 + zeta
- Coverage: |gamma + delta - alpha - zeta| <= 1

This is a slab in shifted-param space.

---

### The LP coverage check: the correct proof path

Since each `R_T` is a convex slab, the coverage question is:

**Does the union of finitely many convex slabs cover the bounded region polytope?**

This is verifiable by LP: For each point x in the bounded region, is there some template T with `|A_T · x + c_T| <= 1`?

LP formulation: Find x satisfying (a) bounded region constraints [linear], and (b) `|A_{T_v} · x + c_{T_v}| > 1` for all 93 templates T_v. If **infeasible**, coverage is proved.

For (2,1,1) templates: each slab constraint = 2 linear inequalities. With 93 templates = at most 186 linear constraints. Finite, computationally checkable LP.

---

### Zero-sum templates: v_0-independent coverage conditions

There are exactly **3 distinct (2,1,1) coverage conditions with Sum(A_T) = 0** — these conditions depend ONLY on the rank assignment (permutation of sorted params), NOT on v_0 or the gap g:

1. |-alpha - gamma + epsilon + zeta| <= 1
2. |-alpha + gamma + delta - zeta| <= 1  (covers wrs=35 template)
3. |-alpha - beta + delta + zeta| <= 1

These 3 conditions cover **26 of 62 AP-type vertices** (verified by exact rational arithmetic over all permutations with wrs in {36,...,41}).

For these 26 vertices, coverage extends to ALL interior points with the same rank assignment (at any g, any v_0), because the condition is independent of v_0.

The remaining 36 AP-type vertices need templates with Sum(A_T) != 0, giving v_0-dependent conditions. These conditions hold at specific vertices but do NOT automatically extend to all interior points with the same rank assignment.

---

### Vertices requiring (2,2,1) strategies

**Computational finding:** Exactly **1 of 62 AP-type vertices** cannot be covered by ANY (2,1,1) template:

- wrs=39, ranks=(r_alpha, r_beta, r_gamma, r_delta, r_epsilon, r_zeta) = (1, 2, 0, 3, 5, 4)
- v_0 = 1/7
- Pieces: [5/147, 37/441, 5/49, 74/441, 13/49, 17/49]
- min LB over all feasible (2,1,1) templates = 509/1000 ≈ 0.509 > c(5) ≈ 0.508

For this vertex, a (2,2,1) strategy works: cut P_3 at 2 equal positions (approximately P_3/3 each) + cut P_6 at a small position + halve P_4. Numerical optimization gives min LB ≈ 0.503, margin ≈ 0.005 > 0.

For the (2,2,1) strategies with optimally chosen cut positions, the LB formula (when the uncut piece P_w is the largest singleton) is: LB = P_u + P_v + P_c/2 + R_a + P_w + (P_b - R_a)/2 — a LINEAR function of piece sizes. The coverage set is again a half-space (convex).

---

### Distinct openings to close the gap

**Opening A: LP-based coverage verification (recommended)**
- For each of the 93 vertices, identify its template T_v (92 are (2,1,1), 1 is (2,2,1))
- Each R_{T_v} is a convex slab (2 linear constraints)
- Run LP: find x in bounded region with `|A_{T_v} · x + c_{T_v}| > 1` for all 93 templates
- If infeasible (as computational evidence strongly suggests): coverage proved rigorously
- This is a FINITE, COMPUTABLE, RIGOROUS proof

**Opening B: Direct algebraic proof for all 93 vertices**
- Already done for wrs=35 with exact rational arithmetic (certified)
- Extend to all 93 vertices with exact rational arithmetic
- Note: proves VERTEX coverage only; still need interior argument
- Interior argument can be LP-based as in Opening A

**Opening C: Piecewise-linear subdivision argument**
- Partition the bounded region into "chambers" where the (2,1,1) minimizer T* is constant
- Within each chamber, f = LB_{T*} is LINEAR, so its max in the chamber is at a vertex of the chamber
- Vertices of chambers are either: (a) vertices of the bounded region [93 already verified], or (b) intersection of chamber boundaries with bounded region faces
- Type (b) vertices lie on faces of the bounded region, where v_0=0 or g=1 -- potentially many more points to check
- This is more complex than the LP approach

**Opening D: Monotonicity in g argument**
- For zero-sum templates: coverage condition is INDEPENDENT of v_0 and g. These cover 26/62 AP vertices completely (no interior issues).
- For the other 36 AP vertices: try to show coverage monotonically improves as we move from the vertex into the interior (i.e., the coverage margin increases as g decreases from 1 or as v_0 increases from 0).
- If TRUE: vertex verification suffices for these 36 vertices too.
- This requires a monotonicity proof for each non-zero-sum template.

---

### Candidate techniques

- LP feasibility (for coverage verification): finite, standard
- Linear programming duality (to certify infeasibility of "uncovered" LP)
- Interval arithmetic (for rigorous numerical LP bounds)
- Exact rational LP (using Fraction arithmetic, computationally feasible for 93 templates)

---

### Cheap-kill candidates

- **None available**: the gap is a genuine logical flaw in the "max at vertex" claim. No simple structural argument resolves it without computing the LP or providing exact proofs for all vertices.

- **However**: for the 26 vertices covered by zero-sum conditions, NO LP is needed — the coverage condition is purely rank-based and obviously extends to all interior points. Only the remaining 66 vertices (36 AP + 31 Z-type - 1 needing (2,2,1)) need the LP.

Wait, re-checking: 62 AP-type vertices total, 26 covered by zero-sum conditions, 36 need v_0-dependent conditions. Among the 36: 35 need (2,1,1) with nonzero sum, 1 needs (2,2,1). All 31 Z-type vertices need explicit verification too (unknown whether zero-sum conditions cover them).

---

### Knowledge-base entries to use

- "Casework / exhaustion": Finite cases (93 vertices); currently accepted by reviewer for vertex-level verification
- "Linear programming / LP duality": The LP coverage check; each slab is 2 linear inequalities
- "Compactness + continuity": Berge's theorem gives continuity of f; combined with LP this proves coverage
- "Convex sets intersection": Each coverage slab is convex; union-coverage argument

---

### Analogous past problems (cruxes)

None retrieved from crux corpus (focus was on convexity analysis).

---

### Prior progress

- 93 vertices enumerated and computationally verified (min margin 0.0026)
- wrs=35 Z-type vertex has exact algebraic proof: LB = 1/2, margin = 1/126 (CERTIFIED)
- V_j strategies (Tier 1): PROVED and CERTIFIED
- Pairwise strategies (Tier 2, 10 non-adjacent pairs): PROVED and CERTIFIED
- Bounded region characterization: PROVED and CERTIFIED

---

### Dead ends (do not retry)

- **"Max of piecewise linear at vertex"**: FALSE for f = min_T LB_T. This is the minimum of convex functions, NOT a convex function. Do not attempt to salvage this argument.
- **Type 3 strategies (2 cuts + 3 halves)**: ~95% coverage, genuine failures near alpha→0. Do not retry.

---

### Small-case / intuition notes (labeled as conjecture)

**Conjecture:** The LP to find a point in the bounded region outside all 93 coverage slabs is INFEASIBLE — i.e., the 93 slabs DO cover the entire bounded region. Evidence: 100% computational sampling coverage with minimum margin 0.0026. This is a conjecture, not a proof.

**Conjecture:** For the 26 AP vertices covered by zero-sum conditions (including many in the wrs=37-40 range), the interior coverage is immediate and requires no additional argument (since the condition is rank-only and g-independent).

**Key structural fact (proved):** For each (2,1,1) template, the LB formula simplifies to 1/2 + |linear form| / 2, giving a coverage slab that is convex. This is the correct structural basis for a coverage argument.

**Key failure (proved by counterexample):** wrs=39, ranks=(1,2,0,3,5,4) requires a (2,2,1) strategy with non-standard cut positions. No (2,1,1) template achieves LB <= c(5) at this vertex. The (2,2,1) coverage condition is also linear (LB = P_1/2 + 1/2 in a specific simplification, requiring P_1 <= L_0 which FAILS in the bounded region — so the natural strategy fails; only a general (2,2,1) with optimized cuts works with margin ~0.005).
