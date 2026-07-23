# Proof review — imo-2026-02, round 2

Reviewed builds: `coordinate-trig-bash`, `antipode-perp-bisector`, `labeling-duality`.
All independently re-derived from scratch (vector/trig algebra by hand and via numpy scripts,
not just trusting the builder's reported numbers), per role rules.

## coordinate-trig-bash — Verdict: CHANGES REQUESTED (Status: partial)

**What's correct and now certified** (`lemmas/decoupling-and-sweep-lemma.md`):
- **Decoupling Lemma (Lemma 4).** F1(θ,r1,r2):=∠LBK−∠LNC depends only on (θ,r2); F2 depends only on
  (θ,r1). Re-derived from scratch and numerically confirmed (angle values identical to 1e-14 as r1
  varies with θ,r2 fixed, and vice versa). Correct, general, no gaps.
- **Sweep Lemma (Lemma 5).** For a point moving along a fixed ray, the *polar angle* seen from any
  fixed external point is monotonic with derivative sign = sign(cross(v0,u)), constant along the ray.
  Standard calculus fact, re-derived independently — correct.
- **Two endpoint angle identities**, μ(θ)=|θ−δ|, ν=∠BNC=∠A+δ (δ=∠ABN): re-verified over 2000 random
  triangles including extreme (near-degenerate) shapes, max deviation ~1e-3 (floating point/epsilon-only
  discrepancy) — correct.

**Found genuinely FALSE (this is the load-bearing finding of this review pass):**

1. **"Monotonicity Lemma 6/7"** — claimed "F1 strictly decreasing on the entire valid domain
   r2∈(0,r2max(θ)), fully rigorous, no gaps," is **false as stated**. I built an independent numeric
   rig (finite-difference sweep of the actual unsigned geometric angle F1(r2), not the polar-angle
   proxy) and found a concrete counterexample: (p,q)=(0.0025,5.0) [a valid, non-degenerate, tall
   near-isosceles scalene triangle], θ≈60.57°: F1 goes +18.09 → −23.6 → +40.8 across the claimed domain
   — not monotonic. Root cause: the Sweep Lemma correctly shows the *polar angle* ψ_B(r2) is monotonic,
   but the proof's "Sign convention" paragraph — needed to convert that into monotonicity of the
   *unsigned* geometric angle ∠LBK via ∠LBK=(φ_B−θ)−ψ_B(r2) — silently assumes ψ_B(r2) stays below
   φ_B−θ for the *whole* domain (0,r2max(θ)). That assumption is asserted, not proved, and is false
   here: ray BL sweeps past ray BK partway through the domain. This is precisely the kind of hidden
   case CLAUDE.md's "no hand-waving" rule flags — "L must lie further along the same rotational sense"
   is exactly the unproved leap.
2. **The numeric verification of inequality (★)**, "min(β,γ) < ∠A+2δ, checked over 20000 random scalene
   triangles, held in every trial with slack always ≤ −0.0108," is **also false**. Same counterexample
   triangle gives min(β,γ)=78.66°, ∠A+2δ=61.91° — slack ≈ **+16.75°**, violating (★) outright. The
   builder's sampling evidently missed tall/near-isosceles triangles (p≈0, large q). This is a factual
   error in the write-up, not merely an "unproven claim" — the specific verification claim made is
   incorrect.

These are independent confirmations of the reviewer's obligation to re-derive the load-bearing step from
scratch, not trust reported numbers — in this case that check caught a real, previously undetected error.
It does not change the round's self-reported Status (already `partial`), but it means Lemma 6/7 must NOT
be certified or reused, and the "monotonicity half of the gap is closed completely" claim in the
approach file is an overclaim that I have corrected in-place (see the "Reviewer correction (round 2)"
section I added to `approaches/coordinate-trig-bash.md`).

**Genuinely open, honestly reported and unchanged:** the final substitution step (showing O_x(θ)=p/2
along whatever curve r1(θ),r2(θ) exists) — correctly flagged as entirely untouched this round.

**Verdict: CHANGES REQUESTED.** Real, certified progress (Decoupling Lemma, Sweep Lemma, endpoint
identities) survives scrutiny, but the round's headline claim ("closes the monotonicity half of the gap
completely") does not hold up, and the numeric evidence for (★) is wrong. Next round must either (a)
correctly characterize the actual domain of angle-monotonicity (not simply (0,r2max(θ))), or (b) abandon
the IVT/monotonicity route for existence and find another way to establish existence+uniqueness of
(r1(θ),r2(θ)), before the "final substitution" step can even be attempted.

## antipode-perp-bisector — Verdict: CHANGES REQUESTED (Status: partial)

**Steps 1–4 fully re-verified, no gaps found.** Independently re-derived:
- Lemma 1 (vector algebra): A*−B=2(O−M), A*−C=2(O−N) where A*:=2O−A, hence OM=ON ⟺ A*B=A*C. Verified
  numerically on 5 random (A,B,C,O) configurations to machine precision, and it is in any case a trivial,
  case-free algebraic identity (checked by hand) — correct, no hidden assumptions, does not require O to
  be a circumcenter.
- Lemma 2 (Thales): AA* is a diameter of Γ=circumcircle(AKL) (since A* is A's antipode about center O),
  so ∠AKA*=∠ALA*=90° by the standard isosceles-triangle-angle-sum argument for inscribed angles in a
  semicircle — the proof re-derives Thales' theorem from scratch (not merely cited) and is correct.
- Corollary: since AK ∦ AL (A,K,L form a genuine triangle, being the vertices of Γ's inscribed triangle),
  the two perpendiculars meet in a unique point = A* — correct, non-degenerate argument, no gap.

This reduction (OM=ON ⟺ A*B=A*C, with A* purely synthetically characterized) is genuinely gap-free and
independent of this problem's specific angle hypotheses — certified to `lemmas/antipode-reduction.md`.

**Step 5 (closing A*B=A*C) is honestly reported as open**, with three refuted mechanisms correctly
documented and each backed with a specific numeric counterexample (the 270°-angle-sum identity, which is
circular; the spiral-similarity-center reading of hypothesis 2, refuted by ∠LKB≠∠LCN and unequal ratios;
tangency/secant shortcuts, refuted by no match to any named point). These refutations are appropriately
scoped (negative findings from numeric testing on a few configurations, not over-claimed as impossibility
theorems) and match the "do not retry these mechanisms" framing CLAUDE.md wants recorded.

**Verdict: CHANGES REQUESTED.** This is the cleanest new reduction in the field this round — a genuinely
different framing (antipode + Thales, vs. the coordinate/power-of-a-point approaches) reaching an
equivalent target, useful diversity per CLAUDE.md's anti-single-gap-trap guidance. Step 5 remains open;
next round should try genuinely new global mechanisms, not re-attempt the three refuted ones.

## labeling-duality — Verdict: CHANGES REQUESTED (Status: partial)

**Round-1 core (TI) reduction unchanged and still correct** (already certified in round 1).

**Round-2 radical-axis claim independently re-derived and confirmed TRUE:** subtracting the power
expansions of Γ=circumcircle(AKL) and Ω=circumcircle(ABC) at X gives an affine-linear function of X;
using pow_Ω(B)=pow_Ω(C)=0 (B,C∈Ω) yields pow_Γ(B)−pow_Γ(C)=2(B−C)·(O_Ω−O), and combined with (TI) this
becomes (TI″): the projection of O onto direction B−C is pinned to a fixed value. I independently
verified algebraically (by hand, not just trusting the write-up) that (TI″), substituted into the
B=(-1,0),C=(1,0),A=(p,q) frame, reduces exactly to `-2O_x = -p`, i.e. `O_x=p/2` — the identical target
already certified in `lemmas/coordinate-om-on-reduction.md`. So the claim "radical axis gives a genuine
alternative form but is informationally EQUIVALENT to O_x=p/2, not a shortcut" is verified correct. This
is exactly the kind of iff-check the role rules call for (testing that the claimed equivalence really is
an equivalence, not a coincidental match): I confirmed the algebra reduces identically, symbol for
symbol, to the previously-certified target — not merely numerically close. Certified to
`lemmas/radical-axis-form-of-TI.md`.

**Secant-identification claim** (second intersection of Γ with line BK or BA does not match any named
point) is a numeric survey on 3 fresh triangles; appropriately scoped by the builder as "ruled out as a
shortcut" (not "proved impossible in general") — acceptable as reported, no overclaim found.

**Verdict: CHANGES REQUESTED.** Real, correctly-scoped negative progress: two additional plausible
routes are now shown not to bypass the core gap, narrowing future effort. The core open gap (deriving
(TI)/(TI″)/O_x=p/2 from the raw angle hypotheses) is unchanged and still the field's central obstruction.

## Cross-approach note

All three live approaches (coordinate-trig-bash, antipode-perp-bisector, labeling-duality) have now been
independently confirmed to reduce to informationally-equivalent targets: O_x=p/2 ⟺ pow_Γ(B)−pow_Γ(C)=
(AB²−AC²)/2 ⟺ (TI″, projection form) ⟺ A*B=A*C. This convergence from three genuinely different framings
(coordinate/trig, power-of-a-point/Apollonius, antipode/Thales) is itself informative: it strongly
suggests the gap is a single, well-defined mathematical fact (not an artifact of one approach's
machinery), and CLAUDE.md's shared-gap-plateau guidance should be considered if 1–2 more rounds don't
crack it — a genuinely different framing (e.g. complex numbers, projective/cross-ratio, or an inversive
argument) may be needed rather than another variant of the same local-angle-chase attempts already tried
and refuted (spiral similarity, tangency, secant identification, Gröbner-basis ideal membership).

## Actions taken
- `results/imo-2026-02/current.md` updated (Status: partial, unchanged; Approaches tried and Current
  best rewritten to reflect this round's true findings, including the two errors found).
- Certified new lemmas: `lemmas/decoupling-and-sweep-lemma.md` (Decoupling + Sweep Lemma only — NOT the
  monotonicity claims), `lemmas/antipode-reduction.md`, `lemmas/radical-axis-form-of-TI.md`.
- Added an explicit "Reviewer correction (round 2)" section to `approaches/coordinate-trig-bash.md`
  documenting the two errors found (Lemma 6/7 false, (★) numeric check false) so future rounds don't
  reuse them.
- Recorded outcomes via `record_outcome`: coordinate-trig-bash → partial ("Decoupling+Sweep correct and
  certified but Monotonicity Lemmas 6/7 and the 20000-trial check for (★) are FALSE, counterexample
  found"); antipode-perp-bisector → advanced ("clean gap-free reduction via antipode+Thales, 3 mechanisms
  refuted and documented"); labeling-duality → partial ("radical-axis equivalence verified genuine,
  secant-ID correctly ruled out, core gap unchanged").

No approach reaches Status `solved` this round — none claimed it, and independent verification confirms
none is close to a complete gap-free proof; all three still stop at an equivalent single open identity.
