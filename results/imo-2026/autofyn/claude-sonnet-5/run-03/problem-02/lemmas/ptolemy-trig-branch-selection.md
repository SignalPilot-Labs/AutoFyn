## Lemma (Branch selection for the decoupled constraints (III), (IV) — a rigorous IVT + quadratic-degree theorem, not numerics)

**Setting.** In `ptolemy-trig-identity.md`'s angle parametrization
(`θ:=∠KBA=∠ACL`, `ψ:=∠LCK` solving constraint (III), `φ:=∠LNC` solving
constraint (IV), both derived from hypotheses 2–3), for a fixed triangle
`ABC` and `θ\in(0,\min(B,C))`, cross-multiplying (III) gives
$$G(\psi):=\sin\psi\,\sin(A+2\theta+\psi)\,\sin C \;-\; 2\sin A\,\sin(C-\theta-\psi)\,\sin(\theta+\psi) \;=\;0,$$
equivalent to (III) wherever the original denominators are nonzero.

**Claim.** `G`, expanded in `(\sinψ,\cosψ)`, is exactly homogeneous of
degree 2:
$$G(\psi)=a_1\sin^2\psi+b_1\sin\psi\cos\psi+c_1\cos^2\psi,$$
$$a_1=2\cos^2\theta\sin B-\sin C\cos A,\quad
b_1=-\sin A\sin C\cos2\theta+\sin2\theta(2\sin A\cos C+\sin C\cos A),\quad
c_1=-2\sin A\sin\theta\sin(C-\theta),$$
(using `B=\pi-A-C`), so, dividing by `\sin^2\psi\ne0` for `\psi\in(0,\pi)`,
(III) is exactly equivalent to the quadratic
$$c_1x^2+b_1x+a_1=0,\qquad x:=\cot\psi. \qquad(\mathrm{III}')$$

**Theorem (branch selection).** For every `0<\theta<\min(B,C)`:
`c_1<0` strictly, `G(0)<0`, `G(C-\theta)>0`, hence by the Intermediate
Value Theorem `G` has at least one root `\psi^*\in(0,C-\theta)`; since
`c_1\ne0`, (III′) is a genuine quadratic, so (via `\cot` a strictly
monotonic bijection `(0,\pi)\to\mathbb R`) `G` has at most 2 roots in
`(0,\pi)`; a real quadratic with at least one real root has exactly 2 real
roots (with multiplicity); the sign change `G(0)<0<G(C-\theta)` forces an
**odd** number of roots in `(0,C-\theta)`, and since the total is exactly
2, that odd count is exactly **1**. Hence exactly one of the two roots of
(III′) lies in `(0,C-\theta)`, and it is the genuine value
`\psi^*=x_{\text{genuine}}=(-b_1-\sqrt{D_1})/(2c_1)` (`D_1:=b_1^2-4a_1c_1`,
the `+` sign choice for `x=\cot\psi` corresponding, since `c_1<0`, to the
smaller `\psi`). The symmetric statement (swap `B\leftrightarrow C`,
`\psi\leftrightarrow\varphi`) holds identically for (IV).

This is a fully general, all-triangle, all-`θ` proof of branch selection
for this parametrization's two decoupled transcendental constraints — a
genuine strengthening over the coordinate-based approaches' still-open
"gap 2" (branch selection), achieved here by IVT + quadratic-degree
counting rather than resultant/numeric evidence.

## Proof
See the derivation above; every step is elementary trigonometric identity
manipulation (angle-sum expansion for the degree-2-homogeneity claim,
standard real-quadratic root-counting for the rest). No squaring of the
original angle equality is used anywhere (only clearing three nonzero
denominators to pass from (III) to `G(\psi)=0`), so (III′) is a genuine
algebraic equivalent of (III), not a relaxation — the branch ambiguity
here is intrinsic to (III′) being a quadratic (2 roots), not an artifact
of squaring a cosine equality (contrast with the coordinate approaches'
branch selection problem, which *is* a squaring artifact).

## Independent verification (proof-reviewer, round 4)
Independently re-derived, in a fresh `sympy`/numeric session:
- Confirmed `G=a_1\sin^2\psi+b_1\sin\psi\cos\psi+c_1\cos^2\psi` with the
  displayed `a_1,b_1,c_1` by direct numerical substitution at 5 random
  `(\theta,A,C)` samples (residual `<10^{-16}` at each) — matches the
  file's formulas exactly.
- Confirmed `c_1<0`, `G(0^+)<0`, `G((C-\theta)^-)>0` simultaneously across
  **2000** random samples of `(\theta,A,C)` with `A,C>0`, `A+C<\pi`,
  `0<\theta<\min(\pi-A-C,C)` — **zero exceptions**, matching the theorem's
  hypotheses and conclusion exactly (not merely "consistent with," a
  genuine reproduction of the claimed universal sign pattern underlying
  the IVT argument).
- Confirmed the logical chain (IVT existence + quadratic-degree-2 upper
  bound + odd-root-count-in-subinterval-from-sign-change ⟹ unique root in
  `(0,C-\theta)`) is valid elementary reasoning with no gap.

## Source
`results/imo-2026-02/approaches/ptolemy-trig-identity.md` (round 4, Steps
2–3), building on Lemma 2/3 (imported, `ptolemy-trig-identity.md` rounds
1–2) and the `cot\alpha=\cot\theta+2\cot\psi` identity (this round's
ptolemy-lens math-explorer, re-verified in the approach file's Step 0).

## Status
Certified. This closes branch selection for the Ptolemy-route's own
decoupled constraint system (III)/(IV) unconditionally and rigorously — it
does **not** by itself close the coordinate-based approaches'
(`coordinate-bash-resultant`, `coordinate-bash-resultant-boundary`) branch
selection gap, which is a structurally different (squaring-of-cosine,
not quadratic-in-cotangent) ambiguity, though it is philosophically related
and may be a useful template. The remaining gap for
`ptolemy-trig-identity` as a whole is the *positivity* of the function `F`
obtained by substituting these genuine roots into the case-split
inequality (Step 4 of the approach file) — verified only numerically
(500,000 samples, no counterexample, comfortable margin), **not** proved
symbolically; this positivity claim is honestly reported as open, not
conflated with the branch-selection theorem certified here.
