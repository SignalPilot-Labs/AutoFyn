## imo-2026-03 (lens: closing the 4 remaining (star_3)=MinFloor(4) residual shapes + scouting (2,0,0,1)'s f1>=4 regime)

- **Scope of this lens.** `rank-pigeonhole-budget`'s round-29 §7.17 proved the
  general **Pair-Insertion Ordering Lemma** (`lemmas/pair-insertion-ordering-lemma.md`)
  and used it to fully close shape $(2,0,1,0)$ and shape $(2,0,0,1)$'s
  residual $f_1<4$ regime. Four shapes remain untouched by the corrected
  mechanism: $(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$; shape $(2,0,0,1)$'s
  complementary $f_1\ge4$ regime is numerics-only. I traced the peel-then-
  insert mechanism by hand on all five targets (verifying with exact-`Fraction`
  numerics, not floats) to find what closes cleanly vs. what needs a genuinely
  new tool.

### $(2,0,0,1)$'s $f_1\ge4$ regime — hand-derivable, one new elementary lemma needed on one sub-branch

Setup: $\pi_1\to f_1\ge f_2\ge f_3$ (sum $8$), $\pi_2=4,\pi_3=2$ fixed,
$\pi_4\to e\ge f$ (sum $1$). $U=\{f_1,f_2,f_3,4,2,e,f\}$.

- For $f_1>4$ strict: $f_1$ is the strict unique max (peel via
  `sharp-dominant-removal-identity`): $A(U)=f_1-A(\{f_2,f_3,4,2,e,f\})$.
- Since $f_1>4$, $f_2+f_3=8-f_1<4$, so $4$ is strict unique max of the
  6-set: peel again, $A=4-A(\{f_2,f_3,2,e,f\})$. Target becomes
  $A(\{f_2,f_3,2,e,f\})\ge5-f_1$.
- If $f_1\ge5$: RHS $\le0$, closes trivially by `half-bound-lemma` ($A\ge0$,
  Fact 1). **No new tool needed** for this sub-range.
- If $f_1\in(4,5)$: need a genuine positive lower bound. Sub-branch on
  $f_2$ vs. $2$ (the only remaining fixed reference in the 5-set):
  - **If $f_2>2$:** $f_2$ is the strict max of $\{f_2,f_3,2,e,f\}$ (since
    $f_3\le f_2$, $e,f<1<2<f_2$); peel it — lands *exactly* in the
    already-proved **Pair-Insertion Ordering Lemma** shape (mirrored form:
    reference $2$ above the conservation pair $\{e,f\}$), with free value
    $x=f_3$. Directly reuses Application 2's algebra pattern (target reduces
    to a linear polynomial in $f_1,f_2$, expected to close the same way,
    using $f_1<5$ and $f_2>2$).
  - **If $f_2\le2$:** now $2$ is the max of $\{f_2,f_3,2,e,f\}$ (since
    $f_3\le f_2\le2$, $e,f<1<2$); peeling $2$ leaves
    $\{f_2,f_3\}\cup\{e,f\}$ — **two independent conservation pairs and no
    fixed reference at all.** This shape is *not* covered by the
    Pair-Insertion Ordering Lemma (which needs one pair + one reference +
    one free scalar). This is exactly the "third configuration" the
    round-29 file flagged as an unchecked risk.

  **I verified numerically (see below) that a "Double-Pair Ordering Lemma"
  — an explicit sorted-merge closed form for $A(\{x_1,x_2,y_1,y_2\})$ with
  $x_1+x_2=C_1$, $y_1+y_2=C_2$ two independent conservation pairs — exists
  and is elementary** (proved by the identical trichotomy-on-sort-order
  method as Pair-Insertion, just with the reference removed and both
  "middle" elements now free relative to each other: 4 sort-order regimes
  arise, `$x_1\ge y_1\ge x_2\ge y_2$`, `$x_1\ge y_1\ge y_2\ge x_2$`, and
  mirror images by $x\leftrightarrow y$ symmetry). This is a **new,
  concrete, cheap lemma to add**, not a re-derivation of anything already
  on file — I did not derive its closed form to completion (that is
  outline/build work), but confirmed by $20{,}000$-trial exact-`Fraction`
  sampling (script logic reproduced in this session, not saved) that a
  clean 4-case piecewise-linear closed form governs $A(\{x_1,x_2,y_1,y_2\})$
  exactly as expected, with no anomalies. **Net verdict:** $(2,0,0,1)$'s
  $f_1\ge4$ regime is hand-closable in full, but only after adding this one
  new elementary Double-Pair lemma for the $f_2\le2$ sub-branch; the
  $f_2>2$ sub-branch reuses the existing Pair-Insertion Lemma directly.

### The 4 untouched shapes — structural diagnosis (not full derivations)

