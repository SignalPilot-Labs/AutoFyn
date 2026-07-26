## imo-2026-02 (transformation / inversion / reflection / projective route)

### Setup recap (notation)
Let H = homothety centered A, factor 1/2: H(B)=M, H(C)=N, H maps line BC to line MN (MN ∥ BC, |MN|=|BC|/2). Let D = H^{-1} = dilation centered A, factor 2: D(M)=B, D(N)=C, D(K)=K* (A,K,K* collinear, AK*=2·AK), D(L)=L*. Let O* = D(O) = circumcenter of △AK*L* (D carries circumcircle of AKL to circumcircle of AK*L*, center to center).

### Distinct openings (each a rival framing the outliner could build into a slug)

**Opening A — Homothety + equal-power (the cleanest transformation reformulation).**
OM = ON  ⟺  O ∈ perp bisector of MN. Because H is a similarity, perp bisector of MN = H(perp bisector of BC). Applying D:
  OM = ON  ⟺  O* ∈ perp bisector of BC  ⟺  O*B = O*C  ⟺  |O*B|² − R*² = |O*C|² − R*²  (R* = circumradius of △AK*L*, since O*A = R*)
  ⟺  Pow_{circle(AK*L*)}(B) = Pow_{circle(AK*L*)}(C).
So the asymmetric "OM=ON" becomes the symmetric statement "B and C have equal power wrt the circumcircle of A K* L*." Numerically verified (B,C powers equal to ~1.415 in test triangle; O*B=O*C=2.133). The angle conditions (transformed under D) must then yield this equality. Work needed: decode conditions under D — they become
  (1) ∠KBA = ∠ACL  →  ∠K* B' A = ∠A C' L*   with B'=D(B)=2B, C'=D(C)=2C
  (2) ∠LBK = ∠LNC  →  ∠L* B' K* = ∠L* C K*   (N→C under D)
  (3) ∠LCK = ∠BMK  →  ∠L* C' K* = ∠B M* K*  (M→B, so this becomes ∠L* C' K* = ∠B B K*??)
Check (3) carefully: D sends M→B, so ∠BMK (at M, rays MB,MK) becomes ∠(D(B)=B') (D(M)=B) (D(K)=K*) = angle at B between B' and K*. So (3) ↔ ∠L* C' K* = ∠(at B between B' and K*). The transformed conditions live on the dilated picture with extra points B',C' — not obviously cleaner, but the *target* (equal power of B,C) is symmetric and natural. This is the most promising transformation opening.

