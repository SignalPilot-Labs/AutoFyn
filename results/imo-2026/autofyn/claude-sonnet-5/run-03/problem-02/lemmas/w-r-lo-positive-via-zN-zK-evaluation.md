## Lemma (`W(r_lo) > 0` unconditionally, via evaluation at the sibling
zero, both `Y>0` and `Y<0` cases)

**Setup.** `A=(0,0)`, `B=(a,0)`, `C=(b,cc)` (`a,cc>0`), `N=C/2`,
`d(\beta)=(-\cos\beta,\sin\beta)`, `L(s_2)=C+s_2R(\beta)(A-C)`. Define
(already-certified, `lemmas/complex-affine-L1-DK-and-r-lo-selection.md` and
`lemmas/g2b-true-supplementary-parity.md`) `D_K(s_2):=\mathrm{dot}(d,L(s_2)-B)`
and `D_N(s_2):=\mathrm{dot}(L(s_2)-N,\,C-N)`. `G_{2a}(s_2)$ is the
already-certified degree-4-in-`u` factor of hypothesis 2's polynomial
(`u=\tan(\beta/2)`), with leading coefficient `A_2<0` (certified,
`lemmas/cross-product-sign-selection-G2a.md`) and two real roots
`r_{\mathrm{lo}}<r_{\mathrm{hi}}` (certified, same lemma, via the
`L_1`-straddle argument). `Y:=2a(u^2-1)^2-b(u^2+1)^2` (certified,
`lemmas/yb2z-trig-identification.md`, `\propto2a\cos^2\beta-b`). `F_2`,
`A_2` as certified in `lemmas/cross-product-sign-selection-G2a.md`
(`F_2<0`, `A_2<0` throughout the valid range).

**Claim.** `W(r_{\mathrm{lo}}):=D_K(r_{\mathrm{lo}})D_N(r_{\mathrm{lo}})>0`
for every triangle and every `\beta` in the valid range `(0,\min(\angle B,
\angle C))`, provided the genericity conditions `Y\ne0`, `Q_K\ne0`
(`Q_K$ as below) already implicit elsewhere in the population.

