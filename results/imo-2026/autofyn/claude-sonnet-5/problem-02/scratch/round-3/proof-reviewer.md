# Proof review — round 3 — imo-2026-02

Reviewed independently. Read `current.md`, all 5 lemma files, and all three
built approach files in full. For each approach I re-derived the load-bearing
computation from scratch in an independent Python script (not trusting the
builder's own numbers) and probed targeted/extreme configurations, per
standing role rules. Scripts and output are summarized inline below.

## 1. `antipode-perp-bisector.md`

**Claim under review:** a new, "fully proved, no gap" case-exhaustive proof
of `(L1 ∧ L2) ⟹ A*B = A*C`, with L1 (`∠ABA*=θ+90°−γ`) and L2
(`∠ACA*=θ+90°−β`) honestly left open.

**What I verified as correct:**
- The trichotomy on the sign of `90°−α−θ`, and the Isosceles Triangle
  Converse application in Cases 1/2, are valid Euclidean arguments — given
  correct unsigned base angles `∠A*BC=∠A*CB`, the conclusion `A*B=A*C`
  follows regardless of which side of `BC` A* sits on.
- Case 3 (degenerate, `90°−α−θ=0`) via continuity from Cases 1/2 is a valid
  argument structure (single-point removable discontinuity via IVT-style
  continuity, given `f` continuous on the interval and zero off one point).
- The refuted "spiral similarity centered at B" lead (testing whether
  `∠O'BA*=θ` reflects a genuine spiral similarity `(O',A)↦(A*,K)`) is
  reported correctly as refuted (ratio mismatch `BK/BA≈0.40` vs.
  `BA*/BO'≈0.92` at a tested point), not silently reused elsewhere in the
  chain. Good practice.

**Gap found (real, not previously flagged):** the derivation of the two
directed-angle relations `(†) ∠CBA*=90°−α−θ` and `(‡) ∠BCA*=90°−α−θ` (both
as *directed* angles, needed to feed the case split) rests on two unjustified
steps:

1. At B, converting unsigned L1 into the directed relation
   `dir(B,A*)=dir(B,A)−(θ+90°−γ)` requires knowing A* is "further clockwise
   from BA than K" — asserted only as a numerical observation ("confirmed in
   every one of the 20 numerical trials"), never derived from H1∧H2∧H3.
2. At C, the proof claims "the identical computation gives (‡) ... with the
   same numerical value and the same sign convention," attributing this to
   "the roles of CCW and CW swap[ping], exactly compensated." **I checked
   this directly** (independent script, 5 triangle shapes, computing
   `dir(C,A*)−dir(C,B)` in the builder's own stated frame convention
   `dir(C,B)=0`): the actual value in every trial is
   `dir(C,A*)−dir(C,B) = −(90°−α−θ)`, i.e. the *opposite* sign from what
   the proof asserts (`+`). Concretely, at `(p,q)=(0.3,1.7),θ=10°`:
   `dir(C,A*)−dir(C,B)=−20.21°`, not `+20.21°`. The correct relation
   (verified in all 5 trials) is `dir(C,A*)=dir(C,A)+L2` (a `+`), not the
   mirrored `−` the "exactly compensated" claim implies. So the "symmetric
   argument" step is a genuine, uncaught error in the proof as literally
   written — an unjustified "by symmetry" hiding an actual mistake, exactly
   the class of hand-waving `CLAUDE.md` prohibits.

**Why the proof's final conclusion still numerically holds anyway:** Cases
1/2 only use the *unsigned* magnitudes `|90°−α−θ|` (after the sign is
stripped by `|·|`), and `|−(90°−α−θ)| = |90°−α−θ|` trivially, so the sign
bug happens not to propagate into the final numeric conclusion. But this
means the written derivation does not actually establish what it claims to
establish (a directed identity); it is salvageable (re-derive directly with
unsigned angles, or fix the C-side sign) but is **not currently a closed,
gap-free proof** as the approach file claims ("new, rigorous, no gap...
Proof of (L1∧L2)⟹A*B=A*C").

**True status:** `partial`, not the "fully proved sub-lemma" claimed. Real,
reusable progress (the trichotomy + isosceles-converse + continuity
skeleton), but with an internal correctness gap that must be fixed before
certification, on top of the already-acknowledged L1/L2 gap.

**Verdict: CHANGES REQUESTED.**

I did **not** certify the "directed-angle isosceles reduction" lemma
proposed for promotion — it needs the sign-derivation step repaired first
(either prove the orientation claim from H1–H3, or restate the lemma purely
in terms of unsigned angles, dropping the directed-angle machinery that is
currently wrong).

## 2. `coordinate-trig-bash.md`

**Claim under review:** a fully rigorous existence-and-uniqueness theorem
for `(r1(θ),r2(θ))` for every `θ∈(0,min(β,γ))`, via new Lemmas 8/8′
(sign-flip points), 9 (domain correction), 10/10′ (case dichotomy), 12/12′
(unconditional endpoint sign) — explicitly built to replace round 2's false
monotonicity/(★) claims.

**Independent re-derivation (own script, not trusting builder's numbers):**

- Re-derived `r2_signflip(θ) = 2sin(φ_B−θ)/sin(α+2θ)` from the linear
  cross-product equation myself and cross-checked against a direct
  line-intersection computation: **exact match** in every one of ~35
  (shape, θ) trials across 5 triangle shapes including
  `(p,q)=(0.0025,5.0)`.
- Re-derived and tested the dichotomy `r2_signflip(θ)≤r2max(θ) ⟺ θ≥δ`:
  **matched in every trial**, including at the shape `(-0.6,1.2)` where the
  dichotomy stayed in the `θ<δ` branch for the entire tested range (a good
  targeted, non-generic check).
- Directly scanned `F1(θ,r2)` (via `arccos` on the true unsigned geometric
  angles, not the polar-angle proxy) across the *corrected* domain
  `(0,r2*(θ))` at the exact configuration/θ-range that broke round 2's
  claim (`(0.0025,5.0)`, θ up to 70°, plus 4 other shapes, 8 θ values each):
  **F1 is now genuinely strictly monotonic decreasing in every single trial**
  — no sign flips, confirming the domain correction (not just a relabeled
  claim) is what fixes round 2's error.
- Verified the case-(b) endpoint closed form `F1(θ,r2max⁻) = −θ−∠A` matches
  direct computation to displayed precision in 5 configurations.

No gap found in this round's existence/uniqueness Theorem. This is a
genuine, verified repair of a previously-false claim (per the standing rule
to independently re-run "verified over N trials" claims — this one holds up
under adversarial, targeted testing, unlike round 2's).

**Confirmed genuinely open (per the dispatch instruction):** the final
substitution `O_x(θ)=p/2`. The approach file explicitly states no closed
form for `r1(θ),r2(θ)` was found and reports only a numerical sanity check
(5 shapes, ~1e-13–1e-15 agreement) — correctly distinguished from proof.

**Verdict: CHANGES REQUESTED** (real, substantial, verified progress —
outcome "advanced" — but Status remains `partial`; the final-substitution
gap is the sole, sharply-isolated remaining target for this approach).

Certified `lemmas/existence-uniqueness-r1-r2.md`.

## 3. `trig-ceva-chase.md` (new approach)

**Claim under review:** closed-form quadratics for `r1(θ), r2(θ)` via a
general "Lemma T1" (angle-matching on a ray is degree ≤2), verified
numerically including at the exact `(p,q)=(0.0025,5.0)` counterexample
point; plus a claim that the final `OM=ON` step is NOT a genuine bypass.

**Lemma T1 proof check:** the algebra is elementary and correct (affine
`Cross_i(r),Dot_i(r)` from bilinearity of cross/dot in `r`; `Q(r)` a
difference of two affine products, hence degree ≤2). No gap.

**Independent re-derivation of the application to F2(θ,r1):** re-implemented
the construction from scratch (own script: built `w1=B−M`, `u1,u2` from
`θ`, fit the quadratic from 3 sampled values of `Q(r1)`, solved for roots)
in 5 configurations including `(0.0025,5.0)` at `θ=60°` and `θ=34.4°`
(≈0.6 rad, the builder's own tested value). In 4/5 direct trials the
smaller quadratic root matched the true `arccos`-based root of `F2=0` to
8+ significant figures; the 5th trial's apparent mismatch was a
bracketing artifact in my own bisection call, and a direct scan confirmed
`F2` does cross zero exactly at the quadratic's smaller root
(`r1≈0.5526`) — Lemma T1's application is correct and reusable.

**Branch-selection caveat:** correctly and explicitly flagged by the
builder as numerically-confirmed only, not proven — appropriately scoped,
not overclaimed as a theorem. Matches the standing caveat pattern already
attached to the Sweep Lemma.

**Negative finding on §5 (the final `OM=ON` step is not a bypass):**
assessed as correctly argued, not merely asserted. The approach's own
Lemma T1 machinery already works with actual vector positions of
`B, C, M, N` (an implicit affine frame) to compute cross/dot products —
so the claim that pinning `pow_Γ(B)` (or equivalently `O`'s position
relative to `B,C`) requires reintroducing frame-equivalent data is
essentially forced by the approach's own construction, not a new
assumption smuggled in. This is a legitimate, appropriately-modest
negative finding (an argument, not a bare assertion), consistent with the
already-certified equivalence of `O_x=p/2` and the radical-axis form (TI″)
from round 2.

**Verdict: CHANGES REQUESTED** (real new, correct, reusable machinery —
Lemma T1 and its verified applications — but the shared gap is untouched;
Status `partial`).

Certified `lemmas/angle-matching-ray-quadratic.md` (with the
branch-selection caveat explicitly excluded from certification, per the
builder's own scoping).

## Whole-problem check

None of the three approaches, individually or combined, closes the full
problem this round. All three converge on the same underlying fact that
must still be derived from the three angle hypotheses (`O_x=p/2` /
`pow_Γ(B)−pow_Γ(C)=(AB²−AC²)/2` / `A*B=A*C`), and `trig-ceva-chase`'s own
negative finding (independently confirmed reasonable) explicitly rules out
its route as a bypass. `coordinate-trig-bash`'s existence/uniqueness half
is now fully closed (a genuine, reviewer-verified fix of a previously false
claim), sharpening the field's single remaining target to one clearly
stated gap (the final substitution / equivalent scalar identity), but that
gap itself remains open. `current.md` `## Status` updated to reflect all
three round-3 outcomes; remains `partial`.

## Lemma certification summary

- `lemmas/existence-uniqueness-r1-r2.md` — **certified** (coordinate-trig-bash,
  Lemmas 8/8′/9/10/10′/12/12′ + closing theorem).
- `lemmas/angle-matching-ray-quadratic.md` — **certified**, Lemma T1 only
  (trig-ceva-chase); branch-selection claim explicitly excluded.
- antipode-perp-bisector's proposed "directed-angle isosceles reduction"
  lemma — **rejected for certification this round**: contains an unrepaired
  sign error in its C-side derivation (see §1 above); resubmit once fixed
  or restated in unsigned-angle form.

## Outcomes recorded (mcp__approach-ranker__record_outcome)

- `antipode-perp-bisector` → `partial` (gap in claimed complete reduction
  found and detailed).
- `coordinate-trig-bash` → `advanced` (round-2 false claim genuinely fixed,
  existence/uniqueness closed, one sharp gap remains).
- `trig-ceva-chase` → `partial` (new correct machinery, no progress on
  shared wall, negative finding on final step confirmed reasonable).
