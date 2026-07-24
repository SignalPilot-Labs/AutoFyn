# Outline review — imo-2026-02, round 4

## Independent verification performed before review

The centerpiece of `coordinate-trig-bash: revise` is a brand-new claimed
identity from `math-explorer-substitution.md`: that the branch-independent
polynomial identity `T = quo1·Q2 + quo2·Q1` holds, where `Q1(R2)`, `Q2(R1)`
are trig-ceva-chase's Lemma T1 quadratics and `T := 2[Nx-(p/2)D]` is the
denominator-cleared circumcenter-x target. Per standing rule ("always
independently re-derive a fresh headline numerical/symbolic claim before
approving it as centerpiece"), I rebuilt this **entirely from scratch** in a
fresh sympy script (own hinge construction, not copy-pasted from either the
explorer's or trig-ceva-chase's code):

- Built `Q2(R1)` from hinges `(M,B-M)` and `(C,d2(θ))`, moving point `K(R1)`;
  `Q1(R2)` from hinges `(B,d1(θ))` and `(N,C-N)`, moving point `L(R2)` — both
  degree exactly 2, matching Lemma T1's certified statement.
- Built `T` via the standard circumcenter-numerator/denominator formula,
  keeping `cosθ,sinθ` as free symbols (no Pythagorean identity used).
- Polynomial-divided `T` by `Q2` in `R1`, then the remainder by `Q1` in `R2`:
  **final remainder is identically 0** (confirmed by `sympy.expand`).
- Checked non-vacuity: `T`, `Q1`, `Q2` are all nonzero at a generic
  (non-root) point — the vanishing is not degenerate/trivial.
- Numerically instantiated at `(p,q,θ)=(0.3,1.7,0.35)`: got the *same* root
  values as the explorer's report (`R1≈0.3362,1.0421`; `R2≈0.2676,1.1107`),
  and `T=0` (to `~1e-14`, floating-point noise) for **all four** root
  combinations.

**Conclusion: the explorer's claim is CONFIRMED, independently, from a
from-scratch construction.** This is a genuinely valid, branch-independent
closing mechanism: since the implication `F_i=0 ⟹ Q_i=0` only needs the
*easy* direction (exact unsigned angle equality is one of the two cases
covered by "equal mod π"; the branch-selection ambiguity flagged in
`lemmas/angle-matching-ray-quadratic.md`'s caveat only concerns the *other*,
harder direction, which this route never invokes), chaining: certified
existence/uniqueness (`lemmas/existence-uniqueness-r1-r2.md`) gives a real
`(r1*,r2*)` with `F1=F2=0` ⟹ `Q1(R2*)=Q2(R1*)=0` ⟹ (by the now-confirmed
identity) `T=0` ⟹ `O_x=p/2` (given `D≠0`). This is airtight logic, not
hand-waving, contingent only on gap (b) below.

## Approach-by-approach verdicts

### coordinate-trig-bash (revise) — **APPROVE** (build, top priority)

- Steps 1-2 (import existence/uniqueness, decoupling) — already certified,
  correctly cited, not re-derived (good practice).
- Step 3 (the "only if" direction of Lemma T1) — logically trivial and
  correctly identified as sidestepping the branch-selection caveat. Verified
  above that this direction indeed requires nothing more than "exact
  equality ⟹ equality mod π."
- Step 4 (the polynomial identity) — **independently reverified from
  scratch above; confirmed correct and non-vacuous.**
- Step 5 (conclusion) — valid chaining, contingent on step 6.
- **Step 6 (D≠0 nondegeneracy) is a real, currently open gap, correctly
  flagged as such in the outline** — not yet addressed by any approach. This
  is not hand-waving (the outline explicitly calls it out and gives a
  candidate argument sketch), but it must actually be closed by the builder,
  not asserted as "generic." Suggest to the builder: since `K` is a fixed
  interior point of the *open* region `triangle BMC` and `L` of the open
  region `triangle BNC` for every `θ` in the domain, and these regions are
  disjoint from the *line* `AK`/`AL` except at isolated crossing points,
  a continuity/isolated-zero argument on `θ↦D(θ)` (a real-analytic function
  of `θ` on a connected open interval, not identically zero since it isn't
  zero generically) plus checking it doesn't vanish at the domain endpoints
  should suffice — but this must be written out, not left as "should follow."
- Also flag as a build condition (not a fatal issue): the certificate
  `quo1, quo2` must be presented explicitly and hand-checkably (per rigor
  rules — a "sympy said so" black box is not acceptable as final proof text,
  even though it is legitimate to *use* CAS for a symbolic derivation, the
  written proof must give the reader a way to verify it, e.g. by explicit
  coefficient listing or a stated evaluation-at-sample-points check).

This is now the single strongest lead in the whole run and should be the
round's top priority.

### antipode-perp-bisector (revise) — **CHANGES REQUESTED** (build, second priority)

- Steps 1-2 (import, classical isosceles-circumcenter fact) — sound, correct
  citation of a standard fact, 2-line proof given.
- Step 3 (new unsigned trichotomy L1'/L2') — this correctly fixes round 3's
  root cause (an unjustified/incorrect directed-angle sign step) by moving
  to unsigned angles with an explicit, checkable case-split on
  `sign(θ+90°-γ)` (resp. `β`) instead of an asserted-by-symmetry sign
  convention. This is a genuine, structural fix, not a cosmetic one — approve
  this reformulation.
- Step 4 (isogonal-conjugate reformulation) — **this is honestly labeled a
  "lead," not a proof step** ("If this isogonality can be derived directly
  from hypotheses ... not yet found — flagged as the key remaining
  mechanism to search for"). This is an acceptable open-gap disclosure per
  standing rule (explicit "not yet found" ≠ circular reasoning), but the
  builder must not let step 5's case-combination be contingent on step 4
  succeeding — L1'/L2' themselves (not just the isogonal packaging) are the
  actual load-bearing lemma still needed, and no mechanism for either is in
  hand yet. **Change requested:** treat step 4 as one candidate attack, not
  a guaranteed unlock; if the isogonal mechanism doesn't pan out quickly,
  the builder should still attempt L1'/L2' directly (e.g. via the law of
  sines in the appropriate sub-triangle at B combined with the ∠AKA*=90°
  Thales fact already certified) rather than stalling on step 4.
- Cases (2×2 sign combinations + boundary) are explicitly enumerated —
  good, satisfies the casework-completeness check.
- No re-attempt of any refuted mechanism (270° identity, spiral similarity,
  tangency/secant) — confirmed clean.

Worth keeping in the build set as the structurally independent backstop in
case coordinate-trig-bash's D≠0 gap proves harder than expected, and because
L1/L2's mechanism (once found) would give a second, independent full proof.

### inversive-swap-line (new) — registered, **not built this round**

- The outline itself correctly stages this as reconnaissance: step 3 (the
  cheap-kill check, "does `∠σ(K)Aσ(L)` reduce cheaply to `∠KAL` expressible
  from the three hypotheses?") is explicitly unresolved, and the outline
  instructs to do this FIRST before further development. This is honest and
  appropriately scoped — not fatal (RETHINK), just not yet actionable as a
  build item (no proof skeleton exists past step 2, only classical/general
  facts independent of the hypotheses).
- Given `coordinate-trig-bash` is now within one nondegeneracy lemma of a
  full solve, and builder bandwidth should concentrate there this round, I
  am registering this approach into the population (so it isn't lost) but
  **not** including it in this round's build set. If the top two approaches
  stall next round, this is the natural diversification pick.

### trig-ceva-chase — no action (lemma provider only), confirmed correct role

Its Lemma T1 is exactly the tool now driving `coordinate-trig-bash`'s
breakthrough step. No further building needed on the approach itself this
round; its earlier "not a bypass on its own terms" finding is correctly
reconciled in the outline (it wasn't a bypass alone, but combined with the
new identity it is now the key ingredient of a different, working
combination) — no confusion here, correctly explained.

### labeling-duality — no action (dormant), correctly deprioritized

Confirmed algebraically equivalent to `coordinate-trig-bash`'s gap; correctly
left dormant. If `coordinate-trig-bash` closes, this closes automatically —
no need for a separate build slot.

### complex-circle-power, nine-point-link — untouched, no action needed

Not referenced in this round's outline; correctly left low-priority/dormant,
consistent with round 3's assessment (likely same-wall collapse).

### two-step-spiral-chain — confirmed dead-end, not revisited (correct)

## Diversity assessment

The field currently has one approach (`coordinate-trig-bash`) that appears
close to a genuine full closure via a route (branch-independent polynomial
certificate) that is *not* shared by `antipode-perp-bisector`'s target
(`A*B=A*C` via unsigned angle trichotomy) — these two remain structurally
independent, satisfying CLAUDE.md's anti-single-framing concern. `labeling-
duality`/`trig-ceva-chase` are confirmed to reduce to the same wall as
`coordinate-trig-bash` (not independent, correctly kept dormant/support-role
rather than double-counted as diversity). `inversive-swap-line` remains the
reserve diversification pick if needed. No plateau risk this round — real,
verified progress on the sharpest gap in the whole run.

## Ranking

Registered `inversive-swap-line` (new). Ranked the whole field via
`update_ranking`: `coordinate-trig-bash` now clearly best (advanced this
round, closest to full closure, independently re-verified centerpiece claim),
`antipode-perp-bisector` second (real structural fix, live open gap),
`labeling-duality` third (dormant but more developed than the untouched
approaches), `trig-ceva-chase` fourth (support role, no further gap-closing
progress of its own), `inversive-swap-line` above the fully-untouched
`nine-point-link`/`complex-circle-power` (has at least classical-fact
groundwork laid), those two drawn (both equally undeveloped), and
`two-step-spiral-chain` last (confirmed dead-end).

## Rules learned this round (for /tmp/memory/outline-reviewer.md)

- Confirms standing rule: independently re-deriving a fresh headline claim
  (this round: the branch-independent polynomial certificate) from scratch,
  not just re-running the explorer's script, caught nothing wrong this time
  but is exactly the right level of scrutiny for a claim this load-bearing —
  worth the ~15 minutes.

build set: coordinate-trig-bash, antipode-perp-bisector