**Opening B — Isoceles-degenerate then generalize (indirect similarity).**
Verified numerically: when |AB|=|AC|, the angle conditions FORCE L = reflection of K over the angle-bisector of ∠A (axis), and O lies on that axis, so OM=ON is trivial symmetry. (Tested: A=(0,3),B=(-2,0),C=(2,0); every solution has K=(-x,y), L=(x,y), O on y-axis.) This proves the conclusion is a "generalized symmetry" statement. BUT: the naive generalization fails — the unique indirect similarity fixing A and swapping B↔C is a similarity ONLY when |AB|=|AC| (a linear map fixing origin and swapping B,C is a similarity ⟺ |B|=|C|). Likewise reflection over the perp bisector of BC swaps B↔C but sends M=(A+B)/2 to (A'+C)/2 ≠ N unless A on the axis. So no reflection/indirect-similarity centered at A swaps BOTH {B,C} and {M,N} in a scalene triangle. The general indirect similarity must have a different center (not A) — finding it is the crux and the risk. Possible center: the midpoint of BC, or the circumcenter of ABC, or a point on the perp bisector of BC. Outliner should pursue this only as a high-risk slug.

**Opening C — Complex/coordinate with rotation operators (transformation-flavored analytic).**
Place A at origin in the complex plane. The three angle equalities become equations of the form arg((k-b)/(a-b)) = arg((a-c)/(l-c)) etc., i.e., ratios being real-positive multiples. With b,c known and k,l unknown (4 real dof, 3 real equations = 1-parameter family, consistent with the numerical 1-dim family). Solve for k,l parametrically (one free parameter t), compute circumcenter o = (k·l·(k̄−l̄)+...)/(...), then verify |o−m|²=|o−n|² algebraically. This is a guaranteed-existence slug (no inspiration needed) but heavy; rotation/multiplication is the "transformation" flavor. Best used as a verification/backup or to extract the algebraic identity that a synthetic proof should mirror.

**Opening D — Spiral similarity centered at a constructed point.**
The angle pairing pattern (see below) suggests a spiral (or indirect) similarity swapping segments. Every segment pair (M,K)/(B,C), (B,K)/(C,L), etc., has a spiral center numerically, so the center alone isn't distinctive — the distinctive move is to find a spiral similarity whose *center is O* (circumcenter of AKL) or whose axis is the perp bisector of MN. Since O is equidistant from A,K,L, any spiral similarity centered at O that permutes {A,K,L} is a rotation; the question is whether such a rotation relates M↔N. Promising but requires constructing the right rotation/inversion; currently speculative.

**Opening E — Radical-axis / perpendicular-bisector-of-image.**
Show O ∈ perp bisector of MN by exhibiting two circles Γ₁, Γ₂ whose radical axis is exactly the perp bisector of MN and proving Pow_Γ₁(O)=Pow_Γ₂(O). Natural candidate circles: circumcircle of AKL (= the one defining O) and a circle symmetric in M,N (e.g., circle with diameter MN, or circle through A,M,N = nine-point-style). Since OM=ON ⟺ O on perp bisector of MN ⟺ O has equal power wrt any two circles symmetric about that line. This is a sibling of Opening A.

### Candidate technique(s) (pointers, not plans)
- Homothety (H centered A, factor 1/2) to convert midpoint conclusion into a circumcenter-on-perp-bisector statement — the structural backbone.
- Power of a point + radical axis (the reformulated target "Pow(B)=Pow(C) wrt circle AK*L*").
- Indirect similarity / generalized reflection (motivated by the isoceles degenerate case; the general center is the open problem).
- Complex numbers with rotations (Opening C, the analytic fallback).
- Inversion about A: maps the circumcircle of AKL to line K*L* (since the circle passes through A); then O (center) maps to... the inverse of a circle-through-center is a line, and the circumcenter's inverse is the reflection of A over line K*L*. This could turn "O on perp bisector of MN" into a statement about the line K*L* and its relation to M,N. Worth one probe but not yet validated.

### Cheap-kill candidates
- Parity / pigeonhole: none (geometry, no counting).
- Size bound: none.
- Symmetry (isoceles degenerate): YES — proves the special case instantly by reflection; useful as a sanity check and as a guide to the general symmetry, but NOT a proof for scalene triangles.
- Injection / v_p: none.

### Knowledge-base entries to use (named)
- "Geometry (synthetic & analytic)": spiral similarity, inversion, homothety, power of a point (concyclicity converse PA·PB=PC·PD), radical axes & radical center, similar triangles, trig cevians (Ceva/Menelaus).
- "Coordinates / complex / barycentric": rotate axes to align with a key line — relevant for Opening C (align perp bisector of MN with an axis).
- Circle/triangle configuration: Miquel point of a complete quadrilateral (the four lines AB, AC, BK, CL form a complete quadrilateral with vertices A, B, C and a Miquel point — possibly O or related). Worth a probe.

### Analogous past problems (cruxes)
- None. The crux corpus (per crux_moves_documentation.md) has NO geometry cruxes — domains are number_theory, combinatorics, algebra only. The past_problems_database.json contains geometry problems with solutions but no extracted crux moves. Cannot match by subtopic. Do not force a (nonexistent) geometry crux match.

### Prior progress
- None. Round 1 baseline; results/imo-2026-02/ has only approaches/ (empty), no lemmas, no current.md yet.

### Dead ends (do not retry)
- **Direct AA-triangle-similarity from the angle conditions.** Verified numerically: NONE of the candidate pairs are similar. Computed angle tables (deg, test triangle A=(0,0),B=(4,0),C=(1,3)):
  - △BMK: [M=30.8, K=124.6, B=24.5]
  - △LNC: [N=14.5, C=24.5, L=141.0]
  - △LCK: [C=30.8, K=7.1, L=142.0]
  - △LBK: [B=14.5, K=158.6, L=6.9]
  - △ABK: [B=24.5, K=145.2, A=10.2]
  - △ACL: [C=24.5, L=149.7, A=5.7]
  No two share a full angle triple. So "△BMK ~ △LNC" / "△LBK ~ △LNC" / "△ABK ~ △ACL" are all FALSE. Each condition gives exactly ONE angle equality, not two; there is no free AA similarity. The outliner must NOT build a slug on "the three conditions make two triangles similar."
- **Reflection over angle-bisector of A as the general mechanism.** Only swaps {B,C} and {M,N} simultaneously when |AB|=|AC| (verified: reflection over angle bisector of A does not fix O in a scalene triangle — tested O=(1.33,0.83) does not lie on the A-angle-bisector). The isoceles symmetry does NOT extend verbatim.
- **Reflection over perp bisector of BC.** Swaps B↔C but sends M=(A+B)/2 to (A'+C)/2 ≠ N (A' = reflection of A) unless A is on the axis. Does not swap {M,N} in general.
- **Indirect similarity centered at A swapping B↔C.** Exists as a linear map but is a similarity ⟺ |AB|=|AC|. Not a transformation (angle-preserving) in the scalene case.

### Small-case / intuition notes (all CONJECTURE, numerically verified not proved)
- OM = ON confirmed to ~1e-7 on: scalene A=(0,0),B=(4,0),C=(1,3); scalene A=(0,0),B=(5,0),C=(2,4); right A=(0,0),B=(6,0),C=(0,4); isoceles A=(0,3),B=(−2,0),C=(2,0). In every case multiple distinct solutions of the angle system (1-parameter family) all give OM=ON. Conjecture: the conclusion is an invariant of the 1-parameter family, not a coincidence of one configuration.
- The angle system is 4-dof (K,L each 2D) with 3 equations ⟹ 1-parameter family per triangle; existence of interior solutions is numerically robust but not proved. (A proof of existence is NOT required by the problem — the problem assumes K,L are given satisfying the conditions; we only need OM=ON.)
- In the isoceles case, the whole family has L = reflection(K) over the axis, O on the axis. CONJECTURE: the general proof should exhibit an indirect similarity (not a reflection, center ≠ A in general) that sends K↔L and whose "axis / fixed locus" contains O, with M,N symmetric wrt that locus. The center of this indirect similarity is the central object to identify; candidates to test numerically: midpoint of BC, circumcenter Ω of ABC, the midpoint of the arc BC.
- Dilation reformulation numerically confirmed: O* = circumcenter of △A K* L* (K*=2K, L*=2L from A) satisfies O*B = O*C exactly. This is the cleanest equivalent form of the conclusion and the recommended backbone of Opening A.

### Hardest sub-steps (for the chosen transformation slug)
1. Decoding the three angle conditions under the dilation D(A,2) into a usable symmetric form — conditions (1)–(3) involve the auxiliary points B'=2B, C'=2C, which is awkward; the outliner must find a way to use them without drowning in B',C' bookkeeping.
2. Identifying the general indirect similarity (Opening B/D) — if it exists — i.e., its center and ratio. This is the crux of the symmetry-flavored proof; currently unidentified.
3. If going analytic (Opening C): the algebraic verification |o−m|²=|o−n|² after solving the 3 angle equations is large; the outliner needs to organize it via a well-chosen parameter (the free 1-dof parameter t) and aim for a cancellation, not a brute expansion.

### One-line idea seeds (stop here — outliner's job to develop)
- Homothety H(A,1/2) turns "OM=ON" into "circumcenter of AK*L* is on perp bisector of BC" — chase angle conditions to equal powers of B,C.
- Isoceles case = pure reflection; general case = find the indirect similarity that replaces it.
- Invert about A: circumcircle(AKL) → line K*L*; O's inverse is the reflection of A over K*L*; restated conclusion becomes a relation between line K*L* and B,C. Probe only.
