# Outline Review - Round 3

## Summary of Verification

I numerically verified the central claims:
- Key Lemma (A' on circumcircle of AKL): Holds to Im(CR) ~ 1e-12
- OM = ON: Holds to 1e-12
- Inversion collinearity (A*, K*, L* collinear): Holds to 6e-11

The numerical verification confirms that ALL proposed approaches target a true statement. The question is whether any skeleton provides a viable path to a rigorous proof.

---

## inversion-collinearity (NEW)

**Technique:** Invert at A' with radius |A'B| = |A'C|, transforming the Key Lemma (A' on circumcircle AKL) to collinearity (A*, K*, L* collinear), then prove collinearity via Menelaus or directed angles.

**Assessment:**

1. **Steps 1-4 are correct.** The inversion setup is sound:
   - B and C are fixed (lie on the inversion circle) - VERIFIED
   - A* lies on the horizontal y = b - VERIFIED
   - Circumcircle through center A' maps to a line - standard inversion fact

2. **Step 5 (angle preservation at B, C) is correct.** Inversion is conformal at non-center points, and B, C are fixed, so angles at these vertices are preserved.

3. **Step 8 (collinearity proof via Menelaus) is the GAP.** The outline claims the angles at N* and M* (transformed C2 and C3) force collinearity, but:
   - N and M are NOT fixed under this inversion - they map to circles
   - The angle conditions at N and M become circle-circle tangent angle conditions, not line-line angles
   - The "Watch out for" note acknowledges this but provides no mechanism to handle it

**Issues:**
- The Menelaus condition requires explicit computation of the transversal K*L* cutting triangle BCA*. The outline gives no mechanism for computing where K* and L* lie on specific rays - it states "Ray construction" but doesn't show how the distances |BK*| and |CL*| are determined from the angle conditions.
- The outline says "Menelaus on a suitable triangle" but doesn't specify which triangle or how the angle conditions translate to Menelaus ratios.

**Verdict: CHANGES REQUESTED**

The technique is viable (inversion collinearity is a standard move), but Step 8 needs a concrete mechanism. Specifically:
- Show how the transformed C2 (at B and N*) and C3 (at C and M*) constraints determine K* and L* positions
- State the specific Menelaus triangle and show how the transversal ratios follow from the angle conditions

---

## trig-identity-direct (NEW)

**Technique:** Substitute explicit trig formulas for K and L into the cross-ratio condition Im[(A-K)(A'-L)/((A-L)(A'-K))] = 0, using constraints (*) and (**) to eliminate mu and nu.

**Assessment:**

1. **Steps 1-4 are correct.** The coordinate setup and Law of Sines formulas for BK and CL are already proved in existing approaches.

2. **Steps 5-6 (constraints * and **):** The explorer derived these trigonometric constraints and numerically verified them. They ARE correct formulations of C2 and C3 in pure trig form.

3. **Steps 7-8 (algebraic verification) is the GAP.** This is a direct computation approach - substitute everything in and simplify. The outline provides:
   - The explicit form of the identity to prove
   - The constraints that hold
   - But NO mechanism for why the identity should simplify to 0

**Issues:**
- This is essentially "brute force symbolic algebra" - it's valid but unguided. The power-of-point approach already tried this in Round 1 and reported "symbolic computation produces a complicated trigonometric expression that does not simplify cleanly."
- No product-to-sum strategy is specified; no factorization insight is given.
- The constraint coupling (mu depends on K's position, which depends on nu) makes the algebra intricate.

**Verdict: CHANGES REQUESTED**

The technique is viable but needs guidance on the simplification strategy:
- Should one use specific product-to-sum identities? If so, which?
- Should one work with complex exponentials instead of sin/cos?
- Is there a clever combination that makes the factor vanish?

Without this, the builder will repeat Round 1's failure (expression doesn't simplify).

---

## directed-angle-concyclic (ADVANCE)

