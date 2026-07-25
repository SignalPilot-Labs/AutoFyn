## Outline review — imo-2026-02, round 14

Outline reviewed: `/tmp/round-14/proof-outliner.md` (three "advance" items, no new
slugs, no RETHINK, no copy). Cross-checked against `results/imo-2026-02/current.md`
(round 13 adjudication) and the three explorer reports.

### 1. `coordinate-bash-resultant-boundary` (parity-guided certificate search)

**Verdict: APPROVE.**

Independently re-derived the finer `(Z_2)^4`-grading claim from scratch, not
trusting the explorer's report:
- Took `Num = c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3-6c^2ds^3t^2-9cd^2s^4t`
  from the certified `lemmas/num-identity-exact-squaring-equivalence.md` and
  hand-classified every one of its six monomials by `(deg_c,deg_s,deg_d,deg_t)
  mod 2`: all six land in exactly `(1,0,0,1)` or `(0,1,1,0)`, confirming the
  claimed two-graded-piece concentration exactly as stated (not merely
  plausible — verified term-by-term by hand).
- Did the same for `G_0=ct(1-2d^2)-2sd^3` from the certified
  `lemmas/parity-obstruction-q1-r0-certificate.md`: term `ct`, `-2ctd^2` both
  `(1,0,0,1)`; term `-2sd^3` is `(0,1,1,0)`. Matches.
- Ran an independent `sympy` symmetrization (own script, own sign-flip
  averaging over `c\to\pm c,d\to\pm d`) of `ct\cdot G_0` reduced modulo the
  Pythagorean ideal, and got `-2\sigma\tau^2+\sigma\tau+2\tau^2-\tau`, which
  factors to exactly `-\tau(\sigma-1)(2\tau-1)` — matching the file's claimed
  `(ct\cdot G_0)_{00}` bit-for-bit.
- Verified by hand that the coarse-`(0,0)` part of `c\cdot G_0` (the "fix"
  round 13 flagged and this round's explorer refutes) is
  `t(2t^2-1)(1-s^2)`, an odd-`t` expression, i.e. genuinely NOT a function of
  `\sigma,\tau` alone — confirming the refutation is correct, not a hasty
  claim.

This is a clean, mechanically verifiable sharpening; the technique
(Positivstellensatz certificate search, now correctly re-targeted at a
degree-/grade-matched basis) remains sound and is now better-targeted than
round 13's basis. The open gap (Step 4, the actual nonnegative-combination
search) is honestly still open — not overclaimed. No fatal flaw found.

### 2. `coordinate-bash-resultant-boundary-pointwise-tangent` (corner-reduction on Tgt)

**Verdict: APPROVE, with a domain-membership caution for the builder.**

Independently rebuilt `X_0,\beta_0,K_c,P,Q,G,\mathrm{RHS},D_2,T_1',\mathrm{Tgt}`
from scratch (own `sympy`/`mpmath`, not reusing the explorer's or file's
scripts):
- Confirmed exactly `X_0(\pi/3,\pi/3)=1/4` (`sympy` exact).
- Confirmed the sum-to-product identity `\sin A-\cos(A/2)-\cos(3A/2) =
  2\cos(A/2)(\sin(A/2)-\cos A)` holds identically (own `sympy` residual
  check at multiple points, all `0`), and that on `(0,\pi)` this vanishes
  only at `A=\pi/3` (and the degenerate `A=\pi`) — `sympy.solveset` confirms
  `\{\pi/3,\pi\}`, so `T_1'=0` on `B=C` **only** at `A=\pi/3` in the valid
  range, exactly as claimed — this is a genuine exact identity, not a
  numerical coincidence.
- Confirmed `\mathrm{Tgt}(\pi/3,\pi/3)=(9/4)D_2(\pi/3,\pi/3)^2` numerically
  to 30 digits (`1.57413855...` both sides), matching the claim.