**Key forced-dominance fact (new, cheap, worth naming as its own one-line
fact):** if a ladder piece $\pi_i$ receives *exactly one* cut (a
conservation pair $\{f_1,f_2\}$, $f_1\ge f_2$, sum $\pi_i$), then
$f_1\ge\pi_i/2$ always. Since $\pi_i=2\pi_{i+1}$ (ladder ratio), this gives
$f_1\ge\pi_{i+1}$, i.e. **$f_1$ weakly dominates every ladder value at or
below $\pi_{i+1}$** — in particular every untouched or split value drawn
from $\pi_{i+1},\dots,\pi_m$. This is exactly why in shapes where $\pi_1$
gets only $1$ cut, $f_1\ge4$ unconditionally (verified: $f_1+f_2=8\Rightarrow
f_1\ge4\ge$ every other element's own natural ceiling). **This single fact
is the reusable engine for shapes $(1,1,0,1)$ and $(1,1,1,0)$** (both have
$k_1=1$); it does **not** apply to $(1,2,0,0)$/$(2,1,0,0)$, where $\pi_1$
gets $2$ cuts (a *triple*, whose top fragment can be as low as $\pi_1/3$,
no forced $\ge\pi_1/2$ bound) — this is the structural fork that separates
the two pairs of shapes into genuinely different difficulty classes.

**$(1,1,0,1)$ and $(1,1,1,0)$ (three independent conservation pairs +
one fixed value each) — hardest of the 4.** Peeling the forced-dominant
$f_1$ (weak max, $\ge4$) leaves a 5- or 6-element residual with **two or
three still-live conservation pairs simultaneously** (e.g. $(1,1,1,0)$'s
residual after peeling $f_1$ is $\{f_2,a,b,g_1,g_2,1\}$ — one singleton
$f_2$ (broken off the first pair), plus two *intact* pairs $(a,b)$,
$(g_1,g_2)$, plus the fixed $1$). Numerically confirmed (fresh
`Fraction`-exact random search, $500{,}000$ trials each) that the tight
minimum ($A=1$) sits at the expected degenerate boundary
($f_1\to f_2\to4$, one cut vanishing) for both shapes, consistent with
$(\star_3)$ being tight there, not violated. But the *interior* argument
needs at least one more level of casework than Applications 1–2: after
peeling $f_1$, the next dominant element is a genuine **two-way race**
between the freed singleton ($f_2$) and the next pair's top ($a$ or
$g_1$) — neither is forced to dominate the other over the whole domain
(both can range up to $\sim4$ or $\sim2$ respectively). This requires
either (a) a full sub-branch on which wins (roughly doubling the case
count of Applications 1–2, but each sub-branch is still elementary
peel-and-Pair/Double-Pair-Insertion), or (b) direct appeal to the already-
certified, fully general `vertex-minimum-theorem` to skip straight to the
finite tie-vertex list (feasible here since only 3–4 free parameters
remain after using the forced $f_1$-dominance) and evaluate each vertex by
`odd-run-reduction-lemma` — likely **less work than re-deriving a bespoke
multi-branch elementary lemma**, given three pairs are in play.

