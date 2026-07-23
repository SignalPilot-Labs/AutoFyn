## imo-2026-02

coordinate-trig-bash: revise
Target: OM=ON for the given configuration (K,L,M,N,O as in the problem statement).
Technique: Coordinate/trig bash with an explicit θ-parametrized ray family
(certified Lemmas 1-3 in `lemmas/coordinate-om-on-reduction.md` and the
approach file), now closing the branch-isolation gap via single-variable
monotonicity/IVT instead of Positivstellensatz/Gröbner.
Skeleton:
  1. (Certified) OM=ON ⟺ O_x=p/2 — Lemma 1.
  2. (Certified) Circumcenter formula for AKL — Lemma 2.
  3. (Certified) Ray parametrization K=B+r1·u_K(θ), L=C+r2·u_L(θ), with
     u_K, u_L fixed unit directions depending only on θ,p,q — Lemma 3.
  4. NEW (this round): Prove the **decoupling lemma** rigorously (not just
     numerically): F1(θ,r1,r2):=∠LBK−∠LNC is independent of r1, and
     F2(θ,r1,r2):=∠LCK−∠BMK is independent of r2 — by symbolic partial
     differentiation (sympy) or the direct structural argument: ray BK has
     direction u_K(θ) fixed regardless of r1 (K only slides along a fixed
     ray from B); in ∠LBK the two rays are BL (from B to L, depends on r2)
     and BK (fixed direction u_K(θ), independent of r1); wait — the angle
     ∠LBK is *at vertex B*, between ray BL and ray BK, and BOTH depend on
     which vertex; the actual claimed independence is on ∠LNC (vertex N,
     ray NC fixed since C fixed, ray NL depends on L hence r2 only) vs ∠LBK
     (vertex B: ray BK has FIXED direction u_K(θ) independent of r1, ray BL
     depends on r2) — so F1 is a function of θ and r2 ONLY (not r1); confirm
     this precisely algebraically, not just restate the numeric claim.
     Symmetrically F2 is a function of θ, r1 only. Write this up as a
     genuine lemma with a proof (not merely "verified numerically to 1e-13").
  5. NEW: Prove **strict monotonicity** of F1(θ,·) in r2 and F2(θ,·) in r1
     on the containment-valid domain r2∈(0,r2max(θ)), r1∈(0,r1max(θ)) — via
     an explicit derivative-sign computation (d/dr2 of each arccos term has
     a determinable sign from the geometry: as r2 increases, L moves away
     from C along a fixed ray, so ∠LNC and ∠LBK both vary monotonically in
     a provable direction — e.g. via the "angle subtended by a segment as
     the far endpoint recedes along a fixed ray" fact, which itself should
     be proved as a mini-lemma using the law of sines / exterior angle
     argument, not asserted). This + a sign change at the two endpoints
     (r2→0+ giving F1>0 by an explicit limiting computation, r2→r2max
     giving F1<0, both provable in closed form since the endpoints are
     geometrically meaningful — r2→0 is L→C degenerate, r2max is L exiting
     the triangle) gives existence+uniqueness of r2(θ) via IVT — a fully
     rigorous, elementary substitute for Gröbner/Positivstellensatz.
  6. Having pinned down r1(θ), r2(θ) as the UNIQUE roots on the valid
     domain (steps 4-5, both single-variable), substitute into Lemma 2's
     circumcenter formula and simplify O_x − p/2 along this specific curve.
     Since r1(θ), r2(θ) are still only characterized implicitly (as roots
     of transcendental arccos equations, no closed form found), this final
     algebraic verification likely needs either (a) an implicit-function /
     derivative argument showing d/dθ(O_x − p/2)=0 identically plus one
     verified base case (θ→0 or a symmetric special case), or (b) a
     resultant-based elimination restricted to the now RIGOROUSLY isolated
     single branch (justified this time, unlike round 1, because the branch
     is pinned down by monotonicity+IVT rather than asserted from numerics).
