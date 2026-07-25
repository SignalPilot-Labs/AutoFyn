# Build report — orbit-telescoping-aimo0710 (imo-2026-05), round 1

## Outcome: SOLVED (Status: solved)

The non-diagonal adaptation the outline called for **worked**, closing the gap fully. Wrote the
complete proof to `results/imo-2026-05/approaches/orbit-telescoping-aimo0710.md`.

## What was proven

- Re-derived the shared base layer from scratch (functional equation `f(f(y))=2f(y)-y`,
  injectivity, `g:=f-id ≥ 0`, `g(f(y))=g(y)`, orbit `f^n(y)=y+n·g(y)`, sufficiency of `f(x)=x+c`
  via the `(x-y-c)^2≥0` SOS identity for both original inequalities).
- Derived two algebraic tools by substitution into the two halves of the hypothesis:
  - **Lemma S** (from the GM/right inequality, `x=f(a),y=b`): `(a-b)^2 ≥ 4f(a)(g(b)-g(a))` for
    all `a,b>0`. Matches "tool (A)" already independently found by sibling approaches
    `extremal-sup-inf.md` / `cross-substitution-fixed-point.md`.
  - **Lemma T** (from the QM/left inequality, `x=b,y=a`, valid when `a` is a fixed point of `f`):
    `(a-b)^2 ≥ g(b)^2+2g(b)(a+b)`. This one is new to the record and turned out to be the key
    extra tool.
- **Lemma A** (both-positive case): if `g(x0)>0` and `g(y0)>0` then `g(x0)=g(y0)`. Proved by the
  fix to the diagonal dead end: instead of matching orbit indices `n=m`, pair `Y_m` with a
  MISMATCHED index `n(m) = round((Y_m-x0)/p)` (nearest integer). This keeps `|X_{n(m)}-Y_m|
  ≤ p/2` bounded forever while the RHS of Lemma S at that pairing (`4(Y_m+q)(p-q)`) grows
  linearly and unboundedly in `m` — contradiction. This is the actual working adaptation of the
  `aimo-0710` telescoping idea (bounded quantity vs. unboundedly growing forced lower bound),
  realized via nearest-lattice-point pairing rather than a literal sum.
- **Lemma B** (fixed-point set is downward closed): if `x0` is a fixed point and `0<y0≤x0`, then
  `y0` is also a fixed point. Same nearest-lattice-point trick, using Lemma T this time (needed
  because Lemma S alone only gives one-directional, non-shrinking bounds when one side is stuck
  at a literal fixed point).
- **Global constancy of `g`** (Section 4): case split on whether the fixed-point set `F` is
  empty, unbounded, or has a finite supremum `X^*`. The finite-supremum sub-case is ruled out by
  a fresh argument: (a) a limiting argument shows `X^*` itself must be a fixed point (using
  Lemma S's special form at nearby fixed points `x_ε→X^*`), so `F=(0,X^*]` exactly; (b) Lemma A
  then forces `g` to be a single constant `c>0` on all of `(X^*,\infty)`; (c) plugging a point
  `y_0=X^*+\sqrt{X^*c}` into Lemma S at the fixed point `X^*` gives `0 ≥ 3X^*c`, contradicting
  `X^*,c>0`. Hence the finite-supremum case is impossible, so either `F=∅` (giving `g≡c>0`
  globally by Lemma A) or `F=(0,\infty)` (giving `g≡0`).
- Concluded `f(x)=x+c` for a single global constant `c≥0`, matching the round-1 explorer
  consensus, with sufficiency already verified in Step 0.4.

All algebraic identities (Lemma S, Lemma T, and the sufficiency SOS identities) were derived by
hand in the written proof and cross-checked with sympy for correctness; the closest-approach
contradiction computations in Lemma A and Lemma B were also numerically sanity-checked.

## Honesty note

I initially could NOT close the "fixed point `x0` with `y0>x0` having `g(y0)>0`" sub-case using
Lemma S/T applied directly at `(x0,y0)` — extensive substitution search (4-5 different
compositions of `f` into LEFT/RIGHT) showed this specific pointwise pairing genuinely has no
forced contradiction. The fix was structural, not more algebra: promote to the "downward-closed
zero-set + supremum" argument (Section 4), which sidesteps the bad ordering entirely by finding
a DIFFERENT, better-positioned fixed point (or proving the boundary point `X^*` itself must be
fixed) rather than trying to force the original arbitrary pair to work.

## Files touched

- `/home/agentuser/repo/results/imo-2026-05/approaches/orbit-telescoping-aimo0710.md` — full
  proof, Status: solved.
- `/tmp/memory/proof-builder.md` — appended one new rule about the nearest-lattice-point
  mismatched-pairing technique for orbit telescoping.
