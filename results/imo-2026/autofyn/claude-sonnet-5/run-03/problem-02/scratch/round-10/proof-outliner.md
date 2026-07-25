## imo-2026-02

### Context (round 10)
Per round-9 adjudication, the *entire* proof chain (every live route: coordinate
rotation-parametrization, fixed-point-concyclic + inversion-at-A, Ptolemy-trig)
now stands or falls on **one shared sub-case**: the `Y(\gamma)<0` branch of
Theorem 16.2 (Claim (II), Case (b)) in `coordinate-bash-resultant-boundary`,
equivalently `G_{2b}`-exclusion / the `(Y,B_2,Z)` three-way sign classification.
This round's `fresh-framing-lens` explorer reconfirmed (antipode/power-of-point
repackaging, spiral similarity, isogonal — all re-checked) that no genuinely new
top-level synthetic framing exists; the algebraic wall is real, not an artifact
of the coordinate route. **No new top-level approach is opened this round.**
Two concrete, independently-verified new levers on the exact same sub-case were
found by this round's explorers and are outlined below as the next moves for
the two approaches that jointly own this gap.

**Load-bearing correction surfaced this round (Yneg-lens):** the round-9 file's
literal statement of Case (b) — `2K-f(\beta_1)\ge0` given only `Y(\gamma)<0` and
domain-nonemptiness — is **FALSE as stated** (35,519/80,555 violations, own
independent 2M-sample sweep). The fix is to restore the implicit hypothesis
`\sin(A+3\beta_1)<0` (equivalently `\beta_1>\beta_0=(\pi-A)/3`, i.e. the Case-(b)
window is itself non-vacuous). With that hypothesis, 0/29,548 independent
violations. This correction must be baked into the target statement before any
builder attacks it further — the uncorrected version would waste a round.

---

coordinate-bash-resultant-boundary: revise
Target: the whole problem's claim (existence/characterization of the fixed
point on the perpendicular bisector of `BC`, per the population's standing
reduction), proved via the rotation-parametrization + Law-of-Sines chain,
Claims (I) and (II) as in `current.md`'s round-9 record.
Technique: direct trigonometric-inequality analysis of the endpoint value
`2K-f(\beta_1)` at the implicitly-defined crossing `\beta_1` (root of
`Y(\beta)=0`), building on the already-certified monotonicity `f'>0` /
`(2K-f)'=-f'<0` (Theorem 16.1, unconditionally closed).
Skeleton:
  1. Restate Case (b)'s target as the corrected **Claim (A′)**: given
     `\cos^2\beta_1 = X_0 := \sin B\cos A/(2\sin(A+B))` (the root of
     `Y(\beta_1)=0`) AND `\sin(A+3\beta_1)<0` (equiv. `\beta_1>\beta_0`, the
     Claim-(I) domain-nonempty threshold), prove
     `G(\beta_1):=2K-f(\beta_1)\ge0`, where
     `K=2\sin A\sin(A+B)`, `f(\beta)=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)`
     — by direct algebra (`G=K+\sin A\sin B\,x-Py`, `x=\cos\beta_1,y=\sin\beta_1`,
     `P=\sin(A-B)/2+\tfrac32\sin(A+B)`, `Q=-\sin A\sin B` from the already-
     certified `f=K+P\sin\beta+Q\cos\beta` decomposition).
  2. **Case split on `\mathrm{sign}(P)`** — by elementary sign inspection.
     - `P\le0`: `G\ge \mathrm{expr}_1:=K+\sin A\sin B\,x>0` trivially, since
       `x=\sqrt{X_0}>0` and `K,\sin A\sin B>0` for genuine triangle angles —
       **fully closed, no further hypothesis needed in this branch** (this is
       a free, cheap sub-closure the outliner is flagging explicitly, not
       merely a placeholder).
     - `P>0`: both `\mathrm{expr}_1,Py>0`; need `\mathrm{expr}_1\ge Py`.
       Square (valid, both sides `\ge0`): reduces to
       `D:=\mathrm{expr}_1^2-P^2(1-x^2)\ge0`, a quadratic in `x` with
       `x=\sqrt{X_0}` substituted in, i.e. `D=E+B_{\mathrm{coef}}\sqrt{X_0}`
       with `E:=A_{\mathrm{coef}}X_0+C_{\mathrm{coef}}` a genuine rational
       function of `A,B` alone (no radicals) — by direct expansion,
       `A_{\mathrm{coef}}=\sin^2A\sin^2B+P^2>0`,
       `B_{\mathrm{coef}}=4\sin^2A\sin B\sin(A+B)>0` (product of positive
       triangle-trig quantities), `C_{\mathrm{coef}}=4\sin^2A\sin^2(A+B)-P^2`.
  3. Sub-split on `\mathrm{sign}(E)` — by inspection.
     - `E\ge0`: `D\ge0` trivially since `B_{\mathrm{coef}}\sqrt{X_0}\ge0` —
       closed. (Numerically dominant, ≈91% of the corrected-domain sample
       space per Yneg-lens — worth a builder attempting a clean symbolic
       proof `E\ge0` as its own sub-lemma; not yet attempted.)
     - `E<0` (the residual ≈9%): reduces, by squaring again (valid since
       both `B_{\mathrm{coef}}\sqrt{X_0}` and `-E` are `\ge0` here), to the
       explicit rational (no-radical) degree-6-in-trig inequality
       `B_{\mathrm{coef}}^2X_0-E^2\ge0`, displayed in full in the Yneg-lens
       report (a single polynomial identity in `\sin A,\cos A,\sin B,\cos B`
       — no longer containing `\beta_1` at all) — the genuine hard core of
       the whole shared gap. THIS is the one true remaining open target.
  4. Conclude Claim (A′), hence Theorem 16.2 in full, hence Claims (I)+(II),
     hence the whole problem — by combining Cases (a) (already closed) and
     (b) (this skeleton).
