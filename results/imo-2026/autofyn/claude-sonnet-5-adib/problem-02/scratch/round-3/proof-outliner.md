## imo-2026-02

antipode-perp-bisector: revise
Target: OM = ON (full problem), via the certified reduction OM=ON ⟺ A*B=A*C
(A* = 2O−A, antipode of A on Γ=circumcircle(AKL)), now further reduced to two
explicit angle formulas.
Technique: Antipode construction (Thales/inscribed-angle-in-semicircle,
already certified in `lemmas/antipode-reduction.md`) + a NEW closing
mechanism: two angle formulas for A* as seen from B and C, closed by an
elementary base-angle isosceles-triangle chase. This is a genuinely different
closing mechanism from all four previously-refuted step-5 attempts (270°
right-triangle identity, spiral-similarity center, tangency/secant, and this
round's newly-refuted A*=circumcenter(ABC) / A*BK~A*CL similarity /
four concyclicity guesses).
Skeleton:
  1. (Certified, import from `lemmas/antipode-reduction.md`) OM=ON ⟺ A*B=A*C,
     and A* = (perp to AK at K) ∩ (perp to AL at L).
  2. NEW Lemma L1: ∠ABA* = θ + 90° − γ, where θ=∠KBA=∠ACL (hypothesis 1),
     γ=∠ACB. Measured from ray BA to ray BA*.
  3. NEW Lemma L2 (symmetric): ∠ACA* = θ + 90° − β, β=∠ABC. Measured from ray
     CA to ray CA*.
  4. Elementary angle chase (no new machinery): ∠A*BC = β − ∠ABA* =
     90° − α − θ, and symmetrically ∠A*CB = γ − ∠ACA* = 90° − α − θ (using
     β+γ = 180°−α). Hence ∠A*BC = ∠A*CB identically, so triangle A*BC is
     isosceles, giving A*B = A*C — by the Isosceles Triangle Converse
     (equal base angles ⇒ equal sides, knowledge_base.md's triangle-congruence
     toolkit).
  5. Combine with step 1 to conclude OM = ON.
Key lemmas (claim + mechanism):
  - L1: ∠ABA* = θ + 90°−γ — mechanism (conjectured route, must be verified,
    not assumed): since ∠AKA*=90° (certified), triangle ABK has known angle
    θ at B; the direction of BA* should follow from chaining ∠AKA*=90° at K
    together with hypothesis H3 (∠LCK=∠BMK, which per the certified
    Decoupling Lemma pins r1=BK as a function of θ alone) through triangle
    ABK's own angle sum plus the right angle at K. This is the mechanism to
    attempt FIRST (H3 ↔ L1, since both live "at the B/K side"); if it does
    not close, try law of sines in triangle ABA* directly (Extended Law of
    Sines, knowledge_base.md) using AB, ∠ABK=θ, and AK as intermediate
    quantities.
  - L2: symmetric mechanism via H2 (∠LBK=∠LNC, pins r2=CL as function of θ)
    and ∠ALA*=90° at L, chained through triangle ACL.
  - Base-angle chase (step 4): elementary, fully rigorous once L1/L2 are
    established — no further gap.
Open gaps: L1 and L2 themselves — currently only numerically verified
(3 triangle shapes, several θ each, to ~1e-6) by this round's explorer, NOT
derived synthetically from H1–H3. The builder must either (a) prove them
from scratch using the H3↔L1 / H2↔L2 pairing conjectured above, or (b) find
they are false as stated and report the refutation with a counterexample
(do not silently assume them true because they are numerically strong).
Cases to cover: the sign/branch of 90°−α−θ (whether A* is on the same side
of BC as A) — the explorer flagged this correlates with the
containment/orientation hypotheses but did not verify the correlation in
detail; the builder must check the target A*B=A*C holds regardless of this
sign (it's a squared/unsigned distance equality, so the isosceles argument
should survive taking absolute values, but state this explicitly rather than
gloss over it).
Watch out for: do not repeat the four already-refuted mechanisms (270°
right-triangle sum, spiral-similarity center for L, tangency/secant
identification, A*=circumcenter(ABC) or A*BK~A*CL similarity, or the four
concyclicity guesses) — all confirmed dead this round or earlier. L1/L2 must
be derived from the FULL hypothesis system (H1∧H2∧H3∧containment); the
explorer already checked L1 fails if r1,r2 are perturbed off their
hypothesis-satisfying values with θ fixed, so any derivation must genuinely
use H2/H3, not just H1.

