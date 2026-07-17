# Approach: Mulan's Winning Strategy via Cascade

## Target
**Mulan wins if theta = 180/n for integer n >= 2.**

More precisely: for any such theta and any initial triangle T chosen by Shan-Yu, Mulan has a strategy to force an angle of exactly theta to appear in finitely many steps.

## Technique
Constructive strategy with two phases, using the pair-sum forcing trick and angle bisection.

## Skeleton

### Phase 1: Force a multiple of theta into the triangle

**Step 1.1 (Pair-Sum Lemma):** For theta = 180/n with n >= 2, there exist positive integers j1, j2 with j1 + j2 = n.

**Step 1.2 (Cut Construction):** Given any triangle {A, B, C}, Mulan can cut from edge BC to vertex A with parameter t = 180 - B - j1*theta. This creates:
- Sub-tri 1: angles {B, j1*theta, 180 - B - j1*theta}
- Sub-tri 2: angles {A - t, C, B + t} = {A - (180 - B - j1*theta), C, j2*theta}

**Step 1.3 (Forcing):** Since (j1 + j2)*theta = 180, both sub-triangles have a positive multiple of theta as an angle. Shan-Yu must keep one.

**[GAP 1.3]:** Need to verify that t lies in the valid range (0, A) for any triangle. If A is too small, the cut may not be valid. Handle the case where the direct cut fails.

### Phase 2: Cascade down via bisection

**Step 2.1 (Bisection Lemma):** If the current triangle has angle 2^k * theta (for k >= 1) as a vertex angle, Mulan bisects that angle. Both sub-triangles then contain 2^(k-1) * theta.

**Step 2.2 (Iteration):** Repeat bisection. After at most log2(n) steps, the triangle has vertex angle 2*theta.

**Step 2.3 (Final Win):** When vertex angle = 2*theta, Mulan cuts with t = theta. Both sub-triangles have angle theta. Mulan wins.

**[GAP 2.1]:** Need to verify that once a multiple of theta enters the triangle via Phase 1, it remains as a vertex angle (or we can steer to a suitable configuration) in the "kept" triangle until we reduce to 2*theta.

### Finiteness

**Step 3.1:** Define the "level" of a triangle as the largest k such that 2^k * theta appears as a vertex angle (or 0 if no multiple of theta is present). Phase 1 increases level from 0 to at least 1. Phase 2 decreases level by 1 per step. Total steps bounded by 1 + log2(n).

## Key Lemmas

1. **Pair-Sum Lemma:** For theta = 180/n, integers j1, j2 >= 1 with j1 + j2 = n exist. -- Because n >= 2, take j1 = 1, j2 = n-1.

2. **Dual Forcing Lemma:** After Phase 1 cut, both sub-triangles contain a positive multiple of theta as an angle. -- Because the constructed angles j1*theta and j2*theta satisfy (j1+j2)*theta = 180, so these are valid triangle angles summing correctly.

3. **Bisection Forcing Lemma:** If angle A = 2^k * theta for k >= 1, bisecting forces 2^(k-1)*theta into both sub-triangles. -- Because setting t = A/2 gives both sub-tris an angle of A/2.

4. **Terminal Win Lemma:** If vertex angle = 2*theta, Mulan wins in one cut. -- Because cutting with t = theta gives both sub-tris an angle theta.

## Open Gaps

- **[GAP 1.3]:** Valid cut range verification for Phase 1 in all triangles.
- **[GAP 2.1]:** Maintaining/steering the multiple of theta through Shan-Yu's choices.

## Cases to Cover

- theta = 90 (n = 2): Special instant-win case (cut forces 90 into both subs from any triangle).
- theta = 60 (n = 3): Phase 1 with j1 = 1, j2 = 2; then one bisection.
- General n >= 2: Full two-phase cascade.

## Watch Out For

- Triangles where max angle < theta (Phase 1 cut might have t outside (0, A)).
- The "level" might not be monotone if Shan-Yu can choose triangles that avoid certain multiples.
- Edge cases: very flat triangles where computations approach boundary conditions.
