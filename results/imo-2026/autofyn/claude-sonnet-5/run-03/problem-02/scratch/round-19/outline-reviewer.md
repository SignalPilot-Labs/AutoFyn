# Outline review — round 19, imo-2026-02

## Independent re-derivations performed (fresh sympy/numpy sessions, not reusing outliner's/explorers' scripts)

1. **f'(β) claim.** Built `f(β)=Kc+P sinβ+Q cosβ` from the raw definitions
   `P=½sin(A−B)+3/2 sin(A+B)`, `Q=−sinA sinB`, `Kc=2sinA sin(A+B)` in a
   fresh sympy session, differentiated, and confirmed exactly (zero
   residual) `f'(β)=sin(A+β)cosB+sin(A+B−β)`. Then re-read
   `lemmas/claim-I-closed-and-claim-II-caseA-closed.md`'s Theorem A *proof*
   text directly (not just its headline statement): the sign argument used
   — `cosB>0` (from `B<π/2`), `sin(A+β)>0` (from `A+β∈(0,A+B)⊂(0,π)`),
   `sin(A+B−β)>0` (from `A+B−β∈(A,A+B)⊂(0,π)`) — uses only `β∈(0,γ)=(0,B)`
   nowhere invoking `β>β0`. **Confirmed: this is genuinely a proof of
   `f'>0` on the whole `(0,γ)`, load-bearing, not a misreading.** The
   theorem's *stated conclusion* is narrower (`(β0,γ)`) only because of how
   it happens to be invoked downstream in Theorem A's own write-up
   (`f(β)>f(β0)>0` for `β>β0`), not a limitation of the derivative proof
   itself. This is exactly what the outline and both explorers claim —
   verified true, not an overclaim.

2. **`f(0)=sinA(2sinC−sinB)≥0`, via `sinB≤sinC` for `B≤C`.** Independently
   simplified `f(0)=Kc+Q` and confirmed exactly `f(0)=sinA(2sin(A+B)−sinB)`
   (zero residual), which equals `sinA(2sinC−sinB)` after `C=π−A−B`. Ran a
   fresh 3,000,000-sample sweep over genuine triangles with `B≤C` enforced
   by construction (not reusing the explorers' domain code): **zero
   violations** of `sinB≤sinC`, minimum margin `sinC−sinB≈1.2e-8`
   (vanishing only in the fully degenerate limit). Checked the specific
   edge cases requested:
   - `A→0` (nearly degenerate, `B,C→π/2`): `sinB,sinC` both `→1`, no
     violation, consistent with equality only in the limit.
   - `C=π/2` exactly: falls cleanly into Case 1 (`C≤π/2`) of the two-case
     proof, `sinB=0.9553<sinC=1`, correct.
   - `B=C` (isosceles): `sinB=sinC` exactly, correctly captured as the
     equality case of Case 1's monotonicity argument.
   - `C` near `π` (`B` tiny, very obtuse `C`): falls into Case 2
     (`C>π/2`), `sinB=0.001<sinC=0.011`, correct, no issue with the
     reflection argument `π−C<π/2`, `B<π−C`.
   The two-case proof itself is elementary and gap-free: **Case `C≤π/2`**
   gives `B≤C≤π/2` directly (sin increasing on `[0,π/2]`); **Case `C>π/2`**
   uses `π−C<π/2` and `B=π−A−C<π−C` (since `A>0`), placing both `B,π−C` in
   `(0,π/2)` with `B<π−C`, so `sinB<sin(π−C)=sinC`. Both cases are fully
   written out (not just the easy one), and I could not find a gap or
   missed sub-case. **Confirmed: this is a complete, gap-free elementary
   proof of `sinB≤sinC`, hence of `f(0)≥sinA·sinC>0` strictly.** This is
   exactly the kind of "looks obviously right" claim that burned rounds 17
   and 18 (a wrong-scope citation, an unproved 6-round-old coincidence) —
   here, unlike those, the claim is genuinely elementary and checks out
   under direct symbolic + numeric + edge-case scrutiny, not a hidden
   citation of unproved machinery.

3. **Domain containment (`β1∈(0,β0(A)]⊂(0,γ)`).** Re-read Step 2 of the
   "Full proof" in `coordinate-bash-resultant-boundary-pointwise-tangent.md`
   directly: `β1` is *defined* there as "the unique angle with
   `cosβ1=√X0(A,B)`, `β1∈(0,γ)`" — i.e. `β1∈(0,γ)` is already established
   **before** the Case (a)/(b) split; Case (a) merely additionally requires
   `β1≤β0(A)`. So the outline's proposed step 7 (checking containment) is
   in fact automatic/trivial given the existing Step 2 definition, not a
   new obligation — a minor simplification the builder can note, not a gap.

4. **Which sub-argument the outliner chose.** Compared gap7a's `sinB≤sinC`
   argument (fully general, no case split on `A`, no numeric residual)
   against gap7b's Opening 1 (`term1+term2` split, closes only `A≤π/3`
   algebraically, leaves `A>π/3` numeric-only per the explorer's own
   report) and Opening 2 (no-interior-critical-point argument, explicitly
   left unfinished — "sketched, not completed" per the explorer). **The
   outliner's rejection of gap7b's weaker sub-arguments in favor of
   gap7a's full-domain one is correct** — gap7a's lemma genuinely covers
   the entire triangle domain with no residual case, and is logically
   independent of (does not need) gap7b's `A≤π/3` split at all. Gap7b's
   Opening 3 (confirming Theorem B's `β0`-anchor casework does not
   transfer to `β=0`) is a useful negative result correctly folded into the
   outline's "watch out for" section, not silently dropped.

