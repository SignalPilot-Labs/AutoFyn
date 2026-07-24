## Status
unsolved

## Approaches tried
- (round 1, initial) Synthetic concyclicity + radical-axis framing, gated on a
  numerical existence check for a genuinely concyclic quadruple among
  {A,B,C,M,N,K,L,O} forced by the angle conditions (ii) ∠LBK=∠LNC and
  (iii) ∠LCK=∠BMK. **Outcome: the gate fails.** An exhaustive numerical scan
  (below) over all 4-point subsets of {A,B,C,M,N,K,L,O}, across two distinct
  scalene triangles and dozens of valid (K,L) configurations per triangle,
  found **no 4-point subset that is concyclic identically along the family**
  — every subset's signed-concyclicity determinant is macroscopically nonzero
  (order 0.05 to ~19 in absolute value, versus the ~1e-9 to 1e-13 floor that
  a genuine identity shows elsewhere in this problem, e.g. OM−ON itself). The
  closest candidate, {M,N,K,L}, is not consistently small across triangles
  (0.05 in triangle 1, 0.42 in triangle 2 — growing, not shrinking, i.e. not
  even asymptotically vanishing). This is a clean, reproducible negative
  result, not an inconclusive one. Reporting this approach as a dead end
  (RETHINK-worthy) rather than forcing a synthetic argument onto a false
  premise.

## Current best

**Target reformulation (Lemma 0, shared with other approaches, re-verified here).**
Let N9 be the nine-point center of ABC. Since M, N (midpoints of AB, AC) both
lie on the nine-point circle, N9M = N9N. For any point P,
`|P−M|² − |P−N|² = (P−M+P−N)·(P−M−P+N) = (2P−M−N)·(N−M)`. Applying this at
P = O and at P = N9 and subtracting (the `(2P−M−N)` linear-in-P part cancels
the `−M−N` piece, leaving only the `2P` piece):
`(OM² − ON²) − (N9M² − N9N²) = 2(O − N9)·(N − M)`. Since N9M = N9N, the left
side is exactly `OM² − ON²`, so
```
OM² − ON² = 2(O − N9)·(N − M).
```
Since M, N are midpoints of AB, AC, the segment MN is the midline of triangle
ABC parallel to BC, so `N − M = (C − B)/2`, giving the clean target:
```
OM = ON   ⟺   (O − N9) · (C − B) = 0.
```
This reduction is correct and unconditional (no use of the K, L conditions
yet); it is shared across the population.

**The synthetic route attempted here.** The idea was to find a concyclic
quadruple among {B, C, M, N, K, L} (or a small set of auxiliary points built
from them) forced by conditions (ii) ∠LBK = ∠LNC and (iii) ∠LCK = ∠BMK, form
two circles ω1, ω2 of equal radius from such quadruples, and place O (or a
point differing from O by an already-understood fixed vector) on the radical
axis of ω1, ω2 — which for equal-radius circles is the perpendicular bisector
of the segment joining their centers — aiming to identify that radical axis
with the perpendicular bisector of MN directly, without ever computing O in
coordinates. This would have been a genuinely non-algebraic proof.

**Why the plan's premise is suspect on inspection (before even running numerics).**
The classical "equal inscribed angle ⟹ concyclic" criterion requires the two
equal angles to subtend a *common segment* from two different vertices: if
`∠XPY = ∠XQY` with P, Q on the same side of line XY, then P, Q, X, Y are
concyclic. Condition (ii), `∠LBK = ∠LNC`, has vertex B with rays to {L, K}
and vertex N with rays to {L, C}: the two angles share the point L as one arm
but the *other* arm differs (K vs. C). This is **not** the shape of the
classical criterion (which needs both arms to match, i.e. a common chord).
The same issue applies to (iii): `∠LCK = ∠BMK` has vertex C with arms {L, K}
and vertex M with arms {B, K}: here K is a shared arm, but the other arm
differs (L vs. B). So neither (ii) nor (iii) is, by itself, a textbook
concyclicity criterion on any 4-point subset of {B, C, M, N, K, L} — the
outline's claim that these conditions "have the classic shape of an
inscribed-angle / concyclicity criterion" does not survive a careful
re-reading of which points appear as which arms. This was a plausible-looking
but, on closer inspection, incorrect premise. (It remains conceivable that a
*more elaborate* auxiliary construction — e.g. introducing the second
intersection point of two other circles, a Miquel-point argument, or folding
in condition (i) as well — could still produce a genuine concyclicity not
visible in the raw 4-point subsets of {A,B,C,M,N,K,L,O}; the numerical work
below tests exactly the raw subsets and finds none, which is strong but not
absolute evidence against every possible auxiliary construction.)

**Numerical existence check (performed as instructed, before any further
synthetic work).**

*Setup.* For a fixed scalene triangle ABC (vertices as concrete floating
point coordinates), M, N are midpoints of AB, AC. Unsigned angles are encoded
as `ang(V,P,Q) = |atan2(cross(P−V, Q−V), dot(P−V, Q−V))| ∈ [0,π]`, matching
the round-1 explorers' convention. The defining system is:
```
F1(K,L) = ang(B,K,A) − ang(C,A,L)     [∠KBA = ∠ACL]
F2(K,L) = ang(B,L,K) − ang(N,L,C)     [∠LBK = ∠LNC]
F3(K,L) = ang(C,L,K) − ang(M,B,K)     [∠LCK = ∠BMK]
```
(K, L) ranges over ℝ⁴; F = (F1,F2,F3): ℝ⁴ → ℝ³, so the zero set is generically
a curve (1-parameter family), matching the dof count both this approach's
outline and the round-1 explorers independently derived.

