## Status
unsolved

## Approach: Spiral Similarity Composition

### Target
Identify spiral similarities from conditions (2) and (3), compose them, and show the composition fixes A' or maps A to A', forcing circumcircle(AKL) to pass through A'.

### Skeleton

1. **Interpret condition (2) as a spiral similarity angle**:
   Condition (2): angle(LBK) = angle(LNC).
   
   In directed angle form: angle(BL, BK) = angle(NL, NC) (mod pi).
   
   This is the angle condition for a spiral similarity centered at L that maps:
   - The direction from L toward B to the direction from L toward N
   - The direction from L toward K to the direction from L toward C (or related points)
   
   Let sigma_L be the spiral similarity centered at L with rotation angle mu = angle(LBK).

2. **Interpret condition (3) as a spiral similarity angle**:
   Condition (3): angle(LCK) = angle(BMK).
   
   In directed angle form: angle(CL, CK) = angle(MK, MB) (mod pi).
   
   This is the angle condition for a spiral similarity centered at K that maps:
   - The direction from K toward C to the direction from K toward M
   - The direction from K toward L to the direction from K toward B (or related points)
   
   Let sigma_K be the spiral similarity centered at K with rotation angle nu = angle(LCK).

3. **Determine the scale factors**:
   For sigma_L: if it maps B -> N, the scale factor is |LN|/|LB|.
   For sigma_K: if it maps C -> M, the scale factor is |KM|/|KC|.
   
   Use Law of Sines in the relevant triangles to compute these ratios.

4. **Compose sigma_L and sigma_K**:
   The composition tau = sigma_K . sigma_L is either:
   - Another spiral similarity (if the centers and angles conspire)
   - A translation (if the net rotation is 0 mod 2pi)
   - The identity (if both rotation and translation cancel)
   
   Key claim: The composition tau has a special relationship to the perpendicular bisector of MN.

5. **Show tau fixes A' or maps A to A'**:
   If tau(A) = A', then the circumcircle of AKL (which is transformed to itself under the spiral similarities up to rotation) must pass through both A and A'.
   
   Alternatively: tau might fix A', making A' a natural center for the configuration.

6. **Alternative: direct concyclicity from spiral similarity**:
   The spiral similarity sigma_L centered at L mapping B -> N also maps the circumcircle of ABL to the circumcircle of ANL (scaled and rotated).
   
   Track where A' lands under this map; if it stays on circumcircle(AKL), we're done.

7. **Conclude**: Once A' is shown to lie on circumcircle(AKL), the reflection symmetry gives OM = ON.

### Gaps

1. **Gap 1 (Step 2-3)**: Make the spiral similarity interpretation precise. The conditions give angles, but we need to identify which points map to which. The explorer noted that sigma_L(B) = N with K -> C is numerically false, so a more careful analysis is needed.

2. **Gap 2 (Step 4)**: Compute the composition tau and determine its fixed point structure. This may require explicit coordinates.

3. **Gap 3 (Step 5)**: Show how tau's structure implies A' on circumcircle(AKL). This is the conceptual gap.

### Why this might work

Spiral similarities are the natural tool when angle conditions are given (they preserve angles). Conditions (2) and (3) have the form "angle at X = angle at Y," which is exactly the setup for a spiral similarity with angle equal to that angle. The cross-pairing (B-N and C-M in conditions 2-3) suggests the spiral similarities will compose in a way that respects the midpoint structure.
