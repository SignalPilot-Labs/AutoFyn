# Lemma: `Tgt(A,B) ≥ Tgt(π/3,π/3) > 0` throughout the full closure `D̄` — near-corner gap closed quantitatively

**Source.** `Tgt ≥ Tgt(corner)` on the boundary curves and away-from-corner
interior is `lemmas/tgt-ge-corner-on-both-boundary-curves.md` (Theorems
B, C) plus the round-15 2-D adaptive interval sweep, both in
`approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
("Round 15"). **This lemma supplies the missing piece**: an explicit,
quantitative radius `r₀ = 0.01` such that `Tgt ≥ Tgt(corner)` holds
throughout the near-corner neighbourhood `D̄ ∩ {A ≥ π/3 − 0.01}`, proved
in `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`,
**Round 16**. Combined, these give `Tgt ≥ Tgt(corner)` (hence `Tgt>0`,
since `Tgt(corner)≈1.574>0`, certified below) **everywhere on `D̄`**,
closing Open gap 5 of that file in full, and closing Target 1 of
`lemmas` "New result 5" net assessment (the file's round-13 `f-g`
reformulation's first of two remaining sub-targets).

**Setup (all notation exactly as in the approach file's "Setup (reused)"
paragraph).** `X₀(A,B):=\dfrac{\sin B\cos A}{2\sin(A+B)}`,
`β₀(A):=(π−A)/3`, `K_c=2\sin A\sin(A+B)`,
`P=\tfrac12\sin(A-B)+\tfrac32\sin(A+B)`, `Q=-\sin A\sin B`,
`G(β₀):=K_c-P\sinβ₀-Q\cosβ₀`, `\mathrm{RHS}:=(1+\cos B)\cosβ₀-\sinβ₀G(β₀)`,
`D_2:=\partial\mathrm{RHS}/\partial B`,
`T_1:=(1+\cos B)^2\partial_BX_0-2(1+\cos B)\sin B\,X_0`,
`\mathrm{Tgt}(A,B):=4(1+\cos B)^2X_0D_2^2-T_1^2`. Near `(π/3,π/3)`, `D`
is bounded by `𝒞_{\mathrm{hi}}:B=(π-A)/2` (exact) and `𝒞_{\mathrm{lo}}:
X_0=\cos^2B$, with the exact closed-form parametrization (Theorem A,
`lemmas/clo-closed-form-parametrization.md`) `A(B)=\arctan\bigl(-\sin B
\cos(2B)/(2\cos^3B)\bigr)`.

**Statement (Round 16 result).** Let `\varepsilon:=\pi/3-A\ge0`,
`t:=(B-\pi/3)/\varepsilon` for `\varepsilon>0`. For every
`(A,B)\in\bar D` with `0<\varepsilon\le r_0:=0.01`,
$$\mathrm{Tgt}(A,B)-\mathrm{Tgt}(\pi/3,\pi/3)=\varepsilon\cdot
q(\varepsilon,t),\qquad q(\varepsilon,t)\ \ge\ 3.46\ >0.$$
Hence `Tgt(A,B) > Tgt(π/3,π/3)` strictly for every such `(A,B)` (equality
only at the corner itself, `\varepsilon=0`).

