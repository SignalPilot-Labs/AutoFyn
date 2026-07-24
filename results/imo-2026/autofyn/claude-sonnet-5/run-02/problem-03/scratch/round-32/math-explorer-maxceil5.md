## imo-2026-03 (lens: MaxCeil(m>=5))

### Setup / notation recap (from `rank-pigeonhole-budget`'s §7.9-7.18)
- The whole problem reduces (via `claiming-subgame-reduction`) to proving,
  for every $n$, $c(n)=2^n/(2^{n+1}-1)$ via the combinatorial extremal
  quantity $A(S)=\sum_{\text{odd rank}}L_i$ on multisets. Central open
  obstruction family: $(\star_k)$, $k\ge3$ (unconditionally certified only
  for $k\le2$).
- $\mathrm{MaxCeil}(\ell)$: for a ratio-2 superincreasing tail
  $\sigma=(\sigma_1,\dots,\sigma_\ell)$ and any legal $\le(\ell-2)$-cut
  refinement $S$, claims $A(S)\le\sigma_1-\sigma_\ell$.
- $\mathrm{MinFloor}(\ell)$: dual quantity, $A(S)\ge\sigma_\ell$.
- **Index-Chain Identity (§7.11, certified):** $\mathrm{MinFloor}(\ell)
  \equiv(\star_{\ell-1})$ exactly (biconditional, via rescaling). So
  $(\star_3)=\mathrm{MinFloor}(4)$.
- **Untouched-top reduction (§7.10.4, certified as an "exact reduction," not
  yet a standalone `lemmas/` file):** $\mathrm{MaxCeil}(\ell)$'s
  **top-untouched branch** ($\sigma_1$ left whole) is *exactly equivalent*
  to $\mathrm{MinFloor}(\ell-1)$, via `sharp-dominant-removal-identity`.
- $\mathrm{MaxCeil}(\ell)$'s **top-cut branch** (the harder half, $\sigma_1$
  itself split) further splits into: **$\sigma_2$-untouched** sub-family
  (§7.14, $\sigma_2$-Untouched Closure Theorem, **certified, unconditional
  for every $m\ge2$**) and **$\sigma_2$-touched** residual (open for
  $m\ge5$; §7.15 Necessity Theorem below).
- $\mathrm{MaxCeil}(3),\mathrm{MaxCeil}(4)$ are **fully closed** (both
  branches, round 26, direct 5-shape-style case analysis). $\mathrm{MaxCeil}
  (m\ge5)$ remains open — this is my assigned target.

### Distinct openings

**Opening 1 — a free corollary nobody has banked yet: MaxCeil(5)'s
top-untouched branch is now closed.** By the certified §7.10.4 identity,
$\mathrm{MaxCeil}(\ell)$'s top-untouched branch $\Leftrightarrow
\mathrm{MinFloor}(\ell-1)=(\star_{\ell-2})$. For $\ell=5$ this is
$(\star_3)=\mathrm{MinFloor}(4)$, which round 31 fully closed (all 20
maximal shapes, both directions). **This means half of
$\mathrm{MaxCeil}(5)$ — its top-untouched branch — is already an immediate,
essentially free consequence of round 31's work**, via the same mechanism
that already unlocked $\mathrm{MaxCeil}(\ell)$'s top-untouched branch for
$\ell\le4$ (round 26, when only $(\star_1),(\star_2)$ were certified). As
far as I can tell from `current.md`'s round-31 summary and the approach
file's own "Recommend next round" list, **this specific corollary has not
yet been explicitly stated or written up** — round 31's headline is about
$(\star_3)$ itself, and the recommended next target is phrased generally as
"the general-$n$ $(\star_k)$, $k\ge3$, obstruction," not this concrete,
essentially-mechanical unlock. This is a genuine, cheap, near-immediate win
to formalize first before attacking the harder residual — it needs only
(a) restating §7.10.4's reduction as a standalone certified lemma (it says
it isn't one yet, "since $\mathrm{MinFloor}$ itself is only partially
closed" — that blocker is now gone for $\ell=5$) and (b) instantiating it
at $\ell=5$.

