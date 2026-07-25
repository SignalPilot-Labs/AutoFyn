# Lemma: Theorem 16.2 first branch — `Y(\gamma)\ge0 \Rightarrow G(\beta)>0` on `(0,\gamma)` (Case (c) closure)

**Status:** Certified (proof-reviewer, round 22).

**Source:** `approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
"Round 22" section (Facts 0,3,4,5 + Theorem), re-deriving and applying
`coordinate-bash-resultant-boundary.md` §16 Theorem 16.2 (round 9).

## Statement
Let `ABC` be a triangle with WLOG `\angle B\le\angle C`, so `\gamma:=\angle B\le\pi/2`
and `\cos B>0`. Set `X_0:=\sin B\cos A/(2\sin(A+B))`,
`Y(\beta):=2\cos^2\beta-2X_0`, `K:=2\sin A\sin(A+B)`,
`f(\beta):=2\sin(A+B)(\sin\beta+\sin A)-\sin B\sin(A+\beta)`, `G(\beta):=2K-f(\beta)`.
Assume the domain-nonempty premise `\beta_0(A):=(\pi-A)/3<\gamma` (equivalently
`A+3B>\pi`). If `Y(\gamma)\ge0`, then
$$G(\beta)>0\quad\text{for every }\beta\in(0,\gamma),$$
so the conditional `(II)` of `-boundary.md` §15 holds unconditionally on `(0,\gamma)`.
Equivalently, whenever the angle `\beta_1\in[0,\pi/2)` with `\cos^2\beta_1=X_0`
satisfies `\beta_1\ge\gamma` (or when `X_0<0`, making `Y(\gamma)>0`), `(II)` is closed.

## Proof (self-contained, all identities residual `0`)
- **Fact 0.** `Y(\beta)=2\cos^2\beta-m\cos A` with `m=\sin B/\sin(A+B)` equals
  `2\cos^2\beta-2X_0`. `Y'=-2\sin2\beta<0` on `(0,\gamma)`: `Y` strictly decreasing.
- Hence `Y(\gamma)\ge0 \Rightarrow Y(\beta)>Y(\gamma)\ge0` on `(0,\gamma)`, so the
  `Y(\beta)>0` conjunct never restricts.
- **Fact 3.** `G(\beta)=2K-f(\beta)` identically (elementary trig; sympy residual `0`).
- **f'.** `f'(\beta)=\sin(A+\beta)\cos B+\sin(A+B-\beta)>0` on `(0,\gamma)`, so
  `G'=-f'<0`: `G` strictly decreasing. Thus `G(\beta)>G(\gamma)` on `(0,\gamma)`.
- **Fact 4.** `2K-f(\gamma)=\sin(A+B)(2\sin A-\sin B)` (sympy residual `0`).
- **Fact 5.** `\cos B(2\sin A-\sin B)-\sin(A+B)Y(\gamma)=\sin B(\cos\delta-\cos B)`
  for `A=\pi-2B-\delta`, `\delta=C-B` (sympy residual `0`). With `0\le\delta<B<\pi/2`
  (`\delta\ge0\iff B\le C`; `\delta<B\iff A+3B>\pi`, the domain-nonempty premise —
  **not** the Case hypothesis, so non-circular), `\cos\delta>\cos B`, giving RHS `>0`.
  Then `\cos B(2\sin A-\sin B)=\sin(A+B)Y(\gamma)+\sin B(\cos\delta-\cos B)>0`
  (using `\sin(A+B)>0`, `Y(\gamma)\ge0`), and `\cos B>0`, so `2\sin A-\sin B>0`.
- Therefore `G(\gamma)=\sin(A+B)(2\sin A-\sin B)>0`, so `G(\beta)>G(\gamma)>0`
  for all `\beta\in(0,\gamma)`. `\blacksquare`

## Independent verification (round 22)
Facts 0/3/4/5 and `f'` all symbolic residual `0` (fresh sympy). Over 600,000 random
triangles: `(I)\wedge(II)` 0 violations; `\beta_1\ge\gamma\iff Y(\gamma)\ge0` 0
mismatches. Over all 25,903 domain-nonempty Case-(c) triangles: `2\sin A-\sin B>0`
and `G(\beta)>0` on `(\beta_0,\gamma)`, 0 violations. `X_0>1` never occurs (0/2M);
`X_0<0\Rightarrow Y(\gamma)\ge0` (0 danger cases).

## Scope
Closes Case (c) of the `\beta_1`-trichotomy (`Y(\gamma)\ge0`). Complement of the
round-21 Case (a) vacuity lemma and the round-20 Case (b) `T\ge0` lemma. Together the
three close `(II)` for every `\beta\in(0,\gamma)` and every triangle.
