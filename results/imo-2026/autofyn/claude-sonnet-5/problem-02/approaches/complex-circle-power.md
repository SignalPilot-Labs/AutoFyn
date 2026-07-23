## Status
unsolved

## Approaches tried
(none yet — new approach, round 1)

## Current best
(empty — outline only, no builder pass yet)

## Approach: complex-circle-power

Target: Prove OM=ON by working in the complex plane with O placed at the
ORIGIN (rather than deriving O's coordinates from A,B,C as in
coordinate-trig-bash) — i.e., treat A, K, L as three points on a circle of
unknown radius R centered at 0, and show |M|=|N| follows from the angle
hypotheses via power-of-a-point / law-of-cosines identities in this frame,
without ever solving for K, L explicitly as functions of a parameter t. This
is a genuinely different computational strategy from coordinate-trig-bash: it
never parametrizes the 1-parameter family explicitly, instead treating A,K,L
as free points on |z|=R and translating the angle hypotheses into constraints
on their arguments, then computing M,N (which depend on B,C, not directly on
the circle) via power-of-the-point-B/-C relative to circle(AKL).

Technique: Complex-number/circle-power method (knowledge_base.md "Coordinates
/complex/barycentric" + "power of a point"). Key trick: for O the circumcenter
of AKL with radius R, the power of any point P w.r.t. circle(AKL) is
|P|² − R² (with O at origin), which for P=B or P=C can be computed two ways:
(i) directly via |B|²−R², and (ii) via any secant/chord through B meeting the
circle — since B is likely NOT on the circle, use the power-of-a-point-via-two-
secants trick if BK or another cevian from B meets circle(AKL) twice
(identify a second intersection point explicitly, e.g. where line BK meets
circle(AKL) again — call it K').

Skeleton:
  1. Place O at the origin, circle(AKL) = {|z|=R}, with A, K, L ∈ ℂ on this
     circle (unknowns: their arguments α, κ, λ, and R). B, C, M, N are then
     determined by the actual triangle: M=(A+B)/2, N=(A+C)/2, but B, C
     themselves are NOT on the circle — they are free points of the plane
     related to A, K, L only through the angle hypotheses.
  2. Express the three angle hypotheses (∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK) as
     complex-number angle-of-quotient equations, e.g. ∠KBA = arg((A−B)/(K−B))
     (up to sign/orientation convention) — standard complex-number angle
     formula. This gives 3 real equations relating B, C (2+2 real unknowns,
     but B,C are actually fixed — the real unknowns are α,κ,λ,R and the
     *shape* of ABC) — need to be careful about what's free vs fixed: for a
     FIXED triangle ABC (hence fixed B,C, and A on the circle only after also
     fixing the circle to pass through the given A), the free unknowns are
     really κ, λ, R (three real parameters) constrained by 3 real angle
     equations — generically a 0- or 1-dimensional solution set, consistent
     with the confirmed 1-parameter family.
  3. Compute the target |M|²−|N|² = |A+B|²/4 − |A+C|²/4 directly in terms of
     A,B,C only (NOT involving K,L,R at all!) — this is a key simplification:
     since M,N depend only on A,B,C, the target reduces to a statement purely
     about A,B,C UNLESS the claim OM=ON is understood correctly as |M|²=|N|²
     in the O-at-origin frame, i.e. |A+B|²=|A+C|² ⟺ 2Re(A·B̄)+|B|² =
     2Re(A·C̄)+|C|² — this is FALSE in general for arbitrary O; it can only
     hold because O is NOT actually placed independent of A,B,C — O is
     determined by A,K,L which in turn are constrained relative to B,C by the
     angle hypotheses. So the real content is: the angle hypotheses, applied
     with O at the origin (i.e. R,κ,λ chosen so that circle(AKL) is exactly
     circle(A,K,L) with the ACTUAL geometric K,L), force
     2Re(A·(B̄−C̄)) = |C|²−|B|² — this is exactly the O_x=p/2 condition
     transported into complex/rotation-invariant form. State this explicit
     target equation and confirm it matches the real-coordinates version from
     coordinate-trig-bash (cross-check both approaches agree on the target).
  4. Attack the target equation via power-of-a-point: let line through B and
     K meet circle(AKL) again at K'; then power of B = BK·BK' = |B|²−R² (with
     sign convention). Similarly for C and a suitable line through L (or K).
     Try to choose the secant lines so that K' or L' is a RECOGNIZABLE point
     (e.g. the second intersection of BM extended, or of BA extended — note
     line BA extended meets the circle at A and possibly a second point A''
     related to K via the angle hypothesis ∠KBA — this is the natural secant
     to try first, since ∠KBA is literally one of the three given angles).
  5. Assemble the power-of-a-point relations from step 4 into the target
     equation of step 3, using the given angle equalities to match up the
     secant angles between the B-side and C-side computations (this again
     surfaces the same B↔C, K↔L duality noted by labeling-duality, but here
     it is used INSIDE a power-of-a-point computation rather than a pure
     algebraic-symmetry argument — a different mechanism, not a duplicate).

Key lemmas (claim + mechanism):
  - Target reduces to 2Re(A·(B̄−C̄)) = |C|²−|B|² in the O-at-origin complex
    frame — because OM²−ON² is bilinear/linear in O and this is its complex-
    number expansion (direct algebra from |M|²=|A+B|²/4 etc.), matching
    coordinate-trig-bash's O_x=p/2 condition under the correspondence A=p+iq,
    B=−1, C=1 (sanity check: 2Re(A(B̄−C̄)) with B=−1,C=1 gives 2Re(A·(−2))=
    −4p, and |C|²−|B|²=0, giving −4p=0 i.e. p=0 only if B,C symmetric about
    origin — reconciling this requires being careful that O is NOT at the
    origin of the B,C-coordinate system in coordinate-trig-bash; this
    reconciliation/consistency check must be done explicitly by the builder
    as the first sanity step, since it is easy to conflate "O at origin" with
    "B,C symmetric about origin" — they are different coordinate choices).
  - Power of point B w.r.t. circle(AKL) via the secant through A (line BA
    extended, since ∠KBA is a given angle) equals BA·BA'' for the second
    intersection A'' — because power-of-a-point is secant-length-product,
    standard theorem (knowledge_base.md).

Open gaps:
  - Step 3's reconciliation between "O at origin" complex frame and
    coordinate-trig-bash's "B,C symmetric about origin" frame must be nailed
    down precisely before proceeding — flagged as an immediate must-check
    (risk of an approach-invalidating frame confusion).
  - The actual power-of-a-point computation (steps 4-5) identifying a useful
    second intersection point is undeveloped and the main computational risk.

Cases to cover: none identified yet.

Watch out for:
  - This approach shares intellectual territory with coordinate-trig-bash
    (both reduce to the "linear condition on O" fact) but attacks the
    remaining work via power-of-a-point / secants rather than explicit
    (r₁(t), r₂(t)) parametrization + sympy elimination — if the builder finds
    they are converging to the identical computation, prefer
    coordinate-trig-bash (more concrete, sympy-checkable) and reduce this
    approach's priority or recast it as a genuinely synthetic power-of-a-point
    finish rather than a parallel algebra grind.
