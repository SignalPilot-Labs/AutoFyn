## Status
certified (round 7)

## Statement (Theorem 6 + Theorem 7 of `fixed-point-concyclic.md` §6)
Let `B,C\in\mathbb C^\times`, `B\ne C`, `K,L\in\mathbb C` arbitrary (no
geometric hypothesis required beyond `K\ne B,L\ne B,K\ne C` so that
`h_1=H_1(K,L),h_2=H_2(K,L),h_3=H_3(K,L)` are well defined), and
`M=B/2,N=C/2`. Write the three cleared hypothesis equations and the target
cross-ratio equation as bilinear forms in `(K,L)`:
`G_1=KL-CK-BL+BC(1-h_1)`, `G_2=KL-\tfrac C2K+(-B-\tfrac{h_2C}2)L+\tfrac
{BC}2(1+h_2)`, `G_3=KL+(-C-\tfrac{h_3B}2)K-\tfrac B2L+\tfrac{BC}2(1+h_3)`,
and `G_4=KL-\chi Q\,K+(-Q+\chi Q)L$ (`Q=(C\bar C-B\bar B)/(2(\bar C-\bar
B))$, the fixed point of `fixed-point-concyclic.md` Step 1). Let `\Delta$
be the `3\times3$ determinant of `(a_i,b_i,c_i)_{i=1,2,3}$ (the
`p,K,L$-coefficients of `G_1,G_2,G_3$); then

**(Theorem 6)** `\Delta = \tfrac{BC}4(1-h_2h_3)`, and (whenever `\Delta\ne0`)
`D_p\Delta=D_KD_L` where `D_p,D_K,D_L` are the Cramer's-rule numerators.

**(Theorem 7)** whenever additionally `D_1\ne0$ (the `4\times4$ determinant
of rows `G_1,G_2,G_3,(0,-Q,Q,0)`), the target cross-ratio is given exactly,
in closed form, by
$$\chi = -\frac{D_0}{D_1}, \qquad D_0:=\det(\text{rows }G_1,G_2,G_3,(1,0,-Q,0)).$$

## Proof
Standard linear algebra: `(KL,K,L)` is *the* solution of the `3\times3`
linear system `a_ip+b_iK+c_iL=-d_i$ (`i=1,2,3`, this is `G_i=0$ rewritten)
by construction, giving Theorem 6 by Cramer's rule uniqueness. For Theorem
7, `G_4=0$ adjoins a 4th linear equation which the true `(KL,K,L)$ also
satisfies; consistency of the resulting `4\times3$ overdetermined system
(with the rank-3 `3\times3$ sub-block nonsingular) forces the full
`4\times4$ augmented determinant to vanish; since row 4 is affine-linear in
`\chi` (`=u+\chi v`), the determinant is affine in `\chi$, giving
`D_0+\chi D_1=0`. Full proof: `fixed-point-concyclic.md` §6.2–6.3.

## Independent verification (proof-reviewer, round 7)
- Verified `\Delta=BC(1-h_2h_3)/4` symbolically from the displayed
  `a_i,b_i,c_i` (own `sympy` session, `3\times3` determinant), exact match.
- Verified Theorem 7's formula end-to-end **numerically, for a fully
  independent random configuration not from the file**: picked random
  complex `B,C,K,L` (not required to satisfy any geometric hypothesis, and
  the resulting `h_1,h_2,h_3` were NOT real), computed `h_1,h_2,h_3,Q$
  directly from their geometric ratio definitions, built the four rows, and
  compared `\chi_{\text{direct}}=L(K-Q)/(Q(K-L))$ against `-D_0/D_1$:
  agreement to `<4\times10^{-15}` absolute error. Confirms Theorem 6/7 hold
  as stated, unconditionally (no geometric/reality hypothesis used in the
  proof or in this check), exactly as claimed.

## What this lemma does NOT establish
`\chi\in\mathbb R$ is NOT established by this lemma alone; it requires the
further condition `\mathrm{Rem}(h_1,h_2,h_3,B,\bar B,C,\bar C)=0` (§6.4 of
the approach file), which is shown (by a completed Gröbner-basis
computation) to NOT be a formal algebraic consequence of `\Delta,D_0,D_1$'s
defining identities plus bare realness of `h_1,h_2,h_3` — i.e. the true
geometric hypotheses (positivity of `h_1,h_2,h_3`, and/or the specific
branch selected by containment) must supply additional information. This
remains the open gap for the `fixed-point-concyclic` route; the
proof-reviewer did not independently re-run the Gröbner-basis negative
check this round (time-limited) but found no reason to doubt it, given the
approach's established track record of honest, precisely-scoped negative
disclosures.

## Reusable by
Any future work on the `fixed-point-concyclic` route needing an explicit,
radical-free, closed-form expression for `\chi$ in terms of `H_1,H_2,H_3`.