Key lemmas (claim + mechanism):
  - `P\le0\Rightarrow G(\beta_1)\ge0$ unconditionally — because
    `\mathrm{expr}_1=K+\sin A\sin B\,x>0` always and `-Py\ge0` when `P\le0`
    (both terms of `G` become individually nonnegative).
  - `B_{\mathrm{coef}}=4\sin^2A\sin B\sin(A+B)>0` always — because it is a
    product of manifestly positive trig quantities for genuine triangle
    angles (`\sin A,\sin B,\sin(A+B)\in(0,1]`).
  - Residual target `B_{\mathrm{coef}}^2X_0-E^2\ge0` on `E<0,\;\sin(A+3\beta_1)<0`
    — mechanism not yet found; a Sturm-sequence sign-chart (fix one variable,
    e.g. `A`, treat as a 1-variable polynomial in `\tan(B/2)` or similar) or
    an SOS decomposition via `sympy.polys` is the natural next lever, per
    the sturm-sos-lens explorer's diagnosis that naive `sympy.factor`/
    `simplify` does not close it directly.
Open gaps: the residual `E<0` degree-6 trig inequality (step 3, second
bullet) is the sole remaining unproved step; everything else in this
skeleton (steps 1-2, the `P\le0` and `E\ge0` closures pending their own
symbolic proofs) should be nailed down rigorously by the builder even
where "trivial," since CLAUDE.md requires no hand-waving.
Cases to cover: `P\le0` / `P>0\wedge E\ge0` / `P>0\wedge E<0` — all three
must be covered; the first two are algebraically easy but must still be
written up rigorously (not just asserted), the third is the hard core.
Watch out for: (a) do NOT attack the round-9 file's literal uncorrected
Case-(b) statement — it is false, confirmed by explicit counterexample; (b)
the squaring steps in 2 and 3 require checking sign nonnegativity of both
sides before squaring is valid — this must be stated explicitly, not
skipped; (c) `E\ge0` is only numerically confirmed to dominate ~91% of
cases — its own proof is still open and must not be asserted without
derivation.

---

coordinate-bash-resultant-boundary-pointwise: advance
Target: same as sibling — the whole problem's claim, via the pointwise
`W(r_{\mathrm{lo}})=D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})>0` root-selection
machinery (Lemma P1) plus the certified `z_N/z_K`-evaluation closure of its
own target in both `Y\gtrless0` cases (round 9, fully closed).
Technique: **boundary/degeneration argument** — bound the sibling's residual
quantity `G(\beta_1)=2K-f(\beta_1)` below by an explicit multiple of the
domain-width `(\gamma-\beta_0)` (or of `Y(\gamma)`, or of `\sin(A+3\beta_1)` —
the three quantities that jointly vanish only at the codimension-2 corner
where the sub-case degenerates), leveraging the **already-certified**
unconditional monotonicity `(2K-f)'=-f'<0` (Theorem 16.1) via a mean-value
argument, instead of a global polynomial-positivity/SOS certificate.
Skeleton:
  1. Recall the certified fact (Theorem 16.1, unconditional, already proved):
     `(2K-f)'(\beta)=-f'(\beta)<0` on the relevant domain — `2K-f` is
     strictly decreasing in `\beta`.
  2. Identify the "bad corner": `G(\beta_1)\to0` only as `\gamma-\beta_0\to0`
     (equivalently `\beta_0\to\gamma`, forcing `Y(\gamma)\to0` and
     `\beta_1\to\beta_0\to\gamma` simultaneously) — established numerically
     this round (300 Nelder-Mead runs + 250×250 grid sweep, sturm-sos-lens
     explorer, own independent code): `\min G` on `\{\gamma-\beta_0\ge
     \varepsilon\}` shrinks roughly linearly in `\varepsilon`
     (`\varepsilon=0.3\Rightarrow\min G\approx0.19`; `\varepsilon=0.02
     \Rightarrow\min G\approx0.036`). This is evidence, not yet a proof, that
     the true inequality shape is `G(\beta_1)\ge c\cdot(\gamma-\beta_0)` for
     some explicit/derivable `c>0` (or an analogous bound in `Y(\gamma)` or
     `\sin(A+3\beta_1)`).
  3. **Derive the linear lower bound rigorously**, by mean-value theorem
     applied to `2K-f` on the interval `[\beta_0,\gamma]` (or the sub-interval
     containing `\beta_1`): since `G=2K-f` is strictly decreasing with
     derivative `-f'(\beta)`, and `G(\beta_0)>0` is already established
     (Theorem 16.1's endpoint lemma, certified), a bound of the shape
     `G(\beta_1) \ge G(\beta_0) - \sup_{[\beta_0,\gamma]}|f'|\cdot(\beta_1-\beta_0)`
     is the natural mechanism — the builder's job is to make `G(\beta_0)>0`
     and `\sup|f'|` both explicit enough in `A,B` to close the sign, using
     the same closed forms already certified in `f'(\beta)=\sin(A+\beta)
     \cos B+\sin(A+B-\beta)`.
  4. Combine with the corrected hypothesis `\sin(A+3\beta_1)<0` (equiv.
     `\beta_1>\beta_0`) from `coordinate-bash-resultant-boundary`'s Claim
     (A′) to pin down the sign/scale of `(\beta_1-\beta_0)` and close
     `G(\beta_1)\ge0`.
  5. This closes Theorem 16.2 Case (b) by an **independent mechanism** from
     the sibling's algebraic 3-way split — if it succeeds, gives a second,
     structurally different proof of the same shared gap (valuable even if
     redundant, since it may be substantially shorter/more robust than the
     residual degree-6 trig inequality the sibling's route bottoms out on).
Key lemmas (claim + mechanism):
  - `\inf G(\beta_1)=0` is attained ONLY at the degenerate corner
    `\gamma-\beta_0\to0` — because that is exactly where `Y(\gamma)\to0`
    (the Case (a)/(b) boundary) and `\beta_1\to\beta_0` simultaneously,
    collapsing the interval on which the monotonicity/endpoint argument has
    room to operate; confirmed numerically this round via two independent
    optimization methods (Nelder-Mead + grid), not yet a proof.
  - `G` decreasing (`G'=-f'<0`) plus `G(\beta_0)>0` (both already certified)
    together give a mean-value bound `G(\beta_1)\ge G(\beta_0)-M(\beta_1-
    \beta_0)` for `M=\sup|f'|` on the interval — because MVT/Lipschitz bounds
    are the standard tool to convert a derivative bound + one endpoint value
    into a lower bound at a nearby point.
Open gaps: step 3 (making the MVT bound explicit and showing it is strong
enough, i.e. `M(\beta_1-\beta_0) \le G(\beta_0)`, using the actual closed
forms of `f'` and `G(\beta_0)`) is entirely open — this is the one new
computation this approach must complete. Not yet attempted by any builder.
Cases to cover: none beyond the standing `A\le\pi/2` domain restriction
already built into `\beta_1`'s existence (`\cos^2\beta_1=X_0\ge0` needs
`\cos A\ge0`); note if `\cos A<0` the sub-case is vacuous (no real
`\beta_1`) and Case (b) does not arise — should be stated explicitly by
the builder, not silently assumed.
Watch out for: this mechanism may turn out to give a bound too weak to
directly conclude `G(\beta_1)\ge0` (a naive Lipschitz/MVT bound is often
lossy compared to the sharp inequality) — if step 3 fails to close, the
"linear in `\gamma-\beta_0`" numeric pattern is still valuable evidence to
report back, but should not be asserted as proved without the explicit
constant computation.

---

ptolemy-trig-identity: advance
Target: same whole-problem claim, via the fully independent (non-coordinate)
Ptolemy/inversion parametrization, radical-free sextic reduction `\Psi(\tau,
A,C)>0`.
Technique: unchanged — resultant-elimination to a radical-free sextic,
already reduced (round 6/7) to a four-branch "odd number exceed 4" parity
claim (`lemmas/ptolemy-sextic-parity-reduction.md`).
Skeleton: unchanged from round 7's certified reduction; the outstanding step
is proving the parity claim (why the genuine-genuine branch is the one
exceeding 4) — no new lever surfaced this round for this specific route.
Key lemmas: as previously certified (`radical-isolation-equals-psi.md`,
`lemma-a-equals-psi.md`, `ptolemy-sextic-parity-reduction.md`) — all
independently re-verified in prior rounds, unchanged.
Open gaps: the four-branch parity claim itself remains open; no round-10
explorer targeted this route directly (all three focused on the coordinate
route's shared gap per dispatch), so kept live but not this round's
priority.
Cases to cover: the four sign branches of the parity claim, as previously
enumerated.
Watch out for: this route's gap is a *different* algebraic object from the
coordinate route's `G_{2b}`-exclusion (confirmed independent in round 7-8) —
do not assume progress on one transfers to the other without re-deriving.
Kept live for population diversity per CLAUDE.md (a field that only
advances the leader starves to one proof), but not in this round's build
set since neither this round's dispatch nor any explorer surfaced new
leverage on it.

---

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise
