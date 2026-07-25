## Status
certified (round 5), with one corrected constant (cosmetic, not substantive)

## Statement
Let `\tau:=\tan\theta`. Define
$$\tilde P_1 = \sin A\,\tau(\tau\cos C-\sin C), \quad
\tilde Q_1 = \sin A\sin C(\tau^2+1) + 2\tau\sin B, \quad
\tilde R_1 = -2\tau^2\sin C\cos A - \tau\sin A\sin C + \sin A\cos C,$$
and `\tilde P_2,\tilde Q_2,\tilde R_2` the same with `B\leftrightarrow C`
swapped (`B=\pi-A-C`). Let `U,V` denote `\cot\alpha,\cot\alpha'` (the genuine
roots of `\tilde P_1U^2+\tilde Q_1U+\tilde R_1=0`,
`\tilde P_2V^2+\tilde Q_2V+\tilde R_2=0` respectively — certified,
`ptolemy-trig-branch-selection.md` + this round's Step 1), and
`L(U,V):=F-4=\sin A\cdot UV-\cos A(U+V)-\sin A-4` (`F` as in
`approaches/ptolemy-trig-identity.md` Round 4 Step 1). Write
`m:=\sin A\cdot U-\cos A`, `n:=-\cos A\cdot U-\sin A-4` (so `L=mV+n`), and
`\Phi(U):=\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2`.

Then, **with the corrected constant** (see Correction below):
$$\mathrm{Res}_U\bigl(\tilde P_1U^2+\tilde Q_1U+\tilde R_1,\ \Phi(U)\bigr) =
\sin^2A\cdot(\tau\cos C-\sin C)\cdot(\sin B-\tau\cos B)\cdot\Psi(\tau,A,C)$$
for an explicit polynomial `\Psi`, degree `6` in `\tau`, with
$$\Psi(0,A,C) = 4\sin^3A\,\sin B\,\sin C.$$
The two linear factors `\tau\cos C-\sin C` and `\sin B-\tau\cos B` never
vanish for `0<\theta<\min(B,C)` (since they vanish only at `\theta=C` resp.
`\theta=B`, excluded by the strict inequality) — hence on the open domain,
`\Psi(\tau,A,C)=0` is a **necessary** condition for `F=4` on any combination
of the (up to 4) branch choices of `(U,V)`.

## Correction (found by independent verification, round 5)
The approach file `ptolemy-trig-identity.md` (Round 5, Step 3) states the
prefactor as `4\sin^2A\cdot(\ldots)` (an extra factor of `4`). Independent
recomputation (two different rational-trig test triangles, exact rational
arithmetic, see Review) shows the resultant, divided by `4\sin^2A(\ldots)`,
gives a quotient whose constant term (`\tau=0`) is `\sin^3A\sin B\sin C`, a
factor of `4` short of the file's own claimed `\Psi(0,A,C)=4\sin^3A\sin B\sin
C`. Dividing instead by `\sin^2A(\ldots)` (no leading `4`) gives a quotient
matching `\Psi(0,A,C)=4\sin^3A\sin B\sin C` **exactly**, confirmed at two
independent rational test triangles. **This is a cosmetic transcription
error in the displayed constant (a stray factor of 4), not a substantive
error**: the resultant, the degree-6-in-`\tau` structure, the two spurious
linear factors, and the value `\Psi(0,A,C)=4\sin^3A\sin B\sin C` are all
independently confirmed exactly correct once the constant is corrected as
above. This lemma states the corrected form.

## Independent verification (proof-reviewer, round 5)
Rebuilt `\tilde P_1,\tilde Q_1,\tilde R_1,\tilde P_2,\tilde Q_2,\tilde
R_2,\Phi,L` from scratch (fresh sympy session) using algebraic symbols
`sa,ca,sc,cc` for `\sin A,\cos A,\sin C,\cos C` (with `\sin B=sa\cdot cc+
ca\cdot sc`, `\cos B = sa\cdot sc-ca\cdot cc`, from `B=\pi-A-C`), avoiding
slow trig simplification. Computed `\mathrm{Res}_U` directly via
`sympy.resultant` and divided by both candidate prefactors at two
independent rational-trig test triangles (`(\sin A,\cos A)=(4/5,3/5)`,
`(\sin C,\cos C)=(12/13,5/13)`; and a second pair `(8/17,15/17)`,
`(7/25,24/25)`): in both cases, division by the prefactor **without** the
leading `4` gives remainder `0` and quotient-at-`\tau=0` exactly
`4\sin^3A\sin B\sin C` (matching the file's own stated target); division
**with** the leading `4` also gives remainder `0` but quotient-at-`\tau=0`
off by a factor of `4`. Also independently re-verified Step 1 (the
substitution `U=\cot\theta+2\cot\psi` composed with the already-certified
`c_1x^2+b_1x+a_1=0` quadratic for `\cot\psi` gives a quadratic proportional
to `\tilde P_1U^2+\tilde Q_1U+\tilde R_1`) numerically at a generic point —
proportionality confirmed to high precision (ratio identical across all
three coefficients). Step 4 (the two linear factors are exactly the domain
boundaries `\theta=B,C`, via `\tan`-injectivity on `(0,\pi)\setminus\{\pi/2\}`)
is elementary and re-checked by hand, no gap. **`\Psi(\tau,A,C)>0` for
`\tau\ne0` remains unproven** (numeric only, 20,000 samples, zero
violations) — this is honestly disclosed by the builder as the approach's
sole remaining gap, not overclaimed.

## Used by
`approaches/ptolemy-trig-identity.md` Round 5 §Steps 1–7.
