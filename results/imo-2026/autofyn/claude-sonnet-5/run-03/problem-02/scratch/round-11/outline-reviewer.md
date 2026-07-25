# Outline review — imo-2026-02, round 11

## Independent verification performed

Before ranking, I independently re-derived (own `numpy`/`scipy` scripts, not
the outliner's/builders' code) the two central numeric claims underlying
this round's whole build set:

1. **The pinned corner point.** Using the file's own closed forms
   (`K_c=2\sin A\sin(A+B)`, `P,Q,f(\beta),G(\beta)`, `\beta_0=(\pi-A)/3`,
   `X_0=\sin B\cos A/(2\sin(A+B))`, `\mathrm{RHS}=(1+\cos B)\cos\beta_0-
   \sin\beta_0 G(\beta_0)`), a fresh `scipy.differential_evolution` global
   search over the Case-(b) domain finds the infimum of
   `(1+\cos B)^2X_0-\mathrm{RHS}^2` is `2\times10^{-16}` (i.e. exactly `0`
   to machine precision), attained at `A^*\approx0.406378,
   B^*\approx0.911738` — matches the outline's reported corner to 5+ digits.
   A 200,000-sample restricted sweep of the true Case-(b) domain found
   `0` violations, min slack `\approx0.0073`, consistent.
2. **The "simultaneous system, not a single curve" claim.** Scanning `A`
   along the raw curve `B=(\pi-A)/3` (i.e. `\gamma=\beta_0`), `G(\beta_0(A))`
   changes sign exactly once at `A\approx0.4061`-`0.4064` (matching `A^*`),
   and the target slack changes sign at the *same* point — confirming the
   corner genuinely is the joint solution of `\{B=(\pi-A)/3,\,
   G(\beta_0(A))=0\}`. I found a second apparent sign change further along
   the same raw curve near `A\approx1.108`; checking domain membership
   directly (scanning both `B`-directions near that `A`) shows the true
   Case-(b) domain has **no valid interior points** anywhere nearby — this
   second "sign change" is exactly the artifact the outline already warned
   about (evaluating the boundary curve past where Case (b) actually
   applies), not a second genuine corner. This corroborates, rather than
   contradicts, the outline's uniqueness claim.
3. **The MVT/Lipschitz derivation of `(\star)` itself.** Worked through the
   chain by hand: `G(\beta_1)\ge G(\beta_0)-(1+\cos B)(\beta_1-\beta_0)`
   combined with `\beta_1-\beta_0\le(\cos\beta_0-\cos\beta_1)/\sin\beta_0`
   gives, after multiplying by `\sin\beta_0>0`, exactly the file's
   `\mathrm{RHS}\le(1+\cos B)\cos\beta_1` reduction and, on squaring in the
   `\mathrm{RHS}>0` case (valid since both sides are then nonnegative,
   `\cos\beta_1=\sqrt{X_0}\ge0`), exactly `(\star)`. No gap found in this
   reduction; it is sound.

No independent check was made this round of the restricted `P>0\wedge E<0`
sign-combination sweep for `coordinate-bash-resultant-boundary` (Step 2 of
its outline) since that check is explicitly *this round's own new work*, not
yet performed by anyone — nothing to verify yet; the plan to restrict the
existing certified `q_1,r_0` closed forms to the exact `P>0\wedge E<0`
region (rather than reuse the full-domain 1.5M/2M-sample census) is a valid,
previously-unperformed check, cheap, and correctly scoped.

## Per-approach verdicts

### `coordinate-bash-resultant-boundary-pointwise` (revise) — APPROVE
The inherited backbone and `(\star)` reduction are independently
re-verified sound (above). The new Step 2 (Hessian check before committing
to a Taylor expansion) is a sensible gating step, correctly sequenced before
Step 3 — the outline does not assume PSD without checking, and explicitly
provides a fallback (Step 4, tangent-line) if the check fails. This is a
genuinely different mechanism from what has already been tried (MVT/
Lipschitz produced `(\star)`; the naive domain-width bound was already
refuted round 10) and is not a repeat of any recorded dead end. Sound
skeleton, correctly scoped, no fatal flaw.

