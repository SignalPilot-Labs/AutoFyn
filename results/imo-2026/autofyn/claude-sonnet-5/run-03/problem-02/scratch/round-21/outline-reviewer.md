# Outline review — round 21 — imo-2026-02

## Independent verification of the two key premises

### 1. caseA-lens's "Y(β)<0 throughout (β0,γ)" finding (witness A=0.02, B=1.5)

Reproduced from scratch (own `mpmath`, dps=50, raw definitions `X0 := sinB
cosA/(2sin(A+B))`, `β1 := arccos(√X0)`, `β0 := (π−A)/3`, `Y(β) := 2cos²β −
m cosA`, `m := sinB/sin(A+B)`), not reusing the explorer's script:

- `X0 = 0.499291761…`, `cos²β0 = 0.255795553…` ⇒ `X0 > cos²β0` — genuine
  Case (a) point, confirmed.
- `β1 = 0.786106…`, `β0 = 1.040531…` ⇒ `β1 ≤ β0`, confirmed.
- `Y(β0) = −0.486992…`, and `Y` strictly decreasing on the scanned grid down
  to `Y(γ)=Y(B) = −0.988576…`. **Y < 0 at every one of 11 sampled points
  across `[β0,γ]`, matching the explorer's report exactly.**

Went further than the explorer (single-witness only) and ran a fresh
300,000-sample sweep over `(A,B)` restricted to the population's own domain
(`A ≤ π/2`, `B ≤ C`) and to genuine Case-(a) points (`X0 > cos²β0(A)`,
equivalently `β1 ≤ β0`): **15,273 genuine Case-(a) samples, 0 violations of
`Y<0` throughout `(β0,γ)`**, max observed `Y` over the whole sweep
`≈ −5.2×10⁻⁵` (approaching 0 only in the degenerate limit `β1→β0`). This is
strong, broad (not single-point) corroboration.

