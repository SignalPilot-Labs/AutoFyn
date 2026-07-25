## Status
certified (round 6)

## Statement (`coordinate-bash-resultant-boundary.md` §13)
With the setup of `magnitude-bound-and-sign-coincidence.md`, a root `s_2` of
the extraneous branch `G_{2b}(s_2)=0` corresponds to the genuine
(non-supplementary) solution of hypothesis 2's unsquared equation
`\angle LBK=\angle LNC` (as opposed to the spurious squaring alternative
`\angle LBK=\pi-\angle LNC`) if and only if
$$W(s_2):=\mathrm{dot}(BL,BK)\cdot\mathrm{dot}(NL,NC)>0,$$
where `\mathrm{dot}(BL,BK)\propto D_K(s_2):=(bu^4-6bu^2+b+4cc\,u^3-4cc\,u)s_2
-(u^2+1)(au^2-a-bu^2+b-2cc\,u)` and `\mathrm{dot}(NL,NC)\propto D_N(s_2):=
2(b^2+cc^2)(u^2-1)s_2+(b^2+cc^2)(u^2+1)` (both affine in `s_2`, positive
proportionality constants). Then: **`G_{2b}`'s two roots (when both real)
always share the same true/supplementary status** — i.e. `W(r_1)W(r_2)\ge0`
for the two roots `r_1,r_2` of `G_{2b}`, throughout the valid range, for
every triangle.

## Proof
Direct resultant computation:
$$\mathrm{Res}_{s_2}(G_{2b},\,D_KD_N)=-4u(b^2+cc^2)^2(1+u^2)^6\,F_2\,
[2a(u^2-1)^2-b(u^2+1)^2]^2.$$
By the standard two-quadratics resultant-value formula
`\mathrm{Res}(f,g)=\mathrm{lc}(f)^2\,g(r_1)g(r_2)`, `W(r_1)W(r_2)=
\mathrm{Res}_{s_2}(G_{2b},D_KD_N)/B_2^2` where `B_2` is `G_{2b}`'s leading
coefficient. On the valid range `u>0` and `F_2<0` (already certified,
`branch-crossing-locus-equals-angle-C.md` + Lemma 11.6), so the prefactor
`-4u(b^2+cc^2)^2(1+u^2)^6\cdot F_2` is a product of a negative constant and
`F_2<0`, hence positive; multiplied by the perfect square
`[2a(u^2-1)^2-b(u^2+1)^2]^2\ge0` gives `\mathrm{Res}\ge0`, hence
`W(r_1)W(r_2)\ge0` (dividing by `B_2^2\ge0`).

## Independent verification (proof-reviewer, round 6)
Independently re-derived `G_{2b}` from scratch (own `sympy` session, direct
construction of the squared-cosine polynomial `(\dagger)` from the vector
definitions of hypothesis 2, division by `t_1^2`, factorization) — matches
the file's `G_{2b}` exactly. Independently re-derived `D_K,D_N`'s exact
closed forms via direct dot-product computation — exact match, zero
symbolic difference. Independently computed
`\mathrm{Res}_{s_2}(G_{2b},D_K^{\rm num}D_N^{\rm num})` via `sympy.resultant`
— matches the displayed closed form exactly (zero symbolic remainder).
Independently verified the two-quadratics resultant-value formula
`\mathrm{Res}(f,g)=\mathrm{lc}(f)^2g(r_1)g(r_2)` via a generic symbolic
check. Independently reproduced the numeric corroboration at smaller scale
(own fresh script, ~17,800 (triangle,β,G2b-root) samples): found 0 splits
among real-root cases, matching the theorem. Also independently reproduced
the disclosed `s_2>0`-scoping correction: without restricting to `s_2>0`,
found thousands of "counterexamples" to the population's joint
containment+sign exclusion conjecture (7,410 among ~17,800 in an independent
run); restricting to `s_2>0` and the true-root filter `W>0` gave 0
counterexamples in the same independent run — confirming the file's
diagnosis that the `s_2>0` physical constraint is essential and was
previously implicit, not a new finding invented after the fact.

## Reuse
The true/supplementary criterion `W(s_2)>0` and the "always same status"
theorem are reusable by any approach needing to identify the genuine branch
of a squared-cosine angle-equality construction of this general shape. The
remaining, NOT-yet-closed question (a full symbolic proof that no `s_2>0`,
`W>0` root of `G_{2b}` also passes the containment+sign test `L_1<0\wedge
\tilde N_2>0`) is explicitly NOT part of this certified lemma.