### `coordinate-bash-resultant-boundary-pointwise-sos` (copy) — APPROVE
Legitimate second mechanism (polynomial-ring/SOS, global, no case split) on
the same verified target. Correctly distinguishes the new triple-angle
substitution (`\cos(A/3),\sin(A/3)`) from the `\tan(\beta/2)` substitution
that stalled in round 10 — a genuine, not cosmetic, methodological change.
Appropriately hedges: flags that whether `P(x,B)` even reduces to a clean
polynomial after squaring is itself unverified and must be checked before
the SOS machinery can run; a fallback (numeric Gram-matrix fit) is named
for when symbolic factoring stalls. I wrote the approach file's body this
round (source didn't yet have a copy body) directly from the outliner's
detailed skeleton, keeping the same open-gap disclosures.

### `coordinate-bash-resultant-boundary-pointwise-tangent` (copy) — APPROVE
Legitimate third mechanism (tangent-line trick, crux `aimo-0005` adapted,
local/algebraic) on the same verified target. Correctly identifies the two
candidate linearization targets (`X_0` vs `\cos^2\beta_0`) as an open choice
rather than presupposing one works, and explicitly names the exact failure
mode to avoid (a bound one-sided only locally, the same mode that already
killed the cruder domain-width bound) — this is the right adversarial
posture for a construction whose entire value depends on genuine global
one-sidedness, not just a local Taylor match at the corner. Also wrote this
file's body this round from the outliner's skeleton.

### `coordinate-bash-resultant-boundary` (advance) — APPROVE
The new Step 2 (restrict the sign-combination sweep to the true
`P>0\wedge E<0` sub-region, rather than reusing the full-domain census) is a
cheap, well-scoped, previously-unperformed check that correctly does not
reuse stale full-domain statistics as if they already answered the
restricted question. Both outcomes (sign-definite combination found, or
genuinely restricted-but-still-negative) are honestly planned for in the
outline (Steps 3a/3b) — no risk of overclaiming built in.

## Diversity / shared-gap-plateau assessment (flagged per CLAUDE.md)

All four build-set entries are, as the outliner itself states, variations on
closing one of two live sub-targets (`(\star)` for the three
`-pointwise*` siblings, or the narrower `T\ge0` restricted sub-case for
`coordinate-bash-resultant-boundary`) of the single remaining shared
branch-selection gap. This is a genuine, long-standing (10+ round) plateau.
It is *justified* rather than a same-framing rubber-stamp this round because:
(a) four independent top-level-framing searches (rounds 3, 5, 8, 10) found no
alternative route to the whole problem, a fact I have no reason to doubt
given the depth of the prior rounds' documented negative results
(fixed-point-concyclic, inversion-at-A, ptolemy all independently converged
onto the identical algebraic object per round 7-8's structural-equivalence
theorem); and (b) the three `(\star)`-attacking mechanisms genuinely differ
in kind — analytic/local (width-expansion), algebraic/global (SOS), and
algebraic/local-pinned (tangent-line) — so a wall hit by one is not
automatically hit by the others. That said: if none of the three closes
`(\star)` again next round, this is a strong signal the plateau is now
about `(\star)` specifically (not merely "branch selection" abstractly), and
CLAUDE.md's guidance to seek a framing genuinely far from the coordinate/
rotation-parametrization route (untried since round 8's negative results on
fixed-point-concyclic/inversion/Ptolemy) should be revisited by an explorer,
not just another mechanism on `(\star)`.

## Ranking

Registered the two new copies (`-sos`, `-tangent`) via `copy_approach`
(inheriting the source's Elo/counts, as intended — no birth nudge). Ranked
the whole sampled field head-to-head, anchoring newcomers against
established siblings using this round's independent verification as
evidence: `coordinate-bash-resultant-boundary` (established, three sub-cases
concretely closed by hand) edges its `-pointwise` sibling in a draw-leaning
comparison (both "advanced" last round, complementary scope — `(\star)` is
strictly more general per current.md's own cross-pollination analysis, but
neither is closed, so treated as a draw); both established siblings beat the
brand-new, as-yet-untried `-sos`/`-tangent` copies (no concrete progress yet
on their own new mechanisms) and beat the long-dormant `fixed-point-
concyclic`/`ptolemy-trig-identity`/`power-of-point-secants`/`inversion-at-A-
collinearity` (all last touched rounds 1, 7, or 8, with `inversion-at-A`
a confirmed dead-end for this problem). `-sos` vs `-tangent`: drawn (twins,
no differentiating evidence yet).

## Build set

All four dispatched approaches are sound, non-redundant (given the
justified plateau above), and free of fatal flaws. No RETHINK this round.

build set: coordinate-bash-resultant-boundary-pointwise, coordinate-bash-resultant-boundary-pointwise-sos, coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary
