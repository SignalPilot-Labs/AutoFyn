## Lemma (First shared branch-crossing locus is exactly β=∠ABC)

In the symbolic rotation parametrization (`A=(0,0),B=(a,0),C=(b,cc)`,
`u=tan(β/2)`, `K=B+t1(-cosβ,sinβ)`), consider `G2a,G2b` (§ of
`symbolic-genericity-certificate.md`), the two branches of hypothesis 2's
polynomial. The resultant `Res_{s2}(G2a,G2b)` factors as
$$64\,u^2(u^2+1)^4\cdot F_1\cdot F_2\cdot F_3,$$
$$F_1 = 2au-2bu+cc\,u^2-cc = (1+u^2)\big[(a-b)\sin\beta-cc\cos\beta\big].$$
`F1=0` holds exactly when the direction of ray `BK`, `(-\cos\beta,\sin\beta)`,
is parallel to `B-C` — i.e. exactly at `β=∠ABC` (the moment `K`, extended
along its ray, reaches side `BC`, the natural upper boundary of "`K` inside
triangle `BMC`").

## Proof
Direct substitution (`1-u²=(1+u²)cosβ`, `2u=(1+u²)sinβ`) confirms the
displayed factorization of `F1` exactly (verified by `sympy.simplify`);
`(a-b)sinβ-cc\cosβ` is, up to sign, the 2D cross product of `(cosβ,sinβ)`
with `B-C=(a-b,-cc)`, hence vanishes iff these two vectors are parallel.

## Independent verification
Independently re-derived by the proof-reviewer (round 3): computed
`Res_{s2}(G2a,G2b)` via `sympy.resultant` on the reviewer's own
independently-built `G2a,G2b` (matching `coordinate-bash-resultant`'s
displayed polynomials) and confirmed the factorization
`64u²(u²+1)⁴·(2au−2bu+ccu²−cc)·(−2abu+accu²−acc+2b²u+2cc²u)·(2au⁴−4au²+2a−bu⁴−2bu²−b)`
exactly, and confirmed `F1 = (1+u²)[(a-b)sinβ-cc cosβ]` exactly by direct
symbolic substitution (residual 0).

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 3, §4).

## Status
Certified as an algebraic fact (the factorization and the parallel-vector
characterization of `F1=0`).

**Round 4 update — the stronger exactness claim is now also certified.**
`coordinate-bash-resultant-boundary.md` §7 (round 4) supplies the missing
uniqueness argument, independently re-verified by the proof-reviewer
(round 4): `F1=(1+u^2)[(a-b)\sinβ-cc\cosβ]` vanishes, for `u\in\mathbb R`
(equivalently `β\in(-\pi,\pi)` under the Weierstrass substitution, which is
a bijection onto this interval), exactly when `\sin(\beta-\varphi)=0` where
`\varphi\in(0,\pi)` is the polar angle of `C-B` (i.e. `\varphi=\angle ABC`
by the standard calibration of `β` from the `BA` direction). The zeros of
`\sin(\beta-\varphi)` are `\beta=\varphi+k\pi`; since the geometrically
relevant domain is `\beta\in(0,\pi)` and `\varphi` itself lies in `(0,\pi)`,
the only zero inside the domain is `\beta=\varphi=\angle ABC` itself (the
neighbors `\varphi-\pi\le0` and `\varphi+\pi\ge\pi` are both excluded). This
closes the previously-flagged gap: `F1=0\iff\beta=\angle ABC` **exactly**,
with no residual "parallel but supplementary" ambiguity. The reviewer
independently re-checked this reasoning (it is elementary given the
`(0,\pi)`-domain fact, which was itself independently reconfirmed) and
found no gap. See also `lemmas/branch-crossing-locus-equals-angle-C.md` for
the mirror statement for `F2=0\iff\beta=\angle ACB`, proved by the identical
argument.

Both the algebraic factorization and the exactness statement are now
certified unconditionally.
