## Lemma (the `f-g` reformulation of `(\star)`, its Reduction Lemma, the
exact `f-g|_{\mathcal C}=D_1` identity, a radical-free factorization of
`T_1`, and a domain-connectedness/sign-determination device)

**Setup.** Reusing the certified backbone of `lemmas/mvt-lipschitz-
reduction-case-b.md` and `lemmas/rhs-partial-b-derivative-and-
decomposition.md`: `X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`,
`\beta_0(A):=(\pi-A)/3`, `K_c=2\sin A\sin(A+B)`, `P=\tfrac12\sin(A-B)+
\tfrac32\sin(A+B)`, `Q=-\sin A\sin B`, `G(\beta_0):=K_c-P\sin\beta_0-Q\cos
\beta_0`, `\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
`S:=(1+\cos B)^2X_0-\mathrm{RHS}^2` (target `(\star)`: `S\ge0`), on the
exact Case-(b) domain `\mathcal D` (`0<A<\pi/2`, `\beta_0(A)<B\le C`,
`\cos^2B<X_0<\cos^2\beta_0(A)`, WLOG `\angle B\le\angle C$). Define
`f:=(1+\cos B)\sqrt{X_0}\ge0`, `g:=\mathrm{RHS}`, so `S=f^2-g^2=(f-g)(f+g)`.
`\mathcal C:=\{X_0=\cos^2B\}` is `\mathcal D`'s implicit lower `B`-boundary
(round 11), `D_1:=(1+\cos B)\cos B-\mathrm{RHS}` (`-twopoint` sibling,
`lemmas/star-factorization-on-boundary-curve.md`).

**Theorem 1 (`\cos B>0`, elementary, reused).** WLOG `\angle B\le\angle C`
gives `2B\le B+C=\pi-A<\pi`, so `B<\pi/2`, hence `\cos B>0`.

**Theorem 2 (`f-g|_{\mathcal C}=D_1$, exact).** On `\mathcal C`, `X_0=
\cos^2B`, so (using Theorem 1) `\sqrt{X_0}=\cos B`, hence `f=(1+\cos B)
\cos B` and `f-g=(1+\cos B)\cos B-\mathrm{RHS}=D_1` identically.

**Theorem 3 (radical-free factorization of `T_1$).** With `T_1:=(1+\cos
B)^2\partial_BX_0-2(1+\cos B)\sin B\,X_0` (certified) and `\partial_BX_0=
\dfrac{\sin A\cos A}{2\sin^2(A+B)}$ (certified, `lemmas/x0-partial-b-
derivative.md`):
$$T_1=\frac{(1+\cos B)\cos A}{2\sin^2(A+B)}\Bigl[(1+\cos B)\sin A-2\sin^2B
\,\sin(A+B)\Bigr].$$
*Proof.* Substitute the two certified closed forms and factor out the
common term `(1+\cos B)\cos A/(2\sin^2(A+B))` — direct algebra.

**Theorem 4 (the radical-free target).** `2f\cdot\partial f/\partial B=
\partial(f^2)/\partial B=T_1`, so `(\partial f/\partial B)^2=T_1^2/(4f^2)=
T_1^2/(4(1+\cos B)^2X_0)`. Hence, on the interior of `\mathcal D` (where
`X_0>0`), `(\partial g/\partial B)^2>(\partial f/\partial B)^2\iff
\mathrm{Tgt}:=4(1+\cos B)^2X_0\,D_2^2-T_1^2>0` (`D_2:=\partial\mathrm{RHS}/
\partial B`, certified), a fully radical-free inequality.

**Theorem 5 (Reduction Lemma).** Suppose (A) `\partial(f-g)/\partial B>0`
throughout `\mathcal D`, and (B) `D_1(A)\ge0` on `\mathcal C`. Then `f\ge g`
throughout `\mathcal D`.

*Proof.* Fix `A`. The admissible `B`-range is `[B_{\mathrm{lo}}(A),
B_{\mathrm{hi}}(A)]` with `B_{\mathrm{lo}}(A)$ on `\mathcal C`. By (A),
`f-g` is increasing in `B` there, so for any admissible `B`,
`f(A,B)-g(A,B)\ge f(A,B_{\mathrm{lo}}(A))-g(A,B_{\mathrm{lo}}(A))=D_1(A)
\ge0` (Theorem 2 for the equality, (B) for the inequality). `\blacksquare`

