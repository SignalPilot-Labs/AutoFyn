## Status
certified (round 6)

## Statement (Theorem 12.6, `coordinate-bash-resultant-boundary.md` §12)
Setting: `A=(0,0), B=(a,0), C=(b,cc)` (`a,cc>0`, CCW, scalene), `M`=midpoint
`AB`, `N`=midpoint `AC`, `β` in the valid range `(0,\min(\angle ABC,\angle
ACB))`, `u=\tan(\beta/2)`, `K=B+t_1(-\cos\beta,\sin\beta)` (`t_1>0`),
`L=C+s_2R(\beta)(A-C)` (`s_2>0`). Let `G_{2a}(s_2), G_{3a}(t_1)` be the
degree-4-in-`u`, quadratic-in-`(s_2` resp. `t_1)` branch cofactors of
`homogeneity-decoupling-rotation-param.md` (explicit formulas in
`coordinate-bash-resultant.md` §4). Then, for **every** scalene triangle and
every `β` in the valid range:

1. `G_{3a}(t_1)=0` has two real roots, exactly one of which places
   `K=B+t_1d(\beta)` on the correct (`B`-)side of line `MC` — combined with
   the (already-certified) ray-direction fact that `d(\beta)` stays strictly
   inside `\angle ABC`, this places `K` strictly inside the finite triangle
   `BMC`. Symmetrically, exactly one root of `G_{2a}(s_2)=0` places `L`
   strictly inside `\triangle BNC`.
2. That magnitude-bound-selecting root of `G_{3a}` (resp. `G_{2a}`) is
   **exactly** the root already selected by `cross-product-sign-selection-G2a.md`'s
   Theorem 11.10 (resp. 11.8) sign test ("L inside angle ACK" / "K inside
   angle LBA") — the two selection criteria always coincide, no separate
   case analysis needed.

## Proof
Via: (a) an affine-vs-quadratic resultant identity (mirroring Lemma 11.5's
method) for the containment tests `\tilde N_1(t_1):=(1+u^2)\,
\mathrm{cross}(C-M,K-M)` (K-vs-edge-MC) and `\tilde N_2(s_2):=4(1+u^2)\,
\mathrm{cross}(B-N,L-N)` (L-vs-edge-NB):
$$\mathrm{Res}_{t_1}(G_{3a},\tilde N_1)=\tfrac a4\,u\,A_3\,[(a-2b)^2+4cc^2]\,F_1,\qquad
\mathrm{Res}_{s_2}(G_{2a},\tilde N_2)=4u\,A_2\,[(2a-b)^2+cc^2]\,F_2,$$
where `A_2=A_3=2(1+u^2)(cc(u^2-1)-2bu)` is `G_{2a}/G_{3a}`'s shared leading
coefficient and `F_1,F_2<0` throughout the valid range (already certified,
`branch-crossing-locus-equals-angle-B/C.md` + Lemma 11.6); (b) a new general
"root-pairing lemma": if a real quadratic `f=At^2+Bt+C` has two distinct
real roots `r_1<r_2`, and real affine `X,Y` (nonzero slopes) each satisfy
`X(r_1)X(r_2)<0`, `Y(r_1)Y(r_2)<0`, then `\mathrm{sign}(X(r_1))=
\mathrm{sign}(Y(r_1))\iff\mathrm{sign}(\text{slope}(X))=\mathrm{sign}
(\text{slope}(Y))` (proved by locating each affine function's unique zero
strictly between `r_1,r_2` via IVT); (c) three trigonometric sign facts,
each proved via a general "single-crossing sinusoid" lemma (an interval
shorter than one half-period of `p\sin k\beta+q\cos k\beta` with both
endpoints positive has no interior zero) plus explicit closed-form endpoint
values at `\beta=\angle ABC,\angle ACB` (using "larger angle opposite larger
side"): `Q^{\rm ptrig}(\beta):=(b-a/2)\sin\beta+cc\cos\beta>0`,
`Q^{\rm trig}(\beta):=b\sin2\beta+cc\cos2\beta>0`,
`R^{\rm trig}(\beta):=\tfrac12(b^2+cc^2-2ab)\sin\beta-a\,cc\cos\beta<0`,
throughout the entire valid range, for every scalene triangle.

## Independent verification (proof-reviewer, round 6)
Rebuilt from scratch (fresh `sympy` session, own script, using only the
already-certified explicit `G_{2a},G_{3a}` polynomials): confirmed `A_2=A_3`
exactly (symbolic subtraction, 0); confirmed `\tilde N_1,\tilde N_2`'s exact
closed forms via direct cross-product computation from the coordinate
definitions (both match the file's Lemmas 12.1/12.3 with zero symbolic
difference); confirmed both resultant identities
`\mathrm{Res}_{t_1}(G_{3a},\tilde N_1)` and `\mathrm{Res}_{s_2}(G_{2a},
\tilde N_2)` exactly via `sympy.resultant`, matching the file's displayed
closed forms with zero symbolic remainder; independently verified the
resultant-value formula `\mathrm{Res}(f,g)=\mathrm{lc}(f)\,g(r_1)g(r_2)` for
a quadratic `f` against a linear `g` via a generic symbolic identity check
(0 remainder); confirmed the root-pairing lemma's IVT proof by hand (sound,
no gap); confirmed all three trig-sign closed forms at the range endpoints
(`\beta=0,\angle ABC,\angle ACB`) by direct symbolic/numeric substitution on
5 random triangles (exact match to the displayed closed forms in every
case); confirmed the "single-crossing" sub-lemma's proof by hand (sound
IVT/simple-zero argument). No gap found; the scalene hypothesis is used
essentially only at one point (excluding the isosceles equality case in the
`Q^{\rm trig}(\gamma)\ge0` bound), consistently with the population's
standing scalene convention.

## Reuse
Fully general, all-triangle, all-`β` (within the valid range) result. Closes
`coordinate-bash-resultant-boundary.md` §8's long-standing magnitude-bound
gap outright: combined with `cross-product-sign-selection-G2a.md`, the
single sign-test-selected root of `G_{2a}=G_{3a}=0` now provably satisfies
containment in its own triangle **and** both of the problem's "inside the
angle" hypotheses simultaneously, at every `β` in the valid range, for every
triangle. Does **not** by itself rule out the extraneous branch `G_{2b}`
(that is `coordinate-bash-resultant-boundary.md` §13's separate, still-open
question).
