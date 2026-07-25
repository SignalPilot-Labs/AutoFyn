## imo-2026-02 (lens: the (⋆) target, `(1+cosB)^2 X0 ≥ RHS^2`, full Case-(b) coverage)

### Exact definitions (confirmed from the -tangent/-sos files, cross-checked)
`K_c=2\sin A\sin(A+B)`, `P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `Q=-\sin A\sin B`,
`\beta_0(A)=(\pi-A)/3`, `G(\beta)=K_c-P\sin\beta-Q\cos\beta`,
`X_0(A,B)=\dfrac{\sin B\cos A}{2\sin(A+B)}`,
`\mathrm{RHS}=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
`S(A,B):=(1+\cos B)^2X_0-\mathrm{RHS}^2` — target is `S\ge0` (only load-bearing
when `\mathrm{RHS}>0`, else trivial). Case-(b) domain `\mathcal D`: `0<A<\pi/2`,
`0<B\le C=\pi-A-B` (i.e. `B\le(\pi-A)/2`, the WLOG `\angle B\le\angle C`),
`B>\beta_0(A)`, `0\le X_0\le1`, and — writing `\beta_1=\arccos\sqrt{X_0}` —
`\beta_0<\beta_1<B`, equivalently the two purely algebraic conditions
`\cos^2\beta_0(A)>X_0(A,B)>\cos^2B` (`n_1>0`, `n_2>0` in the `-sos` file's
notation). This exact domain characterization (two implicit curves, not one)
is the -tangent file's genuine new structural finding from round 11 and I
independently re-derived/re-used it here without modification.

### What I did this round (verification/scouting only, no proof attempted)
1. Reconfirmed `\partial X_0/\partial B=\sin A\cos A/(2\sin^2(A+B))>0` exactly
   (matches the certified `lemmas/x0-partial-b-derivative.md`).
2. Attempted a direct `sympy.simplify` of `\partial S/\partial B` in one shot —
   **times out after 2+ minutes even on this scouting machine** (14 CPUs); the
   full expression is too large for blind simplification. This confirms the
   round-11 file's own experience (it gave the raw unsimplified `\partial_B
   \mathrm{RHS}` and stopped there) — a straight-line symbolic attack on
   `\partial S/\partial B` needs a smarter decomposition (e.g. via the
   `u=\tan(A/6)` rational parametrization from the `-sos` file, which turns
   trig into polynomial algebra and might make `sympy` tractable, or a
   hand-factored decomposition using the proven sign of `\partial X_0/
   \partial B` as one piece) — not attempted here due to time, flagged as the
   natural next symbolic step.
3. Ran a fresh, independent high-precision (`mpmath`, 20-30 digit) finite-
   difference sweep for `\partial S/\partial B`, entirely from scratch (own
   script, own domain-membership test rebuilt directly from the raw
   definitions, not copied from any file): ~2,200 valid domain points total
   across three separate sweeps (broad random sweep over `A\in(0,\pi/2)`,
   `B\in(0,\pi)`; a sweep concentrated near the corner `A^*\approx0.40638`;
   a further 20,000-draw broad sweep). **Zero violations of `\partial S/
   \partial B\ge0` in any sweep**, and — more informative than round 11's own
   report — **the minimum observed derivative across every sweep was
   `\approx0.178`–`0.19`, never closer to `0`**, including in samples
   deliberately placed near the corner `(A^*,B^*)`. This is a stronger form
   of corroboration than round 11's own finding (which only reported "zero
   violations among 11,764 samples," not how close to the sign boundary the
   minimum got): the monotonicity appears to hold with **comfortable
   uniform margin**, not as a knife-edge fact, which is a good sign for
   eventual provability (a knife-edge numeric fact would be more suspicious /
   harder to prove; a fact with margin ~0.18 across the whole domain suggests
   a clean algebraic reason exists). I could not evaluate the derivative
   exactly at the corner itself — the domain-membership test correctly
   returns "not in domain" there (consistent with round 11's cusp finding:
   the corner is a boundary point, approached but not attained).
4. Positivstellensatz feasibility (SOS + `n_1,n_2` multipliers on `\mathrm{Num}`,
   the degree-34-in-`u` polynomial from the `-sos` file): `cvxpy` is **not
   installed** in this environment (checked; `pip install` would be needed).
   Given the 60-minute budget I did not attempt an SDP search this round —
   flagging this as unattempted, not as "tried and failed." If a future round
   pursues this, note the objects are already fully specified in the `-sos`
   file's Step 5 (`\mathrm{Num}$, `n_1$ deg-10, `n_2$ deg-6, all in
   `\mathbb Q(\sqrt3)[u,\cos B,\sin B]`), so no re-derivation is needed —
   only the SDP setup and solve.
