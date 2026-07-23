# IMO 2026 P2 — Synthetic/Spiral Route Exploration

## Key Constructions Explored

### 1. Antipode Reformulation (Most Promising)

With A = 0, the circumcenter O satisfies R = |O| (since A is on the circle). The **antipode of A** in the circumcircle of AKL is:

**A\* = 2O**

The condition OM = ON (with M = B/2, N = C/2) is equivalent to: **A\* = 2O is equidistant from B and C**, i.e., A\* lies on the perpendicular bisector of BC.

Why: |O - B/2| = |O - C/2| iff |2O - B| = |2O - C| iff |A\* - B| = |A\* - C|.

**Properties of A\*:**
- A\* lies on the circumcircle of AKL (it's the antipode of A).
- AA\* is a diameter of the circumcircle of AKL.
- **∠AKA\* = 90°** (angle in semicircle at K). A\*K ⊥ AK at K.
- **∠ALA\* = 90°** (angle in semicircle at L). A\*L ⊥ AL at L.

This means: A\* is the unique intersection of the line through K perpendicular to AK and the line through L perpendicular to AL. In complex coordinates with A=0:

A\* = k(1 − iλ) = l(1 − iμ) for real λ, μ.

So the condition A\* equidistant from B and C becomes: the intersection of (line through K ⊥ to AK) and (line through L ⊥ to AL) lies on perp bisector of BC.

### 2. Derived "Pure" Conditions D1 and D2

From C1+C2 (eliminating the shared angle α): **D1: B(L−N)/((L−C)(L−B)) ∈ ℝ**

From C1+C3 (eliminating α): **D2: (K−C)(K−B)/(C(2K−B)) ∈ ℝ**

These are conditions on K only (D2) and L only (D1).

**Geometric identification of D1 and D2 loci** (verified for b=1, c=i via SymPy):

- **D2 locus**: The cubic 2(kr)³ − 3(kr)² + 2(kr)(ki)² + kr − (ki)² + ki = 0, which:
  - Passes through A=0, B=1, C=i, M=1/2
  - **Is tangent to line BC at B** (double root at B on BC)
  - Factors as (2kr−1)(kr²−kr+(ki)²) + ki = 0 i.e., Re(2K−B)·pow(K, ω_AB) + Im(K) = 0 where ω_AB is the circle with diameter AB.

- **D1 locus**: Same cubic but with (x,y)=(li,lr) i.e., 2(li)³−3(li)²+2(li)(lr)²+li−(lr)²+lr = 0, which:
  - Passes through A=0, B=1, C=i, N=i/2
  - **Is tangent to line BC at C** (double root at C on BC; confirmed by sigma symmetry)

The two cubics are related by the sigma symmetry B↔C, K↔L, M↔N.

### 3. Groebner Basis Analysis

**Critical finding**: T (the target polynomial, = 0 is equivalent to OM=ON) does **NOT** lie in the ideal (C1, C2, C3) over Q. Explicit reduction gives a nonzero remainder. This means:

- The purely algebraic approach "T ∈ ideal(C1, C2, C3)" **cannot work**.
- T vanishes on the RADICAL of the variety (proven numerically), but is not in the ideal itself.
- The degenerate components of V(C1, C2, C3) (K on line BC, K on line AB, L on line BC) are where T does NOT vanish; the proof needs to use the "interior" conditions.

The Groebner basis G1 = (ki + kr − 1)·(quadratic) reveals that ki+kr=1 (line BC) is a spurious component. The proof must be restricted to the non-degenerate main component.

### 4. Sigma Symmetry (Not a Direct Proof)

The transformation σ: (A,B,C,K,L,M,N) → (A,C,B,L,K,N,M) is a SYMMETRY of the angle conditions {C1, C2, C3} (C1 is self-symmetric; C2 ↔ C3 under σ). Under σ, triangle AKL is unchanged (just K↔L relabeling), so O is fixed. And M↔N. This means the problem's conditions are "self-symmetric" under swapping B↔C, but this is a relabeling, NOT a geometric isometry in general. It does NOT directly prove OM = ON.

### 5. Concyclicity Tests

**B, K, N, L NOT concyclic** from C2 alone (C2 says angle at B from BL to BK = angle at N from NL to NC, which is NOT the standard concyclicity cross-ratio condition).

**K, L, M, N NOT necessarily concyclic** (no clean circle through all four found).

The conditions C2 and C3 do NOT correspond to standard concyclicity of "nice" quadruples.

---

## Most Promising Synthetic Route

**The Antipode + Perpendicularity Route:**

The problem reduces to: prove A\* = 2O lies on the perpendicular bisector of BC, where A\* has the geometric properties:
- A\*K ⊥ AK (so A\* is on the line through K perpendicular to AK)
- A\*L ⊥ AL (so A\* is on the line through L perpendicular to AL)

The angle conditions C2 and C3 involve midpoints N = C/2 and M = B/2 in a "cross" structure:
- C2: angle at B (from BL to BK) = angle at N (from NL to NC)  ← connects B to midpoint of AC
- C3: angle at C (from CL to CK) = angle at M (from MB to MK)  ← connects C to midpoint of AB

The key step would be: show that the intersection of (K-perpendicular to AK) and (L-perpendicular to AL) — which is A\* — is forced by conditions C2 and C3 onto the perpendicular bisector of BC.

**Possible mechanism**: C3 says ∠BMK = ∠LCK. Since A\*K ⊥ AK (so A\*K ⊥ OK direction), the angle that A\* "makes" with K relative to A can be related to C3's condition through the inscribed angle theorem (B, M on the circumcircle of A\*K? No. But K sees A and A\* at 90°, so K lies on the circle with diameter AA\*, and C3's angle condition at M might force A\* toward the perpendicular bisector of BC.)

