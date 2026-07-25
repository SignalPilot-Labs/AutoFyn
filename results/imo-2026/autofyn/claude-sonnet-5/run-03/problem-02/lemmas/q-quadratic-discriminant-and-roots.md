## Lemma (Discriminant and exact roots of the scale-invariant `Q(m)` quadratic)

For a triangle with vertex angle `A` (at `A`) and free rotation parameter
`β` in the valid range, define, on the scale-invariant reformulation
`AB=1, AC=m` used by `coordinate-bash-resultant-boundary`,
$$Q(m) := m^2\sin(A+\beta) - 4m\sin\beta - 4\sin(A-\beta).$$
Then, for **every** `A\in(0,\pi)` and every real `β` (no sign hypothesis on
`\sin(A+3\beta)` or any other quantity needed):
$$\mathrm{disc}(Q) = 16\sin^2\beta + 16\sin(A+\beta)\sin(A-\beta) = 16\sin^2A > 0.$$
Consequently `Q` has two real, distinct roots (since `\sin A\ne0` for a
genuine triangle angle)
$$r_{1,2} = \frac{2(\sin\beta \mp \sin A)}{\sin(A+\beta)},\qquad
r_1 := \frac{2(\sin\beta-\sin A)}{\sin(A+\beta)} < r_2 := \frac{2(\sin\beta+\sin A)}{\sin(A+\beta)}$$
(strict ordering whenever `\sin(A+\beta)>0`, which holds throughout the
valid range `0<\beta<\min(\angle B,\angle C)` — see
`lemmas/branch-crossing-locus-equals-angle-B.md`/`-C.md` context), and the
exact factorization
$$Q(m) = \sin(A+\beta)\,(m-r_1)(m-r_2)$$
holds identically in `A,\beta,m`.

## Proof
Write `Q(m)=\alpha m^2+\beta_1 m+\gamma_1` with `\alpha=\sin(A+\beta)`,
`\beta_1=-4\sin\beta`, `\gamma_1=-4\sin(A-\beta)`. Then
`\mathrm{disc}(Q)=\beta_1^2-4\alpha\gamma_1=16\sin^2\beta+16\sin(A+\beta)\sin(A-\beta)`.
By the standard product-to-sum identity
`\sin(x+y)\sin(x-y)=\sin^2x-\sin^2y` (one line from the angle-addition
formulas — knowledge_base.md, trigonometric identities), with `x=A,y=\beta`,
this collapses to `16\sin^2\beta+16(\sin^2A-\sin^2\beta)=16\sin^2A`. Since
`A\in(0,\pi)`, `\sin A>0` strictly, so `\mathrm{disc}(Q)=16\sin^2A>0`
strictly. The quadratic formula then gives the stated roots exactly (using
`\sqrt{\mathrm{disc}(Q)}=4\sin A`, unambiguous since `\sin A>0`), and the
standard fact that a quadratic factors over its two roots with leading
coefficient `\alpha` gives the displayed factorization. All steps verified
by direct `sympy` symbolic expansion (`sympy.simplify` gives residual `0`
for both the discriminant identity and the factorization identity).

## Independent verification
Independently re-derived by the proof-reviewer (round 8) in a fresh `sympy`
session: confirmed `disc(Q) - 16 sin^2(A)` simplifies to `0` symbolically,
and `Q(m) - sin(A+β)(m-r1)(m-r2)` simplifies to `0` symbolically, using only
the bare definitions above (not copying any intermediate formula from the
approach file). No gap found.

## What this does NOT prove
This lemma is purely a fact about the quadratic `Q(m)`; it says nothing
about whether the actual triangle-shape value `m=\sin B/\sin(A+B)` (Law of
Sines) lies inside `(r_1,r_2)` under the hypotheses `Y>0,B_2>0` — that is
the separate, still-open two-part trigonometric inequality (I),(II) of
`coordinate-bash-resultant-boundary` §15.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 8, §15).

## Status
Certified.
