# Lemma: Sum-Bound Base Case (`rest = ∅`, `q=3`)

**Status:** CERTIFIED (round 16, proposed by `potential-weighting-upper-bound` §25.1/§26, following
the round-16 `math-explorer-gap1b-basecase` finding and independently re-verified from scratch by
both the round-16 outline-reviewer and the round-16 proof-builder — two independent fresh
`Fraction`-exact harnesses, `0` violations in both, plus the pure algebraic core re-derived by hand
by three independent agents this round with no discrepancy). Closes the base case (`|Z_1|=1`) of
`potential-weighting-upper-bound.md`'s Gap 1b (the Sum Bound). The general recursion-depth induction
for `|Z_1|\ge2` remains open — **this lemma is a base case only, not the full Sum Bound.**

## Setting and notation

Fix a genuine `q=3` `\mathcal F` base-generator instance: `b_0\ge0` and `Z_0=(z_1,z_2,z_3)` sorted
strictly descending (`z_1>z_2>z_3\ge0`), in the sense of `potential-weighting-upper-bound.md` §17.5.
For `k^*\in\{2,3\}` write `d_{k^*}:=z_1-z_{k^*}`, `D_{k^*}:=|b_0-d_{k^*}|`, and let `w_1` denote the
*other* element of `\{z_2,z_3\}` (i.e. `\mathrm{Res}=Z_0\setminus\{z_1,z_{k^*}\}=\{w_1\}`, a
singleton — this is exactly the `\mathrm{rest}=\emptyset` case of the general Sum Bound induction, so
called because the *residual list feeding the recursion one level further* is empty; the single
element `w_1` sits at the level being resolved right now). Let
```
A_1 := OPT_{+1}(\{b_0\}, Z_0\setminus\{z_1\}),      A_{3,l} := OPT_{+1}(\{b_0,d_l\}, Z_0\setminus\{z_1,z_l\})  (l=2,3),
M := \min(A_{3,2}, A_{3,3}),
```
using the `\mathrm{OPT}_\sigma$ notation of the certified Generalized Multi-Background Peeling Lemma
(`potential-weighting-upper-bound.md` §13.2). Say **the trigger holds at `k^*`** if `M=A_{3,k^*}<A_1`,
and say **`h=0` holds at `k^*`** if `b_0<w_1` and `d_{k^*}<w_1` (both elements of the 2-element
background `\{b_0,d_{k^*}\}` used at level `k^*` are strictly below `w_1:=\max(\mathrm{Res})`).

## Statement

**Lemma.** At any genuine `q=3` `\mathcal F` base-generator instance, for any `k^*\in\{2,3\}` at which
both the trigger and `h=0` hold,
```
M = D_{k^*}          (equivalently, w_1 >= 2 D_{k^*}).
```
I.e. at the base case of the recursion (`\mathrm{Res}$ a singleton), DELETE beats or ties KEEP inside
`k^*`'s own sub-problem, whenever `k^*`'s trigger and `h=0` both hold.

## Proof

**Ingredients used (all already certified or already-proved-elsewhere, cited precisely — none are
re-derived here, only combined):**

