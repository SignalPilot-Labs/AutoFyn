## imo-2026-02 (Synthetic Structure Lens)

### Problem restatement
Triangle ABC, M = midpoint AB, N = midpoint AC. Points K inside BMC, L inside BNC. Conditions:
1. ∠KBA = ∠ACL (= α)
2. ∠LBK = ∠LNC (= β)
3. ∠LCK = ∠BMK (= γ)

O = circumcenter of AKL. Prove OM = ON.

---

### Prior progress
None — fresh terrain (round 1, no approaches).

---

### Distinct openings

**Opening A — Power-of-a-point reformulation (most algebraically grounded).**
OM = ON iff the power of M and N w.r.t. circumcircle(AKL) are equal. Since M is the midpoint of AB and N the midpoint of AC, a direct calculation gives:

> pow(M, circ AKL) = pow(B, circ AKL)/2 − AB²/4
> pow(N, circ AKL) = pow(C, circ AKL)/2 − AC²/4

So OM = ON is **equivalent** to:
**pow(B, circumcircle AKL) − pow(C, circumcircle AKL) = (AB² − AC²)/2.**

This is confirmed numerically to machine precision across many triangles and α-values. It reduces the proof to one clean scalar identity about the powers of B and C.

**Opening B — Algebraic identity in A-at-origin coordinates.**
Translating A to the origin, the circumcenter O satisfies 2O·K = |K|² and 2O·L = |L|². The power-of-point condition becomes the identity:

> |K|²·[(C−B)×L] − |L|²·[(C−B)×K] = (|C|²−|B|²)/2 · (K×L)

where × denotes the 2D cross product and all vectors are from A. This identity is the **direct algebraic target**: verify it using the angle conditions. Numerically confirmed. Crucially, the identity fails for arbitrary (α,β,γ): it requires the full interlocking of all three conditions.

**Opening C — Antipode reformulation.**
Let A* = 2O − A be the antipode of A on the circumcircle of AKL (so AA* is a diameter and ∠AKA* = ∠ALA* = 90°). Then:

> OM = ON ⟺ |A*B| = |A*C|

i.e., the antipode of A on the circumcircle of AKL is equidistant from B and C (lies on the perpendicular bisector of BC). This is a striking synthetic statement amenable to angle-chasing: show that A* lies on the perp-bisector of BC by exhibiting equal distances or a reflection argument.

**Opening D — Trigonometric cevian formulas.**
From the angle conditions the following formulas can be derived:
- cot(∠KAB) = cot α + 2 cot γ  (from conditions 1 and ∠BMK = γ)
- cot(∠LAC) = cot α + 2 cot β  (from conditions 1 and ∠LNC = β)
- AK = c · sin α / sin(α + ∠KAB),   AL = b · sin α / sin(α + ∠LAC)
- BK = (c/2) sin γ / sin(α+γ),       CL = (b/2) sin β / sin(α+β)
- KM = (c/2) sin α / sin(α+γ),       LN = (b/2) sin α / sin(α+β)

These give K and L explicitly once (α,β,γ) is determined. The remaining "linking" conditions — ∠LBK = β forces L on the ray from B at angle α+β from BA, and ∠LCK = γ forces K on the ray from C at angle α+γ from CA — are the additional constraints that make the identity in Opening B hold.

**Opening E — Perp-bisector of MN as locus.**
MN ∥ BC (midsegment), so the perp-bisector of MN is the line through (2A+B+C)/4 perpendicular to BC. The condition OM = ON is:

> (O − (2A+B+C)/4) · (C−B) = 0

i.e., O lies on the line through the midpoint of MN perpendicular to BC. This is the "pure synthetic" statement: the circumcenter of AKL is constrained to a specific line determined by the triangle. One can try to find two independent locus conditions (each a line) whose intersection is exactly this perp-bisector.

---

### Candidate techniques

