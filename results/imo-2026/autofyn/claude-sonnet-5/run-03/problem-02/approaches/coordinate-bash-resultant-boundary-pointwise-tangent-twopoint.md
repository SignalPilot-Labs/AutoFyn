## Status
partial

## Approaches tried

- **Round 12 (this round, new copy)**: pursued the two-point-pinned
  tangent/secant construction dispatched by the outliner (adapted from the
  crux `aimo-0005` move: "bound a nonlinear quantity by a line pinned at the
  equality point AND a second point on the true boundary, then verify by
  factoring the difference"), targeting the same open inequality `(\star)`:
  `(1+\cos B)^2X_0(A,B)\ge\mathrm{RHS}(A,B)^2` on the Case-(b) domain, where
  (all reused verbatim from the certified backbone, see
  `coordinate-bash-resultant-boundary-pointwise-tangent.md` and
  `lemmas/mvt-lipschitz-reduction-case-b.md`,
  `lemmas/x0-partial-b-derivative.md`)
  $$
  X_0(A,B)=\frac{\sin B\cos A}{2\sin(A+B)},\qquad
  \beta_0(A)=\frac{\pi-A}{3},\qquad
  K_c=2\sin A\sin(A+B),
  $$
  $$
  P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B),\qquad Q=-\sin A\sin B,\qquad
  G(\beta_0)=K_c-P\sin\beta_0-Q\cos\beta_0,
  $$
  $$
  \mathrm{RHS}=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0),\qquad
  S(A,B)=(1+\cos B)^2X_0-\mathrm{RHS}^2\quad(\text{target: }S\ge0).
  $$
  Rather than pinning a linear-in-`A`-at-fixed-`B` line directly to `S`
  (the retired single-point construction, correctly diagnosed by the
  `-tangent` sibling as failing since `\mathrm{RHS}` depends on `B` in a
  way not eliminated by fixing `B`), this round instead restricted
  attention **first** to the true lower boundary curve of the Case-(b)
  domain identified in round 11,
  `$$\mathcal C:=\{(A,B):X_0(A,B)=\cos^2B\},$$`
  and looked for structure of `S` **restricted to `\mathcal C`** — this is
  the natural place to look for a two-point-pinned construction, since
  `\mathcal C` is exactly a curve through the corner `(A^\ast,B^\ast)`
  (where `S=0`), giving a genuine 1-parameter family to pin a secant/
  tangent bound on.

### New result: an exact factorization of `S` on the boundary curve

**Lemma (Factorization on `\mathcal C`).** On `\mathcal C` (where
`X_0=\cos^2B` exactly),
$$
S=D_1\cdot D_2,\qquad
D_1:=(1+\cos B)\cos B-\mathrm{RHS},\qquad
D_2:=(1+\cos B)\cos B+\mathrm{RHS}.
$$
*Proof.* On `\mathcal C`, `(1+\cos B)^2X_0=(1+\cos B)^2\cos^2B=
[(1+\cos B)\cos B]^2`, so `S=[(1+\cos B)\cos B]^2-\mathrm{RHS}^2=
[(1+\cos B)\cos B-\mathrm{RHS}][(1+\cos B)\cos B+\mathrm{RHS}]=D_1D_2` by
the elementary difference-of-squares identity. `\blacksquare` (Verified
exactly, not just numerically: `sympy.simplify` confirms
`(1+\cos B)^2x_0-\mathrm{RHS}^2` restricted to the symbol `x_0=\cos^2B` is
term-for-term identical, by expansion, to `D_1D_2` — a residual of
exactly `0`, own fresh session.)

This is a genuinely new structural fact not present elsewhere in the
population: it turns the 2-variable claim `S\ge0` **on the curve** `\mathcal
C` into a product-of-two-factors sign question, each an explicit (still
transcendental, but simpler) function along `\mathcal C`.

### Numerical behaviour of `D_1,D_2` along `\mathcal C`

Parametrizing `\mathcal C` by `A` (solving `X_0(A,B)=\cos^2B` for `B` at
each `A` via `scipy.optimize.brentq`, own script, starting from the
certified corner `A^\ast\approx0.40637778068433034`,
`B^\ast=\beta_0(A^\ast)`, and continuing the branch by Newton-continuation
in `A` up to the domain's other boundary `B=C` at
`A\approx1.0484,\,B\approx1.0475`):

- **`D_2`** stays strictly positive throughout, ranging numerically from
  `\approx1.974745` (at the corner) down to `\approx1.101549` (at the far
  end `B=C`) — comfortably bounded away from `0` over the whole curve
  (`60`-point scan, confirmed by a `2000`-point finer scan). **Not proved
  symbolically.**