**Opening 2 — the top-cut branch's $\sigma_2$-touched residual, now
partially de-risked by $(\star_3)$.** The genuinely hard remaining piece of
$\mathrm{MaxCeil}(5)$ is the top-cut branch's $\sigma_2$-touched residual
(§7.15's subject). The **Necessity Theorem** proves — via a rigorous
$\varepsilon\to0^+$ continuity argument on the family
$S_\varepsilon=\{\sigma_1-\varepsilon,\varepsilon\}\cup Z\cup\tau$ — that
closing this residual for general $m$ *entails*, as a **necessary** (not
merely sufficient) condition, a restricted instance of $(\star_{m-2})$: the
inequality $A(Z\cup\tau)\ge\sigma_m$ for $Z$ an arbitrary legal
$\le(m-3)$-cut refinement of $\sigma_2$, tail untouched. For $m=5$ this
restricted instance is inside $(\star_3)$'s own case (ii) content — **and
$(\star_3)$ is now fully closed**, so the potential "impossibility"
(Necessity Theorem's contrapositive: if this fails, $\mathrm{MaxCeil}(m)$
fails) can no longer materialize at $m=5$; the necessary condition is
guaranteed satisfied. **This is genuinely good news but not a closure**:
the Necessity Theorem is one-directional (necessity, not sufficiency), and
its own proof shows the "cheap facts" route (two-peel + Fact 2) provably
*cannot* establish (7.15.1) even granting the tail identity — it reduces
to $z_1\ge\sigma_2$, false for any genuine split $z_1$. What actually needs
proving for full $\mathrm{MaxCeil}(5)$ closure is the **general**
$\sigma_2$-touched case (arbitrary $\varepsilon$, not just the $\varepsilon
\to0$ boundary instance identified with $\star_3$'s case (ii)) — i.e. a
genuinely new argument is still needed, but it can now legitimately *use*
$(\star_3)=\mathrm{MinFloor}(4)$'s full closure (all 20 shapes, with their
explicit vertex data) as an available ingredient/base case, rather than
working against an unknown quantity.

**Opening 3 — does the vertex-enumeration technique that closed
$(\star_3)$ transfer?** Yes, structurally, but the search space is larger
and only partially reduced. $(\star_3)=\mathrm{MinFloor}(4)$'s closure used
budget $\le\ell-2=2$ cuts over 4 pieces (35 "$\le2$-cut" compositions
collapsing to 20 maximal shapes via a padding argument), closed via
`vertex-minimum-theorem` + `odd-run-reduction-lemma` +
`sharp-dominant-removal-identity` + `pair-insertion-ordering-lemma` +
Fact 2 (the toolbox that also closed $\mathrm{MaxCeil}(3),(4)$ originally).
$\mathrm{MaxCeil}(5)$'s **remaining** work (top-cut, $\sigma_2$-touched
only, since $\sigma_2$-untouched is already generally closed by §7.14) has
budget $\le m-2=3$ cuts over 5 pieces $(\sigma_1,\dots,\sigma_5)$ with
$\sigma_1$ necessarily cut (top-cut branch) and $\sigma_2$ necessarily
touched — a strictly smaller shape space than "all $\le3$-cut compositions
of 5 pieces" but plausibly still comparable in size to, or larger than,
$(\star_3)$'s 20-shape census (more pieces, same-order budget). The same
toolbox should transfer mechanically shape-by-shape, **and now has
$(\star_3)$ itself available as a certified fact for any shape that reduces
one level down to a length-4 ratio-2 tail** (exactly as §7.14/§7.15 already
do). This is the natural, concrete next build target: enumerate the
$\sigma_2$-touched shapes of $\mathrm{MaxCeil}(5)$ (budget 3, 5 pieces,
$\sigma_1$ cut, $\sigma_2$ touched) the same way MinFloor(4)'s were
enumerated, using $(\star_3)$ as an input wherever a shape reduces to it.

### Overlap with `greedy-halving-adversary`'s $h(m)$ — precise, not to be
duplicated
`greedy-halving-adversary`'s round-31 work on $h(m)$'s "simultaneous
$q_1$-cut and tail-refinement" piece identified its **vertex $c=x$** as a
proven **term-for-term identity** with $\mathrm{MaxCeil}(m)$ (not an
analogy) — closed for $m\le4$ by direct citation, **open for $m\ge5$
exactly because $\mathrm{MaxCeil}(m\ge5)$ is open**. So this literal
sub-target is the *same object* as my lens's target; closing
$\mathrm{MaxCeil}(5)$ directly closes $h(5)$'s $c=x$ vertex, no extra work
needed, and vice versa — the two fronts should **not** duplicate this
piece.

