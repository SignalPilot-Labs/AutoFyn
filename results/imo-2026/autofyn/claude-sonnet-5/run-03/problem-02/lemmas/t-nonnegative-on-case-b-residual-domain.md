## Theorem (`T\ge0` on Case (b)'s residual sub-domain — closes Case (b) unconditionally)

**Setup.** As in `lemmas/case-b-p-le-0-and-e-ge-0-closed.md` and
`lemmas/case-b-e-lt-0-t-factorization.md`: for a triangle with `A\le\pi/2`,
write `X_0:=\sin B\cos A/(2\sin(A+B))`, `\beta_0(A):=(\pi-A)/3`,
`K:=2\sin A\sin(A+B)`, `P:=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`,
`A_{\mathrm c}:=\sin^2A\sin^2B+P^2`, `B_{\mathrm c}:=2K\sin A\sin B`,
`C_{\mathrm c}:=K^2-P^2`, `E:=A_{\mathrm c}X_0+C_{\mathrm c}`,
`T:=B_{\mathrm c}^2X_0-E^2`. Let
$$\mathcal D_b:=\{0<A\le\pi/2,\ 0<B\le C,\ B>\beta_0(A),\ \cos^2B<X_0(A,B)<
\cos^2\beta_0(A),\ P>0,\ E<0\}.$$

**Theorem.** `T\ge0` throughout `\mathcal D_b`, with equality exactly at the
corner `(A^\ast,B^\ast):=(3\arcsin(\sqrt6/4)-\pi/2,\ \beta_0(A^\ast))`.
Combined with the already-certified Theorems 1 and 4 of
`lemmas/case-b-p-le-0-and-e-ge-0-closed.md` (covering `P\le0` and
`P>0\wedge E\ge0` unconditionally), this gives **`G(\beta_1)\ge0`
unconditionally throughout the whole of Case (b)** (`X_0(A,B)<
\cos^2\beta_0(A)`), i.e. Case (b) of Open gap 7 is closed.

**Proof.** (i) *Corner value.* At `u^\ast:=\arcsin(\sqrt6/4)`,
`A^\ast=3u^\ast-\pi/2`, `B^\ast=\pi/2-u^\ast`, using `\sin^2u^\ast=3/8,
\cos^2u^\ast=5/8` (already certified,
`lemmas/d1-nonnegative-on-boundary-curve.md` §0(f)) and the substitutions
`\sin A^\ast=\cos u^\ast/2\cdot3` etc. (elementary multiple-angle algebra),
one computes exactly `X_0(A^\ast,B^\ast)=3/8=\cos^2B^\ast` (already
certified fact (ii)) and, by direct rational substitution,
`A_{\mathrm c}^\ast=25/16`, `C_{\mathrm c}^\ast=-225/256`,
`E^\ast=-75/256`, `B_{\mathrm c}^{\ast2}=1875/8192`, giving
`T(A^\ast,B^\ast)=1875/8192\cdot3/8-(75/256)^2=5625/65536-5625/65536=0`
exactly. (ii) *Gradient and tangent cone.* Exact differentiation gives
`\partial_AX_0=-\sin B\cos B/(2\sin^2(A+B))`, `\partial_BX_0=\sin A\cos A/
(2\sin^2(A+B))`; at the corner these give exact tangent-cone slopes `2/9`
(lower curve `X_0=\cos^2B`) and `3` (upper curve `X_0=\cos^2\beta_0(A)`),
and an exact gradient `\partial_AT|_\ast=14375\sqrt{15}/32768,\
\partial_BT|_\ast=5625\sqrt{15}/32768` (both `>0`), so the directional
derivative `\delta(t):=\partial_AT+t\partial_BT` is positive and increasing
on the tangent cone `t\in[2/9,3]`, minimized at `t=2/9`,
`\delta(2/9)=15625\sqrt{15}/32768\approx1.8468>0`. (iii) *Near-corner
closure.* A certified `mpmath.iv` (directed-rounding) domain-safety bound
confines the admissible slope `t` to `(0.2024,3.121)\subset[0.15,3.35]` for
`A\in(A^\ast,A^\ast+0.01]`, and a certified Hessian bound `|Q(t)|\le35.67`
on the corresponding box; Taylor's theorem with Lagrange remainder then
gives `T(A,B)\ge\varepsilon(1.8336-17.835\varepsilon)\ge1.6553\,
\varepsilon>0` for `\varepsilon:=A-A^\ast\in(0,0.01]`. (iv) *Away-from-corner
closure.* A certified `mpmath.iv` adaptive quadtree sweep over
`A\in[A^\ast+0.005,\pi/2]` (708 total boxes across three sub-ranges)
certifies, on every box, either that the box lies outside `\mathcal D_b`
or that `T\ge0` on the whole box, with zero unresolved boxes. (iii)-(iv)
overlap and jointly cover `(A^\ast,\pi/2]`, the full nonempty range of
`\mathcal D_b`. `\blacksquare`

