## Status
certified (round 7)

## Statement
With notation as in `radical-isolation-equals-psi.md` and
`\Phi(U):=\tilde P_2n(U)^2-\tilde Q_2n(U)m(U)+\tilde R_2m(U)^2` (quadratic in
`U`; `m(U)=\sin A\,U-\cos A`, `n(U)=-\cos A\,U-\sin A-4`), write
`X_i:=(2\tilde P_1)^2\Phi(U_i)` (`i=1,2`, the two roots of `q_1`). Then
$$X_1X_2 = 16\,\tilde P_1^2\sin^2A\,(\tau\cos C-\sin C)(\sin B-\tau\cos
B)\,\Psi(\tau,A,C),$$
with the same strictly-negative-throughout-`D` prefactor as
`radical-isolation-equals-psi.md`. Equivalently: `X_1,X_2` have the same
sign (i.e. `X_1X_2>0`) iff `\Psi<0` (never happens on `D` if `\Psi>0` is
eventually proved); and (given `\tilde P_2<0`) `X_2/(2\tilde P_1)^2=\tilde
P_2 F_{21}F_{22}$, so pinning `\mathrm{sign}(X_2)` is data-equivalent to
pinning `\mathrm{sign}(F_{21}F_{22})` — i.e. "Lemma A" (`F_{21},F_{22}<0`
both) is, via this specific discriminant/resultant route, provably
equivalent in difficulty to `\Psi>0` itself, not a smaller sub-problem.

## Proof
`X_1X_2=(2\tilde P_1)^4\Phi(U_1)\Phi(U_2)=16\tilde P_1^4\tilde P_2^2\,
F_{11}F_{12}F_{21}F_{22}=16\tilde P_1^2\cdot\mathrm{Res}_U(q_1,\Phi)`, then
substitute the certified (corrected-constant) factorization of
`\mathrm{Res}_U(q_1,\Phi)`. Full derivation:
`ptolemy-trig-identity-parity-decomposition.md`, Steps 1–2.

## Independent verification (proof-reviewer, round 7)
Rebuilt from scratch (fresh `sympy` session, base definitions only,
50-digit precision, 5 independent random domain samples): confirmed
`X_1X_2` (computed directly via `\Phi(U_1),\Phi(U_2)`) matches
`16\tilde P_1^2\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos B)\Psi` to
relative error `<10^{-15}`, using the same corrected (no-leading-4) `\Psi`
definition as `radical-isolation-equals-psi.md`. No error found.

## Certification note
This is the structural counterpart, on the `q_1`-side, of
`radical-isolation-equals-psi.md` (`q_2`-side); both establish the same
qualitative fact via mirror computations. The key structural difference
from `lemmas/g2b-true-supplementary-parity.md` (where the analogous
resultant produced a manifest perfect square, giving an unconditional sign)
is explicitly noted and correct: here the analogous quantity is `\Psi`
itself, not a perfect square, so the chain closes back on the open problem.

## Reusable by
Any future attempt at Lemma A/B (or the master `\Psi>0` claim) via a
discriminant-product decomposition of `\Phi` at `q_1`'s roots — this lemma
shows that specific route does not simplify the problem.
