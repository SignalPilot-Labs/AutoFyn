## Status
certified (round 7)

## Statement
Let `\tau=\tan\theta`, and let `q_1(U)=\tilde P_1U^2+\tilde Q_1U+\tilde R_1`,
`q_2(V)=\tilde P_2V^2+\tilde Q_2V+\tilde R_2` be the certified quadratics for
`U=\cot\alpha`, `V=\cot\alpha'` (`ptolemy-resultant-elimination-to-sextic.md`),
with roots `U_1,U_2` (resp. `V_1,V_2`), and `F(U,V):=\sin A\,UV-\cos
A(U+V)-\sin A`. Define `\Xi(V):=\mathrm{Res}_U(q_1(U), F(U,V)-4)`, a
quadratic `c_2V^2+c_1V+c_0` in `V`.

**(a)** `\Xi(V)=\tilde P_1\,(F(U_1,V)-4)(F(U_2,V)-4)` for all `V`
(instantiation of the standard quadratic-vs-linear resultant formula).

**(b)** Writing `\Xi(V_1)=(a+b\sqrt{\Delta_2})/(4\tilde P_2^2)` for explicit
radical-free `a,b` (`\Delta_2:=\tilde Q_2^2-4\tilde P_2\tilde R_2` the
discriminant of `q_2`), then
$$a^2-b^2\Delta_2 = 16\,\tilde P_2^2\sin^2A\,(\tau\cos C-\sin
C)(\sin B-\tau\cos B)\cdot\Psi(\tau,A,C),$$
where `\Psi` is the already-certified sextic
(`ptolemy-resultant-elimination-to-sextic.md`, defined via
`\mathrm{Res}_U(q_1,\Phi)=\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos
B)\Psi`, corrected constant, no leading `4`).

Since `\tau\cos C-\sin C<0` and `\sin B-\tau\cos B>0` throughout the domain
`D=\{0<\theta<\min(B,C)\}` (already certified,
`ptolemy-resultant-elimination-to-sextic.md`), the prefactor
`16\tilde P_2^2\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos B)` is strictly
negative throughout `D`, so
$$a^2-b^2\Delta_2<0 \iff \Psi(\tau,A,C)>0 \qquad\text{(exact equivalence, pointwise on } D\text{)}.$$

**Consequence (negative result).** The "single-radical-clearing" route
(comparing `a^2` vs. `b^2\Delta_2` to settle non-vanishing/sign of
`\Xi(V_1)`) is **provably equivalent in difficulty** to the master claim
`\Psi>0` itself — not a simplification. Any future attempt via this exact
route inherits the same difficulty as `\Psi>0`.

## Proof
(a) is the standard resultant-of-quadratic-against-linear-values identity,
already used repeatedly in this population. (b) follows by substituting the
quadratic formula for `V_1` into the quadratic `\Xi`, clearing the radical
(`s:=\sqrt{\Delta_2}`, `s^2=\Delta_2`), and combining `\Xi(V_1)\Xi(V_2)=(a+bs)(a-bs)=a^2-b^2\Delta_2`
with (a) applied at both `V_1,V_2` and the already-certified factorization
of `\mathrm{Res}_U(q_1,\Phi)` (which supplies the substitution
`\prod_{i,j}(F(U_i,V_j)-4) = \sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos
B)\Psi/(\tilde P_1^2\tilde P_2^2)`). Full derivation in
`ptolemy-trig-identity.md` Round 7, Steps 1–3.

## Independent verification (proof-reviewer, round 7)
Rebuilt the entire chain from scratch in a fresh `sympy`/high-precision
session, using only the base definitions (`\tilde P_1,\tilde Q_1,\tilde
R_1`, `\tilde P_2,\tilde Q_2,\tilde R_2`, `F(U,V)`) — not copying any
intermediate formula from the approach file. Confirmed, at 6 independent
random domain samples (50-digit precision):
- The corrected-constant `\Psi`-factorization identity
  `\mathrm{Res}_U(q_1,\Phi)=\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos
  B)\Psi` (no leading 4) holds to full precision, confirming the round-5
  correction is the one actually used in this round's derivation (the
  file's own restatement in Round 7 Step 3 is consistent with the
  corrected constant, not the stale round-5-displayed one).
- The master identity `a^2-b^2\Delta_2 = 16\tilde P_2^2\sin^2A(\tau\cos
  C-\sin C)(\sin B-\tau\cos B)\Psi` holds to relative error `<10^{-15}` at
  every sample.
No error found; this is a genuinely correct, rigorously-derived negative
result.

## Reusable by
Any future attempt at `\Psi>0` that considers radical-isolation on a single
one of the two roots of either quadratic — this lemma shows that route
collapses back to `\Psi` itself, saving future rounds from re-attempting it
expecting a computational shortcut.
