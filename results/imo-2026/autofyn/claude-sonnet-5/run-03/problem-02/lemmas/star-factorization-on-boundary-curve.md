# Lemma: exact difference-of-squares factorization of `S` on the boundary curve `X_0=\cos^2B`

**Setup.** As in `lemmas/rhs-partial-b-derivative-and-decomposition.md`:
`X_0(A,B),\mathrm{RHS}(A,B),S(A,B):=(1+\cos B)^2X_0-\mathrm{RHS}^2`. Let
`\mathcal C:=\{(A,B):X_0(A,B)=\cos^2B\}` (the Case-(b) domain's implicit
lower `B`-boundary, per round 11's domain characterization).

**Statement.** On `\mathcal C`,
$$
S=D_1\cdot D_2,\qquad D_1:=(1+\cos B)\cos B-\mathrm{RHS},\qquad
D_2:=(1+\cos B)\cos B+\mathrm{RHS}.
$$

**Proof.** On `\mathcal C`, `(1+\cos B)^2X_0=(1+\cos B)^2\cos^2B=
[(1+\cos B)\cos B]^2`, so
`S=[(1+\cos B)\cos B]^2-\mathrm{RHS}^2=D_1D_2` by the elementary
difference-of-squares identity. `∎` Independently re-verified (own
`sympy` session: substituting `X_0=\cos^2B` into `S`'s definition and
expanding `D_1D_2` gives an identical polynomial in `\cos B,\mathrm{RHS}`,
residual `0`).

**Scope / caveat.** This factorization holds only on the curve `\mathcal
C` (a codimension-1 subset of the Case-(b) domain), not on the full
2-variable domain. Neither `D_1\ge0` nor `D_2>0` on `\mathcal C` is proved
symbolically — both are numeric-only findings this round (own
independent re-derivation of the curve via `scipy.optimize.brentq`
root-finding at 3000 sample `A`-values, `D_2\in[1.10,1.97]`, `0`
violations of `D_2>0`; `D_1\ge0` with equality only at the corner
`(A^*,B^*)`, maximum `\approx0.405` near `A\approx0.979`, second-difference
negative at `\approx90\%` of interior grid points — consistent with, but
not a proof of, concavity/unimodality of `D_1(A)` along `\mathcal C`).
Even if both were proved, extending `S\ge0` from `\mathcal C` to the full
Case-(b) domain still requires a separate monotonicity argument
(`\partial S/\partial B\ge0`, itself open — see
`lemmas/rhs-partial-b-derivative-and-decomposition.md`).

**Origin.**
`coordinate-bash-resultant-boundary-pointwise-tangent-twopoint.md`, round
12, certified by the round-12 proof-reviewer after independent
re-derivation and independent reproduction of the numeric scan (own fresh
`scipy`/`numpy` script, matching the file's reported `D_1,D_2` values and
extremal locations closely).