However, `greedy-halving-adversary` also separately opened a **genuinely
different, harder object** it calls "punctured $\mathrm{MaxCeil}$," arising
from a *different* vertex ($c=t\in S''$, the "$q_2$ untouched, $t\ne q_2$"
sub-case). This is **not** the same as standard $\mathrm{MaxCeil}(m-1)$: it
requires an upper bound on $A(S''\setminus\{t,q_2\})$ where one rung's
fragments sum to *strictly less than* that rung's full value (a genuine
puncture — the object is not a legal refinement of any clean ratio-2 tail
at any rescaling, so neither the $(\star_k)$ family nor
`single-rung-removal-closed-form` apply directly). This is honestly
reported as untouched, no lemma addresses it. **Do not conflate this with
$\mathrm{MaxCeil}(m\ge5)$ itself** — it is a distinct, harder, still
entirely open object that happens to sit one step further along the same
inductive chain. A future round attacking it should treat it as its own
target (perhaps: does the vertex-enumeration/peel toolbox extend to
punctured tails at all? — genuinely unclear, worth a dedicated
reconnaissance pass, not assumed to transfer).

### Candidate technique(s)
- Direct transfer of the shape-enumeration/vertex-minimization toolbox
  (`vertex-minimum-theorem`, `odd-run-reduction-lemma`,
  `sharp-dominant-removal-identity`, `pair-insertion-ordering-lemma`, Fact 2
  / $A\le\mathrm{Total}$) to $\mathrm{MaxCeil}(5)$'s residual $\sigma_2$-
  touched shapes, now with $(\star_3)$ as an available discharge for
  one-level-down reductions.
- The already-certified §7.10.4 untouched-top reduction, instantiated at
  $\ell=5$, for the cheap Opening-1 win.
- For the "punctured MaxCeil" object: no existing technique is known to
  apply; would need a genuinely new peel/identity adapted to a
  non-full-mass rung (possibly an extension of
  `sharp-dominant-removal-identity`'s hypothesis, or a fresh case split on
  how far short of full mass the punctured rung falls).

### Cheap-kill candidates
- Opening 1 (MaxCeil(5) top-untouched branch = free corollary of
  $(\star_3)$'s closure) — essentially a two-line write-up, should be
  banked before anything else; costs almost nothing and immediately halves
  the open scope of $\mathrm{MaxCeil}(5)$.
- Sanity-check the Necessity Theorem's numeric corroboration at $m=5$
  (already done in the file: 2000-trial search, min of $A(Z\cup\tau)$ over
  $\le2$-cut splits of $\sigma_2$ found exactly $=\sigma_5$) — worth an
  independent re-verification before building on it, per the reviewer's
  own standard practice, but it is *evidence*, not the target itself
  (§7.15 is a Necessity theorem, not a sufficiency proof).

### Knowledge-base entries to use
Nothing new beyond what the population already invokes; the load-bearing
tools are internal certified lemmas (`vertex-minimum-theorem`,
`odd-run-reduction-lemma`, `sharp-dominant-removal-identity`,
`pair-insertion-ordering-lemma`, `sigma2-untouched-closure-theorem`,
`minfloor-4-full-closure`), not generic `knowledge_base.md` entries — this
project is almost entirely running on its own from-scratch machinery at
this depth. From `knowledge_base.md`, the general "Extremal/optimization
via convex polytope vertices, LP duality" entries under General Proof
Methods remain the closest generic match to `vertex-minimum-theorem`'s own
technique, but the population has already fully internalized and extended
this beyond what the KB entry states generically.

### Analogous past problems (cruxes)
Given the extreme specificity and depth of this project's own internal
machinery (30+ rounds of bespoke lemmas), I did not find a crux-corpus
problem that meaningfully resembles the *current* residual (a
continuity/limiting Necessity argument coupled to a finite vertex
enumeration on ratio-2 superincreasing sequences under a cut budget). This
is consistent with prior rounds' explorer reports (not re-derived here to
avoid duplicating effort) — recommend not spending further budget
re-searching the corpus for this specific residual unless the outliner
flags a new sub-target where a generic combinatorial-optimization crux
might apply (e.g. if the "punctured MaxCeil" object turns out to reduce to
a cleaner discrete extremal statement).

