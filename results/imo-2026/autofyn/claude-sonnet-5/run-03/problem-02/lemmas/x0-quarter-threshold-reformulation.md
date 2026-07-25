# Lemma: exact radical-free reformulation of `X_0 \in (1/4,3/4)`

**Statement.** Let `A,B,C` be the angles of a genuine triangle
(`A,B,C>0`, `A+B+C=\pi`), `s=\sin A,c=\cos A,t=\sin B,d=\cos B`, and
`X_0:=\dfrac{ct}{2(sd+ct)}=\dfrac{\sin B\cos A}{2\sin(A+B)}`
(well-defined since `\sin C=sd+ct>0` always for a genuine triangle). Then
$$X_0>\tfrac14\iff ct>sd,\qquad\qquad X_0<\tfrac34\iff ct+3sd>0.$$

**Proof.** Since `\sin C=sd+ct>0` unconditionally,
$$X_0-\tfrac14=\frac{2ct-(sd+ct)}{4(sd+ct)}=\frac{ct-sd}{4\sin C},
\qquad
X_0-\tfrac34=\frac{2ct-3(sd+ct)}{4(sd+ct)}=\frac{-(ct+3sd)}{4\sin C}.$$
Both denominators are strictly positive, so the sign of each difference is
exactly the sign of its numerator, giving the two stated equivalences. `∎`

**Verification.** Confirmed as an exact symbolic identity
(`sympy.simplify` of both differences against the claimed closed forms
gives `0` identically, independent of any triangle constraint beyond
`sd+ct \ne 0`), and cross-checked numerically on 2,000,000 fresh random
`(A,B)` samples (`<10^{-13}` relative residual, consistent with floating
point noise only).

**Scope / caveat.** This is a pure algebraic identity in `c,s,d,t`; it does
**not** by itself establish `X_0\in(1/4,3/4)` on any particular domain —
that still requires proving `ct>sd` and `ct+3sd>0` on whatever domain is
under study (in the parent approach, the Case-(b)/`E<0` residual sub-case,
which remains open).

**Origin.** `coordinate-bash-resultant-boundary.md`, round 12 (Step 4
reformulation), certified by the round-12 proof-reviewer after independent
re-derivation.
