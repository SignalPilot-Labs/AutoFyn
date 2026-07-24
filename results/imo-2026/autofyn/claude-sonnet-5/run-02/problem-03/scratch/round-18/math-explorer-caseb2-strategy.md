## imo-2026-03 (front 2 / case (b2), lp-duality-certificate)

### Setup recap (verified against the approach file, not re-derived)
Case (b2) = { p1 < T/2 } ∩ { T/D_n < p2 < a_nT/2 }, the sub-region of the
general-upper-bound target `c(n) <= a_nT` left open after: Theorem A closes
p1 in [T/2,a_nT]; case (b1) (`unconditional-p2-threshold-closure`) closes
p2 <= T/D_n unconditionally; case (a) (peel-p1-vs-p2 + full IH) closes
p2 >= a_nT/2 conditionally. Everything on the "peel/bisect + IH" family and
the whole weighted-combination family is now PROVEN (not just suspected)
incapable of reaching case (b2) — see Dead ends below. Round 17 explicitly
asked for a genuinely new *explicit strategy construction*, not a
recombination of Theorem A–D / Bisect-Top-k / Cross-Piece-Sign-Assignment /
Alternating-Gap-Cross.

### Distinct openings
1. **Worst-tail / majorization reduction (new, not tried before).** Fix
   p1,p2 in case (b2)'s box and ask: over all legal tails (p3,...,pm) with
   fixed total, which tail shape maximizes Φ_min (i.e. is hardest for Xiang
   Yu)? If the maximizing tail has a *canonical, low-dimensional* form
   (e.g. close to the ladder ratio-2 shape, or some other explicit family),
   case (b2) collapses from an (n-2)-dimensional continuum of tails to a
   1-2 parameter family that can be checked directly — this is a genuinely
   different mechanism from peel/bisect/recurse/convex-combination, closer
   in spirit to the crux `aimo-0560` move "replace the adversary with a
   strictly stronger surrogate whose reply is pointwise at least as
   damaging, collapsing the reply to a finite menu" (there: replace the
   real lumberjack by a surrogate that damages a strict superset; here:
   replace the real Liu Bang tail-choice adversary by "the tail shape that
   provably majorizes Φ_min for any other tail with the same total," if
   such a dominance/smoothing lemma can be proved). **Numeric probe (n=3,
   p1=0.4, p2=0.25, tail total=0.35, budget 3 cuts, Φ_min computed by a
   from-scratch `differential_evolution` search over every cut-composition
   0..3 cuts split among the 4 pieces, not reusing any builder script):**
   the *maximum* Φ_min over tail shapes tested was **not** at the exact
   ladder ratio 2 (Φ_min≈0.5083) but at ratio≈1.8 (Φ_min≈0.5125), both
   comfortably below the target a_3T=8/15≈0.5333, and both strictly above
   the "even" or "concentrated" tail shapes (Φ_min≈0.5000). This is
   suggestive (not proved) that the worst tail for fixed p1,p2 is *some*
   ladder-like/superincreasing shape but not exactly ratio 2 — so a clean
   "worst tail = ladder" lemma as literally stated is probably FALSE, but a
   *fuzzier* smoothing lemma ("worst tail is superincreasing / concentrated
   toward the front, in some neighborhood of ratio 2") may still be provable
   and would still give the needed dimensional collapse. This numeric
   evidence is weak (single point, DE not fully converged — values are not
   landing on clean rationals, so treat the ratio≈1.8 finding as noisy, not
   exact) but is a genuinely fresh direction, worth a real smoothing/
   exchange-argument attempt (e.g. does swapping a small amount of mass from
   p4 to p3, holding p3+p4 fixed, ever strictly increase Φ_min inside case
   (b2)? — a local perturbation/exchange lemma, in the spirit of the
   already-certified `exchange-smoothing-vertex-maximization` machinery but
   applied to the *tail-generating* adversary rather than to Xiang Yu's own
   response).
2. **Position-adaptive cut pattern (dispatch option (a)).** Rather than a
   fixed-k Bisect-Top-k or a fixed peel target, make Xiang Yu's move depend
   continuously on *where p3 sits relative to p2* (e.g. peel p1 against a
   *blend* of p2 and p3, with the blend weight a function of p3/p2) so the
   reduced instance's own p1',p2' land back inside an *already-closed*
   region (case (a)/(b1)/Theorem-A-band) rather than back in case (b2).
   **This is very likely to hit the same wall as `recursive-image-escape-
   dead-end`**: that lemma proves any mechanism whose only lever is "make
   the recursed image land in a solved case" is capped at the same
   zero-slack ceiling a_{n-1}T', regardless of *how* cleverly the peel
   target is chosen to steer the image there — so a smoothly-varying peel
   target is a special case of exactly the mechanism already ruled out, not
   an escape from it. Flag this to the outliner: don't spend a full
   approach on "adaptive peel target" unless it explicitly produces a
   *strictly smaller than a_{n-1}T'* bound on the recursed tail (not just
   membership in a solved case) — which is precisely opening 1 above,
   reframed.
