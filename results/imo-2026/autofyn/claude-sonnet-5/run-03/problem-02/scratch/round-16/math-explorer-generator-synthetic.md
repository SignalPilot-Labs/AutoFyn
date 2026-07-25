# Scouting report — round 16 (imo-2026-02)

Two threads scouted, exploration only, no proof written.

## Thread 1 — `coordinate-bash-resultant-boundary`: generator-search techniques for `q1<0`, `r0<0`

**State as of round 15.** The population has an exact, sign-checked basis of 9
generators on `(sigma,tau) in (0.1565,0.2610)x(0.6251,0.7863)` (the true
residual domain, characterized by `G0>0, Enum<0, Bc>=0, Num<0`):
`B1, -B2, B3, B4, B5, B6` (degree-matched `(ct/sd)*{G0,-Enum,-Num}` products)
plus the three round-15 pairwise products `B_{G0E}=(G0*Enum)_00`,
`B_{G0N}=(G0*(-Num))_00` (**note: current.md round-15 flags a confirmed sign
error here — the file's own displayed range `B_{G0N} in (0.0121,0.0789)>0`
is actually the range of `-B_{G0N}=(G0*Num)_00`; the true `B_{G0N}` is
uniformly negative, `(-0.079,-0.012)`. Any round-16 work must use the
corrected sign: the positive generator is `(G0*Num)_00`, not `(G0*(-Num))_00`
as currently written**), and `B_EN=(Enum*Num)_00`. All nine natural
nonnegative multiplier extensions of `(1-sigma)`/`(1-tau)` (`tau(1-sigma)`,
`sigma(1-tau)`, `(1-sigma)(1-tau)`, `(1-sigma)^2`, `(1-tau)^2`,
`sigma(1-sigma)`, `tau(1-tau)`) bring `-q1` into the unsigned span of the
9-generator basis but leave the nonnegative-coefficient LP infeasible in
*every* case (confirmed via a phase-1 L1-residual LP, not just a solver
flag — residual `~65.46`, decisively nonzero). `r0` is confirmed structurally
harder: only `(1-sigma)` (not `(1-tau)`) repairs its span obstruction, and
even then the LP is infeasible.

**What generator-search techniques could plausibly close this, given what has
already failed:**

1. **Use the corrected `(G0*Num)_00` as a genuinely new (tenth) basis
   element** — this was flagged but not yet exploited: round 15's LP runs all
   used the *wrong-signed* `B_{G0N}`, so none of the 9-multiplier x 10-generator
   LP feasibility grid has actually been run with the correct generator. This
   is the cheapest, most direct next step (not a new technique, just fixing a
   bug and rerunning the same LP sweep) and should be done before any new
   machinery is invented.

2. **Full Lasserre/Putinar moment-SOS relaxation (SDP), not a hand-picked
   generator basis + LP.** Everything tried so far is "guess a handful of
   sign-definite products, then LP over a *fixed*, small multiplier set." The
   natural generalization — from knowledge_base.md's "Quadratic forms /
   PSD" entry and the population's own repeated (but only *pointwise*, per
   `coordinate-bash-resultant-boundary-pointwise-sos`'s round-15 SDP work) use
   of SDP — is to pose the *joint* Putinar certificate directly: search for
   SOS polynomials `sigma_0, sigma_{G0}, sigma_{Enum}, sigma_{Bc}, sigma_{Num}`
   (up to some fixed degree, via an SDP over their Gram matrices) with
   `-q1 = sigma_0 + sigma_{G0}*G0 + sigma_{Enum}*(-Enum) + sigma_{Bc}*Bc +
   sigma_{Num}*(-Num)`. This subsumes every generator/multiplier the LP
   approach has hand-picked (an SOS multiplier of degree `2k` covers *all*
   nonnegative-coefficient combinations of monomial-times-square terms up to
   that degree at once) and is the standard escalation from "LP-with-guessed-
   basis infeasible" to "does a certificate exist at this degree at all,"
   which the LP search cannot answer definitively (LP infeasibility only
   rules out *that* basis, never the existence of a certificate). `scipy`
   does not do SDP; `cvxpy`+`SCS`/`MOSEK`, or `sympy`+manual Gram-matrix setup
   feeding an LP after fixing signs, are the practical routes — not yet
   installed/tried in this population (`pip install cvxpy` would be needed).
   This is the single highest-value untried technique for closing `q1,r0`.

