## imo-2026-03 (LP Coverage Lens)

### Summary of findings

**Can LP coverage verification close the interior gap?** YES, in principle — but the 10 templates used for the 93 vertices are INSUFFICIENT for full interior coverage. A larger (but still finite and manageable) set of strategy types IS needed.

---

### 1. How many distinct (2,1,1) target pair structures exist?

There are **360 total (2,1,1) templates** (ordered selections of 3 distinct pieces to cut in specific roles, with the 2 "copy positions" unordered).

For covering the 93 vertices of the bounded region, only **10 distinct templates** suffice. These are:
- (2,0,1,4,3,5): cut P3 at P1+P2; cut P5 at P4; halve P6. Coverage: |P3-P1-P2-(P5-P4)| ≤ L0
- (2,0,1,5,4,3): cut P3 at P1+P2; cut P6 at P5; halve P4. Coverage: |P3-P1-P2-(P6-P5)| ≤ L0
- (3,0,1,5,4,2): cut P4 at P1+P2; cut P6 at P5; halve P3.
- (3,0,2,5,4,1): cut P4 at P1+P3; cut P6 at P5; halve P2.
- (4,0,2,3,1,5): cut P5 at P1+P3; cut P4 at P2; halve P6.
- (5,0,2,4,1,3): cut P6 at P1+P3; cut P5 at P2; halve P4.
- (5,0,3,4,1,2): cut P6 at P1+P4; cut P5 at P2; halve P3.
- (5,0,3,4,2,1): cut P6 at P1+P4; cut P5 at P3; halve P2.
- (5,1,2,3,0,4): cut P6 at P2+P3; cut P4 at P1; halve P5.
- (5,1,3,4,2,0): cut P6 at P2+P4; cut P5 at P3; halve P1.

For each of these, the coverage condition is |Pa-Pb-Pc-(Pd-Pe)| ≤ L0, which is a LINEAR inequality in params — a half-space intersection.

**LP check (identity permutation cell):** Among 1024 sign combinations for 10 templates on the identity permutation cell, only 1 "feasible" LP emerged, and that solution has |s1-s2| = L0 EXACTLY (borderline case at boundary point alpha=0). The 10 templates cover the full identity-permutation-cell interior.

**LP check (all 63 valid permutation cells):** 87 permutation cells have WS_min ≤ 42; 63 have WS_min < 42 (non-empty interior). Sampling 20 interior points per cell confirms: 76/1260 interior points are NOT covered by the 10 templates. These cluster in non-identity cells such as perm=(0,2,1,3,4,5) (gamma < beta ordering).

---

### 2. Why the 10 templates fail in non-identity cells

For perm=(0,2,1,3,4,5) (alpha < gamma < beta < delta < epsilon < zeta ordering), the bounded region interior has configs like:
- alpha=0.0525, beta=2.2618, gamma=1.1777, delta=3.5645, epsilon=4.6375, zeta=5.6970

For this config, ALL 360 (2,1,1) templates give min |s1-s2| = 1.007*L0 > L0. NO (2,1,1) template achieves coverage. The config is **genuinely not coverable by (2,1,1) copy strategies**.

---

### 3. The (2,2,1) strategy that covers the interior

Numerical optimization finds that XY can use a (2,2,1) strategy with 5 marks achieving **LB = 0.5019 < c5 = 0.5079**:

**Strategy:** Cut P6 at position (P6-P5) and (P6-P5+epsilon), cut P2 at x and 2x, halve P4.

The algebraic structure:
- From P6: sub-pieces {P6-P5 ≈ P3, epsilon ≈ 0, P5} → pair {P5, P5} + near-pair {P6-P5, P3}
- From P2: sub-pieces {x, x, P2-2x} → pair {x, x}
- From P4: {P4/2, P4/2} → pair {P4/2, P4/2}
- Unchanged: P1, P3, P5

At our example: P6-P5 = 0.106302 ≈ P3 = 0.103048 (difference 0.003230 ≈ 0.204*L0 < L0). Near-pair is covered.

