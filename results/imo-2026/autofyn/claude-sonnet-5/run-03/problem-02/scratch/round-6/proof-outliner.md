## imo-2026-02

coordinate-bash-resultant-boundary: advance
Target: For every real scalene triangle ABC, K,L (defined by the problem's three
hypothesis angle equalities + the two containment/interior conditions) satisfy
OM=ON where O=circumcenter(A,K,L), M,N are midpoints of AB,AC — i.e. the whole
original olympiad claim, via the coordinate/rotation-parametrization route.
Technique: Resultant/Vieta branch-selection (Theorem 11.8's cross-product-sign
recipe), now extended to two more sub-lemmas of the *same* species, plus a
reframing that removes the need for the still-unresolved F3/F3' continuity
argument.
Skeleton (unchanged core, §1-§6 imported/certified; new work is §11-continuation):
  1. Reduction to O·(C−B)=(|C|²−|B|²)/4 — certified (`lemmas/vector-reduction-OM-ON.md`).
  2. Rotation parametrization of K (angle β, magnitude t1) and L (magnitude s2)
     — certified (`lemmas/homogeneity-decoupling-rotation-param.md`).
  3. Symbolic genericity certificate: target ∈ ⟨G2a,G3a⟩ for every triangle —
     certified (`lemmas/symbolic-genericity-certificate.md`).
  4. Branch selection on the K/L-direction level (which quadratic root of
     G2a is genuine, given L∈△BNC): Theorem 11.8 — certified
     (`lemmas/cross-product-sign-selection-G2a.md`).
  5. NEW sub-lemma (magnitude bound): show the selected G3a-root t1(β) puts
     the actual point K=B+t1·d(β) on the correct (B-)side of edge MC, i.e.
     inside the finite triangle BMC, not just the correct angular sector —
     by the identical resultant/Vieta recipe applied to N1(t1):=cross(C−M,K−M)
     (affine-linear in t1, exactly Lemma 11.5's shape) against G3a(t1).
  6. NEW sub-lemma (G2b exclusion): show that no root of G2b=0 that is a
     *genuine* (non-supplementary) solution of the unsquared hypothesis-2
     equation ∠LBK=∠LNC can simultaneously satisfy full containment L∈△BNC
     AND the sign test cross(BK,BL)<0 — proved via the σ-mirror of steps 4–5's
     machinery: distinguish true vs. supplementary roots of G2b by the
     auxiliary sign condition sign(dot(BL,BK))=sign(dot(NL,NC)) (to be derived
     algebraically, not just numerically filtered), then run the same
     resultant/Vieta argument against both the containment test and Lemma
     11.1's cross-product angle test on this restricted root set.
  7. Combine steps 4–6 (plus their σ-mirrors for hypothesis 3 / L / G3a,G3b)
     pointwise, at each fixed β: exactly one of the 4 candidate roots
     (2 from G2a, 2 from G2b) survives every hypothesis + containment
     condition simultaneously — this is the "fresh pointwise-exclusion"
     reframing (see below), which makes the still-open F3/F3'-crossing
     question (item 9 below) IRRELEVANT rather than requiring it be resolved:
     no continuity/IVT argument along β is needed at all if the selection is
     proved independently at each β.
  8. Conclude target identity holds on the unique genuine root ⟹ OM=ON.
Key lemmas (claim + mechanism):
  - Magnitude bound: cross(C−M,K−M)=P'(u)+t1·Q'(u) is affine in t1 (same
    algebraic shape as Lemma 11.5's L1(s2)), so Res_{t1}(G3a, N1) factors
    into known pieces by the identical machinery that produced Theorem 11.8;
    a sign case-split (mirroring Lemma 11.7's b≥0/b<0 split) on the resulting
    explicit factor should pin the sign of N1 at the selected root — because
    the same "affine function crossed with a quadratic ⟹ Vieta sign trick"
    mechanism (Lemma 11.6/11.7) is degree/structure-agnostic to which affine
    functional or which quadratic is used, only the concrete coefficients
    change.
  - G2b exclusion (the joint containment+sign criterion): because G2b's
    two roots split into one "true" (∠LBK=∠LNC exactly) and one
    "supplementary" (∠LBK=π−∠LNC) root generically — a fact forced by the
    squaring step doubling the root set — and the true root, when isolated
    algebraically via the dot-product sign condition, is disjoint from the
    joint containment+sign-test region; this mirrors exactly how Theorem
    11.8 isolated G2a's genuine root, just applied to the complementary
    branch and shown to always fail instead of always succeed.
Open gaps: both new sub-lemmas (steps 5, 6) are algebraically well-specified
but unproved — strongly evidenced numerically (magnitude bound: population's
existing multi-triangle sweeps; G2b exclusion: 4500+ stress trials, 0
counterexamples this round). Step 7's "pointwise exclusion supersedes
continuity" reframing needs to be explicitly verified as logically sufficient
(i.e. does it actually retire item 9 below, or does σ-symmetry / hypothesis-3
combination reintroduce a need for range-connectedness after all?) before
being relied on as the closing argument.
Cases to cover: sign(b) case-split for each new resultant sign lemma
(mirroring Lemma 11.7); true-vs-supplementary root case for G2b.
Watch out for: (a) don't conflate the magnitude-bound test (point-vs-edge,
uses M) with the sign test (ray-vs-ray, uses only B) — they are logically
independent per the magnitude explorer's finding, both must be proved; (b) the
σ-mirror for K-side/L-side/hyp-3 must actually be re-derived, not assumed for
free, since the parametrization frame is not σ-invariant (established round 2);
(c) item 9 (F3/F3' crossings) becomes moot ONLY if step 7's pointwise argument
is complete for ALL of steps 4-6's mirrors — a partial pointwise argument
still needs the continuity fallback.

ptolemy-trig-identity: advance
Target: same whole-problem claim, via the independent Ptolemy/trig-angle
parametrization route (no coordinates), reducing to F(θ,A,B,C)>4.
Technique: resultant elimination (already done, certified) reducing F>4 to a
single radical-free sextic Ψ(τ,A,C)>0 on τ=tanθ∈(0,tan(min(B,C))); NOW
reframed (per this round's sextic explorer) from "global positivity" (refuted,
dead) to a root-count + boundary-sign IVT argument on the bounded interval —
structurally the same architecture as the already-certified
`lemmas/ptolemy-trig-branch-selection.md`'s IVT + degree-counting method, one
level down (applied to Ψ itself, not to F).
Skeleton:
  1. Angle parametrization + Ptolemy-equality-to-concyclic reduction —
     certified (`lemmas/general-ptolemy-equality-concyclic.md`,
     `lemmas/ray-angle-determines-cyclic-order.md`).
  2. Branch selection for constraints (III)/(IV) — certified
     (`lemmas/ptolemy-trig-branch-selection.md`).
  3. Resultant elimination F>4 ⟺ Ψ(τ,A,C)>0 on τ∈(0,tan(min(B,C))) —
     certified (`lemmas/ptolemy-resultant-elimination-to-sextic.md`,
     corrected constant this round).
  4. NEW: prove Ψ has no zero in the open interval (0, tan(min(B,C))), via:
     (a) Ψ(0,A,C)=4sin³A sinB sinC>0 — already exact/certified;
     (b) a real-root-count bound on Ψ as a sextic in τ (Descartes' rule of
     signs on the coefficient sign pattern, or a Sturm sequence, parametrized
     by A,C) showing at most one positive real root generically;
     (c) show that root (when it exists) is ≥ tan(min(B,C)) — i.e. outside
     the geometric domain — via a case split on sign(B−C) (since
     min(B,C) is whichever is smaller) and an explicit sign check of Ψ
     evaluated AT τ=tan(min(B,C)) itself (a substitution, not a root-finding
     problem — much more tractable: reduces to signing one explicit
     trig expression in A,B,C at the boundary, using A+B+C=π);
  5. IVT: Ψ(0)>0 and no interior zero (steps a-c) ⟹ Ψ>0 throughout the open
     interval ⟹ F>4 throughout ⟹ target inequality holds ⟹ conclude the
     original olympiad claim (via the population's standing reduction of the
     whole problem to this inequality).
Key lemmas (claim + mechanism):
  - Ψ has ≤1 positive real root (generically): because a degree-6 polynomial
    with a fixed sign pattern of coefficients (as a function of A,C, subject
    to A,C∈(0,π), A+C<π) has a Descartes-bound-limited number of sign changes
    — this round's explorer found numerically exactly 2 real roots total (one
    typically negative), consistent with ≤1 positive root; needs to be
    established via an actual sign-pattern argument on the coefficients, not
    just numerics.
  - Boundary sign at τ=tan(min(B,C)): because this is a SUBSTITUTION (not a
    search over an interval) into the explicit sextic formula, reducing to
    verifying one trig inequality in the two free angles A,C (with B=π−A−C
    implicit) — tractable by the same rational-parametrization (m=tan(A/2),
    n=tan(C/2)) technique the sextic explorer already used to rebuild Ψ from
    scratch this round.
Open gaps: step 4(b) (root-count bound) and 4(c) (boundary-sign case split)
are both unproved — the explorer only confirmed the ≤1-positive-root pattern
numerically (6 samples) and did not attempt the boundary substitution. This is
the newly-corrected framing (previous global-SOS framing is dead, do not
retry).
Cases to cover: sign(B−C) (which of B,C is the binding boundary); possibly a
degenerate sub-case where Ψ has a double root or the two real roots coincide
with τ=0 (A→0 boundary, already known to be where Ψ→0, needs care that this
limiting case doesn't hide a genuine interior zero for A near but not equal 0).
Watch out for: do not re-attempt a global (all-τ or all-τ>0) SOS/positivity
certificate for Ψ — refuted this round with explicit counterexamples (Ψ<0 for
τ beyond tan(min(B,C)) in ~29% of sampled points); any proof MUST use the
domain bound τ<tan(min(B,C)) as an active hypothesis, not just A,B,C>0,
A+B+C=π.

coordinate-bash-resultant-boundary-pointwise: new (copy-of coordinate-bash-resultant-boundary, targeting the SAME gap cluster via a distinct top-level closing strategy)
Target: same whole-problem claim as the sibling, same underlying algebra
(G2a/G2b/G3a/G3b, Theorem 11.8), but a DIFFERENT closing architecture: instead
of continuity/IVT-along-β (which needs F3/F3'-crossing-harmlessness, item 9,
still open and stuck since round 4), prove branch selection is correct
POINTWISE at every fixed β independently, making the crossing question moot.
Technique: exhaustive 4-candidate-root pointwise exclusion (this round's
magnitude explorer's "genuinely fresh idea"), reusing all of the sibling's
certified sub-results (Theorem 11.8, the new magnitude-bound and G2b-exclusion
sub-lemmas once proved) but assembling them into a pointwise, not continuity-
based, argument.
Skeleton:
  1-3. Import steps 1-3 of the sibling verbatim (reduction, parametrization,
     genericity certificate).
  4. For each fixed β in the valid range, enumerate the (at most) 4 real
     candidate roots for K's magnitude t1: 2 from G2a=0, 2 from G2b=0 (and
     symmetrically 4 for L's s2, from G3a, G3b).
  5. Prove, independently at each β (no reference to neighboring β, no IVT):
     exactly one of the 4 t1-candidates and one of the 4 s2-candidates
     jointly satisfy ALL of: (i) K,L on the correct angular side (Lemma 11.1
     direction test), (ii) the magnitude bound (K inside finite triangle BMC,
     L inside finite triangle CNB — new sub-lemma from the sibling), (iii)
     the cross-product sign test cross(BK,BL)<0 (Theorem 11.8), (iv) the
     G2b/G3b joint exclusion criterion (new sub-lemma from the sibling).
  6. Since this selection holds at every β independently (not "generically"
     or "except at finitely many crossing points"), it needs no continuity
     argument at all — the F3/F3' crossing question (item 9 in current.md)
     becomes structurally irrelevant to this framing, not merely resolved:
     even if F3=0 occurs inside the range, the pointwise selection at that
     exact β is still independently valid.
  7. Conclude: the unique jointly-valid root pair satisfies target identity
     (by step 3's ideal-membership certificate) ⟹ OM=ON.
Key lemmas: same as sibling's steps 5-6 (magnitude bound, G2b exclusion) —
this approach's distinguishing claim is architectural (assembling proved
per-β facts into a proof with NO continuity step), not a new algebraic fact.
Open gaps: identical underlying algebra to the sibling (magnitude bound,
G2b/G3b exclusion) — both still open; ADDITIONALLY needs a clean logical
argument that "exactly one 4-tuple survives, for every β" (step 5) truly
requires no case where two candidates simultaneously pass (a genericity/
non-degeneracy check the sibling's continuity framing sidesteps but this one
must confront head-on).
Cases to cover: same case splits as sibling (sign(b), true-vs-supplementary
root of G2b/G3b); PLUS an explicit check that no β value admits two
simultaneously-valid candidate tuples (would break "exactly one").
Watch out for: this is a genuine architectural fork from the sibling, not a
duplicate — if the pointwise argument in step 5 turns out to need range-
connectedness anyway (e.g. because the "exactly one survives" claim itself
needs an argument that spans neighboring β), it collapses back into the
sibling's framing; the outline-reviewer should watch for this collapse and
treat it as informative (a genuine negative finding), not a wasted round.

ptolemy-trig-identity-synthetic: leave alone (no build this round)
Rationale: per round-5 adjudication, all three of its searches (nine-point
circle, circle-through-B/C, target-circle-itself) are closed negative results,
and its one live contribution (Lemma T, the cotangent-monotonicity
reformulation) is already folded into the sibling's bookkeeping. It is
explicitly self-flagged as subsumed once `ptolemy-trig-identity`'s algebraic
route succeeds. No new synthetic auxiliary-circle idea was surfaced by any
explorer this round, and re-proposing another synthetic search without new
evidence would repeat a documented negative pattern (see
`/tmp/memory/proof-outliner.md` rule 7: don't re-propose hidden-circle
shortcuts without new evidence). Do not dispatch a builder to this slug this
round; revisit only if a future explorer surfaces a concretely new auxiliary
construction.

fixed-point-concyclic: leave alone (no build this round)
Rationale: per round-5 adjudication, its §5.3 general argument conclusively
retires the entire "extend by more polynomial-ideal generators" lever for
this route (antiholomorphic conjugation constraint cannot be captured by any
finite polynomial ideal in the independent variables) — this is a structural,
not incremental, dead end for the route's central mechanism. No explorer this
round proposed a repair. Leaving it live in the population (untouched, not
retired) as a record, but not worth a build slot this round given two other
routes are making concrete, well-evidenced progress on precisely-scoped
sub-gaps.
