## imo-2026-02 (lens: analytic/computational — coordinates, complex numbers, trig identities)

- Distinct openings:
  1. **1-parameter family + line-locus target.** The three angle-equalities
     (∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK) are only 3 scalar equations in the 4
     coordinates of K,L — the region conditions ("K inside angle LBA" etc., "K
     inside triangle BMC") are inequalities, not equations. So for a fixed
     triangle ABC the valid configurations (K,L) form (numerically) a
     **1-parameter family** (a curve), not an isolated point. The theorem must
     therefore be proved for the whole family at once — a coordinate/algebraic
     approach should look for an identity that holds identically in the free
     parameter, not just verify a single point. This reframes the target: don't
     solve for "the" K,L, find the invariant that makes O·(perp bisector of MN)
     hold along the whole locus.
  2. **Circumcenter-as-vector approach.** Write O as the standard circumcenter
     formula in coordinates (or as a complex-number formula
     `O = A + [(K-A)(L-A)(conj(K-A)-conj(L-A)) - ...]`-style expression) and
     directly show `(O-M)·(N-M) - |N-M|^2/2 = 0` i.e. `O` lies on the
     perpendicular bisector line `{P : |P-M|=|P-N|}`. Numerically this reduces
     (in my coordinate frame with BC on the x-axis) to showing `O_x` equals the
     x-coordinate of the midpoint of MN identically — a strikingly simple target
     if one sets up coordinates with BC horizontal and computes O_x as a
     function of the angle data.
  3. **Trig-Ceva / directed-angle chase to locate K, L via two independent
     spiral-similarity-like constructions**, then use the sine rule on each of
     triangles ABK, ACL, LBK/LNC, LCK/BMK to get algebraic (trig) relations
     among the angles at B and C, feeding into a coordinate computation of O.
     I checked whether ABK ~ ACL as a spiral similarity centered at A (which
     would follow if additionally AB/AC = AK/AL and ∠BAK=∠CAL) — **numerically
     false** (AK/AL ≈ 0.96 while AB/AC ≈ 0.92, and ∠BAK ≠ ∠CAL); so a spiral
     similarity centered at A sending B→C, K→L is NOT the right structure. Do
     not pursue that as a shortcut.
  4. **Complex-number "reflection" ansatz**: since O always sits on the fixed
     line (perp bisector of MN) while K, L vary, and M, N are themselves
     midpoints of AB, AC, there may be a clean complex-number identity
     `2O - A = f(unit circle argument)` where `f` traces a line — i.e. `O - m`
     is purely imaginary times a fixed direction, where `m` = midpoint of MN.
     Worth trying: express K, L via the angle conditions as `B + r·e^{iθ}` etc.
     and see if `O - midpoint(M,N)` is forced orthogonal to `MN` identically in
     the free parameter by algebra (this is a concrete, checkable complex-bash
     target for the outliner/builder).

- Candidate technique(s): coordinate bash with the perpendicular bisector as
  explicit target (`O_x = (M_x+N_x)/2` when BC is the x-axis), OR complex
  numbers with A,B,C as free complex parameters and K,L expressed via the
  angle conditions using arguments of ratios (`arg((K-B)/(A-B)) = arg((A-C)/(L-C))`
  etc, since angle equalities translate to argument equalities of complex
  ratios) — this is the natural complex-number encoding of "∠KBA = ∠ACL" etc.
  and could turn the three angle conditions into three real equations on
  args of complex ratios, directly amenable to algebraic elimination.

- Cheap-kill candidates: none obvious as a full kill, but the **spiral-similarity-
  at-A dead end (see opening 3)** is a cheap thing to rule out before an outliner
  wastes a round on it. Also: checking whether BKLC or AKBL are concyclic is a
  cheap first test (I did not check this numerically — flag for next round if a
  synthetic circle-based approach is proposed, verify concyclicity numerically
  before trusting it).

- Knowledge-base entries to use: "Coordinates / complex / barycentric: place
  coordinates to exploit symmetry" (knowledge_base.md Geometry section);
  "Synthetic toolkit: angle chasing, power of a point, spiral similarity" (for
  cross-checking any synthetic claim numerically before the outliner commits);
  "Trig identities & interval intersection" entry is not directly relevant here
  (that's for a different geometry flavor) but the general sine-rule /
  directed-angle chasing implied by "Synthetic toolkit" is.

- Analogous past problems (cruxes): **none** — `crux_moves_documentation.md`
  states explicitly that geometry is "Not in the corpus yet; the problems DB
  includes geometry problems with solutions, but no geometry cruxes have been
  extracted." So there is no crux-corpus geometry retrieval possible for this
  lens; do not force a match.

- Prior progress: none (results/imo-2026-02/current.md is empty, round 1,
  no approaches yet).

- Dead ends (do not retry):
  - Treating (K,L) as uniquely determined by the 3 angle equations alone (4
    unknowns, 3 equations ⇒ underdetermined by construction; confirmed
    numerically — many distinct (K,L) pairs satisfy all 3 equalities and the
    region constraints for a fixed triangle). An approach that tries to "solve
    for K, L" as an isolated point will fail or silently pick one member of a
    family; the proof must work for the whole family.
  - Spiral similarity centered at A mapping B→C and K→L (checked and refuted
    numerically, see opening 3).

- Small-case / intuition notes (all labeled CONJECTURE / numerically verified,
  not proved):
  - Built a numeric solver (Python, scipy.optimize.fsolve) that, for a fixed
    triangle ABC, treats K_x as a free parameter and solves the remaining 3
    unknowns (K_y, L_x, L_y) from the 3 angle-equality equations, then filters
    solutions where K ∈ triangle BMC and L ∈ triangle BNC (using a
    same-side/barycentric-sign inside-test).
  - Triangle 1: A=(0,3), B=(-2,0), C=(2.5,0). Found 143 valid (K,L) solutions
    across the free parameter. M=(-1,1.5), N=(1.25,1.5), midpoint(M,N) =
    (0.125, 1.5). **In every solution found, O_x = 0.125 to ~1e-9 to
    1e-13 precision**, i.e. O lies exactly on the vertical line x=0.125 (the
    perpendicular bisector of MN, since MN is horizontal in this frame). O_y
    itself varies continuously across solutions (range ≈ 0.90 to 1.79),
    tracing out (numerically) the whole perpendicular-bisector line as the
    parameter varies. Correspondingly `|OM-ON|` was ≤ ~1e-9 in every case —
    consistent with the theorem, not just at isolated points but along the
    entire admissible family.
  - Repeated on two more scalene triangles (A=(0.5,4),B=(-3,0),C=(2,0); and a
    "flatter" triangle A=(1,2.5),B=(-1.5,0),C=(3,0.2)) with the same solver:
    again O always landed exactly on the perpendicular bisector of MN
    (`dot(O - midpoint(M,N), N-M) ≈ 0` to 1e-10 or better) and `max|OM-ON|`
    over ~100 solutions per triangle was ≤ ~2.4e-9 and ≤ 6.4e-10 respectively.
    This is strong numerical (not proof) confirmation that the claim OM=ON
    holds for the *entire* 1-parameter locus of valid (K,L), across triangle
    shapes (acute-ish and flatter/near-degenerate), not just for one special
    K,L.
  - Checked AK/AL vs AB/AC and ∠BAK vs ∠CAL (spiral similarity test at A): NOT
    equal numerically — rules out the naive "spiral similarity at A sends
    B→C, K→L" hypothesis as the mechanism (see Dead ends above).
  - Did NOT check (time-limited): whether K,L,B,C concyclic; whether AO is
    related to the A-median or A-symmedian direction; whether OA is constant
    along the family (numerically OA visibly varies across solutions in my
    runs, e.g. range 1.22–2.10 in triangle 1, so **OA is not constant** — only
    the projection onto the MN-perpendicular direction, i.e. OM=ON, is
    invariant). This rules out "O is a fixed point" as too strong a claim —
    the correct invariant is exactly "O lies on line = perp bisector of MN",
    matching the problem statement precisely (no stronger fixed-point claim
    should be assumed by the outliner).
