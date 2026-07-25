## Lemma (Symbolic, all-triangle genericity certificate for the central identity)

In the rotation parametrization of the family — `A=(0,0)`, `B=(a,0)`,
`C=(b,cc)` fully symbolic (any non-degenerate real triangle), `β` the free
angle of hypothesis 1, `u=tan(β/2)` the Weierstrass parameter,
`t1=BK>0`, `s2=CL/|AC|>0`,
$$K = B + t_1(-\cos\beta,\sin\beta), \qquad L = C + s_2\,R(\beta)(A-C),$$
— write `eq2, eq3` for the polynomial (squared-cosine) forms of hypotheses 2
(`∠LBK=∠LNC`) and 3 (`∠LCK=∠BMK`). By the homogeneity-decoupling lemma
(`homogeneity-decoupling-rotation-param.md`), `eq2 = t1²g2(s2,u,a,b,cc)`,
`eq3 = s2²g3(t1,u,a,b,cc)`, and each of `g2,g3` factors (via `sympy.factor`)
into an overall non-vanishing scalar/`(u²+1)` prefactor times two
polynomial branches:
$$g_2 = -(b^2+cc^2)^2(u^2+1)\,G_{2a}\,G_{2b}, \qquad g_3 = -a^2(u^2+1)\,G_{3a}\,G_{3b},$$
with `G2a,G3a` the branches quadratic in `s2` resp. `t1`, of degree 4 in `u`
(the other branches `G2b,G3b` are degree 6 in `u`). Let `T` be the numerator
(fully reduced, i.e. via `sympy.cancel`, coprime with its denominator) of
$$O\cdot(C-B) - \frac{|C|^2-|B|^2}{4}$$
where `O` is the circumcenter of `A,K,L` (Cramer's-rule closed form). Then
$$T \in \langle G_{2a}, G_{3a}\rangle \subset \mathbb Q[t_1,s_2,u,a,b,cc]$$
(Gröbner-basis ideal membership, grevlex order, 18 generators, remainder 0),
and `T` is in **neither** `⟨G2a⟩` nor `⟨G3a⟩` alone (the certificate
genuinely needs both constraints jointly).

Consequently: **for every real, non-degenerate triangle `A,B,C` and every
`(t1,s2,u)` with `t1,s2>0` on the branch `G2a=G3a=0`**, the target identity
`O·(C−B)=(|C|²−|B|²)/4` (equivalently `OM=ON`, via
`vector-reduction-OM-ON.md`) holds identically.

## What this does NOT prove
This lemma says nothing about *which* branch (`G2a=G3a=0` vs `G2b=G3b=0`)
the genuine geometric solution of the problem's hypotheses lies on — that
is a separate, still-open "branch selection" question (see
`results/imo-2026-02/approaches/coordinate-bash-resultant.md` §8–9 and
`coordinate-bash-resultant-boundary.md` §4).

## Independent verification
Independently reproduced from scratch by the proof-reviewer (round 3), in a
fresh `sympy` session using only the geometric definitions (not the
builders' scripts): built `K,L` from the stated formulas, built `eq2,eq3`
via the squared-cosine cross-equation on the four hypothesis vectors,
confirmed exact divisibility by `t1²`/`s2²`, confirmed the factored `G2a`
and `G3a` match the approach file's displayed polynomials term-for-term,
built the target `T` via `sympy.cancel` (a stricter, fully-reduced
numerator than the builders' `together/numer`, which can carry spurious
extra factors — reviewer's `T` has total degree 10, degree 4 in `u`,
differing cosmetically from the file's reported degree 12/6, but this is a
reporting-only discrepancy: the ideal-membership check gives remainder 0
either way), and confirmed `groebner([G2a,G3a],...).reduce(T) == 0` (18
generators) while `reduce(T)` modulo `⟨G2a⟩` alone or `⟨G3a⟩` alone is
nonzero. All checks passed.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant.md` (round 3, §§2–6),
independently re-derived by `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 3, §3).

## Status
Certified. This is the strongest single result the population has produced:
gap 1 (genericity, for every triangle) of the central identity is closed on
the correct branch. Supersedes `homogeneity-decoupling-rotation-param.md`'s
concrete-triangle-only scope for the downstream ideal-membership fact
(the homogeneity-decoupling fact itself remains separately certified and
correct). Branch selection (gap 2) remains open — do not cite this lemma as
closing the whole central identity unconditionally.
