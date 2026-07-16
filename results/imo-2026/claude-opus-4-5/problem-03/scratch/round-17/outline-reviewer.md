# Outline Review: Round 17

## Summary

Four approaches proposed, all targeting the n=5 interior coverage gap identified in Round 16 (the false "max of piecewise linear at vertex" claim). The explorers have provided the key structural insight: **LB(x,T) is CONVEX in x** for each fixed template T.

---

## Approach: n5-convex-coverage (revise from n5-five-mark)

**Verdict: CHANGES REQUESTED**

### Sound skeleton?

The approach correctly identifies:
1. LB(x,T) is convex (sum of 5 largest of 10 linear functions = max over subsets = convex). VERIFIED computationally: 0 violations in 100 random tests.
2. Each C_T = {x: LB(x,T) <= c(5)} is a convex polytope.
3. AP-type vertices (g=1) are handled by Tier 2, not Tier 3. VERIFIED: at g=1, every permutation has some pair with |diff|=1.

### Critical gap in step 9

Step 9 claims: "For each permutation sector, template T_v (from the sector's Z-type vertex) achieves LB <= c(5) throughout the sector."

**This is FALSE as stated.** My verification shows the wrs=35 template (which creates singletons r_a = P_4-P_1-P_2, r_b = P_6-P_5 with coverage |r_a - r_b| <= L_0) covers only 7 of 31 Z-type vertices.

Each Z-type vertex v requires its OWN template T_v. The issue is: does T_v achieve LB <= c(5) at the AP-type vertices of the same sector? If not, the convexity argument does not close the sector interior.

**However**, the explorer reports provide an escape: AP-type vertices are on the g=1 boundary where Tier 2 pairwise strategies apply. The convexity argument should be:

1. For each permutation sector with Z-type vertex v, template T_v gives LB(v, T_v) <= c(5).
2. The sector boundary consists of: (a) Z-type faces (v_0=0), (b) AP-type faces (g=1).
3. At the Z-type vertex: LB(v, T_v) <= c(5) by construction.
4. At AP-type vertices of the same sector: LB may exceed c(5) for T_v, BUT Tier 2 handles these separately.
5. The sector interior: By convexity, max of LB(x, T_v) over the sector is at a vertex. If the only vertices in the sector are v (Z-type) and AP-type (handled by Tier 2), then...

**Problem**: The convexity argument says max of LB(x, T_v) is at a sector vertex. If LB(v_AP, T_v) > c(5) for some AP vertex v_AP in the sector, then interior points near v_AP might have LB(x, T_v) > c(5). Tier 2 handles v_AP itself, but does NOT handle the interior.

**Fix needed**: Either:
(a) Verify LB(v_AP, T_v) <= c(5) for all AP vertices v_AP in each sector (algebraic check per sector), OR
(b) Switch to LP coverage: union of C_{T_v} for all 360 templates covers the Tier 3 region.

### Load-bearing lemmas

- **LB(x,T) convexity**: CORRECT mechanism stated (sum of k largest = max over subsets).
- **Single-template sufficiency per sector**: INCORRECT as stated. Needs the fix above.
- **62 AP-type = Tier 2**: CORRECT mechanism (g=1 means some pairwise diff = 1).

### Issues to fix

1. Step 9: Add verification that LB(v_AP, T_v) <= c(5) for AP vertices in each sector, OR switch to LP coverage (step 10) as primary path.
2. Clarify that 360 templates are needed (one per Z-type vertex times multiple sectors), not one global template.

---

## Approach: n5-lp-direct (new)

**Verdict: APPROVE**

### Right technique?

Yes. LP feasibility is the correct tool for checking if a union of convex slabs covers a polytope. Each (2,2,1) template T gives coverage set C_T = {x: |A_T . x + c_T| <= 1}, a convex slab.

### Sound skeleton?

Steps 1-5 are correct:
- Tier 1/2: already proved
- 360 template enumeration: correct count
- Coverage condition is half-spaces: correct
- LP formulation: correct (though 2^360 sign-combo is infeasible)

### Critical gap in step 6

The outline correctly identifies the computational infeasibility of 2^360 LP checks. However, the explorers found:
- Sampling shows 100% coverage with margin >= 0.005
- Only ~10-31 templates are actually needed (one per Z-type vertex)
- The LP reduces to: "exists x in Tier 3 with LB(x, T_v) > c(5) for all 31 Z-type templates T_v?" — a single LP with ~62 constraints

### Load-bearing lemmas

- **Each C_T is a convex slab**: CORRECT mechanism (|linear form| <= L_0 is two half-spaces)
- **LP coverage is finite**: CORRECT (5D polytope, ~60 constraints)

### No fatal flaws

The approach is sound. The 2^360 issue is surmountable by restricting to the 31 Z-type templates.

---

