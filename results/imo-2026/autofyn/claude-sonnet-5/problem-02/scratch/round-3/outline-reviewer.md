## imo-2026-02 — outline review, round 3

### antipode-perp-bisector (revise) — VERDICT: APPROVE

The outliner's new lead is well-posed and I independently re-verified it
numerically (not just trusted the explorer's claim): built an independent
`fsolve` rig for K,L satisfying the hypothesis system on 4 fresh triangle
shapes (p,q)=(0.3,1.7),(-0.6,1.2),(0.1,2.5),(0.9,1.3), 3 values of θ each,
computed A*=2O-A directly, and confirmed

  ∠ABA* = θ + 90° − γ,  ∠ACA* = θ + 90° − β

to 1e-10–1e-13 in every trial (script output attached below). This is a
strong, independent corroboration beyond what the explorer already reported.
The subsequent angle chase (∠A*BC=∠A*CB=90°−α−θ ⟹ A*BC isosceles ⟹ A*B=A*C)
is elementary and correct, and OM=ON followed numerically in every trial to
1e-10 or better, consistent.

Issues to flag for the builder (not fatal, but must be closed, not glossed):
- L1/L2 themselves are still *conjectural* — verified numerically only, not
  yet derived from H1∧H2∧H3. The outline's proposed mechanism ("H3 pins r1,
  chain through ∠AKA*=90° and triangle ABK's angle sum") is stated as a
  conjecture to attempt first, with a fallback (Law of Sines in ABA*
  directly) — this is honest hedging, acceptable for CHANGES REQUESTED-style
  progress, not a hidden circularity. Builder must actually derive it, not
  assume it because it's numerically clean.
- The sign/branch of `90°−α−θ` (whether A* is on the same side of BC as A)
  is correctly flagged as needing explicit handling — since the target is
  the *unsigned* distance equality A*B=A*C, the isosceles argument via equal
  *unsigned* base angles survives a sign flip, but the outline is right that
  this must be stated, not silently assumed. Builder should verify the
  isosceles-triangle-converse step still applies when `90°−α−θ<0` (in which
  case ∠A*BC=∠A*CB=α+θ−90°, still equal to each other — same conclusion,
  just write it out).
- No case is skipped in the reduction chain (Lemma 1 vector algebra, Lemma 2
  Thales, corollary characterization of A* — all previously certified,
  unchanged this round).

This is the strongest, cleanest gap in the whole field right now — a genuine
different sub-target (not O_x=p/2) with a two-lemma closing plan and fresh,
independently-reproduced numerical support. Build this.

### coordinate-trig-bash (revise) — VERDICT: APPROVE (with gaps to close)

The domain-correction fix (r2_signflip, corrected domain
(0,min(r2max,r2_signflip))) is well-posed: it correctly diagnoses that the
prior round's counterexample was not a genuine failure of the underlying
mechanism but an artifact of applying Lemma 6 outside the region where "K
inside angle LBA" actually holds. This round's monofix explorer verified the
repair concretely at the exact counterexample point
((p,q)=(0.0025,5.0),θ≈60.57°: r2max≈1.759, r2_signflip≈1.051, F1 goes
+18.09→−24.23 monotonically on the corrected domain) and across 2300+ trials
with zero counterexamples — this is a genuine, checkable repair, not wishful
thinking, and the case-split (a)/(b) at the endpoint is exhaustive by
construction (r2* is defined as a min, so one of the two cases always binds).

Issues to close, correctly flagged as open in the outline itself:
- r2_signflip(θ) needs a rigorous (not just numerical) definition/derivation
  as the true boundary of "K inside angle LBA" — must be proved, not merely
  observed to work in 2300 trials.
- Case (a) endpoint sign ∠LNC(r2*)>0 and case (b)'s weaker per-θ inequality
  `θ<∠A+2δ` are both still unproven scalar claims — smaller and more
  tractable than the old false global (★), but not yet proven.
- The symmetric F2/r1 analysis (step 5) is not yet carried out — must mirror
  steps 2–4, not be waved through as "obviously symmetric."
- The final substitution O_x(θ)=p/2 remains completely untouched and is
  correctly flagged as the largest remaining gap even after existence and
  uniqueness are settled.
- Per the standing rule from round 2 (never reuse "checked over N trials"
  claims without independent re-verification), the builder must re-derive
  the r2_signflip repair analytically at least at one worked example, not
  just cite the monofix explorer's 2300-trial count as sufficient.

This is legitimate, bounded, well-scoped repair work — build it.

### labeling-duality (advance, dormant) — VERDICT: no objection, correctly deprioritized

Confirmed algebraically equivalent to coordinate-trig-bash's O_x=p/2 gap
(certified in `lemmas/radical-axis-form-of-TI.md`); the outliner's decision
not to spend a build slot here this round is sound — any progress on
coordinate-trig-bash's domain-fix/final-substitution transfers automatically.
Not in this round's build set; keep registered, do not build.

### trig-ceva-chase (new) — VERDICT: APPROVE, with a mandatory early check

This is the plateau-break candidate CLAUDE.md's rule calls for (top
approaches have been circling the same O_x=p/2-equivalent wall for 2
rounds). It genuinely changes computational medium (pure trig/Law-of-Sines
chase in the hypothesis sub-triangles, no Cartesian frame, no complex
numbers, no power-of-a-point abstraction) versus the three live approaches,
which all eventually fix a coordinate frame, a complex frame at O, or a
power/radical-axis abstraction respectively. The newframing explorer
scouted 4 candidate "genuinely far" framings this round and ruled out two
(rigid spiral similarity, reflection symmetry across perp-bisector(MN)) as
dead on arrival; this is the one live "genuinely far" survivor it
recommended.