1. **Singleton-list dichotomy + Keep-Top Bound (exact `q=3` value of `M`).** Since
   `\mathrm{Res}=\{w_1\}$ is a singleton, `A_{3,k^*}=\mathrm{OPT}_{+1}(\{b_0,d_{k^*}\},\{w_1\})` is a
   minimum over *exactly two* selections of a one-element list: "delete `w_1`" (value
   `e(\{b_0,d_{k^*}\})=D_{k^*}`, since a deleted element contributes nothing — the standing convention
   of `potential-weighting-upper-bound.md` §13.2) or "keep `w_1`" (value
   `e(\{b_0,d_{k^*},w_1\})`). Under `h=0` at `k^*`, the certified **Keep-Top Bound**
   (`lemmas/three-bound-domination-and-keep-top-bound.md`) computes the "keep" value exactly: `w_1` is
   strictly the largest of `\{b_0,d_{k^*},w_1\}`, so `e(\{b_0,d_{k^*},w_1\})=w_1-|b_0-d_{k^*}|=w_1-D_{k^*}`
   exactly (not merely an upper bound — the Keep-Top Bound's own proof identifies this as the *value* of
   the one alternative selection, and here it is literally the only other selection, so it is exact,
   not merely an upper bound on a minimum over many candidates). Hence
   ```
   A_{3,k^*} = min(D_{k^*}, w_1 - D_{k^*})    ...  (dichotomy)
   ```
   exactly. **This is a two-step combination — a trivial enumeration fact (a singleton list has
   exactly two selections) plus the certified Keep-Top Bound — not itself a pre-existing standalone
   certified lemma** (the round-15 lemma file `lemmas/three-bound-domination-and-keep-top-bound.md`
   explicitly declined to certify this exact-dichotomy identity on its own, as "too narrow"; it is
   reconstructed here from its two free ingredients).

2. **`A_1\le b_0`.** The certified **Shrink-List Monotonicity Corollary**
   (`lemmas/shrink-list-monotonicity.md`): iterating `OPT_{+1}(C,W)\le OPT_{+1}(C,W\setminus\{x\})`
   down to the empty list gives `OPT_{+1}(C,W)\le e(C)` unconditionally. Applied with `C=\{b_0\}`,
   `W=Z_0\setminus\{z_1\}$: `A_1\le e(\{b_0\})=b_0`.