**Theorem 6 (why `\mathrm{RHS}>0` need not be proved unconditionally).**
By the parent reduction (`lemmas/mvt-lipschitz-reduction-case-b.md`), the
ultimate target `G(\beta_1)\ge0` already follows unconditionally, by a
different argument, whenever `\mathrm{RHS}\le0` — `(\star)`/`S\ge0` (hence
`f\ge g`) is only ever *needed* where `\mathrm{RHS}>0`. Theorem 5 proves
`f\ge g` on **all** of `\mathcal D`, which is more than sufficient (it
covers both cases at once, though only the `\mathrm{RHS}>0` sub-case's
conclusion is actually used downstream).

**Theorem 7 (domain connectedness and sign-determination).** `\mathcal D`
is path-connected: for each `A\in(A^\ast,A_{\max}]`, `B_{\mathrm{hi}}(A)=
(\pi-A)/2` is continuous, and `B_{\mathrm{lo}}(A)` (the unique zero in `B`
of `h_A(B):=X_0(A,B)-\cos^2B`, which is strictly increasing in `B` since
`\partial_BX_0>0$ — certified `D1'` — and `-\partial_B\cos^2B=2\sin B\cos B
>0` on `(0,\pi/2)`) is continuous in `A` (continuity of `h` jointly in
`(A,B)$ plus strict monotonicity in `B` implies continuity of the implicit
root). Hence `\mathcal D` is the region between the graphs of two
continuous functions over a connected `A`-interval — path-connected.
Consequently: if a continuous function `\phi$ on `\mathcal D` is known
never to vanish (e.g. because it is a nonzero factor of a nonvanishing
product `\mathrm{Tgt}\ne0`), then `\phi` has one constant sign throughout
`\mathcal D`, determined by evaluating `\phi` at any single point (else, by
the Intermediate Value Theorem, `\phi` would vanish somewhere between a
positive and negative value, contradicting nonvanishing).

## Status of the hypotheses
- Theorems 1-7 above are all **fully proved** (elementary calculus/algebra
  plus one application of the IVT and a standard continuity-of-implicit-
  root argument), independently `sympy`-confirmed for the algebraic
  identities (Theorems 2, 3, 4).
- **Hypothesis (A)** of Theorem 5 (equivalently `\mathrm{Tgt}>0`
  throughout `\mathcal D`, via Theorem 4 + Theorem 7 + a one-point sign
  check, which gives `\partial(f-g)/\partial B>0$ at the sample
  `(A,B)\approx(0.603,1.269)`) is **NOT proved symbolically** — strong
  numeric evidence only (global-optimization minimum of `\mathrm{Tgt}`
  `\approx1.574>0` over `\mathcal D`).
- **Hypothesis (B)** (`D_1\ge0` on `\mathcal C`) is the `-twopoint`
  sibling's own open gap (`\approx90\%$ numerically confirmed unimodality/
  concavity, corner-vanishing exact).

Given both open hypotheses, the whole problem follows via Theorem 5 +
Theorem 6. Neither is proved this round — this lemma packages the fully
rigorous reduction connecting them, not a proof of the remaining
inequalities themselves.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-
pointwise-tangent.md` (round 13, "Round 13: the `f-g` reformulation").

## Status
Proposed (pending proof-reviewer independent verification/certification).
The elementary/algebraic Theorems 1-7 are fully proved and ready for
certification; the two open numeric hypotheses (A) and (B) are explicitly
NOT part of the certifiable content.
