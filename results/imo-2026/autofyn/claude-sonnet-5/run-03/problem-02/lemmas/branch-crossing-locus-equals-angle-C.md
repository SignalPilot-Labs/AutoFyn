## Lemma (Second shared branch-crossing locus is exactly β=∠ACB)

In the symbolic rotation parametrization (`A=(0,0),B=(a,0),C=(b,cc)`,
`u=tan(β/2)`, `K=B+t1(-cosβ,sinβ)`, `L=C+s2·R(β)(A-C)`), consider
`G3a,G3b` (`lemmas/symbolic-genericity-certificate.md`), the two branches
of hypothesis 3's polynomial. The resultant `Res_{t1}(G3a,G3b)` (and,
symmetrically, `Res_{s2}(G2a,G2b)`) shares the factor
$$F_2 = -2ab\,u+a\,cc\,u^2-a\,cc+2b^2u+2cc^2u.$$
`F2=0` holds **exactly** when `β=∠ACB` (not merely up to a supplementary
ambiguity), and geometrically this is the moment ray `CL`, extended, reaches
side `BC` — the natural upper boundary of "`L` inside triangle `BNC`" —
mirroring `F1=0⟺β=∠ABC` (`lemmas/branch-crossing-locus-equals-angle-B.md`)
under the `B↔C, K↔L` symmetry.

## Proof

**Algebraic identification.** Solving `F2=0` for `u` and evaluating
`tanβ=2u/(1-u²)` at either root gives, symbolically,
$$\tan\beta\big|_{F_2=0} = \frac{a\cdot cc}{b^2+cc^2-ab}.$$
Independently, `tan(∠ACB)` computed via the signed cross/dot formula on
`CA=A-C=(-b,-cc)`, `CB=B-C=(a-b,-cc)`:
$$\tan(\angle ACB)=\frac{\mathrm{cross}(CA,CB)}{CA\cdot CB} = \frac{a\cdot cc}{b^2+cc^2-ab},$$
an exact match (both roots).

**Exactness/uniqueness.** By the identical argument certified for `F1`
(tan-injectivity on `(0,π)`, `β`'s domain being the open interval `(0,π)`
since it is a genuine angle of a non-degenerate configuration, and
`∠ACB∈(0,π)` itself): the only solution of `tanβ=tan(∠ACB)` inside
`β∈(0,π)` is `β=∠ACB` exactly, with no residual "parallel but
supplementary" ambiguity. Equivalently, `F2` is (up to the positive factor
`(1+u^2)^2`) the cross product of `(\cosβ,\sinβ)` with a fixed vector of
polar angle `∠ACB`, so `F2=0⟺\sin(\beta-\angle ACB)=0`, whose only zero in
`(0,\pi)` is `\beta=\angle ACB`.

## Independent verification (proof-reviewer, round 4)
Re-derived from scratch (own `sympy` session, own resultant computation):
reproduced `Res_{s2}(G2a,G2b)=64u^2(u^2+1)^4\cdot F_1\cdot F_2\cdot F_3`
with `F_1,F_2,F_3` exactly as reported (`F_3=(2a-b)u^4-(4a+2b)u^2+(2a-b)`,
matching the population's independently-computed value), confirmed
`tanβ|_{F_2=0}=a\,cc/(b^2+cc^2-ab)=\tan(\angle ACB)` by independent
symbolic computation (`sympy.solve` + signed cross/dot formula, exact
match), and confirmed the exactness/uniqueness argument is a straightforward,
correct consequence of `tan`-injectivity on `(0,\pi)` (no gap found).

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 4, §7), building on this round's `F2lens` math-explorer's
identification and the geometric confirmation (continuation-tracked
numerics on 4 triangles) that `F2=0` is the mirror boundary of `F1=0`: the
point where `L` (extended along ray `CL`) exits triangle `BNC` through
side `BC`.

## Status
Certified — both the algebraic identification `F2=0⟺β=∠ACB` and its
exactness (no supplementary ambiguity) are proved, independently
re-verified by the proof-reviewer. Note this lemma identifies only *where*
`F2=0` sits geometrically; it does **not** by itself establish that `F2`'s
root lies outside the valid parameter range for every triangle, nor does
it address the population's separate open finding (round 4) that a further,
un-shared resultant factor `F3` (see
`coordinate-bash-resultant-boundary.md` §9) *can* have roots strictly
inside the valid range — that question remains open and is not resolved by
this lemma.