A random multi-start solve (`scipy.optimize.least_squares`, thousands of
random initial guesses for K in triangle BMC and L in triangle BNC per
triangle) was run, keeping only solutions with residual < 1e-20 (essentially
exact) and then filtering by ALL FOUR hypothesis containments: K ∈ int(BMC),
L ∈ int(BNC), K inside angle LBA, and L inside angle ACK (the last two tested
via a signed-arc "is the ray to the test point between the two bounding rays"
routine, taking the shorter arc between the two bounding directions).

*Triangle 1:* A=(0,3), B=(−2,0), C=(2.5,0). 27 distinct valid (K,L)
configurations found satisfying all three equalities and all four
containments to ≤1e-14 (essentially machine precision) residual.
*Triangle 2:* A=(0.5,4), B=(−3,0), C=(2,0). 18 distinct valid configurations
found, same precision.

For every valid configuration on both triangles, `O = circumcenter(A,K,L)`
was computed via the closed-form circumcenter formula, and `|OM − ON|` was
verified to be ≤ 5×10⁻¹⁰ in every case (machine/solver precision) — this is
an independent re-confirmation of the theorem itself (OM=ON) across two
triangles and 45 total configurations, consistent with the shared Lemma 0
route and with the round-1 explorers' findings.

*Concyclicity scan.* For every one of the `C(8,4) = 70` four-point subsets of
`{A, B, C, M, N, K, L, O}` (including O and A, in case the intended
quadruple involves them, not just the "obvious" six points), the signed
concyclicity determinant
```
det | x  y  x²+y²  1 |   (one row per point)
```
was computed for every valid (K,L) configuration on both triangles, and the
maximum absolute value across the family was recorded (a genuine identity
would show this at the ~1e-9 to 1e-13 floor, matching how OM−ON behaves).

*Result:* **no 4-point subset showed a determinant compatible with an
identity.** The smallest maximum was {M,N,K,L}, at 0.050 (triangle 1) and
0.418 (triangle 2) — three to four orders of magnitude above the ~1e-10
noise floor that a true identity exhibits elsewhere in this problem, and
*growing* rather than shrinking between the two triangles tested (ruling out
"it's just numerically small but exact" as an explanation). Every other
subset (including all subsets containing O or A) had maximum determinant
between roughly 1 and 20 — decisively nonzero. Full determinant tables for
both triangles are reproducible from the Python setup above.

**Conclusion.** The concyclicity claim gating this approach — that some
natural 4-point subset of {A,B,C,M,N,K,L,O} is forced concyclic by conditions
(ii),(iii) — is **numerically false** for the raw 6+2 point set. Combined
with the a priori structural objection above (neither (ii) nor (iii) has the
matching-chord shape the classical inscribed-angle converse requires), this
approach's central premise does not hold as stated. Per the outline's own
exit condition ("if no clean concyclicity is found within a bounded numerical
scan: this approach should be abandoned... reported as a dead end"), this
approach is reported as a dead end at the outline stage: **RETHINK**. It
should not be resampled in its current form; if a future round wants a
synthetic, non-algebraic route, it should look for a genuinely different
mechanism (e.g., an actual spiral similarity taking one *constructed* triangle
to another, not a concyclicity among the raw named points, or an
inversion-centered argument), rather than retrying "find a concyclic
quadruple among the named points," which this round's scan rules out.

## Full proof
(not established — Status: unsolved; this approach's gating premise fails)

## Promotable lemmas
- **Lemma 0 (shared reduction).** For triangle ABC with M, N the midpoints
  of AB, AC and N9 the nine-point center, and any point O:
  `OM = ON ⟺ (O − N9)·(C − B) = 0`.
  Proof: `|P−M|² − |P−N|² = (2P−M−N)·(N−M)` for any P (difference of two
  squares applied to vectors `P−M` and `P−N`). Instantiating at P=O and
  P=N9 and subtracting cancels the `−(M+N)` term (it is independent of P... 
  more precisely the terms linear in P telescope): `OM²−ON² − (N9M²−N9N²) =
  2(O−N9)·(N−M)`. Since M,N both lie on the nine-point circle (midpoints of
  two sides), N9M = N9N, so N9M²−N9N² = 0, giving `OM²−ON² = 2(O−N9)·(N−M)`.
  Since MN is a midline of ABC, `N−M = (C−B)/2`, giving
  `OM²−ON² = (O−N9)·(C−B)`, whence `OM=ON ⟺ (O−N9)·(C−B)=0`. (This lemma is
  already recorded as certified/shared per the outline review; restated here
  in full for completeness. No new certification needed if already in
  `results/imo-2026-02/lemmas/`.)
- No new lemma toward the main theorem was established this round — the
  concyclicity premise this approach depended on was refuted, not proved, so
  there is nothing further to promote from the synthetic route itself.