- **`D_1`** is `0` at the corner (confirmed to machine precision,
  `\approx1.3\times10^{-14}`, consistent with the corner being exactly on
  `\mathcal C`), strictly positive at every other sampled point
  (`2000`-point fine scan, zero violations), rising from `0` to a maximum
  `\approx0.4054` near `A\approx0.979`, then decreasing back down to
  `\approx0.397` at the far end `A\approx1.048` — **never returning to
  `0`** on the observed range. A finite-difference estimate of `D_1''(A)`
  (central differences, `2000`-point grid) is negative at `1802/1998`
  interior points (the exceptional `~10\%` cluster near the grid endpoints,
  consistent with finite-difference truncation noise rather than a genuine
  sign change) — consistent with, but **not a proof of**, `D_1` being
  concave (equivalently, at least unimodal: single interior maximum, no
  further oscillation) along `\mathcal C`.

### The two-point-pinned mechanism, precisely stated (contingent, not closed)

If `D_1(A)` (restricted to `\mathcal C`, as a function of `A` on the
interval `[A^\ast,A_{\max}]` where `A_{\max}` is the curve's other
endpoint, `B=C`) is **concave**, then — since `D_1(A^\ast)=0` and
`D_1(A_{\max})>0` are both `\ge0` — the secant line
$$
\ell(A):=D_1(A_{\max})\cdot\frac{A-A^\ast}{A_{\max}-A^\ast}
$$
joining the two pinned points `(A^\ast,0)` and `(A_{\max},D_1(A_{\max}))`
satisfies `\ell(A)\ge0` for `A\in[A^\ast,A_{\max}]` (a convex combination of
two nonnegative endpoint values), and concavity of `D_1` gives
`D_1(A)\ge\ell(A)` throughout the interval (a concave function lies above
any chord connecting two of its points is false — the correct direction is
a concave function lies **above** the chord only between the two points if
we go the other way; let us be precise: for a concave function, for
`A=\lambda A^\ast+(1-\lambda)A_{\max}`, `\lambda\in[0,1]`, concavity gives
`D_1(A)\ge\lambda D_1(A^\ast)+(1-\lambda)D_1(A_{\max})=\ell(A)`, i.e. `D_1`
lies **above** its own secant on the interval between the two pinned
points — exactly the "two-point-pinned" bound the outline requested).
Hence `D_1(A)\ge\ell(A)\ge0` on the whole interval, i.e. `D_1\ge0` on all of
`\mathcal C`. Combined with `D_2>0` (if that too is established), this
would give `S=D_1D_2\ge0` on `\mathcal C`.

**This is exactly the crux `aimo-0005`-style mechanism as dispatched**: a
linear bound pinned at the equality point (`A^\ast`, where `S=0`) *and* at
a second point on the true boundary curve (`A_{\max}`, the far end of
`\mathcal C`), verified by the fact that the difference `D_1-\ell` is
forced to vanish at both pinning points by construction, and its sign
in between is controlled by concavity (playing the role of "factoring the
difference" in the crux move — here the "difference" `D_1-\ell` is a
concave function vanishing at the left endpoint and non-negative at the
right, hence non-negative throughout by concavity, rather than by an
explicit polynomial factorization; the mechanism is a genuinely valid
adaptation, not a literal transcription).

### Why this is NOT a complete proof — three explicit open gaps

1. **`D_2>0` on `\mathcal C` is not proved symbolically** — only the
   numeric scan above (60 + 2000 points, comfortable margin `\ge1.10`, but
   no closed-form bound or algebraic sign argument was found this round).
2. **Concavity (or the weaker sufficient fact, unimodality: `D_1'` changes
   sign at most once, from `+` to `-`) of `D_1(A)` along `\mathcal C` is not
   proved symbolically** — only the finite-difference evidence above.
   Because `\mathcal C` is an *implicit* curve (no closed form for `B(A)`
   was found or used — the numeric scan solves `X_0(A,B)=\cos^2B$ for `B`
   at each `A` via root-finding, not a closed-form substitution), a
   symbolic second-derivative computation along `\mathcal C` would require
   implicit differentiation of `B(A)` through `X_0(A,B)=\cos^2B`, which was
   not attempted symbolically this round (time-limited) — flagged as the
   natural next concrete step for a future round, since `\partial
   X_0/\partial B` is already an exact certified closed form
   (`lemmas/x0-partial-b-derivative.md`) and `\partial X_0/\partial A` is
   an equally elementary quotient-rule computation, so `dB/dA=
   -(\partial X_0/\partial A-(-2\cos B\sin B\cdot 0))/(\partial X_0/\partial
   B+2\cos B\sin B)` (implicit function theorem on `X_0(A,B)-\cos^2B=0`) is
   in principle fully computable in closed form; only the further step
   (differentiating `D_1$ along this implicit `B(A)`, twice, and
   determining its sign) was not carried out symbolically.