- **Power of a point** (identity pow(B) − pow(C) = (AB²−AC²)/2): the cleanest path to the final step.
- **Trigonometric cevian / sine rule** (∠KAB and ∠LAC formulas, law of sines in triangles BMK and LNC): gives explicit coordinates for K and L in terms of α,β,γ.
- **Ptolemy / inscribed angle theorem**: relate the second intersections of BK and CL with the circumcircle of AKL to the given angles.
- **Coordinate bash** (BC on x-axis, trigonometric substitution): systematically verifiable once K,L are expressed via the angle conditions.

---

### Cheap-kill candidates

- **Symmetry check**: The three conditions are invariant under (B,M,K) ↔ (C,N,L) (conditions 2 and 3 swap, condition 1 is self-symmetric). This is a structural fact but does NOT immediately give OM = ON for a general triangle — the problem is not bilaterally symmetric.
- **Isosceles ABC**: K and L are reflections of each other across the perp-bisector of BC = perp-bisector of MN, so OM = ON follows by bilateral symmetry. Establishes the result for the special case; the general case needs more.

---

### Knowledge-base entries to use

- **Geometry (synthetic toolkit)**: spiral similarity, power of a point, radical axes, similar triangles, trig cevians (Ceva/Menelaus).
- **Circle/triangle configuration facts**: inscribed angle theorem, Miquel point of a complete quadrilateral, Simson line (for completeness check).
- **Coordinates / complex / barycentric**: coordinate placing BC on x-axis; possibly complex number circumcenter formula.
- **Trig identities & interval intersection**: the key identity cot φ = cot α + 2 cot γ is a trig identity consequence.

---

### Analogous past problems (cruxes)

Crux corpus has no geometry entries. No directly analogous problems found via the corpus.

The problem structurally resembles:
- Problems where the circumcenter of a constructed triangle lies on a specific line (perp-bisector of a midsegment) — these typically use power-of-a-point or radical axis arguments.
- Problems with isobarycentric / isogonal conditions giving circumcenter locus results.

---

### Dead ends (do not retry)

- **Concyclicity of {A,B,C,M,N,K,L} (various subsets)**: Checked all 35 quadruples — none are concyclic (for generic triangles). No clean cyclic quadrilateral emerges.
- **Spiral similarity centered at L mapping (B,K)→(N,C)**: ratios LB/LN ≠ LK/LC in general; the angle equality ∠LBK = ∠LNC does NOT imply a spiral similarity of this form.
- **K₁ (second intersection of BK with circumcircle AKL) lies on a simple known line**: checked lines BN, CM, BL — none work.
- **O on perp-bisector of KL implies O on perp-bisector of MN**: O is on perp-bisector of KL by definition (circumcenter) but KL is NOT parallel to MN, so no direct inference.

---

### Small-case / intuition notes

**Conjecture (strongly supported numerically):** The identity pow(B) − pow(C) = (AB²−AC²)/2 holds for ALL valid (α,β,γ) satisfying the three conditions. It fails for arbitrary (α,β,γ) — all three conditions are needed jointly. The linking conditions ∠LBK = β (forces L on a specific ray from B) and ∠LCK = γ (forces K on a specific ray from C) are the essential "interlocking" that makes the identity hold.

**Conjecture (numerical):** The circumcenter O traces out the entire perpendicular bisector of MN as α varies over the admissible range — the 1-parameter family of valid configurations sweeps this line.

**Key numerical fact verified:** For every valid configuration tested (6+ triangles, 3–5 α-values each): OM = ON to machine precision (< 10⁻¹⁴). The identity pow(B) − pow(C) = (AB²−AC²)/2 also holds to machine precision.

**Clean formula:** cot(∠KAB) = cot α + 2 cot γ and cot(∠LAC) = cot α + 2 cot β. These are exact algebraic consequences of the sine-rule in triangles BMK and LNC respectively. They give the angles that AK and AL make with AB and AC at vertex A, which is the key input for computing the circumcenter of AKL.
