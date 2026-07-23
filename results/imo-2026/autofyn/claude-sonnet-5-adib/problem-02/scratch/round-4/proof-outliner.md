## imo-2026-02

coordinate-trig-bash: revise
Target: OM = ON (the full problem statement), via the certified reduction
OM=ON ⟺ O_x=p/2 in the frame B=(-1,0), C=(1,0), A=(p,q)
(`lemmas/coordinate-om-on-reduction.md`).
Technique: existence/uniqueness (already certified, IVT + monotonicity) of
the geometric parameters (r1(θ),r2(θ)) combined with a NEW unconditional
polynomial (Bézout-style) identity — found this round by
math-explorer-substitution.md via sympy polynomial division and independently
cross-checked via Gröbner-basis reduction — showing the scalar target O_x=p/2
follows from the quadratics of trig-ceva-chase's Lemma T1 for EITHER root of
EITHER quadratic, i.e. without ever resolving the branch-selection ambiguity
that has stalled the field for 3 rounds. This is the single highest-priority
build item this round: it is a candidate full closure of the shared wall.
Skeleton:
  1. Import setup unchanged: for θ∈(0,min(β,γ)), K=B+r1·(cos(φ_B−θ),sin(φ_B−θ)),
     L=C+r2·(cos(φ_C+θ),sin(φ_C+θ)) — cite `lemmas/existence-uniqueness-r1-r2.md`
     setup.
  2. Existence/uniqueness (already certified, Theorem in
     `lemmas/existence-uniqueness-r1-r2.md`): there is a unique
     (r1(θ),r2(θ)) with F1(θ,r2)=∠LBK−∠LNC=0 and F2(θ,r1)=∠LCK−∠BMK=0, for
     every θ in the domain. Nothing to reprove here — import as-is.
  3. NEW STEP A (the "only if" direction of Lemma T1, currently unstated as
     a standalone step though immediate from Lemma T1's own proof — write it
     out explicitly): exact angle equality is a special case of angle
     equality mod π, so F1(θ,r2)=0 ⟹ Q1(R2)=0 and F2(θ,r1)=0 ⟹ Q2(R1)=0,
     where R1:=r1·|BA|, R2:=r2·|CA| are the rescaled radii and Q1,Q2 are
     Lemma T1's degree-≤2 polynomials applied to the hinges
     (B,d1(θ)),(N,C−N) [for Q1] and (M,B−M),(C,d2(θ)) [for Q2] — cite
     `lemmas/angle-matching-ray-quadratic.md` (Lemma T1) for the mechanism
     (Q(r)=|w1||w2||P(r)−V1||P(r)−V2|sin(φ1(r)−φ2(r))=0 ⟺ φ1≡φ2 mod π).
     This step needs the hinge vectors nonvanishing along the relevant
     domain — this nonvanishing is already established by the nondegeneracy
     arguments inside Lemma 12/12′ of `lemmas/existence-uniqueness-r1-r2.md`
     (e.g. K(r1)≠M, L(r2)≠N); the builder must explicitly re-cite (not
     re-derive) those specific sub-facts here rather than assume them.
  4. NEW STEP B (this round's core finding, math-explorer-substitution.md):
     the polynomial identity
     ```
     T(R1,R2,cosθ,sinθ,p,q) := 2[Nx − (p/2)D] = quo1(R1,R2,c,s,p,q)·Q2(R1)
                                                 + quo2(R1,R2,c,s,p,q)·Q1(R2)
     ```
     holds identically (Nx, D the numerator/denominator of the standard
     circumcenter-x formula for triangle A,K,L), with cosθ,sinθ kept as free
     symbols (no dependence on the Pythagorean identity). The builder must
     (a) reproduce this computation independently in a CAS (not copy-paste
     trust) — build Q1,Q2 directly from Lemma T1's general formula applied
     to the stated hinges (do NOT reuse trig-ceva-chase's own displayed
     r1,r2-based coefficients verbatim — math-explorer-substitution.md
     flagged a units mismatch, R vs r, between its self-built Q1,Q2 and
     trig-ceva-chase's displayed table; rebuilding from Lemma T1's general
     statement directly sidesteps this), (b) present quo1,quo2 explicitly as
     a checkable certificate (a polynomial identity is verified by expanding
     both sides and comparing coefficients, or evaluating at
     deg+1 sample points in each variable — standard, hand-checkable even
     though quo1,quo2 are moderate-size), (c) confirm the identity is
     nonvacuous (T is far from 0 at generic non-root (R1,R2), only vanishes
     modulo the ideal (Q1,Q2)).
  5. Conclude: since (R1,R2)=(r1(θ)|BA|, r2(θ)|CA|) is (by step 3) a root of
     Q2 and Q1 respectively for the unique existence/uniqueness solution
     (step 2), step 4's identity gives T=0, i.e. O_x(θ)=p/2 (once D≠0, see
     nondegeneracy below) for every θ∈(0,min(β,γ)). Combined with
     `lemmas/coordinate-om-on-reduction.md` this proves OM=ON.
  6. Nondegeneracy D≠0 (A,K,L not collinear): must be established — not yet
     addressed by any approach. Candidate argument: if A,K,L were collinear,
     Γ=circumcircle(AKL) is undefined/degenerate, but K is a fixed interior
     point of triangle BMC and L of triangle BNC, both strictly inside
     (hence off line at infinity through A in the generic sweep); a clean
     argument is to show the line AK meets triangle BNC's interior region
     only at isolated θ (or show K,L,A collinear forces a specific θ value
     excluded by the open domain) — this is an open sub-gap the builder must
     close, not gloss over.
