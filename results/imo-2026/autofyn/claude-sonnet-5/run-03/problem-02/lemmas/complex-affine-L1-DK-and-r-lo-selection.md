## Lemma (L1, D_K as Re/Im of one complex-affine function; the L1<0-selected
root of G2a is always the smaller root, unconditionally)

With `d(\beta)=(-\cos\beta,\sin\beta)` (direction of ray `BK`, as a complex
number `d=-\cos\beta+i\sin\beta`) and `v(s_2):=L(s_2)-B` (complex-affine in
the real parameter `s_2`, `L(s_2)=C+s_2R(\beta)(A-C)`), define
`L_1(s_2):=\mathrm{cross}(d,v(s_2))`, `D_K(s_2):=\mathrm{dot}(d,v(s_2))`
(the already-certified numerators of
`lemmas/cross-product-sign-selection-G2a.md` and
`lemmas/g2b-true-supplementary-parity.md` respectively). Then:

**(a)** `\bar d\cdot v(s_2) = D_K(s_2) + i\,L_1(s_2)` identically (exact
equality, not merely proportionality).

**(b)** The `s_2`-coefficient (slope) of `L_1` is
`Q(u)=(1+u^2)^2\cdot AC\sin(2\beta+\angle A)` (`u=\tan(\beta/2)`,
`b=AC\cos\angle A,\ cc=AC\sin\angle A`), and `\sin(2\beta+\angle A)>0`
unconditionally throughout the valid range `0<\beta<\min(\angle B,\angle C)`
(since `2\beta<\angle B+\angle C`, so `0<2\beta+\angle A<\pi`). Hence `L_1`
is strictly increasing in `s_2`.

**(c)** Consequently, combined with the already-certified fact
`L_1(r_1)L_1(r_2)<0` (`G_{2a}`'s two roots straddle `L_1`'s unique zero,
`lemmas/cross-product-sign-selection-G2a.md`), the `L_1<0`-selected root of
`G_{2a}` is **always** the algebraically smaller root,
`r_{\mathrm{lo}}:=\min(r_1,r_2)` — unconditionally, with no case split on
`\mathrm{sign}(Y)` or any other quantity.

## Proof
(a) Writing `d,v` as complex numbers, `\bar d v = (d_x-id_y)(v_x+iv_y) =
(d_xv_x+d_yv_y) + i(d_xv_y-d_yv_x) = \mathrm{dot}(d,v)+i\,\mathrm{cross}(d,v)
= D_K(s_2)+i L_1(s_2)`, a direct algebraic identity of complex-number
multiplication (no geometric content beyond `\mathrm{Re}(\bar dv)=
\mathrm{dot}(d,v)`, `\mathrm{Im}(\bar dv)=\mathrm{cross}(d,v)`, standard).

(b) `v(s_2)=v_0+s_2v_1` with `v_1=R(\beta)(A-C)` (`s_2`-independent), so
`\bar dv(s_2)=\bar dv_0+s_2\bar dv_1` is complex-affine, giving slope
`\bar dv_1` for both `D_K$ (real part) and `L_1` (imaginary part). Direct
symbolic computation (own vector definitions, Weierstrass substitution)
gives the trig closed form `Q(u)/(1+u^2)^2=b\sin2\beta+cc\cos2\beta`, which
equals `AC\sin(2\beta+\angle A)` since `b=AC\cos\angle A, cc=AC\sin\angle A`
and `\sin(2\beta+\angle A)=\sin2\beta\cos\angle A+\cos2\beta\sin\angle A`.
Positivity of `\sin(2\beta+\angle A)`: since `\beta<\min(\angle B,\angle C)
\le(\angle B+\angle C)/2`, `2\beta<\angle B+\angle C`, so
`2\beta+\angle A<\angle A+\angle B+\angle C=\pi`; trivially
`2\beta+\angle A>\angle A>0`. So `2\beta+\angle A\in(0,\pi)`, where sine is
positive.

(c) A strictly increasing continuous function with a unique zero `z_1` is
negative below `z_1` and positive above it. `L_1(r_1)L_1(r_2)<0` means `z_1`
lies strictly between `r_1,r_2`; since `L_1` is increasing,
`L_1(r_{\mathrm{lo}})<L_1(r_{\mathrm{hi}})`, and the only sign assignment
consistent with the product being negative and this ordering is
`L_1(r_{\mathrm{lo}})<0<L_1(r_{\mathrm{hi}})`. Hence the `L_1<0` root is
`r_{\mathrm{lo}}`. `\blacksquare`

## Independent verification
Independently re-derived by the proof-reviewer (round 8), in a fresh
`sympy` session, directly from the raw vector definitions (`A=(0,0)`,
`B=(a,0)`, `C=(b,cc)`, `d(\beta)`, `L(s_2)=C+s_2R(\beta)(A-C)`, `v=L-B`),
NOT copying any polynomial from the approach file: computed
`\mathrm{cross}(d,v)` and `\mathrm{dot}(d,v)` directly, confirmed their
`s_2`-slopes equal `b\sin2\beta+cc\cos2\beta` and `b\cos2\beta-cc\sin2\beta`
respectively (both exact, `sympy` residual `0`), and confirmed both trig
identifications `AC\sin(2\beta+\angle A)` and `AC\cos(2\beta+\angle A)`
algebraically (`b=AC\cos A`, `cc=AC\sin A` substitution, residual `0`). The
monotone/straddle argument in (c) is elementary real analysis, checked by
hand — no gap. No error found in (a)-(c).

## What this does NOT prove
This does not resolve the still-open "same-root correlation"
`W(r_{\mathrm{lo}})>0` (whether the `L_1<0`-selected root also satisfies
the true/supplementary "matched-sign" test `W=D_KD_N>0`) — it only converts
that question from an abstract same-root correlation into the concrete
single-point evaluation question "is `W(r_{\mathrm{lo}})>0`?", still open.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md`
(round 8).

## Status
Certified.
