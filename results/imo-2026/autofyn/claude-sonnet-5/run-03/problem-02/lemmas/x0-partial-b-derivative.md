## Fact (exact partial derivative of `X_0` in `B`)

**Setup.** `X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}` (as used throughout
the Case-(b) apparatus of `coordinate-bash-resultant-boundary-pointwise`
and its round-11 forks).

**Theorem.**
$$\frac{\partial X_0}{\partial B}=\frac{\sin A\cos A}{2\sin^2(A+B)}.$$

*Proof.* By the quotient rule (treating `A` as constant),
$$\frac{\partial X_0}{\partial B}=\frac{\cos A}{2}\cdot
\frac{\cos B\sin(A+B)-\sin B\cos(A+B)}{\sin^2(A+B)}
=\frac{\cos A}{2}\cdot\frac{\sin((A+B)-B)}{\sin^2(A+B)}
=\frac{\sin A\cos A}{2\sin^2(A+B)},$$
using the sine-subtraction identity `\cos B\sin(A+B)-\sin B\cos(A+B)=
\sin A`. `\blacksquare`

**Corollary.** Since `\sin(A+B)\ne0` on `0<A+B<\pi` and, on the Case-(b)
domain, `\cos A\ge0` (standing assumption `A\in(0,\pi/2]`) with `\sin A>0`,
$$\frac{\partial X_0}{\partial B}\ge0\text{ always, and }>0\text{ whenever
}A\in(0,\pi/2)\text{ strictly}.$$
I.e. `X_0` is nondecreasing (strictly increasing for `A<\pi/2`) in `B` at
fixed `A`, throughout the Case-(b) domain.

## Independent verification (proof-reviewer, round 11)
Re-derived by hand from the raw quotient-rule computation (elementary,
matches the file exactly) and independently confirmed symbolically
(`sympy.diff(X0,B)` minus the claimed closed form simplifies to `0`
exactly, fresh session, no code reused from the source file). No gap.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
(round 11).

## Status
Certified (elementary, exact, gap-free; reusable by any future attempt at
`(\star)` via monotonicity-in-`B`).
