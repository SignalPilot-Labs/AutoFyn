## Theorem (`T(A^\ast,B^\ast)=0` — independent, exact rational-arithmetic proof via `(\sigma,\tau)`)

**Setup.** Let `A^\ast=3\arcsin(\sqrt6/4)-\pi/2` (the certified closed form
of `lemmas/d1-nonnegative-on-boundary-curve.md`), `B^\ast:=\beta_0(A^\ast)=
(\pi-A^\ast)/3`. In the notation of `lemmas/case-b-e-lt-0-t-
factorization.md` (`s:=\sin A,c:=\cos A,t:=\sin B,d:=\cos B,\sigma:=s^2,
\tau:=t^2`, and the certified identity
`T=c(dQ_1-cR_0)/(4\sin^2(A+B))`, `Q_1=-4st\,q_1(\sigma,\tau)`,
`R_0=r_0(\sigma,\tau)`, with `q_1,r_0` the explicit degree-`(4,2)`/`(4,3)`
polynomials in that lemma).

**Theorem.**
$$\sigma^\ast:=\sin^2A^\ast=\frac5{32},\qquad
\tau^\ast:=\sin^2B^\ast=\frac58,$$
$$q_1(\sigma^\ast,\tau^\ast)=\frac{75}{131072},\qquad
r_0(\sigma^\ast,\tau^\ast)=-\frac{125}{262144},$$
and `T(A^\ast,B^\ast)=0` **exactly**.

**Proof.** `\sigma^\ast,\tau^\ast` follow from the certified `u:=A/3+\pi/6`
substitution (`\cos A=\sin3u,\ \sin\beta_0(A)=\cos u`) and the certified
fact `\sin^2u^\ast=3/8` (`lemmas/d1-nonnegative-on-boundary-curve.md`
§0(f)): `\tau^\ast=\cos^2u^\ast=5/8`, and via the triple-angle identity
`\cos3u=\cos u(4\cos^2u-3)`, `\cos(3u^\ast)=-\tfrac12\cos u^\ast`, so
`\sigma^\ast=\cos^2(3u^\ast)=\tfrac14\cos^2u^\ast=5/32`. Substituting these
two exact rationals into the certified degree-`(4,3)` polynomials `q_1,r_0`
is a finite rational-arithmetic computation, giving the displayed exact
values. Writing `s^\ast,c^\ast,t^\ast,d^\ast` for `\sin A^\ast,\cos A^\ast,
\sin B^\ast,\cos B^\ast$ (all strictly positive, `(s^\ast)^2=5/32,
(c^\ast)^2=27/32,(t^\ast)^2=5/8,(d^\ast)^2=3/8`), the identity
`d^\ast Q_1^\ast-c^\ast R_0^\ast=0` reduces to
`-4s^\ast t^\ast d^\ast q_1(\sigma^\ast,\tau^\ast)=c^\ast
r_0(\sigma^\ast,\tau^\ast)`, an equality of two strictly negative reals
(LHS: `-4\times(\text{positive})\times(\text{positive }q_1^\ast)<0`; RHS:
`c^\ast\times(\text{negative }r_0^\ast)<0`), hence equivalent (squaring is
injective on negatives) to
`16(s^\ast)^2(t^\ast)^2(d^\ast)^2q_1(\sigma^\ast,\tau^\ast)^2=
(c^\ast)^2r_0(\sigma^\ast,\tau^\ast)^2`, i.e.
`16\cdot\frac5{32}\cdot\frac58\cdot\frac38\cdot(75/131072)^2=
\frac{27}{32}\cdot(125/262144)^2`, a pure rational identity: both sides
equal `421875/2199023255552` exactly. Hence `d^\ast Q_1^\ast-c^\ast R_0^\ast
=0`, and since `\sin(A^\ast+B^\ast)=\sin(2u^\ast)\ne0` (already certified),
`T(A^\ast,B^\ast)=0`. `\blacksquare`

**Where proved.** `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent-via-T.md`, "New result 1".

## Independent verification (proof-reviewer, round 20)
- Own fresh `sympy.Rational` session: substituted `\sigma^\ast=5/32,
  \tau^\ast=5/8` into the exact `q_1,r_0` polynomials (typed independently
  from `lemmas/case-b-e-lt-0-t-factorization.md`'s displayed coefficients)
  — got `q_1^\ast=75/131072`, `r_0^\ast=-125/262144` exactly, matching.
- Own fresh exact-rational check of the squared identity: both
  `16\sigma^\ast\tau^\ast(1-\tau^\ast)(q_1^\ast)^2` and
  `(1-\sigma^\ast)(r_0^\ast)^2` computed via `sympy` equal
  `421875/2199023255552` exactly — confirmed.
- Own fresh `mpmath` (`dps=50`) numeric check that `\sin^2A^\ast=5/32` and
  `\sin^2B^\ast=5/8` exactly (to 50 digits), computed from the raw
  `u^\ast=\arcsin(\sqrt6/4)` definition, not copied from the file.
- Own fresh `mpmath` (`dps=50`) verification that the closed-form identity
  `T=c(dQ_1-cR_0)/(4\sin^2(A+B))` matches the raw `T:=B_{\mathrm c}^2X_0-E^2`
  definition to 50 digits at several sample `(A,B)` (not merely at the
  corner), confirming the underlying `T`-factorization this lemma relies on.
- Own fresh `sympy` symbolic computation of `T(A^\ast,B^\ast)` directly from
  the raw trigonometric definitions gives `0` to 192 displayed digits.

**Certified.** A complete, self-contained, gap-free rational-arithmetic
proof of the corner value `T(A^\ast,B^\ast)=0`, independent in mechanism
(via `(\sigma,\tau)`-polynomials rather than trig-identity Taylor expansion)
from the sibling `coordinate-bash-resultant-boundary-pointwise-tangent.md`'s
own derivation of the same fact. Reusable as the base case of any future
Lagrange-remainder/MVT argument for `T` on any sub-domain, and as an
independent cross-check of the sibling's Step 0.