Key lemmas (claim + mechanism):
  - Decoupling: F1 depends only on (θ,r2), F2 only on (θ,r1) — because ray
    BK's direction is fixed once θ is fixed (K only slides along that ray,
    changing r1 moves K but not the ray's direction, hence doesn't change
    any angle measured using only that ray's direction as one of its two
    legs when the OTHER leg doesn't involve K's position along the ray in a
    way that matters — precise proof needed: an angle ∠(V;P,Q) generally
    depends on |VP|,|VQ| too, not just directions, UNLESS V is on the ray
    through P... this needs care, flag as the first thing the builder must
    nail down rigorously, since the naive "direction-only" argument in the
    explorer report is not obviously complete — arccos of a dot product
    ratio depends on both direction AND magnitude in general, so the
    independence claim needs the specific structure of B being the vertex
    of the ray, not just "fixed direction."]
  - Monotonicity: F1(r2) strictly monotone on the valid domain — because
    (heuristically) increasing r2 moves L monotonically away from C along a
    fixed ray, so both ∠LBK and ∠LNC vary monotonically with the same or
    complementary sign; needs a genuine proof (derivative sign or a
    synthetic "angle subtended from a fixed point by a point receding along
    a ray is monotone" fact — this classical fact IS true and provable via
    the law of sines in the moving triangle, cite as needed).
Open gaps: Step 4's independence claim needs a rigorous (not just numeric)
proof — flag to the builder that the naive "fixed direction ⇒ independent"
argument in the explorer report may be incomplete since arccos depends on
magnitudes too; re-derive carefully. Step 5's monotonicity and endpoint
signs need closed-form derivative work. Step 6 (final substitution) is
still open even after branch isolation — this approach may close the
*existence/uniqueness* gap this round but not yet the whole problem.
Cases to cover: none (single continuous family, θ ranges over (0,min(β,γ))).
Watch out for: do not re-claim the branch-isolation gap "closed" until the
independence lemma is proved symbolically, not just checked to 1e-13 on 6
configs — that numeric confirmation is real evidence but not a proof.

labeling-duality: revise
Target: OM=ON, via the certified reduction to (TI): pow_Γ(B)−pow_Γ(C) =
(AB²−AC²)/2, Γ=circumcircle(AKL) (see `lemmas/median-length-power-reduction.md`).
Technique: Power of a point + inscribed-angle/law-of-sines chase using the
shared parameter θ, per the synthetic-gap explorer's most promising untried
lever (radical axis of Γ vs circumcircle(ABC) is a second untried lever to
combine with this).
Skeleton:
  1. (Certified) Reduction OM=ON ⟺ (TI) — already proved, reuse directly.
  2. NEW: In triangle ABK, angle θ=∠KBA is known (hypothesis 1) and AB is
     known (side of the fixed triangle); apply law of sines in triangle ABK
     using ∠AKB (unknown, but the third angle once ∠BAK is expressed via
     β and other knowns) to get BK as an explicit trig function of θ, β
     (and AB). Symmetrically get CL as an explicit trig function of θ, γ, AC
     in triangle ACL.
  3. NEW: Use condition (3), ∠LCK=∠BMK, in triangle BMK: extended law of
     sines gives BK/sin∠BMK = BM/sin∠BKM, i.e. BK·sin∠BKM = BM·sin∠BMK =
     BM·sin∠LCK (substituting condition 3). Since BM=AB/2 is known, and BK
     is now known from step 2, this gives a relation pinning sin∠BKM (hence
     the direction of ray KM relative to KB) as a function of θ,β,γ. Repeat
     symmetrically with condition (2) in triangle CNL for CL, sin∠CLN.
  4. NEW: With BK, CL, and enough angle data at K, L (from step 3) pinned
     down purely in terms of θ,β,γ (and the fixed side lengths of ABC), find
     ∠AKL and ∠ALK (needed to locate the second intersection of line BA or
     CA with Γ, i.e. to compute pow_Γ(B), pow_Γ(C) via the secant-through-A
     trick the explorer flagged as blocked without this data) — this is the
     step that was blocked before; steps 2-3 are meant to supply exactly the
     missing angle data at K, L that stalled the original secant attempt.
  5. Compute pow_Γ(B) = BA·BA′ (A′ = second intersection of line BA with Γ,
     located via inscribed-angle theorem using ∠AKL/∠ALK from step 4), and
     pow_Γ(C) similarly, then verify (TI) by direct trig substitution.
  6. (Parallel/fallback lever, not required if 2-5 succeeds) Radical axis
     idea: pow_Γ(B)−pow_Γ(C) = [pow_Γ(B)−pow_Ω(B)] − [pow_Γ(C)−pow_Ω(C)]
     where Ω=circumcircle(ABC) (pow_Ω(B)=pow_Ω(C)=0 trivially since B,C∈Ω);
     the bracketed differences are controlled by the (fixed, A-independent-
     of-K,L) radical axis of Γ and Ω, which passes through A perpendicular
     to line OO_Ω. If this radical axis can be located explicitly using only
     A, β, γ (i.e. independent of where exactly K,L sit beyond fixing Γ),
     (TI) might reduce to a single clean trig identity in β,γ,θ. Flag for a
     builder to try symbolically (sympy) before committing to the full
     synthetic law-of-sines chase of steps 2-5, since if it works it is
     much shorter.
