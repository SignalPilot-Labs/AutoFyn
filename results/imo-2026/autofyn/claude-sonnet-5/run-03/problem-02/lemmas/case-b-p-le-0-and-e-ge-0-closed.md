## Theorem (Case (b) target `G(\beta_1)\ge0`: the `P\le0` sub-case closed
unconditionally, and the `E\ge0` sub-case closed unconditionally, of the
`P>0` regime)

**Setup.** For a triangle with `A\le\pi/2` (else Case (b) is vacuous —
`X_0<0` and `\beta_1` does not exist as a real number), write
`X_0:=\sin B\cos A/(2\sin(A+B))\in[0,1]`, `x:=\cos\beta_1=\sqrt{X_0}\ge0`,
`y:=\sin\beta_1=\sqrt{1-X_0}\ge0`,
$$K:=2\sin A\sin(A+B)>0,\qquad
P:=\tfrac12\sin(A-B)+\tfrac32\sin(A+B),\qquad
G(\beta_1):=K+\sin A\sin B\,x-Py.$$
(`G(\beta_1)=2K-f(\beta_1)`, the round-8/9 target, restricted to `\beta_1`
the root of `Y(\beta_1)=0`, i.e. `\cos^2\beta_1=X_0`.) Goal: `G(\beta_1)\ge0`.

**Theorem 1 (the `P\le0` branch).** If `P\le0`, then `G(\beta_1)\ge
K+\sin A\sin B\,x>0` strictly.

*Proof.* `K>0` (`\sin A>0,\sin(A+B)=\sin C>0`, genuine triangle-angle
sines), `\sin A\sin B>0`, `x\ge0`, so `K+\sin A\sin B\,x>0` strictly. If
`P\le0` then `-Py\ge0` (`y\ge0`), so
`G(\beta_1)=(K+\sin A\sin B\,x)+(-P)y\ge K+\sin A\sin B\,x>0`. `\blacksquare`

**Theorem 2 (the squaring reduction is an iff, when `P>0`).** Assume `P>0`.
Write `\mathrm{expr}_1:=K+\sin A\sin B\,x>0` (as above). Since
`\mathrm{expr}_1>0` and `Py\ge0`, both sides of `\mathrm{expr}_1\ge Py` are
`\ge0`, so squaring is an **iff**:
$$\mathrm{expr}_1\ge Py\iff D:=\mathrm{expr}_1^2-P^2(1-x^2)\ge0,$$
and expanding, `D=A_{\mathrm c}x^2+B_{\mathrm c}x+C_{\mathrm c}` with
`A_{\mathrm c}:=\sin^2A\sin^2B+P^2`, `B_{\mathrm c}:=2K\sin A\sin B`,
`C_{\mathrm c}:=K^2-P^2` (elementary algebra, `sympy`-verified, zero
residual). `\blacksquare`

**Theorem 3 (`D` strictly increasing in `x` on `[0,\infty)`, when `P>0`).**
`D'(x)=2A_{\mathrm c}x+B_{\mathrm c}`. `B_{\mathrm c}>0` strictly (`K>0`,
`\sin A\sin B>0`) and `A_{\mathrm c}\ge0` (sum of two squares), so
`D'(x)\ge B_{\mathrm c}>0` for `x\ge0`. Hence at `x=\sqrt{X_0}$,
`D=E+B_{\mathrm c}\sqrt{X_0}`, `E:=A_{\mathrm c}X_0+C_{\mathrm c}`
(substituting `x^2\to X_0` in the `x^2$ term, `x\to\sqrt{X_0}` in the
linear term — valid since `x=\sqrt{X_0}\ge0` exactly). `\blacksquare`

**Theorem 4 (the `E\ge0` branch, when `P>0`).** If `P>0` and `E\ge0`, then
`D=E+B_{\mathrm c}\sqrt{X_0}\ge0` (both terms `\ge0`), so by Theorem 2's
biconditional, `\mathrm{expr}_1\ge Py`, i.e. `G(\beta_1)\ge0`.
`\blacksquare`

**Corollary.** `G(\beta_1)\ge0` is established unconditionally whenever
`P\le0` (Theorem 1) or `P>0\wedge E\ge0` (Theorem 4). The only case NOT
covered is `P>0\wedge E<0`, which reduces (Theorem 2's iff, applied a
second time since both `-E>0` and `B_{\mathrm c}\sqrt{X_0}\ge0`) to the
single polynomial condition `T:=B_{\mathrm c}^2X_0-E^2\ge0` — see
`case-b-e-lt-0-t-factorization.md` for the further (unclosed) reduction of
this residual case.

## Independent verification (proof-reviewer, round 10)
Every algebraic step (Theorems 1-4) was independently re-derived by hand
from the raw definitions of `K,P,\mathrm{expr}_1,D,A_{\mathrm c},B_{\mathrm
c},C_{\mathrm c},E` — each identity (the expansion of `D`, the substitution
giving `E+B_{\mathrm c}\sqrt{X_0}`, the sign arguments) matches the source
file exactly, with no gap. This is elementary algebra with no computer-
algebra dependency, hence particularly low-risk; independent hand
verification is fully conclusive here (no sympy needed for these steps).

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 10, Steps 1-3).

## Status
Certified.
