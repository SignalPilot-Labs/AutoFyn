# Outline Review: IMO 2026 P2

## Diversity Assessment

The four approaches fall into two clusters:
1. **Algebraic cluster**: `complex-identity` and `dot-product-identity` are essentially the same approach in different notation (complex vs. real coordinates). Both reduce OM = ON to the identity `4(b-c).O_0 = |b|^2 - |c|^2` and both have the same gap: algebraic elimination from the three angle conditions.
2. **Geometric/Conceptual cluster**: `power-balance` (power of a point + lever identity) and `sigma-symmetry` (symmetry + identity principle).

**Warning**: The algebraic cluster is too close together. If the algebraic elimination fails (e.g., the identities don't simplify cleanly), both approaches fail simultaneously. However, for round 1, exploring both algebraic and geometric routes is appropriate.

---

## Approach: power-balance

**Verdict: APPROVE**

**Strengths:**
- Clean reformulation: OM = ON iff pow(M) = pow(N) w.r.t. circumcircle of AKL
- The lever identity AB.MP_B = AC.NP_N is concrete and verifiable
- Sine-rule formulas BK = (AB/2)sin(gamma)/sin(alpha+gamma) and CL = (AC/2)sin(beta)/sin(alpha+beta) are correct and provide explicit handles on K and L
- Conditions (ii) and (iii) directly involve midpoints M and N, giving hope that these control the positions of P_B and P_N

**Concerns:**
- Gap 1 (lever identity derivation) is substantial but tractable. The explorer reports confirm the structure is correct numerically.
- The connection from angle conditions to P_B and P_N positions needs to be spelled out more explicitly, but the inscribed angle mechanism is sound.

**The gap has a mechanism**: The inscribed angle theorem at P_B gives angle(KP_B L) = angle(KAL), and condition (iii) involves angle(BMK) = gamma, which constrains the arc. This is a valid synthetic route.

---

## Approach: complex-identity

**Verdict: APPROVE**

**Strengths:**
- The encoding is correct: (C1) bc/((k-b)(l-c)) in R, (C2) (k-b)(2l-c)/((l-b)c) in R, (C3) b(k-c)/((l-c)(2k-b)) in R
- The "factor of 2" structure (2l-c and 2k-b encode midpoints N and M) is the key insight that connects the conditions to the conclusion
- The target identity Re(O_0(conj(c)-conj(b))) = (|c|^2-|b|^2)/4 is correct

**Concerns:**
- Gap 1 (algebraic elimination) is substantial. This requires either CAS or clever manipulation. The explorer notes this is "computationally feasible but extremely messy by hand."
- The signed angle convention is critical and correctly noted.

**The gap has a mechanism**: The three real-ratio conditions give three polynomial equations in 4 real unknowns (Re(k), Im(k), Re(l), Im(l)), defining a 1D family. The target is a polynomial identity that must hold on this 1D family. This is verifiable by resultants or Groebner bases.

---

## Approach: sigma-symmetry

**Verdict: CHANGES REQUESTED**

**Strengths:**
- Conceptually elegant: sigma-symmetry (B<->C, K<->L, M<->N) is self-conjugate
- Isoceles case (AB = AC) is trivially solved by reflection symmetry

**Critical Issue:**
- **Step 6 (identity principle) is under-specified.** The outline says "use identity principle: OM=ON is polynomial identity, holds on isoceles dense locus => holds everywhere." But:
  1. The isoceles locus is NOT Zariski-dense in the space of all triangles with valid (K,L) pairs
  2. The constraint manifold (K,L satisfying the angle conditions for a given triangle) depends on the triangle; it's not a single algebraic variety over all triangles
  3. The identity principle requires OM=ON to hold on a Zariski-dense subset of an irreducible variety; this setup doesn't obviously fit

**Required fix**: Either:
  (a) Prove the constraint manifold (over all triangles) is irreducible and the isoceles locus is Zariski-dense, OR
  (b) Abandon the identity principle route and give a direct algebraic proof that f = |OM|^2 - |ON|^2 = 0 on the constraint manifold, OR
  (c) Show sigma acts as a geometric isometry in some transformed coordinate system

The step 5 "direct sigma argument" is incomplete as noted in the outline itself. This approach needs significant rethinking of its main gap.

---

## Approach: dot-product-identity

**Verdict: APPROVE**

**Strengths:**
- The reformulation 4(b-c).O_0 = |b|^2 - |c|^2 is correct and clean
- The circumcenter formula is standard and correctly stated
- Explicitly notes the "midpoint factors" in conditions (C2) and (C3)

**Concerns:**
- Gap 1 is essentially identical to the gap in `complex-identity`. Both approaches reduce to the same algebraic elimination.
- This is a variant of `complex-identity`, not a genuinely distinct approach.

**Recommendation**: Since this is so close to `complex-identity`, only one of them needs to be built. Build `complex-identity` (which has more explicit detail) and skip this one unless `complex-identity` fails.

---

## Small-Case Sanity Check

The explorers have already verified OM = ON numerically to machine precision (< 1e-11) for multiple triangles and multiple values of alpha. The key structural observations are confirmed:
- Target O_x = (2*A_x + B_x + C_x)/4 = midpoint of M_x and N_x
- The sine-rule formulas for BK and CL are correct
- K, L, M, N are NOT concyclic (ruling out some naive approaches)

---

## Dead Ends (from explorer reports, do not retry)

- K,L,M,N concyclic: FALSE
- Spiral similarity S(K) = L: FALSE (S(K) and L are on opposite sides of CA)
- Radical axis of cc(BMK) and cc(CLN) passes through O: FALSE
- Unsigned angle encoding: Gives wrong system

---

## Ranking Update

Registered all four approaches. Initial rankings:
1. power-balance (Elo 1513) - synthetic, different framing from algebraic
2. complex-identity (Elo 1502) - algebraic with explicit encoding
3. dot-product-identity (Elo 1501) - essentially same as complex-identity
4. sigma-symmetry (Elo 1484) - conceptually elegant but risky gap

---

## Build Set Selection

For round 1, select approaches with different framings to maximize coverage:

1. **power-balance**: Synthetic geometric approach (lever identity via power of point)
2. **complex-identity**: Algebraic approach (eliminate via real-ratio conditions)

Skip `dot-product-identity` (too close to `complex-identity`) and `sigma-symmetry` (needs rework of the identity-principle gap).

---

build set: power-balance, complex-identity
