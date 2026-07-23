## imo-2026-03 — Gap 1b base case (rest=∅ sub-case of the Sum Bound)

### Headline

**Found a complete, elementary, hand-checkable proof of the base case** (`M = D_{k*}`, i.e.
`w_1 >= 2*D_{k*}` at genuine `q=3`, `h=0`-triggered instances). It needs nothing beyond two bounds
on `A_1` that are *already either certified or trivial on file* — the only missing ingredient was
combining **both** of them simultaneously (round 15 only chained one). I verified the resulting pure
algebraic core claim computationally (1.1M random exact-`Fraction` trials, 0 counterexamples) in
addition to re-confirming the original game-level claim from scratch (905/905 genuine triggered `h=0`
instances, 0 violations). This is a proof, not just stronger corroboration — recommend the outliner
route it straight to a builder for write-up/certification rather than further exploration.

### The missing step, precisely

**Setup (restating the dispatch's own notation).** At a genuine `q=3` base-generator instance
(`b_0`, `Z_0=(z_1,z_2,z_3)`, `z_1>z_2>z_3\ge0`), fix `k^*\in\{2,3\}`, write `d:=d_{k^*}=z_1-z_{k^*}`,
`w_1:=` the other element of `\{z_2,z_3\}` (i.e. `\mathrm{Res}=\{w_1\}`), `D:=D_{k^*}=|b_0-d|`. The
**exact q=3 dichotomy** (certified, `lemmas/three-bound-domination-and-keep-top-bound.md`) gives,
whenever `h=0` (`b_0<w_1` and `d<w_1`):
```
M = min(D, w_1-D)        exactly.
```
Goal: prove `M=D`, i.e. `2D<=w_1`, whenever the base generator's own trigger `M<A_1` holds
(`A_1:=OPT_{+1}(\{b_0\},(z_2,z_3))`, independent of which `k^*`).

**Two already-available bounds on `A_1` (neither new, both cheap):**
1. `A_1 <= b_0` — the trivial "delete everything" selection. This is exactly the certified
   **Shrink-List Monotonicity Corollary** (`lemmas/shrink-list-monotonicity.md`, iterating
   `OPT_{+1}(C,W)<=OPT_{+1}(C,W\setminus\{x\})` down to the empty list gives `OPT_{+1}(C,W)<=e(C)`).
2. `A_1 <= |b_0-w_1| = w_1-b_0` (using `b_0<w_1` from `h=0`) — the "keep `w_1`, delete the other
   element of `A_1`'s own 2-element free list `(z_2,z_3)`" selection. This is exactly round 14's
   **Step 1 (†)**: "for any index `j`, `A_1<=|b_0-z_j|`" — already an unconditional, elementary fact
   on file, instantiated at `j=` the index of `w_1`.

**Round 15 used only bound 2** (getting `D>b_0`, correctly, but "not yet reconciled into a full
contradiction"). **The fix is to use bound 1 as well**, in the same contradiction argument:

**Proof.** Suppose for contradiction `2D>w_1`, i.e. `D>w_1-D`, so the dichotomy gives `M=w_1-D`.
The trigger `M<A_1` combined with bound 1 and bound 2 gives:
```
w_1-D < A_1 <= b_0        =>  w_1 < D+b_0                       ... (i)
w_1-D < A_1 <= w_1-b_0     =>  D > b_0                            ... (ii)
```
From (ii): `D=|b_0-d|>b_0>=0`. This forces `d>b_0` (if instead `d<=b_0` then `D=b_0-d<=b_0`,
contradicting `D>b_0`), so `D=d-b_0` exactly. Substituting into (i):
```
w_1 < (d-b_0)+b_0 = d.
```
But `h=0` requires `d<w_1` (the *other* half of `h=0`: both elements of `C=\{b_0,d\}` are `<w_1`).
So `w_1<d<w_1` — a direct contradiction. Hence `2D<=w_1`, i.e. `M=D` (DELETE wins or ties). `\blacksquare`

**This is a ~10-line proof, uses no case-work beyond one dichotomy split, and needs no computation
beyond substitution.** It does **not** need `k^*`'s *global* argmin-ness at all — only that `k^*`
itself satisfies the trigger `M<A_1` (`M` being *its own* value `A_{3,k^*}`) and `h=0` at `k^*`. This
is a genuine simplification worth flagging: the base case does not need the "global" part of
"global argmin," only the trigger.

### Isolated pure-algebra form (verified independently of the game)

The whole argument reduces to one clean, game-independent lemma, which is the "finite algebraic
claim" the dispatch predicted:

> **Lemma.** Let `0<=b_0<w_1` and `0<=d<w_1` be reals, `D:=|b_0-d|`. If
> `min(D,w_1-D) < min(b_0,w_1-b_0)`, then `2D<=w_1`.

Proof as above (contradiction: assume `2D>w_1`, use both halves of the `min` hypothesis). I verified
this **isolated** form computationally, decoupled entirely from the game's OPT recursion: 1,108,500
random exact-`Fraction` trials (`w_1` integer 1–50, `b_0,d` random fractions in range, filtered to the
hypothesis pool), **0 counterexamples**. Also checked the tightness mechanism: at the boundary
`2D=w_1` exactly, `min(D,w_1-D)=w_1/2`, while `min(b_0,w_1-b_0)<=w_1/2` always (elementary, since one
of `b_0,w_1-b_0` is `<=w_1/2`) — so the hypothesis `min(D,w_1-D)<min(b_0,w_1-b_0)` is *automatically
impossible* exactly at the boundary, which is why the conclusion is a tight, non-strict `<=` (matching
the dichotomy's own `<=` convention) rather than something sloppier.

### Why `A_1<=A_1`'s bound suffices (i.e. why the real trigger `M<A_1` implies the lemma's weaker
hypothesis)

Since `A_1<=min(b_0,w_1-b_0)` always (bounds 1+2 above, unconditional), the real trigger `M<A_1`
implies the *weaker* statement `M<min(b_0,w_1-b_0)` — exactly the pure lemma's hypothesis (with
`M=min(D,w_1-D)` by the certified dichotomy). No information is lost in the direction needed: `A_1`
could in principle be even smaller than `min(b_0,w_1-b_0)` (e.g. via internal MATCH-term
cancellation, `A_1=|b_0-(z_2-z_3)|`), which only makes the trigger a *stronger* hypothesis than what
the lemma needs — so the reduction from "real game trigger" to "pure algebra hypothesis" is valid
with no case lost.

### Verification performed (both re-derivation and re-confirmation)

1. **Pure algebra lemma**: 1,108,500 random `Fraction` trials, 0 violations (script above).
2. **Full game-level re-confirmation from scratch** (own harness, brute-force `OPT_\sigma` via
   complete enumeration of all `K/D/M` selections, not reusing any prior round's code): built genuine
   `q=3` base generators (real trigger `M<A_1`, `M=\min_l A_{3,l}` over `l\in\{2,3\}`), filtered to
   `h=0` at each candidate `k^*` achieving `M` (ties handled by checking every argmin index), 905
   genuine triggered `h=0` instances found across 20,000 raw random trials, **`M=D_{k^*}` in
   905/905**, 0 violations — consistent with all prior rounds' corroboration and with the new proof.
3. Symbolically re-derived the `A_1 = \min(b_0, w_1-b_0, |b_0-g|)` closed form for the 2-element free
   list `(z_2,z_3)` (`g:=z_2-z_3`), confirming along the way that the "keep both" and "keep the
   non-`w_1` element only" candidates are *always* dominated by simpler terms — not needed for the
   final proof (which only uses the two cheap bounds), but useful context: it shows `A_1`'s exact
   value can in fact be strictly below `\min(b_0,w_1-b_0)` (via the match term `|b_0-g|`), confirming
   the reduction direction discussed above is not vacuous/accidental.

### What remains (for the outliner/builder)

- This closes the **base case** (`\mathrm{rest}=\emptyset`) of Gap 1b's induction, i.e. Priority
  Build Target 2 of §23.4/§24.3. The **inductive step** (recursion-depth induction promised in §23.3,
  handling the three named bookkeeping subtleties — argmin-tie filtering, flat zero-slope intervals,
  the killed `\max(\mathrm{rest})` shortcut) is a **separate, still-fully-open task**, not touched by
  this finding.
- The `\sigma=-1` mirror of the Sum Bound (queued since §21.2/§23.3) is **not** addressed by this
  finding either — worth checking next whether it reduces to this `\sigma=+1` result plus the
  certified Shrink-List lemma (as flagged, not yet attempted).
- Recommend writing this base-case proof up verbatim as a new sub-lemma (e.g. "Sum-Bound Base Case
  Lemma") citing `lemmas/shrink-list-monotonicity.md`'s Corollary and round 14's Step 1 (†) as its two
  inputs, plus the certified exact `q=3` dichotomy from
  `lemmas/three-bound-domination-and-keep-top-bound.md`.

### Cheap-kill / structural notes

- No case-work beyond one dichotomy split was needed — this is *not* a case-heavy proof, contrary to
  what the induction-on-recursion-depth framing for the general Sum Bound might suggest. The base
  case is genuinely easy once both cheap `A_1` bounds are chained; the earlier "not yet reconciled"
  status was purely a matter of not having used bound 1 (`A_1<=b_0`) alongside bound 2, not a sign of
  deep difficulty.
- The base case's proof does **not** need `k^*`'s *global* argmin-ness (only its own local trigger) —
  worth propagating this simplification to any future write-up of the surrounding induction, in case
  it also reduces bookkeeping there (unverified whether the inductive step similarly avoids needing
  global-argmin-ness — flagged, not tested this round, out of scope for "base case only").

### Dead ends / prior work status (unchanged, for completeness)

- Round 13/14's asymptotic-tightness family (`Z_0=(n,n,n+1)`, `b_0=n/2`, ratio `\to2`) is consistent
  with this proof: the isolated pure-algebra lemma's tightness analysis above independently explains
  *why* the ratio can approach (but never cross) `2` — confirms, does not contradict, prior rounds'
  findings.
- Round 15's `D_{k^*}>b_0` forced-consequence chain is exactly step (ii) above — reused verbatim, not
  re-derived from scratch; this report's contribution is adding step (i) (from the previously-unused
  `A_1<=b_0` bound) and the final substitution that closes the contradiction.
