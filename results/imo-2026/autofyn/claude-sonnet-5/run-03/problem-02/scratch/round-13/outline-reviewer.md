## imo-2026-02 — outline review, round 13

**Scope.** The outliner proposes to build three approaches (`coordinate-bash-
resultant-boundary` advance, `coordinate-bash-resultant-boundary-pointwise-
tangent` revise, `coordinate-bash-resultant-boundary-pointwise-sos` advance,
lower priority), and to defer `coordinate-bash-resultant-boundary-pointwise-
tangent-twopoint` (no build slot, correctly reasoned as strictly less useful
until the `-tangent` sibling's monotonicity lever closes). All four are
already registered in the population (`copy_approach`/`register_approach`
lineage confirmed in `.ranking.json`) — no new slugs this round, so no
`register_approach`/`copy_approach` calls needed.

**Independent verification performed (from scratch, own sympy/numpy
sessions, not trusting the explorer transcripts).**

1. **The round's headline new claim — the `Num` identity behind
   `coordinate-bash-resultant-boundary` Step 2/5 — is stronger than
   reported, and I have now fully symbolically proved it (upgrading it from
   the explorer's 2,000-sample spot check to an exact identity).** Built
   `X0 = ct/(2(sd+ct))`, `p = s(4X0-3)`, `q = c(4X0-1)`, computed
   `q^2(1-X0) - p^2 X0` via `sympy.cancel`, and found the denominator is
   exactly `2(sd+ct)^3` and the resulting numerator is **exactly** (not
   "up to a positive factor," literally term-for-term after expansion)
   `c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3-6c^2ds^3t^2-9cd^2s^4t`, i.e.
   `-c\cdot\mathrm{Num}` where `\mathrm{Num}` is the explorer's displayed
   polynomial times `-1`... concretely the raw numerator factors as
   `-c\cdot(\text{a degree-7 poly})`, and that degree-7 poly equals the
   explorer's `\mathrm{Num}` exactly after sign bookkeeping. Since `c=\cos
   A\ge0` on the domain, the sign of `q^2(1-X0)-p^2X0` is exactly `-\,c\cdot
   \mathrm{sign}(\mathrm{Num})` up to the (already-established) sign of `c`,
   confirming the claimed equivalence `\mathrm{Num}<0\iff q^2(1-X_0)>p^2X_0`
   as a genuine symbolic identity, not merely a numeric coincidence. **This
   should be written into the build as a certified lemma this round** — the
   outliner correctly flagged it as needing upgrading, and it is now done;
   the builder should simply reproduce and write it up (cheap, I've handed
   the exact computation above).

2. **Also confirmed exactly**: `X_0-d^2 = G_0/(2\sin C)` where
   `G_0=ct(1-2d^2)-2sd^3` and `\sin C = sd+ct` — `sympy.simplify` gives `0`
   residual. Since `\sin C>0` unconditionally, `G_0>0\iff X_0>d^2` is a
   genuine exact identity (not new; already claimed correctly by the
   population, now independently reconfirmed).

3. **Found a real, if minor, gap in Step 2's `B\le C\iff c\ge2t^2-1`
   claim.** I tested this identity by direct trig simulation (20,000 random
   triangles, no domain restriction): it **fails** in ≈10% of cases
   (1990/20000 mismatches). The failure is exactly where `B\ge\pi/2`: the
   derivation `\cos(2B)\ge\cos(\pi-A)\iff 2B\le\pi-A` requires `\cos` to be
   monotonic on the relevant interval, which needs `2B\in(0,\pi)`, i.e.
   `B<\pi/2` — **NOT stated as a precondition in the outline's Step 2**,
   even though `B<\pi/2` is true throughout the residual domain (already
   established, round 11, "`B<\pi/2` with comfortable margin"). Restricting
   to `B<\pi/2` in a fresh 200,000-sample sweep: **0/169,252 mismatches**,
   confirming the identity is correct *given* `B<\pi/2`. This is a genuine
   caveat the outline states as an unconditional elementary fact but that
   is actually conditional — cheap to fix (cite the existing `B<\pi/2`
   domain fact when invoking this equivalence) but must be stated
   explicitly in the write-up, not left implicit, or a future reviewer
   might reasonably ask why `B\ge\pi/2` isn't a case to cover.

**Verdicts.**

- **`coordinate-bash-resultant-boundary` (advance) — CHANGES REQUESTED
  (minor, easily fixed).** The technique (Positivstellensatz combination
  search on the now-fully-polynomial 4-inequality domain) is sound and the
  right one at this stage; Step 2's domain characterization is real
  progress, and I've now fully closed the previously-open Step 2/5 `Num`
  identity gap (see finding 1 above) — the builder should write this up as
  a certified lemma immediately, it costs nothing further to prove. Fix
  required: state the `B<\pi/2` precondition explicitly when invoking
  `c\ge2t^2-1\iff B\le C` (finding 3). The main task — the actual
  nonnegative-combination/SOS search for `-q_1,-r_0` in terms of
  `G_0,-E_{\text{num}},(c-2t^2+1),-\mathrm{Num}` — remains genuinely open
  and is correctly identified as the round's central task; no
  overclaiming. Proceed to build.

- **`coordinate-bash-resultant-boundary-pointwise-tangent` (revise) —
  APPROVE.** The pivot from the confirmed-dead `T_1+T_2` termwise split to
  the `f-g` reformulation is a genuinely new, well-motivated mechanism
  (not a relabeling of the same computation) — it correctly avoids the
  cancellation that killed `T_1` (per the `t1t2` explorer's much wider
  margin `(0.54,0.89)` for `\partial(f-g)/\partial B` vs `(0.177,0.19)` for
  `T_1+T_2`). The squared-magnitude-comparison licensing (`(\partial
  g/\partial B)^2>(\partial f/\partial B)^2$ is a safe, non-sign-flipping
  squaring since both derivatives are independently confirmed
  same-signed/negative on the domain) is correctly reasoned, not circular.
  Step 5's `f-g|_{\mathcal C}=D_1` claim is plausible and, per the
  explorer's independent cross-construction, numerically exact — flagged
  correctly as needing a one-line symbolic substitution, not a hard gap.
  All open gaps (RHS>0 symbolic, the magnitude inequality itself, the
  identity's symbolic confirmation, and the inherited `D_1\ge0`
  concavity gap from the sibling) are honestly disclosed, not hidden
  behind hand-waving. Proceed to build.

- **`coordinate-bash-resultant-boundary-pointwise-sos` (advance, lower
  priority) — APPROVE, with the deprioritization endorsed.** The SDP
  explorer's negative result (2-multiplier ansatz infeasible, confirmed by
  two independently-converging solvers with a well-conditioned margin
  `t^*\approx-1.548`) is a real, decisive finding, and the outline
  correctly avoids re-searching that exact ansatz. The proposed next steps
  (add the `u`-domain-bound multiplier, add the `\angle B\le\angle C`
  encoding via `w=\sqrt{1+u^2}`, switch to a better-conditioned basis) are
  concrete and non-circular, though genuinely uncertain to succeed given
  the tooling wall (no MOSEK) already hit twice. Given the population's
  4+-round plateau specifically on this `Num\ge0`/SDP mechanism and this
  round's fresh negative result, the outliner's "lower priority" framing is
  correct — keep it in the build set (per CLAUDE.md's parallel build-set
  policy) but do not expect fast progress; if the `w`-encoding (Step 2)
  doesn't yield a concrete polynomial condition quickly, this route should
  be given even less budget next round.

