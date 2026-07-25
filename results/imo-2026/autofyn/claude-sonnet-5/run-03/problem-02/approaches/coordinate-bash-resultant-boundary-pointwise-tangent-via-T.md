## Status
partial

## Approaches tried
- **Round 20 — forked from `coordinate-bash-resultant-boundary-pointwise-tangent`
  (identical Elo/history at fork point; diverges only in the mechanism used
  to close the shared Open gap 7).** Both this file and its sibling target
  the exact same remaining obstruction: `G(\beta_1)\ge0` on the residual
  Case-(b) sub-case `P>0\wedge E<0` (certified equivalent, via
  `case-b-e-lt-0-t-factorization.md`, to `T:=B_c^2X_0-E^2\ge0`), which
  round 19 showed is also the one remaining piece of Case (a). The sibling
  closes this by Taylor-expanding the *trigonometric* function `G(\beta_1)`
  (or `T`) directly in `(A,B)` near the corner
  `(A^\ast,\beta_0(A^\ast))`, `A^\ast=3\arcsin(\sqrt6/4)-\pi/2`. **This
  file instead expands the certified rational-polynomial form**
  `T=c(dQ_1-cR_0)/(4\sin^2(A+B))`, `Q_1=-4st\cdot q_1(\sigma,\tau)`,
  `R_0=r_0(\sigma,\tau)` (`\sigma=\sin^2A,\tau=\sin^2B`, explicit
  degree-(4,2)/(4,3) polynomials, `case-b-e-lt-0-t-factorization.md`),
  Taylor-expanding `q_1,r_0` **directly as polynomials in
  `(\sigma,\tau)`** around `(\sigma^\ast,\tau^\ast):=(\sin^2A^\ast,
  \sin^2\beta_0(A^\ast))`, avoiding trig-identity manipulation in the
  expansion step (at the cost of higher polynomial degree). This is a
  genuine alternative mechanism for the identical target, not a
  reformulation of the same computation — worth running in parallel per
  the round-12 "two distinct untried levers, field as a copy" precedent,
  since it is not obvious in advance which expansion (trigonometric,
  low-degree but keeps trig structure; or polynomial, degree-(4,3) but
  algebraically clean) yields an easier-to-certify Lagrange-remainder
  bound.
- **Independently reconfirmed this round (outline-reviewer, fresh mpmath,
  60 digits):** `T(A^\ast,\beta_0(A^\ast))=7.78\times10^{-62}\approx0`
  exactly; `X_0(A^\ast,\beta_0(A^\ast))=\cos^2(\beta_0(A^\ast))=3/8`
  exactly (to 60 displayed digits); and along the active boundary curve
  `B=\beta_0(A)`, `T(A^\ast+\varepsilon,\beta_0(A^\ast+\varepsilon))/
  \varepsilon\to\approx1.4774` as `\varepsilon\to0^+`
  (`\varepsilon\in\{10^{-2},\ldots,10^{-6}\}`, ratio stable to 4 significant
  figures) — confirming **linear, not quadratic**, vanishing at the corner
  along the domain's own active edge. This is the same corner and the same
  order-of-vanishing diagnosis as the sibling file and as
  `lemmas/d1-nonnegative-on-boundary-curve.md`.

### Round 20 (this build) — the `(\sigma,\tau)`-rational route: an exact
### algebraic proof of `T(A^\ast,B^\ast)=0`, plus a diagnosed (not yet
### closed) directional-derivative gradient