**Proof.**
Closed forms (exact, verified by direct symbolic computation from the raw
vector definitions):
$$D_K(s_2)(1+u^2)^2=P_K+s_2Q_K,\quad P_K=-(1+u^2)[(a-b)(u^2-1)-2cc\,u],
\quad Q_K=b(u^4-6u^2+1)+4cc\,u(u^2-1),$$
$$D_N(s_2)=\tfrac{b^2+cc^2}4(1-2s_2\cos\beta).$$
Let `z_N:=1/(2\cos\beta)` (`D_N`'s zero) and `z_K:=-P_K/Q_K` (`D_K`'s
zero). Direct symbolic evaluation gives the exact identities
$$G_{2a}(z_N)=\frac{u(u^2+1)}{(u^2-1)^2}\,Y,\qquad
G_{2a}(z_K)=\frac{(u^2+1)^3F_2}{Q_K^2}\,Y,$$
$$D_K(z_N)=\frac{2a\cos^2\beta-b}{2\cos\beta}=\frac{Y}{2\cos\beta\,(1+u^2)^2},
\qquad D_N(z_K)=\frac{(b^2+cc^2)}4\cdot\frac{Y}{Q_K}.$$
Since `u\in(0,1)` on the valid range (as `\beta<\pi/2`, so `u=\tan(\beta/2)
<1`) and `\cos\beta>0`: the prefactor of the first identity is `>0`, so
`\mathrm{sign}(G_{2a}(z_N))=\mathrm{sign}(Y)`; the prefactor of the second is
`\le0\cdot\mathrm{sign}(F_2)$, and since `F_2<0` (certified),
`\mathrm{sign}(G_{2a}(z_K))=-\mathrm{sign}(Y)`.

Using `G_{2a}(x)=A_2(x-r_1)(x-r_2)`, `A_2<0` (certified): `G_{2a}(x)>0`
for `x` strictly between the roots (interior) and `<0` outside (exterior).
Hence: `Y>0\Rightarrow z_N` interior, `z_K` exterior; `Y<0\Rightarrow z_K`
interior, `z_N` exterior.

*Case `Y>0`.* `D_N` has slope `-\tfrac{b^2+cc^2}2\cos\beta<0`
(`\cos\beta>0` always on the valid range), so `D_N` is strictly
decreasing; since `z_N` is interior, `r_{\mathrm{lo}}<z_N`, so
`D_N(r_{\mathrm{lo}})>D_N(z_N)=0`. `D_K` is affine with zero `z_K`
exterior to `[r_{\mathrm{lo}},r_{\mathrm{hi}}]`, so it has one constant
sign on this interval, equal to its value at any interior point, e.g.
`z_N`: `\mathrm{sign}(D_K(z_N))=\mathrm{sign}(Y)=+`. Hence
`D_K(r_{\mathrm{lo}})=D_K(z_N)>0`. So `W(r_{\mathrm{lo}})=(+)(+)>0`.

*Case `Y<0`.* `z_K` is interior, so (an affine function is negative below
its zero if increasing, positive if decreasing) `\mathrm{sign}
(D_K(r_{\mathrm{lo}}))=-\mathrm{sign}(Q_K)$ (`Q_K` is `D_K`'s slope up to
the positive factor `1/(1+u^2)^2`). `z_N` is exterior, so `D_N` has
constant sign on `[r_{\mathrm{lo}},r_{\mathrm{hi}}]` equal to its value at
the interior point `z_K`: `\mathrm{sign}(D_N(z_K))=\mathrm{sign}(Y)
\mathrm{sign}(Q_K)=-\mathrm{sign}(Q_K)$ (`Y<0`). So both factors equal
`-\mathrm{sign}(Q_K)`, and
$$W(r_{\mathrm{lo}})=\bigl(-\mathrm{sign}(Q_K)\bigr)^2>0,$$
regardless of the actual sign of `Q_K`. `\blacksquare`

**Scope — what this does and does not establish.** This fully proves that
`r_{\mathrm{lo}}`, the already-certified unique `L_1<0`-selected root of
`G_{2a}` (matching "K inside angle LBA"), also satisfies the "matched
sign"/true-equation test for hypothesis 2 (as opposed to the spurious
supplementary alternative). Combined with the already-certified
`L_1`-selection and Theorem 11.8, this shows `r_{\mathrm{lo}}` is the
**unique** root of `G_{2a}` satisfying Lemma P1's conditions (2)-(4). It
does **not** rule out a root of the extraneous branch `G_{2b}` also
satisfying those conditions — full branch selection additionally requires
`G_{2b}`-exclusion, which remains open (shared verbatim with
`coordinate-bash-resultant-boundary`'s `(Y,B_2,Z)` classification).

## Independent verification (proof-reviewer, round 9)
Rebuilt the entire chain from scratch in a fresh `sympy` session,
independent of the builder's code: re-derived `D_K,D_N` directly from the
raw vector definitions (exact match, zero residual, against `D_K(1+u^2)^2
=P_K+s_2Q_K` and `D_N=(b^2+cc^2)/4\cdot(1-2s_2\cos\beta)`); independently
re-derived `G_{2a}` itself from the raw `cross_eq` construction (not
copied from any file — confirmed, en route, that the `G_{2a}` polynomial
as literally displayed in `coordinate-bash-resultant.md` §2 is missing its
`cc`-dependent terms, a stale cosmetic transcription bug, while the
`A_2`,`F_2` formulas used throughout the certified lemma chain are
unaffected and correct); confirmed `G_{2a}(z_N)/Y=u(u^2+1)/(u^2-1)^2` and
`G_{2a}(z_K)/Y=(u^2+1)^3F_2/Q_K^2` exactly via `sympy.factor`, zero
residual in both; confirmed `D_K(z_N)` and `D_N(z_K)` closed forms exactly,
zero residual. The interior/exterior sign logic and the two-case straddle
argument were checked by hand — sound, no gap. No error found anywhere in
this chain.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise.md`
(round 9).

## Status
Certified.
