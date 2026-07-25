# Lemma: the Weierstrass (`u=\tan(A/6)`) denominator-clearing of `(⋆)`'s pieces has unconditionally positive denominator

**Setup.** `u:=\tan(A/6)`, `x:=\cos(A/3)=\frac{1-u^2}{1+u^2}`,
`y:=\sin(A/3)=\frac{2u}{1+u^2}`, `\cos A=4x^3-3x`, `\sin A=3y-4y^3`
(triple-angle formulas, since `A=3\cdot(A/3)`). Let `\mathrm{Num},
\mathrm{Den}` be the numerator/denominator (in lowest terms) obtained by
clearing denominators in `S=(1+\cos B)^2X_0-\mathrm{RHS}^2` after this
substitution (`S,X_0,\mathrm{RHS}` as in the sibling lemma
`rhs-partial-b-derivative-and-decomposition.md`), and similarly
`n_1=\cos^2\beta_0-X_0`, `n_2=X_0-\cos^2B` with numerators/denominators
`\mathrm{num}_1/\mathrm{den}_1`, `\mathrm{num}_2/\mathrm{den}_2`.

**Statement (Theorem 1).** Define
$$h(u,\cos B,\sin B):=-6\cos B\,u^5+20\cos B\,u^3-6\cos B\,u+\sin B\,u^6-15
\sin B\,u^4+15\sin B\,u^2-\sin B.$$
Then, as an exact polynomial identity,
$$h(u,\cos B,\sin B)=-(1+u^2)^3\sin(A+B),$$
and consequently, in lowest terms,
$$\mathrm{Den}=16(1+u^2)^{17}\sin(A+B),\qquad
\mathrm{den}_1=4(1+u^2)^5\sin(A+B),\qquad
\mathrm{den}_2=2(1+u^2)^3\sin(A+B).$$

**Corollary.** For any genuine triangle, `\sin(A+B)=\sin C>0` and
`(1+u^2)^k>0`, so `\mathrm{Den},\mathrm{den}_1,\mathrm{den}_2>0`
unconditionally. Hence the three equivalences
`(\star)\iff\mathrm{Num}\ge0`, `\cos^2\beta_0>X_0\iff n_1>0` (well,
`\mathrm{num}_1>0`), `X_0>\cos^2B\iff \mathrm{num}_2>0` hold rigorously,
not merely numerically.

**Proof / independent verification.** This round's proof-reviewer
independently re-derived, from scratch (own `sympy` session, not copying
any file's script):
1. `\sin(A+B)=\sin A\cos B+\cos A\sin B` with `\sin A,\cos A` the
   triple-angle polynomials above, cleared via `sympy.together`, gives
   denominator exactly `(1+u^2)^3` and numerator exactly `-h` — confirmed
   by `sympy.expand` of the difference, residual `0`.
2. `n_1=\cos^2\beta_0-X_0` (with `\cos\beta_0=\tfrac12x+\tfrac{\sqrt3}2y`,
   using `\beta_0=\pi/3-A/3`), after `sympy.together` and
   `sympy.factor`, has denominator exactly `-4(1+u^2)^2\,h` — confirmed
   directly (`sympy.factor` output matches term-for-term).
3. `n_2=X_0-\cos^2B` likewise has denominator exactly `-2h` — confirmed
   directly.
4. `S=(1+\cos B)^2X_0-\mathrm{RHS}^2`, after `sympy.cancel` (not merely
   `sympy.together`, which leaves an uncanceled common factor of
   `(1+u^2)^2` between numerator and denominator — a genuine pitfall
   independently encountered and resolved in this verification), has
   denominator in lowest terms exactly `16(1+u^2)^{14}\,h` (matching the
   file's `\mathrm{Den}=-16(u^2+1)^{14}h` up to the file's own sign
   convention).
Combining 1 with 2–4 gives the three displayed closed forms exactly, zero
symbolic residual throughout.

**Scope.** This lemma establishes only that the denominator-clearing step
is sign-preserving (an unconditional structural fact about the
substitution, true for any triangle). It does **not** establish
`\mathrm{Num}\ge0` itself (equivalently `(\star)`), which remains the
open target.

**Origin.** `coordinate-bash-resultant-boundary-pointwise-sos.md`, round
12 (Theorem 1), certified by the round-12 proof-reviewer after a complete
independent re-derivation of all four denominator computations from the
raw definitions (own `sympy` session, including independently discovering
and resolving the `together`-vs-`cancel` pitfall in item 4).
