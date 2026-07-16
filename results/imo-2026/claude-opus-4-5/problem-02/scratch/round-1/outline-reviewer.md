# Outline Review: IMO 2026 P2

## Problem Summary
Triangle ABC with midpoints M (of AB) and N (of AC). Points K inside BMC, L inside BNC satisfy:
- (Cond 1) angle(KBA) = angle(ACL)
- (Cond 2) angle(LBK) = angle(LNC)
- (Cond 3) angle(LCK) = angle(BMK)

Prove OM = ON where O = circumcenter(AKL).

---

## Approach 1: `directed-angle-concyclic`

**Verdict: APPROVE**

**Summary**: Prove circumcircle(AKL) passes through A' (reflection of A over perp-bisector(MN)), then OM = ON by symmetry.

**Strengths**:
1. The reduction is correct: A' on circumcircle(AKL) implies the circumcircle is symmetric under reflection over perp-bisector(MN), so O lies on this line, giving OM = ON.
2. The definition of A' is clean: A' = intersection of (perp-bisector of BC) with (line through A parallel to BC). This gives |A'B| = |A'C|.
3. Numerical verification confirms A' lies on circumcircle(AKL) to 10^{-14} precision.
4. Directed angle chase is the natural synthetic technique for proving concyclicity.

**Gaps identified**:
- Gap 1 (Step 4-5): Expressing angles at A' in terms of the given conditions (2) and (3). The mechanism is not yet stated — this is the crux.
- Gap 2 (Step 7): Final directed angle calculation showing angle(KAL) = angle(KA'L).

**Risk assessment**: Low to medium. The technique is sound. The main risk is that the angle chase may be intricate, but the symmetric structure (|A'B| = |A'C|, conditions mix B-N and C-M) should make the algebra close. No circular reasoning detected.

**Recommendation**: Build this round. The skeleton is complete end-to-end, and the gaps are computational rather than structural.

---

## Approach 2: `power-of-point`

**Verdict: APPROVE**

**Summary**: Prove pow(B, omega) - pow(C, omega) = (AB^2 - AC^2)/2, then derive OM = ON from midpoint relations.

**Strengths**:
1. The power identity is numerically verified to machine precision across multiple triangles and phi values.
2. The Law of Sines formulas BK = (AB/2) sin(nu)/sin(phi+nu) and CL = (AC/2) sin(mu)/sin(phi+mu) are correct (verified by structure explorer).
3. The approach is analogous to IMO-SL 2009 G2, which used a similar power-of-point framework.
4. The cross-pairing structure (B-N in cond 2, C-M in cond 3) naturally produces the factor 1/2 via midpoints.

**Gaps identified**:
- Gap 1 (Step 7): The main power computation — deriving pow(B) - pow(C) = (AB^2 - AC^2)/2 from the angle conditions. This requires careful Law of Sines in triangles ABK, ACL, and possibly BKL or CKL.
- Gap 2 (Step 8): Translating the power identity to OM = ON. The outline says this uses midpoint relations but doesn't specify the exact calculation.

**Risk assessment**: Medium. The technique is correct, but the algebra may be heavy. The outline should clarify Step 8: specifically, use |XO|^2 = |XA|^2 + |AO|^2 - 2(X-A).O or the direct relation |OM|^2 - |ON|^2 = (pow(M) - pow(N)) + 0 when M, N are equidistant from some reference.

**Note on Step 8**: The exact relation is:
- pow(X, omega) = |XO|^2 - R^2
- So |BO|^2 - |CO|^2 = pow(B) - pow(C)
- For midpoints: |MO|^2 - |NO|^2 = |BO|^2/4 + |AO|^2/4 + ... (needs expansion)

Actually, the cleaner path is: since M = (A+B)/2 and N = (A+C)/2, we have |MO|^2 - |NO|^2 = ((A+B)/2 - O)^2 - ((A+C)/2 - O)^2. This expands to (1/2)(B-C).(A+B+C-2O)/2 = ... The builder should verify this closes.

**Recommendation**: Build this round. The approach is viable, and the gaps are algebraic.

---

## Approach 3: `spiral-similarity`

**Verdict: RETHINK**

**Summary**: Interpret conditions (2) and (3) as spiral similarity angles, compose the transformations, and show the composition fixes A' or maps A to A'.

**Fatal flaw**: The naive interpretation (sigma_L centered at L maps B -> N and K -> C) is **numerically false**. I verified:
- For phi = 20 deg, the spiral ratio (N-L)/(B-L) = -0.29 - 0.43i
- But (C-L)/(K-L) = -0.86 + 0.93i
- These ratios differ by ~1.48 in magnitude and ~133 deg in angle.

The outline acknowledges this ("the naive guess is numerically false") but proposes to proceed anyway by "careful analysis of what the spiral similarities actually map." However, no alternative interpretation is provided. Without a correct identification of what spiral similarity is actually induced by the conditions, the entire skeleton is speculative.

**Structural problem**: The outline says "interpret condition (2) as spiral similarity angle" but condition (2) only gives an angle equality, not a ratio. A spiral similarity requires both angle and ratio. The condition does NOT determine a spiral similarity uniquely — it determines only a family parameterized by the ratio.

**Recommendation**: Do not build. Send back to outliner with instruction: either identify the correct spiral similarity interpretation (with verification) or abandon this technique in favor of an alternative.

---

## Approach 4: `complex-coords`

**Verdict: APPROVE**

**Summary**: Set up coordinates with perp-bisector(MN) as imaginary axis, verify cross-ratio (A, K; L, A') is real.

**Strengths**:
1. The coordinate setup is clean and well-suited to the target (O on imaginary axis).
2. The cross-ratio criterion for concyclicity is standard and correct.
3. The approach is complementary to the synthetic approaches — if the algebra is tractable, it provides a rigorous verification path.

**Gaps identified**:
- Gap 1 (Step 4-5): Parameterizing K and L from the angle conditions. The complex form of angle conditions (arg ratios) needs to be translated to constraints on the ray parameters.
- Gap 2 (Step 6-8): Algebraic verification that Im(cross-ratio) = 0. This may be heavy but is mechanically sound.

**Risk assessment**: Medium to high on tractability. The algebra could be messy, but sympy or careful hand calculation can verify it. No structural flaw.

**Note**: Step 2 has a minor error in the reflection formula. A = a (complex), reflection over imaginary axis: A' = -conj(a) only if origin is on the axis. With origin at midpoint(MN) (which is on the imaginary axis at 0), reflection of a = x + iy over Im axis gives A' = -x + iy = -Re(a) + i*Im(a). The outline's formula in the approach file is slightly muddled but the final answer A' = -Re(a) + i*Im(a) is correct.

**Recommendation**: Build this round as a backup/verification path. It's computationally heavy but mechanically sound.

---

## Cross-Approach Assessment

1. **directed-angle-concyclic** and **complex-coords** attack the same key lemma (A' on circumcircle) via different methods — one synthetic, one algebraic. Building both provides a verification check.

2. **power-of-point** attacks a different (but equivalent) target identity. It's independent of the A' lemma and provides a distinct route.

3. **spiral-similarity** is fatally flawed in its current form — the claimed spiral similarity interpretation doesn't hold.

---

## Ranking Comparisons

Since all approaches are new (round 1, cold-start Elo 1500), I compare based on soundness and likelihood of success:

1. **directed-angle-concyclic** > **spiral-similarity**: The former has a sound skeleton; the latter has a false premise.
2. **power-of-point** > **spiral-similarity**: Same reasoning — sound vs. flawed.
3. **complex-coords** > **spiral-similarity**: Sound vs. flawed.
4. **directed-angle-concyclic** vs **power-of-point**: Both sound; draw — different routes, both worth pursuing.
5. **directed-angle-concyclic** vs **complex-coords**: Both attack A' lemma; directed-angle is more elegant if it works, but complex-coords is more mechanical. Slight edge to directed-angle for being more insightful, but draw is fair.
6. **power-of-point** vs **complex-coords**: Both algebraic in different ways; draw.

---

## Registrations

Register the following approaches (all new this round):
- `directed-angle-concyclic`: "Prove A' on circumcircle(AKL) via directed angle chase, then OM=ON by symmetry"
- `power-of-point`: "Prove pow(B)-pow(C)=(AB^2-AC^2)/2 via Law of Sines, then derive OM=ON"
- `complex-coords`: "Algebraic verification of A' on circumcircle via complex cross-ratio"

Do NOT register `spiral-similarity` — it has a fatal flaw and cannot be built.

---

## Build Set

build set: directed-angle-concyclic, power-of-point, complex-coords
