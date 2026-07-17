## imo-2026-02

### Problem recap
Triangle ABC, M = midpoint AB, N = midpoint AC. K inside triangle BMC, L inside triangle BNC.
Conditions:
1. ∠KBA = ∠ACL (= α)
2. ∠LBK = ∠LNC (= β)
3. ∠LCK = ∠BMK (= γ)
O = circumcenter of AKL. Prove OM = ON.

---

## Distinct openings

**Opening 1: Algebraic reformulation as a single clean identity.**

OM = ON is equivalent to O lying on the perpendicular bisector of MN. In coordinates where BC is horizontal, the perpendicular bisector of MN is the vertical line x = (2A_x + B_x + C_x)/4. Numerically confirmed (error < 1e-15) for multiple (K,L) pairs satisfying all three conditions.

The cleanest algebraic form: **4(B–C)·(O–A) = AB² – AC²** (Euclidean dot product). This is a single linear condition on the circumcenter O.

Equivalently, since the circumcenter O_0 = O–A (relative to A) satisfies 2(K–A)·O_0 = |K–A|² and 2(L–A)·O_0 = |L–A|² (the standard circumcenter equations with A at origin), the condition OM = ON reduces to showing:

**4(b–c)·O_0 = |b|² – |c|²**   (b = B–A, c = C–A, O_0 = O–A)

This is the fundamental identity to prove. The LHS is a dot product involving O_0, expressed via the circumcenter equations; the RHS depends only on the triangle geometry.

**Opening 2: Power of midpoints reformulation.**

OM = ON iff the powers of M and N w.r.t. the circumcircle ω of AKL are equal.

pow(M, ω) = MA · MA_M   where A_M = second intersection of line AB with ω.
pow(N, ω) = NA · NA_N   where A_N = second intersection of line AC with ω.

Since MA = AB/2 and NA = AC/2:
OM = ON ⟺ **(AB/2)·MA_M = (AC/2)·NA_N**

Numerically: MA_M · AB = NA_N · AC = –0.323 (constant across all valid (K,L) pairs). This is a clean "lever" identity.

Key: A_M is on line AB (= line through A and M) and on the circumcircle of AKL. A_N is on line AC and on the circumcircle of AKL. The three angle conditions must force the power balance.

**Opening 3: Sine-rule formulas from conditions 2 and 3.**

Conditions 2 and 3 give, via the sine rule in triangles BMK and CLN:

In triangle BMK (with ∠MBK = α, ∠BMK = γ, ∠BKM = π–α–γ, BM = AB/2):
**BK = (AB/2) · sin γ / sin(α+γ)**

In triangle CLN (with ∠NCL = α, ∠LNC = β, ∠CLN = π–α–β, CN = AC/2):
**CL = (AC/2) · sin β / sin(α+β)**

These are explicit, exact formulas for BK and CL in terms of the angles. These characterize the distances from vertices to the interior points K and L and could be used to express the circumcenter position of AKL directly.

**Opening 4: The σ-symmetry and why it can't be used naively.**

Define σ: (A,B,C,K,L,M,N) → (A,C,B,L,K,N,M). Then:
- Condition 1 (∠KBA = ∠ACL) is σ-self-conjugate.
- Condition 2 (∠LBK = ∠LNC) maps under σ to condition 3 (∠LCK = ∠BMK) and vice versa.
- Triangle AKL maps to triangle ALK under σ — the SAME triangle.
- Hence O (circumcenter) is fixed by σ.
- σ maps M → N.

IF σ were a geometric isometry (fixing O and swapping M,N), then OM = ON immediately. In the isoceles case AB = AC, σ IS the reflection over the perpendicular bisector of BC, which passes through A, fixes O, and maps M↔N. So the isoceles case is trivial.

For general ABC, σ is not a geometric isometry. The perpendicular bisector of MN is NOT the perpendicular bisector of BC (they are parallel, 2× further apart from A). So the proof must use the specific angle conditions beyond just this symmetry argument.

**Opening 5: The spiral similarity S centered at A.**

Define S: z → (c/b)·z (centered at A, maps B→C, M→N). This is the spiral similarity with ratio AC/AB and rotation angle ∠BAC.

Condition 1 (∠KBA = ∠ACL) can be restated: S maps the direction from B toward K to the direction from C toward S(K), and this direction makes the same unsigned angle α with CA as CL does. Numerically verified: ∠S(K)CA = ∠LCA = α to 5 significant figures.

CRITICAL SUBTLETY: S(K) and L are on OPPOSITE sides of line CA. The signed angle from CA to CS(K) is –α, while the signed angle from CA to CL is +α. So S maps K to the "isogonal" of L at C, not to L itself.