- **Adversarially tried to break sub-target (a)** (corner is the global
  min over `D`). First attempt (naive domain reconstruction using only
  `B>\beta_0(A)` and `B\le C`) found points with `\mathrm{Tgt}\approx1.40`,
  *below* the corner value — an apparent counterexample. Tracing it down:
  this was my own bug, not a flaw in the outline — those points violate the
  domain's third constraint `X_0(A,B)<\cos^2\beta_0(A)` (I directly checked:
  at `(A^*, C\text{-boundary})`, `X_0\approx0.459>\cos^2\beta_0\approx0.375`,
  outside `\mathcal D`). After correctly enforcing **all three** domain
  constraints (`B>\beta_0(A)`, `\cos^2B<X_0<\cos^2\beta_0(A)`, `B\le C`), a
  300k-point domain-restricted scan plus a dense local scan around the
  corner found **no point below the corner's value 1.5741**, minimum found
  `\approx1.580` (i.e. consistent with, not contradicting, the claim).
  **This is a useful finding to hand to the builder**: the domain `\mathcal
  D`'s upper bound `X_0<\cos^2\beta_0(A)` is easy to silently drop when
  setting up a boundary/monotonicity argument for sub-target (a), and doing
  so gives a false counterexample near the *other* corner `(A^*,B^*)`. The
  builder must carry all three domain inequalities through the boundary
  argument, not just `B>\beta_0(A)$ and `B\le C`.

Sub-target (a) itself remains open and is honestly disclosed as such — not
a free identity, genuinely needs the boundary/monotonicity argument
outlined. Sub-target (b) is essentially mechanical. No fatal flaw; the
reduction is sound and my adversarial check found no counterexample.

### 3. `coordinate-bash-resultant-boundary-pointwise-sos` (SDP/SOS on Num)

**Verdict: CHANGES REQUESTED (not RETHINK) — the plan is right, but treat
Step 1 as a hard gate, not a formality.**

The dispatched scrutiny target (the sign-flip between round 13's monomial-
basis "-1.548, clean two-solver agreement" and this round's Chebyshev-basis
"+1.6e-5 to +6e-5, both optimal_inaccurate") is exactly the kind of
numerically-noisy near-zero SDP result that should not be trusted either
way. I did not re-run the SDP myself (degree-34, not a cheap
verification), but the outline's own account is self-consistent and
appropriately cautious: both this round's *and* round 13's numbers are now
in question (this round's own attempt to reproduce round 13's monomial-basis
result got `optimal_inaccurate` on both solvers with 3-orders-of-magnitude
disagreement, not the "clean" result originally reported). A `t^*` within
`~2\times10^{-8}` of the PSD boundary on a degree-34 SDP is squarely inside
numerical noise; neither sign should be elevated to a fact.

The outline's skeleton correctly makes Step 1 (bit-for-bit reproduction of
round 13's exact script) a hard prerequisite before Step 2's Chebyshev
result is used for anything, and explicitly says not to "silently drop this
route as a dead end nor silently declare it solved" on the current
contradictory evidence. That is the right discipline. My one addition: the
builder must not proceed past Step 1 if it, too, comes back inconclusive —
in that case the right move is higher-precision arithmetic (e.g. exact
rational SDP via `sympy`/`SCS` with rational Chebyshev coefficients, or a
higher-precision solver) or moving to the degree-reduction fallback in Step
5, not another numeric solver sweep at the same precision. This is a
process caution, not a fatal flaw in the technique (SOS/Positivstellensatz
via SDP is still the right general tool here, per `knowledge_base.md`) — so
CHANGES REQUESTED, not RETHINK.

### Population diversity

All three approved approaches are forks of the same backbone reduction
(`coordinate-bash-resultant-boundary` → Case (b) residual positivity),
differing only in which equivalent reformulation of "the residual
inequality" they attack (`q_1,r_0<0` via graded Positivstellensatz; `Tgt>0`
via corner-extremal calculus; `Num\ge0` via SDP/SOS). This is genuine
technique diversity (algebraic certificate search, calculus/extremal
argument, and semidefinite programming are different tools, and a wrong
turn in one doesn't directly kill another), so I am not RETHINKing any of
them on diversity grounds alone — each made real, independently-verified
progress again this round (parity grading exactly confirmed; Tgt corner
value exactly confirmed; SDP contradiction correctly quarantined). But this
is now round 14 and the *entire* population's build budget has gone to
forks of one backbone since around round 9–11; the dormant `ptolemy-trig-
identity` family (a genuinely different top-level route to the whole
problem, Elo ≈1490, last built round 7) and `spiral-similarity-bootstrap`
(never registered — RETHUNK'd round 1) have not been touched in 6+ rounds.
Recommend: if none of the three coordinate-bash forks closes within 2 more
rounds, the orchestrator should dispatch a math-explorer to revisit
`ptolemy-trig-identity`'s own remaining gap (`\Psi(\tau,A,C)>0`, general
case still numeric-only) as an insurance line, or scout a fresh framing —
per CLAUDE.md's "break a shared-gap plateau" guidance — rather than
spawning a fourth fork of the same backbone.

### Ranking

No new slugs to register this round (outline proposes "advance" on all
three existing slugs, no copy). Registered comparisons via
`update_ranking`: `coordinate-bash-resultant-boundary` and
`coordinate-bash-resultant-boundary-pointwise-tangent` both beat
`coordinate-bash-resultant-boundary-pointwise-sos` (the latter's headline
result this round is an unresolved contradiction, weaker than the other
two's exactly-verified new identities); `coordinate-bash-resultant-boundary`
vs `-pointwise-tangent` recorded as a draw (both produced comparably strong,
independently-verified exact progress this round); `-pointwise-sos` still
beats the dormant `ptolemy-trig-identity` (it has more certified structural
content overall, even with this round's hiccup). This clears `stale` on all
three build-set slugs. Updated Elo: `coordinate-bash-resultant-boundary`
≈1732 (top), `-pointwise-tangent` ≈1681, `-pointwise-sos` ≈1542.

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise-tangent, coordinate-bash-resultant-boundary-pointwise-sos