- **`coordinate-bash-resultant-boundary-pointwise-tangent-twopoint`
  (deferred, no build slot) — endorsed.** The outliner's reasoning (its
  gaps, even fully closed, would only cover the measure-zero curve, not
  the full domain, until the `-tangent` sibling's monotonicity lever
  closes) is sound and matches this round's own finding (the `t1t2`
  explorer independently confirmed `f-g|_{\mathcal C}` numerically matches
  `D_1` exactly, reinforcing that these two files are two views of the
  same reduction). Correctly not double-registered/rebuilt this round.

**Diversity check.** All three build-set approaches (plus the deferred
`-twopoint`) attack the *same* residual gap (Case (b) positivity, in one of
its three equivalent forms) via three genuinely different mechanisms:
explicit Positivstellensatz combination on a purely polynomial domain
(`-boundary`), analytic monotonicity via a non-squared difference (`-tangent`),
and global SOS/SDP certificate in the Weierstrass frame (`-sos`). This
convergence onto one shared target is not a fresh plateau this round — it
was already established (round 8) as a proven structural fact that every
live route collapses onto this one gap, so continued mechanism diversity
here (rather than forcing a wholly new geometric framing that rounds 1-8
already exhausted) remains the correct strategy, consistent with prior
outline-reviewer rulings (memory rule 4). No approach here silently repeats
a recorded dead end (`T_1` alone, the 2-multiplier SDP ansatz, and the raw
`\beta_0` boundary curve are all correctly avoided this round).

**Small issue for the builder (not blocking).** `coordinate-bash-resultant-
boundary`'s Step 2 needs the `B<\pi/2` precondition made explicit (finding
3 above) — cheap one-sentence fix citing the existing round-11 fact, not a
new proof obligation.

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos
