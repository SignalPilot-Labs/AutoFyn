## Theorem (an MVT/Lipschitz reduction of the whole Case-(b) target
`G(\beta_1)\ge0` to a single radical-free inequality `(\star)` in `A,B`
alone)

**Setup.** WLOG `\angle B\le\angle C` (`\gamma=\angle B<\pi/2`, so
`\cos B>0`). `K_c=2\sin A\sin(A+B)`,
`P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `Q=-\sin A\sin B`,
`f(\beta)=K_c+P\sin\beta+Q\cos\beta`, `G(\beta):=2K_c-f(\beta)`,
`\beta_0:=(\pi-A)/3`. Certified facts reused (`claim-I-closed-and-claim-
II-caseA-closed.md`): `f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)>0` on
`(0,\gamma)`, so `G'=-f'<0` strictly there. Given `X_0:=\sin B\cos A/
(2\sin(A+B))\in[0,1]` and `\beta_1\in(\beta_0,\gamma)` with `\cos\beta_1=
\sqrt{X_0}` (Case (b)'s domain, `\beta_0<\beta_1<\gamma`), prove
`G(\beta_1)\ge0`.

**Theorem (the reduction).** Define
`\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)` (an explicit
closed form in `A,B` alone, via `\beta_0=(\pi-A)/3`). Then:
- if `\mathrm{RHS}\le0`, `G(\beta_1)\ge0` unconditionally;
- if `\mathrm{RHS}>0`, `G(\beta_1)\ge0$ follows from
$$(\star)\qquad (1+\cos B)^2X_0\ \ge\ \mathrm{RHS}^2.$$

*Proof.* **Step 1 (Lipschitz bound).**
`f'(t)=\sin(A+t)\cos B+\sin(A+B-t)\le\cos B+1` for every `t` (since
`\sin(A+t)\le1`, `\cos B>0`, `\sin(A+B-t)\le1`).

**Step 2 (MVT bound on `f`).** `f` smooth, `f'\le1+\cos B` everywhere, so
`f(\beta_1)-f(\beta_0)=\int_{\beta_0}^{\beta_1}f'\,dt\le(1+\cos B)
(\beta_1-\beta_0)` (`\beta_1>\beta_0`). Since `G=2K_c-f`:
$$G(\beta_1)\ \ge\ G(\beta_0)-(1+\cos B)(\beta_1-\beta_0).\tag{MVT-1}$$

**Step 3 (MVT bound eliminating `\beta_1`).** `[\beta_0,\beta_1]\subset
(0,\pi/2)` (`\beta_1<\gamma<\pi/2`), so `\sin` is strictly increasing there:
`\cos\beta_0-\cos\beta_1=\int_{\beta_0}^{\beta_1}\sin t\,dt\ge\sin\beta_0
(\beta_1-\beta_0)`, i.e.
$$\beta_1-\beta_0\ \le\ \frac{\cos\beta_0-\cos\beta_1}{\sin\beta_0}
\qquad(\sin\beta_0>0).\tag{MVT-2}$$

**Step 4 (combine).** `1+\cos B>0`, so (MVT-2) gives `-(1+\cos B)
(\beta_1-\beta_0)\ge-(1+\cos B)(\cos\beta_0-\cos\beta_1)/\sin\beta_0`;
combined with (MVT-1):
$$G(\beta_1)\ \ge\ G(\beta_0)-(1+\cos B)\frac{\cos\beta_0-\cos\beta_1}
{\sin\beta_0}.\tag{\dagger}$$
It suffices that the right side is `\ge0`, i.e. (multiplying by
`\sin\beta_0>0`) `\sin\beta_0\,G(\beta_0)\ge(1+\cos B)(\cos\beta_0-
\cos\beta_1)`, i.e. `(1+\cos B)\cos\beta_1\ge\mathrm{RHS}`. Since
`\cos\beta_1=\sqrt{X_0}\ge0` and `1+\cos B>0`, the left side is `\ge0`
always: if `\mathrm{RHS}\le0` this holds trivially; if `\mathrm{RHS}>0`
both sides are `\ge0` so squaring is valid and equivalent, giving `(\star)`.
`\blacksquare`

**Status of `(\star)` itself.** NOT proved symbolically — tested
numerically (random sampling and global optimization) with the infimum of
`(1+\cos B)^2X_0-\mathrm{RHS}^2` over the valid domain found to be
`\approx0` (attained at the degenerate corner `\gamma\to\beta_0`), never
negative in any test, but this remains a conjecture, not a theorem.

**Negative finding (recorded so it is not re-attempted).** The cruder
bound obtained by replacing `\beta_1-\beta_0` with the full domain width
`\gamma-\beta_0` (i.e. testing `G(\beta_0)\ge(1+\cos B)(\gamma-\beta_0)`
directly, dropping Step 3) is FALSE in general — an explicit numerical
violation exists (`\approx-0.078` at `A\approx0.48,B\approx1.12`, well away
from any degenerate corner). The finer two-step MVT chain above (via
`\cos\beta_1$ rather than the raw domain width) is necessary.

## Independent verification (proof-reviewer, round 10)
`f'`'s closed form was independently re-derived symbolically (`sympy`,
zero residual). Every step of the reduction (Steps 1-4) is elementary
calculus/algebra and was independently re-derived by hand from the raw
definitions of `f,G,K_c,P,Q,\beta_0,\beta_1,X_0` — matches the source file
exactly, no gap. The final target `(\star)` and the antecedent
`G(\beta_1)\ge0` were independently checked over 2,000,000 random
`(A,B)` samples restricted to the true Case-(b) domain: `0` violations of
either `G(\beta_1)\ge0` (min value `\approx0.003`) or, among the subset
with `\mathrm{RHS}>0`, `(\star)` (min value `\approx0.005`) — both minima
occurring at the same corner `(A,B)\approx(0.407,0.914)` independently
found, matching the source file's own reported degenerate corner
`(0.4064,0.9117)`. The negative finding (crude bound false) was
independently reproduced exactly: own sampling found the same order-of-
magnitude violation `\approx-0.077` near the source file's own witness
`(A,B)\approx(0.48,1.14)`. Also independently confirmed the file's honest
"Step 0" self-correction: `G(\beta_0)>0` is false on `\approx11-23\%` of
the FULL `(A,B)` domain (own sampling: `\approx11.5\%`; order-of-magnitude
match, exact percentage sampling-distribution-dependent) but has `0`
violations restricted to the true Case-(b) domain (own 1,000,000-sample
sweep) — the reduction correctly does not rely on `G(\beta_0)>0` as a
separately-proved lemma, only as an intermediate quantity subsumed by the
final target.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md`
(round 10).

## Status
Certified (reduction itself is gap-free and reusable; `(\star)` remains
open).
