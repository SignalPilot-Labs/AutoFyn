## Status
certified (round 5)

## Statement
Work in the rotation parametrization `A=(0,0), B=(a,0), C=(b,cc)` (CCW,
`a,cc>0`), `K=B+t_1(-\cos\beta,\sin\beta)`, `L=C+s_2 R(\beta)(A-C)`,
`u=\tan(\beta/2)`. Let
$$G_{2a}(s_2,u,a,b,cc)= 2au^3+2au-4bs_2^2u^3-4bs_2^2u-4bs_2u^3+4bs_2u-2bu^3-2bu$$
$$\qquad{}+2cc\,s_2^2u^4-2cc\,s_2^2+3cc\,s_2u^4-2cc\,s_2u^2+3cc\,s_2+cc\,u^4-cc$$
(the degree-4-in-`u` branch cofactor of hypothesis 2, certified in
`symbolic-genericity-certificate.md`), and let
`F_1=2au-2bu+cc\,u^2-cc`, `F_2=-2ab\,u+a\,cc\,u^2-a\,cc+2b^2u+2cc^2u` (certified
in `branch-crossing-locus-equals-angle-B.md`/`-C.md`, with `F_1=0\iff\beta=
\angle ABC`, `F_2=0\iff\beta=\angle ACB`, each the unique zero in
`\beta\in(0,\pi)`).

Then, for every triangle `A,B,C` and every `\beta` in the valid range
`(0,\min(\angle ABC,\angle ACB))`:

1. **(Explicit affine form.)** Given the standing hypothesis `L\in\triangle
   BNC`, "K lies inside angle LBA" is equivalent to `L_1(s_2)<0`, where
   `L_1(s_2):=P(u)+s_2Q(u)`,
   $$P(u)=(1+u^2)F_1(u), \qquad Q(u)=-4bu^3+4bu+cc\,u^4-6cc\,u^2+cc.$$
2. **(Leading-coefficient sign.)** The coefficient of `s_2^2` in `G_{2a}`,
   `A_2:=2(1+u^2)(cc(u^2-1)-2bu)`, satisfies `A_2<0` throughout the valid
   range, for every triangle (proved by a case split on `\mathrm{sign}(b)`:
   trivial for `b\ge0`; via `\tan(\angle B)<\tan\theta_0` for `b<0`, using
   that `b<0\Rightarrow\angle A` obtuse `\Rightarrow\angle B,\angle C<\pi/2`).
3. **(Resultant identity.)** `\mathrm{Res}_{s_2}(G_{2a},L_1) =
   4u(1+u^2)^3F_1F_2` (a polynomial identity in `a,b,cc,u`, independently
   verified — see Review).
4. **(Main theorem.)** `G_{2a}(s_2)=0` (a quadratic in `s_2`) always has two
   distinct real roots on the valid range, and exactly one of them satisfies
   `L_1(s_2)<0` (i.e. "K inside angle LBA," given `L\in\triangle BNC`); the
   other fails it.

By the certified `σ`-symmetry, the mirror statement holds for `G_{3a}` and
"L inside angle ACK" (given `K\in\triangle BMC`).

## Proof
See `approaches/coordinate-bash-resultant-boundary.md` §11 (Lemmas
11.1–11.7, Theorem 11.8, Theorem 11.10). Sketch: `F_1,F_2<0` throughout the
valid range (each has its unique zero in `(0,\pi)` exactly at the *upper*
endpoint of the range or beyond, so by IVT from `F_1(0)=-cc<0`, `F_2(0)=
-a\cdot cc<0`, they stay negative on the whole open range), so `F_1F_2>0`;
combined with `u>0` (valid range `\subset(0,\pi/2)`) and `A_2<0`, the
resultant identity gives
`L_1(r_1)L_1(r_2)=4u(1+u^2)^3F_1F_2/A_2<0`. A real quadratic with real
coefficients whose two roots give a negative product of `L_1`-values at
those roots cannot have complex-conjugate roots (else `L_1(r_1)L_1(r_2)=
|L_1(r_1)|^2\ge0`), so the roots are real; and since the product of the two
real values `L_1(r_1),L_1(r_2)` is negative, they have opposite signs. ∎

## Independent verification (proof-reviewer, round 5)
Rebuilt from scratch, in a fresh sympy session, using ONLY the geometric
construction and the already-certified `G_{2a}` (from
`coordinate-bash-resultant.md` §4) and `F_1,F_2` formulas (from the
already-certified `branch-crossing-locus-equals-angle-B/C.md`):
- Recomputed `L=C+s_2R(\beta)(A-C)`, `d(\beta)=(-\cos\beta,\sin\beta)`, and
  `\mathrm{cross}(d,L-B)` directly via the Weierstrass substitution, using
  `sympy.cancel` (not `together`, which can leave a spurious un-canceled
  common factor — a real pitfall hit and corrected mid-verification).
  Confirmed the *exactly reduced* numerator is affine in `s_2` with
  `P(u)=(1+u^2)F_1(u)` and `Q(u)=-4bu^3+4bu+cc\,u^4-6cc\,u^2+cc`, matching
  Lemma 11.5 term-for-term (zero difference, symbolic).
- Recomputed the coefficient of `s_2^2` in `G_{2a}` directly from the
  displayed polynomial: `A_2=2(1+u^2)(cc(u^2-1)-2bu)`, matching Lemma 11.7's
  stated formula exactly, and independently reconfirmed the Weierstrass
  back-substitution `A_2=-2(1+u^2)^2(cc\cos\beta+b\sin\beta)`.
- Computed `\mathrm{Res}_{s_2}(G_{2a},L_1)` directly via `sympy.resultant`
  and confirmed it equals `4u(1+u^2)^3F_1F_2` **exactly** (symbolic
  difference `0`, verified by `sympy.expand`), independently of the
  builder's own computation. This is a genuine, fully general (all `a,b,cc`)
  polynomial identity, not a numerical check.
No gap found in Theorem 11.8/11.10 as stated. **What this lemma does NOT
establish** (correctly, and honestly, not claimed by the builder): whether
the extraneous branch `G_{2b}` can also produce a competing root passing
both containment and the sign test (checked only numerically, found to lack
the same fixed-sign structure); the magnitude bound `t_1<t_1^{\max}(\beta)`;
and the population's standing (separately unproven) identification of
`G_{2a}=0` as the actual geometrically genuine branch.

## Used by
`coordinate-bash-resultant-boundary.md` §11.
