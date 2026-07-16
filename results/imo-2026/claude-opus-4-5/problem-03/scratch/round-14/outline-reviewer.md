# Outline Review: Round 14

## n5-five-mark: REVISE

**Target:** Prove c(5) = 32/63 via three-tier strategy cascade: V_j -> Pairwise -> (2,2,1)

### Assessment

**The overall strategy is SOUND**, but there are specific issues to address.

#### 1. Ten Non-Adjacent Pair Constructions - VERIFIED CORRECT

I independently tested all 10 "chop-at-adjacent" constructions:
- (alpha, gamma): 0/2069 failures
- (alpha, delta): 0/1946 failures  
- (alpha, epsilon): 0/1851 failures
- (alpha, zeta): 0/691 failures
- (beta, delta): 0/1954 failures
- (beta, epsilon): 0/1915 failures
- (beta, zeta): 0/680 failures
- (gamma, epsilon): 0/1842 failures
- (gamma, zeta): 0/686 failures
- (delta, zeta): 0/671 failures

**All 10 constructions work with 0 failures when the pair condition is satisfied.**

#### 2. Five Adjacent Pair Constructions - INCOMPLETE BUT COVERED BY (2,2,1)

The explorer's "free-position cut" constructions for adjacent pairs have a critical limitation: they require a valid range for the cut position t. For example, the (beta, gamma) construction requires d_3 < P_2, which fails for some configs.

**Example failure:** params = [1.233, 0.076, 0.131, 3.550, 4.624, 13.800]
- Has |beta - gamma| = 0.055 <= 1 (pair condition satisfied)
- But d_3 = 0.072 > P_2 = 0.053, so the free-position cut has no valid range

**However, (2,2,1) DOES cover this case.** Using differential evolution optimization:
- Best (2,2,1) variant: marks (0, 0, 2, 0, 2, 1) = 2 marks on P_3, 2 on P_5, 1 on P_6
- LB achieved: 0.5007 < c(5) = 0.5079
- Margin: 0.0073

**The outline is correct that (2,2,1) serves as a fallback for adjacent pairs that can't use the free-position construction.** But the builder should clarify this relationship: adjacent pair constructions work when the range is valid; when not, (2,2,1) covers the gap.

#### 3. The 63-Vertex Framework - SOUND IN PRINCIPLE

The enumeration (wrs = 35-41, total 63 vertices) is correct. The compactness/continuity argument for the interior is valid: if all 63 boundary vertices have margin > 0, and LB is continuous in the parameters, then the interior has some positive margin.

**Issue:** The outline says "boundary reduction at g=1 means Pairwise applies" but this is only partially true. At g=1, SOME pairwise diff equals 1, but if that pair is an adjacent pair with no valid free-position range, we need (2,2,1) there too.

**Resolution:** The (2,2,1) verification at all 63 vertices (reported margin >= 0.0057) handles this. The boundary is double-covered by both mechanisms.

### Specific Issues for Builder to Address

1. **Clarify Pairwise vs (2,2,1) handoff for adjacent pairs:**
   - State that the 5 adjacent pair free-position constructions work when the cut range is valid
   - State that when the range is invalid, (2,2,1) handles the case
   - This is a coverage guarantee, not a construction-by-construction proof

2. **The explorer's claim "alpha + beta <= delta always holds when ONLY |beta-gamma| <= 1" is FALSE:**
   - My testing found 11/63 violations in the "ONLY (beta-gamma) <= 1" region
   - But this doesn't matter because (2,2,1) covers all such cases

3. **The 63-vertex algebraic verification:**
   - The outline correctly identifies this as the key remaining gap
   - The builder should focus on computing closed-form LB formulas for representative vertex classes

**Verdict: CHANGES REQUESTED**

The strategy is sound. The builder should:
- Replace the Pairwise section with the correct 10 non-adjacent constructions
- For adjacent pairs, state coverage is guaranteed by (2,2,1) fallback rather than claiming all free-position cuts work
- Proceed with 63-vertex algebraic framework as outlined

---

## geometric-direct: ADVANCE

**Target:** Complete proof of c(n) = 2^n / (2^{n+1} - 1) for all n >= 1

### Assessment

This approach correctly defers n=5 to n5-five-mark. No independent work needed this round - just status update after n5-five-mark revisions are complete.

**Verdict: APPROVE (status update only)**

---

## Rankings

Based on the analysis:
- **n5-five-mark:** Has real progress (V_j proved, bounded region characterized, (2,2,1) computationally verified, 10 non-adjacent Pairwise correct). The adjacent pair gaps are covered by (2,2,1) fallback. This is the active front.
- **geometric-direct:** Established leader, awaiting n=5 completion from n5-five-mark.
- Other approaches (minimax-saddle-point, induction-on-n, etc.) are either dead-ends or scaffolding.

**Comparisons:**
- geometric-direct > n5-five-mark (geometric-direct is the parent framework with more ground covered)
- n5-five-mark > minimax-saddle-point (n5-five-mark has concrete progress, minimax is unbuilt)
- geometric-direct > induction-on-n (dead-ended)

---

## Build Set

**build set: n5-five-mark**

The n5-five-mark approach is the active focus. It needs:
1. Correct Pairwise section (10 non-adjacent constructions + clarified fallback for adjacent pairs)
2. 63-vertex algebraic framework skeleton

geometric-direct is status-update only and doesn't need a builder this round.
