## imo-2026-03 (lens: n=3 Existence Theorem, Region II)

### Setup recap (from `global-lp-vertex-sufficiency.md` + certified lemma
`construction-h-and-p4-margin-identity.md`)

- $B(3)$: $g_1,g_2,g_3>\gamma(3)=1/15$, $p_1<1/2$ (gaps $g_1=p_1-p_2$,
  $g_2=p_2-p_3$, $g_3=p_3-p_4$; mass identity $4p_4+g_1+2g_2+3g_3=1$).
- Region I $:=B(3)\cap\{p_4\le\gamma(3)\}\cap\{g_3+p_4>3g_1\}$ — **fully
  closed** (round 21) via Construction H: $p_1\to(g_1,p_2)$,
  $p_3\to(x,x,g_1)$, $x=(p_3-g_1)/2$, giving the exact identity
  $\mathrm{OddSum}(H)-c(3)=(p_4-\gamma(3))/2$.
- Region II $:=B(3)\setminus$ Region I $=\{p_4>\gamma(3)\}\cup
  \{g_3+p_4\le3g_1\}$ — **open**. Round 21 found best-of-$\{$C,H$\}$
  (C = double-cascade: $p_1\to\{p_2,g_1\}$, $p_3\to\{p_4,g_3\}$) fails on
  a genuine $\approx3\%$ sample of Region II, exact witness:
  $g_1=\tfrac{3161}{46875},g_2=\tfrac{205073}{3000000},
  g_3=\tfrac{456719}{3000000},p_4=\tfrac{339131}{4000000}$
  ($p=(0.3728,0.3054,0.2370,0.0848)$; both $\mathrm{OddSum}(C)=
  \mathrm{OddSum}(H)\approx0.5424>c(3)\approx0.5333$).

### Verified this round: the "$p_1$-touching" construction family works
where C/H fail, and Region II splits into (at least) two structurally
distinct hard sub-cases, not one.

**Structural read of the round-21 counterexample point** (verified in
exact `Fraction` arithmetic): $p_4=0.0848>\gamma(3)=0.0667$ — this point
falls in Region II purely because $p_4$ is **not small** (fails the
$p_4\le\gamma(3)$ half of Region I), while it actually *does* satisfy
$g_3+p_4>3g_1$ ($0.237>0.202$). All four pieces are comparable in size
($p_1{=}0.373,p_2{=}0.305,p_3{=}0.237,p_4{=}0.085$) — a genuinely
"near-uniform" configuration, unlike Region I's near-degenerate corner
$p^\dagger=(6,5,4,0)/15$ where $p_4\to0$.

