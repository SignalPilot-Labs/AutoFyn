## Status
unsolved

## Approaches tried
(none yet — new approach, round 1)

## Current best
(empty — outline only, no builder pass yet)

## Approach: nine-point-link

Target: Prove OM=ON by relating the circumcircle of AKL to the nine-point
circle of ABC (which passes through M and N, the midpoints of AB, AC) — a
different top-level target than computing O directly: instead show a fixed
transformation (inversion, or a spiral similarity / homothety) carries
circle(AKL) to a circle centered on the perpendicular bisector of MN, or
carries the pair (M,N) to a pair of points that are visibly symmetric relative
to O.

Technique: Classical circle-transformation toolkit (inversion, spiral
similarity, radical axis) per knowledge_base.md "Synthetic toolkit." This is
the most speculative/exploratory approach in the field — put up because the
projective-lens explorer flagged a suggestive (unproven) numeric coincidence:
O's x-coordinate matched the nine-point center's x-coordinate in one test case,
and the nine-point circle is exactly the circle through M, N (and the third
midpoint of BC), so its center is manifestly equidistant from M and N already.
If circle(AKL) can be shown to share the SAME perpendicular bisector of MN as
the nine-point circle — without literally being the nine-point circle (it
isn't: OA≠OM numerically per the explorer) — that would give a clean proof.

Skeleton:
  1. Recall the standard fact: the nine-point circle of ABC passes through the
     three midpoints of the sides (M, N, and midpoint of BC) — by the standard
     nine-point circle theorem (not yet in knowledge_base.md explicitly, but a
     classical fact citable directly: "the midpoints of the three sides, the
     feet of the three altitudes, and the midpoints of segments from each
     vertex to the orthocenter, all lie on one circle"). Its center, the
     nine-point center N₉, is the midpoint of OH (circumcenter-orthocenter of
     ABC) and is trivially equidistant from M and N as they're both on that
     circle.
  2. State precisely what must be shown: O (circumcenter of AKL) is NOT N₉ in
     general (ruled out numerically by the projective explorer), but O and N₉
     both lie on the perpendicular bisector of MN. So the goal reduces to:
     find the actual relationship between O and this fixed perpendicular
     bisector line ℓ = perp-bisector(MN), without needing O = N₉.
  3. Attempt an inversive/projective link: consider whether inversion centered
     at A (which fixes lines through A and swaps circles/lines through the
     center's "opposite" data) maps K,L to points K*,L* related to B,C or M,N
     in a way that transfers "circle(AKL) centered on ℓ" to a known incidence.
     Concretely: check whether inversion at A with power AM·AB = AN·AC
     (both equal (AB²)/2 and (AC²)/2 respectively — NOT equal in general
     unless AB=AC, so a single inversion at A does not simultaneously fix both
     M and N as A M·AB, A N·AC differ — this must be checked/adjusted,
     possibly using two different auxiliary circles or a spiral similarity
     instead of inversion).
  4. Alternative mechanism: try to directly express O·(C−B) (the quantity
     controlling O_x, cf. coordinate-trig-bash's step 2) as a sum of two
     "local" contributions, one from the perpendicular bisector of AK and one
     from AL, and match each to a known length relation from the angle
     hypotheses via the extended law of sines in circle-cutting sub-triangles
     (e.g. circle(ABK) or circle(ACL) if such circles are natural — must be
     checked whether A,B,K or A,C,L support a clean circle with an inscribed-
     angle read of the given angle equalities).
  5. If a genuine transformation link cannot be found, fall back to reporting
     the nine-point circle fact itself (step 1) as a certified, reusable
     lemma (import into other approaches: "M, N, midpoint(BC) are concyclic,
     center N₉ equidistant from M,N") — a legitimate partial contribution to
     the shared lemma cache even if this approach's main thrust stalls.

Key lemmas (claim + mechanism):
  - Nine-point circle passes through M, N (and midpoint of BC): standard
    theorem — because M and N are each the midpoint of a chord AB, AC and the
    classical nine-point circle theorem places all three side-midpoints on
    one circle (proof: the medial triangle MNP is similar to ABC with ratio
    1/2 and the same orientation, so its circumcircle, the nine-point circle,
    is the image of circle(ABC) under the homothety at the centroid G with
    ratio −1/2 composed appropriately — standard citation).
  - (Open, speculative) circle(AKL) and the nine-point circle share the same
    perpendicular bisector of MN as an axis — because [mechanism not yet
    found; the candidate mechanisms are inversion at A or a two-step spiral
    similarity, both unconfirmed].

Open gaps:
  - The core transformation link (steps 3-4) is NOT established — this is the
    speculative heart of the approach and the primary risk it does not close
    at all. This approach should be evaluated after 1 round of builder effort;
    if no concrete transformation is found, downgrade priority in favor of
    coordinate-trig-bash / labeling-duality.
  - Even if a transformation is found, must confirm it respects the
    containment/orientation hypotheses (not just the angle equalities).

Cases to cover: none identified (would be a uniform synthetic argument if it
works).

Watch out for:
  - Do NOT assume O = nine-point center (explicitly refuted numerically by
    the projective explorer — O moves along the family, N₉ is fixed for a
    given ABC). The claim is only that they share membership on line ℓ, not
    that they coincide.
  - Do NOT re-attempt the already-refuted hypotheses from the projective
    explorer's dead ends (spiral similarity BK↔CL at A with ratio BK/BA=
    CL/CA; M,K,N,L concyclic) — these are recorded dead ends, not to be
    retried in disguise here.
  - This is the highest-risk / most speculative approach in the field —
    include it for framing diversity, but do not let it consume
    disproportionate builder time if step 3/4 doesn't yield a mechanism
    quickly.
