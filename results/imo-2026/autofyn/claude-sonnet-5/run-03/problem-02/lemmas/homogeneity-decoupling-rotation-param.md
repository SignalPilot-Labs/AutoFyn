## Lemma (Homogeneity/decoupling of the rotation parametrization)
In the rotation parametrization of the family (A at the origin, β the free
angle of hypothesis 1, t1=BK, t2=CL):
$$K = B + t_1(-\cos\beta,\sin\beta), \qquad L = C + t_2\cdot R(\beta)\frac{A-C}{|AC|},$$
the polynomial form of hypothesis 2 (∠LBK=∠LNC, via the squared-cosine
cross-multiplication device) is independent of $t_1$ up to an overall factor
$t_1^2$: $eq_2 = t_1^2\cdot g_2(t_2,\beta)$. Symmetrically, hypothesis 3's
polynomial form ($\angle LCK=\angle BMK$) is independent of $t_2$ up to an
overall factor $t_2^2$: $eq_3 = t_2^2\cdot g_3(t_1,\beta)$.

## Proof
$BK = K-B = t_1\cdot(-\cos\beta,\sin\beta)$ is exactly homogeneous in $t_1$
(zero intercept: $K=B$ when $t_1=0$), so $|BK|^2=t_1^2$ identically (using
$\sin^2\beta+\cos^2\beta=1$), and for any fixed vector $V$,
$V\cdot BK = t_1\cdot(V\cdot(-\cos\beta,\sin\beta))$ is linear-homogeneous
in $t_1$. In the squared-cosine identity used to encode
$\angle LBK=\angle LNC$,
$$(BL\cdot BK)^2\,|NL|^2|NC|^2 = (NL\cdot NC)^2\,|BL|^2|BK|^2,$$
every term on both sides carries an overall factor of $|BK|^2=t_1^2$ (the
left side via $(BL\cdot BK)^2$, the right side via $|BK|^2$ directly), so
the whole equation factors as $t_1^2\cdot(\text{an equation not involving }
t_1)$. The argument for hypothesis 3 and $t_2$ (via $CL=t_2\cdot
R(\beta)(A-C)/|AC|$, exactly homogeneous in $t_2$) is symmetric. ∎

**Geometric meaning.** Hypothesis 2 depends only on the *direction* of ray
BK (fixed by β), not on how far K is along it, so it cannot constrain $t_1$;
symmetrically for hypothesis 3 and $t_2$. This is a coordinate-free fact
about the vertex-angle structure, not an artifact of the specific
coordinates chosen.

## Independent verification
Re-derived independently by proof-reviewer (round 2) via direct `sympy`
computation on the concrete triangle A=(0,0), B=(2,0), C=(3/5,4/5) with the
Weierstrass substitution $u=\tan(\beta/2)$: computed `eq2`, divided by
$t_1^2$, confirmed the quotient is free of $t_1$ and matches the reported
factorization $g_2 = -G_{2a}\cdot G_{2b}$ (and symmetrically for `eq3`,
$g_3=-4\,G_{3a}\cdot G_{3b}$) term-for-term with the polynomials stated in
`coordinate-bash-resultant.md`.

## Source
Derived in `results/imo-2026-02/approaches/coordinate-bash-resultant.md`
(round 2, §3).

## Status
Certified — reusable by any coordinate approach using this or an equivalent
rotation parametrization; reduces a 4-variable elimination
($t_1,t_2,\sin\beta,\cos\beta$) to two independent 2-variable problems.