coordinate-trig-bash: revise
Target: OM = ON (full problem), via the certified reduction OM=ON ⟺ O_x=p/2
in frame B=(−1,0), C=(1,0), A=(p,q), pursued via IVT existence + uniqueness
of the hypothesis-satisfying (r1(θ),r2(θ)) family, then the final
substitution.
Technique: Analytic/coordinate bash with monotonicity (Sweep Lemma) + IVT,
now REPAIRED to use the correct (smaller) domain of validity rather than the
false global domain from round 2.
Skeleton:
  1. (Certified) Decoupling Lemma, Sweep Lemma, ray parametrization Lemma 3 —
     import from `lemmas/decoupling-and-sweep-lemma.md` unchanged.
  2. **Domain correction (this round's core fix).** Define
     r2_signflip(θ) := the r2 at which ray BL (as seen from B) crosses the
     fixed polar angle φ_B−θ (direction of ray BK) — i.e. where L reaches
     line BK. Prove the TRUE valid r2-domain (where the hypothesis "K lies
     inside angle LBA" actually holds, not just "L inside triangle BNC") is
     `(0, r2*(θ))` with `r2*(θ) := min(r2max(θ), r2_signflip(θ))`, NOT the
     previously-claimed `(0, r2max(θ))`.
  3. Re-prove Lemma 6 (F1 strictly decreasing) on the corrected domain
     `(0, r2*(θ))`: the "sign convention" step (ψ_B(r2) < φ_B−θ) now holds
     BY CONSTRUCTION on this domain (it's the defining property of
     r2_signflip, not an assumption) — so the existing monotonicity
     computation goes through verbatim once restricted here.
  4. Existence via IVT on the corrected domain, via a two-case split at the
     right endpoint r2*(θ):
     - Case (a) r2_signflip ≤ r2max: at r2→r2*(θ)⁻, ∠LBK→0⁺ (ray BL aligned
       with fixed ray BK), so F1 → −∠LNC(r2*(θ)), negative provided
       ∠LNC(r2*(θ)) > 0 (need: L,N,C not collinear there — prove this is not
       a degenerate case, or show it can't happen given θ∈(0,min(β,γ))).
     - Case (b) r2max < r2_signflip: this is the original argument's regime;
       endpoint gives F1 → |θ−δ|−(∠A+δ), needing the much weaker per-θ
       inequality `θ < ∠A+2δ` (NOT the false global (★) `min(β,γ)<∠A+2δ`) —
       prove this per-θ inequality directly, or show case (b) never actually
       arises for θ close enough to min(β,γ) to threaten it.
     Combined with the r2→0⁺ endpoint (F1→φ_B−θ>0, already certified),
     conclude existence of a root r2(θ) by IVT in both cases.
  5. Symmetric F2/r1 analysis (mirror of steps 2–4 via B↔C,K↔L,M↔N,δ↔δ').
  6. Uniqueness of (r1(θ),r2(θ)) from strict monotonicity (steps 3,5).
  7. Final substitution: show O_x(θ) = p/2 along the resulting curve — still
     entirely open, largest remaining gap in this approach.
Key lemmas (claim + mechanism):
  - r2_signflip(θ) is well-defined and the TRUE domain is
    (0, min(r2max,r2_signflip)) — because "K inside angle LBA" is exactly
    the condition ψ_B(r2) < φ_B−θ (ray BL between ray BA and ray BK, in the
    correct rotational sense), which is precisely what fails past
    r2_signflip; past that point the configuration violates the problem's
    own hypothesis and is out of scope, not a gap.
  - Case (a) endpoint sign: ∠LNC(r2_signflip(θ)) > 0 — because L,N,C
    collinear would force L on line NC, a codimension-1 degeneracy that
    should be excluded or shown impossible given L strictly inside triangle
    BNC at that boundary value.
  - Case (b) weaker inequality `θ < ∠A+2δ`: a genuine per-θ trigonometric
    fact, narrower than the refuted global (★) — must still be proved, not
    assumed from the 2300-trial numeric check.
Open gaps: (i) formalize r2_signflip(θ) synthetically/algebraically and
prove the domain-correction claim rigorously (not just numerically over
2300 trials); (ii) prove the case (a) endpoint sign and case (b) weaker
inequality, or find a case-split-free unified argument; (iii) carry out the
symmetric F2 analysis; (iv) the final substitution O_x(θ)=p/2 — untouched,
likely the hardest remaining step even after existence+uniqueness close.
Cases to cover: case (a) vs case (b) at the r2 endpoint (and the symmetric
r1 endpoint) — both must be handled, not just the numerically-common one.
Watch out for: do NOT reuse Lemma 6/7 "as literally stated" on the full
(0,r2max(θ)) domain (confirmed false, counterexample (p,q)=(0.0025,5.0),
θ≈60.57°) — every claim must be restated on the corrected domain. Do NOT
reuse the global inequality (★) min(β,γ)<∠A+2δ (confirmed false, same
counterexample and also (p,q)=(0.9096,4.7429), θ→0.995·min(β,γ)) — only the
weaker per-θ case-(b) inequality `θ<∠A+2δ` is claimed, and even that remains
unproven. Require the builder to independently re-verify any "checked over N
trials" claim before trusting it (per run_state.md rule from round 2 — a
prior monotonicity/inequality claim was falsified this way already).

labeling-duality: advance (deprioritized this round — explicit decision)
Target: OM = ON, via the certified power-of-a-point reduction
pow_Γ(B)−pow_Γ(C) = (AB²−AC²)/2, equivalently the radical-axis form (TI″).
Technique: Power of a point / radical axis (unchanged from rounds 1–2).
Skeleton: unchanged from `approaches/labeling-duality.md` — import
`lemmas/median-length-power-reduction.md` and
`lemmas/radical-axis-form-of-TI.md`.
Key lemmas: none new this round.
Open gaps: same underlying gap as coordinate-trig-bash (confirmed
algebraically equivalent, both reduce to `-2O_x=-p`, per
`lemmas/radical-axis-form-of-TI.md`).
Cases to cover: none new.
Watch out for: **explicit decision, per dispatch instruction** — do NOT
spend a separate build slot re-deriving the same scalar target this round;
this approach's gap is a certified reformulation of coordinate-trig-bash's
gap, so any progress coordinate-trig-bash makes on the domain-correction /
final-substitution steps transfers automatically. Recommend the
outline-reviewer NOT put labeling-duality in this round's build set (mark it
explicitly "advance, dormant" rather than silently ignoring it) — revisit
only if coordinate-trig-bash's revised route stalls again, or if a
labeling-duality-specific lever (e.g. a fresh secant-identification idea) is
proposed that is NOT just a restatement of O_x=p/2.

trig-ceva-chase: new
Target: OM = ON (full problem, proved via a pure trigonometric identity in
θ, A, B, C — no coordinate frame, no complex numbers, working directly with
angles and the Extended Law of Sines in the sub-triangles determined by the
hypotheses).
Technique: Trigonometric Ceva / Extended Law of Sines chase (knowledge_base
"Synthetic toolkit" — trig cevians), a genuinely different computational
medium from all three live approaches, which all eventually fix a Cartesian
frame (B,C on an axis), an origin-at-O complex frame, or a power/radical-axis
abstraction. Explicitly ruled out as a bypass: literal spiral similarity
BKL~NLC or {C,K,M,X} concyclicity (dead, `two-step-spiral-chain`), and
reflection across perp-bisector(MN) swapping B↔C (dead, this round's
newframing explorer, ℓ is NOT the perp bisector of BC).
Skeleton:
  1. Parametrize by θ := ∠KBA = ∠ACL ∈ (0, min(β,γ)) exactly as
     coordinate-trig-bash's Lemma 3, but work with lengths/angles only: in
     triangle ABK, by Law of Sines, AK/sin(θ) = AB/sin(∠AKB), so
     AK = AB·sinθ/sin(∠AKB) — express ∠AKB in terms of θ and the still-free
     r1=BK via the triangle's own angle sum (∠AKB = 180°−θ−∠BAK), i.e. treat
     AK, BK as functions of θ and one free ratio, not Cartesian coordinates.
  2. Do the symmetric expansion for triangle ACL: AL in terms of θ, γ, r2=CL.
  3. Use hypothesis H3 (∠LCK=∠BMK) in triangle BMK (∠BMK is known once K is
     placed — M is the midpoint of AB, so BM=AB/2 is known) via Law of Sines
     in BMK to get a trig equation pinning r1=BK as an explicit function of
     θ alone (this is exactly the content the Decoupling Lemma already
     isolates — reuse `lemmas/decoupling-and-sweep-lemma.md` for the
     decoupling structure, but redo the actual r1(θ) solve as a closed-form
     trig expression rather than leaving it as an implicit root of F2=0).
  4. Symmetrically pin r2=CL as an explicit function of θ via H2 and
     triangle CNL / Law of Sines.
  5. Compute the circumradius R and circumcenter O of triangle AKL using the
     Extended Law of Sines (R = AK/(2 sin∠ALK), or via the standard
     circumcenter-as-intersection-of-perpendicular-bisectors formula
     expressed in trig form) purely in terms of θ, A, B, C — no coordinates.
  6. Express OM, ON via the median-length formula (Apollonius, already
     certified in `lemmas/median-length-power-reduction.md`) applied in
     trig form, and show OM²−ON² ≡ 0 as a trig identity in θ, A, B, C (using
     sum-to-product / product-to-sum identities rather than Gröbner bases).
Key lemmas (claim + mechanism):
  - r1(θ), r2(θ) admit closed trig forms — because H2/H3 each reduce, via
    Law of Sines in exactly one sub-triangle (BMK for r1, CNL for r2), to a
    single scalar trig equation in one unknown (the Decoupling Lemma already
    proves this reduction is possible in principle; this approach's new
    content is solving it in closed trig form instead of leaving it as an
    implicit IVT root).
  - OM²−ON² identity reduces to a trig identity in θ,A,B,C — because both
    OM and ON are expressed via Apollonius' median-length formula applied to
    triangle AKL with AK, AL, KL all now explicit trig functions of θ,A,B,C.
Open gaps: step 3/4's closed-form solve for r1(θ), r2(θ) (may not have a
literal closed form — if the trig equation is itself transcendental, this
approach reduces to the same obstruction as coordinate-trig-bash, just in
trig dress; the builder must check this early and report if it's a
relabeling rather than a genuine bypass); step 6's final trig identity is
the whole remaining content and is unproven.
Cases to cover: none new beyond the standard θ∈(0,min(β,γ)) range and acute
vs obtuse ABC (may affect sign conventions in the Law of Sines steps).
Watch out for: this approach's Step 3/4 risks silently reducing to exactly
the same transcendental system coordinate-trig-bash already has (the
Decoupling Lemma shows F1=0, F2=0 are each one equation in one unknown given
θ — trig dress does not automatically make them closed-form solvable). The
builder must flag explicitly, early, whether r1(θ) is expressible in closed
form or not, rather than assume the "no coordinate frame" framing
automatically avoids the transcendental-solve wall. If it does reduce to the
same wall, this approach's value is then purely as a cross-check / cleaner
route to the final identity in step 6, not a genuine bypass — report this
finding either way rather than silently abandoning without a note.
