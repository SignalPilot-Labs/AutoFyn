# Outline review — round 12, imo-2026-02

## Independent verification performed (from scratch, not trusting the outliner's numbers)

**q1r0lens's β1-elimination (Steps 1,3,5).** Re-derived by hand and confirmed by an
independent fresh sympy/numpy check:
- Step 1 identity `sin(A+3β1) = s(4X0-3)x + c(4X0-1)y` (x=cosβ1,y=sinβ1,X0=x²) is an
  **exact algebraic identity** (triple-angle formulas + licit substitution x²→X0,
  y²→1-X0, both ≥0) — verified exactly on 200,000 fresh random samples (max abs error
  ~1e-14, consistent with floating-point noise only, i.e. genuinely 0).
- Step 5 squaring (`px+qy<0 ⟺ q²(1-X0)<p²X0`, given p<0,q>0) is a valid iff since both
  sides are ≥0 after negation — verified on 167,020 fresh samples restricted to
  p<0∧q>0, **zero mismatches**.
- Step 3 (`β1<γ=B ⟺ X0>d²`) is trivial cos-monotonicity given x,d≥0 — sound.
These three steps are genuinely exact reductions, not just numerically-suggestive —
correctly disclosed as such by the outline (not overclaimed).

**Steps 2 and 4 (the two remaining open sub-gaps).** Ran an independent 10,000,000-sample
sweep from the raw definitions (K, P, A_c, C_c, E, X0, γ=min(B,C), β1, all rebuilt from
scratch, not copied from any file), correctly imposing the FULL Case-(b) domain
(β1<γ ∧ sin(A+3β1)<0) intersected with E<0 — not merely X0>d² alone (an initial naive
sweep using only X0>d² without the C-side condition badly over-included points with
B>C, confirming why the outline is careful to require proving γ=B, i.e. C≫B, as a real
gap, not a free assumption). On the genuine residual sub-case (25,552 samples):
- **X0 range: (0.3486, 0.3955)** — deep inside (1/4,3/4) with huge margin (X0<3/4 and
  X0>1/4: zero violations, and not even close). This corroborates Step 4 strongly and
  suggests it is likely the *easiest* remaining sub-gap in the outline, not a hard one.
- **B<C in all 25,552 samples (zero violations), B<π/2 always** — corroborates Step 2
  (γ=B) exactly, matching the outline's claimed window (A∈(0.407,0.536), B∈(0.912,1.090)).
- q1<0, r0<0 reconfirmed (zero violations, matching round 11).
No fatal contradiction found; the outline's claims are numerically rock-solid and the
mechanism (resultant/Gröbner elimination of c,s,d,t) is the same style already certified
elsewhere in this population (T-factorization). Sound plan.

**starlens's ∂S/∂B margin claim.** Independently reproduced via a fresh finite-difference
sweep (own domain-membership test, 36,254 valid samples restricted correctly to
β0<β1<B, RHS>0): **zero violations of ∂S/∂B≥0, min observed derivative ≈0.177** — matches
the reported 0.178–0.19 margin almost exactly. This is a real, reproducible non-knife-edge
fact, good evidence a clean algebraic proof exists (decomposition into a manifestly
positive piece plus a bounded ∂RHS/∂B term, per the outline's plan).

Both headline numeric claims check out under independent re-derivation. No overclaiming
found in the outline — every claimed-open item (Step 2, Step 4, ∂S/∂B's symbolic proof,
the boundary-curve residual) is correctly disclosed as unproven, not asserted.

## Per-approach verdicts

**coordinate-bash-resultant-boundary — APPROVE (advance).** Technique (resultant/Gröbner
elimination of c,s,d,t mod Pythagorean identities) is the right tool, already proven
capable in this population (T-factorization, magnitude bound, etc.). Skeleton is sound:
imports certified facts unchanged, splices q1r0lens's exact-identity steps, isolates
Step 4 as a genuinely smaller polynomial claim. Given the huge observed margin on X0
(0.35–0.40 vs. target (0.25,0.75)), Step 4 looks tractable by a much cruder bound than a
sharp characterization — flag this to the builder as a shortcut worth trying first
(e.g. bound X0 crudely via known A,B ranges rather than a tight elimination). Step 2
(γ=B) needs an explicit inequality from the certified E<0/Case-(b) constraints — the
outline correctly flags not to silently assume it (round-9/10 lesson).

**coordinate-bash-resultant-boundary-pointwise — APPROVE, no build slot (dormant, per
standing round-9 rule).** Its content is fully inherited by the two forks below; do not
give it a separate build slot.

**coordinate-bash-resultant-boundary-pointwise-tangent — APPROVE (advance).** Sound
decomposition plan (reuse certified ∂X0/∂B>0 as one clean positive piece, bound ∂RHS/∂B
separately). Rationalize via u=tan(A/6) before attempting sympy.simplify — correct
tractability fix (blind simplify times out, confirmed independently this round). Margin
evidence (~0.177–0.19, confirmed) supports that a genuine algebraic proof, not a
coincidence, is the target. Step 5 (boundary-curve residual) is honestly flagged as its
own remaining sub-target.

**coordinate-bash-resultant-boundary-pointwise-tangent-twopoint — APPROVE (new copy,
registered).** Genuinely different mechanism (two-point-pinned tangent/secant, crux
aimo-0005-style) on the same (⋆) gap — correctly diagnoses why the single-point version
failed (under-determination: 1 pin, 2 unknowns) and proposes a concrete fix (2 pins).
Exploratory/untried, honestly scoped as such (open gap: does a usable second closed-form
point on X0=cos²B exist at all). Worth a build slot as a real second lever, not a rehash.

**coordinate-bash-resultant-boundary-pointwise-sos — APPROVE (advance).** Correctly
restricts to a CONSTRAINED (n1,n2-multiplier) Positivstellensatz search, since the
outline correctly does NOT re-attempt an unconditional SOS certificate (round 11 proved
none exists — the "Watch out for" note is correctly worded and matches the certified
negative result). Hand-ansatz coefficient-matching (in lieu of unavailable cvxpy) is a
reasonable fallback; explicitly flags installing cvxpy as a future option rather than
silently giving up if the hand search stalls. No fatal flaw.

## Diversity / shared-gap-plateau note (as required)

All four approaches in the build set are structurally the same lineage (copies of
coordinate-bash-resultant-boundary), all targeting the one remaining Case-(b) residual
gap, differing only in mechanism (algebraic elimination / MVT-monotonicity /
Positivstellensatz / two-point tangent). This is NOT a fresh instance of the
shared-gap-plateau problem CLAUDE.md warns about — round 8 already PROVED (not just
observed) that every live route in this population (fixed-point-concyclic, inversion,
ptolemy) reduces to the identical underlying branch-selection object, and the
newframing-lens/other explorers have repeatedly (rounds 3, 5, 8) run exhaustive negative
searches for a genuinely different top-level target and found none. Given that structural
proof, deploying multiple independent *mechanisms* on the one real remaining gap is the
correct final push, not a diversity violation — but it should be watched: if none of
these four closes the gap in the next 1–2 rounds, the next round should seriously
reconsider whether (⋆)/T≥0 are themselves too lossy a target (per starlens's own
closing remark) and revisit the un-squared G(β1)≥0 directly.

## Build set

All four are strong, independently-verified, complementary levers on the same tightly-
scoped final gap, with real (not manufactured) margin evidence for two of them. Build all
four in parallel.

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-tangent-twopoint, coordinate-bash-resultant-boundary-pointwise-sos
