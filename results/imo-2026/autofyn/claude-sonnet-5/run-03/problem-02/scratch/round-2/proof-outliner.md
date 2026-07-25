## imo-2026-02

Context (all four approaches below build on the certified, gap-free reduction
already established in round 1 — import, do not re-derive):
- `lemmas/vector-reduction-OM-ON.md`: OM=ON ⟺ O·(C−B) = (|C|²−|B|²)/4 (A at origin).
- `lemmas/amnq-concyclic-and-reduction.md`: Q := reflection of A in the
  perpendicular bisector ℓ of MN is the unique point with AQ∥BC, QB=QC; A,M,N,Q
  concyclic; and **A,K,L,Q concyclic ⟹ OM=ON** (fully proved, gap-free, modulo
  the isosceles caveat AB=AC where Q=A — see Watch out for below, common to
  all four approaches).
- The ONE remaining gap for the whole population: **prove A,K,L,Q concyclic**
  using the three angle hypotheses (∠KBA=∠ACL, ∠LBK=∠LNC, ∠LCK=∠BMK) and the
  four containment conditions. Three round-1 routes (synthetic directed-angle
  chase, Cartesian coordinate/Gröbner elimination, power-of-a-point) all
  stalled here — this is a same-framing plateau (CLAUDE.md's shared-gap rule).
  This round's field puts up ONE genuinely different top-level technique
  (Ptolemy/Law-of-Sines) plus a genuinely different *algebraic mechanism* for
  the synthetic chase (complex cross-ratio), alongside pushing the two most
  mechanical routes forward with sharper next steps.
- Family-wide dead ends confirmed this round (do NOT retry in any approach
  below): no fixed length ratio among {AK/AL, BK/CL, MK/NL} exists (all drift
  along the 1-parameter family); no hidden similar triangle touches K or L
  (exhaustive AA-search over all 56 triangles on the 8 named points, family-
  wide); no hidden concurrency of BK,CL at vertex B/C, BKLC not concyclic; no
  hidden 4-point concyclic subset among {A,B,C,K,L,M,N,Q} other than the
  known (A,M,N,Q) and the target (A,K,L,Q) (exhaustive 70-subset search,
  reconfirmed twice); no naive spiral similarity at A (B↦C,K↦L) or at K
  (B↦L) or center-S (B↦K,C↦L) — all numerically refuted. Any lemma proposed
  below must not silently assume one of these.

---

ptolemy-trig-identity: new
Target: The problem's whole claim OM=ON, via the standard reduction chain
  (import the two certified lemmas above) reduced to proving A,K,L,Q
  concyclic — proved here by a **length identity** (Ptolemy), not an angle
  chase or Cartesian elimination.
Technique: Law of Sines chase in the four auxiliary triangles the hypotheses
  naturally hand us (ABK, ACL, BMK, CNL), feeding six explicit length
  expressions into Ptolemy's theorem (knowledge_base.md, Circle/triangle
  configuration facts: for four points in convex cyclic order W,X,Y,Z,
  WY·XZ = WX·YZ + XY·WZ, with equality iff W,X,Y,Z concyclic in that order —
  cite the converse direction explicitly). This is a length-algebra route,
  structurally different from both coordinate-bash's Cartesian polynomial
  elimination and fixed-point-concyclic's pure directed-angle chase.