3. **`A_1\le w_1-b_0`.** `A_1`'s own search space is `Z_0\setminus\{z_1\}=\{w_1,z_{k^*}\}` (a
   2-element list, since `\{z_2,z_3\}=\{w_1,z_{k^*}\}`). The single selection "keep `w_1`, delete
   `z_{k^*}`" is one particular member of this search space, with value `e(\{b_0,w_1\})=|b_0-w_1|`.
   Since `A_1` is a minimum over its whole search space, `A_1\le|b_0-w_1|`. This is exactly Step-1
   `(†)` of `potential-weighting-upper-bound.md` §21.1 (`A_1\le|b_0-z_j|` for any index `j`,
   instantiated at `j=$ the index of `w_1`), an unconditional, already-on-file elementary fact
   (immediate from the "delete contributes 0" convention, requiring no further proof). Using `b_0<w_1`
   (the `h=0` hypothesis), `|b_0-w_1|=w_1-b_0`, so `A_1\le w_1-b_0`.

**Main argument.** Suppose, for contradiction, `M\ne D_{k^*}`, i.e. (by the dichotomy (1))
`M=w_1-D_{k^*}<D_{k^*}$, i.e. `2D_{k^*}>w_1`. The trigger hypothesis gives `M<A_1`. Combine this with
Ingredients 2 and 3 in turn:
```
w_1 - D_{k^*} = M < A_1 <= b_0            =>   w_1 < D_{k^*} + b_0                      ...(i)
w_1 - D_{k^*} = M < A_1 <= w_1 - b_0      =>   D_{k^*} > b_0                            ...(ii)
```
From (ii): `D_{k^*}=|b_0-d_{k^*}|>b_0\ge0`. If instead `d_{k^*}\le b_0`, then
`D_{k^*}=b_0-d_{k^*}\le b_0`, contradicting `D_{k^*}>b_0`; hence `d_{k^*}>b_0`, forcing
`D_{k^*}=d_{k^*}-b_0` exactly (the absolute value resolves without ambiguity). Substituting this exact
form into (i):
```
w_1 < D_{k^*} + b_0 = (d_{k^*}-b_0) + b_0 = d_{k^*}.
```
But `h=0` at `k^*$ requires (by definition) `d_{k^*}<w_1`. So `w_1<d_{k^*}<w_1`, a direct, immediate
contradiction (a real number strictly less than itself).

Hence the supposition `2D_{k^*}>w_1` is false: `2D_{k^*}\le w_1`, i.e. (by the dichotomy)
`M=\min(D_{k^*},w_1-D_{k^*})=D_{k^*}`. `\blacksquare`

## Tightness

At the boundary `2D_{k^*}=w_1` exactly, the dichotomy gives `M=\min(D_{k^*},w_1-D_{k^*})=w_1/2`, while
Ingredients 2+3 give `A_1\le\min(b_0,w_1-b_0)\le w_1/2` always (elementary: for any `b_0\in[0,w_1]`,
one of `b_0,w_1-b_0` is `\le w_1/2`). Hence the trigger `M<A_1$ is *automatically vacuous exactly at
the boundary* — the hypothesis "trigger holds" cannot be satisfied there, which is precisely why the
lemma's conclusion is the tight, non-strict `w_1\ge2D_{k^*}` rather than a strict inequality: no
sharper (unconditional) statement is possible, since the boundary case cannot be excluded by any
argument that only uses the trigger.

## Isolated pure-algebraic core (verified independently of the surrounding game)

The entire argument above reduces to one self-contained real-number fact, decoupled from
`\mathrm{OPT}_\sigma`'s recursive definition entirely:

> **Pure Lemma.** Let `0\le b_0<w_1` and `0\le d<w_1` be reals, `D:=|b_0-d|`. If
> `\min(D,w_1-D)<\min(b_0,w_1-b_0)`, then `2D\le w_1`.

The proof above, with `d_{k^*}\to d`, is exactly a proof of this Pure Lemma (the trigger `M<A_1`
combined with the dichotomy and Ingredients 2/3 gives precisely its hypothesis, since
`A_1\le\min(b_0,w_1-b_0)` unconditionally by Ingredients 2+3, so `M<A_1$ implies the *weaker*
`M<\min(b_0,w_1-b_0)`, losing no needed case — the real trigger could make `A_1` strictly smaller than
`\min(b_0,w_1-b_0)$ via internal MATCH-term cancellation, which only strengthens the hypothesis, never
weakens it).

## Verification

- **Isolated Pure Lemma:** independently checked by the round-16 explorer (`1{,}108{,}500` random
  exact-`Fraction` trials filtered to the hypothesis, `0` counterexamples) and independently
  re-verified by this round's builder with fresh code (`/tmp/round-16/verify_builder/pure_algebra.py`):
  `65{,}403` filtered trials (integer/rational `w_1,b_0,d`, `v_{\max}` up to `100`), `0` violations;
  plus a dedicated boundary sweep (`14{,}439` trials forced exactly onto `2D=w_1`), confirming the
  hypothesis is **never** satisfiable there (`0` cases where it held), matching the tightness argument
  above exactly.
- **Full game-level statement:** independently checked by the round-16 explorer (own harness,
  `905/905` genuine triggered `h=0` `q=3` instances, `0` violations) and by this round's builder with
  an independently-coded brute-force `\mathrm{OPT}_{+1}` (full enumeration of every Keep/Delete/Match
  selection, not the closed-form dichotomy — `/tmp/round-16/verify_builder/gap1b_check.py`):
  `2{,}976` genuine triggered `h=0` instances out of `29{,}126` raw random trials (mixed
  integer/rational alphabets, `v_{\max}\in\{5,10,20,30,50\}`), **`0` violations** of `M=D_{k^*}`, and
  `0` mismatches between the brute-force `M` and the dichotomy formula `\min(D_{k^*},w_1-D_{k^*})`
  (an independent sanity check that Ingredient 1 is being applied correctly). Independently by the
  outline-reviewer this round: exhaustive small-integer grid (`0/24`), exhaustive half-integer grid
  targeting boundary/tie cases (`0/88`), a targeted boundary construction (`0/1{,}630`), and a negative
  control (dropping the trigger while keeping `h=0` gives `12.4\%` violations, confirming the trigger
  hypothesis is load-bearing, not vacuous).

## Scope — what this does NOT prove

This closes **only** the base case `\mathrm{rest}=\emptyset` (`|Z_1|=1`, equivalently `q=3`) of the
general Sum Bound conjectured in `potential-weighting-upper-bound.md` §21.2/§23.3. The general
recursion-depth induction for arbitrary `|Z_1|\ge2` (needing its own three named bookkeeping
subtleties — argmin-tie branch filtering, continuous zero-slope tie intervals, the killed
`\max(\mathrm{rest})` shortcut) is a **separate, much larger, still fully open task**, not addressed
by this lemma. Do not cite this lemma as "the Sum Bound is proved" — only as "the Sum Bound's base
case is proved."

## Used by

- `potential-weighting-upper-bound.md` §25.1/§26 (Gap 1b's base case, the `|Z_1|=1$ instance of the
  Sum Bound induction skeleton of §21.2/§23.3).