3. **Boundary continuity/compactness argument (dispatch option (c)).**
   Tested and this looks like a **likely dead end**, not a viable opening:
   case (b1) and case (a) both close with *zero slack* at their shared
   boundaries with case (b2) (per `peel-zero-slack-dead-end`/
   `unconditional-p2-threshold-closure`), which is exactly the situation
   where a naive "Φ_min is small at both walls of the p2-interval, hence
   small throughout by continuity/concavity" argument would need Φ_min(p2)
   to be *concave* (or at least quasi-concave) in p2 with p1, tail-shape
   held fixed — but the numeric sweep above shows Φ_min as a function of
   tail *shape* is **not monotone/concave** (it bumps up at an interior
   ratio, ≈1.8, above both the ratio-2 and ratio-2.5 neighbors) — so a
   pure "boundary pins the interior" compactness argument, without an
   accompanying concavity/majorization proof, is not credible as stated.
   If pursued, it would have to be a genuine two-variable (p2 *and* tail
   shape) joint compactness/vertex argument, which is really opening 1
   wearing different language, not a shortcut around it.
4. **Direct LP/exchange dominance on the (p1,p2,tail) triple, not a
   weighted-combination-of-strategy-values certificate.** The
   Convex-Combination-Futility-Theorem only forecloses combining *already-
   exhibited primal values* Φ_i(p) — it does **not** foreclose an actual
   LP-duality argument over the space of Xiang Yu's *legal responses*
   themselves (a genuine dual certificate assigning weights to *response
   constraints*, not to a finite menu of pre-computed strategies), which is
   structurally different and was noted by the theorem's own "structural
   diagnosis" paragraph as the *correct* tool for lower bounds (Claim B),
   not explicitly ruled out here for the upper bound if reframed as "the
   set of case-(b2) markings is itself covered by a finite union of
   explicit-strategy regions with no gap" — i.e. push harder on finding
   more exact identities (a Theorem E/F/G in the Theorem-A-D family) whose
   union's *domain* (not value combination) covers case (b2), rather than
   averaging values. This is largely a re-statement of "find a genuinely
   new explicit strategy," which is the round's actual mandate — listed
   here mainly to clarify that the futility theorem does not block this.

### Candidate technique(s)
Primary candidate: a **smoothing/exchange-majorization lemma on the tail
shape** (opening 1) — an exchange argument in the style of the certified
`exchange-smoothing-vertex-maximization` / `simplex-exchange-smoothing-
vertex-maximization`, but applied to the space of Liu Bang's *tail choices*
(the adversary's freedom in constructing the marking) rather than Xiang
Yu's response space. This is a genuinely different object than anything
built so far in this front (all existing lemmas smooth over Xiang Yu's
response space, holding the marking fixed).

### Cheap-kill candidates
- Before investing in opening 1: check numerically whether the "worst
  tail" location (ratio argmax) moves as p1,p2 vary across case (b2)'s box
  — if it drifts far from any clean closed form, the collapse to a
  low-dimensional family is likely too messy to close in one round, and
  effort is better spent sharpening the crude bound (e.g. proving *some*
  uniform-in-shape ceiling like Φ_min(tail-shape) <= p2 + f(n-2) regardless
  of shape, even if not tight) rather than exact worst-tail characterization.
- Parity/size check: case (b2)'s box is 2-dimensional in (p1,p2) alone
  (tail shape is (n-2)-dimensional) — confirm whether n=3 (only 1 tail
  parameter) already resists a clean closed form before generalizing; if
  even the single-parameter n=3 case has no clean maximizer, general-n
  worst-tail characterization is probably out of reach this round.

### Knowledge-base entries to use
`knowledge_base.md` has no problem-specific LP-duality/adversary-game entry
beyond generic exchange-argument/smoothing and convexity techniques already
in active use by this project (already cited via `exchange-smoothing-
vertex-maximization`). No new generic KB entry stood out as directly
applicable beyond what's already certified in `lemmas/`.

### Analogous past problems (cruxes)
- **`aimo-0560`** (IMO 2022 P6, Gardener–Lumberjack; subtopic
  `games-and-strategy`) — crux move "replace the adversary with a strictly
  stronger surrogate whose reply is pointwise at least as damaging, so a
  win against the surrogate transfers down and the reply collapses to a
  finite per-region menu." Genuinely analogous *in structure* (an
  alternating two-player game where the prover needs a bound that holds
  against an arbitrary continuum of adversary replies, and the fix is to
  replace the real adversary/environment with a coarser, analyzable
  surrogate that dominates it) — this is the source of opening 1 above.
  Adapt with care: their surrogate strengthens the *opponent's per-move
  power* (cut a superset); our natural analogue would strengthen *Liu
  Bang's tail-construction power* (let him choose among a coarser but
  dominant family of tail shapes) — the crux move must be reproven from
  scratch for this game's very different move structure (continuous cuts
  vs. discrete grid), not transplanted mechanically.