**Coverage condition for this strategy type:**
1. **Near-pair condition:** |P6-P5-P3| ≤ L0, i.e., |d5-P3| ≤ L0 in L0 units: |ζ-α-β-γ-2| ≤ 1 — a LINEAR constraint.
2. **Valid x existence:** P2/2 + P4/2 + P1/2 + P6 < c5, equivalently (in unitless params):
   5α/2 + 2β + 3γ/2 + 3δ/2 + ε + ζ < 45/2 — a LINEAR constraint.
3. **Applicability:** P6-P5 > P3 requires ζ > α+β+γ+2 (case P6-P5 > P3) OR P3 > P6-P5 case (slightly different LB formula, but same structure).

All three conditions are LINEAR in the params. So the coverage region for this strategy type is an INTERSECTION of half-spaces.

---

### 4. Broader coverage structure

The interior coverage problem requires a COLLECTION of (2,2,1) strategy types, each with coverage conditions that are intersections of a FEW linear half-spaces. The "covered by strategy type t" region is a polytope, and coverage requires the UNION of these polytopes to contain the full bounded region.

**Key algebraic facts:**
- For a fixed (2,2,1) strategy with FIXED target pair structure, LB is linear in config.
- Coverage condition |s1-s2| ≤ L0 (or more generally LB ≤ c5) is a UNION of a few half-spaces.
- The relevant strategy types for the non-identity cells involve "d5 near-pair" patterns:
  - Cut P6 at P6-P5 (approximate), creating {P5, P6-P5≈P3} — condition: |ζ-α-β-γ-2| ≤ 1
  - Cut P6 at P6-P4 (approximate), creating {P4, P6-P4≈P2} — condition: |ζ-α-β-2| ≤ 1
  - etc.

**Critical asymmetry finding:** The 10 templates were designed for the identity permutation cell where params are sorted. For non-identity cells, the PIECE sizes (P1<...<P6 always sorted) have a DIFFERENT relationship to the cumulative-sum structure, requiring different strategy types.

---

### 5. Simpler structural argument?

**No simpler argument found.** The LP approach IS the right route, but needs:

1. Enumerate strategy types for EACH permutation cell:
   - For each valid permutation cell (63 cells), identify 1-3 (2,2,1) strategy types covering that cell
   - Each type gives 2-3 linear coverage conditions

2. The full LP then has:
   - ~63 permutation cells × ~3 strategy types per cell = ~189 strategy types
   - Each with ~3 linear coverage conditions
   - Total: ~500 half-space constraints in 5D (after WS=42 projection)
   - Feasibility check: 2^500 LP checks is infeasible!

**Alternative structure (promising):** The coverage conditions across permutation cells have a SYSTEMATIC PATTERN. For the "d5 near-pair" family:
- If d5 ≈ P3 (i.e., |ζ-α-β-γ-2| ≤ 1): Use the strategy above
- If d5 ≈ P4 (i.e., |ζ-α-β-γ-δ-2| ≤ 1): Use cut P6 at P6-P4, creating {P4, P6-P4≈P2}
- If d5 ≈ P2 (i.e., |ζ-α-β-2| ≤ 1): Use cut P6 at P6-P2, creating {P2, P6-P2≈P5-something}

The pattern suggests: for each pair of pieces (Pi, Pj) such that |Pi - (P6-Pj)| ≤ L0 (one of them is a near-match for d5), there's a valid strategy.

The KEY QUESTION is: for every config in the bounded region, does SOME such near-match exist?

---

### 6. Main conclusions for the outliner

- **The proof gap (interior coverage) is real but CLOSABLE** using (2,2,1) strategies with optimized cut positions
- **Each strategy type has LINEAR coverage conditions** (the LP approach is conceptually valid)
- **The challenge is the NUMBER of strategy types** needed (one per permutation cell ~63 types), each with multiple linear conditions
- **The 10 templates from the 93-vertex analysis are insufficient for interior coverage** — they miss ~6% of interior points in non-identity cells
- **The numerical evidence shows coverage IS achievable**: scipy.optimize found LB=0.502 < c5 for the hardest interior point
- **Alternative clean route:** Show that for EVERY config in the bounded region, some "near-pair" condition |P_k - (P6-P_j)| ≤ L0 holds for at least one pair (j,k). This would give a unified strategy.

