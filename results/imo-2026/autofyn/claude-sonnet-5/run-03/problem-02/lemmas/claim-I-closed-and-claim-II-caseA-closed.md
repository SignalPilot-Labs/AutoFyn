## Theorem (claim (I): `f(\beta)>0` throughout the effective domain, fully
closed for every triangle; claim (II): `2K-f(\beta)>0` closed on the
sub-case `Y(\gamma)\ge0`)

**Setup.** WLOG `\angle B\le\angle C` (so `\gamma:=\min(\angle B,\angle C)
=\angle B`; the mirror case follows by the certified `\sigma`-symmetry,
`lemmas/sigma-symmetry.md`). Write
$$f(\beta):=K_c+P\sin\beta+Q\cos\beta,\quad P:=\tfrac12\sin(A-B)+\tfrac32
\sin(A+B),\quad Q:=-\sin A\sin B,\quad K_c:=2\sin A\sin(A+B),$$
the round-8 target (equivalent, via an independently-verified exact
identity, to the two-part reformulation (I),(II) with `f` matching (I)'s
target and `2K_c-f` matching (II)'s). `\beta_0:=(\pi-A)/3` is the unique
zero of `\sin(A+3\beta)` in the effective range, and `Y(\beta):=2\cos^2
\beta-m\cos A` (`m=\sin B/\sin(A+B)`).

**Theorem A (claim (I), unconditional).** `f(\beta)>0` for every `\beta\in
(\beta_0,\gamma)` (the domain where `\sin(A+3\beta)<0`), for every
triangle with `\beta_0<\gamma`.

*Proof.* `f'(\beta)=P\cos\beta-Q\sin\beta=\sin(A+\beta)\cos B+\sin(A+B-
\beta)$ (exact identity). For `\beta\in(0,\gamma)=(0,B)`: `2B\le B+C<\pi`
gives `B<\pi/2`, so `\cos B>0`; `A+\beta\in(0,A+B)\subset(0,\pi)` gives
`\sin(A+\beta)>0`; `A+B-\beta\in(A,A+B)\subset(0,\pi)` gives `\sin(A+B-
\beta)>0`. So `f'(\beta)>0` throughout `(0,\gamma)`, unconditionally — `f`
is strictly increasing on the whole domain. Combined with `f(\beta_0)>0`
(Theorem B below), strict monotonicity gives `f(\beta)>f(\beta_0)>0` for
`\beta\in(\beta_0,\gamma)`. `\blacksquare`

**Theorem B (`f(\beta_0)>0`, the endpoint lemma).** For every triangle
with `\beta_0<\gamma$ (`\beta_0=(\pi-A)/3`, `\gamma=B`), `f(\beta_0)>0`
strictly.

*Proof.* Substituting `A=\pi-3\beta_0`, `B=\beta_0+s` (`s\in(0,\beta_0/2]`,
`s>0$ since `\beta_0<\gamma=B`, `s\le\beta_0/2` since `B\le C\iff B\le
3\beta_0/2`): `f(\beta_0)=2\sin(\beta_0)G(\beta_0,s)`, `G:=C_1\cos s-C_2
\sin s`, `C_1=\tfrac32\sin(2\beta_0)+\sin(4\beta_0)`, `C_2=\tfrac32+
\tfrac52\cos(2\beta_0)+\cos(4\beta_0)` (all exact, verified identities).
`\sin\beta_0>0` (`\beta_0\in(0,\pi/3)`). Writing `x=\cos(2\beta_0)\in
(-\tfrac12,1)`: `C_1=\sin(2\beta_0)(\tfrac32+2x)>0` always (`\sin(2\beta_0)
>0`, `\tfrac32+2x>\tfrac12>0`); `C_2=2x^2+\tfrac52x+\tfrac12=2(x+1)
(x+\tfrac14)` (note: `2x^2+\tfrac52x+\tfrac12`, NOT `+\tfrac32` as
displayed in one place in the source file — a cosmetic transcription slip
that does not affect the correctly-used factored form `2(x+1)(x+1/4)`),
so `\mathrm{sign}(C_2)=\mathrm{sign}(x+\tfrac14)` (`x+1>\tfrac12>0`
always).

If `C_2\le0` (`\beta_0\ge\beta_0^*:=\tfrac12\arccos(-\tfrac14)`): `s\in(0,
\pi/6)` gives `\cos s,\sin s>0`, so `G=C_1\cos s+|C_2|\sin s>0`.

