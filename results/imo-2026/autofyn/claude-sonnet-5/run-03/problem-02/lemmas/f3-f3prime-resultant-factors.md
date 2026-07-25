## Lemma (Identification of the un-shared resultant factors F3, F3′, and a counterexample to "always outside the valid range")

**Setting.** As in `lemmas/symbolic-genericity-certificate.md` and
`lemmas/branch-crossing-locus-equals-angle-B.md`/`-C.md`, with
`A=(0,0),B=(a,0),C=(b,cc)`, `u=\tan(\beta/2)`:
$$\mathrm{Res}_{s_2}(G_{2a},G_{2b}) = 64u^2(u^2+1)^4\cdot F_1\cdot F_2\cdot F_3,\qquad F_3=(2a-b)u^4-(4a+2b)u^2+(2a-b),$$
$$\mathrm{Res}_{t_1}(G_{3a},G_{3b}) = -64(b^2+cc^2)a\,u^2(u^2+1)^4\cdot F_1\cdot F_2\cdot F_3',\qquad F_3'=(ab-2b^2-2cc^2)u^4+(2ab+4b^2+4cc^2)u^2+(ab-2b^2-2cc^2).$$

**Algebraic identification (proved).** Both are palindromic quartics in
`u` (coefficient of `u^4` = constant term), hence symmetric under
`u\mapsto1/u`, i.e. `\beta\mapsto\pi-\beta`. Back-substituting
`u=\tan(\beta/2)`:
$$F_3=0 \iff \cos^2\beta=\frac{b}{2a},\qquad F_3'=0\iff\cos^2\beta=\frac{ab}{2(b^2+cc^2)}.$$

**Counterexample to "F3's root always lies outside the valid range"
(disproves an implicit assumption carried since round 3).** Triangle
`A=(0,0),B=(1,0),C=(0.9,0.2)`: `\angle ABC\approx63.435°`,
`\angle ACB\approx104.036°`, so the valid range (per
`lemmas/branch-crossing-locus-equals-angle-B.md`/`-C.md`) is
`(0°,63.435°)`. Here `b/(2a)=0.45`, giving `F_3=0` at
`\beta=\arccos\sqrt{0.45}\approx47.870°` — **strictly inside** the valid
range. A systematic random search over 4000 triangles found 12 further
such triangles among the first dozen hits.

**Numerical finding (not proved in general): at every crossing checked,
the genuine solution branch survives undisturbed.** At the counterexample
triangle's crossing (`\beta\approx47.87°`), the two roots of `G_{2a}(s_2,u)`
(as a quadratic in `s_2`) are `s_2\approx\{0.0502,\ 0.745\}` and of
`G_{2b}(s_2,u)` are `s_2\approx\{0.108,\ 0.745\}` — the *shared* root
responsible for the resultant vanishing is `s_2\approx0.745`, which is
**not** the genuine branch's root (`s_2\approx0.0502`, tracked continuously
via the true unsquared hypothesis-2 equation and confirmed to satisfy
`G_{2a}\approx0` throughout a fine `\beta`-sweep straddling the crossing).
This shows the resultant-zero condition is necessary but not sufficient
for the genuine branch to actually swap — but this was checked only at a
handful of crossings, not proved for every triangle and every crossing.

## Independent verification (proof-reviewer, round 4)
Independently reproduced, from scratch (own `sympy`/`scipy` session): the
exact resultant factorization (`F_1,F_2,F_3` byte-for-byte, including the
extraction of `G_{2a}` as the degree-4-in-`u` quadratic-in-`s_2` cofactor);
`F_3/(1+u^2)^2` symbolically simplifies to `2a\cos^2\beta-b` exactly
(`sympy.simplify`, residual 0); the counterexample triangle's `F_3=0` root
at `\beta\approx47.870°`, strictly inside `(0,63.435°)`, confirmed
independently; and the "harmless crossing" numerics reproduced
independently via continuation-tracked root-finding on the true (unsquared)
hypothesis-2 equation, confirming `G_{2a}\approx0` (`<10^{-13}`) throughout
the sweep while the shared resultant-zero root (`s_2\approx0.745`) is a
distinct, non-genuine value — matches the approach file's own reported
interpretation exactly.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 4, §9), correcting an implicit assumption in round 3's single-triangle
numerics (that these factors always lie outside the valid range).

## Status
The algebraic identification of `F_3,F_3'` and the counterexample
(disproving "always outside the range") are **certified** — both proved/
confirmed exactly, no gap. The "genuine branch survives every crossing
harmlessly" claim is **not certified** — it remains open, checked at only
a small number of crossings (independently re-confirmed at one), with no
general proof attempted or found. Any approach reusing this lemma must
treat the survival claim as a conjecture backed by consistent (but
limited) numerical evidence, not a proved fact.
