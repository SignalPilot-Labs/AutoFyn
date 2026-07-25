## imo-2026-02 — Gap 6 scouting (`D_1(A)\ge0` on boundary curve `\mathcal C`)

### 0. Key structural fact confirmed first: `\mathcal C = \mathcal C_{\mathrm{lo}}`

Verified numerically (own fresh `mpmath`, 50 dps) that the `-twopoint`
sibling's curve `\mathcal C=\{X_0(A,B)=\cos^2B\}` **is exactly** the
`-tangent` file's `\mathcal C_{\mathrm{lo}}`, and Theorem A's closed form
$$
\tan A=\frac{-\sin B\cos(2B)}{2\cos^3B},\qquad A=\arctan(\cdot)\in(0,\pi/2)
$$
correctly reproduces the curve: substituting `A=\mathrm{Aof}(B)` into
`X_0(A,B)-\cos^2B` gives residual `0` to 50 digits at three test points,
including both known corners (`B=B^\ast\approx0.91174` gives
`A=A^\ast\approx0.40637778068433033`, matching the certified 40-digit value
to all displayed digits, and `B=\pi/3` gives `A=\pi/3` exactly). **So
Theorem A is directly reusable to write `D_1` as an explicit (not merely
implicit) single-variable function of `B` alone** — this was flagged as
"not attempted symbolically" in the `-twopoint` file but is actually already
available for free from the sibling's own Theorem A.

**Important range correction.** Checking whether the curve continues past
`B=\pi/3` (as the `-twopoint` file's report of `A_{\max}\approx1.0484,\,
B\approx1.0475$ "where `B=C`" suggested): it does **not**, within the valid
domain. At `A=B=\pi/3` we get `C=\pi-A-B=\pi/3` too — i.e. `(\pi/3,\pi/3)`
itself is already the point `B=C`. Continuing Theorem A's `\mathrm{Aof}(B)`
past `B=\pi/3` (e.g. `B=1.1`) gives `C=\pi-A-B\approx0.813<B` — i.e. `B>C`,
**outside** the domain (`B\le C` required). So the true `A`-range of
`\mathcal C\cap\mathcal D` is `[A^\ast,\pi/3]`, equivalently `B\in[B^\ast,
\pi/3]$ — **not** the `A_{\max}\approx1.0484` claimed by the `-twopoint`
file's Newton-continuation scan (that scan likely drifted off the true
domain-restricted branch, or conflated a different curve component; this
should be flagged to the outliner/builder as a numeric artifact to recheck,
not load-bearing for anything already certified). This matters: gap 6's
actual target interval is the **shorter, cleaner** `B\in[B^\ast,\pi/3]`
(or `A\in[A^\ast,\pi/3]`), with both endpoints already exactly known and
certified.

### 1. `D_1` as an explicit function of `B`: structure

Building `D_1(B):=(1+\cos B)\cos B-\mathrm{RHS}(\mathrm{Aof}(B),B)` directly
(own `sympy`/`mpmath`), `D_1$ is smooth (`C^\infty`) on the open interval
(no singularities: `\cos A\ne0,\sin(A+B)\ne0` throughout), but its **exact
symbolic closed form does not simplify to a rational or radical function of
`\cos B,\sin B`** — attempting `sympy.expand_trig` on the full expression
leaves irreducible `\sin(\arctan(t)/3),\cos(\arctan(t)/3)` terms (`t` a
rational function of `\cos B,\sin B`), i.e. it hits the **same trisection /
casus-irreducibilis wall** the `-sos` sibling already documented for
`\beta_0=(\pi-A)/3` in terms of `A` (round 10-13 population history). So a
literal polynomial-SOS or fully-rational Weierstrass closed form for `D_1`
is **not available** by direct substitution — this avenue is a dead end,
confirmed independently this round (own `sympy` attempt, not just cited).

### 2. The real finding: concavity/unimodality is UNNECESSARY — a much weaker, already-provable fact suffices

Numerically (`mpmath`, 30-50 dps):
- `D_1(B^\ast)=0` exactly (residual `\approx7\times10^{-24}` at the
  certified 23-digit `A^\ast`, consistent with 0 up to input truncation).
