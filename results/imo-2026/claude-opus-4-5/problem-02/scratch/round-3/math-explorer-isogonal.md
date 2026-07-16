## imo-2026-02 (UPDATED — Round 3 Isogonal/Inversion Lens)

### Lens: Isogonal Conjugates / Inversions / Pedal Triangles

---

### CRITICAL DISCOVERIES THIS ROUND

#### 1. The correct cross-ratio sign structure for each condition

All three conditions have the SAME algebraic form: product of two complex ratios whose arguments CANCEL, making the product real.

**C1**: arg((K-B)/(A-B)) = -φ (angle from BA to BK, clockwise)
       arg((L-C)/(A-C)) = +φ (angle from CA to CL, counterclockwise)
       R1 = [(K-B)/(A-B)] · [(L-C)/(A-C)] has arg 0, is real positive.

**C2**: arg((K-B)/(L-B)) = +μ (angle from BL to BK)
       arg((L-N)/(C-N)) = -μ (angle from NC to NL)
       R2 = [(K-B)/(L-B)] · [(L-N)/(C-N)] has arg 0, is real positive.

**C3**: arg((K-C)/(L-C)) = +ν (angle from CL to CK)
       arg((B-M)/(K-M)) = -ν (angle from MK to MB)
       R3 = [(K-C)/(L-C)] · [(B-M)/(K-M)] has arg 0, is real positive.

**Key Lemma**: arg((A-K)/(A-L)) = -angle(KAL) (directed angle at A)
              arg((A'-L)/(A'-K)) = +angle(KA'L) (directed angle at A')
              R_KL = [(A-K)/(A-L)] · [(A'-L)/(A'-K)] real iff angle(KAL) = angle(KA'L).

Numerically: R1 = 0.07526, R2 = 0.33641, R3 = 2.64035, R_KL = 0.97028 (all real positive, verified).

#### 2. The symmetric pairing structure — the KEY STRUCTURAL OBSERVATION

Each condition pairs two "midpoint-related" points that see K and L at equal but opposite angles:
- C2: B ↔ N (N = midpoint AC)
- C3: C ↔ M (M = midpoint AB)
- Key Lemma: A ↔ A' (A' = reflection of A over perp-bisector of MN)

The PATTERN: the conditions at the "vertex level" (B, C, A) are "reflected" at the "midpoint level" (N, M, A'). The Key Lemma has the SAME algebraic structure as C2 and C3, but with the pair (A, A') in place of (B, N) or (C, M). This is NOT a coincidence — A' is defined precisely as the midpoint-level reflection of A.

#### 3. All three conditions are needed (verified)

Numerical test: C2+C3 alone (without C1) gives Key Lemma error ~1%. All three conditions are needed. The proof must use C1 in a load-bearing way, not just as a "minor condition."

#### 4. Inversion centered at A' (fixing B and C)

Under inversion i centered at A' with radius r = |A'B| = |A'C|:
- B → B, C → C (fixed — they lie on the inversion circle)
- A → A* = (1/2 + r²/(a-1/2), b) [a far point on the horizontal line y=b]
- K → K*, L → L*

**Key Lemma equivalent: A*, K*, L* are collinear** (verified to 10^{-12}).

Under this inversion, angles at B and C are PRESERVED (since B, C are fixed points of i):
- ∠(K*, B, A*) = φ   [C1 at B]
- ∠(A*, C, L*) = φ   [C1 at C]
- ∠(L*, B, K*) = μ   [C2 at B]
- ∠(L*, C, K*) = ν   [C3 at C]

So K* = intersection of (ray from B at angle φ from BA*) with (ray from C at angle φ+ν from CA*).
And L* = intersection of (ray from B at angle φ+μ from BA*) with (ray from C at angle φ from CA*).

Key Lemma = A* lies on line K*L*. Since A* is on y=b and K*, L* are determined by the B/C-angle conditions alone (plus constraints from N*, M*), this might be provable via Menelaus on triangle B C A* (a near-degenerate triangle, since A* is far from BC on the y=b line).

#### 5. Spiral similarity interpretations are WRONG (numerically verified)

- Spiral centered at L (B→N, K→C): error = 1.95 (far from 0)
- Spiral centered at K (C→M, L→B): error = 1.74 (far from 0)

C2 and C3 are PENCIL PERSPECTIVITY conditions (equal angles at two different vertices), NOT spiral similarities.

#### 6. Miquel point of {BK, BL, CK, CL} ≈ (0.43, 0.007) — NOT A or A'

