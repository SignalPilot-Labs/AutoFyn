## Finding (the `(\star)`-corner is a domain-boundary cusp, not an interior
critical point — high-precision numerical, NOT a symbolic proof)

**Setup.** `\mathrm{star\_slack}(A,B):=(1+\cos B)^2X_0(A,B)-\mathrm{RHS}(A,B)^2`
(the slack in the open target `(\star)` of
`lemmas/mvt-lipschitz-reduction-case-b.md`). The corner
`(A^*,B^*)`, `B^*=\beta_0(A^*)=(\pi-A^*)/3`, is pinned by
`G_{\mathrm{curve}}(A^*):=G(\beta_0(A^*),A^*,\beta_0(A^*))=0` (the already-
certified endpoint equation), with
`A^*=0.4063777806843303293871746903293092626710\ldots` (40 digits).

**Numerical finding.** At `(A^*,B^*)`, computed by centered finite
differences (`mpmath`, 30-digit arithmetic, step sizes `h=10^{-6},
10^{-10},10^{-15}`, all mutually consistent to the digits shown):
$$\nabla(\mathrm{star\_slack})(A^*,B^*)\approx(1.7809,\,1.1205)\ne(0,0),$$
$$\mathrm{Hess}(\mathrm{star\_slack})(A^*,B^*)\approx
\begin{pmatrix}-2.7332&1.8559\\1.8559&-2.0478\end{pmatrix},\quad
\det\approx2.15>0,\ \mathrm{tr}<0.$$
I.e. `\mathrm{star\_slack}`, extended as a smooth unconstrained function of
`(A,B)\in\mathbb R^2` past the true domain boundary, has a nonzero gradient
and a negative-definite Hessian (a local MAXIMUM) at `(A^*,B^*)` — it is
**not** an interior stationary point of any kind (not a minimum, saddle, or
degenerate critical point).

**Consequence.** Any argument that treats the corner as an "interior
PSD-Hessian critical point" of the unconstrained slack function is invalid;
the tightness of `(\star)` at this point must instead be a first-order
domain-boundary phenomenon (the true admissible `(A,B)`-region shrinks to a
point at `A=A^*`, per the companion finding that Case (b)'s domain is empty
for `A\le A^*`), not a Taylor-around-a-critical-point argument.

## Independent verification (proof-reviewer, round 11)
Rebuilt the corner-pinning equation, `\mathrm{star\_slack}`, and the
finite-difference gradient/Hessian entirely from scratch (own fresh
`mpmath` session, 40-digit precision for the root-find, 30-digit for the
derivatives, step sizes `10^{-6},10^{-10},10^{-15}`): reproduced
`A^*=0.4063777806843303293871746903293092626710` to all 40 displayed
digits, `\mathrm{star\_slack}(A^*,B^*)=0` to the precision used, and the
gradient/Hessian values exactly as reported above (own computation:
gradient `(1.780926\ldots,1.120546\ldots)`, Hessian
`(-2.733152\ldots,1.855850\ldots,-2.047813\ldots)`, `\det\approx2.153`,
`\mathrm{tr}<0`) — matches the source file's reported values to all
displayed digits, and the values are stable across three widely-separated
step sizes (no floating-point-noise artifact). This is decisive numerical
evidence (a value robustly and reproducibly bounded away from zero by a
comfortable margin, not a marginal floating-point coincidence), though it
remains a numerical computation at one point, not a closed-form symbolic
proof (`A^*` itself has no known closed form).

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md`
(round 11).

## Status
Certified as a decisive, independently-reproduced numerical finding
(reusable as a "do not re-attempt a plain PSD-Hessian argument at this
corner" fact for any future round) — NOT a symbolic theorem, since `A^*`
has no known closed form; any future round that wants an unconditional
proof of "gradient nonzero at the corner" must first characterize `A^*`
algebraically.