**Method — exact Taylor identity with a certified Lagrange-remainder
bound (not a raw quotient-of-intervals sweep, which degenerates at the
equality point).** Fix `t\in[-0.3,0.5]` (this interval is a certified
*safe superset* of the true tangent-cone/curve range `[t_{\mathrm{lo}}
(\varepsilon),1/2]` for every `\varepsilon\in(0,0.01]$ — see "Domain
safety" below) and define `F_t(e):=\mathrm{Tgt}(\pi/3-e,\pi/3+te)`. Since
`\sin(A+B)$ is bounded away from `0` throughout the box `e\in[0,0.01],
t\in[-0.3,0.5]` (there `A+B=2\pi/3+e(t-1)\in[2\pi/3-0.013,2\pi/3-0.0005]`,
comfortably inside `(0,\pi)`, since `\sin(2\pi/3)=\sqrt3/2\ne0`),
`\mathrm{Tgt}` — and hence `F_t` — is `C^\infty` in `e` there. Taylor's
theorem with Lagrange remainder gives, for `e=\varepsilon>0`,
$$F_t(\varepsilon)=F_t(0)+\varepsilon F_t'(0)+\frac{\varepsilon^2}2F_t''(\xi)$$
for some `\xi\in(0,\varepsilon)`. Since `F_t(0)=\mathrm{Tgt}(\pi/3,\pi/3)`
for every `t` (setting `e=0` collapses `(A,B)` to the corner regardless of
`t`), this is exactly
$$q(\varepsilon,t):=\frac{F_t(\varepsilon)-\mathrm{Tgt}(\pi/3,\pi/3)}
\varepsilon=F_t'(0)+\frac\varepsilon2F_t''(\xi).$$

**Certified piece 1: `F_t'(0)=-g_A+t\,g_B`.** By the chain rule (as in New
result 9), independently re-certified here via `mpmath.iv` (60-digit
directed rounding, own fresh evaluation):
$$g_A\in[-4.28096012358944778,-4.28096012358944777],\quad
g_B\in[-1.55725707997121229,-1.55725707997121228]$$
(matching New result 9's values to all displayed digits). Since
`F_t'(0)=-g_A+t\,g_B` is affine and strictly decreasing in `t` (as
`g_B<0`), its minimum over `t\in[-0.3,0.5]` occurs at `t=1/2$ (the
extreme point, unaffected by extending the interval down to `-0.3`,
since decreasing functions attain their min at the *larger* endpoint):
$$\min_{t\in[-0.3,0.5]}F_t'(0)=-g_A+\tfrac12g_B\in
[3.50233158360384163,3.50233158360384164]=:\delta_{\min}.$$

**Certified piece 2: a bound on `F_t''`.** Computing `F_2:=\partial^2/
\partial e^2\bigl[\mathrm{Tgt}(\pi/3-e,\pi/3+te)\bigr]` symbolically
(direct `sympy.diff`, raw unsimplified expression) and sweeping it with
`mpmath.iv` (`dps=40`) over the box `e\in[0,0.01],\,t\in[-0.3,0.5]`,
subdivided into `40\times40=1600` sub-boxes (own script):
$$F_2(e,t)\in[-6.64158630888731416,\,6.12971692053590261]\quad\text{for
every }(e,t)\text{ in the box (certified enclosure of the union).}$$
In particular `|F_t''(\xi)|\le M:=6.6415863089` for every `\xi\in[0,0.01]`,
`t\in[-0.3,0.5]`.

**Combining.** For every `\varepsilon\in(0,0.01]`, `t\in[-0.3,0.5]`:
$$q(\varepsilon,t)\ \ge\ \delta_{\min}-\frac\varepsilon2M\ \ge\
3.50233158360384163-\frac{0.01}2\times6.6415863089=3.46912\ldots>0.$$

**Domain safety — `[-0.3,0.5]` really contains `[t_{\mathrm{lo}}
(\varepsilon),1/2]` for every `\varepsilon\in(0,0.01]`.** `t_{\mathrm{hi}}
(\varepsilon)=1/2` exactly for every `\varepsilon` (since `𝒞_{\mathrm{hi}}:
B=(\pi-A)/2` gives `B=\pi/3+\varepsilon/2` exactly). For the lower edge,
using Theorem A's `A(B)=\arctan(-\sin B\cos2B/(2\cos^3B))` (increasing in
`B` near `\pi/3`, `A'(\pi/3)=4` exactly, `sympy`-confirmed): define
`\varphi(\varepsilon):=(\pi/3-\varepsilon)-A(\pi/3-0.3\varepsilon)`.
`\varphi(0)=0`. Certified interval sweep (`mpmath.iv`, `2000`
sub-intervals) of `A'(B)` on `B\in[\pi/3-0.003,\pi/3]` (the range swept
by `\pi/3-0.3\varepsilon` as `\varepsilon` ranges over `[0,0.01]`) gives
`A'(B)\ge3.99994544\ldots>10/3` throughout (`0` bad sub-intervals), so
`\varphi'(\varepsilon)=-1+0.3\,A'(\pi/3-0.3\varepsilon)\ge
-1+0.3\times3.99994544=0.19998\ldots>0` throughout `[0,0.01]`. By the Mean
Value Theorem, `\varphi(\varepsilon)>\varphi(0)=0` for every
`\varepsilon\in(0,0.01]`, i.e. `A(\pi/3-0.3\varepsilon)<\pi/3-\varepsilon`.
Since `A(\cdot)` is increasing (its derivative is certified `>0` on this
range), this means the true curve point `B_{\mathrm{lo}}(\varepsilon)`
(defined by `A(B_{\mathrm{lo}}(\varepsilon))=\pi/3-\varepsilon`) satisfies
`B_{\mathrm{lo}}(\varepsilon)>\pi/3-0.3\varepsilon`, i.e.
`t_{\mathrm{lo}}(\varepsilon)>-0.3`. Since (round 13, "New result 5") the
admissible `B`-range at fixed `A` is exactly the single interval
`[B_{\mathrm{lo}}(A),B_{\mathrm{hi}}(A)]`, every `(A,B)\in\bar D` with
`\varepsilon\in(0,0.01]` has `t\in(t_{\mathrm{lo}}(\varepsilon),1/2]\subset
(-0.3,0.5]`, inside the swept box. `\blacksquare`

**Conclusion.** `\mathrm{Tgt}(A,B)-\mathrm{Tgt}(\pi/3,\pi/3)=
\varepsilon\,q(\varepsilon,t)\ge3.46\,\varepsilon>0` for every
`(A,B)\in\bar D` with `0<\varepsilon\le0.01`. Since `0.01\gg5\times10^{-8}`
(the radius of the residual region left unresolved by the round-15 2-D
adaptive interval sweep, which independently certifies
`\mathrm{Tgt}\ge\mathrm{Tgt}(\text{corner})$ throughout `\bar D` outside
that tiny residual ball, over the safe superset box `A\in[0.40,\pi/3],\,
B\in[0.90,1.33]\supseteq\bar D`), the two results' domains of validity
overlap and their union is all of `\bar D`. Hence:
$$\boxed{\mathrm{Tgt}(A,B)\ \ge\ \mathrm{Tgt}(\pi/3,\pi/3)\
\text{for every }(A,B)\in\bar D,\ \text{with equality only at the
corner.}}$$
Since `\mathrm{Tgt}(\pi/3,\pi/3)\approx1.574>0$ (certified, `New result
6/7`, and independently re-confirmed here via `mpmath.iv`:
`\mathrm{Tgt}(\pi/3,\pi/3)\in[1.574136224814062593,1.574136224814062593]`),
this gives `\mathrm{Tgt}(A,B)>0` for **every** `(A,B)\in\bar D` —
**Target 1 of the `f-g` reformulation's "Net assessment" (New result 5)
is fully closed.**

**Explicit caveat (honest scope).** This lemma closes Open gap 5 of the
approach file **in full**. It does **not** touch Open gap 6
(`D_1(A)\ge0` on the boundary curve `𝒞`, inherited from the `-twopoint`
sibling, `lemmas/star-factorization-on-boundary-curve.md`) — a wholly
separate hypothesis (B) of the Reduction Lemma (New result 1), needed
*in addition to* `Tgt>0` to conclude `f\ge g` throughout `D`. **The
approach is not complete**: gap 6 remains the sole open obstruction to
finishing this route.

**Reusability.** The Taylor-with-certified-Lagrange-remainder technique
used here (sweep the *second derivative* of the target quantity along
rays from the equality point, rather than the quantity's raw value or a
raw finite-difference quotient) is reusable for any other "prove `f\ge
f(\text{corner})` near a point of exact equality" target in this
population — it sidesteps the interval-degeneracy that defeats direct
value sweeps at equality points, without requiring an explicit closed
form for the curve inversion (only a one-sided MVT/derivative-sign
argument for the domain-safety half).
