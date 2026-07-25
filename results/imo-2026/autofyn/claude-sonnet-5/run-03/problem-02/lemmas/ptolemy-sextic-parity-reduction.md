## Status
certified (round 6)

## Statement (`ptolemy-trig-identity.md` Round 6, Steps 1-3)
With the setup of `ptolemy-resultant-elimination-to-sextic.md`
(`q_1(U)=\tilde P_1U^2+\tilde Q_1U+\tilde R_1`, `q_2(V)=\tilde
P_2V^2+\tilde Q_2V+\tilde R_2`, `F(U,V)=\sin A\cdot UV-\cos A(U+V)-\sin A`,
`L=F-4`, `\Phi(U):=\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2` with
`m=\sin A\cdot U-\cos A`, `n=-\cos A\cdot U-\sin A-4`), let `U_1,U_2` be the
roots of `q_1` and `V_1,V_2` the roots of `q_2`. Then:

**(Multiplicative identity.)**
$$\mathrm{Res}_U(q_1,\Phi) = \tilde P_1^2\tilde P_2^2\prod_{i,j\in\{1,2\}}
\bigl(F(U_i,V_j)-4\bigr).$$

**(Sign lemma.)** For every `(\theta,A,B,C)` with `0<\theta<\min(B,C)`,
`A,B,C>0`, `A+B+C=\pi`: `\tau\cos C-\sin C<0` and `\sin B-\tau\cos B>0`
(`\tau=\tan\theta`); consequently `\tilde P_1,\tilde P_2<0` throughout the
domain.

**(Parity reduction.)** Combined with the certified factorization
`\mathrm{Res}_U(q_1,\Phi)=\sin^2A\cdot(\tau\cos C-\sin C)(\sin B-\tau\cos
B)\cdot\Psi(\tau,A,C)`:
$$\Psi(\tau,A,C)>0 \iff \prod_{i,j}\bigl(F(U_i,V_j)-4\bigr)<0 \iff
\text{an odd number (1 or 3) of the four values } F(U_i,V_j) \text{ exceed }4$$
(generically, away from the measure-zero locus where some `F(U_i,V_j)=4`
exactly).

## Proof
Multiplicative identity: by the standard resultant-via-roots formula
`\mathrm{Res}(f,g)=\mathrm{lc}(f)^{\deg g}\prod_ig(\alpha_i)`, resultant
multiplicativity in the second argument
(`\mathrm{Res}_U(f,gh)=\mathrm{Res}_U(f,g)\mathrm{Res}_U(f,h)`), and the
factorization `\Phi(U)=\tilde P_2\cdot L(U,V_1)\cdot L(U,V_2)` (since
`\Phi(U)=m^2q_2(-n/m)` and `q_2(V)=\tilde P_2(V-V_1)(V-V_2)`). Sign lemma:
elementary case split on `\mathrm{sign}(\cos C)` (resp. `\cos B`) using
`\theta<\min(B,C)<\pi/2` and monotonicity of `\tan` on `(0,\pi/2)`. Parity
reduction: sign bookkeeping of the prefactor `\tilde P_1^2\tilde
P_2^2/[\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos B)]`, which is strictly
negative throughout the domain (positive numerator, strictly negative
denominator).

## Independent verification (proof-reviewer, round 6)
Independently re-derived the multiplicative identity with **fully generic**
symbols `P1,Q1,R1,P2,Q2,R2,sinA,cosA` (own `sympy` session, not the
builder's `A,B,C`-specific setup) — confirmed `\mathrm{Res}_U(q_1,\Phi) =
P_1^2P_2^2\prod_{i,j}(F(U_i,V_j)-4)` exactly (zero symbolic remainder),
independent of any triangle-specific substitution — this is a strictly
stronger check than a numeric/specific-triangle verification, since it
confirms the identity as a general algebraic fact, not a trig coincidence.
Independently confirmed the sign lemma numerically on 5 random triangles
(both inequalities held with correct sign in every case). Independently
confirmed, via the certified `ptolemy-resultant-elimination-to-sextic.md`,
that Round 6's version of the resultant factorization (no leading `4`)
matches the certified corrected constant, not the stale round-5 draft value
still displayed elsewhere in the approach file's historical Round-5 section
— Round 6's own derivation is internally consistent with the correction.
Independently reproduced the odd-parity pattern (2000/2000 random domain
samples, using the certified `\tilde P_1,\ldots,\tilde R_2` formulas rebuilt
independently) with zero exceptions, corroborating (not proving) Step 4's
disclosed open claim.

## Reuse
Reduces `\Psi(\tau,A,C)>0` (a degree-6-in-`\tau` positivity question with
unwieldy trigonometric coefficients) to a parity question about four
explicit real numbers, each a value of the fixed bilinear form `F` at one of
the four combinations of roots of two already-understood quadratics. **Does
NOT itself close the gap**: the parity claim (that exactly the
genuine-genuine combination `F(U_1,V_1)` exceeds 4, the other three never
do) remains open, numerics-only (2000+8 samples, 0 exceptions across two
independent implementations).