Not A (at (0.3, 2)), not A' (at (0.5, 2)), not foot of altitude (0.3, 0), not midpoint of BC (0.5, 0).

---

### Distinct openings for the outliner

**Opening 1 (Symmetric pairing structure — most structurally natural):**

The argument should "lift" the angle condition from the {B, C} level (where C1 acts) to the {A, A'} level via the midpoint structure. Specifically:

Step 1: C2 says (B, K, L, N) satisfies: directed angles at B and N are equal (both = μ). This is equivalent to: B and N lie on the circle such that they subtend equal arcs to K and L.

Step 2: C3 says (C, L, K, M) satisfies similarly: directed angles at C and M are equal (both = ν).

Step 3: C1 connects the two "sides" (B-side and C-side) via the common angle φ.

Step 4: The Key Lemma is the same structure at the A-level: A and A' subtend equal angles to K and L. This follows because A' is the unique point (at height b, on the perp-bisector of BC) that is "mid-level" to M and N, just as N is "mid-level" to C and A and M is "mid-level" to B and A.

The concrete calculation: Since A' = midpoint-analog of A (via the midpoints M, N), the angle condition at A' is determined by the conditions at M and N (which are the second parts of C2 and C3). The Key Lemma then follows from a "two-step lifting": {B,C} → {M,N} → {A,A'}.

**Opening 2 (Inversion + Menelaus in the inverted picture):**

After inversion at A' (fixing B, C), prove A*, K*, L* collinear. The points K* and L* lie on specific rays from B and C. Apply trigonometric Menelaus to triangle B, A*, C:

The transversal K*L* cuts:
- Side BA* at some point P₁ (on the line through B and A*, which is the ray from B toward A*)
- Side CA* at some point P₂ (on the ray from C toward A*)
- Side BC at some point P₃

But since K* is on ray BA* rotated by φ from B, and L* is on ray CA* (unrotated) from C, the Menelaus condition gives:
(BP₁/P₁A*) · (A*P₂/P₂C) · (CP₃/P₃B) = -1.

The angles φ, μ, ν and their constraints from C2-at-N*, C3-at-M* determine these ratios via the sine rule in the respective sub-triangles.

**Opening 3 (Direct directed-angle chain):**

Write ∠(KAL) - ∠(KA'L) = 0 by decomposing into contributions from B, C (via C1), N (via C2), M (via C3).

∠(KAL) = ∠(KAB) + ∠(BAL) [decompose at A]
∠(KA'L) = ∠(KA'B) + ∠(BA'L) [decompose at A']

Need: ∠(KAB) - ∠(KA'B) = ∠(BA'L) - ∠(BAL).

LHS = the "angular shift" of K as we move from A to A'.
RHS = the "angular shift" of L as we move from A to A'.

The fact that A and A' are on the horizontal line y=b means: the "shift" depends only on the horizontal displacement (A_x vs A'_x = 1/2), weighted by sin/cos of the angle to K and L from this horizontal.

C1 makes K and L at equal angles φ from the B-to-A and C-to-A directions respectively, giving a symmetric structure that might make these shifts equal.

**Opening 4 (Explicit trig computation closing the algebraic gap):**

From the proved formulas BK = (AB/2)sin(ν)/sin(φ+ν) and CL = (AC/2)sin(μ)/sin(φ+μ), also derive:
- BL via the law of sines in triangle BLN: ∠LBN = φ+μ - ∠ABN, ∠LNB = π - μ, ∠BLN = μ + ∠ABN - π.
- CK via law of sines in triangle CMK.

Then: K and L are fully determined (both position on rays and distance), so the circumcenter O_x can be computed explicitly. Show O_x = (2a+1)/4 = (a + 1/2)/2 using the trigonometric identity that results.

---

### Candidate techniques

- **Directed angles mod π** with the symmetric-pairing structure (most direct route)
- **Inversion** (knowledge_base.md): the A'-centered inversion reducing Key Lemma to collinearity
- **Trigonometric Menelaus**: in the inverted picture for the collinearity
- **Law of Sines**: for explicit positions (already partly done in prior approaches)

---

### Knowledge-base entries to use

- Inversion: "Inversion centered at A' fixes B and C, transforms circumcircle through A' to a line"
- Simson line: alternative formulation of Key Lemma (A' on circumcircle iff Simson feet collinear)
- Directed angles mod π (insribed angle theorem)

---

### Analogous past problems (cruxes)

None — geometry domain not in the crux corpus.

---

### Prior progress

- **Key Reduction PROVED**: A' on circumcircle(AKL) ⟹ OM = ON. (All three approaches)
- **Key Lemma**: Verified to 10^{-14}. Not proved.
- **Law of Sines**: BK = (AB/2)sin(ν)/sin(φ+ν), CL = (AC/2)sin(μ)/sin(φ+μ). Proved.
- **Basic fact**: A, A', M, N always concyclic (no conditions needed).

---

### Dead ends (do not retry)

- **Spiral similarity centered at L (B→N, K→C)**: NUMERICALLY FALSE (error 1.95).
- **Spiral similarity centered at K (C→M, L→B)**: NUMERICALLY FALSE (error 1.74).
- **Concyclic quadruples beyond {A,A',K,L} and {A,A',M,N}**: Exhaustive check (all C(8,4)=70 quadruples) found only these two.
- **Simple product R1·R2/R3 etc.**: None of 12 combinations gives R_KL.
- **Miquel point of {BK,BL,CK,CL} = A or A'**: FALSE, the point is ≈ (0.43, 0.007).

---

### Small-case / intuition notes

- **Conjecture (structural)**: The proof should "lift" the angle equality from {B,C} to {M,N} to {A,A'} in two steps, using C2 and C3 respectively, with C1 providing the "bridge" between the B-side and C-side.
- **Conjecture (inversion)**: The line K*L* passes through A* because the angle conditions at B and C (from C1, C2, C3) determine K* and L* as intersections of specific rays, and the collinearity with A* follows from the constraints (at N*, M*) via a Menelaus-type argument.
- In the isoceles case (a = 1/2, so A = A'), R_KL = 1 trivially. For general triangles R_KL ≠ 1 but remains real. This suggests the Key Lemma is NOT just "A and A' happen to be on the same circle" but is a genuine consequence of the angle conditions.
- **Key algebraic fact**: The cross-ratio R2 is real because arg((K-B)/(L-B)) = +μ and arg((L-N)/(C-N)) = -μ exactly cancel. This "opposite-sign" structure is the algebraic signature of C2, and is likely what drives the proof.

### What the exploration found

**Setup confirmed.** The Key Lemma is: A' lies on circumcircle(AKL), where A' = (1/2, b) in coordinates B=(0,0), C=(1,0), A=(a,b). This is equivalent to OM = ON.

---

### Critical new discovery: all three conditions are needed

Numerical test with B=(0,0), C=(1,0), A=(0.3,2):

- C2 + C3 alone (without C1): A' distance from circumcircle = 0.012 (NOT on it)
- C1 + C2 + C3 all three: distance < 10^{-14} (on it)

Conclusion: C1 is NOT redundant. The Key Lemma requires all three conditions. This matters for proof strategy: any approach that uses only C2 and C3 and then "adds" C1 must use C1 in a genuinely load-bearing way.

---

### Correct cross-ratio form of each condition

Let B=0, C=1, A=a+bi, A'=1/2+bi, M=A/2, N=(A+1)/2 (complex coords).

- **C1** (∠KBA = ∠ACL = φ):  
  arg(K-B)/(A-B) = -φ and arg(L-C)/(A-C) = +φ, so they are negatives of each other.  
  Correct cross-ratio form: **(K-B)(L-C) / [(A-B)(A-C)] is real and positive** (= sin²φ times a triangle-dependent constant).  
  Numerically (phi=20°): 0.07526 ✓ (purely real)

- **C2** (∠LBK = ∠LNC = μ):  
  **(K-B)(L-N) / [(L-B)(C-N)] is real** (= 0.3364 for phi=20°)

- **C3** (∠LCK = ∠BMK = ν):  
  **(K-C)(B-M) / [(L-C)(K-M)] is real** (= 2.640 for phi=20°)

- **Key Lemma** (A' on circumcircle(AKL)):  
  **(A-K)(A'-L) / [(A-L)(A'-K)] is real** (= 0.9703 for phi=20°)

**No simple algebraic combination** of R1, R2, R3 gives R_KL. Exhaustive check over {Rᵢ·Rⱼ, Rᵢ/Rⱼ, Rᵢ·Rⱼ/Rₖ} found no match within 0.08. The relationship is NOT a Ceva-type product identity.

---

### What C2 and C3 actually encode (the spiral similarity was wrong)

The existing approaches (including the unsolved spiral-similarity approach) assumed:
- C2 ⟺ spiral centered at L maps B→N and K→C

This is **FALSE**. Numerically: |(K-L)(N-L)/(B-L) - (C-L)| = 1.34 (far from 0).

What C2 and C3 actually encode:

**C2**: The central perspectivity of pencils with center L maps:  
- The ray BL (pencil at B) → the ray NL (pencil at N) [trivially, both pass through L]  
- The ray BK (pencil at B) → the ray NC (pencil at N)  
This is because arg((K-B)/(L-B)) = arg((C-N)/(L-N)).

**C3**: The central perspectivity of pencils with center K maps:  
- The ray CK → MK [trivially]  
- The ray CL → MB  
This is because arg((L-C)/(K-C)) = arg((B-M)/(K-M)).

These perspectivities-of-pencils (NOT spiral similarities) are the correct geometric reading of C2 and C3.

---

### The inversion centered at A' — a viable bypass

Under inversion centered at A' with radius r = |A'B| = |A'C| = sqrt(1/4 + b²):
- **B → B** and **C → C** (both are fixed — they lie on the circle of inversion)
- A → A* = far point (−20.75, 2) for a=0.3, b=2
- K → K*, L → L*

**Key Lemma becomes: A*, K*, L* are collinear** (since circumcircle(AKL) passes through the center A', it maps to a LINE, and A* must be on the line K*L*).

Numerically confirmed: collinearity error < 10^{-12}.

Under this inversion (conformal at B and C since they're fixed):
- Angle at B between BL* and BK* is preserved → angle(L*BK*) = μ (C2 part-1)
- But angle(LNC) at N transforms to the tangential angle at N* between circles (A',N*,L*) and (A',N*,C), equal to μ by conformality of inversion at N (C2 part-2)

So the inverted problem is: prove A* lies on line K*L*, given:
- Angle(L*BK*) = μ (from C2, preserved by inversion)
- Angle(K*BL*) from C1 condition at B (preserved)
- Angles at N*, M* transformed conformally to circle-circle tangential angles through A'

This reformulation might be easier for a synthetic argument, since A* is the unique real point (along the horizontal through A') at distance r²/d from A', and the collinearity condition A*, K*, L* might follow from a Menelaus-type argument on some triangle with base K*L*.

---

### A, A', M, N are always concyclic — basic structural fact

This requires NO angle conditions. Proof: both AA' and MN are horizontal (parallel to BC), and both midpoints of AA' and MN lie on the perpendicular bisector of MN at x=(2a+1)/4. So the four points share a common circumcircle centered at ((2a+1)/4, y₀) where y₀ = (a²-a+3b²)/(4b).

This basic fact is NOT the Key Lemma. The Key Lemma is A' on circumcircle(AKL), which changes with K and L.

---

### Distinct openings for the outliner

**Opening 1 (Directed angle chain, sharper):**  
The Key Lemma ∠(KA,AL) = ∠(KA',A'L) might follow from chaining C2 and C3 TOGETHER with the specific property that A'B = A'C. Since C2 says ∠(BL,BK) = ∠(NL,NC) and C3 says ∠(CK,CL) = ∠(MK,MB), and C1 links angles at B and C symmetrically, try the chain:  
∠(KA,AL) = ∠(KB,AB) + [triangle BAL terms] and ∠(KA',A'L) = ∠(KB',A'B) + [...] where B' relates to the isoceles property A'B=A'C. The cross-pairing (B↔N, C↔M) creates a "twist" that condition C1 untwists.

**Opening 2 (Inversion + Collinearity via Menelaus):**  
Under the inversion centered at A' (radius |A'B|), the Key Lemma becomes: A*, K*, L* collinear. Since A* lies on the horizontal line y=b (same as A and A'), and K*, L* are the images of K and L (which are near the bottom of the configuration), A* collinear with K* and L* is a MENELAUS condition. Specifically: A* is the point at which the line K*L* extended meets the horizontal y=b. Condition C1 says the angles at B and C are matched, which (after inversion) constrains the slope of line K*L* to pass through the specific real point A* on y=b. This might be a natural Menelaus argument on triangle BK*L* or CK*L*.

**Opening 3 (Law of Sines direct computation):**  
From C1, C2, C3 we know:
- BK = (AB/2)sin(ν)/sin(φ+ν), CL = (AC/2)sin(μ)/sin(φ+μ) [proved in prior approaches]
- The positions of K and L on their rays from B and C are fully determined by (φ, μ, ν) and the triangle

The circumcenter O of AKL has x-coordinate O_x that can be computed from these positions. The Key Lemma is O_x = (2a+1)/4. Substituting the explicit formulas (using law of sines in ABK and ACL), the claim reduces to a trigonometric identity in φ, μ, ν, β, γ (angles of the triangle). The identity should be verifiable by expressing BL and CK via the law of sines in triangles BKL and CKL (using C2 for BL and C3 for CK), then using C1 to close.

**Opening 4 (Miquel point of BK, CL, MK, NL):**  
The four lines BK (extension), CL (extension), MK (extension), NL (extension) form a complete quadrilateral. The Miquel point of this quadrilateral might be A or A'. If A' is the Miquel point, then A' lies on all four circumcircles of the sub-triangles, including circumcircle(AKL) if A is one of the 6 intersection points of the quadrilateral. This should be tested numerically (my computation had an error and didn't complete) — it's a strong enough claim to be worth checking.

**Opening 5 (Cross-ratio identity from projective geometry):**  
The three conditions give three real cross-ratios. There might be a "projective closure" argument: the map z ↦ (az+b)/(cz+d) (a Möbius transformation) that maps the 6 points {A, A', K, L, B/N, C/M} to a configuration where the Key Lemma is obvious. The argument of this Möbius transformation might be determined by requiring R1, R2, R3 all to be real, which forces R_KL to be real.

---

### Candidate techniques

- **Directed angle chains** (knowledge_base.md: "Circle/triangle configuration facts") — the primary tool
- **Inversive geometry** (knowledge_base.md: "Synthetic toolkit: inversion") — the bypass via inversion at A' looks promising
- **Miquel's theorem** (knowledge_base.md: "Miquel point of a complete quadrilateral") — for Opening 4
- **Law of Sines in BMK and LNC** (already proved) — use these to build explicit positions for K, L

---

### Cheap-kill candidates

- **Parity/symmetry**: None obvious since the triangle is general.
- **Isoceles special case first**: In the isoceles triangle (a=1/2), A=A' and the result is trivial. The general proof must "deform" from this special case.
- **The perspectivity centers**: The conditions C2 (center L) and C3 (center K) define perspectivities. Check whether the composition of these perspectivities maps A → A'. If the composition is a simple map (like a translation or reflection), the Key Lemma follows.

---

### Knowledge-base entries to use

- Geometry (synthetic & analytic): "Miquel point of a complete quadrilateral" — for Opening 4
- Geometry: "Simson line (feet from P collinear iff P on circumcircle)" — Simson reformulation of Key Lemma
- Geometry: "inversion" — the A'-centered inversion bypass
- Geometry: "angle chasing, power of a point" — for the directed angle approach

---

### Analogous past problems (cruxes)

None — the crux corpus has no geometry entries (confirmed in crux_moves_documentation.md: "geometry — Not in the corpus yet").

---

### Prior progress

- Key Reduction PROVED: A' on circumcircle(AKL) ⟹ OM = ON.
- Key Lemma: A' on circumcircle(AKL). Numerically verified to 10^{-14} for 10+ configurations. Not proved.
- Law of Sines in BMK and LNC: BK = (AB/2)sin(ν)/sin(φ+ν), CL = (AC/2)sin(μ)/sin(φ+μ). Proved.
- A, A', M, N always concyclic: Basic fact, proved (no conditions needed).

---

### Dead ends (do not retry)

- **Spiral similarity σ_L centered at L mapping B→N, K→C**: FALSE. Numerically |(K-L)(N-L)/(B-L) - (C-L)| ≈ 1.34. C2 encodes a PENCIL PERSPECTIVITY with center L, not a spiral similarity.
- **Concyclic quads from {A,A',K,L,B,C,M,N} besides A,A',K,L and A,A',M,N**: None exist. Exhaustive check of all C(8,4) = 70 quadruples shows only these two.
- **Simple algebraic combination R1*R2/R3 or similar**: None of the 12 tested combinations gives R_KL.

---

### Small-case / intuition notes

- All three conditions are NEEDED (C2+C3 alone give ~1% error in the Key Lemma).
- The correct C1 cross-ratio is (K-B)(L-C)/[(A-B)(A-C)] = REAL POSITIVE. Numerically ≈ sin²(φ)/|term depending on triangle|; this is the product of two complex numbers with arguments -φ and +φ.
- The value of R_KL varies with φ and the triangle shape; it equals 1 in the isoceles case (A=A'). As A moves away from isoceles, R_KL deviates from 1 but remains real (Key Lemma).
- **Conjecture**: The Key Lemma might follow from a "harmonic" argument where conditions C2 and C3 together give a "cross-ratio equality" at N and M respectively, and C1 provides the "bridge" that makes A and A' symmetric with respect to this cross-ratio configuration.