5. Corpus check: **no geometry cruxes exist in the corpus** (confirmed via
   `crux_moves_documentation.md`: "geometry — Not in the corpus yet"). The
   closest available analogy is in `algebra`/`inequalities-SOS-and-convexity`
   (149 cruxes): `aimo-0005`'s move — "bound a nonlinear term by the tangent
   line at the equality point, chosen so it *also* passes through the value at
   a second (boundary) point, then verify the bound by factoring the
   difference" — is conceptually close to what the `-tangent` file's dispatch
   tried and retired (a tangent line pinned at the corner). It is not a
   literal match (that crux is 1-variable; `(\star)` is genuinely 2-variable
   with an implicit-curve boundary), but it suggests a *two-point* pinned
   tangent/secant construction (forcing the linear bound through both the
   corner **and** a second domain-boundary point, e.g. a point on the curve
   `X_0=\cos^2B`) might succeed where the single-point tangent failed —
   this is a genuinely new, untried lever, not yet attempted by anyone in the
   population. Flagging it as a candidate, not a result.

### Distinct openings for the outliner
- **(a) Monotonicity-in-`B` reduction** (the -tangent file's live lead): prove
  `\partial S/\partial B\ge0` on `\mathcal D`, then `(\star)` reduces to a
  single inequality along the implicit lower-boundary curve `X_0(A,B)=
  \cos^2B` (a curve with no known closed form for `B(A)`). Numeric evidence
  now stronger than previously reported (margin ~0.18, not knife-edge) —
  most promising single lever per the evidence gathered this round.
- **(b) Positivstellensatz / SOS on `\mathrm{Num}` w.r.t. `n_1,n_2`** (the -sos
  file's live lead): fully specified target, degree-34 `\mathrm{Num}`,
  degree-10/6 constraint polys `n_1,n_2`, needs SDP tooling not yet installed
  or attempted by anyone.
- **(c) Two-point-pinned tangent/secant construction** (new, from the crux
  corpus analogy): instead of a single tangent line at the corner (which the
  `-tangent` file showed fails to eliminate `B`), pin a linear (in `A`, at
  fixed structure) bound through **both** the corner and a second point on
  the true boundary curve `X_0=\cos^2B`, in the style of `aimo-0005`. Untried;
  worth a line in the outline as a genuinely different variant of the
  tangent idea, not a rehash of the retired one-point version.
- **(d)** direct `u=\tan(A/6)` rationalization of `\partial S/\partial B` (turn
  the transcendental derivative into polynomial algebra before attempting
  `sympy.simplify`, since blind trig simplification times out) — a
  tractability lever for route (a), not a new mathematical idea.

### Candidate technique(s)
Monotonicity/MVT-in-one-variable reduction (route a); constrained
Positivstellensatz / SOS-with-multipliers (route b); tangent-line-pinned-at-
two-points (route c, new). All three operate on the same already-reduced
target `(\star)`; none is a "different top-level framing" of the whole
problem — per CLAUDE.md's shared-gap-plateau guidance, if none of these
closes in the next 1-2 rounds, the population should seriously consider
whether `(\star)` itself (a lossy one-squaring MVT bound, per round 10) is
too weak a target, and revisit the un-squared `G(\beta_1)\ge0` directly, or
the sibling `T\ge0`/`q_1,r_0` factorization route, rather than continuing to
refine `(\star)`.

### Cheap-kill candidates
None found. `S` does not factor as an obvious difference of squares or
product of manifestly-signed pieces on inspection of its definition (it is
genuinely `(1+\cos B)^2X_0-\mathrm{RHS}^2`, a difference, not a sum, of two
positive quantities — no parity/pigeonhole/injection shortcut applies to a
continuous 2-variable transcendental inequality of this kind).

### Knowledge-base entries to use
- **Sum of squares (SOS) / completing the square** (`knowledge_base.md` line
  ~17) — directly relevant to route (b), but the KB entry is the generic
  SOS idea only; it does not cover constrained/Positivstellensatz SOS
  (needed here since round 11 proved no domain-free SOS certificate exists).
- No KB entry specifically covers "tangent-line trick" or "MVT/Lipschitz
  reduction" by name; the population has been improvising both, which is
  fine (KB entries are generic pointers, not a menu limited to this
  problem).

### Analogous past problems (cruxes)
- **`aimo-0005`** (algebra / inequalities-SOS-and-convexity): tangent line at
  the equality point, forced to also pass through the boundary-equality
  value, verified by factoring the difference. Reasonably analogous in
  *spirit* to route (c) above (a two-point-pinned linear bound) — worth
  adapting, not citing.
- No geometry cruxes exist in the corpus at all (confirmed via
  `crux_moves_documentation.md`), so there is no closer geometric analogy
  available to retrieve.

### Prior progress
Full history preserved in `current.md` through round 11; nothing changed
this round (I only ran independent verification, no new claim submitted).
Current best remains: whole problem reduced to Case (b) reduced to `(\star)`
(entire branch); `\partial X_0/\partial B>0` proved exactly
(`lemmas/x0-partial-b-derivative.md`); the corner `(A^*,B^*)` proved to be a
domain-boundary cusp, not an interior critical point
(`lemmas/star-corner-is-boundary-cusp-not-critical-point.md`); no domain-free
SOS certificate exists for `(\star)`'s cleared numerator (round 11, `-sos`).

### Dead ends (do not retry)
- Naive `\cos(A/3)`-basis substitution for radical-clearing — leaves a
  genuine linear-in-`y` residual, requires an extra squaring (round 11,
  `-sos`). Use `u=\tan(A/6)` instead.
- Literal tangent-line-in-`A`-at-fixed-`B` construction pinned only at the
  corner — does not eliminate `B` from the resulting inequality after
  substitution into `\mathrm{RHS}` (round 11, `-tangent`); tried with both
  candidate factors (`X_0` and `\cos^2\beta_0`), neither works. (Route (c)
  above, pinning at *two* points, is a distinct, untried variant — do not
  conflate the two.)
- Domain-free (unconditional) SOS certificate for `\mathrm{Num}(u,\cos B,
  \sin B)` — proved impossible (round 11, `-sos`): relaxing the domain gives
  ~37-50% negative samples. Any certificate must use `n_1,n_2` as
  Positivstellensatz multipliers.
- Scanning along `B=\beta_0(A)` as if it were the relevant domain boundary —
  it is essentially outside the true domain closure away from the corner
  (round 11, `-tangent`); the true lower `B`-boundary is the different,
  implicit curve `X_0(A,B)=\cos^2B`.

### Small-case / intuition notes (all conjecture, not proof)
- `\partial S/\partial B\ge0` on `\mathcal D`: re-confirmed independently
  this round with ~2,200 fresh high-precision samples (0 violations),
  **and, new this round, found the minimum observed value is comfortably
  positive (~0.178-0.19), never near 0** — this is new evidence (not just a
  reproduction) suggesting the fact is not a knife-edge coincidence and
  should be provable by a genuine algebraic mechanism (most likely: show
  `2(1+\cos B)\bigl[\tfrac12(1+\cos B)\partial_BX_0-\sin B\,X_0\bigr]\ge
  2\,\mathrm{RHS}\,\partial_B\mathrm{RHS}` via a clean bound on
  `\partial_B\mathrm{RHS}`, not attempted here).
- The corner `(A^*,B^*)` is confirmed (again) to sit exactly on the domain
  boundary, not reachable by the finite-difference test — consistent with,
  not contradicting, round 11's cusp finding.