**New construction "Q" (bisect $p_1$; tie a $p_2$-fragment to $p_3$):**
$p_1\to(p_1/2,p_1/2)$, $p_2\to(g_2,p_3)$ (i.e. split off a fragment
exactly equal to $p_3$'s own value from $p_2$), leave $p_3,p_4$
untouched. At the round-21 counterexample: $\mathrm{OddSum}(Q)=
\tfrac{12197101}{24000000}\approx0.5082<c(3)$ — a **comfortable margin**
($0.508$ vs. C/H's $0.542$, target $0.533$), found via exact
breakpoint/vertex enumeration of the 1-free-parameter LP with $p_1$
bisected (piecewise-linear objective in the $p_2$-split point; global
min located exactly, not by grid search). A sibling variant "R" (tie the
$p_2$-fragment to $p_4$ instead of $p_3$) gives the **identical** exact
value at this point (the objective is flat/tied on the whole interval
$[g_2,p_4]$ of the split parameter) — both are legitimate, interchangeable
witnesses here.

**Global search (differential_evolution over $B(3)$, own float
parametrization $4p_4+g_1+2g_2+3g_3=1$) confirms best-of-$\{$C,H,Q,R$\}$
still fails**, but on a *different*, genuinely smaller/different-shaped
residual than the original $\{$C,H$\}$ residual: the worst point found
sits near the *opposite* extreme, $p_1\to1/2^-$ (the $B(3)$ boundary),
with $g_3=\gamma(3)$ exactly (tight at the floor) and $g_1\approx g_2$
both large — e.g. $p=(0.5^-,0.311,0.128,0.061)$,
$g=(0.189,0.183,0.0667)$, all of C, Q, R tied at $\mathrm{OddSum}=
0.5611$, violation $\approx1/36$ (H illegal there, $x<0$). This is
**structurally the opposite regime from the original counterexample**:
$p_1$ large (near the region's own upper edge) rather than
near-uniform, and $g_3$ pinned at the floor rather than large.

**New construction "W" (self-referential trisection of $p_1$):** $p_1\to
(p_2,p_3,p_1-p_2-p_3)$ — split $p_1$ into three fragments exactly
matching $p_2$, $p_3$, and the remainder; legal only when $p_1>p_2+p_3$
(true near this $p_1\to1/2$ regime, false at the original near-uniform
counterexample). At the $p_1\to1/2^-$ worst point: $\mathrm{OddSum}(W)=
0.5<c(3)$ — **clears the target with a comfortable margin**, where
C/Q/R all fail. Adding W to the panel and re-running the global search:
the worst residual shrinks from $\approx0.0278$ (best-of-$\{$C,H,Q,R$\}$)
to $\approx0.0074$ (best-of-$\{$C,H,Q,R,W$\}$) — genuine, large
improvement, not closed. The residual concentrates exactly where $W$'s
legality condition $p_1>p_2+p_3$ becomes marginal ($\mathrm{rem}=p_1-
p_2-p_3\to0^+$), i.e. a boundary between W's validity domain and the
region where it isn't usable.

**New construction "BB" (bisect $p_1$ like C's split, but bisect $p_3$
instead of splitting it toward $p_4$):** $p_1\to(g_1,p_2)$, $p_3\to
(p_3/2,p_3/2)$, leave $p_2,p_4$ untouched. At the near-worst
$p_1\to1/2^-$ point found by the panel-augmented search (residual
$\approx0.0074$ above), BB lands **within $5\times10^{-10}$ of $c(3)$
exactly** (essentially tight from above, almost certainly the true
equality locus of a genuine algebraic boundary, not a numeric fluke —
the optimizer's point is itself only an approximate vertex). BB also
clears the *original* near-uniform counterexample comfortably
($\mathrm{OddSum}(BB)\approx0.5087<c(3)$). This near-exact tightness is a
strong structural signal that BB (or a small variant of it) is the
*natural* construction for the $p_1$-large/$g_3$-tight sub-regime, in
the same sense Construction H is natural for Region I (both give clean
closed-form-looking equality boundaries).

### Structural characterization of Region II's hard points (conjectural,
not proved)

Two distinct extremal "shapes" have been found, not one:

1. **Near-uniform / $p_4$ moderately large** ($p_4>\gamma(3)$, all four
   pieces comparable in size, $g_1,g_2$ both close to the floor
   $\gamma(3)$, $g_3$ large): C and H both fail here; **Q/R (bisect $p_1$
   + tie a $p_2$-fragment to $p_3$ or $p_4$) fix it with comfortable
   margin.**
2. **$p_1$ near its own upper boundary $1/2$, $g_3$ pinned at the floor
   $\gamma(3)$, $g_1\approx g_2$ both large** ($p_4\le\gamma(3)$ but
   $g_3+p_4\le3g_1$, i.e. the *other* half of Region II's definition):
   C/Q/R all fail here; **W (self-referential trisection of $p_1$ into
   $p_2,p_3$, and remainder) and BB (bisect $p_1$'s C-split further by
   also bisecting $p_3$) both help, with BB landing essentially exactly
   on the boundary** — the more promising lead of the two for a clean
   closed-form proof, since W's usable domain ($p_1>p_2+p_3$) doesn't
   cover the whole sub-case.

This split lines up with the algebraic case-split already implicit in
Region II's own definition ($\{p_4>\gamma(3)\}$ vs. $\{g_3+p_4\le3g_1\}$
— these are not disjoint but the two hard points found sit essentially
one in each half), suggesting the outliner should **not** look for one
uniform Region-II construction (round 21 already showed 8 single
mechanisms all fail somewhere) but a **further two-way (or more) case
split *within* Region II itself**, mirroring Region I's own successful
single-construction/single-region pairing.

### Candidate technique(s) for the outliner

- Formalize Construction Q/R (bisect $p_1$, tie a $p_2$-fragment to $p_3$
  or $p_4$) as the closer for the "$p_4>\gamma(3)$" / near-uniform half
  of Region II — derive its exact closed-form value identity (analogous
  to $\mathrm{OddSum}(H)-c(3)=(p_4-\gamma(3))/2$) via the same
  order-condition + mass-identity substitution method that closed Region
  I, then find the exact order conditions under which it applies and
  check they cover (at least) $\{p_4>\gamma(3)\}\cap B(3)$.
- Formalize Construction BB (bisect $p_1$ like C, bisect $p_3$ in half)
  as the closer for the "$g_3+p_4\le3g_1$" / $p_1$-large / $g_3$-tight
  half — its near-exact tightness at the found worst point is a strong
  signal a clean closed form exists; derive it the same way.
- Both are genuinely different splitting *patterns* (not tie-parameter
  tweaks of C/H): Q/R never touch $p_3$ or $p_4$ directly, splitting
  $p_1$ and $p_2$ only; BB splits $p_1$ and $p_3$ but ties differently
  than C (bisection of $p_3$, not a $p_4/g_3$-tied split); W is a
  3-fragment self-referential split of $p_1$ alone, structurally unlike
  anything in the round-21 panel of 8.

### Cheap-kill candidates
- Before investing proof effort in Q/R: check their legality condition
  ($g_2,p_2-g_2>0$, i.e. always legal since $p_2>g_2>0$ in $B(3)$) —
  cheap, likely always legal, unlike H which needs $x>0$.
- Before investing in W: its legality condition $p_1>p_2+p_3$ is a real
  constraint, not always true in Region II (false at the near-uniform
  counterexample) — must be paired with a fallback (BB or Q/R) exactly
  where it's illegal or marginal.
- Before investing in BB: verify whether $g_1-p_3/2$ (order condition
  needed for BB's sorted-position formula) actually holds throughout the
  $g_3$-tight sub-regime — not yet checked exactly this round (only
  numerically at two points).

### Knowledge-base entries to use
- Same machinery as Region I's closure: piecewise-linear/rank-parity
  vertex argument (`OddSum` affine within a fixed rank-order cell), mass
  identity $4p_4+g_1+2g_2+3g_3=1$ for algebraic substitution, per
  `construction-h-and-p4-margin-identity.md`.
- Greedy-optimality lemma (`greedy-optimality-oddsum.md`) underlying all
  `OddSum` computations.

### Analogous past problems (cruxes)
None newly consulted this round (lens was numeric/structural
reconnaissance on an already-scoped algebraic sub-target, not a fresh
top-level framing search) — round 17/19's prior findings (no viable
generating-function/entropy/rearrangement route for this problem family)
still stand; no reason to expect a crux match for this specific
construction-design sub-task.

### Prior progress
Region I fully closed (round 21, certified). Region II open; round 21
found best-of-$\{$C,H$\}$ leaves a genuine $\approx3\%$ residual. This
round found two new constructions (Q/R and W/BB) that each fix one of
the two structurally distinct hard sub-cases found in Region II, cutting
the worst-case violation found by a broad global search from
$\approx0.0278$ (best-of-C,H,Q,R) to $\approx0.0074$ (adding W) — real
progress, **not a closure**: a residual remains near the boundary where
W's legality condition ($p_1>p_2+p_3$) becomes marginal, and none of
Q/R/W/BB have been proved in exact closed form yet (only spot-verified
numerically at a handful of points, unlike Region I's Construction H
which has a fully proved closed-form identity).

### Dead ends (do not retry)
- The 8 single-mechanism constructions from round 21's panel (A/B tied
  pairings, C, D shift-down, E skip-$p_2$, F skip-$p_3$, G cascade, K
  full-cascade, trisection) as **standalone universal** Region-II
  closers — all already confirmed to fail somewhere (round 21).
- Best-of-$\{$C,H$\}$ alone as a Region-II closer — confirmed to fail on
  a genuine (not sampling-noise) $\approx3\%$ residual (round 21,
  reproduced this round at the exact cited point).
- Bisecting both $p_1$ and $p_2$ in half simultaneously (no ties to
  other pieces) — tested this round at the near-uniform counterexample,
  gives $\mathrm{OddSum}\approx0.576$, far worse than target.
- "Tie everything to $p_4$" (split $p_1,p_2,p_3$ each into a $p_4$-valued
  fragment plus remainder, leave $p_4$ whole) — tested at the
  near-uniform counterexample, gives $\mathrm{OddSum}\approx0.610$, much
  worse; this mechanism concentrates too much mass at low rank and is
  not promising.

### Small-case / intuition notes (conjecture only, not proved)
- Region II's hard points are NOT one connected extremal shape; the
  numeric search strongly suggests (not proves) at least two local
  extrema with different structural signatures, matching the region's
  own two-part definition ($p_4>\gamma(3)$ vs. $g_3+p_4\le3g_1$). A
  natural conjecture for next round: split Region II itself into
  Region IIa $:=\{p_4>\gamma(3)\}$ (closed by Q/R) and Region IIb
  $:=\{p_4\le\gamma(3)\}\cap\{g_3+p_4\le3g_1\}$ (closed by BB, with W as
  a secondary witness where legal) — analogous to how Region I itself was
  carved out with a clean two-inequality intersection. This is a
  **conjecture based on 2 hard points and one global optimizer run each**,
  not an exhaustive sweep; the outliner/builder should re-run a dedicated
  worst-case search restricted to each half separately before trusting
  the split is exhaustive.
