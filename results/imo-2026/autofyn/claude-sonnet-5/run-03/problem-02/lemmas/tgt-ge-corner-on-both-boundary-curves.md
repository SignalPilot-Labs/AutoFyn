# Lemma: `Tgt ≥ Tgt(corner)` on both boundary curves of D, via certified interval arithmetic

**Source.** Proved in `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`,
round 15, "Theorem B" and "Theorem C."

**Setup.** `X_0(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`,
`\beta_0(A):=(\pi-A)/3`, `K_c=2\sin A\sin(A+B)`,
`P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `Q=-\sin A\sin B`,
`G(\beta_0):=K_c-P\sin\beta_0-Q\cos\beta_0`,
`\mathrm{RHS}:=(1+\cos B)\cos\beta_0-\sin\beta_0\,G(\beta_0)`,
`D_2:=\partial\mathrm{RHS}/\partial B`,
`T_1:=(1+\cos B)^2\partial X_0/\partial B-2(1+\cos B)\sin B\,X_0`,
`\mathrm{Tgt}(A,B):=4(1+\cos B)^2X_0D_2^2-T_1^2`. The domain `\mathcal D`
has two boundary curves relevant near the corner `(\pi/3,\pi/3)`:
`\mathcal C_{\mathrm{hi}}=\{B=(\pi-A)/2\}` and
`\mathcal C_{\mathrm{lo}}=\{X_0=\cos^2B\}`.

**Statement.**
$$
\mathrm{Tgt}(A,(\pi-A)/2)\ge\mathrm{Tgt}(\pi/3,\pi/3)\quad\text{for all
}A\in[0.5,\pi/3),
$$
$$
\mathrm{Tgt}(A(B),B)\ge\mathrm{Tgt}(\pi/3,\pi/3)\quad\text{for all
}B\in[0.9,\pi/3),
$$
where `A(B)` is the closed-form parametrization of `\mathcal C_{\mathrm{lo}}`
from `lemmas/clo-closed-form-parametrization.md`. Both ranges are safe
supersets of the true domain-restricted valid ranges of the respective
curves (`A_L\approx0.55788\ldots>0.5` for `\mathcal C_{\mathrm{hi}}`;
`B^\ast\approx0.91174\ldots>0.9` for `\mathcal C_{\mathrm{lo}}`), so this
proves `\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})` on the entirety of
both boundary curves within `\mathcal D`.

**Method (rigorous, not a numeric sample).** For each curve, split the
range into (I) a sub-range bounded away from `\pi/3` (`[\cdot,\pi/3-0.05]`)
and (II) the sliver `[\pi/3-0.05,\pi/3)` approaching the corner.

- On (I): partition into `N` (3000 for `\mathcal C_{\mathrm{hi}}`, 1500 for
  `\mathcal C_{\mathrm{lo}}`) sub-intervals; on each, evaluate
  `\mathrm{Tgt}$ restricted to the curve using `mpmath`'s directed-rounding
  interval arithmetic (`mp.iv`, `dps=30`), which propagates a provable
  two-sided enclosure through every `+,-,\times,\div,\sin,\cos` in the raw
  (unsimplified) symbolic expression. Every sub-interval's enclosure has
  lower bound `\ge` the corner value's certified interval upper bound —
  `0` failures in both curves.
- On (II): the same interval method applied to the **derivative** of the
  curve-restricted `\mathrm{Tgt}` (obtained by direct, unsimplified
  `sympy.diff`) certifies the derivative is strictly negative throughout
  (`0` failures, `N=4000$ for `\mathcal C_{\mathrm{hi}}`, `1500` for
  `\mathcal C_{\mathrm{lo}}`). Since the function is `C^1` and its
  derivative is certified `<0` on the whole closed sub-range, the Mean
  Value Theorem gives strict monotone decrease, and continuity of
  `\mathrm{Tgt}` at the corner (all constituent closed forms are smooth
  there since `\sin(A+B)=\sin(2\pi/3)\ne0`) gives
  `\mathrm{Tgt}\to\mathrm{Tgt}(\pi/3,\pi/3)` as the parameter `\to\pi/3^-`,
  hence `\mathrm{Tgt}>\mathrm{Tgt}(\pi/3,\pi/3)` strictly throughout (II).

Combining (I) and (II) proves the stated inequality on the whole range for
each curve.

**Reusability.** This is a fully certified (interval-arithmetic branch-
covering, not sampling) proof of the entire boundary-curve content of the
outline's "global minimality of the corner" target. Combined with a proof
that `\mathrm{Tgt}` has no interior point of `\mathcal D` where its value
is `<\mathrm{Tgt}(\pi/3,\pi/3)` (still open — see the approach file's Open
gap 5), this would complete the global-minimality claim, hence the whole
problem via this route.

**Explicit caveat (not proved by this lemma).** This lemma says nothing
about the interior of `\mathcal D`, nor about the small residual
neighbourhood of the corner itself where a separate 2-D interval sweep
(same round, same approach file) could not resolve the inequality to
arbitrary precision (an unavoidable feature of interval methods near a
point of equality) — that residual gap is explicitly NOT closed by this
lemma or by the round-15 file as a whole.