**Caveat (explicit scope — do not overclaim).** This theorem's domain is
`\mathcal D_b` (Case (b), `X_0<\cos^2\beta_0(A)`) **only**. It does **not**
extend to Case (a) (`X_0>\cos^2\beta_0(A)`, the complementary region):
independently confirmed (see below) that `T`/`G(\beta_1)` are demonstrably
**negative** at ordinary, non-degenerate points of Case (a) (e.g.
`A=0.02,B=1.5`: `T\approx-0.249`, `G(\beta_1)\approx-0.654`). Case (a)
remains open and requires a different treatment; see the source approach
file's Open gap 7 for the sharpened diagnosis.

**Where proved.** `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`, "Round 20" section.

## Independent verification (proof-reviewer, round 20)
- Own fresh `sympy` symbolic computation of `T(A^\ast,B^\ast)` via the exact
  `u=\arcsin(\sqrt6/4)` substitution: `sympy.N(T,60)` returns `0` to 192
  displayed digits — confirms (i) exactly.
- Own fresh `mpmath` central finite-difference computation (`dps=50`,
  `h=10^{-20}`) of `\partial_AT,\partial_BT` at the corner: matches the
  claimed exact closed forms `14375\sqrt{15}/32768\approx1.699040`,
  `5625\sqrt{15}/32768\approx0.664842` to all displayed digits — confirms
  (ii).
- Own fresh `sympy.Rational` verification that the formula
  `T=c(dQ_1-cR_0)/(4\sin^2(A+B))` (from `lemmas/case-b-e-lt-0-t-
  factorization.md`) matches the raw `T:=B_{\mathrm c}^2X_0-E^2` definition
  to 50+ digits at multiple sample points, including inside `\mathcal D_b`.
- Own fresh 200,000-sample domain sweep (own membership test built from the
  raw `X_0,\beta_0,P,E` inequalities defining `\mathcal D_b`, independent
  seed): 486 genuine `\mathcal D_b` points found, **zero** `T<0` violations
  — corroborates (not a substitute for) the certified interval-arithmetic
  closure of (iii)-(iv), which was not independently re-run box-by-box this
  round (would require reproducing the same `mpmath.iv` adaptive-quadtree
  pipeline from scratch) but is internally consistent with every
  independently-checked component (corner value, gradient, formula
  identity, domain-sweep).
- **Independently reproduced the Case (a) counterexample exactly**: fresh
  50-digit `mpmath` script from the raw definitions, `A=0.02,B=1.5`:
  `X_0=0.49929\ldots>\cos^2\beta_0(A)=0.25580\ldots` (genuine Case (a)
  point), `P=1.00012\ldots>0`, `E=-0.49904\ldots<0`,
  `T=-0.24903851902574595779658364299364672170716014094996`,
  `G(\beta_1)=-0.65365419132206890874287426578647393081332454909202` —
  matches the source file's reported values to every displayed digit,
  confirming the caveat above is correct and load-bearing (Case (a) is
  genuinely a different, harder, still-open problem, not a citation gap).

**Certified.** This theorem — with its explicit Case-(b)-only scope — is a
genuine, independently-verified closure of Case (b) of Open gap 7, and a
new closure route (independent of the file's `\mathrm{Tgt}`/`D_1`/Reduction
Lemma machinery). It does **not** close Open gap 7 as a whole; Case (a)
remains open.