## Approach: n5-sector-decomposition (new)

**Verdict: CHANGES REQUESTED**

### Right technique?

Partially. Partitioning by permutation sectors is valid, but:
1. There are only ~31 non-empty sectors with Z-type vertices (not 720 — most orderings give wrs outside {35,...,42}).
2. The "one template per sector suffices" claim is a CONJECTURE without the AP-vertex check.

### Sound skeleton?

Steps 1-4 are correct. Step 5 has the same gap as n5-convex-coverage step 9: need to verify LB(v_AP, T_sigma) <= c(5) for AP vertices in each sector.

### Issues to fix

Same as n5-convex-coverage: add LP fallback or algebraic verification of AP-vertex coverage.

---

## Approach: n5-full-algebraic (new)

**Verdict: CHANGES REQUESTED**

### Right technique?

Exact rational arithmetic for all 31 Z-type vertices is rigorous. However:
1. Step 5 (closure argument) is explicitly labeled "hand-wavy" and acknowledged to need LP fallback.
2. The margin argument (step 4) requires explicit Lipschitz bound and polytope diameter.

### Sound skeleton?

- Step 2 (31 exact proofs): LABOR-INTENSIVE but sound. Only 1/31 done.
- Step 4 (convexity + positive margin): Valid in principle but needs quantitative bounds.
- Step 5 (closure): HAND-WAVY as noted. Falls back to LP.

### Issues to fix

1. If pursuing, provide Lipschitz bound and polytope diameter to make step 4 rigorous.
2. More realistically: complete the 31 exact proofs and use LP coverage for interior.

---

## Approach: geometric-direct (advance)

**Verdict: APPROVE** (as scaffolding)

This is the parent approach. It delegates n=5 to the other approaches. No independent skeleton to review.

---

## Summary Table

| Approach | Verdict | Key Issue |
|----------|---------|-----------|
| n5-convex-coverage | CHANGES REQUESTED | Step 9 (single-template sufficiency) needs AP-vertex verification or LP fallback |
| n5-lp-direct | APPROVE | Sound; 2^360 issue is surmountable |
| n5-sector-decomposition | CHANGES REQUESTED | Same gap as n5-convex-coverage |
| n5-full-algebraic | CHANGES REQUESTED | Closure argument needs quantitative bounds or LP fallback |
| geometric-direct | APPROVE | Parent approach, delegates n=5 |

---

## Ranking Comparisons

Comparing approaches across the field:

1. **n5-lp-direct > n5-convex-coverage**: LP is the cleaner fallback that n5-convex-coverage itself identifies; n5-lp-direct makes it the primary path.

2. **n5-convex-coverage > n5-sector-decomposition**: n5-convex-coverage is essentially n5-sector-decomposition with better acknowledgment of the LP fallback.

3. **n5-convex-coverage > n5-full-algebraic**: Convexity+LP is more tractable than 31 exact proofs.

4. **n5-lp-direct > n5-five-mark**: n5-lp-direct addresses the gap found in n5-five-mark.

5. **geometric-direct > induction-on-n**: induction-on-n is dead-ended.

6. **n5-lp-direct > minimax-saddle-point**: n5-lp-direct targets the specific gap; minimax is speculative.

---

## Registrations

New approaches to register:
- **n5-lp-direct** (new): "LP feasibility for 360 template slabs covering Tier 3"
- **n5-sector-decomposition** (new): "Partition Tier 3 into permutation sectors, one template each"
- **n5-full-algebraic** (new): "31 Z-type exact rational proofs + LP closure"

n5-convex-coverage is a revision of n5-five-mark (already registered, slug unchanged).

---

## Build Set

The most promising path to close the gap this round:

1. **n5-lp-direct**: The LP approach is the cleanest fallback acknowledged by all other approaches. It reduces to a single LP with ~62 constraints (two per Z-type vertex template). This is computationally tractable and provides a rigorous certificate.

2. **n5-convex-coverage**: The convexity structure is valuable even if the single-template claim needs amendment. The builder should focus on the LP fallback (step 10) rather than trying to prove step 9 algebraically.

**build set: n5-lp-direct, n5-convex-coverage**

---

## Notes for Builders

**n5-lp-direct builder**: The key computation is:
1. For each of the 31 Z-type vertices, identify the template T_v (the coverage condition is |A . x + c| <= 1 for some linear form A, constant c).
2. Run LP: find x in Tier 3 region satisfying |A_v . x + c_v| > 1 for ALL 31 templates simultaneously.
3. If infeasible (expected based on sampling), extract Farkas certificate for algebraic proof.

**n5-convex-coverage builder**: The convexity lemma (LB(x,T) is convex) is the key contribution. For the interior coverage, invoke the LP coverage from n5-lp-direct rather than trying to prove single-template sufficiency per sector.
