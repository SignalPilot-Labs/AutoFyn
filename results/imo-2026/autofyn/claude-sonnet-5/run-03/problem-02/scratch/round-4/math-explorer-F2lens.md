## Lens: identify F2 geometrically; check range-connectedness numerically

Scope per assignment: not a proof attempt — numerics + symbolic factoring only,
to feed the outliner/builder working on
`approaches/coordinate-bash-resultant-boundary.md`'s continuity/IVT
branch-selection mechanism (gap 2, the sole remaining gap for imo-2026-02).

### (a) F2's geometric meaning: F2 = 0 is exactly β = ∠ACB

Using the file's exact symbolic setup (`A=(0,0),B=(a,0),C=(b,cc)`,
`u=tan(β/2)`, `F2 = -2ab*u + a*cc*u² - a*cc + 2b²u + 2cc²u`), solved `F2=0`
for `u` in `sympy` and computed `tan β` at the root (via `2u/(1-u²)`):

```
tan(β) at root = a*cc/(b² + cc² - a*b)   (both roots of the quadratic give the same tan β)
```

Independently computed the tangent of every "natural" triangle angle at
`A,B,C,M,N` via the signed cross/dot formula `tan(∠XPY)=cross(PX,PY)/dot(PX,PY)`,
symbolically in `a,b,cc`. Exact match:

```
tan(∠ACB) = cross(CA,CB)/dot(CA,CB) = a*cc/(b² + cc² - a*b)   ← identical to F2's root
```

No other candidate (∠BAC, ∠ABC, ∠ANB, ∠ANC, ∠ABN, ∠ACM, ∠NBC) matched.

**Conclusion: `F2 = 0 ⟺ β = ∠ACB` exactly** (mod π; within the relevant
domain `β∈(0,π)` this pins down a single value, `β=∠ACB`, by the same
argument the population already uses for `F1 ⟺ β=∠ABC` — tan is injective
mod π, so the unique solution in `(0,π)` of `tan β = tan(∠ACB)` is `β=∠ACB`
itself). This is a clean, fully symbolic, general fact — no numerics needed
for the algebraic identification, exactly parallel to `F1`'s certified
identification with `∠ABC`.

### (b) Geometric confirmation: F2 = 0 is the L-exits-triangle-BNC boundary