Skeleton:
  1. Import Lemma A (A,M,N,Q concyclic) and Lemma B (concyclic(A,K,L,Q) ⟹
     OM=ON) verbatim from `lemmas/amnq-concyclic-and-reduction.md` — no
     re-proof needed.
  2. Establish the cyclic order A,K,L,Q is convex in that order (numerically
     confirmed by the trig explorer; must be proved synthetically here, not
     assumed) — by the containment hypotheses "K inside ∠LBA" and "L inside
     ∠ACK" plus AQ∥BC (Lemma 2) placing Q on the far side of line BC from
     A's interior rays to K, L, this pins the angular order of rays AK, AL,
     AQ around A; combine with K,L both lying strictly between rays
     AB,AC-ish sectors (from the triangle-interior containments K∈△BMC,
     L∈△BNC) to get the order. This is a genuine sub-lemma, not automatic —
     flag as an explicit step, not "clearly."
  3. Let θ := ∠KBA = ∠ACL (hypothesis 1). In triangle ABK: angle at B is θ,
     angle at A is an unknown α (a function of the family's free parameter);
     Law of Sines gives AK = AB·sin θ / sin(θ+α), BK = AB·sin α / sin(θ+α).
     Symmetrically in triangle ACL: angle at C is θ, angle at A is unknown
     α′; AL = AC·sin θ / sin(θ+α′), CL = AC·sin α′ / sin(θ+α′).
  4. Feed hypothesis 2 (∠LBK=∠LNC =: φ) through triangle BMK (angle at M is
     hyp. 3's ψ := ∠LCK=∠BMK, BM = AB/2 known) and triangle LNC (angle at N
     is φ, NC = AC/2 known) to express BK, NL and CL, BL respectively via a
     second Law-of-Sines pass — this is where α, α′ get pinned as functions
     of ONE free parameter (matching the family's known 1 degree of freedom;
     do not over-constrain to a point solution — carry the free parameter
     symbolically throughout, per the explorer's confirmed dead end that no
     length ratio is family-constant).
  5. Compute AQ, KQ, LQ: AQ is a fixed function of triangle ABC alone (via
     Lemma 1's closed form for Q — no free parameter), while KQ, LQ are
     obtained either via Law of Cosines in triangles AKQ, ALQ using AK/AL
     from step 3 and the angle ∠KAQ = ∠(AK,AQ) (expressible via θ and the
     known direction of AQ ∥ BC from Lemma 2), or via a second Law-of-Sines
     pass in the same auxiliary triangles.
  6. Substitute all six lengths into the Ptolemy target
     AL·KQ = AK·LQ + KL·AQ and show it is a trigonometric identity in θ and
     the free parameter, using the two elimination relations from step 4 —
     i.e. show the identity holds not at a point but identically along the
     whole 1-parameter family (sum-to-product / angle-addition manipulation,
     verified symbolically with sympy before writing the human-readable
     algebra).
  7. Handle the degenerate case AB=AC (Q=A) separately — see Watch out for.
Key lemmas (claim + mechanism):
  - Ptolemy's theorem (equality case, convex cyclic order) — because for
    W,X,Y,Z concyclic in that order, rotating triangle WXY about a spiral
    similarity at Y sending W↦Z (or the standard trig proof via
    Law of Sines applied to the two triangles cut by a diagonal) gives the
    identity; the converse (equality ⟹ concyclic, for four points already
    known to be in convex position W,X,Y,Z) follows since the identity
    characterizes the degenerate/extremal case of the general Ptolemy
    inequality (knowledge_base.md).
  - Law of Sines in ABK / ACL / BMK / CNL — because each triangle has one
    hypothesis-given angle and one known side (AB, AC, BM, CN are all
    determined by the fixed triangle ABC), so the other two sides are
    explicit trig functions of the triangle's third angle.
  - The elimination identity (step 6 collapsing to 0=0) — because the two
    Law-of-Sines passes (steps 3–4) express every length in terms of the
    SAME free parameter and θ, so Ptolemy's difference AK·LQ+KL·AQ−AL·KQ,
    expanded, must vanish as a rational-trig-function identity once the
    hyp-2/hyp-3 constraint relations are substituted — this is the concrete,
    checkable target (verify symbolically with sympy first).
Open gaps: step 2 (cyclic order, needs a careful containment argument, not
  yet written out); steps 3–6 (the actual Law-of-Sines elimination — set up
  here, not executed); step 7 (isosceles case).
Cases to cover: generic scalene ABC (main line of attack); degenerate
  AB=AC (Q=A) needs a separate argument, common to all four approaches below.
Watch out for: (1) do NOT assume a fixed length ratio anywhere — confirmed
  false by this round's family-wide sweep; (2) the "unknown angle α" in each
  Law-of-Sines triangle is NOT independently free — hyp. 2/3 pin it via M, N,
  so the elimination must actually carry those constraints, not just assert
  Ptolemy holds termwise; (3) Ptolemy's equality case requires the CONVEX
  cyclic order A,K,L,Q — using the wrong pairing (e.g. AL·KQ vs AK·LQ+... in
  the wrong assignment) silently proves nothing, or worse, a false statement
  (the trig explorer confirmed the wrong pairing gives residual 10–50, not 0)
  — get the order lemma (step 2) genuinely right before running Ptolemy.

fixed-point-concyclic: revise
Target: unchanged — OM=ON via A,K,L,Q concyclic (same overall route: define
  Q, prove the two certified lemmas, close the concyclicity gap). Revising
  ONLY the mechanism for the stuck Step 3 (concyclicity), which was a plain
  real-plane directed-angle chase that has not closed after two rounds.
Technique: switch Step 3's mechanism from real-plane directed-angle chasing
  to a **complex-number cross-ratio** computation — represent all points as
  complex numbers (A at origin as already set up), and use the standard
  criterion: four points z1,z2,z3,z4 (no three collinear) are concyclic or
  collinear iff the cross ratio (z1−z3)(z2−z4) / [(z1−z4)(z2−z3)] is real.
  This is algebraically the same content as the directed-angle criterion but
  the complex-conjugate algebra (multiply by z̄/z relations, use |z|²=z z̄)
  often collapses trig-identity verification faster than either raw
  Cartesian coordinates (coordinate-bash's stalled Gröbner route) or a pure
  synthetic angle chase (this approach's own stalled Step 3) — a genuinely
  different algebraic vehicle for the SAME target, not a re-run of either.
Skeleton:
  1. Keep Steps 1–2 verbatim (Lemmas 1–5, already certified/proved — Q's
     vector formula, A,M,N,Q concyclic, the reduction lemma). No change.
  2. Re-express the three hypothesis angle equalities as complex-number
     ratio equations: ∠KBA=∠ACL becomes arg((k−b)/(a−b)) = ±arg((a−c)/(l−c))
     (mod π) for complex a=0,b,c,k,l — i.e. (k−b)/(a−b) divided by its own
     conjugate equals the same ratio for (a−c)/(l−c), OR (the branch fixed
     by the containment hypotheses, per the round-1 rule "use signed/
     directed angles since containment selects the branch") the two ratios
     are positive real multiples of each other's conjugate-normalized form.
     Do this explicitly for all three hypotheses (∠KBA=∠ACL, ∠LBK=∠LNC,
     ∠LCK=∠BMK), producing three complex-algebraic constraint equations in
     k, l (with b,c,m=b/2,n=c/2 fixed).
  3. Compute q (Q's complex coordinate) from the already-certified vector
     formula (Lemma 1), and form the cross ratio
     χ := (a−l)(k−q) / [(a−q)(k−l)] with a=0, i.e. χ = −l(k−q)/(q(k−l))
     (using a=0). Target: show χ ∈ ℝ (equivalently χ = χ̄), using the three
     constraint equations from step 2.
  4. Use conjugation algebra: for each hypothesis constraint from step 2,
     also write down its conjugate equation (since k̄,l̄,b̄,c̄ are the
     conjugates of the same points — NOT independent unknowns), and eliminate
     k̄, l̄ (and correspondingly k,l) using the constraint pairs, reducing
     χ − χ̄ to an expression that must vanish given the constraints — this
     is the elimination, done in complex variables instead of x,y.
  5. Handle the degenerate case AB=AC (Q=A, χ undefined/degenerate) — see
     Watch out for; likely needs the same limiting-argument fix noted in the
     existing file's Remark, made rigorous.
Key lemmas (claim + mechanism):
  - Cross-ratio-real criterion for concyclicity — because the cross ratio of
    four points is invariant under Möbius maps, and a Möbius map sending
    three of the points to 0,1,∞ sends the circle/line through them to the
    real axis; the fourth point lies on that circle/line iff its image is
    real, i.e. iff the cross ratio is real (standard fact, knowledge_base.md
    Synthetic toolkit / inversion-projective ideas — cite explicitly).
  - The conjugate-elimination step (4) — because each hypothesis angle
    equality, written as a ratio-of-differences equation, has a conjugate
    counterpart obtained by bar-ing every symbol (points map to their own
    conjugates since A,B,C,M,N are real data w.r.t. a chosen real axis, or
    more generally by treating z̄ as an independent formal symbol subject to
    the same three constraint equations bar-ed) — this lets one eliminate
    k̄,l̄ algebraically rather than geometrically, mirroring coordinate-bash's
    elimination but in a coordinate system where reflections/perpendicular
    bisectors (already used to define Q) are natively multiplicative.
Open gaps: step 2's precise branch-selection (which ratio equals which,
  fixed by the containment hypotheses — must be nailed down explicitly, not
  guessed) and the full elimination in steps 3–4 (not executed this round).
Cases to cover: generic scalene (main target); AB=AC degenerate case.
Watch out for: this is the SAME gap as the file's existing Step 3 in a new
  algebraic language — if the complex-number elimination also stalls after a
  serious attempt, that is strong evidence the real difficulty is
  combinatorial/degree-of-the-identity, not the choice of algebra, and the
  next round should not try a fourth encoding of the same chase without new
  structural insight (e.g. a genuinely different auxiliary point). Also:
  don't silently assume A is real/on an axis in a way that hides a
  dependency — A is the origin but B,C are general complex numbers, keep
  full generality.

coordinate-bash: advance
Target: unchanged — OM=ON via O·(C−B) = (|C|²−|B|²)/4, using the already-
  proved rotation parametrization (K,L via one angle β and two lengths
  t1=BK, t2=CL) and the two polynomial constraint equations from hypotheses
  2–3, whose final elimination stalled last round (Gröbner basis too large).
Technique: same overall route (Cartesian coordinate/rotation
  parametrization + polynomial elimination), with two concrete next steps to
  make the elimination tractable that were not tried last round:
  (a) exploit the certified σ-symmetry lemma (`lemmas/sigma-symmetry.md`,
  swap B↔C,K↔L,M↔N) to only eliminate "half" the system and obtain the
  other half by the symmetry, roughly halving the polynomial degree/variable
  count the Gröbner basis has to handle; (b) replace the general-purpose
  Gröbner basis with a targeted Sylvester-resultant elimination, eliminating
  t1 first (using hyp. 3's equation, the one most directly tied to t1 via M)
  then t2 (using hyp. 2's equation), instead of a simultaneous Gröbner basis
  over all four variables t1,t2,s=sinβ,cc=cosβ at once.
Skeleton:
  1. Reuse the exact reduction and rotation parametrization already in the
     file (no re-derivation needed — cite verbatim).
  2. Apply σ-symmetry: note that proving the target identity's dependence on
     t2, and hyp-2's constraint, is literally the σ-image of proving it in
     t1 and hyp-3's constraint (already proved as a lemma) — so it suffices
     to carry out ONE elimination (say eliminate t1 via hyp-3) explicitly and
     invoke σ for the other, cutting the symbolic computation roughly in half.
  3. Eliminate t1 from hyp-3's polynomial constraint via a Sylvester
     resultant with the target-identity polynomial (viewing both as
     polynomials in t1 over the field ℚ(t2,s,cc)), producing a polynomial
     R1(t2,s,cc) that must vanish given hyp-2's constraint.
  4. Substitute hyp-2's constraint (as a second resultant, or directly if
     R1 factors nicely) to check R1 vanishes identically subject to
     s²+cc²=1 — if the resultant degree is still too large, fall back to
     numerically confirming the resultant is the zero polynomial by
     evaluating it symbolically at several rational points of
     ℚ(t2,s,cc)/(constraint ideal) as a sanity check before finishing the
     exact algebraic proof (numerics only as a guide, not a substitute for
     the final symbolic proof).
  5. Once R1 ≡ 0 subject to the constraint ideal is established, translate
     back through the σ-symmetry to close the whole target identity.
Key lemmas (claim + mechanism):
  - σ-symmetry halves the elimination — because σ is a genuine automorphism
    of the hypothesis system (certified lemma) mapping the t1-side
    computation isomorphically onto the t2-side, so one resultant
    computation suffices for both.
  - Sylvester resultant elimination — because Res_{t1}(f,g) = 0 iff f,g share
    a common root in t1 (standard elimination theory), which is a more
    targeted, often lower-degree tool than a full Gröbner basis over all
    four variables simultaneously, especially with only two polynomials to
    combine at each stage instead of four.
Open gaps: the actual resultant computation (not yet run this round);
  whether it terminates within a reasonable degree/time budget is unknown
  until tried — if it still blows up, that is new negative information for
  next round (evidence the identity's true algebraic degree is high, further
  motivating the Ptolemy/complex-number routes above).
Cases to cover: generic scalene (main target); AB=AC degenerate case (the
  parametrization likely needs a separate limit t1,t2 → special values, or a
  direct symmetric-case argument — not yet handled).
Watch out for: do not silently specialize β or t1,t2 to a single numeric
  solution while "eliminating" — the elimination must produce an identity
  that holds along the entire 1-parameter solution variety, matching the
  family's confirmed one degree of freedom.

coordinate-bash-resultant: copy-of coordinate-bash
Target: identical to coordinate-bash (OM=ON via the same rotation
  parametrization and constraint polynomials).
Technique: an independent second way to fill coordinate-bash's same open
  elimination gap, worth running in parallel rather than sequentially: instead
  of Sylvester resultants eliminating t1 first (coordinate-bash's step 3),
  eliminate t2 first from hyp-2's constraint (the σ-mirror order), OR — a
  genuinely different elimination strategy — substitute a Weierstrass/
  tangent-half-angle rationalization (s=2u/(1+u²), cc=(1−u²)/(1+u²) for
  u=tan(β/2)) to turn the whole system into a pure polynomial system in
  t1,t2,u with no trigonometric identity s²+cc²=1 to track separately, then
  run a single combined Gröbner basis in these three variables only (one
  fewer variable and no algebraic-relation side-constraint, which was likely
  a major contributor to the round-1 blow-up).
Skeleton:
  1–2. Same as coordinate-bash steps 1–2 (reduction, parametrization, note
     σ-symmetry as a cross-check but do not rely on it for this route).
  3. Rationalize via Weierstrass substitution u = tan(β/2), eliminating
     sinβ, cosβ in favor of the single rational parameter u; rewrite hyp-2,
     hyp-3's constraints and the target identity as genuine polynomials in
     t1, t2, u (clearing denominators (1+u²) uniformly).
  4. Run a Gröbner basis (or, if still too large, a resultant chain) in the
     now-3-variable polynomial ring ℚ[t1,t2,u], eliminating t1 and t2 in turn
     to check the target polynomial lies in the ideal generated by the two
     constraint polynomials.
  5. Same closing step as coordinate-bash (translate back, handle AB=AC).
Key lemmas (claim + mechanism): Weierstrass substitution eliminates the
  s²+cc²=1 side relation — because it parametrizes the unit circle
  rationally, so every trig polynomial becomes an honest polynomial in u
  with no extra ideal generator, which can substantially shrink Gröbner
  basis computations compared to the s,cc form.
Open gaps: same as coordinate-bash (the elimination itself, not yet run);
  additionally, u=tan(β/2) has a pole at β=π that must be checked not to
  occur in the valid configuration range (containment hypotheses likely
  bound β away from π, but this should be verified, not assumed).
Cases to cover: same as coordinate-bash.
Watch out for: the two coordinate-bash variants (resultant-first-in-t1 vs
  Weierstrass-then-Gröbner) are genuinely different computational paths on
  the identical target — if BOTH stall, that's strong evidence for pivoting
  fully to the Ptolemy or complex-cross-ratio approaches next round rather
  than a third coordinate variant.
