# Lemma: exact closed-form parametrization of the boundary curve `\mathcal C_{\mathrm{lo}}`

**Source.** Proved in `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`,
round 15, "Theorem A."

**Statement.** Let `X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`. On the
implicit curve `\mathcal C_{\mathrm{lo}}=\{(A,B):X_0(A,B)=\cos^2B\}`, with
`A\in(0,\pi/2)` and `B\in(0,\pi/2)` (so `\cos A,\cos B,\sin B>0`), the
curve has the exact closed-form parametrization
$$
\tan A=\frac{\sin B\,(1-2\cos^2B)}{2\cos^3B}=\frac{-\sin B\cos(2B)}{2\cos^3B}.
$$

**Proof.** `X_0=\cos^2B` means `\sin B\cos A=2\cos^2B\sin(A+B)`. Expanding
`\sin(A+B)=\sin A\cos B+\cos A\sin B` (sine addition formula):
$$
\sin B\cos A=2\cos^3B\sin A+2\cos^2B\sin B\cos A.
$$
Collecting `\cos A` terms:
$$
\cos A\cdot\sin B(1-2\cos^2B)=2\cos^3B\sin A.
$$
Since `\cos A\ne0` (as `A\in(0,\pi/2)`), divide both sides by
`\cos A\cos^3B` (both strictly positive) to get the boxed identity, using
`1-2\cos^2B=-\cos(2B)` (double-angle identity). ∎

**Verification.** Independently `sympy`-confirmed (substituting
`A\to\arctan(\text{RHS})` into `X_0(A,B)-\cos^2B` and simplifying, using
`A\in(0,\pi/2)` to fix the branch, gives `0`). At the two known reference
points of `\mathcal D`, the formula recovers: `A(\pi/3)=\pi/3` exactly
(the corner `(\pi/3,\pi/3)`), and `A(0.9117433492\ldots)\approx
0.406400542949\ldots` (matching the population's long-standing corner
`A^\ast\approx0.4064`, established in rounds 9-14 by other means).

**Scope / caveat.** This gives a parametrization of the *whole* curve
`\mathcal C_{\mathrm{lo}}` restricted to `A\in(0,\pi/2),B\in(0,\pi/2)`
(both facts already independently established as holding throughout the
domain `\mathcal D` in prior rounds); it does not by itself say anything
about which `B`-range corresponds to the domain's true boundary (that is
determined separately by the other domain inequalities).

**Reusability.** This is the first non-implicit formula for `\mathcal
C_{\mathrm{lo}}` in the population's history. Directly enables reducing
any 2-variable target restricted to this curve to a 1-variable target in
`B` alone (used in the same round's Theorem C to prove
`\mathrm{Tgt}\ge\mathrm{Tgt}(\pi/3,\pi/3)` on the whole curve).