Built a from-scratch numeric solver (not reusing either builder's script) of
the true (unsquared) hypothesis-2/hypothesis-3 angle equations, using the
homogeneity-decoupling fact (hyp2 depends only on `(β,s2)`, hyp3 only on
`(β,t1)`) to solve each as an independent 1-D root-finding problem via
`scipy.optimize.brentq`, then checked the actual containment conditions
"`K` inside triangle `BMC`" and "`L` inside triangle `BNC`" (three signed-area
test) as `β` is swept.

**Key test triangle, chosen specifically because `∠C < ∠B`** (all four
triangles tested by round 3's siblings happened to have `∠B < ∠C`, so this
case was never actually exercised): `A=(0,0), B=(2,0), C=(-1,3)`,
giving `∠B=45.000°`, `∠C=26.565°`.

Sweeping `β` finely (steps of 0.1°) across the `∠C` value: **`L` inside
`BNC` is `True` for all sampled `β<26.5651°` and `False` for all sampled
`β>26.6651°`** — i.e. the transition is pinned to `β=∠C=26.565°` to at
least 4 decimal digits, exactly where `F2=0` predicts it, while `K` inside
`BMC` remains `True` throughout (its own boundary, `∠B=45°`, is farther
out). This is a **new, previously-unobserved phenomenon**: `F2=0` is not
some unrelated/mysterious locus — it is **the exact mirror image of `F1`**:
`F1=0` ⟺ `β=∠B` ⟺ the boundary where `K` (extended along ray `BK`) exits
triangle `BMC` through side `BC`; `F2=0` ⟺ `β=∠C` ⟺ the boundary where `L`
(extended along ray `CL`) exits triangle `BNC` through side `BC`. Same
containment-exit mechanism, applied to the other of the two moving points.

### (c) Range-connectedness: strong positive evidence, with one important numerical caveat

Tested 4 triangles total (the 3 from round 3's numerics plus the new
`∠C<∠B` one above) with dense `β`-sweeps. Finding, consistent across all 4:
**the valid range (where both containments hold) is exactly
`(0, min(∠B,∠C))`** — i.e. whichever of `F1`'s root (`∠B`) or `F2`'s root
(`∠C`) is smaller is the true upper endpoint of the valid range, and the
range never reaches the *other*, larger root at all. Since the valid range
is by construction bounded above by `min(∠B,∠C)`, it **cannot cross either
`F1=0` or `F2=0` in its interior** — range-connectedness would follow
immediately from establishing this "valid range = `(0,min(∠B,∠C))`" fact
rigorously (i.e., ruling out any *other*, unrelated boundary cutting the
range shorter still — see the open item below).

**Important methodological caveat, worth flagging for the next builder**:
a naive per-`β` independent bracket search for `s2`/`t1` (scan `[lo,hi]`,
take the first sign change) is **numerically unreliable** near/past the
boundary, because for larger `β` the hyp2/hyp3 polynomials can have
*multiple* real roots (confirmed: 1 root for small `β`, jumping to 3 roots
for `β` past roughly 32–33° in one test triangle) — an independent bracket
search can silently jump to the wrong (spurious/extraneous) root, producing
a **false discontinuity** that looks like a containment failure but is
actually a root-tracking artifact. Concretely, this happened in an initial
pass on triangle `A=(0,0),B=(5,0),C=(4,1)` (`∠B=45°,∠C=120.96°`, so `F2`'s
root is far outside and should be irrelevant): the naive solver reported
`K` exiting `BMC` around `β≈34–44°`, well before `∠B=45°`, contradicting
`F1`'s certified boundary. Re-solving with **continuation** (track the root
closest to the previous `β`'s root, not the first bracket found) shows this
was spurious: with continuation, `K` stays inside `BMC` all the way to
`β≈44.9°` with the signed distance to edge `CB` shrinking smoothly to 0
exactly as `β→∠B=45°` from below, and only the *last* sample (`β=44.9°`,
past the true boundary) shows a genuine, expected exit. **Recommendation:
any builder doing further numerics on this branch-selection question should
use continuation-based root tracking, not independent bracket search per
`β`, to avoid false-positive "range cut short" artifacts.**

With continuation applied, all 4 triangles cleanly confirm valid range
`=(0,min(∠B,∠C))` with no earlier cutoff observed (i.e. no evidence that the
range is cut short by the edges `BM`/`BN` of the containment triangles, or
by the two extra hypotheses "`K` inside `∠LBA`"/"`L` inside `∠ACK`" —
though this was checked only by the same containment/sign tests, not
exhaustively for every conceivable failure mode).

### What this hands to the builder

1. **`F2=0 ⟺ β=∠ACB`**, proved symbolically/generally exactly like `F1`'s
   certified identification (§(a) above; ready to write up as a lemma
   parallel to `branch-crossing-locus-equals-angle-B.md`, replacing `∠ABC`
   with `∠ACB` and the `K`/`BMC` containment with the `L`/`BNC` containment).
2. **Range-connectedness reduces to one clean geometric claim**: the valid
   range for `β` (satisfying both `K∈int(BMC)` and `L∈int(BNC)`) is exactly
   `(0, min(∠ABC,∠ACB))` — i.e. `K` exits its triangle through side `BC`
   exactly at `β=∠B` and `L` exits its triangle through side `BC` exactly at
   `β=∠C`, and *neither* exits earlier via a different edge or a different
   hypothesis. If a builder can prove this claim synthetically (it looks
   tractable: it's a monotonicity/ray-sweep argument — as `β` increases from
   `0`, ray `BK` sweeps from direction `BA` and only ever approaches `BC`,
   with `K` staying inside `∠ABC` throughout so the only way to leave
   triangle `BMC` is through `BC` or through `BM`; symmetric for `L`/`BNC`),
   then `F1,F2 ∉ (0,\min(\angle B,\angle C))$'s interior follows
   trivially (they equal the interval's own endpoints, not interior points),
   closing gap 2's range-connectedness requirement outright.
3. Confirmed numerically on 4 independent triangles (2 with `∠B<∠C`, 2 with
   `∠C<∠B`, using continuation-based root tracking) — no counterexample to
   "valid range `=(0,min(∠B,∠C))`" found, but not yet a general proof.
