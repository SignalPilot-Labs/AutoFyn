# Lemma: exact closed form for `∂RHS/∂B` and the `T_1+T_2` decomposition of `∂S/∂B`

**Setup.** `X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`,
`\beta_0(A):=(\pi-A)/3`, `K_c:=2\sin A\sin(A+B)`,
`P:=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `Q:=-\sin A\sin B`,
`G(\beta_0):=K_c-P\sin\beta_0-Q\cos\beta_0`,
`\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
`S(A,B):=(1+\cos B)^2X_0-\mathrm{RHS}^2`.

**Statement 1 (D2).** Since `\beta_0` does not depend on `B`,
$$
\frac{\partial\mathrm{RHS}}{\partial B}=-\sin B\cos\beta_0-\sin\beta_0\,
\frac{\partial G(\beta_0)}{\partial B},
$$
$$
\frac{\partial G(\beta_0)}{\partial B}=2\sin A\cos(A+B)+\sin\beta_0\Bigl(
\tfrac12\cos(A-B)-\tfrac32\cos(A+B)\Bigr)+\sin A\cos\beta_0\cos B.
$$

**Statement 2 (D3).** With `\partial X_0/\partial B=\dfrac{\sin A\cos A}
{2\sin^2(A+B)}` (already certified, `lemmas/x0-partial-b-derivative.md`),
$$
\frac{\partial S}{\partial B}=T_1+T_2,\qquad
T_1:=(1+\cos B)^2\frac{\partial X_0}{\partial B}-2(1+\cos B)\sin B\,X_0,
\qquad T_2:=-2\,\mathrm{RHS}\,\frac{\partial\mathrm{RHS}}{\partial B}.
$$

**Proof.** Both are direct product/chain-rule computations (elementary
calculus, `\partial\beta_0/\partial B=0` since `\beta_0=(\pi-A)/3` is a
function of `A` alone). Independently re-verified in a fresh `sympy`
session (symbolic differentiation of `RHS` and `S` with respect to `B`,
holding `A` fixed, matches the displayed closed forms exactly —
`sympy.simplify` of the difference gives `0` in every case).

**Scope / caveat.** This is an exact algebraic identity, not a positivity
result. In particular `T_1` is numerically **not** sign-definite on the
Case-(b) domain `\mathcal D` (observed as negative throughout the sampled
sub-region tested, down to `\approx-0.645`, and never observed positive in
this round's independent 2,000,000-sample re-check) — so a proof of
`\partial S/\partial B\ge0` cannot proceed by showing `T_1,T_2\ge0`
separately; the two terms must be bounded jointly. `\partial S/\partial
B\ge0` itself remains open (numeric-only, margin `\approx0.177`–`0.19`).

**Origin.** `coordinate-bash-resultant-boundary-pointwise-tangent.md`,
round 12, certified by the round-12 proof-reviewer after independent
re-derivation (own fresh `sympy` session, own finite-difference
cross-check at 20,000+ points).