Key lemmas:
  - BK = AB·sinθ/sin∠AKB-type explicit trig formula — because law of sines
    in triangle ABK with known angle θ at B and known side AB.
  - Radical axis of Γ,Ω passes through A, perpendicular to OO_Ω — because
    two circles' radical axis is always perpendicular to the line joining
    their centers, and A is a common point (A∈Γ∩Ω... wait, ABC's
    circumcircle Ω passes through A,B,C, and Γ passes through A,K,L — they
    share exactly the point A generically, so A is one point of the radical
    axis but the radical axis is determined by A and the perpendicularity
    direction, not by two shared points; note this carefully — if Γ,Ω are
    NOT tangent at A they meet at a second point too, need to check).
Open gaps: Steps 2-5 (the full law-of-sines chase) are UNTRIED — this is the
main content to build this round. Step 6 (radical axis) is a cheaper
untried alternative worth a quick symbolic sanity check first.
Cases to cover: none additional beyond what's already handled by the
reduction (single continuous family).
Watch out for: the secant-through-A route was explicitly checked by the
synthetic-gap explorer and A′ (second intersection of BA with Γ) does NOT
coincide with any named point — so step 4/5 requires genuinely computing
∠AKL, ∠ALK via steps 2-3's data, not hoping for a shortcut identification.

antipode-perp-bisector: new
Target: OM=ON.
Technique: A completely different reduction, avoiding power-of-a-point on
B,C entirely — via the antipode A* = 2O−A of A on Γ=circumcircle(AKL), using
only that M=(A+B)/2, N=(A+C)/2, and Thales' theorem (angle in a semicircle).
This is the diversification move away from the shared (TI)/O_x=p/2 gap that
both coordinate-trig-bash and labeling-duality are stuck on — a genuinely
different top-level target (a perpendicularity/incidence statement, not a
scalar power identity).
Skeleton:
  1. Define A* := 2O − A (the point antipodal to A on Γ; well-defined since
     O is Γ's center and A∈Γ, so A* is just the reflection of A through O,
     always on Γ).
  2. LEMMA (fully elementary vector algebra, proved from scratch): since
     M=(A+B)/2, A*−B = (2O−A)−B = 2(O−(A+B)/2) = 2(O−M), so |A*B| = 2·OM.
     Identically, since N=(A+C)/2, A*−C = 2(O−N), so |A*C| = 2·ON. Hence
       **OM = ON ⟺ A*B = A*C ⟺ A* lies on the perpendicular bisector of BC.**
     (This equivalence is complete and gap-free — no case analysis, holds
     for any position of O, A, B, C as long as M,N are the stated midpoints.)
  3. LEMMA (Thales, fully elementary): since A, A* are antipodal on Γ (O is
     the midpoint of AA* and the center of Γ), and K, L ∈ Γ, the inscribed
     angles ∠AKA* and ∠ALA* both subtend the diameter AA*, hence
       ∠AKA* = ∠ALA* = 90°.
     So A* is characterized synthetically, with NO reference to O or circle
     power, as: **the intersection of the line through K perpendicular to
     AK, and the line through L perpendicular to AL.**
  4. Reduce the whole problem to: show that the intersection point A* of
     (perpendicular to AK at K) and (perpendicular to AL at L) lies on the
     perpendicular bisector of BC, i.e. A*B = A*C.
  5. NEW computational step (open — the actual content of the proof): show
     A*B=A*C using the angle hypotheses. Concrete lever: in right triangle
     A*KB (right angle NOT at K in general — ∠AKA*=90° is the angle at K in
     triangle AKA*, not directly a right angle in triangle A*KB; need
     ∠A*KB = 90° ± ∠AKB depending on configuration/orientation, since
     ∠AKA*=90° and ∠AKB is a known-ish quantity), apply the law of cosines
     or the Pythagorean-adjacent relation A*B² = A*K² + KB² ∓ 2·A*K·KB·cos(...)
     to express A*B² using KB (known from labeling-duality's step 2 style
     law-of-sines work, or independently), A*K (= 2R sin∠ALK via extended
     law of sines in Γ, chord A*K subtends arc equal to ∠ALK... verify
     carefully which inscribed angle), and the angle between KA* and KB.
     Do the same for A*C² via triangle A*LC. Show the two expressions are
     equal using hypotheses (1)-(3). This is the open computational gap;
     flag explicitly for the builder — do NOT claim it's easy.
  6. Alternative for step 5: coordinate/complex verification as a fallback —
     since A* has the simple closed form 2O−A, and O_x=p/2, O_y is already
     known in closed form from coordinate-trig-bash's Lemma 2 (once O is
     found), A*B=A*C can be checked directly in the SAME coordinate frame,
     but this reduces back to needing O in closed form on the correct
     branch, i.e. reinherits coordinate-trig-bash's branch-isolation gap —
     so the synthetic route (step 5 as stated) is the one that genuinely
     avoids the shared gap; prioritize it.