3. **Explicit case split (per current.md's own honest assessment, option
   (iii)), guided by the crux corpus's Schur-inequality pattern.** A relevant
   retrieved crux (`algebra/inequalities-SOS-and-convexity`): *"Prove a
   Schur-type cyclic sum by ordering the variables and dominating the lone
   negative term by an adjacent positive one"* — for `sum(x-y)(x-z)/x^2>=0`,
   WLOG `x<=y<=z`, the middle term is the only negative one and is directly
   dominated termwise by a neighbor using `1/x^2>=1/y^2`. This is a hint to
   adapt, not reuse verbatim: split the residual `(sigma,tau)` domain into
   2-3 sub-regions by an explicit sign/ordering condition on the intermediate
   quantities that make `q1` (or `r0`) mixed-sign as a bare sum, then find a
   different termwise-dominating pairing valid on each sub-region. This is
   the "genuinely new base generator" option the file's own round-15 note (i)
   flags but has not tried — no ordering-based case split of `(sigma,tau)` or
   of `(G0,Enum,Bc,Num)`'s signs has been attempted in any round so far
   (rounds 10-15 all search a *single* global certificate).

4. **Higher-degree multipliers.** Only degree-1/2-in-`(sigma,tau)`
   multipliers have been tried on the 9-generator basis. A systematic
   degree-3 or degree-4 multiplier sweep (still LP, not SDP — cheap to try
   first) is a strict escalation of the existing infrastructure and should be
   tried before jumping to full SDP if compute/time is tight this round.

**Recommendation for math-explorer/outliner priority:** (1) is a 5-minute
bug-fix rerun that should happen regardless; (2) (Putinar/SDP) is the
technique most likely to actually resolve the "does *any* certificate exist"
question this generator-search family has been probing blindly for 4+
rounds; (3) is the fallback if (2) is infeasible to set up in one round.

## Thread 2 — `ptolemy-trig-identity-synthetic`: is the auxiliary-circle route a live alternative?

**Verdict: not a live independent route — it converges to the same
polynomial-positivity difficulty as the sibling `ptolemy-trig-identity`, and
its own round-5 build already demonstrated why no auxiliary circle can help.**

The file's Lemma T (fully proved, genuine content) reformulates the shared
gap `alpha+alpha'<A` as a single cross-product sign
`x_K y_L - x_L y_K > 0`, i.e. "as seen from A, ray AL is CCW of ray AK." This
converts the target into exactly the shape an inscribed-angle/auxiliary-
circle argument (via the already-proved and certified
`lemmas/ray-angle-determines-cyclic-order.md`, Lemma S1) could close *for
free*, with no further computation, **if** `K` and `L` could be placed on a
common fixed circle. The file then tries the three natural candidates:

- nine-point circle of `ABC` (motivated by `M, N` being midpoints, and
  `psi=angle BMK`, `phi=angle CNL` being angles at those midpoints) — **fails
  structurally**: `K(theta)` traces a one-parameter transcendental curve
  (governed by the non-constant-coefficient-in-theta quadratic-in-cot(psi)
  equation (III)), and a fixed circle can only meet a non-conic curve in
  finitely many points, so `K` is not generically on it.
- a circle through `B, C` (motivated by both `K, L` sharing the same
  parameter `theta`) — **fails structurally**: would require `angle BKC`
  constant in `theta`, but `angle BKC = A+2theta+psi(theta)` is confirmed
  non-constant (consistent with the sibling's own extremal analysis, where
  `F` is non-constant and approaches its infimum `4` only in a degenerating
  limit `A->0`).
- the problem's own circle `omega` through `A,K,L,Q` — **circular reasoning**:
  `omega`'s existence and which Ptolemy pairing to use both already
  presuppose `(dagger)`, so it cannot be used to prove `(dagger)`.

