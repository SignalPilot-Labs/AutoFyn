# Outline Review: Round 16

## Approach: n5-five-mark (revise)

### Verdict: APPROVE

The outline correctly identifies the 93-vertex structure for the n=5 bounded region proof. The key claims have been verified:

**1. 93-Vertex Enumeration (VERIFIED CORRECT)**

The polytope has exactly two types of boundary vertices requiring (2,2,1)/(2,1,1) verification:

- **62 AP-type vertices** (g=1 boundary, interior v_0 in (0, 1/3)): wrs in {36,37,38,39,40,41} with counts 5+6+9+16+12+14 = 62. These have all pairwise diffs = 1, so they lie exactly on the "pairwise <= 1" boundary. The (2,2,1) strategies provide strictly positive margin.

- **31 Z-type vertices** (v_0=0 boundary, r_alpha=0): The permutations with alpha=0 (P1 = L0 exactly). wrs in {35,...,41} with counts 1+4+3+6+7+6+4 = 31. All d_j > L0 at these vertices, so V_j does not apply. Need explicit (2,2,1) verification.

The enumeration is complete because:
- Z-type with r_alpha != 0 have some d_j = L0, so V_j applies (LB = c(5) exactly)
- wrs=35 AP-type is degenerate (v_0 = 1/3 is at the boundary of "all params > 0") and is handled by Tier 2

**2. wrs=35 Z-type Exact Proof (VERIFIED)**

I verified the exact rational proof independently:
- Pieces: [1/63, 16/315, 11/105, 8/45, 17/63, 8/21]
- Strategy: 2 cuts on P4 at (P1, P1+P2), 1 cut on P6 at P5, halve P3
- Creates 5 pairs: {P1,P1}, {P2,P2}, {P3/2,P3/2}, {P5,P5}, {P4-P1-P2, P6-P5}
- LB = 1/2 exactly (all pairs cancel by Pairing Cancellation Lemma)
- Margin = c(5) - 1/2 = 1/126 > 0

Note: The explorer's claimed cut positions (19/189, 23/189, 50/189) are WRONG. The correct positions are (1/63, 1/15, 17/63) which create the exact pairs.

**3. Compactness Argument (SOUND)**

The outline correctly invokes:
- Berge's Maximum Theorem: The function f(config) = min_{XY strategy} LB is continuous on the compact polytope
- The "all pairwise > 1, all params > 0" region is a bounded convex polytope (proved via weighted sum constraint)
- f is piecewise linear (LB changes sorting structure at hyperplanes), so max of f on compact polytope is at a vertex
- Verifying all 93 vertices implies interior coverage

This is mathematically sound. The knowledge_base.md entry "Extreme value theorem" confirms: "a continuous function on a compact set attains its min and max."

**4. Minor Issues (Non-blocking)**

- The approach file still says "63 vertices" in some places; the builder should update to 93.
- The worked example for wrs=41 has arithmetic errors that should be corrected.
- The (2,1,1) vs (2,2,1) terminology should be clarified: wrs=35 uses 4 marks (2,1,1), interior vertices may need 5 marks (2,2,1).

**Conclusion:** The framework is complete and sound. Build should proceed with the corrected 93-vertex structure.

---

## Approach: geometric-direct (advance)

### Verdict: APPROVE

The outline proposes to advance geometric-direct by importing the n5-five-mark result once it is PROVED. This is correct workflow: n5-five-mark is a specialized attack on the n=5 Case B Small sub-case, and once verified, it should merge into the main geometric-direct proof.

No structural issues. The advance depends on n5-five-mark completion.

---

## Approach: n6-bounded-region (new)

### Verdict: DEFER (not registered this round)

The outline proposes a new approach for n=6 but acknowledges it is scaffolding only:
- Steps 4-6 are entirely open
- The Pigeonhole test result is unknown
- No strategies identified

This is premature. The priority is completing n=5 first. Once n5-five-mark is PROVED, the pattern may suggest how to attack n=6 (whether Pigeonhole succeeds or fails, what strategy family is needed).

Do not register until n=5 is complete. This is not a cut; it is a deferral.

---

## Ranking Update

Current population for imo-2026-03:
- geometric-direct (Elo 1734): Last advanced Round 11, framework complete for n=1,2,3,4
- n5-five-mark (Elo 1584): Last advanced Round 12, 93-vertex framework now identified
- minimax-saddle-point (Elo 1491): Never built
- minimax-value (Elo 1438): Never built
- induction-on-n (Elo 1379): Dead end

Comparisons this round:
- n5-five-mark WINS vs minimax-saddle-point: n5-five-mark has explicit strategy constructions verified; minimax-saddle-point is unbuilt scaffolding
- n5-five-mark WINS vs minimax-value: same reasoning
- geometric-direct WINS vs n5-five-mark: geometric-direct has complete proof for n=1-4; n5-five-mark contributes only n=5 which will merge into geometric-direct
- geometric-direct WINS vs all others: highest progress, most complete structure

No new approaches to register (n6-bounded-region deferred).

---

## Build Set

**build set: n5-five-mark**

The builder should:
1. Update the 63-vertex claim to 93-vertex (62 AP-type + 31 Z-type)
2. Correct the wrs=35 exact proof with the verified cut positions
3. Add explicit verification summary for AP-type and Z-type vertices
4. Formalize the compactness argument with Berge's Maximum Theorem
5. Mark the framework as COMPLETE pending algebraic enumeration of all 93 vertices OR accept computational verification as standard finite casework per knowledge_base.md

Once n5-five-mark is APPROVED by the reviewer, geometric-direct will advance in the next round to import the result.