- Re-checked `aimo-0117` (already on file as a confirmed non-analog per
  round 4 — one-shot Stackelberg marking stage has no multi-round
  invariant to attach) and found no reason to revisit that verdict.
- No other `games-and-strategy` or `extremal-principle` crux in the corpus
  (39 total in games-and-strategy) resembled this problem's specific
  "one-shot two-stage marking then forced-greedy-claim" structure closely
  enough to be worth citing; the rest are pairing/mirroring/invariant-based
  combinatorial games with no natural surrogate-adversary or LP-duality
  move.

### Prior progress
See `current.md` / round-17 summary: front 2's entire peel/bisect/recurse
family (`peel-zero-slack-dead-end`, `bisect-containment-dead-end`,
`recursive-image-escape-dead-end`) and the entire weighted-combination
family (`convex-combination-futility-theorem`) are now proven dead for case
(b2). Coverage from explicit unconditional constructions on file
(`bisect-top-k-lemma`, `cross-piece-sign-assignment-identity`,
`alternating-gap-cross-lemma`) is only ~10-26% of case (b2) witnesses at
n=3-5 combined. No approach has yet closed case (b2) in general; round-16's
non-rigorous n=3 grid check (212/214 points) is the closest empirical
corroboration on file but is explicitly not a proof.

### Dead ends (do not retry)
- Peel-p1-vs-p2 / bisect-p1, each + full IH one level down: proven
  zero-slack, thresholds coincide with/are contained in already-closed
  regions (`peel-and-bisect-ih-dead-ends.md`).
- "Recursed image lands in a solved case (a)/(b1)" as the sole lever, for
  *any* choice of peel/bisect target k: proven exactly as inert as the
  above, same ceiling a_{n-1}T', tight at every level
  (`recursive-image-escape-dead-end.md`) — this also pre-empts opening 2
  above unless the adaptive construction supplies something strictly
  sharper than case membership.
- Any weighted/convex combination of a fixed finite family of primal
  strategy values, any weighting rule whatsoever, fixed or p-dependent:
  proven to add zero coverage beyond the pointwise minimum
  (`convex-combination-futility-theorem.md`).
- "Peel-then-dominate" (2-cut extension) and "bisect-largest-cascade":
  both refuted by concrete exact-Fraction witnesses (rounds 12-13, on file
  in the approach file's R12.4/R13.3).

### Small-case / intuition notes (all conjectural, exact-optimizer noise
present — DE was not driven to full convergence, treat ratios as order-of-
magnitude, not exact)
- At n=3, p1=0.4, p2=0.25 (case (b2)): Φ_min for the pure ladder tail
  (ratio 2) ≈ 0.5083; for a slightly less steep tail (ratio ≈1.8) ≈ 0.5125
  (higher, i.e. harder for Xiang Yu); for even/concentrated tails ≈ 0.5000
  (lower/easier). All strictly below target 8/15≈0.5333, consistent with
  case (b2) being true but with real slack at this point (matching round
  14's independent finding of margins ~0.015-0.03 near known witnesses).
  This conjecturally suggests the extremal/worst tail shape inside case
  (b2) is superincreasing-like but not exactly the canonical ratio-2 ladder
  — a genuinely new, previously-unrecorded structural observation, worth a
  real (non-numeric) exchange/perturbation proof attempt next round rather
  than further numeric refinement (the DE noise floor here is too coarse to
  pin the exact maximizer).