- `D_1(\pi/3)=0.397686404277917446\ldots>0` exactly (both endpoints
  independently recomputed, matching the `-twopoint` file's scan trend).
- **`D_1'(B^\ast)\approx4.6257691667\ldots>0`** — a clean, strictly
  positive, non-degenerate one-sided derivative at the corner (central
  finite difference at `h=10^{-15}$, 50 dps). This means the corner is
  **not** a higher-order tangency; `D_1` leaves `0` linearly with slope
  `\approx4.63`.
- Scanning `D_1'` outward from the corner: `D_1'(B^\ast+0.02)\approx5.02`,
  `D_1'(B^\ast+0.05)\approx4.46`, `D_1'(B^\ast+0.1)\approx1.29` — **stays
  comfortably `>1` throughout `[B^\ast,B^\ast+0.1]`**, i.e. `D_1` is
  strictly increasing on a full-width neighbourhood of the corner, not just
  infinitesimally.
- Correspondingly `D_1(B^\ast+0.02)\approx0.0974`,
  `D_1(B^\ast+0.05)\approx0.2433`, `D_1(B^\ast+0.1)\approx0.3933` — already
  bounded well away from `0` by `\delta=0.02`.
- A finer 40-point scan of `D_1` over the **whole** interval
  `[B^\ast,\pi/3]` (`\approx0.136` rad wide) shows a single interior local
  max `\approx0.4054` near `B\approx1.030` (`A\approx0.977`, matching the
  `-twopoint` file's report), then a monotone decrease back down to
  `D_1(\pi/3)\approx0.3977$ — **never approaching `0` again** after leaving
  the corner. The minimum of `D_1$ on `[B^\ast+0.02,\pi/3]` is
  `\approx0.0974` (at the left end of that sub-range), comfortably `>0`.

**Consequence — the proof does NOT need concavity or even unimodality of
`D_1`.** All that is needed is:
(a) a certified interval-arithmetic sweep (branch-covering, exactly
Theorem B/C's Step-1 method) of `D_1(B)>0` on the compact sub-interval
`[B^\ast+\delta,\pi/3]` for some small fixed `\delta` (e.g. `\delta=0.02`,
where the numeric minimum is `\approx0.097`, a comfortable margin, no
equality-point degeneracy anywhere in this sub-range — this is the *easy*
part, structurally identical to Theorem B/C which are already fully proved
in the same file); **plus**
(b) a certified interval-arithmetic sweep of `D_1'(B)>c>0` (e.g. `c=1`) on
`[B^\ast,B^\ast+\delta]` — exactly the Round-16 near-corner technique
(Taylor + explicit derivative-sign/Lagrange-remainder certification) — which
then gives, by the Mean Value Theorem, `D_1(B)-D_1(B^\ast)=D_1(B)\ge
c\cdot(B-B^\ast)>0` for `B\in(B^\ast,B^\ast+\delta]`.

This is **strictly easier than what round 16 already did for gap 5**: gap 5
needed a full 2-D argument (Tgt on a 2-variable domain) glued at one
equality point; gap 6 is now a **single 1-variable function on a compact
interval with one equality endpoint**, closeable by literally reusing the
same two certified techniques (Theorem-B/C-style away-from-corner interval
sweep + Round-16-style near-corner Taylor/derivative-sign argument) that are
already proved to work in this exact file, on a simpler target. No new
machinery is needed — only reapplication.

### 3. Crux corpus check

Per `crux_moves_documentation.md`, **geometry has no cruxes in the corpus**
(only number_theory/combinatorics/algebra). Queried `algebra` /
`inequalities-SOS-and-convexity` (155 cruxes) for tangent-line / derivative
/ equality-point techniques: the only genuinely analogous move is
**`aimo-0005`** ("bound a nonlinear term by the line tangent at the
equality point, chosen to also pass through a second boundary value, verify
by factoring the difference") — already identified and used by the
`-twopoint` sibling. No new analogous crux found; `aimo-0905`'s
"log-convexity forces max at endpoints" is the wrong direction (we want a
*min* forced to an endpoint, and via derivative sign, not convexity of a
log). Given the population's own Round-16 technique is already the closest
match and is native to this file, further crux search is not the priority.

### 4. Cheap-kill / pruning checks

- No parity/pigeonhole applicable (this is a continuous inequality).
- The "closed-form rational function" route is a genuine dead end (trisection
  obstruction), confirmed independently — do not re-attempt a Weierstrass/
  polynomial-SOS closed form for `D_1(B)` directly; any future attempt should
  go through interval arithmetic on the transcendental expression instead
  (as `mpmath.iv` already does successfully for `\mathrm{Tgt}$).
- The `-twopoint` file's `A_{\max}\approx1.0484` (curve continued past
  `B=\pi/3`) appears to be a numeric-continuation artifact, not the true
  domain-restricted endpoint — the true endpoint is exactly `(\pi/3,\pi/3)`.
  Flag this for correction; it does not affect any certified content, only
  the file's own numeric scan description.

## Report summary

- **Distinct openings**:
  1. **(Primary, recommended)** Reuse Theorem A's *explicit* closed form
     `A(B)=\arctan(-\sin B\cos2B/(2\cos^3B))` to write `D_1` as a genuine
     1-variable function of `B` on the compact interval `[B^\ast,\pi/3]`,
     and close `D_1\ge0` by splitting into (i) a certified interval sweep
     of `D_1>0$ on `[B^\ast+\delta,\pi/3]` (Theorem-B/C-style, easy, strong
     margin `\ge0.097` observed) and (ii) a certified derivative-sign sweep
     of `D_1'>c>0$ on `[B^\ast,B^\ast+\delta]` (Round-16-style Taylor/
     Lagrange-remainder near-corner argument) — **no concavity or
     unimodality needed at all**.
  2. (Fallback, more work) The concavity/secant-line mechanism as originally
     dispatched (`-twopoint` file) — still viable in principle but requires
     proving concavity of an implicit-curve function, strictly harder than
     opening 1 and not needed if opening 1 succeeds.
  3. (Dead end, do not pursue) Literal closed-form/polynomial/Weierstrass
     reduction of `D_1(B)` — blocked by the trisection/casus-irreducibilis
     obstruction (`\sin(\arctan(t)/3)` not algebraic in `t` via radicals),
     confirmed independently this round.

- **Candidate technique(s)**: interval-arithmetic branch-covering (`mpmath.iv`,
  as already used for Theorems B/C in `coordinate-bash-resultant-boundary-
  pointwise-tangent.md`) for the away-from-corner part; the Round-16 Taylor +
  certified-Lagrange-remainder (or, more simply here, a direct certified
  lower bound on `D_1'`) technique for the near-corner part. Both techniques
  are already proved to work in this population on this exact file's
  machinery — this is reapplication, not new invention.

- **Cheap-kill candidates**: none beyond the trisection-obstruction dead end
  documented above (rules out the polynomial/SOS route cheaply, saving a
  round of wasted effort).

- **Knowledge-base entries to use**: whichever KB entries the file already
  cites for interval-arithmetic branch-covering / Taylor-remainder positivity
  certification (used for Theorems B, C and the round-16 near-corner
  closure) — same toolkit, no new KB entry needed. (I did not find a
  geometry-specific KB entry beyond what's already cited in the file; the
  technique is generic real-analysis, not geometry-specific.)

- **Analogous past problems (cruxes)**: `aimo-0005` (already used/cited by
  the `-twopoint` sibling: tangent line pinned at equality point + second
  boundary point) — still the best match, no new crux found. Geometry has
  no cruxes in the corpus at all, so this is necessarily an algebra-domain
  borrow, exactly as the population has already been doing.

- **Prior progress**: `D_1(A^\ast)=0` exactly (certified), `D_2\in[1.10,1.97]`
  numerically (not yet closed-form), `D_1\ge0` numerically confirmed on the
  whole curve with the true range now identified as `[A^\ast,\pi/3]` (a
  correction/narrowing of the previously-cited `A_{\max}\approx1.0484`).
  Gap 6 is the sole remaining obstruction of the `-tangent` route's
  Reduction Lemma.

- **Dead ends (do not retry)**: (1) literal Weierstrass/polynomial closed
  form for `D_1(B)` — blocked by trisection (`\sin(\theta/3)` not radical in
  `\cos\theta`), confirmed independently this round via `sympy.expand_trig`
  leaving irreducible `\sin(\arctan(t)/3)` terms. (2) Concavity via
  finite-difference-only evidence is insufficient and, per the analysis
  above, is not even necessary — chasing an exact concavity proof is likely
  a wasted round given a strictly easier sufficient condition exists.

- **Small-case / intuition notes** (all numeric, i.e. conjectural until
  interval-arithmetic-certified): `D_1'(B^\ast)\approx4.626>0` (corner is a
  simple, non-degenerate zero with positive one-sided slope, not a cusp or
  higher-order tangency); `D_1'$ stays `\ge1.29` throughout
  `[B^\ast,B^\ast+0.1]`; `D_1$'s single interior maximum
  `\approx0.4054$ at `B\approx1.030$ and its value at the far endpoint
  `D_1(\pi/3)\approx0.3977>0` are both comfortably positive, with no
  near-zero dip anywhere except the single corner endpoint. This strongly
  supports (as conjecture, pending certification) that `D_1\ge0` throughout
  `[B^\ast,\pi/3]`, vanishing only at `B^\ast`, via the much weaker
  "positive derivative at the corner + bounded-away-from-zero elsewhere"
  argument rather than global concavity.
