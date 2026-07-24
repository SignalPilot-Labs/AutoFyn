# Proof review — IMO-2026-02, round 1

Problem: Let ABC be a triangle, M, N midpoints of AB, AC. K inside △BMC, L
inside △BNC, with K inside ∠LBA, L inside ∠ACK, ∠KBA=∠ACL, ∠LBK=∠LNC,
∠LCK=∠BMK. O = circumcenter(AKL). Prove OM=ON. (proof_only, answer_type none.)

Reviewed knowledge_base.md (synthetic toolkit: angle chasing, power of a
point, standard coordinate/circle facts — no named theorem misused by any
approach below).

---

## coordinate-trig-bash.md

**Claims checked independently.**

- *Lemma 1 (OM=ON ⟺ O_x=p/2)* in the B=(-1,0), C=(1,0), A=(p,q) frame: correct
  algebra (`OM²-ON² = 2O_x - p`), re-derived from scratch and confirmed
  numerically (O_x=p/2 ⟹ OM=ON exactly; O_x≠p/2 ⟹ OM≠ON). Valid, complete,
  reusable.
- *Lemma 2 (circumcenter formula via Cramer's rule)*: standard, correctly
  re-derived from the two perpendicular-bisector linear equations. Valid.
- *Lemma 3 (ray parametrization of K, L via shared angle θ)*: the
  orientation argument (K's ray has polar angle φ_B−θ not φ_B+θ, forced by
  "interior of angle MBC") is argued correctly and is not hand-waved away
  ("clearly"/"obviously" is avoided; the direction is justified by which
  side of ray BM the interior of the angle lies on). This is acceptable.
- *Negative Gröbner-basis finding*: I independently reconstructed the three
  angle-equality polynomials (via the same cross/dot "directed tangent"
  identity, for the same test triangle p=3/10, q=11/10) from scratch in
  sympy, without looking at the builder's code, and computed a Gröbner
  basis (grevlex) of the resulting {eq1(deg2), eq2(deg3), eq3(deg3)} ideal.
  Reducing the target polynomial Ox·D − (p/2)·D against this basis gives a
  **nonzero remainder**, exactly reproducing the builder's finding
  (see /tmp/verify3.py). This is a genuine, correctly-executed negative
  result, not an artifact of a coding mistake — the claim that "raw angle
  equalities alone don't force O_x=p/2, and the branch-selection gap is
  real and open" is honestly reported, not overclaimed. The builder never
  states this as a proof of anything beyond the negative finding itself,
  and clearly separates "fully established" from "numerical confirmation
  only" from "attempted, failed."
- The Status `partial` is accurate: real, certified progress (Lemmas 1–3),
  honest report of what remains (isolating the correct semialgebraic branch,
  or an explicit closed-form solve of r₁(θ), r₂(θ)), no overclaim.

**Verdict: CHANGES REQUESTED.** Status: partial (confirmed correct
self-assessment). Gap to close next round: derive O_x=p/2 (or the
equivalent (TI) from labeling-duality) from the angle hypotheses AND the
containment/orientation constraints — not from the angle equalities alone.
Concretely: either (a) find a Positivstellensatz/branch-isolating algebraic
argument, or (b) solve r₁(θ), r₂(θ) in closed form on the geometric branch
and substitute into the circumcenter formula.

---

## labeling-duality.md

**Claims checked independently.**

- *Step 0 (σ-invariance of the hypothesis system)*: a purely syntactic
  relabeling check (B↔C, K↔L, M↔N, using ray-equality facts BM=BA-ray,
  CN=CA-ray). Verified by hand-tracing the substitution on all three
  conditions; correct, and the caveat that σ is not a rigid map of the
  actual figure (only a symmetry of the equation *labels*, relating two
  different problem instances) is explicitly and correctly stated — this
  is exactly the trap CLAUDE.md warns about ("by symmetry" hiding an
  invalid step), and the builder avoids it by being precise about what σ
  does and does not license.
- *Lemma A (Apollonius/median-length identity)*: re-derived from scratch
  independently (both symbolically via the parallelogram law and
  numerically on 3 random points, /tmp/verify.py) — matches exactly,
  residual ~1e-16. Fully general, fully proved.
- *Reduction to (TI)*: `OM=ON ⟺ pow_Γ(B) − pow_Γ(C) = (AB²−AC²)/2`. I
  independently re-derived this chain (Lemma A applied twice, subtract,
  substitute OA=R) and confirmed it is a genuine **iff**, not a tautology:
  using an arbitrary triangle A,K,L (NOT satisfying the problem's angle
  hypotheses) and its actual circumcenter O, I checked that (TI) and
  OM=ON fail *together* (both sides mismatch), consistent with — not just
  numerically checked on — the iff (/tmp/verify2.py). This is a genuinely
  proven reduction, not merely a numerically-checked conjecture; the
  builder is explicit that the numerical example in the writeup is "a
  consistency check... not a substitute for" the algebraic derivation,
  which is the correct framing per CLAUDE.md's proved-vs-conjectured rule.
- *Open gap*: proving (TI) from the three angle hypotheses via secant
  lines / inscribed angle theorem is honestly flagged as not completed,
  with a clear diagnosis of where it stalls (no hypothesis directly pins
  down ∠AKL, ∠ALK, ∠KAL — these live on Γ, but the hypotheses relate K, L
  to B, C, M, N, not to Γ directly). No hand-waving; the difficulty is
  named precisely.
- Status `partial` is accurate — a real, fully-proved reduction lemma plus
  an honestly-stated remaining gap, not an overclaim.

**Verdict: CHANGES REQUESTED.** Status: partial (confirmed). This is the
sharpest reduction across all approaches this round: the *entire* problem
is now equivalent to proving a single scalar identity (TI). Next round
should attack (TI) directly, likely by combining it with
coordinate-trig-bash's explicit ray parametrization (Lemma 3) to compute
pow_Γ(B), pow_Γ(C) directly rather than via secant/inscribed-angle
synthetic search.

---

## two-step-spiral-chain.md

**Claims checked independently.**

- Reconstructed the exact numeric test (triangle (p,q)=(0.3,1.7), t=0.40,
  fsolve on the 4-equation system for K,L) from scratch, independently of
  the builder's code (/tmp/verify4.py). Got residuals ~1e-16 (valid
  solution), OM−ON ~ −4.4e-16 (confirms OM=ON on this branch, sanity check
  on rig correctness), and **BK/BL=0.399732, NL/NC=0.582386** — these
  match the builder's reported table row for t=0.40 to 6 significant
  figures exactly. This independently confirms both that the test rig is
  correctly implemented and that the claimed spiral-similarity ratio
  equality genuinely fails (difference ≈ −0.183, far above numerical
  noise).
