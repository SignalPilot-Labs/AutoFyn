# Proof Review: Round 16

## Approach: n5-five-mark

### Summary of Changes

The builder corrected the vertex count from 63 to 93 (62 AP-type + 31 Z-type), added the wrs=35 exact proof with full rational arithmetic, and formalized the compactness argument via Berge's Maximum Theorem.

---

### Verification Results

#### 1. 93-Vertex Enumeration: VERIFIED

Independently enumerated using Python:
- **AP-type (g=1 boundary):** wrs in {36,37,38,39,40,41} with counts 5+6+9+16+12+14 = 62 vertices
- **Z-type (v_0=0, r_alpha=0):** wrs in {35,...,41} with counts 1+4+3+6+7+6+4 = 31 vertices
- **Total: 93 vertices**

The counting is correct. The explanation for why Z-type vertices with r_alpha != 0 are handled by V_j (some d_j = L_0) is also correct.

#### 2. wrs=35 Exact Proof: VERIFIED

Independently verified using Python's Fraction class:
- **Piece sizes:** [1/63, 16/315, 11/105, 8/45, 17/63, 8/21] sum to 1. CORRECT.
- **Strategy:** 2 cuts on P_4 at positions P_1 and P_1+P_2; 1 cut on P_6 at P_5; halve P_3
- **Resulting 10 pieces:** Creates exactly 5 pairs:
  - {1/63, 1/63} (original P_1 and cut from P_4)
  - {16/315, 16/315} (original P_2 and cut from P_4)
  - {11/210, 11/210} (halved P_3)
  - {17/63, 17/63} (original P_5 and cut from P_6)
  - {1/9, 1/9} (P_4 remainder and P_6 remainder)
- **LB = 1/2 exactly** (greedy picks one from each pair)
- **Margin = c(5) - 1/2 = 32/63 - 1/2 = 1/126 > 0**

The exact rational proof is complete and correct.

#### 3. Compactness Argument: **GAP IDENTIFIED**

The proof claims: "A piecewise linear function on a compact convex polytope attains its maximum at a vertex."

**This claim is FALSE in general.** It is true for CONVEX piecewise linear functions (supremum of finitely many linear functions), but f(config) = min_strategy LB(config, strategy) is:
- A minimum of piecewise linear functions (each strategy gives piecewise linear LB)
- The minimum of convex functions is convex, but the resulting function is NOT necessarily the supremum of linear functions

**Counterexample structure:** Consider f(x) = min(1, 2-x) on [0,2]. This is piecewise linear with max at x=1 (interior), not at the vertices x=0 or x=2.

**However, the gap may be closable:**
- The (2,2,1) strategies, when the cut positions are chosen to create matching pairs (as in the wrs=35 example), form a DISCRETE set of strategies
- Each discrete strategy gives LB as a LINEAR function of config (once the target pair structure is fixed)
- "Some strategy achieves LB <= c(5)" is a union of finitely many half-spaces
- The coverage reduces to checking if this union contains the polytope

The proof does not complete this LP-style coverage verification.

#### 4. Finite Casework Rigor: PARTIALLY ACCEPTABLE

Per knowledge_base.md "Casework / exhaustion": "Split into finitely many cases and settle each. Keep cases disjoint and exhaustive."

- The 93 vertices ARE finite cases that can be settled individually
- The wrs=35 case is settled algebraically (LB = 1/2 exact)
- The other 92 cases are settled computationally with positive margins (min 0.0026)

**The issue:** Verifying 93 vertices does NOT automatically imply coverage of the entire polytope interior. The proof's claim that "maximum of piecewise linear at vertex" is false for this f. The computational sampling of interior points provides evidence but not rigor.

#### 5. Other Gaps/Errors

- **Berge's Maximum Theorem invocation:** Correctly stated that f is continuous. This is valid.
- **Polytope boundedness:** Correctly proved (v_0 in (0, 1/3), g in (1, 6/5)).
- **No circular reasoning detected.**
- **No skipped cases in vertex enumeration.**

---

### Scores

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| Correctness | 4 | All explicit calculations verified; compactness argument has logical error |
| Completeness/Rigor | 3 | 93 vertices correct; interior coverage argument flawed |
| Progress | 5 | Major advance: 93-vertex framework complete, exact wrs=35 proof |

---

### True Status

**Status: partial**

The proof has made significant progress:
- V_j strategies: PROVED
- Pairwise strategies (10 non-adjacent pairs): PROVED  
- Bounded region characterization: PROVED
- 93-vertex enumeration: COMPLETE
- wrs=35 exact proof: COMPLETE

The gap is in the interior coverage argument. The claim "max of piecewise linear on polytope is at vertex" is FALSE for non-convex piecewise linear functions. The proof needs one of:

1. **LP coverage verification:** Show that the union of half-spaces {LB_S <= c(5)} for discrete strategies S covers the polytope
2. **Structure argument:** Prove that for the specific structure of (2,2,1) strategies, the optimization has max at vertices
3. **Full algebraic enumeration:** Provide exact rational proofs for all 93 vertices (only 1/93 done)

---

### Verdict: CHANGES REQUESTED

The n5-five-mark approach has made substantial progress but the compactness argument has a logical error. The 93-vertex finite casework is correct, but the extension to interior points needs a different argument.

**Specific gap to close:**
- Replace the claim "max of piecewise linear at vertex" with a valid coverage argument
- Either: (a) verify that the discrete (2,2,1) strategies' half-spaces cover the polytope via LP, or (b) provide an explicit "for each interior point, which vertex strategy applies" mapping based on convexity/proximity, or (c) algebraically verify all 93 vertices (expensive but unimpeachable)

---

### Promotable Lemmas

**Lemma: V_j Strategy (n=5)** - CERTIFIED (already certified in prior rounds)

**Lemma: Pairwise Strategy - 10 Non-Adjacent Pairs (n=5)** - CERTIFIED (already certified in prior rounds)

**Lemma: Bounded Region (n=5)** - CERTIFIED (already certified in prior rounds)

**Lemma: wrs=35 Z-type Exact Construction** - **CERTIFIED (NEW)**
- Statement: For the wrs=35 Z-type vertex with pieces [1/63, 16/315, 11/105, 8/45, 17/63, 8/21], the 4-mark strategy (2 cuts on P_4 at {P_1, P_1+P_2}, 1 cut on P_6 at P_5, halve P_3) achieves LB = 1/2 exactly, with margin c(5) - 1/2 = 1/126.
- Verification: Complete rational arithmetic proof verified independently.

**Lemma: 93-Vertex Sufficiency (n=5)** - **REJECTED**
- The claim that verifying 93 vertices proves interior coverage is INVALID as stated
- The compactness argument invokes a false claim about piecewise linear functions
- Can be certified once a valid coverage argument is provided

---

### Record Outcome

The approach advanced from "63 vertices with flawed count" to "93 vertices with correct count, 1 exact proof, but flawed interior argument."
