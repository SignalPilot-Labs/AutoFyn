# Lemma: `n4≥0` is equivalent to a plain-polynomial condition `n4sq≥0` (no algebraic extension)

**Source.** Proved in
`approaches/coordinate-bash-resultant-boundary-pointwise-sos.md`, round 15,
"Theorem 4" (extracted here into a standalone certified lemma file, since
the approach file itself only recorded it in a "Promotable lemmas"
section).

**Setup.** `u:=\tan(A/6)` (as in Theorem 1 of the approach file),
`w:=\sqrt{1+u^2}>0`, and `n_4(u,w,\cos B):=w^3\cos B-u(3-u^2)` (as in
Theorem 2, certified `lemmas/angle-b-le-c-weierstrass-encoding.md`).
Case (b)'s domain requires `A\in(0,\pi/2]` and `\angle B\le\angle C`.

**Statement.** Define the plain polynomial (no `w`, no algebraic
extension)
$$
n4sq(u,\cos B):=(1+u^2)^3\cos^2B-u^2(3-u^2)^2\ \in\ \mathbb Q[u,\cos B].
$$
Then, on Case (b)'s domain,
$$
n_4(u,w,\cos B)\ \ge\ 0\ \iff\ n4sq(u,\cos B)\ \ge\ 0.
$$

**Proof.**

*(i) `\cos B>0` on Case (b)'s domain.* Since `\angle B\le\angle C$ and
`A+B+C=\pi` with `A>0`, `B+C<\pi`. If `B\ge\pi/2` then, since `B\le C`,
also `C\ge B\ge\pi/2`, giving `B+C\ge\pi`, a contradiction. Hence `B<\pi/2`,
and since `B>0` (genuine triangle angle), `\cos B>0`.

*(ii) `u(3-u^2)>0` on Case (b)'s domain.* `A\in(0,\pi/2]` gives
`A/6\in(0,\pi/12]`, so `u=\tan(A/6)\in(0,\tan(\pi/12)]=(0,2-\sqrt3]` (using
`\tan` strictly increasing on `[0,\pi/2)`, and the standard value
`\tan(\pi/12)=2-\sqrt3`). In particular `u>0`, and since `2-\sqrt3<\sqrt3`,
`u^2<3`, so `3-u^2>0`. Hence `u(3-u^2)>0`.

*(iii) Squaring is lossless.* By (i), `w^3\cos B\ge0` (as `w>0`); by (ii),
`u(3-u^2)>0`. So `n_4\ge0` compares two nonnegative reals `X:=w^3\cos B`
and `Y:=u(3-u^2)`. For `X,Y\ge0`, `X\ge Y\iff X^2\ge Y^2`: the forward
direction is monotonicity of `t\mapsto t^2` on `[0,\infty)`; conversely,
`X^2\ge Y^2\iff(X-Y)(X+Y)\ge0`, and since `X+Y\ge0` with `X+Y=0` only when
`X=Y=0` (a case where `X\ge Y` trivially holds), `X^2\ge Y^2\Rightarrow
X\ge Y` whenever `X,Y\ge0`. Hence
$$
n_4\ge0\iff w^3\cos B\ge u(3-u^2)\iff(w^3\cos B)^2\ge(u(3-u^2))^2
\iff w^6\cos^2B-u^2(3-u^2)^2\ge0.
$$
Since `w^2=1+u^2` by definition, `w^6=(w^2)^3=(1+u^2)^3`, so the final
condition is exactly `n4sq(u,\cos B)\ge0`. `\blacksquare`

**Independent verification (proof-reviewer, round 15).** Own fresh `sympy`
session: computed `(w^3\cos B)^2-(u(3-u^2))^2`, substituted `w^2\to1+u^2`
(eliminating `w` entirely — confirmed no residual `w`-dependence), and
compared against `n4sq`: symbolic residual is identically `0`. Confirmed
`\tan(\pi/12)=2-\sqrt3` exactly via `sympy` (`sp.tan(sp.pi/12)` simplifies
to `2-\sqrt3`, difference is `0`). Both elementary sign facts (i), (ii) are
correct, standard triangle-angle / tangent-monotonicity arguments. No gaps
found; the proof is case-free and fully rigorous.

**Scope / caveat.** This lemma only establishes the pointwise equivalence
`n_4\ge0\iff n4sq\ge0` — it does NOT itself establish `n_4\ge0` (or
`n4sq\ge0`) on Case (b)'s domain; that remains open (see the approach
file's central gap, `\mathrm{Num}\ge0`).

**Reusability.** Removes the need for the algebraic extension
`w=\sqrt{1+u^2}` from any future Positivstellensatz search on Case (b)'s
domain: the domain is now fully polynomially encoded in the plain ring
`\mathbb Q(\sqrt3)[u,\cos B,\sin B]` via three generators `n_1>0` (degree
10), `n_2>0` (degree 6), `n4sq\ge0` (degree 6), plus the interval bound
`u\in(0,2-\sqrt3)` — a genuine simplification over the prior 4-generator
extended-ring ansatz.