**Technique:** Directed angle chase using the symmetric pairing structure (B<->N, C<->M, A<->A').

**Assessment:**

1. **Steps 1-3 are unchanged** from Round 1 (setup and Key Reduction proved).

2. **Step 4 (NEW: symmetric pairing structure):** This is an OBSERVATION, not a mechanism. The explorer noted B<->N (from C2), C<->M (from C3), A<->A' (Key Lemma), but calling this a "symmetric pairing" doesn't explain WHY the Key Lemma follows.

3. **Step 5 (NEW: decompose angle difference):** The outline says "The 'lift' from {B,C} to {M,N} via C2 and C3, then from {M,N} to {A,A'} via the midpoint structure." This is hand-waving - no concrete angle chain is given.

4. **Step 6 (C1 untwists):** Numerically verified that C2+C3 alone give ~1% error; C1 is needed. But saying "C1 untwists" is not a mechanism.

**Issues:**
- No concrete directed angle chain. "Lift" and "twist" are metaphors, not proofs.
- The "symmetric pairing" observation is structurally interesting but doesn't directly yield angle equalities.
- Step 5 says "GAP" explicitly but gives no approach to closing it.

**Verdict: CHANGES REQUESTED**

The outline acknowledges the gap but provides no new mechanism to close it. For this to advance, the builder needs:
- A specific sequence of inscribed angle equalities or directed angle substitutions
- Explicit use of C1, C2, C3 in the chain (not just "C1 untwists")

---

## power-of-point (ADVANCE)

**Technique:** Use explicit trig constraints (*) and (**) to simplify the algebraic identity for the power condition.

**Assessment:**

1. **Steps 1-4 are unchanged** (power identity reduction proved).

2. **Steps 5-6 (NEW: use constraints * and ** for simplification):** The explorer's trig constraints DO capture C2 and C3. The outline says "substitute into the algebraic identity... the identity should reduce to 0=0."

**Issues:**
- This is the SAME gap as Round 1 - algebraic simplification of a complicated trig expression.
- The outline says "identity should reduce" but gives no mechanism for why.
- No new technique is introduced beyond "use the constraints."

**Verdict: CHANGES REQUESTED**

Adding the explicit constraints (*) and (**) is incrementally helpful, but doesn't provide a simplification strategy. Same issue as trig-identity-direct.

---

## complex-coords (ADVANCE)

**Technique:** Show that C2 and C3 (in complex "real ratio" form) together with C1 (s*t real positive) force the Key Lemma's cross-ratio to be real.

**Assessment:**

1. **Steps 1-3 are unchanged.**

2. **Step 4 (NEW: C2 and C3 in complex form):** The explorer found that C2 is equivalent to K(N-L)/(L(A-1)) being real, and C3 is equivalent to A(C-K)/((C-L)(K-M)) being real. These are correct formulations.

3. **Step 5 (product C2*C3 is real):** Numerically verified as -0.888. Both conditions kill one imaginary-part degree of freedom each.

4. **Step 6 (GAP):** "Show that the two 'real' conditions... force the Key Lemma's Im[...] = 0."

**Issues:**
- The algebraic path from "two things are real" to "a third thing is real" is NOT obvious. The outline says "may need to find the right combination/quotient" - this is not a mechanism.
- The explorer checked 12 combinations of R1*R2/R3 etc. and NONE gave R_KL. So simple product/quotient combinations don't work.

**Verdict: CHANGES REQUESTED**

The complex formulation is cleaner than real coordinates, but the gap remains: why do two "real" constraints force a third? The builder needs guidance on what algebraic manipulation might work.

---

## spiral-similarity (DEAD)

**Verdict: CONFIRMED DEAD**

The outliner correctly marks this as dead. Numerical verification shows spiral similarity centered at L (B->N, K->C) has error 1.95, far from zero. Do not revive.

---

## Ranking Assessment

All five live approaches reduce to the SAME gap: proving the Key Lemma (A' on circumcircle AKL) from the angle conditions. The differences are:

1. **inversion-collinearity** - Transforms the problem to collinearity, which may be easier to prove synthetically
2. **trig-identity-direct** - Direct algebraic verification (same approach that failed in Round 1)
3. **directed-angle-concyclic** - Angle chase (no new mechanism provided)
4. **power-of-point** - Algebraic identity (same approach that failed in Round 1)
5. **complex-coords** - Complex algebra (slightly cleaner form, but same gap)

The **inversion-collinearity** approach stands out as the most promising because:
- It transforms to a potentially easier sub-problem (collinearity vs. concyclicity)
- The collinearity condition can be attacked by Menelaus or by direct computation
- The angles at B and C are preserved, so C1 conditions translate cleanly

The algebraic approaches (trig-identity-direct, power-of-point, complex-coords) all face the same obstacle: simplifying a complicated expression. Without a new algebraic insight, they're likely to repeat Round 1's failure.

The directed-angle-concyclic approach has structural insight (the "pairing") but no concrete mechanism.

---

## Registrations

Two NEW approaches to register:
- `inversion-collinearity`
- `trig-identity-direct`

## Ranking Comparisons

Based on my assessment:
- `inversion-collinearity` > `directed-angle-concyclic` (new technique vs. no new mechanism)
- `inversion-collinearity` > `power-of-point` (transforms problem vs. brute force algebra)
- `inversion-collinearity` > `complex-coords` (transforms problem vs. algebra)
- `inversion-collinearity` > `trig-identity-direct` (transforms problem vs. algebra that already failed)
- `complex-coords` > `trig-identity-direct` (cleaner formulation)
- `directed-angle-concyclic` vs `power-of-point` (draw - both stuck at same gap without new ideas)

---

## Build Set

The build set should prioritize:
1. **inversion-collinearity** - The most promising new approach; the transformation to collinearity may unlock progress
2. **complex-coords** - The cleanest algebraic formulation; worth one more attempt with the new "two real conditions" insight
3. **directed-angle-concyclic** - The structural "pairing" insight might lead somewhere if the builder can find a concrete angle chain

Skip power-of-point and trig-identity-direct for this round - they're essentially the same as approaches that stalled in Round 1, with no new mechanism.

---

build set: inversion-collinearity, complex-coords, directed-angle-concyclic