More importantly: **this fact is not merely numeric — it is elementary and
provable in one line**, and the outline should say so explicitly rather than
present it as a numeric finding to be re-verified. `Y` is strictly
decreasing with unique zero at `β1` (already an established fact per the
population's own derivation). If `β1 ≤ β0`, then by monotonicity
`Y(β0) ≤ Y(β1) = 0`, and for every `β > β0` in the interval, `Y(β) < Y(β0)
≤ 0`. So "Case (a) ⇒ Y<0 throughout `(β0,γ)`" is a two-line consequence of
monotonicity + the defining property of `β1`, not a fact requiring further
sampling. This *strengthens* the outline's premise (H-wrong-target)'s
foundation from numeric-only to essentially certified — good, but the
outline (line 12) undersells it as "already certified fact" without stating
the one-line argument; the builder should write it out explicitly as a
standalone certified lemma before building on it (cheap, ~5 minutes,
removes any residual doubt).

**Verdict on this premise: sound and independently confirmed, strictly
stronger than the outline claims (elementary, not just numeric).**

### 2. spiral route's new ∠(AQ,AB) = ∠B claim

Reproduced from scratch (own `numpy`, 5 random non-degenerate triangles,
own `Q` construction as `A + t·(C−B)` solving `(Q−mid(B,C))·(C−B)=0`, own
directed-angle-mod-π helper via `atan2` difference reduced into `(−π,π]`):
at every one of 5 trials, `angle(AQ,AB) + angle(ABC) ≡ 0 (mod π)` — e.g.
`(−1.7014, angleB=−1.4402)` sum `= −π`; `(1.7601, 1.3815)` sum `= +π`;
`(−1.2478, 1.2478)` sum `= 0`. This confirms the claimed identity up to the
directed-angle sign convention the explorer already flagged (mod π,
`∠(l1,l2) = −∠(l2,l1)`, so "equal in magnitude, opposite formal sign" is
the expected form of an alternate-interior-angle fact through a parallel
line, not a discrepancy). The underlying geometric content — `AQ∥BC`
(already certified) makes `AB` a transversal, giving equal alternate
angles with `∠ABC` — is genuinely elementary and requires no further
verification; this is a correct, gap-free one-line lemma as claimed.

**Verdict on this premise: sound and independently confirmed.**

## Approach-by-approach review

### `coordinate-bash-resultant-boundary-pointwise-tangent` (revise)

Right technique (same certified Reduction-Lemma route, only the final
gap-7/Case-(a) sub-target changes). The outline correctly avoids the
recorded dead end (re-attacking `T`/`G(β1)` positivity in Case (a) directly,
which round 20 proved is genuinely false there). Both premises checked above
hold up under independent re-derivation, and premise 1 is in fact provable
outright, not just numerically likely — this is a real strengthening over
what the outline itself claims.

Two gaps to flag, both already honestly disclosed by the outliner as open
(not overclaimed), so this is CHANGES-REQUESTED-shaped guidance for the
builder, not a rejection of the outline:

- Step 2a's mechanism ("no valid K,L configuration exists when X0>cos²β0")
  is explicitly marked "TBD by builder" — this is fine for a build-set
  dispatch (it's the actual open content, correctly flagged as such, not
  hidden behind "then it follows"), but the builder must not claim closure
  of 2a from the single round-20 witness alone; it needs either (i) a
  witness-independent algebraic argument, or (ii) if numeric-only evidence
  is all that's found this round, it must stay `partial`, not `solved`.
- Step 2b's claimed reduction ("(II) vacuous ⇒ target collapses to
  f(β1)>0 alone") is plausible given (I)/(II)'s structure in
  `coordinate-bash-resultant-boundary.md` §15 (I is the sole active
  hypothesis-conditional when (II)'s hypothesis set is empty), but the
  outline does not yet show that (I) is exactly equivalent to `f(β1)>0`
  (as opposed to some other still-unproved trig fact) — this identification
  itself is unverified and must be shown by direct term-matching before it
  can be cited, not asserted by analogy to the already-proved
  `f-positive-on-full-interval.md`.

Both gaps are correctly scoped as open work, not sloppy hand-waving —
approved for build with the above two items flagged for the builder.

**Verdict: APPROVE (build).**

### `spiral-similarity-bootstrap` (revise)

Right technique (directed-angle inscribed-angle criterion, standard and
already in use elsewhere in this file for criterion `(∗)`). Step 1's new
lemma is checked and sound (see above). Steps 2-3 are open — the outline is
honest that "step 2 is not yet derived by any round in this exact form" and
that step 3's identity is "entirely open." This is a legitimate, concretely
scoped next attempt (not a rehash of the exhausted H1-only relabeling sweep,
which the outline correctly instructs the builder to avoid). No circular
step: criterion `(∗)` at vertex A is logically equivalent to concyclicity,
a standard fact correctly cited to knowledge_base.md's inscribed-angle
criterion.

**Verdict: APPROVE (build).**

### `ptolemy-trig-identity` (advance, deprioritized, no build slot)

Correctly not building this round; the outline's reasoning (no new lever
found this round, the coordinate route's gap-7 is a higher-value single
remaining-gap target) is sound. No objection to leaving it out of the build
set.

## Diversity check

The build set (pointwise-tangent, spiral-similarity-bootstrap) is
genuinely diverse in framing — one is the coordinate/resultant/algebraic
route hunting its single remaining gap, the other is a synthetic
directed-angle route on an entirely different reduction (`A,K,L,Q`
concyclic). They do not share a wall; good balance per CLAUDE.md's
diversity guidance. `ptolemy-trig-identity` (a third, also-distinct
Ptolemy/sextic framing) remains alive in the population at lower Elo but is
correctly not competing for a build slot this round given no new lever was
found for it.

No evidence of a shared-gap plateau across the two build-set approaches —
their gaps (Case (a) reachability/reduction vs. the A-vertex angle
identity) are structurally unrelated.

## Ranking

Registered: no new slugs this round (both `coordinate-bash-resultant-
boundary-pointwise-tangent` and `spiral-similarity-bootstrap` are already in
the population). Ran `update_ranking` anchoring the two build-set
approaches against the deprioritized `ptolemy-trig-identity` and against
sibling `coordinate-bash-resultant-boundary-pointwise-tangent-via-T`
(cross-check-only, not driving progress this round):
`pointwise-tangent` beats `ptolemy-trig-identity`, `spiral-similarity-
bootstrap`, and `pointwise-tangent-via-T`; `spiral-similarity-bootstrap`
and `pointwise-tangent-via-T` both beat `ptolemy-trig-identity`. This
reflects `pointwise-tangent`'s standing as the closest-to-solved route
(single remaining precisely-diagnosed gap) and clears the `stale` flags set
since round 20.

build set: coordinate-bash-resultant-boundary-pointwise-tangent, spiral-similarity-bootstrap
