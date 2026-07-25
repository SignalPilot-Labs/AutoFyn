# Proof review: imo-2026-05 (round 1)

Problem: determine all `f:\mathbb R_{>0}\to\mathbb R_{>0}` with
`sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(xf(y))` for all `x,y>0`.
Claimed answer (all four): `f(x)=x+c`, `c\ge0`.

## Method

I independently re-derived the shared base layer by hand and cross-checked all load-bearing
algebraic identities with `sympy` (not trusting the "verified by sympy" claims in the files
themselves), then scrutinized each approach's own closing argument line by line for hidden
continuity/monotonicity assumptions, circularity, and skipped cases. I also numerically
spot-checked the claimed answer family: `f(x)=x` and `f(x)=x+3` satisfy the inequality on
200,000 random `(x,y)` pairs in `[0.01,50]^2`; `f(x)=2x` and `f(x)=x+\sin x+2` both fail it
(consistent with the claimed characterization being exactly `f(x)=x+c`, `c\ge0`).

## Shared base layer (all four) — VERIFIED

- `x=f(y)` substitution: both sides of `(\star)` collapse to `f(y)` exactly, forcing
  `f(f(y))=2f(y)-y`. Correct in all four — verified by hand.
- Injectivity: immediate from the functional equation. Correct.
- `g(y):=f(y)-y`: `g(f(y))=g(y)` (orbit invariance) and `f^{(n)}(y)=y+n\,g(y)` (exact AP), proved
  by clean induction. `g\ge0` follows since the orbit must stay in `\mathbb R_{>0}` for all `n`
  (if `g(y)<0` the AP goes to `-\infty`). Correct in all four.
- "Tool A" (`(x-y)^2 \ge 4f(y)(g(x)-g(y))`, valid for **all** `x,y>0`, not just orbit pairs):
  derived by substituting `(u,v)=(f(y),x)` into the RIGHT/GM inequality and eliminating
  `f(f(y))` via the exact FE. I re-derived this expansion independently with sympy
  (`(x+y+2q)^2-4(y+q)(x+p) == (x-y)^2-4(p-q)(y+q)`, confirmed identically 0 as a polynomial
  identity) — matches all three files that state it (`extremal-sup-inf`,
  `cross-substitution-fixed-point`, and "Lemma S" in `orbit-telescoping-aimo0710`, and "Tool A"
  in `monotonicity-order`). Correct.
- "Tool C" (LEFT-inequality analogue, `(x-y)^2 \ge 2(q-p)(2x+p+q)`, used by
  `monotonicity-order`) and "Lemma T" (fixed-point specialization used by
  `orbit-telescoping-aimo0710`): both independently re-derived and symbolically confirmed
  correct (see below).
- Sufficiency of `f(x)=x+c`: both L and R reduce identically to `(x-y-c)^2\ge0` in all four
  files — verified by hand and by sympy. Correct.

All four files' base layer is correct and non-circular; none of them assumes what is to be
proven, and none appeals to an external "crux" citation as a proof step — the `aimo-0710`-flavored
orbit ideas in two of the four are fully re-derived from scratch here, only the *shape* of the
idea (telescoped bound forces vanishing) is borrowed, consistent with CLAUDE.md's "hint to adapt,
never a citation" rule.

## Per-approach closing-argument review

### `extremal-sup-inf.md` — APPROVE (Status: solved)

Closing route: derives **continuity of `g`** directly and unconditionally from Tool A/B applied
at `x=y+\varepsilon` for a genuine real perturbation `\varepsilon` (not an orbit point) — this is
legitimate since Tool A/B were established for *all* `x,y>0`, not merely orbit-related pairs.
Squeeze theorem gives `g(y+\varepsilon)\to g(y)`, so `g` (hence `f`) is continuous — with **no
prior assumption of continuity**, which would otherwise be circular; I checked this carefully and
it is not: the bound comes purely from the algebraic Tool A/B, evaluated at a free real
perturbation.

Then: continuous + injective on an interval `\Rightarrow` strictly monotonic (classical
IVT-based fact, correctly justified in-line). Ruling out "decreasing" uses `g\ge0` (`f(y)\ge y`)
against an unbounded increasing `y`, valid. `g` non-decreasing then follows from strict increase
of all iterates `f^n` plus the exact AP orbit structure (a clean, checked argument: if `g(a)>g(b)`
for `a<b`, then `a+np` eventually exceeds `b+nq`, contradicting `f^n(a)<f^n(b)`). The "Crossing
Lemma" (any `a<b` with both `g`-values positive have `g(a)=g(b)`) uses only the already-proven
monotonicity of `g` and the AP orbit — correct, checked in detail. Final case split on the zero
set `Z=\{g=0\}` (empty vs. nonempty, using downward-closedness + continuity at `\sup Z`) is
exhaustive and each branch is closed rigorously; I verified the "downward-closed + unbounded
`\Rightarrow` `Z=(0,\infty)`" claim and the boundary continuity argument by hand. No gaps found.
Sufficiency direction is a clean SOS computation, verified. **Status confirmed solved.**

### `cross-substitution-fixed-point.md` — APPROVE (Status: solved)