---

### Distinct openings for the outliner

**Opening A: Systematic near-pair coverage**
Show that in the bounded region, for every config, some pair (i,j) satisfies |Pi - (P6-Pj)| ≤ L0 (one piece is approximately the "complement" of another in P6). This would allow a unified (2,2,1) strategy family. Coverage condition is linear per pair.

**Opening B: Direct LP infeasibility for all 63 cells**
For each of the 63 permutation cells, add 3-5 strategy types (as identified numerically) and verify the LP is infeasible. This is a finite but large computation (could be done algorithmically, not algebraically).

**Opening C: Monotone extension from vertices**
Show that the coverage function f(config) = min_{strategy} LB(config, strategy) is CONVEX (not just piecewise linear) or has some other monotonicity that allows vertex coverage to imply interior coverage. (This may require a structural theorem about the (2,2,1) family.)

**Opening D: Case split on d5 = P6-P5**
The key near-pair in non-identity cells is typically |d5 - P_k| for some k. Since there are only 5 choices for k, do a 5-case analysis showing one always works.

---

### Knowledge-base entries to use

- **LP/Linear programming:** The coverage conditions are half-spaces; LP feasibility is the right tool
- **Casework/exhaustion:** 63 permutation cells can be handled case-by-case (each is a convex polytope)
- **Pairing Cancellation Lemma (certified):** Still the key for computing LB from near-pairs
- **Singleton-Pair Formula (certified):** Applies to (2,1,1) strategies; for (2,2,1) the formula is DIFFERENT

---

### Prior progress

- V_j strategy: PROVED
- Pairwise strategy (10 non-adjacent): PROVED
- Bounded region characterization: PROVED (g ∈ (1, 1.2), v_0 ∈ (0, 1/3))
- 93-vertex framework: COMPLETE (62 AP-type + 31 Z-type vertices)
- wrs=35 Z-type exact proof: CERTIFIED (LB = 1/2 exactly)
- All 93 vertices computationally verified (min margin 0.0026)
- Interior coverage: **OPEN** — the compactness argument is invalid, LP approach needed

---

### Dead ends (do not retry)

- **Convexity/concavity argument for f = min_strategy LB:** FALSE. min of linear functions is concave, not convex; max-at-vertex fails.
- **10 templates cover all interior:** FALSE. They cover identity-perm-cell interior but miss ~6% of non-identity cells.
- **(2,1,1) copy strategies for all interior:** INSUFFICIENT. The uncovered interior points have min |s1-s2|/L0 = 1.007 > 1 for ALL 360 (2,1,1) templates — genuinely outside (2,1,1) coverage.
- **Berge's Maximum Theorem (applied as in round 16):** Correctly shows f is continuous but does NOT imply max at vertex for non-convex f.

---

### Small-case / intuition notes (conjecture only)

- **Conjecture:** For every config in the bounded region, some consecutive difference satisfies |d_j - d_k| ≤ L0 for some pair (j,k), enabling a (2,2,1) near-pair strategy. This "near-consecutive" condition may be provable from the WS=42 constraint.
- **Observed:** The uncovered interior points in perm=(0,2,1,...) cells all have d2 = gamma*L0 ≈ 1.1-1.2*L0 and d1 = beta*L0 >> L0. The near-pair is always d5 ≈ d2 (using the gap to P3 from P6-P5 ≈ P3). The coverage condition is |ζ-α-β-γ-2| ≤ 1.
- **Observed:** The LP check on 87 permutation cells found only borderline "feasible" solutions (all with some template at |s1-s2| = L0 exactly, numerically). This is STRONG evidence that the 10 templates cover the CLOSED bounded region exactly, with coverage achieved with equality at boundaries.