All three failures share one root cause, stated explicitly in the file:
`K(theta)` and `L(theta)` are each cut out by a *transcendental* relation (a
quadratic in `cot(psi)`/`cot(phi)` whose coefficients depend on `theta` in a
way that is not compatible with a fixed inscribed angle), so no
`theta`-independent circle can carry the points that actually get realized.
This is a structural obstruction, not a failure of search effort — a fourth
or fifth "try a different named circle" attempt (Miquel point, spiral-
similarity image, incircle/excircle-adjacent circles per
knowledge_base.md's "Circle/triangle configuration facts" entry) would very
likely hit the identical wall, since the obstruction is about the *shape of
the locus* (non-conic), not about which particular circle was chosen.

**Cross-check against the sibling `ptolemy-trig-identity`.** That file
independently reduces the *same* gap (`alpha+alpha'<A`, there phrased as
`F>4`) via resultant-elimination/radical-clearing to a single radical-free
sextic `Psi>0` in one variable set — i.e. the sibling has *already* arrived
at exactly the same kind of target (one explicit polynomial positivity
claim with a strong numeric margin, no symbolic proof yet) that the
coordinate-bash-resultant-boundary family has been stuck on for the whole
main route. `ptolemy-trig-identity-parity-decomposition` (not read in full
this round, but referenced by both current.md and the synthetic file as
having "independently proved their reformulations are exactly equivalent in
difficulty to the same Psi>0 gap") corroborates this: three independent
framings of the same underlying gap (synthetic cross-product, radical-
clearing sextic, and a parity-decomposition variant) all bottom out at one
polynomial-positivity statement.

**Is a genuinely different lever visible?** The synthetic file's own closing
paragraph identifies the only structurally different idea it has not yet
tried: comparing `alpha(theta)` and `beta_L(theta)` (equivalently `K(theta)`,
`L(theta)`) *directly* as functions of the shared parameter `theta`, via a
monotonicity/convexity argument (e.g. showing `d(beta_L-alpha)/d(theta)` has
a fixed sign, or a trigonometric-Ceva-style ratio bound), rather than via any
static circle-membership fact. This is *not* the same computation as the
radical-clearing route (it works with `theta` as the free variable and the
implicit equations (III)/(IV) directly, rather than eliminating `theta` via
resultants down to a sextic in other variables) — so it is arguably a
genuinely different lever, still synthetic/calculus-flavored rather than
algebraic-elimination-flavored. However: (a) it was not attempted this round
(explicitly listed as "would more likely need," not tried), (b) it still
targets the identical inequality, so if it succeeds it closes the shared
gap by a different method, but if it fails it very plausibly fails for the
same underlying reason (the true difficulty seems to live in the geometry/
algebra of the gap itself, not in the framing) — three independent
reformulations already hitting the same wall is suggestive that the gap
is "really" hard, not an artifact of one representation.

**No geometry cruxes exist in the corpus** (`crux_moves_documentation.md`
line 73: "geometry — Not in the corpus yet"), so no retrieval-based lever
(e.g. a named inscribed-angle/auxiliary-circle theorem from a solved past
problem) is available to seed a fourth circle candidate; the only usable
crux material is from algebra (SOS/Schur-domination patterns, see Thread 1)
if the population pivots this gap to the pure `Psi>0` polynomial form.

**Recommendation:** do not spend another full round on "try another named
circle" for this approach — that specific mechanism is now exhausted with a
proven structural reason (transcendental, non-conic loci). If the outliner
wants a genuinely new framing for this shared gap (per CLAUDE.md's
plateau-breaking guidance), the monotonicity-in-theta idea sketched above is
the one live, not-yet-tried synthetic lever; otherwise this approach should
be deprioritized relative to whichever of the three equivalent
reformulations (coordinate-bash sextic, parity-decomposition, or this one)
has the cleanest remaining polynomial target for an SOS/Positivstellensatz
push (see Thread 1's technique recommendations, directly reusable here since
the target shape — one polynomial positivity claim on a semialgebraic
domain — is the same class of problem).