Closing route: the cleanest of the four. Combines Tool A and B pointwise into a **local
quadratic bound** `|g(x)-g(y)|\le(x-y)^2/(4\min(f(x),f(y)))` (algebra re-verified). Then, for
arbitrary `x\ne y`, partitions `[\min(x,y),\max(x,y)]` into `N` equal pieces, uses `f(t)\ge t`
to lower-bound the denominator by `a:=\min(x,y)`, and telescopes via the triangle inequality to
get `|g(x)-g(y)|\le(x-y)^2/(4aN)` for **every** positive integer `N`. Since the left side is a
fixed non-negative real independent of `N` and the right side `\to0`, `g(x)=g(y)` follows
directly. This is a genuinely finite, elementary argument (not smuggling in continuity) — I
checked the denominator bound direction and the triangle-inequality sum carefully; both correct.
This is strictly simpler than the other three closing arguments (no orbit-pairing, no
monotonicity, no case splits) and I selected it as the proof recorded in `current.md`.
Sufficiency direction verified independently, matches the SOS form. **Status confirmed solved.**

### `orbit-telescoping-aimo0710.md` — APPROVE (Status: solved)

Closing route: heavier machinery — a "nearest lattice point" orbit-pairing argument. Lemma A
(any two positive `g`-values coincide): for `p=g(x0)>q=g(y0)>0`, pairs orbit points
`X_n=x0+np`, `Y_m=y0+mq` via `n(m):=\mathrm{round}((Y_m-x0)/p)`, giving `|X_{n(m)}-Y_m|\le p/2`
(bounded) while Tool A/S forces `(X_{n(m)}-Y_m)^2\ge4(Y_m+q)(p-q)\to\infty` — a genuine
contradiction; I verified the nearest-integer bound and the unboundedness of the RHS by hand and
with the file's own numerical sanity check. Lemma B (fixed-point set `F` downward closed) uses
an analogous nearest-integer argument with "Lemma T" (re-derived and confirmed by sympy) and
correct algebra (`-3q^2/4\ge2qx_0` leading to a sign contradiction, checked). The final
sup/inf limiting argument (Section 4) to rule out the "mixed" case (some `t` with `g(t)=0`
coexisting with `g\equiv c>0` elsewhere) is done via genuine limits of two explicit converging
real-number sequences plugged into the already-established (pointwise) Lemma S₀ inequality — not
an appeal to continuity of `f` or `g` as functions, which the file explicitly (and correctly)
disclaims. I traced through both the `X^*` finite and `X^*=\infty` sub-cases and both boundary
directions (`S=Z_c\cap(x_0,\infty)` and its symmetric case below `x_0`); all exhaustive and each
closed correctly. More complex than necessary but no gap found. **Status confirmed solved.**

### `monotonicity-order.md` — APPROVE (Status: solved)

Closing route: same "escaping double orbit" mechanism as `orbit-telescoping-aimo0710`'s Lemma A
for showing any two positive `g`-values coincide (re-verified independently — algebra and orbit
argument correct). The mixed-case exclusion (Part 4) uses a LEFT-inequality-derived "Tool C"
(independently re-derived and symbolically confirmed: `(x-y)^2\ge2(q-p)(2x+p+q)`) plus an
infimum/supremum limiting argument on two explicit converging sequences (`w_k\to m`, `y_k\to m`)
plugged into the already-established Tool C — again a genuine real-sequence limit, not an
appeal to continuity of `f`. Both directions (`Z_c` above `x_0` and below `x_0`) are handled
symmetrically and exhaustively; I checked both the algebra of Tool C and the final
`\varepsilon`-`K` argument (spelled out explicitly in the file) and found no gap. **Status
confirmed solved.**

## Overclaim check

All four files' self-reported "Status: solved" is accurate; none of them overclaims. All four
correctly state and separately verify **both** necessity (every solution has the claimed form)
**and** sufficiency (every `f(x)=x+c`, `c\ge0`, satisfies the inequality), as CLAUDE.md's
characterization-problem rigor rule requires. No skipped cases (each proof's own case analysis on
`g`'s zero set / sign structure is genuinely exhaustive), no hand-waving language load-bearing
(the few uses of "trivially"/"WLOG" found by grep are legitimate: base-case induction and a
genuine symmetry relabeling, both explicitly justified).

## Promotable lemmas

Not certified into `results/imo-2026-05/lemmas/` — the problem is now fully solved and
`current.md` holds the complete self-contained proof (using the `cross-substitution-fixed-point`
closing argument, which is the cleanest and needs no imported lemma cache). The shared base
layer and Tool A/B are recorded inline in `current.md` rather than as separate lemma files, since
no further round is needed on this problem.

## current.md

Updated to `## Status: solved` with a complete, self-contained `## Full proof` synthesizing the
shared base layer (Steps 1–4, common to all four and independently re-verified here) with the
`cross-substitution-fixed-point` telescoping closing argument (Steps 5–6), which I judged the
most rigorous and simplest of the four correct closing arguments. Sufficiency direction included
and verified by direct algebraic identity `(x-y-c)^2\ge0`.

## Verdicts

- `extremal-sup-inf` — **APPROVE** (Status: solved). Correct, complete, rigorous.
- `cross-substitution-fixed-point` — **APPROVE** (Status: solved). Correct, complete, rigorous;
  cleanest closing argument, used as the `current.md` proof.
- `orbit-telescoping-aimo0710` — **APPROVE** (Status: solved). Correct, complete, rigorous
  (heavier machinery than needed, but no gap).
- `monotonicity-order` — **APPROVE** (Status: solved). Correct, complete, rigorous.

The problem `imo-2026-05` is now solved; `results/imo-2026-05/current.md` reflects this with the
full proof. No further rounds are required on this problem.