### Prior progress
- $(\star_3)=\mathrm{MinFloor}(4)$: **fully closed**, all 20 maximal
  shapes, both directions (round 31), building on round 26's Index-Chain
  Identity and rounds 28-31's shape-by-shape closure.
- $\mathrm{MaxCeil}(3),\mathrm{MaxCeil}(4)$: fully closed, both branches
  (round 26).
- $\mathrm{MaxCeil}(\ell)$'s $\sigma_2$-untouched sub-family: closed for
  every $m\ge2$ (§7.14, round 27).
- $\mathrm{MaxCeil}(m\ge5)$: **open**, but (per Opening 1 above) its
  top-untouched branch is now an unclaimed free corollary of $(\star_3)$'s
  closure; its top-cut/$\sigma_2$-touched residual is de-risked (necessary
  condition now satisfiable) but not closed (§7.15 Necessity Theorem,
  round 27).

### Dead ends (do not retry)
- The "cheap two-peel + Fact 2" route to close (7.15.1)/the $\sigma_2$-
  touched residual directly: §7.15 proves this algebraically reduces to
  $z_1\ge\sigma_2$, which is false for any genuine split — this specific
  mechanical route provably cannot work, for any $Z$, at any $m$. Any new
  attempt on $\mathrm{MaxCeil}(m\ge5)$'s $\sigma_2$-touched residual needs a
  different mechanism than the peel-and-Fact-2 toolbox that closed
  $\sigma_2$-untouched and $\mathrm{MaxCeil}(3)/(4)$.
- Triangle-Bound / Max-Domination shortcut for $\mathrm{MaxCeil}(4)$'s
  shape census: already flagged (round 26) as insufficient; presumably
  also insufficient for $\mathrm{MaxCeil}(5)$'s larger shape space — avoid
  re-attempting it as a shortcut here.
- Assuming the round-27 outline's premise that the $\sigma_2$-touched
  residual is "self-contained" (independent of $(\star_k)$): explicitly
  refuted by the Necessity Theorem for $m\ge5$.

### Small-case / intuition notes
- Numeric corroboration (2000 trials, $m=5$, per §7.15) of (7.15.1) at
  $m=5$: minimum of $A(Z\cup\tau)$ over random $\le2$-cut splits of
  $\sigma_2$ found exactly $=\sigma_5$ — **conjectural** support (not
  proof) that the $\sigma_2$-touched residual's true extremal value at
  $m=5$ matches the target exactly, consistent with $(\star_3)$'s now-
  proven truth but not itself a proof of the general (non-$\varepsilon\to0$)
  case.
- The shape-count growth pattern (round 28's explorer flagged
  $28\%\to64\%$ density growth between $n=3$ and $n=4$ for a related
  chamber-coverage problem elsewhere in the file) suggests the
  $\mathrm{MaxCeil}(5)$ $\sigma_2$-touched shape enumeration is likely to be
  meaningfully larger than $\mathrm{MaxCeil}(4)$'s 5-shape census — budget
  accordingly; this is an intuition/scaling signal, not a hard count (I did
  not enumerate the exact shape count myself in this pass).

### Recommendation
1. **Immediate, cheap:** write up Opening 1 explicitly — $\mathrm{MaxCeil}
   (5)$'s top-untouched branch is closed via §7.10.4's identity plus
   $(\star_3)$'s round-31 closure. Promote §7.10.4's "exact reduction" to a
   standalone certified lemma now that its dependency ($\mathrm{MinFloor}$)
   is no longer only partially closed at the relevant index.
2. **Main target:** attack $\mathrm{MaxCeil}(5)$'s top-cut,
   $\sigma_2$-touched residual via the same vertex-enumeration toolbox that
   closed $(\star_3)$, now explicitly using $(\star_3)$'s certified 20-shape
   result as an available ingredient (not just as a necessary condition per
   §7.15, but as a positive tool for any sub-case that reduces to a
   length-4 tail one level down).
3. **Coordinate, don't duplicate:** the sibling `greedy-halving-adversary`'s
   $c=x$ vertex of $h(5)$ is literally the same target — one closure closes
   both. Its separate "punctured $\mathrm{MaxCeil}$" object ($c=t\in S''$,
   "$q_2$ untouched, $t\ne q_2$") is a genuinely different, harder,
   completely untouched object — flag it as a distinct future target, not
   folded into this round's $\mathrm{MaxCeil}(5)$ push.