## Verdicts

### `coordinate-bash-resultant-boundary-pointwise-tangent` — APPROVE

This is a whole-problem attempt (Steps 1–5 target `OM=ON` end to end via
the already-certified chain plus the newly-outlined Step 3 fix), not a
sub-lemma fragment. Both load-bearing new facts (extended-scope `f'>0`,
and `sinB≤sinC`) independently verified above, gap-free. The skeleton
(Theorem A′ extension + continuity + MVT-corollary monotonicity + `f(0)`
evaluation + combine) is logically sound, no circularity, no hidden
citation of unproved material — a real improvement over rounds 17/18's
false-solve patterns, since here the mechanism is genuinely elementary and
checks out under scrutiny rather than resting on a numeric coincidence or
a wrong-interval citation. One thing to flag for the builder, not a
blocking gap: the outline's own "Watch out for" list already includes the
correct instruction — after Step 3 is spliced in, run the SAME full
dependency-chain audit discipline that caught gaps 6 and 7 before claiming
`solved` (this will be the third time this exact route reaches for
`solved`; the first two were each caught by a careful audit — the
population's per-role rules already flag this, reiterate it strongly to
the builder). No changes requested to the outline itself.

### `spiral-similarity-bootstrap` — APPROVE

Genuinely different framing (pure directed-angle synthetic route, no
coordinate/resultant/SOS machinery) — real diversity value per CLAUDE.md,
independent of whether it reaches a solve this round. Step 1 (Lemmas A, B,
Corollary) is already certified from round 18. Step 2 (the
`MN∥BC`-based linear-functional reduction of `OM=ON`) is elementary and
correctly flagged as "already implicit in the file, now made explicit,"
not overclaimed as new. Step 3 (Extended Law of Sines parametrization of
`O`'s projection, checking `φ`-cancellation) is honestly presented as an
open gap, not yet attempted anywhere — appropriately scoped as the
concrete next target, with a clear mechanism (not a bare "then it
follows"). The outline correctly declines to reopen the `-pointwise-sos`
sibling's diagnostics (per the diversity explorer's witness-dependence
finding) and correctly retires three dead-end product-identity
candidates (items 3–5 of the diversity explorer). The approach's own
"Open gap 2" (containment/sign-convention assumption, numeric-only) is
correctly left flagged as a separate, still-open gap, not silently
assumed proved in the new step.

## Diversity check

The field remains genuinely diverse: `-pointwise-tangent` is
coordinate/resultant/MVT machinery; `spiral-similarity-bootstrap` is pure
synthetic directed-angle chasing with zero coordinate elimination. No
shared-gap-plateau concern this round — if anything, `-pointwise-tangent`
is one clean step from a full solve via a route now independently
double-verified elementary, while `spiral-similarity-bootstrap` provides
real insurance diversity per CLAUDE.md's standing guidance. No RETHINK
needed on either.

## Ranking

Both slugs already registered from prior rounds; no new slugs to register
this round (no `copy_approach` needed — the outliner made no branch
request).

build set: coordinate-bash-resultant-boundary-pointwise-tangent, spiral-similarity-bootstrap