**Secondary approach**: Power-of-point via D1 and D2. Since K is on the D2 cubic (passing through A, B, C, M with tangency to BC at B) and L is on the D1 cubic (passing through A, B, C, N with tangency to BC at C), these cubics define the geometric locus. The equal-power condition pow(M, circumcircle AKL) = pow(N, circumcircle AKL) might follow from the specific way K on D2 and L on D1 interact with the circumcircle.

---

## Dead Ends

1. **Algebraic ideal membership**: T ∉ (C1, C2, C3) as polynomial ideal. Do NOT retry this approach without adding supplementary conditions.

2. **Concyclicity of B, K, N, L or C, L, M, K**: C2 and C3 do NOT state these concyclicities. Repeated checking of different quadruples showed no clean concyclicity condition.

3. **Spiral S(K) = L**: Already confirmed dead in Round 1. No spiral centered at O or elsewhere cleanly maps K to L.

4. **Isogonal conjugate interpretation**: C1 is a "balanced isogonal" condition (angle at B from BA to BK = angle at C from CA to CL), but K and L are not isogonal conjugates w.r.t. any sub-triangle in a clean sense.

5. **Nine-point circle**: The condition pow(M, 9-point circle of AKL) = pow(N, 9-pt circle) requires Re(O(C̄−B̄)) = (|C|²−|B|²)/2, which is TWICE the actual target. Wrong circle.

---

## Recommended Next Steps for the Outliner

**Primary direction** (new approach): Develop a proof via the **antipode A\* = 2O**. The steps:
1. Establish that A\* is the intersection of (line through K ⊥ AK) and (line through L ⊥ AL).
2. Use conditions C2 and C3 to show A\*B = A\*C.

   One path: C3 says ∠BMK = ∠LCK. Since M = B/2 and 2K−B = 2(K−M), the condition C3 links the geometry of K with respect to M and C. The line through K ⊥ AK passes through A\*. If this line intersects the circle through B and C at specific points forced by C3 and C2, that might constrain A\* to the perp bisector.

3. Use C1 to link the AK and AL perpendicular directions.

**Secondary direction** (advance existing): For the algebraic approach, instead of showing T ∈ ideal(C1, C2, C3), show T ∈ radical by finding k such that T^k ∈ ideal (likely k=2 based on double roots in Groebner basis). Or add the explicit constraint "K inside BMC" as an additional condition that removes the spurious components.

**Third direction** (new): Use the D2 cubic (for K through A,B,C,M, tangent to BC at B) and D1 cubic (for L through A,B,C,N, tangent to BC at C). These are classical curves associated with the triangle's midpoints. Study their intersection with the circumcircle of AKL and how the power of M and N with respect to circumcircle(AKL) is forced equal.
