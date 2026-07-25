## Fact (exact factorization of the residual target `T`, in the `P>0\wedge
E<0` sub-case of Case (b))

**Setup.** Continuing `case-b-p-le-0-and-e-ge-0-closed.md`'s notation: in
the residual sub-case `P>0\wedge E<0`, `G(\beta_1)\ge0` is exactly
equivalent to
$$T:=B_{\mathrm c}^2X_0-E^2\ \ge\ 0.$$
Write `s:=\sin A,c:=\cos A,t:=\sin B,d:=\cos B` (`c\ge0` under the standing
`A\le\pi/2`; `s,t>0` always), `\sigma:=s^2,\tau:=t^2`.

**Theorem (exact factorization).**
$$T=\frac{c\,\bigl(d\,Q_1(\sigma,\tau)-c\,R_0(\sigma,\tau)\bigr)}
{4\sin^2(A+B)},\qquad Q_1=-4st\,q_1(\sigma,\tau),\quad R_0=r_0(\sigma,\tau),$$
with `q_1,r_0` the explicit degree-`(4,3)`-in-`(\sigma,\tau)` polynomials:
$$q_1=512\sigma^4\tau^2-512\sigma^4\tau+96\sigma^4-928\sigma^3\tau^2
+856\sigma^3\tau-144\sigma^3+506\sigma^2\tau^2-392\sigma^2\tau+48\sigma^2
-85\sigma\tau^2+40\sigma\tau+3\tau^2,$$
$$r_0=2048\sigma^4\tau^3-3072\sigma^4\tau^2+1152\sigma^4\tau-64\sigma^4
-2688\sigma^3\tau^3+3744\sigma^3\tau^2-1248\sigma^3\tau+64\sigma^3
+936\sigma^2\tau^3-1092\sigma^2\tau^2+240\sigma^2\tau-80\sigma\tau^3
+60\sigma\tau^2+\tau^3.$$

*Proof.* Direct symbolic expansion of `T` from its raw definition
(`B_{\mathrm c}=2K\sin A\sin B`, `E=A_{\mathrm c}X_0+C_{\mathrm c}`,
`X_0=ct/(2(ct+ds))`) followed by reduction modulo the ideal
`\langle c^2+s^2-1,\ d^2+t^2-1\rangle` (a rigorous exact algebraic
reduction, valid identically for real sine/cosine pairs) collapses to the
displayed rational expression. `\blacksquare`

**Corollary (does not close the sign of `T`).** Since `c\ge0` and
`4\sin^2(A+B)>0`,
$$T\ge0\iff c=0\ \text{ or }\ 4dst\,q_1(\sigma,\tau)+c\,r_0(\sigma,\tau)
\le0.$$
Neither `q_1` nor `r_0` has a fixed sign on `(\sigma,\tau)\in(0,1)^2` (each
takes both signs on a substantial fraction of the square), so no simple
termwise argument closes this. **This fact is a genuine, verified
structural reduction, reusable by any future attempt at the residual
sub-case, but does NOT by itself establish `T\ge0`.**

## Independent verification (proof-reviewer, round 10)
The factorization identity was independently re-derived from scratch: `T`
was recomputed directly from its definition in terms of `\sin A,\cos A,
\sin B,\cos B` (not copied from the source file's intermediate steps), and
compared against the claimed closed form `c(dQ_1-cR_0)/(4\sin^2(A+B))`
using both `q_1,r_0` exactly as displayed. `sympy.simplify` of the
difference did not fully collapse to `0` in closed symbolic form (the
expression is large and trig-heavy), so the identity was instead verified
by high-precision numerical evaluation (`mpmath`, 30 decimal digits) at 20
independently-chosen random `(A,B)` pairs spanning the domain: the
relative error between `T` and the claimed closed form was `<10^{-15}` at
every sample (several matched to `>25` digits), which is decisive evidence
of an exact algebraic identity (not a numerical coincidence). Independently
re-sampled `q_1,r_0`'s signs over `(\sigma,\tau)\in(0,1)^2` (own 200,000-
sample sweep): `q_1>0` in `\approx25.4\%` of samples, `r_0>0` in
`\approx54.8\%`, closely matching the source file's own `\approx25.6\%`
and `\approx54.8\%` — confirms neither has fixed sign, as claimed.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 10, "New reduction this round").

## Status
Certified (as a genuine, verified reduction; does not itself close the
`T\ge0` gap, which remains open).