- The concyclicity determinant test (standard 4-point circle determinant,
  correctly cited as the standard test) is methodologically sound; the
  builder checked all 20 four-subsets containing K (a superset of the
  outline's named candidates), not just the outline's guesses — this is
  more thorough than required and rules out "maybe a different 4th point
  works" objections.
- The refutation is robust: tested on two independent, non-symmetric
  triangles, over a spread of parameter values, with deviations that are
  large (order 0.1–1, not noise-level) and vary smoothly/monotonically —
  the builder's argument that this is inconsistent with a real identity
  with an accidental sign-matching artifact is sound reasoning.
- Status `unsolved` / dead-end diagnosis is honest and correctly
  self-assessed; no overclaiming, no lemma promoted (correctly — nothing
  survived).

**Verdict: RETHINK.** Status: unsolved (confirmed, independently
reproduced). This specific approach (these two named local rigid-map
mechanisms) cannot work as set up and should not be re-attempted verbatim.
If this "local rigid-map/spiral-similarity" framing is to be pursued
further, the next outline must propose a genuinely different candidate
transformation — not a variant of BKL~NLC or a C,K,M,X concyclicity.

---

## Promotable lemmas — certified

Two lemma files written to `results/imo-2026-02/lemmas/`:

1. **`median-length-power-reduction.md`** (from labeling-duality): the
   general Apollonius median-length identity, plus the problem-specific
   reduction OM=ON ⟺ pow_Γ(B) − pow_Γ(C) = (AB²−AC²)/2. Certified — fully
   proved, independently re-derived and numerically spot-checked by the
   reviewer.
2. **`coordinate-om-on-reduction.md`** (from coordinate-trig-bash): the
   coordinate criterion OM=ON ⟺ O_x=p/2, the circumcenter Cramer's-rule
   formula, and an honest note of the Gröbner-basis negative finding (so
   future approaches don't redo the same failed ideal-membership
   computation without first isolating the geometric branch). Certified.

Lemma 3 (ray parametrization) from coordinate-trig-bash was NOT split into
a separate certified lemma file — it remains valid but is left inline in
its approach file since it is setup-specific to that coordinate frame and
its main reuse value is already captured in the approach's own writeup.

## current.md

Updated `results/imo-2026-02/current.md`: Status `partial`, Approaches
tried section covering all three reviewed slugs (+ note that
complex-circle-power and nine-point-link exist but were not built/reviewed
this round), Current best section summarizing the two proven reductions
((TI) and O_x=p/2) as the shared frontier, no Full proof section (nothing
solved yet).

## Ranker outcomes recorded

- coordinate-trig-bash → partial
- labeling-duality → advanced
- two-step-spiral-chain → dead-end

## Verdicts (one line per slug)

coordinate-trig-bash: CHANGES REQUESTED
labeling-duality: CHANGES REQUESTED
two-step-spiral-chain: RETHINK