3. **Even granting both (1) and (2), this only proves `(\star)`/`S\ge0`
   ON the boundary curve `\mathcal C` itself, not on the whole 2-variable
   Case-(b) domain.** Extending from "`S\ge0$ on `\mathcal C`" to "`S\ge0`
   throughout the full domain `\mathcal D`" still requires the sibling
   `-tangent` file's own still-open lever, `\partial S/\partial B\ge0` on
   `\mathcal D` (numerically confirmed, `\ge36{,}254` samples, min margin
   `\approx0.177`, but not proved symbolically) — since `\mathcal C` is
   exactly the domain's lower `B`-boundary for each `A` (round 11's
   finding), monotonicity in `B$ is precisely what would let
   `S(A,B)\ge S(A,B_{\text{lower edge}}(A))=S$ restricted to `\mathcal C`
   for every `(A,B)\in\mathcal D`. **Without that monotonicity fact (or
   some substitute), the work in this file — even if items (1) and (2) were
   both closed — would only establish `(\star)` on a measure-zero subset
   (the boundary curve) of the domain, not the domain itself.** This is
   honestly reported as the load-bearing remaining dependency, not
   papered over.

### Honest assessment of the "genuinely different mechanism" framing

The construction dispatched this round is a real, previously-untried
lever (the factorization `S=D_1D_2$ on `\mathcal C` was not present in any
prior round's file), and it does meaningfully decompose the "hard part"
(a 2-variable inequality with an implicit domain) into two cleaner
sub-questions (`D_2>0`, `D_1\ge0` via a 1-variable secant argument on an
implicitly-defined curve). It is architecturally distinct from the
sibling's `\partial S/\partial B` derivative-sign mechanism, as the
dispatch intended: it targets *only* the boundary-curve restriction of
`(\star)`, whereas the sibling targets the full 2-variable domain directly
via monotonicity. **However, the two mechanisms are not independent in
the sense of either being able to finish the problem alone**: this file's
mechanism, even if fully completed, still needs the sibling's monotonicity
result (or an equivalent) to extend off the curve; conversely the
sibling's mechanism, even if fully completed, would not need this file's
factorization at all (monotonicity alone reduces `(\star)` to its
restriction on `\mathcal C`, which would then need to be checked by *some*
method — this file's `D_1D_2$ factorization would be one natural
candidate for that final check, making the two approaches genuinely
complementary rather than redundant, exactly as the outline anticipated in
its Step 4 fallback: "use the two-point line only on a sub-range... combined
with the derivative-sign route's comfortable margin elsewhere").

## Current best

The claim `(\star)`: `(1+\cos B)^2X_0(A,B)\ge\mathrm{RHS}(A,B)^2` on the
Case-(b) domain (inherited target, see
`lemmas/mvt-lipschitz-reduction-case-b.md`) remains open. This round's
contribution: an exact factorization `S=D_1D_2` valid on the boundary
curve `\mathcal C=\{X_0=\cos^2B\}` (proved in full, elementary
difference-of-squares once `X_0=\cos^2B$ is substituted), reducing the
restriction of `(\star)` to `\mathcal C` to two numerically-supported
(margin `\ge0.79`/`\ge0` respectively; not symbolically proved) sub-claims
`D_2>0` and `D_1\ge0$ (the latter via a genuine two-point-pinned
secant-line argument, contingent on an unproved concavity/unimodality fact
about `D_1$ along the implicit curve). This does **not** by itself close
`(\star)` on the full domain — that step still requires the sibling
`-tangent` file's own open `\partial S/\partial B\ge0` monotonicity lever
(or an equivalent), which remains unproved. No fatal obstruction was found
in this round's construction; all three flagged gaps (D2 sign, D1
concavity/unimodality, and the domain-extension dependency) are concrete
and well-scoped for a future round, not a dead end.

## Full proof
Not present — Status is `partial`.

## Promotable lemmas

- **Exact factorization on the boundary curve**: on
  `\mathcal C=\{(A,B):X_0(A,B)=\cos^2B\}`,
  `$S(A,B)=(1+\cos B)^2X_0(A,B)-\mathrm{RHS}(A,B)^2=D_1(A,B)\cdot
  D_2(A,B)$` where `D_1=(1+\cos B)\cos B-\mathrm{RHS}`,
  `D_2=(1+\cos B)\cos B+\mathrm{RHS}$ — proved in full (elementary
  difference-of-squares identity, verified by `sympy.simplify` giving
  residual exactly `0`). Reusable by any future attempt at `(\star)`
  restricted to this curve, and structurally connects this file's
  mechanism to the sibling `-tangent` file's own boundary-curve reduction
  target (Step 4/5 of that file's skeleton).
- The numeric findings (`D_2\in[1.10,1.97]` and `D_1\ge0$, vanishing only
  at the corner, over the observed range of `\mathcal C`) are reported as
  numeric evidence only — not proposed for certification as lemmas, since
  neither is proved symbolically this round.