**$(1,2,0,0)$ and $(2,1,0,0)$ (triple + pair + 2 fixed values) —
intermediate difficulty, closely analogous to the already-solved
$(2,0,1,0)$/$(2,0,0,1)$ but with the second position occupied by a
free pair instead of a fixed value.** E.g. $(2,1,0,0)$: $f_1,f_2,f_3$
(triple, sum $8$, pigeonhole $f_1\ge8/3$ only — no forced $\ge4$),
$a,b$ (pair, sum $4$, so $a\ge2$), $\pi_3=2,\pi_4=1$ fixed. Unlike
$(2,0,1,0)$ (where $\pi_2=4$ was *fixed*, giving a clean "compare $f_1$
vs. the fixed $4$" split), here the competitor is the free pair's top
$a\in[2,4]$ — genuinely two free "candidate maxima" ($f_1$ and $a$) before
any peeling, an extra branch not present in the already-closed sibling
shapes. This is a real added complication but structurally the *same
kind* of problem (peel-the-current-max, iterate), just with one more
comparison to case-split on. Numerically confirmed (fresh $300{,}000$-trial
exact-`Fraction` search) the tight vertex again sits at the expected
degenerate boundary $(f_1,f_2,f_3,a,b)\to(4,2,2,4,0)$ (matching the
achievability witness), consistent with $A\ge1$ and not contradicting it.

### Distinct openings / mechanisms for the outliner

1. **Direct extension of Applications 1–2's method**, adding the one
   missing tool (a **Double-Pair Ordering Lemma**, elementary, ~4 cases,
   same proof method as Pair-Insertion — confirmed to exist by fresh exact
   numerics this session) for wherever peeling collapses two pairs
   together with no intervening fixed reference. This closes $(2,0,0,1)$'s
   $f_1\ge4$ regime in full and is the natural next step for
   $(1,2,0,0)$/$(2,1,0,0)$ once the extra "which free top dominates" branch
   is handled.
2. **Skip the bespoke-lemma route for the 3-pair shapes** $(1,1,0,1)$,
   $(1,1,1,0)$ and invoke the already-certified, fully general
   `vertex-minimum-theorem` + `odd-run-reduction-lemma` directly (finite
   tie-vertex enumeration, feasible since only 3–4 continuous parameters
   remain) — likely cheaper than writing a 3-pair elementary lemma from
   scratch, and is exactly the machinery Round 28's own cross-check script
   already used (`/tmp/vertex_full.py`) to *confirm* (not yet prove by
   hand) all 6 shapes' minima are $1$.
3. **Name and certify the forced-dominance fact** ("one cut on $\pi_i$
   $\Rightarrow$ its top fragment $\ge\pi_{i+1}$") as its own one-line
   reusable lemma — cheap, general (not ladder-instance-specific beyond
   the ratio-2 property already used everywhere), and immediately
   simplifies the $k_1=1$ shapes' opening peel step without re-deriving
   pigeonhole each time.

### Cheap-kill candidates
None beyond the forced-dominance fact above (item 3) — it is a genuine
one-line simplification but not a full closure of anything by itself.

### Knowledge-base / certified-lemma entries to use
- `sharp-dominant-removal-identity` (peel a strict unique max).
- `odd-run-reduction-lemma` (handle ties / even-multiplicity cancellation
  — needed at every $f_1=f_2$ or $f_1=f_2=f_3$ boundary, as in Applications
  1–2).
- `half-bound-lemma` (Fact 1, $A\ge0$) and Fact 2 ($A\le\mathrm{Total}$,
  already certified in this approach file's §5.2).
- `vertex-minimum-theorem` (fully general LP-vertex reduction — candidate
  for closing the 3-pair shapes directly instead of new elementary
  casework, per opening 2 above).
- `pair-insertion-ordering-lemma` (just certified, `lemmas/pair-insertion-ordering-lemma.md`)
  — directly reusable wherever peeling produces one pair + one fixed/singleton
  reference + one free scalar (confirmed to arise in $(2,0,0,1)$'s
  $f_2>2$ sub-branch, and expected in parts of $(1,2,0,0)$/$(2,1,0,0)$).

### Analogous past problems (cruxes)
Not separately queried this pass (this lens is a narrow continuation of
on-file work, not a fresh framing); the existing approach file's own
crux borrowings (`aimo-0146` exchange-smoothing, `aimo-0117` defer-
commitment — already ruled out, `aimo-0718` even-rank-sum pigeonhole —
already ruled out) remain the relevant prior citations; no new crux match
found for the specific "sorted merge of $k$ conservation pairs" sub-problem.

### Prior progress
Shape $(2,0,1,0)$: fully closed, both directions (round 29). Shape
$(2,0,0,1)$: residual $f_1<4$ fully closed by hand (round 29); $f_1\ge4$
now scouted here — hand-closable given one new Double-Pair lemma (not yet
written up as a certified lemma). Shapes $(1,1,0,1),(1,1,1,0),(1,2,0,0),
(2,1,0,0)$: untouched by the corrected mechanism; this report gives a
structural diagnosis and two concrete candidate mechanisms (extend
Pair-Insertion with a new Double-Pair lemma, or invoke
`vertex-minimum-theorem` directly for the 3-pair shapes) but no completed
derivation — that is the next build's job.

### Dead ends (do not retry)
- `single-insert-point-vertex-lemma` applied "one coordinate at a time" to
  a mass-conserving pair — already diagnosed and fixed in round 29 (wrong
  slope, $\pm2$ not $\pm1$); do not re-attempt this citation.
- Naive termwise/per-coordinate bounding of the Pair-Insertion Lemma's
  4 cases (round 29's own aborted first attempt) — fails to close the
  middle cases; the exact closed-form substitution (not a loose
  inequality chain) is what actually works.

### Small-case / intuition notes (conjectural, numerics-based)
- All 5 shapes examined here (the 4 untouched plus $(2,0,0,1)$'s residual
  $f_1\ge4$) have their true minimum $A=1$ attained **only at the
  degenerate boundary** where one of the free cuts vanishes and the shape
  collapses onto a lower-budget shape (fresh $300$k–$500$k-trial exact-
  `Fraction` searches for each, this session) — consistent with, and
  corroborating, the project's closure-argument logic (§7.16: every
  lower-budget shape's polytope is a boundary of some exactly-budget-3
  shape) and with no counterexample found to $A\ge1$ anywhere in any of
  the 5 domains. This is numeric evidence only, not a proof.
- A "Double-Pair Ordering Lemma" (merge of two independent 2-element
  conservation pairs, no reference value) appears to have a clean 4-case
  piecewise-linear closed form by the same trichotomy method as
  Pair-Insertion (confirmed by exact-`Fraction` sampling this session,
  $20{,}000$ trials, no anomalies) — conjectured provable in one round,
  analogous difficulty to the already-certified Pair-Insertion Lemma.