However — the outline is honest, and I agree with its own risk assessment:
steps 3/4 (closed-form solve for r1(θ), r2(θ) via Law of Sines in triangles
BMK/CNL) may simply be the *same* transcendental system as
coordinate-trig-bash's F1=0/F2=0, dressed in trig notation instead of
coordinates — not a genuine bypass. This is NOT grounds for RETHINK (the
outline explicitly flags it as an open question to check, not a hidden
assumption or a fatal circularity), but it IS grounds for a mandatory
condition on the build: **the builder must determine and report, early and
explicitly, whether r1(θ)/r2(θ) admit closed trig forms or whether the
system is transcendental exactly as before.** If it's the latter, the
approach's remaining value is as a cross-check / cleaner route to the final
identity (step 6's trig OM²-ON² identity), not a genuine independent
bypass — and this should be reported honestly rather than silently retried
as if it were new territory. This condition is already written into the
outline's own "Watch out for" section, so no revision is needed before
building — just enforce it.

Diversity assessment for the field: with antipode-perp-bisector's L1/L2
target (genuinely distinct from O_x=p/2), coordinate-trig-bash's domain fix
(same underlying scalar target, different technique for existence), and
trig-ceva-chase (different medium, possibly same wall), the field now has
real framing diversity at the top — one approach (antipode) is on a
structurally different target, one (trig-ceva) uses a different medium, and
one (coordinate-trig-bash) is the incumbent with the most concretely
bounded remaining gaps. This satisfies the plateau-break requirement; no
further diversification action needed this round.

### Not built this round
- `two-step-spiral-chain`: confirmed dead-end (unchanged, no new evidence to
  revisit).
- `complex-circle-power`, `nine-point-link`: still unbuilt outlines, lower
  priority than the three approaches above; revisit only if all three live
  approaches stall again.

### Ranking
Registered `trig-ceva-chase` (cold-start 1500). Ran `update_ranking` with 13
comparisons anchored to this round's evidence: antipode-perp-bisector and
coordinate-trig-bash both beat labeling-duality (dormant) and
trig-ceva-chase (untested, new); antipode-perp-bisector edges out
coordinate-trig-bash (fresher, more concretely-verified new lead this
round, vs. a repair of a previously-corrected false claim); trig-ceva-chase
beats the three unbuilt/dead approaches (two-step-spiral-chain dead-end,
complex-circle-power and nine-point-link never built). Post-update Elo
(best-first): coordinate-trig-bash 1611.6, antipode-perp-bisector 1594.7,
labeling-duality 1541.0, trig-ceva-chase 1517.6, two-step-spiral-chain
1423.5, complex-circle-power 1420.7, nine-point-link 1390.9.

### Verification note
Independently re-derived the antipode-perp-bisector L1/L2 numerical claim
from scratch this round (own fsolve rig, 4 triangle shapes × 3 θ values,
agreement to 1e-10–1e-13) rather than trusting the explorer's report at
face value, per standing rule (never let terrain evidence substitute for
own verification when time allows).

build set: antipode-perp-bisector, coordinate-trig-bash, trig-ceva-chase