**New result 1 (exact rational-arithmetic proof of the corner value,
independent of the sibling's trig-identity route).**

*Step (a): exact values `\sigma^\ast=\sin^2A^\ast=5/32`,
`\tau^\ast=\sin^2B^\ast=5/8`, derived from the already-certified
`u`-substitution.* Reuse (not re-derive) the certified substitution
`u:=A/3+\pi/6` from `lemmas/d1-nonnegative-on-boundary-curve.md` §0(a),
which gives, for `A=3u-\pi/2` and `\beta_0(A)=\pi/2-u`:
$$\cos A=\sin3u,\qquad \sin A=-\cos3u,\qquad \sin\beta_0(A)=\cos u,\qquad
\cos\beta_0(A)=\sin u .$$
Hence, writing `s_u:=\sin u,\ c_u:=\cos u`,
$$\sigma=\sin^2A=\cos^2(3u),\qquad \tau=\sin^2\bigl(\beta_0(A)\bigr)=
\cos^2u .$$
(Both are elementary consequences of the boxed identities above; no new
trig manipulation needed beyond squaring.) The certified closed form
`A^\ast=3\arcsin(\sqrt6/4)-\pi/2` (`lemmas/d1-nonnegative-on-boundary-
curve.md`, "(A-STAR)") corresponds to `u^\ast=\arcsin(\sqrt6/4)`, for which
that same lemma establishes **exactly** `\sin^2u^\ast=3/8` (§0(f): "since
`\sin^2u^\ast=3/8\Rightarrow\sin u^\ast=\sqrt{3/8}`"). Hence
`\cos^2u^\ast=1-3/8=5/8`, giving
$$\tau^\ast=\cos^2u^\ast=\frac58 .$$
For `\sigma^\ast`, use the triple-angle identity `\cos3u=\cos u(4\cos^2u-3)$
(elementary, from `\cos3u=4\cos^3u-3\cos u`). At `u=u^\ast`,
`\cos^2u^\ast=5/8`, so
$$\cos(3u^\ast)=\cos u^\ast\Bigl(4\cdot\tfrac58-3\Bigr)=\cos u^\ast\cdot
\Bigl(-\tfrac12\Bigr)=-\tfrac12\cos u^\ast,$$
hence
$$\sigma^\ast=\cos^2(3u^\ast)=\tfrac14\cos^2u^\ast=\tfrac14\cdot\tfrac58=
\frac5{32}.$$
Both `(\sigma^\ast,\tau^\ast)=(5/32,\,5/8)$ are exact rational numbers —
this is itself notable: the corner point maps to a rational point in
`(\sigma,\tau)` coordinates, even though `A^\ast,B^\ast` themselves are
irrational (transcendental, in fact — `\arcsin(\sqrt6/4)` is not a
rational multiple of `\pi`, by the standard Niven-type argument, though
this fact is not needed anywhere below).

*Step (b): `q_1(\sigma^\ast,\tau^\ast)` and `r_0(\sigma^\ast,\tau^\ast)` are
exact rationals.* Substituting the exact rationals `\sigma^\ast=5/32,\
\tau^\ast=5/8` into the certified degree-`(4,2)` and degree-`(4,3)`
polynomials `q_1,r_0$ (`lemmas/case-b-e-lt-0-t-factorization.md`) is a
finite rational-arithmetic computation (every coefficient and every power
of `5/32,5/8` is a rational number, and the whole expression is a finite
sum of products of rationals):
$$q_1(\sigma^\ast,\tau^\ast)=\frac{75}{131072},\qquad
r_0(\sigma^\ast,\tau^\ast)=-\frac{125}{262144}.$$
(Verified in a fresh `sympy.Rational` session with exact fractions
throughout — no floating point anywhere in this step; independently
confirmed by high-precision `mpmath` evaluation at `A^\ast,B^\ast$ to 100
digits, matching the fixed rationals to full displayed precision.) In
particular `q_1(\sigma^\ast,\tau^\ast)>0$ and `r_0(\sigma^\ast,\tau^\ast)
<0`.

*Step (c): `d\,Q_1-c\,R_0=0` at the corner, exactly, via a rational
squaring argument.* Write `s^\ast:=\sin A^\ast,\ c^\ast:=\cos A^\ast,\
t^\ast:=\sin B^\ast,\ d^\ast:=\cos B^\ast`, so `(s^\ast)^2=\sigma^\ast=
5/32`, `(c^\ast)^2=1-\sigma^\ast=27/32`, `(t^\ast)^2=\tau^\ast=5/8`,
`(d^\ast)^2=1-\tau^\ast=3/8` — all exact rationals, and all four of
`s^\ast,c^\ast,t^\ast,d^\ast$ are strictly positive (since
`A^\ast\in(0,\pi/2)$, established exactly in
`lemmas/d1-nonnegative-on-boundary-curve.md` §0(f), and `B^\ast=
\beta_0(A^\ast)\in(0,\pi/2)$ likewise). By definition,
$$d^\ast Q_1^\ast-c^\ast R_0^\ast=-4\,s^\ast t^\ast d^\ast\,
q_1(\sigma^\ast,\tau^\ast)-c^\ast\,r_0(\sigma^\ast,\tau^\ast).$$
Both terms have a definite, and in fact equal, sign: the first term is
`-4\times(\text{positive})\times q_1(\sigma^\ast,\tau^\ast)$ with
`q_1(\sigma^\ast,\tau^\ast)=75/131072>0`, so the first term is **negative**;
the second term is `-c^\ast\times r_0(\sigma^\ast,\tau^\ast)` with
`r_0(\sigma^\ast,\tau^\ast)=-125/262144<0` and `c^\ast>0`, so
`-c^\ast r_0(\sigma^\ast,\tau^\ast)>0`, i.e. the claimed identity
`d^\ast Q_1^\ast-c^\ast R_0^\ast=0` is equivalent to
$$-4\,s^\ast t^\ast d^\ast\,q_1(\sigma^\ast,\tau^\ast)=c^\ast\,
r_0(\sigma^\ast,\tau^\ast),$$
a statement of the form `(\text{negative})=(\text{negative})` — both sides
have the same sign, so this equality of two negative reals holds **iff**
their squares agree (squaring is injective on negatives-to-positives in
the sense that if `x<0,y<0` and `x^2=y^2` then `x=y`, since `x=-\sqrt{x^2},
\ y=-\sqrt{y^2}`). Squaring converts the claim into a **pure rational
arithmetic identity**, with every quantity replaced by its (rational)
square:
$$16\,(s^\ast)^2(t^\ast)^2(d^\ast)^2\,q_1(\sigma^\ast,\tau^\ast)^2\ \overset?=\
(c^\ast)^2\,r_0(\sigma^\ast,\tau^\ast)^2,$$
i.e.
$$16\cdot\frac5{32}\cdot\frac58\cdot\frac38\cdot\Bigl(\frac{75}{131072}
\Bigr)^2\ \overset?=\ \frac{27}{32}\cdot\Bigl(\frac{125}{262144}\Bigr)^2.$$
Direct computation (exact rational arithmetic, independently checked in a
fresh `sympy.Rational` session): both sides equal
$$\frac{421875}{2199023255552}$$
**exactly**, confirming the identity. Hence
$$d^\ast Q_1^\ast-c^\ast R_0^\ast=0\qquad\text{exactly},$$
and since `T=c(dQ_1-cR_0)/(4\sin^2(A+B))` with `\sin(A^\ast+B^\ast)=
\sin(2u^\ast)=2s_{u^\ast}c_{u^\ast}\ne0` (as `u^\ast\in(\pi/6,\pi/3)`, so
neither `\sin u^\ast` nor `\cos u^\ast` vanishes — already certified,
`lemmas/d1-nonnegative-on-boundary-curve.md` §0(e)-(f)),
$$\boxed{\ T(A^\ast,B^\ast)=0\quad\text{exactly}.\ }$$

**This is a genuinely new, fully rigorous proof of the corner value**,
independent of and structurally different from the sibling
`coordinate-bash-resultant-boundary-pointwise-tangent.md`'s planned
trigonometric-`G`-expansion route: it works entirely through the certified
rational polynomials `q_1,r_0` in `(\sigma,\tau)`-space, reduces to finite
rational arithmetic once `\sigma^\ast,\tau^\ast$ are pinned as rationals
(itself a clean consequence of the already-certified `u`-substitution and
`\sin^2u^\ast=3/8` fact), and needs no `sympy.simplify` black box or
high-precision numeric coincidence-detection — every step above is
hand-checkable rational arithmetic. Independently spot-checked against the
100-digit `mpmath` evaluation of `T(A^\ast,B^\ast)` directly from its raw
trigonometric definition (`\approx-1.79\times10^{-102}`, i.e. `0` to the
full working precision).

**New result 2 (gradient of `T` at the corner, diagnostic — NOT a proof of
positivity).** Central finite-difference computation (own fresh `mpmath`,
`dps=50`, step `h=10^{-20}`) of the raw partial derivatives of `T(A,B)` at
`(A^\ast,B^\ast)`:
$$\frac{\partial T}{\partial A}(A^\ast,B^\ast)\approx1.69903978276768852919,
\qquad
\frac{\partial T}{\partial B}(A^\ast,B^\ast)\approx0.66484165412648681577.$$
Along the domain's active boundary curve `B=\beta_0(A)` (`\beta_0'(A)=
-1/3`), the one-sided directional derivative of `T` as `A\to A^{\ast+}`
is
$$\frac{d}{dA}\Bigl[T(A,\beta_0(A))\Bigr]_{A=A^\ast}=\frac{\partial T}
{\partial A}-\frac13\frac{\partial T}{\partial B}\approx1.69903978\ldots-
\frac{0.66484165\ldots}3\approx1.47742589806,$$
matching this round's independently-reconfirmed ratio
`T(A^\ast+\varepsilon,\beta_0(A^\ast+\varepsilon))/\varepsilon\to1.4774
\ldots` **exactly** (both computed from the raw trigonometric definitions,
one via a direct one-sided secant limit, the other via the two-partial
chain rule — an internal cross-check that the linear-vanishing diagnosis
is numerically self-consistent). This confirms `T` vanishes to exactly
first order at the corner along the active edge, with a strictly positive
one-sided directional derivative `\approx1.477>0` — the qualitative shape
needed for a Lagrange-remainder argument of the `D_1`-lemma's style
(nonzero first derivative, not a tangential/quadratic degeneracy) — but
this is a **numerical finite-difference computation, not a certified
interval-arithmetic bound**, and it is only a *derivative value*, not yet
assembled into the actual near-corner Lagrange-remainder inequality nor
glued to an away-from-corner sweep.

## Current best
Same certified Reduction Lemma and case-tree closure as
`coordinate-bash-resultant-boundary-pointwise-tangent.md` (hypothesis (A)
`Tgt>0` closed round 16; hypothesis (B) `D_1\ge0` on the boundary curve
closed rounds 17-18; Case (b) closed except the residual `P>0\wedge E<0`
sub-case, identified round 19 as the same residual piece needed for Case
(a) too). The one open target is `T\ge0` (equivalently `G(\beta_1)\ge0`)
on `D\cap\{P>0,E<0\}`, `D=\{0<A\le\pi/2,0<B\le C,B>\beta0(A),
\cos^2B<X_0(A,B)<\cos^2\beta_0(A)\}`.

**Genuinely new and fully proved this round:** `T(A^\ast,\beta_0(A^\ast))
=0` **exactly**, via a self-contained rational-arithmetic argument through
the `(\sigma,\tau)`-polynomial factorization (New result 1 above) — this
is an independent, differently-structured re-derivation of the same fact
the sibling file's trig-identity route also needs, giving the population
two independently-verified proofs of the corner value via genuinely
different mechanisms (a useful robustness check per the round-20 dispatch
instruction to work independently of the sibling).

**Still open (the actual remaining gap, honestly unclosed this round):**
1. A **certified** (not merely finite-difference-numeric) lower bound on
   the directional derivative of `T` along the active boundary curve near
   `A^\ast`, e.g. via `mpmath.iv` directed-rounding evaluation of `\partial
   T/\partial A-\tfrac13\partial T/\partial B` over a small interval
   `[A^\ast,A^\ast+\delta]$ (mirroring `lemmas/d1-nonnegative-on-boundary-
   curve.md`'s Step 2 "Deriv-bound" exactly, but for `T` instead of `D_1`,
   and — since the corner here is a genuine 2-D domain corner, not merely a
   1-D curve as `D_1`'s was — the bound must also account for the
   direction *transverse* to the active curve, into the interior of
   `D\cap\{P>0,E<0\}`, which the current work has NOT yet analyzed at all).
2. A certified Lagrange-remainder bound converting New result 2's
   numerical derivative value into a genuine `T(A,B)\ge c_1(A-A^\ast)+
   c_2(B-\beta_0(A^\ast))-(\text{certified remainder})>0` inequality valid
   on an explicit neighbourhood of the corner within the true 2-D domain
   (not yet attempted).
3. A certified `mpmath.iv` value sweep of `T` over `D\cap\{P>0,E<0\}`
   away from the corner (`|A-A^\ast|>\delta`) — this round's math-explorer
   reports only an uncertified coarse numeric estimate (`T_{\min}\approx
   0.0187` at `\varepsilon=\delta=10^{-2}`), not a certified interval-
   arithmetic sweep; building this is comparatively routine (same
   machinery as `lemmas/d1-nonnegative-on-boundary-curve.md`'s Step 3) but
   has not been executed this round.
4. The gluing step (MVT/Lagrange-remainder argument combining 1-3) has not
   been assembled.

**Why this is honestly reported as `partial`, not `solved`:** the target
domain for `T` is a genuine 2-D region (not a 1-D curve, unlike `D_1`'s
domain `\mathcal C`), so the corner is a true 2-D corner where the
domain itself pinches to zero width — a directional-derivative argument
here needs to control behavior in a whole cone of directions into the
domain, not just along one curve, which is strictly more delicate than
either of the two previously-closed corner arguments (`Tgt`'s tangent-cone
argument, round 16; `D_1`'s single-curve MVT argument, rounds 17-18). This
additional 2-D structure is not yet worked out, and claiming `T\ge0`
throughout `D\cap\{P>0,E<0\}` on the strength of New results 1-2 alone
would be exactly the kind of unproved logical leap CLAUDE.md's rigor rules
prohibit (analogous to the round-17/18 mis-citations this population has
twice already caught and corrected). The correct, honest status is:
**one genuinely new fully-proved sub-lemma this round (corner value `T=0`,
via an independent rational-arithmetic mechanism), the diagnostic
groundwork for the remaining Lagrange-remainder argument laid out with
real numeric values, but the full near-corner-plus-sweep closure not yet
built.**

## Full proof
Not present — Status is `partial`; the open gaps above (a certified 2-D
directional-derivative/Lagrange-remainder bound near the corner, a
certified interval sweep away from it, and the gluing step) remain.

## Promotable lemmas

### `T(A^\ast,\beta_0(A^\ast))=0` via the `(\sigma,\tau)`-rational
### factorization (New result 1 above)

**Statement.** Let `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` (the certified
closed form of `lemmas/d1-nonnegative-on-boundary-curve.md`), `B^\ast:=
\beta_0(A^\ast)=(\pi-A^\ast)/3`. Then, in the notation of
`lemmas/case-b-e-lt-0-t-factorization.md`,
$$\sigma^\ast:=\sin^2A^\ast=\frac5{32},\qquad
\tau^\ast:=\sin^2B^\ast=\frac58,$$
$$q_1(\sigma^\ast,\tau^\ast)=\frac{75}{131072},\qquad
r_0(\sigma^\ast,\tau^\ast)=-\frac{125}{262144},$$
and
$$T(A^\ast,B^\ast)=0\qquad\text{exactly}.$$

**Proof.** Exactly as in New result 1 above (Steps (a)-(c)): `\sigma^\ast,
\tau^\ast` are computed from the certified `u`-substitution and the
certified fact `\sin^2u^\ast=3/8$ of `lemmas/d1-nonnegative-on-boundary-
curve.md` §0(f); `q_1(\sigma^\ast,\tau^\ast),r_0(\sigma^\ast,\tau^\ast)`
are exact finite rational-arithmetic evaluations of the certified
polynomials of `lemmas/case-b-e-lt-0-t-factorization.md`; the vanishing of
`d^\ast Q_1^\ast-c^\ast R_0^\ast` reduces, via a same-sign argument, to the
rational identity
`16\cdot\frac5{32}\cdot\frac58\cdot\frac38\cdot(75/131072)^2=
\frac{27}{32}\cdot(125/262144)^2`, both sides equal `421875/2199023255552`
exactly; and `T=c(dQ_1-cR_0)/(4\sin^2(A+B))` with the nonzero denominator
already certified. `\blacksquare`

This lemma is reusable by any future attempt at the `T\ge0`/`-q_1,-r_0`
target: it gives a **second, independent** (rational-arithmetic, not
trig-identity) proof of the corner value, alongside whatever the sibling
`-pointwise-tangent` file's own trig-based derivation produces — useful as
a cross-check, and directly reusable as the base case ("value 0 at the
corner") of any future Lagrange-remainder/MVT gluing argument for `T`, in
the same role `lemmas/d1-nonnegative-on-boundary-curve.md`'s Step 0 played
for `D_1`.

**Not yet submitted as a separate `lemmas/` file** — recommend the
proof-reviewer certify it as `lemmas/t-corner-value-exact-via-sigma-tau.md`
if independently re-verified, since it is a complete, self-contained, fully
rigorous result on its own (independent of whether the surrounding `T\ge0`
gap is ever closed).