This means: S does NOT map K to L. Instead, an isogonal reflection at C (over line CA) followed by S maps K near L. The composition "isogonal-at-C ∘ S" is the transformation that condition 1 really encodes.

**Opening 6: Complex-plane condition for OM = ON.**

With A at origin, B and C having Im(b) = Im(c) (both on the horizontal line below A):

OM = ON ⟺ Re(O_0) = (Re(b) + Re(c))/4

The circumcenter O_0 satisfies:
Re(O_0) = (|k|²·Im(l) – |l|²·Im(k)) / (2·Im(k̄l))

where k = K–A, l = L–A (complex). The three angle conditions constrain k and l to a 1-parameter locus. The above expression for Re(O_0) is CONSTANT along this locus (= (Re(b)+Re(c))/4), even though Im(O_0) varies. This strong constraint must be a consequence of the three conditions.

---

## Candidate technique(s)

- **Power of a point** combined with the sine rule in triangles BMK and CLN to compute pow(M) and pow(N).
- **Spiral similarity + isogonal conjugate**: The compound of S (centered at A, B→C) with isogonal reflection at B (for K) and at C (for L) might relate the configuration symmetrically.
- **Complex number / trigonometric identity**: Express O_0 in terms of k and l, use the three conditions (expressed as "Im(some rational function) = 0") to prove Re(O_0) = const.
- **Directed angle / inscribed angle**: Use conditions 2 and 3 (∠LBK = ∠LNC, ∠LCK = ∠BMK) as concyclicity conditions in disguise; find the right quadruples.

## Cheap-kill candidates

- **σ-symmetry in isoceles case**: For AB = AC, the perpendicular bisector of MN = the axis of symmetry; conditions force K and L to be reflections, so OM = ON trivially. The general case is the hard part.
- **Direct size check**: pow(M, ω_AKL) = pow(N, ω_AKL) means the equation 4(B–C)·(O–A) = AB²–AC² holds. This is a SINGLE scalar identity involving O, which the circumcenter equations reduce to a condition on k and l.

## Knowledge-base entries to use

- **Synthetic toolkit** (spiral similarity, power of a point, inscribed angle theorem) — "Synthetic toolkit" and "Circle/triangle configuration facts" entries.
- **Coordinates / complex / barycentric** — using complex numbers and the circumcenter formula Re(O) = (|k|²Im(l)–|l|²Im(k))/(2Im(k̄l)).
- **Trig identities & interval intersection** — the BK and CL formulas from sine rule.
- **Pólya: Work backward** and **Reformulate** — translating OM = ON into 4(B–C)·(O–A) = AB²–AC².

## Analogous past problems (cruxes)

Geometry cruxes not in the corpus (the documentation states "geometry — not in the corpus yet"). No analogous past problems available.

## Prior progress

None (round 1, no approaches yet).

## Dead ends (do not retry)

- **Concyclicity of B,K,N,L or C,L,K,M**: Numerically verified NOT concyclic (errors ~0.24, ~0.23).
- **S(K) = L (spiral centered at A maps K to L)**: S(K) ≠ L in general; they are on opposite sides of line CA (the sign of the directed angle flips).
- **Radical axis of cc(BMK) and cc(CLN) passes through O**: Numerically false (errors ~0.005).
- **O on perpendicular bisector of BC**: Numerically false in the general triangle (O_x ≠ midBC_x).

## Small-case / intuition notes

**Numerical evidence** (conjecture, confirmed to machine precision ~1e-15):

1. For A=(0.2,1), B=(-1,0), C=(1.3,0) (non-isoceles), all (K,L) satisfying the three conditions give O_x = 0.175 exactly = (2A_x+B_x+C_x)/4 and |OM–ON| < 3e-16.

2. The 1-parameter locus of valid (K,L) pairs is confirmed (3 conditions, 4 unknowns = 1D freedom).

3. **Key formula confirmed**: BK = (AB/2)·sin(γ)/sin(α+γ), CL = (AC/2)·sin(β)/sin(α+β) (errors < 1e-6).

4. **Power balance**: pow(M, ω_AKL) = pow(N, ω_AKL) = –0.162 exactly. Equivalent: MA_M · AB = NA_N · AC (= –0.323) where A_M, A_N are second intersections of lines AB, AC with the circumcircle.

5. **Nine-point center of ABC** also lies on the perpendicular bisector of MN (as expected, since the nine-point circle passes through M and N). This is a different point on the same vertical line — does NOT directly help the proof.

6. The **second intersections A_M (of line AB with circumcircle of AKL) and A_N (of line AC with circumcircle of AKL)**: s_M ≈ 0.633, s_N ≈ 0.646 (parameters from A along the respective sides). OM = ON ↔ (s_M–0.5)·AB² = (s_N–0.5)·AC² (verified numerically). This involves both the position along the side and the lengths AB, AC.
