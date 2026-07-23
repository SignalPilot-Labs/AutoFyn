# Outline Review: imo-2026-04 (Mulan's Triangle Game)

## Problem Recap
For which theta in (0, 180) can Mulan guarantee a win? The expected answer is theta = 180/n for integer n >= 2.

---

## Approach: mulan-cascade

**Target:** Sufficiency direction only (Mulan wins for theta = 180/n).

**Assessment:**

1. **Whole attempt?** NO. This is only the sufficiency direction of a characterization problem. By itself it does not prove the full answer. However, paired with shanyu-invariant, the two together would cover the full problem.

2. **Technique soundness:** The cascade/bisection strategy is plausible. I verified computationally that:
   - The pair-sum constraint (angles at cut-point P sum to 180) is geometrically correct.
   - For every triangle avoiding multiples of theta = 180/n, there exists at least one valid Phase 1 cut (tested for n = 2 through 9). The interval-based argument shows Mulan can always find a valid j.

3. **Key lemmas with mechanisms:**
   - Pair-sum forcing: VALID mechanism (supplementary angles at cut-point).
   - Bisection forcing: VALID (straightforward angle splitting).
   - Terminal win: VALID.

4. **Open gaps:**
   - GAP 1.3 (Phase 1 cut validity): My analysis shows this is closable. The condition is C < j*theta < 180 - B for some j in {1,...,n-1}. Since the interval width is n*A/180, and we always have some angle > theta for n >= 2, a valid j exists.
   - GAP 2.1 (multiple persistence): This is the harder gap. After Phase 1, Shan-Yu keeps one sub-triangle with a multiple of theta. Then Mulan bisects. But bisection only works if the multiple is at a VERTEX, not at the cut-point P. Need to verify that either the multiple persists at a vertex, or Mulan can steer it there.

5. **Verdict for mulan-cascade:** CHANGES REQUESTED
   - Closable gaps, but GAP 2.1 (steering the multiple to a vertex for bisection) needs explicit mechanism. The outline assumes the multiple stays trackable, but after Shan-Yu keeps a triangle, the multiple might be at the interior cut-point, not at a vertex of the new triangle. The builder must address this.

---

## Approach: shanyu-invariant

**Target:** Necessity direction only (Shan-Yu wins for theta != 180/n).

**Assessment:**

1. **Whole attempt?** NO. Only one direction.

2. **Technique soundness:** The invariant method is correct. If theta != 180/n, then (j1 + j2)*theta != 180 for any integers j1, j2 >= 1, so Mulan cannot force both sub-triangles to have multiples of theta at P.

3. **Key lemmas with mechanisms:**
   - Invariant closure: VALID. The pair-sum constraint (j1 + j2)*theta = 180 has no solution when 180/theta is not an integer.
   - Existence of initial safe triangle: VALID (discrete avoidance in continuous space).
   - Irrational case: VALID (irrational*integer != rational).

4. **Open gaps:**
   - GAP 2 (existence): Straightforward, closable.
   - GAP 3 (pair-sum derivation): VALID mechanism stated (supplementary angles at P).

5. **Verdict for shanyu-invariant:** CHANGES REQUESTED
   - Sound skeleton. The pair-sum constraint derivation needs to be explicit in the proof, but the mechanism is correct. Builder should fill in the geometric detail.

---

## Approach: unified-characterization

**Target:** Full characterization (both directions).

**Assessment:**

1. **Whole attempt?** YES. This is the only approach targeting the complete problem.

2. **Technique soundness:** Combines the two above. Both directions share the pair-sum constraint as the central divide, which is elegant and correct.

3. **Diversity check:** This approach subsumes the other two. The three approaches are NOT truly diverse -- they're all variations of the same framing (pair-sum + invariant/cascade). However, since this framing appears correct, that's acceptable for now.

4. **Key lemmas:** All mechanisms stated, same as in the split approaches.

5. **Open gaps:**
   - GAP A3 (pair-sum derivation): Closable, mechanism known.
   - GAP B1 (Phase 1 cut validity): Closable, verified computationally.
   - GAP B2 (multiple persistence): Same issue as mulan-cascade -- the cascade phase needs to track/steer the multiple to a vertex.

6. **Special case theta = 90:** The instant-win construction is explicitly stated and valid.

7. **Verdict for unified-characterization:** CHANGES REQUESTED
   - Most complete approach. GAP B2 is the main concern: after Phase 1 forces a multiple at cut-point P, Mulan needs to work with triangles where the multiple is at a vertex (for bisection). The outline assumes this without explicit mechanism. The builder must either: (a) show the cut-point P becomes a vertex of the kept triangle, or (b) show Mulan can re-inject the multiple at a vertex.

---

## Diversity Assessment

All three approaches share the same core insight: the pair-sum constraint at the cut-point. This is not a field of diverse routes -- it's one route with a split presentation. However, the insight appears correct, so we proceed. If this bottoms out, a genuinely different framing would be needed (e.g., game-theoretic analysis, potential functions, or a different characterization of winning angles).

---

## Registration and Ranking

All three approaches are new. Registering:
- mulan-cascade: one direction (sufficiency), sound skeleton
- shanyu-invariant: one direction (necessity), sound skeleton
- unified-characterization: full problem, most complete

**Ranking rationale:**
- unified-characterization > mulan-cascade: unified covers both directions
- unified-characterization > shanyu-invariant: unified covers both directions
- shanyu-invariant vs mulan-cascade: draw (both are one direction, similar completeness)

---

## Build Set

The outliner recommended: unified-characterization (most complete), mulan-cascade (backup).

Given that unified-characterization covers the full problem and shares all gaps with the split approaches, I recommend building only unified-characterization this round to avoid redundant work. If it stalls on a specific direction, we can fall back to the split approaches.

**build set: unified-characterization**
