## Status
certified (round 6)

## Statement
Let `f(t)=At^2+Bt+C` be a real quadratic, `A\ne0`, with two distinct real
roots `r_1<r_2`. Let `X(t)=Q_Xt+P_X`, `Y(t)=Q_Yt+P_Y` be real affine
functions with `Q_X,Q_Y\ne0`, such that `X(r_1)X(r_2)<0` and
`Y(r_1)Y(r_2)<0`. Then
$$\mathrm{sign}\big(X(r_1)\big)=\mathrm{sign}\big(Y(r_1)\big)
\iff \mathrm{sign}(Q_X)=\mathrm{sign}(Q_Y).$$

## Proof
Since `X` is affine with nonzero slope, it has a unique zero `t_X=-P_X/Q_X`.
Since `X(r_1)X(r_2)<0`, the (continuous, monotonic) function `X` changes
sign strictly between `r_1` and `r_2`, so `r_1<t_X<r_2`. If `Q_X>0`, `X` is
increasing, so (being left of its zero) `X(r_1)<0`; if `Q_X<0`, `X` is
decreasing, so `X(r_1)>0`. Either way `\mathrm{sign}(X(r_1))=
-\mathrm{sign}(Q_X)`. Identically `\mathrm{sign}(Y(r_1))=-\mathrm{sign}
(Q_Y)`. Hence `\mathrm{sign}(X(r_1))=\mathrm{sign}(Y(r_1))\iff
-\mathrm{sign}(Q_X)=-\mathrm{sign}(Q_Y)\iff\mathrm{sign}(Q_X)=
\mathrm{sign}(Q_Y)`. `\blacksquare`

## Independent verification (proof-reviewer, round 6)
Elementary IVT argument, checked by hand — no gap, no hidden case (the
"unique zero strictly between the roots" step follows directly from `X`
being monotonic and continuous with opposite-sign endpoint values).

## Reuse
General and reusable independently of this problem's specific polynomials:
whenever two different sign-selection criteria are each known to split a
common quadratic's two real roots by sign, this lemma reduces "do the two
criteria pick the same root?" to a one-line comparison of the criteria's
slopes. Used in `magnitude-bound-and-sign-coincidence.md` (this problem) to
show the magnitude-bound test and the cross-product-sign test always select
the same root of `G_{2a}`/`G_{3a}`.
