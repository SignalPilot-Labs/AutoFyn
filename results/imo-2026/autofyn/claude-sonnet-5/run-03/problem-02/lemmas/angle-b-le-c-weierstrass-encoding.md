## Theorem (polynomial encoding of `\angle B\le\angle C` in the
`u=\tan(A/6)` Weierstrass basis)

**Status.** Proposed by `coordinate-bash-resultant-boundary-pointwise-sos`,
round 13, for reviewer certification. **CERTIFIED** by the proof-reviewer,
round 13 (independently re-derived in full).

**Setup.** `u:=\tan(A/6)` as in the already-certified
`lemmas/star-weierstrass-denominators-positive.md` (Theorem 1). Define
`w:=\sqrt{1+u^2}>0` (subject only to the algebraic relation `w^2=1+u^2`)
and
$$n_4(u,w,\cos B):=w^3\cos B-u(3-u^2).$$

**Theorem.** For `A\in(0,\pi/2]` and `B\in(0,\pi)` (Case (b)'s domain),
with `C:=\pi-A-B`,
$$\angle B\le\angle C\ \iff\ n_4(u,w,\cos B)\ge0,$$
a genuine polynomial condition on the extended variable set
`(u,w,\cos B,\sin B)` subject to the single ideal relation `w^2=1+u^2`.

*Proof.* `\angle B\le\angle C\iff B\le C=\pi-A-B\iff B\le\tfrac{\pi-A}2=
\tfrac\pi2-\tfrac A2`. For `A\in(0,\pi/2]`, `\tfrac\pi2-\tfrac A2\in
[\tfrac\pi4,\tfrac\pi2)\subset(0,\pi)`, and `B\in(0,\pi)` by hypothesis, so
both angles being compared lie in `(0,\pi)`, on which `\cos` is strictly
decreasing (hence injective). Therefore
$$B\le\tfrac\pi2-\tfrac A2\iff\cos B\ge\cos\bigl(\tfrac\pi2-\tfrac A2\bigr)
=\sin\tfrac A2.$$
(No extra precondition such as `B<\pi/2` is needed: both compared angles
are directly shown to lie in the full injectivity interval `(0,\pi)`.)

Write `t:=A/6`, so `\cos t=1/w`, `\sin t=u/w` (valid since
`w=\sqrt{1+u^2}=\sec t>0` for `t\in(0,\pi/12]\subset(0,\pi/2)`, giving
`\cos t>0`, and `u=\tan t\ge0` giving `\sin t\ge0`). Since `A/2=3t`, the
triple-angle formula gives
$$\sin\tfrac A2=\sin3t=3\sin t-4\sin^3t=\frac{3u}w-\frac{4u^3}{w^3}
=\frac{3uw^2-4u^3}{w^3}.$$
Substituting `w^2=1+u^2`: `3uw^2-4u^3=3u(1+u^2)-4u^3=3u-u^3=u(3-u^2)`, so
$$\sin\tfrac A2=\frac{u(3-u^2)}{w^3}.$$
Since `w^3>0`,
$$\cos B\ge\sin\tfrac A2\iff w^3\cos B\ge u(3-u^2)\iff n_4:=w^3\cos B-
u(3-u^2)\ge0.$$
Chaining the two displayed equivalences proves the theorem. `\blacksquare`

**Independent verification (proof-reviewer, round 13, from scratch).**

1. The reduction `3uw^2-4u^3\equiv u(3-u^2)\pmod{w^2-(1+u^2)}` was
   re-derived symbolically (own `sympy` session): expanding
   `3*u*(1+u^2) - 4*u^3` gives `3u - u^3 = u(3-u^2)` exactly, residual `0`.
2. The underlying trig identity `\sin(3t)=u(3-u^2)/w^3` (with
   `u=\tan t,\ w=\sec t`) was independently checked to 30-digit precision
   (`mpmath`, `mp.dps=30`) at 4 fresh sample values of `t`, agreement
   `<10^{-30}` absolute error in every case.
3. The full equivalence `B\le C\iff n_4(u,w,\cos B)\ge0` was independently
   re-tested directly against the raw trig definitions (own Python/`numpy`
   script, not reusing the file's `u,w` construction beyond the stated
   formula), `A` uniform on `(0,\pi/2)`, `B` uniform on `(0,\pi-A)`,
   `375{,}037` valid fresh random samples: **zero mismatches**.

All independent checks confirm the theorem exactly as stated. This closes
the round-12-flagged prerequisite (a polynomial encoding of `\angle B\le
\angle C` in the `u`-basis) needed for any future Positivstellensatz
attempt on `\mathrm{Num}\ge0` (equivalently `(\star)`) that wishes to
include the `\angle B\le\angle C` domain condition as an explicit
generator. It does **not** by itself close `\mathrm{Num}\ge0`, which
remains open.

## Source
`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-
pointwise-sos.md` (round 13, "Theorem 2").
