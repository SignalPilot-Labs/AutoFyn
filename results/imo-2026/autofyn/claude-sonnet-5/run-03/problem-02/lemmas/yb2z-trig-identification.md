## Status
certified (round 7)

## Statement
Working with `A=(0,0), B=(a,0), C=(b,cc)` (`a,cc>0`), the rotation
parametrization `K=B+t_1(-\cos\beta,\sin\beta)`, `L=C+s_2 R(\beta)(A-C)`,
and the Weierstrass substitution `u=\tan(\beta/2)`, define:
- `Y := 2a(u^2-1)^2 - b(u^2+1)^2` (the un-shared resultant factor of
  `\mathrm{Res}_{s_2}(G_{2b},D_K)` / `\mathrm{Res}_{s_2}(G_{2b},D_N)`, and
  also of `\mathrm{Res}_{s_2}(G_{2a},D_K)` / `\mathrm{Res}_{s_2}(G_{2a},D_N)`
  — the same polynomial appears in both, `lemmas/f3-f3prime-resultant-factors.md`'s
  `F_3`),
- `B_2 :=` the leading (`s_2^2`) coefficient of `G_{2b}(s_2)`,
- `Z :=` defined by `\mathrm{Res}_{s_2}(G_{2b},\tilde N_2) = -8u(u^2+1)^2 F_2 Z`.

Then, exactly (zero remainder, full polynomial identity, not a numeric fit):
$$Y = (1+u^2)^2\bigl(2a\cos^2\beta - b\bigr),$$
$$B_2 = -2(1+u^2)^3\bigl(b\sin3\beta + cc\cos3\beta\bigr),$$
$$Z = (1+u^2)\bigl(p_1\sin\beta + q_1\cos\beta\bigr), \qquad
p_1 = b(2a-b)^2 + cc^2(b-4a),\quad q_1 = -cc(4a^2-b^2-cc^2).$$

Since `(1+u^2)^k>0` for every real `u`, these identities show
`\mathrm{sign}(Y)=\mathrm{sign}(2a\cos^2\beta-b)`,
`\mathrm{sign}(B_2)=-\mathrm{sign}(b\sin3\beta+cc\cos3\beta)`,
`\mathrm{sign}(Z)=\mathrm{sign}(p_1\sin\beta+q_1\cos\beta)`.

## Proof
Direct polynomial substitution `\sin\beta=2u/(1+u^2)`, `\cos\beta=(1-u^2)/(1+u^2)`
(and the triple-angle formulas `\sin3\beta=3\sin\beta-4\sin^3\beta`,
`\cos3\beta=4\cos^3\beta-3\cos\beta`) into the right-hand sides reproduces
the left-hand sides exactly, verified by full symbolic expansion (zero
remainder). Independently re-verified by the proof-reviewer (round 7, own
`sympy` session) for all three identities: `sympy.simplify(LHS-RHS)=0` in
each case, using the polynomials `Y, B_2, Z` exactly as displayed in
`coordinate-bash-resultant-boundary.md` §14 and §11.

## Certification note
This is a self-contained algebraic fact about the three displayed
polynomials `Y, B_2, Z`; the proof-reviewer independently re-verified the
trigonometric identity itself (exact, symbolic) but did not re-derive `Y,
B_2, Z` from the raw vector definitions from scratch this round (that
rebuild was performed independently by this round's outline-reviewer, who
confirmed exact agreement with the builder's polynomials). Certified as a
reusable structural fact; the outstanding open question is *positivity/sign
classification of the conditional trigonometric inequality*
`2a\cos^2\beta>b \wedge b\sin3\beta+cc\cos3\beta<0 \implies
p_1\sin\beta+q_1\cos\beta<0` on the valid `\beta`-range — NOT established by
this lemma, reconfirmed only numerically (independently reproduced by the
proof-reviewer at 300,000-sample scale, round 7, zero exceptions to the
"`(+,+,+)` forbidden" pattern).

## Reusable by
Any approach reasoning about `G_{2b}`'s branch-exclusion polynomials, or
about `F_3`'s (`=Y`, up to a positive constant) geometric meaning, via
trigonometric rather than raw-coefficient sign arguments.