If `C_2>0` (`\beta_0<\beta_0^*`): `G'(s)=-C_1\sin s-C_2\cos s<0` on
`[0,\beta_0/2]` (`C_2\cos s>0` regardless of `\sin s`), so `G` is
decreasing, minimized at `s=\beta_0/2`. There, `G(\beta_0,\beta_0/2)=
\cos(\beta_0)\cdot\sin(3\beta_0/2)(4\cos\beta_0-1)` (exact, via sum-to-
product). `\cos\beta_0>0` (`\beta_0<\pi/3<\pi/2`); `\sin(3\beta_0/2)>0`
(`3\beta_0/2<3\beta_0^*/2\approx1.37<\pi`); `4\cos\beta_0-1>0`
(`\cos\beta_0>\cos\beta_0^*\approx0.61>\tfrac14`). So `G(\beta_0,\beta_0/2)
>0`, hence `G(\beta_0,s)>0` for all `s` in this case too.

Both cases give `G>0`, so `f(\beta_0)=2\sin\beta_0\,G>0`. `\blacksquare`

**Theorem C (claim (II), sub-case `Y(\gamma)\ge0`).** If `Y(\gamma)\ge0`
(equivalently `N:=\sin(A-B)+\tfrac12\sin(A+B)+\tfrac12\sin(A+3B)\ge0`,
since `N=\sin(A+B)Y(\gamma)` and `\sin(A+B)>0`), then `2K_c-f(\beta)>0`
for every `\beta\in(0,\gamma)`.

*Proof.* `(2K_c-f)'=-f'<0` (Theorem A), so `2K_c-f` is strictly decreasing
— suffices to bound at `\beta=\gamma`. `f(\gamma)=(2\sin A+\sin B)\sin
(A+B)` (exact), so `2K_c-f(\gamma)=\sin(A+B)(2\sin A-\sin B)`. Writing
`A=\pi-2B-\delta`, `\delta\ge0` (`B\le C`), the domain-nonempty condition
`\beta_0<\gamma` is exactly `\delta<B` (exact algebra: `A+3B>\pi\iff
\delta<B`), and the exact identity `\cos B(2\sin A-\sin B)-N=\sin B(\cos
\delta-\cos B)` holds. For `0\le\delta<B<\pi/2`, `\cos\delta>\cos B`
strictly (cosine decreasing on `[0,\pi/2)`), so `\cos B(2\sin A-\sin B)-N
>0`. In this sub-case `N\ge0`, so `\cos B(2\sin A-\sin B)>0`, and `\cos B
>0` gives `2\sin A-\sin B>0`. Hence `2K_c-f(\gamma)=\sin(A+B)(2\sin A-\sin
B)>0`, and by the decreasing-monotonicity, `2K_c-f(\beta)>2K_c-f(\gamma)>0`
for every `\beta\in(0,\gamma)`. `\blacksquare`

**What remains open.** The mirror sub-case `Y(\gamma)<0` (Case (b) of
(II)) is NOT covered by this lemma — there the true effective right
endpoint is an implicitly-defined `\beta_1<\gamma$ with no known closed
form, and this is the sole remaining open item of the whole
`coordinate-bash-resultant-boundary` approach (and, by the population's
proven structural-equivalence theorem, of the whole live branch-selection
gap).

## Independent verification (proof-reviewer, round 9)
Every displayed identity in Theorems A, B, C was independently re-derived
from scratch in a fresh `sympy` session (own definitions of `f,P,Q,K_c`,
own substitutions `A=\pi-3\beta_0,B=\beta_0+s` and `A=\pi-2B-\delta`), with
zero symbolic residual against the file's claims in every case, including:
`f'(\beta)` closed form; `f(\beta_0)=2\sin\beta_0G(\beta_0,s)`; the
`C_1,C_2` closed forms and their `x`-polynomial factorizations (one
cosmetic constant-term transcription slip found and corrected, `+\tfrac32`
should read `+\tfrac12`, matching the correctly-used factored form
`2(x+1)(x+1/4)` — does not affect the proof); `G(\beta_0,\beta_0/2)`'s
closed form and its sum-to-product collapse; `f(B)$ and `2K_c-f(B)$ closed
forms; the key identity `\cos B(2\sin A-\sin B)-N=\sin B(\cos\delta-\cos
B)`; and `N=\sin(A+B)Y(\gamma)`. All sign arguments (elementary interval
membership, monotonicity of `\cos,\sin` on stated sub-intervals) checked by
hand — sound, no gap, no case omitted within the stated scope. This is a
genuine, complete closure of claim (I) and of claim (II) restricted to
`Y(\gamma)\ge0`; the `Y(\gamma)<0` sub-case is correctly and honestly left
open by the source file, not overclaimed.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
(round 9, "New results 1-3").

## Status
Certified.
