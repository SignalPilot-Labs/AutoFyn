## Theorem (exact squaring-equivalence identity behind the `\beta_1`-triple-angle
Step 4/5 reduction)

**Status.** Proposed by `coordinate-bash-resultant-boundary`, round 13, for
reviewer certification. Upgrades the round-13 `math-explorer-q1r0`
2,000-sample spot check to a full symbolic identity.

**Setup.** `c:=\cos A,\ s:=\sin A,\ d:=\cos B,\ t:=\sin B` for a genuine
triangle (`s,t>0`, `\sin C=\sin(A+B)=ct+ds>0`). Let
$$X_0:=\frac{ct}{2(ds+ct)},\qquad p:=s(4X_0-3),\qquad q:=c(4X_0-1).$$

**Theorem.** The following is an exact polynomial identity (not merely a
numerical coincidence):
$$q^2(1-X_0)-p^2X_0=\frac{\mathrm{Num}}{2(ct+ds)^3},\qquad
\mathrm{Num}:=c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3-6c^2ds^3t^2-9cd^2s^4t.$$

*Proof.* Substitute `X_0=ct/(2(ct+ds))` into `p,q` and compute
`q^2(1-X_0)-p^2X_0` by clearing denominators (`\mathrm{sympy.together}`,
`\mathrm{sympy.fraction}`). The resulting single fraction has denominator
`2(ct+ds)^3$ exactly, and its numerator, expanded, equals
`-c\cdot\big(-c^4t^3+3c^2d^2s^2t+c^2s^2t^3-2cd^3s^3+6cds^3t^2+9d^2s^4t\big)`,
which expands term-by-term to exactly `\mathrm{Num}` as displayed above
(`\mathrm{sympy.expand}` confirms the difference is `0` identically).
`\blacksquare`

**Corollary (the sign equivalence used by Step 4/5).** Since
`2(ct+ds)^3=2\sin^3C>0` strictly for a genuine triangle,
$$q^2(1-X_0)-p^2X_0<0\iff\mathrm{Num}<0.$$
Combined with the (separately established, currently numeric-only) fact
that `p<0,q>0` throughout the residual sub-domain `\{G_0>0\}\cap\{E_{
\mathrm{num}}<0\}\cap\{c\ge2t^2-1\}` (licensing `qy<-px\iff q^2y^2<p^2x^2`
as a valid squaring, both sides nonnegative there), this gives the exact
equivalence `\sin(A+3\beta_1)<0\iff\mathrm{Num}<0` on that sub-domain.

**Scope note.** This theorem proves the algebraic identity unconditionally
(it holds for every `A,B` with `s,t,ct+ds\ne0`, no domain restriction
needed). It does *not* by itself establish `p<0,q>0` — that remains a
separately-flagged, currently numeric-only fact (see the parent approach
file, round 11/13).
