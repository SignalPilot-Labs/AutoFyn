# Round 16 report — approach `coordinate-bash-resultant-boundary-pointwise-tangent`

## Task
Close the near-corner interior gluing gap left open by round 15 (the
`\lesssim5\times10^{-8}`-radius residual near `(\pi/3,\pi/3)` where the
2-D adaptive interval sweep couldn't resolve `Tgt\ge Tgt(\text{corner})`),
via the outlined "quotient sweep" technique, and check whether closing it
completes the whole approach.

## Result: gap closed, with a more robust method than outlined

Implemented the quotient sweep as an **exact Taylor identity with a
certified Lagrange-remainder bound**, which turns out to be strictly more
robust than a raw interval sweep of `q(\varepsilon,t):=(\mathrm{Tgt}(\pi/3
-\varepsilon,\pi/3+t\varepsilon)-\mathrm{Tgt}(\text{corner}))/\varepsilon`
itself (that raw form divides two intervals that both shrink to `0` as
`\varepsilon\to0`, the exact degeneracy round 15 hit).

Key identity: `\mathrm{Tgt}(\pi/3-\varepsilon,\pi/3+t\varepsilon)-
\mathrm{Tgt}(\pi/3,\pi/3)=\varepsilon F_t'(0)+\tfrac{\varepsilon^2}2F_t''
(\xi)` for some `\xi\in(0,\varepsilon)` (Taylor's theorem, Lagrange form;
`F_t(0)=\mathrm{Tgt}(\text{corner})` trivially for all `t`, so no
continuity argument is even needed for the `\varepsilon=0` endpoint — the
identity is exact for `\varepsilon>0`). Two certified pieces (own fresh
`sympy` + `mpmath.iv`, `dps=40`):

- `F_t'(0)=-g_A+t\,g_B`, `g_A\in[-4.28096012358944778,-4.28096012358944777]`,
  `g_B\in[-1.55725707997121229,-1.55725707997121228]` — independently
  re-derived and re-certified, matching the file's round-14 New result 9
  to all displayed digits. Minimum over the (generous) box
  `t\in[-0.3,0.5]` is `\delta_{\min}=-g_A+\tfrac12g_B\in
  [3.50233158360384163,3.50233158360384164]`.
- `F_t''(\xi)\in[-6.64158630888731,6.12971692053590]` certified via a
  `40\times40`-sub-box `mpmath.iv` sweep of the exact symbolic second
  `\varepsilon`-derivative over `\varepsilon\in[0,0.01],t\in[-0.3,0.5]`.

Combining: `q(\varepsilon,t)\ge3.469>0` for `\varepsilon\in(0,0.01]`,
`t\in[-0.3,0.5]`. A separate MVT argument (certifying `A'(B)\ge
3.99994544\ldots>10/3` on `B\in[\pi/3-0.003,\pi/3]` via `mpmath.iv`)
proves `[-0.3,0.5]` is a genuine safe superset of the true admissible
`t`-range for every `\varepsilon\in(0,0.01]` (the `t_{\mathrm{hi}}=1/2`
edge is exact; the `t_{\mathrm{lo}}` edge, from Theorem A's closed-form
`\mathcal C_{\mathrm{lo}}` parametrization, is shown `>-0.3` throughout).

Since `0.01\gg5\times10^{-8}` (round 15's residual radius) and round 15's
sweep box is a proved superset of `\bar{\mathcal D}`, the two results'
domains overlap and union to give:
$$\mathrm{Tgt}(A,B)\ge\mathrm{Tgt}(\pi/3,\pi/3)\quad\text{for every
}(A,B)\in\bar{\mathcal D},\text{ equality only at the corner.}$$
**Open gap 5 is now fully closed.** New certified lemma:
`results/imo-2026-02/lemmas/tgt-strictly-positive-throughout-D-full.md`.

## Does this complete the whole approach? No — checked and ruled out

The round-13 Reduction Lemma (New result 1) needs **two** hypotheses to
conclude `f\ge g` throughout `\mathcal D` (hence the whole problem via
this route): (A) `\partial(f-g)/\partial B>0` on `\mathcal D` — this is
exactly what gap 5's closure gives (via New result 5's "`Tgt>0` implies
constant sign" + the already-on-file single-point sign check) — and (B)
`D_1(A)\ge0` on the boundary curve `\mathcal C` (Open gap 6), a wholly
separate fact inherited unproved from the `-twopoint` sibling
(`lemmas/star-factorization-on-boundary-curve.md`). **Gap 6 is untouched
by this round's work and remains fully open.** So the approach is *not*
complete; Status stays `partial`. The single remaining obstruction to
this whole route is now precisely gap 6 alone (gaps 1-5 are all closed or
subsumed per the round-13 Reduction Lemma's own accounting).

## Files changed
- `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
  — added "Round 16" section, updated Open gaps (5 closed, 6 now flagged
  as the sole remaining obstruction), updated Approaches-tried summary
  and Promotable-lemmas list.
- `results/imo-2026-02/lemmas/tgt-strictly-positive-throughout-D-full.md`
  (new) — full statement, certified numbers, and honest scope caveat.

## Recommendation for next round
Attack Open gap 6 directly (`D_1(A)\ge0` on `\mathcal C`, i.e. on the
`-twopoint` sibling's boundary curve) — this is now the *only* thing
standing between this whole `f-g`/`Tgt` route and a complete proof of the
problem.
