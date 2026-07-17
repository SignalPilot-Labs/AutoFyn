# Proof Builder Report: unified-characterization

## Summary
Completed a full rigorous proof of the characterization: Mulan wins if and only if theta = 180/n for some integer n >= 2.

## Gaps Closed

### GAP A3 (pair-sum derivation)
Explicitly derived the supplementary angle constraint: when Mulan cuts from P on edge BC to vertex A, the angles at P in the two sub-triangles (angle APB and angle APC) sum to 180 degrees because B, P, C are collinear. This is the Supplementary Angles Lemma in the Preliminaries.

From this, Lemma A1 proves: if both sub-triangles have multiples j_1*theta and j_2*theta at the cut point P, then j_1*theta + j_2*theta = 180, requiring (j_1 + j_2)*theta = 180.

### GAP B1 (Phase 1 cut validity)
Proved in Lemma B1: For theta = 180/n with n >= 3, Mulan needs integer j in (n*beta/180, n*(180-gamma)/180). The interval length is n*alpha/180. For this to contain an integer, need alpha > theta = 180/n. 

Showed: if no angle exceeds theta, then all angles <= 180/n implies 3*(180/n) >= 180, so n <= 3. For n = 3 this forces equilateral (60,60,60), but then theta = 60 and the triangle already has angle theta -- Mulan has won. So before Mulan's turn, some angle exceeds theta, making the cut valid.

### GAP B2 (multiple persistence at vertex)
This was the main concern: after Phase 1, the multiple of theta appears at the cut point P, which becomes a VERTEX of the kept sub-triangle. Lemma B2 confirms this explicitly: in both T_1 and T_2, the point P is a vertex with the multiple of theta as its angle. Whichever Shan-Yu keeps, the multiple is at vertex P.

The cascade then works on this vertex angle via bisection (Lemma B3) or reduction (Lemma B5), maintaining control until reaching 2*theta and then theta.

## Proof Structure
1. **Preliminaries:** Cut mechanics, supplementary angles lemma
2. **Part A (Necessity):** Invariant argument -- Shan-Yu maintains safe set when 180/theta not an integer >= 2
3. **Part B (Sufficiency):** 
   - Special case theta = 90: instant win
   - General case n >= 3: Phase 1 (force multiple) + Phase 2 (cascade to theta)

## Status: solved

The proof is complete with all cases covered, all gaps closed, and the final answer explicitly stated and verified.