Key lemmas (claim + mechanism):
  - Lemma T1 "only-if" direction (Step 3) — because exact angle equality is
    literally a special case of "equal mod π", already covered by Lemma T1's
    proved trig identity; the harder "which root is geometric" direction is
    NOT needed anywhere in this route (this is the key insight that unblocks
    the field: the branch-selection open caveat in
    `lemmas/angle-matching-ray-quadratic.md` becomes irrelevant).
  - Bézout/cofactor identity T=quo1·Q2+quo2·Q1 (Step 4) — because a symbolic
    polynomial-division remainder computed exactly (rationals, no floating
    point) vanishing identically is precisely a certificate that T lies in
    the ideal (Q1,Q2), so it vanishes on their common zero locus regardless
    of which root is selected — this is what makes the argument
    branch-independent.
Open gaps: (a) independent from-scratch reproduction of quo1,quo2 as an
  explicit, hand-checkable certificate (not just "sympy said so" — must be
  presented so the reviewer can re-verify by direct expansion or evaluation);
  (b) the D≠0 nondegeneracy argument (step 6), currently unaddressed by any
  approach; (c) double-check the R1/R2 unit convention self-consistently
  (rebuild Q1,Q2 from Lemma T1's abstract statement, not trig-ceva-chase's
  displayed table, per math-explorer-substitution.md's own flagged caveat).
Cases to cover: none additional — the identity is branch/case-independent by
  construction (that is the whole point of this route), aside from the D≠0
  nondegeneracy check which is a single global fact, not casework.
Watch out for: do not silently trust the sympy computation as "certified" —
  the reviewer must independently re-run the polynomial division/Gröbner
  check (per run_state.md's standing rule on independently re-deriving
  builder claims) and inspect the explicit quo1,quo2 polynomials, not just
  the "remainder=0" boolean. Also watch that Step 3's "F=0 ⟹ Q=0" direction
  really needs zero hidden hypotheses beyond the already-certified
  nonvanishing facts — do not introduce a new unproven nonvanishing
  assumption while writing this up.

antipode-perp-bisector: revise
Target: OM = ON, via the certified reduction OM=ON ⟺ A*B=A*C
(`lemmas/antipode-reduction.md`, A*:=2O−A, perpendicular-intersection point).
Technique: unsigned-angle trichotomy (new this round, from
math-explorer-antipode.md) replacing the directed-angle sign bookkeeping that
round 3's reviewer caught as erroneous — plus a new isogonal-conjugate
reformulation of the key sub-claim.
Skeleton:
  1. Import unchanged: A*B=A*C target (`lemmas/antipode-reduction.md`), plus
     the certified right angles ∠AKA*=∠ALA*=90° (Thales).
  2. Classical fact (2-line proof, cite knowledge_base.md circumcenter/
     isosceles entry): with O'=circumcenter(ABC), triangle O'AB is isosceles
     (O'A=O'B=circumradius), so ∠O'BA=90°−γ; symmetrically ∠O'CA=90°−β.
  3. NEW unsigned lemma L1' (replaces round-3's unsigned-but-unabsolute-valued
     L1, and its buggy directed-angle derivation): ∠ABA* = |θ+90°−γ|, with
     the configuration governed by a checkable trichotomy on sign(θ+90°−γ):
     if θ+90°−γ>0 (i.e. γ<90°+θ), K lies angularly between rays BA,BA*
     (additive: ∠ABK+∠KBA*=∠ABA*); if θ+90°−γ<0, A* lies angularly between
     BA,BK (∠ABA*+∠A*BK=∠ABK); if =0, degenerate case handled by continuity
     (round-3's existing continuity machinery, still valid). Symmetric L2'
     at C: ∠ACA*=|θ+90°−β|, trichotomy on sign(θ+90°−β).
  4. Isogonal reformulation (new lead, from math-explorer-antipode.md, worth
     attempting as the mechanism to actually PROVE L1'/L2' rather than just
     restate them): combine with the also-numerically-found
     ∠O'BA*=θ (round-3 file) to get ∠ABK=∠A*BO'=θ and ∠ABO'=∠KBA*=90°−γ,
     i.e. rays BK,BO' are isogonal conjugates in angle ∠ABA*. If this
     isogonality can be derived directly from hypotheses H1∧H2∧H3 (not yet
     found — flagged as the key remaining mechanism to search for), L1'/L2'
     follow immediately.
  5. Combine the (now up to 4, cleanly case-split) sign combinations of
     step 3's trichotomies at B and C with the isosceles-triangle-converse +
     Law of Sines argument from round 3 (sound machinery, just needs correct
     unsigned inputs) to conclude A*B=A*C in every case.
Key lemmas (claim + mechanism):
  - ∠O'BA=90°−γ — because triangle O'AB is isosceles with O'A=O'B=R (both
    circumradii of ABC), so its base angles are equal and sum with ∠AO'B=2γ
    (central angle) to 180°.
  - L1'/L2' unsigned identities — mechanism NOT yet found (this is the
    honest open gap); the isogonal-conjugate reformulation (step 4) is the
    best current lead, replacing the previously abandoned "full spiral
    similarity at B" (refuted, ratio fails) with an angle-only claim that
    does not require a ratio match.
Open gaps: L1'/L2' themselves (still numerical-only, no synthetic proof, per
  math-explorer-antipode.md's own honest labeling); the isogonality
  mechanism in step 4 is unproven from H1∧H2∧H3.
Cases to cover: sign(θ+90°−γ) ∈ {>0,<0,=0} at B, independently sign(θ+90°−β)
  at C — 2×2 generic combinations plus the boundary/degenerate sub-cases,
  all must be enumerated explicitly by the builder (do not silently assume
  the "generic" case covers everything).
Watch out for: do NOT repeat round 3's error of asserting "by symmetry, same
  sign convention" at C without checking it explicitly — math-explorer-
  antipode.md's trichotomy is exactly the fix, but the builder must still
  verify the C-side case split independently rather than mirror B's by fiat.
  Do not re-attempt the refuted "full spiral similarity at B" mechanism
  (angle matches, ratio BK/BO'≠BA*/BA fails, confirmed again this round).

inversive-swap-line: new
Target: OM = ON, via the certified reduction OM=ON ⟺ A*B=A*C
(`lemmas/antipode-reduction.md`), reached by reconstructing O's direction and
distance from A using an A-centered inversive similarity — a structurally
different top-level route from both the coordinate-substitution family and
the antipode-perp-bisector family (never computes O as an intersection of
two perpendicular bisectors, nor as an explicit (x,y) coordinate pair).
Technique: inversion + reflection (classical "swap B,C" inversive similarity),
from math-explorer-newframing.md's Opening 1.
Skeleton:
  1. Define σ:=ρ∘ι: ι = inversion centered at A with power k:=AB·AC, ρ =
     reflection across the internal bisector of ∠BAC. Prove σ(B)=C, σ(C)=B
     (standard inversive-similarity fact; cite knowledge_base.md's inversion
     entry, or prove directly via ι(B) on ray AB at distance k/AB=AC from A,
     then ρ swaps ray AB↔AC).
  2. Classical fact: since A∈Γ (Γ=circumcircle(AKL), radius R=AO), ι(Γ\{A})
     is the line ℓ perpendicular to AO at distance k/(2R) from A (cite the
     standard inversive-distance formula |P*Q*|=k|PQ|/(AP·AQ) applied to a
     circle through the inversion center — this is a hypothesis-free,
     general classical fact, already verified numerically to 1e-14 by the
     explorer). Hence σ(Γ\{A})=ρ(ℓ)=:ℓ_Γ is a line perpendicular to ρ(AO), at
     the same distance k/(2R) from A, passing through σ(K),σ(L).
  3. CHEAP-KILL CHECK (do this FIRST, before any further development, per
     math-explorer-newframing.md's own recommendation): compute
     ∠σ(K)Aσ(L). Since ρ is an isometry fixing A, it preserves the
     magnitude of the angle between any two rays from A, so
     ∠σ(K)Aσ(L)=∠KAL exactly. Check whether ∠KAL is directly expressible
     from the three angle hypotheses (e.g. via the inscribed-angle relation
     in Γ, or directly from known sub-angles at K,L) WITHOUT reconstructing
     the full (r1,r2) parametrization. If yes — proceed to steps 4-5. If
     this check instead requires the full (r1,r2) data, STOP and report this
     as a same-wall collapse (like trig-ceva-chase's confirmed non-bypass),
     do not force further development.
  4. If step 3 succeeds: with |Aσ(K)|=k/AK, |Aσ(L)|=k/AL and ∠σ(K)Aσ(L)=∠KAL
     known, triangle Aσ(K)σ(L) is fully determined, pinning the direction of
     ℓ_Γ (hence of ρ(AO), hence of AO after applying ρ again) and its
     distance from A.
  5. Combine direction+distance of AO from A with R=AO's magnitude (Law of
     Sines in triangle AKL: 2R=AK/sin∠ALK) to get O explicitly, then A*=2O−A,
     then check A*B=A*C (or directly check O_x=p/2 in the shared frame).
Key lemmas (claim + mechanism):
  - σ(B)=C — because ι sends B to the point on ray AB at distance
    k/AB=AC from A, and ρ maps ray AB to ray AC (bisector reflection), landing
    exactly on C.
  - Γ∋A ⟹ ι(Γ) is a line — because the inversive-distance formula shows any
    two image points P*,Q* satisfy |P*Q*|=k|PQ|/(AP·AQ), and a circle
    through the center of inversion has all its (non-center) points inverting
    to a common line (standard fact, provable directly from this formula plus
    one more image point fixing the line).
Open gaps: the cheap-kill check (step 3) is unresolved — this is genuinely
  reconnaissance-stage, not yet a partial proof. If step 3 fails, this
  approach should be reported as a confirmed non-bypass and deprioritized,
  same as trig-ceva-chase's own final step was in round 3.
Cases to cover: none identified yet (approach not developed far enough to
  need casework).
Watch out for: this is explicitly a lower-priority, higher-risk approach this
  round (kept alive for diversity per CLAUDE.md's anti-single-framing rule,
  not because it is close to closing) — do not let it consume the majority
  of builder time; the coordinate-trig-bash revision above is the
  higher-confidence, closer-to-closing route this round. Do not conflate this
  with `complex-circle-power` (dormant) — math-explorer-newframing.md
  explicitly judged that approach likely to collapse to the same wall and
  recommended NOT prioritizing it; this inversive-swap approach is different
  (a line construction via a center-of-inversion circle, not a unit-circle
  parametrization) and should not be merged with it.

labeling-duality: (no action — remains dormant)
Confirmed (round 2, unchanged) algebraically equivalent to
coordinate-trig-bash's O_x=p/2 target via `lemmas/radical-axis-form-of-TI.md`.
If coordinate-trig-bash's revision above closes this round, labeling-duality
closes automatically with it — do not spend a build slot on it this round.

trig-ceva-chase: (no action — lemma provider only, not re-built)
Its certified Lemma T1 (`lemmas/angle-matching-ray-quadratic.md`) is the
direct input to coordinate-trig-bash's revision above; no further
development of trig-ceva-chase itself is needed this round. Its own round-3
finding that its final step "is not a bypass" is now understood correctly:
it wasn't a bypass on its OWN terms (needing the branch-selection to be
resolved), but combined with coordinate-trig-bash's existence/uniqueness
theorem AND this round's new branch-independent identity, the same
machinery closes the wall via a different combination — flag this
explicitly to avoid confusion in the ranking.