Key lemmas:
  - OM=ON ⟺ A*B=A*C — because A*=2O−A makes A*−B = 2(O−M) and A*−C=2(O−N)
    by direct substitution of M,N as midpoints; pure vector algebra, no
    hidden case split.
  - ∠AKA*=∠ALA*=90° — because AA* is a diameter of Γ and K,L∈Γ (Thales'
    theorem / angle inscribed in a semicircle, standard, cite by name).
Open gaps: Step 5 (showing A*B=A*C from the angle hypotheses via the two
right-triangle relations at K and L) is entirely open — this is the
approach's whole remaining content. The mirror-refuted mechanisms (spiral
similarity BKL~NLC, concyclicity through C,K,M) are DIFFERENT claims from
what step 5 needs (those were about B,K,L,N or C,K,L,M directly; step 5
is about A*,K,B and A*,L,C, a different point set) — do not assume step 5
is dead just because those were refuted, but do check numerically first
before investing in a full synthetic derivation.
Cases to cover: none identified yet beyond standard orientation (verify A*
lies on the same side / the right-angle sign convention ∠A*KB=90°+∠AKB vs
90°−∠AKB is resolved consistently — flag to builder to check both branches
numerically on the same test triangle before writing the general proof, so
the orientation is pinned down empirically before being proved).
Watch out for: this reduction is proven completely rigorously already (step
2, step 3) — the ONLY open content is step 5. Don't waste builder time
re-deriving steps 1-4; start directly from "show A*B=A*C given the angle
hypotheses and A*'s synthetic Thales characterization."

nine-point-link: advance
Target: OM=ON, via relating circle(AKL) to the nine-point circle of ABC.
Technique: Circle transformation toolkit (as in the existing outline).
Skeleton: as already written in `approaches/nine-point-link.md` (unbuilt).
Key lemmas: as already stated there.
Open gaps: entire approach unbuilt; still speculative (explorer notes this
is the weakest-grounded approach in the field). Given this round's stronger
new lever (antipode-perp-bisector) is a cleaner, already-partially-proved
diversification, deprioritize nine-point-link relative to it unless the
build set has spare capacity — advance only as a lower-priority pick.
Cases to cover: none beyond what's in the existing file.
Watch out for: the file itself flags O ≠ nine-point-center numerically, so
any argument must not assume that coincidence.

complex-circle-power: advance
Target: OM=ON, via complex numbers with O at the origin.
Technique: as already written in `approaches/complex-circle-power.md`
(unbuilt).
Skeleton: as already written there.
Open gaps: entire approach unbuilt.
Cases to cover: none beyond what's in the existing file.
Watch out for: likely to re-encounter the same branch-selection issue as
coordinate-trig-bash (same underlying algebra, different coordinates) unless
it also adopts the decoupling/monotonicity route from coordinate-trig-bash's
revision this round — note this link for whichever builder picks it up.

build set: antipode-perp-bisector, coordinate-trig-bash, labeling-duality
